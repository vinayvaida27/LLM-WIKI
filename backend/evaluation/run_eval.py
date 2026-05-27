"""
Retrieval Evaluation Runner

Usage (from backend/ directory):
    python -m evaluation.run_eval
    python -m evaluation.run_eval --top-k 5 --output results.json
    python -m evaluation.run_eval --experiment-id exp_002 --description "test new weights"

Loads the golden test set, runs _retrieve_pipeline() for each question,
computes metrics, prints a summary, and appends an entry to
Evaluation/backend_retrieval_experiments.md.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

# ── path setup ────────────────────────────────────────────────────────────────
# Allow running from backend/ directory
_HERE = Path(__file__).parent
_BACKEND = _HERE.parent
if str(_BACKEND) not in sys.path:
    sys.path.insert(0, str(_BACKEND))

from dotenv import load_dotenv
load_dotenv(_BACKEND / ".env")

# Import app internals after env is loaded
import importlib
app_module = importlib.import_module("app")
_retrieve_pipeline = getattr(app_module, "_retrieve_pipeline")

from evaluation.metrics import compute_all

# ── helpers ───────────────────────────────────────────────────────────────────

def _load_golden_set(path: Path) -> List[Dict[str, Any]]:
    result = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                result.append(json.loads(line))
    return result


def _load_entity_lecture_map(entity_index_path: Path) -> Dict[str, List[int]]:
    with open(entity_index_path, encoding="utf-8") as f:
        ei = json.load(f)
    return {
        k: [int(l) for l in v.get("lectures", [])]
        for k, v in ei.items()
        if not k.startswith("_")
    }


def _format_bar(value: float, width: int = 20) -> str:
    filled = int(value * width)
    return f"[{'#' * filled}{'-' * (width - filled)}] {value:.2f}"


# ── main evaluation loop ──────────────────────────────────────────────────────

def run_evaluation(
    top_k: int = 5,
    output_path: Path | None = None,
    experiment_id: str = "",
    description: str = "",
) -> Dict[str, Any]:
    golden_path     = _HERE / "golden_set.jsonl"
    entity_idx_path = _BACKEND.parent / "llm-wiki" / "retrieval" / "entity_index.json"
    exp_log_path    = _BACKEND.parent / "Evaluation" / "backend_retrieval_experiments.md"

    questions        = _load_golden_set(golden_path)
    entity_lec_map   = _load_entity_lecture_map(entity_idx_path)

    all_metrics: List[Dict[str, Any]] = []
    per_question: List[Dict[str, Any]] = []

    print(f"\n{'='*65}")
    print(f"  LLM-Wiki Retrieval Evaluation  |  top_k={top_k}  |  {len(questions)} questions")
    print(f"{'='*65}\n")

    for q in questions:
        qid            = q["id"]
        query          = q["query"]
        expected       = q.get("expected_entities", [])
        answer_type    = q.get("expected_answer_type", "answer")

        t0 = time.perf_counter()
        try:
            chunks, analysis, strategy = _retrieve_pipeline(query, top_k)
        except Exception as e:
            print(f"  [{qid}] ERROR: {e}")
            continue
        elapsed = time.perf_counter() - t0

        m = compute_all(chunks, expected, entity_lec_map, k=top_k)

        # For refuse questions: expected_answer_type="refuse" means good result = no chunks
        if answer_type == "refuse":
            expected_refuse = len(chunks) == 0 or (chunks[0].get("score", 0) < 2.0
                                                    and len(chunks) <= 2)
            m["expected_refuse"] = float(expected_refuse)

        m["qid"]       = qid
        m["strategy"]  = strategy
        m["latency_s"] = round(elapsed, 3)
        m["n_chunks"]  = len(chunks)
        m["n_raw"]     = sum(1 for c in chunks if c.get("layer") == "raw_chunk")
        m["query"]     = query[:60]

        all_metrics.append(m)

        flag = "OK" if m.get(f"hit@{top_k}", 0) == 1.0 or answer_type == "refuse" else "--"
        print(
            f"  {flag} [{qid}] {query[:50]:<50}  "
            f"hit@{top_k}={m.get(f'hit@{top_k}',0):.0f}  "
            f"rcf={m['raw_chunk_fraction']:.2f}  "
            f"strategy={strategy:<30}  {elapsed:.2f}s"
        )

        per_question.append({**m, "expected_entities": expected})

    if not all_metrics:
        print("No results collected.")
        return {}

    # ── aggregate summary ─────────────────────────────────────────────────
    keys = [f"hit@{top_k}", "mrr", f"ndcg@{top_k}", "entity_coverage",
            "raw_chunk_fraction", "duplicate_rate"]
    agg = {k: sum(m.get(k, 0) for m in all_metrics) / len(all_metrics) for k in keys}
    agg["avg_latency_s"]  = sum(m["latency_s"] for m in all_metrics) / len(all_metrics)
    agg["avg_raw_chunks"] = sum(m["n_raw"] for m in all_metrics) / len(all_metrics)
    agg["n_questions"]    = len(all_metrics)

    print(f"\n{'-'*65}")
    print("  Aggregate Metrics")
    print(f"{'-'*65}")
    print(f"  Hit@{top_k}             {_format_bar(agg[f'hit@{top_k}'])}")
    print(f"  MRR               {_format_bar(agg['mrr'])}")
    print(f"  nDCG@{top_k}           {_format_bar(agg[f'ndcg@{top_k}'])}")
    print(f"  Entity Coverage   {_format_bar(agg['entity_coverage'])}")
    print(f"  Raw Chunk Frac.   {_format_bar(agg['raw_chunk_fraction'])}")
    print(f"  Duplicate Rate    {_format_bar(agg['duplicate_rate'])}")
    print(f"  Avg Latency       {agg['avg_latency_s']:.3f}s")
    print(f"{'='*65}\n")

    result = {"aggregate": agg, "per_question": per_question}

    # ── save JSON output ──────────────────────────────────────────────────
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"  Results saved to: {output_path}")

    # ── append to experiment log ──────────────────────────────────────────
    exp_log_path.parent.mkdir(parents=True, exist_ok=True)
    exp_ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    exp_entry = f"""
## {experiment_id or f'Exp-{int(time.time())}'} — {exp_ts}

**Description:** {description or 'Evaluation run'}
**top_k:** {top_k} | **Questions:** {len(all_metrics)}

| Metric | Score |
|--------|-------|
| Hit@{top_k} | {agg[f'hit@{top_k}']:.3f} |
| MRR | {agg['mrr']:.3f} |
| nDCG@{top_k} | {agg[f'ndcg@{top_k}']:.3f} |
| Entity Coverage | {agg['entity_coverage']:.3f} |
| Raw Chunk Fraction | {agg['raw_chunk_fraction']:.3f} |
| Duplicate Rate | {agg['duplicate_rate']:.3f} |
| Avg Latency | {agg['avg_latency_s']:.3f}s |

---
"""
    with open(exp_log_path, "a", encoding="utf-8") as f:
        f.write(exp_entry)
    print(f"  Experiment log updated: {exp_log_path.relative_to(exp_log_path.parents[1])}")

    return result


# ── CLI ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run LLM-Wiki retrieval evaluation")
    parser.add_argument("--top-k",        type=int, default=5)
    parser.add_argument("--output",       type=Path, default=None)
    parser.add_argument("--experiment-id", default="")
    parser.add_argument("--description",  default="")
    args = parser.parse_args()

    run_evaluation(
        top_k=args.top_k,
        output_path=args.output,
        experiment_id=args.experiment_id,
        description=args.description,
    )
