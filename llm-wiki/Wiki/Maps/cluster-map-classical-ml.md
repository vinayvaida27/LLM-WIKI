---
tags:
  - "topic"
  - "map"
  - "knowledge-graph"
  - "classical-ml"
topics:
  - "MLCB"
  - "machine learning"
status: "generated"
created: 2026-05-25
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_01_course_introduction.md"
  - "Raw/Sources/lecture_02_expression_analysis_and_clustering.md"
source_count: 2
aliases:
  - "Classical ML Cluster Map"
---

# Cluster Map: Classical ML Methods

> Lectures 1â€“2, 4â€“5 | Cross-cutting foundational methods

## Entities in this Cluster

| Entity | Type | Importance | Lectures |
|---|---|---|---|
| [[expectation-maximization|Expectation-Maximization]] | method | 0.82 | 1,2,5 |
| [[k-means-clustering|K-Means Clustering]] | method | 0.78 | 2 |
| [[gaussian-mixture-model|Gaussian Mixture Model]] | method | 0.76 | 2 |
| [[pca|PCA]] | method | 0.78 | 2,3 |
| [[umap|UMAP]] | method | 0.78 | 2,3 |
| [[t-sne|t-SNE]] | method | 0.70 | 2 |
| [[hidden-markov-model|Hidden Markov Model]] | method | 0.85 | 5 |
| [[viterbi-algorithm|Viterbi Algorithm]] | method | 0.78 | 5 |
| [[baum-welch|Baum-Welch]] | method | 0.73 | 5 |
| [[gibbs-sampling|Gibbs Sampling]] | method | 0.68 | 1,6 |
| [[dynamic-programming|Dynamic Programming]] | method | 0.78 | 4,5 |

## Key Relationships

```
expectation-maximization --> gaussian-mixture-model (USES)
expectation-maximization --> hidden-markov-model (USES)
expectation-maximization --> motif-finding (APPLIED_TO)
gaussian-mixture-model --> k-means-clustering (EXTENDS)
baum-welch --> expectation-maximization (IS_A)
hidden-markov-model --> viterbi-algorithm (USES)
hidden-markov-model --> baum-welch (USES)
viterbi-algorithm --> dynamic-programming (USES)
```

## Algorithm Summary

### K-Means
Initialize K centroids â†’ assign each point to nearest centroid â†’ update centroids â†’ repeat until convergence. Hard assignments; minimizes within-cluster sum of squares.

### Gaussian Mixture Model (GMM)
Soft probabilistic version of K-Means. Each cluster is a Gaussian; membership is a probability. Fit by EM: E-step computes expected cluster membership; M-step updates Gaussian parameters.

### EM
General algorithm for maximum likelihood with latent variables. E-step: compute E[latent | observed, parameters]. M-step: maximize expected log-likelihood over parameters. Used in GMMs, HMMs, and motif finders.

### HMM
States emit observed data with probability; states transition with probability. Viterbi decoding (DP) finds the most probable state path. Baum-Welch (EM for HMMs) learns parameters from unlabeled observations.

### Dynamic Programming
Fills a table of overlapping subproblems bottom-up. Used for Viterbi (HMM decoding), Needleman-Wunsch/Smith-Waterman (alignment), and RNA structure prediction.

## Related Clusters

- [[cluster-map-deep-learning]] â€” Deep learning methods replace and extend classical approaches
- [[cluster-map-genomics]] â€” K-means, PCA, UMAP used in RNA-seq analysis
- [[cluster-map-epigenomics]] â€” HMMs underpin ChromHMM chromatin segmentation
- [[cluster-map-sequence-analysis]] â€” Dynamic programming underlies alignment
