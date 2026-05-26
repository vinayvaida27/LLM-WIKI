---
tags:
  - "topic"
  - "map"
  - "index"
topics:
  - "MLCB"
status: "curated"
created: 2026-05-25
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_01_course_introduction.md"
  - "Raw/Sources/lecture_02_expression_analysis_and_clustering.md"
  - "Raw/Sources/lecture_03_single_cell_analysis.md"
  - "Raw/Sources/lecture_04_alignment.md"
  - "Raw/Sources/lecture_05_epigenomics_hmms.md"
  - "Raw/Sources/lecture_06_regulatory_circuitry.md"
  - "Raw/Sources/lecture_07_regulatory_networks.md"
  - "Raw/Sources/lecture_08_intro_to_protein_structure.md"
  - "Raw/Sources/lecture_09_protein_folding_algorithms.md"
  - "Raw/Sources/lecture_10_protein_structure_with_transformers.md"
  - "Raw/Sources/lecture_11_protein_language_models.md"
  - "Raw/Sources/lecture_12_dna_language_models.md"
  - "Raw/Sources/lecture_13_drug_development_intro.md"
  - "Raw/Sources/lecture_14_chemistry_gnns.md"
  - "Raw/Sources/lecture_15_generating_new_molecules.md"
  - "Raw/Sources/lecture_16_training_neural_networks.md"
  - "Raw/Sources/lecture_17_genetics_disease_gwas_prs_mechanism.md"
  - "Raw/Sources/lecture_18_disease_mechanism_circuitry_eqtls_heritability.md"
source_count: 18
aliases:
  - "Methods Index"
  - "Algorithms Index"
---

# Methods Index

> [!info] All methods (algorithms, analytical procedures, statistical techniques) in the MLCB knowledge graph. 32 methods total.

## Sequence Analysis Methods

| Method | Lectures | Description |
|---|---|---|
| [[sequence-alignment|Sequence Alignment]] | 4 | Needleman-Wunsch (global), Smith-Waterman (local) |
| [[hidden-markov-model|Hidden Markov Model]] | 5 | Probabilistic sequential model; used for chromatin state annotation |
| [[viterbi-algorithm|Viterbi Algorithm]] | 5 | Dynamic programming to find optimal HMM state path |
| [[baum-welch|Baum-Welch]] | 5 | EM algorithm for unsupervised HMM parameter learning |

## Clustering and Dimensionality Reduction

| Method | Lectures | Description |
|---|---|---|
| [[expectation-maximization|EM Algorithm]] | 1, 2, 5 | Iterative ML estimation with latent variables |
| [[k-means-clustering|K-Means]] | 2 | Hard-assignment clustering via centroid iteration |
| [[gaussian-mixture-model|Gaussian Mixture Model]] | 1, 2 | Soft-assignment probabilistic clustering |
| [[pca|PCA]] | 2 | Linear dimensionality reduction via SVD |
| [[umap|UMAP]] | 2, 3 | Non-linear dimensionality reduction; preserves local/global structure |
| [[t-sne|t-SNE]] | 2, 3 | Non-linear; optimizes KL-divergence of pairwise distances |

## Epigenomics and Regulatory Methods

| Method | Lectures | Description |
|---|---|---|
| [[chromhmm|ChromHMM]] | 5 | Multivariate HMM for chromatin state annotation from histone marks |
| [[motif-finding|Motif Finding]] | 6 | EM / Gibbs sampling to discover TF binding sequence patterns |
| [[network-inference|Network Inference]] | 7 | Reconstruct gene regulatory networks from expression data |

## Protein Structure Methods

| Method | Lectures | Description |
|---|---|---|
| [[multiple-sequence-alignment|MSA]] | 9, 10 | Align multiple protein sequences to reveal conservation |
| [[coevolution-analysis|Coevolution Analysis]] | 9 | Detect co-evolving residue pairs â†’ contact prediction (DCA) |
| [[masked-language-modeling|Masked Language Modeling]] | 11, 12 | Self-supervised pre-training: predict masked tokens |

## Graph Neural Network Methods

| Method | Lectures | Description |
|---|---|---|
| [[graph-neural-network|Graph Neural Network]] | 1, 14 | Learn on graph-structured data via message passing |
| [[message-passing-neural-network|MPNN]] | 14 | Directional message passing for molecular graphs |

## Generative Methods

| Method | Lectures | Description |
|---|---|---|
| [[variational-autoencoder|Variational Autoencoder]] | 15 | Latent-space generative model; ELBO training objective |
| [[diffusion-model|Diffusion Model]] | 15 | Score-based generative model; reverse a noise process |
| [[normalizing-flow|Normalizing Flow]] | 15 | Invertible transformations for exact likelihood |

## Training and Optimization

| Method | Lectures | Description |
|---|---|---|
| [[backpropagation|Backpropagation]] | 16 | Reverse-mode auto-differentiation for gradient computation |
| [[stochastic-gradient-descent|SGD]] | 16 | Mini-batch gradient descent optimizer |
| [[adam-optimizer|Adam]] | 16 | Adaptive moment estimation optimizer |
| [[batch-normalization|Batch Normalization]] | 16 | Normalize activations; reduces covariate shift |
| [[dropout|Dropout]] | 16 | Stochastic regularization by dropping activations |
| [[transfer-learning|Transfer Learning]] | 11, 16 | Pre-train on large corpus, fine-tune on downstream task |

## Genetics / Statistical Methods

| Method | Lectures | Description |
|---|---|---|
| [[gwas|GWAS]] | 17 | Genome-wide statistical association of SNPs with traits |
| [[polygenic-risk-score|PRS]] | 17 | Aggregate GWAS effect sizes into individual risk score |
| [[fine-mapping|Fine Mapping]] | 17, 18 | Identify causal variant within GWAS peak (SuSiE, FINEMAP) |
| [[ld-score-regression|LD Score Regression]] | 18 | Estimate SNP heritability and partitioned heritability from GWAS summary stats |
| [[mendelian-randomization|Mendelian Randomization]] | 18 | Causal inference using SNPs as instrumental variables |
| [[colocalization|Colocalization]] | 18 | Test whether GWAS and eQTL signals share a causal variant |

## Drug Discovery Methods

| Method | Lectures | Description |
|---|---|---|
| [[virtual-screening|Virtual Screening]] | 13 | Computational filtering of compound libraries |
| [[molecular-docking|Molecular Docking]] | 13 | Predict binding pose of small molecule to protein |

## Navigation

[[Course Graph Map]] Â· [[Models Index]] Â· [[Concepts Index]] Â· [[Biological Entities Index]]
