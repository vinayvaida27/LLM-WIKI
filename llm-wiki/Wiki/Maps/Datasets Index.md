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
  - "Datasets Index"
  - "Resources Index"
---

# Datasets Index

> [!info] Benchmark datasets, large-scale resources, and data repositories referenced in MLCB lectures.

## Protein Structure

| Dataset | Lectures | Size / Content |
|---|---|---|
| [[pdb|Protein Data Bank (PDB)]] | 8,9,10 | ~220K+ experimentally determined 3D structures |
| [[casp|CASP]] | 9,10 | Biennial blind test: ~100 targets with held-out structures |
| UniRef50 / UniRef90 | 11 | Sequence databases used to pre-train ESM-2 (~250M sequences) |

## Genomics

| Dataset | Lectures | Content |
|---|---|---|
| [[encode|ENCODE]] | 6,18 | ChIP-seq, ATAC-seq, TF binding across 100s of cell types |
| GTEx | 17,18 | eQTL maps across 50+ human tissues (~1000 donors) |

## Genetics / GWAS

| Dataset | Lectures | Content |
|---|---|---|
| UK Biobank | 17,18 | ~500K participants; genotype + phenotype; GWAS summary stats for 100s of traits |
| dbSNP | 17 | NCBI database of all cataloged human SNPs |
| 1000 Genomes Project | 17 | Sequenced 2,504 individuals from 26 populations; global LD reference |

## Drug Discovery / Chemistry

| Dataset | Lectures | Content |
|---|---|---|
| ChEMBL | 13,14 | Bioactivity database: molecules + experimental activity data |
| ZINC | 13,14 | ~750M commercially available chemical compounds |
| PubChem | 13 | Chemical substance and bioactivity database |

## Benchmarks

| Benchmark | Lectures | Used For |
|---|---|---|
| [[casp|CASP]] | 9,10 | Protein structure prediction |
| ProteinGym | 11 | Zero-shot protein fitness prediction from LMs |
| MoleculeNet | 14 | Standard drug property prediction benchmark (ADMET tasks) |
| GLUE / SuperGLUE (analogy) | 12 | Downstream genomics task benchmarks analogous to NLP benchmarks |

## Navigation

[[Course Graph Map]] Â· [[Tools and Databases Index]] Â· [[Methods Index]]
