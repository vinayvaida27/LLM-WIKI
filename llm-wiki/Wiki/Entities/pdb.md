---
tags:
  - "entity"
topics:
  - "MLCB"
status: "updated"
created: 2026-05-24
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_08_intro_to_protein_structure.md"
  - "Raw/Sources/lecture_09_protein_folding_algorithms.md"
  - "Raw/Sources/lecture_10_protein_structure_with_transformers.md"
source_count: 3
aliases:
  - "PDB"
  - "Protein Data Bank"
  - "RCSB PDB"
entity_type: "tool"
lectures:
  - "lecture-08"
  - "lecture-09"
  - "lecture-10"
---

# Protein Data Bank (PDB)

The Protein Data Bank (PDB) is the primary worldwide repository for experimentally determined 3D structures of proteins, nucleic acids, and their complexes. Structures are deposited after determination by X-ray crystallography, NMR, or cryo-EM.

## Role in MLCB

In Lectures 8â€“10, PDB appears as:
- The **training and evaluation dataset** for protein structure prediction models
- The source of ground-truth structures for benchmarking [[alphafold2|AlphaFold2]]
- A key resource for understanding [[protein-structure|protein structure]] representations

## Key Facts

| Property | Value |
|---|---|
| Founded | 1971 |
| Current entries | ~220,000+ structures |
| Primary format | PDB / mmCIF |
| Curators | RCSB (US), PDBe (Europe), PDBj (Japan) |

## Limitations Addressed by AlphaFold2

Prior to 2021, PDB coverage was sparse for protein families with no close homologs â€” AlphaFold2 shifted prediction away from template-based methods that relied on PDB lookups.


## Graph Links

### Parent Topics
- [[topic-sequence-alignment|Sequence Alignment]]

## Related

[[alphafold2]], [[protein-structure]], [[multiple-sequence-alignment]], [[protein-sequence]], [[protein]]
