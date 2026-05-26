---
tags:
  - "topic"
  - "map"
  - "knowledge-graph"
  - "epigenomics"
topics:
  - "MLCB"
  - "epigenomics"
status: "generated"
created: 2026-05-25
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_05_epigenomics_hmms.md"
  - "Raw/Sources/lecture_06_regulatory_circuitry.md"
source_count: 2
aliases:
  - "Epigenomics Cluster Map"
---

# Cluster Map: Epigenomics

> Lectures 5â€“6 | Module 1

## Entities in this Cluster

| Entity | Type | Importance | Lectures |
|---|---|---|---|
| [[chromatin|Chromatin]] | biological_entity | 0.80 | 5,6 |
| [[histone-modification|Histone Modification]] | biological_entity | 0.80 | 5 |
| [[chip-seq|ChIP-seq]] | data_type | 0.78 | 5,6 |
| [[atac-seq|ATAC-seq]] | data_type | 0.76 | 5,6 |
| [[dna-methylation|DNA Methylation]] | biological_entity | 0.72 | 5 |
| [[chromhmm|ChromHMM]] | tool | 0.72 | 5 |
| [[cpg-island|CpG Island]] | biological_entity | 0.68 | 5 |
| [[encode|ENCODE]] | tool | 0.73 | 6 |

## Key Relationships

```
chip-seq --> histone-modification (PRODUCES)
atac-seq --> chromatin (PRODUCES)
chromhmm --> hidden-markov-model (USES)
chromhmm --> chip-seq (APPLIED_TO)
cpg-island --> dna-methylation (RELATED_TO)
dna-methylation --> gene (RELATED_TO)
encode --> chip-seq (PRODUCES)
histone-modification --> gene (RELATED_TO)
dna --> chromatin (HAS_PART)
```

## Narrative

The epigenome â€” histone marks, chromatin accessibility, and DNA methylation â€” controls which genes are expressed in which cell types without changing the underlying DNA sequence.

**ChIP-seq** maps protein-DNA binding (TFs, histone marks) genome-wide. **ATAC-seq** maps accessible chromatin. **ChromHMM** learns multi-mark chromatin state annotations using a multivariate HMM trained on histone ChIP-seq tracks, producing 5â€“25 state annotations per genome region.

**DNA methylation** at CpG sites is a stable silencing mark. CpG islands at promoters are typically unmethylated in active genes.

## Related Clusters

- [[cluster-map-regulatory-genomics]] â€” Enhancers and TFs extend epigenomics
- [[cluster-map-classical-ml]] â€” HMMs underpin ChromHMM
- [[cluster-map-genetics-disease]] â€” Epigenomic annotations inform GWAS loci
