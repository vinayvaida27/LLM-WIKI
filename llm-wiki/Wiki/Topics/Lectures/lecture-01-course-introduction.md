---
tags:
  - "topic"
topics:
  - "MLCB"
status: updated
created: 2026-05-24
updated: 2026-05-24
sources:
  - "Raw/Sources/lecture_01_course_introduction.md"
source_count: 1
aliases:
  - "Lecture 1 - Course Introduction"
---

# Lecture 1 - Course Introduction

## Source
- Raw source: `Raw/Sources/lecture_01_course_introduction.md`
- Supporting source: `Raw/Files/lecture_01_course_introduction.md`
- Existing related pages: [[mlcb-2024-computational-biology]], [[mlcb-complete-study-guide]], [[mlcb-methods-map]]
- Last updated: 2026-05-24

## Executive Summary
Lecture 1 - Course Introduction develops course framing, representation learning, self-supervision, latent spaces, GNNs, multimodal embeddings, and the axes of computation versus biology. This page intentionally preserves substantial source detail so a future LLM can reason from the wiki without immediately reopening the raw transcript.

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
- Introduction
- Goals of the Course
- Course at a Glance
- Why Computational Biology
- Why GenAI is different
- Representation Learning: Images + Genomes
- Graph Representation Learning in GNNs
- Language Representation Learning in LLMs
- Visualizing Z vector Embedding Landscapes
- The Road Ahead

## Detailed Lecture Notes
The notes below preserve the processed source order and are intentionally detailed.

# Lecture 1: Course Introduction

