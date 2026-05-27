"""
Retrieval Router: decide which retrieval strategies to activate for a query.

Reads QueryAnalysis and returns a RetrievalStrategy dataclass describing
which components should run (keyword BM25, entity boost, graph traversal).
"""

from __future__ import annotations

from dataclasses import dataclass
from .query_analyzer import QueryAnalysis


@dataclass
class RetrievalStrategy:
    use_keyword: bool = True
    use_entity_boost: bool = False   # boost raw_chunks from entity lectures
    use_graph: bool = False          # expand entity set via graph traversal
    description: str = "keyword"


class RetrievalRouter:
    def route(self, analysis: QueryAnalysis) -> RetrievalStrategy:
        s = RetrievalStrategy()

        if analysis.entities:
            s.use_entity_boost = True

        match analysis.intent:
            case "comparison":
                s.use_graph = True
            case "graph":
                s.use_graph = True
                s.use_entity_boost = True
            case "definition":
                s.use_entity_boost = bool(analysis.entities)
            case "lecture":
                # lecture queries: pure keyword match is most precise
                s.use_entity_boost = False
                s.use_graph = False
            case _:
                pass   # factual — keyword + entity_boost if entities found

        # build description string
        parts = ["keyword"]
        if s.use_entity_boost:
            parts.append("entity_boost")
        if s.use_graph:
            parts.append("graph")
        s.description = "+".join(parts)

        return s
