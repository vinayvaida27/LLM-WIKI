#!/usr/bin/env python3
"""Validate visible Obsidian links using the graph scorer's resolver."""

from __future__ import annotations

from wiki_score import build_graph, graph_search, hidden_by_graph_search, load_notes


def main() -> int:
    search = graph_search()
    all_notes = load_notes()
    notes = [note for note in all_notes if not hidden_by_graph_search(note, search)]
    _outlinks, _inlinks, valid, broken = build_graph(notes, all_notes)
    print(f"Valid links: {len(valid)}")
    print(f"Broken links: {len(broken)}")
    for source, target in broken[:50]:
        print(f"BROKEN {source} -> {target}")
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
