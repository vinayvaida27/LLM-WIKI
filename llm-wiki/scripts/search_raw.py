#!/usr/bin/env python3
"""Search Raw/Sources retrieval chunks, optionally scoped by a Wiki note."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from retrieval_lib import RAW_CHUNKS, ROOT, bm25_rank, load_jsonl, read_markdown, snippet, sources_from


def sources_from_wiki_note(note: str) -> list[str]:
    path = Path(note)
    if not path.is_absolute():
        path = ROOT / note
    if not path.exists():
        raise FileNotFoundError(f"Wiki note not found: {note}")
    frontmatter, _body, _line, _lines = read_markdown(path)
    return sources_from(frontmatter)


def search_raw(query: str, top_k: int = 8, sources: list[str] | None = None) -> list[tuple[dict, float]]:
    rows = load_jsonl(RAW_CHUNKS)
    if sources:
        allowed = set(sources)
        rows = [row for row in rows if row.get("path") in allowed]
    docs = [
        " ".join(
            [
                str(row.get("title", "")),
                " ".join(row.get("heading_path") or []),
                str(row.get("text", "")),
            ]
        )
        for row in rows
    ]
    ranked = bm25_rank(query, docs)[:top_k]
    return [(rows[index], score) for index, score in ranked]


def print_results(query: str, results: list[tuple[dict, float]]) -> None:
    if not results:
        print("No raw matches.")
        return
    for rank, (row, score) in enumerate(results, start=1):
        lecture = row.get("lecture_number") or ""
        location = f"{row.get('path')}:{row.get('start_line')}-{row.get('end_line')}"
        print(f"{rank}. score={score:.3f} lecture={lecture} {location}")
        heading = " > ".join(row.get("heading_path") or [])
        if heading:
            print(f"   heading: {heading}")
        print(f"   {snippet(row.get('text', ''), query)}")


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Search Raw/Sources chunks.")
    parser.add_argument("--query", required=True)
    parser.add_argument("--wiki-note")
    parser.add_argument("--source", action="append")
    parser.add_argument("--top-k", type=int, default=8)
    args = parser.parse_args(argv)

    sources = list(args.source or [])
    if args.wiki_note:
        sources.extend(sources_from_wiki_note(args.wiki_note))
    results = search_raw(args.query, top_k=args.top_k, sources=sources or None)
    print_results(args.query, results)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
