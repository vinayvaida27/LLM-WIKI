---
tags:
  - "topic"
  - "map"
  - "knowledge-graph"
  - "deep-learning"
topics:
  - "MLCB"
  - "deep learning"
  - "neural networks"
status: "generated"
created: 2026-05-25
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_10_protein_structure_with_transformers.md"
  - "Raw/Sources/lecture_11_protein_language_models.md"
  - "Raw/Sources/lecture_16_training_neural_networks.md"
source_count: 3
aliases:
  - "Deep Learning Cluster Map"
  - "Neural Network Cluster Map"
---

# Cluster Map: Deep Learning

> Lectures 10, 11, 12, 16 | Cross-cutting

## Entities in this Cluster

| Entity | Type | Importance | Lectures |
|---|---|---|---|
| [[deep-learning|Deep Learning]] | concept | 0.90 | 1,16 |
| [[transformer|Transformer]] | model | 0.92 | 10,11,12 |
| [[attention-mechanism|Attention Mechanism]] | method | 0.90 | 10,11,12 |
| [[masked-language-modeling|Masked Language Modeling]] | method | 0.85 | 11,12 |
| [[transfer-learning|Transfer Learning]] | concept | 0.85 | 11,16 |
| [[backpropagation|Backpropagation]] | method | 0.82 | 16 |
| [[stochastic-gradient-descent|SGD]] | method | 0.78 | 16 |
| [[adam-optimizer|Adam]] | method | 0.75 | 16 |
| [[batch-normalization|Batch Normalization]] | method | 0.75 | 16 |
| [[dropout|Dropout]] | method | 0.73 | 16 |
| [[cross-entropy-loss|Cross-Entropy Loss]] | equation | 0.80 | 11,16 |

## Key Relationships

```
deep-learning --> backpropagation (USES)
deep-learning --> representation-learning (ENABLES)
transformer --> attention-mechanism (USES)
attention-mechanism --> transformer (HAS_PART)
backpropagation --> stochastic-gradient-descent (ENABLES)
adam-optimizer --> stochastic-gradient-descent (EXTENDS)
masked-language-modeling --> self-supervised-learning (IS_A)
transfer-learning --> esm2 (ENABLES)
transfer-learning --> dnabert (ENABLES)
cross-entropy-loss --> masked-language-modeling (USES)
```

## Narrative

[[deep-learning|Deep learning]] pervades the entire MLCB course. Lecture 16 covers the mechanics: [[backpropagation|backpropagation]] computes gradients; [[stochastic-gradient-descent|SGD]] updates weights; [[adam-optimizer|Adam]] adds adaptive learning rates; [[batch-normalization|BatchNorm]] and [[dropout|Dropout]] regularize training.

The [[transformer|Transformer]] architecture (self-attention + feedforward layers) is the dominant model class: [[alphafold2]] uses it for protein structure; [[esm2]] for protein sequences; [[dnabert]] for DNA; most modern drug-discovery models use it for SMILES/SELFIES strings.

[[transfer-learning|Transfer learning]] is the practical workflow: pretrain a large model with [[masked-language-modeling|MLM]] on unannotated sequences (protein, DNA), then fine-tune on a small labeled downstream dataset.

## Related Clusters

- [[cluster-map-foundations]] â€” Self-supervised learning, representation learning
- [[cluster-map-protein]] â€” AlphaFold2, ESM-2 are deep learning models
- [[cluster-map-genomics-ml]] â€” DNABERT, Nucleotide Transformer
- [[cluster-map-generative-models]] â€” VAE, diffusion models
