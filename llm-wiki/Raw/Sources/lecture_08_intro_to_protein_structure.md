---
Title: "lecture 08 intro to protein structure"
Author: "MLCB24"
Reference: "[Lecture08 - Intro to protein structure - MLCB24](https://www.youtube.com/watch?v=Hp3pjYaMsnU&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=8&t=2830s)"
ContentType:
  - "markdown"
Created: 2026-05-24
Processed: true
tags:
  - "source"
---

[[Lecture 8 - Intro to Protein Structure]]

Video: [Lecture08 - Intro to protein structure - MLCB24](https://www.youtube.com/watch?v=Hp3pjYaMsnU&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=8&t=2830s)

Slides: [Lecture08_IntroToProteinStructure.pdf](https://www.dropbox.com/scl/fi/o5ytgxu9huirhqmt2vvf9/Lecture08_IntroToProteinStructure.pdf?rlkey=1wo5k5p370k5kdepmnj7fy0sz&dl=0)

## [00:00](https://www.youtube.com/watch?v=Hp3pjYaMsnU&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=8&t=0s) Introduction

The focus of this module on protein structure brings together **computational and biological disciplines**â€”a merging that has significantly shaped modern bioinformatics and structural biology. This lecture is a personal and academic journey into protein structure, tracing the lecturer's evolution from an initial disinterest in biology, due to rote memorization, to a profound appreciation for evolutionary biology and genetics, spurred by a transformative realization about the **tree of life** and humanityâ€™s place within it.

With a strong background in **math and computer science**, the lecturerâ€™s shift toward biology began in college. Initial explorations in protein folding during graduate studies under **David Baker** introduced him to the **protein folding problem**â€”an inquiry into the time required for proteins to fold, which varies greatly depending on structural characteristics. This early work sparked a broader interest in biological functions beyond static genetic codes, driven by emerging technologies like the **Human Genome Project**. The excitement surrounding genome sequencing projects at the time involved discovering genes within vast nucleotide sequences and exploring potential applications, from human health to even unexpected uses in consumer products.

This course marks a **return to protein structure** for the lecturer, aiming to reconnect with and inspire an interest in **structural biology** among students. This lecture introduces **key themes in structural biology**:

- **Defining structural biology** and its importance in revealing function at the molecular level.
- **Case study on transcription factors**, specifically the LacI family, to illustrate practical applications.
- **Techniques for determining protein structures**, covering the main experimental and computational methods.
- **Principles of protein structure and comparison**, laying out foundational concepts.
- **Energy functions and physics**, essential for connecting structural biology with physics principles, and foreshadowing the use of **deep learning** in protein structure prediction.

The lecture highlights that **understanding energy functions** remains relevant even with advanced machine learning approaches. The interplay between **statistical mechanics** and deep learning showcases how models originally rooted in physics can translate into modern **neural networks** used in biological modeling, forming a bridge between **quantitative sciences and structural biology**.

This session serves as a gateway into **protein structure fundamentals** while setting the stage for upcoming discussions on **deep learningâ€™s transformative role** in protein structure prediction and the broader implications for biology and computational science.

## [9:48](https://www.youtube.com/watch?v=Hp3pjYaMsnU&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=8&t=588s) What is structural biology

**Structural biology** is the study of molecular structures to understand their function, particularly focusing on proteins. It involves both analyzing **pre-determined structures** to identify patterns (such as common features across enzymes) and **determining structures experimentally or computationally** to uncover specific details. The central challenge in structural biology, particularly for proteins, has been how to transition from a linear **protein sequence (derived from genomic data)** to a **three-dimensional structure**. Such a structure can then shed light on the moleculeâ€™s function, which is essential for understanding biological processes.

**Proteins** form the primary focus of structural biology, especially with advancements in **AI** over the past five years, which have made significant progress in protein structure prediction. Currently, we have around **200,000 experimentally-determined protein structures** and many more that have been **predicted computationally** with increasing accuracy. This vast dataset opens up the possibility of exploring structural patterns at scale.

The importance of structural biology lies in the fact that **we have extensive genomic data**, but the functional interpretation of much of this data remains elusive. If we could **convert all genomic sequences into structures**, and thus infer their function, we could vastly improve our understanding of the genome and its implications. Structural biology also has direct implications for **disease research**, as many disorders result from **protein misfolding**. Diseases like **Alzheimerâ€™s, Parkinsonâ€™s, Huntingtonâ€™s, and cystic fibrosis** are tied to the improper folding or aggregation of specific proteins, leading to cellular dysfunction. Similarly, conditions like **prion diseases** (e.g., Mad Cow Disease) highlight how misfolded proteins can even act as infectious agents, influencing the folding of other proteins.

Furthermore, **protein design** is an emerging field that leverages our understanding of structure and function to **engineer proteins with desired properties**. This field aims to create proteins that can perform specific reactions, bind to targeted molecules, or even inhibit harmful cellular processes. Recent breakthroughs in **deep learning** have enhanced the accuracy and potential of protein design, allowing scientists to conceptualize and build custom proteins for applications in **medicine, biotechnology, and synthetic biology**.

**Key resources** for visualizing and understanding protein structures include:

- The **Protein Data Bank (PDB)** for accessing structural data.
- **PyMOL** and other visualization tools for inspecting molecular structures, many of which now support **Python scripting** for advanced analysis.
- **AlphaFold** and **ESM Fold**, cutting-edge deep learning tools that have revolutionized structure prediction, offering databases of **pre-computed structures** accessible for research.

This overview sets the stage for understanding **structure-function relationships** in proteins and highlights the pivotal role that structural biology plays in both **basic science** and **applied research**. Through case studies and hands-on resources, students will explore how molecular structures can be visualized, analyzed, and designed, building a foundation for more advanced discussions on **predictive modeling** in the following lectures.

## [16:40](https://www.youtube.com/watch?v=Hp3pjYaMsnU&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=8&t=1000s) Using PyMOL for Structural Analysis of Transcription Factors

In structural biology, **understanding the relationship between a proteinâ€™s structure and its function** is crucial, and PyMOL is a valuable tool for visualizing these interactions. Here, we focus on a **transcription factor** from the **LacI family**, commonly found in prokaryotes, which features a **helix-turn-helix motif** for DNA binding. The goal is to explore how this protein binds DNA and controls gene expression, using PyMOL to uncover key structural details.

**Steps in PyMOL:**

1.  **Initial Structure and Crystal Duplication**: The visualized structure shows multiple copies of the DNA-protein complex due to the **x-ray crystallography process**, where protein molecules are crystallized in repeating units. To focus on a single protein-DNA complex, extraneous copies are removed by selecting specific chains (e.g., chain A and chain B).
2.  **Electrostatic Surface Analysis**: Generating **electrostatic surfaces** helps reveal regions with **net positive or negative charges**:
    - **Positive regions (blue)** likely interact with the **negatively charged DNA backbone** (phosphodiester bonds), suggesting where DNA binding occurs.
    - **Negative regions (red)** orient away from DNA due to charge repulsion.
3.  **DNA Binding and Major/Minor Grooves**: After hiding extraneous features, we examine how the **protein fits into the DNA double helix**. DNA features **two grooves**:
    - **Minor Groove**: Tighter with closer backbones.
    - **Major Groove**: More open, allowing transcription factors to access and bind DNA.
4.  **Helix-Turn-Helix Motif and Recognition Helix**:
    - The **recognition helix** is positioned in the **major groove**, enabling specific interaction with DNA bases. This helix, in close proximity to the DNA backbone, allows residues to make both **sequence-specific** contacts (recognizing particular DNA sequences) and **non-specific contacts** (stabilizing the interaction through backbone contacts).
    - **Conservation Across Species**: For residues interacting nonspecifically with the backbone, **high conservation** is expected, whereas residues involved in sequence specificity may vary.
5.  **Symmetry and Palindromic DNA Sequences**:
    - Because this transcription factor binds DNA as a **homodimer**, it binds to two separate DNA sites, often separated by about **10 base pairs**. This configuration requires the DNA binding sites to be **palindromic** to accommodate the symmetry of the homodimer.
    - **Recognition Motifs**: These palindromic motifs are conserved across various species and are used to identify **DNA binding motifs** in prokaryotic genomes.

By examining this transcription factor, PyMOL provides insights into the **physical and chemical principles** underlying DNA binding and transcriptional regulation. This example illustrates how structural biology tools can reveal **functionally significant structural features**, such as charge distribution, binding motifs, and protein symmetry, essential for understanding gene regulation.

## [31:45](https://www.youtube.com/watch?v=Hp3pjYaMsnU&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=8&t=1905s) Transcription factor-DNA binding and functional specificity

In **structural biology**, understanding how transcription factors (TFs) interact with DNA is essential for elucidating gene regulation mechanisms. This example focuses on the **helix-turn-helix motif** in transcription factors from the **LacI family**, illustrating how the structure of transcription factors influences their DNA-binding specificity and regulatory function.

### Helix-Turn-Helix Motif and Recognition Helix

In the LacI family, the **recognition helix** of the helix-turn-helix motif is positioned within the **major groove** of DNA. This positioning allows specific residues in the recognition helix to interact directly with the DNA bases, thereby determining the specificity of DNA binding. For example:

- In **PurR** and similar proteins, three critical residues in the recognition helix protrude into the DNAâ€™s major groove, where they make **specific contacts** with the DNA bases, determining the proteinâ€™s binding specificity.

By comparing different members of this transcription factor family, researchers identified that **three primary residues** are largely responsible for specificity. These residues allow some transcription factors to bind the same DNA sequences, while others target distinct sequences, depending on these key residue differences.

### Allosteric Regulation by Small Molecules

The **binding of small molecules** to transcription factors such as **LacI** or **PurR** alters their conformation, thereby influencing DNA binding. For instance:

- **LacI** binds lactose or a lactose derivative, which changes its structure, reducing its affinity for DNA and preventing it from binding to its operator sequence.
- This conformational shift means that **in the presence of lactose**, the LacI repressor is removed from the DNA, allowing transcription to proceed.

Each member of the LacI family often binds different small molecules (e.g., purines, carbohydrates) but has a similar regulatory effect, allowing cells to respond to specific environmental signals by turning on or off gene expression.

### Synthetic Applications: Designing Molecular Switches

The discovery that **changing these three specificity-determining residues** could transfer DNA binding specificity between transcription factors across species provides a foundation for designing **synthetic molecular switches**. By engineering these switches to respond to various cellular chemicals, scientists can potentially target them to specific genome regions, enabling precise control over gene expression.

### Operon Structure and Regulatory Binding Sites

On a genomic level, the layout of **genes, promoters, and operator sequences** is essential for regulatory control:

- In the **Lac operon**, LacI binds to its operator sequence downstream of the promoter, blocking **RNA polymerase** from initiating transcription of genes necessary for lactose metabolism (LacZ, LacY, and LacA).
- **Repressors**, such as LacI, typically bind downstream or overlapping with the promoter, physically blocking RNA polymerase from binding.
- **Activators**, in contrast, bind upstream of promoters, enhancing transcription by recruiting RNA polymerase to weak promoters, where the polymerase would otherwise have a lower affinity.

This hierarchical organizationâ€”from specific amino acid contacts in DNA-binding helices to operon-level gene layoutâ€”illustrates how structural elements at multiple scales collectively **determine the function** of transcription factors and their role in cellular regulation.

## [37:41](https://www.youtube.com/watch?v=Hp3pjYaMsnU&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=8&t=2261s) Experimental methods for determining structure

In **structural biology**, accurately determining the three-dimensional structure of proteins and protein complexes is crucial for understanding their function. Three primary experimental techniquesâ€”**X-ray crystallography**, **nuclear magnetic resonance (NMR)**, and **cryogenic electron microscopy (cryo-EM)**â€”are widely used to achieve this, each with distinct advantages, limitations, and suitability depending on the protein's size, stability, and the environment in which it functions.

### X-ray Crystallography

**X-ray crystallography** is often considered the gold standard for high-resolution protein structures. In this method, researchers must first grow a **high-quality crystal** of the protein. This process can be challenging because proteins naturally prefer to be in solution, and not all proteins readily form crystals. Often, scientists use complexes of proteins bound to DNA or ligands (such as drugs) to understand not only the protein structure but also how it interacts with these molecules.

Once a crystal is obtained, it is exposed to an **X-ray source**. As X-rays pass through the crystal, they are diffracted, creating a **diffraction pattern** on a detector. Each point in this pattern provides information about the electron density within the crystal, which represents the spatial distribution of atoms. The **electron density map** generated from this pattern can then be used to deduce the protein's 3D structure through a **Fourier transform**.

However, **phase information**â€”critical for constructing the electron density mapâ€”is lost during diffraction. To recover this phase information, researchers use techniques such as:

- **Heavy atom substitution**: Adding atoms with high electron densities (e.g., mercury or gold) to create differences that can help determine phases.
- **Molecular replacement**: Using the structure of a closely related protein as a template to estimate the phase information.

The resulting structure is characterized by its **resolution**, a key metric of quality. Higher resolution (indicated by smaller numbers, typically below 3 Ã…ngstroms) means more detailed and precise atomic positions. Some modern structures are determined at **sub-angstrom resolutions** (below 1 Ã…), allowing researchers to see nearly every atomâ€™s position in exquisite detail.

### Nuclear Magnetic Resonance (NMR) Spectroscopy

**Nuclear magnetic resonance (NMR)** spectroscopy offers a solution for studying proteins that cannot be crystallized. This technique is based on the magnetic properties of atomic nuclei, particularly hydrogen atoms in proteins. NMR is advantageous for examining proteins in **solution**, providing a more natural environment that is close to physiological conditions.

NMR spectroscopy measures **interatomic distances** by analyzing signals from hydrogen nuclei that are close to each other in space. By identifying pairs of hydrogen atoms that are close enough to interact, researchers can infer structural proximity and gradually construct a 3D model of the protein. This makes NMR particularly useful for proteins in which **dynamic flexibility** or **functional conformational changes** are essential aspects of their activity.

However, NMR is limited by:

- **Protein size**: Generally, NMR is most effective for smaller proteins (typically under 30 kDa), as larger proteins produce more complex spectra that are challenging to interpret.
- **Complexity**: Interpreting NMR spectra requires extensive computational processing to assign signals to specific residues and atoms, which can be time-consuming and computationally demanding.

Despite these challenges, NMR provides invaluable insights, especially for studying protein dynamics and interactions under near-physiological conditions.

### Cryogenic Electron Microscopy (Cryo-EM)

**Cryogenic electron microscopy (cryo-EM)** has revolutionized the field of structural biology in recent years, particularly for **large macromolecular complexes** that are difficult to crystallize, such as **viruses, ribosomes, and multi-protein assemblies**. In cryo-EM, samples are flash-frozen to preserve their native structure and then subjected to an electron beam in a transmission electron microscope.

Cryo-EM provides a **direct image** of large protein complexes, capturing them in various conformational states. The technique allows researchers to observe not only the architecture of individual proteins within a complex but also how these proteins fit together and function as a unit. The following features characterize cryo-EM:

- **Native state preservation**: The sample remains in a frozen, hydrated state, which can reveal natural conformations without the need for crystal packing constraints.
- **Large complex suitability**: Cryo-EM is ideal for proteins and complexes that are too large for NMR or difficult to crystallize, such as membrane proteins.

Cryo-EM images often reveal the overall shape and arrangement of large complexes, but at **moderate resolutions** compared to X-ray crystallography. However, the increasing power of modern electron microscopes and advances in image processing have enabled cryo-EM to approach resolutions close to those achieved by X-ray crystallography, with some structures determined below 3 Ã….

In cases where researchers have high-resolution structures of individual components (from crystallography or NMR), they can use these structures as **rigid-body fits** within the cryo-EM density map to create a composite model of the entire complex.

### Summary of Techniques and Applications

Each of these methods provides unique benefits and insights:

- **X-ray crystallography** is best for high-resolution structures of stable, crystallizable proteins and complexes, often used when fine atomic details are required.
- **NMR spectroscopy** allows proteins to be studied in solution, capturing dynamic interactions and flexibility, ideal for small proteins and proteins with conformational variability.
- **Cryo-EM** enables visualization of large macromolecular assemblies in their native state, invaluable for studying complex molecular machines and large viral structures.

Together, these methods enable researchers to obtain comprehensive structural and functional information across a range of protein sizes, shapes, and interaction complexities. As structural biology continues to integrate deep learning methods, each of these experimental approaches remains indispensable for validating and refining AI-predicted protein structures, ensuring that models align with the physical reality of molecular interactions.

## [42:15](https://www.youtube.com/watch?v=Hp3pjYaMsnU&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=8&t=2535s) Protein structure: conformations and Folding

Understanding **protein conformations** is central to grasping how proteins achieve their functional shapes. Proteins are **polymers** of amino acids, and while the **bond lengths and bond angles** between atoms in the backbone remain relatively fixed, the **rotatable bonds** along the backbone allow for flexibility. This flexibility enables proteins to explore multiple **conformations** until they find their lowest-energy folded state.

### Backbone Rotational Angles: Phi, Psi, and Omega

The **protein backbone** is primarily defined by three main angles associated with **rotatable bonds**:

1.  **Phi (Ï†)**: This is the angle between the **nitrogen atom** and the **alpha carbon** (CÎ±). The Ï† angle allows rotation around the bond connecting the nitrogen of one amino acid to the alpha carbon of the same amino acid.
2.  **Psi (Ïˆ)**: This is the angle between the **alpha carbon** and the **carbonyl carbon** of the same amino acid. Rotation around this bond influences the orientation of the backbone downstream of the alpha carbon.
3.  **Omega (Ï‰)**: This bond is between the **carbonyl carbon** of one amino acid and the **nitrogen** of the next amino acid in the chain. The Ï‰ angle usually adopts a **trans configuration** (180Â°) due to steric hindrance, which is generally stable. However, when **proline** is present, the Ï‰ angle may adopt a **cis configuration**, introducing a specific type of rigidity.

While each amino acid has unique side chains that influence these angles, the **phi and psi angles** are the most influential in defining the overall **three-dimensional shape** of the protein, dictating how it will fold and pack into its final structure. A complete description of a proteinâ€™s shape includes specifying these angles for each residue in the chain.

### Conformational Preferences: Energy Minimization

Despite the seeming **continuum of rotational possibilities** (from 0Â° to 360Â°) for each bond, proteins tend to adopt only a few **low-energy conformations**. This preference arises because the **spatial arrangement of atoms** naturally favors configurations that **minimize steric clashes** and maximize stability. For example, if we examine the simple molecule **ethane**, where two large atoms are attached, the lowest energy conformation positions these bulky groups as far from each other as possible. This concept also applies to larger, more complex protein structures, where **rotational freedom** is restricted to avoid high-energy, sterically unfavorable arrangements.

In practice, for a given **phi and psi angle pair**:

- **Three preferred states** often represent the most stable conformations due to steric and energetic considerations.
- The **three-state approximation** is commonly used in protein modeling, acknowledging that within each preferred state, there can be some **minor fluctuations** around the stable conformation. These fluctuations allow proteins to retain some **conformational flexibility** even when fully folded, important for functions like **ligand binding** and **allosteric regulation**.

### Folding Landscape and Conformational Space

To conceptualize the enormity of **conformational space**, consider a simple **thought experiment**:

- Imagine a **100-amino acid protein**, where each phi and psi bond pair can adopt **three stable conformations**. For each amino acid residue, there are thus **three possibilities for phi and three for psi**, totaling nine per residue.
- With 100 residues, the number of potential conformations becomes approximately 32003^{200}3200, or about 1010010^{100}10100. This vast number demonstrates the **astronomical diversity** of possible shapes the protein could theoretically adopt.

Despite this staggering number, only **one conformation** (or a small set of closely related structures) represents the **folded, functional state**. This fold results from a complex **energy landscape** where the protein "searches" for the configuration that minimizes its **free energy**, a process often referred to as **the protein folding problem**.

The **probability of achieving this folded state by chance** is infinitesimally small (roughly 1/101001/10^{100}1/10100), underscoring the idea that protein folding is not a random process. Instead, it follows specific **folding pathways** guided by **intrinsic chemical properties** and **environmental factors** (e.g., temperature, pH).

### Implications of Conformational Flexibility

Conformational flexibility is vital for many **biological functions**. For instance:

- **Enzyme catalysis** often requires small **conformational adjustments** to bring substrates into the optimal orientation.
- **Signal transduction proteins** may undergo significant conformational changes upon ligand binding, allowing them to relay information across cellular membranes or to other molecules.
- **Allosteric proteins** use conformational shifts to modulate their activity in response to binding events at sites distant from the active site.

### Conformational Energy Wells and Fold Stability

The **rotational preference** of bonds, coupled with **interactions among residues**, means that proteins tend to fall into **local energy minima**, or **wells**, in their energy landscape. Within these wells, **microstates** allow for minor rotations and adaptations, contributing to a protein's **stability and functional flexibility**. In completely folded proteins, the **entropy loss** associated with adopting a single conformation from numerous possible ones is offset by **enthalpic stabilization** provided by favorable **hydrogen bonding, van der Waals interactions**, and **hydrophobic effects**.

Understanding these principles of **conformational stability and flexibility** provides essential insights into why proteins fold in specific ways, how they achieve functional forms, and how their **misfolding** can lead to dysfunction or disease. For instance, in misfolding diseases like **Alzheimer's** or **Parkinson's**, proteins fail to reach their low-energy folded state, often aggregating into toxic assemblies that disrupt cellular function.

In summary, **protein conformations** are governed by a combination of **rotational freedom** around specific backbone angles and **energetic preferences** that guide the molecule towards a stable, functional state. This delicate interplay of **structure, flexibility, and stability** is foundational for understanding protein function and dysfunction in a biological context.

## [50:40](https://www.youtube.com/watch?v=Hp3pjYaMsnU&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=8&t=3040s) The protein folding problem: Levinthal's Paradox and the Energy Landscape

The **protein folding problem** is one of the most profound and long-standing questions in molecular biology, centered on understanding how proteins achieve their **functional three-dimensional structures** from a linear chain of amino acids. The process is remarkably efficient, yet theoretically complex, as proteins seem to "know" how to fold rapidly despite the astronomical number of possible conformations.

### Christian Anfinsenâ€™s Hypothesis: Energy Minimization

In the 1950s, **Christian Anfinsen** proposed that a proteinâ€™s folded conformation represents its **global free energy minimum**â€”the lowest energy state it can achieve in its given environment. This hypothesis suggested that proteins would naturally adopt their **native conformation** because this structure is thermodynamically the most stable. Essentially, the idea was that, given the right conditions, the sequence alone contains all the information needed for a protein to fold into its functional form.

### Levinthalâ€™s Paradox: The Search Problem

In 1969, **Cyrus Levinthal** articulated a challenge to Anfinsenâ€™s hypothesis, which became known as **Levinthalâ€™s Paradox**. He observed that if proteins were to search through all possible conformations to find the one with the lowest energy, it would take **longer than the age of the universe** for a protein to reach its folded state. For a small protein of 100 amino acids, the possible conformations number around 1010010^{100}10100â€”an astronomically large space to search.

Yet, in practice, many proteins fold **within milliseconds to seconds**. This apparent contradictionâ€”between the need for exhaustive conformational sampling and the rapidity of actual foldingâ€”highlighted that proteins must employ an **efficient search strategy** to locate their folded state, circumventing a brute-force approach.

### Resolving Levinthalâ€™s Paradox: The Folding Funnel and Energy Landscape Theory

The resolution to Levinthalâ€™s Paradox lies in the concept of the **energy landscape**, often visualized as a **folding funnel**. Rather than randomly sampling every possible conformation, proteins fold through a series of **thermodynamically favorable intermediate states**:

- **Local energy minima** represent stable intermediate structures along the pathway to the native state.
- **Energy barriers** separating these minima are overcome through **local conformational changes** that progressively guide the protein toward its folded form.

The folding funnel model suggests that as a protein folds, it moves down the funnel, where the number of possible conformations decreases while stability increases. The **depth** of the funnel represents the energy, with the **native state** at the global minimum. This landscape structure implies that while proteins can sample various states, they are energetically biased toward progressively lower-energy conformations, thus streamlining the folding process.

### Contact Order and Folding Speed

In 1998, researchers discovered that the **contact order**â€”the **average sequence distance between amino acids that interact in the folded structureâ€”correlates with folding speed**. Proteins with **low contact order** (i.e., where interacting residues are close in sequence) tend to fold faster than those with high contact order. This finding supports the idea that **local interactions** form quickly, helping to stabilize portions of the structure early in the folding process and guiding the overall conformation.

### Levels of Protein Structure

Proteins are organized hierarchically, with each level contributing to the final folded form:

1.  **Primary Structure**: The **linear amino acid sequence** of the protein, determined directly by the gene encoding it.
2.  **Secondary Structure**: **Local structural elements**, such as **alpha helices** and **beta sheets**, stabilized by hydrogen bonding patterns between backbone atoms. These structures form quickly, reflecting local energy minima and helping reduce conformational space.
3.  **Tertiary Structure**: The overall **three-dimensional shape** of the polypeptide chain, encompassing all interactions within a single molecule. This structure includes the folding of secondary elements and interactions between side chains.
4.  **Quaternary Structure**: The **assembly of multiple polypeptide chains** (subunits) into a functional complex. For example, the **Lac repressor** protein discussed earlier achieves functionality as a **homodimer** by forming a stable unit with two identical subunits.

Each level builds upon the last, with the tertiary and quaternary structures representing the final, functional form of the protein. This hierarchical folding allows proteins to efficiently narrow down the folding options, leveraging local structure formation to inform and stabilize the overall fold.

### Implications of the Folding Problem

The protein folding problem remains an area of active research with implications across **biomedicine and biotechnology**. Misfolding and aggregation are central to many **neurodegenerative diseases**, such as Alzheimerâ€™s and Parkinsonâ€™s, where misfolded proteins aggregate, leading to cell damage. Additionally, understanding protein folding mechanisms aids in **protein design** efforts, where scientists aim to engineer new proteins with specific functions by predicting and controlling their folded structures.

The development of **computational techniques** such as **machine learning** (e.g., AlphaFold) has revolutionized our ability to predict protein structures with high accuracy, bypassing some of the limitations of experimental structure determination. However, the protein folding problem remains a rich field that bridges physics, chemistry, and biology, underscoring the elegance of natureâ€™s approach to creating functional biological molecules.

## [55:00](https://www.youtube.com/watch?v=Hp3pjYaMsnU&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=8&t=3300s) Protein secondary structure

**Protein secondary structure** represents a critical level of organization within protein folding, characterized by **localized structural motifs** such as **alpha helices** and **beta sheets**. These motifs are stabilized primarily by **hydrogen bonds** and are foundational elements that contribute to the overall three-dimensional shape and function of proteins.

### The Ramachandran Plot: Mapping Accessible Dihedral Angles

The **Ramachandran plot** is a powerful tool in structural biology, visualizing the **dihedral angles (phi and psi)** of amino acid residues in proteins. By plotting the phi (Ï†) and psi (Ïˆ) angles for residues across many proteins, we observe distinct regions where these angles are more favorable, reflecting the **limited conformational space** due to **steric hindrance** and **backbone rigidity**:

- **Alpha helices** typically appear in a dense region on the plot with characteristic phi and psi angles that allow for **helical hydrogen bonding**.
- **Beta sheets** occupy another prominent region, with angles favoring **extended strands** stabilized by hydrogen bonds between adjacent strands.
- **Glycine**, due to its lack of a side chain, exhibits more flexibility and can adopt unique angles outside these regions, often occurring in **turns or loops**.

The **density of points** in the Ramachandran plot reflects the stability of certain backbone angles, with highly populated areas indicating **preferred conformations** that minimize energy through favorable bonding and spatial arrangement.

### Secondary Structure Elements: Alpha Helices and Beta Sheets

**Alpha Helices**:

- An alpha helix is a **right-handed coil** where each amino acid residue forms a **hydrogen bond** with the residue four positions ahead in the sequence. This results in a tightly packed, rod-like structure with the side chains projecting outward from the helix, minimizing steric clashes.
- The alpha helix is a stable configuration due to **internal hydrogen bonding** along the backbone, which propagates down the helical axis, contributing to its structural resilience.

**Beta Sheets**:

- Beta sheets consist of **extended strands** that align side-by-side to form a sheet. These strands are connected by **hydrogen bonds** between backbone atoms of adjacent strands, creating a **pleated sheet** appearance.
- Beta sheets can be either **parallel** or **anti-parallel**:
    - In **parallel beta sheets**, the strands run in the same direction and typically form larger, less tightly bonded sheets.
    - In **anti-parallel beta sheets**, strands run in opposite directions, resulting in stronger hydrogen bonds and greater stability.
- These sheets play a crucial role in structural scaffolding and are often found in the core of proteins, where they contribute to the **rigid, planar stability** necessary for maintaining the proteinâ€™s overall shape.

### Methods for Predicting Secondary Structure

Predicting secondary structure has been a focal point in computational biology, as it provides insights into protein function and helps guide more complex three-dimensional modeling.

1.  **Chou-Fasman Method**:
    - This early method used **statistical probabilities** based on the frequency of each amino acid in secondary structures derived from known protein crystal structures.
    - For each amino acid, the **probability of occurrence** in an alpha helix, beta sheet, or random coil was calculated. By analyzing stretches of amino acids with a high likelihood of forming specific secondary structures, this method could reasonably predict segments of helices and sheets.
2.  **Neural Network Approaches**:
    - In the 1990s, neural networks became a transformative tool for **secondary structure prediction**, with methods like **PHD (Profile network from Heidelberg)** leveraging **three-layer neural nets** to improve accuracy.
    - These neural networks incorporated **multiple sequence alignments** (MSAs), which analyze the conservation of amino acids across homologous proteins, providing clues about the likelihood of certain residues being part of an alpha helix or beta sheet.
    - This approach marked a pivotal moment in structural biology, allowing the prediction of secondary structures with greater precision by combining sequence information with homologous structure data.
3.  **Modern Predictive Techniques**:
    - Today, advances in **machine learning** and **deep learning**â€”exemplified by models like **AlphaFold**â€”have significantly improved **three-dimensional protein structure prediction**, often rendering isolated secondary structure prediction unnecessary.
    - By incorporating extensive training on sequence-structure relationships and leveraging large protein structure databases, modern algorithms can predict not only the overall tertiary structure but also local secondary structures with high accuracy.

### The Role of Secondary Structure in Protein Folding

Secondary structures form the **initial scaffold** of a proteinâ€™s folded state, guiding the organization of the tertiary structure. The hydrogen bonding patterns and structural rigidity inherent in alpha helices and beta sheets create a **stable framework** upon which other interactions, such as side-chain packing and hydrophobic interactions, can build. This **hierarchical folding process** is critical in ensuring that proteins adopt a functional, low-energy conformation efficiently.

In summary, secondary structures like alpha helices and beta sheets are integral components of protein architecture, supported by the limited conformational space outlined in the Ramachandran plot. Predictive models have evolved from statistical and neural network methods to sophisticated deep learning systems, enabling us to reliably infer protein structure and function. These advancements underscore the connection between **sequence, structure, and biological function**, facilitating our understanding of how proteins achieve their specific roles within cells.

## [59:00](https://www.youtube.com/watch?v=Hp3pjYaMsnU&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=8&t=3540s) Protein tertiary structure: From Sequence to 3D Configuration

**Tertiary structure** encompasses the unique three-dimensional shape that a protein assumes, dictating its functionality, stability, and interactions. Predicting this structure from a **linear amino acid sequence** has been a longstanding goal, capturing the intricate relationships between residues and leveraging insights from both structural biology and computational methods.

### Contact Maps: Visualizing Residue Interactions

A foundational tool in tertiary structure prediction is the **protein contact map**, a two-dimensional grid representing **residue-residue proximities** within the protein:

- On a contact map, residues are plotted on both the **x-axis** and **y-axis**, with **contacts marked at coordinates** where two residues are spatially close.
- **Alpha helices** appear as linear stretches along the diagonal (y = x line) due to consistent bonding patterns within the helical structure.
- **Parallel and anti-parallel beta sheets** manifest as lines perpendicular or parallel to the x = y axis, reflecting the hydrogen bonding patterns between aligned beta strands.

These contact maps reveal not only **secondary structure elements** but also insights into tertiary structure by displaying which residues interact across the proteinâ€™s 3D conformation.

### Evolutionary Insights: Using Co-evolution for Structure Prediction

Proteins evolve under selective pressures that preserve structural integrity, often leading to **co-evolution of residue pairs** that interact. This is critical for understanding tertiary structure:

- By analyzing **multiple sequence alignments (MSAs)** across homologous proteins, scientists observe that certain amino acid pairs change in tandem. When one amino acid in an interaction changes, the paired amino acid may change to maintain the interactionâ€™s stability.
- This **coevolutionary data** offers clues about residue proximity, aiding in the construction of contact maps. Proteins predicted to maintain specific residue pairs often reveal **functionally critical sites** or structural features that are conserved across species.

This co-evolutionary approach laid the groundwork for **machine learning methods** that integrate MSAs with contact maps, significantly improving predictive accuracy in protein folding.

### Computational Advances: From Rosetta to AlphaFold

The quest to solve protein structure prediction has evolved through notable computational tools and milestones:

1.  **Rosetta**:
    - Developed in **David Bakerâ€™s lab**, Rosetta represented an early, transformative approach that combined **statistical and physics-based insights**. Unlike traditional models, Rosetta used **short sequence fragments** (typically five amino acids) from known structures to assemble potential 3D configurations, inferring the **phi and psi angles** from these fragments.
    - This approach iteratively assessed which configurations minimized **free energy**, leading to compact, energetically favorable structures.
    - Rosettaâ€™s **fragment-based methodology** allowed for plausible predictions even for regions without direct homologs, setting a new standard in structure prediction and revealing the utility of leveraging **empirical data** in structural biology.
2.  **The Critical Assessment of Protein Structure Prediction (CASP)**:
    - CASP, a biennial competition, became a proving ground for structure prediction methodologies. In this competition, crystallographers provide protein sequences for which structures are known but unpublished, allowing researchers to test their prediction models against experimentally validated data.
    - CASP exposed the limitations of existing methods, revealing that no approach, until the advent of deep learning models, consistently predicted unknown structures accurately.
3.  **AlphaFold 2**:
    - In 2020, **AlphaFold 2** dramatically advanced the field, using **deep learning techniques** to predict protein structures with near-experimental accuracy for many proteins.
    - AlphaFold 2 integrates **evolutionary data from MSAs** with deep learning architectures, which enables it to infer spatial relationships between residues, effectively capturing **long-range interactions** that are difficult to model in traditional approaches.
    - Its unprecedented success at CASP highlighted the power of combining **large-scale evolutionary data** with neural networks, shifting the landscape of structural biology.
4.  **Protein Language Models and Attention Maps**:
    - Recent models incorporate **protein language models** that leverage attention mechanisms, similar to natural language processing (NLP) techniques. These models capture context-dependent relationships between residues, allowing them to predict contacts and structural features with high accuracy.
    - **Attention maps** visualize which residues communicate strongly with others, aiding in understanding **functional and structural dependencies** across the protein.

### Tertiary Structure Prediction Challenges and Future Directions

**Tertiary structure prediction** remains an area of active research, especially for proteins with complex folding patterns or those that undergo conformational changes. Despite advances, challenges include:

- **Dynamic and flexible regions**: Many proteins contain intrinsically disordered regions that do not adopt a fixed structure, complicating prediction.
- **Membrane proteins and large complexes**: These proteins pose unique difficulties due to their diverse environments and complex interactions, requiring specialized modeling approaches.
- **Integrating multi-scale data**: Future models aim to integrate various types of biological data, such as cryo-electron microscopy for large complexes, enabling holistic predictions that incorporate different structural and environmental contexts.

In summary, predicting protein tertiary structure has evolved from a theoretical challenge into a computational reality, thanks to insights from **contact maps, co-evolution, and machine learning**. With each breakthrough, the field moves closer to a future where **structure-based functional prediction** becomes integral to understanding and manipulating biological systems, from basic research to therapeutic development.

## [1:04:20](https://www.youtube.com/watch?v=Hp3pjYaMsnU&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=8&t=3860s) Comparing protein structures: Quantitative and Structural Alignment Methods

Once we have protein structures, whether from **experimental determination** (e.g., X-ray crystallography) or **predictive models** like AlphaFold, we often need to **compare** these structures. Structural comparison can reveal **conformational similarities**, help assess the **accuracy of predicted models**, and provide insights into **evolutionary relationships** and **functional conservation**.

### RMSD: Root Mean Square Deviation for Structural Comparison

A common metric for assessing similarity between two protein structures is the **root mean square deviation (RMSD)**, which quantifies the average distance between corresponding atoms (usually **C-alpha atoms**). RMSD provides a single numerical value that summarizes the **overall alignment quality**:

- **Formula**: RMSD is calculated by taking the squared differences of the coordinates (x, y, z) of corresponding atoms between two structures, averaging these squared differences, and then taking the square root of the result:

    where NNN is the number of atoms, and (x<sub>i</sub><sup>1</sup>,y<sub>i</sub><sup>1</sup>,z<sub>i</sub><sup>1</sup>) and (x<sub>i</sub><sup>2</sup>,y<sub>i</sub><sup>2</sup>,z<sub>i</sub><sup>2</sup>) are the coordinates of the i-th atom in the two structures.
- **Interpretation**: Lower RMSD values indicate better alignment (closer structural similarity), with values below **2 Ã…** often reflecting very similar structures.

### Structural Alignment Process

1.  **Residue Correspondence**: When comparing two homologous proteins or evaluating a model against an experimentally solved structure, we first need to **map corresponding residues**. For identical sequences, mapping is straightforward, while for homologous proteins, we use **multiple sequence alignments** to match residues across similar regions.
2.  **Centering and Superposition**:
    - **Centering**: To minimize differences due to translational offsets, both proteins are first centered by calculating the **center of mass** and adjusting coordinates so that this center aligns with the origin.
    - **Optimal Rotation**: After centering, the structures are rotated for optimal alignment. This rotation ensures that RMSD measurements reflect structural rather than positional differences. Using **singular value decomposition (SVD)** on the **covariance matrix** of the atomic coordinates allows the calculation of a rotation matrix that aligns the structures optimally.

Once the structures are superimposed, we calculate the RMSD to determine how well they align in three-dimensional space.

### Beyond RMSD: Evaluating Functional and Structural Fidelity

While RMSD provides a robust baseline, additional comparisons may be necessary to capture **local structural deviations** or **specific functional sites**. Other metrics and approaches include:

- **Local RMSD Calculations**: Focusing on specific structural motifs (e.g., binding sites) provides insights into **functional conservation** even if the global structures vary.
- **Secondary Structure Element Matching**: Comparing helices, beta strands, and loops can offer a more detailed view of structural similarity, as these elements often contribute to **stability** and **function**.
- **Global vs. Local Conformational Similarities**: Certain comparisons emphasize **local similarities** within active sites, useful in functional studies or ligand-binding assessments, while global RMSD captures the entire structure.

### Energy Functions in Protein Structure Evaluation and Prediction

In computational modeling and evaluation, **energy functions** play a central role. These functions approximate the **physical interactions** that stabilize protein structures, guiding predictions and offering insight into the effects of **mutations**, **binding affinities**, and **dynamic stability**.

Key components of energy functions include:

1.  **Electrostatics**: Models **charge-based interactions** between residues. Attractions and repulsions between charged side chains (e.g., lysine and glutamate) are key to overall structure.
2.  **Van der Waals Interactions**: These account for **steric effects** and **non-bonded interactions**, capturing the balance between attractive forces at moderate distances and repulsive forces at very close ranges.
3.  **Hydrogen Bonding**: Particularly important in **secondary structures** (alpha helices and beta sheets), hydrogen bonds stabilize the backbone configuration and are vital for folding.
4.  **Hydrophobic Effect**: Reflects the tendency of non-polar side chains to cluster away from water, stabilizing protein interiors and driving the folding process.

### Applications of Energy Functions

Energy functions form the basis of several critical applications in structural biology:

- **Molecular Dynamics (MD)**: By integrating energy functions over time, MD simulations provide insights into **protein motion**, **folding pathways**, and **conformational changes** under physiological conditions.
- **Drug Binding and Docking**: Predicting how a drug or ligand binds to a protein involves assessing binding energy, optimizing binding affinity, and modeling structural stability.
- **Protein Design and Mutagenesis**: By evaluating energy differences between mutations, researchers can predict the **stability** and **functionality** of modified proteins or design entirely new proteins with desired structural properties.

In sum, structural comparisons, RMSD calculations, and energy functions enable researchers to **quantify protein structure accuracy**, **predict stability**, and **design functional proteins** for biomedical applications. Together, these methods provide the foundation for both **experimental validation** and **computational exploration** in structural biology.
