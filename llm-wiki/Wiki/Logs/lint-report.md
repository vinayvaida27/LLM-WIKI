---
tags:
  - "log"
topics:
  - "MLCB"
status: "updated"
created: 2026-05-24
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_01_course_introduction.md"
  - "Raw/Sources/lecture_02_expression_analysis_and_clustering.md"
  - "Raw/Sources/lecture_03_single_cell_analysis.md"
  - "Raw/Sources/lecture_04_alignment.md"
  - "Raw/Sources/lecture_05_epigenomics_hmms.md"
  - "Raw/Sources/lecture_06_regulatory_circuitry.md"
  - "Raw/Sources/lecture_07_regulatory_networks.md"
  - "Raw/Sources/lecture_08_intro_to_protein_structure.md"
  - "Raw/Sources/lecture_09_protein_folding_algorithms.md"
  - "Raw/Sources/lecture_10_protein_structure_with_transformers.md"
  - "Raw/Sources/lecture_11_protein_language_models.md"
  - "Raw/Sources/lecture_12_dna_language_models.md"
  - "Raw/Sources/lecture_13_drug_development_intro.md"
  - "Raw/Sources/lecture_14_chemistry_gnns.md"
  - "Raw/Sources/lecture_15_generating_new_molecules.md"
  - "Raw/Sources/lecture_16_training_neural_networks.md"
  - "Raw/Sources/lecture_17_genetics_disease_gwas_prs_mechanism.md"
  - "Raw/Sources/lecture_18_disease_mechanism_circuitry_eqtls_heritability.md"
source_count: 18
aliases:
  - "lint report"
  - "Lint Report"
  - "lint-report"
---

# Lint Report

## Checks Planned
- Missing index links
- Broken Obsidian links
- Orphan pages
- Very short pages
- Missing frontmatter
- Missing source paths
- Missing lecture references
- Equations without definitions
- Figures without explanation
- Catalog entries missing
- Pages needing manual review

## Preliminary Findings
Lecture pages include source paths and review questions. Entity pages include related page references. Figure detail needs manual improvement because source images are not embedded.

## Final Tool Results
## [2026-05-24 16:03] Deep Update Batch Check
- `python scripts/wiki_tool.py build`: passed; catalog rebuilt with 89 Wiki notes.
- `python scripts/wiki_tool.py lint`: passed with warnings only.
- `python scripts/wiki_tool.py source-lint`: passed; 18 Raw sources checked.
- `python scripts/chunk_sources.py`: passed; rebuilt 2082 Wiki chunks and 981 Raw chunks.
- Query smoke test: `representation learning self supervised latent space Lecture 1` returned the new concept pages as top catalog results.

## Remaining Warnings
The lint warnings are broad source-attribution warnings on existing all-course notes and the master topic map. They are warnings, not failures. The new first-batch concept and comparison pages cite only `Raw/Sources/lecture_01_course_introduction.md`.

## [2026-05-24 16:20] Graph Hygiene Check
- Removed three low-value duplicate entity nodes: `attention`, `graph-neural-network`, and `drug-discovery`.
- Repointed links to stronger canonical pages: `attention-mechanism` / `attention-equation`, `graph-neural-networks`, and `drug-discovery-and-molecular-generation`.
- `python scripts/wiki_tool.py build`: passed; catalog rebuilt with 86 Wiki notes.
- `python scripts/wiki_tool.py lint`: passed with warnings only.
- `python scripts/wiki_tool.py source-lint`: passed; 18 Raw sources checked.
- `python scripts/chunk_sources.py`: passed; rebuilt 2066 Wiki chunks and 981 Raw chunks.

## Graph Connections
- [[knowledge-graph-index]]
- [[mlcb-cross-lecture-connections]]
- [[mlcb-2024-computational-biology]]
