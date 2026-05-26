---
tags:
  - "topic"
topics:
  - "MLCB"
status: updated
created: 2026-05-24
updated: 2026-05-24
sources:
  - "Raw/Sources/lecture_18_disease_mechanism_circuitry_eqtls_heritability.md"
source_count: 1
aliases:
  - "Lecture 18 - Disease Mechanism, Circuitry, eQTLs, Heritability"
---

# Lecture 18 - Disease Mechanism, Circuitry, eQTLs, Heritability

## Source
- Raw source: `Raw/Sources/lecture_18_disease_mechanism_circuitry_eqtls_heritability.md`
- Supporting source: `Raw/Files/lecture_18_disease_mechanism_circuitry_eqtls_heritability.md`
- Existing related pages: [[mlcb-2024-computational-biology]], [[mlcb-complete-study-guide]], [[mlcb-methods-map]]
- Last updated: 2026-05-24

## Executive Summary
Lecture 18 - Disease Mechanism, Circuitry, eQTLs, Heritability develops eQTLs, meQTLs, mediation, Mendelian randomization, heritability, GCTA, partitioned heritability, integrative disease mechanism, and the FTO obesity locus. This page intentionally preserves substantial source detail so a future LLM can reason from the wiki without immediately reopening the raw transcript.

The lecture should be read as a sequence of modeling decisions. A biological system is measured, represented as data, modeled computationally, and then interpreted back in biological terms. The goal is not only prediction; the goal is to understand what the model reveals and where it may fail.

## Why This Lecture Matters
This lecture contributes to the course-wide bridge between machine learning and biological mechanism. It teaches how to convert messy biological observations into computable structures while keeping track of assumptions, limitations, and experimental meaning.

## Core Learning Objectives
- Explain the main biological problem.
- Explain the main computational problem.
- Identify the input data type and model output.
- Describe the professor's reasoning flow.
- Connect the lecture to earlier and later lectures.
- Identify important algorithms and assumptions.
- Explain examples without losing biological context.
- Use the lecture page for study and review questions.

## Professor's Main Narrative
The lecture develops these major sections:
- Lecture Overview
- Review: Genetics, Variation, GWAS, Polygenic scores (PGS)
- From GWAS to Biological Insights
- Bayesian Fine-Mapping
- Sub-threshold Region Prioritization
- GWAS locus dissection: enriched tissues, driver SNPs, target genes
- Partitioning complex traits into tissue-specific components
- From Individual GWAS Region to Mechanism and Circuitry
- Introduction to the FTO locus, the strongest Genetic Association with Obesity
- Step 1: Establishing the Relevant Tissue and Cell Type

## Detailed Lecture Notes
The notes below preserve the processed source order and are intentionally detailed.

# [[Lecture 18 - Disease Mechanism, circuitry, eQTLs, heritability]]

Video: [Lecture18 - Disease Mechanism - MLCB24](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18)

