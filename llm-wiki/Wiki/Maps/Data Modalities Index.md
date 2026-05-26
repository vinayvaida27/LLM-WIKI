---
tags:
  - "topic"
  - "map"
  - "index"
topics:
  - "MLCB"
status: "curated"
created: 2026-05-25
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
  - "Data Modalities Index"
  - "Data Types Index"
---

# Data Modalities Index

> [!info] All data types and representations in the MLCB knowledge graph. 14 data types.

## Genomics Data

| Data Type | Lectures | Format / Description |
|---|---|---|
| [[gene-expression-matrix|Gene Expression Matrix]] | 2,3 | Cells Ã— genes count matrix from RNA-seq |
| [[scrna-seq|scRNA-seq]] | 3 | Single-cell gene expression; sparse count matrix |
| [[dna-sequence|DNA Sequence]] | 4,5,12 | A/C/G/T string; genome or gene locus |

## Epigenomics Data

| Data Type | Lectures | Format / Description |
|---|---|---|
| [[histone-modification|Histone Modification Signals]] | 5 | ChIP-seq read coverage per histone mark |

## Protein Data

| Data Type | Lectures | Format / Description |
|---|---|---|
| [[protein-sequence|Protein Sequence]] | 11 | Amino acid string (FASTA); primary structure |
| [[multiple-sequence-alignment|MSA]] | 9,10 | Aligned protein sequences across species; L Ã— N_seq matrix |
| [[contact-map|Contact Map]] | 9,10 | Binary matrix: residue pairs within 8Ã… in 3D space |

## Chemical / Drug Data

| Data Type | Lectures | Format / Description |
|---|---|---|
| [[smiles|SMILES]] | 14 | Simplified Molecular Input Line Entry System string |
| [[selfies|SELFIES]] | 14 | Self-referencing embedded strings; grammar-guaranteed valid molecules |
| [[molecular-graph|Molecular Graph]] | 14 | Atoms as nodes, bonds as edges; input to MPNNs |

## Genetic Variation Data

| Data Type | Lectures | Format / Description |
|---|---|---|
| [[snp|SNP Array Data]] | 17 | Binary allele calls at ~1M known SNP positions per individual |

## Structural Data

| Data Type | Lectures | Format / Description |
|---|---|---|
| [[contact-map|Contact Map]] | 9,10 | Pairwise residue distance/contact encoding |

## Key Representation Choices

| Biological entity | Common computational representation |
|---|---|
| DNA sequence | k-mer tokenization (DNABERT) or single-nucleotide (NT) |
| Protein sequence | Single amino acid token (ESM-2) |
| Protein structure | Contact map â†’ 3D coordinates (AlphaFold2) |
| Small molecule | SMILES string OR molecular graph |
| Gene expression | Count matrix â†’ log-normalized â†’ PCA/UMAP embedding |
| Genetic variant | Binary allele encoding per individual |

## Navigation

[[Course Graph Map]] Â· [[Methods Index]] Â· [[Biological Entities Index]] Â· [[Models Index]]
