#!/usr/bin/env python3
"""Build heading-aware keyword retrieval chunks for Wiki and Raw sources."""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path

from retrieval_lib import (
    QUERY_LOGS,
    RAW_CHUNKS,
    WIKI_CHUNKS,
    lecture_number_from,
    raw_source_files,
    read_markdown,
    rel,
    sources_from,
    title_from,
    type_from_path,
    tokenize,
    wiki_note_files,
    write_jsonl,
)


MAX_WORDS = 1200
TARGET_WORDS = 1000


def heading_level(line: str) -> int | None:
    match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
    return len(match.group(1)) if match else None


def split_sections(lines: list[str], first_body_line: int) -> list[dict]:
    sections: list[dict] = []
    heading_stack: list[str] = []
    current_lines: list[tuple[int, str]] = []
    current_heading_path: list[str] = []

    def flush() -> None:
        nonlocal current_lines, current_heading_path
        if current_lines and any(text.strip() for _line_no, text in current_lines):
            sections.append(
                {
                    "heading_path": list(current_heading_path),
                    "lines": current_lines,
                }
            )
        current_lines = []

    for zero_index, line in enumerate(lines[first_body_line:], start=first_body_line + 1):
        level = heading_level(line)
        if level is not None:
            flush()
            heading_text = re.sub(r"^#{1,6}\s+", "", line).strip()
            heading_stack = heading_stack[: level - 1]
            heading_stack.append(heading_text)
            current_heading_path = list(heading_stack)
        current_lines.append((zero_index, line))
    flush()
    return sections


def split_long_section(section: dict) -> list[dict]:
    lines = section["lines"]
    total_words = sum(len(tokenize(text)) for _line_no, text in lines)
    if total_words <= MAX_WORDS:
        return [section]

    chunks = []
    current: list[tuple[int, str]] = []
    word_count = 0
    for line_no, text in lines:
        current.append((line_no, text))
        word_count += len(tokenize(text))
        if word_count >= TARGET_WORDS:
            chunks.append({"heading_path": section["heading_path"], "lines": current})
            current = []
            word_count = 0
    if current:
        chunks.append({"heading_path": section["heading_path"], "lines": current})
    return chunks


def build_chunks(paths: list[Path], scope: str) -> list[dict]:
    rows = []
    for path in paths:
        frontmatter, body, body_start_line, all_lines = read_markdown(path)
        title = title_from(path, frontmatter, body)
        note_type = "source" if scope == "raw" else type_from_path(path, frontmatter)
        lecture_number = lecture_number_from(path, title)
        sources = sources_from(frontmatter)
        for section in split_sections(all_lines, body_start_line):
            for piece in split_long_section(section):
                numbered_lines = piece["lines"]
                text = "\n".join(text for _line_no, text in numbered_lines).strip()
                if not text:
                    continue
                if len(tokenize(text)) < 8:
                    continue
                start_line = numbered_lines[0][0]
                end_line = numbered_lines[-1][0]
                basis = f"{rel(path)}:{start_line}:{end_line}:{text[:80]}"
                chunk_hash = hashlib.sha1(basis.encode("utf-8")).hexdigest()[:12]
                rows.append(
                    {
                        "chunk_id": f"{scope}-{chunk_hash}",
                        "path": rel(path),
                        "title": title,
                        "folder": path.parent.name,
                        "type": note_type,
                        "lecture_number": lecture_number,
                        "heading_path": piece["heading_path"],
                        "start_line": start_line,
                        "end_line": end_line,
                        "sources": sources,
                        "text": text,
                    }
                )
    return rows


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Chunk Wiki notes and Raw sources for keyword retrieval.")
    parser.parse_args(argv)

    wiki_chunks = build_chunks(wiki_note_files(), "wiki")
    raw_chunks = build_chunks(raw_source_files(), "raw")
    write_jsonl(WIKI_CHUNKS, wiki_chunks)
    write_jsonl(RAW_CHUNKS, raw_chunks)
    QUERY_LOGS.parent.mkdir(parents=True, exist_ok=True)
    QUERY_LOGS.touch(exist_ok=True)

    print(f"Wrote {rel(WIKI_CHUNKS)} with {len(wiki_chunks)} chunks.")
    print(f"Wrote {rel(RAW_CHUNKS)} with {len(raw_chunks)} chunks.")
    print(f"Ready {rel(QUERY_LOGS)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
