---
tags:
  - "project"
topics:
  - "MLCB"
status: updated
created: 2026-05-24
updated: 2026-05-24
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
  - "full course review"
---

# MLCB Complete Study Guide

## Lecture-by-Lecture Review
- [[lecture-01-course-introduction|Lecture 1 - Course Introduction]] - course framing, representation learning, self-supervision, latent spaces, GNNs, multimodal embeddings, and the axes of computation versus biology.
- [[lecture-02-expression-analysis-and-clustering|Lecture 2 - Expression Analysis and Clustering]] - expression matrices, supervised and unsupervised learning, Bayes rule, GMMs, K-means, EM, PCA, and hierarchical clustering.
- [[lecture-03-single-cell-analysis|Lecture 3 - Single-Cell Analysis]] - single-cell RNA-seq, spatial transcriptomics, quality control, pseudobulk analysis, SVD, gene modules, disease states, and trajectory inference.
- [[lecture-04-alignment|Lecture 4 - Alignment]] - comparative genomics, mutation/insertion/deletion models, dynamic programming, traceback, local alignment, BLAST, PSI-BLAST, and PSSMs.
- [[lecture-05-epigenomics-hmms|Lecture 5 - Epigenomics and HMMs]] - chromatin, DNA methylation, histone marks, ChIP-seq, DNase-seq, hidden chromatin states, Viterbi, and posterior decoding.
- [[lecture-06-regulatory-circuitry|Lecture 6 - Regulatory Circuitry]] - enhancer-promoter looping, HMM training, chromatin compartments, Hi-C, TADs, eQTLs, enhancer modules, motifs, and disease circuitry.
- [[lecture-07-regulatory-networks|Lecture 7 - Regulatory Networks]] - motifs, PWMs, EM, Gibbs sampling, CNN motif prediction, gene regulatory networks, adjacency matrices, PCA, SVD, t-SNE, and GNNs.
- [[lecture-08-intro-to-protein-structure|Lecture 8 - Intro to Protein Structure]] - protein structure, PDB, DNA binding, allostery, crystallography, NMR, Cryo-EM, folding funnels, Ramachandran plots, contact maps, and RMSD.
- [[lecture-09-protein-folding-algorithms|Lecture 9 - Protein Folding Algorithms]] - physical energy functions, molecular dynamics, Boltzmann probabilities, hydrophobicity, SASA, AlphaFold, pair representations, softmax, and geometric constraints.
- [[lecture-10-protein-structure-with-transformers|Lecture 10 - Protein Structure with Transformers]] - self-attention, AlphaFold 3, diffusion, RF Diffusion, Protein MPNN, transformers, positional embeddings, residual connections, and transfer learning.
- [[lecture-11-protein-language-models|Lecture 11 - Protein Language Models]] - protein corpora, BLOSUM, epistasis, autoregressive models, masked language modeling, mutation scoring, ProteinGym, embeddings, attention contacts, and immune escape.
- [[lecture-12-dna-language-models|Lecture 12 - DNA Language Models]] - splicing, 1D CNNs, one-hot DNA, DNABERT, Nucleotide Transformer, SegmentNT, UNets, Hyena, EvoDNA, and sequence-to-expression prediction.
- [[lecture-13-drug-development-intro|Lecture 13 - Drug Development Intro]] - drug classes, pharmacokinetics, pharmacodynamics, GPCRs, therapeutic windows, toxicology, drug interactions, and clinical trials.
- [[lecture-14-chemistry-gnns|Lecture 14 - Chemistry GNNs]] - SMILES, SELFIES, SMARTS, InChI, Morgan fingerprints, molecular graphs, QSAR, geometric deep learning, message passing, pooling, and virtual nodes.
- [[lecture-15-generating-new-molecules|Lecture 15 - Generating New Molecules]] - autoencoders, VAEs, KL divergence, ELBO, reparameterization, beta-VAEs, GANs, Junction Tree VAEs, molecular generation, and Halicin.
- [[lecture-16-training-neural-networks|Lecture 16 - Training Neural Networks]] - BBB prediction, PyTorch datasets, feedforward networks, BCE loss, backpropagation, SGD, momentum, Adam, schedules, bias-variance, and regularization.
- [[lecture-17-genetics-disease-gwas-prs-mechanism|Lecture 17 - Genetics, Disease, GWAS, PRS, Mechanism]] - genetic variation, GWAS, SNP arrays, haplotypes, Manhattan plots, population structure, linkage analysis, PRS, fine-mapping, FTO, and omnigenic traits.
- [[lecture-18-disease-mechanism-circuitry-eqtls-heritability|Lecture 18 - Disease Mechanism, Circuitry, eQTLs, Heritability]] - eQTLs, meQTLs, mediation, Mendelian randomization, heritability, GCTA, partitioned heritability, integrative disease mechanism, and the FTO obesity locus.

## Main Biology Concepts
DNA, RNA, genes, expression, chromatin, enhancers, promoters, transcription factors, proteins, amino acids, variants, disease mechanisms, molecules, and drugs.

## Main ML Concepts
Clustering, PCA, SVD, HMMs, dynamic programming, BLAST, CNNs, Transformers, attention, GNNs, VAEs, GANs, gradient descent, Adam, GWAS, PRS, eQTLs, and heritability.

## Important Examples
Droplet scRNA-seq, BLAST, ChIP-seq, chromatin states, AlphaFold, DNABERT, SMILES/SELFIES, Halicin, BBB permeability, Manhattan plots, and FTO.

## Final Condensed Review
The course teaches how to represent biology as data, infer hidden structure, learn representations, generate candidates, and connect predictions back to mechanism.
