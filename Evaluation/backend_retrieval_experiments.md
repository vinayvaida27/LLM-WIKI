# Backend Retrieval Experiment Log

Track every retrieval pipeline change: what changed, why, and whether it helped.

Run evaluation with:
```bash
cd backend
python -m evaluation.run_eval --experiment-id exp_002 --description "your description"
```

---

## Exp-000 — Baseline (BM25 only, wiki_chunk preferred)

**Description:** Original state before retrieval pipeline redesign.
**Date:** 2026-05-27

| Characteristic | Value |
|---------------|-------|
| Retrieval method | BM25 only (single-pass) |
| Layer boost | wiki_chunk=1.30, wiki_catalog=1.15, **raw_chunk=0.85** |
| Query analysis | None |
| Entity detection | None |
| Graph traversal | None |
| Reranking | None |
| Context packing | Simple top-k slice |

**Key problem:** raw_chunks penalised (0.85) — exact opposite of desired behaviour.
Synthesized wiki_chunks returned as primary evidence instead of lecture transcripts.

**Estimated metrics (no eval harness existed):**
| Metric | Estimated |
|--------|-----------|
| raw_chunk_fraction | ~0.20 (wiki_chunks dominated) |
| entity_coverage | ~0.30 (no entity-aware retrieval) |

---

## Exp-001 — Full Pipeline Redesign (2026-05-27)

**Description:** Complete retrieval pipeline redesign.
Changes made:
1. **Flip LAYER_BOOST**: raw_chunk 0.85 → 1.20, wiki_chunk 1.30 → 0.90
2. **QueryAnalyzer**: entity + intent detection using entity_aliases.json + entity_index.json
3. **GraphTraversal**: BFS over graph_edges/nodes to expand entity lecture set
4. **Reranker**: final_score = 0.50×bm25 + 0.30×entity_match + 0.20×layer_bonus
5. **ContextPacker**: dedup by text hash, raw_chunk preferred, char budget
6. **Updated system prompt**: raw_chunk = primary source of truth, layer-aware instructions
7. **Updated _normalize()**: preserve lecture_number, chunk_id, heading_path
8. **Updated _format_context()**: show layer, lecture number, heading path
9. **New response fields**: llm_wiki_retrieval_strategy, llm_wiki_entities_detected, llm_wiki_confidence

**Run evaluation to get actual metrics:**
```bash
cd backend
python -m evaluation.run_eval --experiment-id exp_001 --description "Full pipeline redesign"
```

**Expected improvements:**
- raw_chunk_fraction: 0.20 → >0.60
- entity_coverage: 0.30 → >0.60
- hit@5: expected increase due to entity+graph boosting
- duplicate_rate: expected decrease due to ContextPacker dedup

---

*Add new entries below after each experiment run.*


## Exp-001 — 2026-05-27 14:50 UTC

**Description:** Full pipeline: entity_boost + graph + reranker + raw_chunk priority
**top_k:** 5 | **Questions:** 20

| Metric | Score |
|--------|-------|
| Hit@5 | 0.850 |
| MRR | 0.825 |
| nDCG@5 | 0.822 |
| Entity Coverage | 0.942 |
| Raw Chunk Fraction | 0.970 |
| Duplicate Rate | 0.000 |
| Avg Latency | 0.031s |

---

## exp_002 — 2026-05-27 15:00 UTC

**Description:** BM25+entity+graph baseline after vector wiring (ENABLE_VECTOR_SEARCH=false)
**top_k:** 5 | **Questions:** 20

| Metric | Score |
|--------|-------|
| Hit@5 | 0.850 |
| MRR | 0.825 |
| nDCG@5 | 0.822 |
| Entity Coverage | 0.942 |
| Raw Chunk Fraction | 0.970 |
| Duplicate Rate | 0.000 |
| Avg Latency | 0.033s |

---
