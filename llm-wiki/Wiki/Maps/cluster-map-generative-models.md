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
  - "Raw/Sources/lecture_15_generating_new_molecules.md"
source_count: 1
aliases:
  - "Generative Models Cluster"
  - "Molecule Generation Cluster"
---

# Cluster Map â€” Generative Models

> [!info] Entities in the Generative Models cluster. Primary lectures: 15. Related: [[cluster-map-drug-discovery]], [[cluster-map-deep-learning]].

## Cluster Overview

| Property | Value |
|---|---|
| Cluster ID | generative-models |
| Primary lectures | 15 |
| Supporting lectures | 2, 11 |
| Core theme | Latent-space generative models for molecule and sequence design |

## Entities in This Cluster

| Entity | Type | Lectures |
|---|---|---|
| [[variational-autoencoder|Variational Autoencoder]] | method | 15 |
| [[diffusion-model|Diffusion Model]] | method | 15 |
| [[latent-space|Latent Space]] | concept | 1,2,11,15 |
| [[small-molecule|Small Molecule]] | biological_entity | 13,14,15 |
| [[smiles|SMILES]] | data_type | 14 |
| [[molecular-graph|Molecular Graph]] | data_type | 14 |

## Key Relationships

```
variational-autoencoder --LEARNS_FROM--> gene-expression-matrix
variational-autoencoder --PRODUCES--> latent-space
diffusion-model --APPLIED_TO--> small-molecule
diffusion-model --EXTENDS--> variational-autoencoder
latent-space --REPRESENTED_BY--> smiles
```

## Conceptual Summary

Generative models learn a compressed **latent space** from data, then sample from it to produce novel outputs. In MLCB Lecture 15, this is applied to drug molecule generation:

- A **VAE** encodes molecules (as SMILES or graphs) into a continuous latent space; decoding samples produces new candidate molecules
- A **diffusion model** learns to reverse a noise-addition process, iteratively refining molecule structure from random noise
- Both approaches rely on the molecule's graph or string representation and evaluate candidates by predicted bioactivity

## Bridge to Other Clusters

- Generation targets come from [[cluster-map-drug-discovery]] (small molecules, protein targets)
- Architecture (attention, embeddings) comes from [[cluster-map-deep-learning]]
- Sequence generation overlaps with [[cluster-map-genomics-ml]]

## Navigation

[[knowledge-graph-index]] Â· [[cluster-map-drug-discovery]] Â· [[cluster-map-deep-learning]] Â· [[lecture-entity-map]]
