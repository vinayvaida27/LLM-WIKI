---
tags:
  - "concept"
topics:
  - "MLCB"
status: updated
created: 2026-05-24
updated: 2026-05-24
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
  - "GNN Message Passing"
---

# GNN Message Passing

## Equation

`	ext
h_v^(k+1) = update(h_v, aggregate(messages from neighbors))
`

## Variables
Variables should be interpreted in the linked lecture context. If a symbol is not clearly defined in the available source, do not invent a definition.

## Meaning
This formalism captures a course-level computational idea used to model biological data.

## Where It Appears
See the lecture pages and [[mlcb-methods-map]].

## Biological Interpretation
The equation helps transform biological data into scores, probabilities, representations, or updates.

## Computational Interpretation
It defines how evidence is combined or optimized.

## Common Confusions
The equation is a model abstraction, not the biological mechanism itself.

## Graph Links

### Parent Topics
- [[topic-epigenomics|Epigenomics]]
