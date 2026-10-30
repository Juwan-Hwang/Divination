#!/usr/bin/env python3
"""DIAG-LR-weight (R37) aggregation: recode h14 Liuren losses (16) under the
candidate 'weight adjudication' (W) dimension, contrasted with the
DIAG-LR-fresh2 eight-class primary codes (A-H).

Codes (fresh2): A=取用误判 B=类神多义未并读 C=缺传误判 D=应期层误
E=断语具体度不足 F=方向反断 G=输入成色所致 H=其他
New code: W=权重裁决 (see DIAG-LR-weight.md for the operational definition;
priority: H不可归因 -> C -> B未并读 -> A取用选择 -> W权重 -> D/E残余).

Recoding was done by the diagnosis role from opened materials only:
holdout14-acceptance predictions (basis+prediction_text), judging
packet-ours outcome_record, final-scores, host-mapping, REPORT.md.
This script only aggregates the coded table and verifies the 16 ids and
their diffs against final-scores.json. No gold files are read.
"""
import json, pathlib, collections

BASE = pathlib.Path.home() / "workspace/divination/benchmark/phase3/runs"
H14 = BASE / "holdout14-acceptance"

# id: (fresh2_primary, new_primary, w_boundary_ambiguous: bool)
RECODE = {
    "DA-015": ("B", "W", False),
    "DA-016": ("B", "W", True),   # W vs 量级校准(E/子型三) interface
    "DA-017": ("D", "W", True),   # W vs 应期层误(D) interface
    "DA-019": ("A", "W", False),
    "DA-020": ("A", "A", False),  # candidate set incomplete -> stays A
    "DA-021": ("E", "E", False),  # final sign aligned -> excluded by rule T4b
    "DA-022": ("B", "W", False),
    "DA-023": ("E", "E", False),  # final sign aligned -> excluded by rule T4b
    "BY-007": ("A", "W", False),
    "BY-008": ("D", "D", False),
    "BY-009": ("A", "W", True),   # W vs 子型三(迟/不成尺度) interface
    "BY-010": ("A", "A", False),  # 次第展开量级 -> 子型三残余, not W
    "BY-011": ("A", "A", True),   # W-candidate vs 天时取象(A); stays A, W secondary-candidate only
    "CY-005": ("D", "D", False),  # 干支级: W untestable (no faces enumerated)
    "CY-006": ("D", "D", False),
    "CY-008": ("H", "H", False),
}

def src(cid):
    return cid.split("-")[0]

final = json.loads((H14 / "judging/final-scores.json").read_text(encoding="utf-8"))
per = final["per_case"]
assert set(RECODE) == {c for c in per if src(c) in ("DA", "BY", "CY")}, "id set mismatch"
assert all(per[c]["diff"] < 0 for c in RECODE), "all 16 must be losses"

n = len(RECODE)
newc = collections.Counter(v[1] for v in RECODE.values())
oldc = collections.Counter(v[0] for v in RECODE.values())
print(f"h14 Liuren losses n={n}")
print("fresh2 primary:", dict(oldc))
print("new primary:  ", dict(newc))
w = newc["W"]
print(f"W primary: {w}/{n} = {w/n:.1%}")
for s in ("DA", "BY", "CY"):
    sub = {c: v for c, v in RECODE.items() if src(c) == s}
    ws = sum(1 for v in sub.values() if v[1] == "W")
    print(f"  {s}: W {ws}/{len(sub)} = {ws/len(sub):.1%}")
amb = [c for c, v in RECODE.items() if v[2]]
amb_w = [c for c in amb if RECODE[c][1] == "W"]
print(f"boundary-ambiguous: {len(amb)}/{n} = {len(amb)/n:.1%} (of which coded W: {len(amb_w)})")
print(f"W conservative (ambiguous W excluded): {w-len(amb_w)}/{n} = {(w-len(amb_w))/n:.1%}")
print("\ntransition (fresh2 -> new):")
tr = collections.Counter((v[0], v[1]) for v in RECODE.values())
for (o, nw), k in sorted(tr.items()):
    print(f"  {o} -> {nw}: {k}")
fam_old = sum(1 for v in RECODE.values() if v[0] in "ABC")
fam_new = sum(1 for v in RECODE.values() if v[1] in "ABC")
print(f"\n取用族 (A+B+C) primary: fresh2 {fam_old}/{n} = {fam_old/n:.1%} -> new {fam_new}/{n} = {fam_new/n:.1%}")
w_from_fam = sum(1 for v in RECODE.values() if v[1] == "W" and v[0] in "ABC")
print(f"W sourced from fresh2 取用族: {w_from_fam}/{fam_old} of that family; W sourced from D: {w - w_from_fam}")
