---
Title: "Lecture 7 - Regulatory Networks"
Author: "MLCB24"
Reference: "[Lecture 7 - Regulatory Circuitry and Networks - MLCB24](https://www.youtube.com/watch?v=LtHvgLA-PW0&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=8)"
ContentType:
  - "markdown"
Created: 2026-05-24
Processed: true
tags:
  - "source"
---


# Lecture 7 - Regulatory Networks

Video: [Lecture 7 - Regulatory Circuitry and Networks - MLCB24](https://www.youtube.com/watch?v=LtHvgLA-PW0&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=8)

Slides: [Lecture07_RegulatoryNetworks.pdf](https://www.dropbox.com/scl/fi/m3lge5x7e7xuykvjarrbx/Lecture07_RegulatoryNetworks.pdf?rlkey=ulqiqy3drl9vdol1u4xvhlwlt&dl=0)

## [0:00](https://www.youtube.com/watch?v=LtHvgLA-PW0&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=0s) Intro to regulatory motifs / gene regulation

Welcome to todayâ€™s discussion on **regulatory circuitry and networks**, where weâ€™ll explore how regulatory motifs function as the foundational elements of gene regulation. This is the final part of our first module, and we will begin by delving into **regulatory motifs**â€”the key molecular mechanisms underlying the regulatory edges we see in genetic networks.

When we talk about gene regulation, the edges connecting regulator A to gene B arenâ€™t just abstract lines in a network diagram. They represent **physical interactions** on the genome, typically at specific sequences called **regulatory motifs**. These motifs are short DNA sequences that bind transcription factors (TFs) or other regulators, allowing control over gene expression.

Motifs are generally located in larger **regulatory regions** like promoters and enhancers, which **compete with nucleosomes** (protein complexes that package DNA) to keep the DNA accessible. This competition is **biophysical**, not orchestrated by any higher-level signaling, but driven by the **probability of regulator binding** and detachment. In these regions, **multiple motifs** often work together, reinforcing each otherâ€™s binding through their interactions with nucleosomes and protein-protein contacts. This makes regulatory regions much more likely to be functional than motifs isolated in the middle of genomic deserts.

**How Regulators Bind to DNA**

Regulators donâ€™t bind by pulling the DNA strands apart and reading the sequence in a straightforward way. Instead, they â€œ**feel**â€ the DNA from the side. The bases A, T, G, and C have unique **molecular signatures** that can be recognized by the transcription factors from the edges of the DNA helix, without needing to disrupt the double strand.

If a regulator binds to a **single side of the DNA**, it will recognize a **continuous motif**. However, if the protein binds two sides, the motif may have a **gap** or spacer region in between. In cases where the regulator is a **homodimer**â€”where two identical proteins bind togetherâ€”it creates a **palindrome** (a sequence that reads the same in both directions), but in reverse on the opposite DNA strand due to the complementary base pairing.

**Motifs and Disease-Associated Variants**

These motifs are not just abstract sequences; they represent critical points of control in the genome. When **genetic variation** disrupts a motif, it can have significant consequences, such as causing **disease**. Mutations within regulatory motifs may alter transcription factor binding, leading to misregulation of gene expression. This regulatory disruption is a common cause of **non-coding genetic variants** associated with disease.

A striking example comes from work on **obesity** genetics, where a single-nucleotide variant disrupted a conserved motif involved in energy balance. This **regulatory variation** results in individuals being less able to burn calories, leading to an average gain of 10 pounds in homozygous carriers. This demonstrates the powerful effects that small changes in regulatory motifs can have on biological processes like **thermogenesis**.

In summary, today's lecture will explore **how regulatory motifs govern gene expression**, how to discover them, and how to analyze the networks that emerge from these interactions.

## [6:18](https://www.youtube.com/watch?v=LtHvgLA-PW0&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=378s) Motifs (generative model) vs. instances (single occurrence)

**Motifs vs. Instances: Understanding the Difference**

When we talk about **motifs**, itâ€™s essential to distinguish between the **concept of a motif** and an **instance** of that motif. A **motif** is a **generative model**â€”a probabilistic representation that describes a recurring pattern, such as a sequence of DNA, RNA, or protein that can bind to regulators. This model captures the likelihood of certain nucleotides or amino acids appearing at each position. In contrast, an **instance** is a **specific occurrence** or realization of the motif in a sequence.

A **generative model** allows us to predict or generate potential sequences by sampling from a distribution. For instance, a motif may specify that a position has an equal likelihood of being an A or G, but C is more likely to appear than T at another position. These motifs are typically represented using **position weight matrices (PWM)**, which describe the frequency of nucleotides across multiple observed instances. By lining up all instances where a regulator binds, you can create a PWM that captures the statistical preference for each base at every position.

For example, in the **abf1 regulator**, there are certain highly conserved positions such as TCA in the motif, and other positions that are more flexible, like the first base that can be either A or G. The **motifâ€™s structure** also informs how the regulator binds to the DNA. Some motifs may have variable **spacing** between parts of the sequence, or depend on a specific **arrangement of nucleotides** due to how the protein interacts with the DNA.

**Motif Independence and Dependencies**

A key assumption made by position weight matrices is that **nucleotide positions are independent**â€”the probability of having a particular base at one position tells you nothing about the probability at another. However, in many cases, this isnâ€™t true. Some motifs exhibit **dependencies between positions**, where having a particular base influences the likelihood of seeing another base nearby. In those cases, you might split the motif into multiple PWMs to capture these dependencies.

Similarly, motifs may vary in **spacing**. If the binding of a regulator allows flexibility in the distance between two parts of a motif, you might create several versions of the PWM to account for this variable spacing.

**Motifs Beyond DNA**

While motifs are most often discussed in the context of **DNA-binding** for gene regulation, they can also exist in **RNA** (e.g., determining whether a transcript will be spliced) and **proteins** (e.g., motifs for post-translational modifications like phosphorylation). In each case, the concept of recurrent patterns holds, allowing motifs to function across different biological levels.

**Discovering Motifs**

Motifs can be discovered using several methods. One approach is **expectation maximization** or **Gibbs sampling**, where you iteratively refine a PWM by aligning multiple sequences. Another method involves **enumerating** potential motifs by scanning the genome for specific sequences. Alternatively, **evolutionary conservation** can help identify functional motifs by focusing on sequences preserved across species. You can also leverage **protein domain knowledge** to infer what sequences a protein is likely to bind based on its structure (e.g., **zinc finger domains** or **helix-loop-helix domains**).

**Experimental Methods for Motif Discovery**

Experimentally, motifs can be discovered through techniques such as **selection assays**. In these assays, DNA fragments that bind to a protein of interest are progressively enriched through multiple rounds of selection, allowing you to identify the bound fragments. Another approach uses **DNA microarrays**, where short DNA sequences are synthesized on a chip, and proteins are washed over the surface. By detecting which sequences bind to the protein, researchers can identify motifs experimentally.

In summary, **motifs** are powerful representations of recurring sequences in gene regulation, and they can be discovered through computational and experimental means. By understanding both the **generative model** (motifs) and their **instances**, we can gain insights into how regulators control gene expression at the molecular level.

## [12:40](https://www.youtube.com/watch?v=LtHvgLA-PW0&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=760s) Regulatory Genomics Challenges: Motifs - Regulators - Targets

When approaching regulatory genomics, there are several key elements and relationships to consider. First, we have **the motif**, which is the **generative model** representing the recurring sequence pattern that binds specific regulators. Next, we have **individual instances** of that motif, which are the specific occurrences of the motif in the genome. Finally, there is the **regulator** that physically binds to a given instance of the motif and has an **affinity** for the broader generative model.

Understanding regulatory genomics involves answering several core questions:

1.  **How do we discover regulators?**
    - One approach is to identify proteins with **homology** to known regulators, suggesting they may also have regulatory functions. Once identified, they can be tested experimentally.
2.  **How do we discover motifs?**
    - **Comparative genomics** can help by highlighting **conserved regions** across species. Within these conserved regions, common sequence patterns (motifs) can be identified, allowing for de novo motif discovery.
3.  **How do we find individual binding sites (instances) for a motif?**
    - Given a motif, matching sequences in the genome can be found, but not all matches will be **functional**. The **chromatin context**â€”whether the region is accessible or actively bound by regulatorsâ€”plays a critical role in determining functionality.
4.  **How do we identify the targets of a regulator?**
    - From a known regulator, you can find its targets using **binding experiments** such as **ChIP-seq**, which identifies regions in the genome where the regulator binds. These regions are potential target sites for regulation.
5.  **How do we find the regulator for a given motif?**
    - If a motif is known, but not its corresponding regulator, you can experiment by generating multiple variants of the motif, allowing them to interact with various proteins. After isolating the proteins that bind to the motif, **mass spectrometry** can be used to identify them.
6.  **How do we find a motif from a collection of target sequences?**
    - If you have a set of target regions bound by a common regulator, you can align these sequences and search for recurring patterns. This process helps in identifying the motif that binds the regulator.

To summarize, the main challenge in regulatory genomics is navigating between these entitiesâ€”motifs, instances, regulators, and targetsâ€”and determining their relationships. Whether you start with a **regulator**, a **motif**, or a set of **targets**, different experimental and computational approaches allow you to uncover the missing links between these elements, helping to map the regulatory networks governing gene expression.

## [17:40](https://www.youtube.com/watch?v=LtHvgLA-PW0&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=1060s) Enrichment-based motif discovery

After conducting a **ChIP-seq experiment** and identifying a set of genomic regions bound by the same regulator, the next challenge is to discover the **motif** that is common to these regions. Similarly, if youâ€™ve performed an **expression analysis** and identified genes that co-express under the same conditions, itâ€™s likely that they share common regulatory elements in their **promoter regions**. In either case, the goal is to search for **common motifs** that indicate shared upstream regulation.

Once you've identified regions of interestâ€”whether through ChIP-seq, expression analysis, or protein binding microarray experimentsâ€”you generally donâ€™t have the exact sequence of nucleotides bound by the regulator. As a result, **motif discovery** becomes necessary. Here are some approaches for motif discovery:

1.  **Local Alignment**: One approach is to look for local sequence alignments across the regions to identify common patterns. These regions may be otherwise unrelated but share similar **motif sequences** that are responsible for regulatory binding.
2.  **Expert Knowledge**: Sometimes, knowledge of known regulatory motifs or binding sites can guide the search. Using a **database of known motifs**, you can compare the discovered regions with well-characterized motifs to find matches.
3.  **Enumeration**: You can systematically search for motifs by enumerating **k-mers** (e.g., 5-mers, 6-mers, or 7-mers) and looking for sequences that occur frequently across the regions. The most common sequences are likely candidates for motifs that the regulator binds to.
4.  **Evolutionary Conservation**: Another powerful approach is to restrict the search to **conserved regions** across species. This is based on the idea that functional regulatory motifs are under **evolutionary pressure** and will be conserved in orthologous sequences, even if the surrounding regions vary. However, this approach has its limitations because motifs can exhibit **degeneracy**â€”allowing for sequence variation such as **A or G** or **C or T** in some positionsâ€”making evolutionary conservation imperfect for motif discovery.

If a motif is **known**, the process is simpler: you can scan the genome for **instances** of that motif by matching the sequence at every position. If the motif is not fully characterized, an **iterative approach** can be used to refine the motif. By aligning the discovered instances and re-evaluating the frequencies of nucleotides at each position, the motif model can be continuously improved.

This iterative refinement allows for increasingly accurate **position weight matrices** (PWMs), which can then be used to scan for further instances of the motif across the genome.

## [20:53](https://www.youtube.com/watch?v=LtHvgLA-PW0&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=1253s) Expectation Maximization for Motif Discovery - starting positions - motif definitions

In the process of **motif discovery**, **expectation maximization (EM)** is a key iterative approach used to improve both motif definitions and motif instance detection. The basic idea behind EM is to use an initial **motif definition** to search for possible instances of that motif across a genomic region, then refine the motif based on those detected instances, and continue cycling through this process to get progressively better results.

To start, once we have a **motif definition**, we can use it to search for possible instances across a genome. At each position where a potential motif instance appears, we can calculate the **likelihood** that the given DNA sequence was generated by the motif model versus being generated by the background. This is expressed as a **likelihood ratio**â€”comparing the likelihood that a sequence belongs to the motif versus a random background sequence.

Once potential motif matches are found, the next step is determining how to handle **uncertainty**. Do we always take the most likely match, even if the likelihood is only slightly higher than the alternatives? Or should we consider all possibilities?

Hereâ€™s where various methods come into play:

- **Greedy method**: Always selects the maximum likelihood match, simplifying the process by focusing only on the most likely candidate.
- **Expectation maximization**: Considers all possible motif instances, but weighs them according to their likelihoods. This method uses a **weighted average** to refine the motif, considering all matching positions, which helps avoid bias but may slow down convergence.
- **Gibbs sampling**: Involves a probabilistic selection where a candidate is chosen based on its likelihood. For example, a motif with 70% probability will be selected 70% of the time, offering a more exploratory approach.

The key challenge with EM is navigating the **landscape of possible motifs**. This involves adjusting the motif model iteratively, trying to discover the best motif sequence. **Expectation maximization** typically converges at a **local maximum** based on the starting point, while **Gibbs sampling** is more flexible, sometimes jumping between different solutions, potentially helping avoid local maxima.

A critical strategy in EM is to use **multiple initializations**, starting from different positions in the sequence space. This helps increase the chances of finding the **global maximum** motif rather than getting stuck in a local optimum.

Ultimately, all of these methods aim to balance **accuracy** with **speed of convergence**, refining the motif model step-by-step until it captures the true underlying regulatory sequence pattern.

This EM approach is analogous to the iterative processes we've seen in **K-means clustering**, **hidden Markov models**, and **Baum-Welch training**, where machine learning is used to refine models iteratively based on data patterns.

## [26:58](https://www.youtube.com/watch?v=LtHvgLA-PW0&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=1618s) Deep Learning and Convolutional Neural Networks for Motif Discovery

**Deep learning** has recently emerged as a powerful tool in the field of **genomics**, providing new ways to understand genomic sequences through **convolutional neural networks (CNNs)**. The same principles that allow CNNs to detect features in imagesâ€”like lines, edges, and eventually objectsâ€”can be applied to genomics, where raw sequence data can be transformed into progressively more abstract representations.

In this approach, CNNs can **learn motifs** from scratch, just as they learn filters or patterns in image data. The process involves feeding the network a series of nucleotide sequences and training it to predict specific outcomes. For example, using experimental data, the model can be trained to predict whether a given sequence is **bound by a specific regulator**, such as **ABF-1**. You provide the CNN with labeled dataâ€”sequences known to be bound or not bound by a particular regulatorâ€”and the network learns which patterns in the sequence lead to binding.

A significant advantage of CNNs is their ability to scale beyond predicting a single regulatory binding site. You can implement **multitask learning**, where the network is tasked with predicting the binding of **multiple regulators** simultaneously. This involves creating a vector of tasks for each sequence, where each task corresponds to whether a specific regulator binds to the sequence. The **shared representations** learned by the network can capture common motifs and patterns that are useful across multiple regulators, making the model more generalizable and versatile.

By learning in this layered fashion, CNNs can capture increasingly complex representations. At the **base layer**, the network might learn individual motifs. In the layers above, it might start combining those motifs into **motif parts** or more intricate **combinations of motifs** with varying spacing. This is analogous to how the structure of a protein, such as a **zinc finger**, can be decomposed into functional parts, and the CNN can learn the building blocks at the lower layers before assembling them into full motifs at higher layers.

Another powerful feature of deep learning is its ability to not only predict whether a sequence is bound or not, but also to predict the **shape** or **signal intensity** of the binding at very high resolution. The model can be trained to handle multiple types of data simultaneously, such as **regulator binding**, **nucleosome positioning**, and **histone modifications**. This versatility allows the network to detect more complex patterns, incorporating various regulatory elements like **splicing sites** or **initiator factors**.

Traditionally, motif discovery involves fishing for motifs that explain experimental results, such as determining which sequences are bound by a known regulator. Deep learning extends this by allowing for more complex **joint learning tasks**, such as predicting multiple types of genomic signals in tandem. This enables a deeper understanding of genomic regulation and opens up new possibilities for exploring **gene regulation** in a more holistic and integrated manner.

## [32:03](https://www.youtube.com/watch?v=LtHvgLA-PW0&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=1923s) Evolutionary signatures for de novo motif discovery

**De novo motif discovery** using **evolutionary signatures** leverages the principle that **conserved genomic regions** often harbor **functional elements** like regulatory motifs. The idea is straightforward: within regulatory regions, some DNA sequences are **conserved across species**, indicating functional importance. These conserved regions often correspond to **motif instances**, but finding individual instances is not enough; you need many instances to infer a **motif**.

In this method, we focus on identifying **conserved islands** across the genome and then search for **sequence patterns** that explain those islands. This involves discovering **recurrent patterns** that are conserved in multiple regions of the genome, which would indicate the presence of a regulatory motif.

For instance, consider the well-known **Gal4 motif** involved in regulating genes like **GAL1** and **GAL10**. By identifying conserved instances of the Gal4 motif across the genome, we can compare these conserved motifs to **randomly shuffled sequences** to distinguish true motifs from background noise. Shuffling, however, must be done carefullyâ€”maintaining certain properties of the original motif (e.g., **dinucleotide frequencies**) ensures that the shuffled sequences are reasonable controls.

The **shuffling process** plays a critical role in motif discovery, as the way you shuffle affects which **distinguishing features** you detect. For example, if you shuffle nucleotides randomly without considering spacing or other contextual factors, you might miss important regulatory signals.

Once these conserved motifs are identified, we can investigate their **conservation patterns** in different genomic contexts, such as intergenic versus coding regions, or upstream versus downstream of genes. For example, **Gal4 motifs** are often more conserved in **intergenic regions**, where they perform their regulatory functions, than in **coding regions**.

This approach allows for **systematic motif discovery**. By **enumerating sequence patterns** with gaps and looking for those that are highly conserved, we can build a catalog of **motifs**. This strategy has been applied across various species, such as yeast, humans, flies, and mammals, leading to the discovery of both **known motifs** and **novel motifs**, many of which were validated experimentally.

By using **evolutionary signatures**, this method enables **de novo motif discovery** without any prior knowledge of the regulatory protein or experimental data. It uncovers conserved regulatory elements across species, expanding our understanding of **gene regulation** at a fundamental level.

## [42:11](https://www.youtube.com/watch?v=LtHvgLA-PW0&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=2531s) Evolutionary signatures for motif instance identification

**Evolutionary signatures** can also be used to identify **individual motif instances** with high confidence. After discovering motifs, the next step is to pinpoint **specific occurrences** of these motifs in the genome that are functionally relevant. This is where **phylogenetic branch length** becomes crucial.

To identify **high-confidence motif instances**, we assess the **phylogenetic branch length** over which the motif is conserved. The key idea is to tolerate minor **mutations** (e.g., an A or G in certain positions) and **gaps** that occur due to insertions or deletions in alignments. However, we focus on **long branches** in phylogenetic trees, which provide more informative signals of conservation compared to **short branches** where mutations are less frequent.

We start by searching sequences independently and calculating a **branch length score** for each motif instance. This score reflects how conserved the motif is across species, measured in terms of **substitutions per site**. Even with multiple mutations, if a motif is highly conserved across many species, the **total branch length** may exceed one substitution per site, indicating that the motif is real.

Next, we generate **shuffled motifs** as controls, ensuring these shuffled versions maintain properties such as length and nucleotide composition similar to the real motif. By comparing the conservation of real motifs against shuffled motifs, we can measure **motif-specific conservation enrichment**. This comparison tells us how much more conserved the motif is than expected by chance, given its length and genomic distribution.

The results are visualized by plotting **confidence scores** based on the ratio of real to shuffled motif conservation. **Higher confidence scores** are associated with greater branch lengths, indicating strong conservation across species, while lower confidence scores suggest random or weak conservation.

As we increase our confidence, we find that **transcription factor motifs** tend to be enriched in **promoters**, while **microRNA motifs**â€”which act on mRNAâ€”are enriched in the **5' untranslated regions** (5' UTRs) of genes. This correlation between motif confidence and known biological functions reassures us that the evolutionary conservation we are detecting is meaningful.

The key takeaway is that we now have a **universal confidence scale** for motif identification, allowing us to compare motifs of different lengths and types using the same metric. This confidence score can be applied across all motifs, making it a powerful tool for identifying functionally relevant **motif instances**.

Finally, this method enables us to predict **individual targets** of motifs with high precision. The combination of **motif discovery** and **instance identification** using evolutionary conservation provides a comprehensive framework for mapping **regulatory elements** across the genome.

## [50:44](https://www.youtube.com/watch?v=LtHvgLA-PW0&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=3044s) Network Analysis Section Overview

We are transitioning from motif and regulatory element discovery to understanding how to **analyze the resulting networks** that emerge from knowledge about regulator bindings. For example, if we know that a certain **regulator binds** to multiple locations in the genome, we can begin to connect these into a **regulatory network**. Similarly, we might understand how other types of networks, such as **metabolic** or **signaling networks**, are structured.

The goal is to understand how to **analyze and interpret** these networks. We will explore several different **types of networks**, such as:

- **Regulatory Networks**: Networks that depict the interactions between transcription factors and the genes they regulate.
- **Metabolic Networks**: Networks of biochemical reactions within a cell.
- **Signaling Networks**: Networks that represent pathways where information flows, such as signaling cascades triggered by external stimuli.
- **Interaction Networks**: Networks of protein-protein or protein-DNA interactions.
- **Functional Networks**: Networks where nodes represent biological entities (genes, proteins, etc.), and edges indicate functional relationships.

Next, we will examine both **Bayesian probabilistic views** and **algebraic views** of networks to understand the **structure** and **functionality** of these networks. This will also involve an introduction to **network centrality**, which helps measure the importance or influence of nodes within a network.

The discussion will include a **linear algebra review**, covering concepts such as **eigenvalues**, **singular value decomposition**, and **low-rank approximation**. These mathematical tools are critical for **dimensionality reduction** techniques like **Principal Component Analysis (PCA)**, which help us uncover patterns in complex network data.

Finally, we will introduce **Graph Neural Networks (GNNs)**, a modern machine learning approach for analyzing and predicting properties of networks. GNNs are especially useful for working with **non-Euclidean data** such as graphs, which donâ€™t fit into traditional neural network architectures. Although GNNs will be introduced here, they will be further explored in **subsequent lectures**.

This section will provide the foundation for performing in-depth **network analysis** across various biological and computational domains.

## [51:55](https://www.youtube.com/watch?v=LtHvgLA-PW0&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=3115s) Network types: regulatory, metabolic, signaling, interaction, functional

The **organization of living systems** is structured in layers. At the base is the **genome**, which is modulated by the **epigenome** (discussed in previous lectures), and the genome also produces the **transcriptome** (mRNAs, microRNAs, etc.). The **transcriptome** then translates into the **proteome** through the process of protein synthesis. We can begin to understand **regulatory networks** at each of these levels:

1.  **Gene Regulatory Networks**: These are networks that capture the interactions between transcription factors and their target genes, representing **pre-transcriptional regulation**. This includes understanding which **regulator binds** to a region of DNA and **activates or represses** a particular gene.
2.  **Post-transcriptional Regulation Networks**: These focus on how elements like **microRNAs** regulate gene expression **after transcription** by influencing processes such as gene stability, degradation, and localization of transcripts.
3.  **Protein-Protein Interaction Networks**: Proteins that **physically interact** with one another can form complexes that either help bind to other proteins or regulate certain pathways.
4.  **Signaling Networks**: These depict **signaling cascades**, where one protein modifies another (e.g., phosphorylation), leading to a chain reaction that eventually affects gene expression. For example, a protein might phosphorylate another, activating a cascade that leads to the expression of genes.
5.  **Metabolic Networks**: These focus on how different **metabolites** are transformed into one another via enzymatic reactions. The **nodes** in these networks are metabolites, while the **edges** represent the enzymes that catalyze transformations between them.

### Characteristics of Network Types:

- **Gene Regulatory Networks**: These are typically **directed** and **signed** (indicating either activation or repression) networks. They often show **weighted edges**, where the strength of activation or repression between nodes may vary.
- **Metabolic Networks**: These are usually **bidirectional**, where an enzyme can catalyze both forward and reverse reactions. However, some reactions might be **irreversible**. In these networks, **nodes** are metabolites, and **edges** represent enzymes.
- **Signaling Networks**: These are **directed** and **unweighted** networks, as phosphorylation or signaling events are binary (either occurring or not).
- **Protein-Protein Interaction Networks**: These are **undirected** and **unweighted** networks, where a physical interaction between two proteins is symmetrical (if protein A interacts with protein B, then protein B interacts with protein A).
- **Functional Networks**: In contrast to physical interactions, these represent **functional relationships** such as **coexpression** of genes. The edges in functional networks represent **correlations**, and the networks are typically **undirected** but **weighted** based on the strength of these correlations.

### Cross-network Interactions:

There is a substantial amount of **cross-talk** between these networks. For instance:

- A **signaling cascade** might activate a regulator that turns on a gene, which then produces a protein that participates in the regulatory or signaling networks.
- A **gene regulatory network** may control the transcription of enzymes that catalyze reactions in a **metabolic network**, and the metabolites produced may serve as **signals** in a **signaling network**, completing the cycle of regulation.

These **interconnections** between networks illustrate the complexity of biological systems, where events at one layer can influence others, contributing to an integrated system of regulation and function.

## [57:20](https://www.youtube.com/watch?v=LtHvgLA-PW0&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=3440s) Network applications and challenges

We face several challenges when working with networks, such as **finding regulators**, **discovering motifs**, and **identifying target genes**. Beyond these, we also want to understand how **networks themselves predict cellular activity**. This is where **graph neural networks** (GNNs) come in. GNNs allow us to learn **representations from networks** to predict specific functions.

For example, given a chemical compound, we might want to predict its effect on a biological system, such as whether it has a **detrimental effect on E. coli** (helping patients by killing the bacteria). We can also use this approach to predict the **properties of molecules** or **proteins** from their network structures.

### Predicting Functions with Graph Neural Networks:

GNNs help predict the **function of a protein** based on its network. For instance, a protein could be part of a **regulatory network**, a **signaling molecule**, or an **enzyme**. By analyzing the **graph structure**, we can infer these functions. GNNs are also used to **infer networks from functional data**, such as gene expression patterns, helping us determine which genes are **correlated** or **interacting** based on the observed data.

### Structure Analysis of Networks:

Network analysis also enables us to explore the **vulnerabilities** or key points of networks. For example, in the case of a viral attack, we might want to know the most **vulnerable hubs** where the virus attacks the host or bacterium. Networks have **hubs**, which are highly connected points, and **network motifs**, which are recurring patterns of connections. For instance:

- **Feedforward loops** occur when regulator A controls both B and C, and B also controls C.
- **Feedback loops** involve mutual regulation among multiple entities, such as when A regulates B, B regulates C, and C regulates A.

We can also **discover functional modules** within networks, which are sub-networks that are **densely connected**, revealing higher levels of cooperation or coordination within certain areas of the graph.

### Network Types:

We distinguish between different types of networks:

- **Physical networks** involve direct physical interactions, such as binding between proteins.
- **Relevance or functional networks** describe how **similar** entities are in function (e.g., coexpression networks where genes exhibit similar expression patterns without necessarily interacting physically).
- **Probabilistic networks** capture **dependencies** between nodes. For example, observing one variable can change the probability distribution of other variables based on the **flow of information** through intermediate nodes.

In **probabilistic networks**, we can also explore **conditional independence**. If certain intermediate variables are fully observed, then nodes that previously depended on one another may become independent. This helps us understand how information propagates through the network and how it changes when new observations are introduced.

By understanding these networks and their structures, we can **predict functions, discover new motifs, and analyze vulnerabilities**, offering powerful insights into **biological systems**.

## [1:02:27](https://www.youtube.com/watch?v=LtHvgLA-PW0&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=3747s) Matrix Representation of Networks and Linear Algebra

We can represent **networks** as **matrices**. For example, a **graph** where node **A** is connected to node **B** with a weight of 1.5 can be represented in an **adjacency matrix**. In the case of an **undirected network**, this adjacency matrix is **symmetric**. The matrix contains entries that reflect the weights of the edges between nodes, allowing us to mathematically capture the network structure.

### Degree of Nodes in a Network:

We can also calculate the **degree** of a node, which is the number of edges connected to it. In a **weighted network**, the degree is simply the **sum of the weights** of all edges connected to a node. For instance, node **B** in our network may have a **degree of three**, meaning it is connected to three other nodes. In a **directed network**, we distinguish between the **in-degree** (edges coming into the node) and **out-degree** (edges going out from the node). This distinction helps identify **in-hubs**, which aggregate a lot of information, and **out-hubs**, which propagate a lot of information.

### Matrix Operations on Networks:

Once we have a matrix representation of a network, we can perform various **matrix operations** to understand how information flows through the network. Applying the **adjacency matrix** to a **vector of starting weights** (such as concentrations of metabolites or initial states of nodes) shows how these values propagate through the network.

In this context, the **matrix multiplication** transforms the **vector**, which could represent initial conditions at each node. For example, if we have an initial value of **7 at node A** and a **rate of 2** for the connection between nodes, the multiplication propagates the value through the network based on these rates.

### Iterative Matrix Applications:

By applying the matrix multiple times (e.g., **A Ã— vector**, **AÂ² Ã— vector**, **AÂ³ Ã— vector**), we can see the **cumulative effect** of repeatedly applying the network transformation. This iterative process shows how the network evolves over multiple steps and allows us to compute **transitive closure**, representing the cumulative effect of applying the transformation repeatedly.

### Eigenvectors and Eigenvalues:

Eigenvectors and eigenvalues are important in **network analysis**. They help us understand the long-term behavior of matrix transformations by identifying **principal directions** along which transformations act. This is particularly useful in identifying **central nodes** in the network or understanding **steady-state distributions** when the network stabilizes after multiple iterations of transformation.

This formalism of representing networks using matrices enables a wide range of **computational techniques** to analyze their behavior, simulate signal propagation, and extract key structural insights.

## [1:06:03](https://www.youtube.com/watch?v=LtHvgLA-PW0&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=3963s) Eigenvalues, Eigenvectors

In network analysis, **eigenvectors** are vectors that remain aligned in the same direction when a matrix transformation is applied, but their magnitude is scaled by a scalar factor called an **eigenvalue**. This concept is essential in understanding how networks behave and in simplifying complex data representations.

### What are Eigenvectors and Eigenvalues?

Every **matrix** transformation alters the space on which it is applied, shifting or stretching vectors. However, certain **eigenvectors** remain in their original direction, and their length is multiplied by a constant factorâ€”this factor is the **eigenvalue**. In other words, applying the matrix to an eigenvector results in a scaled version of the same vector, represented mathematically as: Aâ‹…v=Î»â‹…v, where A is the matrix, v is the eigenvector, and Î» is the eigenvalue. This means that instead of shifting or rotating the vector, the matrix only stretches or shrinks it.

### Why are Eigenvectors and Eigenvalues Important?

Eigenvalues and eigenvectors allow us to **decompose complex systems** and identify **underlying patterns**. For example, in gene regulatory networks, a large set of genes may exhibit highly correlated behavior. By finding the **eigenvectors** of this matrix (the gene expression data), we can reduce the system to a smaller set of "eigen-genes" that capture the most important trends in the data.

This approach helps us:

- **Simplify complex data**: Instead of analyzing hundreds of genes individually, we can analyze a few **principal components** that capture the most significant variations in the system.
- **Reveal patterns of variation**: Eigenvectors can represent large **modules** of co-expressed genes, providing insights into how groups of genes behave under different conditions (e.g., how a set of genes responds to changes in brain vs. liver tissue).

### Geometric Interpretation:

From a **geometric perspective**, eigenvectors represent **directions** in which the transformation acts by simple scaling, rather than more complex rotations or shifts. We can think of matrix transformations as altering the space in multiple dimensions, and **eigen-decomposition** allows us to break down that transformation into simpler operations:

1.  **Rotation** of the matrix into a different space.
2.  **Scaling** the eigenvectors within that transformed space.
3.  **Rotation** back to the original space.

This **decomposition** is useful for making complex transformations more understandable and manageable.

### Eigen-Decomposition and Principal Component Analysis (PCA):

By decomposing a matrix into its **eigenvectors** and **eigenvalues**, we can start to uncover the **principal components** of variation in a system. Principal component analysis (PCA) uses this approach to reduce the dimensionality of a dataset, focusing on the most significant sources of variation. For example, instead of analyzing each gene individually, we can analyze the **principal axes** of variation in gene expression data to understand the main trends that explain differences between conditions or tissues.

Eigen-decomposition is a powerful tool in network analysis, helping us break down complex structures into simpler, more interpretable components.

## [1:09:19](https://www.youtube.com/watch?v=LtHvgLA-PW0&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=4159s) Principal Components Analysis PCA, SVD

Principal Component Analysis (PCA) is a fundamental technique used in data reduction and pattern discovery, particularly in the context of gene expression and other high-dimensional biological data. Here's a breakdown of the key concepts:

### Principal Component Analysis (PCA)

PCA helps to transform a large, complex dataset into a simpler representation by identifying the principal componentsâ€”directions in the data along which the variation is maximized. These components allow for more efficient exploration and interpretation of the data. In biological systems, this might mean reducing thousands of gene expression measurements to a few meaningful variables.

**Steps in PCA:**

1.  **Variation Across Genes:** You start with a dataset where gene expression levels vary across different conditions or samples. These variations can be described in terms of different variables or gene expression patterns.
2.  **Transformation of the Space:** Instead of focusing on the raw expression of individual genes, PCA rotates the data space to find new axes, or "principal components," that capture the most significant patterns of variation.
3.  **Dimension Reduction:** By finding the principal components (often just a few), you reduce the complexity of the dataset. For example, instead of focusing on the expression of 20 individual genes, PCA might reveal that those genes collectively describe a process like heat shock stress or nutritional stress.

These new dimensions are combinations of the original variables and typically explain the **maximum variance** in the data. As a result, PCA allows you to capture the essential features of a dataset in fewer variables.

### Singular Value Decomposition (SVD)

Singular Value Decomposition (SVD) is a broader mathematical technique than PCA and can be applied to matrices that are not square. Itâ€™s essentially a generalization of eigenvalue decomposition. Like PCA, it is useful for **dimension reduction** and **data compression**.

**Matrix Factorization:** SVD decomposes a matrix into three components: U, Î£, and V. These represent different ways of understanding the relationships between rows and columns of the matrix. U represents the left singular vectors (e.g., gene expression). Î£ is a diagonal matrix of singular values (analogous to eigenvalues in PCA). V represents the right singular vectors (e.g., samples or conditions).

**Non-Square Matrices:** Unlike PCA, which operates on square covariance matrices, SVD can be applied to rectangular matrices, making it more flexible for analyzing datasets where the number of variables does not match the number of samples.

### Applications in Biology:

In biological data analysis, both PCA and SVD help to **reduce the dimensionality** of complex datasets like gene expression matrices or metabolic profiles. This makes it easier to identify underlying patterns and relationships among genes or experimental conditions.

For example, in a matrix of gene expression data, SVD allows us to find **latent variables** or "eigen-genes," which can be used to describe major trends in the data. These trends might represent fundamental biological processes or cellular states, reducing the need to analyze individual genes separately.

### Singular Value Decomposition in Practice:

- **Generalization of PCA:** While PCA deals with square matrices, SVD provides a more general method applicable to rectangular data matrices, making it ideal for datasets with unequal numbers of variables (e.g., thousands of genes measured across a few experimental conditions).
- **Eigen Genes and Eigen Experiments:** By applying SVD, we can create abstract representations such as "eigen-genes" and "eigen-experiments." These concepts allow us to reduce a complex biological system to a small number of variables, providing insights into high-level processes, such as how metabolic stress or heat shock affects the system as a whole.

### Sparse PCA and Nonlinear Dimensionality Reduction:

While traditional PCA uses linear combinations of the original variables, **sparse PCA** imposes additional constraints, ensuring that only a small subset of variables is used to describe the principal components. This makes the interpretation of results more biologically meaningful, as it highlights only the most critical genes or features. Additionally, **nonlinear dimensionality reduction techniques** can be applied to capture more complex relationships that cannot be explained by linear transformations alone.

## [1:11:58](https://www.youtube.com/watch?v=LtHvgLA-PW0&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=4318s) Non-linear Dimensionality Reduction: t-SNE

Non-linear dimensionality reduction techniques like **t-SNE** have become widely used for understanding and visualizing high-dimensional data, particularly in complex biological datasets such as single-cell RNA sequencing data. Here's a detailed breakdown of the process and its significance:

### Why Use Non-linear Dimensionality Reduction?

Traditional dimensionality reduction techniques like **PCA** focus on linear transformations. They are useful when data vary linearly across a set of principal components. However, biological systems and high-dimensional data, such as gene expression profiles, often exhibit **non-linear relationships**. These patterns are complex, and PCA may fail to capture important structures in the data.

To address this, **non-linear dimensionality reduction techniques** like t-SNE are applied. t-SNE can capture **non-linearities** in the data, revealing patterns that are not visible in a linear projection.

### t-SNE Overview

t-SNE aims to reduce the dimensionality of high-dimensional data (such as gene expression profiles) while preserving the **local structure**â€”the relationships between close neighborsâ€”of the data. It achieves this by focusing on **pairwise similarities** between data points in high-dimensional space and embedding those into a lower-dimensional space (typically 2D or 3D).

**High-dimensional Relationships:** Imagine having data in a very high-dimensional space (e.g., 20,000 gene expression profiles). In that space, some points (data samples) are very close to each other, representing similar biological profiles (e.g., similar gene expression patterns).

**Neighbor Preservation:** t-SNE tries to ensure that points that are close together in high-dimensional space remain close in the reduced space, while points that are far apart are spread out accordingly.

### t-SNE Mechanics

**Preserving Neighborhoods:** The method begins by measuring how close each point is to its neighbors in the high-dimensional space. This is achieved using **pairwise distances** or a probability distribution that reflects the likelihood that two points are close in the original space.

**Stochastic Mapping:** The algorithm then attempts to embed the data in a lower-dimensional space, adjusting the points such that their **pairwise distances** in this lower space reflect their relationships in the original high-dimensional space. The process is iterative, with the algorithm making small adjustments to the positions of points in the lower-dimensional space over multiple steps to improve the match between high-dimensional and lower-dimensional relationships.

**Non-linear Transformation:** Unlike PCA, which relies on linear transformations, t-SNE uses **non-linear transformations** to better capture the complex relationships in the data. It ensures that clusters of similar data points are tightly packed together in the reduced space while pushing dissimilar points far apart.

**High-dimensional to Low-dimensional Mapping:** The key goal of t-SNE is to map a **high-dimensional k-nearest neighbor graph** to a **low-dimensional k-nearest neighbor graph** while preserving the relationships between pairs of points as closely as possible.

### Visualization and Insights

One of the primary uses of t-SNE is for **visualization**. For example:

In **single-cell RNA sequencing (scRNA-seq)**, t-SNE can be used to project tens of thousands of gene expression profiles into a 2D or 3D space. This reduced representation allows researchers to visualize clusters of cells with similar gene expression profiles, revealing potential subpopulations of cells.

**Cell Differentiation:** Cells that are similar in function or in the same developmental lineage will cluster together, making it easier to identify and interpret biological patterns.

### Limitations

**Interpretation of Distances:** While t-SNE excels at preserving **local structures**, it is less effective at preserving **global structures**. This means that while itâ€™s good for identifying local clusters, distances between clusters may not be meaningful.

**Computational Complexity:** t-SNE is computationally expensive and can be slow to converge, especially for large datasets. Moreover, the algorithm can sometimes produce different results for the same dataset due to the randomness involved in the initialization process.

### Application in Single-cell Data

In the context of **single-cell data analysis**, t-SNE has revolutionized how we visualize and interpret large-scale gene expression datasets. For example, in **scRNA-seq**, the algorithm is used to reduce the data from tens of thousands of dimensions (each dimension representing a geneâ€™s expression level) to just two or three dimensions. This reduced space allows researchers to easily spot **cellular subpopulations** and **transcriptional states**, as distinct groups of cells naturally form clusters in the t-SNE plot.

### Summary

t-SNE provides a powerful way to visualize complex, high-dimensional data by transforming it into a lower-dimensional space while preserving the local relationships between points. This makes it invaluable for biological applications where understanding clusters and patterns in data, such as in gene expression or cellular differentiation, is critical.

## [1:16:23](https://www.youtube.com/watch?v=LtHvgLA-PW0&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=4583s) Machine Learning on Networks

**Learning on Graphs** allows us to directly model complex relationships between entities. These networks can represent **gene-gene interactions**, **physical structures**, **textual relations**, or **molecular structures**. In each case, **edges** between nodes can carry additional constraints, such as **angles in 3D molecular geometry**.

The key challenge is to **learn representations** of these graphs that capture essential features for **predictive modeling**. This can be done at multiple levels:

1.  **Node-level representations**: Predict properties of individual nodes based on their relationships with neighbors.
2.  **Edge-level representations**: Learn interactions or dependencies between nodes.
3.  **Subgraph representations**: Capture local graph structures to infer larger patterns.
4.  **Graph-level representations**: Summarize the entire graph for higher-level predictions.

**Representation Learning** on graphs is analogous to deep learning on images. Just as pixels are abstracted into **edges, corners, shapes, and objects**, **subgraphs** can be used to build **node properties** in layers. For example:

- **Level 0**: Initial node properties.
- **Level 1**: Properties influenced by direct neighbors.
- **Level 2**: Properties influenced by neighbors of neighbors.

This progressive abstraction allows for more complex **relational understanding**. At each level, the representation is updated based on neighborhood interactions, and this is done at both **node** and **edge levels**.

In practice, **graph neural networks (GNNs)** enable this multi-level abstraction. Once the model is trained, we can **benchmark** performance, analyze **explainability**, and refine the learned **representations** for various tasks, from biological networks to molecular property prediction

## [1:18:49](https://www.youtube.com/watch?v=LtHvgLA-PW0&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=4729s) Summary

Today we focused on the **building blocks of regulatory motifs**â€”the physical sequences bound by transcription factors or regulatorsâ€”and how we can discover these motifs through techniques such as **expectation maximization**, **enrichment analysis**, or **evolutionary signatures**. These motifs are fundamental to understanding gene regulation, and from these motifs, we build regulatory networks.

We then explored how to analyze the **resulting networks** to uncover key properties such as **centrality**, **eigenvectors**, **principal components**, and **lower-dimensional projections**. Finally, we discussed how **machine learning** can be applied to these networks, using graph neural networks to infer complex relationships at different levelsâ€”nodes, edges, subgraphs, or the entire graph.

Looking ahead, the next two modules will extend these concepts to **protein structure** and **chemical structure**, where we'll use the same methodologies to deepen our understanding of these biological and chemical systems. This lecture provided a foundation for that exploration, and I encourage you to begin preparing for the next steps by reviewing and attending office hours early to stay on track.
