# MLCB LLM Wiki

This is the human landing page for the MLCB Second Brain. It points to curated entry points first; the generated file listing lives at [[generated-index]].

## Query Order

1. Search compiled Wiki notes first with `python scripts/query_wiki.py --query "question text"`.
2. Open the most relevant notes under [[Topics/index|Topics]], [[Concepts/index|Concepts]], [[Entities/index|Entities]], [[Methods/index|Methods]], [[Equations/index|Equations]], [[Comparisons/index|Comparisons]], or [[Projects/index|Projects]].
3. Use each note's `sources` frontmatter to verify against `Raw/Sources/` only when evidence, quotes, timestamps, or missing details are needed.
4. Ignore `Raw/Files/` during retrieval; it is backup/staging only.

## Main Entrypoints

- [[mlcb-2024-computational-biology]] - course map and study path.
- [[mlcb-complete-study-guide]] - full-course review.
- [[mlcb-methods-map]] - methods, inputs, outputs, and biological uses.
- [[mlcb-cross-lecture-connections]] - how lectures connect.
- [[mlcb-biology-for-ml-students]] - biology concepts for ML learners.
- [[mlcb-exam-and-interview-questions]] - review questions.

## Core Concept Areas

- [[representation-learning]]
- [[self-supervised-learning]]
- [[latent-space]]
- [[multimodal-foundation-models]]
- [[gene-expression-and-single-cell-analysis]]
- [[sequence-alignment-and-regulatory-genomics]]
- [[epigenomics-and-hidden-markov-models]]
- [[protein-structure-and-biological-language-models]]
- [[drug-discovery-and-molecular-generation]]
- [[neural-network-training-for-biology]]
- [[genetics-gwas-and-disease-mechanism]]

## Generated Indexes

- [[mlcb-master-topic-map]] - imported Phase 1 topic coverage backlog.
- [[generated-index]] - generated list of all compiled Wiki files.
- [[figure-index]] - figure and visual-note status.
- [[update-log]] - maintenance history.
- [[lint-report]] - last curated lint report.
- [[unresolved-items]] - known gaps.
