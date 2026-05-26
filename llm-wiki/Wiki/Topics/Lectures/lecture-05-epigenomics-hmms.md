---
tags:
  - "topic"
topics:
  - "MLCB"
status: updated
created: 2026-05-24
updated: 2026-05-24
sources:
  - "Raw/Sources/lecture_05_epigenomics_hmms.md"
source_count: 1
aliases:
  - "Lecture 5 - Epigenomics and HMMs"
---

# Lecture 5 - Epigenomics and HMMs

## Source
- Raw source: `Raw/Sources/lecture_05_epigenomics_hmms.md`
- Supporting source: `Raw/Files/lecture_05_epigenomics_hmms.md`
- Existing related pages: [[mlcb-2024-computational-biology]], [[mlcb-complete-study-guide]], [[mlcb-methods-map]]
- Last updated: 2026-05-24

## Executive Summary
Lecture 5 - Epigenomics and HMMs develops chromatin, DNA methylation, histone marks, ChIP-seq, DNase-seq, hidden chromatin states, Viterbi, and posterior decoding. This page intentionally preserves substantial source detail so a future LLM can reason from the wiki without immediately reopening the raw transcript.

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
- Logistics
- Lecture Overview
- Introduction to Epigenomics
- Three types of Epigenomic Modifications
- Q1: Non-standard modifications
- Q2: Epigenetic inheritance
- Q3: Developmental memory establishment
- Diversity of Histone modifications
- Methylation (Bisulfite) and DNase Profiling
- Antibodies, ChIP-Seq, data generation projects, raw data

## Detailed Lecture Notes
The notes below preserve the processed source order and are intentionally detailed.

# Lecture 5 - Epigenomics - HMMs

Video: [Lecture 5 - Epigenomics, HMMs - MLCB24](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=917s)

