# Workflow Examples

## Ingest A New Source

1. Add a source note to `Raw/Sources/`.
2. Keep source wording faithful to the original material.
3. Set `Processed: false` until compiled notes exist.

## Compile Knowledge Notes

1. Read the relevant source note.
2. Write focused notes in the correct `Wiki/` folder.
3. Add one or more raw source links in `sources`.
4. Set `source_count` to match `sources`.
5. Keep notes short and reusable.

## Query First, Then Expand

1. Start with `Wiki/index.md` and `Wiki/catalog.jsonl`.
2. Run `python scripts/query_wiki.py --query "question text"` for tokenized retrieval over compiled Wiki notes.
3. Open only the most relevant compiled notes.
4. Open `Raw/Sources/` only when additional evidence, quotes, timestamps, or missing details are needed.
5. Ignore `Raw/Files/` during retrieval; it is backup/staging only.

## Maintenance Check

Run build, lint, and source checks before committing.
