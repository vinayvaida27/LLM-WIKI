#!/usr/bin/env python3
"""Small retrieval smoke evaluation for the graph repair loop."""

from __future__ import annotations

from wiki_score import compute_score


def main() -> int:
    report = compute_score()
    print(f"Retrieval score: {report['retrieval_score']}")
    print(f"Broken links: {report['broken_links']}")
    print(f"Duplicate groups: {report['duplicate_title_groups']}")
    return 0 if report["retrieval_score"] >= 85 and report["broken_links"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
