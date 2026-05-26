---
tags:
  - "log"
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
  - "MLCB update log"
---

# Update Log

## [2026-05-25 00:00] build | MLCB Knowledge Graph v1.0
- Built typed, source-grounded knowledge graph from 18 MLCB lecture transcripts.
- Nodes: 120 entities across 11 types (concept, method, model, biological_entity, data_type, application, tool, equation, lecture, topic, person).
- Edges: 158 relationships across 16 types (IS_A, HAS_PART, USES, APPLIED_TO, PRODUCES, ENABLES, etc.).
- Schema: entity_ontology.yaml, relationship_ontology.yaml, graph_schema.json, extraction_schema.json.
- Retrieval artifacts: knowledge_graph.json, knowledge_graph_minimal.json, graph_nodes.jsonl, graph_edges.jsonl, entity_index.json, entity_aliases.json (168 aliases), lecture_index.json, cluster_map.json, retrieval_chunks.jsonl (131 chunks).
- Maps: 14 new Wiki/Maps/ files (cluster maps per domain + lecture-entity map + KG index).
- Lecture files: KG Extraction sections added to all 18 lecture wiki pages.
- Logs: extraction_report.md and validation_report.md created.

## [2026-05-24 00:00] update | Existing MLCB Wiki Deep Update
- Scanned existing wiki structure.
- Raw sources reviewed: 18 primary Raw/Sources/ files and 18 supporting Raw/Files/ files.
- Existing pages preserved: course overview and seven concept pages were expanded.
- Pages updated: Wiki/index.md, Wiki/Topics/mlcb-2024-computational-biology.md, concept pages, and folder indexes.
- Pages created: lecture pages, entity pages, method pages, equation pages, comparison pages, project guides, audit report, lint report, source audit, and unresolved-items log.
- Links added: lecture, concept, entity, method, equation, comparison, project, and log links.
- Catalog updated: pending final build.
- Remaining issues: original slide images are not embedded.

## [2026-05-24 00:00] lecture-update | Lecture 1 - Course Introduction
- Source: Raw/Sources/lecture_01_course_introduction.md`n- Supporting source: Raw/Files/lecture_01_course_introduction.md`n- Lecture page: Wiki/Topics/Lectures/lecture-01-course-introduction.md`n- Notes: Built source-faithful study page from processed source content.

## [2026-05-24 00:00] lecture-update | Lecture 2 - Expression Analysis and Clustering
- Source: Raw/Sources/lecture_02_expression_analysis_and_clustering.md`n- Supporting source: Raw/Files/lecture_02_expression_analysis_and_clustering.md`n- Lecture page: Wiki/Topics/Lectures/lecture-02-expression-analysis-and-clustering.md`n- Notes: Built source-faithful study page from processed source content.

## [2026-05-24 00:00] lecture-update | Lecture 3 - Single-Cell Analysis
- Source: Raw/Sources/lecture_03_single_cell_analysis.md`n- Supporting source: Raw/Files/lecture_03_single_cell_analysis.md`n- Lecture page: Wiki/Topics/Lectures/lecture-03-single-cell-analysis.md`n- Notes: Built source-faithful study page from processed source content.

## [2026-05-24 00:00] lecture-update | Lecture 4 - Alignment
- Source: Raw/Sources/lecture_04_alignment.md`n- Supporting source: Raw/Files/lecture_04_alignment.md`n- Lecture page: Wiki/Topics/Lectures/lecture-04-alignment.md`n- Notes: Built source-faithful study page from processed source content.

## [2026-05-24 00:00] lecture-update | Lecture 5 - Epigenomics and HMMs
- Source: Raw/Sources/lecture_05_epigenomics_hmms.md`n- Supporting source: Raw/Files/lecture_05_epigenomics_hmms.md`n- Lecture page: Wiki/Topics/Lectures/lecture-05-epigenomics-hmms.md`n- Notes: Built source-faithful study page from processed source content.

## [2026-05-24 00:00] lecture-update | Lecture 6 - Regulatory Circuitry
- Source: Raw/Sources/lecture_06_regulatory_circuitry.md`n- Supporting source: Raw/Files/lecture_06_regulatory_circuitry.md`n- Lecture page: Wiki/Topics/Lectures/lecture-06-regulatory-circuitry.md`n- Notes: Built source-faithful study page from processed source content.

## [2026-05-24 00:00] lecture-update | Lecture 7 - Regulatory Networks
- Source: Raw/Sources/lecture_07_regulatory_networks.md`n- Supporting source: Raw/Files/lecture_07_regulatory_networks.md`n- Lecture page: Wiki/Topics/Lectures/lecture-07-regulatory-networks.md`n- Notes: Built source-faithful study page from processed source content.

## [2026-05-24 00:00] lecture-update | Lecture 8 - Intro to Protein Structure
- Source: Raw/Sources/lecture_08_intro_to_protein_structure.md`n- Supporting source: Raw/Files/lecture_08_intro_to_protein_structure.md`n- Lecture page: Wiki/Topics/Lectures/lecture-08-intro-to-protein-structure.md`n- Notes: Built source-faithful study page from processed source content.

