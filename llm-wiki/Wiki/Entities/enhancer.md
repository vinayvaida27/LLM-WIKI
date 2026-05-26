---
tags:
  - "entity"
topics:
  - "MLCB"
status: "compiled"
created: 2026-05-24
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_06_regulatory_circuitry.md"
  - "Raw/Sources/lecture_17_genetics_disease_gwas_prs_mechanism.md"
  - "Raw/Sources/lecture_18_disease_mechanism_circuitry_eqtls_heritability.md"
source_count: 3
aliases:
  - "Enhancer"
  - "Cis-regulatory element"
  - "Distal enhancer"
  - "Regulatory element"
entity_type: "biological_entity"
importance: "0.82"
lectures:
  - "lecture-06"
  - "lecture-17"
  - "lecture-18"
---

# Enhancer

An **enhancer** is a short (100â€“2000 bp) non-coding DNA sequence that increases transcription of its target gene(s). Unlike promoters (which sit immediately upstream of genes), enhancers can act at great distances â€” up to 1 Mb away â€” and from either orientation.

## Mechanism (Lecture 6)

The regulatory circuit:
1. **Transcription factors (TFs)** bind to specific sequence motifs within the enhancer
2. TF binding recruits co-activators and chromatin remodelers
3. The enhancer loops through 3D space to contact the target gene's **[[promoter]]**
4. This loop promotes binding of **RNA polymerase** and initiates **transcription**

The physical looping is mediated by cohesins and CTCF proteins and can be detected by Hi-C or ChIA-PET experiments.

## Histone Mark Signature

Active enhancers are identified epigenomically by characteristic histone modifications:

| Mark | Enhancer activity |
|---|---|
| H3K4me1 | Enhancer (both active and poised) |
| H3K27ac | Active enhancer |
| H3K27me3 | Repressed (Polycomb) |
| H3K4me3 | Promoter (NOT enhancer) |

This signature is what [[chromhmm|ChromHMM]] uses to assign chromatin states (Lecture 5).

## Disease Significance (Lectures 17, 18)

**93% of GWAS-identified disease variants lie in non-coding regions**, most of them in enhancers. This is why regulatory circuitry is central to understanding disease genetics:

- A SNP in an enhancer can disrupt a **TF binding motif**, changing TF occupancy
- Changed TF binding â†’ altered enhancer activity â†’ changed target gene expression
- Changed expression â†’ disease phenotype

Example (Lecture 17): The **FTO locus** (strongest obesity GWAS signal) contains a variant in an enhancer in pre-adipocytes that disrupts ARID5B binding, reducing IRX3/IRX5 expression and promoting obesity.

## Cell Type Specificity

An enhancer is **active only in specific cell types** â€” the same genomic coordinate is a quiescent region in most cell types and an active enhancer in others. This is determined by which TFs are expressed and available in that cell type.

This cell-type specificity explains why **partitioned heritability** analysis (Lecture 18) links GWAS traits to specific tissues: variants enriched in T-cell enhancers â†’ immune trait; variants enriched in cardiomyocyte enhancers â†’ cardiovascular trait.

## Linking Enhancers to Target Genes

Methods to assign enhancers to their regulated genes:
1. **Genomic proximity** â€” assign to nearest gene (simple but imprecise)
2. **[[eqtl|eQTL]] overlap** â€” if a GWAS variant is also an eQTL for gene X, that gene is the likely target
3. **Hi-C / 3D genome conformation** â€” measure physical loops
4. **Correlation** â€” correlate enhancer activity (ATAC-seq accessibility) with gene expression across cell types


## Graph Links

### Parent Topics
- [[topic-epigenomics|Epigenomics]]

## Related

[[promoter]], [[transcription-factor]], [[chromatin]], [[histone-modification]], [[chip-seq]], [[atac-seq]], [[eqtl]], [[disease-circuitry]], [[snp]]
