---
tags:
  - "entity"
  - "redirect"
topics:
  - "MLCB"
status: "redirect"
created: 2026-05-24
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_10_protein_structure_with_transformers.md"
source_count: 1
aliases:
  - "AlphaFold"
  - "AlphaFold2"
  - "AlphaFold 2"
---

# AlphaFold

> [!info] Canonical page: [[alphafold2|AlphaFold2]]
> The MLCB course covers AlphaFold2 specifically (the 2021 version). KG entity ID is `alphafold2`.

AlphaFold2 is DeepMind's deep learning system for protein structure prediction, published in Nature 2021 (Jumper et al.). It achieved near-experimental accuracy on CASP14 benchmarks and effectively solved the protein folding problem for single-chain proteins.

Key architectural components (Lecture 10):
- **[[evoformer|Evoformer]]** â€” the core module processing MSA and pair representations
- **[[multiple-sequence-alignment|MSA]]** â€” multiple sequence alignment as primary input
- **[[attention-mechanism|Attention]]** â€” row-wise and column-wise attention over MSA matrix
- **Structure module** â€” equivariant frame-based prediction of 3D coordinates

**Canonical page:** [[alphafold2]]

**Related:** [[evoformer]], [[multiple-sequence-alignment]], [[protein-structure]], [[transformer]], [[attention-mechanism]], [[protein]]

## Graph Links

### Parent Topics
- [[topic-sequence-alignment|Sequence Alignment]]
