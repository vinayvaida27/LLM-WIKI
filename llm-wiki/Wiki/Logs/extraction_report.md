---
tags:
  - "log"
  - "knowledge-graph"
topics:
  - "MLCB"
status: "completed"
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
  - "Knowledge Graph Extraction Report"
  - "extraction_report"
---

# Knowledge Graph Extraction Report

## Summary

| Metric | Value |
|---|---:|
| Lectures processed | 18 |
| Nodes extracted | 120 |
| Edges extracted | 158 |
| Entity types used | 11 |
| Relationship types used | 16 |
| Clusters defined | 13 |
| Retrieval chunks generated | 131 |
| Aliases registered | 168 |

## Entity Type Breakdown

| Type | Count | Notes |
|---|---:|---|
| concept | 18 | ML + biological concepts |
| method | 32 | Algorithms and procedures |
| model | 13 | Named model architectures |
| biological_entity | 18 | Molecules, cells, structures |
| data_type | 14 | Experimental + computational formats |
| application | 5 | Biological goals |
| tool | 9 | Software and databases |
| equation | 2 | ELBO, Cross-Entropy Loss |
| lecture | 18 | One per MLCB lecture |
| topic | 5 | Module-level groupings |
| person | 2 | Instructors |

## Relationship Type Breakdown

| Relation | Count |
|---|---:|
| RELATED_TO | 26 |
| USES | 24 |
| APPLIED_TO | 22 |
| IS_A | 16 |
| PRODUCES | 16 |
| ENABLES | 15 |
| HAS_PART | 14 |
| EXTENDS | 12 |
| PRECEDED_BY | 5 |
| CONTRASTS_WITH | 5 |
| LEARNS_FROM | 3 |
| BASED_ON | 3 |
| REPRESENTED_BY | 8 |
| MEMBER_OF | 9 |

## Files Generated

| File | Purpose |
|---|---|
| `Schema/entity_ontology.yaml` | Entity type definitions |
| `Schema/relationship_ontology.yaml` | Relationship type definitions |
| `Schema/graph_schema.json` | Full JSON schema |
| `Schema/extraction_schema.json` | 9-pass extraction pipeline |
| `retrieval/knowledge_graph.json` | Full KG (120 nodes, 158 edges) |
| `retrieval/knowledge_graph_minimal.json` | High-importance nodes only |
| `retrieval/graph_nodes.jsonl` | One node per line |
| `retrieval/graph_edges.jsonl` | One edge per line |
| `retrieval/entity_index.json` | Fast entity lookup |
| `retrieval/entity_aliases.json` | Alias â†’ canonical id map |
| `retrieval/lecture_index.json` | Lecture â†’ entities map |
| `retrieval/cluster_map.json` | Thematic cluster definitions |
| `retrieval/retrieval_chunks.jsonl` | 131 RAG-ready chunks |
| `Wiki/Maps/knowledge-graph-index.md` | KG navigation hub |
| `Wiki/Maps/lecture-entity-map.md` | Entities by lecture |
| `Wiki/Maps/high-importance-entity-map.md` | Top entities |
| `Wiki/Maps/relationship-type-map.md` | Edge type examples |
| `Wiki/Maps/cluster-map-foundations.md` | Foundations cluster |
| `Wiki/Maps/cluster-map-classical-ml.md` | Classical ML cluster |
| `Wiki/Maps/cluster-map-deep-learning.md` | Deep Learning cluster |
| `Wiki/Maps/cluster-map-genomics.md` | Genomics cluster |
| `Wiki/Maps/cluster-map-epigenomics.md` | Epigenomics cluster |
| `Wiki/Maps/cluster-map-regulatory-genomics.md` | Regulatory Genomics cluster |
| `Wiki/Maps/cluster-map-protein.md` | Protein cluster |
| `Wiki/Maps/cluster-map-genomics-ml.md` | Genomic LMs cluster |
| `Wiki/Maps/cluster-map-drug-discovery.md` | Drug Discovery cluster |
| `Wiki/Maps/cluster-map-genetics-disease.md` | Genetics & Disease cluster |

## High-Importance Entities Without Wiki Pages

The following entities have importance â‰¥ 0.80 but lack a dedicated `wiki_page` entry. Stub pages should be created:

- `large-language-model` (0.85) â†’ suggest `Wiki/Concepts/large-language-models.md`
- `gwas` (0.92) â†’ suggest `Wiki/Methods/gwas.md`
- `polygenic-risk-score` (0.88) â†’ suggest `Wiki/Methods/polygenic-risk-score.md`
- `esm2` (0.90) â†’ suggest `Wiki/Models/esm2.md`
- `transformer` (0.92) â†’ suggest `Wiki/Models/transformer.md`
- `scrna-seq` (0.85) â†’ suggest `Wiki/Methods/scrna-seq.md`
- `eqtl` (0.85) â†’ suggest `Wiki/Concepts/eqtl.md`
- `snp` (0.85) â†’ suggest `Wiki/Entities/snp.md`
- `dna` (0.88) â†’ suggest `Wiki/Entities/dna.md`
- `rna` (0.85) â†’ suggest `Wiki/Entities/rna.md`
- `gene` (0.85) â†’ suggest `Wiki/Entities/gene.md`
- `protein` (0.90) â†’ suggest `Wiki/Entities/protein.md`
- `masked-language-modeling` (0.85) â†’ suggest `Wiki/Methods/masked-language-modeling.md`
- `transfer-learning` (0.85) â†’ suggest `Wiki/Concepts/transfer-learning.md`
- `deep-learning` (0.90) â†’ suggest `Wiki/Concepts/deep-learning.md`
- `message-passing-neural-network` (0.85) â†’ suggest `Wiki/Methods/message-passing-neural-network.md`
- `heritability` (0.82) â†’ suggest `Wiki/Concepts/heritability.md`

## Extraction Date

2026-05-25

## Graph Connections
- [[knowledge-graph-index]]
- [[mlcb-cross-lecture-connections]]
- [[mlcb-2024-computational-biology]]
