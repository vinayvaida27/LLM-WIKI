---
tags:
  - "topic"
  - "map"
  - "knowledge-graph"
  - "genomics"
topics:
  - "MLCB"
  - "genomics"
  - "single-cell"
status: "generated"
created: 2026-05-25
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_02_expression_analysis_and_clustering.md"
  - "Raw/Sources/lecture_03_single_cell_analysis.md"
source_count: 2
aliases:
  - "Genomics Cluster Map"
---

# Cluster Map: Genomics

> Lectures 2â€“3 | Module 1

## Entities in this Cluster

| Entity | Type | Importance | Lectures |
|---|---|---|---|
| [[gene|Gene]] | biological_entity | 0.85 | 1,2,6,7 |
| [[dna|DNA]] | biological_entity | 0.88 | 1,4,5,12,17 |
| [[rna|RNA]] | biological_entity | 0.85 | 1,2,3 |
| [[gene-expression-matrix|Gene Expression Matrix]] | data_type | 0.80 | 2,3 |
| [[rna-seq|RNA-seq]] | data_type | 0.75 | 2 |
| [[scrna-seq|scRNA-seq]] | data_type | 0.85 | 3 |
| [[cell-type-annotation|Cell Type Annotation]] | application | 0.72 | 3 |
| [[trajectory-inference|Trajectory Inference]] | method | 0.73 | 3 |
| [[scanpy|Scanpy]] | tool | 0.68 | 3 |

## Analysis Pipeline

```
rna-seq / scrna-seq
   --> gene-expression-matrix
       --> pca (dimensionality reduction)
           --> umap (visualization)
               --> k-means / leiden (clustering)
                   --> cell-type-annotation (biological interpretation)
                   --> trajectory-inference (developmental ordering)
```

## Key Distinctions

| Property | RNA-seq | scRNA-seq |
|---|---|---|
| Resolution | Population average | Single cell |
| Input | Bulk tissue | Dissociated cells |
| Dimensionality | genes Ã— samples | genes Ã— cells (sparse) |
| Key challenge | Condition comparison | Sparsity, batch effects |
| Key output | DEGs | Cell type clusters, trajectories |

## Related Clusters

- [[cluster-map-classical-ml]] â€” k-means, GMM, PCA, UMAP used in genomics
- [[cluster-map-epigenomics]] â€” Chromatin regulates gene expression
- [[cluster-map-regulatory-genomics]] â€” GRNs link TFs to gene expression
- [[cluster-map-genomics-ml]] â€” DNA language models trained on genomic sequences