Video: [MLCB24 Lecture01 Introduction](https://www.youtube.com/watch?v=1zZSPeKGRzw&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=1&t=2795s)

Slides: [Lecture01_Introduction_FA24.pdf](https://www.dropbox.com/scl/fi/a8lvwo912g31gmsk4461w/Lecture01_Introduction_FA24.pdf?rlkey=eoedwmsnc7ju1zycvmj9hp2p4&dl=0)

## [00:00](https://www.youtube.com/watch?v=1zZSPeKGRzw&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=1&t=0s) Introduction

Welcome to the 2024 edition of our **Computational Biology** class! This course will provide a comprehensive overview of key topics in both biology and computational methods, combining foundational knowledge with cutting-edge developments in the field. Throughout the semester, we'll delve into **genomics, epigenomics, disease circuitry, protein structure, immunology, imaging, single-cell analysis, gene regulation, and network modeling**, among other topics. Our aim is to equip you with the theoretical background and practical skills needed to tackle complex biological problems through computational approaches.

### Class Structure:

**Lectures**: Held every Tuesday and Thursday from 1:00 to 2:30 PM.

**Recitations**: Scheduled on Fridays at 3:00 PM in the same room, where we'll dive deeper into lecture content and address any questions. If you cannot attend, recordings will be made available.

### Course Goals:

- Understand key principles of **machine learning** and **algorithm design**.
- Explore influential problems and techniques in **computational biology**.
- Analyze large-scale biological datasets to uncover insights relevant to **human disease** and **drug discovery**.
- Master genome analysis, including **sequence alignment**, **regulatory motifs**, and **epigenomic modifications**.
- Gain expertise in **gene expression**, **network modeling**, and **RNA analysis**.
- Learn about evolutionary principles through **comparative genomics** and **phylogenetics**.
- Investigate the connection between **genetic variation** and **disease**.
- Transition from linear sequences to complex structures, including **protein folding** and **ligand binding**.

We will cover both traditional machine learning techniques like **Gibbs sampling**, **expectation maximization**, and **hidden Markov models**, as well as modern advancements in **deep learning** and **generative AI**, including **graph neural networks** and **deep generative models**.

### Faculty and Teaching Staff:

**Manolis Kellis**: Professor in AI and Computer Science at MIT, and a member of the Broad Institute of MIT and Harvard, specializing in genomics, disease circuitry, epigenomics, and protein structure.

**Eric Alm**: Co-instructor, known for his work on the microbiome and generative AI, bringing a deep understanding of both computational and biological sciences.

**Teaching Assistants**: Jared, Sarah, and Dan, who bring a wealth of experience in language models, evolutionary prediction, and single-cell genomics.

### What to Expect:

This class will be fast-paced and highly interactive. We expect you to engage actively with the material, participate in discussions, and collaborate on projects.

WeÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ve structured the course to maximize your learning and provide ample opportunities for you to apply what you learn through **innovative final projects** that often lead to new research directions, papers, and future career paths in computational biology.

### Resources and Logistics:

**Course Website**: All materials, schedules, and announcements will be available at compbio.mit.edu/mlcb

**Survey**: Please fill out the initial survey to help us tailor the course content to your interests and needs. It will also aid in forming project teams that align with your goals.

This course is designed not just to teach you, but to inspire you to push the boundaries of what is possible in computational biology. We look forward to exploring these exciting topics together!

## [10:21](https://www.youtube.com/watch?v=1zZSPeKGRzw&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=1&t=621s) Goals of the Course

The primary goals of this course are to provide a comprehensive introduction to **computational biology**, focusing on both the foundational problems and the algorithmic and machine learning techniques that are crucial for data analysis. The skills and methods you will learn are not only applicable to computational biology but also extend to any field of applied data science where real-world challenges, such as noisy data, complex models, and the need for approximation and summarization, are prevalent. Our aim is to equip you with the ability to build meaningful representations of the world and to think critically about how these representations are constructed.

One of the most exciting aspects of this course is that the field is constantly evolving. We're not just exploring established concepts from the past; we're diving into cutting-edge discoveries and innovations that are unfolding right now. By the end of the course, you will be familiar with methods and ideas that are still being refined and discovered. This dynamic environment is what makes teaching and learning computational biology so thrillingÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂitÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s a living field, continuously shaped by ongoing research and new findings.

Our goal is not merely to teach you how to use existing tools or software packages. Instead, we focus on explaining **how and why** these methods work, enabling you to think algorithmically and from a machine learning perspective. This deeper understanding will empower you to design the next generation of computational methods, rather than just using those that already exist.

A second key objective is to prepare you to tackle independent research. The course is structured around milestones that will guide you through a final project, allowing you to engage with the latest research literatureÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âoften involving papers that are only weeks old. You will have the opportunity to work directly with real data and code from recent publications, exploring questions at the frontiers of the field. Programming assignments and hands-on exercises will challenge you to design parts of algorithms, implement them, and observe their performance in practical scenarios.

The final project is an essential component of the course. You will propose, execute, and present your own research, both in writing and through oral presentations. This experience will not only consolidate your learning but also position you to contribute novel insights to the field.

We like to think of this course as existing along four axes: **computation and biology** on one side, and **foundations and frontiers** on the other. On one hand, we are deeply invested in solving real biological and medical problems, not just developing biologically inspired algorithms. On the other hand, we emphasize computational fundamentals, equipping you with tools from AI, machine learning, and statistical analysis that can be broadly applied.

The second duality of the courseÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âfoundations and frontiersÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âmeans that we aim to balance well-established knowledge with exposure to the latest developments. Typically, each module will start with foundational concepts and gradually transition to more advanced, cutting-edge topics. This approach ensures that you not only gain a solid grounding in the essential theories but also stay informed about the evolving landscape of computational biology.

Everyone should have a handout that outlines the course content at a glance. If you donÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t have one, please raise your hand, and weÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll get one to you. This guide will help you navigate the structure of the course and keep track of the topics weÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll be covering throughout the semester.

## [13:52](https://www.youtube.com/watch?v=1zZSPeKGRzw&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=1&t=832s) Course at a Glance

The **Course at a Glance** provides an overview of the entire semester, outlining the key modules, assignments, and important milestones. At the center of this structure, we have the main schedule, broken down into weeks marked by alternating light and dark blue rows. The course is divided into four modules, each spanning several weeks: Module 1 (Weeks 2-4), Module 2 (Weeks 5-7), Module 3 (Weeks 8-10), and Module 4 (Weeks 11-13). Each module will come with a problem set (P-set), which will be distributed as the module begins and due at the end of the module, right before the next one starts. This design ensures that you are always working on current material, without needing to recall content from weeks past while handling new topics.

There are only three P-sets corresponding to the first three modules. Module 4 will not have a P-set but will lead into the quiz, which covers only Modules 1, 2, and 3. Module 4 content, although not included in the quiz, remains important as it could be relevant for your final projects. The P-sets are structured to directly align with the content of each module, ensuring a synchronized learning process. In addition to these assignments, there is also a "Homework 0" designed to get you comfortable with the computational tools we'll be using, such as Jupyter Notebooks, PyTorch, BioPython, and other essential packages. This initial assignment aims to level the playing field, providing everyone the foundational skills required for the rest of the course.

Fridays will often include mentoring sessions or recitations, especially useful for helping you navigate the milestones associated with your final project. These milestones are spaced at the end of every second week, guiding you through the various stages of your project from forming teams to refining your research proposal. The first milestone involves creating a self-profile and recording an introductory videoÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âboth designed to ease you into the project phase and help with team formation. Subsequent milestones include selecting key papers, assessing the feasibility of your project, and making sure you can access necessary data and tools before diving deeper into the work.

As the semester progresses, additional milestones will serve as checkpoints where youÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll present updates and receive feedback, allowing for adjustments and refinements. One crucial milestone is the mid-course report, scheduled after the quiz. This report functions as a draft of your final project write-up, helping you outline your progress and identify any remaining gaps well before the final submission. Your completed project will be due on the Friday before our last class, with presentations scheduled for the following Tuesday. This timeline is designed to prevent last-minute rushes and ensure that you have ample time to prepare a polished final presentation.

The four modules cover a wide range of topics:

- **Module 1:** Focuses on **genomics, epigenomics, single-cell analysis, and regulatory networks**, providing a deep dive into data that could easily constitute an entire semester on its own.
- **Module 2:** Shifts to **protein structure, protein language models, and geometric deep learning**, exploring the structural and functional complexities of proteins.
- **Module 3:** Covers **chemistry and therapeutics**, including graph neural networks, drug discovery, and molecular interactions, expanding the computational toolkit to tackle challenges in drug development.
- **Module 4:** Wraps up with **electronic health records, imaging, comparative genomics, and metabolomics**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âareas that each represent their own specialized fields of study.

Throughout the course, the emphasis will be on active learning through project-based experiences, where youÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll explore real-world data and state-of-the-art methods. YouÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ll be encouraged to engage with the material in a hands-on way, learning not just from the lectures but also through collaborations with your peers, Tas, and mentors. The goal is not only to master current computational tools but also to gain the skills necessary to innovate and push the boundaries of what is possible in computational biology.

The upcoming sections of the lecture will dive deeper into the specific content of each module and highlight the exciting topics we'll explore together this semester.

## [29:40](https://www.youtube.com/watch?v=1zZSPeKGRzw&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=1&t=1780s) Why Computational Biology

Computational biology leverages the power of computation to address the complexity of biological systems that cannot be easily captured by traditional mathematical equations alone. Biology is inherently **hacky**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âit evolves through a series of tweaks, mutations, and optimizations rather than following a simple, elegant formula like those seen in physics. Biological systems are built from decentralized processes, emerging behaviors, and intricate feedback loops that are not well suited to classical mathematical modeling but can be better understood through computational simulations and machine learning.

**Data and Computation** play a crucial role in biology due to the sheer **volume of data** generated, particularly with advancements in genomics, proteomics, and other high-throughput techniques. The **iterative process** of hypothesis generation, testing, and refinement becomes far more efficient when supported by computational models, which can run thousands of simulated experiments in the time it takes to perform a single biological experiment in the lab. This approach not only saves time but also reduces the need for ethical dilemmas associated with animal testing and human trials.

Furthermore, the **language of biology**, particularly DNA and RNA, is a **programming language** of its own, vastly different from human languages. Computation allows us to decipher this ancient code, translating sequences into functional molecules, protein interactions, and ultimately, phenotypes. By simulating these processes computationally, we can better understand how genetic information is translated into biological functions and how errors in these processes can lead to diseases.

Computational approaches also offer a way to explore **new hypotheses** that might not be immediately intuitive to human researchers. These models can reveal hidden patterns, suggest novel connections, and even propose mechanisms that researchers might overlook. This ability to look beyond human biases and preconceptions opens up new avenues for discovery, pushing the boundaries of our understanding.

Another critical aspect is the **error-prone nature of biological and technical measurements**. Biology is filled with both intrinsic variability and measurement noise. Computational models help to **distill** the signal from the noise, allowing researchers to extract meaningful insights from complex, high-dimensional data. This capability is crucial in fields like genomics, where patterns are often obscured by the sheer volume of data.

In summary, computational biology serves as a bridge between the raw, unstructured nature of biological data and the structured, analytical world of computation. By combining big data, sophisticated algorithms, and iterative modeling, computational biology enables us to tackle some of the most challenging questions in science todayÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âfrom decoding the human genome to designing next-generation therapeutics. ItÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s a field where the frontier of knowledge is constantly expanding, driven by the interplay of biology, computation, and innovation.

## [43:20](https://www.youtube.com/watch?v=1zZSPeKGRzw&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=1&t=2600s) Why GenAI is different

This year feels fundamentally different because of the advent of **generative AI** and specifically **representation learning**, which goes beyond mere pattern recognition to grasp deeper meaning within biological data. Unlike earlier AI models that were restricted to recognizing superficial patterns, generative AI and deep learning are enabling machines to **understand complex biological languages**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âfrom the folding of proteins and the intricate chemistry of drug molecules to the genomic sequences that dictate cellular function and the regulatory codes that control gene expression.

Traditional AI has been around for decades, often dismissed as simply benefiting from more data and better computational power. However, **representation learning** is not just about scaling up old techniques; it's about creating models that capture **emergent properties**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âcapabilities that were not explicitly programmed. These models donÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t just process data; they learn nuanced, hierarchical abstractions that reflect real-world complexities.

For example, deep learning models can interpret the **language of protein folding**, recognizing how amino acid sequences translate into three-dimensional shapes and ultimately into functional molecules. They can parse the **language of genomes**, understanding how specific sequences and motifs govern gene regulation, and how these genetic elements interact to orchestrate cellular behavior. Similarly, they are beginning to comprehend the **language of disease and health**, identifying pathways and mechanisms that drive pathological states, all through vast amounts of biological data that no human could parse unaided.

One of the key breakthroughs of generative AI is its ability to build **foundation models**. These are large, self-supervised models trained on massive datasets that allow them to learn representations that are useful across a wide range of tasks. Foundation models possess **emergent capabilities**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthey can make connections and generate insights that were not directly encoded during training, which is why this era of AI feels profoundly different.

**Self-supervised learning** is at the heart of this transformation. Unlike traditional models that rely on human-annotated data, foundation models are trained by hiding parts of their input and learning to predict the missing pieces. This forces the model to develop an understanding of the underlying data structure, learning everything from basic patterns to complex, abstract concepts. For instance, in language models, initial understanding might come from word frequencies, but deeper learning would capture grammar, context, emotions, and subtleties of human interactionÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âreaching insights that even humans might overlook.

These models are also becoming **multimodal**, capable of interpreting and integrating information from multiple data types simultaneously. Just as models like ChatGPT can blend text and images, new foundation models are being developed to connect **protein structure** and **protein function**, merging 3D molecular geometry with biological descriptions to facilitate novel insights. This capacity to cross domains is key: integrating chemical structures with knowledge graphs, or connecting patient trajectories from clinical notes to structured health data, opens unprecedented opportunities for discovery.

Generative AI and deep learning are thus poised to **transform our understanding of biology** by linking the vast, disconnected pieces of biological knowledge into coherent, interpretable models. Through **hierarchical concepts** and **deep learning**, these models can build layer upon layer of understanding, revealing new insights about disease mechanisms, drug interactions, and much more.

This is why generative AI feels revolutionary: it is not just a new tool but a new way of thinking, capable of expanding human knowledge by interpreting the fundamental codes of life in ways that were previously unimaginable.

## [57:30](https://www.youtube.com/watch?v=1zZSPeKGRzw&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=1&t=3450s) Representation Learning: Images + Genomes

Representation learning, a cornerstone of modern machine learning, transforms how both images and genomes are interpreted by AI. Imagine an AI system analyzing an image of a person carrying a backpack. The process begins with **pixels**, the basic units of a digital image, just as the human retina captures light. These pixels are processed by neurons that recognize fundamental visual features like **edges**, colors, and simple patternsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthe first layer of representation learning. From there, the AI builds progressively more complex features: from lines and shapes to identifiable objects like eyes, wheels, or noses. Ultimately, these layers of abstraction allow the AI to comprehend the entire scene as a person with a backpack.

What makes this revolutionary is that these **representations are not pre-programmed** by human engineers; they are learned directly by the machine. The AI is set loose on vast amounts of data and learns by itself which features are most useful for distinguishing objects in the world, from cars and animals to complex scenes involving human activity. This form of self-directed learning represents a significant departure from earlier AI systems, which relied heavily on predefined rules and hardcoded patterns. Instead, the AI learns its own rules for representation at each level of abstraction, building upon the patterns recognized in previous layers.

The **core innovation** here isn't just the increase in data, computation, or model size; it's the shift towards learning representations directly from data, a concept that didn't exist in early AI systems. The transformation from raw inputs (X) to outputs (Y) has always been central to machine learning, but what sets modern deep learning apart is the **latent space (Z)**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthe hidden layer of **embedding representations** that captures the underlying structure of the data. This latent space serves as a bridge between raw data and the final output, allowing the AI to make sense of complex inputs through layers of learned features.

In image recognition, for example, convolutional neural networks (CNNs) scan images using filters that identify matching patterns at different levels of complexity. At the lowest level, these filters find basic patterns like lines; at higher levels, they recognize increasingly complex shapes and objects. This **hierarchical learning of representations** is what enables the AI to effectively interpret visual information.

The same principles can be applied to genomic data. In genomics, the AI treats DNA sequences much like an image, encoding them in a way that makes **patterns recognizable**. DNA can be represented as a series of four bases (A, C, G, T), each acting like a pixel in a 2D image with only four possible colors. By analyzing these sequences, the AI looks for repeated motifs or structures that resemble patterns in images, such as transcription factor binding sites or regulatory elements. These patterns are critical for understanding how genes are regulated, expressed, and how they contribute to cellular functions.

Representation learning thus bridges the gap between diverse data typesÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âwhether visual images or genetic sequencesÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âby enabling the AI to identify the key features that drive meaningful distinctions. This approach underpins the advances in generative AI, making it possible for machines not only to classify data but to **understand and generate new data**, mimicking the underlying rules and complexities of natural systems.

## [1:03:19](https://www.youtube.com/watch?v=1zZSPeKGRzw&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=1&t=3799s) Graph Representation Learning in GNNs

Graph Representation Learning is a powerful extension of the principles of representation learning applied to images and genomes, but adapted for complex data structures like graphs. In the context of chemistry, molecules are essentially graphs, where atoms are nodes and chemical bonds are edges connecting these nodes. Unlike the structured grid of pixels in a 2D image or the linear sequence of a genome, graphs are inherently irregular and flexible, making them ideal for representing the intricate connections in chemical compounds.

To learn representations on graphs, we start with **Graph Neural Networks (GNNs)**, which apply the same hierarchical learning principles used in image and sequence analysis. The goal is to iteratively build higher-level abstractions from the basic building blocks of the graphÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âin this case, the atoms and their connections.

At the **first layer**, each atom is represented with its intrinsic properties: **hydrophobicity**, **charge**, **polarity**, etc. These properties form the **initial representation** of each node in the graph. The next step involves building **layer one representations** by considering how each atom is positioned relative to its neighbors. For instance, a charged atom surrounded by two polar atoms would form a distinctive pattern, contributing to the atom's new representation in the context of the molecule.

As we progress through layers, each node (atom) aggregates information from its neighbors. **Layer one aggregates** data from direct neighbors, while **Layer two** incorporates information from neighbors of neighbors, and so on. This process allows the network to capture increasingly complex interactions within the graph, ultimately creating a **latent representation** of the entire molecule. This abstract, multi-layered representation can then be used to predict properties of the molecule, such as its chemical reactivity, toxicity, or its effectiveness as a therapeutic agent.

This **bottom-up learning approach** allows GNNs to dynamically understand the spatial and relational properties of molecules, much like how convolutional networks learn features in images. By progressively integrating local neighborhood information, GNNs can discern patterns in how atoms and their interactions influence overall molecular function.

The power of this method extends beyond chemistry; it can be used in various fields where relationships and structures are best captured by graphs. For instance, in biology, GNNs can be applied to **protein-protein interaction networks**, **gene regulatory networks**, or **metabolic pathways**. In a drug discovery context, GNNs can correlate the learned representations of chemical compounds with the diseases they affect, enabling predictive models that guide therapeutic design. This ability to model complex, interconnected data makes GNNs a versatile and transformative tool in modern computational biology.

## [1:06:07](https://www.youtube.com/watch?v=1zZSPeKGRzw&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=1&t=3967s) Language Representation Learning in LLMs

Language models, particularly Large Language Models (LLMs), have revolutionized how we process and understand language by employing sophisticated representation learning techniques. At the foundation of this approach is the concept of representing each word with a **ground-level embedding** that captures its contextual meaning based on its usage across vast corpora of text.

The basic idea begins with **predicting missing words** in sentences, which allows models to learn the contextual representation of words. For example, if the missing word is "President," the surrounding context might be similar to that of words like "king," "leader," or "God." This similarity in contexts means these words will be close together in the **embedding space**, which is the foundational principle behind early language models like **Word2Vec**. This approach clusters words with similar meanings, capturing semantic relationships just through exposure to text.

However, the real power emerges when we move beyond representing single words to understanding the **meaning of entire sentences or documents**. This is where **attention mechanisms** and **Transformer architectures** come into play. By dynamically adjusting the representation of each word based on the surrounding context, Transformers can capture nuanced meanings that evolve with each wordÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s neighborhood in the text. For instance, the word "Apple" in a sentence can shift its meaning from a fruit to a tech company depending on whether it appears with words like "basket" or "Windows." This context-dependent representation is the core innovation of **Transformer models**.

**Attention mechanisms** allow models to focus selectively on different parts of a sentence when constructing the meaning of each word, dynamically reshaping its **latent embedding** based on the surrounding text. This enables models to grasp complex sentence structures and subtle semantic shifts, thus moving from basic word embeddings to deeper, contextualized representations that reflect the full meaning of sentences, paragraphs, or even entire documents.

A striking feature of modern LLMs is their **multimodal capabilities**, where they seamlessly integrate different types of dataÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âsuch as images and textÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âinto a shared representation space. For instance, you can input an image into an LLM, and it can describe what it sees in natural language. Conversely, it can generate images based on textual descriptions, bridging the gap between visual and linguistic information. This joint learning of text and images allows for versatile applications, such as interpreting complex scientific figures or generating novel visuals from descriptions.

This **multimodal embedding space** extends beyond simple image-text pairs; it can encompass representations of proteins, chemicals, genomic sequences, and more, linking them to their functional or descriptive language counterparts. Each point in this space has both a language and a corresponding structural or visual projection, allowing models to navigate seamlessly between different forms of data.

By leveraging these deep, hierarchical, and context-sensitive representations, LLMs enable us to extract, generate, and understand information across diverse fieldsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âfrom protein folding to chemical interactions and beyond. This makes them invaluable tools not only in computational biology but in any domain that requires the interpretation of complex, multidimensional data. For your final projects, consider exploiting these capabilities to merge language with other forms of data, creating innovative solutions that push the boundaries of what these models can achieve.

## [1:09:29](https://www.youtube.com/watch?v=1zZSPeKGRzw&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=1&t=4169s) Visualizing Z vector Embedding Landscapes

Understanding the hidden, complex relationships in data often comes down to visualizing the **latent space**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthe Z vectorsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthat generative AI and deep learning models create. These vectors, formed through layers of abstraction, encapsulate the hidden features that models learn. Rather than treating AI models as inscrutable black boxes, it's crucial that we actively explore these embeddings, visualizing them to uncover new insights and patterns.

In our research group, we've developed an interactive tool that projects these latent embeddings into two dimensions, allowing us to visually explore complex datasets. For instance, we took the 155,000 papers that have cited our work and projected each into a latent embedding space using a large language model. By applying dimensionality reduction techniques such as **t-SNE** or **UMAP**, we can map these high-dimensional representations into two-dimensional clusters, revealing thematic relationships among the papers that might otherwise remain hidden.

The same approach can be applied broadly across various fields: visualize latent spaces of chemicals, proteins, gene expression patterns, or even entire knowledge domains. The key is to look not at the raw data (X space) or the output (Y space) but to immerse ourselves in the Z space, the world of learned representations.

By overlaying these representations with multimodal data, we can start to see new structures emerge. For example, plotting patient data with Alzheimer's disease against gene expression profiles can reveal distinct axes of variationÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âlike cognition and pathology. Each axis can be associated with specific cell types or genetic expressions, providing new insights into how diseases manifest at the cellular level.

A similar approach has been used to co-embed protein structure and function. In a collaborative project, we combined a **knowledge graph** that connected genes, diseases, drugs, and biological functions with graph convolutional neural networks. This approach allowed us to map drugs, proteins, and phenotypes into a shared latent space, providing a unified view where structural data could directly inform functional insights. This emerging capability to **translate between structure and function** is a step towards bridging gaps like those left by AlphaFold, which solves sequence-to-structure but not structure-to-function.

These techniques are not just limited to biology. We've used them to explore vast collections of textual data, such as the New York Times archive, creating cognitive maps that reveal hidden connections among millions of articles. The same methods can be applied to map scientific literature, grants, and patents, linking them together in ways that reflect their underlying semantic and functional relationships.

**Cognitive maps**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âwhether for exploring physical terrain or navigating complex datasetsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âprovide essential simplification and abstraction. They help anchor our understanding, guiding decision-making and sparking new hypotheses. As we progress, the visualization of these latent spaces will be key to unlocking the deeper insights hidden within our data, making this exploration a vital frontier for the field of computational biology and beyond.

## [1:16:50](https://www.youtube.com/watch?v=1zZSPeKGRzw&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=1&t=4610s) The Road Ahead

The landscape of computational biology is undergoing a profound transformation driven by the convergence of multimodal, multi-layer, and hierarchical deep representations of complex biological data. This shift is allowing us to unify the study of diverse data typesÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âfrom genomes and regulatory circuits to proteins, images, and chemicals. We are no longer limited to studying these elements in isolation; we can now interconnect them in ways that were once unimaginable. This class used to focus solely on genomes and circuits, but now it encompasses proteins, 3D structures, chemical compounds, and more. Why? Because it's not only feasibleÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂitÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s transformative for our understanding of biology.

This semester, we will dive deep into the frontiers of **representation learning**, dissecting how these powerful models can capture the essence of complex biological phenomena. Our journey will be structured into four main modules:

- **Module 1:** We'll explore gene expression, regulatory networks, epigenomes, and single-cell analysis. This module will set the foundation for understanding how genes are controlled and how cellular decisions are made at the molecular level.
- **Module 2:** We'll connect the regulatory information from Module 1 to protein structure, delving into protein language models, geometric deep learning, and how structure informs function.
- **Module 3:** We will shift to chemistry and therapeutics, focusing on graph neural networks and how they can predict the behavior of small molecules, aid in drug discovery, and model complex biochemical interactions.
- **Module 4:** Finally, we'll tackle imaging, electronic health records, comparative genomics, evolution, and metabolomics, integrating these diverse data types into cohesive models that can transform our understanding of health and disease.

As we cover these themes, I encourage you to **think boldly and creatively** about your final projects. Pull inspiration from any module or combination of modules and design the most ambitious, forward-thinking project you can imagine. The tools we are learning can finally make these ideas a reality. For many of the challenges I've wanted to tackle since I was in your shoes, the technology has now caught up, and we can finally push the boundaries together.

So, take this opportunity to explore, experiment, and potentially change the world. No pressureÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âbut the possibilities are endless, and we are here to guide you every step of the way.

Who's excited? LetÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s do this!

See you all tomorrow for the recitation on problem set zeroÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âget started on the survey and start brainstorming your project ideas. This is just the beginning.


## Verified Backlog Coverage: L01_T001-L01_T015
This section records the first schema-preserving deep-update batch for Lecture 1. The items below are verified against `Raw/Sources/lecture_01_course_introduction.md` and should be treated as source-grounded expansions of the lecture page, not as a replacement for the detailed transcript-style notes above.

### L01_T001 - Data-driven vs. hypothesis-driven paradigms
The lecture frames computational biology as a field where traditional hypothesis-driven science is strengthened by data-driven modeling. The professor does not present data-driven work as a replacement for biological reasoning. Instead, computation expands the set of hypotheses a researcher can consider, especially when biological systems are too noisy, high-dimensional, or interconnected for intuition alone. This theme connects directly to [[data-driven-vs-hypothesis-driven-paradigms]], [[representation-learning]], and later disease-mechanism lectures where statistical signals must be converted back into testable biology.

### L01_T002 - Representation learning across images, genomes, and graphs
[[representation-learning]] is introduced as the course's core computational language. The same conceptual move appears across images, [[dna|DNA]] sequences, molecules, biological networks, and scientific text: start from raw observations, learn useful intermediate representations, and use those representations to predict or interpret biological function. In images, this means moving from pixels to edges to objects. In genomics, it means moving from bases to motifs and regulatory elements. In graphs, it means moving from atoms or nodes to neighborhood-aware graph embeddings.

### L01_T003 - Graph Neural Networks and Large Language Models
Lecture 1 places [[graph-neural-networks]] and LLM-style representation learning in the same broad family: both build context-sensitive embeddings from structured inputs. A [[graph-neural-networks|Graph Neural Network]] updates each node by aggregating information from neighboring nodes, while language models update token representations from surrounding context. This prepares students for later lectures where molecules are graphs, biological networks are graphs, and protein or DNA sequences are treated as biological languages.

### L01_T004 - Classical ML plus deep learning
The course explicitly includes older probabilistic and statistical methods such as Gibbs sampling, [[expectation-maximization]], and [[hidden-markov-models]], alongside deep learning and generative models. This matters because the course is not a simple march from "old" to "new." Methods are chosen for their assumptions: HMMs are useful when hidden states and local sequential dependence matter; EM is useful when latent assignments must be inferred; deep learning is useful when representations are too complex to hand-design.

### L01_T005 - GNNs and deep generative models
The lecture links [[graph-neural-networks]] to deep generative modeling by showing that molecules and biological networks can be represented as structured objects rather than flat feature vectors. A GNN can learn a molecule's latent representation from atom and bond neighborhoods, and a generative model can use learned latent spaces to suggest new structures or hypotheses. This is the early conceptual bridge to Lecture 14 on chemistry GNNs and Lecture 15 on molecular generation.

### L01_T006 - Computation vs. biology and foundations vs. frontiers
The professor defines the course around two axes: computation versus biology, and foundations versus frontiers. The point is not to teach algorithms in isolation or biology as vocabulary. The course repeatedly asks how a biological problem becomes a computational representation, and how a computational result becomes a biological interpretation. See [[computation-vs-biology-and-foundations-vs-frontiers]] for this framing.

### L01_T007 - Four course modules
Lecture 1 presents the semester as four connected modules. Module 1 covers genomics, epigenomics, single-cell analysis, and regulatory networks. Module 2 moves into protein structure, protein language models, and geometric deep learning. Module 3 shifts to chemistry, therapeutics, and molecule-level graph learning. Module 4 connects genetics, disease, and mechanism. This structure is the backbone of [[mlcb-2024-computational-biology]] and [[mlcb-cross-lecture-connections]].

### L01_T008 - Biology as a noisy, decentralized system
The professor emphasizes that biology is not a clean engineered system. It is historically evolved, decentralized, redundant, and full of feedback loops. This is why the course needs statistical modeling, simulation, representation learning, and careful validation. A method that performs well on a benchmark may still miss biological mechanism if it ignores noise, cell context, tissue context, or experimental artifacts.

### L01_T009 - Computational acceleration of hypothesis testing
Computational biology can run many candidate explanations before an expensive wet-lab experiment is attempted. The lecture frames this as an acceleration of hypothesis generation and filtering, not as a replacement for experiments. This idea reappears in drug discovery, where models prioritize molecules, and in genetics, where computational priors prioritize variants and loci for validation.

### L01_T010 - DNA and RNA as biological language
The lecture describes [[dna|DNA]] and [[rna|RNA]] as code-like biological languages. That analogy is useful because sequences have syntax-like patterns, local motifs, long-range dependencies, and functional outputs. The analogy is also limited: DNA is not human language, and biological meaning depends on cell state, chromatin, protein binding, and evolutionary context. Later DNA language model lectures build directly on this framing.

### L01_T011 - Signal vs. noise in biological measurement
Lecture 1 makes noise a central reason for computation. Biological measurements contain technical noise, intrinsic biological variation, sampling noise, and hidden structure. A computational method must separate useful signal from nuisance variation without erasing real biology. This prepares the learner for clustering, single-cell QC, differential expression, HMM state inference, GWAS confounding control, and model validation.

### L01_T012 - From pattern recognition to generative AI and representation learning
The lecture distinguishes older AI pattern recognition from modern [[representation-learning]] and generative AI. The shift is that models increasingly learn internal abstractions rather than relying only on human-engineered features. In MLCB, this means models can learn useful representations of images, sequences, graphs, molecules, proteins, and multimodal biological knowledge.

### L01_T013 - Emergent properties in biological languages
The professor uses protein folding and biological languages as examples of emergent structure: a model may learn patterns that were not explicitly programmed. This matters because many biological functions arise from interactions across scale: bases form motifs, motifs regulate genes, genes form networks, amino acids fold into structures, and structures drive function. Representation learning is powerful when these levels are too complex to hand-code.

### L01_T014 - Self-supervised learning
[[self-supervised-learning]] is introduced as a way to learn from unlabeled data by hiding part of the input and training a model to predict it. This is a major reason foundation models work in biology: protein sequences, DNA sequences, molecular strings, and scientific text all contain internal structure. The model can learn useful embeddings before it is fine-tuned for a specific task.

### L01_T015 - Multimodal foundation models
The lecture introduces [[multimodal-foundation-models]] as models that connect different data types in a shared representation space. For MLCB, the important idea is that biological meaning may require connecting sequence, structure, chemical form, phenotype, and language. This anticipates later links among [[protein]], [[molecule]], [[drug-discovery-and-molecular-generation|drug discovery]], [[protein-structure-and-biological-language-models]], and [[dna|DNA]] sequence modeling.

## Biological Concepts
Key biological concepts are explained in the source-faithful notes above and cross-linked through entity pages such as [[dna|DNA]], [[rna|RNA]], [[gene|Gene]], [[gene-expression|Gene Expression]], [[protein|Protein]], [[enhancer|Enhancer]], [[promoter|Promoter]], [[chromatin|Chromatin]], [[snp|SNP]], [[variant|Variant]], [[eqtl|eQTL]], and [[heritability|Heritability]].

## Machine Learning / Computational Concepts
Relevant computational ideas include [[representation-learning]], [[self-supervised-learning]], [[latent-space]], [[multimodal-foundation-models]], representation choice, objective functions, inference, optimization, graph/message-passing structure, sequence modeling, and validation. See [[mlcb-methods-map]].

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
### Q1. Why does the course combine older probabilistic methods with deep learning?
Older methods such as [[expectation-maximization]] and [[hidden-markov-models]] make assumptions explicit, while deep learning can learn richer representations when hand-designed features are not enough.

### Q2. What does it mean to treat DNA and RNA as biological languages?
It means sequence patterns can carry functional meaning, but the analogy must be grounded in biology: chromatin, cell state, protein binding, and evolution all change how sequence is interpreted.

### Q3. Why is representation learning central to the course?
[[representation-learning]] is the bridge from raw biological measurements to computable features. It lets models learn useful intermediate structures from images, genomes, graphs, proteins, molecules, and text.

### Q4. How does a GNN fit the course framing?
A [[graph-neural-networks|Graph Neural Network]] learns from objects whose relationships matter, such as atoms connected by bonds or genes connected in networks. It builds node and graph representations by aggregating neighborhood information.

### Q5. Why is biology described as noisy and decentralized?
Biological systems evolved through many local changes rather than a clean top-down design. Measurements also contain technical and biological noise, so computational models must separate signal from noise carefully.

### Q6. What are the two course axes?
The course balances computation with biology and foundations with frontiers. Students learn both reusable methods and the biological problems those methods are meant to illuminate.

### Q7. What makes self-supervised learning useful in biology?
[[self-supervised-learning]] can learn from abundant unlabeled data by predicting hidden parts of an input, such as missing words, sequence tokens, or structural patterns.

### Q8. What is the role of latent space?
[[latent-space]] is the learned intermediate representation between raw input and output. It can organize proteins, molecules, sequences, papers, or patients so hidden relationships become easier to inspect.

### Q9. How does computational biology accelerate hypothesis testing?
Models can prioritize hypotheses, variants, molecules, or mechanisms before expensive laboratory validation. They reduce the search space, but experiments remain necessary for causal claims.

### Q10. What is the big course-wide promise of multimodal foundation models?
[[multimodal-foundation-models]] may connect sequence, structure, text, chemistry, and phenotype in shared representations, helping future models move from isolated predictions toward biological explanation.

## Key Takeaways
- course framing, representation learning, self-supervision, latent spaces, GNNs, multimodal embeddings, and the axes of computation versus biology is part of the MLCB modeling arc.
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

- [[representation-learning]]
- [[latent-space]]
- [[self-supervised-learning]]
- [[multimodal-foundation-models]]
- [[data-driven-paradigm]]
- [[hypothesis-driven-paradigm]]
- [[graph-neural-network]]
- [[large-language-model]]
- [[gibbs-sampling]]
- [[expectation-maximization]]

### Cluster Membership

- [[cluster-map-foundations]]
- [[cluster-map-classical-ml]]
- [[cluster-map-deep-learning]]

### Key Relationships (from KG)

See [[lecture-entity-map]] for the full relationship list, and [[knowledge-graph-index]] for the global entity index.
