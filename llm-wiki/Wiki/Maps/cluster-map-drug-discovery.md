---
tags:
  - "topic"
  - "map"
  - "knowledge-graph"
  - "drug-discovery"
  - "chemistry"
topics:
  - "MLCB"
  - "drug discovery"
  - "chemistry"
status: "generated"
created: 2026-05-25
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_13_drug_development_intro.md"
  - "Raw/Sources/lecture_14_chemistry_gnns.md"
  - "Raw/Sources/lecture_15_generating_new_molecules.md"
source_count: 3
aliases:
  - "Drug Discovery Cluster Map"
  - "Chemistry Cluster Map"
---

# Cluster Map: Drug Discovery and Chemistry

> Lectures 13â€“15 | Module 3

## Entities in this Cluster

| Entity | Type | Importance | Lectures |
|---|---|---|---|
| [[drug-discovery|Drug Discovery]] | application | 0.90 | 13,14,15 |
| [[small-molecule|Small Molecule]] | biological_entity | 0.85 | 13,14,15 |
| [[molecular-graph|Molecular Graph]] | data_type | 0.85 | 14 |
| [[message-passing-neural-network|MPNN]] | method | 0.85 | 14 |
| [[variational-autoencoder|VAE]] | method | 0.85 | 15 |
| [[diffusion-model|Diffusion Model]] | method | 0.82 | 15 |
| [[smiles|SMILES]] | data_type | 0.82 | 14 |
| [[drug-target|Drug Target]] | biological_entity | 0.80 | 13 |
| [[admet|ADMET]] | concept | 0.78 | 13 |
| [[selfies|SELFIES]] | data_type | 0.75 | 14 |
| [[virtual-screening|Virtual Screening]] | method | 0.75 | 13 |
| [[reinforcement-learning-drug|RL for Drug Design]] | method | 0.75 | 15 |
| [[normalizing-flow|Normalizing Flow]] | method | 0.72 | 15 |
| [[molecular-docking|Molecular Docking]] | method | 0.75 | 13 |
| [[schnet|SchNet]] | model | 0.68 | 14 |
| [[dimenet|DimeNet]] | model | 0.68 | 14 |
| [[inchi|InChI]] | data_type | 0.65 | 14 |

## Molecular Representations Comparison

| Representation | Format | Unique? | Valid always? | 3D? |
|---|---|---|---|---|
| SMILES | String | No | No | No |
| SMARTS | Pattern string | â€” | â€” | No |
| SELFIES | String | No | **Yes** | No |
| InChI | String | **Yes** | Yes | No |
| Molecular Graph | Graph | â€” | Yes | Optional |

## Key Relationships

```
small-molecule --> smiles (REPRESENTED_BY)
small-molecule --> molecular-graph (REPRESENTED_BY)
selfies --> smiles (EXTENDS)
message-passing-neural-network --> molecular-graph (APPLIED_TO)
message-passing-neural-network --> drug-discovery (ENABLES)
schnet --> message-passing-neural-network (IS_A)
dimenet --> message-passing-neural-network (EXTENDS)
variational-autoencoder --> latent-space (PRODUCES)
variational-autoencoder --> small-molecule (PRODUCES)
variational-autoencoder --> elbo (BASED_ON)
diffusion-model --> small-molecule (PRODUCES)
virtual-screening --> molecular-docking (USES)
molecular-docking --> drug-target (APPLIED_TO)
reinforcement-learning-drug --> drug-discovery (ENABLES)
```

## Narrative

### Lecture 13 â€” Drug Discovery Pipeline

The drug discovery process spans target identification â†’ hit finding â†’ lead optimization â†’ ADMET filtering â†’ clinical trials. [[virtual-screening|Virtual screening]] and [[molecular-docking|docking]] enable computational hit finding across large libraries.

### Lecture 14 â€” GNNs for Chemistry

Small molecules are naturally represented as [[molecular-graph|molecular graphs]]. [[message-passing-neural-network|MPNNs]] learn molecular representations by iteratively aggregating neighbor features. [[schnet|SchNet]] adds 3D geometry via continuous-filter convolutions. [[dimenet|DimeNet]] adds bond-angle directional information.

Molecular strings ([[smiles|SMILES]], [[selfies|SELFIES]], [[inchi|InChI]]) have different trade-offs. SELFIES is preferred for generative models because every valid string decodes to a valid molecule.

### Lecture 15 â€” Generative Molecule Design

Three generative paradigms:
- **[[variational-autoencoder|VAE]]** â€” continuous latent space; gradient-based optimization toward desired properties.
- **[[diffusion-model|Diffusion Model]]** â€” noise-reversal; state-of-the-art 3D molecule generation.
- **[[reinforcement-learning-drug|RL]]** â€” policy gradient with reward from docking/ADMET to guide generation.

## Related Clusters

- [[cluster-map-deep-learning]] â€” Backprop, Adam, generative training
- [[cluster-map-protein]] â€” Drug targets are proteins; AlphaFold structures inform docking
- [[cluster-map-generative-models]] â€” VAE, diffusion, flows
