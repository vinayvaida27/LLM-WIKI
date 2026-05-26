---
tags:
  - "topic"
topics:
  - "MLCB"
status: updated
created: 2026-05-24
updated: 2026-05-24
sources:
  - "Raw/Sources/lecture_13_drug_development_intro.md"
source_count: 1
aliases:
  - "Lecture 13 - Drug Development Intro"
---

# Lecture 13 - Drug Development Intro

## Source
- Raw source: `Raw/Sources/lecture_13_drug_development_intro.md`
- Supporting source: `Raw/Files/lecture_13_drug_development_intro.md`
- Existing related pages: [[mlcb-2024-computational-biology]], [[mlcb-complete-study-guide]], [[mlcb-methods-map]]
- Last updated: 2026-05-24

## Executive Summary
Lecture 13 - Drug Development Intro develops drug classes, pharmacokinetics, pharmacodynamics, GPCRs, therapeutic windows, toxicology, drug interactions, and clinical trials. This page intentionally preserves substantial source detail so a future LLM can reason from the wiki without immediately reopening the raw transcript.

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
- What is a drug?
- Modern drug discovery framework
- Types of drugs
- Pharmacokinetics (PK): How the Body Processes Drugs
- Pharmacodynamics (PD): What Drugs Do to the Body
- Toxicology: Assessing the Safety and Side Effects of Drugs
- Steps in the drug development process
- Structure-Activity Relationships (SAR)
- Drug development timeline

## Detailed Lecture Notes
The notes below preserve the processed source order and are intentionally detailed.

# Lecture 13 - Drug Development Intro

