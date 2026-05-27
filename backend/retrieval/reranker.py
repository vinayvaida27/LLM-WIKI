"""
Reranker: compute a composite final_score for each retrieved chunk.

Scoring components (all normalised to [0, 1] before weighting):
  bm25_norm      — keyword match score from BM25 search
  vector_norm    — cosine similarity from vector search (0 when disabled)
  entity_match   — 1.0 if chunk.lecture_number ∈ entity_lectures, 0.5 otherwise
  layer_bonus    — raw_chunk preferred over wiki_chunk

Weights depend on whether vector search is active:

  With vector:      bm25 0.30 | vector 0.30 | entity 0.25 | layer 0.15
  Without vector:   bm25 0.50 | vector 0.00 | entity 0.30 | layer 0.20

No external dependencies.
"""

from __future__ import annotations

from typing import Any, Dict, List, Set

_LAYER_BONUS: Dict[str, float] = {
    "raw_chunk":    1.0,
    "wiki_catalog": 0.6,
    "wiki_chunk":   0.4,
}


def _safe_float(v: Any, default: float = 0.0) -> float:
    try:
        return float(v)
    except (TypeError, ValueError):
        return default


def _normalise(values: List[float]) -> List[float]:
    mx = max(values) if values else 0.0
    return [v / mx if mx > 0 else 0.0 for v in values]


def rerank(
    chunks: List[Dict[str, Any]],
    entity_lectures: Set[int],
) -> List[Dict[str, Any]]:
    """
    Attach ``final_score`` and ``entity_matched`` to each chunk.
    Automatically detects whether vector_score is present and adjusts weights.

    Parameters
    ----------
    chunks:           candidate chunks (BM25 + optional vector results merged)
    entity_lectures:  union of seed + graph-expanded lecture numbers
    """
    if not chunks:
        return []

    # Determine whether any chunk carries a vector_score
    has_vector = any(c.get("vector_score") is not None for c in chunks)

    if has_vector:
        W_BM25, W_VECTOR, W_ENTITY, W_LAYER = 0.30, 0.30, 0.25, 0.15
    else:
        W_BM25, W_VECTOR, W_ENTITY, W_LAYER = 0.50, 0.00, 0.30, 0.20

    bm25_scores   = [_safe_float(c.get("score", 0))        for c in chunks]
    vector_scores = [_safe_float(c.get("vector_score", 0)) for c in chunks]

    bm25_norm   = _normalise(bm25_scores)
    vector_norm = _normalise(vector_scores)

    scored: List[Dict[str, Any]] = []
    for i, c in enumerate(chunks):
        bm25   = bm25_norm[i]
        vector = vector_norm[i]
        layer  = _LAYER_BONUS.get(c.get("layer", ""), 0.3)

        chunk_lec = c.get("lecture_number")
        if entity_lectures and chunk_lec is not None:
            entity = 1.0 if int(chunk_lec) in entity_lectures else 0.0
        else:
            entity = 0.5  # no entity signal — neutral

        final = (
            W_BM25   * bm25 +
            W_VECTOR * vector +
            W_ENTITY * entity +
            W_LAYER  * layer
        )

        out = dict(c)
        out["final_score"]    = round(final, 4)
        out["entity_matched"] = entity == 1.0
        scored.append(out)

    scored.sort(key=lambda x: x["final_score"], reverse=True)
    return scored