## [2026-05-24 00:00] lecture-update | Lecture 9 - Protein Folding Algorithms
- Source: Raw/Sources/lecture_09_protein_folding_algorithms.md`n- Supporting source: Raw/Files/lecture_09_protein_folding_algorithms.md`n- Lecture page: Wiki/Topics/Lectures/lecture-09-protein-folding-algorithms.md`n- Notes: Built source-faithful study page from processed source content.

## [2026-05-24 00:00] lecture-update | Lecture 10 - Protein Structure with Transformers
- Source: Raw/Sources/lecture_10_protein_structure_with_transformers.md`n- Supporting source: Raw/Files/lecture_10_protein_structure_with_transformers.md`n- Lecture page: Wiki/Topics/Lectures/lecture-10-protein-structure-with-transformers.md`n- Notes: Built source-faithful study page from processed source content.

## [2026-05-24 00:00] lecture-update | Lecture 11 - Protein Language Models
- Source: Raw/Sources/lecture_11_protein_language_models.md`n- Supporting source: Raw/Files/lecture_11_protein_language_models.md`n- Lecture page: Wiki/Topics/Lectures/lecture-11-protein-language-models.md`n- Notes: Built source-faithful study page from processed source content.

## [2026-05-24 00:00] lecture-update | Lecture 12 - DNA Language Models
- Source: Raw/Sources/lecture_12_dna_language_models.md`n- Supporting source: Raw/Files/lecture_12_dna_language_models.md`n- Lecture page: Wiki/Topics/Lectures/lecture-12-dna-language-models.md`n- Notes: Built source-faithful study page from processed source content.

## [2026-05-24 00:00] lecture-update | Lecture 13 - Drug Development Intro
- Source: Raw/Sources/lecture_13_drug_development_intro.md`n- Supporting source: Raw/Files/lecture_13_drug_development_intro.md`n- Lecture page: Wiki/Topics/Lectures/lecture-13-drug-development-intro.md`n- Notes: Built source-faithful study page from processed source content.

## [2026-05-24 00:00] lecture-update | Lecture 14 - Chemistry GNNs
- Source: Raw/Sources/lecture_14_chemistry_gnns.md`n- Supporting source: Raw/Files/lecture_14_chemistry_gnns.md`n- Lecture page: Wiki/Topics/Lectures/lecture-14-chemistry-gnns.md`n- Notes: Built source-faithful study page from processed source content.

## [2026-05-24 00:00] lecture-update | Lecture 15 - Generating New Molecules
- Source: Raw/Sources/lecture_15_generating_new_molecules.md`n- Supporting source: Raw/Files/lecture_15_generating_new_molecules.md`n- Lecture page: Wiki/Topics/Lectures/lecture-15-generating-new-molecules.md`n- Notes: Built source-faithful study page from processed source content.

## [2026-05-24 00:00] lecture-update | Lecture 16 - Training Neural Networks
- Source: Raw/Sources/lecture_16_training_neural_networks.md`n- Supporting source: Raw/Files/lecture_16_training_neural_networks.md`n- Lecture page: Wiki/Topics/Lectures/lecture-16-training-neural-networks.md`n- Notes: Built source-faithful study page from processed source content.

## [2026-05-24 00:00] lecture-update | Lecture 17 - Genetics, Disease, GWAS, PRS, Mechanism
- Source: Raw/Sources/lecture_17_genetics_disease_gwas_prs_mechanism.md`n- Supporting source: Raw/Files/lecture_17_genetics_disease_gwas_prs_mechanism.md`n- Lecture page: Wiki/Topics/Lectures/lecture-17-genetics-disease-gwas-prs-mechanism.md`n- Notes: Built source-faithful study page from processed source content.

## [2026-05-24 00:00] lecture-update | Lecture 18 - Disease Mechanism, Circuitry, eQTLs, Heritability
- Source: Raw/Sources/lecture_18_disease_mechanism_circuitry_eqtls_heritability.md`n- Supporting source: Raw/Files/lecture_18_disease_mechanism_circuitry_eqtls_heritability.md`n- Lecture page: Wiki/Topics/Lectures/lecture-18-disease-mechanism-circuitry-eqtls-heritability.md`n- Notes: Built source-faithful study page from processed source content.

## [2026-05-24 16:03] deep-update | Lecture 1 backlog topics L01_T001-L01_T015
- Source reviewed: `Raw/Sources/lecture_01_course_introduction.md`.
- Expanded lecture page: `Wiki/Topics/Lectures/lecture-01-course-introduction.md`.
- Created concept pages: `representation-learning`, `self-supervised-learning`, `latent-space`, `multimodal-foundation-models`.
- Created comparison pages: `data-driven-vs-hypothesis-driven-paradigms`, `computation-vs-biology-and-foundations-vs-frontiers`.
- Updated method page: `graph-neural-networks`.
- Updated maps/backlog: `Wiki/Maps/mlcb-master-topic-map.md`, `Schema/topic-backlog.jsonl`, `Schema/topic-processing-log.jsonl`.
- Notes: First 15 Lecture 1 backlog topics are marked `expanded` and `verified: true`; raw transcripts were not modified.

## [2026-05-24 16:20] graph-hygiene | Remove three thin duplicate nodes
- Removed duplicate entity pages: `Wiki/Entities/attention.md`, `Wiki/Entities/graph-neural-network.md`, `Wiki/Entities/drug-discovery.md`.
- Canonical pages kept: `Wiki/Methods/attention-mechanism.md`, `Wiki/Equations/attention-equation.md`, `Wiki/Methods/graph-neural-networks.md`, and `Wiki/Concepts/drug-discovery-and-molecular-generation.md`.
- Updated links in Lecture 1, `latent-space`, and `representation-learning` so graph links point to the stronger canonical pages.
- Notes: This was intentionally conservative; thin placeholders such as logs, figure index, and required entity anchors were left intact.
