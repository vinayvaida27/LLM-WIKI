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
  - "Raw/Sources/lecture_02_expression_analysis_and_clustering.md"
  - "Raw/Sources/lecture_03_single_cell_analysis.md"
source_count: 2
aliases:
  - "Gene Expression"
  - "Expression"
  - "mRNA Expression"
---

# Gene Expression

> [!info] Canonical page: [[gene-expression-matrix|Gene Expression Matrix]]
> In the MLCB computational context, gene expression is almost always represented as a matrix. See also: [[lecture-02-expression-analysis-and-clustering]].

Gene expression is the process by which information encoded in a gene is converted into a functional product (usually a protein, via mRNA). Computationally, it is measured as:

- **Bulk RNA-seq** â€” expression averaged over millions of cells; produces a per-gene count vector
- **[[scrna-seq|scRNA-seq]]** â€” expression measured per individual cell; produces a cell Ã— gene matrix

In the MLCB course (Lectures 2â€“3):
- Expression data is stored as a **[[gene-expression-matrix|gene expression matrix]]**
- Analyzed by clustering ([[expectation-maximization|EM]], k-means) and dimensionality reduction
- Used to identify cell types, states, and regulatory programs

**Canonical page:** [[gene-expression-matrix]]

**Related:** [[scrna-seq]], [[gene-expression-matrix]], [[gene]], [[rna]], [[expectation-maximization]], [[latent-space]]

## Graph Links

### Parent Topics
- [[topic-single-cell-analysis|Single-cell Analysis]]
