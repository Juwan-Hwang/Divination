#!/usr/bin/env python3
# W42 R79 diagnostic seat script: verification + aggregation only.
import json, math, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
R79 = os.path.join(BASE, "runs/round79")

neg = json.load(open(os.path.join(R79, "diagnosis/lr-negatives-dev79.json")))
fs = json.load(open(os.path.join(R79, "final-scores.json")))
print("final-scores top keys:", list(fs.keys()))
for k in fs.keys():
    if k.startswith("analysis"):
        print(k, json.dumps(fs[k], ensure_ascii=False)[:3000])

mb9 = json.load(open(os.path.join(BASE, "data/master-baseline-dev9.json")))
mb8 = json.load(open(os.path.join(BASE, "data/master-baseline-dev8.json")))

def mb_total(mb, cid):
    v = mb.get(cid)
    if isinstance(v, dict):
        return v.get("total")
    return v

negs = neg["negatives"]
assert neg["n_negative"] == len(negs) == 24, len(negs)
assert neg["n_liuren_total"] == 30

# main labels transcribed from DIAG-LR-fresh-h16 s2.1 (dev40 codings), cross-checked vs round78 s2
LABELS = {
 "LR2-013": ("D", ""), "LR2-014": ("W*", "W-face, interface; W<->C interface"),
 "LR2-015": ("E", "same-sign exclusion; W note only"),
 "LR2-016": ("D", "W<->magnitude interface note only"),
 "LR2-017": ("E", ""), "LR2-018": ("D", ""),
 "LR2-019": ("E", ""), "LR2-021": ("A*", "MW/SEAT; A<->B interface"),
 "LR2-022": ("W*", "W-face, interface; W<->A interface"),
 "LR2-023": ("W*", "W-face, interface; W<->D/E interface"),
 "LR2-024": ("C*", ""),
 "LR3-002": ("E", "A secondary candidate GZ/SEAT"),
 "LR3-006": ("C*", ""), "LR3-008": ("D", ""),
 "LR3-101": ("W*", "W-face, interface; W<->A/C interface"),
 "LR3-107": ("A", "SF/SEAT"), "LR3-110": ("E", ""),
 "LR3-112": ("H", "W not measurable"), "LR3-114": ("C*", ""),
 "LR3-116": ("A", "QX/SEAT"),
 "OC-026": ("E", "same-sign exclusion note"),
 "OC-027": ("W*", "W-name, interface; W<->C interface"),
 "OC-029": ("E", "A secondary candidate MW/MIX"),
 "OC-030": ("A", "SF/SEAT"),
}
assert set(LABELS) == {n["case_id"] for n in negs}, set(LABELS) ^ {n["case_id"] for n in negs}

rows = []
ok_pd = ok_ours = ok_master = ok_dev8 = 0
for n in negs:
    cid = n["case_id"]
    if abs((n["ours"] - n["master"]) - n["pair_diff"]) < 1e-9: ok_pd += 1
    if fs["ours_axis2"].get(cid) == n["ours"] and fs["ours_sub"][cid]["total"] == n["ours"]: ok_ours += 1
    if mb_total(mb9, cid) == n["master"]: ok_master += 1
    if cid in mb8:
        if mb_total(mb8, cid) == n["master"]: ok_dev8 += 1
    card = json.load(open(os.path.join(BASE, "inputs-dev12", cid + ".json")))
    book = card.get("provenance", {}).get("book")
    seg = "dev8" if n["in_dev8"] else "LR3"
    lab, note = LABELS[cid]
    rows.append(dict(case_id=cid, seg=seg, pair_diff=n["pair_diff"], ours=n["ours"],
                     master=n["master"], label=lab, note=note, book=book,
                     in_dev8_baseline=(cid in mb8)))
print("pair_diff self-consistent:", ok_pd, "/", len(negs))
print("ours vs final-scores both calibers:", ok_ours, "/", len(negs))
print("master vs baseline-dev9:", ok_master, "/", len(negs))
print("in dev8-baseline & equal:", ok_dev8, "; in-dev8-baseline count:", sum(r["in_dev8_baseline"] for r in rows))

def se(p, n): return math.sqrt(p * (1 - p) / n) * 100 if n else None

for seg in ("dev8", "LR3", "ALL"):
    rs = rows if seg == "ALL" else [r for r in rows if r["seg"] == seg]
    n = len(rs)
    s = sum(r["pair_diff"] for r in rs)
    med = sorted(r["pair_diff"] for r in rs)
    median = (med[n//2] if n % 2 else (med[n//2-1] + med[n//2]) / 2)
    from collections import Counter
    dist = Counter(r["label"].rstrip("*") for r in rs)
    w = sum(1 for r in rs if r["label"].startswith("W"))
    print(seg, "neg n=", n, "sum=", round(s, 4), "mean=", round(s/n, 4), "median=", median,
          "dist=", dict(sorted(dist.items())), "W=", w, "W%=", round(w/n*100, 1), "SEpp=", round(se(w/n, n), 1))
    print("  books:", Counter(r["book"] for r in rs))

# LR3-010 status this round
print("LR3-010 ours_axis2:", fs["ours_axis2"].get("LR3-010"), "master dev9:", mb_total(mb9, "LR3-010"),
      "in negatives:", any(n["case_id"] == "LR3-010" for n in negs))
# all-30 liuren totals from final-scores + baseline for segment overall means:
# liuren ids = keys present in both with tradition liuren per negatives def is host-side; use analysis_r79 if present instead.
json.dump(rows, open(os.path.join(R79, "diagnosis/w42_r79_rows.json"), "w"), ensure_ascii=False, indent=1)
print("rows written:", len(rows))
for r in rows: print(r["case_id"], r["seg"], r["pair_diff"], r["label"], "|", r["book"])
