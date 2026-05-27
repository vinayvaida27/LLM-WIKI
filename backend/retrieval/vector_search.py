"""
Vector Search: semantic similarity over raw_chunks using OpenAI text-embedding-3-large.

Only raw_chunks are indexed — they are the primary source of truth (direct lecture
content).  wiki_chunk / wiki_catalog entries are intentionally excluded because
they are synthesized summaries, not ground-truth evidence.

Lifecycle
---------
1. On startup, VectorSearch.load_or_build() is called.
   - If a valid cache file exists, embeddings are loaded from disk (~12 MB).
   - Otherwise, the full raw_chunk corpus is embedded via OpenAI and cached.
2. Per query, search(query, top_k) returns cosine-ranked raw_chunks with a
   ``vector_score`` field (0–1).

Environment variables
---------------------
ENABLE_VECTOR_SEARCH   Set to "true" to activate (default: off)
VECTOR_EMBED_MODEL     Override the embedding model (default: text-embedding-3-large)
VECTOR_CACHE_PATH      Override the cache file path
"""

from __future__ import annotations

import logging
import os
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

log = logging.getLogger("llm-wiki.vector")

# ── optional numpy import ─────────────────────────────────────────────────────
try:
    import numpy as np
    _HAS_NUMPY = True
except ImportError:
    _HAS_NUMPY = False
    log.warning("numpy not installed — VectorSearch will be disabled")

import litellm

# ── constants ─────────────────────────────────────────────────────────────────
DEFAULT_EMBED_MODEL     = "text-embedding-3-large"
DEFAULT_EMBED_DIM       = 3072          # text-embedding-3-large output dimensions
_BATCH_SIZE             = 100           # max inputs per embedding API call
_MIN_COSINE_SIMILARITY  = 0.25          # discard very weak semantic matches


class VectorSearch:
    """
    Semantic search over raw_chunks using OpenAI text-embedding-3-large.

    Parameters
    ----------
    raw_chunks:   list of normalised raw_chunk dicts (layer == 'raw_chunk')
    cache_path:   path to the .npz embedding cache file
    model:        LiteLLM-compatible embedding model string
    """

    def __init__(
        self,
        raw_chunks: List[Dict[str, Any]],
        cache_path: Path,
        model: str = DEFAULT_EMBED_MODEL,
    ) -> None:
        self._chunks: List[Dict[str, Any]] = raw_chunks
        self._cache: Path = cache_path
        self._model: str = model
        self._embeddings: Optional["np.ndarray"] = None   # shape (n_chunks, dim)
        self._norms: Optional["np.ndarray"] = None        # shape (n_chunks,)
        self.enabled: bool = False

    # ── public API ────────────────────────────────────────────────────────────

    def load_or_build(self) -> None:
        """Load embeddings from cache, or build and cache them if missing."""
        if not _HAS_NUMPY:
            log.warning("numpy unavailable — VectorSearch disabled")
            return
        if not self._chunks:
            log.warning("No raw_chunks provided — VectorSearch disabled")
            return
        if not os.getenv("OPENAI_API_KEY") and not os.getenv("LITELLM_API_KEY"):
            log.warning("No OpenAI key found — VectorSearch disabled")
            return

        if self._try_load_cache():
            return

        log.info(
            "Building embedding index: %d raw_chunks × model=%s …",
            len(self._chunks), self._model,
        )
        self._build_and_cache()

    def search(self, query: str, top_k: int = 10) -> List[Dict[str, Any]]:
        """
        Return up to top_k raw_chunks sorted by cosine similarity to the query.
        Each result has a ``vector_score`` field (float, 0–1).
        Returns [] when disabled or on error.
        """
        if not self.enabled or self._embeddings is None:
            return []

        try:
            resp = litellm.embedding(model=self._model, input=[query])
            q_vec = np.array(resp.data[0].embedding, dtype=np.float32)
        except Exception as e:
            log.warning("Vector query embedding failed: %s", e)
            return []

        q_norm = float(np.linalg.norm(q_vec))
        if q_norm == 0:
            return []

        scores = (self._embeddings @ q_vec) / (self._norms * q_norm + 1e-9)
        top_idx = int(np.argsort(scores)[::-1][0])  # get top index first for bounds check

        top_indices = np.argsort(scores)[::-1][:top_k]
        results: List[Dict[str, Any]] = []
        for idx in top_indices:
            sim = float(scores[idx])
            if sim < _MIN_COSINE_SIMILARITY:
                break
            chunk = dict(self._chunks[int(idx)])
            chunk["vector_score"] = round(sim, 4)
            results.append(chunk)

        return results

    # ── private helpers ───────────────────────────────────────────────────────

    def _try_load_cache(self) -> bool:
        """Attempt to load cached embeddings. Return True on success."""
        if not self._cache.exists():
            return False
        try:
            data = np.load(str(self._cache))
            emb = data["embeddings"]
            if emb.shape[0] != len(self._chunks):
                log.warning(
                    "Cache size mismatch (%d vs %d chunks) — rebuilding",
                    emb.shape[0], len(self._chunks),
                )
                return False
            self._embeddings = emb.astype(np.float32)
            self._norms = np.linalg.norm(self._embeddings, axis=1)
            self.enabled = True
            log.info(
                "Vector index loaded from cache: %d vectors, dim=%d, model=%s",
                emb.shape[0], emb.shape[1], self._model,
            )
            return True
        except Exception as e:
            log.warning("Failed to load embedding cache: %s — rebuilding", e)
            return False

    def _build_and_cache(self) -> None:
        """Embed all raw_chunks, cache to disk, and enable search."""
        t0 = time.perf_counter()

        # Build rich text representation for each chunk
        texts = [
            _chunk_text(c) for c in self._chunks
        ]

        all_vecs: List[List[float]] = []
        n = len(texts)
        for i in range(0, n, _BATCH_SIZE):
            batch = texts[i: i + _BATCH_SIZE]
            try:
                resp = litellm.embedding(model=self._model, input=batch)
                all_vecs.extend(item.embedding for item in resp.data)
            except Exception as e:
                log.error("Embedding batch %d–%d failed: %s", i, i + len(batch), e)
                raise

            pct = min(100, int((i + len(batch)) / n * 100))
            log.info("Embedding progress: %d%% (%d/%d)", pct, i + len(batch), n)

        self._embeddings = np.array(all_vecs, dtype=np.float32)
        self._norms = np.linalg.norm(self._embeddings, axis=1)

        self._cache.parent.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(str(self._cache), embeddings=self._embeddings)

        elapsed = time.perf_counter() - t0
        self.enabled = True
        log.info(
            "Vector index built in %.1fs: %d vectors, dim=%d, cached at %s",
            elapsed, self._embeddings.shape[0], self._embeddings.shape[1], self._cache,
        )


# ── helpers ───────────────────────────────────────────────────────────────────

def _chunk_text(c: Dict[str, Any]) -> str:
    """
    Build a rich text string for embedding a raw_chunk.

    Includes title, heading path, and text body (first 1000 chars).
    The heading path adds structural context without ballooning token count.
    """
    parts: List[str] = []

    title = (c.get("title") or "").strip()
    if title:
        parts.append(title)

    heading = c.get("heading_path")
    if isinstance(heading, list) and heading:
        heading_str = " > ".join(str(h) for h in heading if h)
        if heading_str and heading_str != title:
            parts.append(heading_str)

    text = (c.get("text") or "").strip()
    if text:
        parts.append(text[:1000])

    return "\n".join(parts)
