---
tags:
  - "method"
topics:
  - "MLCB"
status: "updated"
created: 2026-05-24
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_01_course_introduction.md"
source_count: 1
aliases:
  - "Graph Neural Networks"
  - "GNNs"
  - "graph-neural-network"
  - "Graph Neural Network"
  - "GNN"
  - "Graph Network"
  - "graph neural network"
---

# Graph Neural Networks

## Purpose
Graph Neural Networks are used when the biological or chemical object is best represented as nodes connected by edges. Lecture 1 introduces them as an extension of [[representation-learning]] from grids and sequences into irregular relational structures.

## Input Data
The input is a graph:
- nodes, such as atoms, proteins, genes, or network entities
- edges, such as chemical bonds, physical interactions, regulatory links, or pathway connections
- node features, such as atom charge, hydrophobicity, polarity, or other intrinsic properties

## Output
A GNN can produce:
- node embeddings
- edge predictions
- whole-graph embeddings
- property predictions for molecules or biological networks
- latent representations that can support downstream prediction or generation

## Core Intuition
A GNN learns by repeatedly letting each node look at its neighbors. The first layer starts with intrinsic node properties. The next layer mixes in direct-neighbor context. Deeper layers include neighbors of neighbors. This is why a GNN can learn not only what an atom is, but what chemical neighborhood it sits in.

## Algorithm Steps
1. Represent the object as a graph with nodes, edges, and node features.
2. Initialize each node with its local properties.
3. Aggregate messages from neighboring nodes.
4. Update each node representation using the aggregated neighborhood information.
5. Repeat for multiple layers so larger neighborhoods influence the representation.
6. Pool or read out node representations if a whole-graph prediction is needed.

## Mathematical Form
Lecture 1 gives the conceptual update rather than a formal equation. See [[gnn-message-passing]] for the course-level message-passing equation page.

## Use in Computational Biology
Lecture 1 names several graph settings:
- molecules, where atoms are nodes and bonds are edges
- protein-protein interaction networks
- gene regulatory networks
- metabolic pathways
- drug-discovery settings where chemical compounds are linked to disease effects

## Strengths
- Works on irregular structures that do not fit image grids or simple sequences.
- Preserves relational information instead of flattening objects into independent features.
- Builds hierarchical representations from local neighborhoods to larger graph context.

## Limitations
- The graph representation matters: missing or wrong edges can hide biology.
- More layers are not automatically better; later lectures revisit oversmoothing and graph-depth issues.
- A learned graph embedding can be predictive without being a validated biological mechanism.

## Lecture References
- [[lecture-01-course-introduction]]
- [[lecture-14-chemistry-gnns]]
- [[lecture-15-generating-new-molecules]]


## Graph Links

### Parent Topics
- [[topic-regulatory-networks|Regulatory Networks]]

## Related Methods
- [[representation-learning]]
- [[gnn-message-passing]]
- [[drug-discovery-and-molecular-generation]]
- [[variational-autoencoders]]

## Example From Lecture
In the molecule example, each atom begins with properties such as hydrophobicity, charge, and polarity. A first GNN layer updates each atom based on its direct neighbors. A second layer adds information from a wider neighborhood. The resulting latent representation can help predict chemical reactivity, toxicity, therapeutic effect, or other molecule-level behavior.
