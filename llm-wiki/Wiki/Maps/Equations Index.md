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
  - "Raw/Sources/lecture_05_epigenomics_hmms.md"
  - "Raw/Sources/lecture_17_genetics_disease_gwas_prs_mechanism.md"
  - "Raw/Sources/lecture_15_generating_new_molecules.md"
  - "Raw/Sources/lecture_18_disease_mechanism_circuitry_eqtls_heritability.md"
source_count: 4
aliases:
  - "Equations Index"
  - "Metrics Index"
  - "Loss Functions Index"
---

# Equations and Metrics Index

> [!info] Mathematical equations, loss functions, and evaluation metrics appearing in MLCB. 2 named equations in KG; additional metrics listed from lectures.

## Named Equations in KG

| Equation | Lectures | Definition |
|---|---|---|
| [[elbo|ELBO]] | 15 | Evidence Lower BOund: objective for variational autoencoders. `ELBO = E_q[log p(x|z)] - KL(q(z|x) || p(z))` |
| [[cross-entropy-loss|Cross-Entropy Loss]] | 16 | Classification loss: `-Î£ y log(Å·)`. Also used as LM pre-training objective. |

## Evaluation Metrics (from lectures)

| Metric | Used In | Meaning |
|---|---|---|
| [[lddt-score|lDDT]] | 10 (AlphaFold2) | Local Distance Difference Test; measures local structural accuracy (0â€“100) |
| TM-score | 9, 10 | Template Modeling score; global structural similarity (0â€“1) |
| RMSD | 9, 10 | Root Mean Square Deviation of CÎ± atoms between predicted and true structure |
| AUROC | drug discovery | Area Under ROC Curve; classification performance |
| Spearman Ï | 11 | Rank correlation for fitness prediction benchmarks |

## Statistical Quantities

| Quantity | Context | Definition |
|---|---|---|
| p-value (GWAS) | 17 | Probability of seeing association by chance; threshold 5Ã—10â»â¸ |
| LD Score (â„“_j) | 18 | Sum of rÂ² between SNP j and all others; input to LDSC |
| Beta coefficient (Î²) | 17 | Effect size per SNP in GWAS / PRS calculation |
| KL Divergence | 15 | `KL(q||p) = Î£ q log(q/p)`; regularizer in VAE |
| Posterior probability | 5,18 | P(hidden state | observed data); output of HMM forward-backward |

## Key Identities / Equations from Lectures

**Viterbi recurrence** (Lecture 5):
```
V_t(k) = max_j [ V_{t-1}(j) Â· a_{jk} ] Â· b_k(x_t)
```

**PRS calculation** (Lecture 17):
```
PRS_i = Î£_j Î²_j Â· G_{ij}
```
where Î²_j is effect size from GWAS, G_ij is allele count at SNP j for individual i.

**ELBO** (Lecture 15):
```
log p(x) â‰¥ E_q[log p(x|z)] - KL[q(z|x) || p(z)]
```

**LD Score Regression** (Lecture 18):
```
E[Ï‡Â²_j] = N hÂ²_SNP â„“_j / M + 1
```

## Navigation

[[Course Graph Map]] Â· [[Methods Index]] Â· [[Models Index]]
