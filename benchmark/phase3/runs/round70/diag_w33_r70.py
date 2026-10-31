#!/usr/bin/env python3
"""R70 W-monitoring round 33: recompute liuren negative subset stats and
per-case provenance.book family classification from on-disk artifacts only.
Reads: round70 final-scores.json (two designated family entries only),
round70 lr-negatives-dev70.json, inputs-dev12/<case_id>.json provenance.book.
Writes nothing except stdout summary."""
import json
import os
import statistics

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
NEG = os.path.join(BASE, "runs/round70/diagnosis/lr-negatives-dev70.json")
FS = os.path.join(BASE, "runs/round70/final-scores.json")
INPUTS = os.path.join(BASE, "inputs-dev12")
GUIDE_KEY = "大六壬占验指南"

neg = json.load(open(NEG, encoding="utf-8"))
fs = json.load(open(FS, encoding="utf-8"))
fam = fs["analysis_r70"]["families"]
print("analysis_r70.round =", fs["analysis_r70"]["round"])
for key in ("liuren_dev8", "liuren_merged"):
    e = fam[key]
    print(f"{key}: n={e['n']} pair_diff={e['pair_diff']} SE={e['SE']} "
          f"ours_mean={e['ours_mean']} master_mean={e['master_mean']} W/T/L={e['W/T/L']}")

negs = neg["negatives"]
print(f"negatives file: round={neg['round']} n_liuren_total={neg['n_liuren_total']} "
      f"n_negative={neg['n_negative']} listed={len(negs)}")

rows = []
for item in negs:
    cid = item["case_id"]
    card_path = os.path.join(INPUTS, cid + ".json")
    book = None
    if os.path.exists(card_path):
        card = json.load(open(card_path, encoding="utf-8"))
        book = (card.get("provenance") or {}).get("book")
    if book is None:
        fam_name = "待核"
    elif GUIDE_KEY in str(book):
        fam_name = "指南族"
    else:
        fam_name = "非指南族"
    rows.append({**item, "book": book, "family": fam_name})

def mean(xs):
    return round(statistics.fmean(xs), 3) if xs else None

all_d = [r["pair_diff"] for r in rows]
dev8 = [r for r in rows if r["in_dev8"]]
non8 = [r for r in rows if not r["in_dev8"]]
print(f"neg subset mean all: {mean(all_d)} (n={len(all_d)})")
print(f"neg subset mean dev8: {mean([r['pair_diff'] for r in dev8])} (n={len(dev8)})")
print(f"neg subset mean non-dev8: {mean([r['pair_diff'] for r in non8])} (n={len(non8)})")
print(f"negative share: {len(rows)}/{neg['n_liuren_total']} = {len(rows)/neg['n_liuren_total']:.1%}")

for scope, subset in (("all-neg", rows), ("dev8-neg", dev8), ("nondev8-neg", non8)):
    counts = {"指南族": 0, "非指南族": 0, "待核": 0}
    for r in subset:
        counts[r["family"]] += 1
    print(f"{scope}: n={len(subset)} guide={counts['指南族']} "
          f"non-guide={counts['非指南族']} pending={counts['待核']}")

print("--- per-case rows ---")
for r in rows:
    print(json.dumps(r, ensure_ascii=False))
