#!/usr/bin/env python3
"""Graph-focused quality score for the local LLM Wiki."""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter, defaultdict, deque
from pathlib import Path
from statistics import median


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "Wiki"
RAW_SOURCES = ROOT / "Raw" / "Sources"
GRAPH_JSON = ROOT / ".obsidian" / "graph.json"
LINK_RE = re.compile(r"!?\[\[([^\]\n]+)\]\]")
TOKEN_RE = re.compile(r"[a-z0-9]+")
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
MAINTENANCE_TAGS = {"maintenance", "log", "template", "schema", "command-reference"}
MAINTENANCE_PATH_PARTS = {
    "_maintenance",
    "Logs",
    "Schema",
    "_templates",
    ".agents",
    ".obsidian",
}
REQUIRED_WIKI_KEYS = {"tags", "topics", "status", "created", "updated", "sources", "source_count", "aliases"}
RETRIEVAL_TESTS = [
    ("What is HMM?", {"hidden markov", "hmm", "viterbi"}),
    ("How are HMMs used in epigenomics?", {"epigenomics", "chromatin", "chromhmm"}),
    ("Explain chromatin states.", {"chromatin state", "histone", "enhancer"}),
    ("What is gene regulation?", {"gene regulation", "enhancer", "transcription factor"}),
    ("How does RNA-seq clustering work?", {"rna-seq", "gene expression", "clustering"}),
    ("What is the difference between supervised and unsupervised learning?", {"supervised", "unsupervised", "classification"}),
    ("Explain sequence alignment dynamic programming.", {"sequence alignment", "dynamic programming", "blast"}),
    ("What are protein language models?", {"protein language", "esm", "transformer"}),
    ("What is DNA language modeling?", {"dna language", "dnabert", "masked language"}),
    ("How does single-cell RNA-seq analysis work?", {"single-cell", "scrna-seq", "cell type"}),
    ("What is a gene regulatory network?", {"gene regulatory network", "network inference", "transcription factor"}),
    ("How are GNNs used in chemistry?", {"graph neural", "molecular graph", "message passing"}),
    ("How does molecule generation work?", {"molecule generation", "diffusion", "vae"}),
    ("What is GWAS?", {"gwas", "snp", "association"}),
    ("What is polygenic risk score?", {"polygenic risk", "prs", "gwas"}),
]


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def parse_scalar(value: str):
    value = value.strip()
    if value == "[]":
        return []
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if re.fullmatch(r"\d+", value):
        return int(value)
    if re.fullmatch(r"\d+\.\d+", value):
        return float(value)
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
    return data, "\n".join(lines[end + 1 :])


def as_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def title_from(path: Path, frontmatter: dict, body: str) -> str:
    for key in ("title", "Title"):
        value = frontmatter.get(key)
        if isinstance(value, str) and value:
            return value
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").replace("_", " ").title()


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(text).lower())


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())


def graph_search() -> str:
    if not GRAPH_JSON.exists():
        return ""
    try:
        return str(json.loads(GRAPH_JSON.read_text(encoding="utf-8")).get("search") or "")
    except json.JSONDecodeError:
        return ""


def hidden_by_graph_search(note: dict, search: str) -> bool:
    text = search.lower()
    path = note["path"].lower()
    tags = {str(tag).lower().lstrip("#") for tag in note["tags"]}
    for match in re.finditer(r"-(path|tag):([^\s]+)", text):
        kind, value = match.group(1), match.group(2).strip('"').lower()
        value = value.lstrip("#")
        if kind == "path" and value in path:
            return True
        if kind == "tag" and value in tags:
            return True
    return False


def note_kind(path: Path, frontmatter: dict) -> str:
    path_text = rel(path)
    parts = path.relative_to(ROOT).parts
    tags = {str(tag) for tag in as_list(frontmatter.get("tags"))}
    if path_text.startswith("Wiki/Topics/Lectures/") or re.search(r"lecture[-_ ]\d{1,2}", path.name, re.I):
        return "lecture"
    if path_text.startswith("Raw/Sources/"):
        return "source"
    if "topic" in tags or (path_text.startswith("Wiki/Topics/") and "/Lectures/" not in path_text):
        return "topic"
    if "concept" in tags or path_text.startswith("Wiki/Concepts/"):
        return "concept"
    if "entity" in tags or path_text.startswith("Wiki/Entities/"):
        return "entity"
    if "method" in tags or path_text.startswith("Wiki/Methods/"):
        return "method"
    if "equation" in tags or path_text.startswith("Wiki/Equations/"):
        return "equation"
    if "comparison" in tags or path_text.startswith("Wiki/Comparisons/"):
        return "comparison"
    if "figure" in tags or path_text.startswith("Wiki/Figures/"):
        return "figure"
    if parts and parts[0] in MAINTENANCE_PATH_PARTS:
        return "maintenance"
    if tags & MAINTENANCE_TAGS:
        return "maintenance"
    return "other"


