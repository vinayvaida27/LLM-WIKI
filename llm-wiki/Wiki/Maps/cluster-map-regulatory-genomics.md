---
tags:
  - "topic"
  - "map"
  - "knowledge-graph"
  - "regulatory-genomics"
topics:
  - "MLCB"
  - "regulatory genomics"
  - "gene regulation"
status: "generated"
created: 2026-05-25
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_06_regulatory_circuitry.md"
  - "Raw/Sources/lecture_07_regulatory_networks.md"
source_count: 2
aliases:
  - "Regulatory Genomics Cluster Map"
---

# Cluster Map: Regulatory Genomics

> Lectures 6â€“7 | Module 1

## Entities in this Cluster

| Entity | Type | Importance | Lectures |
|---|---|---|---|
| [[transcription-factor|Transcription Factor]] | biological_entity | 0.85 | 6,7 |
| [[enhancer|Enhancer]] | biological_entity | 0.80 | 6 |
| [[promoter|Promoter]] | biological_entity | 0.78 | 6 |
| [[gene-regulatory-network|Gene Regulatory Network]] | concept | 0.82 | 7 |
| [[network-inference|Network Inference]] | method | 0.75 | 7 |
| [[network-motif|Network Motif]] | concept | 0.72 | 7 |
| [[motif-finding|Motif Finding]] | method | 0.75 | 4,6 |
| [[encode|ENCODE]] | tool | 0.73 | 6 |
| [[scenic|SCENIC]] | tool | 0.68 | 7 |

## Key Relationships

```
transcription-factor --> enhancer (RELATED_TO)
transcription-factor --> promoter (RELATED_TO)
transcription-factor --> gene (RELATED_TO)
gene-regulatory-network --> transcription-factor (HAS_PART)
gene-regulatory-network --> gene (HAS_PART)
network-inference --> gene-regulatory-network (PRODUCES)
network-motif --> gene-regulatory-network (HAS_PART)
motif-finding --> transcription-factor (APPLIED_TO)
scenic --> network-inference (USES)
encode --> chip-seq (PRODUCES)
```

## Biological Concepts

**Transcription factors** bind specific short DNA sequences (motifs, ~6â€“20 bp) at enhancers and promoters to activate or repress transcription of target genes.

**Enhancers** are distal regulatory elements (often >10 kb from target genes) that physically contact promoters via DNA looping. They are marked by H3K27ac, H3K4me1, and open chromatin (ATAC-seq signal).

**GRNs** are directed graphs encoding which TFs regulate which genes. Key motifs: feed-forward loops (FFL) confer signal filtering; autoregulation enables bistability and robust on/off states.

## Regulatory Network Inference Methods

| Method | Data | Approach |
|---|---|---|
| Correlation-based | Expression | Pearson/Spearman correlation |
| Mutual information | Expression | ARACNE, VIPER |
| Regression | Expression | LASSO, ElasticNet |
| SCENIC | scRNA-seq + TF motifs | GRN + regulon scoring |

## Related Clusters

- [[cluster-map-epigenomics]] â€” Chromatin marks identify active enhancers and TF binding
- [[cluster-map-genetics-disease]] â€” Disease circuitry uses regulatory network logic
- [[cluster-map-sequence-analysis]] â€” Motif finding underlies TF binding site prediction
