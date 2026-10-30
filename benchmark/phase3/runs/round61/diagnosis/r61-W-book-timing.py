#!/usr/bin/env python3
"""R61 W monitoring: extract liuren dev readings, book provenance, timing subscores.
Only reads analysis_r61 section of final-scores.json, plus ours_sub timing
for negative cases listed in lr-negatives-dev61.json (mirrors R60 procedure),
and provenance.book from inputs-dev12 for those cases only.
Does not open any judging/ directory or gold files.
"""
import json, pathlib, statistics

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
neg_path = BASE / "runs/round61/diagnosis/lr-negatives-dev61.json"
fs_path = BASE / "runs/round61/final-scores.json"
inputs_dir = BASE / "inputs-dev12"

neg = json.loads(neg_path.read_text())
fs = json.loads(fs_path.read_text())

print("== final-scores top-level keys ==")
print(list(fs.keys()))
ana = fs.get("analysis_r61")
print("== analysis_r61 keys ==")
print(list(ana.keys()) if isinstance(ana, dict) else type(ana))
print(json.dumps(ana, ensure_ascii=False, indent=1))

# ours_sub timing for negatives
ours_sub = fs.get("ours_sub")
print("== ours_sub type ==", type(ours_sub))
timing = {}
if isinstance(ours_sub, dict):
    for cid, v in ours_sub.items():
        if isinstance(v, dict) and "timing" in v:
            timing[cid] = v["timing"]
elif isinstance(ours_sub, list):
    for v in ours_sub:
        if isinstance(v, dict) and "timing" in v:
            timing[v.get("case_id") or v.get("id")] = v["timing"]
neg_ids = [n["case_id"] for n in neg["negatives"]]
print("== timing for negatives ==")
for cid in neg_ids:
    print(cid, timing.get(cid, "MISSING"))
vals = [timing[c] for c in neg_ids if c in timing]
dev8_ids = [n["case_id"] for n in neg["negatives"] if n["in_dev8"]]
non_ids = [n["case_id"] for n in neg["negatives"] if not n["in_dev8"]]
def mean(xs): return round(sum(xs)/len(xs), 4) if xs else None
print("timing mean all neg", mean(vals), "n", len(vals))
print("timing mean dev8 neg", mean([timing[c] for c in dev8_ids if c in timing]))
print("timing mean non-dev8 neg", mean([timing[c] for c in non_ids if c in timing]))
print("timing==0", [c for c in neg_ids if timing.get(c)==0])
print("0<timing<1", [(c, timing[c]) for c in neg_ids if c in timing and 0<timing[c]<1])
print("timing==1", [c for c in neg_ids if timing.get(c)==1.0])
print("timing>1", [(c, timing[c]) for c in neg_ids if c in timing and timing[c]>1])

# negative subset pair_diff means from list itself
def pd_mean(ids):
    d = {n["case_id"]: n["pair_diff"] for n in neg["negatives"]}
    xs=[d[c] for c in ids]
    return round(sum(xs)/len(xs),4)
print("neg pair_diff mean all", pd_mean(neg_ids))
print("neg pair_diff mean dev8", pd_mean(dev8_ids))
print("neg pair_diff mean non-dev8", pd_mean(non_ids))
print("counts: total", neg["n_liuren_total"], "neg", neg["n_negative"], "dev8 neg", len(dev8_ids), "non", len(non_ids))

# provenance.book per negative
print("== provenance.book ==")
for cid in neg_ids:
    p = inputs_dir / f"{cid}.json"
    if not p.exists():
        print(cid, "FILE_MISSING")
        continue
    d = json.loads(p.read_text())
    prov = d.get("provenance") or {}
    print(cid, "|", prov.get("book"))
