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
  - "SNP"
  - "Single Nucleotide Polymorphism"
  - "Variant"
  - "Genetic Variant"
entity_type: "biological_entity"
importance: "0.87"
lectures:
  - "lecture-17"
  - "lecture-18"
---

# Single Nucleotide Polymorphism (SNP)

A **Single Nucleotide Polymorphism (SNP)** is a position in the genome where a single DNA base differs between individuals in a population. SNPs are the most common type of genetic variation, occurring roughly once per 1,000 bases across the genome (~3 million SNPs per genome).

## Biology

At a SNP position, one individual might have cytosine (C) while another has guanine (G). These alternative forms are called **alleles**. The more common version is the **major allele**; the less common version is the **minor allele**.

Other types of genetic variation (from Lecture 17):
| Type | Frequency | Example |
|---|---|---|
| SNP | ~1 per 1,000 bp | C â†’ G substitution |
| Indel | ~1 per 10,000 bp | Insertion or deletion of bases |
| Short Tandem Repeat (STR) | Variable | GTC repeated N times |
| Copy Number Variant (CNV) | ~1 per 1 Mb | Deleted or duplicated gene region |

## Role in GWAS

[[gwas|GWAS]] tests each SNP across the genome for statistical association with a disease or trait. The key idea:

1. Genotype thousands of individuals at ~1 million SNP positions
2. Compare SNP frequencies between cases (disease) and controls (no disease)
3. A **Manhattan plot** shows âˆ’logâ‚â‚€(p-value) per SNP position; peaks indicate associated loci
4. Genome-wide significance threshold: p < 5 Ã— 10â»â¸ (correcting for ~1 million independent tests)

## Haplotype Blocks and LD

Nearby SNPs are often co-inherited as **haplotype blocks** â€” chunks of DNA between recombination hotspots. SNPs within a block are in **[[linkage-disequilibrium|linkage disequilibrium (LD)]]**, meaning knowing one SNP tells you about others in the same block. This makes GWAS peaks broad, complicating identification of the causal variant.

## Common vs. Rare Variants

| Property | Common SNPs (MAF > 5%) | Rare SNPs (MAF < 1%) |
|---|---|---|
| Effect size | Usually weak | Often stronger |
| Detectable by GWAS | Yes | Requires large sequencing cohorts |
| Selection pressure | Survived selection â†’ smaller effect | Strong effect â†’ under negative selection |

Exception: APOE Îµ4 (Alzheimer's risk) is common with strong effect â€” may reflect late-onset disease evading early selection.

## Classic Disease Examples (Lecture 17)

- **Sickle cell anemia** â€” single Aâ†’T substitution in HBB gene (glutamic acid â†’ valine); protective against malaria in heterozygotes
- **Huntington's disease** â€” expanded CAG repeat in HTT gene (>30 repeats â†’ neurodegeneration)
- **Cystic fibrosis** â€” deletion of 3 bp in CFTR gene â†’ misfolded channel protein

## Downstream Analysis

SNPs feed into:
- **[[polygenic-risk-score|PRS]]** â€” sum of GWAS effect sizes (Î² coefficients) per individual
- **[[eqtl|eQTL]]** analysis â€” SNPs associated with gene expression levels
- **Fine mapping** â€” identify the likely causal SNP within a GWAS peak using multi-ethnic data or Bayesian methods


## Graph Links

### Parent Topics
- [[topic-dna-language-models|DNA Language Models]]

## Related

[[gwas]], [[linkage-disequilibrium]], [[polygenic-risk-score]], [[eqtl]], [[heritability]], [[dna]]
