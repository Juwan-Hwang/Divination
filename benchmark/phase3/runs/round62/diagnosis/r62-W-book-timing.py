#!/usr/bin/env python3
"""R62 W monitoring: extract liuren dev readings, book provenance, timing subscores.
Only reads analysis_r62 section of final-scores.json, plus ours_sub timing
for negative cases listed in lr-negatives-dev62.json (mirrors R61 procedure),
and provenance.book from inputs-dev12 for those cases only.
Does not open any judging/ directory or gold files.
"""
import json, pathlib

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
neg_path = BASE / "runs/round62/diagnosis/lr-negatives-dev62.json"
fs_path = BASE / "runs/round62/final-scores.json"
inputs_dir = BASE / "inputs-dev12"

neg = json.loads(neg_path.read_text())
fs = json.loads(fs_path.read_text())
ana = fs.get("analysis_r62")
print("== analysis_r62 families liuren ==")
for k in ("liuren_dev8","liuren_lr3_new","liuren_merged"):
    print(k, json.dumps(ana["families"][k], ensure_ascii=False))
print("== platform ==")
print(json.dumps(ana["platform"], ensure_ascii=False))
print("== guardrails_attribution liuren ==")
print(json.dumps(ana["guardrails_attribution"]["liuren_continued_deterioration"], ensure_ascii=False))

ours_sub = fs.get("ours_sub")
timing = {cid: v["timing"] for cid, v in ours_sub.items() if isinstance(v, dict) and "timing" in v}
neg_ids = [n["case_id"] for n in neg["negatives"]]
dev8_ids = [n["case_id"] for n in neg["negatives"] if n["in_dev8"]]
non_ids = [n["case_id"] for n in neg["negatives"] if not n["in_dev8"]]
def mean(xs): return round(sum(xs)/len(xs), 4) if xs else None
print("== timing for negatives ==")
for cid in neg_ids:
    print(cid, timing.get(cid, "MISSING"))
print("timing mean all neg", mean([timing[c] for c in neg_ids if c in timing]), "n", len(neg_ids))
print("timing mean dev8 neg", mean([timing[c] for c in dev8_ids if c in timing]), "n", len(dev8_ids))
print("timing mean non-dev8 neg", mean([timing[c] for c in non_ids if c in timing]), "n", len(non_ids))
print("timing==0", [(c, timing[c]) for c in neg_ids if timing.get(c)==0])
print("0<timing<1", [(c, timing[c]) for c in neg_ids if c in timing and 0<timing[c]<1])
print("timing==1", [c for c in neg_ids if timing.get(c)==1.0])
print("timing>1", [(c, timing[c]) for c in neg_ids if c in timing and timing[c]>1])
def pd_mean(ids):
    d = {n["case_id"]: n["pair_diff"] for n in neg["negatives"]}
    xs=[d[c] for c in ids]
    return round(sum(xs)/len(xs),4)
print("neg pair_diff mean all", pd_mean(neg_ids))
print("neg pair_diff mean dev8", pd_mean(dev8_ids))
print("neg pair_diff mean non-dev8", pd_mean(non_ids))
print("counts: total", neg["n_liuren_total"], "neg", neg["n_negative"], "dev8 neg", len(dev8_ids), "non", len(non_ids))
print("== provenance.book ==")
for cid in neg_ids:
    p = inputs_dir / f"{cid}.json"
    if not p.exists():
        print(cid, "FILE_MISSING"); continue
    d = json.loads(p.read_text())
    prov = d.get("provenance") or {}
    print(cid, "|", prov.get("book"))
