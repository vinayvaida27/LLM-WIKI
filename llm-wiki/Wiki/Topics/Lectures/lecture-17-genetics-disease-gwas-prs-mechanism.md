---
tags:
  - "topic"
topics:
  - "MLCB"
status: updated
created: 2026-05-24
updated: 2026-05-24
sources:
  - "Raw/Sources/lecture_17_genetics_disease_gwas_prs_mechanism.md"
source_count: 1
aliases:
  - "Lecture 17 - Genetics, Disease, GWAS, PRS, Mechanism"
---

# Lecture 17 - Genetics, Disease, GWAS, PRS, Mechanism

## Source
- Raw source: `Raw/Sources/lecture_17_genetics_disease_gwas_prs_mechanism.md`
- Supporting source: `Raw/Files/lecture_17_genetics_disease_gwas_prs_mechanism.md`
- Existing related pages: [[mlcb-2024-computational-biology]], [[mlcb-complete-study-guide]], [[mlcb-methods-map]]
- Last updated: 2026-05-24

## Executive Summary
Lecture 17 - Genetics, Disease, GWAS, PRS, Mechanism develops genetic variation, GWAS, SNP arrays, haplotypes, Manhattan plots, population structure, linkage analysis, PRS, fine-mapping, FTO, and omnigenic traits. This page intentionally preserves substantial source detail so a future LLM can reason from the wiki without immediately reopening the raw transcript.

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
- Genetics: From Ancient Times to Today
- Disease-associated Variants
- Challenge of Mechanism
- Variation and Disease
- Defining Variants
- Common Variants and Haplotype Blocks
- GWAS Genome-wide Association Studies: Genotype-Phenotype
- Common/weak-effect vs. Rare/Strong-effect variants
- Family studies (Linkage Analysis) vs. Unrelated Individuals (GWAS)
- Population Differences, Ancestry Painting, PCA, Multi-Ethnic Fine-Mapping

## Detailed Lecture Notes
The notes below preserve the processed source order and are intentionally detailed.

# Lecture 17 - Genetics, Disease, GWAS, PRS, Mechanism

