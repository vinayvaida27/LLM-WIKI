---
tags:
  - "topic"
  - "map"
  - "knowledge-graph"
  - "foundations"
topics:
  - "MLCB"
  - "machine learning"
status: "generated"
created: 2026-05-25
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_01_course_introduction.md"
source_count: 1
aliases:
  - "Foundations Cluster Map"
  - "ML Foundations Map"
---

# Cluster Map: ML Foundations

> Lecture 1 | Cross-cutting

## Entities in this Cluster

| Entity | Type | Importance |
|---|---|---|
| [[representation-learning|Representation Learning]] | concept | 0.95 |
| [[latent-space|Latent Space]] | concept | 0.85 |
| [[self-supervised-learning|Self-Supervised Learning]] | concept | 0.88 |
| [[multimodal-foundation-models|Multimodal Foundation Models]] | concept | 0.72 |
| [[data-driven-paradigm|Data-Driven Paradigm]] | concept | 0.70 |
| [[hypothesis-driven-paradigm|Hypothesis-Driven Paradigm]] | concept | 0.68 |
| [[deep-learning|Deep Learning]] | concept | 0.90 |
| [[benchmarking|Benchmarking]] | concept | 0.70 |

## Central Ideas from Lecture 1

### The Two Axes of the Course
```
                Biology <----> Computation
                                   |
               Foundations <----> Frontiers
```

### The Representation Learning Loop
```
Biology (raw observations)
   --> Measurement (sequencing, imaging, structure)
       --> Representation (embedding, graph, sequence)
           --> Model (GNN, Transformer, HMM)
               --> Latent Space (Z)
                   --> Interpretation (biology)
```

### Data-Driven vs. Hypothesis-Driven

| Property | Data-Driven | Hypothesis-Driven |
|---|---|---|
| Start | Dataset | Hypothesis |
| Goal | Pattern discovery | Hypothesis testing |
| Risk | Spurious correlations | Confirmation bias |
| Examples | GWAS, expression clustering | Targeted experiment |
| Course emphasis | Both â€” data-driven methods, biologically motivated |

## Related Clusters

All clusters build on these foundations.

- [[cluster-map-classical-ml]] â€” Classical probabilistic methods
- [[cluster-map-deep-learning]] â€” Deep learning implementations
- [[cluster-map-protein]] â€” Representation learning for proteins
- [[cluster-map-genomics-ml]] â€” Representation learning for DNA
