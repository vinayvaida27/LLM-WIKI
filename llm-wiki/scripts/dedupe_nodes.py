#!/usr/bin/env python3
"""Check duplicate visible graph nodes."""

from __future__ import annotations

import argparse

from wiki_score import duplicate_groups, graph_search, hidden_by_graph_search, load_notes


def main() -> int:
    parser = argparse.ArgumentParser(description="Find duplicate node labels in the visible graph.")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    search = graph_search()
    notes = [note for note in load_notes() if not hidden_by_graph_search(note, search)]
    exact, near = duplicate_groups(notes)
    print(f"Duplicate title groups: {len(exact)}")
    for _key, paths in list(exact.items())[:50]:
        print("DUPLICATE " + " | ".join(paths))
    print(f"Near duplicate groups: {len(near)}")
    for paths in near[:25]:
        print("NEAR " + " | ".join(paths))
    if args.check and exact:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
