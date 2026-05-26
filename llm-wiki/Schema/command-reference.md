# Command Reference

Use `scripts/wiki_tool.py` as the repo-local maintenance tool.

## Health

```bash
python scripts/wiki_tool.py doctor
```

Checks folders, Python version, catalog status, source manifest status, and note counts.

## Build

```bash
python scripts/wiki_tool.py build
```

Generates `Wiki/catalog.jsonl`, `Wiki/generated-index.md`, and per-folder index files. `Wiki/index.md` is the hand-curated human landing page and is not overwritten by build.

## Lint

```bash
python scripts/wiki_tool.py lint
python scripts/wiki_tool.py source-lint
```

Validates compiled Wiki notes, source links, source counts, and Raw source metadata.

## Sources

```bash
python scripts/wiki_tool.py source-scan
python scripts/wiki_tool.py source-scan --update --accept-covered
python scripts/wiki_tool.py source-delta
python scripts/wiki_tool.py source-coverage
```

Scans Raw sources, updates `Schema/source-manifest.jsonl`, reports manifest deltas, and shows coverage.

## Search

```bash
python scripts/wiki_tool.py search-catalog --query "llm wiki"
```

Searches compiled Wiki notes through the catalog.

## Retrieval

```bash
python scripts/wiki_tool.py chunk
python scripts/query_wiki.py --query "hidden markov models epigenomics"
python scripts/query_wiki.py --query "hidden markov models epigenomics" --verify
python scripts/search_raw.py --query "hidden chromatin state" --wiki-note Wiki/Topics/Lectures/lecture-05-epigenomics-hmms.md
```

`chunk` builds standard-library keyword retrieval chunks in `retrieval/wiki_chunks.jsonl` and `retrieval/raw_chunks.jsonl`. `query_wiki.py` searches compiled Wiki chunks first and opens Raw chunks only when verification is requested, evidence/timestamps are requested, or Wiki results are weak.

## Log

```bash
python scripts/wiki_tool.py log --title "title" --details "details"
```

Appends a short entry to `Wiki/log.md`.

## Public Audit

```bash
python scripts/audit_public.py
```

Checks tracked files for obvious secrets, local machine paths, private keys, and tracked plugin or cache state.
