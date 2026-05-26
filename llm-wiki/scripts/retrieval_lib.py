#!/usr/bin/env python3
"""Small standard-library helpers for local Wiki retrieval."""

from __future__ import annotations

import datetime as dt
import json
import math
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "Wiki"
RAW_SOURCES = ROOT / "Raw" / "Sources"
RETRIEVAL = ROOT / "retrieval"
WIKI_CHUNKS = RETRIEVAL / "wiki_chunks.jsonl"
RAW_CHUNKS = RETRIEVAL / "raw_chunks.jsonl"
QUERY_LOGS = RETRIEVAL / "query_logs.jsonl"
CATALOG = WIKI / "catalog.jsonl"

TOKEN_RE = re.compile(r"[a-z0-9]+")

FOLDER_TYPES = {
    "Topics": "topic",
    "Concepts": "concept",
    "Entities": "entity",
    "Projects": "project",
    "Logs": "log",
    "Methods": "method",
    "Equations": "equation",
    "Comparisons": "comparison",
    "Figures": "figure",
}


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def now_iso() -> str:
    return dt.datetime.now().replace(microsecond=0).isoformat()


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(json.dumps(row, sort_keys=True, ensure_ascii=False) for row in rows)
    path.write_text(text + ("\n" if text else ""), encoding="utf-8")


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, sort_keys=True, ensure_ascii=False) + "\n")


def parse_scalar(value: str):
    value = value.strip()
    if value == "[]":
        return []
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.isdigit():
        return int(value)
    return value.strip('"').strip("'")


def parse_frontmatter(text: str) -> tuple[dict, str, int]:
    lines = text.splitlines()
    if not lines or lines[0].lstrip("\ufeff").strip() != "---":
        return {}, text, 0

    end = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = index
            break
    if end is None:
        return {}, text, 0

    data: dict = {}
    current_key = None
    for line in lines[1:end]:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("- ") and current_key:
            data.setdefault(current_key, []).append(parse_scalar(stripped[2:]))
            continue
        if ":" in line and not line.startswith(" "):
            key, raw_value = line.split(":", 1)
            key = key.strip()
            raw_value = raw_value.strip()
            if raw_value:
                data[key] = parse_scalar(raw_value)
                current_key = None
            else:
                data[key] = []
                current_key = key

    body = "\n".join(lines[end + 1 :])
    return data, body, end + 1


def read_markdown(path: Path) -> tuple[dict, str, int, list[str]]:
    text = path.read_text(encoding="utf-8")
    frontmatter, body, body_start_line = parse_frontmatter(text)
    return frontmatter, body, body_start_line, text.splitlines()


def title_from(path: Path, frontmatter: dict, body: str) -> str:
    for key in ("title", "Title"):
        value = frontmatter.get(key)
        if isinstance(value, str) and value:
            return value
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").replace("_", " ").title()


def sources_from(frontmatter: dict) -> list[str]:
    sources = frontmatter.get("sources", [])
    if isinstance(sources, str):
        return [sources]
    return list(sources) if isinstance(sources, list) else []


def type_from_path(path: Path, frontmatter: dict) -> str:
    parts = path.relative_to(WIKI).parts if WIKI in path.resolve().parents else path.parts
    if len(parts) >= 2 and parts[0] == "Topics" and parts[1] == "Lectures":
        return "lecture-note"
    if parts:
        folder_type = FOLDER_TYPES.get(parts[0])
        if folder_type:
            return folder_type
    tags = frontmatter.get("tags", [])
    if isinstance(tags, str):
        return tags
    if isinstance(tags, list) and tags:
        return str(tags[0])
    return ""


def lecture_number_from(path: Path, title: str) -> int | None:
    text = f"{path.name} {title}"
    match = re.search(r"lecture[-_\s]*(\d+)", text, flags=re.IGNORECASE)
    return int(match.group(1)) if match else None


def bm25_rank(query: str, docs: list[str]) -> list[tuple[int, float]]:
    query_terms = tokenize(query)
    if not query_terms or not docs:
        return []
    doc_terms = [tokenize(doc) for doc in docs]
    doc_lengths = [len(terms) for terms in doc_terms]
    avgdl = sum(doc_lengths) / len(doc_lengths) if doc_lengths else 0.0
    dfs: Counter[str] = Counter()
    for terms in doc_terms:
        dfs.update(set(terms))

    n_docs = len(docs)
    k1 = 1.5
    b = 0.75
    scores = []
    for index, terms in enumerate(doc_terms):
        counts = Counter(terms)
        dl = doc_lengths[index] or 1
        score = 0.0
        for term in query_terms:
            tf = counts.get(term, 0)
            if not tf:
                continue
            df = dfs.get(term, 0)
            idf = math.log(1 + ((n_docs - df + 0.5) / (df + 0.5)))
            denom = tf + k1 * (1 - b + b * dl / (avgdl or 1))
            score += idf * ((tf * (k1 + 1)) / denom)
        if score > 0:
            scores.append((index, score))
    return sorted(scores, key=lambda item: item[1], reverse=True)


def snippet(text: str, query: str, max_chars: int = 360) -> str:
    clean = re.sub(r"\s+", " ", text).strip()
    if len(clean) <= max_chars:
        return clean
    terms = tokenize(query)
    lower = clean.lower()
    hit = min((lower.find(term) for term in terms if lower.find(term) >= 0), default=0)
    start = max(0, hit - max_chars // 3)
    end = min(len(clean), start + max_chars)
    prefix = "..." if start else ""
    suffix = "..." if end < len(clean) else ""
    return prefix + clean[start:end].strip() + suffix


def wiki_note_files() -> list[Path]:
    if not WIKI.exists():
        return []
    skip_names = {"index.md", "generated-index.md"}
    return sorted(
        path
        for path in WIKI.rglob("*.md")
        if path.is_file() and path.name not in skip_names and rel(path) != "Wiki/log.md"
    )


def raw_source_files() -> list[Path]:
    if not RAW_SOURCES.exists():
        return []
    return sorted(path for path in RAW_SOURCES.rglob("*.md") if path.is_file())

