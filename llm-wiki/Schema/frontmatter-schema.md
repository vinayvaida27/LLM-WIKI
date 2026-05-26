# Frontmatter Schema

This schema defines required metadata for source notes and compiled Wiki notes.

## Source Notes

Source notes live in `Raw/Sources/`.

Required fields:

- `Title`
- `Author`
- `Reference`
- `ContentType`
- `Created`
- `Processed`
- `tags`

Expected `tags` value: include `source`.

## Compiled Wiki Notes

Compiled notes live under `Wiki/`.

Required fields:

- `tags`
- `topics`
- `status`
- `created`
- `updated`
- `sources`
- `source_count`
- `aliases`

Allowed compiled note tags:

- `topic`
- `concept`
- `entity`
- `project`
- `log`
- `method`
- `equation`
- `comparison`
- `figure`
- `lecture-note`

Validation rules:

- Use exactly one compiled tag from the allowed list.
- `sources` must point to existing files under `Raw/Sources/`.
- `source_count` must equal the number of entries in `sources`.
- Broad source lists are allowed for existing notes, but lint warns when source attribution is too broad to be precise.
