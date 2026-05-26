#!/usr/bin/env python3
"""Small public-safety audit for the starter LLM Wiki."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    re.compile(r"(?i)\b(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"),
    re.compile(r"C:\\Users\\[^\\\s]+"),
    re.compile(r"/Users/[^/\s]+"),
]
BLOCKED_PARTS = {
    ".git",
    ".obsidian/plugins",
    ".obsidian/cache",
    ".obsidian/logs",
}


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--", "."],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        return [path for path in ROOT.rglob("*") if path.is_file()]
    return [ROOT / line for line in result.stdout.splitlines() if line.strip()]


def is_blocked(path: Path) -> bool:
    text = path.relative_to(ROOT).as_posix()
    return any(text == part or text.startswith(f"{part}/") for part in BLOCKED_PARTS)


def main() -> int:
    errors = []
    for path in tracked_files():
        if not path.exists() or not path.is_file():
            continue
        if path.relative_to(ROOT).as_posix() == "scripts/audit_public.py":
            continue
        if is_blocked(path):
            errors.append(f"blocked path is tracked: {path.relative_to(ROOT).as_posix()}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"sensitive-looking content in {path.relative_to(ROOT).as_posix()}")
                break

    for error in errors:
        print(f"ERROR: {error}")
    print(f"Public audit checked {len(tracked_files())} tracked files.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
