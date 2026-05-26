---
tags:
  - "log"
  - "deduplication"
topics:
  - "MLCB"
status: "generated"
created: 2026-05-25
updated: 2026-05-25
sources:
  - "Raw/Sources/lecture_08_intro_to_protein_structure.md"
  - "Raw/Sources/lecture_09_protein_folding_algorithms.md"
  - "Raw/Sources/lecture_10_protein_structure_with_transformers.md"
source_count: 3
aliases:
  - "Deduplication Report â€” Phase 2"
  - "deduplication_report"
---

# Deduplication Report â€” Phase 2

> [!info] Records all deduplication and cleanup actions taken during Phase 2 of the autoresearch integration.

## Summary

| Action Type | Count |
|---|---|
| Entity stubs converted to redirect pages | 6 |
| Entity stubs rewritten with real content | 1 |
| Cluster maps created (missing) | 2 |
| Wikilink fixes (backslash-pipe bug) | ~140 links across 12 files |
| KG metadata corrections | 2 (node_count, edge_count) |
| Redirect stubs from Phase 1 (prior session) | 3 |

**Total entity pages fixed:** 10  
**Total map files created:** 2  
**Total broken links resolved:** ~140

---

## Entity Redirect Stubs (Phase 1 â€” prior session)

| File | Old Content | Redirect Target | Reason |
|---|---|---|---|
| `Wiki/Entities/blast.md` | Template stub | `Wiki/Methods/blast.md` | BLAST is a method/tool, not a biological entity |
| `Wiki/Entities/variant.md` | Template stub | `Wiki/Entities/snp.md` | MLCB uses SNP as the primary variant type |
| `Wiki/Entities/chromatin-state.md` | Template stub | `Wiki/Entities/chromatin.md` | Chromatin state is a sub-concept of chromatin |

---

## Entity Redirect Stubs (Phase 2 â€” this session)

| File | Old Content | Redirect Target | Reason |
|---|---|---|---|
| `Wiki/Entities/transformer.md` | Template stub | `Wiki/Methods/transformer.md` | Transformer is an ML model architecture, not a biological entity |
| `Wiki/Entities/gwas.md` | Template stub | `Wiki/Methods/gwas.md` | GWAS is a statistical method, not a biological entity |
| `Wiki/Entities/molecule.md` | Template stub | `Wiki/Entities/small-molecule.md` | Too generic; MLCB uses `small-molecule` as canonical |
| `Wiki/Entities/alphafold.md` | Template stub | `Wiki/Entities/alphafold2.md` | KG canonical ID is `alphafold2`; course covers AlphaFold2 specifically |
| `Wiki/Entities/gene-expression.md` | Template stub | `Wiki/Entities/gene-expression-matrix.md` | Computational context â†’ data matrix representation |

---

## Entity Stubs Rewritten with Real Content

| File | Old Content | New Content Summary |
|---|---|---|
| `Wiki/Entities/pdb.md` | Template stub | Full entry: Protein Data Bank, role in Lectures 8â€“10, stats table, connection to AlphaFold2 |

---

## Missing Cluster Maps Created

| File | Covers | Referenced From |
|---|---|---|
| `Wiki/Maps/cluster-map-generative-models.md` | VAE, diffusion model, latent space | `cluster-map-drug-discovery.md` |
| `Wiki/Maps/cluster-map-sequence-analysis.md` | Sequence alignment, HMM, MSA, DNA/protein sequences | `cluster-map-classical-ml.md` |

---

## Systemic Wikilink Bug Fixed

**Bug:** All 12 cluster map tables used `id\|label` (backslash before pipe). Obsidian treats `\|` as a literal backslash+pipe, breaking the wikilink and creating phantom targets like `alphafold2\` in the graph.

**Fix:** `fix_links.py` applied regex substitution to 12 files:
```python
re.sub(r'\[\[([^|\]\\]+)\\([|][^\]]*)\]\]', replacement with the captured target and label, txt)
```

Files affected:
- `cluster-map-foundations.md`
- `cluster-map-classical-ml.md`
- `cluster-map-deep-learning.md`
- `cluster-map-genomics.md`
- `cluster-map-epigenomics.md`
- `cluster-map-regulatory-genomics.md`
- `cluster-map-protein.md`
- `cluster-map-genomics-ml.md`
- `cluster-map-drug-discovery.md`
- `cluster-map-genetics-disease.md`
- `high-importance-entity-map.md`
- `knowledge-graph-index.md`

Script deleted after use.

---

## Remaining Issues (Phase 3 scope)

1. **Orphan nodes in KG** â€” `scoring-matrix`, `manolis-kellis`, `eric-alm` have no edges
2. **Wrong source lists** â€” entity stubs still list all 18 lectures as sources
3. **Phantom wikilink targets** â€” `mlcb-2024-computational-biology`, `mlcb-cross-lecture-connections`, `mlcb-biology-for-ml-students` are referenced but don't exist
4. **Thin entity stubs** â€” high-importance entities still have minimal content

---

## Alias Consistency Check

The following aliases were added or confirmed in `retrieval/entity_aliases.json` during this phase:

| Alias | Canonical ID |
|---|---|
| `AlphaFold` | `alphafold2` |
| `AlphaFold 2` | `alphafold2` |
| `Molecule` | `small-molecule` |
| `Chemical Molecule` | `small-molecule` |
| `Gene Expression` | `gene-expression-matrix` |
| `mRNA Expression` | `gene-expression-matrix` |
| `Protein Data Bank` | `pdb` |
| `RCSB PDB` | `pdb` |
| `Genome-Wide Association Study` | `gwas` |
| `Transformer Architecture` | `transformer` |

---

## Navigation

[[graph_health_report]] Â· [[update-log]] Â· [[knowledge-graph-index]]

## Graph Connections
- [[knowledge-graph-index]]
- [[mlcb-cross-lecture-connections]]
- [[mlcb-2024-computational-biology]]
