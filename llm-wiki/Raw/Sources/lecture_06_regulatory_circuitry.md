---
Title: "Lecture 6 - Regulatory Circuitry"
Author: "MLCB24"
Reference: "[Lecture 6 - Regulatory Circuitry - MLCB24](https://www.youtube.com/watch?v=PJFRz1vrGEI&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=21s)"
ContentType:
  - "markdown"
Created: 2026-05-24
Processed: true
tags:
  - "source"
---


# Lecture 6 - Regulatory Circuitry

Video: [Lecture 6 - Regulatory Circuitry - MLCB24](https://www.youtube.com/watch?v=PJFRz1vrGEI&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=7&t=21s)

Slides: [Lecture06_RegulatoryGenomics.pdf](https://www.dropbox.com/scl/fi/2aip7m2tcdco3f10dqoqg/Lecture06_RegulatoryGenomics.pdf?rlkey=fb4lvf6tbgdvm6akd760szc1o&dl=0)

## [0:00](https://www.youtube.com/watch?v=PJFRz1vrGEI&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=6&t=0s) Introduction

Welcome, everyone! Today, we're diving into **regulatory circuitry**. We've previously discussed different parts of the genome, but todayâ€™s focus will be on understanding how **non-coding regions**â€”particularly **regulatory elements** like **enhancers** and **promoters**â€”play a key role in disease-associated genetic variants. Remarkably, 93% of these disease-linked variants are found in non-coding regions, not in **protein-coding regions**. This raises critical questions: Where are these variants located? Are they targeting promoter regions, enhancer regions, or other control regions? If they are targeting **enhancers**, how do they affect target genes, and what are the **upstream regulators** that control these regions? Additionally, how do these regulatory regions behave dynamically across different **cell types**?

We'll tackle these key questions regarding regulatory circuitry today. Our focus will be on laying the **foundations at the genomic level**, and later in the week, we'll transition to the networks that arise from these circuits, helping us to understand **biological networks** more comprehensively.

There are several core topics on the agenda:

1.  **Epigenomic Dynamics**: Building on what we discussed previously, we'll dive deeper into understanding **chromatin states** across multiple cell types and how this contributes to gene regulation dynamics.
2.  **Enhancer-Gene Linking**: We will examine how enhancers are linked to their **target genes**. This includes exploring different methods such as **3D genome conformation**, **correlation-based methods**, and a brief discussion of **expression quantitative trait loci (eQTLs)**, which are genetic variants that affect nearby gene expression, rather than influencing **phenotypic traits** directly.
3.  **Regulatory Motif Discovery**: We will explore various methods for discovering **regulatory motifs**. These include traditional methods such as **enrichment analysis**, **expectation maximization**, and **Gibbs sampling**, as well as more advanced approaches like **deep learning** and **convolutional neural networks (CNNs)**.
4.  **Comparative Genomics**: We'll also delve into **global motif discovery** through comparative genomics, focusing on conserved sequence identification across species.

Finally, time permitting (though it's unlikely), we'll explore **massively parallel reporter assays** for discovering new regulatory elements.

In this lecture, weâ€™ll touch on concepts from previous weeks, such as **expression analysis**, **single-cell analysis**, **sequential data in hidden Markov models (HMMs)**, and **epigenomics**, as we integrate all of these into todayâ€™s topic of **regulatory genomics**. We'll also get ready to move on to **biological networks** next time.

Let's begin!

## [3:45](https://www.youtube.com/watch?v=PJFRz1vrGEI&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=6&t=225s) Epigenomics review: signals, mapping, HMMs

Enhancers and promoters play a crucial role in regulating gene expression, as they contain **motifs** that bind to **regulatory proteins**, forming key parts of the **regulatory circuitry**. This circuitry is physically instantiated through **DNA interactions**, where regulatory proteins bind to enhancers, which in turn loop around to physically interact with promoters. This allows **RNA polymerase** to bind and initiate **transcription** of RNAs.

Last time, we discussed the challenge of mapping **hundreds of millions of short reads** to the genome efficiently. We explored the **Burrows-Wheeler transform**, a computational breakthrough initially implemented in **BWA** (Burrows-Wheeler Aligner), which allows for rapid and memory-efficient genome mapping. This technique builds on the idea of **growing suffixes** of a search string and progressively **narrowing the search space** by using pointers to guide the process.

We then introduced the idea of using **multiple independent epigenomic marks** to analyze genomic signals. By combining these signals, we can leverage **Hidden Markov Models (HMMs)**, which is the focus of today's lecture. HMMs offer a powerful framework for distinguishing between **observed** and **hidden** states, enabling us to model dependencies between **adjacent genomic positions**.

This approach is critical because **genomic features**, such as enhancers and promoters, tend to occur near each other. For instance, itâ€™s far more likely to find an **enhancer** near a **transcribed region** rather than in the middle of **repressed regions**. These relationships are encoded in the **transition probability matrix** of the HMM, which tells us the probability that the next state at position iii is LLL given that the state at position iâˆ’1i-1iâˆ’1 was KKK. This captures transitions such as **enhancer to promoter**, **promoter to transcribed region**, and so on.

Additionally, the **emission probabilities** describe the likelihood of observing a particular signal (or "character") given that we are in a specific **hidden state**. This allows us to model the generative process behind the **observed genomic data** using a **probabilistic framework**.

## [6:30](https://www.youtube.com/watch?v=PJFRz1vrGEI&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=6&t=390s) Parsing, scoring, Viterbi decoding, optimal path

In our last lecture, we explored the foundation of **Hidden Markov Models (HMMs)**, focusing on how we transition between different states and self-transition within the same state. These transitions help determine the **length** of certain regions like **promoter sequences** or **background sequences**. This is crucial because the **probability of staying in the same state** may be very high (e.g., 99%), but it decreases **geometrically** with each time step, resulting in a **geometric length distribution** for these states.

We also discussed **emission probabilities**, which tell us how likely certain states are to emit particular **characters**. For example, in a **background state**, **ACGT** might have equal probabilities, while in a **promoter state**, **C** and **G** might have a higher probability than **A** and **T**.

Next, we introduced how to **parse** sequences by analyzing transitions between background and promoter states. The **transition penalty** for switching between states (e.g., from **background** to **promoter**) was high, meaning that switching states frequently incurs a substantial **cost**. Therefore, while the emission probabilities might offer slight gains in likelihood, the high cost of transition discourages frequent changes, which is one of the central features of HMMs: avoiding **jittery transitions** between states. Instead, the model ensures **smooth transitions** to allow **nearby positions** to influence the probability of a given state.

To handle the exponential complexity of possible **parses** (since each position could have two possible states, leading to 2n2^n2n combinations for nnn positions), we introduced **dynamic programming** for optimal parsing. Using the **Viterbi algorithm**, we computed the **optimal path** by:

1.  **Setting up a variable V** for each position, representing the maximum score at that position based on the best possible score from the previous position.
2.  The current **maximum score** is computed by choosing the best score from the previous state, factoring in the **transition cost** and **emission probability**.

This approach ensures that we efficiently compute the best path without scoring every possible path. The key is balancing a **high score** in the previous state with a **low transition cost**.

Once we compute the best score for the final state, we can **trace back** the arrows (similar to **dynamic programming alignment**) to reconstruct the entire **optimal parse**, which is the **best interpretation** of the sequence of **hidden states** given the observations.

This process led to the **Viterbi decoding equation**, where the **current maximum** is the **product** of the previous state's maximum score and the transition cost to the current state, ensuring that we find the **best path**.

## [11:47](https://www.youtube.com/watch?v=PJFRz1vrGEI&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=6&t=707s) Posterior decoding, Forward Algorithm

We introduced a new way to approach parsing sequences by focusing on individual **positions** rather than the entire path. In the previous Viterbi method, we found the **best single path** through the sequence. However, this approach might miss important information, since there are an **exponential number of paths** that can explain the sequence, and many of these paths could pass through different **hidden states** at a given position.

For instance, while the best path might pass through an **enhancer** state at position 523, many other high-probability paths could pass through the **promoter** state at that same position. In this case, itâ€™s not enough to focus only on the best path. Instead, we should sum over **all possible paths** that pass through the enhancer and compare them to the sum of all paths that pass through the promoter at position 523. This gives us a better understanding of the likelihood of being in one state versus another at that specific position.

To calculate this, we introduced the concept of **total probability mass** for each state at a given position. This required us to move away from the Viterbi approach of maximizing probabilities and instead to sum all probabilities up to a given point. This process is done using **recursion**: if we know the total probability up to a certain point, we can sum the probabilities at the next position by factoring in **transition** and **emission** probabilities.

This leads us to the **Forward Algorithm**, which calculates the probability mass for each state moving **forward** through the sequence. Once we reach the end of the sequence, we need to do the same process but moving **backwards**, which is accomplished with the **Backward Algorithm**. The Forward Algorithm tells us the total probability mass going up to a point, and the Backward Algorithm gives us the probability mass after a point, working in tandem.

A small adjustment is needed: we donâ€™t want to count the **emission probabilities** twice, so we include them in the Forward Algorithm but exclude them from the Backward Algorithm.

Once weâ€™ve completed these two steps, we can calculate the **posterior probability** of being in a given state at any position. This is known as **Posterior Decoding**, which looks at the **posterior probability** of being in a state after observing the entire sequence. This method doesnâ€™t necessarily give us a valid transition path, but it allows us to determine the most likely state at each individual position.

The key difference between this method and Viterbi is that Posterior Decoding focuses on the **best state at each position**, while Viterbi gives the **best overall path**. This means that Posterior Decoding might produce a sequence of states where transitions are not valid according to the model, but it still reflects the **most likely states** at each position when considering all possible paths.

Does this distinction between Viterbi and Posterior Decoding make sense?

## [18:39](https://www.youtube.com/watch?v=PJFRz1vrGEI&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=6&t=1119s) Learning HMM parameters: Supervised

In a **supervised learning** context, we already have labeled data, meaning we know both the **observations** (the sequence of emitted symbols) and the **hidden states**. With this information, itâ€™s straightforward to estimate both the **emission** and **transition** probabilities for the Hidden Markov Model (HMM).

### Estimating Emission Probabilities

The emission probability describes the likelihood of a state emitting a particular symbol. Given a labeled sequence, we simply count how often a particular symbol is emitted from a particular state and divide it by the total number of emissions from that state.

For example, imagine you have a sequence of symbols like **G, C, A, A, G, C** labeled with states **B, B, B, P, P, B**. If we want to estimate the probability of emitting the symbol "A" from state **P**:

- **Numerator:** Count the number of times **A** is emitted from state **P** (which might be 2 times).
- **Denominator:** Count the total number of emissions from state **P** (which might be 3 times).

Thus, the **emission probability** of **A** from **P** is 23\\frac{2}{3}32â€‹. You repeat this process for all symbols and states to build the full **emission probability matrix**.

### Estimating Transition Probabilities

The **transition probability** is the likelihood of moving from one state to another. For example, if we are in state **B**, how likely is it that we will transition to state **P**?

You can estimate this by counting how many times you observe a transition from **B** to **P** and dividing by the total number of times you are in state **B**. For instance:

- **Numerator:** Count the number of transitions from **B** to **P**.
- **Denominator:** Count the total number of transitions starting from **B**.

For example, if you observed 5 transitions from state **B**, and one of those transitions led to **P**, the **transition probability** from **B** to **P** would be 15\\frac{1}{5}51â€‹.

Similarly, if you were in **P** three times and transitioned to **B** once, the **transition probability** from **P** to **B** would be 13\\frac{1}{3}31â€‹. If you stayed in **P** twice, the **transition probability** from **P** to **P** would be 23\\frac{2}{3}32â€‹.

This is a **maximum likelihood estimation** approach, which works well when thereâ€™s plenty of data.

### Addressing Zero Counts

One challenge in this supervised approach arises when you donâ€™t observe certain transitions or emissions. If you only have a small dataset, some transitions might never occur, leading to **zero probabilities**, which can skew the model. To address this, we introduce **pseudo counts**, which add a small number (like 1) to each count to avoid zeros in the probabilities. This technique smooths the estimates and ensures the model remains robust, even with limited data.

### Summary:

1.  **Emission Probabilities:** Count how often a symbol is emitted from a state and divide by the total number of emissions from that state.
2.  **Transition Probabilities:** Count how often you transition from one state to another and divide by the total number of transitions from that state.
3.  **Pseudo Counts:** Add small values to counts to avoid zero probabilities in small datasets.

## [21:22](https://www.youtube.com/watch?v=PJFRz1vrGEI&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=6&t=1282s) Learning HMM parameters: Unsupervised (Best Path, Viterbi)

When learning HMM parameters without labeled data, the problem becomes significantly more interesting and challenging. In an **unsupervised** setting, we're given sequences but no information about the underlying states. Our task is to infer both the **hidden states** (like promoters, enhancers, repressed regions, etc.) and the **parameters** (the emission and transition probabilities).

### The Basic Approach

1.  **Initial Parameters:** We start with some **initial guess** for the model parameters, including the **transition** and **emission probabilities**. These initial values might be based on general biological assumptions or randomized.
2.  **Infer States:** Using these initial parameters, we apply the **Viterbi algorithm** to find the **best path** (sequence of hidden states) through the given sequence. This allows us to predict which regions are likely promoters, enhancers, etc., based on the sequence and the current model.
3.  **Parameter Updates:** Once we have the predicted sequence of hidden states (the **Viterbi path**), we can now update the **transition** and **emission probabilities** by counting how often different symbols (e.g., nucleotides) are emitted by different hidden states, and how often transitions between hidden states occur.
4.  **Iterate:** With the updated parameters, we run the Viterbi algorithm again to find a **better path** through the sequence. This process is repeated iteratively, improving both the parameters and the inferred path over time, gradually **converging** to a solution where both the parameters and the hidden states are well-estimated.

### Dynamic Interplay Between Parsing and Parameters

**Parsing with Viterbi:** At each step, the Viterbi algorithm identifies the **best path** through the hidden states, based on the current parameters. This path represents the most likely sequence of hidden states that generated the observed sequence.

**Parameter Updates:** After obtaining this best path, we treat it as if it were the **true labeling** and use it to update the model's parameters. For example, if a certain region is inferred as a promoter, we update the emission probabilities for promoters based on the symbols (nucleotides) observed in that region.

**Convergence to Better Annotations.** Initially, the model might not be very accurate, but as it repeatedly alternates between inferring the best hidden state path and refining the parameters, it **converges** to a better solution. Over time, the model learns to annotate the genome with no prior labels by: Identifying **distinct patterns**, like regions with high or low GC content. Learning that certain **sequential dependencies** (e.g., enhancers tend to be near transcribed regions) are more likely than others.

**Comparison to K-means Clustering.** This unsupervised HMM learning is conceptually similar to **K-means clustering**: In K-means, we start with arbitrary cluster centers and iteratively assign points to the nearest center and update the centers. In HMM learning, we start with arbitrary parameters, use them to assign hidden states, and then update the parameters based on these assignments. Both methods involve **iterating between assignment and updating** until convergence.

### Example: Partitioning Genome by GC Content

As an example, imagine the task of clustering the genome into regions of **high GC** and **low GC** content. By starting with an initial guess, the model can progressively refine these regions by:

- Assigning hidden states based on the current parameters (e.g., regions with more GC nucleotides being classified as "high GC").
- Refining the parameters to better reflect the data, such as adjusting the emission probabilities for GC nucleotides in the high GC state.

Over time, the model will find regions that are consistently high or low GC and will update its parameters and state assignments accordingly.

### The Sequential Homogeneity Constraint

One key difference between unsupervised HMM learning and other clustering methods (like K-means) is that **sequential structure matters** in HMMs. The model assumes that certain hidden states are more likely to follow others (e.g., a promoter might be near a transcribed region), which constrains the sequence of state transitions. This constraint is encoded in the **transition matrix**, ensuring that the genome is **parsed** in a way that respects the biological context.

### Iterative Process in Summary

1.  Start with some initial parameters.
2.  Use **Viterbi** to find the best hidden state path.
3.  Use the inferred hidden states to update the parameters.
4.  Repeat until convergence, alternating between finding the best path and refining the parameters.

This iterative back-and-forth between estimating hidden states and updating parameters is key to unsupervised learning in HMMs.

## [27:02](https://www.youtube.com/watch?v=PJFRz1vrGEI&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=6&t=1622s) Learning HMM parameters: Unsupervised (All Paths, Baum-Welch)

The **Baum-Welch algorithm** represents a more sophisticated method for unsupervised learning in Hidden Markov Models (HMMs), extending beyond the limitations of the Viterbi algorithm. While Viterbi focuses on finding a single optimal path through the hidden states, Baum-Welch leverages the **entire distribution of possible paths** to derive more accurate estimates of the HMM parameters, such as transition and emission probabilities.

Baum-Welch operates through an **Expectation-Maximization (EM)** framework. In the **Expectation step (E-step)**, it calculates the total probability across all possible paths through the hidden states, rather than only considering the most likely path. In the **Maximization step (M-step)**, the algorithm updates the HMM parameters based on these probabilities, refining the estimates iteratively.

A key element of this approach is using the **forward-backward algorithm**, which computes the probability of the sequence up to a certain point (forward probability) and from that point onward (backward probability). These two probabilities together give the **posterior probability** of being in a particular state at any given position in the sequence. Baum-Welch thus captures the **probability mass of all possible paths**, rather than just the single best path, making it more comprehensive and accurate.

**In contrast to Viterbi training**, which generates an annotation based on the best path, Baum-Welch performs **posterior decoding**, where the algorithm estimates the most likely state for each position based on the probability mass summed over all paths. This allows for a more nuanced understanding of the sequence, as it accounts for the contribution of many paths that might pass through different states at any given position.

The **core process** of Baum-Welch involves:

1.  **Initial parameters**: Starting with some guesses for the transition and emission probabilities.
2.  **Forward-backward calculation**: Using the forward algorithm to compute the total probability mass up to each point and the backward algorithm to compute the total mass from that point forward.
3.  **Parameter updates**: Summing over all possible paths to determine the expected number of transitions and emissions, updating the HMM parameters accordingly.

For example, instead of simply counting how many times a particular state emits a symbol in a single best path, Baum-Welch considers the **weighted contributions** of all paths that could emit that symbol from that state, providing a more accurate estimate of the emission probabilities. Similarly, it accounts for **all transitions** between states, weighted by the probabilities of the paths that make those transitions.

Ultimately, **Baum-Welch training** converges on a set of transition and emission probabilities that best explain the observed data, given all the possible paths the HMM might follow. This approach contrasts with the **supervised learning scenario**, where labeled data simplifies the task of counting transitions and emissions directly. In Baum-Welch, however, the lack of labeled data necessitates this iterative approach of refining both the path estimates and the model parameters over time.

In summary, Baum-Welch allows us to handle **unsupervised learning** of HMMs in a more robust and statistically grounded way, accounting for the full range of possibilities inherent in the data, rather than relying on a single optimal interpretation. This method significantly enhances the ability of HMMs to capture the complexity of real-world biological sequences, making it a powerful tool in fields like **epigenomics** and **gene regulation** analysis.

## [31:45](https://www.youtube.com/watch?v=PJFRz1vrGEI&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=6&t=1905s) Chromatin State Characterization

Once weâ€™ve developed the capabilities to analyze chromatin states, we can essentially unleash the model on the human genome to explore its architecture. The model identifies patterns, such as regions with **higher GC content**, and we then ask: **What are these regions?** Through enrichment analysis, we can check if these regions overlap with known genomic elements, such as **repeat elements**, **enhancers**, **transcription start sites**, and **exons**. For example, if we find that these regions are enriched around transcription start sites, we may hypothesize that the identified hidden state represents a **promoter**.

This process involves **annotating the genome** by dividing it into a set of distinct states based on their epigenomic signatures. Each state represents a combination of chromatin marks, and by examining the enrichment of these states in different genomic regions, we can give meaningful labels to them, such as **promoter**, **transcribed**, **enhancer**, or **repressed** states.

#### Model Output and Genome Parsing

For example, after partitioning the genome into 50 chromatin states, we may find that certain states are consistently associated with **gene start sites**, others with **gene body regions**, and others with **repressed regions**. This allows us to start interpreting the roles of these chromatin states in gene regulation. A key discovery is that some states appear in regions near active genes, while others occur in **intergenic** or **repressed** regions.

The model also helps us understand the genomeâ€™s overall structure. A large portion of the genome may fall into what we might call â€œboringâ€ states, representing regions where chromatin activity is low or uniform. In contrast, smaller portions of the genome, where **active chromatin marks** are concentrated, may be more **biologically interesting**. For example, the model might show intense activity in **gene-dense regions** and little activity in **centromeric** or **heterochromatic regions**. The model may even reveal differences between **chromosomal territories**, such as the **A compartment** (associated with active chromatin) and the **B compartment** (associated with repressed chromatin, often located at the **nuclear periphery**).

#### Assigning Functional Labels to Chromatin States

To assign meaningful labels to the chromatin states discovered by the model, we examine their enrichment for known genomic features. For instance:

- **Promoter states** are strongly enriched around transcription start sites.
- **Repressed states** may show strong enrichment for **nuclear lamina** association, reflecting their inactive nature.
- **Repeat states** may be enriched in **repetitive elements** such as **LINEs** or **SINEs**.
- **Transcribed states** show enrichment in gene bodies, corresponding to active gene transcription.

This analysis allows us to systematically annotate the genome based on epigenomic features, moving from a purely **data-driven model** to one that is **biologically interpretable**. For example, we may find that certain states are enriched near **developmental enhancers** or regions marked by **long non-coding RNAs**.

#### Discovering New Functional Elements

Through this process, we can also uncover previously unknown elements in the genome. For instance, we may identify **new protein-coding genes**, **developmental enhancers**, or regions corresponding to **long intergenic non-coding RNAs (lincRNAs)**, which may have critical regulatory roles despite being non-coding. These discoveries are made possible by combining epigenomic signatures with **functional enrichment analyses**.

#### Relevance to Disease: Genome-Wide Association Studies (GWAS)

Perhaps one of the most significant applications of this chromatin state analysis is in understanding **disease-associated non-coding regions**. Initial genome-wide association studies (GWAS) revealed that only a small percentage (around 7%) of disease-associated variants are found within protein-coding regions. The majority are located in **non-coding regions**, previously termed **â€œdark matterâ€** of the genome. By characterizing chromatin states, we now have a powerful tool to shine a light on these non-coding regions. We can identify that many of these disease-associated variants are located in **enhancer regions**, providing a new understanding of their regulatory roles in disease.

Thus, chromatin state annotation allows us to map the non-coding genome in a way that directly links genetic variation to gene regulation and disease mechanisms, transforming our understanding of the genome's regulatory architecture.

## [43:26](https://www.youtube.com/watch?v=PJFRz1vrGEI&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=6&t=2606s) Model complexity: selecting the number of states/marks

When addressing **model complexity** in Hidden Markov Models (HMMs) and deciding on the number of states or marks, it's crucial to determine an appropriate balance between model simplicity and detail. The question arises: how many states are sufficient to capture the biological complexity without overfitting or introducing unnecessary redundancy?

One approach is to assess whether increasing the number of states improves the model's ability to capture **mark dependencies**. For example, as you add more states (e.g., moving from 10 to 50 or 100), you can analyze the **occurrence frequency of pairs of marks** within a state. As the number of states increases, the **deviation from expectation decreases**. This indicates that, with a sufficient number of states, the model can capture more complex dependencies between marks. When using fewer states, the model tends to only capture **mark-independent effects**.

Another method to determine the optimal number of states is through **nested initialization**. This technique avoids fixing the number of states from the start. Instead, you start with a larger number of states (say 80) and then **prune redundant states** after training. This approach allows the model to initially explore more states, increasing the chance of discovering important but rare states that may not appear in a smaller model. Once the model is trained, you can remove states that are redundant or less informative, refining the model down to the most meaningful states.

This approach offers several advantages. For instance, if you randomly initialize the model with a specific number of states (e.g., 50), it might capture the same state multiple times due to random fluctuations, missing important ones. By starting with a higher number of states and then pruning, the model can discover rare states and avoid redundancies. This is analogous to running a clustering algorithm multiple times and selecting the most consistent clusters across runs.

**Nested initialization** further ensures that **once a state is discovered**, it remains part of the model, even as you reduce the number of states. This robustness makes the model less sensitive to random fluctuations in initialization. For example, you might only start consistently recovering a particular state after reaching seven states, but once recovered, it remains stable even as you reduce the total number of states.

In biological interpretation, the model first operates in an **unbiased manner**. The interpretation of each state comes after the model is fully pruned and refined. At this stage, biological meaning is assigned to the states based on their observed characteristics. However, there's a risk of **overfitting** to known biological stories. For instance, if a particular state isn't recovered until much later in the process (e.g., after discovering 75 states), it might be disregarded. This could mean missing an important biological feature simply because it wasnâ€™t obvious at the start.

In summary, selecting the number of states in HMMs involves balancing model complexity with interpretability. Techniques like **nested initialization** allow for a more exploratory and refined approach, discovering rare and informative states while avoiding redundancy. However, care must be taken not to overfit the model based on current biological knowledge, as previously overlooked states may hold significant value with further data or insights.

## [49:50](https://www.youtube.com/watch?v=PJFRz1vrGEI&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=6&t=2990s) Learning chromatin states jointly across multiple cell types

When you have data from **multiple cell types**, it's possible to learn chromatin states not just for individual types but jointly across them, allowing for more powerful insights into the dynamic behavior of gene regulation. For example, consider a scenario where you have various cell types like **human vein endothelial cells, keratinocytes, fibroblasts, and embryonic stem cells**, and you're able to profile chromatin marks across each of them. The challenge becomes how to model these multiple cell types together.

There are several strategies you can adopt. One approach is to treat all the data from different cell types as one large dataset. This is the **stacking approach**, where you stack all the chromatin marks from different cell types together, learning the chromatin states from this collective set. This allows you to capture chromatin states that may only appear in specific cell types, helping to identify **cell-type-specific enhancers** or **promoters**.

Alternatively, you can use a **concatenation approach**, where instead of stacking, you concatenate the data across all chromosomes for each cell type. This method treats each cell typeâ€™s chromosomal data as a continuous genome, learning the same chromatin states for each cell type but with different dynamic locations. The advantage of this method is that it forces the model to use a common set of chromatin state definitions across cell types, making it easier to compare and track chromatin state changes between cell types.

A third strategy is to learn **independent models** for each cell type and then **cluster the emission matrices** to find common patterns across different types. This allows for a more granular view of how certain chromatin states are shared or unique between cell types. For example, you might discover that certain chromatin states (like promoter or enhancer states) are found consistently across many cell types, while others may only appear in specific tissues.

Once the chromatin states are learned, you can observe **dynamic transitions** in chromatin states across cell types. For example, a gene might be in a **poised state** in embryonic stem cells, showing both repressive and activating marks, but then shift to an **active state** in differentiated cell types. These dynamic shifts help in understanding how genes are regulated during development and differentiation.

### Handling Missing Data and Imputation

A common issue when profiling multiple cell types is that certain marks might be missing from some cell types due to technical limitations or failed experiments. In these cases, one approach is to **impute missing marks** by using the information from other marks that are present in the same cell type. This imputation can be incredibly useful, especially when you are dealing with rare cell types or samples that cannot be easily replicated. Instead of discarding incomplete datasets, imputation allows for the recovery of potentially valuable data and enables a more complete model of chromatin state dynamics.

## [58:20](https://www.youtube.com/watch?v=PJFRz1vrGEI&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=6&t=3500s) Three ways of linking enhancers to target genes

Once you have learned chromatin states across multiple cell types, the next step is to start linking **non-coding regions** (like enhancers) to their **target genes**. One method of linking is based on **correlation**. By observing when enhancers become active in certain cell types and correlating that with the activity of nearby genes, you can make functional inferences about which enhancers regulate which genes.

Another method is **genetics-based linking**, using **expression quantitative trait loci (eQTLs)**. eQTLs are genetic variants that affect gene expression. By studying how different genetic variants (e.g., single-nucleotide polymorphisms) influence gene expression, you can link genetic differences in non-coding regions to changes in the expression of specific genes. This is a powerful approach, as it uses both genetic and expression data to make connections between enhancers and target genes, often revealing previously unknown regulatory relationships.

Both of these methodsâ€”**correlation-based** and **genetics-based linking**â€”allow for a more comprehensive understanding of how **non-coding genetic variation** impacts gene regulation and ultimately contributes to different phenotypes, including disease states.

## [1:00:50](https://www.youtube.com/watch?v=PJFRz1vrGEI&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=6&t=3650s) Three-dimensional Genome, Chromatin Conformation Capture, Hi-C

The third method for linking enhancers to their target genes is based on **physical interactions** within the **three-dimensional structure of the genome**. This is where techniques like **Chromatin Conformation Capture** (Hi-C) come into play.

To visualize this, imagine looking at regions of the genome, such as the region around the **FTO gene**, which is linked to obesity. Through Hi-C, we can observe **long-range physical interactions** between the FTO gene and other distant genes, such as **IRX3** and **IRX5**. These interactions indicate that certain genomic regions, though distant in terms of linear sequence, may fold and loop in three-dimensional space to come into close proximity.

#### The Concept of Chromatin Conformation Capture

Imagine taking a bowl of spaghetti (representing the genome), and you want to know which strands of spaghetti (or regions of DNA) are physically near each other. In the same way, chromatin is compacted in the cell nucleus, and different regions of the genome may come into contact as the DNA folds. To capture these interactions, you start by **fixing** the DNA in place using a chemical fixation agent, which essentially freezes the spatial organization of the genome.

Next, you **chop** the genome into smaller segments and allow these fragments to randomly rejoin. Most often, these segments will rejoin with nearby regions, forming loops and re-ligations. However, some of these fragments will reconnect with more **distant regions** in the genome, because those distant regions were physically close due to the three-dimensional folding of the DNA. These distant re-ligations create **off-diagonal dots** in Hi-C interaction maps, representing long-range interactions between different genomic regions.

#### Hi-C and Chromatin Territories

Hi-C is a powerful technique that allows us to investigate the **spatial organization of the genome** within the nucleus. Inside the nucleus, chromosomes do not just float randomly. Instead, they occupy distinct **chromosomal territories**. Using Hi-C, we can identify these territories and observe how chromosomes are arranged relative to each other. By staining chromosomes with different colors (through combinatorial labeling), it becomes clear that **chromosomes occupy distinct, non-overlapping domains** within the nucleus.

Hi-C begins with **3C** (Chromosome Conformation Capture), evolves through **5C** (Carbon Copy Chromosome Conformation Capture), and culminates in **Hi-C**, which adds a biotin label to every cut and religation event, making it easier to pull down and sequence these regions. This technique allows for a **comprehensive view of the three-dimensional genome architecture** by mapping interactions between all regions of the genome.

#### Understanding Chromosome Interaction Maps

When the Hi-C data is plotted, you can see a **checkerboard pattern**. This pattern shows that different regions of the genome tend to interact with one another in a structured manner. The diagonal of the matrix represents interactions within close proximity (cis-interactions), while off-diagonal elements indicate long-range interactions (trans-interactions). Through this analysis, two main classes of chromatin emerge:

1.  **Gene-rich regions**: These regions tend to cluster together and are often found in the **middle of the nucleus**.
2.  **Gene-poor regions**: These regions are more likely to be located near the **nuclear periphery**, often associated with the **nuclear lamina**.

This insight reveals a spatial segregation between **active** and **repressed chromatin domains**.

#### Loop Extrusion and Topologically Associated Domains (TADs)

A key discovery from Hi-C is the identification of **Topologically Associated Domains (TADs)**, regions of the genome that interact more frequently within themselves than with other regions. These domains are formed by mechanisms such as **loop extrusion**, where **CTCF binding proteins** and **cohesin** create loops in the chromatin, bringing distant regulatory elements and genes into close proximity. This loop extrusion process helps to define boundaries between active and repressive chromatin regions, allowing for **spatial organization** of gene regulation.

Overall, Hi-C and chromatin conformation capture techniques provide a crucial tool for studying the **three-dimensional architecture of the genome** and for understanding how spatial interactions influence gene regulation. These methods allow us to map how the genome folds and loops to bring **regulatory elements**, such as enhancers, into physical proximity with their **target genes**, providing deeper insight into **gene expression** and **disease mechanisms**.

## [1:08:50](https://www.youtube.com/watch?v=PJFRz1vrGEI&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=6&t=4130s) Linking Enhancers to Function, Motifs, Upstream Regulators

We can now **link non-coding regions** like enhancers to their **target genes** using various methods, including correlated activity, 3D genome structure, and genetic associations. For instance, by **unbiased clustering** of **2.3 million genomic regions** based on their enhancer activity across **127 epigenomes**, we can organize these regions into **modules**. These modules consist of enhancers that show similar activity patterns across different cell types.

Each genomic region that lights up as an enhancer in a given cell type can be represented as a **vector** of activity. This vector is 127 cell types long, indicating how **enhancer-like** that element is across all 127 types. By clustering these vectors, we can identify **enhancer modules** that are specific to certain cell types or show more generalized activity. For instance, some modules are highly **cell type-specific**, while others are active across a range of cell types, such as in **T-cells** or **embryonic stem cells**. These modules can also be linked to **specific functions**, such as neuronal development, immune response, or heart function, based on the nearby genes.

Once these modules are identified, we can investigate the **genes nearby**. By clustering the enhancers and identifying the genes close to them, we can see whether these genes share **common functions**. For example, a group of enhancers active in **embryonic stem cells** and the **brain** may be enriched for **neuronal development genes**, while enhancers active in **T-cells** and **B-cells** might be enriched for **immune-related genes**.

### Motif Enrichment and Upstream Regulators

A key question is whether these enhancers turn on **randomly** or if they share common **regulatory motifs** that drive their activity. By analyzing the **motif enrichments** of these enhancer modules, we can identify the **regulators** that bind to these motifs. These regulators might be transcription factors that are **expressed** in the same cell types where the enhancers are active. This allows us to link **enhancers** with **upstream regulators** and identify how gene regulation occurs across the genome.

For example, we can study the **motif enrichments** within enhancer modules to see which transcription factors are likely to be binding to these regions. Then, by linking this information with gene expression data, we can determine whether the corresponding **regulators** are expressed in the relevant cell types. This provides a powerful tool to connect **enhancer activity**, **regulatory motifs**, and **gene expression**.

### Correlating Enhancers and Gene Expression

We can also study the **correlation** between **enhancer activity** and **gene expression** directly. By analyzing enhancer marks such as **H3K27 acetylation** (a mark of active enhancers) and comparing it to gene expression data, we can predict which genes are regulated by which enhancers. For instance, if an enhancer's activity is strongly correlated with the expression of a nearby gene, we can hypothesize that the enhancer is regulating that gene.

By systematically analyzing the **enhancer-gene links** across the genome, we can start building a **regulatory map** that connects enhancers to their **target genes** and identifies the **regulatory motifs** and **transcription factors** that control these processes. This integration of chromatin state, motif analysis, and gene expression data allows us to uncover the **regulatory circuits** governing gene expression in different cell types and contexts.

## [1:14:30](https://www.youtube.com/watch?v=PJFRz1vrGEI&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=6&t=4470s) Distinguishing Upstream Activator vs. Repressor TFs

We can uncover a **three-way correlation** between the **activation of an enhancer region**, the **enrichment of corresponding motifs**, and the **expression of the associated regulator**. This enables us to distinguish **activators** from **repressors** among transcription factors (TFs).

For each **module of enhancers**, which might be active in different cell types, such as stem cells, immune cells, or hepatic cells, we can ask: What is the **enrichment** (red) or **depletion** (blue) of a specific **motif** in those regions? A **depletion** of a motif might indicate that a **repressor** TF binds to that motif and prevents the region from becoming active. Thus, when the motif is absent, the enhancer is **active**, implying that the absence of the repressor allows the enhancer to turn on.

We can use this information to identify **activators** and **repressors**. For example:

- **Activators** are identified when a motif is **enriched**, and the associated factor is **expressed**, leading to enhancer activity.
- **Repressors** are identified when the motif is **depleted**, and the factor is expressed, or conversely, when the motif is **enriched**, but the factor is **not expressed**.

For instance:

- **OCT4** and **RFX** appear as **activators** in **embryonic stem cells**.
- **GATA1**, **SPI1**, and **STAT** factors act as **activators** in **immune cells**.
- **GFI1** functions as a **repressor** in immune cells.

### Building Regulatory Networks

This insight allows us to **build regulatory networks**, linking enhancer modules to their transcription factors. By identifying motifs associated with specific enhancers, and correlating them with the activity of corresponding TFs, we can infer how **activators** and **repressors** control gene expression across different cell types. For example, in immune cells, **ETS1** and **SPI1** (also known as PU.1) activate immune-specific enhancers, while **GFI1** acts as a repressor.

### High-Resolution Motif Localization

We can visualize how transcription factor binding motifs are distributed around specific genomic features, like the **transcription start site** (TSS), and how chromatin states differ around active motifs. For example, the **HNF4** motif (hepatocyte nuclear factor 4) in **hepatocytes** (liver cells) is surrounded by a strong **enhancer state** in hepatic cells, and the **repressed chromatin state** is depleted around this motif. This provides a **high-resolution map** of regulatory motifs and their surrounding chromatin context.

### Functional Impact of Motif Changes

By conducting experiments like **luciferase assays**, we can validate the functional significance of specific motifs. For example, altering a single base pair in the **HNF4 motif** results in a significant reduction in gene expression, demonstrating the critical role of specific motifs in enhancer function. While motifs don't act in isolation, changing one can dramatically affect gene regulation in the context of other nearby motifs.

This systematic approach allows us to integrate **motif enrichment**, **chromatin state data**, and **gene expression** to understand the complex regulatory networks controlling gene expression across different cell types and biological contexts.

## [1:20:10](https://www.youtube.com/watch?v=PJFRz1vrGEI&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=6&t=4810s) Summary

In todayâ€™s lecture, we explored the **dynamics of the epigenome** and discussed approaches for **joint chromatin state learning** across multiple cell types. We delved into **hidden Markov models (HMMs)**, examining both **supervised** and **unsupervised learning** methods for modeling chromatin states. In the supervised approach, we simply **count** transitions and emissions, while in the unsupervised method, we first **infer** hidden states and then update our model parameters iteratively. We explored the two unsupervised techniques: **Viterbi decoding**, which relies on the **best path**, and **Baum-Welch**, which sums over **all possible paths**.

We also covered the process of **annotating chromatin states**, where we assign meaningful biological labels to states based on **enrichments** for known genomic features, such as promoters, enhancers, and repetitive elements. We discussed **model complexity** and how increasing the number of states captures **pairwise dependencies** between chromatin marks. This led to the concept of **nested initialization**, where models are built with a larger number of states and later **pruned** to remove redundant or less informative states, resulting in a more **robust model**.

Next, we covered three different ways to learn chromatin states **jointly across multiple cell types**:

1.  **Stacking** the chromatin marks for each cell type.
2.  **Concatenating** the genomes from different cell types.
3.  Learning **independently** in each cell type and later aligning the states across cell types.

We then examined how we can **link regulatory elements** like enhancers to their target genes using three strategies:

1.  **Correlated activity** between enhancers and nearby genes.
2.  **Genetic information** (e.g., expression quantitative trait loci or eQTLs).
3.  **Physical proximity** revealed through **chromatin conformation capture** techniques, such as **Hi-C**, which allows us to understand **three-dimensional genome architecture** by analyzing regions of the genome that physically interact.

Lastly, we discussed how to identify **activators** and **repressors** by examining the correlation between enhancer activity, the **motifs** present or absent within enhancer regions, and the **expression** of the transcription factors that bind those motifs. This allowed us to **map regulatory networks** and infer how transcription factors control gene expression across different cell types.

We'll continue exploring the **theme of networks** in the next lecture, which will further expand on how these regulatory circuits form complex biological networks.
