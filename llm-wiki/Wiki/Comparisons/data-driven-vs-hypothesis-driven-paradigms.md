---
tags:
  - "comparison"
topics:
  - "MLCB"
status: "updated"
created: 2026-05-24
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_01_course_introduction.md"
source_count: 1
aliases:
  - "data-driven vs hypothesis-driven paradigms"
  - "data-driven-paradigm"
  - "Data-Driven Paradigm"
  - "Data-Driven Approach"
  - "data driven paradigm"
  - "hypothesis-driven-paradigm"
  - "Hypothesis-Driven Paradigm"
  - "Hypothesis-Driven Science"
  - "hypothesis driven paradigm"
---

# Data-Driven vs Hypothesis-Driven Paradigms

## Quick Difference

| Feature | Hypothesis-driven | Data-driven |
|---|---|---|
| Starting point | A proposed biological explanation | Large-scale observations |
| Main strength | Mechanistic focus | Pattern discovery and hypothesis generation |
| Main risk | Missing unexpected structure | Finding correlations without mechanism |
| MLCB role | Guides validation and interpretation | Expands the search space of possible explanations |

## Detailed Explanation
Lecture 1 presents computational biology as a bridge between these paradigms. A hypothesis-driven scientist starts with a possible mechanism and tests it. A data-driven scientist uses high-dimensional measurements and models to discover patterns, prioritize hypotheses, and reveal hidden structure.

The course does not choose one side. It repeatedly combines them: models propose or prioritize patterns, then biological reasoning and experiments decide whether those patterns are meaningful.

## When to Use Hypothesis-Driven Reasoning
Use it when the mechanism is clear enough to formulate a direct test, such as validating whether a specific enhancer affects a gene or whether a variant disrupts a motif.

## When to Use Data-Driven Reasoning
Use it when the system is too large, noisy, or complex for one hand-built hypothesis, such as clustering single-cell states, scanning genomes, prioritizing variants, or learning molecular embeddings.

## Biological Example
Lecture 1 emphasizes that computation can suggest hypotheses that human researchers might not consider, but those hypotheses still need biological interpretation.

## ML Interpretation
This comparison is about where the model enters the scientific loop. It can generate candidates, reduce search space, learn representations, or support interpretation, but it does not replace validation.

## Lecture References
- [[lecture-01-course-introduction]]


## Graph Links

### Parent Topics
- [[topic-epigenomics|Epigenomics]]

## Related Pages
- [[representation-learning]]
- [[latent-space]]
- [[mlcb-cross-lecture-connections]]

## Summary
MLCB uses data-driven models to expand and organize possible explanations, then uses hypothesis-driven biology to test and interpret them.
