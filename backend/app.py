"""
LLM-Wiki RAG Backend

OpenAI-compatible FastAPI server that retrieves grounded context from a
compiled Markdown wiki (Wiki/ + retrieval/) and answers via LiteLLM, so any
provider (OpenAI / Anthropic / Gemini / Ollama / etc.) works with the same code.

Endpoints:
    GET  /                       basic info
    GET  /health                 readiness + corpus stats
    GET  /v1/models              OpenAI-style model list
    POST /chat                   simple {message, top_k} -> {answer, sources}
    POST /v1/chat/completions    OpenAI-compatible chat (streaming + non-stream)
    POST /admin/reload           rebuild the in-memory corpus + index

Env vars:
    LLM_WIKI_ROOT       path to the wiki repo root (default: .)
    MODEL_NAME          LiteLLM model string (e.g. "gpt-4.1-mini",
                        "anthropic/claude-sonnet-4-5", "gemini/gemini-1.5-pro",
                        "ollama/llama3.1")
    OPENAI_API_KEY      provider keys are read from env by LiteLLM directly
    ANTHROPIC_API_KEY   ...
    GEMINI_API_KEY      ...
    API_HOST / API_PORT bind address (used only by __main__)
    CORS_ORIGINS        comma-separated list, default "*"
"""

from __future__ import annotations

import json
import logging
import math
import os
import re
import time
import uuid
from collections import Counter
from pathlib import Path
from threading import RLock
from typing import Any, Dict, Iterable, List, Optional, Union

import litellm
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

load_dotenv()

for secret_name in (
    "OPENAI_API_KEY",
    "ANTHROPIC_API_KEY",
    "GEMINI_API_KEY",
    "GOOGLE_API_KEY",
):
    if os.getenv(secret_name):
        os.environ[secret_name] = os.environ[secret_name].strip()

LLM_WIKI_ROOT = Path(os.getenv("LLM_WIKI_ROOT", ".")).resolve()
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", "0.2"))
DEFAULT_TOP_K = int(os.getenv("DEFAULT_TOP_K", "6"))
MAX_CHUNK_CHARS = int(os.getenv("MAX_CHUNK_CHARS", "2500"))
CORS_ORIGINS = [o.strip() for o in os.getenv("CORS_ORIGINS", "*").split(",") if o.strip()]

# Quiet LiteLLM's chatty defaults; let users opt back in via env if they want.
litellm.drop_params = True  # silently drop unsupported params per provider
litellm.suppress_debug_info = True

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s %(levelname)s %(name)s | %(message)s",
)
log = logging.getLogger("llm-wiki")

# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class Message(BaseModel):
    role: str
    content: Union[str, List[Dict[str, Any]], None] = ""


class ChatCompletionRequest(BaseModel):
    model: Optional[str] = "llm-wiki"
    messages: List[Message]
    temperature: Optional[float] = None
    top_k: Optional[int] = Field(default=None, ge=1, le=20)
    stream: Optional[bool] = False
    max_tokens: Optional[int] = None


class SimpleChatRequest(BaseModel):
    message: str
    top_k: Optional[int] = Field(default=DEFAULT_TOP_K, ge=1, le=20)
    model: Optional[str] = None
    temperature: Optional[float] = None


class Source(BaseModel):
    title: str
    path: str
    layer: str
    score: float


# ---------------------------------------------------------------------------
# Corpus + retrieval (cached in memory; rebuilt on /admin/reload)
# ---------------------------------------------------------------------------

STOPWORDS = {
    "the", "a", "an", "and", "or", "to", "of", "in", "on", "for", "with",
    "is", "are", "was", "were", "be", "by", "as", "from", "this", "that",
    "what", "how", "why", "when", "where", "explain", "describe", "tell",
    "me", "about", "into", "using", "use", "do", "does", "did", "it", "its",
    "you", "your", "i", "we", "they", "them", "can", "should", "would",
}

LAYER_BOOST = {
    "wiki_chunk":   1.30,  # compiled wiki notes — preferred
    "wiki_catalog": 1.15,  # metadata
    "raw_chunk":    0.85,  # raw transcript — evidence only
}

_TOKEN_RE = re.compile(r"[a-zA-Z0-9_]+")


def tokenize(text: str) -> List[str]:
    return [
        w for w in (m.group(0).lower() for m in _TOKEN_RE.finditer(text or ""))
        if len(w) > 2 and w not in STOPWORDS
    ]


