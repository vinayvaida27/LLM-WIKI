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
  - "Raw/Sources/lecture_05_epigenomics_hmms.md"
source_count: 1
aliases:
  - "Chromatin State"
  - "Epigenomic State"
  - "Chromatin Annotation"
---

# Chromatin State

> [!info] Canonical page: [[chromatin|Chromatin]]
> "Chromatin state" is a specific computational characterization of chromatin, documented within the Chromatin page.

A chromatin state is a discrete annotation label assigned to each genomic position based on a combination of histone modification ChIP-seq signals. Tools like [[chromhmm|ChromHMM]] learn these states from data using a multivariate HMM.

**Common chromatin states (ChromHMM 15-state model):**
- Active TSS (TssA)
- Flanking active TSS (TssAFlnk)
- Transcr. at gene 5' and 3' (TxFlnk)
- Strong transcription (Tx)
- Weak transcription (TxWk)
- Enhancer (Enh)
- Genic enhancers (EnhG)
- ZNF genes & repeats (ZNF/Rpts)
- Heterochromatin (Het)
- Bivalent/Poised TSS (TssBiv)
- Flanking Bivalent TSS (BivFlnk)
- Bivalent Enhancer (EnhBiv)
- Repressed PolyComb (ReprPC)
- Weak Repressed PolyComb (ReprPCWk)
- Quiescent/Low (Quies)

**Canonical page:** [[chromatin]]

**Related:** [[chromhmm]], [[histone-modification]], [[chip-seq]], [[atac-seq]], [[epigenomics-and-hidden-markov-models]]

## Graph Links

### Parent Topics
- [[topic-epigenomics|Epigenomics]]
