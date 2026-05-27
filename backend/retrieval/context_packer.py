"""
Context Packer: deduplicate, filter, and pack the final context for the LLM.

Preferences (in order):
  1. raw_chunk  — primary source of truth (direct lecture content)
  2. wiki_catalog — supporting metadata
  3. wiki_chunk  — synthesized notes (last resort)

Removes near-duplicate chunks by text content hash.
Respects a character budget and maximum chunk count.
Assigns citation labels C1, C2, … for use in the prompt.
"""

from __future__ import annotations

import hashlib
from typing import Any, Dict, List


_LAYER_RANK: Dict[str, int] = {
    "raw_chunk":    0,   # best
    "wiki_catalog": 1,
    "wiki_chunk":   2,   # last resort
}


def pack_context(
    chunks: List[Dict[str, Any]],
    max_chars: int = 10_000,
    max_chunks: int = 8,
    citation_base_url: str = "/api/llm-wiki/sources",
) -> List[Dict[str, Any]]:
    """
    Return a deduplicated, budget-capped list of chunks with citation labels.

    Each returned chunk has two extra fields:
      ``citation``      — "C1", "C2", …
      ``citation_url``  — full URL for the citation link
    """
    # ── dedup by text hash ────────────────────────────────────────────────
    seen_hashes: set = set()
    unique: List[Dict[str, Any]] = []
    for c in chunks:
        h = hashlib.md5((c.get("text") or "").encode("utf-8", errors="ignore")).hexdigest()
        if h not in seen_hashes:
            seen_hashes.add(h)
            unique.append(c)

    # ── sort: raw_chunk first, then by final_score ────────────────────────
    def _sort_key(c: Dict[str, Any]) -> tuple:
        rank  = _LAYER_RANK.get(c.get("layer", ""), 3)
        score = -float(c.get("final_score") or c.get("score") or 0.0)
        return (rank, score)

    unique.sort(key=_sort_key)

    # ── pack within budget ────────────────────────────────────────────────
    packed: List[Dict[str, Any]] = []
    total_chars = 0
    for c in unique:
        if len(packed) >= max_chunks:
            break
        text_len = len(c.get("text") or "")
        if total_chars + text_len > max_chars and packed:
            break
        packed.append(c)
        total_chars += text_len

    # ── assign citation labels ────────────────────────────────────────────
    result: List[Dict[str, Any]] = []
    for i, c in enumerate(packed, start=1):
        out = dict(c)
        out["citation"]     = f"C{i}"
        out["citation_url"] = f"{citation_base_url}/{c['id']}"
        result.append(out)

    return result
