---
tags:
  - "topic"
topics:
  - "MLCB"
status: updated
created: 2026-05-24
updated: 2026-05-24
sources:
  - "Raw/Sources/lecture_04_alignment.md"
source_count: 1
aliases:
  - "Lecture 4 - Alignment"
---

# Lecture 4 - Alignment

## Source
- Raw source: `Raw/Sources/lecture_04_alignment.md`
- Supporting source: `Raw/Files/lecture_04_alignment.md`
- Existing related pages: [[mlcb-2024-computational-biology]], [[mlcb-complete-study-guide]], [[mlcb-methods-map]]
- Last updated: 2026-05-24

## Executive Summary
Lecture 4 - Alignment develops comparative genomics, mutation/insertion/deletion models, dynamic programming, traceback, local alignment, BLAST, PSI-BLAST, and PSSMs. This page intentionally preserves substantial source detail so a future LLM can reason from the wiki without immediately reopening the raw transcript.

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
- Intro: Aligning Sequential Datasets/Models
- Comparative Genomics & Evolution
- Computation Re-use, Dynamic Programming
- Dynamic Programming Principles and Fibonacci
- Alignment Matrix, Paths, Traceback, 2^N-vs-N^2
- Local Alignment, Linear-Time, Linear Space
- Hashing, BLAST, Inexact Matching, and PSI-BLAST

## Detailed Lecture Notes
The notes below preserve the processed source order and are intentionally detailed.

# [[Lecture 4 - Alignment]]