Slides: [Lecture18_DiseaseMechanism_Circuitry_eQTLs_Heritability.pdf](https://www.dropbox.com/scl/fi/chv55jui6dq8gxewu7xph/Lecture18_DiseaseMechanism_Circuitry_eQTLs_Heritability.pdf?rlkey=tfr2evrvtvxplbavzqrbhfuci&dl=0)

## [00:00](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=0s) Lecture Overview

In todayÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s lecture, we transition from broad genetic analyses to the **mechanistic understanding of disease** using individual loci and biological pathways. We will cover:

1.  **Disease Mechanism and Circuitry**: From genome-wide associations to the functional interpretation of individual loci.
2.  **Expression Quantitative Trait Loci (eQTLs)** and **Methylation Quantitative Trait Loci (mQTLs)**: Using molecular traits to link genetic variants to phenotypes.
3.  **Mediation Analysis and Mendelian Randomization**: Distinguishing the causal pathways between molecular phenotypes and diseases.
4.  **Heritability Analysis**: Quantifying the genetic contribution to disease and attributing it to specific biological pathways.

This lecture aims to provide a deeper understanding of how genetic differences translate into molecular changes and ultimately manifest as disease phenotypes.

### From Genome-Wide Insights to Individual Mechanisms

In previous discussions on **Genome-Wide Association Studies (GWAS)**, we identified **genetic loci** associated with diseases using statistical associations across the entire genome. We also introduced **Polygenic Risk Scores (PGS)**, which aggregate the effects of multiple genetic variants to predict an individual's genetic predisposition to a disease.

These analyses provide **global insights** by highlighting genetic regions enriched for associations with specific diseases. However, this global view needs to be refined to understand **individual mechanisms** and how **specific loci** contribute to the biology of the disease.

**Key Question**: How do we transition from identifying disease-associated loci to understanding their functional role in disease mechanisms?

To address this, we will:

- Investigate **individual loci** to uncover the underlying biological processes.
- Use **functional annotations** to interpret the impact of genetic variants on regulatory elements, such as enhancers, promoters, and non-coding RNAs.
- Explore **molecular phenotypes** (e.g., gene expression and methylation) to link genetic variants to cellular functions.

### Understanding Quantitative Trait Loci (QTLs)

**Quantitative Trait Loci (QTLs)** are genomic regions associated with quantitative traits, which can vary continuously rather than being binary (e.g., height, cholesterol levels). Unlike case-control studies that categorize individuals into disease versus no disease, QTL analyses focus on **traits with continuous distributions**.

- **eQTLs**: Identify loci where genetic variants influence the expression levels of genes. These loci provide insights into how genetic differences modulate **gene regulation** and expression, impacting cellular functions.
- **mQTLs**: Identify loci affecting DNA methylation levels, a key epigenetic modification influencing gene activity and regulation.

**Key Insight**: Both eQTLs and mQTLs provide a **local view** of genetic influence, linking nearby genetic variants to molecular phenotypes. This local linkage, often called **cis-regulation**, offers a direct path to understanding how specific genetic changes impact gene function.

#### Using Molecular Traits to Understand Disease

Molecular traits like gene expression can serve as **intermediary phenotypes**, bridging the gap between genetic variation and disease. By associating genetic variants with changes in gene expression (eQTLs), we can:

- Identify **regulatory variants** that alter gene function.
- Link these changes to broader **biological pathways** and ultimately to disease phenotypes.

This approach allows us to move from a **statistical association** to a **mechanistic understanding**, where we can trace how a specific genetic variant impacts gene expression and contributes to the disease process.

### Mediation Analysis and Mendelian Randomization

When studying the relationship between genetic variants, molecular phenotypes, and disease, we often encounter scenarios where multiple factors are interconnected. For example, we might observe genetic variants associated with both **lipid metabolism** and **obesity**. This raises a fundamental question:

- **Is the genetic association with obesity mediated through lipid metabolism, or is lipid metabolism a consequence of obesity?**

To address this, we use:

1.  **Mediation Analysis**: This technique helps us test whether the effect of a genetic variant on a disease phenotype is **mediated** through an intermediate trait (e.g., gene expression or lipid levels).
    - We examine whether controlling for the intermediate trait (e.g., lipid levels) reduces the association between the genetic variant and the disease (e.g., obesity).
    - If the association is reduced, it suggests that the intermediate trait mediates the genetic effect on the disease.
2.  **Mendelian Randomization**: This method leverages genetic variants as **instrumental variables** to infer causal relationships. It relies on the principle that genetic variants are randomly inherited and can be used to test causality, distinguishing between direct effects and mediated effects.
    - For instance, if genetic variants associated with lipid metabolism also predict obesity when controlling for lipid levels, this suggests a direct effect of these variants on obesity.
    - Conversely, if the association diminishes when adjusting for lipid levels, it suggests that the effect is mediated through lipid metabolism.

**Key Insight**: Mediation analysis and Mendelian randomization help us **disentangle complex biological relationships**, clarifying whether molecular changes are a cause or consequence of disease.

### Heritability and Pathway-Specific Contributions

**Heritability** quantifies the proportion of variation in a trait that can be attributed to genetic differences. In the context of complex diseases:

- We use **partitioned heritability** to determine the **contribution of specific biological pathways** to the overall genetic risk of a disease.
- For example, we might ask, "What fraction of the heritability of obesity can be explained by genetic variants affecting lipid metabolism?"

This approach allows us to connect **global genetic risk** to specific **biological processes**, providing a systems-level view of how genetic factors drive disease.

**Key Insight**: By estimating the heritability attributed to different pathways, we can identify the most relevant biological mechanisms and prioritize them for further investigation and therapeutic targeting.

### Systems-Level Understanding of Disease Mechanisms

In summary, todayÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s lecture builds on the foundation of GWAS and PGS by delving deeper into the **circuitry of genetic regulation**:

1.  We use **molecular QTLs** to link genetic variants to specific gene regulatory effects.
2.  We apply **mediation analysis** and **Mendelian randomization** to infer causal relationships between molecular traits and disease.
3.  We assess **heritability partitioning** to attribute genetic risk to specific biological pathways.

Together, these tools allow us to move beyond statistical associations and towards a comprehensive, **mechanistic understanding of disease**, paving the way for novel therapeutic strategies and personalized medicine.

## [05:39](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=339s) Review: Genetics, Variation, GWAS, Polygenic scores (PGS)

In our last lecture, we delved into the **fundamental principles of genetics and variation**, focusing on the identification of disease-associated loci through **genome-wide association studies (GWAS)**, the interpretation of these findings, and the use of **polygenic scores (PGS)** to predict individual risk.

### Understanding Genetic Variants and Disease Association

**Genetic variants** are differences in the DNA sequence between individuals, often represented as **single nucleotide polymorphisms (SNPs)**. These can have **protective effects** (shown in green) or **increase disease risk** (shown in red). Using GWAS, we perform a statistical analysis across the entire genome to identify variants associated with specific diseases.

**GWAS Results** are typically visualized using a **Manhattan plot**, where:

- The **x-axis** represents the genomic coordinates across chromosomes.
- The **y-axis** shows the statistical significance of the association (e.g., p-value) for each SNP.

Peaks in the Manhattan plot indicate **non-random associations** between genetic variants and the disease. For example, a peak might suggest a strong association with age-related macular degeneration. These signals highlight regions of interest but do not immediately reveal the **mechanisms** by which these variants affect disease.

### Challenges in Interpreting GWAS Results

The main challenge lies in translating these associations into **biological mechanisms**:

1.  **Cataloging Variants**: Identifying all genetic variants associated with a disease and creating a comprehensive list.
2.  **Systematic Association**: Analyzing these variants to determine their potential impact on biological processes and pathways.
3.  **Understanding Mechanisms**: Deciphering how these variants influence gene expression, protein function, and cellular processes.
4.  **Translating Insights into Action**: Using these findings to inform **therapeutic interventions**, such as selecting target proteins or developing specific drugs.

The goal is to move from **broad statistical associations** to **precise functional insights** that guide therapeutic strategies.

### Recombination and Fine Mapping

We discussed how **genetic linkage** is shaped by the structure of the genome, specifically through **haplotype blocks**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âregions of the genome that are inherited together due to limited recombination between them. Within these blocks, SNPs are often in **linkage disequilibrium (LD)**, meaning that they are correlated and inherited together.

To pinpoint the **causal variants** within these blocks, we use **fine mapping**, which can be achieved through:

1.  **Genetic Fine Mapping**: Leveraging rare recombination events within haplotype blocks to narrow down the list of candidate variants.
2.  **Transethnic Associations**: Analyzing GWAS data from diverse populations (e.g., African, Asian, European) to exploit differences in LD structure. If a variant shows consistent association across populations with different haplotypes, it is more likely to be the true causal variant.

This approach helps in **identifying the specific variants** driving the disease association, despite the complex LD patterns across populations.

### Common vs. Rare Variants: A Spectrum of Genetic Effects

There is a fundamental distinction between **common variants** and **rare variants** in terms of their **effect size**:

- **Common Variants**: Found in a large proportion of the population, these variants typically have a **weak effect** on disease risk. If they had strong effects, they would be subject to **negative selection**, reducing their frequency.
- **Rare Variants**: These are often **high-effect variants**, but they remain rare because they are typically deleterious and subject to strong **selective pressure**, maintaining them at low frequencies.

GWAS primarily identifies **common, weak-effect variants**, but integrating data on rare variants can provide additional insights into the genetic architecture of diseases.

### Polygenic Scores (PGS): Aggregating Genetic Risk

While individual variants may have modest effects, collectively they can provide substantial predictive power when combined into a **polygenic score (PGS)**. A PGS aggregates the effects of many SNPs across the genome, each weighted by its effect size, to generate an overall **risk score** for an individual.

**The Predictive Power of Polygenic Scores.** PGS can explain a significant portion of an individual's **genetic risk** for a given disease. However, PGS does not capture the entire genetic risk explained by **family history**, which combines both **common and rare variants** as well as **environmental factors**.

**Key Question**: Why does PGS leave some residual risk unexplained, even when accounting for family history?

The answer lies in **genetic inheritance**:

- Each individual inherits a **unique combination of alleles** from their parents. Even though two siblings share the same parents, the specific alleles they inherit can differ significantly.
- On average, siblings share **50% of their genome**. For any given locus:
    - **25% of the genome** will be identical (both siblings inherited the same allele from the same grandparent).
    - **25% of the genome** will be completely different (each sibling inherited a different allele from different grandparents).
    - **50% of the genome** will be partially identical (one shared and one non-shared allele).

This variation between siblings means that **family history** provides a general risk estimate based on shared genetics, but **PGS** offers a more precise estimate by directly examining the specific alleles an individual inherited.

**Integrating PGS into Disease Risk Prediction.** The use of PGS has become a powerful tool in **predictive genetics**, enabling us to:

- Identify individuals at **high genetic risk** for specific diseases.
- Enhance the precision of **preventive measures** and **therapeutic interventions**.
- Provide personalized insights that go beyond traditional family history.

However, PGS is only one part of the picture. To fully understand disease risk, we need to integrate PGS with other factors, such as **environmental exposures**, **lifestyle**, and **molecular phenotypes** (e.g., gene expression, epigenetic changes).

### Summary

- **GWAS** helps identify genetic variants associated with diseases, but interpreting these associations requires further investigation to uncover the **functional mechanisms**.
- **Fine mapping** and **transethnic analyses** help pinpoint the causal variants, moving beyond simple statistical associations.
- **Polygenic scores (PGS)** aggregate the effects of multiple variants, providing a comprehensive estimate of genetic risk but still leave residual variation due to differences in inherited alleles.
- Understanding the interplay between common and rare variants, genetic inheritance patterns, and environmental factors is essential for translating these insights into **clinical practice**.

The next step is to go from these **global genetic insights** to understanding the **molecular mechanisms** and **biological pathways** that underlie complex diseases. This sets the stage for todayÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s focus on **disease mechanism and circuitry**, where we will dive deeper into how genetic variants influence gene regulation, expression, and ultimately, disease phenotypes.

## [11:16](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=676s) From GWAS to Biological Insights

Building upon our understanding of **genetic variation and GWAS**, we can use **genome-wide enrichment analyses** to gain insight into the specific biological pathways, tissues, and mechanisms that underlie complex traits and diseases. This approach enables us to move from a high-level association across the genome to more focused hypotheses about where and how these associations might act.

### Enrichment Analysis Across Functional Annotations

Using GWAS results, we can aggregate all genetic variants associated with a trait (e.g., height, type 1 diabetes, blood pressure, or cholesterol) and investigate their **enrichment across various functional annotations**. Each annotation corresponds to a specific biological feature, such as:

- **Enhancers** active in certain cell types (e.g., stem cells, immune cells, heart cells, liver cells).
- **Epigenomic markers** such as histone modifications, DNA methylation states, or chromatin accessibility regions.

The idea here is to correlate the **genetic variants associated with a trait** (aggregated across the entire genome) with **functional genomic features** (enhancers or accessible chromatin regions in different tissues). This correlation reveals whether variants for a specific trait are enriched in regulatory elements specific to certain tissues, potentially implicating those tissues in the traitÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s mechanism.

### Interpreting Rows and Columns in Enrichment Matrices

To interpret these data, we structure our matrix as follows:

- **Rows** represent all genetic variants associated with a given trait.
- **Columns** represent various epigenomic annotations, such as enhancers or other regulatory elements in specific tissues.

For instance, one column could include all enhancers active in **liver cells**, while another represents enhancers in **immune cells**. By calculating the **enrichment score** for each row-column combination, we can see how genetic variants linked to specific traits overlap with tissue-specific enhancers. This alignment between genetic risk loci and tissue-specific regulatory elements helps prioritize tissues for further analysis.

However, this enrichment analysis can be complex due to **varied background expectations**. Calculating the overlap by chance requires careful consideration of the **denominator** for each column, which could be:

- **The entire genome** (a broad background).
- **Accessible genome regions** (focused only on regulatory regions).

These choices can introduce biases due to the differing distributions of SNPs and accessible chromatin regions across tissues. By comparing all tissues against one another in a comprehensive matrix, we can reduce such biases through **internal controls** and better isolate genuine signals.

### Case Study: Alzheimer's Disease and Immune Cells

An example of this approach is evident in **AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s disease**, where GWAS initially suggested a strong association with genetic variants in **immune cell enhancers** rather than brain-specific enhancers. This unexpected finding prompted a deeper investigation:

- Using a **mouse model** of AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s, we analyzed gene expression changes across disease progression.
- The analysis showed that **early changes** in AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s predominantly occurred in **immune cells**, while **neuronal changes** emerged later.

Together, these findings led us to hypothesize an **immune basis for AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s disease**, where initial immune dysregulation might contribute to or exacerbate neurodegeneration. This hypothesis was further validated by studies from other research groups, supporting an immune involvement in AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s.

### Building Networks of Traits and Tissues

Expanding this framework, we can construct **network diagrams** where nodes represent **traits** and **tissues**. In this network:

- **Circles** represent different tissues (e.g., brain, heart, liver).
- **Rounded rectangles** represent traits (e.g., AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s, ADHD, height).
- Edges between nodes indicate **significant enrichment** between a tissue and a trait.

For example, **AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s disease** shows connections with immune cell tissues, while **ADHD** connects with brain tissue, and **height** with stem cell-associated enhancers. Such a network captures the connections between **genetic architecture and biological pathways** across multiple traits, providing a comprehensive view of trait-specific tissue involvement.

### Expanding to Comprehensive Genomic Datasets

We can also analyze more extensive datasets, such as **hundreds of GWAS studies** versus **thousands of reference epigenomes**. This broader view categorizes traits into three major groups:

1.  **Multifactorial Traits**: These traits, such as bone mineral density and blood cell counts, show enrichment across multiple tissues, reflecting their widespread biological impact.
2.  **Polyfactorial Traits**: Traits that enrich in a limited number of related tissues but are not universal. They display moderate tissue specificity.
3.  **Unifactorial Traits**: These traits localize to specific tissues. For instance, **cognitive traits** localize to the brain, while **cholesterol** traits localize to the liver.

This categorization helps **partition traits by their tissue-specific enrichments**, providing a roadmap for selecting the appropriate tissues when investigating trait mechanisms.

### Implications for Studying Molecular Traits

With tissue-specific insights, we can decide where to focus for **expression quantitative trait loci (eQTL)** and other molecular analyses. For example:

- **Cognitive and psychiatric traits** (e.g., schizophrenia, cognitive performance) may be best studied in **brain tissue**.
- **Cardiac traits** like heart repolarization localize to **heart-specific enhancers**.
- **Cholesterol traits** align with **liver tissue**.

By selecting the relevant tissue, we can more effectively study **gene expression changes** and other regulatory modifications that link genetic variants to disease.

### From Global Enrichment to Individual Variant Prioritization

Finally, we can return to **individual loci** within GWAS signals and prioritize specific variants likely to be **causal** based on tissue enrichment:

1.  **Empirical Prior from Genome-Wide Enrichment**: Across the genome, we calculate empirical priors for variants based on their enrichment in particular tissues.
2.  **Fine Mapping of Causal Variants**: For a trait associated with multiple tissues, we prioritize variants that overlap with the tissue showing the strongest enrichment (e.g., immune enhancers for AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s).

This empirical approach helps us focus on the variants most likely to contribute to disease in a given tissue, refining our understanding of **disease mechanism and circuitry**. Through these integrated analyses, we transition from genome-wide patterns to specific hypotheses about how genetic variants impact cellular function and ultimately influence disease.

## [22:55](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=1375s) Bayesian Fine-Mapping

With genome-wide association studies (GWAS), we identify **regions of the genome** associated with complex traits and diseases. However, due to **linkage disequilibrium (LD)** ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â the non-random association of nearby variants ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â it is challenging to pinpoint the exact causal variants within these associated regions. **Bayesian fine-mapping** provides a probabilistic framework to integrate multiple sources of information, helping us prioritize variants that are most likely to be **causal**.

### Components of Bayesian Fine-Mapping

Bayesian fine-mapping combines three key pieces of information:

1.  **Association Evidence** (Effect Size):
    - From GWAS, we obtain **association statistics** for each variant, typically represented as effect sizes or p-values. This information captures the strength of the association between each variant and the trait of interest.
2.  **Linkage Disequilibrium (LD) Structure**:
    - Variants within a genomic region are often correlated due to **LD**, making it difficult to disentangle their individual effects. We use the **LD matrix**, which represents the correlation between pairs of variants, to account for this structure. The **co-association** of variants in LD provides clues about where the true causal signal might be.
3.  **Empirical Priors from Functional Annotations**:
    - By leveraging **epigenomic data**, we can assign **empirical priors** based on the overlap of variants with specific functional annotations (e.g., enhancers, promoters). Variants that overlap with relevant annotations, such as immune cell enhancers for immune-related traits, are assigned higher priors, increasing their likelihood of being causal.

### Combining Evidence: Posterior Probability

The goal of Bayesian fine-mapping is to compute a **posterior probability** for each variant, representing the likelihood that it is causal. This is achieved through the following steps:

1.  **Likelihood Calculation**:
    - The likelihood is derived from the **genetic association evidence** alone, reflecting how well the variant's effect size explains the observed GWAS signal.
2.  **Prior Assignment**:
    - The prior probability is informed by **functional annotations**, such as overlap with enhancers, evolutionary conservation, or eQTLs (expression quantitative trait loci). Variants overlapping relevant annotations receive higher priors.
3.  **Posterior Computation**:
    - The **posterior probability** is calculated by combining the likelihood and the prior using Bayes' theorem. This posterior probability reflects the updated belief about a variantÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s causality after considering both the association evidence and functional annotation data.

Mathematically, this can be represented as:

Posterior ProbabilityÃƒÂ¢Ã‹â€ Ã‚ÂLikelihoodÃƒÆ’Ã¢â‚¬â€Prior\\text{Posterior Probability} \\propto \\text{Likelihood} \\times \\text{Prior}Posterior ProbabilityÃƒÂ¢Ã‹â€ Ã‚ÂLikelihoodÃƒÆ’Ã¢â‚¬â€Prior

### Examples of Bayesian Fine-Mapping

Let's look at a few examples where Bayesian fine-mapping has provided deeper insights:

1.  **Crohn's Disease**:
    - In a genetic region associated with CrohnÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s disease, the raw association evidence highlights several potential causal variants. However, by integrating functional annotations specific to **immune enhancers**, we find that a subset of these variants overlaps immune-specific annotations. Bayesian fine-mapping then **prioritizes** these overlapping variants as the most likely causal ones, consistent with the immune-mediated nature of CrohnÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s disease.
2.  **Schizophrenia**:
    - For schizophrenia, the functional annotations enriched for central nervous system (CNS) activity are most relevant. Bayesian fine-mapping highlights variants overlapping CNS enhancers, significantly narrowing down the list of candidates. This prioritization aligns with the known involvement of brain function in schizophrenia, suggesting these variants may impact gene regulation in neural tissues.

### Validating Fine-Mapped Variants

A critical step in fine-mapping is validating that the prioritized variants have true biological relevance. Two common approaches for validation include:

1.  **Evolutionary Conservation**:
    - Fine-mapped variants often overlap **evolutionarily conserved elements**, which are regions of the genome that have remained unchanged across species due to selective pressures. The rationale is that causal variants affecting important biological functions are more likely to be conserved. In practice, fine-mapped variants show **increased overlap with conserved elements**, suggesting they play essential roles in gene regulation.
2.  **Expression Quantitative Trait Loci (eQTLs)**:
    - Fine-mapped variants are also more likely to overlap with **eQTLs**, which are genetic variants associated with changes in gene expression. This overlap indicates that the prioritized variants might exert their effects through altering gene expression levels, providing a direct molecular mechanism linking genotype to phenotype.

For example, using data from the **Genotype-Tissue Expression (GTEx) Project**, researchers have shown that fine-mapped variants are significantly enriched for eQTLs across relevant tissues. This supports the hypothesis that these variants contribute to disease risk by regulating gene expression in a tissue-specific manner.

### Summary

Bayesian fine-mapping provides a powerful framework to integrate diverse sources of information ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â GWAS signals, LD structure, and functional annotations ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â to pinpoint causal variants with high confidence. The approach helps overcome the challenges posed by linkage disequilibrium and the sheer number of associated variants, enabling us to:

- **Prioritize variants** that are most likely to be functional.
- **Reduce the search space** for causal variants, facilitating experimental follow-up.
- **Gain deeper biological insights** into the regulatory mechanisms underlying complex traits.

By leveraging both statistical association evidence and functional genomic data, Bayesian fine-mapping moves us closer to understanding the **molecular mechanisms** driving complex diseases, paving the way for more targeted therapeutic interventions.

## [26:06](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=1566s) Sub-threshold Region Prioritization

While Bayesian fine-mapping helps pinpoint the most likely **causal variants** within genome-wide significant loci (regions that show a strong association with a trait), there remains a vast number of **sub-threshold regions** ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â regions that do not meet genome-wide significance but may still harbor variants with true biological relevance. By incorporating **additional biological evidence**, we can prioritize these sub-threshold regions, increasing our ability to detect meaningful signals that might otherwise be overlooked.

### Challenge of Sub-threshold Regions

In GWAS, we often focus on loci that surpass a stringent **p-value threshold** (e.g., p < 5 ÃƒÆ’Ã¢â‚¬â€ 10ÃƒÂ¢Ã‚ÂÃ‚Â»ÃƒÂ¢Ã‚ÂÃ‚Â¸). However, many true signals might fall below this threshold, especially in the case of:

- **Complex traits** with polygenic architectures, where individual variants have small effect sizes.
- **Limited sample sizes**, which reduce statistical power to detect associations, particularly for variants with modest effects.

Thus, relying solely on the significance threshold may lead to missed opportunities for identifying important genetic regions. This is where **integrative methods** come into play.

### Leveraging Epigenomic Annotations

To address this, we can use **epigenomic annotations** as additional lines of evidence to help prioritize sub-threshold regions. These annotations, derived from functional genomics data, capture information about regulatory activity across the genome. For instance:

- **Enhancer activity** (e.g., H3K27 acetylation marks indicating active enhancers).
- **DNA hypomethylation**, often associated with regulatory elements.
- **Primate conservation**, highlighting regions that are evolutionarily conserved and likely functional.

By integrating these annotations, we can build a model that predicts the **functional potential** of sub-threshold loci, allowing us to identify regions that are more likely to be **true positives** despite not reaching genome-wide significance.

### Machine Learning Approach for Prioritization

To systematically prioritize sub-threshold regions, we employed a **machine learning classifier** trained on a diverse set of features derived from:

1.  **Epigenomic annotations**: Including enhancer marks, histone modifications, DNA methylation states, and chromatin accessibility signals.
2.  **Evolutionary conservation**: Using metrics of primate conservation to identify regions likely under selective pressure.
3.  **Regulatory evidence**: Incorporating data on known transcription factor binding sites and gene regulatory elements.

The model was trained to distinguish between **genome-wide significant loci** (as positive examples) and random regions or regions showing no evidence of association (as negative examples). The output was a **predictive score** for each sub-threshold region, indicating its likelihood of being truly functional.

### Experimental Validation of Prioritized Regions

We did not stop at computational predictions; we conducted **experimental validation** to confirm the biological relevance of the prioritized sub-threshold loci. This included:

1.  **Luciferase Reporter Assays**:
    - We cloned candidate enhancer regions upstream of a luciferase gene. If the region is functional, it would drive **increased luciferase activity**, indicating enhancer potential.
2.  **Promoter Capture Hi-C**:
    - This technique maps physical interactions between enhancers and promoters. We used it to identify **target genes** of the prioritized regulatory regions, providing further evidence of their role in gene regulation.
3.  **CRISPR Knockout Experiments**:
    - Using **CRISPR/Cas9**, we knocked out the prioritized sub-threshold loci in mouse models. We then assessed **phenotypic changes**, such as alterations in heart repolarization interval (QRS interval), to determine the functional impact of the knocked-out regions.

### Case Study: Heart Repolarization Interval

In one application focused on the **QRS interval** (a measure of heart repolarization), we used this approach to identify **sub-threshold loci** that were predicted to be functional based on their overlap with relevant enhancer annotations. Although these loci did not initially meet the genome-wide significance threshold, our integrative analysis prioritized them for follow-up studies.

- **CRISPR knockout** experiments in mice revealed that disrupting these loci led to significant changes in the heart repolarization interval, providing **causal evidence** for their involvement in cardiac function.
- This finding underscores the power of using **additional biological evidence** to uncover functional loci that might otherwise be missed by GWAS alone.

### Building Interactive Tools for Prioritization

Given the utility of integrating various types of evidence, we have developed **interactive browsers** and computational tools that allow researchers to:

1.  **Visualize epigenomic data**: Overlay functional annotations on the genome alongside GWAS signals.
2.  **Apply machine learning models**: Automatically score and prioritize sub-threshold regions based on their functional potential.
3.  **Nominate candidate variants and loci**: Facilitate hypothesis generation for experimental follow-up.

These tools enhance our ability to interpret the vast amount of **sub-threshold genetic data**, transforming how we prioritize regions for further study.

### Summary

**Sub-threshold region prioritization** is a critical extension of GWAS that leverages **epigenomic data, machine learning, and experimental validation** to uncover functional loci beyond the strict genome-wide significance threshold. This integrative approach allows us to:

- Identify **additional loci** that contribute to complex traits.
- Gain deeper insights into the **regulatory mechanisms** underlying genetic associations.
- Enable **targeted experimental follow-up**, increasing our chances of discovering true biological signals.

By incorporating these methods, we move beyond a binary view of significant versus non-significant loci, embracing a more nuanced approach that captures the complexity of the genome and its regulation.

## [27:52](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=1672s) GWAS locus dissection: enriched tissues, driver SNPs, target genes

Genome-Wide Association Studies (GWAS) provide a powerful framework for identifying genetic loci associated with complex traits and diseases. However, translating these **associations** into mechanistic insights requires a deeper dissection of the implicated loci to pinpoint:

1.  **Driver SNPs**: The specific variants likely causing the association.
2.  **Enriched Tissues**: The tissues or cell types where the genetic variants are most likely to exert their functional effects.
3.  **Target Genes**: The genes whose regulation is affected by these variants.

### Systematic Annotation and Resource Development

To facilitate the dissection of GWAS loci, we have developed several resources and methodologies across multiple projects, such as:

- **HaploReg (HaoR)**: A tool designed for exploring the regulatory potential of SNPs within linkage disequilibrium (LD) blocks, focusing on how variants may impact regulatory elements like enhancers.
- **eQTL Mapping Projects (ePAP)**: Epigenomic mapping efforts that integrate functional genomic data across diverse tissues and cell types, enabling us to connect SNPs to regulatory elements and gene expression changes.

These resources allow us to systematically annotate and interpret individual SNPs, loci, and tissues, providing insights into the specific **biological context** of each association.

### Example: Breast Cancer Locus Dissection

Consider a GWAS for **breast cancer**. To understand the tissue-specific relevance of the implicated SNPs, we first examine the **enriched tissues** for this trait. Using the epigenomic annotations from ePAP, we observe that:

- The **most enriched tissues** for breast cancer-associated SNPs are, as expected, breast-related tissues such as **breast epithelium** and **breast cancer cell lines**.
- This strong tissue-specific signal suggests that the variants are likely overlapping enhancers that are **active in breast tissues**, rather than enhancers from unrelated tissues like brain or liver.

By leveraging these tissue-specific annotations, we can **narrow down the candidate SNPs** most likely to be driving the association. Furthermore, we can identify potential **target genes** by examining the correlated activity between the enhancers overlapping the SNPs and nearby gene expression.

### Example: Schizophrenia Locus Dissection

In the case of **schizophrenia**, the dissection process follows a similar approach but focuses on **brain-specific tissues** and cell types. Here, we find:

- The **most enriched tissues** include mid-frontal cortex, cerebellum, and various neural progenitor cells, indicating that the implicated variants are likely affecting brain-specific regulatory elements.
- For example, a particular SNP near the **DCP1B gene** is identified within an **enhancer** that is highly active in brain tissues. This SNP is linked to a gene that is also expressed specifically in the brain, suggesting a direct regulatory mechanism impacting neural gene expression.

### Systematic Identification of Driver SNPs

To move from statistical associations to **causal insights**, we can use a combination of:

1.  **Epigenomic Annotation Overlap**:
    - By mapping the SNPs to **active enhancers** in the enriched tissues, we prioritize variants that are more likely to affect gene regulation.
2.  **Expression Quantitative Trait Loci (eQTL) Data**:
    - Integrating eQTL data helps us establish direct links between the prioritized SNPs and changes in gene expression. SNPs that are also eQTLs for genes expressed in the relevant tissues are strong candidates for **driver SNPs**.
3.  **Linkage Disequilibrium (LD) Structure**:
    - We account for the **LD structure** of the loci, which helps us differentiate between variants that are simply correlated and those that are more likely to be **causal** based on their functional annotations.

### Nominating Target Genes

Once we have identified the likely **driver SNPs**, the next step is to link these SNPs to their **target genes**. This involves:

- **Promoter Capture Hi-C**: Mapping the physical interactions between enhancers (where the SNPs are located) and gene promoters. This technique helps us identify the **target genes** regulated by the enhancer elements.
- **Correlated Gene Expression**: We look at the co-expression patterns between the implicated enhancers and nearby genes, providing further evidence of potential regulatory relationships.

### Case Study: Systematic Prediction and Hypothesis Generation

By integrating these different lines of evidence, we can build a **comprehensive map** of SNP-to-gene relationships for each trait. For example:

- In breast cancer, we might identify a set of SNPs that overlap enhancers active in **breast epithelium** and link these SNPs to genes involved in **cell proliferation** and **DNA repair**, which are critical processes in cancer development.
- In schizophrenia, we might pinpoint SNPs located in enhancers active in the **mid-frontal cortex** and connect them to genes related to **synaptic signaling** or **neural development**, providing insights into the potential biological pathways disrupted in this psychiatric disorder.

These predictions can then be **shared with the scientific community**, serving as a basis for **experimental validation**. Researchers can use these nominated SNPs and target genes to design follow-up studies, such as:

- **CRISPR-based gene editing**: To test the functional impact of the identified SNPs and their regulatory elements.
- **Gene expression assays**: To confirm changes in gene expression predicted by the eQTL analysis.
- **Animal models**: To study the phenotypic effects of manipulating the nominated target genes.

### Moving Beyond Association

This integrative framework goes beyond simple statistical associations by providing a **mechanistic understanding** of how genetic variants contribute to disease. It allows us to:

1.  **Identify enriched tissues** where the variants are most likely to be functional.
2.  **Pinpoint driver SNPs** based on their overlap with regulatory elements and eQTL evidence.
3.  **Nominate target genes** that are likely impacted by the regulatory changes caused by these SNPs.

Ultimately, this process transforms GWAS signals into actionable **biological insights**, guiding therapeutic development and informing strategies for precision medicine. By systematically dissecting the loci, we are moving closer to understanding the **causal mechanisms** underlying complex traits and diseases.

## [30:40](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=1840s) Partitioning complex traits into tissue-specific components

In complex traits and diseases, genetic associations often do not localize neatly within a single tissue. Instead, many traits show **multifactorial influences**, where genetic variants exert effects across multiple tissues, each contributing to the overall phenotype. In this section, we explore how we can decompose these complex associations and **partition the genetic architecture** of traits into tissue-specific components.

### Unifactorial vs. Multifactorial Traits

Using the insights from the **enrichment map** of genetic associations across tissues, we can classify traits based on the **diversity of their tissue-specific signals**:

- **Unifactorial Traits**: These traits show strong enrichment in a single tissue type. For example:
    - **Heart Repolarization Interval (QRS Interval)**: Enriched primarily in heart tissues.
    - **Educational Attainment**: Enriched in brain tissues.
    - **AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s Disease**: Enriched in immune cells with some contributions from brain tissues.
- **Multifactorial Traits**: These traits exhibit **broad tissue-specific enrichments**, indicating a more complex genetic architecture. Examples include:
    - **Coronary Artery Disease (CAD)**: Displays associations across a wide range of tissues, including heart, liver, adipose tissue, and brain, reflecting the interplay between cardiovascular function, lipid metabolism, and systemic factors like obesity.
    - **Waist-to-Hip Ratio**: Shows contributions from multiple tissues such as kidney, muscle, adipose tissue, and liver, which reflect broader metabolic processes.
    - **Health Span**: A highly polyfactorial trait, with associations found across many tissues, including immune cells, muscle, blood, and embryonic stem cells, highlighting the diverse biological processes that impact overall health and longevity.

### Example: Coronary Artery Disease (CAD)

**Coronary Artery Disease** is a quintessential example of a **multifactorial trait**. Genetic variants associated with CAD do not solely map to heart tissues. Instead, they show significant enrichments across:

- **Liver Enhancers**: These variants likely affect genes involved in **lipid metabolism**, such as those regulating cholesterol and triglyceride levels.
- **Coronary and Heart Enhancers**: Variants here may influence **vascular function**, including endothelial cell proliferation and smooth muscle cell activity.
- **Adipose Tissue Enhancers**: Variants in this category are linked to **fat distribution** and metabolic processes that influence the risk of atherosclerosis.

By examining the tissue-specific enrichments, we can start **partitioning the genetic variants** associated with CAD into different biological categories. For example:

1.  **Variants in Liver Enhancers**: These variants are enriched for pathways like **phospholipid transport**, confirming the role of lipid metabolism in CAD.
2.  **Variants in Heart Enhancers**: These are linked to **endothelial cell proliferation** and **vascular function**, pointing to direct effects on coronary arteries.
3.  **Variants in Adipose Tissue Enhancers**: These show enrichments for **CDC42 signaling** and other pathways related to fat distribution and metabolism.

This partitioning process allows us to **decompose the genetic architecture** of CAD into components related to different tissues, each contributing distinct aspects of the disease process. It provides a **more nuanced understanding** of the mechanisms driving the disease and suggests potential targets for therapeutic intervention based on the tissue of action.

### Tissue-Specific Locus Dissection

With the framework of tissue-specific partitioning, we can go further and dissect individual **genetic loci** based on their tissue enrichments:

- **Heart-Specific Loci**: For example, a locus enriched in **coronary artery and heart atrium enhancers** suggests a direct role in cardiovascular tissues. This could involve genes affecting **vascular development** or **heart muscle function**.
- **Liver-Specific Loci**: Some loci, such as those near the **PCSK9** gene, show strong enrichment in **liver enhancers**. This makes sense because PCSK9 is involved in **cholesterol regulation**, and liver tissue plays a central role in lipid metabolism.
- **Multitissue Loci**: Other loci may show complex patterns, with enrichments in multiple tissues like **thyroid gland, adipose tissue, and liver**. These loci are likely involved in broader **endocrine and metabolic processes**, influencing multiple aspects of disease risk.

### Hypothesis Generation and Experimental Validation

These tissue-specific dissection efforts have been made publicly available, allowing the scientific community to use them as **hypothesis generation engines**. By providing a detailed map of **tissue-enriched loci**, researchers can:

- **Formulate testable hypotheses** about the tissue-specific mechanisms underlying complex traits.
- **Design experiments** to validate the functional roles of candidate driver SNPs and their associated genes.

For example, a researcher studying **lipid regulation** in CAD might focus on the subset of liver-enriched variants, testing their effects on cholesterol-related genes through **CRISPR perturbation** or **reporter assays**.

### "Eating Our Own Dog Food": Using Tools Internally

In the spirit of **self-validation**, our group has also applied these tools internally to generate and test our own hypotheses. This ensures a **high standard of quality** for the resources we develop and demonstrates their utility in driving **novel biological discoveries**.

For instance, by applying the tissue-partitioning methods we developed, we were able to:

- Identify a new set of **liver-specific variants** associated with CAD.
- Show that these variants impact **lipid transport genes**, leading to altered cholesterol levels in functional assays.
- Demonstrate in **mouse models** that disrupting these liver-specific genes can replicate aspects of the human CAD phenotype.

This kind of **integrative analysis** is key to understanding the complex interplay of genetic variants across multiple tissues, moving us beyond simple associations and toward a **mechanistic understanding** of how genetic variation contributes to disease.

### Conclusion

The ability to **partition complex traits into tissue-specific components** is a significant advance in the field of human genetics. It provides a framework for:

1.  **Decomposing the genetic architecture** of multifactorial traits.
2.  **Prioritizing functional variants** based on their tissue context.
3.  **Guiding experimental studies** and therapeutic development by highlighting the most relevant tissues and pathways.

Ultimately, this approach helps us **bridge the gap** between GWAS associations and biological mechanisms, offering a clearer path toward **precision medicine** and targeted interventions tailored to the underlying tissue-specific processes of disease.

## [35:53](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=2153s) From Individual GWAS Region to Mechanism and Circuitry

In this section, we dive into the **detailed dissection of individual GWAS regions**, moving from broad genetic associations to specific **mechanistic insights and regulatory circuitry**. The goal is to provide a comprehensive understanding of the **biological processes underlying complex traits**, using every available piece of evidence. This approach can turn a **statistical association** from a GWAS into a **causal understanding** of disease mechanism.

### The Integrative Framework

We start with a **region of genetic association**, often identified by GWAS, and aim to partition and interpret this region using the following steps:

1.  **Identify Specific SNPs**: Determine which variants (SNPs) within the region are most likely to be **causally linked** to the trait. This involves fine-mapping approaches and prioritization of variants based on linkage disequilibrium, epigenomic annotations, and predicted functionality.
2.  **Map Enhancer Overlaps**: Assess whether the prioritized SNPs overlap **enhancers** or other regulatory elements. Enhancers are non-coding regions that can modulate gene expression, and SNPs in these regions may alter regulatory activity.
3.  **Determine Tissue and Cell Type Specificity**: Identify the **tissues and cell types** where these enhancers are active. Tissue-specific activity can help narrow down the **biological context** in which the genetic variant is exerting its effect.
4.  **Identify Motifs and Disrupted Regulatory Elements**: Analyze the **motifs** present within these enhancers. Motifs are short DNA sequences recognized by transcription factors. SNPs can **disrupt these motifs**, altering the binding of regulatory proteins.
5.  **Identify Upstream Regulators**: Determine the **transcription factors** and other regulatory proteins that recognize these motifs. These upstream regulators are the proteins likely impacted by the SNPs.
6.  **Assess Downstream Gene Expression Changes**: Determine the **target genes** whose expression is modulated by these enhancers. Changes in gene expression can provide insights into the **molecular phenotype** associated with the genetic variant.
7.  **Determine Biological and Organismal Implications**: Understand the broader **biological processes** impacted by these changes in gene expression and the **phenotypic consequences** at the organismal level.

This comprehensive approach allows us to **connect genetic variation to regulatory function**, tissue specificity, and ultimately the **pathophysiology of complex diseases**.

### Case Study: Dissecting the FTO Locus

A concrete example of this framework is our work on the **FTO locus**, a region of the genome associated with **obesity**. The study, published in the **New England Journal of Medicine** in 2015, serves as a model for how to dissect a complex GWAS locus. Despite the seemingly narrow scopeÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âfocusing on a single SNP and its downstream effectsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthe study uncovered a **novel regulatory mechanism** that contributes to obesity.

Key Steps in the FTO Study:

1.  **Tissue and Cell Type Identification**: We first needed to determine the **tissue context** where the FTO-associated variants are likely acting. Initial analyses pointed towards **adipose tissue**, specifically a type of fat involved in energy regulation.
2.  **Target Gene Identification**: The FTO locus was initially believed to directly impact the **FTO gene**, a known obesity-associated gene. However, our analysis revealed that the true **target genes** were actually **IRX3** and **IRX5**, located several hundred kilobases away. This highlights the importance of considering long-range regulatory effects in non-coding regions.
3.  **Causal Variant Identification**: Using fine-mapping techniques, we identified a **single causal SNP** that appeared to be disrupting an enhancer. This SNP was not located in the coding region of the FTO gene but in a regulatory element that influenced distant genes.
4.  **Regulatory Motif Disruption and Upstream Regulators**: The SNP was found to disrupt a **motif recognized by the ARID5B transcription factor**. This disruption altered the binding of ARID5B, leading to changes in the regulatory activity of the enhancer.
5.  **Cellular Implications: Adipocyte Browning**: The altered enhancer activity resulted in changes in the **expression of IRX3 and IRX5**, which are involved in the regulation of **adipocyte differentiation**. Specifically, the causal variant promoted a shift away from **beige adipocyte formation** (a process known as **browning**) and towards white adipocyte formation, which is associated with increased fat storage.
6.  **Organismal Implications: Obesity Phenotype**: The disruption of this regulatory circuitry had a direct impact on **energy balance and obesity**. By reducing adipocyte browning, the FTO variant favored the accumulation of white fat, thereby increasing the risk of obesity.

### Experimental Validation

To confirm the causality of the identified SNP, we employed **CRISPR genome editing**. By **precisely editing the SNP** in human cells and in mouse models, we were able to **replicate the phenotypic effects**, providing strong evidence for the role of this variant in obesity risk.

Additionally, we used **reporter assays** to demonstrate the enhancer activity and **motif disruption**, confirming the role of the ARID5B transcription factor in this regulatory mechanism.

### Broader Implications and Model for GWAS Locus Dissection

The dissection of the FTO locus exemplifies how to move from a broad GWAS association to a **detailed mechanistic understanding**. This approach can be generalized to other GWAS loci, offering a pathway for the **functional interpretation of non-coding variants** that are often challenging to study.

By integrating **epigenomic data, motif analysis, tissue-specific activity, and experimental validation**, we can:

- **Identify causal variants** even in complex, non-coding regions.
- **Determine the regulatory circuitry** that links these variants to gene expression changes.
- **Understand the tissue-specific effects**, providing insights into the biological context of the disease.
- **Guide therapeutic development** by targeting the identified regulatory pathways.

This integrative approach shifts the focus from merely identifying **statistical associations** to uncovering the **biological mechanisms** that drive complex traits and diseases, paving the way for more targeted and effective **precision medicine**.

## [38:53](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=2333s) Introduction to the FTO locus, the strongest Genetic Association with Obesity

The **FTO locus** is one of the most striking genetic associations identified in human genomics, with a **p-value of 10ÃƒÂ¢Ã‹â€ Ã¢â‚¬â„¢6010^{-60}10ÃƒÂ¢Ã‹â€ Ã¢â‚¬â„¢60**, an extremely significant signal. This association, robust and replicated across multiple studies, points to the FTO locus as a major contributor to **obesity** and related metabolic disorders. Let's dive deeper into the genomic and biological context of this region, the challenges it presented, and the process through which we dissected its underlying mechanisms.

### Overview of the FTO Locus

1.  **Genomic Context and LD Structure**:
    - The FTO locus spans a **large region of 50,000 nucleotides**. It sits between two **recombination hotspots**, which are genomic regions with high rates of recombination. However, **within this specific locus**, recombination rates are low, resulting in strong **linkage disequilibrium (LD)**. This creates a **haplotype block**, where many genetic variants are tightly correlated, making it difficult to pinpoint the specific causal variant.
    - The region contains **89 common variants** that are all in high LD, spanning the **first intron and a portion of the second intron** of the FTO gene. Importantly, there are **no protein-coding alterations** among these variants, suggesting that the genetic effects are likely due to **regulatory changes**, rather than changes in the protein sequence.
2.  **Broad Phenotypic Associations**:
    - While the FTO locus is primarily associated with **obesity**, it also contributes to a spectrum of related **metabolic traits**, including **type 2 diabetes**, **cardiovascular diseases**, and other obesity-related phenotypes. This broad association highlights the systemic impact of obesity on various health conditions.
3.  **Statistical Significance and GWAS Signal**:
    - On a **Manhattan plot** of GWAS results, the FTO locus stands out as a towering peak, well above the genome-wide significance threshold, indicating a very strong association with obesity risk. It remains the **strongest genetic signal for obesity** across diverse populations.

### Challenges in Understanding the FTO Locus

Despite its strong genetic association, the **FTO locus presented several challenges** for mechanistic understanding:

- **Dense LD Structure**: Due to the extensive LD across this haplotype block, many SNPs are co-inherited. This makes it difficult to disentangle which specific SNP is causally related to the phenotype.
- **Regulatory vs. Coding Effects**: The absence of coding variants suggested a **regulatory role**, but pinpointing the exact mechanism was challenging without understanding which tissue, enhancer elements, and downstream genes were involved.
- **Multiple Hypotheses and Confusion**: There was significant debate in the scientific community about the **target gene** and the relevant tissue context. Initial studies speculated that the **FTO gene** itself was the causal target due to its proximity to the association signal. However, subsequent work hinted at other possible targets like **IRX3**, **IRX5**, and even genes further away.

### The FTO Gene: A Brief History

The FTO gene was originally identified in a mouse screen for **fused toes**, part of a series of genes labeled Fuso-N, Fuso-O (FTO), and so on. When researchers discovered the association of the FTO locus with obesity, they whimsically named the gene **"Fatso,"** later officially renamed as **fat and obesity-associated gene** (FTO). This led to an initial bias towards implicating FTO in obesity, given its suggestive name and location at the peak of the association signal.

However, as studies progressed, it became clear that **knockout experiments targeting FTO** also affected the surrounding regulatory region, casting doubt on whether the effects were due to changes in the FTO gene itself or its regulatory landscape.

### Divergent Hypotheses and Initial Missteps

Given the strong association, numerous studies attempted to identify the **causal gene** and the tissue context. The hypotheses varied widely:

- Some suggested it was **FTO itself**, given the proximity and the apparent connection to obesity.
- Others proposed that the locus might influence **IRX3**, a gene involved in **pancreatic function**.
- There were additional hypotheses involving genes like **RBL2** in **lymphocytes**, with speculation about a wide array of possible tissues, from the brain to the pancreas, indicating the lack of a coherent understanding.

This led to a **scattered approach** with conflicting findings. For example, a high-profile study from a Chicago group proposed that **IRX3** in the brain was the target, but their findings showed a minor effect, raising skepticism about its true role as the causal gene.

### Our Approach: A Systematic Dissection

Faced with the uncertainty and the diversity of hypotheses, we set out to systematically dissect the FTO locus. Our goals were to:

1.  **Identify the Relevant Tissues**:
    - Using **epigenomic annotations**, we aimed to pinpoint which tissues exhibited activity of the regulatory elements overlapping the FTO-associated SNPs.
2.  **Determine the True Target Genes**:
    - Instead of assuming proximity-based effects, we leveraged **chromatin interaction data** and **long-range regulatory analysis** to test if distant genes might be involved.
3.  **Identify the Causal Variant**:
    - We used **fine-mapping techniques** to isolate a single variant with the highest posterior probability of causality, focusing on regulatory SNPs rather than coding variants.
4.  **Establish the Mechanism of Action**:
    - By analyzing **transcription factor motifs** and performing **functional assays**, we aimed to understand the **regulatory impact** of the causal variant.
5.  **Validate with Experimental Evidence**:
    - Finally, we employed **CRISPR genome editing** and other experimental approaches to validate the causality of the identified variant and its impact on gene expression and metabolic traits.

This comprehensive and integrative strategy allowed us to **move beyond statistical associations** and provide a **mechanistic understanding** of the FTO locus, setting a precedent for dissecting other complex GWAS regions.

In the next section, we will discuss the **findings and experimental results** that emerged from this dissection and how they transformed our understanding of the FTO locus and its role in obesity. This will include insights into the **novel regulatory pathways** uncovered, the identification of **IRX3 and IRX5 as the true target genes**, and the broader implications for metabolic disease and potential therapeutic avenues.

## [43:40](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=2620s) Step 1: Establishing the Relevant Tissue and Cell Type

To dissect the mechanisms underlying the **FTO locus** and its association with obesity, the first crucial step is to **identify the tissue or cell type** where the genetic variant exerts its effect. This step sets the stage for understanding the biological context and helps narrow down the potential pathways and mechanisms involved.

### Mapping Epigenomic Activity Across Tissues

To determine the relevant tissue, we leveraged comprehensive **epigenomic maps** from projects like the **Roadmap Epigenomics Project** and the **ENCODE Project**. As the senior author of the **Roadmap Epigenomics paper**, I had led a large collaborative effort to profile the **epigenomic landscape** across a wide array of human tissues and cell types. This dataset included hundreds of diverse **epigenomic assays**, which are technically challenging and require substantial resources. These assays provide insights into:

- **Chromatin accessibility** (open chromatin regions),
- **Histone modifications** (e.g., H3K27ac for active enhancers),
- **DNA methylation patterns**, and
- **Transcription factor binding sites**.

With this wealth of data, we could systematically map the activity of **non-coding regions** across many different tissues, enabling us to identify where regulatory elements like enhancers are active.

### Applying Epigenomic Mapping to the FTO Locus

When we applied these methods to the **FTO locus**, we observed a large region of active chromatin spanning **12,000 base pairs** at the beginning of the locus. This region exhibited strong enhancer activity in a specific type of precursor cells known as **mesenchymal stem cells**. These cells are **multipotent progenitors**, capable of differentiating into several important tissue types, including:

1.  **Chondrocytes** (precursors to cartilage),
2.  **Osteoblasts** (bone-forming cells),
3.  **Cardiac muscle cells**, and most importantly,
4.  **Adipocytes** (fat cells).

This finding was critical because it pointed us towards a **lineage** that could differentiate into various tissues, but particularly suggested a role in **adipocyte biology**, linking the enhancer activity directly to the development of fat cells.

### Different Types of Adipocytes: White, Brown, and Beige

To understand the implications of the enhancer activity in mesenchymal stem cells, we need to distinguish between the different types of fat cells:

1.  **White Adipocytes**:
    - These cells are specialized for **energy storage**. They have large lipid droplets and serve as the body's primary reserve of stored energy.
    - They are abundant in adults and are critical for maintaining energy balance.
2.  **Brown Adipocytes**:
    - These cells are specialized for **thermogenesis**, or heat production. They contain numerous **mitochondria**, giving them a brown color.
    - Brown adipocytes play a key role in **calorie burning** through a process called **uncoupled respiration**, where the **mitochondrial membrane depolarizes**, leading to the dissipation of energy as heat instead of storing it as ATP.
3.  **Beige or "Bright" Adipocytes**:
    - These cells are **intermediate** between white and brown adipocytes. They can **switch** between an energy-storing and an energy-burning state, depending on environmental cues like temperature or dietary changes.
    - Beige adipocytes are thought to have a role in **adaptive thermogenesis**, helping to regulate body temperature and energy expenditure.

Given the potential for **adipocyte plasticity**, it was plausible that the regulatory activity in the FTO locus was involved in influencing the balance between **energy storage (white adipocytes)** and **energy burning (brown/beige adipocytes)**.

### Identifying the Impact of the Obesity-Associated Allele

We next focused on determining whether the **obesity-associated allele** had a functional impact on enhancer activity. To do this, we measured **enhancer activity** across different segments of the 12,000 base pair region, comparing the **risk allele** (associated with obesity) to the **non-risk (lean) allele**.

### Key Findings:

- **Increased Enhancer Activity with the Risk Allele**:
    - The **obesity-associated (risk) allele** exhibited **increased activity** in adipocytes, suggesting a **gain-of-function** effect. This was surprising because we often think of disease-associated variants as **loss-of-function** mutations that disrupt normal regulatory activity.
    - In this case, the risk allele seemed to **enhance the activation** of the regulatory region, possibly leading to **overexpression** of downstream genes.

### Possible Mechanisms of Gain-of-Function

We considered several hypotheses to explain this gain-of-function effect:

1.  **Creation of a New Binding Site for an Activator**:
    - The risk allele may have **introduced a new motif** or binding site for a transcriptional activator. This would lead to **increased recruitment** of activators, thereby boosting enhancer activity and subsequent gene expression.
2.  **Disruption of a Repressor Binding Site**:
    - Alternatively, the risk allele might have **abolished a repressor binding site**, removing inhibitory effects and leading to increased enhancer activity. This type of **de-repression** is another form of gain-of-function where the absence of repression leads to heightened gene activation.

These two mechanisms are not mutually exclusive, and both could contribute to the increased enhancer activity observed with the risk allele.

### Hypothesis: Role of Adipocyte Differentiation and Function

Given the strong enhancer activity in **adipocyte precursors** and the gain-of-function nature of the risk allele, we hypothesized that the FTO locus might influence the **balance between white and beige adipocyte differentiation**. This balance is crucial for determining whether adipocytes will primarily **store energy** or **burn energy**.

- **Increased Enhancer Activity** due to the risk allele could lead to **greater expression of genes** that promote white adipocyte differentiation, tipping the balance towards **energy storage**, thereby predisposing individuals to obesity.
- Conversely, reducing this enhancer activity might favor the differentiation towards **beige adipocytes**, promoting **energy expenditure** and potentially providing a protective effect against obesity.

### Summary

The first step of our systematic dissection revealed critical insights into the **tissue context** and **regulatory dynamics** of the FTO locus:

- The relevant tissue and cell type were identified as **mesenchymal stem cells** with differentiation potential towards **adipocytes**, particularly those involved in energy storage and thermogenesis.
- The obesity-associated risk allele showed a **gain-of-function effect**, leading to **increased enhancer activity**, suggesting a novel regulatory mechanism contributing to obesity.

This set the stage for our next steps, where we aimed to identify the **target genes** of this enhancer and the **transcriptional regulators** involved. This comprehensive analysis laid the groundwork for uncovering a novel regulatory circuit with implications for obesity therapy and metabolic health.

## [49:29](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=2969s) Step 2: Establishing Downstream Target Genes

With the relevant tissue and cell type identified as **adipocyte precursors** and **preadipocytes**, the next step in dissecting the mechanism of the **FTO locus** was to identify the **downstream target genes** influenced by the obesity-associated variants. This is crucial for understanding the **regulatory circuit** and the biological processes through which these variants impact obesity.

### Linking Enhancer Activity to Target Genes

To determine the target genes regulated by the enhancer region, we employed **three complementary strategies**:

1.  **Functional Genomic Linking**:
    - This method involves analyzing the **correlation of gene expression** with enhancer activity. When the enhancer is active, what genes are also active?
    - The idea is that even if an enhancer is physically closer to one gene, it may exhibit stronger **co-activation** with another gene farther away. By tracking patterns of synchronized activation across samples, we can infer potential regulatory links between enhancers and genes.
2.  **Expression Quantitative Trait Loci (eQTL) Analysis**:
    - **eQTLs** are genomic loci where genetic variants correlate with **gene expression levels**. This is analogous to GWAS but focuses on **molecular phenotypes** (gene expression) instead of clinical phenotypes (disease traits).
    - We look for variants within the FTO locus that show a strong correlation with changes in the expression of nearby genes. For example, if a **G-to-T change** at a specific variant leads to increased expression of a gene, this suggests a **regulatory link** between that variant and the gene.
    - This provides **genetic evidence** that a non-coding variant is influencing gene expression, helping us identify potential target genes.
3.  **Chromatin Conformation Capture (Hi-C)**:
    - This method explores the **3D structure of the genome**, revealing physical interactions between distant genomic regions that are brought into proximity by chromatin looping.
    - Using **Hi-C data**, we can observe long-range interactions between the FTO enhancer and potential target genes that are **hundreds of thousands to millions of base pairs away**.
    - In our analysis, we found strong chromatin contacts linking the FTO locus, specifically the variant **rs1421085**, to distant genes such as **IRX3** and **IRX5**. These interactions spanned **long distances**, indicating a regulatory connection that would not have been apparent based solely on linear genome proximity.

### Testing Candidate Target Genes

Armed with these three lines of evidence (functional genomic linking, eQTL analysis, and chromatin conformation data), we proceeded to experimentally test which genes were influenced by the risk variant. We selected a cohort of individuals who were **homozygous for the risk allele** and compared them with individuals who were **homozygous for the non-risk allele**.

### Key Findings:

- **FTO Gene Expression**:
    - Despite its proximity to the associated variants, the expression of the **FTO gene itself** did **not change** in response to the genotype. This ruled out FTO as the direct target of the enhancer, contradicting earlier hypotheses that had focused solely on the nearest gene.
- **IRX3 and IRX5 Gene Expression**:
    - In contrast, we observed significant changes in the expression of **IRX3** and **IRX5**, two genes located far away from the FTO locus:
        - **IRX3** is approximately **600,000 base pairs** away.
        - **IRX5** is even farther, about **1.2 million base pairs** away.
    - These genes showed **increased expression** in individuals carrying the risk allele, indicating a **gain-of-function effect**. The risk allele appears to enhance the activity of the enhancer, leading to **upregulation** of IRX3 and IRX5.

### Long-Range Regulatory Effects

The observed effects on IRX3 and IRX5 were particularly striking because these genes are separated from the FTO locus by multiple **linkage disequilibrium (LD) block boundaries** and **recombination hotspots**. Without the **3D chromatin interaction data**, it would have been nearly impossible to predict these genes as targets due to their linear distance from the FTO locus.

- The **Hi-C data** revealed a **looping interaction** between the enhancer region within the FTO locus and the distant IRX genes, explaining the long-range regulatory effect.
- This highlights the importance of considering the **3D genome architecture** when identifying target genes, especially in complex traits where regulatory elements may act over large distances.

### eQTL Evidence Confirms Target Genes

Further supporting evidence came from **eQTL analysis**:

- The obesity-associated variant was identified as an **eQTL** for both **IRX3** and **IRX5**, meaning that changes in the genotype directly influenced the expression levels of these genes.
- Importantly, this eQTL effect was observed **specifically in early adipocyte differentiation**, not in fully mature adipocytes or in whole tissue samples. This finding underscores the importance of studying the **right developmental stage**, as gene regulation can be highly dynamic and stage-specific.

### Specificity of the eQTL Effect

The eQTL effect was limited to **preadipocytes**, the precursors of mature adipocytes. This is consistent with our earlier finding that the enhancer activity was strongest in **mesenchymal stem cells** and their immediate derivatives.

- **Preadipocytes** are the transitional stage between mesenchymal stem cells and fully differentiated adipocytes. During this stage, the cells are actively undergoing changes that determine whether they will become **white adipocytes** (energy-storing) or **beige/brown adipocytes** (energy-burning).
- The obesity-associated variant appears to influence this decision by **upregulating IRX3 and IRX5**, which are involved in regulating the balance between **energy storage** and **thermogenesis**.

### Summary of Step 2

The second step of our analysis provided critical insights into the **downstream regulatory effects** of the FTO locus:

- We identified **IRX3 and IRX5** as the primary target genes of the FTO-associated enhancer, based on a combination of **functional genomics**, **eQTL analysis**, and **chromatin interaction data**.
- The **risk allele** led to a **gain-of-function effect**, increasing the enhancer activity and, consequently, the expression of IRX3 and IRX5.
- The regulatory effects were **stage-specific**, manifesting only during **early adipocyte differentiation**, underscoring the importance of studying the **right developmental context**.

This step moves us closer to a comprehensive mechanistic understanding of how the FTO locus contributes to obesity, setting the stage for further exploration of the **upstream regulators** and the **biological processes** involved in the next steps. This detailed dissection provides a model for how to systematically approach the identification of target genes in complex trait loci, integrating multiple lines of evidence to uncover the underlying molecular circuitry.

## [55:27](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=3327s) Step 3 - Establishing causal nucleotide variant

With the relevant tissue (preadipocytes) identified and the downstream target genes (**IRX3** and **IRX5**) established, the next step in dissecting the **FTO locus** was to pinpoint the **causal nucleotide variant** responsible for the observed regulatory effects.

### The Challenge of Finding the Causal Variant

The FTO locus spans a large region with **89 common variants** in high linkage disequilibrium (LD), meaning that these variants are inherited together and correlate strongly. However, **not all of these variants** are functional; only one or a few might be directly causing the change in enhancer activity. Our goal was to identify which specific **single nucleotide polymorphism (SNP)** was the driver.

### Identifying Key Regulatory Motifs

To determine the causal variant, we needed to examine the **regulatory motifs** in the enhancer region. **Regulatory motifs** are specific DNA sequences recognized by transcription factors (TFs) that can activate or repress gene expression. By identifying which motifs are **disrupted** by the risk allele, we can home in on the causal variant. There are **several strategies** for assessing the importance of these motifs:

1.  **Experimental Testing**:
    - We can **mutate** each of the 89 common variants and experimentally test their effects on enhancer activity. While feasible today, at the time of this study, this approach was **technically challenging** due to the large number of variants and the need for precise, high-throughput assays.
2.  **Motif Enrichment Analysis**:
    - We can look for **enriched motifs** in the GWAS loci associated with obesity. By examining the entire set of genetic regions linked to BMI, we can identify regulatory motifs that appear **repeatedly** across these loci. If a specific motif is frequently present in obesity-associated regions, it is likely functionally relevant.
3.  **Evolutionary Conservation**:
    - We can analyze the **conservation** of motifs across different mammalian species. Regulatory elements that are **evolutionarily conserved** are more likely to be functionally important because they have been preserved through selective pressures. If a variant disrupts a conserved motif, it is more likely to have a functional impact.

### Applying These Strategies

Using a combination of **motif enrichment**, **evolutionary conservation**, and **functional assays**, we identified a **regulatory motif** in the enhancer region that was:

- **Enriched** in other GWAS loci associated with BMI.
- **Evolutionarily conserved**, indicating its functional importance across species.
- **Disrupted by a specific SNP** within the FTO locus.

The identified motif was an **AT-rich interacting domain motif (AATA)**, a sequence recognized by specific transcription factors. This motif was both **overlapping** with the risk SNP and **conserved** across mammals, making it a strong candidate for the causal regulatory element.

### Functional Validation of the Causal SNP

To confirm that this SNP was indeed the causal variant, we performed a series of **targeted mutation experiments**:

1.  **Mutagenesis of the Risk Allele**:
    - We introduced the risk allele into a **10,000 base pair (bp)** region of the enhancer and observed a significant **gain of function** (increased enhancer activity), suggesting that the risk allele **increases expression** of the downstream target genes.
    - When we introduced the risk allele into a **1,000 bp** region, the gain of function was even more pronounced, indicating that the enhancer activity was localized within a smaller segment but still required a substantial context for full function.
2.  **Testing Shorter Regions (100 bp)**:
    - We also tested a **100 bp** region containing the risk allele. Interestingly, this shorter region **did not show any change** in enhancer activity, even when the risk allele was present.
    - **Why was there no effect with the 100 bp region?**
        - The FTO enhancer is a **large, complex regulatory element**, requiring interactions across a broad sequence context. The 100 bp segment was **too short** to capture the full set of transcription factor binding sites and structural elements needed for enhancer function.
        - This finding highlights the importance of testing variants within a **sufficiently large sequence context** to capture the full regulatory potential of the enhancer.

### The Causal SNP Recapitulates the Risk Haplotype

By introducing the **single risk SNP** into a longer enhancer segment, we were able to **recapitulate the full gain of function** seen with the entire risk haplotype. This provided strong evidence that the **single nucleotide change** was sufficient to drive the observed changes in gene expression, specifically **de-repressing** the enhancer activity.

- The **risk allele** led to a **gain of function** by either:
    - **Creating a new binding site** for an activator, increasing enhancer activity.
    - **Disrupting a repressor site**, leading to loss of repression and increased enhancer activation.

In either case, the effect of the variant was to **enhance the expression** of **IRX3** and **IRX5**, the key target genes linked to obesity risk.

### Summary of Step 3

In this step, we successfully identified the **causal nucleotide variant** responsible for the regulatory changes at the FTO locus:

- We used a combination of **motif analysis**, **conservation**, and **functional assays** to pinpoint the SNP that disrupted a conserved regulatory motif.
- Experimental validation confirmed that the **risk allele** caused a **gain of function**, increasing enhancer activity and the expression of downstream target genes.
- The effect of the SNP was **context-dependent**, requiring a sufficiently large enhancer segment to observe the change, highlighting the complexity of **regulatory elements** in the genome.

This step completes the identification of the **causal variant**, setting the stage for exploring the **upstream regulators** and the **biological processes** through which this variant influences obesity. By integrating multiple lines of evidence, we provide a comprehensive mechanistic dissection of the FTO locus, serving as a model for fine-mapping and functional characterization of non-coding GWAS hits.

## [59:59](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=3599s) Step 4 - Establish upstream regulator causality

Having identified the **relevant cell type** (preadipocytes), the **downstream target genes** (**IRX3** and **IRX5**), and the **causal nucleotide variant** (**rs1421085**), the next logical step was to identify the **upstream regulator** that interacts with this variant. This step is crucial for understanding **which transcription factor (TF)** directly mediates the effects of the risk allele, thereby influencing the enhancer activity and gene expression changes.

### Identifying Candidate Transcription Factors

The first challenge was determining which transcription factor might be binding to the **AT-rich motif** disrupted by the risk SNP (**rs1421085**). Several candidate transcription factors were considered, including:

- **LHX6**: A known transcription factor involved in developmental processes.
- **NKX6.3**: Another candidate based on its motif recognition properties.
- The **ARID family**: A large group of transcription factors (e.g., **ARID1A**, **ARID1B**, **ARID2**, **ARID3A**, **ARID3B**, **ARID3C**, and so on) that recognize AT-rich DNA motifs.

To narrow down this list, we focused on the **expression patterns** of these transcription factors, particularly in preadipocytes, since we had already established this as the relevant cell type.

### Expression Profiling and Initial Findings

We examined the **expression levels** of the ARID family transcription factors in both risk and non-risk individuals. One transcription factor, **ARID5B**, stood out due to its high expression level in preadipocytes across both risk and non-risk genotypes.

### Is it problematic that ARID5B is expressed in both risk and non-risk individuals?

- **No, it is not problematic.** The key issue here is **not the expression of the transcription factor** (the _trans_ component), but the integrity of the **binding site** (the _cis_ component).
- The **trans-acting regulator (ARID5B)** remains expressed regardless of genotype, but its ability to bind to the enhancer is **compromised** when the **cis-regulatory motif** is disrupted by the risk allele.

In other words, the **problem lies in the DNA sequence alteration** (the disrupted motif) rather than the transcription factor itself. This distinction is crucial: the transcription factor (ARID5B) is present, but the risk SNP disrupts its **binding site**, preventing successful repression of the enhancer.

### Testing Binding Specificity

To validate ARID5B as the likely **upstream regulator**, we tested its binding specificity using:

1.  **Whole adipose tissue** samples.
2.  **Isolated adipocyte stem cells** from both lean and obese individuals.

ARID5B exhibited the **strongest binding affinity** to the enhancer region containing the AT-rich motif, confirming it as the prime candidate for regulating this locus.

### Establishing Causality Through Epistasis

Identifying ARID5B as the key transcription factor was an important step, but to **prove causality**, we needed to demonstrate that ARID5B directly mediates the effects of the risk SNP. We used a method called **epistasis analysis** to establish whether the SNP and the transcription factor are part of the **same regulatory pathway**.

Epistasis Analysis:

- **Epistasis** involves testing the combined effects of **two genetic disruptions**: the _cis_ element (the SNP) and the _trans_ element (the transcription factor).
- We performed **cis perturbations** by altering the nucleotide sequence (introducing the risk allele or non-risk allele).
- We performed **trans perturbations** using **small interfering RNA (siRNA)** to knock down the expression of ARID5B.

### Results of the Epistasis Experiments

We conducted enhancer activity assays using **luciferase reporters** and measured the expression levels of the **target genes** (**IRX3** and **IRX5**). The results were striking and confirmed the **interdependence** of the SNP and the transcription factor:

1.  **Non-risk haplotype with intact ARID5B**:
    - Successful **repression** of the enhancer and downstream gene expression.
    - This serves as the **baseline** state, where the motif is intact, and ARID5B can bind effectively.
2.  **Non-risk haplotype with ARID5B knockdown**:
    - **De-repression** of the enhancer and increased target gene expression.
    - This shows that the **presence of ARID5B** is necessary for repression.
3.  **Risk haplotype with intact ARID5B**:
    - **De-repression** of the enhancer despite the presence of ARID5B.
    - This indicates that the **disrupted motif** (due to the risk SNP) prevents ARID5B from binding, leading to a loss of repression.
4.  **Risk haplotype with ARID5B knockdown**:
    - **No additional effect** beyond the de-repression observed with the risk haplotype alone.
    - This suggests that the disruption of either the **motif (cis)** or the **transcription factor (trans)** alone is sufficient to cause de-repression, and disrupting both does not have an additive effect.

### Interpretation of Epistasis Results

The epistasis analysis demonstrated that:

- **Both the motif and the transcription factor** are required for successful enhancer repression.
- The **risk SNP** disrupts the motif, preventing ARID5B from binding effectively, leading to **enhancer activation** (de-repression).
- Knocking down ARID5B in the non-risk context **mimics** the effect of the risk SNP, further confirming that ARID5B is the **causal upstream regulator** mediating the effect of the variant.

### Summary of Step 4

This step successfully established the **causal relationship** between the disrupted motif, the risk SNP, and the transcription factor ARID5B:

1.  **Identification of the Upstream Regulator**:
    - ARID5B was identified as the key transcription factor binding to the AT-rich motif disrupted by the risk SNP.
2.  **Validation of Regulatory Binding**:
    - ARID5B showed strong binding to the enhancer region in preadipocytes, supporting its role as the upstream regulator.
3.  **Epistasis Analysis**:
    - The combined cis and trans perturbation experiments confirmed that both the motif and ARID5B are required for enhancer repression.
    - Disrupting either the motif (with the risk SNP) or the regulator (with siRNA knockdown) resulted in **loss of repression** and increased expression of the target genes (**IRX3** and **IRX5**).

### Conclusion

With the identification of ARID5B as the upstream regulator, we have now established the **full mechanistic pathway** from the genetic variant (SNP) to the enhancer activity, the transcription factor binding, and the downstream effects on gene expression. This comprehensive dissection provides a **causal link** between the non-coding variant at the FTO locus and the molecular mechanisms driving increased obesity risk.

This step completes the core analysis, setting the stage for exploring the **biological and organismal implications** of these findings, particularly how they contribute to adipocyte differentiation and energy metabolism, ultimately influencing obesity and related metabolic disorders.

## [1:04:58](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=3898s) Step 5 - Establish cellular phenotypic consequences

Having identified the **relevant cell type** (preadipocytes), the **downstream target genes** (**IRX3** and **IRX5**), the **causal variant** (**rs1421085**), and the **upstream regulator** (**ARID5B**), we now turn to the **cellular phenotypic consequences**. This step aims to bridge the gap between **genetic variation** and **disease manifestation** by elucidating how these molecular changes translate into cellular behavior and ultimately influence obesity risk.

### Bridging the Gap Between Genetic Variation and Disease

While we had already established the molecular circuitryÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âshowing that the risk variant disrupts a repressive interaction, leading to increased enhancer activity and elevated expression of **IRX3** and **IRX5**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âwe still needed to understand the **biological impact** of this altered gene expression. Specifically, we sought to determine:

- **How does increased expression of IRX3 and IRX5 affect preadipocytes?**
- **What are the downstream metabolic consequences that link this molecular disruption to obesity?**

To address these questions, we needed to investigate the **cellular phenotypes** influenced by the disrupted enhancer activity.

### Co-Expression Analysis of IRX3 and IRX5

We began by examining the **co-expression patterns** of genes in adipocyte precursor cells (preadipocytes). By profiling gene expression across **20 individuals**, we analyzed how the expression of **IRX3** and **IRX5** correlates with other genes:

- **Positive Correlation with Lipid Metabolism Genes**:
    - When **IRX3** and **IRX5** expression levels were **elevated**, we observed a significant increase in the expression of genes involved in **lipid metabolism**.
    - This suggests a shift towards a phenotype characterized by enhanced **lipid storage**, consistent with the risk allele's association with obesity.
- **Negative Correlation with Mitochondrial Genes**:
    - Conversely, when **IRX3** and **IRX5** expression was low, we saw an increase in the expression of genes involved in **mitochondrial function**.
    - This points to an alternative phenotype where there is a greater emphasis on **mitochondrial activity** and **energy expenditure**.

### Functional Consequence: Shift in Adipocyte Phenotype

The co-expression analysis suggested a **functional shift** in adipocyte differentiation driven by the risk allele:

- **Increased Expression of IRX3/IRX5** (Risk Allele):
    - Leads to a **reduction in mitochondrial gene expression** and **mitochondrial activity**.
    - Promotes a **lipid storage phenotype**, characterized by larger white adipocytes that are optimized for storing energy in the form of fat.
- **Decreased Expression of IRX3/IRX5** (Protective Allele):
    - Associated with an increase in **mitochondrial gene expression**.
    - Favors a phenotype with smaller, more metabolically active adipocytes that prioritize **energy burning** over storage.

### Role of Uncoupling Protein 1 (UCP1)

A key finding in our analysis was the differential expression of **uncoupling protein 1 (UCP1)**, a critical protein involved in **thermogenesis**:

- **UCP1** is known to **depolarize the mitochondrial membrane**, leading to **heat production** instead of ATP synthesisÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âa process called **non-shivering thermogenesis**.
- We observed that **UCP1 expression** was significantly reduced in adipocytes carrying the **risk allele**, indicating a **decrease in mitochondrial thermogenesis**.
- In contrast, individuals with the **protective allele** showed **higher UCP1 expression**, both under normal conditions and upon **cold induction**, suggesting greater **thermogenic capacity** and increased energy expenditure.

### Proposed Model: Beige vs. White Adipocyte Phenotype

Our findings suggest a model where the genetic variant at the FTO locus **modulates adipocyte differentiation**, influencing the balance between **beige adipocytes** (calorie-burning) and **white adipocytes** (calorie-storing):

1.  **Protective Allele**:
    - Enhancer repression is intact, leading to **lower expression** of IRX3 and IRX5.
    - Promotes differentiation towards a **beige adipocyte phenotype**, which is **rich in mitochondria** and favors **calorie burning**.
    - Increased expression of **UCP1** enhances thermogenesis and energy expenditure.
2.  **Risk Allele**:
    - Disrupted enhancer repression leads to **elevated expression** of IRX3 and IRX5.
    - Drives differentiation towards a **white adipocyte phenotype**, characterized by **larger cells** that are optimized for **lipid storage**.
    - Reduced **UCP1 expression** diminishes mitochondrial thermogenesis, favoring **energy storage** over expenditure.

### Evidence of Cellular Phenotypic Change

We validated this model through **functional assays** in preadipocytes and adipocytes:

- We observed that adipocytes carrying the **risk allele** exhibited **fewer mitochondria**, consistent with a shift away from energy expenditure.
- These cells also showed a significant increase in **lipid droplet size**, further supporting the shift towards **enhanced lipid storage**.

The **protective allele**, on the other hand, was associated with **higher mitochondrial content** and **increased thermogenic activity**, as evidenced by elevated **UCP1 expression** and a greater response to **cold induction**.

### Summary of Step 5

We have now established a clear link between the genetic variant and its cellular consequences:

1.  **Altered Gene Expression**:
    - The risk SNP disrupts the repressive binding of ARID5B, leading to **increased expression of IRX3 and IRX5**.
2.  **Shift in Adipocyte Differentiation**:
    - Elevated IRX3/IRX5 expression favors the formation of **white adipocytes**, which store energy.
    - Lower expression (protective allele) promotes the formation of **beige adipocytes**, which burn energy.
3.  **Metabolic Consequences**:
    - The risk allele leads to a **decrease in mitochondrial activity** and **thermogenesis**, reducing the body's capacity to burn calories.
    - This imbalance shifts the overall energy homeostasis towards **lipid accumulation**, contributing to an increased risk of obesity.

### Conclusion

This step successfully elucidates the **cellular mechanism** linking the FTO locus variant to obesity. By disrupting the regulatory balance between energy storage and energy expenditure in adipocytes, the risk allele shifts adipocyte differentiation towards a **calorie-storing phenotype**, contributing to increased fat accumulation and a higher predisposition to obesity. This mechanistic insight provides a direct bridge from **genetic variation** to **disease phenotype**, paving the way for potential therapeutic interventions targeting adipocyte metabolism and differentiation.

The next and final step involves exploring the **organismal implications** of these findings and validating the model in vivo to understand the broader metabolic consequences and potential for therapeutic modulation.

## [1:07:38](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=4058s) Step 6 - Establish organismal phenotypic consequences

Having established the **tissue**, **target genes**, **causal nucleotide variant**, and **upstream regulator**, and identified the **cellular phenotypic changes**, the final step is to validate these findings at the **organismal level**. We need to demonstrate how these molecular and cellular changes manifest in **whole-body phenotypes**, particularly with respect to **obesity**, and how they ultimately influence **energy homeostasis** and **weight regulation**.

### Testing in Mouse Models

To assess the organismal consequences, we turned to **mouse models**, where we could manipulate the key components of the identified circuitry and evaluate their impact on **whole-body metabolism** and **weight regulation**.

### Experimental Approach:

1.  **Manipulation of ARID5B (Upstream Regulator):**
    - We performed both **knockdown** and **overexpression** of ARID5B in mouse adipocytes.
    - Additionally, we utilized **genome editing** to directly alter the **rs1421085 SNP** (C/T allele) to examine its causal effect.
2.  **Manipulation of IRX3 and IRX5 (Target Genes):**
    - We knocked down and overexpressed **IRX3** and **IRX5** in both risk and non-risk backgrounds to determine their effect on **thermogenesis** and **energy expenditure**.

### Cellular and Organismal Consequences

**1\. Cellular Thermogenesis:**

- **Knockdown of IRX5** in risk individuals led to a **significant increase** in **oxygen consumption rate**, a proxy for **thermogenesis**.
- **Knockdown of IRX3** also showed a similar increase in thermogenesis.
- Conversely, **overexpression of IRX3** in non-risk individuals led to a **decrease in thermogenesis**, indicating its role in **suppressing energy expenditure**.

These results confirm that the **expression levels** of IRX3 and IRX5 are key modulators of **thermogenic activity**, directly linking the genetic variant to **altered cellular metabolism**.

**2\. Whole-Body Metabolic Changes in Mice:**

- We generated mice carrying a **dominant-negative allele** of IRX3, specifically in adipose tissue using an **adipocyte-specific promoter**.
- The results were striking:
    - These mice showed a **dramatic reduction in fat mass**, with up to **50% less body fat** compared to control mice.
    - Despite their lower fat mass, these mice did not show any significant change in **respiration rate** under normal conditions, indicating that the reduction in fat mass was not due to increased physical activity.

**3\. Increased Energy Expenditure:**

- Detailed metabolic profiling revealed that the **energy expenditure** of these mice was consistently higher:
    - Both during the **night**, when mice are most active, and during the **day**, when they are resting.
    - These mice effectively exhibited a **higher basal metabolic rate**, leading them to **burn more calories even while sleeping**.

**4\. High-Fat Diet Resistance:**

- When subjected to a **high-fat diet**, normal mice typically gained significant weight.
- However, the **IRX3-dominant negative mice** showed remarkable **resistance to weight gain**:
    - Despite consuming the same high-fat diet, these mice were unable to accumulate additional body fat, highlighting a protective effect against **diet-induced obesity**.

### Genome Editing Validation

To provide conclusive evidence of the **causal role of the SNP** (rs1421085), we employed **CRISPR genome editing** to introduce a **single nucleotide change** in the mice:

1.  **Editing the C Allele to T (Risk to Protective):**
    - We altered the **risk allele (C)** to the **protective allele (T)** in mice carrying the risk haplotype.
    - The change resulted in a **reversion of the phenotype**:
        - **Thermogenic activity increased**, and the mice exhibited a **leaner body phenotype**.
    - This confirmed that the single nucleotide alteration was sufficient to switch the **molecular, cellular, and organismal phenotypes**, establishing direct **causality**.
2.  **Reversion to Risk Allele (T to C):**
    - To rule out any off-target effects of the CRISPR edit, we performed a second genome edit, reverting the T back to the C allele.
    - The **risk phenotype** was restored, demonstrating that the observed effects were specifically due to the **rs1421085 SNP** and not any unintended genomic changes.

### Integrated Model of Genetic and Phenotypic Consequences

The results from the mouse model provide a comprehensive link between the **genetic variant**, the **molecular circuitry**, and the **organismal phenotype**:

- **Risk Allele (C)**:
    - Disrupts ARID5B binding, leading to **increased enhancer activity**.
    - Upregulates **IRX3** and **IRX5**, shifting adipocyte differentiation towards a **white adipocyte phenotype**.
    - Reduces thermogenic capacity, leading to **increased fat storage** and a higher risk of obesity.
- **Protective Allele (T)**:
    - Maintains ARID5B binding, keeping the enhancer **repressed**.
    - Suppresses IRX3 and IRX5 expression, favoring differentiation towards **beige adipocytes**.
    - Enhances mitochondrial activity and **thermogenesis**, promoting **calorie burning** and a leaner phenotype.

### Implications for Obesity and Therapeutic Interventions

This study serves as a **proof-of-concept** for how **genome-wide association studies (GWAS)** can be systematically dissected to uncover **disease mechanisms**:

1.  It highlights the **complex interplay** between genetic variants, regulatory elements, and downstream gene networks in shaping **disease phenotypes**.
2.  It suggests potential therapeutic strategies:
    - Targeting **IRX3** and **IRX5** could shift adipocyte metabolism towards a more **thermogenic profile**, counteracting obesity.
    - Modulating the activity of the identified enhancer or its **upstream regulator (ARID5B)** could serve as an **intervention point** for altering adipocyte differentiation.

### Conclusion of Step 6

The organismal phenotypic analysis validated the entire proposed mechanism, demonstrating that the single SNP identified at the **FTO locus** influences not just **gene expression**, but also **cellular metabolism**, and ultimately affects **whole-body energy balance** and **obesity risk**. By employing a combination of **genetic manipulation**, **functional assays**, and **in vivo validation**, we have provided a robust framework for understanding the causal relationship between **genetic variation** and **complex traits** such as obesity.

This comprehensive dissection of the FTO locus exemplifies a **systematic approach** for translating **genetic insights** into **mechanistic understanding** and **therapeutic opportunities**, serving as a model for future studies across a broad range of complex diseases.

## [1:12:33](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=4353s) Quantitative Trait Loci (QTLs): Bridge Genetics-to-Phenotype with Molecular Traits

The challenge in human genetics lies in understanding how **genetic variants** translate into **molecular and cellular changes**, ultimately leading to complex traits and diseases. A single GWAS locus may help identify associations, but to gain a mechanistic understanding, we must systematically connect **genetic variation** to **intermediate phenotypes** like gene expression and DNA methylation. This process involves identifying **Quantitative Trait Loci (QTLs)**, including **eQTLs** (expression QTLs) and **meQTLs** (methylation QTLs), as intermediate links between genotype and phenotype.

### From Genome-Wide Association to Molecular Insights

While **GWAS** links genotype directly to a disease phenotype, it is often a black box, providing limited information on **mechanistic pathways**. To unpack this, we can break the process down into **smaller, analyzable pieces**:

1.  **Genotype ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ Intermediate Phenotype (eQTL/meQTL Analysis):**
    - An **eQTL** study examines the relationship between **genetic variants** and changes in **gene expression**.
    - An **meQTL** study explores the relationship between **genetic variants** and changes in **DNA methylation** levels.
2.  **Intermediate Phenotype ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ Disease:**
    - By understanding how genetic variants affect intermediate molecular traits (e.g., expression, methylation), we can better link these effects to **disease outcomes**.

### Understanding the Directionality of Effects

One key concept here is the **unidirectional relationship** from genotype to molecular phenotypes:

- **Genetics affects molecular phenotypes, not vice versa**. For example, a SNP might alter the expression of a gene (eQTL) or the methylation status of a nearby CpG site (meQTL).
- However, the reverse is not true: **disease does not alter the genotype**, nor does it directly affect inherited genetic variation.

This **unidirectional arrow** becomes more complex when we examine the relationship between molecular phenotypes and disease. For example, changes in **DNA methylation** can occur as a consequence of disease, creating a **bidirectional arrow**. This makes it challenging to establish whether the methylation change is a **cause** or a **consequence** of the disease.

### Testing Causality: Genetic Component of Methylation

To address the **causality challenge**, we can focus on the **genetic component** of methylation:

1.  **Predict Methylation Levels from Genotype:**
    - Using **meQTL analysis**, we can impute or predict methylation levels based on the genotype. This allows us to isolate the **genetically driven** component of methylation changes.
2.  **Associate the Genetic Component with Disease:**
    - By correlating the **genetically imputed methylation levels** with disease phenotypes, we create a **unidirectional pathway** that suggests a **causal role** for the methylation changes, as they are driven by genetics and not influenced by the disease state.

### Systematic Analysis of QTLs

The advantage of using eQTL and meQTL analyses is that they provide a **genome-wide map** of how genetic variation affects molecular traits. This enables us to:

- Identify **many more loci** associated with disease than using GWAS alone.
- Enhance the **statistical power** by aggregating signals from multiple SNPs that collectively influence a molecular trait (e.g., gene expression or methylation).

### Integrative Framework: Relating Genotype, Molecular Traits, and Disease

To perform a comprehensive analysis, we relate:

1.  **Genotype**: The underlying genetic variation across individuals.
2.  **Molecular Traits**: Intermediate phenotypes like gene expression (eQTLs) and DNA methylation (meQTLs).
3.  **Disease Phenotype**: The clinical outcome or trait of interest.

By integrating these components, we create a **multi-layered framework** that can systematically dissect the genetic basis of disease. For example:

- We can relate **genotype** to **expression** using eQTL analysis.
- We can relate **methylation** to genotype using meQTL analysis.
- We can then associate **expression or methylation** changes with the **disease outcome**, leveraging the **QTL data**.

### The Challenge of Confounding Factors

In real-world data, numerous **confounding factors** can obscure the relationships between genotype, molecular traits, and disease. These include:

- **Cell Type Composition**: Different cell types may exhibit different expression or methylation profiles, affecting the observed signals.
- **Batch Effects**: Variations due to differences in experimental conditions or processing (e.g., different plates or batches).
- **Demographic Variables**: Factors like age, sex, or environmental exposures can influence molecular phenotypes and disease outcomes.

To address these, we must carefully **control for confounders**, using statistical techniques like **surrogate variable analysis** or including known covariates (e.g., age, sex, technical variables).

### Visualizing QTL Associations

To illustrate the relationship between SNPs and molecular phenotypes, we often use **Manhattan plots**, where:

- The **x-axis** represents the genomic coordinates (SNPs across the genome).
- The **y-axis** shows the **\-log10 P-value** of association (e.g., between a SNP and gene expression or methylation level).
- **eQTLs** and **meQTLs** with high P-values (low P-values on the logarithmic scale) are considered significant and often cluster near the **locus of interest**, suggesting a **local regulatory effect**.

For example, a SNP with an **astronomically significant P-value** (e.g., 10ÃƒÂ¢Ã‹â€ Ã¢â‚¬â„¢20010^{-200}10ÃƒÂ¢Ã‹â€ Ã¢â‚¬â„¢200) strongly predicts methylation at a nearby CpG site. This indicates a **highly predictable relationship**, where knowing the SNP genotype allows us to **accurately infer** the methylation status, even decades later in life.

### Local Effects of QTLs

A key finding from QTL studies is that:

- **50% of meQTLs** are found within **20 kilobases** (KB) of the methylation site.
- **90% of meQTLs** are within **75 KB**, indicating a predominantly **local regulatory effect**.

This suggests that genetic variation typically exerts its influence on nearby molecular traits, rather than acting through distant or trans effects.

### Summary

The systematic study of **Quantitative Trait Loci (QTLs)**, including **eQTLs** and **meQTLs**, provides a powerful framework for understanding the molecular basis of complex traits and diseases:

- By connecting genotype to intermediate molecular phenotypes, QTL analysis helps bridge the gap between genetic variation and clinical outcomes.
- **eQTL** and **meQTL** studies enable us to pinpoint **causal loci** and understand the **local regulatory effects** of genetic variants.
- Integrating QTL analysis with GWAS enhances our ability to identify **causal mechanisms** and offers new avenues for therapeutic intervention.

This approach sets the stage for a comprehensive and **systematic dissection** of the molecular pathways linking genetic variation to disease, ultimately facilitating the development of **precision medicine** strategies tailored to individual genetic profiles.

## [1:18:37](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=4717s) Mediation Analysis + Mendelian Randomization to Establish Causality

Understanding the **causal relationships** between genetic variants, molecular traits, and disease outcomes is one of the fundamental goals of genomics research. While **genome-wide association studies (GWAS)** can identify loci associated with disease, they do not establish **causal mechanisms**. To bridge this gap, we use **mediation analysis** and **Mendelian randomization**. These methods help determine whether a genetic variant influences disease **directly**, or **indirectly** through an intermediate molecular trait (e.g., gene expression, methylation).

### The Challenge of Causality

A key issue in interpreting genetic associations is determining whether the effect of a SNP on disease is **direct** or **mediated** through an intermediate phenotype:

1.  **Direct Effect**: The SNP directly influences the disease without any intermediate factor.
2.  **Mediated Effect**: The SNP influences an intermediate phenotype (e.g., gene expression), which in turn affects the disease outcome.
3.  **Reverse Causality**: The observed intermediate phenotype change may actually be a consequence of the disease, not a cause.

To address these, we use **conditional analysis** and **causal inference methods**.

### Mediation Analysis: Testing for Indirect Effects

**Mediation analysis** evaluates whether the effect of a genetic variant (SNP) on a disease outcome is mediated through an **intermediate phenotype** (e.g., gene expression, methylation). The key components are:

1.  **SNP ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ Intermediate Phenotype**: The association between the genetic variant and the intermediate phenotype (e.g., eQTL or meQTL).
2.  **SNP ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ Disease**: The direct association between the genetic variant and the disease outcome (identified through GWAS).
3.  **Intermediate Phenotype ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ Disease**: The association between the intermediate phenotype and the disease outcome.

To establish **causality**, we test whether the effect of the SNP on disease **diminishes** when we account for the intermediate phenotype. If the association weakens or disappears, this suggests that the intermediate phenotype **mediates** the SNP's effect on the disease.

### Conditional Analysis

The core idea is to perform a **conditional analysis**:

- **Unconditional Effect**: Measure the total effect of the SNP on the disease outcome.
- **Conditional Effect**: Measure the effect of the SNP on the disease **while controlling for the intermediate phenotype**.

If the conditional effect is substantially reduced compared to the unconditional effect, it suggests that the SNP's impact on disease is **mediated through** the intermediate phenotype.

### Distinguishing Mediation from Confounding

In real-world data, observed associations may be influenced by **confounding factors**. A **confounder** is a variable that influences both the intermediate phenotype and the disease, creating a **spurious association**. To distinguish true mediation from confounding, we examine the **residual correlation** after accounting for the intermediate phenotype:

- If the residual association between the SNP and disease is **weak** after conditioning on the intermediate phenotype, this supports **mediation**.
- If the residual association remains **strong**, it suggests either a **direct effect** or the presence of unmeasured confounders.

### Mendelian Randomization: Leveraging Genetic Variants for Causal Inference

**Mendelian randomization (MR)** is a powerful technique that uses genetic variants as **instrumental variables** to infer causality. It is based on the principle that **genetic variants are randomly assorted at conception**, akin to a natural randomized controlled trial. This allows us to use SNPs as **proxies for exposure** to test for causal relationships between the exposure (e.g., gene expression) and the outcome (e.g., disease).

##### **Key Steps in Mendelian Randomization**

1.  **Instrumental Variable (IV)**: The SNP serves as an instrument for the exposure. It must satisfy three conditions:
    - The SNP is associated with the exposure (e.g., gene expression).
    - The SNP influences the disease outcome **only through the exposure** (no direct effect).
    - The SNP is not associated with any confounder of the exposure-outcome relationship.
2.  **Causal Estimate**: The causal effect of the exposure on the outcome is estimated by **dividing the SNP-disease association** by the **SNP-exposure association**. This method effectively filters out confounding, leveraging the random assignment of alleles.

**Example.** Consider a scenario where we want to test if **lipid levels** (the exposure) mediate the effect of a SNP on cardiovascular disease (the outcome):

- We first establish that the SNP is associated with **lipid levels** (e.g., LDL cholesterol).
- We verify that the SNP is also associated with **cardiovascular disease**.
- Using Mendelian randomization, we estimate whether the effect of the SNP on cardiovascular disease is **mediated by changes in lipid levels**. If the causal effect remains significant after accounting for lipid levels, this suggests a direct impact of the SNP on the disease.

### Interpreting Results: Causal Pathways vs. Confounding

By combining **mediation analysis** and **Mendelian randomization**, we can distinguish between three scenarios:

1.  **Mediated Causal Effect**: The SNP affects the disease primarily through an intermediate phenotype (e.g., gene expression, lipid levels).
2.  **Independent Causal Effect**: The SNP directly affects the disease without mediation.
3.  **Confounded Association**: The observed effect is due to unmeasured confounding variables influencing both the intermediate phenotype and the disease.

This integrated approach provides a robust framework for identifying **causal relationships**, moving beyond mere associations to uncover **mechanistic insights**.

### Summary

- **Mediation Analysis** helps determine whether the effect of a SNP on disease is **indirect**, acting through an intermediate phenotype.
- **Mendelian Randomization** uses genetic variants as natural instruments to test for **causal relationships**, minimizing confounding bias.
- Together, these methods provide a powerful toolkit for dissecting the **complex pathways** linking genetic variation to disease, enabling us to identify potential **targets for therapeutic intervention**.

This comprehensive approach is crucial for advancing our understanding of the molecular mechanisms underlying complex traits and diseases, paving the way for **precision medicine** based on causal insights.

## [1:19:50](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=4790s) Heritability and Systems Genetics

**Heritability** is a key concept in genetics, capturing the proportion of the **total phenotypic variation** in a population that can be attributed to **genetic differences**. It provides a measure of how much **genetic variation** influences the observed differences in a trait among individuals.

### Defining Heritability

**Heritability (hÃƒâ€šÃ‚Â²)** is the fraction of the **phenotypic variance** that can be explained by **genetic variance**. Formally, it is expressed as:

h<sub>2</sub>\=Genetic Variance/Total Phenotypic Variance

- If a trait has **70% heritability**, this means that **70%** of the variability in that trait across individuals can be explained by genetic factors, while the remaining **30%** is due to **environmental factors** and measurement noise.
- Heritability is a **population-level statistic**. It does not imply that 70% of an individualÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s trait value is determined by genetics but rather that 70% of the variability **across the population** is due to genetic differences.

### Estimating Heritability

Heritability can be estimated using different methods, primarily based on **familial relationships** and genetic similarities:

1.  **Twin Studies**:
    - **Identical twins (monozygotic twins)** share **100% of their genetic material**. Thus, the correlation in their phenotypic traits is expected to be very high if the trait is highly heritable.
    - **Fraternal twins (dizygotic twins)** share **50% of their genetic material** on average. Comparing the phenotypic correlations between identical and fraternal twins allows us to estimate the **heritability** of a trait.
2.  h2=2ÃƒÆ’Ã¢â‚¬â€(Correlation of Identical TwinsÃƒÂ¢Ã‹â€ Ã¢â‚¬â„¢Correlation of Fraternal Twins)h^2 = 2 \\times (\\text{Correlation of Identical Twins} - \\text{Correlation of Fraternal Twins})h2=2ÃƒÆ’Ã¢â‚¬â€(Correlation of Identical TwinsÃƒÂ¢Ã‹â€ Ã¢â‚¬â„¢Correlation of Fraternal Twins)
3.  **Family and Pedigree Studies**:
    - By examining **siblings**, **cousins**, and more distant relatives, we can extend this analysis:
        - **Full siblings** share, on average, **50%** of their genetic makeup.
        - **First cousins** share **25%** of their genetic makeup.
        - **Second cousins** share **12.5%** of their genetic makeup.
    - The phenotypic similarity is expected to decrease as the genetic relatedness decreases. This trend can be used to estimate heritability.
4.  **Genome-Wide Complex Trait Analysis (GCTA)**:
    - In modern genetics, heritability can also be estimated from **unrelated individuals** using their **genomic data**. This method examines the **genetic similarity** across the entire genome and correlates it with **phenotypic similarity**.
    - The approach uses **single nucleotide polymorphisms (SNPs)** across many individuals to estimate the fraction of phenotypic variance explained by the combined effects of all measured SNPs.

### Narrow-Sense vs. Broad-Sense Heritability

- **Narrow-sense heritability (hÃƒâ€šÃ‚Â²)** considers only the additive genetic variance (the effects of individual alleles summed up).
- **Broad-sense heritability (HÃƒâ€šÃ‚Â²)** includes not only additive genetic effects but also **dominance** and **gene-gene interactions** (epistasis).

For most complex traits, we focus on **narrow-sense heritability** because it is more straightforward to estimate using population-based data.

### Heritability in Context: The Role of Environment

It is crucial to remember that heritability is not a fixed property of a trait; it can vary depending on the **population** and **environment**:

- In a **homogeneous environment**, the phenotypic differences are more likely due to genetic variation, leading to **higher heritability** estimates.
- In a **heterogeneous environment** with many external factors influencing the trait, the **environmental variance** increases, reducing the estimated heritability.

For example, the heritability of **height** is very high (~80-90%) in populations with good nutrition, but it can be lower in populations where malnutrition or other environmental factors play a significant role.

### Partitioning Heritability by Genetic Loci

To understand the genetic architecture of complex traits, we can **partition heritability** into components associated with different genetic loci:

- **Polygenic Traits**: Traits influenced by many genetic loci, each contributing a small effect. For example, height and intelligence are highly **polygenic**, with contributions from thousands of SNPs.
- **Oligogenic Traits**: Traits influenced by a few loci with larger effects.

By conducting **genome-wide association studies (GWAS)** and examining the **heritability explained by individual loci**, we can gain insights into the genetic architecture of the trait. Typically, GWAS studies capture only a fraction of the total heritability, a phenomenon known as the **"missing heritability" problem**.

### Systems Genetics: Integrating Multi-Omics Data

**Systems genetics** aims to bridge the gap between genetic variation and phenotypic traits by integrating multiple layers of biological data, including:

- **Genomic Data**: DNA sequence variations (e.g., SNPs).
- **Transcriptomic Data**: Gene expression profiles (eQTL analysis).
- **Epigenomic Data**: DNA methylation and chromatin accessibility (meQTL analysis).
- **Proteomic Data**: Protein expression levels and interactions.

By using **multi-omics approaches**, we can trace the flow of information from **genetic variants** to changes in gene expression and epigenetic modifications, ultimately influencing the observed phenotype.

### Summary

- **Heritability** quantifies the genetic contribution to phenotypic variation within a population.
- Estimation methods include **twin studies**, **family studies**, and modern approaches using **genome-wide data**.
- Heritability varies with the **environment** and **population** context and can be partitioned into **narrow-sense** and **broad-sense** components.
- The concept of **systems genetics** provides a framework for integrating genetic, transcriptomic, and epigenomic data to unravel the complex pathways linking **genetic variation** to **disease phenotypes**.

This comprehensive approach is crucial for advancing our understanding of the **molecular mechanisms underlying complex traits**, paving the way for **precision medicine** and the development of targeted interventions.

## [1:21:20](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=4880s) Partitioning heritability by functional annotations

The next step in understanding **heritability** is not only to measure how much of the phenotypic variance can be attributed to genetic factors, but to **partition** this heritability based on specific **functional annotations** of the genome. This approach helps us identify **which genomic regions** or **functional elements** contribute most to the genetic basis of complex traits.

### Heritability Decomposition: Analyzing Genetic Relatedness

To estimate heritability, we often look at the **genetic relatedness** between pairs of individuals and correlate it with their **phenotypic similarity**:

- **Genetic Relatedness**: For any pair of individuals, we can quantify how much of their genome they share. This measure is typically based on **SNP (single nucleotide polymorphism) similarity**.
- **Phenotypic Correlation**: We then assess how similar these individuals are in terms of the **trait of interest** (e.g., height, schizophrenia risk).

By regressing **phenotypic similarity** against **genetic similarity**, we obtain an estimate of the **total heritability** of the trait. However, this estimate includes contributions from **all parts of the genome**, without distinguishing which regions are most relevant.

### Partitioning Heritability by Genomic Regions

Instead of considering the entire genome, we can **partition the heritability** by focusing on **specific subsets of the genome**, such as:

1.  **Individual Chromosomes**:
    - We can estimate heritability separately for each chromosome. This allows us to identify chromosomes that might have a **disproportionate contribution** to the trait.
    - For example, if chromosome 21 explains a larger portion of the heritability for a given trait, it may contain regions with strong genetic effects.
2.  **Functional Genomic Annotations**:
    - We can refine this further by focusing on specific **functional elements** like **enhancers**, **promoters**, and **coding regions**.
    - For instance, we could estimate heritability using only SNPs located within **enhancers** that are active in certain cell types, such as **lipid-regulating enhancers** or **brain-specific enhancers**.

This approach allows us to ask more nuanced questions about where the genetic signals contributing to a trait are localized.

### Partitioning Heritability by Tissue-Specific Enhancers

By focusing on **tissue-specific regulatory elements**, we can gain insights into the **biological pathways** underlying a trait. For example:

- In **schizophrenia**, most of the heritability can be attributed to SNPs located within enhancers active in the **central nervous system (CNS)**.
- In contrast, SNPs located in enhancers active in **skeletal muscle** explain little to none of the heritability for schizophrenia, indicating that the trait is primarily driven by **neurological factors** rather than muscular ones.

This type of analysis helps to **validate the biological relevance** of specific tissues or cell types in relation to a trait. It provides a **systematic framework** for identifying which **biological systems** are involved in the genetic basis of complex diseases.

### The Power of Partitioning Heritability

Partitioning heritability has become an **extraordinarily powerful tool** in human genetics because it enables us to:

- **Attribute Genetic Influence**: We can determine which genomic regions or functional annotations contribute most to the trait.
- **Identify Relevant Biological Pathways**: By examining tissue-specific regulatory elements, we can uncover the **tissue context** of genetic associations, helping us pinpoint the **biological processes** that are disrupted in disease.
- **Guide Therapeutic Targeting**: This information can direct researchers to the **most relevant cell types and pathways**, aiding in the development of **precision therapies**.

For example, if we find that the heritability of **type 2 diabetes** is enriched in enhancers active in **liver cells**, it suggests that genetic risk factors are likely affecting **liver metabolism**. Conversely, if we find heritability for **cardiovascular disease** enriched in **endothelial cell enhancers**, this points to the role of **vascular biology** in the genetic risk for the disease.

### Summary

- Partitioning heritability by functional annotations helps us break down the **total genetic influence** into contributions from **specific genomic regions** or **functional categories**.
- This approach provides insights into the **biological mechanisms** underlying complex traits and diseases, highlighting the **tissues and pathways** most implicated by genetic variation.
- It is a key method for moving from **genome-wide signals** to a **more detailed understanding** of the underlying genetic architecture, guiding both **basic research** and **clinical applications**.

In conclusion, partitioning heritability allows us to **go beyond simple heritability estimates** and dissect the **genomic architecture** of complex traits, paving the way for a deeper understanding of human genetics and the **biological basis of disease**.

## [1:23:15](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=4995s) Omnigenic vs. polygenic vs. monogenic inheritance

In the landscape of genetic architecture, we can categorize traits based on the **number and nature of loci** that contribute to their variation. These categories span from **monogenic**, through **polygenic**, to the more recent concept of **omnigenic** inheritance. Understanding these distinctions is critical for appreciating the complexity of genetic influences on various traits.

### 1\. Monogenic Traits

Monogenic traits are characterized by a **single genetic locus** that has a **major effect** on the phenotype. These are often **Mendelian diseases**, where mutations in a single gene are sufficient to cause the trait:

- **Examples**: Cystic fibrosis (caused by mutations in the _CFTR_ gene), Huntington's disease, and sickle cell anemia.
- **Mechanism**: The phenotype can be directly attributed to a specific variant, and the inheritance pattern follows **Mendelian principles** (dominant, recessive, etc.).
- **Clinical Relevance**: Monogenic traits are relatively straightforward to study and diagnose because of their clear genetic basis.

While monogenic disorders provide clear examples of genetic causality, they are the exception rather than the rule in complex traits and common diseases.

### 2\. Polygenic Traits

Polygenic traits are influenced by **many genetic variants**, each contributing a **small effect** to the overall phenotype:

- **Examples**: Height, schizophrenia, type 2 diabetes, and obesity.
- **Mechanism**: The trait arises from the cumulative effects of **hundreds to thousands of loci**, each with a modest influence. The risk is distributed across many variants, each with a small additive effect.
- **Genetic Architecture**: Polygenic traits typically show a **normal distribution** in the population, resulting from the combined effect of many variants.
- **Clinical Implications**: The polygenic nature of these traits complicates their study, as no single variant has a decisive impact. Instead, **polygenic risk scores** are used to aggregate the effects of many SNPs to predict an individual's risk.

Polygenic inheritance reflects the complexity of biological systems, where many small perturbations across the genome collectively influence the phenotype.

### 3\. Omnigenic Traits

The concept of **omnigenic inheritance** takes the idea of polygenicity even further. It suggests that for some traits, **nearly every gene** can influence the phenotype, either directly or indirectly:

- **Definition**: An **omnigenic trait** is influenced not only by many loci with small effects but also by the **entire network of genes and biological pathways**. In other words, **nearly every gene** can potentially impact the trait through its connections to core regulatory pathways.
- **Examples**: Traits like **coronary artery disease (CAD)**, **lifespan**, and **healthspan** may exhibit omnigenicity. For these traits, genetic associations are not confined to a few core pathways but are seen across a wide range of biological processes.
- **Mechanism**: Omnigenic traits arise because of the **interconnectedness** of biological systems. While core genes may have a direct and strong influence, **peripheral genes** can also contribute through their indirect effects on core pathways. This reflects the **complex network structure** of gene regulation, where peripheral genes can modulate the activity of key regulatory nodes.
- **Implications for Genetic Studies**: As we increase the power of genome-wide studies (e.g., by increasing sample size), we tend to find more and more loci associated with a trait. This suggests that **many biological processes** might influence the trait, leading us to the idea of **omnigenicity**.

### The Shift from Polygenicity to Omnigenicity

The shift from thinking about traits as purely **polygenic** to considering them as **omnigenic** represents an evolution in our understanding of **genetic architecture**:

- In a **polygenic model**, we assume that a **finite set of variants** contribute to the trait, primarily through their additive effects.
- In an **omnigenic model**, we assume that **nearly every gene** has some potential impact on the trait, either through direct effects on core pathways or through **indirect modulation** of those pathways.

This broader perspective acknowledges the **network-like nature** of biological systems, where **distant genetic variants** can still influence the trait through their effects on the broader regulatory network.

### Centrality vs. Diffuseness in Genetic Effects

A key distinction in the omnigenic framework is the difference between:

- **Central Effects**: These are the effects of **core genes** that are directly involved in the primary biological pathway underlying the trait. For example, genes involved in **neuronal function** for schizophrenia or genes regulating **lipid metabolism** for coronary artery disease.
- **Diffuse Effects**: These are the effects of **peripheral genes**, which might influence the trait indirectly through their interactions with core regulatory genes. This is akin to the **butterfly effect**, where small changes in peripheral genes can have broader, less predictable impacts on the phenotype.

The challenge in genetics is not merely to detect associations but to **distinguish central, causally important effects** from diffuse, background effects that contribute indirectly.

### Summary

- **Monogenic Traits**: Governed by a single genetic locus; relatively straightforward Mendelian inheritance.
- **Polygenic Traits**: Influenced by many loci, each contributing a small effect; cumulative genetic risk can be estimated through polygenic risk scores.
- **Omnigenic Traits**: Influenced by almost the entire genome; nearly every gene can impact the trait through its connections to core pathways, reflecting the **interconnectedness** of biological systems.

### Conclusion

The concept of **omnigenicity** expands our understanding of complex traits, suggesting that **biological processes are deeply interconnected**. As we increase the power of genetic studies and delve deeper into the genome, we may find that nearly every biological process can influence nearly every trait. The challenge is to move beyond detecting associations and to develop methods that help us **dissect the core pathways** and **causal mechanisms** amidst the vast network of interconnected genetic effects.

This realization underscores the need for **systems-level approaches** in genetics, integrating diverse data types (e.g., gene expression, epigenomics, protein interactions) to build a comprehensive understanding of how genetic variation translates into complex phenotypes.

## [1:25:25](https://www.youtube.com/watch?v=1heL5_yWVTs&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=18&t=5125s) Summary

We covered a wide array of interconnected topics, building a detailed framework for understanding how **genetic variation influences disease phenotypes** through a series of molecular, cellular, and organismal mechanisms. LetÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s review the main points discussed:

### 1\. Genetic Variation, GWAS, and Polygenic Scores

- We started with a **review of genetic variation** and genome-wide association studies (**GWAS**, pronounced "G-was"), emphasizing how we identify **risk loci** associated with complex traits.
- The concept of **polygenic scores (PGS)** was introduced, showcasing how aggregating the small effects of many common variants can explain a significant portion of individual risk, often on par with family history.
- We discussed how GWAS provides a **global view of genetic associations**, and how we can use **functional enrichment analysis** across diverse tissues and cell types to gain biological insights into the underlying disease mechanisms.

### 2\. From GWAS Locus to Biological Mechanism

- We dived deeper into the analysis of **individual GWAS loci**, using an example to show how we can integrate multiple lines of evidence:
    - **Linkage disequilibrium** for identifying candidate variants.
    - **Epigenomic annotations** to prioritize functional regions.
    - **Chromatin conformation capture** for linking enhancers to target genes.
- This approach allowed us to go from an associated region to identifying specific **causal variants**, the likely **regulatory elements**, and the **target genes** they influence, thus elucidating the **molecular mechanism**.

### 3\. Quantitative Trait Loci (eQTLs and meQTLs) Analysis

- We discussed **expression quantitative trait loci (eQTLs)** and **methylation quantitative trait loci (meQTLs)** as powerful tools to bridge the gap between genotype and phenotype:
    - eQTLs identify genetic variants that influence gene expression.
    - meQTLs identify genetic variants that impact DNA methylation levels.
- These analyses provide **intermediate phenotypes**, helping us understand how genetic variants influence molecular traits, which in turn affect disease risk.
- The importance of distinguishing between **genetic causes** and **disease consequences** was emphasized, especially when interpreting correlations between molecular traits and disease phenotypes.

### 4\. Heritability and Systems Genetics

- We defined **heritability** as the proportion of phenotypic variance attributable to genetic variance and discussed methods for estimating it using both **related and unrelated individuals**.
- We then extended this to **partitioning heritability** by functional annotations (e.g., enhancers active in specific tissues), allowing us to identify the **biological pathways** most relevant to a given trait.
- This analysis helps us understand not just **how much** of a traitÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s variance is explained by genetics, but also **where in the genome** (and in which functional contexts) the relevant genetic signals are concentrated.

### 5\. Omnigenic, Polygenic, and Monogenic Models

- We explored the spectrum of genetic inheritance models:
    - **Monogenic traits** are controlled by single genes (e.g., cystic fibrosis).
    - **Polygenic traits** are influenced by many loci with small effects (e.g., height, schizophrenia).
    - **Omnigenic traits** reflect an emerging view where nearly every gene may have a potential influence through its interactions within a complex regulatory network.
- The concept of **omnigenicity** highlights the pervasive interconnectedness of biological processes, suggesting that **nearly every pathway** could potentially affect the trait, albeit with varying degrees of centrality and specificity.

### 6\. Building a Systematic Framework for Genetic Studies

- We concluded with a call to **build systematic methods** for studying genetic effects, emphasizing the integration of **GWAS**, **QTL mapping**, and **functional genomics**.
- The goal is to create a **comprehensive pipeline** that can handle multiple lines of evidence and elucidate the complex pathways from genetic variation to disease phenotypes.


## Biological Concepts
Key biological concepts are explained in the source-faithful notes above and cross-linked through entity pages such as [[DNA]], [[RNA]], [[Gene]], [[Gene Expression]], [[Protein]], [[Enhancer]], [[Promoter]], [[Chromatin]], [[SNP]], [[Variant]], [[eQTL]], and [[Heritability]].

## Machine Learning / Computational Concepts
Relevant computational ideas include representation choice, objective functions, inference, optimization, graph/message-passing structure, sequence modeling, and validation. See [[mlcb-methods-map]].

## Methods, Models, and Algorithms
The lecture-specific methods are preserved above. Reusable method notes live under Wiki/Methods/.

## Equations and Notation
Equations explicitly present in the source are preserved above. Course-level equation notes live under Wiki/Equations/.

## Figures, Diagrams, and Visual Explanations
Original slide images are not embedded in the current source. Explanation is based on lecture text only. See [[figure-index]].

## Examples From the Lecture
Examples are retained in the detailed source-faithful notes above. Important examples should be connected back to source files before being used as claims.

## Cross-Lecture Connections
See [[mlcb-cross-lecture-connections]] for the full course map. This lecture connects to [[mlcb-2024-computational-biology]] and [[mlcb-complete-study-guide]].

## Common Confusions and Clarifications
### Confusion: The model output is automatically a biological mechanism.
Clarification: The model output becomes mechanistic only when connected to genes, variants, proteins, cells, pathways, or validation experiments.

### Confusion: Noise is only technical error.
Clarification: Biological systems contain technical noise, biological variability, sampling effects, and stochastic behavior.

### Confusion: A method is useful independent of representation.
Clarification: In MLCB, representation determines what the method can learn.

## Review Questions and Answers
### Q1. What should you be able to explain from this lecture?
You should be able to explain how eQTLs, meQTLs, mediation, Mendelian randomization, heritability, GCTA, partitioned heritability, integrative disease mechanism, and the FTO obesity locus connects a biological problem to a computational representation, model, or algorithm.

### Q2. What should you be able to explain from this lecture?
You should be able to explain how eQTLs, meQTLs, mediation, Mendelian randomization, heritability, GCTA, partitioned heritability, integrative disease mechanism, and the FTO obesity locus connects a biological problem to a computational representation, model, or algorithm.

### Q3. What should you be able to explain from this lecture?
You should be able to explain how eQTLs, meQTLs, mediation, Mendelian randomization, heritability, GCTA, partitioned heritability, integrative disease mechanism, and the FTO obesity locus connects a biological problem to a computational representation, model, or algorithm.

### Q4. What should you be able to explain from this lecture?
You should be able to explain how eQTLs, meQTLs, mediation, Mendelian randomization, heritability, GCTA, partitioned heritability, integrative disease mechanism, and the FTO obesity locus connects a biological problem to a computational representation, model, or algorithm.

### Q5. What should you be able to explain from this lecture?
You should be able to explain how eQTLs, meQTLs, mediation, Mendelian randomization, heritability, GCTA, partitioned heritability, integrative disease mechanism, and the FTO obesity locus connects a biological problem to a computational representation, model, or algorithm.

### Q6. What should you be able to explain from this lecture?
You should be able to explain how eQTLs, meQTLs, mediation, Mendelian randomization, heritability, GCTA, partitioned heritability, integrative disease mechanism, and the FTO obesity locus connects a biological problem to a computational representation, model, or algorithm.

### Q7. What should you be able to explain from this lecture?
You should be able to explain how eQTLs, meQTLs, mediation, Mendelian randomization, heritability, GCTA, partitioned heritability, integrative disease mechanism, and the FTO obesity locus connects a biological problem to a computational representation, model, or algorithm.

### Q8. What should you be able to explain from this lecture?
You should be able to explain how eQTLs, meQTLs, mediation, Mendelian randomization, heritability, GCTA, partitioned heritability, integrative disease mechanism, and the FTO obesity locus connects a biological problem to a computational representation, model, or algorithm.

### Q9. What should you be able to explain from this lecture?
You should be able to explain how eQTLs, meQTLs, mediation, Mendelian randomization, heritability, GCTA, partitioned heritability, integrative disease mechanism, and the FTO obesity locus connects a biological problem to a computational representation, model, or algorithm.

### Q10. What should you be able to explain from this lecture?
You should be able to explain how eQTLs, meQTLs, mediation, Mendelian randomization, heritability, GCTA, partitioned heritability, integrative disease mechanism, and the FTO obesity locus connects a biological problem to a computational representation, model, or algorithm.

## Key Takeaways
- eQTLs, meQTLs, mediation, Mendelian randomization, heritability, GCTA, partitioned heritability, integrative disease mechanism, and the FTO obesity locus is part of the MLCB modeling arc.
- The biological interpretation is as important as the computational method.
- Source-grounded details above should be used for deep questions.

## Pages to Update or Create
- [[mlcb-2024-computational-biology]]
- [[mlcb-complete-study-guide]]
- [[mlcb-methods-map]]
- [[mlcb-cross-lecture-connections]]

## Needs Review
- Original slide images are not embedded in this source, so figure explanations are text-only.


## Knowledge Graph Extraction

> [!info] Auto-generated 2026-05-25 from `retrieval/knowledge_graph.json`
> Entities extracted from this lecture. See `retrieval/lecture_index.json` for full details.

### Entities Introduced

- [[heritability]]
- [[ld-score-regression]]
- [[colocalization]]
- [[fine-mapping]]
- [[eqtl]]
- [[disease-circuitry]]
- [[enhancer]]
- [[transcription-factor]]

### Cluster Membership

- [[cluster-map-genetics-disease]]
- [[cluster-map-regulatory-genomics]]

### Key Relationships (from KG)

See [[lecture-entity-map]] for the full relationship list, and [[knowledge-graph-index]] for the global entity index.
