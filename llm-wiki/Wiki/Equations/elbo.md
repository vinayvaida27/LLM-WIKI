---
tags:
  - "equation"
topics:
  - "MLCB"
  - "generative-models"
status: "compiled"
created: 2026-05-25
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_15_generating_new_molecules.md"
source_count: 1
aliases:
  - "elbo"
  - "Evidence Lower Bound"
  - "ELBO"
  - "Variational Lower Bound"
kg_id: "elbo"
entity_type: "equation"
importance: 0.78
---

# Evidence Lower Bound

## Definition
Objective function for VAEs: ELBO = E[log p(x|z)] - KL(q(z|x)||p(z)). Maximizing ELBO is equivalent to maximizing a lower bound on log p(x).

## Why It Matters
Evidence Lower Bound is a canonical MLCB graph node. Keeping it as a source-backed Wiki page prevents Obsidian from creating a phantom node for `[[elbo]]` links and gives retrieval a stable target.

## Lecture Source
- [[lecture-15-generating-new-molecules|Lecture 15 - Generating New Molecules]]

## Key Relationships
- [[variational-autoencoder|Variational Autoencoder]] based on this node.

## Related Concepts
- [[mlcb-2024-computational-biology]]
- [[mlcb-cross-lecture-connections]]
- [[cluster-map-generative-models|Cluster map: generative-models]]


## Graph Links

### Parent Topics
- [[topic-drug-discovery|Drug Discovery]]

## Retrieval Keywords
Evidence Lower Bound, elbo, ELBO, Variational Lower Bound, equation, generative-models

## Aliases
- elbo
- Evidence Lower Bound
- ELBO
- Variational Lower Bound
