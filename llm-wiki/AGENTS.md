# AGENTS

## LLM Wiki Starter

This repository is a starter LLM Wiki for humans and agents.

Default structure:

- `Raw/` holds captured source material.
- `Wiki/` holds compiled, source-traceable knowledge notes.
- `Schema/` holds rules, commands, and maintenance references.

Canonical source rule:

- `Raw/Sources/` is the only canonical source layer.
- `Raw/Files/` is backup/staging and should be ignored by retrieval, lint, source manifests, and source citation.

Default workflow:

1. Add source material to `Raw/Sources/`.
2. Compile short reusable notes in `Wiki/`.
3. Rebuild indexes and `Wiki/catalog.jsonl`.
4. Run lint and source checks.
5. Append `Wiki/log.md`.

Use `scripts/wiki_tool.py` as the canonical repo-local maintenance tool for build, lint, source scan, source delta, source coverage, catalog search, and log commands.

Query architecture:

Use two retrieval passes when answering questions from the LLM Wiki.

Pass 1: Wiki retrieval

- Search `Wiki/catalog.jsonl` with `scripts/wiki_tool.py search-catalog`.
- Prefer `scripts/query_wiki.py --query "..."` for upgraded tokenized retrieval over catalog metadata and compiled Wiki chunks.
- Open the most relevant compiled Wiki notes first.
- Prefer clean concept, topic, entity, method, project, and comparison notes over broad Raw context.

Pass 2: Raw verification

- Open Raw transcripts only for evidence, quotes, timestamps, missing details, or source verification.
- Use the `sources` frontmatter from compiled Wiki notes to choose which Raw files to open.
- Do not search broad Raw context until the compiled Wiki layer has been checked.

Query priority:

1. `Wiki/index.md`
2. `Wiki/catalog.jsonl` and `retrieval/wiki_chunks.jsonl`
3. Relevant compiled Wiki notes
4. Compiled note frontmatter `sources`
5. Matching `Raw/Sources/` transcript/source evidence through `retrieval/raw_chunks.jsonl`
6. Answer with cited Wiki notes and Raw sources when Raw verification was used

Default write locations:

- Topic hubs: `Wiki/Topics/`
- Concepts: `Wiki/Concepts/`
- Entities: `Wiki/Entities/`
- Projects: `Wiki/Projects/`
- Logs: `Wiki/Logs/`

Non-negotiable rules:

- Treat `Raw/Sources/` as source material, not as compiled notes.
- Keep Raw source notes source-faithful.
- Do not overwrite Raw source content during compilation.
- Write reusable knowledge only under `Wiki/`.
- Keep every compiled note linked to one or more Raw sources.
- Use plain tags only.
- Use `topics` and `sources` frontmatter on compiled Wiki notes.
- Treat `source_count` as derived.
- Keep compiled notes short, single-purpose, and source-traceable.
- Query from `Wiki/index.md`, `Wiki/catalog.jsonl`, `retrieval/wiki_chunks.jsonl`, and relevant compiled Wiki notes before opening Raw context.
- Run `build`, `lint`, and source checks before commits.
- Do not invent citations or create unsupported claims.
