---
tags:
  - "topic"
topics:
  - "MLCB"
status: updated
created: 2026-05-24
updated: 2026-05-24
sources:
  - "Raw/Sources/lecture_03_single_cell_analysis.md"
source_count: 1
aliases:
  - "Lecture 3 - Single-Cell Analysis"
---

# Lecture 3 - Single-Cell Analysis

## Source
- Raw source: `Raw/Sources/lecture_03_single_cell_analysis.md`
- Supporting source: `Raw/Files/lecture_03_single_cell_analysis.md`
- Existing related pages: [[mlcb-2024-computational-biology]], [[mlcb-complete-study-guide]], [[mlcb-methods-map]]
- Last updated: 2026-05-24

## Executive Summary
Lecture 3 - Single-Cell Analysis develops single-cell RNA-seq, spatial transcriptomics, quality control, pseudobulk analysis, SVD, gene modules, disease states, and trajectory inference. This page intentionally preserves substantial source detail so a future LLM can reason from the wiki without immediately reopening the raw transcript.

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
- Intro
- Bulk vs. Single-Cell
- Why Single Cells
- scRNA-seq Technologies
- scRNA-seq Biological Questions
- 84k cells from 48 individuals
- Cleaning up Data
- Clustering and Cell Annotation
- DEGs Gene Expression Changes with Phenotypes
- Multi-Region Analysis

## Detailed Lecture Notes
The notes below preserve the processed source order and are intentionally detailed.

