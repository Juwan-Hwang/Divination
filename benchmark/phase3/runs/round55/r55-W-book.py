#!/usr/bin/env python3
"""R55 W monitoring: per-case book provenance + negative subset stats.
Reads only the round55 negatives list, final-scores ours_sub timing for
those ids, and inputs-dev12/<case_id>.json opened exactly by id.
No glob, no predictions/judging access.
"""
import json
from pathlib import Path

BASE = Path("/home/hatch/workspace/divination/benchmark/phase3")
neg_path = BASE / "runs/round55/diagnosis/lr-negatives-dev55.json"
fs_path = BASE / "runs/round55/final-scores.json"
inputs_dir = BASE / "inputs-dev12"

neg = json.loads(neg_path.read_text(encoding="utf-8"))
fs = json.loads(fs_path.read_text(encoding="utf-8"))
ours_sub = fs["ours_sub"]

def family(book: str) -> str:
    if "大六壬占验指南" in book:
        return "指南族"
    if "六壬断案" in book:
        return "断案族"
    if "六壬辨疑" in book:
        return "辨疑族"
    if "六壬粹言" in book:
        return "粹言族"
    return "其他族"

rows = []
for item in neg["negatives"]:
    cid = item["case_id"]
    card_path = inputs_dir / f"{cid}.json"
    card = json.loads(card_path.read_text(encoding="utf-8"))
    book = card.get("provenance", {}).get("book", "")
    rows.append({
        "case_id": cid,
        "tradition": item["tradition"],
        "in_dev8": item["in_dev8"],
        "pair_diff": item["pair_diff"],
        "book": book,
        "family": family(book),
        "timing": ours_sub.get(cid, {}).get("timing"),
        "total": ours_sub.get(cid, {}).get("total"),
    })

def mean(xs):
    return sum(xs) / len(xs) if xs else None

all_diffs = [r["pair_diff"] for r in rows]
dev8 = [r for r in rows if r["in_dev8"]]
non = [r for r in rows if not r["in_dev8"]]
print(f"n_total={neg['n_liuren_total']} n_negative={neg['n_negative']}")
print(f"neg_share={neg['n_negative']/neg['n_liuren_total']*100:.1f}%")
print(f"mean_all={mean(all_diffs):.4f} n={len(all_diffs)}")
print(f"mean_dev8={mean([r['pair_diff'] for r in dev8]):.4f} n={len(dev8)}")
print(f"mean_nondev8={mean([r['pair_diff'] for r in non]):.4f} n={len(non)}")

from collections import Counter
print("family_all", Counter(r["family"] for r in rows))
print("family_dev8", Counter(r["family"] for r in dev8))
print("family_non", Counter(r["family"] for r in non))

timings = [(r["case_id"], r["timing"], r["total"], r["in_dev8"]) for r in rows]
print(f"timing_mean_all={mean([t[1] for t in timings]):.4f}")
print(f"timing_mean_dev8={mean([t[1] for t in timings if t[3]]):.4f}")
print(f"timing_mean_non={mean([t[1] for t in timings if not t[3]]):.4f}")
print("timing_zero", [t for t in timings if t[1] == 0])
print("timing_0_1", [t for t in timings if 0 < t[1] < 1])
print("timing_eq1", [t[0] for t in timings if t[1] == 1.0])
print("timing_gt1", [t for t in timings if t[1] > 1])

for r in rows:
    print(json.dumps(r, ensure_ascii=False))
