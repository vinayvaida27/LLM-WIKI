"""
Query Enhancement: HyDE + multi-query expansion.

HyDE (Hypothetical Document Embeddings — Gao et al. 2022)
----------------------------------------------------------
Instead of embedding a short question for vector search, the LLM first
generates a hypothetical answer paragraph.  That paragraph lies in the same
embedding space as the corpus documents, so cosine similarity is dramatically
sharper than query ↔ document comparison.

Query Expansion
---------------
Two alternative phrasings of the question are generated.  BM25 is run on all
variants (original + alternatives + HyDE doc) in parallel and results are
merged by max-score before the reranker sees them.  This recovers documents
that use different vocabulary than the user's exact words.

Parallelism
-----------
When both techniques are enabled the two LLM calls run concurrently inside a
ThreadPoolExecutor so total added latency is ~max(t_hyde, t_expansion) rather
than the sum.

Environment variables
---------------------
ENABLE_HYDE             set to "true" to activate HyDE
ENABLE_QUERY_EXPANSION  set to "true" to activate multi-query expansion
"""

from __future__ import annotations

import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from typing import List, Optional

import litellm

log = logging.getLogger("llm-wiki.enhancer")

# ── LLM prompts ───────────────────────────────────────────────────────────────

_HYDE_SYSTEM = (
    "You are a machine learning and computational biology expert. "
    "Write a concise, factual paragraph (3-5 sentences) that directly answers "
    "the question below, using precise technical language typical of a lecture "
    "transcript or course textbook. Do not hedge or say 'hypothetically'. "
    "Write as if you are the author of a lecture note."
)

_EXPANSION_SYSTEM = (
    "You are a search-query specialist for a machine learning / computational "
    "biology course wiki. Given a student question, output exactly 2 alternative "
    "phrasings that would retrieve different but relevant documents. "
    "Rules: one line per phrasing, no numbering, no explanation, no blank lines."
)


# ── data class ────────────────────────────────────────────────────────────────

@dataclass
class EnhancedQuery:
    """
    Holds the original query and any enhancement artefacts.

    Attributes
    ----------
    original_query:  the raw user question
    hyde_doc:        hypothetical answer paragraph (None when HyDE disabled/failed)
    bm25_queries:    list of strings to run BM25 on — always starts with the
                     original query, then expansion alternatives, then the HyDE
                     doc (if produced).  BM25 results are merged by max-score.
    vector_query:    string to use for dense/vector retrieval.
                     = hyde_doc when HyDE is active, else original_query.
    """
    original_query: str
    hyde_doc:        Optional[str]  = None
    bm25_queries:    List[str]      = field(default_factory=list)
    vector_query:    str            = ""

    def __post_init__(self) -> None:
        if not self.bm25_queries:
            self.bm25_queries = [self.original_query]
        if not self.vector_query:
            self.vector_query = self.original_query


# ── enhancer ──────────────────────────────────────────────────────────────────

class QueryEnhancer:
    """
    Applies HyDE and/or query expansion to a raw user question.

    Parameters
    ----------
    model:              LiteLLM-routable model string (e.g. "gpt-4.1-mini")
    enable_hyde:        generate a hypothetical answer paragraph
    enable_expansion:   generate 2 alternative phrasings for multi-query BM25
    """

    def __init__(
        self,
        model: str,
        enable_hyde: bool = False,
        enable_expansion: bool = False,
    ) -> None:
        self._model            = model
        self._enable_hyde      = enable_hyde
        self._enable_expansion = enable_expansion

    @property
    def active(self) -> bool:
        return self._enable_hyde or self._enable_expansion

    # ── public API ────────────────────────────────────────────────────────────

    def enhance(self, question: str) -> EnhancedQuery:
        """
        Run the enabled enhancement techniques and return an EnhancedQuery.

        Both LLM calls are issued concurrently when both techniques are on,
        so latency ≈ max(t_hyde, t_expansion) instead of the sum.
        Falls back gracefully if any LLM call fails.
        """
        hyde_doc:     Optional[str] = None
        alternatives: List[str]     = []

        if self._enable_hyde and self._enable_expansion:
            # Parallel path
            with ThreadPoolExecutor(max_workers=2) as ex:
                futures = {
                    ex.submit(self._generate_hyde,    question): "hyde",
                    ex.submit(self._expand_query,     question): "expansion",
                }
                for future in as_completed(futures):
                    tag = futures[future]
                    try:
                        result = future.result()
                        if tag == "hyde":
                            hyde_doc = result
                        else:
                            alternatives = result
                    except Exception as e:
                        log.warning("Enhancement future %s failed: %s", tag, e)

        elif self._enable_hyde:
            hyde_doc = self._generate_hyde(question)

        elif self._enable_expansion:
            alternatives = self._expand_query(question)

        # Build bm25_queries: original first, then alternatives, then hyde doc.
        # The hyde doc is appended last so its keyword-rich text can boost recall
        # for concepts the user didn't name explicitly.
        bm25_queries = [question] + alternatives
        if hyde_doc:
            bm25_queries.append(hyde_doc)

        # Vector search uses the hypothesis if available (core HyDE insight).
        vector_query = hyde_doc if hyde_doc else question

        return EnhancedQuery(
            original_query = question,
            hyde_doc       = hyde_doc,
            bm25_queries   = bm25_queries,
            vector_query   = vector_query,
        )

    # ── private helpers ───────────────────────────────────────────────────────

    def _generate_hyde(self, question: str) -> Optional[str]:
        """
        Ask the LLM to produce a short hypothetical answer paragraph.
        Returns None on failure so the pipeline falls back to the original query.
        """
        try:
            resp = litellm.completion(
                model    = self._model,
                messages = [
                    {"role": "system", "content": _HYDE_SYSTEM},
                    {"role": "user",   "content": question},
                ],
                temperature = 0.3,
                max_tokens  = 220,
                seed        = 42,
            )
            text = (resp.choices[0].message.content or "").strip()
            if text:
                log.debug("HyDE: generated %d-char hypothesis", len(text))
                return text
            return None
        except Exception as e:
            log.warning("HyDE generation failed (%s) — original query used", e)
            return None

    def _expand_query(self, question: str) -> List[str]:
        """
        Ask the LLM to produce 2 alternative query phrasings.
        Returns [] on failure so only the original query is used.
        """
        try:
            resp = litellm.completion(
                model    = self._model,
                messages = [
                    {"role": "system", "content": _EXPANSION_SYSTEM},
                    {"role": "user",   "content": question},
                ],
                temperature = 0.5,
                max_tokens  = 120,
                seed        = 42,
            )
            raw  = (resp.choices[0].message.content or "").strip()
            alts = [ln.strip() for ln in raw.splitlines() if ln.strip()][:2]
            log.debug("Query expansion: %d alternatives generated", len(alts))
            return alts
        except Exception as e:
            log.warning("Query expansion failed (%s) — no alternatives added", e)
            return []
