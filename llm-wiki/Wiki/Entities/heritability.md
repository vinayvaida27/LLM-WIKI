---
tags:
  - "entity"
topics:
  - "MLCB"
status: "compiled"
created: 2026-05-24
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_18_disease_mechanism_circuitry_eqtls_heritability.md"
source_count: 1
aliases:
  - "Heritability"
  - "SNP Heritability"
  - "hÂ²"
  - "h-squared"
entity_type: "concept"
importance: "0.82"
lectures:
  - "lecture-18"
---

# Heritability

**Heritability** (hÂ²) quantifies the proportion of phenotypic variation in a trait that is attributable to genetic differences between individuals. It answers: "How much of the variation in this trait across a population is due to genes vs. environment?"

## Key Distinction: Narrow-sense vs. Broad-sense

| Type | Symbol | What it captures |
|---|---|---|
| Narrow-sense heritability | hÂ² | Additive genetic effects (linear SNP effects) |
| Broad-sense heritability | HÂ² | All genetic effects including dominance, epistasis |

MLCB and GWAS work almost exclusively with **narrow-sense heritability**, which is what [[polygenic-risk-score|PRS]] estimates.

## SNP Heritability

**SNP heritability** is the proportion of trait variance explained by all common SNPs simultaneously, estimated using **LD Score Regression (LDSC)**:

```
Î§Â² = N Ã— hÂ²_SNP Ã— â„“_j + 1
```

where â„“_j is the LD score of SNP j (sum of rÂ² with all other SNPs), N is sample size, and Î§Â² is the chi-squared test statistic from GWAS. Regressing GWAS chi-squared statistics on LD scores yields hÂ²_SNP as the slope.

SNP heritability is typically lower than total narrow-sense heritability because rare variants and non-additive effects are not captured.

## Partitioned Heritability (Lecture 18)

The key innovation for disease mechanism discovery: partition hÂ² by **functional annotation**. Ask:

> "What fraction of total heritability is explained by SNPs that overlap enhancers active in T-cells?"

If variants in T-cell enhancers are enriched for heritability of an immune disease, this implicates T-cells as a key disease tissue.

**Method:** LDSC-SEG (stratified LDSC) â€” run LDSC while including annotation-specific LD scores. Significant enrichment = that tissue/annotation is biologically important for the trait.

## Examples from Lecture 17/18

| Trait | Enriched annotation |
|---|---|
| Height | Enhancers in embryonic stem cells |
| T1 diabetes / immune traits | T-cell and B-cell enhancers |
| Alzheimer's disease | Immune cell (microglial) enhancers â€” *surprising, not brain-specific* |

The Alzheimer's result was an early demonstration that combining epigenomics + genetics could reveal unexpected biology (immune component to AD).

## Missing Heritability

Even summing all GWAS hits often explains only a fraction of known trait heritability. This "missing heritability" comes from:
- Rare variants not captured by SNP arrays
- Small-effect common variants below GWAS significance threshold
- Gene-gene interactions (epistasis)
- Gene-environment interactions

PRS with large biobank data (UK Biobank, ~500K individuals) has substantially reduced missing heritability for some traits.


## Graph Links

### Parent Topics
- [[topic-epigenomics|Epigenomics]]

## Related

[[snp]], [[gwas]], [[polygenic-risk-score]], [[eqtl]], [[linkage-disequilibrium]], [[enhancer]]
