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
  - "Raw/Sources/lecture_07_regulatory_networks.md"
source_count: 2
aliases:
  - "Transcription Factor"
  - "TF"
  - "TFs"
  - "Regulatory Protein"
entity_type: "biological_entity"
importance: "0.87"
lectures:
  - "lecture-06"
  - "lecture-07"
---

# Transcription Factor (TF)

A **transcription factor (TF)** is a protein that binds to specific short DNA sequences (called **motifs** or **binding sites**) and regulates the transcription of nearby genes. TFs are the primary effectors of gene regulation â€” they interpret the combination of signals in a cell and determine which genes are turned on or off.

## Mechanism (Lecture 6)

TFs do not unzip DNA to read it; they interact with the **major groove of the DNA double helix**, feeling the pattern of hydrogen-bond donors and acceptors on the base pairs without breaking them apart. This interaction is sequence-specific: a TF has a preferred binding motif (e.g., a 6â€“20 bp sequence) and will bind only where that motif (or a close match) occurs.

The regulatory circuit:
```
TF protein â†’ binds motif in enhancer â†’ recruits coactivators â†’ loops to promoter â†’ initiates transcription
```

**DNA methylation** (specifically 5-methylcytosine) can block TF binding by altering the chemical pattern in the major groove.

## TF Binding Motifs

A TF's binding preference is represented as a **position weight matrix (PWM)** â€” a 4Ã—L matrix where each column gives the probability of each nucleotide (A/C/G/T) at that position of the motif. Databases of known TF motifs: JASPAR, ENCODE TFBS, HOCOMOCO.

Motif discovery methods (Lecture 6):
- **Enrichment analysis** â€” test known motifs for over-representation in open chromatin or ChIP-seq peaks
- **Expectation-Maximization (EM)** â€” de novo motif discovery without a prior motif database
- **Gibbs sampling** â€” probabilistic approach to motif finding
- **Deep learning (CNNs)** â€” learn sequence features predictive of TF binding or chromatin accessibility

## TFs in Gene Regulatory Networks (Lecture 7)

TFs are the **nodes** in gene regulatory networks ([[gene-regulatory-network|GRN]]). Key circuit motifs:
- **Autoregulation** â€” a TF binds its own promoter (positive feedback â†’ bistability; negative feedback â†’ oscillation or damping)
- **Feed-forward loop** â€” TF A activates TF B, and both together regulate target C
- **Mutual inhibition** â€” two TFs repress each other, creating a binary cell-fate switch

## Cell Type Identity

A cell type is largely defined by its **TF expression profile**. Master regulators (e.g., MyoD in muscle, Oct4/Sox2 in pluripotency) can reprogram cell identity. [[encode]] catalogues TF binding sites across hundreds of cell types and conditions.

## Role in Disease Genetics (Lecture 17/18)

Disease-associated [[snp|SNPs]] in [[enhancer|enhancers]] often disrupt TF binding motifs. When a SNP falls in a TF motif and is also an [[eqtl|eQTL]] for a nearby gene, it becomes strong evidence that the causal mechanism runs: SNP â†’ disrupted TF binding â†’ altered target gene expression â†’ disease.


## Graph Links

### Parent Topics
- [[topic-epigenomics|Epigenomics]]

## Related

[[enhancer]], [[promoter]], [[gene-regulatory-network]], [[chromatin]], [[chip-seq]], [[motif-finding]], [[eqtl]], [[dna]]
