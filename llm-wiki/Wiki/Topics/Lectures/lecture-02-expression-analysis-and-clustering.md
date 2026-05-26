---
tags:
  - "topic"
topics:
  - "MLCB"
status: updated
created: 2026-05-24
updated: 2026-05-24
sources:
  - "Raw/Sources/lecture_02_expression_analysis_and_clustering.md"
source_count: 1
aliases:
  - "Lecture 2 - Expression Analysis and Clustering"
---

# Lecture 2 - Expression Analysis and Clustering

## Source
- Raw source: `Raw/Sources/lecture_02_expression_analysis_and_clustering.md`
- Supporting source: `Raw/Files/lecture_02_expression_analysis_and_clustering.md`
- Existing related pages: [[mlcb-2024-computational-biology]], [[mlcb-complete-study-guide]], [[mlcb-methods-map]]
- Last updated: 2026-05-24

## Executive Summary
Lecture 2 - Expression Analysis and Clustering develops expression matrices, supervised and unsupervised learning, Bayes rule, GMMs, K-means, EM, PCA, and hierarchical clustering. This page intentionally preserves substantial source detail so a future LLM can reason from the wiki without immediately reopening the raw transcript.

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
- What is Machine Learning
- Making Inferences about the World
- Reversing the Arrows: Bayesian Inference
- Clustering and Classification
- AI vs. ML vs. Representation Learning vs. Generative AI
- ML for Gene Expression Analysis
- K-means Clustering
- Gaussian Mixture Model Sampling
- Hierarchical Clustering

## Detailed Lecture Notes
The notes below preserve the processed source order and are intentionally detailed.

# [[Lecture 2: Expression Analysis and Clustering

