---
tags:
  - "topic"
  - "map"
  - "knowledge-graph"
topics:
  - "MLCB"
status: "generated"
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
  - "Relationship Map"
  - "Edge Type Map"
---

# Relationship Type Map

> [!info] All 16 relationship types used in the MLCB KG, with representative examples.

## IS_A â€” Subtype / Inheritance
Source is a specific instance of target.

- [[baum-welch]] IS_A [[expectation-maximization]]
- [[esm2]] IS_A [[transformer]]
- [[dnabert]] IS_A [[transformer]]
- [[large-language-model]] IS_A [[transformer]]
- [[eqtl]] IS_A [[snp]]

## HAS_PART â€” Composition
Target is a component of source.

- [[alphafold2]] HAS_PART [[evoformer]]
- [[gene-regulatory-network]] HAS_PART [[transcription-factor]]
- [[protein-structure]] HAS_PART [[alpha-helix]]
- [[protein-structure]] HAS_PART [[beta-sheet]]
- [[disease-circuitry]] HAS_PART [[enhancer]]

## USES â€” Method dependency
Source uses target technique.

- [[alphafold2]] USES [[attention-mechanism]]
- [[hidden-markov-model]] USES [[viterbi-algorithm]]
- [[expectation-maximization]] USES [[gaussian-mixture-model]]
- [[esm2]] USES [[masked-language-modeling]]
- [[deep-learning]] USES [[backpropagation]]

## APPLIED_TO â€” Domain application
Method applied to biological domain.

- [[hidden-markov-model]] APPLIED_TO [[chromatin]]
- [[k-means-clustering]] APPLIED_TO [[gene-expression-matrix]]
- [[gwas]] APPLIED_TO [[snp]]
- [[message-passing-neural-network]] APPLIED_TO [[molecular-graph]]
- [[blast]] APPLIED_TO [[dna-sequence]]

## PRODUCES â€” Output artifact
Source produces target as output.

- [[scrna-seq]] PRODUCES [[gene-expression-matrix]]
- [[alphafold2]] PRODUCES [[protein-structure]]
- [[network-inference]] PRODUCES [[gene-regulatory-network]]
- [[variational-autoencoder]] PRODUCES [[latent-space]]
- [[ld-score-regression]] PRODUCES [[heritability]]

## ENABLES â€” Capability
Source makes target possible.

- [[graph-neural-network]] ENABLES [[drug-discovery]]
- [[scrna-seq]] ENABLES [[cell-type-annotation]]
- [[esm2]] ENABLES [[zero-shot-fitness-prediction]]
- [[gwas]] ENABLES [[polygenic-risk-score]]
- [[transfer-learning]] ENABLES [[esm2]]

## EXTENDS â€” Build-on
Source is a generalization or improvement of target.

- [[selfies]] EXTENDS [[smiles]]
- [[scrna-seq]] EXTENDS [[rna-seq]]
- [[gaussian-mixture-model]] EXTENDS [[k-means-clustering]]
- [[mendelian-randomization]] EXTENDS [[gwas]]
- [[adam-optimizer]] EXTENDS [[stochastic-gradient-descent]]

## PRECEDED_BY â€” Succession
Source is a successor to target.

- [[alphafold2]] PRECEDED_BY [[alphafold1]]
- [[pca]] PRECEDED_BY [[umap]]
- [[umap]] PRECEDED_BY [[t-sne]]
- [[smiles]] PRECEDED_BY [[selfies]]

## CONTRASTS_WITH â€” Comparison
Source and target are explicitly compared.

- [[data-driven-paradigm]] CONTRASTS_WITH [[hypothesis-driven-paradigm]]
- [[diffusion-model]] CONTRASTS_WITH [[variational-autoencoder]]
- [[hyena]] CONTRASTS_WITH [[dnabert]]
- [[inchi]] CONTRASTS_WITH [[smiles]]

## BASED_ON â€” Mathematical grounding
Source is grounded in target.

- [[expectation-maximization]] BASED_ON Maximum Likelihood Estimation
- [[variational-autoencoder]] BASED_ON [[elbo]]
- [[heritability]] BASED_ON [[snp]]

## LEARNS_FROM â€” Training data
Model trained on target data.

- [[esm2]] LEARNS_FROM [[protein-sequence]]
- [[dnabert]] LEARNS_FROM [[dna-sequence]]
- [[nucleotide-transformer]] LEARNS_FROM [[dna-sequence]]

## REPRESENTED_BY â€” Computational encoding
Biological entity encoded as data type.

- [[protein-structure]] REPRESENTED_BY [[contact-map]]
- [[small-molecule]] REPRESENTED_BY [[smiles]]
- [[small-molecule]] REPRESENTED_BY [[molecular-graph]]
- [[dna]] REPRESENTED_BY [[dna-sequence]]
- [[protein]] REPRESENTED_BY [[protein-sequence]]

## MEMBER_OF â€” Cluster membership
Entity belongs to thematic cluster.

- [[gwas]] MEMBER_OF Module 4 (Genetics and Disease)
- [[alphafold2]] MEMBER_OF Module 2 (Protein)
- [[scrna-seq]] MEMBER_OF Module 1 (Genomics)

## RELATED_TO â€” General relatedness
Thematic or conceptual link not captured by other types.

- [[transcription-factor]] RELATED_TO [[enhancer]]
- [[gwas]] RELATED_TO [[eqtl]]
- [[disease-circuitry]] RELATED_TO [[eqtl]]
