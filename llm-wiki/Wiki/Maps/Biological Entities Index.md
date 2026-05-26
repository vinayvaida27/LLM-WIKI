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
  - "Biological Entities Index"
  - "Biology Index"
---

# Biological Entities Index

> [!info] All biological entities (molecules, genes, genomic features, cellular structures) in the MLCB knowledge graph. 18 biological entities.

## Nucleic Acids and Sequences

| Entity | Lectures | Description |
|---|---|---|
| [[dna|DNA]] | 1,4,5,12,17 | Deoxyribonucleic acid; the genome |
| [[rna|RNA]] | 1,2,3 | Ribonucleic acid; transcribed from DNA |
| [[gene|Gene]] | 1,2,6,7 | A genomic locus encoding a functional product |

## Proteins

| Entity | Lectures | Description |
|---|---|---|
| [[protein|Protein]] | 8,9,10,11 | Polymer of amino acids; the primary functional molecule |
| [[amino-acid|Amino Acid]] | 8,9,11 | Monomer of proteins; 20 canonical types |

## Genomic Regulatory Features

| Entity | Lectures | Description |
|---|---|---|
| [[enhancer|Enhancer]] | 6,17,18 | Non-coding regulatory element that increases transcription |
| [[promoter|Promoter]] | 6 | Proximal regulatory element where transcription initiates |
| [[transcription-factor|Transcription Factor]] | 6,7 | Protein that binds DNA motifs to regulate gene expression |
| [[chromatin|Chromatin]] | 5,6 | DNA + histone complex packaging the genome |
| [[histone-modification|Histone Modification]] | 5 | Chemical tags on histone tails encoding chromatin state |

## Genetic Variation

| Entity | Lectures | Description |
|---|---|---|
| [[snp|SNP]] | 17,18 | Single nucleotide polymorphism; most common genetic variant |

## Drug Molecules

| Entity | Lectures | Description |
|---|---|---|
| [[small-molecule|Small Molecule]] | 13,14,15 | Low-molecular-weight organic drug candidate |

## Defined by Biological Context

> These entities appear in the course as primary computational inputs or prediction targets.

| Entity | Context |
|---|---|
| [[dna|DNA]] | Sequence input to alignment, HMM annotation, genomic LMs |
| [[rna|RNA]] | RNA-seq count data; mRNA as transcribed product |
| [[protein|Protein]] | 3D structure prediction target; language model sequence |
| [[snp|SNP]] | GWAS test unit; PRS input; eQTL entity |
| [[enhancer|Enhancer]] | Disease variant location; TF binding site; ChIP-seq peak |
| [[small-molecule|Small Molecule]] | Drug generation target; GNN node set; docking ligand |

## Navigation

[[Course Graph Map]] Â· [[Methods Index]] Â· [[Data Modalities Index]] Â· [[Tools and Databases Index]]
