#!/usr/bin/env python3
"""Two-pass keyword retrieval for the local LLM Wiki."""

from __future__ import annotations

import argparse
import json
import sys

from retrieval_lib import (
    CATALOG,
    QUERY_LOGS,
    WIKI_CHUNKS,
    append_jsonl,
    bm25_rank,
    load_jsonl,
    now_iso,
    snippet,
)
from search_raw import search_raw


RAW_TRIGGER_WORDS = {
    "quote",
    "quotes",
    "timestamp",
    "timestamps",
    "evidence",
    "source",
    "sources",
    "raw",
    "verbatim",
    "cite",
    "citation",
}


def catalog_docs(rows: list[dict]) -> list[str]:
    return [
        " ".join(
            [
                str(row.get("title", "")),
                str(row.get("path", "")),
                str(row.get("tag", "")),
                " ".join(row.get("topics") or []),
                " ".join(row.get("sources") or []),
            ]
        )
        for row in rows
    ]


def chunk_docs(rows: list[dict]) -> list[str]:
    return [
        " ".join(
            [
                str(row.get("title", "")),
                str(row.get("path", "")),
                str(row.get("type", "")),
                " ".join(row.get("heading_path") or []),
                str(row.get("text", "")),
            ]
        )
        for row in rows
    ]


def should_search_raw(query: str, verify: bool, wiki_results: list[tuple[dict, float]]) -> bool:
    if verify:
        return True
    query_terms = set(query.lower().split())
    if RAW_TRIGGER_WORDS & query_terms:
        return True
    if not wiki_results:
        return True
    return wiki_results[0][1] < 1.0


def print_catalog_results(rows: list[tuple[dict, float]]) -> None:
    print("\nWiki catalog results:")
    if not rows:
        print("- No catalog matches.")
        return
    for rank, (row, score) in enumerate(rows, start=1):
        print(f"{rank}. score={score:.3f} {row.get('path')} - {row.get('title')}")
        sources = row.get("sources") or []
        if sources:
            print(f"   sources: {', '.join(sources[:5])}{' ...' if len(sources) > 5 else ''}")


def print_chunk_results(query: str, rows: list[tuple[dict, float]]) -> None:
    print("\nWiki chunk results:")
    if not rows:
        print("- No Wiki chunk matches.")
        return
    for rank, (row, score) in enumerate(rows, start=1):
        location = f"{row.get('path')}:{row.get('start_line')}-{row.get('end_line')}"
        print(f"{rank}. score={score:.3f} {location}")
        heading = " > ".join(row.get("heading_path") or [])
        if heading:
            print(f"   heading: {heading}")
        sources = row.get("sources") or []
        if sources:
            print(f"   sources: {', '.join(sources[:5])}{' ...' if len(sources) > 5 else ''}")
        print(f"   {snippet(row.get('text', ''), query)}")


def print_raw_results(query: str, rows: list[tuple[dict, float]]) -> None:
    print("\nRaw verification results:")
    if not rows:
        print("- No Raw matches.")
        return
    for rank, (row, score) in enumerate(rows, start=1):
        location = f"{row.get('path')}:{row.get('start_line')}-{row.get('end_line')}"
        lecture = row.get("lecture_number") or ""
        print(f"{rank}. score={score:.3f} lecture={lecture} {location}")
        heading = " > ".join(row.get("heading_path") or [])
        if heading:
            print(f"   heading: {heading}")
        print(f"   {snippet(row.get('text', ''), query)}")


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Search compiled Wiki notes before Raw sources.")
    parser.add_argument("--query", required=True)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--top-k", type=int, default=5)
    args = parser.parse_args(argv)

    catalog_rows = load_jsonl(CATALOG)
    wiki_chunks = load_jsonl(WIKI_CHUNKS)

    catalog_ranked = [(catalog_rows[index], score) for index, score in bm25_rank(args.query, catalog_docs(catalog_rows))[: args.top_k]]
    wiki_ranked = [(wiki_chunks[index], score) for index, score in bm25_rank(args.query, chunk_docs(wiki_chunks))[: args.top_k]]

    raw_used = should_search_raw(args.query, args.verify, wiki_ranked)
    raw_ranked: list[tuple[dict, float]] = []
    if raw_used:
        source_scope = sorted({source for row, _score in wiki_ranked for source in (row.get("sources") or [])})
        raw_ranked = search_raw(args.query, top_k=args.top_k, sources=source_scope or None)

    print(f"Query: {args.query}")
    print_catalog_results(catalog_ranked)
    print_chunk_results(args.query, wiki_ranked)
    if raw_used:
        print_raw_results(args.query, raw_ranked)
    else:
        print("\nRaw verification results: skipped; Wiki results were strong enough and verification was not requested.")

    append_jsonl(
        QUERY_LOGS,
        {
            "timestamp": now_iso(),
            "query": args.query,
            "verify": args.verify,
            "raw_used": raw_used,
            "top_wiki_paths": [row.get("path") for row, _score in wiki_ranked[:3]],
            "top_raw_paths": [row.get("path") for row, _score in raw_ranked[:3]],
        },
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