Video: [Lecture02 - Expression Analysis Clustering Classification - MLCB24](https://www.youtube.com/watch?v=Air6zIVf0M8&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=2)

Slides: [Lecture02_ExpressionClusteringClassification.pdf](https://www.dropbox.com/scl/fi/i2gdxf8ssucwqgizwdy9m/Lecture02_ExpressionClusteringClassification.pdf?rlkey=zqh8s7pqlneq1ywcj7on1qdme&dl=0)

## [0:00](https://www.youtube.com/watch?v=Air6zIVf0M8&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=2&t=0s) Intro

Welcome to Lecture 2! I hope everyone is feeling great today. Just a quick reminderÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âplease fill out the first day survey by Friday. WeÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢re organizing teams for the formal mentoring session, and this survey will help us understand you better and form balanced groups. The more information we have, the better we can structure these teams for the mentoring session on Friday, where you will also be completing a one-page profile. This will help your classmates get to know you and facilitate more effective collaboration.

### Module 1: Genomics, Epigenomics, Single Cell Analysis, and Networks

Today marks the beginning of our first module, which will cover a wide range of topics in genomics, epigenomics, single-cell technologies, and network analysis. We will delve into the fundamental techniques used to analyze gene expression, explore how these approaches are applied to understand complex biological systems, and introduce key machine learning concepts.

### Today's Focus: Expression Analysis

We start with the basics of **expression analysis**, which is foundational in understanding the activity of genes across different conditions or cell types.

We'll introduce clustering and classification, exploring how they fit into broader contexts of **supervised** and **unsupervised learning**.

We will touch upon concepts such as **semi-supervised learning**, which bridges the gap between these two main paradigms.

### Key Techniques: Clustering and Classification

**K-means Algorithm**: A simple yet powerful clustering method that partitions data into groups based on similarity.

**Gaussian Mixture Models (GMMs)**: WeÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll build on K-means to understand GMMs, which provide a probabilistic approach to clustering that accounts for the inherent variability within data.

These methods will set the stage for deeper exploration of machine learning principles, including Bayesian inference and the contrasts between generative and discriminative models. This will be our first foray into the application of machine learning to computational biology, grounding us in the core techniques that will reappear throughout the course.

### Looking Ahead: The Structure of Module 1

**Thursday**: We will shift focus to sequential data, examining how to align and decode complex patterns using techniques like **dynamic programming**, **Hidden Markov Models (HMMs)**, and **posterior decoding**.

**Next Week**: We dive into **Gene Regulation**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âexploring the regulatory motifs, signals of histone modifications, and the broader regulatory landscape that drives gene expression. This will also involve methods to model these signals computationally.

**Single-Cell Genomics**: While todayÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s lecture will touch on the basics of clustering and classification, we will dedicate a future lecture to the nuances of single-cell genomics and spatial transcriptomics. These rapidly evolving technologies are reshaping our understanding of cellular heterogeneity and gene expression in situ.

**Advanced Visualization**: We will also explore nonlinear embeddings for visualizing high-dimensional single-cell data, a topic that we will revisit in detail later in the module.

**Graphs and Circuitry**: Our journey will culminate in a deep dive into **regulatory circuitry**, using techniques like **principal component analysis** and other dimensionality reduction methods to unravel complex biological networks.

### Overview of Future Modules

- **Module 2**: Focus on **protein structure**, diving into the intricate world of protein folding and function.
- **Module 3**: **Chemistry**, examining molecular interactions at a computational level.
- **Module 4**: Exploring **Electronic Health Records (EHRs)** and other large-scale biomedical data sources.

Are you excited to begin Module 1? Today marks our first formal introduction to machine learning within the context of computational biology. We will begin to see how these powerful tools can be leveraged to make sense of the vast and complex datasets that define modern genomics.

## [4:37](https://www.youtube.com/watch?v=Air6zIVf0M8&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=2&t=277s) What is Machine Learning

### What is Machine Learning?

Machine learning is fundamentally about the ability to **improve performance on a task with more training data**. This concept distinguishes machine learning from traditional artificial intelligence (AI). While AI has been a topic of interest since the 1960s, many AI systems were designed to simulate intelligence by hard-coding decisions and rules. These systems appear intelligent but do not inherently improve over time. If an AI system does not get better with additional data, it is not genuinely engaging in machine learning.

**Core Principles of Machine Learning:**

1.  **Task**: The objective or problem you want the model to solve.
2.  **Training Data**: The experience that feeds the model, allowing it to learn patterns and relationships.
3.  **Improvement**: The model's performance must enhance as it encounters more data.

### Types of Learning Tasks

Machine learning encompasses a broad spectrum of tasks, each with distinct goals:

- **Classification**: A form of supervised learning where the goal is to assign labels to data. For example, distinguishing Alzheimer's patients from healthy controls. Here, we know the correct answer, and the learning is supervised.
- **Clustering**: An unsupervised learning task where we group data without predefined labels, discovering natural groupings or patterns.
- **Regression**: Predicting a continuous value, such as forecasting the age at which an individual might develop Alzheimer's. Regression is about numbers, not categories.
- **Transcription**: Converting data from one form to another, like transforming spoken words into text, as seen with speech-to-text systems.
- **Translation**: Converting information between languages, for example, from English to Greek or French.
- **Structured Output**: Generating organized, meaningful information from raw, unstructured data. For example, translating a doctorÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s spoken diagnosis into structured fields like ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œtumor size: 7ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â or ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œdiabetes stage: severe.ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â

Structured data is organized and quantifiable, while **unstructured data**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âlike free text or imagesÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âlacks such format. Machine learning has traditionally focused on structured data, but this distinction is blurring as techniques for processing unstructured data (e.g., clustering on text or images) have advanced.

### Additional Machine Learning Tasks

**Anomaly Detection**: Identifying unusual or unexpected patterns within data. For example, monitoring patient activities through Wi-Fi signals and detecting falls, triggering an alert to emergency services.

**Synthesis**: Combining multiple datasets to create a more comprehensive understanding, summarizing key insights from the data.

**Imputation**: Filling in missing values within a dataset by predicting what those values should be based on the existing data.

**Denoising**: Identifying and removing noiseÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âunwanted variability in data that can obscure the true signal, such as technical artifacts rather than biological differences.

Across all these tasks, the key is to improve performance with more data. This is the essence of machine learning. To measure improvement, we need a performance metric that quantifies the modelÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s accuracy or effectiveness.

### Machine Learning Process

The **training data** serves as the **experience** for the model, akin to how a robot learns from interacting with its environment or how an AI system learns from observing doctor-patient interactions. This ongoing experience allows the model to refine its predictions and responses.

### Summary:

- Machine learning is about continuous improvement with more data.
- Performance metrics are essential to validate this improvement.
- It encompasses a wide range of tasks, from classification and clustering to more complex processes like synthesis and anomaly detection.

Understanding these fundamental principles will guide our exploration of machine learning applications in computational biology, as we move from basic techniques to more sophisticated models.

## [9:32](https://www.youtube.com/watch?v=Air6zIVf0M8&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=2&t=572s) Making Inferences about the World

In computational biology, and indeed in all scientific analysis, there is a crucial distinction between what we **observe** and what remains **hidden**. Observations might include direct measurements like gene expression values, while hidden states might represent underlying conditions, such as whether a patient has Alzheimer's.

We can think of the world as divided into two realms:

- **The World of Measurements**: This is the domain of observable data, such as expression values, weather conditions, or clinical symptoms.
- **The World of Models and Inferences**: This realm involves the hidden states, hypotheses, and the underlying factors driving those observations.

**Inference** is the process of deducing hidden states based on observed data. For example, looking outside and seeing bright sunlight might lead you to infer itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s summer. If you see snow, you infer itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s winter. The observations are directÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âlight, rain, snowÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âbut the hidden states are inferred: the season, the weather system, or any other underlying condition.

### Why Inferences Matter

Understanding hidden states allows us to make **predictions** about future conditions or decisions. For example, if you infer that a storm is building based on current weather patterns, you might decide against sailing. Similarly, in a medical context, observing high expression of a specific gene might allow us to infer a higher probability of a disease like Alzheimer's.

**Key Concept**: You observe measurable parts of the world to infer hidden, often more critical aspects of that world.

### Forward Probabilities and Inferences

Very often, we can directly measure and express **forward probabilities**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthe likelihood of observable events given a known state of the world. For example: **Winter** might have a 60% chance of snow. **Summer** might have a 60% chance of sunshine. These are relatively easy to measure because they start from a known condition and predict observable outcomes.

However, **inferences** work in the reverse direction. They aim to determine the hidden state given the observations: **Given itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s raining, whatÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s the probability of a storm? Given high expression of a particular gene, whatÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s the probability of Alzheimer's?**

Forward probabilities are often described as **generative probabilities** because they model how known states of the world generate observable data. For instance, if you know itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s summer, you can predict temperatures and weather patterns typical of that season.

### Generative Models

Generative models describe how data is produced by sampling from a hidden state. For example:

1.  If you are in the state of "June," you might sample temperatures typical of June, resulting in a range of observed values.
2.  If you know the distribution of these values (mean, standard deviation), you can compare any given observation to these expectations.

When you have an observation, like a temperature reading, you can assess how likely it is to have come from a "June" or "July" distribution. This helps determine whether it is more likely that you are in June or July based on the observed data.

**Example**: If you record a temperature of 72 degrees, you can compare how probable that reading is under different generative models (e.g., June vs. July) and make an inference about the most likely state.

While weather in places like Boston may not follow neat patterns due to its variability, the broader concept holds: **you use known generative models of the world to interpret and infer hidden states from new observations.**

## [14:25](https://www.youtube.com/watch?v=Air6zIVf0M8&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=2&t=865s) Reversing the Arrows: Bayesian Inference

In machine learning and computational biology, we often work with a **generative model** that allows us to calculate the probability of specific observations given a particular state of the world. For example, we can determine the probability of observing snow given that it is winter, or more broadly, the probability of any measurement given a specific condition.

However, our real goal is to **reverse these arrows**. We want to infer the hidden state (e.g., "the patient has Alzheimer's") given the observed data (e.g., gene expression measurements). This requires reversing the direction of the relationship between data and the underlying hypothesis or state of the world.

#### Using BayesÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Rule for Inference

This reversal is precisely where **Bayes' Rule** comes in. Bayesian inference uses Bayes' Rule to flip the direction of the relationship:

- **Forward Probability (Generative)**: Probability of observing data given a hypothesis, P(DataÃƒÂ¢Ã‹â€ Ã‚Â£Hypothesis)P(\\text{Data} \\mid \\text{Hypothesis})P(DataÃƒÂ¢Ã‹â€ Ã‚Â£Hypothesis).
- **Reverse Inference**: Probability of the hypothesis given the data, P(HypothesisÃƒÂ¢Ã‹â€ Ã‚Â£Data)P(\\text{Hypothesis} \\mid \\text{Data})P(HypothesisÃƒÂ¢Ã‹â€ Ã‚Â£Data).

Bayes' Rule helps us go from knowing the probability of data given a hypothesis to inferring the probability of the hypothesis given the data:

#### Understanding BayesÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Rule in Simple Terms

To simplify, consider this analogy: The purple area in a diagram could represent the part of the world that is both red and blue. You can calculate it in two ways:

1.  Multiply the fraction of the world that is blue (P(B)P(B)P(B)) by the fraction of the blue that is also red (P(AÃƒÂ¢Ã‹â€ Ã‚Â£B)P(A \\mid B)P(AÃƒÂ¢Ã‹â€ Ã‚Â£B)).
2.  Multiply the fraction of the world that is red (P(A)P(A)P(A)) by the fraction of the red that is also blue (P(BÃƒÂ¢Ã‹â€ Ã‚Â£A)P(B \\mid A)P(BÃƒÂ¢Ã‹â€ Ã‚Â£A)).

In both cases, the purple area remains the same, demonstrating how these probabilities are interconnected.

#### Applying BayesÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Rule to Inference

In the context of Bayesian inference, the formula helps us derive what we call the **posterior probability**:

- **Posterior Probability** (P(HypothesisÃƒÂ¢Ã‹â€ Ã‚Â£Data)P(\\text{Hypothesis} \\mid \\text{Data})P(HypothesisÃƒÂ¢Ã‹â€ Ã‚Â£Data)): The probability of the hypothesis after observing the data.
- **Likelihood** (P(DataÃƒÂ¢Ã‹â€ Ã‚Â£Hypothesis)P(\\text{Data} \\mid \\text{Hypothesis})P(DataÃƒÂ¢Ã‹â€ Ã‚Â£Hypothesis)): The probability of observing the data given the hypothesis.
- **Prior Probability** (P(Hypothesis)P(\\text{Hypothesis})P(Hypothesis)): The initial probability of the hypothesis before observing any data.
- **Marginal Probability** (P(Data)P(\\text{Data})P(Data)): The probability of observing the data under all possible hypotheses.

This marginal probability is calculated as a weighted sum of the likelihoods across all hypotheses. It helps normalize the results but doesnÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t change the relative ranking of different hypotheses.

#### Importance of the Prior Probability

One critical insight in Bayesian inference is the role of the **prior probability**. It adjusts the inference based on what we already know before observing the data. For instance, if a disease is extremely rare (like one in a million), even a positive test result might not be enough to strongly suggest you have the disease because the prior probability of having it was so low to begin with.

This principle explains why medical testing often follows symptoms rather than random screening: tests are not perfect, and without a high enough prior likelihood (such as symptoms suggesting a specific condition), the probability of a false positive can outweigh the true detection.

#### Example in Medical Contexts

Consider taking a test for a rare disease. If the test is positive, is it more likely that you have the disease or that it was a false positive? Often, due to the low prior probability of the disease, the latter is trueÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âyou might not have the disease even with a positive result. This highlights the crucial role of priors in Bayesian inference, especially for rare conditions.

### Summary

- **Likelihood** tells us the probability of observing the data given the hypothesis.
- **Prior** tells us the probability of the hypothesis before considering the data.
- **Posterior** combines these to provide the probability of the hypothesis after seeing the data.

Bayesian inference allows us to formally incorporate prior knowledge and data to make reasoned judgments about hidden states, a powerful tool in both scientific research and decision-making.

## [20:20](https://www.youtube.com/watch?v=Air6zIVf0M8&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=2&t=1220s) Clustering and Classification

In the context of Bayesian inference and machine learning, we are first introducing a simple algorithm for clustering, which is a key unsupervised learning task. We will also touch upon how this relates to more general approaches like Gaussian Mixture Models (GMMs).

### Gaussian Mixture Models (GMMs)

- **GMMs** represent scenarios where data is generated from a mixture of multiple Gaussian distributions.
- Imagine sampling data points from several distributions: one green, one red, one blue.
- In a real-world problem, we donÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t know the underlying distributions, centroids, or spreads.
- **Clustering** attempts to infer the hidden distributions without any labeled guidance.

### Supervised vs. Unsupervised Learning

- **Unsupervised Learning**: Finds patterns or structures in data without labels. For example, inferring clusters when you donÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t know the green, red, or blue labels.
- **Supervised Learning**: Uses labeled data to classify new points. For instance, if we have clusters of labeled points (green, red, blue) and we encounter a new gray point, we use the learned structure to classify it based on proximity.

These two main tasksÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â**clustering (unsupervised)** and **classification (supervised)**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âare central to the lecture. For example, in genomics, you may measure gene expression in different tissues (like brain and liver) and attempt to classify or cluster the data based on these measurements.

### Visualizing High-Dimensional Data

We often visualize data in two dimensions due to human limitations, even though biological data can have thousands of dimensions (e.g., 20,000 genes measured simultaneously).

**Dimensionality Reduction Techniques**: **Principal Component Analysis (PCA)**: Identifies major axes of variation in data. **Nonlinear Embeddings**: Techniques like t-SNE or UMAP that help project high-dimensional data into lower dimensions while preserving the structure.

### Clustering vs. Classification

**Classification**: Uses known labels to develop rules for assigning new data points into existing classes. This involves feature selection and creating metrics like accuracy, false positives, and false negatives.

**Clustering**: Groups data points based on proximity without predefined labels, identifying structure and patterns within the data. ItÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s challenging to validate because it lacks explicit performance metrics and often requires external validation.

### Feature Selection and Representation Learning

**Feature Selection**: Involves choosing relevant variables from a dataset, especially when you have many more features than samples (e.g., 20,000 genes vs. 70 students).

**Feature Construction**: Creating new variables from existing ones (e.g., combinations of gene expressions).

**Representation Learning**: The process of discovering underlying features or patterns that best represent the dataÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s true nature, such as latent variables like disease states or demographic factors.

### Semi-Supervised and Self-Supervised Learning

**Semi-Supervised Learning**: Combines labeled and unlabeled data, allowing the model to learn the structure from unlabeled data and refine it using the labeled points.

**Self-Supervised Learning**: Uses a pretext task, such as predicting hidden parts of data, to help the model learn underlying structures. This approach blurs the line between supervised and unsupervised learning, especially useful in scenarios with massive datasets but limited labels.

### Metrics and Validation

**Classification Metrics**: When labels are available, we can validate models using performance measures like accuracy, sensitivity, specificity, etc.

**Clustering Validation**: Often relies on indirect methods, like assessing how well the clusters correlate with additional, unseen measurements.

## [33:45](https://www.youtube.com/watch?v=Air6zIVf0M8&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=2&t=2025s) AI vs. ML vs. Representation Learning vs. Generative AI

In this lecture, itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s crucial to differentiate between various concepts like AI, Machine Learning (ML), Representation Learning, and Generative AI. LetÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s explore these concepts in detail.

### Artificial Intelligence (AI)

**AI encompasses many systems**, including those that are not inherently learning from data but are designed to simulate intelligence. **Examples include** rule-based or knowledge-based systems, where rules are hardcoded to make decisions based on input without improvement over time. **ML is a subset of AI** that involves learning from data to improve performance on a task. **Classical ML** often involves hand-designed features. For example, in ML models, we manually choose measurements or features and use data to infer the parameters that weigh these features, improving with more data. **Representation Learning goes beyond ML** by automatically discovering the features from raw data rather than relying on hand-designed features. Instead of specifying the relevant gene expression features manually, representation learning allows the model to infer these features, potentially uncovering complex combinations and patterns.

**Deep Learning** is a special type of representation learning where features are learned hierarchically: Lower layers learn simple features. Higher layers build on these, learning more complex patterns. This multi-layered learning approach leads to increasingly abstract representations.

**Generative AI** falls within the broader field of deep learning and focuses on models that can generate new data instances similar to the training data. Examples include image generation, text generation, and more.

### Distinguishing AI, ML, and Deep Learning

**AI (Broadest Scope)**: Encompasses systems that mimic intelligent behavior, including non-learning systems.

**ML (Within AI)**: Systems that learn from data to improve at tasks.

**Representation Learning (Within ML)**: Automatically learns features from data rather than relying on human-designed features.

**Deep Learning (Within Representation Learning)**: Uses multiple layers of feature learning, each layer building on the previous one, allowing for more complex abstractions.

### Applications and Evolution

**Classical AI in Chess**: Earlier AI approaches in games like chess involved hardcoded rules, handcrafted scoring functions, and algorithms like Minimax to decide moves. This approach highlighted the limitations of hardcoded intelligence.

**Shift from Hard Tasks for Humans to Hard Tasks for Machines**:

- **Old Paradigm**: Tasks like chess, logic, and planning were seen as the pinnacle of intelligenceÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âhard for humans, but structured and rule-based, making them easier for machines.
- **New Paradigm**: Recognizing images, driving cars, and understanding natural language are innately easier for humans but were extremely challenging for machines until recent advancements in deep learning.

### Deep Learning and Human Cognition

**Layers of Abstraction**: Similar to how the human brain processes information, deep learning uses layers of neurons (real or artificial) to recognize increasingly complex patternsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âfrom edges to shapes to complete objects.

**Neocortex Expansion**: Evolutionarily, humans have greatly expanded the neocortex, enabling us to perform complex reasoning, sensory processing, and abstract thinkingÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âall of which are mirrored in the architecture of deep learning models.

**General AI Implications**: Current models excel at pattern recognition, a domain where humans also excel innately. There is ongoing debate about whether artificial general intelligence (AGI) will emerge from scaling these models or if new, structured approaches are needed.

### Summary

The concepts of AI, ML, representation learning, and deep learning represent a progression towards models that can better understand and interact with the world.

These techniques are not just technical; they mirror how we think and learn, offering profound insights into both artificial and natural intelligence.

## [46:06](https://www.youtube.com/watch?v=Air6zIVf0M8&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=2&t=2766s) ML for Gene Expression Analysis

### Machine Learning for Gene Expression Analysis

Gene expression analysis involves studying how genes are expressed in different cells or tissues, which can reveal important biological insights, such as identifying disease mechanisms or cell types. This process starts with isolating tissue samples and often involves extracting nuclei from complex tissues like the brain. The extracted nuclei are encapsulated in tiny droplets, each tagged with a unique DNA barcode. This barcode ensures that all RNA molecules from a particular cell are identifiable, linking them back to their original cell of origin.

The barcoding process allows researchers to sequence the RNA from individual cells and generate a dataset known as an expression matrix. This matrix contains counts of RNA molecules corresponding to specific genes in each cell. The matrixÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s rows typically represent individual genes, and the columns represent individual cells, with each entry indicating the expression level of a gene in a particular cell. Modern sequencing technologies have dramatically reduced the cost of sequencing, enabling the quantification of gene expression at a single-cell level with unprecedented resolution.

Once the expression matrix is generated, it is used for downstream analyses such as principal component analysis (PCA) and clustering. PCA helps reduce the dimensionality of the data, making it easier to visualize and identify patterns. Clustering, on the other hand, groups similar cells or genes, revealing hidden structures within the data. For example, clustering might group genes that have similar expression profiles across various conditions or group cells that exhibit similar gene expression patterns, potentially indicating a common cell type or state.

Gene expression data can be analyzed in two main ways: comparing expression profiles across genes or across conditions (e.g., different patients or treatments). In the context of disease, such as AlzheimerÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s, clustering can reveal how gene expression patterns differ between affected and unaffected individuals, helping to identify disease-associated genes.

### Clustering vs. Classification

Clustering and classification are core tasks in gene expression analysis but serve different purposes. Clustering is an unsupervised learning technique used to discover groups of similar data points, such as cells with similar expression patterns, without prior knowledge of group labels. The goal of clustering is to find inherent structure in the data, which can reveal biologically meaningful patterns like distinct cell types or subtypes.

Classification, on the other hand, is a supervised learning approach where the objective is to assign predefined labels to new data points based on features extracted from the data. For example, classification can be used to predict cell types based on gene expression profiles or to distinguish between diseased and healthy cells. This process involves training a model using labeled data, where the classes are known, and then using this model to predict labels for new, unlabeled data points.

In practice, real-world gene expression data is highly complex, often involving millions of cells and thousands of genes, as seen in large-scale datasets with millions of single cells from hundreds of donors. To make sense of this high-dimensional data, dimensionality reduction techniques are often employed, projecting the data into lower dimensions that capture the most relevant biological variation while preserving as much information as possible.

### Practical Challenges in Gene Expression Analysis

While the concept of clustering and classifying cells or genes seems straightforward, the actual implementation involves overcoming several practical challenges. These include technical noise, batch effects from different experimental runs, sparsity in the data due to dropout events where certain genes are not detected, and variability between cells that might not be biologically meaningful. Researchers must also contend with the integration of data from different platforms and experimental designs, alignment issues, and the possibility of capturing doublets or multiplets, where more than one cell is encapsulated in the same droplet.

These complexities require careful preprocessing and normalization to ensure that the clustering reflects true biological differences rather than technical artifacts. Understanding these nuances is crucial for interpreting results correctly and for making meaningful biological inferences from gene expression data.

In the subsequent parts of this lecture, we will explore algorithms like Gaussian Mixture Models and K-means clustering, which are fundamental tools in this field. These models help to infer the underlying structure of gene expression data, allowing researchers to make predictions and identify key patterns that can advance our understanding of biology and disease.

## [54:29](https://www.youtube.com/watch?v=Air6zIVf0M8&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=2&t=3269s) K-means Clustering

**K-means clustering** is a popular **unsupervised learning** algorithm used to partition data points into a specified number of clusters, KKK. The primary goal is to group data in a way that points within each cluster are as similar as possible, while being distinct from points in other clusters. The process involves an iterative approach, where clusters are progressively refined until a stable configuration is reached.

The algorithm works through the following steps:

1.  **Initialization**: K-means begins by randomly placing KKK cluster centroids within the data space. These centroids serve as initial guesses for the cluster centers.
2.  **Assignment Step**: Each data point is assigned to the nearest centroid based on a distance metric, typically **Euclidean distance**. This step groups points into KKK clusters based on proximity.
3.  **Update Step**: Once points are assigned, the centroids are updated by calculating the **mean position** of all points assigned to each cluster. This effectively moves each centroid to the center of its associated points.
4.  **Iteration**: These steps are repeatedÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âreassigning points and recalculating centroidsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âuntil convergence, which occurs when there are no further changes in the assignments of points to clusters or when the centroids stop moving significantly.

### How K-means Works: Step-by-Step Illustration

Imagine a set of scattered data points with no prior knowledge of how they were generated. K-means starts by placing KKK centroids randomly. In each iteration, the algorithm assigns each point to the nearest centroid, effectively grouping them into clusters. After assigning the points, the centroids are recalculated based on the average position of their assigned points, effectively refining the clusters.

For instance, if the centroids are initially placed close to certain clusters, the assignment step will immediately group nearby points. As centroids adjust and shift closer to the true centers of their respective clusters, the algorithm gradually refines the cluster boundaries, improving the representation of the data structure with each iteration.

### Objective of K-means

The primary objective of K-means is to **minimize the within-cluster sum of squares (WCSS)**, which is a measure of how spread out the points in each cluster are around their centroid. The goal is to make clusters compact and well-defined. Mathematically, this is expressed as:

where CkC_kCkÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â¹ denotes the set of points assigned to cluster kkk, and ÃƒÅ½Ã‚Â¼k\\mu_kÃƒÅ½Ã‚Â¼kÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â¹ is the centroid of that cluster. The algorithmÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s iterative process of assigning points and updating centroids is specifically designed to minimize this cost, thereby improving the quality of the clustering.

### Challenges and Modifications of K-means

While K-means is straightforward and effective, it has notable limitations, including sensitivity to the initial placement of centroids and the assumption that clusters are **spherical and equally sized**. Moreover, K-means assigns each point rigidly to a single cluster, which can be problematic when points lie near cluster boundaries.

**Fuzzy K-means** is one variation that addresses these limitations by allowing partial assignment of points to multiple clusters. Instead of assigning a point entirely to one cluster, Fuzzy K-means assigns probabilities that represent the likelihood of the point belonging to each cluster. For example, a point near the boundary of two clusters might be 60% associated with one cluster and 40% with another, reflecting the inherent uncertainty.

### K-means as a Special Case of Gaussian Mixture Models (GMMs)

K-means can be seen as a special case of **Gaussian Mixture Models (GMMs)**, where each cluster is modeled as a Gaussian distribution. In GMMs, points are assigned probabilistically based on the likelihood that a given cluster generated each point. This probabilistic framework allows GMMs to capture more complex data structures, especially when clusters overlap or have different shapes.

In summary, K-means clustering provides a simple, yet powerful way to discover hidden structure in data. It iteratively refines clusters to minimize internal variance, offering a clear, interpretable approach to understanding complex datasets. Its extensions, such as fuzzy K-means and GMMs, further enhance its ability to model the true underlying distributions of data, making it a versatile tool in gene expression analysis and beyond.

## [1:01:27](https://www.youtube.com/watch?v=Air6zIVf0M8&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=2&t=3687s) Gaussian Mixture Model Sampling

Gaussian Mixture Models (GMMs) provide a framework for understanding data generated from a mixture of multiple Gaussian distributions. In GMMs, we assume that data points are generated by a set of Gaussian distributions, each with its own mean and variance. This model allows for a more nuanced understanding of data compared to K-means, which only considers cluster centers.

Imagine a scenario where you have different clusters of points, each generated from a different Gaussian distribution. For instance, some points come from a red cluster, others from a blue cluster, and so on. In GMMs, you start by flipping a coin (or rolling a die) to decide which Gaussian distribution to sample from, and then you draw a point from that distribution based on its spread and mean. This process leads to clusters where the density of points decreases exponentially as you move away from the center, following the familiar bell-shaped curve of the Gaussian.

### The Ubiquity of the Gaussian Distribution

The Gaussian distribution isnÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t just a mathematical construct; it frequently appears in real-world scenarios. A classic physical example is the Galton board, where balls randomly fall left or right as they bounce through a grid of pegs, creating a distribution of balls that forms the shape of a Gaussian curve at the bottom. This highlights how randomness in many natural processes often results in Gaussian distributions, making them a powerful model for data analysis.

### Understanding Points in the Context of Multiple Gaussians

When dealing with GMMs, each point in your dataset has a likelihood of being generated by each of the different Gaussian distributions. For example, a point near the center of the red distribution is highly likely to have been generated by the red cluster, while a point between the red and blue clusters might have probabilities of belonging to both, with varying likelihoods. This probabilistic assignment differentiates GMMs from K-means, where each point is rigidly assigned to the closest cluster.

However, GMMs go beyond simple cluster centersÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthey incorporate different spreads and variances, allowing for clusters of different sizes and shapes. This is particularly useful when clusters overlap or have elongated shapes, which are not well captured by K-means.

### Expectation-Maximization (EM): Iterative Refinement

To find the optimal set of clusters in a GMM, we use an iterative approach called **Expectation-Maximization (EM)**. EM allows us to iteratively refine our estimates of the cluster parameters (means, variances, and priors) and the assignments of points to clusters. This process involves two main steps:

1.  **Expectation Step (E-step)**: Assume that the cluster parameters (means, variances) are known and use them to estimate the probability that each point belongs to each cluster. This step assigns points probabilistically rather than deterministically, accommodating the inherent uncertainty near cluster boundaries.
2.  **Maximization Step (M-step)**: Given these probabilistic assignments, update the cluster parameters to better fit the data. Specifically, you compute new means, variances, and mixing proportions that maximize the likelihood of the observed data under the current probabilistic assignments.

These steps are repeated iteratively, gradually refining both the cluster assignments and parameters until convergence, i.e., until further updates no longer significantly improve the fit of the model to the data.

### Connection to K-means and Beyond

The EM algorithm can be seen as a generalization of K-means, where instead of hard assignments, we make probabilistic assignments of points to clusters. This probabilistic nature allows GMMs to capture more complex data structures, accounting for varying cluster sizes, shapes, and overlapping areas.

In K-means, each point is assigned to the closest cluster center based purely on Euclidean distance, without considering variance or priors. In contrast, GMMs consider both the probability of a point being generated by a cluster and the shape of the distribution. This makes GMMs a much more powerful tool for modeling real-world data, especially when the assumptions of equal variance and distinct boundaries do not hold.

Overall, Gaussian Mixture Models, paired with the EM algorithm, offer a robust framework for discovering the underlying probabilistic structure of data, accommodating overlapping clusters, variable spreads, and complex shapes, which are beyond the reach of simpler clustering methods like K-means.

## [1:09:58](https://www.youtube.com/watch?v=Air6zIVf0M8&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=2&t=4198s) Hierarchical Clustering

Hierarchical clustering provides a versatile approach to grouping data without requiring you to pre-select the number of clusters, as is necessary in methods like K-means. It works by building a nested set of clusters, arranged as a hierarchy, which can be visualized in a tree-like diagram called a dendrogram. This approach is particularly useful when you want to explore data relationships at multiple levels of granularity.

### How Hierarchical Clustering Works

The basic process of hierarchical clustering involves iteratively merging the closest pairs of points or clusters. HereÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s how it unfolds:

1.  **Initialization**: Each data point starts as its own cluster.
2.  **Merging Closest Pairs**: At each step, the two closest clusters are merged into a single cluster. The definition of "closest" can vary, affecting how the clusters form:
    - **Single Linkage**: Merges clusters based on the closest pair of points from each cluster. This approach can create elongated, chain-like clusters.
    - **Complete Linkage**: Merges clusters based on the furthest pair of points between clusters, promoting compact cluster formations.
    - **Average Linkage**: Uses the average of all pairwise distances between points in the two clusters, balancing between the single and complete linkage.
    - **Centroid Linkage**: Merges clusters based on the distance between their centroids (centers of mass), recalculating centroids after each merge.
3.  **Forming the Hierarchy**: As clusters are merged, a hierarchy forms. This hierarchical representation allows you to choose the number of clusters dynamically by cutting the dendrogram at different levels.

### Advantages of Hierarchical Clustering

**No Need to Predefine K**: Unlike K-means, hierarchical clustering doesn't require setting the number of clusters beforehand. You can decide how many clusters make sense after examining the dendrogram.

**Flexible Cluster Shapes**: It can capture complex cluster structures, including nested clusters, which are challenging for methods like K-means that assume spherical clusters.

**Visual Insights**: The dendrogram offers a clear visual representation of how clusters merge, providing insights into the dataÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s structure at multiple levels.

### Challenges and Considerations

**Distance Metrics**: The choice of distance metric (e.g., Euclidean, Manhattan, Pearson correlation) can significantly influence clustering results. For example, Pearson correlation is useful when you want to cluster based on similarity in pattern rather than magnitude.

**Time Complexity**: The approach can be computationally intensive, particularly when calculating all pairwise distances (O(NÃƒâ€šÃ‚Â²)). Using centroid linkage can reduce some of this computational burden but requires recalculating centroids each time clusters merge.

### Applications and Evaluation

Hierarchical clustering is widely used in various fields, such as biology (e.g., gene expression analysis) and market segmentation, where itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s helpful to see data grouped naturally. To evaluate the results, you can compare clusters with external labels or additional measurements to assess how well the clustering captures meaningful patterns.

In summary, hierarchical clustering provides a flexible, intuitive way to group data, especially when exploring hierarchical relationships without needing to commit to a specific number of clusters in advance.

## [1:13:10](https://www.youtube.com/watch?v=Air6zIVf0M8&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=2&t=4390s) Clustering of Documents and Free-Form Text

In 2024, clustering is no longer confined to numerical data points; it has expanded into the realm of text and free-form documents, enabling the analysis of vast and varied datasets in new, insightful ways. This capability allows us to group not just structured data but also unstructured data like survey responses, patient descriptions, or any textual information that conveys complex, nuanced meaning.

### Clustering Text: Beyond Numbers

Traditionally, clustering involves grouping points based on numerical features. For example, we might cluster millions of cells by their gene expression patterns or patients by their clinical profiles. However, text clustering takes this further by allowing us to work directly with language, extracting hidden themes, and patterns that would be impossible to see with numbers alone.

One example involves clustering survey responses about personal experiences. Responses like "I have a relationship that did not go as expected" or "I struggled with personal setbacks" can be clustered based on semantic similarity. This approach reveals common psychological or emotional themes that arenÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t captured by standard psychiatric categories defined decades ago. It provides a more personalized understanding of human experiences, showing that individual struggles often share common threads, even if they donÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t fit neatly into traditional categories.

### Applications of Text Clustering

**Psychiatric and Emotional Analysis**: Clustering text responses can highlight shared struggles, like parental health concerns or relationship breakups, allowing for a more dynamic understanding of mental health that adapts to the diversity of human experience.

**Gene Function Descriptions**: Instead of clustering genes solely by their expression data, one can cluster them based on the descriptions of their functions. For example, by analyzing the free-text descriptions of proteins, you can organize 20,000 genes by their roles, such as lipid metabolism or biosynthesis, creating an intuitive navigation through biological functions.

**Exploring Knowledge Spaces**: Tools like gene function explorers or curated knowledge maps, built by students and researchers, demonstrate how clusters of text can reveal connections between seemingly disparate topics. For instance, a cluster might highlight how lipid-related genes intersect with various diseases, providing an interactive way to explore complex biological relationships.

**Media Content Analysis**: Clustering text goes beyond scientific data. For instance, clustering topics from thousands of podcast transcripts, like Lex FridmanÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s discussions, allows one to visualize thematic landscapes. You might find that philosophical discussions, including "the meaning of life," naturally cluster near other profound topics, revealing the underlying structure of content in a way thatÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s immediately accessible and engaging.

### Implications for Broader Applications

The power of text clustering lies in its ability to connect diverse data types, merging quantitative measurements with qualitative descriptions. For example, co-embedding gene expression data with the textual descriptions of those genes can create a unified space that combines biological function with experimental observations, opening new avenues for understanding complex datasets.

These techniques encourage a broader view of what clustering can achieve, moving beyond the limitations of traditional numerical analysis. By embracing text clustering, we can uncover insights in everything from personal experiences to genetic functions, providing a richer, more nuanced understanding of data across multiple domains.

## [1:17:06](https://www.youtube.com/watch?v=Air6zIVf0M8&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=2&t=4626s) Naive Bayes Classification

Naive Bayes classification is a **simplified version of Bayesian inference** where you already know the classes that data points belong to, such as Class 1 and Class 2. This pre-knowledge allows you to directly assign **probability distributions** to data points within each class. Unlike clustering methods where class membership and distributions must be inferred from scratch, Naive Bayes leverages known class memberships, making it a more straightforward approach.

### Estimating Distributions

With Naive Bayes, estimating the **center of mass** (mean) and the **spread** (standard deviation) of each class becomes trivial since you already know the points belonging to each class. From these estimations, you can calculate the **probability of a given class** given the observed data, essentially flipping the probabilities using Bayes' rule. The goal is to compare the probability of Class 1 given the data versus Class 2 given the data.

**Forward Probability**: This represents the likelihood of observing certain data points given that they belong to a specific class.

**Backward Probability**: Using Bayes' rule, we reverse the direction of inference, estimating how likely it is that a data point belongs to a class given the observed data.

### Bayesian Classification

In Bayesian classification, the task is to determine which class a new data point most likely belongs to by comparing probabilities. We compute:

**Probability of Class 1 given the data**: Uses the forward probability of data generation multiplied by the prior probability of Class 1.

**Probability of Class 2 given the data**: Similar calculation with respect to Class 2.

Using these probabilities, you can define a **discriminant function**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âa threshold to classify a point based on which class probability is higher. This decision boundary can be tuned by adjusting the log probabilities or raw probabilities until it accurately separates the classes.

### Parametric vs. Non-Parametric Models

To estimate these distributions, you have two main approaches:

1.  **Parametric Models**: Assume a predefined form (e.g., Gaussian distribution) with parameters like mean and standard deviation. This works well when the distribution fits a known shape.
2.  **Non-Parametric Models**: Do not assume any specific distribution shape. Instead, they segment the data space and measure the frequency of observations in each segment, making them more flexible when the data doesn't conform to a simple bell-shaped curve.

### Combining Multiple Features with Naive Bayes

The classic Naive Bayes approach makes the **naive assumption** of **feature independence**, meaning it treats all features as if they don't affect each other. This assumption simplifies calculations, as the joint probability of all features given a class becomes the product of individual feature probabilities.

However, this independence assumption is rarely true in real-world data. To address this, you can:

- Use **Principal Component Analysis (PCA)** to reduce the data to independent components.
- Apply Bayesian classification on these principal components, which are designed to be less correlated.

### Key Takeaways

- Naive Bayes classification works well when class memberships are known, allowing straightforward estimation of distributions.
- It simplifies multi-feature probability calculations by assuming independence, though this assumption often needs adjustments in practice.
- Despite its simplicity, Naive Bayes remains powerful for many classification tasks, especially when combined with dimensionality reduction techniques like PCA.

This approach offers an accessible yet robust method for tackling classification challenges, especially in domains where quick, interpretable models are valuable.

## [1:20:50](https://www.youtube.com/watch?v=Air6zIVf0M8&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=2&t=4850s) Summary

In this lecture, we covered several foundational topics in **gene expression analysis** and **machine learning**:

- **Gene Expression Analysis**: We explored how gene expression data is collected, processed, and represented as a matrix of gene counts across various conditions or cells. This matrix forms the basis for further analysis using machine learning techniques.
- **K-Means Clustering**: We discussed this classic algorithm for partitioning data into a fixed number of clusters. By iteratively assigning points to the nearest cluster center and updating the cluster centers based on the mean of the points assigned to them, K-means helps identify underlying structure in the data.
- **Hierarchical Clustering**: Unlike K-means, hierarchical clustering doesn't require the number of clusters to be specified in advance. Instead, it builds a nested set of clusters organized into a hierarchy, which can be visualized as a dendrogram. This method is flexible and can be used to explore data at various levels of granularity.
- **Naive Bayes Classification**: We covered this simple yet powerful probabilistic classifier that assumes independence among features. By applying Bayes' theorem, Naive Bayes calculates the likelihood that a data point belongs to a specific class based on its features, making it an effective tool for classification tasks.
- **Clustering and Classification Beyond Numbers**: We extended the discussion to clustering and classification of text, showing how these techniques can be applied not only to numerical data but also to free-form text and other data types. This highlights the versatility of these methods, especially in the context of modern tools like large language models.

This lecture provided a broad overview of key machine learning techniques used in computational biology, setting the stage for more advanced topics in the next sessions. On Thursday, we'll delve into **Hidden Markov Models**, **dynamic programming**, **parsing**, and the analysis of **sequential data**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âcontinuing to build on these foundational concepts.


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
You should be able to explain how expression matrices, supervised and unsupervised learning, Bayes rule, GMMs, K-means, EM, PCA, and hierarchical clustering connects a biological problem to a computational representation, model, or algorithm.

### Q2. What should you be able to explain from this lecture?
You should be able to explain how expression matrices, supervised and unsupervised learning, Bayes rule, GMMs, K-means, EM, PCA, and hierarchical clustering connects a biological problem to a computational representation, model, or algorithm.

### Q3. What should you be able to explain from this lecture?
You should be able to explain how expression matrices, supervised and unsupervised learning, Bayes rule, GMMs, K-means, EM, PCA, and hierarchical clustering connects a biological problem to a computational representation, model, or algorithm.

### Q4. What should you be able to explain from this lecture?
You should be able to explain how expression matrices, supervised and unsupervised learning, Bayes rule, GMMs, K-means, EM, PCA, and hierarchical clustering connects a biological problem to a computational representation, model, or algorithm.

### Q5. What should you be able to explain from this lecture?
You should be able to explain how expression matrices, supervised and unsupervised learning, Bayes rule, GMMs, K-means, EM, PCA, and hierarchical clustering connects a biological problem to a computational representation, model, or algorithm.

### Q6. What should you be able to explain from this lecture?
You should be able to explain how expression matrices, supervised and unsupervised learning, Bayes rule, GMMs, K-means, EM, PCA, and hierarchical clustering connects a biological problem to a computational representation, model, or algorithm.

### Q7. What should you be able to explain from this lecture?
You should be able to explain how expression matrices, supervised and unsupervised learning, Bayes rule, GMMs, K-means, EM, PCA, and hierarchical clustering connects a biological problem to a computational representation, model, or algorithm.

### Q8. What should you be able to explain from this lecture?
You should be able to explain how expression matrices, supervised and unsupervised learning, Bayes rule, GMMs, K-means, EM, PCA, and hierarchical clustering connects a biological problem to a computational representation, model, or algorithm.

### Q9. What should you be able to explain from this lecture?
You should be able to explain how expression matrices, supervised and unsupervised learning, Bayes rule, GMMs, K-means, EM, PCA, and hierarchical clustering connects a biological problem to a computational representation, model, or algorithm.

### Q10. What should you be able to explain from this lecture?
You should be able to explain how expression matrices, supervised and unsupervised learning, Bayes rule, GMMs, K-means, EM, PCA, and hierarchical clustering connects a biological problem to a computational representation, model, or algorithm.

## Key Takeaways
- expression matrices, supervised and unsupervised learning, Bayes rule, GMMs, K-means, EM, PCA, and hierarchical clustering is part of the MLCB modeling arc.
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

- [[gene-expression-matrix]]
- [[rna-seq]]
- [[k-means-clustering]]
- [[gaussian-mixture-model]]
- [[expectation-maximization]]
- [[pca]]
- [[umap]]
- [[t-sne]]

### Cluster Membership

- [[cluster-map-genomics]]
- [[cluster-map-classical-ml]]

### Key Relationships (from KG)

See [[lecture-entity-map]] for the full relationship list, and [[knowledge-graph-index]] for the global entity index.
