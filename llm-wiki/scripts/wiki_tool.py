#!/usr/bin/env python3
"""Deterministic maintenance tool for the starter LLM Wiki."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_SOURCES = ROOT / "Raw" / "Sources"
WIKI = ROOT / "Wiki"
SCHEMA = ROOT / "Schema"
CATALOG = WIKI / "catalog.jsonl"
GENERATED_INDEX = WIKI / "generated-index.md"
MANIFEST = SCHEMA / "source-manifest.jsonl"
ALLOWED_TAGS = {
    "topic",
    "concept",
    "entity",
    "project",
    "log",
    "method",
    "equation",
    "comparison",
    "figure",
    "lecture-note",
}
WIKI_FOLDERS = [
    "Topics",
    "Concepts",
    "Entities",
    "Projects",
    "Logs",
    "Methods",
    "Equations",
    "Comparisons",
    "Figures",
]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def today() -> str:
    return dt.date.today().isoformat()


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


def parse_frontmatter(text: str) -> tuple[dict, str]:
    lines = text.splitlines()
    if not lines or lines[0].lstrip("\ufeff").strip() != "---":
        return {}, text

    end = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = index
            break
    if end is None:
        return {}, text

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
    return data, body


def read_note(path: Path) -> tuple[dict, str]:
    return parse_frontmatter(path.read_text(encoding="utf-8"))


def note_title(path: Path, frontmatter: dict, body: str) -> str:
    for key in ("title", "Title"):
        value = frontmatter.get(key)
        if isinstance(value, str) and value:
            return value
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def markdown_files(folder: Path) -> list[Path]:
    if not folder.exists():
        return []
    return sorted(path for path in folder.rglob("*.md") if path.is_file())


def wiki_note_files() -> list[Path]:
    files = []
    for path in markdown_files(WIKI):
        relative = rel(path)
        if path.name == "index.md" or path.name == "generated-index.md" or relative == "Wiki/log.md":
            continue
        files.append(path)
    return files


def catalog_entries() -> list[dict]:
    entries = []
    for path in wiki_note_files():
        frontmatter, body = read_note(path)
        tags = frontmatter.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        tag = next((item for item in tags if item in ALLOWED_TAGS), "")
        entries.append(
            {
                "path": rel(path),
                "title": note_title(path, frontmatter, body),
                "tag": tag,
                "topics": frontmatter.get("topics", []),
                "sources": frontmatter.get("sources", []),
                "updated": frontmatter.get("updated", ""),
            }
        )
    return entries


def source_coverage() -> dict[str, list[str]]:
    coverage: dict[str, list[str]] = {}
    for entry in catalog_entries():
        for source in entry.get("sources", []):
            coverage.setdefault(source, []).append(entry["path"])
    return coverage


def load_manifest() -> list[dict]:
    if not MANIFEST.exists():
        return []
    rows = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(json.dumps(row, sort_keys=True) for row in rows)
    path.write_text(text + ("\n" if text else ""), encoding="utf-8")


def command_doctor(_args: argparse.Namespace) -> int:
    required_dirs = [RAW_SOURCES, ROOT / "Raw" / "Files", WIKI, SCHEMA, ROOT / "_templates"]
    missing = [rel(path) for path in required_dirs if not path.exists()]
    print(f"Python: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print(f"Raw sources: {len(markdown_files(RAW_SOURCES))}")
    print(f"Wiki notes: {len(wiki_note_files())}")
    print(f"Catalog: {'present' if CATALOG.exists() else 'missing'}")
    print(f"Source manifest: {'present' if MANIFEST.exists() else 'missing'}")
    if missing:
        print("Missing folders:")
        for item in missing:
            print(f"- {item}")
        return 1
    return 0


def command_build(_args: argparse.Namespace) -> int:
    entries = catalog_entries()
    write_jsonl(CATALOG, entries)

    index_lines = ["# Wiki Index", ""]
    if entries:
        for entry in entries:
            index_lines.append(f"- [{entry['title']}]({entry['path'].removeprefix('Wiki/')})")
    else:
        index_lines.append("No compiled Wiki notes yet.")
    GENERATED_INDEX.write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    for folder in WIKI_FOLDERS:
        folder_path = WIKI / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        folder_entries = [entry for entry in entries if entry["path"].startswith(f"Wiki/{folder}/")]
        lines = [f"# {folder} Index", ""]
        if folder_entries:
            for entry in folder_entries:
                lines.append(f"- [{entry['title']}]({Path(entry['path']).name})")
        else:
            lines.append("No notes yet.")
        (folder_path / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Built catalog with {len(entries)} Wiki notes.")
    print(f"Wrote {rel(GENERATED_INDEX)}.")
    return 0


def command_lint(_args: argparse.Namespace) -> int:
    errors = []
    warnings = []
    raw_source_count = len(markdown_files(RAW_SOURCES))
    for path in wiki_note_files():
        frontmatter, _body = read_note(path)
        tags = frontmatter.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        compiled_tags = [tag for tag in tags if tag in ALLOWED_TAGS]
        sources = frontmatter.get("sources", [])
        if isinstance(sources, str):
            sources = [sources]
        source_count = frontmatter.get("source_count")

        if len(compiled_tags) != 1:
            errors.append(f"{rel(path)} must use exactly one allowed compiled tag.")
        if source_count != len(sources):
            errors.append(f"{rel(path)} source_count must equal number of sources.")
        if not sources:
            errors.append(f"{rel(path)} must link to at least one Raw source.")
        for source in sources:
            source_path = ROOT / source
            if not source.startswith("Raw/Sources/") or not source_path.exists():
                errors.append(f"{rel(path)} has invalid source link: {source}")
        if len(sources) > 5:
            warnings.append(
                f"{rel(path)} cites {len(sources)} Raw sources; broad source attribution weakens evidence precision."
            )
        if (
            raw_source_count
            and len(sources) == raw_source_count
            and any(part in path.parts for part in ("Methods", "Equations", "Comparisons"))
        ):
            warnings.append(
                f"{rel(path)} cites all {raw_source_count} lectures from a method/equation/comparison area; prefer narrower evidence sources."
            )

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"Lint checked {len(wiki_note_files())} Wiki notes.")
    return 1 if errors else 0


def command_chunk(_args: argparse.Namespace) -> int:
    from chunk_sources import main as chunk_main

    return chunk_main([])


def command_query(args: argparse.Namespace) -> int:
    from query_wiki import main as query_main

    argv = ["--query", args.query]
    if args.verify:
        argv.append("--verify")
    if args.top_k is not None:
        argv.extend(["--top-k", str(args.top_k)])
    return query_main(argv)


def command_search_raw(args: argparse.Namespace) -> int:
    from search_raw import main as search_raw_main

    argv = ["--query", args.query]
    if args.wiki_note:
        argv.extend(["--wiki-note", args.wiki_note])
    for source in args.source or []:
        argv.extend(["--source", source])
    if args.top_k is not None:
        argv.extend(["--top-k", str(args.top_k)])
    return search_raw_main(argv)


def source_rows(accept_covered: bool = False) -> list[dict]:
    coverage = source_coverage()
    rows = []
    for path in markdown_files(RAW_SOURCES):
        frontmatter, body = read_note(path)
        path_text = rel(path)
        covered_by = sorted(coverage.get(path_text, []))
        processed = bool(frontmatter.get("Processed", False))
        if accept_covered and covered_by:
            processed = True
        rows.append(
            {
                "path": path_text,
                "title": note_title(path, frontmatter, body),
                "processed": processed,
                "covered_by": covered_by,
                "updated": today(),
            }
        )
    return rows


def command_source_scan(args: argparse.Namespace) -> int:
    rows = source_rows(accept_covered=args.accept_covered)
    for row in rows:
        print(f"{row['path']} processed={row['processed']} covered_by={len(row['covered_by'])}")
    if args.update:
        write_jsonl(MANIFEST, rows)
        print(f"Updated {rel(MANIFEST)} with {len(rows)} sources.")
    return 0


def command_source_lint(_args: argparse.Namespace) -> int:
    errors = []
    coverage = source_coverage()
    for path in markdown_files(RAW_SOURCES):
        frontmatter, _body = read_note(path)
        path_text = rel(path)
        for field in ("Title", "Reference", "Created", "Processed", "tags"):
            if field not in frontmatter:
                errors.append(f"{path_text} missing {field}.")
        if frontmatter.get("Processed") is True and not coverage.get(path_text):
            errors.append(f"{path_text} is processed but has no Wiki coverage.")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"Source lint checked {len(markdown_files(RAW_SOURCES))} Raw sources.")
    return 1 if errors else 0


def command_source_delta(_args: argparse.Namespace) -> int:
    manifest_paths = {row.get("path") for row in load_manifest()}
    raw_paths = {rel(path) for path in markdown_files(RAW_SOURCES)}
    missing = sorted(raw_paths - manifest_paths)
    if missing:
        for path in missing:
            print(path)
    else:
        print("No source delta.")
    return 0


def command_source_coverage(_args: argparse.Namespace) -> int:
    coverage = source_coverage()
    for path in markdown_files(RAW_SOURCES):
        path_text = rel(path)
        covered_by = coverage.get(path_text, [])
        print(f"{path_text}: {', '.join(covered_by) if covered_by else 'not covered'}")
    return 0


def command_search_catalog(args: argparse.Namespace) -> int:
    query = args.query.lower()
    rows = []
    if CATALOG.exists():
        rows = [json.loads(line) for line in CATALOG.read_text(encoding="utf-8").splitlines() if line.strip()]
    else:
        rows = catalog_entries()
    matches = [
        row for row in rows if query in json.dumps(row, sort_keys=True).lower()
    ]
    for row in matches:
        print(f"{row['path']} - {row['title']}")
    if not matches:
        print("No catalog matches.")
    return 0


def command_log(args: argparse.Namespace) -> int:
    WIKI.mkdir(parents=True, exist_ok=True)
    log_path = WIKI / "log.md"
    entry = f"\n## {today()} - {args.title}\n\n{args.details}\n"
    if not log_path.exists():
        log_path.write_text("# Wiki Log\n", encoding="utf-8")
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(entry)
    print(f"Appended {rel(log_path)}.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Maintain the LLM Wiki.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("doctor").set_defaults(func=command_doctor)
    subparsers.add_parser("build").set_defaults(func=command_build)
    subparsers.add_parser("lint").set_defaults(func=command_lint)

    source_scan = subparsers.add_parser("source-scan")
    source_scan.add_argument("--update", action="store_true")
    source_scan.add_argument("--accept-covered", action="store_true")
    source_scan.set_defaults(func=command_source_scan)

    subparsers.add_parser("source-lint").set_defaults(func=command_source_lint)
    subparsers.add_parser("source-delta").set_defaults(func=command_source_delta)
    subparsers.add_parser("source-coverage").set_defaults(func=command_source_coverage)
    subparsers.add_parser("chunk").set_defaults(func=command_chunk)

    search = subparsers.add_parser("search-catalog")
    search.add_argument("--query", required=True)
    search.set_defaults(func=command_search_catalog)

    query = subparsers.add_parser("query")
    query.add_argument("--query", required=True)
    query.add_argument("--verify", action="store_true")
    query.add_argument("--top-k", type=int, default=None)
    query.set_defaults(func=command_query)

    search_raw = subparsers.add_parser("search-raw")
    search_raw.add_argument("--query", required=True)
    search_raw.add_argument("--wiki-note")
    search_raw.add_argument("--source", action="append")
    search_raw.add_argument("--top-k", type=int, default=None)
    search_raw.set_defaults(func=command_search_raw)

    log = subparsers.add_parser("log")
    log.add_argument("--title", required=True)
    log.add_argument("--details", required=True)
    log.set_defaults(func=command_log)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
