#!/usr/bin/env python3
"""W monitoring round 71 (W34) recomputation script.
Only reads allowed materials:
 - final-scores.json: analysis_r71.round + families[liuren_dev8, liuren_merged]
 - lr-negatives-dev71.json
 - inputs-dev12/<case_id>.json provenance.book for negative ids
"""
import json, os, statistics

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
FS = f"{BASE}/runs/round71/final-scores.json"
NEG = f"{BASE}/runs/round71/diagnosis/lr-negatives-dev71.json"
PRIORS = [
    f"{BASE}/runs/round38/diagnosis/W-CHARTER.md",
    f"{BASE}/runs/round41/diagnosis/DIAG-LR-fresh-h16.md",
    f"{BASE}/runs/round70/diagnosis/DIAG-LR-weight-dev70.md",
    FS, NEG,
]

print("== prior existence / sizes ==")
for p in PRIORS:
    print(p, os.path.exists(p), os.path.getsize(p) if os.path.exists(p) else None)

with open(FS, encoding="utf-8") as f:
    fs = json.load(f)
a = fs.get("analysis_r71")
print("\n== analysis_r71 keys ==")
print(list(a.keys()) if isinstance(a, dict) else type(a))
print("round:", a.get("round"))
fams = a.get("families", {})
print("families keys:", list(fams.keys()))
for k in ("liuren_dev8", "liuren_merged"):
    print(k, json.dumps(fams.get(k), ensure_ascii=False))

with open(NEG, encoding="utf-8") as f:
    neg = json.load(f)
print("\n== negatives meta ==")
print("round:", neg.get("round"), "n_liuren_total:", neg.get("n_liuren_total"), "n_negative:", neg.get("n_negative"))
negs = neg["negatives"]
print("len negatives:", len(negs))

def mean(xs): return sum(xs)/len(xs) if xs else None
all_d = [x["pair_diff"] for x in negs]
d8 = [x for x in negs if x["in_dev8"]]
nd8 = [x for x in negs if not x["in_dev8"]]
print(f"neg subset mean all n={len(all_d)} mean={mean(all_d):.4f}")
print(f"neg subset mean dev8 n={len(d8)} mean={mean([x['pair_diff'] for x in d8]):.4f}")
print(f"neg subset mean non-dev8 n={len(nd8)} mean={mean([x['pair_diff'] for x in nd8]):.4f}")
print("dev8 breakdown:", sum(1 for x in d8 if x['case_id'].startswith('LR2-')), "LR2 +", sum(1 for x in d8 if x['case_id'].startswith('OC-')), "OC")

print("\n== per-case book ==")
counts = {"guide":0, "non_guide":0, "pending":0}
counts_d8 = {"guide":0, "non_guide":0, "pending":0}
counts_nd8 = {"guide":0, "non_guide":0, "pending":0}
rows = []
for x in negs:
    cid = x["case_id"]
    p = f"{BASE}/inputs-dev12/{cid}.json"
    book = None
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            card = json.load(f)
        prov = card.get("provenance") or {}
        book = prov.get("book")
    if book is None or (isinstance(book, str) and not book.strip()):
        fam = "pending"
    elif "大六壬占验指南" in str(book):
        fam = "guide"
    else:
        fam = "non_guide"
    counts[fam]+=1
    (counts_d8 if x["in_dev8"] else counts_nd8)[fam]+=1
    rows.append((cid, x["tradition"], x["in_dev8"], x["ours"], x["master"], x["pair_diff"], book, fam))
    print(json.dumps({"case_id":cid,"tradition":x["tradition"],"in_dev8":x["in_dev8"],"ours":x["ours"],"master":x["master"],"pair_diff":x["pair_diff"],"book":book,"family":fam}, ensure_ascii=False))
print("\ncounts all:", counts)
print("counts dev8:", counts_d8)
print("counts non-dev8:", counts_nd8)