[[# Lecture 3 - Single-cell Analysis]]

Video: [Lecture 03 - Single Cell Analysis - MLCB24](https://www.youtube.com/watch?v=xmLoR3ynwkw)

Slides: [Lecture03_SingleCellGenomics.pdf](https://www.dropbox.com/scl/fi/ipzapq4fxcb8g85mn5thr/Lecture03_SingleCellGenomics.pdf?rlkey=ophx8nig9v718ib5mlylx75ny&dl=0)

## [0:00](https://www.youtube.com/watch?v=xmLoR3ynwkw&t=0s) Intro

**Intro:** Alrighty, welcome everyone! Today, we're going to be talking about **single-cell genomics**. On Tuesday, we talked about **gene expression analysis**, and I mentioned that there are a lot of complications with single-cell genomics, which we would cover in lecture 13. Well, guess what? We're going to talk about them today because your problem set includes the entire pipeline of single-cell analysis, including **differential analysis, pathway enrichment, and some single-cell epigenomics**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âall blended into an awesome **Jupyter notebook**.

Why are we doing this? As you start thinking about your final projects, we want you to have all the tools at your disposal. A lot of people have talked about including single-cell genomics in their projects, so we want to enable and empower all of you to carry out these single-cell analyses, which are at the forefront of where biology is right now. A lot of mysteries about how genes work and how disease impacts the body are very difficult to uncover when you're looking at **bulk analysis**. However, the moment you're able to separate the different cell types in the body, things become much more amenable to these types of analyses.

So, let's dive right in. We're going to start with **why single cells** are important. We will review traditional approaches and the emergence of single-cell **RNA sequencing** across different types of technologies, because understanding the technological underpinnings can help you understand issues with **noise** and when the technology doesnÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t work exactly right. Then, we're going to dive into the **biology**: what are the questions you can ask about single cells? WeÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll focus on a lot of the work our lab is doing on understanding the brain in the context of **Alzheimer's, schizophrenia**, and so on.

Then, weÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll step back and look at the **basic computational tasks** associated with single-cell analysis. WeÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll explore some frontiers of the field, including **deep learning and representation learning methods** for understanding single cells. Finally, weÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll touch briefly on areas beyond **transcriptomics**, including some of the **epigenomics, multiomics**, and so forth. Excited? Yes? Awesome! Great, letÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s do it!

**Why Single Cell:** Again, there are many ways to think about gene expression analysis. The easiest analogy often used in talks, lectures, and newspaper articles is the **smoothie versus individual fruits** or the **fruit salad**. When you're doing bulk transcriptomics, youÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢re essentially blending everything together like a smoothie.

## [4:48](https://www.youtube.com/watch?v=xmLoR3ynwkw&t=288s) Bulk vs. Single-Cell

**Bulk vs. Single-Cell:** Remember in the first lecture, or TuesdayÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s lecture, I was basically saying, "Oh, you look at brain expression versus liver expression." It sounds reasonable, right? Like if I tell my parents, "Oh yeah, we looked at brain expression relative to liver expression," it makes complete sense to them. But to a scientist, especially someone working on the liver or brain, they're like, "Liver? Okay, which of the 47 cell types in the liver?" And someone working on the brain would ask, "Which of the 143 subtypes of excitatory neurons in the brain?"

So, when you think about liver expression, what youÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢re actually doing is taking this extraordinary diversity of cell types and blending them together into a **smoothie**. You're looking at the liver smoothie, or the brain smoothie, or the lung smoothie. But this analogy is not great; in reality, what youÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢re after are the **individual fruits**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthe distinct cell typesÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âand how they behave separately.

Today, weÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll especially look at this in the context of **self-projected phenotypes**, a measure and method weÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ve been developing in my group with Gerald Bond and others. Even within a single cell type, there are **continuums of variation** that are very often biologically driven. So, even at the level of sorting the beautiful kiwis, there isnÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t just one type of kiwiÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂthereÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s a gradient, and that gradient is associated with different biological properties, sometimes even different disease properties.

When our group started looking at single-cell biology, it became very difficult to go back to bulk analysis. We've gone all out, profiling more single cells than we could have imagined. For example, weÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ve profiled over **20 million cells** from our group alone, which sounds unfathomable. If someone had told you, "IÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢m going to give you 20 million cells," it would have seemed impossible not long ago. Remember when I showed you the gene expression by condition? It was thousands of genes across hundreds of conditions. Now, weÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢re not just talking about hundreds of conditions or thousandsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂweÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢re talking about millions and tens of millions of conditions, which are the cells.

This is important because in every tissue in your bodyÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âwhether it's the brain, lung, liver, or any otherÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂthereÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s an extraordinary diversity of interplaying cell types. ThatÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s concept number one. Concept number two is that often, when we talk about single-cell analysis, weÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢re dealing with neurons in the brain that can extend all the way down to our toes. So, how do you do single-cell profiling? You would have to pull out the entire neuron, take all the RNA from all the different axons and dendrites, unweave it, and then profile it.

This is very challenging, especially in the brain, where cell typesÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âlike **oligodendrocytes, astrocytes,** and **excitatory or inhibitory neurons**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âare intricately interwoven. So, sequencing the entire RNA content of a single cell is hard. As a result, an approximation we often use is **single-nucleus sequencing** because the RNA in the cytoplasm is produced in the nucleus before it gets transported to the rest of the cell. You can think of it as an approximation of whatÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s being produced right now rather than the actual RNA molecules that are being translated into proteins in the cytoplasm.

Moreover, as we push for more resolution, we might not just want to know the total content of RNA inside a neuron; we might want to know how much RNA is sitting in one part of the axon versus another, or in specific dendrites. The **transport of RNA** along the cell body to different parts is extraordinarily important, and thatÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s a technological frontier on its own.

There are some purists who argue, ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œOh, single-nucleus sequencing makes no sense,ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â while others say, ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRNA expression makes no sense; everything happens at the protein level.ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Others still argue that, ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œProteins donÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t make sense; everything happens at the post-translational modifications of the protein level,ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â and so on. My answer to all of these purists is that we have to start somewhere. We start where the data is, with the technologies that are accessible today. By using current methods, we drive innovation and push the frontiers of technology further.

To give a historical perspective: in 1995, we could have waited another decade for sequencing costs to drop before starting the **Human Genome Project**, but without doing it with the available technology, we wouldnÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t have driven the innovation needed to reduce costs, improve technology, and create the market demand that propelled the field forward. So, even though single-nucleus RNA sequencing is an approximation, itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s incredibly useful, and we should be aware that better techniques will come as technology evolves. Until then, we will keep pushing the boundaries of whatÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s possible with the current tools.

In summary, even though we know itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s an approximation, single-nucleus RNA sequencing provides extraordinary insights. The analogy here is the **smoothie, the individual fruits**, and then the third analogyÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthe **tart**, which represents **spatial transcriptomics**. Spatial transcriptomics doesnÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t just look at cells isolated from their context but examines where each cell is positioned within the tissue. This spatial context is crucial because cells located in different parts of the tissue, such as near blood vessels, may behave differently from those elsewhere.

Single-cell technologies are incredibly powerful but also limited because they donÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t always tell you exactly where each cell is positioned. Spatial transcriptomics, which weÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll touch on later, addresses this by linking the cellsÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ transcriptomes to their physical location, revealing spatially distinct patterns that contribute to our understanding of tissue function and disease.

## [12:08](https://www.youtube.com/watch?v=xmLoR3ynwkw&t=728s) Why Single Cells

**Why Single Cells:** Let's talk a little more about why studying individual cells is so important. As IÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ve been emphasizing, itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s crucial to study single cell types separately, like analyzing a kiwi distinct from a banana. But itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s also essential to study multiple kiwis separately and multiple bananas separately because even within a single cell type, there is a remarkable diversity.

When you look at cells in the body or in a dish, they can look very different from each other. Under the microscope, they display different **morphologies** and have different expression levels of individual proteins. Even cells of the same type can exhibit dramatic differences from one another. For example, in **blood differentiation**, you have an extraordinary diversity and nearly a **continuum of cellular identity** as you go from **hematopoietic stem cells**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthe progenitors of all blood lineagesÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthrough the various stages of differentiation. These hematopoietic lineages give rise to a wide array of cell types, each with distinct functions, and even within those cell types, there is further diversity.

One of the main reasons for this variability is **stochasticity**. Each cell has an expression program, but which subset of genes gets activated at any given moment can differ. Even though all the necessary genes are there, the order and timing of their activation can vary. Some of this variability is due to **stochastic processes**, like how specific regulators move through the nucleus, interact with various genomic regions, and influence which genes are expressed.

There's also stochasticity in how cells respond to **intracellular signals**. For instance, receptors on a cell might receive different amounts of a given signal, leading to variations in cellular state transitions even among otherwise similar cells. These transitions can create significant diversity between individual cells.

Developmentally, each cell follows a program that starts with a single genome and evolves through a series of divisions influenced by factors like **maternal deposition of gradients** and the cellÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s position within the embryo. For example, cells positioned ventrally versus dorsally, or anteriorly versus posteriorly, are subject to different signals and decisions at each cell division. These choices are ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œrememberedÃƒÂ¢Ã¢â€šÂ¬Ã‚Â by the **epigenome**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âa layer of regulation weÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll discuss in more detail next weekÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âand this epigenetic memory influences how cells respond to subsequent signals.

Early methods for studying individual cells involved dissociating tissue, isolating cells, placing each one into a separate well, amplifying the RNA from each well, and sequencing it. This initial approach to **single-cell profiling** allowed us to sequence about 600 cells at a time, which was extraordinary back then. It enabled us to see dramatic differences between cells, distinguish cell types, and observe their varied responses and activation stages, such as how cells react to stimulation after one hour, two hours, four hours, or six hours.

This traditional approach has evolved into more automated methods. Now, we can use technologies like **cell sorting** apparatuses that shoot individual cells through sorting devices and place them into wells. Even more advanced are **microfluidic technologies** that encapsulate each cell in a dropletÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âa tiny reaction chamber about the size of one cell. Inside each droplet, a bead loaded with millions of **barcodes** tags the RNA molecules from that cell, allowing us to identify which RNA originated from which droplet and therefore from which cell.

However, challenges arise when isolating cells or nuclei. Ambient contamination can affect the quality of the RNA, especially in compromised samples like those from cancer patients or individuals with neurodegeneration. For example, neurons in neurodegenerative conditions might have damaged nuclei, making them more susceptible to contamination during sequencing.

Regarding **spliced versus unspliced RNA**, since we're often working with nuclear RNA, we capture both forms. This can provide insights into the **dynamics of gene expression**. By analyzing the proportion of spliced versus unspliced transcripts, we can infer cellular trajectories, such as differentiation paths from one state to another. If you see that a gene is still unspliced in one cell but fully spliced in another, you can map these observations onto a differentiation lineage, identifying cells transitioning between developmental states.

Single-cell analysis also highlights the pitfalls of bulk analysis. In bulk, you average gene expression across many cells, which can obscure significant variability. For example, if some rare cells express high levels of a particular RNA, bulk analysis might suggest moderate expression across all cells, misleadingly implying that all cells express that RNA when, in reality, most cells have none, and a few have a lot.

This variabilityÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âwhether due to stochastic processes, environmental influences, or intrinsic differences between cellsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âis mostly biological, not just technical noise. Single-cell sequencing reveals these subtleties, helping us appreciate the rich complexity of cellular behavior that is otherwise hidden in bulk measurements. Understanding this variability is crucial for exploring the diverse responses of cells and the underlying mechanisms driving health and disease.

## [24:37](https://www.youtube.com/watch?v=xmLoR3ynwkw&t=1477s) scRNA-seq Technologies

**scRNA-seq Technologies:** Early single-cell RNA sequencing (scRNA-seq) studies started with just a few cellsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âsometimes 10 or 100 cells. In less than a decade, weÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ve progressed to capturing millions of cells, which is mind-blowing. So, what are the key technologies that enabled this dramatic innovation?

LetÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s start with the basics of isolating single cells. In the earliest methods, you could simply pipette individual cells by eye and place them into 96-well plates, treating each well as if it were a sample from a different tissue or individual. Another method involved using **capillary pipettes under a microscope** to capture cells more precisely.

A more advanced technique is **fluorescence-activated cell sorting (FACS)**, where a laser detects the presence of specific cell surface markers or other proteins on the cells. As each cell travels through a tube, you can decide whether to keep it or remove it by applying a current or magnetic field. This approach allows you to isolate specific cell types of interest, such as activated T cells, which can be identified by their markers of activation.

You can also use **laser capture microdissection**, where you look at a tissue and precisely cut out a tiny part with a laser. However, one of the most widely used methods today is **microfluidics**, which involves cells in suspension flowing through a microfluidic tube while beads loaded with barcodes capture each cellÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s RNA. These barcodes are sequences of nucleotides, and every bead has millions of barcodes that are identical. For example, one cellÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s RNA might be tagged with the barcode sequence "AGGTTCGA," while another cellÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s RNA might get "TGACCAGG."

These microfluidic systems leverage the physical properties of materials, where the lysis buffer and oil do not mix, forming tiny reaction chambersÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âessentially bubblesÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthat encapsulate each cell. The bead inside the bubble tags every RNA molecule from the cell with the same barcode, allowing researchers to determine which RNAs came from the same droplet and, therefore, the same cell.

The general methodology across these technologies involves first isolating the cells, then amplifying the RNA, and ultimately counting or measuring the RNA molecules. There are different approaches, such as **full-length sequencing**, which provides the splicing patterns for each RNA, or **digital gene expression analysis**, which focuses on sequencing only the tail end of each RNA molecule.

Why sequence the tail end? The sequencing process starts with a primer that initiates the polymerase reaction. For many eukaryotic genes, this primer can simply be "TTTT," because eukaryotic mRNA transcripts often end with a **poly-A tail** composed of "AAAA." The primer binds to this tail, allowing sequencing to start from the end of the molecule. This method captures the number of times a gene is expressed without providing detailed splicing information.

There are many different technologies for scRNA-seq, each varying in the number of cells captured, sensitivity, cost, and cell capture methods. For example, traditional methods of isolating each cell in a well can cost about $3 to $6 per cell, which sounds cheap until you start working with millions of cells. On the other hand, microfluidic-based methods can bring the cost down to as little as five cents per cell.

Microfluidic systems work by encapsulating each cell in a droplet, where a bead with a specific barcode tags every RNA molecule. After lysis, all the mRNA from a cell gets the same barcode, allowing you to pool all the droplets together and sequence the entire mixture in one bulk reaction. This tagging process makes it possible to trace back each RNA to its original cell, even though the final sequencing is performed on a combined sample.

ThereÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s also another technology that uses multiple rounds of barcoding. Imagine you start with a million cells and split them into 100 wells, each well getting a unique barcode. You then blend the cells and split them again, adding a second unique barcode, and repeat the process a third time. By the end, each RNA molecule from each cell has three distinct barcodes, representing the different wells it passed through.

This combination of barcodes allows you to trace RNA molecules back to their original cells with a high level of precision. The probability that two cells would end up with the same three-barcode combination is extremely lowÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âeffectively one in a millionÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âmaking this a robust method for distinguishing RNA from different cells, even when sequenced together.

These technological innovations have transformed single-cell analysis, allowing us to capture the extraordinary diversity of cellular behaviors and states at unprecedented resolution. The microfluidic and multi-round barcoding methods are particularly impactful because they enable high-throughput and cost-effective scRNA-seq, pushing the boundaries of whatÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s possible in biological research.

## [36:16](https://www.youtube.com/watch?v=xmLoR3ynwkw&t=2176s) scRNA-seq Biological Questions

**scRNA-seq Biological Questions:** Is everybody with me on technologies? Great. LetÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s now talk about **biology**. There are three parts to this lecture: the **technological part**, the **biological part**, and the **computational part**. WeÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ve covered the technological part; letÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s dive into the biological aspect. What do we actually do when we have tons of single-cell data? This is a lot of the research happening in my lab, and itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s exciting because I get to teach about things that didnÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t exist just a year or two ago. So, what do we do?

The goal of our lab is to understand the **circuitry underlying disease**. We aim to explore how **genetic differences** or **environmental factors** lead to **molecular changes** that then manifest as disease states. These molecular differences can occur at the **RNA level** or at the **epigenome level**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthe latter of which we will discuss next week.

We profile massive numbers of both **healthy and diseased samples** using single-cell profiling. We then perform the analyses that I will show you to identify **driver genes, regulatory regions, regulators, cell types, pathways, and processes**. The key aim is to infer **causality** from this analysis because **genetics** inherently gives us a causal link. Genetic variants can lead to observable differences in a direct, causal manner, unlike environmental exposures, which occur after genetic differences are already present.

You inherit genetic differences from your parents, so it's far more plausible that the genetic differences are driving the phenotypic changes rather than the other way around. However, genetic differences could also indirectly lead to behaviors, like eating unhealthily, which then contributes to disease, demonstrating the complex interplay of genetics and environment.

We try to infer these **causal paths** by understanding how genetic variants act at the molecular level, allowing us to pinpoint where to **intervene** in the disease process. Now, IÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll share some of the lessons we've learned from applying these methods to a variety of disease samples. WeÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ve established numerous collaborations, applied for dozens of grants, and weÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢re studying a wide range of traits at single-cell resolution.

This work requires incredible coordination across multiple teams: **doctors** who provide the samples, **patients and their families** who generously contribute samples (often postmortem), **lab technicians** who handle the sorting and profiling, and the **experimental scientists** who push forward the technologies necessary to make all of this possible. Then, there are the **computational analysts** who analyze the data, and the entire team comes together to interpret the results. It truly takes a village to conduct these studies.

We apply this approach across a wide spectrum of conditions, including **AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s disease, frontal temporal dementia, Lewy body dementia, ALS, HuntingtonÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s disease, schizophrenia, bipolar disorder, Down syndrome, autism, depression, PTSD, suicide, and aging**. We profile dozens of cell types across tens of millions of cells, often from multiple regions of the brain and sometimes from other tissues outside the brain. Most of the time, we perform **RNA profiling through single-cell transcriptomics**, which is our main focus today, though we also analyze **DNA accessibility** in some casesÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âa topic weÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll cover more next week.

## [40:49](https://www.youtube.com/watch?v=xmLoR3ynwkw&t=2449s) 84k cells from 48 individuals

**84,000 Cells from 48 Individuals:** In our study on AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s disease, we embarked on a groundbreaking exploration of the postmortem human brain, conducting the first analysis of AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s at single-cell resolution. We collected data from **84,000 cells** across **48 individuals**, a pivotal moment in a long and extraordinary collaboration with Lee Wei, the director of the Picower Institute for Learning and Memory. This work was spearheaded by Hyejung Maddis, who has led the project both experimentally and computationally, and has since established his own lab at the University of Pittsburgh.

This initial study, led by Matheus Jose DavillaÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âwho now has his own lab in ItalyÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âset the stage for a series of papers that have continued to push the boundaries of our understanding of Alzheimer's disease at the cellular level. The core question we aimed to address was: **What do these cells reveal about the disease?** Understanding the roles and states of these cells in the context of AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s required a series of complex computational analyses.

## [41:45](https://www.youtube.com/watch?v=xmLoR3ynwkw&t=2505s) Cleaning up Data

The first critical step in our analysis is to **clean up the data**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âa process that is crucial for ensuring the accuracy and reliability of our findings. But what does it mean to clean up the data? This involves identifying **quality metrics** that allow us to filter out problematic data points. We may need to remove individual cells that do not meet quality standards, discard entire experiments if they were compromised, or exclude specific genes that exhibit abnormal behavior.

Once this data cleaning is completed, what remains is an **expression matrix**, a foundational tool in our analysis. This matrix represents a comprehensive view of gene expression across thousands of cells, where rows correspond to genes and columns correspond to individual cells. This cleaned and structured dataset provides the basis for all subsequent analyses, enabling us to uncover the hidden dynamics of gene activity within the complex landscape of AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s disease.

## [42:22](https://www.youtube.com/watch?v=xmLoR3ynwkw&t=2542s) Clustering and Cell Annotation

**Clustering and Cell Annotation:** After data cleaning, the next crucial step is **clustering the cells**. This involves grouping cells together based on their gene expression profiles to identify distinct cell types. However, defining these clusters can be challenging. For instance, you might label a group as progenitor cells, but within that group, there could be subtle subtypes. Similarly, in the brain, **excitatory neurons** may not form discrete types but instead exist on a gradient across cortical layers 1 to 5, each with distinct but overlapping expression patterns.

The task of clustering is essentially about identifying the **major drivers of variation** in the data, and itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s a form of **unsupervised learning**. Once youÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ve clustered the cells, the next step is to **annotate these clusters**, giving each one a name based on its most characteristic features. For example, cells within a cluster that share a particular expression pattern might be identified as a specific cell type.

Annotation relies on understanding which **genes are most highly expressed** within each cluster. This process is not done in isolation; it builds on decades of research where scientists meticulously studied gene expression in individual cells using microscopes and small-scale methods. The key difference with modern scRNA-seq is the scaleÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âwhile traditional studies might have analyzed 20 or 100 cells, todayÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s technologies allow us to examine millions of cells simultaneously, revealing new insights into cellular diversity that were previously hidden.

## [44:18](https://www.youtube.com/watch?v=xmLoR3ynwkw&t=2658s) DEGs Gene Expression Changes with Phenotypes

With our dataset of 84,000 cells from 48 individuals, one of the first questions we asked was: **How do the expression patterns of these cells correlate with the phenotypes of the individuals?** Each column in our data represents a different person, each with a unique phenotype. Some individuals are categorized as controls or non-Alzheimer's, meaning that, based on pathological analysis, they do not display the classic **signatures of Alzheimer's**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âsuch as neurofibrillary tangles, neuritic plaques, or amyloid-beta deposition. In these individuals, these pathological markers are very low, while they are significantly elevated in others.

Additionally, we analyzed other indicators such as **signatures of parkinsonism** and **cognitive decline**. Among the control group, most individuals maintained high global cognition, except for one who showed signs of parkinsonism. In contrast, those diagnosed with severe AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s exhibited marked cognitive decline and high levels of pathology. Another subset of individuals showed intermediate levels of pathology, categorized as mild cognitive impairment (MCI) or mild Alzheimer's.

The next step was to determine what differentiates these groups. We focused on identifying **differentially expressed genes (DEGs)** between the AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s cases and controls. This allowed us to explore whether the cells from AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s patients exhibited higher expression of certain genes compared to cells from non-AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s individuals.

Conducting these analyses raises important statistical considerations. Imagine you have 20,000 cells from advanced AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s patients and another 20,000 from controls. It seems straightforward to compare the gene expression distributions between these groups. However, this approach mistakenly assumes that each cell is an independent sample. In reality, these cells are not sampled in isolation; they come from 24 individuals in each group. Thus, the sampling process is hierarchical: you first sample individuals, and then you sample cells from within those individuals.

This hierarchical nature affects how we assess DEGs. In bulk data, differential expression is simpler because you have one measurement per group. In single-cell data, however, you end up with thousands of measurements for each individual rather than 20,000 independent measurements.

There are three main approaches to DEG analysis in single-cell data:

**1\. Cell-Centric Approach:** This method treats every cell as an independent sample, which can lead to overconfidence in the results because it underestimates the true variance by not accounting for the hierarchical sampling. You mistakenly think you have more samples than you actually do.

**2\. Pseudobulk Approach:** This method averages gene expression across all cells from each individual, effectively creating one measurement per person. While this approach is statistically sound, it oversimplifies the data, losing critical insights into cellular variability that could be biologically meaningful.

**3\. Hierarchical Mixture Models:** These models recognize the hierarchical sampling process, accounting for the fact that cells are nested within individuals. This approach is statistically powerful but more complex, requiring more time and assumptions about the sampling process. If these assumptions are incorrect, the results can be misleading.

Using these methods, we can identify DEGs and explore biological differences between AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s and control groups. One of our findings was that late-stage AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s shows extensive gene expression changes that are often shared across multiple cell types. In contrast, early-stage AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s reveals more **cell-type-specific alterations**, suggesting distinct molecular mechanisms at different disease stages.

We also examined how **biological sex** influences these expression changes. For example, in non-AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s individuals, there are significant differences in gene expression between male and female excitatory neurons. In AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s cases, these sex differences in expression patterns are even more pronounced, indicating that sex may play a critical role in disease biology.

Similarly, we assessed the impact of **age** on gene expression. Differences in expression could be driven by age rather than disease status alone, especially in a cohort where individuals vary widely in age. Recognizing these factors helps refine our understanding of the underlying biology and emphasizes the importance of considering variables such as sex and age in disease studies.

Ultimately, these analyses are not just about finding the answers but about learning **how to think critically** about the data and the complex biological questions it raises.

## [52:33](https://www.youtube.com/watch?v=xmLoR3ynwkw&t=3153s) Multi-Region Analysis

**Multi-Region Analysis:** scRNA-seq allows us to go beyond single regions of the brain to explore how **AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s disease** and other conditions progress through different areas. AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s progression often follows a stereotypical pattern, starting near the **locus coeruleus** at the base of the brain, then spreading to the **entorhinal cortex**, hippocampus, and eventually reaching broader cortical areas.

We extended our study to multiple regions of the brain to understand these disease dynamics better. We profiled cells from the **entorhinal cortex, hippocampus, thalamus, mammillary body**, and various neocortical regions, such as the **angular gyrus, medial cortex, and prefrontal cortex**. This multi-region approach reveals how different cell types are distributed across the brain and how their expression patterns vary by location.

For example, in some regions, we observe specific **subtypes of excitatory neurons** that are unique to that area, while in others, a broader diversity of neuron types exists. Similarly, different types of **astrocytes** and **oligodendrocytes** show distinct spatial distributions. This spatial variability in cell types and their gene expression is critical for understanding how diseases affect different parts of the brain.

The next step is to **annotate** these additional cell types and determine their distinguishing features or **marker genes**. As we expand the analysis from 84,000 cells to 1.6 million cells, the increased data volume enables us to identify finer distinctions between cell types. Technological advances since our initial study in 2019 have further improved our ability to capture and profile large numbers of cells.

With these detailed annotations, we can begin to explore **cellular trajectories** within each region, painting a picture of how disease-related changes propagate over time and space. For example, some cell types might display a progression of gene expression that corresponds to advancing stages of AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s, providing clues about how the disease spreads from one brain area to another.

## [55:45](https://www.youtube.com/watch?v=xmLoR3ynwkw&t=3345s) Module Analysis

In traditional analysis, we often look at individual genes to assess how their expression changes in response to conditions like AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s disease. This approach involves running **thousands of independent tests**, one for each gene, to determine what changes are occurring. However, the statistical confidence in any one geneÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s change can be limited. But if multiple genes within the same **pathway** show consistent changes, our confidence increases, revealing a coordinated biological response.

Instead of analyzing each gene independently and then retrospectively examining whether these genes belong to the same pathway, a more powerful approach is to directly group genes based on their co-expression patterns. Imagine taking the vast expression matrixÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âwhere rows represent genes and columns represent cellsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âand **decomposing** it into smaller, meaningful components using techniques like **singular value decomposition (SVD)**. This mathematical method allows us to simplify the data, revealing underlying patterns where genes are not acting in isolation but are instead organized into **modules**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âgroups of genes that function together.

These gene modules provide a way to think about the complex interplay within cells, allowing us to interpret high-dimensional data as being driven by lower-dimensional spaces. Each module captures a set of genes that are co-regulated, reflecting shared biological processes. By clustering genes into these modules, we can begin to ask deeper questions: **Which genes are grouped together? What biological roles do these modules represent?**

The development of this modular analysis approach was led by researchers including Benjamin James, who has been instrumental in simplifying complex problem sets for further exploration, and Carlos Bacheschi, now a postdoc at Harvard Medical School. They focused on understanding what these gene modules actually represent. By examining correlations between pairs of genes within the matrix, they could identify **networks** of interconnected genes, offering a visual and functional understanding of how genes interact.

These modules arenÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t just abstract groupings; they can be visualized as **networks** where each geneÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s position reflects its connections to other genes. This network-based view allows us to go beyond the question of whether a gene is simply part of a cluster. It reveals the **strength and nature of each connection**, showing how tightly genes are co-regulated and helping us understand the broader functional landscape of the transcriptome.

With this framework, we can start exploring how these **gene modules change in a coordinated manner** across different cell types and in association with various pathological signatures of AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s disease. This approach enables us to link specific modules to key phenotypesÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âsuch as **cognitive impairment, diffuse plaques, neuritic plaques**, or **neurofibrillary tangles**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âand assess their roles in the progression of disease. By focusing on gene modules rather than isolated genes, we can capture a more integrated view of cellular behavior, bringing us closer to understanding the molecular underpinnings of AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s and other complex conditions.

## [58:50](https://www.youtube.com/watch?v=xmLoR3ynwkw&t=3530s) Q1: Why Modules instead of single-genes

**Question 1: Why Analyze Modules Across Clusters Instead of Individual Genes?
**A fundamental question arises: Why analyze gene modules across clusters of cells rather than focusing on individual genes in single cells? The primary advantage of this approach is **robustness**. When measuring individual genes in individual cells, the sample size is often too small, making the data inherently noisy. For example, if a gene is expressed at only a few molecules per cell, these measurements can vary widely, leading to high levels of uncertainty.

By shifting the focus to **modules of co-expressed genes** rather than single genes, and by examining these modules across clusters of cells, we gain more stable and reliable measurements. When youÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢re not just looking at one RNA molecule but rather at a set of molecules that are correlated and act together, the overall signal becomes stronger and more consistent. This collective approach captures the underlying biological processes more accurately, reducing noise and increasing the statistical power of the analysis.

## [59:30](https://www.youtube.com/watch?v=xmLoR3ynwkw&t=3570s) Q2: Difference from Bulk

**Question 2: Difference from Bulk Analysis
**One of the key limitations of bulk analysis is the loss of **cell-type specificity**. In bulk experiments, all cell types are averaged together, making it impossible to discern how gene expression changes within specific subpopulations, such as particular subclasses of microglia or neurons. For instance, when comparing gene expression between AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s patients and controls in bulk, you might observe an overall decrease in the expression of certain genes. However, this decrease could be misleading, as it often reflects the loss of neuronsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âa hallmark of AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢sÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Ârather than a true downregulation of those genes within the remaining cells.

In AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s, neuron loss skews the data significantly. For example, you might find 4,000 neurons in a control individual but only 2,000 in an AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s patient. This disparity creates an illusion that thousands of neuron-specific genes are decreasing in expression, simply because there are fewer neurons to contribute their gene expression to the average.

Single-cell analysis overcomes this by allowing you to examine gene expression changes **within each specific cell type**. This enables you to accurately measure how gene expression is altered within neurons, microglia, astrocytes, and other cell types separately, without being confounded by changes in cell composition. Even with pseudobulk analysis, where cells are dissociated and grouped into broad categories like excitatory neurons, inhibitory neurons, or astrocytes, you still maintain the ability to observe expression changes within defined cell populations.

This targeted approach reveals the true dynamics of gene expression changes across different cell types, providing a much clearer picture of the underlying biology than bulk analysis ever could. By focusing on each distinct cell type, single-cell analysis not only enhances our understanding of disease mechanisms but also highlights the critical roles of individual cell populations in conditions like AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s.

## [1:01:30](https://www.youtube.com/watch?v=xmLoR3ynwkw&t=3690s) Q3: Robustness and Reproducibility

A common concern when analyzing complex data, especially when moving from individual genes to broader modules, is **robustness and reproducibility**. You may wonder: If I run the analysis again, will the results be exactly the same? Will ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œModule 13ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â appear again, and if so, will it look the same as before? This is a valid question, and one that delves into the heart of scientific reproducibility.

However, itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s important to recognize that **exact reproducibility** is not always the ultimate goal. If the experiment were repeated with a slightly different set of individuals, what matters more is whether the **biological insights** remain consistent across varying conditions, datasets, or cohortsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Ânot just whether the analysis can be replicated on a different computer with the same data. True robustness lies in the ability to reproduce findings across different samples, studies, and even populations.

To test robustness, one approach is to perform **subsampling experiments**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Ârandomly selecting cells from the same individuals or splitting the data into two artificial replicates to see if the results hold. Although these methods provide some insight, they are not true biological replicates because each sample or section of tissue might inherently differ due to subtle regional variations.

In a particularly instructive study, two independent teams conducted parallel analyses on overlapping cohorts. Fiorella JaggerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s group, initially based at the Broad Institute and now at Columbia, profiled approximately 200 individuals, creating two biological replicates for each person. Our group profiled over 430 individuals, including around 200 that overlapped with JaggerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s cohort. This setup allowed us to compare three biological replicatesÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âtwo from their study and one from oursÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âfor the same individuals.

Such direct comparisons offer a rare opportunity to test how well results align across different research teams and methodologies. An ideal project, for example, would be to analyze how these biological replicates relate to each other. Despite minor variations in experimental execution, many of the same **pathways and gene modules** emerged consistently across studies, reinforcing the validity of key findings.

It is also essential to acknowledge that results can change with different software versions or analytical settings. These changes may or may not affect the overall interpretation, but they reflect the evolving nature of computational biology. In this rapidly advancing field, some hypotheses will withstand the test of time, while others may need revision as new data and techniques become available. The iterative nature of science means constantly learning, adjusting, and moving forward.

Waiting for perfect reproducibility or fully mature technology can paralyze progress. If we had delayed sequencing the human genome until every tool was refined, we would still be waiting. Instead, by engaging with emerging technologies and data, we advance the field, continually building on what we learn. As more studies replicate findings independently, confidence grows in the robustness of specific biological insights, while other hypotheses may be revised or discarded.

The dynamic nature of this field, filled with ongoing discoveries and opportunities for further exploration, underscores the importance of engaging with the data at hand, even as methods and knowledge continue to evolve.

## [1:07:05](https://www.youtube.com/watch?v=xmLoR3ynwkw&t=4025s) Linked Regions Correlation

One particularly intriguing analysis we conducted was examining the **correlation of changes** in different cell types across brain regions between individuals. Specifically, we asked: How do these changes in cellular behavior co-vary between connected brain areas? For example, we found that specific neurons in the **subiculum** of the hippocampus were highly correlated with corresponding cell types in the **entorhinal cortex**. This observation extended beyond a single brain region, highlighting coordinated patterns of cellular alteration between regions that are anatomically and functionally linked.

This kind of analysis is exciting because it allows us to identify **co-variances** in cellular changes across different brain regions and across individuals. For instance, we could observe that a specific subclass of neurons in one region was consistently covariant with another subclass in a different region across our cohort of individuals. From decades of neuroscience research, we know that these regions often have direct **projections and connections**, suggesting that they communicate and influence each otherÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s function.

These findings align with the well-documented progression pattern of AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s disease, which often follows a stereotypical pathway from the **locus coeruleus** to the **entorhinal cortex** and then into the **hippocampus** and other cortical areas. One hypothesis is that the pathology progresses due to either **physical damage** or disruptions in neuronal signaling between connected regions. Neurons rely on proper signals from connected regions to maintain their health and function; if these signals are disrupted, it may contribute to correlated patterns of damage.

Understanding these linked patterns provides valuable insights into how AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s and similar neurodegenerative diseases spread through the brainÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s complex networks, highlighting the importance of inter-regional connections in maintaining brain health.

## [1:09:01](https://www.youtube.com/watch?v=xmLoR3ynwkw&t=4141s) Discrepancies between Phenotype and Transcriptome

Another compelling avenue of analysis is exploring discrepancies between an individualÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s **phenotype** and their **transcriptome**, which can reveal unexpected patterns and potential misdiagnoses. In a recent study on schizophrenia, published in _Science_, we examined whether we could predict whether a person had schizophrenia based solely on their expression patterns. Remarkably, the model worked well for many individuals, correctly distinguishing between controls and schizophrenia cases. However, the most intriguing findings were the exceptions.

One control individualÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂletÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s call them Control 7ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âwas consistently misclassified by the model as having schizophrenia based on their gene expression. On further investigation, it was discovered that this person was the father of a son diagnosed with schizophrenia. This raised the possibility that the expression patterns captured something **inherited**, suggesting a latent genetic or environmental predisposition to the disorder, despite the absence of clinical symptoms.

Conversely, some diagnosed schizophrenia cases exhibited expression patterns more typical of controls. This suggests the possibility of **distinct pathways** leading to schizophrenia-like symptoms that may not align with the conventional understanding of the disorder. Such findings highlight the potential for gene expression analysis to uncover hidden **subtypes** or alternative mechanisms of disease that might not be captured by traditional diagnostic methods.

Building on this approach, we now have a dataset of 430 individuals with postmortem single-cell data from AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s patients. A fascinating project would be to investigate those diagnosed as having AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s but whose gene expression profiles appear more typical of healthy individuals. This could help identify **misdiagnoses, overdiagnoses,** or previously unrecognized subclasses of the disease, offering insights that could refine clinical practices.

Another valuable analysis involves exploring the **upstream regulators** of differentially expressed genes, identifying common regulatory elements that might drive pathological changes. Studying the genetic impacts on gene expression is another direction, linking somatic mutations or genetic variants to altered transcriptional patterns. This approach has been applied to various conditions, including psychosis, ALS, frontotemporal dementia, HuntingtonÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s disease, and others, each revealing unique regulatory shifts that could inform therapeutic strategies.

For instance, in a recent study published in _Cell_, we identified significant gene expression changes in different subclasses of microglia and vascular cells. Although vascular cells represent only about 0.3% of our data, they exhibit distinct expression patterns depending on whether they are located in venous or arterial regions of the vasculature, with these patterns further altered in AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s patients.

In another study, published in _Nature Neuroscience_, we explored **single-cell accessibility and epigenomic differences** in AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s, identifying widespread epigenomic erosion in affected individuals. We also analyzed the **mutational burden** by comparing reference DNA with sequenced RNA. These mutations, which could result from somatic changes at the DNA level or from damage occurring after RNA transcription, were significantly higher in dementia patients compared to controls. This mutational burden was particularly pronounced in specific cell subtypes, hinting at cellular vulnerabilities contributing to disease progression.

Interestingly, individuals with higher mutational burdens also displayed greater **epigenome erosion**, where the typically distinct boundaries between active and repressed genomic regions began to blur. This pattern of **global epigenomic flattening** underscores a critical aspect of neurodegenerative disease: the gradual loss of cellular identity and function at the molecular level.

These insights illustrate the power of transcriptomic and epigenomic analyses to uncover layers of complexity in disease that go far beyond what can be observed clinically, opening new pathways for understanding and eventually intervening in these challenging conditions.

## [1:14:20](https://www.youtube.com/watch?v=xmLoR3ynwkw&t=4460s) scRNA-seq Analysis Questions

The diversity of analyses that can be performed at the single-cell level is vast, offering a window into the complexities of cellular behavior that bulk analyses cannot match. The workflow typically begins with **raw data**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âcount matrices that detail the number of reads per gene for each cell. From there, a series of preprocessing steps are essential, including **quality control, data correction, normalization,** and **feature selection**. These steps help refine the data by removing low-quality cells, correcting for technical artifacts, and focusing on the most informative genes, often the highly variable ones.

Once the data is preprocessed, the cells can be **visualized** in a lower-dimensional space using methods like **t-SNE** or **UMAP**, which allow for the identification of distinct cell populations based on gene expression patterns. This visualization helps reveal the structure of the data, highlighting clusters that often correspond to specific cell types or states. These clusters can then be **annotated** using known marker genes to assign biological identities to each group.

**Clustering** cells based on their expression profiles is a fundamental step, as it organizes the data into meaningful units that can be further analyzed. This organization allows researchers to explore specific cell types within complex tissues and understand how they interact with each other.

Another powerful analysis is **trajectory inference**, which helps map the developmental or disease progression paths of cells. By examining the proportion of **spliced versus unspliced reads**, we can infer where cells lie along a trajectory, such as the differentiation of stem cells into mature cell types or the degeneration of neurons in neurodegenerative diseases.

**Differential expression analysis** is central to understanding how gene activity differs between conditions, such as healthy versus diseased states. This approach can reveal the genes driving pathological changes and can be linked to phenotypic shifts within specific cell types.

Beyond differential expression, scRNA-seq can be used to assess **cellular composition differences**, such as the loss of neurons in AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s disease. This helps identify not just which genes are altered but also how disease affects the overall structure of the tissue at a cellular level.

The breadth of questions that scRNA-seq can addressÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âfrom basic cell-type identification to complex trajectory analysesÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âunderscores its power in unraveling the intricate dynamics of cellular function and disease progression. As the field continues to evolve, these methods will only grow in their ability to provide deeper insights into the cellular architecture of health and disease.

## [1:15:30](https://www.youtube.com/watch?v=xmLoR3ynwkw&t=4530s) Cell-Projected Phenotypes

Traditional single-cell analyses often categorize cells into discrete typesÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âsuch as microglia, astrocytes, or specific neuronal subtypesÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âbased on their expression patterns. However, an even more granular approach involves studying the **transcriptional neighborhoods** of individual cells, moving beyond rigid cell-type definitions. Instead of labeling an entire cluster as, for example, excitatory neurons of cortical layer 5, this method examines each cellÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s transcriptional proximity to others, creating a continuum of expression states within a broader cell type.

This approach is not about spatial proximity but about **transcriptional similarity**, reflecting how closely related the gene expression profiles of different cells are. By projecting cells into a lower-dimensional space that captures these relationships, we can reveal fine-scale variations that traditional methods might overlook. Given our dataset of 430 individuals, we can then overlay these **phenotypes** onto the transcriptional landscape, effectively projecting AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s versus control states directly onto individual cells.

What emerges is a fascinating pattern: some cells and their surrounding neighborhoods appear distinctly AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s-like, while others are more control-like. This discovery suggests that within cell types and subtypes, there are further subdivisions with nuanced roles in diseaseÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âsubpopulations of cells that diverge from the norm in ways that correspond with disease progression.

This methodology allows us to annotate these neighborhoods according to their disease state, identifying areas within a cell population that are more **AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s-like** or **control-like**. Remarkably, this approach can be applied at the level of individual patients. By examining an individualÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s cells without prior knowledge of their clinical phenotype, we can assess whether their microglia, for example, exhibit more AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s-like or control-like transcriptional states. In some cases, the same individual may have microglia that are AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s-like but astrocytes that are control-like, highlighting the variability within a single brain.

This high-resolution analysis redefines the concept of phenotype from a static diagnosis to a dynamic attribute measurable at the level of individual cells. This allows for a more personalized and precise characterization of disease states within a patient, providing a powerful tool to correlate cellular phenotypes with other clinical and molecular measurements.

The implications are vast: by using single-cell analyses to dissect these transcriptional landscapes, we can refine our understanding of disease pathology, move beyond simple diagnostic labels, and potentially identify new therapeutic targets. This approach transforms how we think about phenotypeÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âexpanding it from a broad label to a detailed map that captures the unique cellular states contributing to disease.

Needless to say, the potential of this field is immense, and the direction it is heading excites me greatly. As we continue to push the boundaries of what single-cell analysis can achieve, IÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢m eager to hear your project ideas and explore how we can collectively contribute to this rapidly evolving area of study.


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
You should be able to explain how single-cell RNA-seq, spatial transcriptomics, quality control, pseudobulk analysis, SVD, gene modules, disease states, and trajectory inference connects a biological problem to a computational representation, model, or algorithm.

### Q2. What should you be able to explain from this lecture?
You should be able to explain how single-cell RNA-seq, spatial transcriptomics, quality control, pseudobulk analysis, SVD, gene modules, disease states, and trajectory inference connects a biological problem to a computational representation, model, or algorithm.

### Q3. What should you be able to explain from this lecture?
You should be able to explain how single-cell RNA-seq, spatial transcriptomics, quality control, pseudobulk analysis, SVD, gene modules, disease states, and trajectory inference connects a biological problem to a computational representation, model, or algorithm.

### Q4. What should you be able to explain from this lecture?
You should be able to explain how single-cell RNA-seq, spatial transcriptomics, quality control, pseudobulk analysis, SVD, gene modules, disease states, and trajectory inference connects a biological problem to a computational representation, model, or algorithm.

### Q5. What should you be able to explain from this lecture?
You should be able to explain how single-cell RNA-seq, spatial transcriptomics, quality control, pseudobulk analysis, SVD, gene modules, disease states, and trajectory inference connects a biological problem to a computational representation, model, or algorithm.

### Q6. What should you be able to explain from this lecture?
You should be able to explain how single-cell RNA-seq, spatial transcriptomics, quality control, pseudobulk analysis, SVD, gene modules, disease states, and trajectory inference connects a biological problem to a computational representation, model, or algorithm.

### Q7. What should you be able to explain from this lecture?
You should be able to explain how single-cell RNA-seq, spatial transcriptomics, quality control, pseudobulk analysis, SVD, gene modules, disease states, and trajectory inference connects a biological problem to a computational representation, model, or algorithm.

### Q8. What should you be able to explain from this lecture?
You should be able to explain how single-cell RNA-seq, spatial transcriptomics, quality control, pseudobulk analysis, SVD, gene modules, disease states, and trajectory inference connects a biological problem to a computational representation, model, or algorithm.

### Q9. What should you be able to explain from this lecture?
You should be able to explain how single-cell RNA-seq, spatial transcriptomics, quality control, pseudobulk analysis, SVD, gene modules, disease states, and trajectory inference connects a biological problem to a computational representation, model, or algorithm.

### Q10. What should you be able to explain from this lecture?
You should be able to explain how single-cell RNA-seq, spatial transcriptomics, quality control, pseudobulk analysis, SVD, gene modules, disease states, and trajectory inference connects a biological problem to a computational representation, model, or algorithm.

## Key Takeaways
- single-cell RNA-seq, spatial transcriptomics, quality control, pseudobulk analysis, SVD, gene modules, disease states, and trajectory inference is part of the MLCB modeling arc.
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

- [[scrna-seq]]
- [[gene-expression-matrix]]
- [[cell-type-annotation]]
- [[trajectory-inference]]
- [[scanpy]]
- [[pca]]
- [[umap]]

### Cluster Membership

- [[cluster-map-genomics]]
- [[cluster-map-classical-ml]]

### Key Relationships (from KG)

See [[lecture-entity-map]] for the full relationship list, and [[knowledge-graph-index]] for the global entity index.