Slides: [Lecture05_Epigenomics_HMMs.pdf](https://www.dropbox.com/scl/fi/o29r2ehf2wq9qfxmdej6j/Lecture05_Epigenomics_HMMs.pdf?rlkey=nc72i4jaf4no11nanmayn9xuk&dl=0)

## [0:00](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5&t=0s) Logistics

**Introduction to Epigenomics and Hidden Markov Models.** Welcome, everyone. Today, we're going to focus on **epigenomics** and use it as a gateway to introduce **Hidden Markov Models (HMMs)**, a type of **sequential learning model** that we touched on briefly last time. Here's the **progression of topics** we've covered so far: **Gene expression analysis:** We explored how to understand **gene expression patterns**, which is crucial in many areas of study. We used this to introduce **clustering**, **classification**, and **Gaussian mixture models**. Then, we delved into **single-cell analysis**, understanding single-cell data in a foundational way.

The problem set (P-set) you're working on tackles **epigenomics**, **single-cell analysis**, and **gene expression analysis**. This P-set is a hands-on way to apply what we've learned so far. The goal of the problem set is to **teach and reinforce** your learning, not to make it unnecessarily hard. Some steps may seem complex, but weÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢re here to walk through them together. There were questions about scheduling office hours around the holiday. To accommodate, weÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll hold **office hours** and likely record them for those who cannot attend live. LetÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s poll for availability: Who's available today? (Raising hands for different times of day). Alternatively, we could schedule the office hours on **Monday**. (Show of hands for availability on Monday). It seems like Monday is the preferred day. WeÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll finalize this with a **doodle poll** and confirm whether the office hours will be at **3 PM, 4 PM**, or **5 PM** on Monday. As you work on the problem set over the weekend, donÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t hesitate to ask for **help** from **ChatGPT**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Ânot for the answers, but to better understand the **code** and **concepts**. The goal is for you to gain clarity and confidence in the material. Next week, weÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll transition into **Regulatory Genomics** and **Regulatory Networks**, but today, letÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s dive deep into **epigenomics**.

## [4:00](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5&t=240s) Lecture Overview

Today, we will be exploring the fascinating world of **epigenomics**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthe study of how **diverse cell types** can emerge from the same underlying genome. Here's an outline of what weÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll cover:

1.  **Epigenomics Overview**: We will begin with a broad look at what **epigenomics** is and its role in cellular diversity.
2.  **Chromatin Modifications**: WeÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll discuss the specific **chromatin modifications** that play a critical role in regulating gene expression.
3.  **Technologies in Epigenomics**: A look at the **experimental technologies** used to study epigenomics, setting the foundation for how we obtain and process data.
4.  **Primary Data Processing**: After collecting experimental data, how do we process it? We'll talk about **signal processing** and introduce the **Burrows-Wheeler Transform (BWT)**, an efficient approach for **read mapping** in epigenomic data. I'll also share an interesting connection: I recently met **Langmead**, the original author of the BWT algorithm, who visited MIT.
5.  **Peak Calling**: Once we map the data, how do we find significant regions or peaks in epigenomic marks? This is crucial for interpreting the data.
6.  **Combining Multiple Epigenomic Marks**: It's not enough to study just one mark in isolation. We'll discuss how to combine multiple **epigenomic marks** to characterize **chromatin states**, revealing patterns of regulation in the genome.
7.  **Hidden Markov Models (HMMs)**: We will introduce **Hidden Markov Models**, starting with the basics, and then extend this to a **multivariate HMM** for epigenomic data.
8.  **Model Complexity**: A key challenge in using HMMs is deciding the **model complexity**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âhow many parameters and states are sufficient to describe the system. We'll address how to make these decisions.
9.  **Learning Chromatin States Jointly**: We'll explore how to **learn chromatin states** not only across multiple epigenomic marks but also across **multiple cell types**, giving us a holistic view of chromatin dynamics.

Ready to dive in? Let's begin with **epigenomics** and explore how we go from a single genome to the **extraordinary cellular diversity** found in different cell types.

## [5:34](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5&t=334s) Introduction to Epigenomics

The **diversity of cell types** in our body is remarkable. In the brain alone, we find a vast range of cell types within the **neocortex**, and even more diversity in the **subcortical regions**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âwith both **excitatory** and **inhibitory neuron subtypes**. Similarly, the **immune system** displays a vast variety of **blood cells**, not just the red blood cells but an extensive range of **white blood cells** with specialized roles in immune function. A small section of **skin** contains **hair follicles**, **innervations**, **sensory organs**, **epithelial cells**, and **veins**, all working together, yet originating from the same genetic material.

Despite the **same underlying genome** in all these cells, their **phenotypes** exhibit extraordinary diversity. This diversity is made possible by the fact that cells use **different subsets** of the genome, regulated by **epigenomics**.

The genome in each of our cells is packed extremely **compactly**. If you were to take the DNA from a single cell, it would measure **2 meters long** when stretched end-to-end. Given that our body consists of **trillions of cells**, the total length of DNA would stretch from Earth to **Jupiter**, and back, multiple times.

This incredible amount of DNA is compacted within each cell by **structural mechanisms**, primarily involving **nucleosomes**. Each nucleosome contains around **200 nucleotides** of DNA wrapped around **histone proteins**. These histones are decorated with **chemical modifications** that signal to the cell whether a region of DNA is **active**, **repressed**, **poised**, or **transcribed**.

Every nucleosome consists of **eight histone proteins**, which, in addition to compacting DNA, play a **functional role** by encoding **epigenomic memory**. This memory allows cells to maintain their identity throughout cell divisions, ensuring that neurons donÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t suddenly start functioning like **immune cells**.

Thus, the **DNA packaging** is not just structural but also **functional**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âenabling the cell to access the DNA it needs for its specific role. During development and through cell divisions, **epigenomic factors** help maintain the specific **chromatin state** needed for each cell type. Additionally, DNA **accessibility** and **chromatin state** are critical, as **DNA interactions** across different segments also contribute to gene regulation.

In summary, **epigenomics** is the mechanism that enables the vast cellular diversity from a single genome, controlling which parts of the DNA are accessible or functional in each cell type.

## [9:57](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5&t=597s) Three types of Epigenomic Modifications

**Three Types of Epigenomic Modifications**

The structural **compaction** of DNA has functional implications. The more **compact** a region of DNA is, the harder it is to access. For example, highly compacted regions in neurons might not be useful for neuron function but could be important for heart, liver, or lung cells. This **compaction** plays a critical role in controlling which genes are available for a cell type to use.

The second aspect is **DNA accessibility**, which goes beyond general compaction. It involves the **local positioning** of nucleosomes. Even in less compact regions, nucleosomes can shift or roll back and forth to open specific segments of DNA, allowing **regulatory factors** to bind to the exposed sequences. This local accessibility determines whether a regulatory protein can engage with that particular part of the DNA.

The third key modification is **DNA methylation**. This occurs directly on the DNA sequence, specifically at **cytosine bases** (C in the ACGT code). A **methyl group** can be added to cytosine, creating a **methyl-C**. This alteration can influence whether a **transcription factor** (TF) can bind to the DNA. Transcription factors donÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t read the DNA by pulling it apart; instead, they interact with it from the side, feeling the atoms along the major groove of the DNA. If a **methyl group** is present, it can block the transcription factor from recognizing the cytosine, preventing it from binding. Conversely, methylation might **enable binding** for some regulators that specifically recognize **methylated cytosines**. Thus, **DNA methylation** acts as a mechanism for changing how transcription factors interact with the DNA, modifying gene expression.

In addition to **DNA methylation** and **accessibility**, there are also **histone modifications**. Each **nucleosome** consists of eight **histone proteins**, with the most common version being made up of two copies each of **H2A, H2B, H3, and H4**. These histones can undergo various modifications, including the replacement of regular histones with **histone variants** (e.g., **H2A Z**). Beyond this, **post-translational modifications** can occur on the **tails** of the histone proteins. These tails serve as a **landing pad** for regulatory proteins that read the signals embedded in these modifications.

These **histone tail modifications** help determine whether a region of DNA will be interpreted as an **enhancer**, **promoter**, **transcribed region**, or **repressed region**. For example, **methylation** on histones can indicate a repressed region, while **acetylation** loosens the chromatin, increasing accessibility and transcriptional activity. Some histone modifications have **informational effects**, while others have **biophysical impacts** that alter the physical **compactness** of the chromatin.

In summary, there are three main types of epigenomic modifications:

1.  **Compaction and accessibility** of the chromatin, which affects whether certain regions are available for transcription.
2.  **DNA methylation**, which alters how transcription factors bind to DNA.
3.  **Histone modifications**, which involve chemical changes to the histone tails that regulate chromatin structure and gene expression.

These modifications provide a multilayered system for controlling the accessibility and interpretation of the genome, ensuring that the right genes are turned on or off in each specific cell type.

## [15:03](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5&t=903s) Q1: Non-standard modifications

**Q1: Non-Standard Modifications**

There was a question about lab-generated epigenomic modifications, specifically **oxidation** and **carbonation**. While I had mainly discussed **DNA methylation** and **acetylation** as common modifications, there are indeed many others, including **ubiquitination**, **sumoylation**, and some lab-generated or synthetic ones like **oxidation** and **carbonation**. These lab-generated modifications can be used experimentally to **mark specific regions** of the genome. However, once these modifications are added, they must be maintained, especially after **DNA replication**, because many of these modifications will be lost during the replication process.

This maintenance requires regulatory mechanisms that establish, read, and reapply these marks after each replication cycle. The nature of the **double helix structure** enables **semi-conservative replication**, where one strand of the DNA can serve as a template for the other. While the **DNA sequence** can easily be copied in this manner, the challenge lies in **maintaining the epigenomic modifications**. These marks need to be reestablished after replication by specialized regulatory proteins.

For instance, **histone marks** are part of the chromatin that wraps around DNA. During replication, these histone proteins might fall off or be partially retained, and the appropriate **histone modifications** need to be **reestablished** after the replication process. This process is similar during **RNA transcription**, where the **chromatin** must be opened up to allow the transcription machinery to access the DNA. Some epigenomic marks are **transcription-associated** or **co-transcriptional**, meaning they travel with the transcription machinery and are modified along the way.

Therefore, we need to consider both the **informational aspect** of the genome and the **biophysical aspects** when thinking about how epigenetic regulation is maintained during these processes.

## [17:20](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5&t=1040s) Q2: Epigenetic inheritance

**Q2: Epigenetic Inheritance**

Many people often think of **epigenetics** as something that carries through generations, similar to genetic mutations, and thus associate it with **inheritance**. This has led to the term **"epimutation"**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âreferring to changes in gene expression or function that occur without altering the underlying DNA sequence. For instance, when an organism is exposed to extreme cold, radiation, or other environmental factors, there might not be changes to the DNA itself, but there could be changes in the **epigenome**. The natural question that arises from this is: are these epigenomic modifications **inherited** by future generations?

The answer, nearly all of the time, is **no**. Humans and other organisms actively **wipe out epigenomic states** between generations. When **sperm** and **egg cells** are formed, their epigenomic landscape is reset, making them very sperm-like and egg-like. For example, if I experience epigenomic modifications in my **brain cells**, it's not clear how these would be reflected in the sperm cells I produce.

When a **zygote** (the fertilized egg) forms, there's an additional **epigenomic wiping out** to ensure that the developing organism starts with a clean slate. This reset allows the zygote to rely on **primary sequence signals** encoded in the DNA itself, rather than epigenetic modifications. The egg, in particular, plays a crucial role here, as it is packed with **proteins and signals** that help establish the foundational epigenetic state of the zygote.

This resetting process happens **multiple times** during development. So, even if I acquire some epigenomic change due to an experienceÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âsay, watching a violent movieÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthat modification would have to make its way into my sperm, survive the fertilization process, persist through the developmental stages of the zygote, and then manifest in the relevant cells (e.g., brain cells) of my child. As you can imagine, this is an incredibly complicated and unlikely process.

However, while this seems nearly impossible based on what we know, there are theoretical ways in which **epigenetic inheritance** might still occur. One possibility involves **small RNAs** associated with **epigenomic regulation**. These small RNAs could theoretically travel throughout the body, enter the germ line (the cells that give rise to sperm or eggs), and pass on to the next generation. They might even make their way through the **mature egg** and play a role in the developing embryo, continuing to influence the epigenome. While this is **possible**, it remains **extremely difficult** and rare.

The overall takeaway is that, while epigenetic modifications do occur, their inheritance across generations is generally wiped out, though rare mechanisms like **small RNA-based inheritance** may provide a potential pathway in certain cases.

## [20:29](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5&t=1229s) Q3: Developmental memory establishment

Epigenetic memory during development is established by **regulatory elements** that were present in the previous cell type. The process begins with the **zygote**, which initially has only one cell typeÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âbecause it is a single cell. As the first **cell division** occurs, one of these daughter cells will become **anterior**, while the other will become **posterior**. This distinction between cells can happen in different ways depending on the species.

In some species, this **marking** happens **randomly**, while in others it is influenced by the **position** of the cells inside the mother's body, inside the egg, or within the replication environment. Additionally, some species establish **gradients** of gene expression for various regulatory signals. These gradients help define the body plan by marking different regions of the developing organism.

For instance, an **anteroposterior gradient** is established, followed by two additional gradients that run in different directions. Specific regulatory regions, or **response elements**, react to different combinations of these gradients. For example, some regulatory regions might require **two-thirds** of one gradient and **one-third** of another, while others might need different proportions, such as **three-fifths** and **two-fifths**. These varying combinations result in distinct **bands of gene expression** and help to further **differentiate cell types**.

In **Drosophila** (fruit flies), these bands of gene expression are often referred to as **stripes**, and in **C. elegans**, each replication is highly programmed. The identity of each cell is precisely tracked, for example, a cell labeled **13A** will divide into **27B** and **27D**, and the fate of each subsequent cell is determined down to specific replication patterns. This highly detailed **cellular differentiation** process has evolved over time in numerous organisms to ensure the correct formation of various cell types.

This process of **breaking symmetry**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âwhere cells that were once identical start to adopt distinct fatesÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âis one of the most **elegant** and **miraculous** aspects of biology. ItÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s incredibly complex, and as I mentioned, itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s a feat that would challenge any engineer to replicate. Imagine creating a **self-replicating robot** that, using just three billion letters of code, not only builds itself but also makes real-time decisions about how to differentiate its parts. This intricacy is likely a reason it took so long to evolve from **unicellular** to **multicellular** organisms, as the rules governing **self-reprogramming** and differentiation needed to be perfected over billions of years of **evolution**.

Who else finds these processes amazing? The beauty and complexity of how life develops and diversifies truly demonstrates the extraordinary ingenuity of evolution.

## [23:25](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5&t=1405s) Diversity of Histone modifications

Histone modifications play a dual role, contributing both **biophysically** and through **read/write mechanisms**. Histone tails can undergo a wide range of modifications, which makes histone modifications one of the **most complex and versatile** mechanisms of epigenetic regulation.

When we talk about histone modifications, we refer to specific **amino acids** in the histone tails that get modified. For example, you might encounter terms like **H3K4 methylation**. Here's how to break it down:

- **H3** refers to the **H3 histone protein**. Histones are classified into **H2A**, **H2B**, **H3**, and **H4**.
- **K4** refers to **lysine** at position 4 on the H3 histone tail.
- **Me3** refers to the addition of **three methyl groups** (trimethylation) to the lysine.

So, **H3K4me3** means that the **lysine at position 4** on the **H3 histone** has been **trimethylated**. These shorthand notations will recur frequently, and it's important to understand how they denote specific modifications.

Histone modifications do not act in isolation. For example, **H3K4me3** might mean one thing when it's present alone, but its functional impact can change significantly when it's found in combination with other modifications. Histones can be modified through processes like **methylation**, **phosphorylation**, **acetylation**, and others, creating a vast array of regulatory possibilities.

In addition to histone modifications, there are other factors like **DNA methylation**, **nucleosome positioning**, and **DNA accessibility** that also regulate gene expression. This interplay between different epigenetic mechanisms can be thought of as a **territorial struggle** on the DNA. **Regulatory factors** fight for access to DNA by pushing aside nucleosomes. Some regulators, known as **pioneer transcription factors**, are strong enough to **displace nucleosomes** and gain access, while others will only bind if the nucleosomes are already displaced.

This balance of access involves both **biophysical forces** and the **read/write system**, where proteins can recognize specific histone modifications and alter the chromatin landscape. These modifications can result in **loosening** or **tightening** of the chromatin structure, preparing it for processes like **RNA polymerase binding** to initiate transcription.

Histone modifications also correlate with specific regions of the genome:

- **Enhancers** are associated with marks like **H3K27ac** and **H3K4me1**.
- **Promoters** are linked to **H3K4me3** and **H3K9ac**.
- **Transcribed regions** have multiple modifications, such as **H3K36me3**, **H3K79me2**, and **H4K20me1**.

**Repression marks** are classified into three types:

1.  **H3K27me3**: Indicates facultative repression (repression that can be reversed in different cell types).
2.  **H3K9me3**: Associated with **stable heterochromatin** repression, forming regions that are highly compact and difficult to reactivate.
3.  **DNA methylation**: Often marks **repressive regions** in regulatory sequences. Interestingly, in transcribed regions, DNA methylation can correlate with **more expression**, potentially acting as a marker for preventing reinitiation of transcription.

**Untranslated regions (UTRs)** are also important to consider. A **5' UTR** exists between the **start of transcription** and the **start of translation** (the **ATG** codon), while a **3' UTR** lies between the **stop codon** and the **end of transcription**. These regions are critical for stabilizing the mRNA transcript, with processes like **capping** and **polyadenylation** helping to ensure transcript stability.

## [29:00](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5&t=1740s) Methylation (Bisulfite) and DNase Profiling

In the realm of **epigenomic modifications**, numerous techniques are still **emerging**, and to achieve a systematic mapping of the epigenome, researchers employ methods like **chromatin immunoprecipitation (ChIP)**, **bisulfite sequencing**, and **DNase accessibility profiling**.

LetÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s break down **bisulfite sequencing** first. The process involves treating DNA with **bisulfite**, a chemical that selectively converts **unmethylated cytosines** into **uracil** (which will be read as thymine during sequencing), while leaving **methylated cytosines** unchanged. After sequencing the treated DNA, researchers compare it with untreated DNA sequences. If the **cytosine** remains unaltered, it indicates **methylation** at that position. This method is widely used for **detecting DNA methylation** patterns across the genome.

Next, **DNase sequencing** involves the use of an enzyme called **DNase I**, which digests DNA at **open chromatin regions**, where DNA is more accessible because nucleosomes or other binding proteins are absent. By selectively cleaving in these accessible regions, researchers can identify **DNA segments** that are not densely packed with **histones** or other regulatory proteins. Interestingly, within these accessible regions, there can be **protected sites** where **regulatory factors** bind to the DNA, preventing the enzyme from cutting those specific regions. This creates a clear pattern where the **accessible chromatin regions** flank the **binding sites** of these regulatory factors, revealing the **regulatory landscape** of the genome.

Lastly, **chromatin immunoprecipitation (ChIP)** is a technique used to identify **protein-DNA interactions**. It involves using an **antibody** that specifically binds to a target **histone modification** or **protein**. After the antibody pulls down the chromatin (the DNA-protein complex), the associated DNA fragments are sequenced. These **sequences** reveal the locations in the genome where the particular modification or protein of interest is present, allowing us to map various epigenomic marks across the genome.

Numerous large-scale projects, like the **Epigenomics Roadmap**, **ENCODE**, and **Blueprint**, are working to map these epigenomic features across various tissues and cell types. These efforts involve identifying a wide range of **histone modifications**, **open chromatin regions**, **DNA methylation sites**, and **gene expression profiles** in multiple tissues. The key takeaway here is that while we may only have **one human genome**, there are many distinct **epigenomes** that differ across various **cell types**, **tissues**, **developmental stages**, and even between **individuals**. For example, the **epigenome** in your **brain** will differ from that in your **lungs**, and even within your brain, different types of neurons will have distinct epigenomic landscapes. Understanding these differences is essential for **decoding the complexity** of human biology.

This broad and systematic mapping of **epigenetic landscapes** helps researchers understand the **dynamic regulation** of genes, providing insights into how **different environments**, **conditions**, and **stages of development** influence our genome.

## [32:31](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5&t=1951s) Antibodies, ChIP-Seq, data generation projects, raw data

One of the most widely used methods for studying epigenomics is **chromatin immunoprecipitation (ChIP-Seq)**. This technique relies on **antibodies** that are designed to specifically recognize **histone modifications** or **DNA-bound proteins**. Here's how it works: scientists first create an antibody by injecting an animal, such as a rabbit, with a specific **histone modification** like **H3K4me3**. The animal's immune system responds by generating antibodies against the introduced modification. These antibodies are then collected and used in the ChIP-Seq process.

The process begins by **chopping up the DNA** and isolating the fragments bound by the antibodies. These fragments are then sequenced to determine which regions of the genome are associated with specific histone modifications or bound by transcription factors. For example, if an antibody is specific to **H3K4me3**, it will pull down all DNA regions where this modification is present. After sequencing, these regions are mapped to the genome to identify the locations enriched with the histone mark.

Through this approach, researchers can identify regions of the genome that are marked by different histone modifications, transcription factor binding, or chromatin states. For example, **H3K4me1** is a mark of **enhancers**, while **H3K4me3** is associated with **promoters**. This mapping helps researchers construct a detailed view of gene regulation, chromatin structure, and transcriptional activity across the genome.

These technologies are employed in large-scale projects like the **Epigenomics Roadmap** and **ENCODE**, which aim to map histone modifications, open chromatin, DNA methylation, and gene expression across various tissues and cell types. Unlike the human genome, which is relatively stable across individuals, the **epigenome** varies significantly between tissues and stages of development. For example, the **brain epigenome** is distinct from the **lung epigenome**, and even within a single organ, such as the brain, different types of neurons have unique epigenomic profiles.

In addition to mapping histone modifications, researchers can also study **DNA accessibility** and **chromatin states**. Some marks indicate active regulatory regions, while others signify repressed chromatin. Understanding how these marks interact provides insights into gene regulation, cellular function, and differentiation.

The ultimate goal of these efforts is to uncover the **language of the epigenome** by identifying **enhancers**, **promoters**, **transcribed regions**, and **repressed regions**. While promoters are often **active and ready** for transcription, enhancers tend to be more **tissue- and cell-type-specific**, activating genes only under certain conditions. A gene might have multiple **enhancers** but typically only one or a few **promoters**.

Understanding these complex layers of regulation requires sophisticated computational tools and algorithms to analyze the large volumes of **sequencing data** generated from these experiments. These tools help researchers decode the **combinations of marks** that define different **chromatin states** and provide insights into the dynamic regulation of the genome across different **cell types**, **conditions**, and **developmental stages**.

## [38:02](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5&t=2282s) Read mapping: Hashing, Suffix Trees, Burrows-Wheeler Transform

The challenge of mapping millions of short sequencing reads back to the genome is immense. Imagine sequencing **100 million reads** across multiple experiments and needing to map them efficiently to a **3 billion base pair** human genome. Traditional dynamic programming techniques, which we discussed earlier in the course, can handle sequence alignment but are too slow when applied at this scale. So, how do we map these vast numbers of reads efficiently?

**Dynamic Programming** is great, but its quadratic time complexity can be too slow for large-scale genomic data. In this context, we need something faster. One solution is **hashing**, where instead of doing full alignments, we create a **hash table** for small segments of the genome, known as **k-mers** (short subsequences), and rapidly match reads to these pre-computed hashes. This allows us to avoid recalculating the alignment for every read, but it can still be memory-intensive, as it requires building and maintaining large hash tables.

An even more advanced solution, which is both **memory efficient** and **fast**, is the **Burrows-Wheeler Transform (BWT)**. The **BWT** was implemented in a highly efficient mapping tool called **Bowtie**, which significantly accelerated the read mapping process. In fact, Bowtie, developed by **Ben Langmead**, became a cornerstone in genomics for mapping sequencing reads to the genome in a fraction of the time compared to older methods.

### How the Burrows-Wheeler Transform Works:

1.  **Traditional Approaches:** Traditional methods like hashing involve chopping the genome into **k-mers**, creating hash tables, and matching reads to these k-mers. While this method is fast, it consumes a lot of memory due to the large number of possible subsequences in a genome.
2.  **Enter Burrows-Wheeler Transform (BWT):** The **Burrows-Wheeler Transform** uses a clever sorting strategy. To understand how BWT works, consider taking all **rotations** of a string (like "banana"), and sorting them alphabetically. The BWT is then the last column of this sorted list. The interesting property of this transformation is that it clusters repeated characters together, allowing for efficient compression and searching.
3.  **Efficient String Searching with BWT:** BWT is especially useful for **string matching**. It allows us to progressively narrow down the search space by matching one character at a time. For example, if we are searching for the string **"CAG"**, we can first identify all locations where **"C"** occurs, then refine this to locations where **"CA"** occurs, and finally pinpoint where **"CAG"** occurs. This method of searching significantly reduces the need to store massive lookup tables.
4.  **Handling Large Genomic Data:** The **BWT** is able to compress and sort the genome in such a way that allows for very fast lookup of subsequences, such as sequencing reads. Instead of maintaining a massive hash table, BWT keeps only **sorted fragments of the genome** and a few pointers, dramatically reducing memory usage while retaining the ability to quickly map reads.
5.  **Mapping Millions of Reads:** Once the genome is pre-processed using **BWT**, you can map millions of reads very efficiently. This pre-processing step is performed once, and afterward, the **BWT** allows for repeated fast mapping of reads to the genome. The time complexity is **linear** with respect to the number of reads, making it vastly more efficient than quadratic or exponential approaches.
6.  **Accommodating Mismatches:** One of the challenges in genome mapping is accounting for sequencing errors or **mismatches**. The **BWT** can handle this by introducing a certain number of allowable mismatches in the search, either by artificially inserting them during the search or by other optimizations that efficiently handle small variations in the sequence.

In summary, the **Burrows-Wheeler Transform** and tools like **Bowtie** revolutionized the way we map reads to genomes. This approach is faster, more memory-efficient, and scales effectively with the massive amounts of data generated by modern sequencing technologies.

The genius of BWT lies in its ability to **compress and sort** genomic data in a way that allows for fast retrieval without the need for massive memory consumption. This has enabled the rapid analysis of millions of reads across many experiments, dramatically advancing fields like genomics and personalized medicine.

## [54:45](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5&t=3285s) Quality Control, Cross-correlation, Peak calling, IDR (similar to FDR)

Once we have mapped our reads to the genome, the next challenge is to interpret the results. We've generated **intensity signals** from mapping 100,000 reads, but how do we now infer biologically relevant information from them? Specifically, we need to determine which regions of the genome are bound by regulators or marked by histone modifications. To do this effectively, we perform a series of **quality control steps** and ultimately identify regions of interest, known as **peaks**, where significant binding or marking events occur.

1.  **Quality Control:** The first step is to ensure that the experimental data is reliable. To assess this, we need to check a number of factors, such as:
    - Are the reads distributed in a way that suggests the experiment was successful?
    - Do the reads match across different marks in a consistent manner?
    - Were there sequencing errors or regions that were not properly mapped?
2.  We also need to run a **control experiment** where we sequence the **DNA by itself** to differentiate between regions that are truly bound by the regulator and regions that are merely **accessible**.
3.  **Handling Redundancy and Fragmentation:** When pulling down DNA fragments bound by a regulator, we often generate redundant reads if the same DNA molecule is sequenced multiple times. To address this, we calculate the **non-redundant fraction** of binding in our library and check if the reads are piling up artificially. Additionally, DNA fragmentation can occur in the experiment, so we need to ensure that we're capturing valid fragments that reflect true binding events rather than experimental artifacts.
4.  **Cross-Correlation Analysis:** One key step is to look at the **distribution of reads** across forward and reverse strands of the DNA. Since the sequencer captures DNA fragments, reads from the **Waton strand** will align to the left of a binding site, and reads from the **Crick strand** will align to the right. By scanning the forward and reverse reads past each other, we can identify a **peak** where they converge, indicating the **fragment length** of the captured DNA.
    This analysis allows us to:
    - Confirm the expected **fragment length**, ensuring it's longer than the read length.
    - Identify artifacts like **re-sequencing** of the same reads, which would show a high degree of redundancy at the read length.
5.  **Peak Calling:** Once we have high-quality data, we move on to **peak calling**, where we identify regions of the genome that exhibit strong binding signals. There are several tools for peak calling, including **MACS** and **PICS**, which use different algorithms to identify significant peaks based on the distribution of reads. These tools rely on models of read distribution and calculate probabilities for identifying real binding events versus noise.
6.  **Combining Replicates:** When we perform the same experiment multiple times, the question arises: how do we combine the results from **replicate experiments**? Several strategies exist:
    - **Intersection:** Only call peaks that appear in both experiments. This is conservative but may miss strong signals if one experiment was noisier.
    - **Union:** Call all peaks detected in either experiment. This may lead to an overabundance of false positives if one replicate was noisy.
    - **Signal Summation:** Sum the signals from both experiments. This can dilute strong signals from one experiment if the other is weaker.
7.  A more sophisticated approach is to sort peaks by **signal strength** in each replicate and determine how well they replicate across experiments. This allows us to determine a **cutoff** where replication falls off, ensuring that we capture the strongest signals from both experiments without introducing noise.
8.  **Irreproducible Discovery Rate (IDR):** IDR is a measure similar to **False Discovery Rate (FDR)**, but it focuses on reproducibility across replicates. By comparing the peaks from multiple experiments, we can determine where the signal starts to diverge between replicates. At this point of divergence, we set the **cutoff** for peak calling. IDR allows us to keep peaks that are **highly reproducible** between replicates, even if one experiment has lower overall signal strength.
    The key idea behind IDR is that as you go down the list of peaks sorted by intensity, the replication rate will start to drop at a certain point. By identifying this drop-off, we can determine which peaks are reliable.

In conclusion, **quality control** ensures that our sequencing data is reliable, **cross-correlation** helps us identify valid fragment lengths, and **peak calling** combined with **IDR** ensures that the peaks we identify are both statistically significant and biologically relevant. This approach allows us to confidently infer regions of the genome that are bound by regulators or marked by histone modifications, leading to deeper insights into gene regulation and chromatin structure.

## [1:05:38](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5&t=3938s) Discovery and characterization of chromatin states

At this stage, we've **carried out our experiments**, mapped our reads, called our peaks, and validated them through replication. The next challenge is to combine the information from **multiple histone modification marks** and uncover biologically relevant patterns across the genome. This leads to the goal of discovering **chromatin states** that represent different functional regions of the genome.

1.  **The Challenge of Multiple Marks:** We have **dozens of histone modification marks** that can occur in various combinations. These combinations are **complex**, **dynamic**, and potentially **diverse in function**. For example, different combinations of marks may correspond to distinct chromatin states, such as enhancers, promoters, or repressed regions. We aim to determine which combinations of marks are biologically meaningful.
2.  **The Goal:** Our ultimate goal is to **learn the language of the epigenome from scratch**. This requires an **unsupervised approach**, where we provide the algorithm with a large dataset, and it identifies patterns in the data without prior assumptions. The algorithm should be able to find **distinct chromatin states**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âsuch as promoters, enhancers, and transcribed regionsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthat represent different functional aspects of the genome.
3.  **Probabilistic Modeling:** To accomplish this, we need a **probabilistic model** that can identify the combinations of marks in a way that reflects biological reality. The model should not only recognize individual marks but also take into account the **relationship between neighboring genomic positions**. This is important because chromatin states are not random; for example, promoter states are more likely to be found near other promoter states, and transcribed states are more likely to be found near other transcribed regions.
4.  **Hidden Chromatin States:** The task is to infer a **hidden chromatin state** at every genomic position. At any given point in the genome, we may be in a promoter state, enhancer state, or transcribed state, each of which will **emit** a specific combination of histone modification marks. The **hidden state** refers to the actual chromatin state that we are trying to infer based on the **observed histone marks**.
5.  **Transition and Emission Matrices:** The approach relies on two key concepts:
    - The **transition matrix** represents the likelihood of moving from one chromatin state to another as we walk along the genome. For instance, promoter states are likely to be near other promoter states, and enhancer states near other enhancer states.
    - The **emission matrix** defines the probability of observing certain histone marks in a given chromatin state. For example, promoter states might emit certain marks like H3K4me3, while enhancer states might emit H3K27ac.
6.  **Hidden Markov Model (HMM):** To model these relationships, we use a **Hidden Markov Model (HMM)**, which allows us to represent the sequence of chromatin states as a probabilistic process. The HMM enables us to infer the **hidden states** (such as enhancers or promoters) from the **observed emissions** (the histone marks). By training the model on the data, we can learn the **transition probabilities** between chromatin states and the **emission probabilities** of histone marks from those states.
    - The **transition probabilities** capture the likelihood that a given chromatin state will transition to another chromatin state.
    - The **emission probabilities** reflect the likelihood that a specific combination of histone marks will be observed in each chromatin state.

Through this approach, we can discover and characterize **chromatin states** across the genome, helping us understand how the epigenome regulates gene expression and cellular function. This method allows us to move beyond individual histone marks and focus on the **higher-order structure** of chromatin, which ultimately governs how the genome functions in different contexts.

## [1:08:02](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5&t=4082s) HMM Foundations, Generating, Parsing, Decoding, Learning

**Hidden Markov Models (HMMs)** are a foundational tool for understanding how **sequential data** is generated, interpreted, and learned. HMMs allow us to model sequences where the underlying states are **hidden**, but they generate observable data.

1.  **Generating Sequences:** HMMs are designed to model processes where the sequence of observed data is **influenced by hidden states**. For instance, in **speech recognition**, an HMM can transcribe words by mapping **utterances** (the observable data) to **hidden linguistic states** (words or phonemes). These utterances come in a sequence, and the interpretation of each sound is influenced by the one that precedes it. Similarly, in genomics, the position along the genome influences the current chromatin state. For example, if the model is in an **intergenic region**, it's more likely to stay in that region, while if it enters a gene, itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s more likely to stay in a transcribed region.
2.  **Temporality in HMMs:** HMMs incorporate the notion of **temporality**, where the sequence of hidden states follows a specific order. In genomics, this temporal structure corresponds to the **position along the genome** from left to right. For example, if the model detects a promoter region, it's likely to stay in a nearby promoter state for several positions. This use of **neighborhood information** constrains the number of possible states at each position, reducing the complexity of the sequence modeling.
3.  **Emitting and Recognizing Sequences:** The main goal of an HMM is to emit observable data based on the hidden states and to recognize these sequences by learning the distinguishing characteristics of each state. For instance, in the genome, HMMs emit **DNA sequences** based on the hidden chromatin stateÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âsuch as promoters, enhancers, or transcribed regionsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âand allow us to recognize these functional regions from the observed marks.
4.  **Observations and Hidden States:** At the beginning of the course, we discussed how thereÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s a distinction between **observations** (the data we see) and **hidden states** (the unobserved, underlying process that generates the data). The observations might seem independent, but they are sampled from a **continuous process** that contains temporal relationships. In HMMs, we combine this framework with **probabilistic models** to make inferences about the hidden states based on the observed data.
5.  **Markov Chain vs. Hidden Markov Model:** In a **Markov Chain**, the sequence of observations directly influences the next state, with no hidden variables. However, in an HMM, the Markov Chain operates on the **hidden states**. These hidden states generate the observable data in a **generative framework**. For instance, in genomics, we transition between hidden states such as **promoters, enhancers, and transcribed regions**. These hidden states then emit the observable **histone marks** or other biological signals.

In summary, **HMMs** are powerful tools for **modeling sequences** with hidden states, allowing us to infer complex patterns in sequential data like speech, text, or genomic sequences. By learning the **transition probabilities** between hidden states and the **emission probabilities** of observable data from these states, we can decode hidden structures within the data.

## [1:11:15](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5&t=4275s) Two Sets of HMM parameters: Emissions, Transitions

In **Hidden Markov Models (HMMs)**, we work with two key sets of parameters: **transition probabilities** and **emission probabilities**. These parameters govern how hidden states evolve over time and how they generate observable data.

1.  **Hidden States and Observations:** In an HMM, we have:
    - A set of **observations** (denoted as **X**), which represent the data we can observe.
    - A sequence of **hidden states** (denoted as **ÃƒÂÃ¢â€šÂ¬**), which are not directly observable but determine the behavior of the observations.
2.  **Transition Probabilities:** The **transition probabilities** define how the model moves from one hidden state to another. Specifically, the probability of transitioning from **state K** to **state L** is determined only by the current state (state K). This means that the HMM is **memoryless**, which is a key property of Markov models. In this context, **memorylessness** means that the transition to the next state depends solely on the current state and not on any prior states.
3.  **Emission Probabilities:** The **emission probabilities** define how the hidden states generate the observable data. For each state, there's a probability distribution over the possible observations. For example, the probability of emitting an observation **XÃƒÂ¡Ã‚ÂµÃ‚Â¢** while being in **state K** is part of the emission probabilities.
4.  **HMM Structure:**
    - We have a **transition matrix**, which encodes the probabilities of moving between hidden states.
    - We have an **emission vector**, which encodes the probabilities of the observed data being generated from each hidden state.
5.  **Bayesian Framework:** HMMs extend the basic **Bayesian framework** by including both transition and emission probabilities. Using these, we can compute the likelihood of a sequence of observations by considering both the likelihood of staying in certain states and the likelihood of generating specific observations from those states.

In summary, an HMM models sequences through two types of probabilities: **transition probabilities** for moving between hidden states and **emission probabilities** for generating observable data from these states. Together, they provide a powerful way to model sequential data with underlying hidden structures.

## [1:12:40](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5&t=4360s) Example 2-state HMM, observations, scoring, inference

In a **2-state Hidden Markov Model (HMM)**, we aim to model sequences of data, such as genomic sequences, by transitioning between different hidden states (e.g., **background** and **promoter**) and generating observable sequences from these states.

1.  **Background vs. Promoter States:**
    - The **background state** is characterized by equal probabilities for nucleotides (**A, C, G, T**), while the **promoter state** might favor **G** or **C** with higher probabilities, such as 40%, and have a lower probability for **A** and **T** (e.g., 10%).
    - The model includes **self-transition probabilities** for both the background and promoter states. For example, the background state might have a 99% chance of remaining in the background, and the promoter state might have a 95% chance of staying in the promoter state.
2.  **Transitioning Between States:**
    - The transition probability from the background to the promoter state could be 1%, while transitioning back from the promoter to the background could be 5%.
    - **Self-transition probabilities** determine how long the model stays in a given state. Since the background has a higher self-transition probability (99%), it is more likely to remain in the background for a longer duration compared to the promoter state.
3.  **Observation Sequence:** Suppose we observe a sequence like **ATAGTC**. To determine if it came from the background state or the promoter state, we calculate the joint probability of the sequence being generated by each state.
    - For the **background state**, we calculate the product of emission probabilities (e.g., 0.25 for each nucleotide in the background) and the self-transition probabilities (e.g., 0.99 for staying in the background at each step).
    - For the **promoter state**, we calculate the product of emission probabilities, such as 0.1 for **A, T** and 0.4 for **G, C**, and the self-transition probabilities (e.g., 0.95).
4.  **Likelihood Comparison:** After calculating the joint probabilities, we can compare the likelihood of the sequence being generated by the background or the promoter state. In this example, the **background state** might be **2.5 times more likely** to generate the sequence because it is **A/T-rich**, which is typical for the background state.
5.  **Transitioning Between States:** We can also consider models where the sequence transitions between the **background** and **promoter** states. For instance, transitioning from background to promoter and back to background might better capture the **G/C-rich** segments of the sequence. However, **transitioning between states** incurs a cost, and excessive transitions make the model less likely.
6.  **Inference:** The challenge with this approach is that there are an **exponential number of possible paths** through the states, making it computationally expensive to evaluate every possible path. Therefore, more efficient algorithms (such as the **Viterbi algorithm**) are needed to find the most likely path without calculating every possible transition.

In summary, this 2-state HMM example illustrates how we model sequences by assigning probabilities to both staying in a state and transitioning between states, while considering the costs of transitions and the likelihood of observing specific nucleotide sequences in each state.

## [1:16:38](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5&t=4598s) Viterbi algorithm: Find best parse ÃƒÂÃ¢â€šÂ¬\*= argmaxÃƒÂÃ¢â€šÂ¬P(x,ÃƒÂÃ¢â€šÂ¬)

The **Viterbi algorithm** is used to find the **most likely sequence of hidden states** (or "parse") that generates the given sequence of observations, using **dynamic programming** to efficiently navigate through the exponentially large space of possible paths.

1.  **Dynamic Programming to Avoid Exponential Complexity:**
    - Instead of evaluating every possible path through the hidden states (which would be exponential in number), we use dynamic programming to align **states** to **positions** in the sequence.
    - The key insight is that we can compute the best score up to a certain position, then reuse this information to compute the best score for the next step. This reduces the computational complexity from exponential to **polynomial**.
2.  **Aligning States to Positions:**
    - For each position in the sequence, we align it to one of the possible hidden states.
    - The alignment of states doesn't happen linearly but rather transitions between states according to the **transition probability matrix**, which governs the likelihood of moving from one state to another.
3.  **Transition and Emission Costs:**
    - As we transition between states, we incur a **transition cost** specific to that transition, rather than a fixed gap penalty as in sequence alignment.
    - Each state also has an **emission probability** for generating the observed character at the given position. The **total score** for a state depends on both the **transition** from the previous state and the **emission** of the observed character.
4.  **Recursive Calculation of Scores:**
    - The algorithm recursively calculates the **best score** for each state at each position in the sequence.
    - For the current state, the score is the product of:
        - The **score** of the best previous state,
        - The **transition probability** to the current state,
        - The **emission probability** for the observed character.
    - This ensures that we find a state with both a **high previous score** and a **low transition penalty**.
5.  **Storing the Best Path:**
    - As we compute the maximum score at each position, we store both the **score** and an **arrow** pointing to the previous state that gave the best score. This allows us to trace back the optimal path once we've processed the entire sequence.
6.  **Backtracking to Recover the Best Path:**
    - Once we reach the end of the sequence, we follow the **stored arrows** backwards to recover the optimal sequence of states (the **best parse**).
    - This backtracking ensures that the entire sequence is optimally aligned to the most likely sequence of states.
7.  **Time and Space Complexity:**
    - The Viterbi algorithm runs in **O(k^2n)** time, where kkk is the number of states and nnn is the length of the sequence. The space complexity is **O(kn)**, since we only need to store the scores for each state at each position and the arrows for backtracking.

In summary, the Viterbi algorithm efficiently finds the most likely path through a Hidden Markov Model by dynamically computing scores, storing intermediate results, and backtracking to reconstruct the optimal state sequence. This method avoids the exponential complexity of brute-force approaches while ensuring a globally optimal solution.

## [1:20:15](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5&t=4815s) Posterior Decoding: Most likely state ÃƒÂÃ¢â€šÂ¬i(over all paths)

1.  **Total Probability Calculation:**
    - Posterior decoding aims to determine the **most likely state** at each position, considering **all possible paths**. Instead of finding a single most likely sequence of states (like in Viterbi decoding), it computes the probability of being in a particular state at each position, summing over all paths that pass through that state.
    - To do this, we need to calculate the **total probability of generating a sequence**, which involves summing the probabilities of **all possible paths** through the sequence.
2.  **Forward-Backward Algorithm:**
    - **Forward pass**: Starting from the left, we calculate the probability of generating the sequence **up to** a particular state. This gives us the likelihood of being in a specific state based on all prior observations.
    - **Backward pass**: Starting from the right, we calculate the probability of generating the sequence **from** a particular state **to the end**. This captures the likelihood of being in a specific state given all future observations.
    - By combining these two passes (forward and backward), we can calculate the probability of being in a particular state at each position.
3.  **Combining Forward and Backward Probabilities:**
    - The **forward probability** represents the likelihood of observing all the states and emissions **up to** the current state.
    - The **backward probability** represents the likelihood of observing all the states and emissions **from** the current state **to the end**.
    - Adding the forward and backward probabilities gives us the **total probability** of being in a specific state at a given position, accounting for both the preceding and following observations.
4.  **Posterior Probability for Each State:**
    - By combining the **forward and backward** probabilities, we calculate the **posterior probability** of being in each state (e.g., enhancer, promoter, transcribed, repressed) at each position in the sequence.
    - This allows us to determine the **most likely state** for each position **independently**, unlike the Viterbi algorithm, which finds the most likely sequence of states as a whole.
5.  **Application in Epigenomics:**
    - In the context of epigenomics, this approach helps infer the probability of a genomic position being in a particular **chromatin state** (e.g., enhancer, promoter) based on the **emitted histone modification marks**.
    - By considering all observations before and after a given position, posterior decoding provides a more **granular view** of the likelihood of each state, rather than committing to a single sequence of states.

In summary, **posterior decoding** calculates the probability of being in each hidden state at every position, considering both past and future observations. This method is especially useful when we want to independently infer the most likely state at each position, rather than finding the single best sequence of states.

## [1:21:48](https://www.youtube.com/watch?v=U6HPrUJex8I&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5&t=4908s) Summary

In today's lecture, we covered key concepts in **epigenomics** and explored various techniques for data processing, sequence mapping, and quality control:

1.  **Epigenomics Foundations**:
    - We began with an overview of **epigenomics** and its role in regulating gene expression and chromatin structure.
2.  **Primary Data Processing**:
    - We discussed methods for processing raw epigenomic data, including the use of the **Burrows-Wheeler Transform (BWT)** for fast read mapping, which helps in aligning sequencing reads to the genome efficiently.
3.  **Quality Control and Peak Calling**:
    - We examined methods for **quality control** of the data and determining where **peaks** (representing binding sites or marks) occur, which indicate areas of interest in the genome.
4.  **Hidden Markov Models (HMMs)**:
    - We introduced the basics of **Hidden Markov Models** for modeling genomic data. HMMs allow us to model sequential data where the **observations** (histone marks, for instance) are generated by **hidden states** (e.g., chromatin states like enhancers or promoters).
    - We covered **sequence generation**, **parsing**, and **decoding** using HMMs, with a focus on the **Viterbi algorithm** for finding the best state path and **posterior decoding** for calculating the probability of each state at each position.
5.  **Next Steps**:
    - While we discussed HMMs in detail, we still need to cover how to **learn the parameters** of an HMM, such as transition and emission probabilities, and how to model more complex **state transitions**. This will be picked up in the next lecture.

In summary, we've laid the groundwork for understanding **epigenomic data processing**, **HMMs**, and key algorithms for sequence decoding. The next lecture will continue from here, expanding on the learning mechanisms and tying this into **regulatory motifs**.

Looking forward to seeing you all for recitation on Monday and for continuing this lecture on Tuesday. Have a great long weekend!


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
You should be able to explain how chromatin, DNA methylation, histone marks, ChIP-seq, DNase-seq, hidden chromatin states, Viterbi, and posterior decoding connects a biological problem to a computational representation, model, or algorithm.

### Q2. What should you be able to explain from this lecture?
You should be able to explain how chromatin, DNA methylation, histone marks, ChIP-seq, DNase-seq, hidden chromatin states, Viterbi, and posterior decoding connects a biological problem to a computational representation, model, or algorithm.

### Q3. What should you be able to explain from this lecture?
You should be able to explain how chromatin, DNA methylation, histone marks, ChIP-seq, DNase-seq, hidden chromatin states, Viterbi, and posterior decoding connects a biological problem to a computational representation, model, or algorithm.

### Q4. What should you be able to explain from this lecture?
You should be able to explain how chromatin, DNA methylation, histone marks, ChIP-seq, DNase-seq, hidden chromatin states, Viterbi, and posterior decoding connects a biological problem to a computational representation, model, or algorithm.

### Q5. What should you be able to explain from this lecture?
You should be able to explain how chromatin, DNA methylation, histone marks, ChIP-seq, DNase-seq, hidden chromatin states, Viterbi, and posterior decoding connects a biological problem to a computational representation, model, or algorithm.

### Q6. What should you be able to explain from this lecture?
You should be able to explain how chromatin, DNA methylation, histone marks, ChIP-seq, DNase-seq, hidden chromatin states, Viterbi, and posterior decoding connects a biological problem to a computational representation, model, or algorithm.

### Q7. What should you be able to explain from this lecture?
You should be able to explain how chromatin, DNA methylation, histone marks, ChIP-seq, DNase-seq, hidden chromatin states, Viterbi, and posterior decoding connects a biological problem to a computational representation, model, or algorithm.

### Q8. What should you be able to explain from this lecture?
You should be able to explain how chromatin, DNA methylation, histone marks, ChIP-seq, DNase-seq, hidden chromatin states, Viterbi, and posterior decoding connects a biological problem to a computational representation, model, or algorithm.

### Q9. What should you be able to explain from this lecture?
You should be able to explain how chromatin, DNA methylation, histone marks, ChIP-seq, DNase-seq, hidden chromatin states, Viterbi, and posterior decoding connects a biological problem to a computational representation, model, or algorithm.

### Q10. What should you be able to explain from this lecture?
You should be able to explain how chromatin, DNA methylation, histone marks, ChIP-seq, DNase-seq, hidden chromatin states, Viterbi, and posterior decoding connects a biological problem to a computational representation, model, or algorithm.

## Key Takeaways
- chromatin, DNA methylation, histone marks, ChIP-seq, DNase-seq, hidden chromatin states, Viterbi, and posterior decoding is part of the MLCB modeling arc.
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

- [[hidden-markov-model]]
- [[viterbi-algorithm]]
- [[baum-welch]]
- [[expectation-maximization]]
- [[chromatin]]
- [[chip-seq]]
- [[atac-seq]]
- [[histone-modification]]
- [[chromhmm]]
- [[dna-methylation]]

### Cluster Membership

- [[cluster-map-epigenomics]]
- [[cluster-map-classical-ml]]

### Key Relationships (from KG)

See [[lecture-entity-map]] for the full relationship list, and [[knowledge-graph-index]] for the global entity index.
