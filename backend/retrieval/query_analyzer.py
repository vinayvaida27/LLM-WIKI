"""
Query Analysis: extract entities, keywords, and intent from a user query.

Uses entity_aliases.json (alias → canonical entity ID) and entity_index.json
(entity ID → metadata including lectures) to ground query terms to known wiki
entities and discover which raw_chunk lectures are most relevant.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# ── data class ────────────────────────────────────────────────────────────────

@dataclass
class QueryAnalysis:
    raw_query: str
    entities: List[str] = field(default_factory=list)          # canonical entity IDs
    aliases_matched: Dict[str, str] = field(default_factory=dict)  # alias → entity_id
    keywords: List[str] = field(default_factory=list)
    intent: str = "factual"     # definition|comparison|graph|lecture|factual
    lecture_hint: Optional[int] = None
    entity_lectures: List[int] = field(default_factory=list)   # lecture ints for found entities
    comparison_pair: Optional[Tuple[str, str]] = None


# ── intent detection ──────────────────────────────────────────────────────────

# Ordered: first match wins (most specific patterns first)
_INTENT_PATTERNS: List[Tuple[str, str]] = [
    ("lecture",    r"\blecture\s*(\d+)\b|\blec\s*(\d+)\b"),
    ("comparison", r"\b(differ\w*|compar\w*|vs\.?\s|versus|contrast|distinguish|similar\w*)\b"),
    ("graph",      r"\b(related\s+to|connect\w+|relationship|link\s+between|how\s+is\s+\w+\s+related|path\s+between)\b"),
    ("definition", r"\b(what\s+is|what\s+are|define|definition|explain|describe|how\s+does)\b"),
]

def _detect_intent(lowered: str) -> Tuple[str, Optional[int]]:
    for intent, pattern in _INTENT_PATTERNS:
        m = re.search(pattern, lowered, re.I)
        if m:
            if intent == "lecture":
                g = next((x for x in m.groups() if x), None)
                try:
                    return "lecture", int(g)
                except (TypeError, ValueError):
                    return "lecture", None
            return intent, None
    return "factual", None


# ── tokenisation ──────────────────────────────────────────────────────────────

_STOPWORDS = frozenset({
    "the", "a", "an", "and", "or", "to", "of", "in", "on", "for", "with",
    "is", "are", "was", "were", "be", "by", "as", "from", "this", "that",
    "what", "how", "why", "when", "where", "explain", "describe", "tell",
    "me", "about", "into", "using", "use", "do", "does", "did", "it", "its",
    "you", "your", "can", "should", "would", "vs", "versus", "between",
})

def _keywords(text: str) -> List[str]:
    return [
        w for w in re.findall(r"[a-z][a-z0-9\-_]*", text.lower())
        if len(w) > 2 and w not in _STOPWORDS
    ]


# ── main class ────────────────────────────────────────────────────────────────

class QueryAnalyzer:
    def __init__(self, entity_index_path: Path, entity_aliases_path: Path) -> None:
        with open(entity_index_path, encoding="utf-8") as f:
            raw = json.load(f)
        self._entity_index: Dict[str, dict] = {
            k: v for k, v in raw.items() if not k.startswith("_")
        }

        with open(entity_aliases_path, encoding="utf-8") as f:
            raw = json.load(f)
        # normalise aliases to lowercase for case-insensitive matching
        self._aliases: Dict[str, str] = {
            k.lower(): v for k, v in raw.items() if not k.startswith("_")
        }

        # entity label → id (for direct label matching)
        self._label_to_id: Dict[str, str] = {
            meta.get("label", "").lower(): eid
            for eid, meta in self._entity_index.items()
            if meta.get("label")
        }

        # pre-sort aliases by length descending (longest match preferred)
        self._sorted_aliases = sorted(self._aliases.items(), key=lambda x: -len(x[0]))

    # ─────────────────────────────────────────────────────────────────────────

    def analyze(self, question: str) -> QueryAnalysis:
        lowered = question.lower()
        intent, lecture_hint = _detect_intent(lowered)
        kws = _keywords(lowered)

        # ── entity detection via aliases (longest match first) ────────────
        entities: List[str] = []
        aliases_matched: Dict[str, str] = {}
        for alias, entity_id in self._sorted_aliases:
            if entity_id in entities:
                continue
            # Use word-boundary matching for short aliases to avoid false positives
            # (e.g. "ld" in "alphafold2" should not match linkage-disequilibrium)
            if len(alias) <= 4:
                matched = bool(re.search(r"\b" + re.escape(alias) + r"\b", lowered))
            else:
                matched = alias in lowered
            if matched:
                entities.append(entity_id)
                aliases_matched[alias] = entity_id

        # ── entity detection via direct label match ───────────────────────
        for label, entity_id in self._label_to_id.items():
            if label and len(label) > 3 and label in lowered and entity_id not in entities:
                entities.append(entity_id)

        # ── collect lecture numbers for matched entities ───────────────────
        entity_lectures: List[int] = []
        for eid in entities:
            for lec in self._entity_index.get(eid, {}).get("lectures", []):
                if lec not in entity_lectures:
                    entity_lectures.append(int(lec))

        # ── comparison pair ───────────────────────────────────────────────
        comparison_pair: Optional[Tuple[str, str]] = None
        if intent == "comparison" and len(entities) >= 2:
            comparison_pair = (entities[0], entities[1])

        return QueryAnalysis(
            raw_query=question,
            entities=entities,
            aliases_matched=aliases_matched,
            keywords=kws,
            intent=intent,
            lecture_hint=lecture_hint,
            entity_lectures=entity_lectures,
            comparison_pair=comparison_pair,
        )

    def get_entity_meta(self, entity_id: str) -> dict:
        return self._entity_index.get(entity_id, {})

    def get_entity_labels(self, entity_ids: List[str]) -> List[str]:
        return [
            self._entity_index.get(eid, {}).get("label", eid)
            for eid in entity_ids
        ]