def load_notes() -> list[dict]:
    roots = [WIKI, RAW_SOURCES, ROOT / "Comparisons", ROOT / "tutorial", ROOT / "Schema", ROOT / "_templates"]
    notes = []
    seen: set[Path] = set()
    for folder in roots:
        if not folder.exists():
            continue
        for path in sorted(folder.rglob("*.md")):
            if path in seen or not path.is_file() or path.name == ".gitkeep":
                continue
            seen.add(path)
            text = path.read_text(encoding="utf-8", errors="replace")
            frontmatter, body = parse_frontmatter(text)
            tags = [str(tag).strip('"') for tag in as_list(frontmatter.get("tags"))]
            title = title_from(path, frontmatter, body)
            aliases = [str(alias).strip('"') for alias in as_list(frontmatter.get("aliases"))]
            note = {
                "path": rel(path),
                "path_obj": path,
                "text": text,
                "body": body,
                "frontmatter": frontmatter,
                "title": title,
                "aliases": aliases,
                "tags": tags,
            }
            note["kind"] = note_kind(path, frontmatter)
            notes.append(note)
    return notes


def resolver(notes: list[dict]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = defaultdict(list)
    for note in notes:
        path = note["path"]
        candidates = {
            path,
            Path(path).with_suffix("").as_posix(),
            note["path_obj"].stem,
            note["title"],
            *note["aliases"],
        }
        for candidate in candidates:
            key = normalize(candidate)
            if key and path not in mapping[key]:
                mapping[key].append(path)
    return mapping


def build_graph(
    notes: list[dict],
    resolver_notes: list[dict] | None = None,
) -> tuple[dict[str, set[str]], dict[str, set[str]], list[tuple[str, str]], list[tuple[str, str]]]:
    mapping = resolver(resolver_notes or notes)
    visible_paths = {note["path"] for note in notes}
    outlinks: dict[str, set[str]] = defaultdict(set)
    inlinks: dict[str, set[str]] = defaultdict(set)
    valid: list[tuple[str, str]] = []
    broken: list[tuple[str, str]] = []
    for note in notes:
        src = note["path"]
        for match in LINK_RE.finditer(note["text"]):
            raw_target = match.group(1).strip()
            target = raw_target.split("|", 1)[0].split("#", 1)[0].strip()
            if not target:
                if raw_target.startswith("#"):
                    continue
                broken.append((src, raw_target))
                continue
            all_candidates = mapping.get(normalize(target), [])
            candidates = [candidate for candidate in all_candidates if candidate in visible_paths]
            if candidates:
                dst = candidates[0]
                if dst != src:
                    outlinks[src].add(dst)
                    inlinks[dst].add(src)
                    valid.append((src, dst))
            elif all_candidates:
                continue
            else:
                broken.append((src, target))
    return outlinks, inlinks, valid, broken


def components(paths: set[str], outlinks: dict[str, set[str]], inlinks: dict[str, set[str]]) -> list[set[str]]:
    seen: set[str] = set()
    groups: list[set[str]] = []
    for path in sorted(paths):
        if path in seen:
            continue
        group: set[str] = set()
        queue: deque[str] = deque([path])
        seen.add(path)
        while queue:
            node = queue.popleft()
            group.add(node)
            for neighbor in outlinks[node] | inlinks[node]:
                if neighbor in paths and neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        groups.append(group)
    return groups


def duplicate_groups(notes: list[dict]) -> tuple[dict[str, list[str]], list[list[str]]]:
    labels: dict[str, set[str]] = defaultdict(set)
    for note in notes:
        for label in [note["title"], note["path_obj"].stem.replace("-", " "), *note["aliases"]]:
            key = normalize(label)
            if key:
                labels[key].add(note["path"])
    exact = {key: sorted(paths) for key, paths in labels.items() if len(paths) > 1}
    title_items = [(note["path"], normalize(note["title"])) for note in notes if len(normalize(note["title"])) >= 8]
    near: list[list[str]] = []
    for index, (path_a, title_a) in enumerate(title_items):
        for path_b, title_b in title_items[index + 1 :]:
            if title_a == title_b:
                continue
            ratio = sum(1 for a, b in zip(title_a, title_b) if a == b) / max(len(title_a), len(title_b))
            if ratio >= 0.88:
                near.append([path_a, path_b])
    return exact, near


def bm25_score(query: str, docs: list[tuple[str, str]]) -> list[tuple[str, float, str]]:
    query_terms = tokenize(query)
    doc_terms = [tokenize(doc) for _path, doc in docs]
    if not query_terms or not docs:
        return []
    avgdl = sum(len(terms) for terms in doc_terms) / max(1, len(doc_terms))
    dfs: Counter[str] = Counter()
    for terms in doc_terms:
        dfs.update(set(terms))
    rows = []
    for index, terms in enumerate(doc_terms):
        counts = Counter(terms)
        dl = len(terms) or 1
        score = 0.0
        for term in query_terms:
            tf = counts.get(term, 0)
            if not tf:
                continue
            df = dfs.get(term, 0)
            idf = math.log(1 + ((len(docs) - df + 0.5) / (df + 0.5)))
            score += idf * (tf * 2.5) / (tf + 1.5 * (0.25 + 0.75 * dl / (avgdl or 1)))
        if score:
            path, doc = docs[index]
            rows.append((path, score, doc.lower()))
    return sorted(rows, key=lambda item: item[1], reverse=True)


def retrieval_score(notes: list[dict], broken_links: int) -> float:
    docs = [
        (
            note["path"],
            " ".join([note["title"], note["path"], " ".join(note["aliases"]), note["text"]]),
        )
        for note in notes
        if note["path"].startswith("Wiki/") and note["kind"] not in {"maintenance"}
    ]
    hits = []
    for query, expected in RETRIEVAL_TESTS:
        top = bm25_score(query, docs)[:5]
        haystack = "\n".join(doc for _path, _score, doc in top)
        hits.append(sum(1 for needle in expected if needle in haystack) / len(expected))
    penalty = min(20, broken_links * 2)
    return max(0.0, 100 * sum(hits) / len(hits) - penalty)


def schema_score(notes: list[dict]) -> tuple[float, list[str]]:
    points = 0
    total = 0
    errors: list[str] = []
    for note in notes:
        if not note["path"].startswith("Wiki/") or note["path"].endswith("/index.md"):
            continue
        total += len(REQUIRED_WIKI_KEYS) + 3
        fm = note["frontmatter"]
        for key in REQUIRED_WIKI_KEYS:
            if key in fm:
                points += 1
            else:
                errors.append(f"{note['path']} missing {key}")
        tags = [str(tag) for tag in as_list(fm.get("tags"))]
        if len([tag for tag in tags if tag in ALLOWED_TAGS or tag in MAINTENANCE_TAGS]) >= 1:
            points += 1
        else:
            errors.append(f"{note['path']} has no valid tag")
        sources = as_list(fm.get("sources"))
        if fm.get("source_count") == len(sources):
            points += 1
        else:
            errors.append(f"{note['path']} source_count mismatch")
        if note["kind"] == "maintenance" or sources:
            points += 1
        else:
            errors.append(f"{note['path']} missing sources")
    return (100.0 * points / max(1, total), errors)


def compute_score() -> dict:
    all_notes = load_notes()
    search = graph_search()
    visible_notes = [note for note in all_notes if not hidden_by_graph_search(note, search)]
    visible_paths = {note["path"] for note in visible_notes}
    outlinks, inlinks, valid_links, broken_links = build_graph(visible_notes, all_notes)
    degree = {path: len(outlinks[path] | inlinks[path]) for path in visible_paths}
    groups = components(visible_paths, outlinks, inlinks)
    largest = max((len(group) for group in groups), default=0)
    orphan_notes = [path for path, value in degree.items() if value == 0]
    weak_notes = [path for path, value in degree.items() if value == 1]
    exact_dupes, near_dupes = duplicate_groups(visible_notes)

    lecture_nodes = [note for note in visible_notes if note["kind"] in {"lecture", "source"}]
    concept_like = {
        note["path"]
        for note in visible_notes
        if note["kind"] in {"concept", "entity", "method", "equation", "comparison", "topic"}
    }
    lecture_connected = [
        note["path"]
        for note in lecture_nodes
        if len((outlinks[note["path"]] | inlinks[note["path"]]) & concept_like) >= 5
    ]
    concept_nodes = [note for note in visible_notes if note["kind"] in {"concept", "method", "entity"}]
    topic_paths = {note["path"] for note in visible_notes if note["kind"] == "topic"}
    lecture_paths = {note["path"] for note in visible_notes if note["kind"] in {"lecture", "source"}}
    concept_with_parent = [
        note["path"]
        for note in concept_nodes
        if (outlinks[note["path"]] | inlinks[note["path"]]) & topic_paths
    ]
    concept_with_related = [
        note["path"]
        for note in concept_nodes
        if len((outlinks[note["path"]] | inlinks[note["path"]]) & concept_like) >= 3
    ]
    concept_with_source = [
        note["path"]
        for note in concept_nodes
        if (outlinks[note["path"]] | inlinks[note["path"]]) & lecture_paths
    ]
    maintenance_visible = [
        note["path"]
        for note in visible_notes
        if note["kind"] == "maintenance"
        or (set(str(tag).lower() for tag in note["tags"]) & MAINTENANCE_TAGS)
        or any(part in note["path_obj"].relative_to(ROOT).parts for part in MAINTENANCE_PATH_PARTS)
    ]

    largest_ratio = largest / max(1, len(visible_notes))
    average_degree = sum(degree.values()) / max(1, len(degree))
    median_degree = float(median(degree.values())) if degree else 0.0
    connected_graph_score = min(
        100.0,
        45 * largest_ratio
        + 20 * min(average_degree / 4, 1)
        + 20 * (1 - min(len(broken_links) / 10, 1))
        + 15 * (1 - min(len(maintenance_visible) / 10, 1)),
    )
    duplicate_cleanup_score = max(0.0, 100 - 12 * len(exact_dupes) - 4 * max(0, len(near_dupes) - 3))
    semantic_link_score = 100.0 * (
        0.45 * len(lecture_connected) / max(1, len(lecture_nodes))
        + 0.25 * len(concept_with_parent) / max(1, len(concept_nodes))
        + 0.20 * len(concept_with_related) / max(1, len(concept_nodes))
        + 0.10 * len(concept_with_source) / max(1, len(concept_nodes))
    )
    orphan_reduction_score = max(0.0, 100 - 12 * max(0, len(orphan_notes) - 3) - 2 * len(weak_notes))
    retrieval = retrieval_score(visible_notes, len(broken_links))
    schema, schema_errors = schema_score(all_notes)
    total = (
        0.25 * connected_graph_score
        + 0.20 * duplicate_cleanup_score
        + 0.20 * semantic_link_score
        + 0.15 * orphan_reduction_score
        + 0.10 * retrieval
        + 0.10 * schema
    )

    return {
        "total_score": round(total, 2),
        "connected_graph_score": round(connected_graph_score, 2),
        "duplicate_cleanup_score": round(duplicate_cleanup_score, 2),
        "semantic_link_score": round(semantic_link_score, 2),
        "orphan_reduction_score": round(orphan_reduction_score, 2),
        "retrieval_score": round(retrieval, 2),
        "schema_quality_score": round(schema, 2),
        "total_notes": len(visible_notes),
        "all_markdown_notes": len(all_notes),
        "total_links": len(valid_links) + len(broken_links),
        "valid_links": len(valid_links),
        "broken_links": len(broken_links),
        "orphan_notes": len(orphan_notes),
        "weak_notes_degree_1": len(weak_notes),
        "duplicate_title_groups": len(exact_dupes),
        "near_duplicate_groups": len(near_dupes),
        "connected_components": len(groups),
        "largest_component_size": largest,
        "largest_component_ratio": round(largest_ratio, 4),
        "average_degree": round(average_degree, 2),
        "median_degree": median_degree,
        "lecture_nodes": len(lecture_nodes),
        "lecture_nodes_connected_to_concepts": len(lecture_connected),
        "concept_nodes": len(concept_nodes),
        "concept_nodes_with_parent": len(concept_with_parent),
        "concept_nodes_with_related_links": len(concept_with_related),
        "concept_nodes_with_source_lecture": len(concept_with_source),
        "maintenance_nodes_in_main_graph": len(maintenance_visible),
        "graph_search": search,
        "orphan_sample": sorted(orphan_notes)[:30],
        "weak_sample": sorted(weak_notes)[:30],
        "broken_link_sample": broken_links[:30],
        "duplicate_groups_sample": list(exact_dupes.values())[:10],
        "near_duplicate_sample": near_dupes[:10],
        "maintenance_visible_sample": sorted(maintenance_visible)[:30],
        "schema_error_count": len(schema_errors),
        "schema_error_sample": schema_errors[:30],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Score LLM Wiki graph quality.")
    parser.add_argument("--json", action="store_true", help="Emit JSON report.")
    args = parser.parse_args()
    report = compute_score()
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(f"total_score={report['total_score']}")
        print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