Video: [Lecture13 Drug Development Intro](https://www.youtube.com/watch?v=m_R_6ItR-qY&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=13)

Slides: [Lecture13_IntroDrugDevelopment.pdf](https://www.dropbox.com/scl/fi/3xbhc438mltum8oq6urkh/Lecture13_IntroDrugDevelopment.pdf?rlkey=l970ogq1i8wnyqr7a44p22xvx&dl=0)

## [0:00](https://www.youtube.com/watch?v=m_R_6ItR-qY&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=13&t=0s) What is a drug?

To effectively understand **drug development**, we must begin by defining what qualifies as a **drug** and how it fits into the broader framework of medical science. Today, drugs are substances that have undergone extensive testing and regulatory scrutiny to be approved for **therapeutic use**. LetÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s explore the technicalities of what defines a drug, its historical context, and the general pathway from idea to market.

### Definition of a Drug

In technical terms, a **drug** is defined as a **substance recognized by an official pharmacopoeia** or formulary. It must meet stringent standards, detailing its **composition, production process, and purity levels**. Key aspects of this definition include:

- **Purpose**: A drug must be intended for **diagnosis, cure, mitigation, treatment, or prevention** of diseases. This purpose distinguishes it from other substances or compounds.
- **Regulatory Distinction**: Drugs are regulated separately from foods and medical devices. Although there are specialized categories such as **medical foods**, which are designed to address specific dietary needs in diseases, these are not classified as drugs. Additionally, medical devices, although integral to healthcare, follow separate regulations.

Drugs fall into two main categories:

1.  **Small Molecule Drugs**: These are chemically synthesized compounds, traditionally the focus of **pharmaceutical research** and commonly taken in oral or injectable form.
2.  **Biologics**: These are larger, more complex molecules produced by living cells or organisms, including **antibodies, vaccines, and gene therapies**. Biologics often require more sophisticated manufacturing processes and delivery systems.

### The Role of Drugs in Human History

Drug use and development are deeply rooted in **human history**, with nearly every culture exploring medicinal substances. Historically, early drug discoveries often emerged from **natural sources**, especially plants, with traditional knowledge guiding usage and benefits. Some of todayÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s standard medications have their origins in these ancient practices:

- **Poppy Extracts**: Used historically for pain relief, poppies led to the discovery of **opiates** (e.g., morphine and codeine), which remain central in pain management.
- **Willow Bark**: This was traditionally used to treat fever, and it later led to the isolation of **salicylic acid**, which served as the foundation for **aspirin**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âone of the most widely used anti-inflammatory and pain-relieving drugs.
- **Artemisia (Sweet Wormwood)**: Recognized in Chinese medicine for treating fevers, it eventually provided the basis for **artemisinin**, a powerful antimalarial drug.

These examples highlight how **natural products** served as starting points for drug discovery, a trend that continues in the search for new drugs today. However, the modern approach to drug development has vastly evolved, characterized by complex scientific, regulatory, and technological frameworks.

### The Modern Framework for Drug Discovery and Development

The modern drug development process is a **multifaceted, highly regulated** pathway involving stages from **initial discovery** to **clinical testing** and **market approval**. Unlike the traditional trial-and-error methods, todayÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s drug discovery is driven by rigorous **scientific methodologies** and **technological advancements** in chemistry, biology, and computational methods. This contemporary framework ensures that drugs are not only effective but also safe for human use.

While we will delve deeper into **machine learning** and **deep learning** contributions to this process in future discussions, understanding the **holistic journey of a drug**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âfrom conceptualization to commercializationÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âis essential for appreciating the complexities and challenges involved.

This foundation sets the stage for exploring **how modern tools, including AI**, are revolutionizing drug discovery and enabling **new therapeutics** that address unmet medical needs more efficiently than ever before.

## [3:00](https://www.youtube.com/watch?v=m_R_6ItR-qY&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=13&t=180s) Modern drug discovery framework

The **modern drug discovery framework** is a highly structured, intentional, and interdisciplinary process that aims to transition an **initial scientific insight** into a **commercially viable drug**. Unlike traditional methods rooted in serendipity or simple trial and error, todayÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s drug discovery is based on a well-defined framework driven by our understanding of **molecular pathways**, **disease mechanisms**, and **targeted therapeutic design**.

### From Basic Science to Therapeutic Agent

The process of drug discovery begins with a **basic scientific idea** about a molecular pathway that plays a role in disease. Researchers identify a **disease target**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âa protein, gene, or cellular mechanism crucial to the disease's pathology. By understanding how this target operates, they can begin a **deliberate search for therapeutic agents** designed to interact with it, modifying or inhibiting its function to produce a beneficial effect. These therapeutic agents can range from **small molecules** to **biologics** like antibodies or even natural products with bioactivity against the target pathway.

### Interdisciplinary Nature of Drug Discovery

This process is profoundly **interdisciplinary**, involving contributions from:

- **Biologists and Chemists**: Essential for understanding the disease and designing molecules with the desired properties.
- **Engineers and Bioinformaticians**: Play roles in optimizing delivery systems and computational models that predict drug behavior.
- **Computational Biologists**: Use bioinformatics to understand complex biological data, select promising targets, and analyze molecular interactions.
- **Business and Legal Experts**: Ensure the process aligns with regulatory standards and is commercially viable, navigating intellectual property (IP) and market strategy.

The collaborative nature of modern drug discovery requires **thousands of people** and can cost **up to or over a billion dollars** for a single drug. This high cost is partly due to stringent standards set by **regulatory agencies like the FDA**, which require extensive evidence demonstrating both **efficacy** and **safety** of a potential drug. These standards help ensure patient safety but significantly raise the **time, complexity, and cost** of the development process.

### The Role of Business Models in Drug Development

Pharmaceutical companies are motivated to invest in drug development because of the **high potential for profit** from patented drugs. This incentive structure is designed to promote innovation, but it can sometimes **conflict with therapeutic needs**. The ideal case aligns **therapeutic need** and **market incentives**; however, this alignment doesnÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t always hold, especially when the business model may not support development in areas with limited commercial appeal.

A prominent example is the **development of antibiotics**. The **rise of antimicrobial resistance** has led to an urgent need for new antibiotics, yet the economic incentives for producing them are weak. For instance, if a pharmaceutical company develops a new antibiotic that effectively combats resistant bacteria, the optimal usage scenario may involve **restricting its distribution** to preserve its efficacy and reduce the likelihood of resistance emerging. However, **limited usage reduces sales**, making such a product less profitable than drugs that require regular, sustained use. As a result, there has been **minimal investment in novel antibiotics** over recent decades despite their critical importance for global health.

### Aligning Business and Therapeutic Needs: New Models

This misalignment between **business models and public health needs** in cases like antibiotics has prompted researchers and policymakers to explore alternative models. These new models may involve:

- **Government Funding and Subsidies**: To offset development costs and encourage research even in areas with low commercial returns.
- **Subscription Models**: Where healthcare systems pay for access to antibiotics, regardless of how often they are prescribed, encouraging companies to invest in antibiotics without needing high volume sales.
- **Patent Extensions and Market Exclusivity**: To provide longer periods of exclusivity and thus greater potential for return on investment.

The **modern drug discovery framework** is thus as much a **scientific and technological enterprise** as it is a **regulatory and economic challenge**. In upcoming sections, we will explore how advances in **machine learning** and **deep learning** are enabling more efficient, targeted, and potentially less costly ways to design new drugs, opening doors to treat diseases with unmet therapeutic needs while reshaping the economics of drug development.

## [7:00](https://www.youtube.com/watch?v=m_R_6ItR-qY&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=13&t=420s) Types of drugs

In modern medicine, drugs can be broadly classified into **small molecule drugs** and **biologics**, each with distinct characteristics, manufacturing requirements, and regulatory pathways. Beyond these primary categories, there are also innovative drug classes such as **live biotherapeutic agents** and **cell-based therapies** that represent emerging frontiers in therapeutic development.

### Small Molecule Drugs

**Small molecule drugs** are **low molecular weight compounds** (typically under 500 Dalton) that are generally synthesized through chemical processes. Often, these drugs are optimized derivatives of natural compounds extracted from various sources, including plants. Their **small size** allows them to diffuse across cell membranes, making them effective for targeting intracellular proteins. Small molecule drugs usually bind to a specific protein target, inhibiting or modifying its function to achieve therapeutic effects.

**Characteristics**:

- **Synthesis**: Typically produced synthetically after initial natural product identification.
- **Administration**: Predominantly oral, though other routes like topical or injectable are possible in certain cases.
- **Examples**: Aspirin, metformin, and statins.
- **Advantages**: Ease of production, stability (often stored as a dry powder), and long shelf-life, usually without refrigeration.
- **Disadvantages**: Small molecule drugs can sometimes produce **toxic metabolites** upon degradation, potentially leading to side effects.

### Biologics

**Biologics** represent a class of drugs derived from **biological sources** and generally include **larger molecular structures**, such as proteins, antibodies, and other cellular products. Unlike small molecules, biologics are primarily administered via **injection or intravenous (IV)** due to their complex structure, which would be broken down in the digestive system if taken orally.

### Characteristics:

- **Production**: Derived through **biological processes** such as fermentation or cell culture.
- **Administration**: Typically non-oral, requiring IV or injection.
- **Examples**: Herceptin for breast cancer and insulin for diabetes.
- **Advantages**: High specificity due to targeted protein binding, potentially resulting in fewer side effects.
- **Disadvantages**: Sensitive to environmental conditions (often requiring refrigeration), expensive production, and administration challenges as they often require medical supervision.

### Live Biotherapeutic Agents

**Live biotherapeutic agents** represent an exciting class of **biologic drugs** that utilize **living organisms** (often bacteria) as therapeutic agents. This field, closely linked to **microbiome research**, aims to exploit beneficial bacteria that may influence health positively. For example, specific bacteria found in the guts of healthy individuals may be absent in individuals with certain diseases, leading researchers to hypothesize that restoring these bacteria could have therapeutic benefits.

**Characteristics**:

- **Administration**: Often as capsules containing live bacteria meant to colonize the patientÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s gut.
- **Advantages**: Leveraging naturally occurring organisms, these agents potentially have a lower risk of toxicity.
- **Disadvantages**: Complex to standardize and regulate due to variability in how they colonize and interact with each patientÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s microbiome. Dosing can be challenging since colonization may lead to bacterial growth over time, creating discrepancies between initial and effective dose levels.

Live biotherapeutic agents have shown promise in treating recurrent **Clostridium difficile infections** through **fecal microbiota transplantation**. Although microbiome-based therapeutics are still in early stages, they represent a promising avenue for precision and personalized medicine.

### Cell-Based Therapies

**Cell-based therapies** involve the use of **live cells**, often derived from the patient or a donor, to treat diseases. Examples include **CAR T-cell therapy** for cancer and **stem cell therapies** for tissue regeneration. These therapies leverage the innate properties of living cells to target disease mechanisms with high specificity.

**Characteristics**:

- **Administration**: Requires precise injection, often into specific tissues or through IV.
- **Advantages**: High personalization potential, especially in targeting specific cells like cancer cells.
- **Disadvantages**: Complex to manufacture, standardize, and regulate due to the need for living cells. The logistics of cell therapies often require specialized storage, transport, and clinical administration.

The field of cell-based therapies is rapidly expanding, driven by advancements in genetic engineering, cell culture techniques, and personalized medicine approaches. However, regulatory challenges remain due to the complexities inherent in using live human cells.

### Companion Diagnostics

While not a type of drug, **companion diagnostics** represent a significant advancement in **personalized medicine** by allowing healthcare providers to tailor treatment based on individual patient profiles. This approach can optimize drug efficacy by identifying patients who are most likely to benefit from specific treatments.

**Concept**:

- **Purpose**: Companion diagnostics are used to screen patients for specific genetic, molecular, or cellular markers that predict a drugÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s effectiveness or likelihood of adverse effects.
- **Examples**: HER2 testing in breast cancer to determine the suitability of Herceptin, and PD-L1 expression testing for immunotherapy responsiveness.
- **Advantages**: This approach allows for targeted treatment, potentially reducing adverse effects and improving outcomes by matching the right drug to the right patient group.

By helping to identify patient subpopulations within broader disease categories, companion diagnostics can sometimes **revive drugs that might otherwise fail clinical trials** due to heterogeneous patient responses. These diagnostics are instrumental in advancing precision medicine, especially in complex diseases where patient populations may have varied underlying molecular mechanisms.

### Emerging and Specialized Drug Types

1.  **Phage Therapy**: A biologic approach using bacteriophages (viruses that target bacteria) to treat bacterial infections, particularly useful against antibiotic-resistant bacteria. Phage therapy is still experimental and faces unique regulatory hurdles.
2.  **Vaccines**: Although traditionally focused on preventing infectious diseases, recent advancements are exploring vaccines in **cancer immunotherapy** and **autoimmune conditions**, where the immune systemÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s activity is modulated to treat or prevent disease.

These various **types of drugs and therapies** underscore the diversity in modern treatment options. Each class comes with unique **advantages, disadvantages, and challenges**, from manufacturing and storage to administration and regulatory approval. In the coming sections, we will delve deeper into the **drug development process**, focusing on **small molecule drugs** and exploring how machine learning and deep learning are transforming discovery, testing, and optimization in this field.

## [23:27](https://www.youtube.com/watch?v=m_R_6ItR-qY&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=13&t=1407s) Pharmacokinetics (PK): How the Body Processes Drugs

**Pharmacokinetics (PK)** is a core concept in drug development that examines what the **body does to a drug** after it is administered. In contrast, **pharmacodynamics (PD)** focuses on what the **drug does to the body**. PK is crucial in determining **dosing schedules, administration routes, bioavailability,** and **potential side effects**. The study of PK involves understanding four main phases: **absorption, distribution, metabolism,** and **excretion** (often abbreviated as **ADME**).

### Absorption

**Absorption** is the process through which a drug **enters the bloodstream** or its **site of action**. Factors influencing absorption include:

- **Route of administration** (e.g., oral, intravenous, or inhalation), with some routes allowing for faster or more direct absorption.
- **Chemical properties** of the drug, such as hydrophilicity (water solubility) or hydrophobicity (fat solubility).
- **Environmental conditions** like blood flow and pH at the absorption site, which can enhance or inhibit the drug's ability to cross cellular membranes.

The extent to which a drug is absorbed effectively determines its **bioavailability**, or the fraction of the drug that reaches systemic circulation in an active form.

### Distribution

**Distribution** describes the movement of the drug from the bloodstream into **various tissues** and **compartments** within the body. Key considerations include:

- **Blood flow** to different organs and tissues, as areas with high blood flow (e.g., heart, liver) typically receive drugs more quickly.
- **Protein binding**, where drugs may bind to plasma proteins in the blood, limiting the amount of free drug available to exert a therapeutic effect.
- The ability to cross **selective barriers**, such as the **blood-brain barrier**.

A critical metric in distribution is the **volume of distribution (Vd)**, which reflects how extensively a drug disperses throughout the body relative to its concentration in the blood.

### The Blood-Brain Barrier

The **blood-brain barrier (BBB)** is a selective, semi-permeable barrier that separates circulating blood from the brain's extracellular fluid. This **tight junction** of endothelial cells allows only specific molecules to pass through, protecting the brain from potentially harmful substances. The BBB is particularly impermeable to **large or hydrophilic molecules**, creating a challenge for delivering drugs aimed at treating central nervous system disorders.

Strategies to overcome the BBB include:

- **Designing drugs** with properties that increase BBB permeability.
- **Nanoparticle-based delivery systems** to shuttle drugs across the barrier.
- **Intranasal administration**, which allows drugs to bypass the BBB by directly accessing nerve pathways in the nasal cavity.

### Metabolism

**Metabolism** transforms drugs into more water-soluble forms for easier excretion. This occurs mainly in the **liver** through two phases:

1.  **Modification (Phase I)**: Involves enzymes like the **cytochrome P450** family, which oxidize or reduce the drug, making it more reactive.
2.  **Conjugation (Phase II)**: Adds a polar group (e.g., glucuronidation) to the drug, increasing its solubility and facilitating excretion.

Metabolism can **activate** drugs, convert them into **inactive metabolites**, or sometimes create **toxic intermediates**. For instance, acetaminophen is metabolized to a toxic intermediate that can cause liver damage, especially in individuals with high alcohol intake who upregulate specific liver enzymes, enhancing this toxic pathway.

### Excretion

**Excretion** is the process of removing drugs and their metabolites from the body. This typically occurs via:

- **Kidneys (urine)**: The most common route for excreting water-soluble metabolites.
- **Liver (bile)**: Some metabolites are secreted into bile and eventually excreted in feces.
- **Other routes**: Sweat, breath, and breast milk also facilitate drug excretion, though to a lesser extent.

The efficiency of excretion impacts the drugÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s **half-life**, which is crucial in determining the **dosing frequency** to maintain therapeutic levels without causing toxicity.

### Modeling Pharmacokinetics

PK models help predict how drugs behave in the body, often using **compartmental models**:

- **One-compartment model**: Simplifies drug behavior to a single space (e.g., bloodstream), with drug levels decaying over time as it is metabolized and excreted.
- **Two-compartment model**: Accounts for an additional compartment, such as tissues or organs, where the drug can move temporarily before returning to the bloodstream for excretion.

These models inform dosing schedules by predicting **peak concentrations (Cmax)**, **minimum concentrations (Cmin)**, and **half-life**, which represents the time required for the drugÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s concentration in the bloodstream to reduce by half.

#### Practical Considerations in Pharmacokinetics

1.  **Absorption limitations**: Poor absorption leads to low bioavailability, necessitating higher doses, which may increase side effects.
2.  **Tissue accumulation**: Some drugs may accumulate in specific tissues (e.g., lipophilic drugs in fat), influencing their effectiveness and safety.
3.  **Toxic metabolites**: Certain drugs can metabolize into harmful byproducts, making it crucial to monitor specific pathways, especially in patients with liver or kidney impairments.
4.  **Patient variability**: Age, health status, and concurrent medications can significantly alter PK properties, necessitating personalized dosing strategies.

### Conclusion

Pharmacokinetics is foundational in **drug development and therapeutic management**, determining how often, in what quantity, and by which route a drug should be administered to maximize its therapeutic benefits while minimizing potential risks. Understanding PK enables researchers and clinicians to **optimize drug design and delivery** to better meet patient needs, paving the way for safer, more effective treatments.

## [42:00](https://www.youtube.com/watch?v=m_R_6ItR-qY&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=13&t=2520s) Pharmacodynamics (PD): What Drugs Do to the Body

**Pharmacodynamics (PD)** investigates the effects drugs have on the body, examining the **mechanisms of drug action, dose-response relationships,** and **therapeutic vs. toxic effects**. PD focuses on how drugs interact with **receptors**, **enzymes**, or **other cellular targets** to produce a biological response. A detailed understanding of PD enables the design of drugs with **maximal therapeutic effects** while minimizing **adverse side effects**.

### Drug-Receptor Interactions

Most **small molecule drugs** exert their effects by **binding to specific receptors**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âtypically **proteins** involved in cellular signaling pathways or enzymatic processes. Key types of drug interactions include:

- **Agonists**, which activate their target receptors to produce a biological response.
- **Antagonists**, which bind to receptors but **block or inhibit** their activation, effectively dampening the response.
- **Partial agonists**, which bind to and activate receptors but produce a **weaker response** than full agonists.

One essential class of receptors is **G protein-coupled receptors (GPCRs)**, highly "druggable" due to their role in a broad range of physiological processes. Other common targets include **ion channels** and **enzymes**.

### Affinity and Potency

The **affinity** of a drug for its receptor represents the **strength of the interaction** between the two. A high-affinity drug binds more readily, leading to stronger or more sustained effects. **Potency** is often characterized by the **effective concentration (EC50)**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âthe concentration at which the drug achieves **50% of its maximal effect**.

The **therapeutic effect** of a drug is often visualized through **dose-response curves**, which show the relationship between dose and the resulting biological effect. Key terms include:

- **Emax**: The maximum possible effect a drug can produce.
- **Therapeutic window**: The range of doses that produce a therapeutic effect without causing toxicity.

### Mechanism of Action (MOA)

A drugÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s **mechanism of action (MOA)** describes how it exerts its effects at the molecular level. For example:

- **Beta blockers** are drugs that **inhibit beta-adrenergic receptors** involved in the bodyÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œfight-or-flightÃƒÂ¢Ã¢â€šÂ¬Ã‚Â response. They are used in cardiovascular medicine to slow heart rate and reduce blood pressure.
- Some beta blockers are highly **selective** for particular receptor subtypes, while others have broader effects, impacting other receptors and leading to **side effects**.

Understanding a drugÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s MOA is essential in predicting its **therapeutic effects** and **side effects**. Drugs targeting **enzymes** often block enzymatic activity, whereas drugs targeting **receptors** may initiate complex **signaling cascades**, which can have broader, context-dependent effects based on other molecules in the pathway.

### Dose-Response Relationships and Therapeutic Window

**Dose-response curves** illustrate how increasing drug doses correlate with biological effects. At higher concentrations, the drug **saturates its target receptors**, meaning additional doses will not increase the therapeutic effect but may heighten **toxicity**.

The **therapeutic window** is the range between an effective dose and a dose that causes toxicity. A narrow therapeutic window means careful dosing is essential, as even small increases in dose can lead to adverse effects.

### Tolerance and Sensitization

Drugs often exhibit changes in effectiveness over time:

- **Tolerance**: The body adapts, requiring **higher doses** to achieve the same effect. This adaptation may involve **increased drug metabolism** or **downregulation** of receptors.
- **Sensitization**: In rare cases, repeated drug exposure **enhances responsiveness** to the drug, often through **upregulation of receptors** or **increased pathway sensitivity**.

Understanding these dynamics is critical in managing **long-term treatment regimens** and reducing **risks of dependency**.

### Toxicology

**Toxicology** focuses on the **adverse effects** of drugs, studying both **acute toxicity** (effects from a single dose) and **chronic toxicity** (effects from repeated exposure). Toxicity can arise from **off-target effects**, where the drug binds to unintended receptors, or from the **metabolic byproducts** of the drug, which may be toxic. For example:

- **Acetaminophen (Tylenol)** is safe at low doses but can produce **toxic metabolites** in high doses, especially in individuals with compromised liver function.

The balance of **therapeutic effects** and **toxicity** is fundamental in pharmacodynamics, shaping decisions on **dosage**, **frequency**, and **administration routes** for safe and effective drug use.

### Conclusion

Pharmacodynamics provides a detailed map of **how drugs exert their effects** on the body, from binding interactions to downstream signaling pathways and physiological outcomes. Understanding PD is crucial for optimizing **efficacy**, **selectivity**, and **safety** in drug development, ensuring that therapeutic goals are met while minimizing adverse reactions. This depth of insight allows for the development of precision therapies tailored to individual patient needs and more effective management of diverse medical conditions.

## [49:39](https://www.youtube.com/watch?v=m_R_6ItR-qY&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=13&t=2979s) Toxicology: Assessing the Safety and Side Effects of Drugs

**Toxicology** is the study of a drugÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s **potential adverse effects** and is crucial for determining its **safety profile** before it can be approved for use. This field assesses the **risk of toxicity** across various systems and scenarios, ensuring that the drug achieves therapeutic goals without posing unacceptable risks to health.

### Types of Toxicology Studies

Toxicology studies assess multiple dimensions of drug safety:

- **Acute Toxicity**: Observes immediate reactions following drug administration. These studies help identify **early side effects** or **toxic responses**.
- **DNA Damage**: Tests if a drug can cause **genotoxic effects**, potentially leading to mutations or cancer.
- **Reproductive Health**: Evaluates effects on **fertility, fetal development,** and the overall health of offspring, critical for drugs intended for reproductive-age populations.
- **Carcinogenicity**: Studies if long-term exposure to the drug increases the risk of **cancer**, which is a costly and time-intensive process, often involving **extended observation periods**.

Additionally, **organ-specific toxicity** is examined, targeting essential systems like the **central nervous system, respiratory system, and cardiovascular system**. Such studies are often performed in **animal models** before human trials to ensure that no severe organ damage occurs.

### Therapeutic Index and Its Importance

The **therapeutic index (TI)** is a key measure of a drugÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s safety. It reflects the **gap between the effective dose** (where the drug has a therapeutic effect) and the **toxic dose** (where adverse effects appear):

- **High TI**: Indicates a wide margin between therapeutic and toxic doses, allowing for safer administration without close monitoring.
- **Low TI**: Shows a narrow margin, making dosing challenging, as small variations can lead to toxicity.

For example, **warfarin**, a blood thinner, has a narrow TI. Too low a dose renders it ineffective, while too high a dose can cause dangerous bleeding. The **microbiome** can further complicate dosing by **metabolizing warfarin differently** in each individual, introducing variability that makes accurate dosing even harder.

### Drug Interactions

Drugs can interact in ways that enhance or diminish their effects:

- **Synergistic Interactions**: Two drugs combined may produce a stronger effect than either alone. For instance, **alcohol** and **sedatives** both depress the central nervous system. When taken together, they can produce a profound, potentially dangerous sedative effect.
- **Antagonistic Interactions**: One drug may counteract or block the action of another. **Naloxone**, for example, binds to **opioid receptors**, effectively blocking opioid drugs from binding, which is why itÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s used as an antidote for opioid overdose.
- **Additive Effects**: Some drugs combine in an additive way, where their effects are simply the sum of each drug's individual effects. For instance, **antihypertensive drugs** used together may collectively lower blood pressure more effectively, but this requires careful balancing to avoid excessive drops.

### Conclusion

Toxicology provides a comprehensive view of the potential risks associated with drug use, from acute responses to long-term effects on genetic stability and organ health. A strong **therapeutic index** and careful **assessment of drug interactions** are central to ensuring a drugÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s safety in diverse patient populations. Through these studies, toxicology helps ensure that medications provide the maximum therapeutic benefit with the least risk, guiding their safe and effective use in clinical settings.

## [54:15](https://www.youtube.com/watch?v=m_R_6ItR-qY&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=13&t=3255s) Steps in the drug development process

The drug development process is a **highly structured, multi-phase endeavor** that begins with a promising idea for **targeting a disease** and endsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âif successfulÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âwith a **marketable therapeutic**. This pathway involves intense **scientific validation, optimization of candidate compounds**, and extensive testing for safety and efficacy. LetÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s break down each of the stages involved:

### 1\. Target Identification

The first step is **identifying a target**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âtypically a protein or gene that plays a central role in the diseaseÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s mechanism. **Target selection** is rooted in **bioinformatics, genomics, and proteomics**, often using high-throughput screening or bioinformatic tools. Key considerations include:

- **Disease connection**: How integral is this target to the disease?
- **Druggability**: Can a small molecule or biologic agent effectively bind to this target?
- **Structural availability**: Are there structural data or predictions (e.g., using AlphaFold) that can guide binding predictions?

Targets generally include proteins like **enzymes, receptors**, or signaling proteins essential to the disease mechanism. Some targets, however, may be challenging due to their **lack of stable binding sites**, as with disordered proteins or large, flat surfaces on transcription factors.

### 2\. Target Validation

After identifying a target, **target validation** ensures it plays a causative role in the disease. Techniques for validation include:

- **CRISPR screens** and **overexpression studies** to manipulate gene activity and observe outcomes.
- **Animal models** that replicate disease states.
- **Biomarker analysis** in human samples, offering early indications of therapeutic efficacy.

Target validation is critical to confirm that modulating this target will indeed produce a **therapeutic effect**, as opposed to targeting an unrelated or ineffective component of the disease mechanism.

### 3\. Hit Identification

With a validated target, the next step is **identifying potential hit compounds** that interact with the target. Methods include:

- **High-throughput screening (HTS)**: Screens a vast chemical library using biochemical or cell-based assays to find initial compounds showing activity.
- **Fragment-based screening**: Involves smaller chemical fragments that bind weakly at high concentrations, which can then be expanded into more potent compounds.
- **Virtual screening**: Uses computational methods to predict compounds likely to bind effectively based on the targetÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s structure, leveraging tools from molecular docking to machine learning.

Hit identification is a winnowing process, often beginning with **millions of compounds**, from which a subset with desirable binding properties is selected.

### 4\. Hit to Lead Optimization

Once a set of hits has been identified, the next stage is **hit to lead** optimization. Here, chemists refine **chemical structures** and study their **structure-activity relationships (SAR)** to improve binding affinity, specificity, and pharmacokinetics:

- **Structural modifications** are iteratively applied and tested to increase efficacy, minimize off-target effects, and improve the compoundÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s stability and solubility.
- **Initial pharmacokinetic assessments** are conducted to assess absorption, distribution, metabolism, and excretion (ADME) characteristics.

This step transitions promising hits into **lead compounds** that have undergone preliminary improvements and are ready for more focused development.

### 5\. Lead Optimization

The lead compounds are now ready for **extensive refinement**. This stage is where **medicinal chemistry** and **biophysical studies** intensify, optimizing compounds for:

- **Increased binding affinity** to the target, enhancing efficacy.
- **Reduced off-target effects**, minimizing potential toxicity.
- **Optimal pharmacokinetic properties**, including half-life and bioavailability.
- **Efficacy in disease models**, ensuring the therapeutic effects seen in early tests translate effectively in more complex models.

Lead optimization typically reduces the number of candidate compounds to a **handful of leads** that balance therapeutic efficacy with acceptable safety profiles, setting the stage for preclinical and clinical studies.

#### Key Concepts in Drug Targeting

- **Structure-Activity Relationship (SAR)**: The relationship between a molecule's structure and its biological activity, guiding chemical modifications to enhance activity or reduce side effects.
- **Drugability**: The potential for a target to be modulated by a drug, influenced by factors like the presence of a well-defined binding pocket.
- **High-Throughput Screening (HTS)**: Allows the rapid testing of large libraries of compounds against a target to find initial hits, using automated systems.

### Conclusion

The drug development process is **incremental and multi-faceted**, involving deep **biological validation, chemical optimization**, and early pharmacological testing. Each stage refines and narrows the field of candidates, moving from thousands of possibilities to a few carefully engineered compounds. By the time a candidate emerges for clinical trials, it has been rigorously tested and optimized, ensuring that it has the best possible chance of success in treating the targeted disease.

## [1:05:18](https://www.youtube.com/watch?v=m_R_6ItR-qY&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=13&t=3918s) Structure-Activity Relationships (SAR)

The study of **structure-activity relationships (SAR)** is foundational in drug development, guiding the optimization of lead compounds to enhance **efficacy, specificity, and safety**. SAR is the study of how a drugÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s **chemical structure** influences its **biological activity**, allowing researchers to pinpoint and modify parts of the molecule to achieve desired properties.

### Key Goals in SAR Analysis

1.  **Identify essential structural features** necessary for biological activity.
2.  **Enhance potency** by making modifications that improve binding affinity to the target.
3.  **Reduce off-target effects** to increase specificity and reduce potential side effects.
4.  **Minimize toxicity** by identifying structural components that contribute to harmful effects.
5.  **Optimize pharmacokinetics (PK)** properties, including absorption, distribution, metabolism, and excretion (ADME).

### The SAR Process

The SAR process is iterative and data-driven, involving the following steps:

- **Starting with Lead Compounds**: Researchers begin with a promising lead compound identified in earlier stages of drug development. The leadÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s **interaction with its target** is examined, ideally using structural data such as **crystal structures** of the target protein bound to the compound.
- **Predicting Modifications**: Based on the initial structure, researchers hypothesize how chemical modifications might affect binding, activity, and other properties. This might include changing side chains, adding or removing rings, or modifying bond types.
- **Empirical Testing**: Modified compounds are synthesized and tested to observe changes in activity, potency, and selectivity. Over time, the accumulation of SAR data allows researchers to refine their predictions and develop an increasingly accurate understanding of how structural changes impact the moleculeÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s properties.

### Common Strategies for Structural Modifications

To enhance the drug's efficacy, specificity, and stability, a range of structural modifications can be applied:

- **Alkyl Chain Variations**: Adjusting the length and branching of alkyl chains can impact how the molecule fits within the binding site and affects interactions.
- **Linker Length Adjustments**: Changing the length and flexibility of linkers between parts of the molecule can influence its orientation and binding.
- **Incorporation of Rings and Double Bonds**: Introducing rings and double bonds can reduce the molecule's **rotational freedom**. By restricting conformations, these modifications reduce **entropy loss** upon binding, enhancing the compound's binding affinity.
- **Use of Conformational Constraints**: Adding structural constraints, such as ring systems, can lock the molecule into preferred conformations, improving target binding.

### Quantitative SAR (QSAR) and Computational Methods

**Quantitative Structure-Activity Relationship (QSAR)** methods use **statistical and computational tools** to model the relationship between structural properties and biological activity quantitatively. QSAR models often involve machine learning and deep learning algorithms to predict a compoundÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s **biological activity** based on its structural features.

These models can significantly speed up the SAR process by:

- **Predicting toxicological properties** before synthesis, thereby identifying compounds with higher safety profiles.
- **Screening for activity** across large virtual libraries, identifying promising compounds without the need for extensive experimental testing.

### Challenges in SAR

Despite advances, several challenges remain in SAR analysis:

1.  **Balancing Multiple Properties**: Modifications to improve one aspect, such as binding affinity, may negatively impact others, such as PK properties or toxicity.
2.  **Off-Target Effects**: A compound may interact with unintended proteins, leading to adverse effects. **Kinase inhibitors**, for example, often show broad activity, which can result in off-target interactions.
3.  **Complexity of Biological Systems**: Biological systems are complex and interconnected, meaning changes to structure can have unpredictable downstream effects.

### Conclusion

**SAR** is a central component of the drug development process, transforming initial hits into highly refined lead compounds ready for preclinical evaluation. By integrating **empirical testing, computational modeling**, and **quantitative SAR (QSAR)**, researchers can systematically optimize compounds to achieve maximal efficacy with minimal adverse effects. The SAR process is one of continuous learning and refinement, balancing various chemical and biological factors to develop safe, effective therapeutic agents.

## [1:10:17](https://www.youtube.com/watch?v=m_R_6ItR-qY&list=PLypiXJdtIca4gtioEPLIExlAKvu64z7rc&index=13&t=4217s) Drug development timeline

The **drug development timeline** is extensive and rigorous, reflecting the high standards set to ensure both efficacy and safety. The journey from initial **drug discovery** to an approved product on the market often spans **decades** and involves multiple distinct phases, each with significant hurdles and regulatory oversight.

1.  **Drug Discovery Phase**:
    - This initial stage can take years or even decades, involving **target identification**, **hit discovery**, and early **lead optimization**.
    - Only a fraction of the initial candidates move forward, with many potential compounds failing due to lack of efficacy or issues with safety and drugability.
2.  **Preclinical Testing**:
    - Once promising leads are identified, they undergo preclinical testing in **cell cultures** and **animal models**. This stage evaluates basic **efficacy, toxicity, pharmacokinetics (PK)**, and **pharmacodynamics (PD)**.
    - At this stage, scientists gather data to support the **Investigational New Drug (IND) application** required by regulatory bodies like the **FDA**.
3.  **IND Application**:
    - Submitting an IND application to the FDA is a critical step before clinical trials can begin. This comprehensive document includes **safety data**, **manufacturing information**, and the proposed **clinical trial plan**.
    - If the FDA does not object within a specified timeframe, the drug sponsor can proceed to **Phase I clinical trials**.

### Clinical Trial Phases

The clinical trials are divided into **three main phases**, each designed to answer specific questions about the drug.

1.  **Phase I** ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“ **Safety and Dosage**:
    - Conducted in a small group of **20-80 healthy volunteers** or patients, Phase I focuses on **safety** and determining an appropriate **dosage range**.
    - The goal is to assess the **initial PK/PD** profile and identify any adverse effects. Dosing begins very low and is increased gradually to observe tolerability and PK characteristics.
2.  **Phase II** ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“ **Efficacy and Side Effects**:
    - Phase II involves a larger group of **a few dozen to several hundred patients** who have the disease or condition being targeted.
    - This phase refines dosing regimens and looks for **preliminary signs of efficacy** while continuing to monitor safety. Companies may test various doses and schedules to determine an optimal dosing strategy.
    - While still focused on safety, Phase II trials also provide initial efficacy data, crucial for deciding whether to invest further in costly Phase III trials.
3.  **Phase III** ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“ **Large-Scale Testing**:
    - Phase III trials are **large-scale studies** involving hundreds to thousands of patients, providing the data required for **regulatory approval**.
    - These studies confirm efficacy, monitor side effects, and collect comprehensive safety data across a broader, more diverse patient population.
    - Due to the scale of these trials, Phase III is costly and time-intensive, but it provides the critical evidence needed for the final regulatory decision.

### Post-Market Surveillance (Phase IV)

After approval, **Phase IV studies** or **post-market surveillance** continues to monitor the drug's performance in the general population. This phase assesses **long-term safety** and may reveal rare side effects not observed during clinical trials.

### Probability of Success and Attrition Rates

- **Attrition is high** throughout this process. Notably, only about **14% of drugs** entering clinical trials are ultimately approved.
- Oncology drugs, for instance, have an especially low success rate, with an estimated **3% success** from Phase I through approval. The high risk reflects the complexity of cancer biology and the stringent requirements for oncology treatments.

### FDA and Regulatory Standards

The **FDA** and other regulatory agencies play a central role in drug development, overseeing each phase and setting the standards for **safety, efficacy, and quality**. The agency enforces regulations covering everything from the design of clinical trials to the manufacturing standards required to ensure drug consistency.

### Financial Implications

- Drug development is incredibly costly, with estimates around **$1 billion** to bring a single drug to market. These costs include not only successful drugs but also the cumulative expenses of failed trials.
- Additionally, the FDA approval process itself involves substantial industry fees. For example, fees are associated with IND and New Drug Application (NDA) filings, which fund part of the regulatory review process.

### Types of FDA-Approved Drugs

The types of drugs approved by the FDA vary widely, with a significant focus on **oncology, psychiatry, and infectious diseases**. However, many approved drugs are modifications or improvements of existing therapies rather than entirely new molecular entities.

In summary, drug development is a **complex, multi-phase process** demanding significant time, resources, and regulatory compliance. The rigorous timeline and high attrition rate highlight the difficulty and expense of developing safe and effective treatments, underscoring the role of precision and innovationÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âparticularly the potential of **AI and machine learning**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âin improving this process. In subsequent discussions, we will explore how modern computational methods can help streamline and potentially shorten the drug development timeline, improve the likelihood of success, and reduce overall costs.


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
You should be able to explain how drug classes, pharmacokinetics, pharmacodynamics, GPCRs, therapeutic windows, toxicology, drug interactions, and clinical trials connects a biological problem to a computational representation, model, or algorithm.

### Q2. What should you be able to explain from this lecture?
You should be able to explain how drug classes, pharmacokinetics, pharmacodynamics, GPCRs, therapeutic windows, toxicology, drug interactions, and clinical trials connects a biological problem to a computational representation, model, or algorithm.

### Q3. What should you be able to explain from this lecture?
You should be able to explain how drug classes, pharmacokinetics, pharmacodynamics, GPCRs, therapeutic windows, toxicology, drug interactions, and clinical trials connects a biological problem to a computational representation, model, or algorithm.

### Q4. What should you be able to explain from this lecture?
You should be able to explain how drug classes, pharmacokinetics, pharmacodynamics, GPCRs, therapeutic windows, toxicology, drug interactions, and clinical trials connects a biological problem to a computational representation, model, or algorithm.

### Q5. What should you be able to explain from this lecture?
You should be able to explain how drug classes, pharmacokinetics, pharmacodynamics, GPCRs, therapeutic windows, toxicology, drug interactions, and clinical trials connects a biological problem to a computational representation, model, or algorithm.

### Q6. What should you be able to explain from this lecture?
You should be able to explain how drug classes, pharmacokinetics, pharmacodynamics, GPCRs, therapeutic windows, toxicology, drug interactions, and clinical trials connects a biological problem to a computational representation, model, or algorithm.

### Q7. What should you be able to explain from this lecture?
You should be able to explain how drug classes, pharmacokinetics, pharmacodynamics, GPCRs, therapeutic windows, toxicology, drug interactions, and clinical trials connects a biological problem to a computational representation, model, or algorithm.

### Q8. What should you be able to explain from this lecture?
You should be able to explain how drug classes, pharmacokinetics, pharmacodynamics, GPCRs, therapeutic windows, toxicology, drug interactions, and clinical trials connects a biological problem to a computational representation, model, or algorithm.

### Q9. What should you be able to explain from this lecture?
You should be able to explain how drug classes, pharmacokinetics, pharmacodynamics, GPCRs, therapeutic windows, toxicology, drug interactions, and clinical trials connects a biological problem to a computational representation, model, or algorithm.

### Q10. What should you be able to explain from this lecture?
You should be able to explain how drug classes, pharmacokinetics, pharmacodynamics, GPCRs, therapeutic windows, toxicology, drug interactions, and clinical trials connects a biological problem to a computational representation, model, or algorithm.

## Key Takeaways
- drug classes, pharmacokinetics, pharmacodynamics, GPCRs, therapeutic windows, toxicology, drug interactions, and clinical trials is part of the MLCB modeling arc.
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

- [[drug-discovery]]
- [[admet]]
- [[virtual-screening]]
- [[molecular-docking]]
- [[drug-target]]
- [[small-molecule]]

### Cluster Membership

- [[cluster-map-drug-discovery]]

### Key Relationships (from KG)

See [[lecture-entity-map]] for the full relationship list, and [[knowledge-graph-index]] for the global entity index.
