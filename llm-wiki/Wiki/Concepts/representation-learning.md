---
tags:
  - "concept"
topics:
  - "MLCB"
status: "updated"
created: 2026-05-24
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_01_course_introduction.md"
source_count: 1
aliases:
  - "representation learning"
  - "representation-learning"
  - "Representation Learning"
  - "Feature Learning"
  - "Learned Embeddings"
---

# Representation Learning

## Overview
Representation learning is the course-wide idea that raw inputs become useful only after they are converted into learned internal features. Lecture 1 introduces this with images, genomes, graphs, language, proteins, chemicals, and scientific knowledge. The model is not merely matching a surface pattern; it is building intermediate representations that make a downstream task easier.

## Plain-English Intuition
Think of representation learning as automatic feature building. Instead of a human saying "look for this exact motif" or "use this exact molecular descriptor," the model learns useful patterns from data. In an image, early layers may learn edges and later layers learn objects. In a genome, early patterns may correspond to bases or motifs and later patterns may correspond to regulatory logic.

## Why It Matters in MLCB
MLCB repeatedly asks how to turn messy biology into computable structure. [[representation-learning]] is the common bridge:
- [[dna|DNA]] sequence can become motif and regulatory-element features.
- [[molecule|Molecules]] can become graph embeddings.
- [[protein|Proteins]] can become sequence, structure, or function embeddings.
- Disease and literature knowledge can become latent maps for hypothesis generation.

## Biological Context
Biological data often has hidden structure. A DNA sequence is not just a string; it can encode binding sites, regulatory grammar, and cell-type-specific function. A molecule is not just a formula; it has atoms, bonds, neighborhoods, and physicochemical behavior. Representation learning matters because much of the biological signal is distributed across these patterns.

## Computational Context
Lecture 1 describes the input-output path as raw input `X`, learned latent representation `Z`, and output `Y`. The `Z` space is where models organize the hidden structure they learned. This connects directly to [[latent-space]], [[self-supervised-learning]], [[graph-neural-networks]], [[attention-mechanism]], [[transformer|Transformer]], [[protein-structure-and-biological-language-models]], and later DNA language models.

## Where It Appears in the Lectures
- [[lecture-01-course-introduction]] - course framing, images, genomes, graphs, language models, and latent spaces.
- [[lecture-10-protein-structure-with-transformers]] - attention-based representations for protein structure.
- [[lecture-11-protein-language-models]] - protein sequence embeddings.
- [[lecture-12-dna-language-models]] - DNA sequence embeddings.
- [[lecture-14-chemistry-gnns]] - molecular graph representations.
- [[lecture-15-generating-new-molecules]] - latent spaces for molecule generation.

## Detailed Explanation
### Images to Genomes
The lecture starts with a familiar image example: raw pixels become edges, shapes, and objects. It then maps the same idea onto genomics. Bases can be encoded so a model can learn motifs and sequence patterns that influence gene regulation.

### Graphs and Molecules
For molecules, the representation must respect graph structure. A [[graph-neural-networks|Graph Neural Network]] begins with atom properties and repeatedly aggregates neighborhood information. This turns local chemical context into a richer molecular representation.

### Language and Context
Language models show why context matters. A token representation changes depending on nearby tokens. Lecture 1 uses this to motivate later biological sequence models, where amino acids or DNA tokens also need context-dependent representations.

## Important Examples
- CNN-like motif detection in genomic sequence.
- GNN representation of atoms, bonds, and molecular neighborhoods.
- LLM embeddings that place words with similar contexts close together.
- Two-dimensional visualization of high-dimensional latent spaces using t-SNE or UMAP.


## Graph Links

### Parent Topics
- [[topic-single-cell-analysis|Single-cell Analysis]]

## Related Concepts
- [[self-supervised-learning]]
- [[latent-space]]
- [[multimodal-foundation-models]]
- [[graph-neural-networks]]
- [[attention-mechanism]]
- [[drug-discovery-and-molecular-generation|drug discovery]]

## Common Confusions
Representation learning is not proof of mechanism by itself. A learned feature can be predictive without being biologically causal. MLCB therefore connects representation learning to source data, validation, perturbation, and biological interpretation.

## Summary
Representation learning is the main computational bridge in Lecture 1: raw biological inputs become learned features, learned features support prediction or generation, and the scientist must then interpret the result biologically.
