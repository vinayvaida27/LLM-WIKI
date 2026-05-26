---
tags:
  - "topic"
  - "map"
  - "navigation"
topics:
  - "MLCB"
status: "curated"
created: 2026-05-25
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_02_expression_analysis_and_clustering.md"
  - "Raw/Sources/lecture_03_single_cell_analysis.md"
  - "Raw/Sources/lecture_05_epigenomics_hmms.md"
  - "Raw/Sources/lecture_06_regulatory_circuitry.md"
  - "Raw/Sources/lecture_10_protein_structure_with_transformers.md"
  - "Raw/Sources/lecture_11_protein_language_models.md"
  - "Raw/Sources/lecture_13_drug_development_intro.md"
  - "Raw/Sources/lecture_14_chemistry_gnns.md"
  - "Raw/Sources/lecture_15_generating_new_molecules.md"
  - "Raw/Sources/lecture_17_genetics_disease_gwas_prs_mechanism.md"
  - "Raw/Sources/lecture_18_disease_mechanism_circuitry_eqtls_heritability.md"
source_count: 11
aliases:
  - "Learning Paths"
  - "Study Guide"
---

# Learning Paths

> [!info] Guided routes through MLCB material, organized by learning goal. Each path links to the most relevant lectures, entities, and methods.

## Path 1: Core ML Background for Biologists

For learners with biology background who need ML foundations:

1. [[cluster-map-foundations]] â€” Start: EM algorithm, GMM, PCA
2. [[cluster-map-classical-ml]] â€” HMMs, clustering, sequence alignment
3. [[cluster-map-deep-learning]] â€” Neural networks, backpropagation, transformers
4. [[high-importance-entity-map]] â€” Representation learning, latent space, self-supervised learning

**Key entities:** [[expectation-maximization|EM]], [[hidden-markov-model|HMM]], [[deep-learning|Deep Learning]], [[latent-space|Latent Space]], [[representation-learning|Representation Learning]]

---

## Path 2: Genomics and Single-Cell Analysis

For learners focused on gene expression and cell biology:

1. [[cluster-map-genomics]] â€” Gene expression matrices, scRNA-seq, clustering
2. [[cluster-map-sequence-analysis]] â€” DNA sequences, HMM annotation
3. [[cluster-map-epigenomics]] â€” Chromatin states, histone marks
4. [[cluster-map-regulatory-genomics]] â€” Enhancers, TFs, motif discovery

**Key entities:** [[scrna-seq|scRNA-seq]], [[gene-expression-matrix|Gene Expression Matrix]], [[transcription-factor|TF]], [[enhancer|Enhancer]], [[chromatin|Chromatin]]

**Key lectures:** [[lecture-02-expression-analysis-and-clustering]], [[lecture-03-single-cell-analysis]], [[lecture-05-epigenomics-hmms]], [[lecture-06-regulatory-circuitry]]

---

## Path 3: Protein Structure and Language Models

For learners focused on structural biology and foundation models:

1. [[cluster-map-protein]] â€” Protein structure, contact maps, Evoformer, AlphaFold2
2. [[cluster-map-deep-learning]] â€” Transformers, attention mechanism
3. Protein language models â€” ESM-2, masked language modeling, zero-shot fitness prediction

**Key entities:** [[alphafold2|AlphaFold2]], [[evoformer|Evoformer]], [[esm2|ESM-2]], [[transformer|Transformer]], [[attention-mechanism|Attention]], [[protein-structure|Protein Structure]], [[multiple-sequence-alignment|MSA]]

**Key lectures:** [[lecture-10-protein-structure-with-transformers]], [[lecture-11-protein-language-models]]

---

## Path 4: Drug Discovery with ML

For learners focused on computational chemistry and generative AI:

1. [[cluster-map-drug-discovery]] â€” Drug development pipeline, ADMET, GNNs, molecular docking
2. [[cluster-map-generative-models]] â€” VAE, diffusion models, latent space
3. [[cluster-map-genomics-ml]] â€” Genomic language models (transfer to molecular sequences)

**Key entities:** [[small-molecule|Small Molecule]], [[molecular-graph|Molecular Graph]], [[message-passing-neural-network|MPNN]], [[variational-autoencoder|VAE]], [[diffusion-model|Diffusion Model]]

**Key lectures:** [[lecture-13-drug-development-intro]], [[lecture-14-chemistry-gnns]], [[lecture-15-generating-new-molecules]]

---

## Path 5: Genetics, GWAS, and Disease Mechanisms

For learners focused on human genetics and disease:

1. [[cluster-map-genetics-disease]] â€” Genetic variation, GWAS, PRS, eQTLs
2. [[cluster-map-epigenomics]] â€” Chromatin states in disease tissue context
3. [[cluster-map-regulatory-genomics]] â€” Enhancers where disease variants live

**Key entities:** [[snp|SNP]], [[gwas|GWAS]], [[polygenic-risk-score|PRS]], [[eqtl|eQTL]], [[heritability|Heritability]], [[linkage-disequilibrium|LD]], [[enhancer|Enhancer]]

**Key lectures:** [[lecture-17-genetics-disease-gwas-prs-mechanism]], [[lecture-18-disease-mechanism-circuitry-eqtls-heritability]]

---

## Full Course Sequence

The MLCB 2024 course follows this logical order:
```
Expression Analysis â†’ Single-Cell â†’ Alignment â†’ Epigenomics â†’ Regulatory Genomics
  â†’ Protein Structure â†’ Protein Language Models â†’ DNA Language Models
  â†’ Drug Discovery â†’ Training â†’ Genetics & Disease
```

See [[lecture-entity-map]] for the full 18-lecture outline.

## Navigation

[[Course Graph Map]] Â· [[Cluster Map]] Â· [[lecture-entity-map]] Â· [[knowledge-graph-index]]
