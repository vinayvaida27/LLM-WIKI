# LLM Wiki Query

Use this skill when answering questions from the Wiki.

## Steps

1. Start from `Wiki/index.md` and `Wiki/catalog.jsonl`.
2. Search compiled notes first with `scripts/query_wiki.py --query "question text"` or, for catalog-only lookup, `scripts/wiki_tool.py search-catalog`.
3. Read the most relevant compiled notes first.
4. Decide whether the Wiki notes are enough to answer.
5. If the compiled notes are thin, missing details, need quotes, need timestamps, or need source verification, search only the Raw files named in the compiled note frontmatter using `scripts/search_raw.py`.
6. Keep answers grounded in compiled notes and linked sources.
7. Cite compiled Wiki notes, and cite Raw sources when Raw verification was used.

## Query Architecture

Use two retrieval passes:

### Pass 1: Wiki retrieval

Search compiled notes for clean concepts.

### Pass 2: Raw verification

Open raw transcripts only for evidence, quotes, timestamps, or missing details.
Ignore `Raw/Files/`; it is backup/staging only.

## Query Priority

1. `Wiki/index.md`
2. `Wiki/catalog.jsonl` and `retrieval/wiki_chunks.jsonl`
3. Relevant compiled Wiki notes
4. Compiled note frontmatter `sources`
5. Matching `Raw/Sources/` transcript/source evidence through `retrieval/raw_chunks.jsonl`
6. Answer
