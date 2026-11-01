#!/usr/bin/env python3
"""W59 (R96) recomputation: self-consistency, inherited-label aggregation,
family double-report, bibliography source check. Assertions only; no edits."""
import json, math, pathlib, statistics

ROOT = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
neg = json.load(open(ROOT / "runs/round96/diagnosis/lr-negatives-dev96.json"))
neg95 = json.load(open(ROOT / "runs/round95/diagnosis/lr-negatives-dev95.json"))
fs = json.load(open(ROOT / "runs/round96/final-scores.json"))

# inherited labels: W55 fresh coding (round92) as carried by W56 (round93) sec.2
# and W58 (round95) sec.2; LR2-020 E and LR2-022 W* per W55/W56; OC-028 no prior
# label anywhere in W55/W56/W58 diagnosis files -> UNC.
LABELS = {
    "LR2-013": "E", "LR2-014": "D", "LR2-015": "W-hard", "LR2-016": "D",
    "LR2-017": "W-hard", "LR2-019": "E", "LR2-020": "E", "LR2-021": "A*",
    "LR2-022": "W*", "LR2-023": "C*", "LR2-024": "C*",
    "LR3-002": "W-hard", "LR3-006": "E", "LR3-008": "UNC",
    "LR3-101": "W*", "LR3-104": "UNC", "LR3-107": "A", "LR3-110": "D",
    "LR3-112": "H", "LR3-114": "UNC", "LR3-116": "A",
    "OC-026": "E", "OC-027": "C*", "OC-028": "UNC", "OC-029": "UNC",
    "OC-030": "A",
}
AMBIG = {"LR2-021", "LR2-022", "LR2-023", "LR2-024", "LR3-101", "OC-027"}

rows = neg["negatives"]
assert neg["n_liuren_total"] == 30 and neg["n_negative"] == 26 and len(rows) == 26
for r in rows:
    assert abs(r["pair_diff"] - (r["ours"] - r["master"])) < 1e-9, r
    assert r["pair_diff"] < 0
    assert r["case_id"] in LABELS, r["case_id"]
assert set(LABELS) == {r["case_id"] for r in rows}

# platform cross-check (analysis_r96 families)
fam = fs["analysis_r96"]["families"]
assert fam["liuren_merged"]["n"] == 30 and fam["liuren_merged"]["L"] == 26
assert fam["liuren_merged"]["pair_diff"] == -1.733
assert fam["liuren_dev8"]["n"] == 18 and fam["liuren_dev8"]["L"] == 16
assert fam["liuren_dev8"]["pair_diff"] == -2.25
assert fam["liuren_lr3_new"]["n"] == 12 and fam["liuren_lr3_new"]["L"] == 10

def se(p, n):
    return round(100 * math.sqrt(p * (1 - p) / n), 1) if n else None

def report(name, subset):
    n = len(subset)
    lab = [r for r in subset if LABELS[r["case_id"]] != "UNC"]
    wi = [r for r in lab if LABELS[r["case_id"]].startswith("W")]
    wh = [r for r in lab if LABELS[r["case_id"]] == "W-hard"]
    s = sum(r["pair_diff"] for r in subset)
    print(f"{name}: n={n} sum={s:.2f} mean={s/n:.3f} median={statistics.median([r['pair_diff'] for r in subset]):.3f} "
          f"labeled={len(lab)} UNC={n-len(lab)}")
    for denom_name, d in (("labeled", len(lab)), ("list", n), ("total30", 30)):
        if d:
            print(f"  W-interface {len(wi)}/{d}={100*len(wi)/d:.1f}% SE {se(len(wi)/d, d)}pp | "
                  f"W-hard {len(wh)}/{d}={100*len(wh)/d:.1f}% SE {se(len(wh)/d, d)}pp")

dev8 = [r for r in rows if r["in_dev8"]]
lr3 = [r for r in rows if not r["in_dev8"]]
report("ALL", rows); report("dev8", dev8); report("LR3", lr3)
assert len(dev8) == 16 and len(lr3) == 10

from collections import Counter
print("label counts (labeled):", Counter(LABELS[r["case_id"]] for r in rows if LABELS[r["case_id"]] != "UNC"))
print("ambiguous in labeled:", sorted(AMBIG & {r["case_id"] for r in rows}),
      f"{len(AMBIG)}/21 = {100*len(AMBIG)/21:.1f}% SE {se(len(AMBIG)/21, 21)}pp")

# membership vs R95
ids96 = {r["case_id"] for r in rows}; ids95 = {r["case_id"] for r in neg95["negatives"]}
print("entered vs R95:", sorted(ids96 - ids95), "| left vs R95:", sorted(ids95 - ids96))
assert ids96 - ids95 == {"LR2-020", "LR2-022", "LR3-112", "OC-028"}
assert ids95 - ids96 == {"LR3-010"}

# bibliography check: every negative's provenance.book
books = {}
for r in rows:
    card = json.load(open(ROOT / f"inputs-dev12/{r['case_id']}.json"))
    books[r["case_id"]] = card["provenance"]["book"]
assert all(b.startswith("《大六壬占验指南》") for b in books.values()), books
menlei = [c for c, b in books.items() if "·" in b]
keci = [c for c, b in books.items() if "·" not in b]
print(f"bibliography: guide-book 26/26; menlei-form {len(menlei)}, keci-form {len(keci)} {sorted(keci)}")
assert len(menlei) == 21 and len(keci) == 5
print("ALL ASSERTIONS PASSED")
