# LLM Wiki Lint

Use this skill when validating Wiki quality before commits.

## Steps

1. Confirm source notes are under `Raw/Sources/`.
2. Confirm compiled notes are under `Wiki/`.
3. Validate allowed compiled tags.
4. Validate `sources` links resolve to existing raw files.
5. Validate `source_count` equals `sources` length.
6. Flag unsupported claims and invented citations.
7. Run lint and source checks with the local maintenance tool.
