"""
Graph Traversal: BFS over the knowledge graph to expand entity coverage.

Given a list of seed entity IDs, traverses the weighted directed graph
(graph_edges.jsonl / graph_nodes.jsonl) to discover related entities and
the lectures they belong to.  The discovered lecture numbers are used by
the reranker to boost raw_chunks that contain primary source evidence.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Set


def _load_jsonl(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    result: List[Dict[str, Any]] = []
    with open(path, encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    result.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return result


class GraphTraversal:
    def __init__(self, edges_path: Path, nodes_path: Path) -> None:
        self._nodes: Dict[str, Dict[str, Any]] = {}
        for node in _load_jsonl(nodes_path):
            self._nodes[node["id"]] = node

        # Bidirectional adjacency: entity_id → list of edge dicts
        self._adj: Dict[str, List[Dict[str, Any]]] = {}
        for edge in _load_jsonl(edges_path):
            src, tgt = edge["source"], edge["target"]
            self._adj.setdefault(src, []).append(edge)
            # reverse edge for bidirectional traversal
            rev = dict(edge)
            rev["source"], rev["target"] = tgt, src
            rev["relation"] = f"INV_{edge['relation']}"
            self._adj.setdefault(tgt, []).append(rev)

    # ─────────────────────────────────────────────────────────────────────────

    def traverse(
        self,
        seed_entity_ids: List[str],
        max_hops: int = 2,
        max_results: int = 15,
    ) -> List[Dict[str, Any]]:
        """
        BFS from seed entities; return related entity records sorted by
        importance / depth (closer, more important entities ranked first).
        """
        visited: Set[str] = set(seed_entity_ids)
        results: List[Dict[str, Any]] = []

        queue: List[tuple] = [
            (eid, 1, [])
            for eid in seed_entity_ids
            if eid in self._adj
        ]

        while queue and len(results) < max_results:
            current, depth, path = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)

            node = self._nodes.get(current, {})
            results.append({
                "entity_id":   current,
                "label":       node.get("label", current),
                "depth":       depth,
                "path":        path[:],
                "lectures":    [int(l) for l in node.get("lectures", [])],
                "wiki_page":   node.get("wiki_page", ""),
                "importance":  float(node.get("importance", 0.5)),
                "description": node.get("description", ""),
            })

            if depth < max_hops:
                for edge in self._adj.get(current, []):
                    neighbor = edge["target"]
                    if neighbor not in visited:
                        step = f'{edge.get("relation", "→")}({neighbor})'
                        queue.append((neighbor, depth + 1, path + [step]))

        # higher importance, shallower depth first
        results.sort(key=lambda x: x["importance"] / x["depth"], reverse=True)
        return results[:max_results]

    def get_related_lectures(
        self,
        entity_ids: List[str],
        max_hops: int = 2,
    ) -> Set[int]:
        """
        Collect all lecture numbers reachable within max_hops of seed entities.
        This is the primary output used to boost raw_chunk retrieval.
        """
        lectures: Set[int] = set()

        # seed entities' own lectures
        for eid in entity_ids:
            for lec in self._nodes.get(eid, {}).get("lectures", []):
                lectures.add(int(lec))

        # related entities' lectures
        for r in self.traverse(entity_ids, max_hops=max_hops):
            for lec in r.get("lectures", []):
                lectures.add(int(lec))

        return lectures
