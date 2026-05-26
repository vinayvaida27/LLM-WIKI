---
tags:
  - "entity"
topics:
  - "MLCB"
status: "compiled"
created: 2026-05-24
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_17_genetics_disease_gwas_prs_mechanism.md"
  - "Raw/Sources/lecture_18_disease_mechanism_circuitry_eqtls_heritability.md"
source_count: 2
aliases:
  - "eQTL"
  - "eQTLs"
  - "Expression Quantitative Trait Locus"
  - "Expression QTL"
entity_type: "concept"
importance: "0.87"
lectures:
  - "lecture-17"
  - "lecture-18"
---

# Expression Quantitative Trait Locus (eQTL)

An **expression quantitative trait locus (eQTL)** is a genomic position where a genetic variant ([[snp|SNP]]) is statistically associated with the expression level of a gene. eQTLs bridge the gap between GWAS associations (which identify disease-linked loci) and biological mechanisms (which require knowing which gene is affected and how).

## Motivation (Lecture 18)

93% of GWAS-identified variants lie in **non-coding regions** â€” they don't change protein sequence. eQTLs help explain *how* these non-coding variants affect biology: by modulating **gene expression** rather than protein structure.

## Types of eQTLs

| Type | Definition |
|---|---|
| **cis-eQTL** | SNP within ~1 Mb of the affected gene; most common type |
| **trans-eQTL** | SNP in a distal region (different chromosome or far locus) affecting gene expression |

cis-eQTLs are the primary target in MLCB because they provide direct local regulatory evidence.

## How eQTLs Are Mapped

1. Collect a cohort with both genotype data (SNP array) and gene expression data (RNA-seq)
2. For each gene, test each nearby SNP for association with expression level (linear regression: expression ~ genotype)
3. Report significant associations at FDR-corrected threshold
4. Result: a table of (SNP, gene, effect size, p-value) pairs

Key resource: **GTEx** (Genotype-Tissue Expression) â€” eQTL maps across 50+ human tissues from ~1000 donors.

## eQTLs and GWAS Colocalization

A GWAS hit may be an eQTL for a nearby gene in a disease-relevant tissue. **Colocalization analysis** tests whether the same variant drives both the GWAS signal and the eQTL signal (versus two distinct variants in LD with each other):

- If colocalized â†’ the variant likely affects disease by regulating that gene's expression
- Tools: coloc, SuSiE-coloc

## Mechanistic Interpretation

eQTL variants often overlap [[enhancer|enhancers]] and disrupt **transcription factor binding motifs**. The causal chain is:
```
SNP in enhancer â†’ disrupted TF binding â†’ altered chromatin state â†’ changed gene expression â†’ disease phenotype
```

Lecture 17 example: FTO locus (obesity GWAS peak) â€” fine-mapping and eQTL analysis revealed the causal variant disrupts an enhancer, reducing expression of IRX3/IRX5 in adipocytes.

## mQTLs

**Methylation QTLs (mQTLs)** are analogous: SNPs associated with DNA methylation levels. Both eQTLs and mQTLs are "molecular phenotype" QTLs used to link genetic variants to functional genomic changes.


## Graph Links

### Parent Topics
- [[topic-epigenomics|Epigenomics]]

## Related

[[snp]], [[gwas]], [[heritability]], [[enhancer]], [[transcription-factor]], [[gene]], [[disease-circuitry]]
