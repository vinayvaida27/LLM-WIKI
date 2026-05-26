---
tags:
  - "entity"
topics:
  - "MLCB"
status: "compiled"
created: 2026-05-24
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_05_epigenomics_hmms.md"
  - "Raw/Sources/lecture_06_regulatory_circuitry.md"
source_count: 2
aliases:
  - "Chromatin"
  - "Chromatin Structure"
  - "Chromatin Organization"
entity_type: "biological_entity"
importance: "0.82"
lectures:
  - "lecture-05"
  - "lecture-06"
---

# Chromatin

**Chromatin** is the complex of DNA and proteins (primarily histones) that packages the genome inside the cell nucleus. It is the physical substrate on which epigenomic regulation operates.

## Structure (Lecture 5)

The human genome is 2 meters of DNA per cell. To fit inside the nucleus, DNA is wrapped around **nucleosomes** â€” units of 8 histone proteins (2Ã— H2A, H2B, H3, H4) with ~200 bp of DNA wrapped around each. This creates the "beads-on-a-string" structure that can be further compacted.

```
DNA â†’ Nucleosome (200 bp + 8 histones) â†’ 30nm fiber â†’ Loop domains â†’ Chromosome
```

## Chromatin Accessibility

Not all chromatin is equally packed. **Open chromatin** (nucleosome-free or nucleosome-depleted regions) is accessible to transcription factors and the transcription machinery. Measured by:

- **[[chip-seq|ChIP-seq]]** â€” maps histone modifications or TF binding
- **[[atac-seq|ATAC-seq]]** â€” maps nucleosome-free (accessible) regions

## Three Layers of Epigenomic Modification (Lecture 5)

1. **Compaction / accessibility** â€” whether a region is physically packed or open
2. **DNA methylation** â€” methyl groups added to cytosine at CpG sites; blocks some TF binding
3. **Histone modifications** â€” chemical tags on histone tails (acetylation, methylation, phosphorylation) that act as "landing pads" for regulatory proteins

## Chromatin States

A **chromatin state** is a discrete label assigned to each genomic position based on combinations of histone mark ChIP-seq signals. [[chromhmm|ChromHMM]] uses a multivariate HMM to jointly learn these states across multiple marks and cell types.

The standard 15-state ChromHMM model (Lecture 5) distinguishes:
- Active TSS (TssA) â€” high H3K4me3
- Active enhancers (Enh) â€” high H3K4me1, H3K27ac
- Strong transcription (Tx) â€” high H3K36me3
- Heterochromatin (Het) â€” high H3K9me3
- Repressed Polycomb (ReprPC) â€” high H3K27me3
- Bivalent TSS (TssBiv) â€” co-occurrence of H3K4me3 and H3K27me3 (poised genes)
- Quiescent (Quies) â€” no marks

See [[chromatin-state]] for the full 15-state annotation.

## Cell Type Specificity

The same genomic position can have different chromatin states in different cell types. An enhancer active in a liver cell may be quiescent in a neuron. This cell-type-specific epigenomic landscape is why disease-associated [[snp|SNPs]] can only be understood in the relevant tissue.


## Graph Links

### Parent Topics
- [[topic-epigenomics|Epigenomics]]

## Related

[[histone-modification]], [[chip-seq]], [[atac-seq]], [[chromatin-state]], [[enhancer]], [[transcription-factor]], [[chromhmm]], [[epigenomics-and-hidden-markov-models]]
