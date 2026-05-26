---
tags:
  - "topic"
  - "map"
  - "cluster"
topics:
  - "MLCB"
status: "generated"
created: 2026-05-25
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_04_alignment.md"
  - "Raw/Sources/lecture_05_epigenomics_hmms.md"
  - "Raw/Sources/lecture_09_protein_folding_algorithms.md"
  - "Raw/Sources/lecture_10_protein_structure_with_transformers.md"
source_count: 4
aliases:
  - "Sequence Analysis Cluster"
  - "Alignment Cluster"
---

# Cluster Map â€” Sequence Analysis

> [!info] Entities in the Sequence Analysis cluster. Primary lectures: 4, 5. Related: [[cluster-map-genomics]], [[cluster-map-classical-ml]], [[cluster-map-protein]].

## Cluster Overview

| Property | Value |
|---|---|
| Cluster ID | sequence-analysis |
| Primary lectures | 4, 5 |
| Supporting lectures | 9, 11 |
| Core theme | Classical algorithms for comparing and annotating biological sequences |

## Entities in This Cluster

| Entity | Type | Lectures |
|---|---|---|
| [[sequence-alignment|Sequence Alignment]] | method | 4 |
| [[hidden-markov-model|Hidden Markov Model]] | method | 5 |
| [[dna-sequence|DNA Sequence]] | data_type | 4,5,12 |
| [[protein-sequence|Protein Sequence]] | data_type | 11 |
| [[multiple-sequence-alignment|MSA]] | data_type | 9,10 |
| [[dna|DNA]] | biological_entity | 1,4,5,12,17 |

## Key Relationships

```
sequence-alignment --APPLIED_TO--> dna-sequence
sequence-alignment --APPLIED_TO--> protein-sequence
hidden-markov-model --APPLIED_TO--> dna-sequence
hidden-markov-model --PRODUCES--> chromatin (chromatin state annotations)
multiple-sequence-alignment --USES--> sequence-alignment
multiple-sequence-alignment --ENABLES--> alphafold2
```

## Conceptual Summary

Sequence analysis covers the classical algorithmic layer of computational biology â€” before deep learning, most genomics pipelines used dynamic programming and probabilistic models:

- **Sequence alignment** (Lecture 4): Needleman-Wunsch (global) and Smith-Waterman (local) dynamic programming; also BLAST for heuristic database search
- **Hidden Markov Models** (Lecture 5): profile HMMs for sequence family modeling; multivariate HMMs for chromatin state annotation (ChromHMM)
- **MSA** (Lecture 9, 10): critical input to AlphaFold2's Evoformer; summarizes evolutionary covariation

## Scoring Matrices

Substitution matrices ([[scoring-matrix|BLOSUM62]], PAM) encode evolutionary distances between amino acids and are used in alignment scoring.

## Bridge to Other Clusters

- DNA sequence connects to [[cluster-map-genomics]] (expression, SNPs) and [[cluster-map-genomics-ml]] (DNABERT, nucleotide LMs)
- Protein sequence connects to [[cluster-map-protein]] (AlphaFold2, ESM-2)
- HMMs connect to [[cluster-map-epigenomics]] (ChromHMM chromatin state annotation)

## Navigation

[[knowledge-graph-index]] Â· [[cluster-map-classical-ml]] Â· [[cluster-map-genomics]] Â· [[cluster-map-protein]] Â· [[lecture-entity-map]]