Video: [Lecture04 - Sequence Alignment - MLCB24](https://www.youtube.com/watch?v=3Fz1wNpFFnw&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=5)

Slides: [Lecture04_DynamicProgramming-BLAST.pdf](https://www.dropbox.com/scl/fi/ygjpn5h34etupzv9ha327/Lecture04_DynamicProgramming-BLAST.pdf?rlkey=nrhrxgta76m7jfkc143fz30fb&dl=0)

## [0:00](https://www.youtube.com/watch?v=3Fz1wNpFFnw&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=4&t=0s) Intro: Aligning Sequential Datasets/Models

Welcome to today's lecture on **sequential pattern matching**, where we'll explore how to align sequences of data across various domains. Whether itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s aligning a string of actions, sequences of text, or matching gene sequences between genomes, the core problem is the same: how do we compare and align **sequential data**?

We encounter this challenge in many contexts:

- **Language translation:** Aligning text in one language with its counterpart in another.
- **Comparative genomics:** Matching genes across different genomes to understand evolutionary relationships.
- **Model states over time:** Aligning states of a model that represents the world across different time points.

The techniques we'll discuss are foundational in computation and broadly applicable across biology and beyond. WeÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll begin with **sequence alignment** as the basis for these techniques, focusing on **dynamic programming**, a key computational strategy that breaks down larger problems into manageable subproblems and efficiently combines them.

We will explore:

1.  **Comparative Genomics and Evolution:** How these foundational techniques apply to evolutionary biology, using sequence alignment to study genetic conservation and mutation across species.
2.  **Dynamic Programming Concepts:** WeÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll start with a simple exampleÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âcomputing Fibonacci numbersÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âto introduce how dynamic programming reuses computations, reducing redundant calculations. This principle extends directly to sequence alignment.
3.  **Sequence Alignment with Dynamic Programming:** By building an alignment matrix, we can compare sequences by aligning prefixes of two sequences step-by-step. WeÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll use this matrix to efficiently construct the optimal alignment path, drastically reducing the runtime from exponential to quadratic.
4.  **Advanced Alignment Techniques:** We will explore local alignment, linear time alignment, and linear space alignment, building on our understanding of sequence alignment and dynamic programming.
5.  **Hashing for Rapid Lookup:** Beyond dynamic programming, weÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll introduce hashingÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âencoding sequential patterns into unique codes for rapid search. This concept extends to content-based search, where the goal is to find similar documents not by title or keywords but by their actual content, using techniques like latent embeddings and context-sensitive hashing.
6.  **Probabilistic Algorithms and Expected Runtime:** WeÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll delve into the probabilistic foundations of these algorithms, culminating in the BLAST (Basic Local Alignment and Search Tool) algorithm, a highly efficient method widely used in genomics with tens of thousands of citations.
7.  **Sequential Data Models:** WeÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll explore the broader family of models used to handle sequential data, including Hidden Markov Models, Gaussian Mixture Models, and neural network architectures like Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) networks.
8.  **Transformers:** WeÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll discuss how Transformers have revolutionized sequence modeling with explicit positional encoding, allowing the model to maintain context over time without the traditional limitations of RNNs.

Understanding these models requires a grasp of how they handle **contextual information** and **time series data**, managing memory across sequences to preserve or forget information as needed. This sets the stage for exploring Transformers, which leverage sophisticated mechanisms to understand relationships across data points in a sequence.

WeÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll begin with **comparative genomics** and use the lens of evolution to explore genomes, setting the groundwork for understanding how sequential data can be aligned and interpreted in various applications.

## [9:31](https://www.youtube.com/watch?v=3Fz1wNpFFnw&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=4&t=571s) Comparative Genomics & Evolution

Comparative genomics is central to understanding the diversity of life on Earth. It allows us to compare genomes across different species, tracing back to their common ancestors. This field opens a window into the evolutionary processes that shaped the vast array of life forms we see today.

Consider the interconnectedness of all life: the wood of the desk you sit at comes from trees, our distant cousins; the viruses and bacteria we fight every day are also part of our extended evolutionary family; even the fungi growing in damp places, like the gym locker room, share a common lineage with us. Every life form on this planet is part of a continuous, unbroken chain of existence stretching back over **three billion years**.

**Comparative genomics** enables us to compare these life forms by aligning their genomes, shedding light on how species have diverged from one another over time. This comparison is not just about observing genetic differences but understanding the evolutionary forces that led to the emergence of new species. It also allows us to appreciate the vast tapestry of life on Earth, which, while beautiful, is also marked by the **brutality of natural selection**. Species often go extinct, either due to competition that eliminates their niche or catastrophic events like asteroid impacts that reset the evolutionary stage.

**Genome alignment** is the process of mapping chunks of DNA from one species to corresponding sequences in another. This approach is similar to aligning a series of frames in a movie with a corresponding textual description or translating text between languages. In evolutionary alignment, we take sequences from different species that descended from a common ancestor and infer the sequence of events that led to their divergence.

Through genome-wide alignments, comparative genomics helps us identify **functional elements** in the genomeÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âregions that are preserved across species due to their biological importance. For example, when comparing the genomes of humans, dogs, mice, rats, chickens, and fish, we observe that some regions are highly conserved, indicating their crucial role in cellular functions. These regions often correspond to **protein-coding exons**, the parts of genes that encode proteins.

Interestingly, conservation is not limited to protein-coding regions. Some conserved regions fall between exons and are not annotated as coding. These non-coding regions, often overlooked, may have critical regulatory functions. For example, between exons 5 and 6 of the DBH gene, there is a conserved block that is not part of the protein-coding sequence. This raises the question: what role does this conserved, non-coding sequence play?

The conservation pattern suggests that these regions are under strong **purifying selection**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âevolutionary pressure to maintain their sequence integrity. Some conserved elements may have evolved relatively recently, becoming important after diverging from common ancestors, such as chickens or fish. Evolution is not a static perfection from 3.5 billion years ago; it is a dynamic process full of **mutations and adaptations** that sometimes lead to beneficial changes.

One intriguing possibility is that conserved non-coding regions function as **regulatory elements**, controlling when and where specific genes are expressed. Only about **1.5% of the human genome** encodes proteins, yet estimates suggest that **7% to 20%** of the genome is under some form of selection, indicating potential functionality. Moreover, a vast majority of disease-causing mutationsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âaround **93%**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âare found in non-coding regions, further emphasizing the importance of these sequences.

Non-coding regions may play roles that are critical yet not fully understood. They could be mistakenly annotated as non-coding, or they might function in ways that are more subtle and complex than simply encoding proteins. Misannotations can happen, as scientists work tirelessly to refine the genomeÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s reference annotations, uncovering new exons and even new genes that were previously missed.

As we map genomes meticulously, aligning each nucleotide across species, we uncover **islands of perfect conservation**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âsmall stretches of DNA that have remained unchanged for millions of years. These sequences often correspond to **regulatory motifs**, such as binding sites for transcription factors that control gene expression. For instance, in yeast, conserved sequences correspond to sites where regulators of glucose and galactose metabolism bind, controlling how the organism adapts to its environment.

By reading the book of evolution, we can infer the **functional elements** of genomes. Each conserved sequence tells a story of selection, adaptation, and survival, offering insights into the fundamental workings of life. As we continue to align sequences and refine our understanding, comparative genomics will remain a cornerstone of modern biology, guiding us through the complex relationships that define the living world.

## [29:01](https://www.youtube.com/watch?v=3Fz1wNpFFnw&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=4&t=1741s) Computation Re-use, Dynamic Programming

To align genomic sequences effectively, we need to model the evolutionary process that has shaped them. This involves defining a set of basic operationsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âmutations, insertions, and deletionsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthat describe how one sequence can be transformed into another. By simulating these evolutionary operations, we can work backward to infer the most likely sequence of events that led to the observed genetic differences.

The first evolutionary operation is **mutation**, where one letter is changed into another. This happens because the DNA polymerase, while highly accurate, is not infallible. As it replicates DNA during cell division, it occasionally makes mistakes, like a medieval monk painstakingly copying ancient manuscripts and sometimes miswriting a letter. Similarly, **deletions** occur when the polymerase skips over a nucleotide, failing to copy it. **Insertions** happen when the polymerase adds an extra nucleotide, perhaps losing track due to repetitive sequences, like a long string of identical bases (e.g., ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œAAAAAAÃƒÂ¢Ã¢â€šÂ¬Ã‚Â) that can cause slippage.

To understand the evolution of sequences, we simulate this forward process of mutations, insertions, and deletions to see how one sequence can evolve into another. The inverse processÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âinferring how two sequences have divergedÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âis the challenge we tackle with **sequence alignment**. We formalize the problem computationally by defining these evolutionary operations and establishing an **optimality criterion**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âa way to evaluate the best alignment.

For instance, when aligning the genomes of human and mouse, which diverged around 60 million years ago, we want to find the minimum number of operations needed to transform one genome into the other. This requires a reversible model that can infer the likely sequence of events from a common ancestor, accounting for both the forward and backward evolutionary paths.

To refine our model, we introduce the concept of **costs** associated with each operation. Not all evolutionary changes are equally likely; thus, each operation has a different cost based on its frequency in nature. For example, mutations might be more common and therefore cheaper than insertions or deletions. We assign these costs using a **probabilistic interpretation**: rarer events have higher costs, computed as the negative logarithm of their probability, making rare events like large deletions more costly than common point mutations.

With our cost model defined, the next step is to develop an algorithm that finds the optimal alignment between two sequences. We seek a balance between biological relevance and computational feasibility. On one hand, we want our model to capture the nuances of real evolutionary processes; on the other, we need algorithms that are efficient and manageable.

One way to simplify the alignment problem is to look for the **longest common substring** between two sequences, which involves finding the longest matching sequence without allowing insertions or deletions. For example, given two sequences, we might find "TCA" as a matching substring. To find such substrings, we can fix one sequence and slide the other across it, checking for matches. The computational cost of this approach is relatively high, but manageable compared to the exponential possibilities of general alignments.

However, real biological sequences often have insertions and deletions, so we expand our approach to find the **longest common subsequence**, allowing gaps in the alignment. For instance, if the sequences are ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œAAGTÃƒÂ¢Ã¢â€šÂ¬Ã‚Â and ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œTCA,ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â the longest common subsequence might include alignments like ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œAAG-TC-A,ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â reflecting possible evolutionary operations such as insertions, deletions, and mutations.

Finally, the challenge extends to assigning appropriate penalties for specific substitutions, which reflect the structural similarity between nucleotides or amino acids. For instance, purines (A and G) are often substituted for each other more frequently than purines are substituted for pyrimidines (C and T), reflecting their structural similarities. These substitution patterns are encoded in **scoring matrices** that help determine the most plausible evolutionary paths between sequences, integrating both mutation frequency and the structural context.

Dynamic programming is the key to efficiently searching through the vast space of possible alignments. Instead of evaluating each potential alignment individually, which would take exponential time, dynamic programming breaks the problem into manageable subproblems, reusing previously computed solutions to build up the overall alignment in polynomial time. This approach transforms what would be a computationally intractable problem into one that can be solved systematically, revealing the evolutionary history encoded within the genomes.

## [46:53](https://www.youtube.com/watch?v=3Fz1wNpFFnw&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=4&t=2813s) Dynamic Programming Principles and Fibonacci

Dynamic programming is a powerful technique that transforms **exponential runtimes into polynomial runtimes** by avoiding repeated work. It achieves this by storing and reusing previously computed results. To illustrate this concept, we start with a classic example: calculating Fibonacci numbers.

**Fibonacci numbers** are a sequence found abundantly in nature, such as in the growth patterns of shells, the arrangement of leaves on a stem, and the spirals of sunflowers. The sequence begins with 1, 1, and each subsequent number is the sum of the previous two: 1,1,2,3,5,8,13,21,1, 1, 2, 3, 5, 8, 13, 21,1,1,2,3,5,8,13,21, and so forth. This recursive pattern reflects a natural process of growth where each stage builds upon the sum of the two preceding stages.

To compute Fibonacci numbers, we can define them recursively in a simple Python function:

**def fibonacci(n):**

if n == 1 or n == 2:

return 1

else:

return fibonacci(n - 1) + fibonacci(n - 2)

This recursive approach, while straightforward, is highly inefficient. When you call fibonacci(6), it triggers calls to fibonacci(5) and fibonacci(4), and each of those calls trigger further calls. This creates a tree of function calls, where the same Fibonacci calculations are repeated multiple times, particularly for lower values like fibonacci(2) and fibonacci(3). The number of operations doubles with each incremental step, leading to an **exponential growth in computation**.

The recursive approach illustrates the inefficiency inherent in top-down computation: each subproblem is recalculated many times, leading to an enormous waste of computational resources.

**Dynamic Programming: Bottom-Up Approach**

To avoid this inefficiency, dynamic programming employs a **bottom-up approach**. Instead of starting at the top and working down, you start at the bottom and build up. When asked to compute fibonacci(100), you donÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t just compute that valueÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âyou compute all Fibonacci numbers from 0 to 100, storing each in a table along the way. This approach ensures that every time you need a Fibonacci value, itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s already available in the table, eliminating the need to recompute it.

HereÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s how the bottom-up method works: you start by initializing the first two values, 1,11, 11,1. From there, you compute each subsequent value by summing the two preceding values and storing the result in the table. When you need fibonacci(100), you simply look it up in the tableÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂitÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s already been computed.

This approach drastically reduces the time complexity. Instead of recalculating fibonacci(2) multiple times, you calculate it once, and then **reuse it** every time itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s needed. The time complexity drops from exponential to linear, making it much faster.

**Key Principles of Dynamic Programming**

1.  **Identifying Subproblems**: Dynamic programming reveals identical subproblems within the larger problem. By identifying these subproblems, you can solve each only once.
2.  **Ordering Computation**: Computation is ordered systematically so that when a subproblemÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s result is needed, it has already been computed and stored.
3.  **Table Filling**: Results are stored in a table, allowing for constant-time lookup instead of recalculating values.
4.  **Bottom-Up Approach**: Larger problems are expressed in terms of their smaller subproblems, ensuring that each subproblem is solved once and only once.

The **top-down recursive approach** is slow because the results of small subproblems arenÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t savedÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂtheyÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢re recomputed each time theyÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢re needed. In contrast, the **bottom-up dynamic programming approach** systematically fills in a table of subproblems, ensuring that each value is available when required. This shift from recomputation to reuse is the essence of dynamic programming and is what makes it so powerful in transforming intractable problems into manageable ones.

This principle doesnÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t just apply to Fibonacci numbers; it extends to other computational problems, such as **sequence alignment** in bioinformatics, where dynamic programming techniques help efficiently align sequences by reusing results of smaller alignment tasks. The power of dynamic programming lies in its ability to simplify complex problems by breaking them down into reusable components, making it an essential tool in algorithm design.

## [51:36](https://www.youtube.com/watch?v=3Fz1wNpFFnw&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=4&t=3096s) Alignment Matrix, Paths, Traceback, 2^N-vs-N^2

When aligning two sequences, each containing n and m nucleotides respectively, the goal is to efficiently calculate the best alignment scores without recalculating each possible alignment from scratch. This is achieved through **dynamic programming**, which involves systematically storing and reusing scores in an **alignment matrix**.

The alignment matrix is an nÃƒÆ’Ã¢â‚¬â€mn \\times mnÃƒÆ’Ã¢â‚¬â€m grid where each cell (i,j) represents the **score of aligning the first iii nucleotides** of sequence 1 with the first j nucleotides of sequence 2. The idea is to compute these scores iteratively and store them so that each sub-alignment can be reused when needed, rather than starting from scratch each time.

To fill this matrix, we compute the score at each cell based on three potential previous alignments: moving **diagonally** (representing a match or mismatch between the current nucleotides), moving **vertically** (representing a gap in sequence 1), or moving **horizontally** (representing a gap in sequence 2). The score at each position (i,j) is the **maximum** of these three values, plus the specific cost associated with the operationÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âwhether itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s a match, mismatch, or gap penalty.

A crucial aspect of this approach is **traceback**. To reconstruct the optimal alignment, we donÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t just calculate scores; we also store **pointers** or **arrows** in each matrix cell that indicate which of the three possible moves (diagonal, up, or left) led to the current score. These pointers allow us to trace the optimal path from the bottom-right corner of the matrix (where the final score is located) back to the top-left corner, effectively reconstructing the sequence alignment step-by-step.

The matrix can be filled in several waysÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Ârow by row, column by column, or diagonallyÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âas long as each cell is computed after the cells it depends on. By progressively building the matrix from simpler sub-problems (aligning smaller sections of the sequences), we efficiently compute the overall alignment score.

The efficiency of this approach is striking. Although there are 2^N potential paths through the matrix (since each position can involve a decision to align, insert, or delete), dynamic programming reduces the problem to filling a matrix of size NÃƒÆ’Ã¢â‚¬â€M. This means the time complexity is only O(NÃƒÆ’Ã¢â‚¬â€M), making it feasible to handle relatively large sequences. Each cell computation takes constant time, leveraging precomputed values from adjacent cells, thus transforming an exponentially complex problem into a quadratic one.

Once the matrix is filled, the real magic happens in the **traceback** process. Starting from the bottom-right, we follow the stored arrows backward, constructing the optimal alignment. Each step corresponds to a specific alignment action: matching two characters, introducing a gap in one sequence, or aligning mismatched characters. This allows us to directly visualize how the sequences align, where gaps occur, and which regions match perfectly.

A fun way to visualize and interact with this process is by implementing it in tools like Excel. By defining local scores and dependencies, and allowing dynamic updates based on gap or mismatch penalties, one can see in real time how the optimal alignment path changes. This hands-on approach makes the abstract concepts of dynamic programming and sequence alignment more tangible.

This matrix-based alignment approach is not just limited to nucleotide sequences. It applies broadly to any scenario where two sequences need to be aligned, such as comparing protein sequences, time-series data, or even aligning text. The structured, iterative methodology of dynamic programming makes it a powerful tool for tackling complex alignment problems efficiently, uncovering the best path through a seemingly vast space of possibilities.

## [1:04:45](https://www.youtube.com/watch?v=3Fz1wNpFFnw&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=4&t=3885s) Local Alignment, Linear-Time, Linear Space

Dynamic programming's strength lies in its ability to transform the complex problem of sequence alignment into a manageable process. By conceptualizing alignments as paths through a matrix, we can optimize the search for the best alignment, but thereÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s more to explore when it comes to efficiency and precision, especially in biological contexts.

### Understanding the Alignment Space

Consider an alignment path that moves all the way down one axis and then across the other, essentially deleting and adding an entire sequence. This kind of alignment is clearly suboptimal as it incurs a massive penalty for insertions and deletionsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âfar from reflecting any meaningful biological relationship between sequences. The question then becomes: **How far off the main diagonal should we allow an alignment to go before it becomes unrealistic?**

If an alignment drifts too far from the diagonal, the penalties from excessive gaps will outweigh any potential gains from matches. To handle this, we can apply a **heuristic approach**: restricting the search to a bounded region around the diagonal. This concept, known as **bounded alignment**, allows us to constrain the search space, focusing only on reasonable alignments that remain close to the diagonal.

This approach is not guaranteed to be globally optimal, as some rare cases might exist where the optimal path lies outside the bounded region. However, for practical purposes, these cases are negligible, and the computational efficiency gained is significant.

### Optimizing Space Requirements

Storing the entire alignment matrix requires quadratic space, as each cell stores a score and pointers that guide the traceback process. But what if we only care about finding the optimal score at the matrix's endpoint? In that case, storing the whole matrix is unnecessary. We only need to keep track of the scores for the current and previous rows or columns, reducing space complexity from O(n2)O(n^2)O(n2) to O(n)O(n)O(n).

This optimization allows us to compute the alignment score with just linear space. However, if we also need to reconstruct the alignment path itself, the problem becomes more complex.

### Finding the Traceback Path with Limited Space

Even with the space optimization, we can still find the optimal alignment path using a clever recursive strategy. HereÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s how:

1.  **Compute Forward and Reverse Scores**: First, calculate alignment scores from the left to the right, storing the necessary values as you go. Next, compute scores in the reverse direction, from right to left, using the same approach.
2.  **Identify the Midpoint**: By summing the scores from the forward and reverse calculations, you can identify the midpoint that provides the best alignment. This midpoint essentially divides the alignment into two sub-alignments, each of which can be processed independently.
3.  **Recursive Alignment**: Use the identified midpoint to recursively align the two halves. This recursive divide-and-conquer strategy continues until the complete alignment path is reconstructed.

This method maintains the linear space requirement for each recursive step, allowing you to handle large-scale alignments efficiently.

### Local Alignment: Finding High-Scoring Sub-Regions

Sometimes, instead of aligning entire sequences, we are more interested in finding **local alignments**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âspecific regions within the sequences that align particularly well. Local alignment is crucial when evolutionary rearrangements, inversions, or duplications have occurred, which may disrupt the continuity of a global alignment.

To perform local alignment, we adjust the dynamic programming algorithm to start and end at any position within the matrix rather than being constrained to the matrixÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s corners. This flexibility captures high-scoring sub-alignments that reflect meaningful biological relationships without requiring the sequences to align perfectly from start to end.

The algorithmÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s adaptation involves modifying the scoring rules:

- Allow the alignment to start anywhere, adding an additional zero to the options for initial alignment.
- Permit it to end at any position where the score is highest, without requiring it to reach the bottom-right corner.
- Optionally, modify the algorithm to avoid penalties for gaps at the ends of sequences, accommodating incomplete data.

### Fast Local Alignment through Hashing

To further accelerate local alignment, particularly when searching for highly conserved motifs or repeated patterns, we can use **hashing**. This technique involves:

- Identifying "seeds" or short segments of exact matches between the sequences.
- Using these seeds to anchor the alignment and then extending outward, rapidly identifying regions of high similarity.

Hashing dramatically speeds up the process by focusing computational resources on promising regions, bypassing the exhaustive pairwise comparison of every possible alignment. ItÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s akin to scanning a video for repeated actions and using those as key points for alignment rather than analyzing every frame in detail.

**Conclusion**

Local alignment and optimized alignment strategies represent crucial advancements in computational biology, enabling the discovery of meaningful relationships between sequences even in the presence of evolutionary rearrangements and other complex changes. By balancing heuristic approaches, space optimization, and efficient recursive methods, dynamic programming extends far beyond global sequence alignment, offering tools that are indispensable for understanding the genetic code and the evolutionary history encoded within.

## [1:14:35](https://www.youtube.com/watch?v=3Fz1wNpFFnw&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=4&t=4475s) Hashing, BLAST, Inexact Matching, and PSI-BLAST

One of the most powerful tools in computational biology is BLAST (Basic Local Alignment Search Tool). Despite its humble name, BLAST has revolutionized the way we compare sequences by employing hashing and other sophisticated techniques to perform local alignments at unprecedented speeds. LetÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s explore the principles behind this transformative approach.

### Hashing: The Foundation of Fast Sequence Matching

The key to rapid sequence alignment lies in a concept borrowed from computer science: hashing. Hashing transforms sequences into numerical representations, allowing for incredibly fast lookups. Imagine you want to find a specific sequenceÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â31415, part of the well-known sequence of piÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âwithin a much longer sequence. Instead of comparing each segment of the long sequence character-by-character, you can treat 31415 as a single number, making the comparison as simple as checking if two numbers are equal.

However, computing such large numbers can be computationally expensive, especially if each calculation involves multiple digits. To make this more efficient, the algorithm uses a rolling hash: it updates the number incrementally by subtracting the contribution of the first digit, shifting the remaining digits, and adding the new digit. This approach reduces the time complexity of each update to constant time.

To avoid the pitfalls of handling extremely large numbers, we apply a modulus operation, which keeps the numbers manageable. This effectively compresses the sequence into a smaller range, allowing fast comparisons. The trade-off is a small chance of collisions, where different sequences yield the same hash. However, these collisions are statistically rare, especially when the hashing space is sufficiently large.

### BLAST: Extending Hashing to Biological Sequences

BLAST builds upon these principles, using hashing to rapidly identify matching sequences in a large database. The algorithm breaks the input sequence into small chunks, or "seeds," and searches for these seeds within the database. Once a seed match is found, BLAST extends the alignment outward from the seed, creating a local alignment between the sequences.

The real power of BLAST comes from its ability to handle not just exact matches but also **inexact matches**. BLAST doesnÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t just look for identical sequences; it also considers close matches, where amino acids or nucleotides are similar but not identical. For instance, it searches for sequences that match a given score threshold, allowing for substitutions that are biologically plausible based on known evolutionary patterns.

In this way, BLAST can find alignments even when there is no perfect match, providing insights into evolutionary relationships and functional similarities between sequences.

### PSI-BLAST: Iterative Search for Deeper Connections

PSI-BLAST (Position-Specific Iterated BLAST) takes this approach further by allowing iterative searches. It builds a position-specific scoring matrix (PSSM) based on the sequences found in the initial BLAST search. This matrix captures the likelihood of each amino acid occurring at each position, accounting for sequence variability seen in evolution.

Subsequent searches use this PSSM to refine the search, identifying sequences that are even more distantly related. PSI-BLAST is particularly powerful for detecting remote homologsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âsequences that share common ancestry but have diverged significantly over time.

### Putting It All Together: Probabilistic Foundations and Efficiency

The probabilistic foundations of BLAST and its extensions are grounded in comparing the likelihood of matching sequences under two models: a related model (where sequences share a common ancestor) and an unrelated model (random sequences). The ratio of these likelihoods informs the scoring of matches, weighting substitutions by their evolutionary plausibility.

Key takeaways include:

- **Hashing** transforms sequences into manageable numbers, allowing rapid matching with minimal computation.
- **BLAST** uses seeds and extensions to perform local alignments, accommodating both exact and inexact matches.
- **PSI-BLAST** builds on BLAST by iteratively refining searches with position-specific scoring, uncovering deeper evolutionary links.
- **Probabilistic scoring** ensures that alignments reflect biologically relevant relationships, not just raw similarity.

These algorithms have become the backbone of comparative genomics, enabling scientists to explore the vast landscape of genetic data efficiently. They highlight the power of computational techniques in deciphering the complex web of life, from individual genes to entire genomes.


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
You should be able to explain how comparative genomics, mutation/insertion/deletion models, dynamic programming, traceback, local alignment, BLAST, PSI-BLAST, and PSSMs connects a biological problem to a computational representation, model, or algorithm.

### Q2. What should you be able to explain from this lecture?
You should be able to explain how comparative genomics, mutation/insertion/deletion models, dynamic programming, traceback, local alignment, BLAST, PSI-BLAST, and PSSMs connects a biological problem to a computational representation, model, or algorithm.

### Q3. What should you be able to explain from this lecture?
You should be able to explain how comparative genomics, mutation/insertion/deletion models, dynamic programming, traceback, local alignment, BLAST, PSI-BLAST, and PSSMs connects a biological problem to a computational representation, model, or algorithm.

### Q4. What should you be able to explain from this lecture?
You should be able to explain how comparative genomics, mutation/insertion/deletion models, dynamic programming, traceback, local alignment, BLAST, PSI-BLAST, and PSSMs connects a biological problem to a computational representation, model, or algorithm.

### Q5. What should you be able to explain from this lecture?
You should be able to explain how comparative genomics, mutation/insertion/deletion models, dynamic programming, traceback, local alignment, BLAST, PSI-BLAST, and PSSMs connects a biological problem to a computational representation, model, or algorithm.

### Q6. What should you be able to explain from this lecture?
You should be able to explain how comparative genomics, mutation/insertion/deletion models, dynamic programming, traceback, local alignment, BLAST, PSI-BLAST, and PSSMs connects a biological problem to a computational representation, model, or algorithm.

### Q7. What should you be able to explain from this lecture?
You should be able to explain how comparative genomics, mutation/insertion/deletion models, dynamic programming, traceback, local alignment, BLAST, PSI-BLAST, and PSSMs connects a biological problem to a computational representation, model, or algorithm.

### Q8. What should you be able to explain from this lecture?
You should be able to explain how comparative genomics, mutation/insertion/deletion models, dynamic programming, traceback, local alignment, BLAST, PSI-BLAST, and PSSMs connects a biological problem to a computational representation, model, or algorithm.

### Q9. What should you be able to explain from this lecture?
You should be able to explain how comparative genomics, mutation/insertion/deletion models, dynamic programming, traceback, local alignment, BLAST, PSI-BLAST, and PSSMs connects a biological problem to a computational representation, model, or algorithm.

### Q10. What should you be able to explain from this lecture?
You should be able to explain how comparative genomics, mutation/insertion/deletion models, dynamic programming, traceback, local alignment, BLAST, PSI-BLAST, and PSSMs connects a biological problem to a computational representation, model, or algorithm.

## Key Takeaways
- comparative genomics, mutation/insertion/deletion models, dynamic programming, traceback, local alignment, BLAST, PSI-BLAST, and PSSMs is part of the MLCB modeling arc.
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

- [[sequence-alignment]]
- [[dynamic-programming]]
- [[blast]]
- [[scoring-matrix]]
- [[motif-finding]]
- [[meme]]
- [[dna-sequence]]

### Cluster Membership

- [[cluster-map-classical-ml]]

### Key Relationships (from KG)

See [[lecture-entity-map]] for the full relationship list, and [[knowledge-graph-index]] for the global entity index.
