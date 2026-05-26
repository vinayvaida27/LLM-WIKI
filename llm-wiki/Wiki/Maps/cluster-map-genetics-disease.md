---
tags:
  - "topic"
  - "map"
  - "knowledge-graph"
  - "genetics"
  - "gwas"
topics:
  - "MLCB"
  - "genetics"
  - "disease"
status: "generated"
created: 2026-05-25
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_17_genetics_disease_gwas_prs_mechanism.md"
  - "Raw/Sources/lecture_18_disease_mechanism_circuitry_eqtls_heritability.md"
source_count: 2
aliases:
  - "Genetics Disease Cluster Map"
---

# Cluster Map: Genetics and Disease

> Lectures 17â€“18 | Module 4

## Entities in this Cluster

| Entity | Type | Importance | Lectures |
|---|---|---|---|
| [[gwas|GWAS]] | method | 0.92 | 17 |
| [[polygenic-risk-score|Polygenic Risk Score]] | method | 0.88 | 17 |
| [[snp|SNP]] | biological_entity | 0.85 | 17 |
| [[eqtl|eQTL]] | concept | 0.85 | 17,18 |
| [[heritability|Heritability]] | concept | 0.82 | 18 |
| [[disease-circuitry|Disease Circuitry]] | concept | 0.82 | 6,18 |
| [[linkage-disequilibrium|Linkage Disequilibrium]] | concept | 0.80 | 17 |
| [[ld-score-regression|LD Score Regression]] | method | 0.78 | 18 |
| [[colocalization|Colocalization]] | method | 0.78 | 18 |
| [[fine-mapping|Fine-Mapping]] | method | 0.78 | 18 |
| [[mendelian-randomization|Mendelian Randomization]] | method | 0.75 | 17 |
| [[manhattan-plot|Manhattan Plot]] | concept | 0.68 | 17 |

## Key Relationships

```
gwas --> snp (APPLIED_TO)
gwas --> polygenic-risk-score (ENABLES)
gwas --> eqtl (RELATED_TO)
gwas --> linkage-disequilibrium (RELATED_TO)
gwas --> manhattan-plot (PRODUCES)
gwas --> disease-circuitry (ENABLES)
polygenic-risk-score --> snp (USES)
polygenic-risk-score --> linkage-disequilibrium (RELATED_TO)
mendelian-randomization --> gwas (EXTENDS)
mendelian-randomization --> snp (USES)
eqtl --> snp (IS_A)
eqtl --> gene (RELATED_TO)
colocalization --> eqtl (APPLIED_TO)
colocalization --> gwas (APPLIED_TO)
fine-mapping --> gwas (APPLIED_TO)
fine-mapping --> linkage-disequilibrium (USES)
ld-score-regression --> heritability (PRODUCES)
ld-score-regression --> gwas (APPLIED_TO)
disease-circuitry --> enhancer (HAS_PART)
disease-circuitry --> transcription-factor (HAS_PART)
disease-circuitry --> eqtl (RELATED_TO)
```

## Narrative

### GWAS Workflow

A GWAS starts with a case-control cohort, tests each of millions of [[snp|SNPs]] for association with a phenotype using logistic regression, and produces a [[manhattan-plot|Manhattan plot]] of -log10(p-values). Associated loci are confounded by [[linkage-disequilibrium|LD]] â€” many correlated variants exist in each locus.

### From Association to Mechanism

GWAS identifies regions, not mechanisms. The mechanistic pipeline:
1. **[[eqtl|eQTL]] mapping** â€” find which GWAS variants affect gene expression in relevant tissues.
2. **[[colocalization|Colocalization]]** â€” test if GWAS and eQTL signals share a causal variant (vs. LD coincidence).
3. **[[fine-mapping|Fine-mapping]]** â€” compute posterior probabilities per variant using LD to identify credible sets.
4. **[[disease-circuitry|Disease circuitry]]** â€” integrate with epigenomic data (enhancers, TF motifs) to build a regulatory model.

### Polygenic Risk and Heritability

[[polygenic-risk-score|PRS]] aggregates genome-wide risk alleles into a single risk score. [[heritability|Heritability]] (hÂ²) quantifies what fraction of phenotypic variance is genetic. [[ld-score-regression|LD Score Regression]] estimates hÂ² from GWAS summary statistics alone, without individual-level data.

### Mendelian Randomization

[[mendelian-randomization|MR]] uses genetic variants as instruments to test causal effects â€” analogous to randomized controlled trials using natural genetic randomization.

## Related Clusters

- [[cluster-map-regulatory-genomics]] â€” Disease circuitry connects to enhancers and TFs
- [[cluster-map-epigenomics]] â€” Chromatin accessibility informs disease loci
- [[cluster-map-deep-learning]] â€” DL methods beginning to be applied to GWAS fine-mapping
