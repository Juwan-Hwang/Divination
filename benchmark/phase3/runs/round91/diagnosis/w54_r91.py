#!/usr/bin/env python3
"""W54 (R91) aggregate-only recomputation for DIAG-LR-weight-dev91.

Licensed inputs only:
- runs/round91/diagnosis/lr-negatives-dev91.json (per-case pair_diff listing)
- runs/round91/final-scores.json analysis_r91 aggregate section ONLY
  (ours_axis2 / ours_sub are never touched)
No predictions / judging / gold files are opened.
"""
import json
import statistics
from pathlib import Path

BASE = Path("/home/hatch/workspace/divination/benchmark/phase3")
NEG = BASE / "runs/round91/diagnosis/lr-negatives-dev91.json"
FS = BASE / "runs/round91/final-scores.json"

neg_doc = json.loads(NEG.read_text(encoding="utf-8"))
negs = neg_doc["negatives"]
assert neg_doc["n_negative"] == len(negs), "n_negative mismatch"
assert neg_doc["n_liuren_total"] == 30

# self-consistency: pair_diff == ours - master for every listed case
for e in negs:
    assert abs((e["ours"] - e["master"]) - e["pair_diff"]) < 1e-9, e["case_id"]
    assert e["pair_diff"] < 0, e["case_id"]

def seg_stats(rows):
    diffs = [r["pair_diff"] for r in rows]
    return {
        "n": len(rows),
        "sum": round(sum(diffs), 4),
        "mean": round(statistics.mean(diffs), 4),
        "median": round(statistics.median(diffs), 4),
        "ids": [r["case_id"] for r in rows],
    }

dev8 = [e for e in negs if e["in_dev8"]]
lr3 = [e for e in negs if not e["in_dev8"]]
out = {
    "n_liuren_total": neg_doc["n_liuren_total"],
    "n_negative": len(negs),
    "dev8": seg_stats(dev8),
    "lr3": seg_stats(lr3),
    "merged": seg_stats(negs),
    "lr3_010": next(
        ({"case_id": e["case_id"], "pair_diff": e["pair_diff"], "in_dev8": e["in_dev8"]}
         for e in negs if e["case_id"] == "LR3-010"), None),
}

# aggregate cross-checks against analysis_r91 families / guardrails (aggregate only)
fs = json.loads(FS.read_text(encoding="utf-8"))
a = fs["analysis_r91"]
fam = a["families"]
out["crosscheck"] = {
    "liuren_merged": fam["liuren_merged"],
    "liuren_dev8": fam["liuren_dev8"],
    "liuren_lr3_new": fam["liuren_lr3_new"],
    "negatives_eq_merged_L": len(negs) == fam["liuren_merged"]["L"],
    "dev8_neg_eq_dev8_L": len(dev8) == fam["liuren_dev8"]["L"],
    "lr3_neg_eq_lr3_L": len(lr3) == fam["liuren_lr3_new"]["L"],
    "liuren_deterioration_guardrail": a["guardrails_attribution"]["liuren_continued_deterioration"],
    "platform_liuren_dev8": a["platform"]["b_guardrails"]["liuren_dev8"],
    "platform_all_stand": a["platform"]["all_stand"],
}
print(json.dumps(out, ensure_ascii=False, indent=2))
