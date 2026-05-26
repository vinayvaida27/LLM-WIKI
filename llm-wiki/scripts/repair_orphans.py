#!/usr/bin/env python3
"""Report orphan and weak visible graph nodes for manual repair loops."""

from __future__ import annotations

from wiki_score import compute_score


def main() -> int:
    report = compute_score()
    print("Orphans:")
    for path in report["orphan_sample"]:
        print(f"- {path}")
    print("Weak degree-1 nodes:")
    for path in report["weak_sample"]:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
