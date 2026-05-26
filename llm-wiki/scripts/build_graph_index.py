#!/usr/bin/env python3
"""Build a semantic graph index for inspection."""

from __future__ import annotations

import argparse
import json

from wiki_score import ROOT, WIKI, build_graph, graph_search, hidden_by_graph_search, load_notes


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Wiki/_maintenance/graph_index.json")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    search = graph_search()
    all_notes = load_notes()
    notes = [note for note in all_notes if not hidden_by_graph_search(note, search)]
    outlinks, inlinks, _valid, _broken = build_graph(notes, all_notes)
    rows = []
    for note in notes:
        path = note["path"]
        rows.append(
            {
                "note": note["title"],
                "path": path,
                "type": note["kind"],
                "aliases": note["aliases"],
                "outlinks": sorted(outlinks[path]),
                "inlinks": sorted(inlinks[path]),
                "degree": len(outlinks[path] | inlinks[path]),
                "source_lectures": sorted(link for link in outlinks[path] | inlinks[path] if "/Lectures/" in link or "Raw/Sources/" in link),
                "parent_topics": sorted(link for link in outlinks[path] | inlinks[path] if "Wiki/Topics/" in link and "/Lectures/" not in link),
                "related_concepts": sorted(link for link in outlinks[path] | inlinks[path] if any(part in link for part in ("Wiki/Concepts/", "Wiki/Methods/", "Wiki/Entities/"))),
            }
        )
    output = json.dumps(rows, indent=2, sort_keys=True)
    if args.write:
        target = WIKI / "_maintenance" / "graph_index.json"
        if target:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(output + "\n", encoding="utf-8")
            print(target.relative_to(ROOT).as_posix())
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
