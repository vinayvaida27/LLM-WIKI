"""
Retrieval evaluation metrics.

All metrics operate on retrieved chunk lists and expected entity sets.
The entity→lecture mapping is the ground truth: a chunk is "relevant" if
its lecture_number appears in the expected entities' lecture lists.
"""

from __future__ import annotations

import math
from typing import Any, Dict, List, Set


# ── building the relevant-ID set from entity lectures ────────────────────────

def relevant_ids_from_entities(
    chunks: List[Dict[str, Any]],
    expected_entities: List[str],
    entity_lecture_map: Dict[str, List[int]],
) -> Set[str]:
    """
    Collect chunk IDs whose lecture_number appears in any expected entity's lectures.
    """
    relevant_lecs: Set[int] = set()
    for e in expected_entities:
        relevant_lecs.update(int(l) for l in entity_lecture_map.get(e, []))

    return {
        c.get("id", "")
        for c in chunks
        if c.get("lecture_number") is not None
        and int(c["lecture_number"]) in relevant_lecs
    }


# ── individual metrics ────────────────────────────────────────────────────────

def hit_at_k(retrieved_ids: List[str], relevant_ids: Set[str], k: int) -> int:
    """1 if at least one relevant chunk appears in the top-k results, else 0."""
    return int(any(rid in relevant_ids for rid in retrieved_ids[:k]))


def reciprocal_rank(retrieved_ids: List[str], relevant_ids: Set[str]) -> float:
    """1/rank of the first relevant chunk; 0 if none found."""
    for i, rid in enumerate(retrieved_ids, start=1):
        if rid in relevant_ids:
            return 1.0 / i
    return 0.0


def ndcg_at_k(retrieved_ids: List[str], relevant_ids: Set[str], k: int) -> float:
    """Binary-relevance nDCG@k."""
    dcg  = sum(
        1.0 / math.log2(i + 2)
        for i, rid in enumerate(retrieved_ids[:k])
        if rid in relevant_ids
    )
    ideal_hits = min(len(relevant_ids), k)
    idcg = sum(1.0 / math.log2(i + 2) for i in range(ideal_hits))
    return dcg / idcg if idcg > 0 else 0.0


def entity_coverage(
    chunks: List[Dict[str, Any]],
    expected_entities: List[str],
    entity_lecture_map: Dict[str, List[int]],
) -> float:
    """
    Fraction of expected entities that have at least one retrieved chunk
    coming from a lecture where the entity is taught.
    """
    if not expected_entities:
        return 1.0
    found = 0
    for entity in expected_entities:
        lecs = {int(l) for l in entity_lecture_map.get(entity, [])}
        if any(c.get("lecture_number") is not None
               and int(c["lecture_number"]) in lecs
               for c in chunks):
            found += 1
    return found / len(expected_entities)


def duplicate_rate(chunks: List[Dict[str, Any]]) -> float:
    """Fraction of retrieved chunks that are exact ID duplicates."""
    if len(chunks) <= 1:
        return 0.0
    ids = [c.get("id") or c.get("chunk_id") or "" for c in chunks]
    return 1.0 - (len(set(ids)) / len(ids))


def raw_chunk_fraction(chunks: List[Dict[str, Any]]) -> float:
    """Fraction of retrieved chunks that come from the raw_chunk layer."""
    if not chunks:
        return 0.0
    return sum(1 for c in chunks if c.get("layer") == "raw_chunk") / len(chunks)


# ── aggregate ─────────────────────────────────────────────────────────────────

def compute_all(
    chunks: List[Dict[str, Any]],
    expected_entities: List[str],
    entity_lecture_map: Dict[str, List[int]],
    k: int = 5,
) -> Dict[str, float]:
    """Compute all metrics and return as a flat dict."""
    ids = [c.get("id", "") for c in chunks]
    relevant = relevant_ids_from_entities(chunks, expected_entities, entity_lecture_map)

    return {
        f"hit@{k}":            float(hit_at_k(ids, relevant, k)),
        "mrr":                 reciprocal_rank(ids, relevant),
        f"ndcg@{k}":           ndcg_at_k(ids, relevant, k),
        "entity_coverage":     entity_coverage(chunks, expected_entities, entity_lecture_map),
        "duplicate_rate":      duplicate_rate(chunks),
        "raw_chunk_fraction":  raw_chunk_fraction(chunks),
    }