def _read_jsonl(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    out: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return out


def _normalize(obj: Dict[str, Any], layer: str) -> Dict[str, str]:
    path = str(
        obj.get("path") or obj.get("file") or obj.get("source")
        or obj.get("source_path") or ""
    )
    title = str(obj.get("title") or obj.get("name") or Path(path).stem or "Untitled")
    text = str(
        obj.get("text") or obj.get("content") or obj.get("chunk")
        or obj.get("body") or obj.get("summary") or ""
    )
    if not text:
        # fall back to a flat dump of the record so nothing is silently lost
        text = " ".join(
            str(v) for v in obj.values()
            if isinstance(v, (str, int, float))
        )
    return {"layer": layer, "path": path, "title": title, "text": text}


class Corpus:
    """In-memory wiki corpus with a small BM25 index."""

    # BM25 hyperparameters
    K1 = 1.5
    B = 0.75

    def __init__(self, root: Path) -> None:
        self.root = root
        self._lock = RLock()
        self.docs: List[Dict[str, str]] = []
        self.doc_tokens: List[List[str]] = []
        self.doc_lens: List[int] = []
        self.df: Counter = Counter()
        self.avgdl: float = 0.0
        self.idf: Dict[str, float] = {}
        self.loaded_at: float = 0.0
        self.sources: Dict[str, Path] = {
            "wiki_chunk":   root / "retrieval" / "wiki_chunks.jsonl",
            "wiki_catalog": root / "Wiki" / "catalog.jsonl",
            "raw_chunk":    root / "retrieval" / "raw_chunks.jsonl",
        }

    def load(self) -> None:
        with self._lock:
            docs: List[Dict[str, str]] = []
            for layer, path in self.sources.items():
                rows = _read_jsonl(path)
                log.info("loaded %d rows from %s (%s)", len(rows), path, layer)
                for obj in rows:
                    docs.append(_normalize(obj, layer))

            doc_tokens = [tokenize(f"{d['title']} {d['text']}") for d in docs]
            doc_lens = [len(t) for t in doc_tokens]
            avgdl = (sum(doc_lens) / len(doc_lens)) if doc_lens else 0.0

            df: Counter = Counter()
            for toks in doc_tokens:
                for term in set(toks):
                    df[term] += 1

            n_docs = len(docs)
            idf = {
                term: math.log(1 + (n_docs - cnt + 0.5) / (cnt + 0.5))
                for term, cnt in df.items()
            }

            self.docs = docs
            self.doc_tokens = doc_tokens
            self.doc_lens = doc_lens
            self.df = df
            self.avgdl = avgdl
            self.idf = idf
            self.loaded_at = time.time()
            log.info(
                "corpus ready: %d docs, avgdl=%.1f, vocab=%d",
                n_docs, avgdl, len(idf),
            )

    def stats(self) -> Dict[str, Any]:
        return {
            "doc_count": len(self.docs),
            "vocab": len(self.idf),
            "avgdl": round(self.avgdl, 2),
            "loaded_at": self.loaded_at,
            "sources": {
                layer: {"path": str(p), "exists": p.exists()}
                for layer, p in self.sources.items()
            },
        }

    def search(self, query: str, top_k: int) -> List[Dict[str, Any]]:
        if not self.docs:
            return []

        q_terms = tokenize(query)
        if not q_terms:
            return []
        q_counts = Counter(q_terms)

        scored: List[tuple] = []
        for i, tokens in enumerate(self.doc_tokens):
            if not tokens:
                continue
            tf_counts = Counter(tokens)
            dl = self.doc_lens[i] or 1
            score = 0.0
            for term, qf in q_counts.items():
                tf = tf_counts.get(term, 0)
                if not tf:
                    continue
                idf = self.idf.get(term, 0.0)
                denom = tf + self.K1 * (1 - self.B + self.B * (dl / (self.avgdl or 1)))
                score += idf * ((tf * (self.K1 + 1)) / denom) * qf

            if score <= 0:
                continue

            doc = self.docs[i]
            # title hit bonus: large reward when query terms appear in the title
            title_toks = set(tokenize(doc["title"]))
            score += 2.0 * sum(1 for t in q_terms if t in title_toks)
            # layer preference
            score *= LAYER_BOOST.get(doc["layer"], 1.0)

            scored.append((score, doc))

        scored.sort(key=lambda x: x[0], reverse=True)
        results: List[Dict[str, Any]] = []
        for score, doc in scored[:top_k]:
            results.append({**doc, "score": round(float(score), 4)})
        return results


corpus = Corpus(LLM_WIKI_ROOT)
corpus.load()

# ---------------------------------------------------------------------------
# Prompt assembly
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are the LLM-Wiki study assistant for Machine Learning for Computational Biology (MLCB).

Rules:
- Answer using the retrieved LLM-Wiki context below. Prefer compiled Wiki notes (wiki_chunk / wiki_catalog) over raw transcripts (raw_chunk).
- Cite sources inline by their file path, e.g. (Wiki/Concepts/bayesian-inference.md). Multiple sources are fine.
- If the context does not support a claim, say so clearly and name what is missing — do not invent facts.
- Keep answers structured (short intro, then bullets or sections), beginner-friendly when biology terms come up.
"""


def _format_context(chunks: List[Dict[str, Any]]) -> str:
    blocks: List[str] = []
    for i, c in enumerate(chunks, start=1):
        text = (c.get("text") or "").strip()
        if len(text) > MAX_CHUNK_CHARS:
            text = text[:MAX_CHUNK_CHARS] + "\n…[truncated]"
        blocks.append(
            f"[SOURCE {i}] layer={c['layer']} score={c.get('score', 0)}\n"
            f"Title: {c['title']}\n"
            f"Path:  {c['path']}\n"
            f"---\n{text}"
        )
    return "\n\n".join(blocks) if blocks else "(no relevant context found)"


def _log_chat_request(
    endpoint: str,
    question: str,
    top_k: int,
    chunks: List[Dict[str, Any]],
) -> None:
    payload = {
        "event": "chat_request",
        "endpoint": endpoint,
        "question": question[:500],
        "top_k": top_k,
        "source_count": len(chunks),
        "sources": [
            {"path": c.get("path"), "layer": c.get("layer"), "score": c.get("score")}
            for c in chunks[:5]
        ],
    }
    log.info(json.dumps(payload, ensure_ascii=False))


def _extract_user_question(messages: List[Message]) -> str:
    for msg in reversed(messages):
        if msg.role != "user":
            continue
        content = msg.content
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            parts: List[str] = []
            for item in content:
                if isinstance(item, dict):
                    text = item.get("text")
                    if text:
                        parts.append(str(text))
            return "\n".join(parts)
    return ""


def _build_llm_messages(question: str, context: str) -> List[Dict[str, str]]:
    user = (
        f"Question:\n{question}\n\n"
        f"Retrieved LLM-Wiki context:\n{context}"
    )
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user},
    ]


# ---------------------------------------------------------------------------
# LiteLLM helpers (with friendly errors)
# ---------------------------------------------------------------------------


def _call_llm(
    messages: List[Dict[str, str]],
    model: str,
    temperature: float,
    stream: bool,
    max_tokens: Optional[int] = None,
) -> Any:
    try:
        return litellm.completion(
            model=model,
            messages=messages,
            temperature=temperature,
            stream=stream,
            max_tokens=max_tokens,
        )
    except litellm.AuthenticationError as e:  # type: ignore[attr-defined]
        raise HTTPException(status_code=401, detail=f"LLM auth failed: {e}") from e
    except litellm.RateLimitError as e:       # type: ignore[attr-defined]
        raise HTTPException(status_code=429, detail=f"LLM rate limit: {e}") from e
    except litellm.BadRequestError as e:      # type: ignore[attr-defined]
        raise HTTPException(status_code=400, detail=f"LLM bad request: {e}") from e
    except litellm.APIConnectionError as e:   # type: ignore[attr-defined]
        raise HTTPException(status_code=502, detail=f"LLM connection error: {e}") from e
    except Exception as e:                    # last resort
        log.exception("LLM call failed")
        raise HTTPException(status_code=500, detail=f"LLM error: {e}") from e


def _openai_envelope(answer: str, model: str) -> Dict[str, Any]:
    return {
        "id": f"chatcmpl-{uuid.uuid4().hex}",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": model,
        "choices": [{
            "index": 0,
            "message": {"role": "assistant", "content": answer},
            "finish_reason": "stop",
        }],
        "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
    }


def _sse_chunk(model: str, delta: Dict[str, Any], stream_id: str, finish: Optional[str] = None) -> str:
    payload = {
        "id": stream_id,
        "object": "chat.completion.chunk",
        "created": int(time.time()),
        "model": model,
        "choices": [{"index": 0, "delta": delta, "finish_reason": finish}],
    }
    return f"data: {json.dumps(payload)}\n\n"


def _stream_delta_text(event: Any) -> str:
    """LiteLLM yields OpenAI-shaped chunks; pull `.choices[0].delta.content` safely."""
    try:
        choices = getattr(event, "choices", None) or event.get("choices")  # type: ignore[union-attr]
        if not choices:
            return ""
        delta = getattr(choices[0], "delta", None) or choices[0].get("delta")
        if not delta:
            return ""
        content = getattr(delta, "content", None)
        if content is None and isinstance(delta, dict):
            content = delta.get("content")
        return content or ""
    except Exception:
        return ""


# ---------------------------------------------------------------------------
# FastAPI app
# ---------------------------------------------------------------------------

app = FastAPI(title="LLM-Wiki RAG API", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> Dict[str, Any]:
    return {
        "status": "running",
        "service": "LLM-Wiki RAG API",
        "model": MODEL_NAME,
        "wiki_root": str(LLM_WIKI_ROOT),
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health() -> Dict[str, Any]:
    return {
        "status": "ok",
        "model": MODEL_NAME,
        "wiki_root": str(LLM_WIKI_ROOT),
        "corpus": corpus.stats(),
    }


@app.get("/v1/models")
def models() -> Dict[str, Any]:
    return {
        "object": "list",
        "data": [{
            "id": "llm-wiki",
            "object": "model",
            "created": int(time.time()),
            "owned_by": "local",
            "backing_model": MODEL_NAME,
        }],
    }


@app.post("/admin/reload")
def reload_corpus() -> Dict[str, Any]:
    corpus.load()
    return {"status": "reloaded", "corpus": corpus.stats()}


@app.post("/chat")
def simple_chat(req: SimpleChatRequest) -> Dict[str, Any]:
    top_k = req.top_k or DEFAULT_TOP_K
    chunks = corpus.search(req.message, top_k)
    _log_chat_request("/chat", req.message, top_k, chunks)
    if not chunks:
        raise HTTPException(
            status_code=404,
            detail="No relevant LLM-Wiki context found. Try POST /admin/reload after rebuilding retrieval files.",
        )

    messages = _build_llm_messages(req.message, _format_context(chunks))
    completion = _call_llm(
        messages=messages,
        model=req.model or MODEL_NAME,
        temperature=req.temperature if req.temperature is not None else DEFAULT_TEMPERATURE,
        stream=False,
    )
    answer = completion.choices[0].message.content or ""
    return {
        "answer": answer,
        "sources": [
            Source(
                title=c["title"], path=c["path"],
                layer=c["layer"], score=c.get("score", 0.0),
            ).model_dump()
            for c in chunks
        ],
    }


@app.post("/v1/chat/completions")
def chat_completions(req: ChatCompletionRequest):
    question = _extract_user_question(req.messages)
    if not question.strip():
        raise HTTPException(status_code=400, detail="No user message found.")

    top_k = req.top_k or DEFAULT_TOP_K
    chunks = corpus.search(question, top_k)
    _log_chat_request("/v1/chat/completions", question, top_k, chunks)
    context = _format_context(chunks) if chunks else "(no relevant context found)"
    messages = _build_llm_messages(question, context)

    output_model = req.model or "llm-wiki"
    temperature = req.temperature if req.temperature is not None else DEFAULT_TEMPERATURE

    if req.stream:
        stream = _call_llm(
            messages=messages,
            model=MODEL_NAME,
            temperature=temperature,
            stream=True,
            max_tokens=req.max_tokens,
        )
        stream_id = f"chatcmpl-{uuid.uuid4().hex}"

        def event_stream() -> Iterable[str]:
            # First chunk advertises the role (OpenAI clients expect this).
            yield _sse_chunk(output_model, {"role": "assistant"}, stream_id)
            try:
                for event in stream:
                    delta = _stream_delta_text(event)
                    if delta:
                        yield _sse_chunk(output_model, {"content": delta}, stream_id)
            except Exception as e:           # pragma: no cover
                log.exception("stream failed")
                yield _sse_chunk(output_model, {"content": f"\n\n[stream error: {e}]"}, stream_id)
            yield _sse_chunk(output_model, {}, stream_id, finish="stop")
            yield "data: [DONE]\n\n"

        return StreamingResponse(event_stream(), media_type="text/event-stream")

    completion = _call_llm(
        messages=messages,
        model=MODEL_NAME,
        temperature=temperature,
        stream=False,
        max_tokens=req.max_tokens,
    )
    answer = completion.choices[0].message.content or ""
    envelope = _openai_envelope(answer, output_model)
    # Non-standard but useful: include source list so UIs can show citations.
    envelope["llm_wiki_sources"] = [
        {"title": c["title"], "path": c["path"], "layer": c["layer"], "score": c.get("score", 0.0)}
        for c in chunks
    ]
    return envelope


# ---------------------------------------------------------------------------
# CLI entry (uv run python app.py also works)
# ---------------------------------------------------------------------------

if __name__ == "__main__":          # pragma: no cover
    import uvicorn
    uvicorn.run(
        "app:app",
        host=os.getenv("API_HOST", "0.0.0.0"),
        port=int(os.getenv("API_PORT", os.getenv("PORT", "8000"))),
        reload=bool(os.getenv("RELOAD", "")),
    )
