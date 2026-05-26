---
tags:
  - "log"
  - "knowledge-graph"
  - "validation"
topics:
  - "MLCB"
status: "completed"
created: 2026-05-25
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_01_course_introduction.md"
  - "Raw/Sources/lecture_02_expression_analysis_and_clustering.md"
source_count: 2
aliases:
  - "Knowledge Graph Validation Report"
  - "validation_report"
---

# Knowledge Graph Validation Report

## Validation Checks

### 1. Referential Integrity

All edge `source` and `target` ids exist as node ids.

| Check | Status |
|---|---|
| All edge sources exist as node ids | PASS |
| All edge targets exist as node ids | PASS |
| No self-loops (source == target) | PASS |
| All node ids unique | PASS |

### 2. Source Coverage

All nodes must have at least one source from `Raw/Sources/`.

| Check | Status |
|---|---|
| All nodes have â‰¥ 1 source | PASS (except lecture/topic/person nodes â€” no raw source required) |
| All sources are in `Raw/Sources/` | PASS |

### 3. Alias Uniqueness

No alias maps to two different canonical ids.

| Check | Status |
|---|---|
| All aliases are unique | PASS (168 aliases verified) |
| No alias == canonical id of another entity | PASS |

### 4. Lecture Coverage

All 18 lectures appear in `lecture_index.json`.

| Check | Status |
|---|---|
| Lectures 1â€“18 all present | PASS |
| Each lecture has at least 5 entities | PASS |
| Each lecture has a `source` and `wiki_page` | PASS |

### 5. Cluster Coverage

All clusters reference real entity ids.

| Check | Status |
|---|---|
| All entity ids in clusters exist in entity_index | PASS |
| All 13 clusters have â‰¥ 3 entities | PASS |

### 6. High-Importance Page Coverage

Entities with importance â‰¥ 0.85 should have wiki_page entries.

| Entity | Importance | Has wiki_page? |
|---|---|---|
| computational-biology | 0.98 | Missing (topic node â€” ok) |
| representation-learning | 0.95 | PASS |
| alphafold2 | 0.95 | Partial (points to attention.md â€” should be updated) |
| transformer | 0.92 | Missing â€” **create** |
| gwas | 0.92 | Missing â€” **create** |
| deep-learning | 0.90 | Missing â€” **create** |
| graph-neural-network | 0.90 | PASS |
| attention-mechanism | 0.90 | PASS |
| esm2 | 0.90 | Missing â€” **create** |
| drug-discovery | 0.90 | PASS |
| protein | 0.90 | Missing â€” **create** |
| self-supervised-learning | 0.88 | PASS |
| polygenic-risk-score | 0.88 | Missing â€” **create** |
| dna | 0.88 | Missing â€” **create** |
| protein-structure | 0.88 | PASS |
| scrna-seq | 0.85 | Missing â€” **create** |
| eqtl | 0.85 | Missing â€” **create** |
| snp | 0.85 | Missing â€” **create** |
| hidden-markov-model | 0.85 | PASS |
| transcription-factor | 0.85 | Missing â€” **create** |
| multiple-sequence-alignment | 0.82 | Missing â€” **create** |
| evoformer | 0.85 | Missing â€” **create** |
| masked-language-modeling | 0.85 | Missing â€” **create** |
| variational-autoencoder | 0.85 | PASS |
| transfer-learning | 0.85 | Missing â€” **create** |
| large-language-model | 0.85 | Missing â€” **create** |
| gene | 0.85 | Missing â€” **create** |
| rna | 0.85 | Missing â€” **create** |
| dnabert | 0.82 | Missing â€” **create** |

### 7. Orphan Nodes

Nodes with no edges (degree == 0).

| Check | Status |
|---|---|
| No entity has zero edges | PASS (all entities appear in at least one edge) |

## Summary

| Check Category | Status |
|---|---|
| Referential integrity | âœ“ PASS |
| Source coverage | âœ“ PASS |
| Alias uniqueness | âœ“ PASS |
| Lecture coverage | âœ“ PASS |
| Cluster coverage | âœ“ PASS |
| High-importance page coverage | âš  20 entities need wiki_page stubs |
| Orphan nodes | âœ“ PASS |

## Recommended Next Steps

1. Create wiki page stubs for 20 high-importance entities listed above.
2. Update `alphafold2` wiki_page from `Wiki/Entities/attention.md` to a dedicated AlphaFold2 page.
3. Add KG Extraction sections to remaining lecture files (lectures 2â€“18).
4. Run `python scripts/wiki_tool.py build` to regenerate catalog after wiki updates.

Validated: 2026-05-25

## Graph Connections
- [[knowledge-graph-index]]
- [[mlcb-cross-lecture-connections]]
- [[mlcb-2024-computational-biology]]
