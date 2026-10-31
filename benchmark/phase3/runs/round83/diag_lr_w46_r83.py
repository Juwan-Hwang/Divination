#!/usr/bin/env python3
"""W46 R83 LR weight monitoring: aggregate recomputation only.
Reads: lr-negatives-dev83.json, final-scores.json, inputs-dev12/<id>.json (provenance only).
Writes: stdout summary."""
import json, math, collections, pathlib

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
NEG = BASE / "runs/round83/diagnosis/lr-negatives-dev83.json"
FS = BASE / "runs/round83/final-scores.json"
INP = BASE / "inputs-dev12"

neg_doc = json.loads(NEG.read_text(encoding="utf-8"))
fs = json.loads(FS.read_text(encoding="utf-8"))
negs = neg_doc["negatives"]
print("neg_doc round", neg_doc.get("round"), "n_total", neg_doc.get("n_liuren_total"), "n_neg", neg_doc.get("n_negative"), "list_len", len(negs))

print("final-scores top-level keys:", sorted(fs.keys()))
for k, v in fs.items():
    if isinstance(v, dict) and k not in ("ours_axis2", "ours_sub"):
        print("SECTION", k, json.dumps(v, ensure_ascii=False)[:3000])

# consistency
bad = []
for n in negs:
    if abs((n["ours"] - n["master"]) - n["pair_diff"]) > 1e-9:
        bad.append((n["case_id"], "pairdiff"))
    a2 = fs.get("ours_axis2", {}).get(n["case_id"])
    if a2 is None or abs(a2 - n["ours"]) > 1e-9:
        bad.append((n["case_id"], "axis2", a2))
    sub = fs.get("ours_sub", {}).get(n["case_id"], {}).get("total")
    if sub is None or abs(sub - n["ours"]) > 1e-9:
        bad.append((n["case_id"], "sub", sub))
print("consistency bad:", bad)

def seg_of(n):
    return "dev8" if n["in_dev8"] else "LR3"

for seg in ("dev8", "LR3", "ALL"):
    rows = [n for n in negs if seg == "ALL" or seg_of(n) == seg]
    s = sum(n["pair_diff"] for n in rows)
    vals = sorted(n["pair_diff"] for n in rows)
    med = vals[len(vals)//2] if len(vals) % 2 == 1 else (vals[len(vals)//2 - 1] + vals[len(vals)//2]) / 2
    print(f"SEG {seg} n={len(rows)} sum={s:.2f} mean={s/len(rows):.3f} median={med:.2f} ids={[n['case_id'] for n in rows]}")

CODING = {
 "LR2-013": ("D", ""), "LR2-014": ("W*", "W-face, interface; W<->C interface"),
 "LR2-015": ("E", "same-sign exclusion; W note only"), "LR2-016": ("D", "W<->magnitude interface note only"),
 "LR2-017": ("E", ""), "LR2-018": ("D", ""), "LR2-019": ("E", ""),
 "LR2-021": ("A*", "MW/SEAT; A<->B interface"), "LR2-022": ("W*", "W-face, interface; W<->A interface"),
 "LR2-023": ("W*", "W-face, interface; W<->D/E interface"), "LR2-024": ("C*", ""),
 "LR3-002": ("E", "A secondary candidate GZ/SEAT"), "LR3-006": ("C*", ""),
 "LR3-008": ("D", ""), "LR3-101": ("W*", "W-face, interface; W<->A/C interface"),
 "LR3-104": ("E", "same-sign exclusion note (per h16 s2.1)"), "LR3-107": ("A", "SF/SEAT"),
 "LR3-110": ("E", ""), "LR3-112": ("H", "W not measurable"), "LR3-114": ("C*", ""),
 "LR3-116": ("A", "QX/SEAT"), "OC-026": ("E", "same-sign exclusion note"),
 "OC-027": ("W*", "W-name, interface; W<->C interface"), "OC-029": ("E", "A secondary candidate MW/MIX"),
 "OC-030": ("A", "SF/SEAT"),
}
HARDCORE = set()  # no hardcore W among this round's negatives per h16 s2.1 (LR3-004 not in list)

for seg in ("dev8", "LR3", "ALL"):
    rows = [n for n in negs if seg == "ALL" or seg_of(n) == seg]
    cnt = collections.Counter(CODING[n["case_id"]][0].rstrip("*") for n in rows)
    w_int = sum(1 for n in rows if CODING[n["case_id"]][0].rstrip("*") == "W")
    w_hard = sum(1 for n in rows if n["case_id"] in HARDCORE)
    n_ = len(rows)
    def pct(c):
        p = c / n_
        se = math.sqrt(p * (1 - p) / n_) * 100 if n_ else 0.0
        return f"{c}={p*100:.1f}% (SE {se:.1f}pp)"
    print(f"CODING {seg} n={n_} dist={dict(sorted(cnt.items()))} W_interface {pct(w_int)} W_hardcore {pct(w_hard)}")

# timing three quantities from coding (D main only codable on dev side per h16 s2.2)
for seg in ("dev8", "LR3", "ALL"):
    rows = [n for n in negs if seg == "ALL" or seg_of(n) == seg]
    d_main = sum(1 for n in rows if CODING[n["case_id"]][0].rstrip("*") == "D")
    print(f"TIMING {seg} D_main={d_main} ids={[n['case_id'] for n in rows if CODING[n['case_id']][0].rstrip('*')=='D']}")

# provenance per case, exact open by id
fam = collections.Counter(); fam_seg = collections.defaultdict(collections.Counter)
for n in negs:
    cid = n["case_id"]
    card = json.loads((INP / f"{cid}.json").read_text(encoding="utf-8"))
    prov = card.get("provenance") or {}
    book = prov.get("book")
    print(f"PROV {cid} | {seg_of(n)} | {book!r} | prov_keys={sorted(prov.keys())}")
    if book is None:
        f = "pending"
    elif "大六壬占验指南" in str(book):
        f = "guide"
    else:
        f = "non-guide"
    fam[f] += 1; fam_seg[seg_of(n)][f] += 1
print("FAM ALL", dict(fam))
for s, c in fam_seg.items():
    print("FAM", s, dict(c))
missing = [n["case_id"] for n in negs if n["case_id"] not in CODING]
print("coding missing:", missing)
