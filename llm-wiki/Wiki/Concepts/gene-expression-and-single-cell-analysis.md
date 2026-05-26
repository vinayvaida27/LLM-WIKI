---
tags:
  - "concept"
topics:
  - "MLCB"
status: "updated"
created: 2026-05-24
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_02_expression_analysis_and_clustering.md"
  - "Raw/Sources/lecture_03_single_cell_analysis.md"
source_count: 2
aliases:
  - "Gene Expression And Single-Cell Analysis"
---

# Gene Expression And Single-Cell Analysis

## Overview
Gene expression and single-cell analysis turn RNA abundance into high-dimensional matrices that reveal cell state, disease state, clusters, modules, and trajectories. Bulk expression gives averaged signals, while single-cell analysis resolves heterogeneity but introduces sparsity, technical noise, doublets, batch effects, and sampling concerns.

## Plain-English Intuition
For an ML student, this concept is a way to convert biological complexity into a computable representation while preserving enough context to make the output biologically meaningful.

## Why It Matters in MLCB
This concept is a recurring bridge between biological measurement and computational modeling. It appears because the course cares about both prediction and mechanism.

## Biological Context
Read the linked lecture pages for the source-specific biology, examples, and caveats.

## Computational / ML Context
The computational side usually involves representation learning, probabilistic inference, optimization, dynamic programming, graph learning, sequence modeling, or statistical association.

## Where It Appears in the Lectures
- [[lecture-02-expression-analysis-and-clustering|Lecture 2 - Expression Analysis and Clustering]]
- [[lecture-03-single-cell-analysis|Lecture 3 - Single-Cell Analysis]]

## Detailed Explanation
The linked lecture pages preserve detailed source order. Use this synthesis page to connect them and then return to the lecture pages for exact source-grounded details.

## Equations or Formalism
See Wiki/Equations/ and the lecture pages. If an equation is not explicitly present in a source, it is not invented here.

## Important Examples
Examples are source-grounded in the lecture pages and summarized in [[mlcb-complete-study-guide]].


## Graph Links

### Parent Topics
- [[topic-single-cell-analysis|Single-cell Analysis]]

## Related Concepts
- [[mlcb-methods-map]]
- [[mlcb-cross-lecture-connections]]
- [[mlcb-biology-for-ml-students]]

## Common Confusions
Do not confuse prediction with mechanism. A model output needs biological interpretation, source grounding, and often experimental validation.

## Study Questions
### Q1. What biological problem does this concept address?
Answer from the linked lecture pages.

### Q2. What computational representation makes the problem tractable?
Answer by identifying the matrix, sequence, graph, state model, latent vector, or statistical association.

## Summary
Gene expression and single-cell analysis turn RNA abundance into high-dimensional matrices that reveal cell state, disease state, clusters, modules, and trajectories. Bulk expression gives averaged signals, while single-cell analysis resolves heterogeneity but introduces sparsity, technical noise, doublets, batch effects, and sampling concerns.
