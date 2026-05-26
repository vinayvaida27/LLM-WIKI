---
tags:
  - "concept"
topics:
  - "MLCB"
status: "updated"
created: 2026-05-24
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_01_course_introduction.md"
source_count: 1
aliases:
  - "self-supervised learning"
  - "self-supervised-learning"
  - "Self-Supervised Learning"
  - "SSL"
  - "Self-Supervision"
  - "self supervised learning"
---

# Self-Supervised Learning

## Overview
Self-supervised learning is introduced in Lecture 1 as a way for foundation models to learn from raw data without needing every example to be manually labeled. The model hides part of the input and learns to predict the missing piece.

## Plain-English Intuition
Instead of giving the model an answer key made by humans, we create a training task from the data itself. Hide a word and predict it. Hide a token in a protein or DNA sequence and predict it. This forces the model to learn structure because guessing well requires context.

## Why It Matters in MLCB
Biology has huge unlabeled datasets: genomes, protein sequences, molecular strings, images, scientific papers, and clinical text. Self-supervision lets models learn useful representations from those datasets before being adapted to a specific biological task.

## Biological Context
The biological reason this works is that biological sequences and structures are not random. Protein sequences carry evolutionary and structural constraints. DNA sequences carry regulatory signals. Molecules encode chemical constraints. A self-supervised model can learn some of those regularities by solving prediction tasks.

## Computational Context
Self-supervised learning connects directly to [[representation-learning]] and [[latent-space]]. The model learns internal embeddings that can later support classification, generation, retrieval, annotation, or hypothesis generation.

## Where It Appears in the Lectures
- [[lecture-01-course-introduction]] - foundation-model framing and missing-input prediction.
- [[lecture-10-protein-structure-with-transformers]] - transformer-style biological sequence models.
- [[lecture-11-protein-language-models]] - masked language modeling for proteins.
- [[lecture-12-dna-language-models]] - masked modeling for genomic sequences.

## Important Examples
- Predicting missing words in natural language.
- Predicting masked amino acids in protein language models.
- Predicting masked k-mers or bases in DNA language models.


## Graph Links

### Parent Topics
- [[topic-regulatory-networks|Regulatory Networks]]

## Related Concepts
- [[representation-learning]]
- [[latent-space]]
- [[multimodal-foundation-models]]
- [[protein-structure-and-biological-language-models]]

## Common Confusions
Self-supervised does not mean unsupervised in the loose sense of "no objective." It has a training objective, but the labels are generated from the input data itself.

## Summary
Self-supervised learning is one reason modern biological foundation models can learn from massive sequence and text corpora without requiring a human-labeled dataset for every task.
