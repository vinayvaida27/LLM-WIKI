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
  - "Models Index"
  - "Architecture Index"
---

# Models Index

> [!info] All neural network architectures, pre-trained models, and computational model systems in the MLCB knowledge graph. 13 models total.

## Protein Structure Models

| Model | Lectures | What It Does |
|---|---|---|
| [[alphafold2|AlphaFold2]] | 10 | Protein structure prediction; near-experimental accuracy on CASP14 |
| [[evoformer|Evoformer]] | 10 | Core attention module of AlphaFold2; processes MSA + pair representations |
| [[alphafold1|AlphaFold1]] | 9 | Earlier AlphaFold version; covariation-based structure prediction |
| [[rosetta|Rosetta]] | 9 | Physics + knowledge-based protein structure and design |

## Protein Language Models

| Model | Lectures | What It Does |
|---|---|---|
| [[esm2|ESM-2]] | 11 | Transformer protein language model trained on UniRef; zero-shot fitness prediction |

## DNA / Genomic Language Models

| Model | Lectures | What It Does |
|---|---|---|
| [[dnabert|DNABERT]] | 12 | BERT-style model on DNA k-mers; genomic sequence understanding |
| [[nucleotide-transformer|Nucleotide Transformer]] | 12 | Large-scale nucleotide LM; multiple genome pre-training |
| [[hyena|Hyena]] | 12 | Long-range convolution-based alternative to transformers for DNA |

## Drug Discovery Models

| Model | Lectures | What It Does |
|---|---|---|
| [[dimenet|DimeNet]] | 14 | Directional message passing GNN for 3D molecular geometry |

## General Architectures (used across many models)

| Architecture | Lectures | Role |
|---|---|---|
| [[transformer|Transformer]] | 10, 11, 12 | Self-attention backbone; underlies AlphaFold2, ESM-2, DNABERT |

## Pre-training Methods Shared Across Models

| Method | Used By |
|---|---|
| [[masked-language-modeling|Masked Language Modeling (MLM)]] | ESM-2, DNABERT, Nucleotide Transformer |
| [[self-supervised-learning|Self-Supervised Learning]] | All LM-based models |
| [[transfer-learning|Transfer Learning]] | All fine-tuned models |

## Key Design Choices

| Choice | Models |
|---|---|
| Attention over MSA rows | AlphaFold2 Evoformer |
| Attention over residue pairs | AlphaFold2 Evoformer |
| Token = single amino acid | ESM-2 |
| Token = k-mer (6-mer) | DNABERT |
| Token = single nucleotide | Nucleotide Transformer |

## Navigation

[[Course Graph Map]] Â· [[Methods Index]] Â· [[cluster-map-protein]] Â· [[cluster-map-deep-learning]] Â· [[cluster-map-genomics-ml]]