Video: [Lecture17 Disease GWAS PRS Mechanism](https://www.youtube.com/watch?v=RlKu1eDbtUQ&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=17)

Slides: [Lecture17_Genetics_GWAS_PRS_Mechanism.pdf](https://www.dropbox.com/scl/fi/uutwoatvvqxg62e42feh3/Lecture17_Genetics_GWAS_PRS_Mechanism.pdf?rlkey=k2mg1k2v3exhm1rc53tvwur3s&dl=0)

## [00:00](https://www.youtube.com/watch?v=RlKu1eDbtUQ&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=15&t=0s) Genetics: From Ancient Times to Today

**Introduction to Genetic Understanding in Disease
**In this lecture, we bridge previous insights into protein modeling, chemical structure, and genomic understanding to address a critical question: how do genetic mechanisms contribute to disease? By synthesizing these domains, we can begin to dissect the genetic basis of human diseases and uncover pathways that lead to effective therapeutic strategies. The focus is to leverage genetic information not only to identify regions associated with disease but to reveal actionable mechanisms that can be targeted or modified to reverse disease pathways.

**Genetics and the Role of Genome-Wide Association Studies (GWAS)
**Genome-wide association studies (GWAS) enable an **unbiased exploration of genetic regions** across the genome that are statistically associated with disease traits. GWAS scans the genome to identify common genetic variants linked to specific diseases, delivering a region-based view of disease risk. This method, while powerful in its scope and scale, identifies **associations without mechanistic insight**. Thus, while GWAS can pinpoint regions of interest, understanding the underlying biological mechanism remains a complex and necessary challenge for translating these associations into therapeutic insights.

**Core Topics in Genetic Variation, GWAS, Polygenic Risk Scores, and Mechanistic Analysis**

1.  **Genetic Variation**: A foundational understanding of genetic diversity across human populations, encompassing how this diversity manifests in phenotypic traits and disease susceptibility.
2.  **GWAS Techniques**: Approaches and statistical frameworks used to identify regions of the genome with genetic variants associated with diseases, paving the way for understanding genotype-phenotype relationships.
3.  **Polygenic Risk Scores (PRS)**: Calculation and utility of PRS involve aggregating small contributions from multiple genetic variants to predict an individualÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s overall genetic predisposition to certain diseases. PRS operates independently of the mechanisms of individual variants, focusing solely on cumulative risk.
4.  **Mechanistic Dissection**: Translating GWAS findings into mechanistic insights requires additional analysis and functional validation. The goal is to move from associative data to **causal understanding of disease pathways**, enabling interventions at a molecular or cellular level.

**Historical Context: Ancient Genetic Manipulation Through Selective Breeding
**From early agricultural societies, humans have influenced genetic selection, reshaping crops, animals, and ecosystems through selective breeding practices. By consciously selecting plants for taste, resilience, or productivity, and animals for specific traits like strength or temperament, humans have long driven the evolutionary trajectories of these species. **Coevolution between plants and animals**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âsuch as the relationship between apple trees and horses, where animals help spread seeds in exchange for nutritionÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âdemonstrates early human influence over genetic outcomes. This historical context underscores the long-standing human understanding of inheritance and the power of selection, even before formal genetic principles were established.

**The Revolution of Mendelian Genetics
**With Gregor MendelÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s experiments in pea plants, the principles of **discrete inheritance** emerged, providing the basis for modern genetics. MendelÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s work identified dominant and recessive traits and demonstrated that traits are inherited independently, a foundational insight that would later define the concept of genes and alleles. Although MendelÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s findings initially went unrecognized, they laid the groundwork for understanding how traits could be inherited without blending, despite the continuous variation observed in traits like height or eye color. His experiments revealed that continuous traits could arise from the combined effects of multiple discrete genetic factors, thus bridging the gap between **phenotypic continuity and genetic discreteness**.

This section sets the stage for understanding how genetic variation, combined with advanced tools like GWAS, enables modern scientists to explore the genetic architecture of diseases with unprecedented detail and precision.

## [17:07](https://www.youtube.com/watch?v=RlKu1eDbtUQ&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=15&t=1027s) Disease-associated Variants

**Identifying Genetic Variants Linked to Disease
**Disease-associated variants are genetic mutations that increase or decrease an individualÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s risk for specific conditions. For instance, certain mutations in the _ARMS2_, _TP53_, _SIN3_, and _C2_ genes have been linked to an elevated risk for age-related macular degeneration (AMD), a condition that leads to progressive central vision loss as individuals age. Understanding the genetic basis of such diseases, and identifying specific variants that contribute to increased susceptibility, enables us to target these pathways for potential treatments. This knowledge serves as the foundation for precision medicine, where interventions can be tailored to an individualÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s genetic risk profile.

**From Association to Treatment
**An example of the potential impact of these insights is in therapeutic development. By identifying genetic variants that elevate AMD risk, researchers and companies, like the one led by Dr. Leon Sad, have developed compounds specifically designed to address the molecular mechanisms associated with these genetic variants. Thus, genetic information does more than just predict riskÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âit can directly inform treatment options. This pathway from genetic association to targeted therapy demonstrates the value of understanding disease mechanisms at the genetic level.

**Methods for Identifying Disease-associated Variants
**The process of identifying these disease-associated variants involves analyzing the genome across a large number of individuals. In studies examining AMD or other traits, researchers use genome-wide scans to compare genetic variation in affected individuals (cases) against those without the condition (controls). By testing each variant across the 23 pairs of human chromosomes, scientists evaluate the statistical likelihood that specific variants are associated with the condition in question, rather than occurring by random chance.

**Case-Control Studies and Variant Analysis
**In practice, these analyses rely on extensive **case-control studies**, where genetic data from patients with the condition are compared against a control group matched by age and other relevant factors. Differences in variant frequencies between cases and controls help highlight **loci** that are potentially causal or at least significantly associated with disease risk. This approach also allows researchers to classify variants as either **risk-increasing** or **protective**, based on whether their presence is associated with higher or lower incidence of the disease.

By understanding disease-associated variants through these comparative studies, we can not only assess an individual's risk for diseases but also identify points of intervention that can lead to effective therapeutic options.

## [19:19](https://www.youtube.com/watch?v=RlKu1eDbtUQ&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=15&t=1159s) Challenge of Mechanism

**Understanding Variant Function Beyond Association
**Identifying genetic variants associated with diseases presents an immediate follow-up challenge: deciphering _how_ these variants contribute to disease mechanisms. Most variants reside in a complex genomic context that includes both coding and non-coding regions, each carrying unique functions and regulatory roles. For example, within protein-coding regions, variants might be directly involved in altering protein structure or function. But in non-coding regionsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âwhere many disease-associated variants are foundÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âtheir roles are less straightforward, often influencing gene expression, splicing, or other regulatory processes without directly coding for proteins.

**Annotating Functional Genomic Regions
**Functional annotations help clarify the role of variants. For example, a variant within an exon may change the amino acid sequence of a protein, whereas variants in introns or intergenic regions may alter regulatory elements, such as enhancers or promoters. In a sequence where _ATG_ denotes a start codon for an exon and adjacent splice sites signal boundaries for intron removal, we can begin to parse out coding from non-coding influences. Some disease-associated variants, however, lie in regions like upstream regulatory sequences or intronic spaces within unrelated genes, making their functional implications more ambiguous. A variant upstream of _TP53_ or within an intron of _SIN3_ could potentially impact nearby or distant gene expression or interact with non-coding RNAs, such as microRNAs or tRNAs, affecting various levels of gene regulation.

**Key Questions and Steps in Mechanism Exploration
**To address these challenges, we aim to:

1.  **Catalog Genetic Variants**: Establish a comprehensive map of single nucleotide polymorphisms (SNPs) and other genetic variants in the human genome.
2.  **Associate Variants with Disease**: Use genome-wide association studies (GWAS) to link these variants with specific diseases, identifying loci that significantly correlate with disease traits.
3.  **Translate Association to Mechanism**: Leverage GWAS results and functional annotations to dissect disease mechanisms. This includes examining variant enrichments in functional regions and integrating multi-omic data to pinpoint regulatory networks or pathways affected by these variants.
4.  **Pathway to Therapeutic Development**: With an understanding of variant impact, we can explore therapeutic strategies aimed at modifying the affected pathways or reversing the underlying disease processes.

Each of these steps moves us closer to translating genetic associations into actionable insights for understanding, diagnosing, and treating complex diseases.

## [21:25](https://www.youtube.com/watch?v=RlKu1eDbtUQ&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=15&t=1285s) Variation and Disease

**Human Genetic Variation
**Each human cell contains two copies of the genome, one from each parent, divided into 23 chromosomes with a total of 3.2 billion DNA letters. Despite only 1.5% of the genome encoding approximately 20,000 genes, millions of polymorphismsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âvariations in DNA sequenceÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âexist across individuals, providing unique genetic "fingerprints." These polymorphisms, or alleles, arise from different forms of a gene or DNA sequence across populations.

**Types of Genetic Variation**

1.  **Single Nucleotide Polymorphisms (SNPs):** These occur when a single nucleotide, such as cytosine (C), mutates to another base, like guanine (G). SNPs happen roughly once per 1,000 bases in the genome, allowing vast genetic diversity and potential disease associations.
2.  **Insertions and Deletions (Indels):** These variations involve the addition or removal of one or more nucleotides, occurring approximately once every 10,000 bases. Indels can disrupt gene sequences or regulatory regions, impacting gene function.
3.  **Short Tandem Repeats (STRs):** STRs involve repeating sequences, like GTC repeated multiple times. Variability in STR length can lead to disease if it alters protein structure or expression, especially within coding regions.
4.  **Structural Variants or Copy Number Variants (CNVs):** Large-scale structural changes, including deletions, duplications, or inversions, occur roughly every million bases. CNVs can affect gene dosage, leading to an increased or decreased number of gene copies, often with significant phenotypic effects.

**Impact of Genetic Variants on Disease
**Genetic variants contribute to disease by altering protein structure or expression. For example:

- **Sickle Cell Anemia:** A single amino acid substitution in hemoglobinÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âreplacing glutamic acid with valineÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âcauses red blood cells to deform, leading to severe health issues if inherited from both parents. However, carrying one copy is protective against malaria, illustrating how a disease-associated variant in one population context can be beneficial in another.
- **Huntington's Disease:** Caused by an expanded repeat of the CAG trinucleotide within the _HTT_ gene. Individuals with more than 30 CAG repeats develop Huntington's, leading to neurodegeneration, movement issues, and dementia. Repeat expansions like these can profoundly affect protein function and stability.
- **Cystic Fibrosis:** In the _CFTR_ gene, a deletion of a single amino acid results in cystic fibrosis, a disorder that impairs lung function and causes chronic infections.

**Mapping Variants to Disease Mechanisms
**Studying these types of variations helps us link genetic changes to specific diseases by examining how variations affect protein function, gene regulation, or cellular pathways. Disease mechanisms, once identified, can reveal therapeutic targets and intervention strategies that address the root cause rather than merely managing symptoms.

## [25:49](https://www.youtube.com/watch?v=RlKu1eDbtUQ&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=15&t=1549s) Defining Variants

**Understanding Variant Frequency
**To study genetic variation and its implications in disease, it is essential to classify variants by frequency. Variants can be categorized as:

- **Common Variants:** Present in more than 5% of the population.
- **Low-Frequency Variants:** Found in less than 5% of individuals.
- **Rare Variants:** Extremely uncommon, sometimes observed in only one individual.
- **Private or De Novo Variants:** Unique mutations that do not appear in the individual's parents; these occur spontaneously in the germline or during somatic cell divisions.

**Allele Types and Population Specificity
**Variants can also be classified based on population data:

- **Major vs. Minor Allele:** A variantÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s status as ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œmajorÃƒÂ¢Ã¢â€šÂ¬Ã‚Â or ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œminorÃƒÂ¢Ã¢â€šÂ¬Ã‚Â depends on its frequency within a particular population. For example, an allele with 0.3% frequency in Europeans would be the minor allele.
- **Reference vs. Alternate Alleles:** Refers to the version found in a selected reference genome.
- **Ancestral vs. Derived Alleles:** By comparing the human genome to our closest evolutionary relatives (e.g., chimpanzees), we can identify which allele likely represents the ancestral state. Derived alleles represent genetic changes from this ancestral version.

**The Human Genome and Diverse Genetic Backgrounds
**The first human genome sequence, finalized in 2003, represented one individualÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s DNA and served as a reference. However, to understand global genetic diversity, scientists now sequence genomes from a broad range of populations, revealing distinct regional allele patterns. Most human genetic diversity originates from African populations, reflecting humanity's origin. Migration out of Africa around 50,000 years ago introduced this variation globally, with new variants arising as humans spread across continents.

**Cataloging Variants with SNP Arrays
**Once common variants, such as SNPs, are cataloged, genotyping can be streamlined. Rather than resequencing entire genomes, researchers use SNP arrays, which contain probes specific to known variant sites. Each probe can detect the presence of variant forms (e.g., "C" or "G" at a particular SNP) through hybridization, making it possible to determine an individual's genotype at thousands of sites efficiently.

This foundational understanding of variant classification and cataloging enables targeted genetic studies, essential for linking specific genetic changes to disease and furthering the study of human evolution and population genetics.

## [31:18](https://www.youtube.com/watch?v=RlKu1eDbtUQ&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=15&t=1878s) Common Variants and Haplotype Blocks

**Profiling Common Variants with DNA Microarrays
**Advances in DNA microarray technology from the 1990s enabled the efficient profiling of genetic variation. By hybridizing DNA samples to probes, researchers can identify which version of an allele a person carries. For instance, a particular SNP may show red if itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s "GG," green if "AA," and yellow if "AG," simplifying genotyping.

**Haplotype Blocks and Co-inheritance Patterns
**Genomic variants are often inherited as groups known as **haplotype blocks**. These are chunks of DNA within which genetic variants are frequently co-inherited due to limited recombination events, called hotspots, that break up these blocks across generations. The pattern of co-inheritance within a block reveals regions of the genome where variants are closely linked, meaning that if an individual has one variant in a block, they likely carry others within that same block.

**Population Differences in Haplotype Structure
**The structure of haplotype blocks can differ significantly between populations. For instance, African, European, and Asian populations may show variations in haplotype size and recombination frequency. For example, East Asian populations might display additional recombination events within a haplotype that arenÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t observed in European populations, leading to smaller blocks and more genetic diversity.

**Advantages and Challenges of Haplotype Blocks in Disease Association
**Haplotype blocks offer both benefits and drawbacks in genetic studies:

- **Advantage:** Researchers can use a single SNP within a haplotype to infer the presence of other variants, reducing the number of SNPs that need to be measured directly. This approach allows for efficient genotyping, especially useful in large-scale studies.
- **Challenge:** Haplotype blocks complicate pinpointing causal variants. When a disease is associated with a haplotype block, it becomes difficult to identify the exact variant responsible since all variants in the block are inherited together and thus appear to be co-associated with the disease.

**New Mutations Within Existing Haplotype Blocks
**Mutations continue to arise within existing haplotype blocks. These new variants accumulate as populations diverge geographically, contributing to regional genetic diversity. For example, specific alleles may define lineages unique to certain populations or regions, such as Asia or the Americas. Thus, genetic diversity expands even within stable haplotype structures, with new mutations creating additional layers of complexity.

Understanding haplotype blocks provides essential insights into the patterns of human genetic variation, helping researchers interpret genetic associations and their implications across different populations. This framework allows for more targeted exploration of disease-linked variants while acknowledging the evolutionary context in which they arise.

## [38:03](https://www.youtube.com/watch?v=RlKu1eDbtUQ&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=15&t=2283s) GWAS Genome-wide Association Studies: Genotype-Phenotype

**Objective of GWAS
**A genome-wide association study (GWAS) seeks to correlate specific alleles with traits or diseases across the genome. It does this by testing each common genetic variant for associations with a particular phenotype. The statistical significance of these associations is quantified, typically represented as a **negative log10 p-value**. Higher values indicate stronger evidence that an association is non-random, and thus more likely to be biologically meaningful. Results are often visualized as **Manhattan plots**, where peaks represent regions with strong associations.

**Understanding Recombination and Haplotype Blocks
**In GWAS, peaks in the Manhattan plot often reflect haplotype blocks that carry an association signal. Due to co-inheritance within these blocks, nearby SNPs exhibit correlated associations, creating "skyscraper" peaks. Recombination hotspots mark the boundaries of these blocks, and understanding the co-inheritance patterns between variants helps researchers interpret the structure of associated regions. Some hotspots can further fragment a region, potentially allowing finer resolution in pinpointing causal variants, though often, haplotype structure limits this precision.

**Adjusting for Statistical Inflation
**Correcting for the sheer number of tests in GWAS is essential to avoid false positives. With approximately a million independent tests (considering haplotype blocks), the accepted genome-wide significance threshold is a p-value of 5 ÃƒÆ’Ã¢â‚¬â€ 10^-8, correcting for multiple hypotheses. This ensures that only robust associations surpass this stringent threshold.

**Addressing Confounders in GWAS
**Several confounding factors can introduce bias in GWAS. **Population structure** can cause associations linked to ancestry rather than function. Similarly, **relatedness** between individuals, **sex biases**, and **population genetics factors** like Hardy-Weinberg equilibrium deviations must be controlled to ensure accurate results. Historically, lack of stringent control led to a "GWAS crisis," with numerous associations failing replication. Improved methodologies, including standardized significance thresholds, have since enhanced the reliability of GWAS findings.

**Limitations of GWAS: Bias Toward Common Variants
**GWAS has traditionally focused on common variants due to the limited number of genomes available for early studies. This means associations are often biased toward common variants with higher minor allele frequencies, generally over 5%. Although capturing nearly all common variants, these studies often miss rare variants, leading to an ascertainment bias. Thus, while GWAS is powerful, it has inherent limitations in detecting associations with rare genetic variants, which may also play crucial roles in disease.

## [50:52](https://www.youtube.com/watch?v=RlKu1eDbtUQ&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=15&t=3052s) Common/weak-effect vs. Rare/Strong-effect variants

**Nature of Common and Rare Variants
**Common genetic variants typically have weak effects on traits or diseases. This is because natural selection filters out highly deleterious mutations over generations; any variant with a strong negative impact on fitness is less likely to be passed down. For example, a variant that drastically increases the risk of schizophrenia would likely diminish in prevalence as it affects social functioning and, consequently, reproductive success.

**Exception to the Rule
**Some common variants have strong effects, such as the APOE ÃƒÅ½Ã‚Âµ4 allele, associated with a significantly increased risk of AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s disease. Despite its strong effect, APOE ÃƒÅ½Ã‚Âµ4 remains common (around 5-10% in certain populations). This could be due to **genetic drift** or **historical selection** that did not account for longer lifespans, where AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s typically manifests. Environmental shifts, like the prevalence of high-calorie diets in modern societies, can also amplify effects of certain alleles, as seen in variants that correlate with obesity post-World War II in industrialized nations. These shifts illustrate how environmental context can alter the impact of genetic variants over time.

**Evolutionary Dynamics and Disease Association
**The interaction between genetic variation and environment can change how variants are selected for or against. For instance, the sickle cell mutation confers a survival advantage against malaria in heterozygous carriers, leading to its higher prevalence in malaria-endemic regions despite its association with sickle cell disease when homozygous. This demonstrates how alleles beneficial in one environment may become detrimental in another, illustrating the complex relationship between **selection, environmental pressures, and genetic variation**.

**Implications Beyond Disease
**This concept extends to non-disease traits. A variant affecting an outwardly visible trait (phenotype) without impacting fitness might persist or even become prevalent if it influences **sexual selection**. For example, a culturally favored traitÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âlike a particular hair colorÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âcould rise in frequency within certain populations due to mating preferences, illustrating that visible phenotypic consequences can impact allele frequencies independent of survival advantage.

**Limitations of GWAS for Rare Variants
**While GWAS effectively identifies common variants with weak effects, it struggles with rare, strong-effect variants due to limited sample sizes in initial studies and the bias of microarrays toward common alleles. Whole-genome sequencing can detect rare variants, but the sheer number of rare alleles introduces noise, making it challenging to discern causal associations. Identifying rare variants with strong effects requires large cohorts to achieve sufficient power and to address the high rate of false positives from **multiple hypothesis testing**.

In summary, the study of genetic variation reflects a balance between selective pressures, environmental changes, and population dynamics, highlighting the nuanced complexity of both common and rare variants in human health and traits.

## [59:06](https://www.youtube.com/watch?v=RlKu1eDbtUQ&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=15&t=3546s) Family studies (Linkage Analysis) vs. Unrelated Individuals (GWAS)

**Linkage Analysis for Rare Variants in Families
**Linkage analysis, or traditional genetics, focuses on rare, strong-effect variants by studying families with a high incidence of a disease, such as cystic fibrosis. This approach uses the **shared inheritance patterns** among affected family members to narrow down the genomic regions likely containing causal variants. By examining siblings who are affected and those who are not, researchers can progressively eliminate regions of the genome that are not associated with the disease. The more affected individuals within the family, the more precisely linkage analysis can pinpoint potential regions. By aggregating data from multiple families with similar genetic conditions, researchers can identify the exact genes involved, which may harbor the rare, disease-causing mutations.

**GWAS for Common Variants in Unrelated Individuals
**GWAS, on the other hand, is well-suited for identifying common variants that increase disease risk across unrelated individuals. By examining a large population and correcting for multiple hypothesis testing, GWAS identifies **statistically significant associations** between specific genetic variants and disease prevalence. This approach, however, is typically limited to common variants due to the large sample size required to detect associations with rare variants. For common variants, a study with around 400 cases might achieve genome-wide significance for a three-fold increase in risk.

**Challenges in Detecting Protective Variants
**Protective variants, which decrease disease risk, present a unique challenge. Identifying families or large cohorts that lack a specific disease is much more complex because these protective traits may not be as readily identifiable. Consequently, studies on protective variants often require **significantly larger sample sizes** (e.g., 30,000 families) to reach statistical power, as itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s harder to assemble enough cases where the absence of the disease can be confidently linked to specific genetic traits.

**Isolated Populations and Specific Disease Frequency
**One strategy for both linkage analysis and GWAS is to study isolated populations where certain diseases are either more or less prevalent. By examining genetic variants within these populations, researchers can identify alleles that either increase or decrease disease risk. This approach benefits from **population-specific allelic distributions** and can reveal insights into both risk-increasing and protective variants.

In summary, linkage analysis excels in identifying rare, high-impact variants within families, while GWAS is optimal for mapping common variants in diverse populations.

## [1:04:05](https://www.youtube.com/watch?v=RlKu1eDbtUQ&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=15&t=3845s) Population Differences, Ancestry Painting, PCA, Multi-Ethnic Fine-Mapping

**Population-Specific Genetic Variants
**The variation in genetic diversity among populations affects how many variants we capture when sequencing genomes. For example, populations with historical isolation, such as Finland, exhibit fewer genetic variants per genome compared to more genetically diverse populations, such as the Yoruba in Africa. The degree of variation also differs within populations, influenced by historical migration patterns, genetic drift, and environmental adaptation.

**Tracing Population History and Genetic Bottlenecks
**By examining genetic variants and calculating coalescence timesÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âpoints at which ancestral genetic lines convergeÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âresearchers can estimate effective population sizes at various historical points. Many human populations experienced genetic bottlenecks in the distant past, followed by expansions. These bottlenecks and expansions are recorded in genetic data, revealing population history embedded within our genomes.

**Ancestry Painting and Principal Components Analysis (PCA)
**To understand the ancestral origins of genome segments, we use ancestry painting, which colors different parts of the genome based on inferred ancestral components. By performing PCA on genetic data, researchers can separate genome diversity into principal components that correlate with geographic and ancestral backgrounds. For instance, principal components often reveal continental and regional differences, with distinct genetic clusters corresponding to geographic locations, effectively mapping populations based on genetic similarity.

**Mapping Individual Genomes
**Ancestry painting allows us to decompose an individual's genome into segments linked to specific ancestral backgrounds, such as subsaharan African, European, or Native American heritage. This process visualizes recombination events over generations, showing the origins of specific genome segments. The ancestral contributions reveal complex histories of population mixing and migration.

**PCA and Geographic Correlation
**Within Europe, for example, PCA can place individuals from different countries along axes that correspond to geographical directions. Principal component one often correlates with north-south variation, while principal component two aligns with east-west differences. This distribution suggests that human migration is relatively slow, resulting in geographically localized genetic variation.

**Multi-Ethnic Fine-Mapping
**To refine disease associations identified in genome-wide studies, researchers use fine-mapping, which becomes particularly powerful when incorporating multiple ethnic groups. By comparing associations across populations, such as Africa and Europe, researchers can identify overlapping genomic regions more likely to contain causal variants. Multi-ethnic mapping thus improves accuracy in pinpointing disease-related variants by leveraging differences in linkage patterns across diverse populations.

**Functional Fine-Mapping and Bayesian Methods
**In addition to purely genetic data, functional annotationsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âsuch as conservation levels or regulatory roles of genomic regionsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âaid in fine-mapping efforts. Bayesian models combine genetic association data with functional annotations to assign posterior probabilities, narrowing down candidate regions or even identifying single, likely causal variants for diseases.

## [1:12:41](https://www.youtube.com/watch?v=RlKu1eDbtUQ&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=15&t=4361s) Polygenic Scores (PGS) and Polygenic Risk Scores (PRS)

**Overview of Polygenic Risk Prediction
**Polygenic risk scores, once viewed skeptically, have now gained significant traction in clinical settings. With advancements in data and statistical approaches, **PRS enables prediction of disease risk by aggregating the effects of multiple common genetic variants across the genome**. As of 2022, organizations like the American Heart Association advocate for using genetic profiling to assess individual risk, particularly in conditions like cardiovascular disease, suggesting its applicability in clinical decisions.

**Individual vs. Population-Level Predictive Power
**Historically, rare variants with strong effects were the focus of genetic predictions for individuals, given their significant but infrequent impacts on conditions like monogenic diseases. **PRS shifts focus to common, weak-effect variants**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âindividually, they contribute minimally to disease risk, but collectively, they can be powerful predictors. For a population, the cumulative effect of these weak variants can surpass that of rare variants, making PRS highly valuable in assessing the genetic risk across diverse individuals.

**Calculating Polygenic Risk Scores
**Each variant in the genome has an associated **effect size, or beta coefficient**, which quantifies its impact on disease risk. To calculate an individualÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s PRS, the beta coefficients of their risk-increasing and protective variants are summed across the genome. This **summed value represents the polygenic score** for the individual, positioning them within a distribution of risk across the population. Individuals with higher PRS values fall into higher risk categories, while those with lower scores are at reduced risk.

**Polygenic Scores in Cardiovascular Risk Prediction
**When PRS is combined with traditional risk factorsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âsuch as high cholesterol, hypertension, and lifestyle choicesÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthe combined model enhances prediction accuracy. Notably, **PRS alone can outperform any single conventional risk factor** and, when added to these factors, improves the precision of risk estimates for conditions like atrial fibrillation and heart disease. Consequently, PRS is now considered a valuable addition to clinical risk assessments.

**PRS and Family History
**PRS also complements family history, an established but limited predictor. For instance, individuals with a **negative family history but a high polygenic risk score** may still have a substantial disease risk, potentially greater than those with a positive family history but a low PRS. This interaction highlights how PRS captures **genetic variation at the individual level** that family history alone may miss.

**Implications for Lifetime Risk and Clinical Use
**PRS can help estimate lifetime disease risk, adjusting for age and other individual factors. As data accumulates, PRS is expected to inform **personalized prevention and intervention strategies** across medical practice, moving genetic risk prediction from academic to practical applications in healthcare.

## [1:18:53](https://www.youtube.com/watch?v=RlKu1eDbtUQ&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=15&t=4733s) Mechanistic Insights from Genome-Wide Functional Enrichments

**Leveraging Functional Genomic Annotations to Decode Mechanisms
**When identifying disease-associated loci, the primary challenge is determining how these genetic regions contribute to disease. For example, the **FTO locus**, one of the strongest genetic associations with obesity, contains multiple variants across a large span, any of which might be causal. By integrating **RNA expression data, epigenomic profiles, and computational models**, researchers can dissect which variants are most likely to disrupt regulatory motifs, affect enhancer activity, or influence specific gene expression patterns in relevant tissues.

**Building a Functional Circuitry Map
**The power of combining genome-wide data with regulatory insights allows for detailed mapping from variant to effect. Instead of a broad association with a genetic region, one can pinpoint specific **variants overlapping enhancers** and other functional elements. This approach includes **annotating enhancers by cell type**, identifying which variants disrupt binding sites for regulatory proteins, and linking these enhancers to their target genes. By leveraging this enriched functional data, researchers can build a **mechanistic map**, identifying how specific variants in the FTO locus influence gene expression and ultimately phenotype.

**Trait-Specific Enrichment Patterns Across Tissues
**Genome-wide functional enrichments reveal that **genetic variants associated with specific traits often map to enhancers active in related tissues**. For example, genetic variants linked to height are enriched in enhancers active in embryonic stem cells, while immune-related traits are enriched in enhancers active in T-cells and B-cells. This tissue-specific enrichment extends across various traits, illustrating a robust relationship between trait-associated variants and tissue-specific enhancer activity. This functional insight is particularly crucial as the majority of disease-associated variants reside in **non-coding regions**, where they exert regulatory rather than protein-coding effects.

**Surprising Associations and Implications for Disease Mechanisms
**Notably, this approach has led to unexpected findings, such as the association of AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s disease variants with **immune-related enhancers** rather than brain-specific regions. This finding, initially identified through combined genetic and epigenomic analysis, suggests an **immune component to AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s disease**, which has since been validated by further studies on microglial cells.

By **linking genome-wide association data with functional annotations**, researchers can derive mechanistic insights that not only clarify how specific variants contribute to disease but also provide new directions for potential therapeutic interventions. This integration of genetic, epigenomic, and computational data offers a transformative approach to understanding complex diseases at the mechanistic level.

## [1:25:18](https://www.youtube.com/watch?v=RlKu1eDbtUQ&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=15&t=5118s) Summary

In this lecture, we covered a comprehensive framework for understanding **human genetic variation** and its implications for disease mechanisms. We discussed how **ancestry and population differences** influence both common and rare variants and explored the distinctions between different ancestries, as well as methods like **fine mapping** that help pinpoint genetic influences on disease. Additionally, we introduced **polygenic risk scores (PRS)**, illustrating their predictive capabilities for assessing disease susceptibility across populations.

We also examined **genome-wide functional enrichments**, which allow us to connect genetic associations with specific tissues and pathways, shedding light on **global disease mechanisms**. This approach is foundational in understanding how various traits are linked to specific tissue functions and biological processes, particularly in non-coding regions.

Looking forward, we will delve deeper into **disease-specific circuitry**, tracing the path from genetic variants to affected cell types, target genes, specific nucleotides, regulators, and ultimately to the **phenotypic outcomes at both cellular and organismal levels**. This progression will further enrich our understanding of genetic architecture and its applications in personalized medicine and therapeutic development.


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
You should be able to explain how genetic variation, GWAS, SNP arrays, haplotypes, Manhattan plots, population structure, linkage analysis, PRS, fine-mapping, FTO, and omnigenic traits connects a biological problem to a computational representation, model, or algorithm.

### Q2. What should you be able to explain from this lecture?
You should be able to explain how genetic variation, GWAS, SNP arrays, haplotypes, Manhattan plots, population structure, linkage analysis, PRS, fine-mapping, FTO, and omnigenic traits connects a biological problem to a computational representation, model, or algorithm.

### Q3. What should you be able to explain from this lecture?
You should be able to explain how genetic variation, GWAS, SNP arrays, haplotypes, Manhattan plots, population structure, linkage analysis, PRS, fine-mapping, FTO, and omnigenic traits connects a biological problem to a computational representation, model, or algorithm.

### Q4. What should you be able to explain from this lecture?
You should be able to explain how genetic variation, GWAS, SNP arrays, haplotypes, Manhattan plots, population structure, linkage analysis, PRS, fine-mapping, FTO, and omnigenic traits connects a biological problem to a computational representation, model, or algorithm.

### Q5. What should you be able to explain from this lecture?
You should be able to explain how genetic variation, GWAS, SNP arrays, haplotypes, Manhattan plots, population structure, linkage analysis, PRS, fine-mapping, FTO, and omnigenic traits connects a biological problem to a computational representation, model, or algorithm.

### Q6. What should you be able to explain from this lecture?
You should be able to explain how genetic variation, GWAS, SNP arrays, haplotypes, Manhattan plots, population structure, linkage analysis, PRS, fine-mapping, FTO, and omnigenic traits connects a biological problem to a computational representation, model, or algorithm.

### Q7. What should you be able to explain from this lecture?
You should be able to explain how genetic variation, GWAS, SNP arrays, haplotypes, Manhattan plots, population structure, linkage analysis, PRS, fine-mapping, FTO, and omnigenic traits connects a biological problem to a computational representation, model, or algorithm.

### Q8. What should you be able to explain from this lecture?
You should be able to explain how genetic variation, GWAS, SNP arrays, haplotypes, Manhattan plots, population structure, linkage analysis, PRS, fine-mapping, FTO, and omnigenic traits connects a biological problem to a computational representation, model, or algorithm.

### Q9. What should you be able to explain from this lecture?
You should be able to explain how genetic variation, GWAS, SNP arrays, haplotypes, Manhattan plots, population structure, linkage analysis, PRS, fine-mapping, FTO, and omnigenic traits connects a biological problem to a computational representation, model, or algorithm.

### Q10. What should you be able to explain from this lecture?
You should be able to explain how genetic variation, GWAS, SNP arrays, haplotypes, Manhattan plots, population structure, linkage analysis, PRS, fine-mapping, FTO, and omnigenic traits connects a biological problem to a computational representation, model, or algorithm.

## Key Takeaways
- genetic variation, GWAS, SNP arrays, haplotypes, Manhattan plots, population structure, linkage analysis, PRS, fine-mapping, FTO, and omnigenic traits is part of the MLCB modeling arc.
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

- [[gwas]]
- [[snp]]
- [[polygenic-risk-score]]
- [[linkage-disequilibrium]]
- [[eqtl]]
- [[mendelian-randomization]]
- [[manhattan-plot]]

### Cluster Membership

- [[cluster-map-genetics-disease]]

### Key Relationships (from KG)

See [[lecture-entity-map]] for the full relationship list, and [[knowledge-graph-index]] for the global entity index.
