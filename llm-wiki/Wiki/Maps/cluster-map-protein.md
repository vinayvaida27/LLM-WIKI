---
tags:
  - "topic"
  - "map"
  - "knowledge-graph"
  - "protein"
topics:
  - "MLCB"
  - "protein structure"
  - "protein language models"
status: "generated"
created: 2026-05-25
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_08_intro_to_protein_structure.md"
  - "Raw/Sources/lecture_09_protein_folding_algorithms.md"
  - "Raw/Sources/lecture_10_protein_structure_with_transformers.md"
  - "Raw/Sources/lecture_11_protein_language_models.md"
source_count: 4
aliases:
  - "Protein Cluster Map"
---

# Cluster Map: Protein Structure and Function

> Lectures 8â€“11 | Module 2

## Entities in this Cluster

| Entity | Type | Importance | Lectures |
|---|---|---|---|
| [[protein|Protein]] | biological_entity | 0.90 | 8,9,10,11 |
| [[alphafold2|AlphaFold2]] | model | 0.95 | 10 |
| [[evoformer|Evoformer]] | model | 0.85 | 10 |
| [[protein-structure|Protein Structure]] | concept | 0.88 | 8,9,10 |
| [[multiple-sequence-alignment|MSA]] | data_type | 0.82 | 9,10 |
| [[esm2|ESM-2]] | model | 0.90 | 11 |
| [[protein-sequence|Protein Sequence]] | data_type | 0.80 | 11 |
| [[contact-map|Protein Contact Map]] | data_type | 0.75 | 8,9 |
| [[coevolution-analysis|Coevolution Analysis]] | method | 0.73 | 9 |
| [[casp|CASP]] | concept | 0.75 | 9,10 |
| [[lddt-score|lDDT Score]] | concept | 0.73 | 10 |
| [[rosetta|Rosetta]] | tool | 0.72 | 9 |
| [[alphafold1|AlphaFold (v1)]] | model | 0.72 | 9 |
| [[alpha-helix|Alpha Helix]] | biological_entity | 0.68 | 8 |
| [[beta-sheet|Beta Sheet]] | biological_entity | 0.68 | 8 |
| [[protein-design|Protein Design]] | application | 0.78 | 11 |
| [[zero-shot-fitness-prediction|Zero-Shot Fitness Prediction]] | application | 0.78 | 11 |

## Key Relationships

```
protein --> protein-structure (HAS_PART)
protein --> protein-sequence (REPRESENTED_BY)
alphafold2 --> evoformer (HAS_PART)
alphafold2 --> multiple-sequence-alignment (USES)
alphafold2 --> attention-mechanism (USES)
alphafold2 --> protein-structure (PRODUCES)
alphafold2 --> alphafold1 (PRECEDED_BY)
evoformer --> attention-mechanism (USES)
evoformer --> multiple-sequence-alignment (APPLIED_TO)
coevolution-analysis --> multiple-sequence-alignment (APPLIED_TO)
coevolution-analysis --> contact-map (PRODUCES)
esm2 --> protein-sequence (LEARNS_FROM)
esm2 --> masked-language-modeling (USES)
esm2 --> zero-shot-fitness-prediction (ENABLES)
esm2 --> protein-design (ENABLES)
```

## Narrative

Lectures 8â€“9 establish the biological context and traditional computational approaches to protein structure. Lecture 8 defines the levels of protein structure (primary, secondary, tertiary) and contact maps as key intermediate representations. Lecture 9 covers coevolution analysis and Rosetta as pre-deep-learning benchmarks, building toward AlphaFold.

Lecture 10 introduces [[alphafold2]], the dominant model. Its key innovations are the Evoformer (joint MSA + pairwise representation processing) and the structure module. The lDDT score measures prediction accuracy per residue.

Lecture 11 pivots to protein language models â€” [[esm2]] specifically â€” which learn structural information from sequences alone through masked language modeling, without explicit evolutionary information. This enables zero-shot fitness prediction and protein design.

## Related Clusters

- [[cluster-map-deep-learning]] â€” Attention mechanism, Transformer
- [[cluster-map-genomics-ml]] â€” DNA language models (analogous to protein LMs)
- [[cluster-map-sequence-analysis]] â€” MSA, coevolution
