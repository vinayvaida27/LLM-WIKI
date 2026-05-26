---
tags:
  - "topic"
  - "map"
  - "knowledge-graph"
  - "genomics-ml"
  - "language-models"
topics:
  - "MLCB"
  - "DNA language models"
status: "generated"
created: 2026-05-25
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_12_dna_language_models.md"
source_count: 1
aliases:
  - "Genomic Language Models Map"
  - "DNA LM Map"
---

# Cluster Map: Genomic Language Models

> Lecture 12 | Module 2

## Entities in this Cluster

| Entity | Type | Importance | Architecture |
|---|---|---|---|
| [[dnabert|DNABERT]] | model | 0.82 | BERT + k-mer tokenization |
| [[nucleotide-transformer|Nucleotide Transformer]] | model | 0.78 | BERT, multi-species |
| [[hyena|HyenaDNA]] | model | 0.75 | Hyena (SSM-like, long context) |
| [[caduceus|Caduceus]] | model | 0.72 | Mamba SSM + RC equivariance |
| [[dna-sequence|DNA Sequence]] | data_type | 0.82 | â€” |

## Model Comparison

| Model | Context Window | Tokenization | RC equivariant | Key feature |
|---|---|---|---|---|
| DNABERT | 512 bp | k-mer (k=3â€“6) | No | First genomic BERT |
| Nucleotide Transformer | 6 kb | BPE on DNA | No | Multi-species pretraining |
| HyenaDNA | 1 Mbp | Single-character | No | Long-range via Hyena operators |
| Caduceus | 131 kbp | Single-character | **Yes** | Reverse-complement equivariant Mamba |

## Key Relationships

```
dnabert --> dna-sequence (LEARNS_FROM)
dnabert --> masked-language-modeling (USES)
dnabert --> transformer (IS_A)
nucleotide-transformer --> dna-sequence (LEARNS_FROM)
hyena --> dnabert (CONTRASTS_WITH)
caduceus --> hyena (EXTENDS)
dnabert --> transfer-learning (ENABLES)
```

## Design Challenges for DNA LMs

1. **Long-range dependencies** â€” regulatory elements can be megabases apart. Standard Transformers (quadratic attention) hit context limits around 1 kb. HyenaDNA and Caduceus address this with sub-quadratic operators.
2. **Reverse-complement symmetry** â€” DNA has two strands; a model should give the same result for a sequence and its reverse complement. Caduceus enforces this through equivariant design.
3. **Tokenization** â€” k-mer tokenization (DNABERT) creates vocabulary overlap issues; single-character tokenization (HyenaDNA) has simpler vocabulary but requires longer sequences.

## Downstream Tasks

- Promoter activity prediction
- Splice site detection
- Transcription factor binding site prediction
- Variant effect scoring
- Chromatin state prediction

## Related Clusters

- [[cluster-map-protein]] â€” ESM-2 is the protein analogue of these DNA LMs
- [[cluster-map-deep-learning]] â€” Transformers, masked language modeling
- [[cluster-map-sequence-analysis]] â€” Traditional sequence analysis methods
