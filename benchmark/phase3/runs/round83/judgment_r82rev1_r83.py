#!/usr/bin/env python3
"""R83 R82-REV1 judgment recount: parse DIAG-H27 section 1 table independently,
recompute five main-code counts, compare with section 2 aggregates, evaluate
written lines from holdout27 seal log section 7 / METHOD-INTEGRATION-r82."""
import json, math, re
from pathlib import Path

DIAG = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round83/acceptance/DIAG-H27.md")
SCORES = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round83/acceptance/judging/final-scores-h27.json")

text = DIAG.read_text(encoding="utf-8")
# Extract section 1 table rows: | CASE | ... | main code | ...
rows = []
in_s1 = False
for line in text.splitlines():
    if line.startswith("## 1."):
        in_s1 = True
        continue
    if in_s1 and line.startswith("## 2."):
        break
    if not in_s1:
        continue
    m = re.match(r"\|\s*([A-Z]+-\d+)\s*\|[^|]*\|\s*([^|]+?)\s*\|", line)
    if m:
        rows.append((m.group(1), m.group(2).strip()))

print(f"rows parsed: {len(rows)}")
assert len(rows) == 27, len(rows)

def classify(main):
    if main.startswith("E5-CLAIM"):
        return "CLAIM"
    if main.startswith("E5-DIR"):
        return "DIR"
    if main.startswith("E5-TIM"):
        return "TIM_SUB"  # section1 TIM main codes here are all substantive per DIAG s2
    if main.startswith("E5-OMIT"):
        return "OMIT"
    if main == "E4" or main.startswith("E4"):
        return "E4"
    return main

from collections import Counter
counts = Counter(classify(main) for _, main in rows)
for k in ["CLAIM", "DIR", "TIM_SUB", "OMIT", "E4"]:
    print(f"{k}: {counts.get(k,0)}")
print("detail:", dict(counts))

# Section 2 aggregates as stated in DIAG (transcribed from task + DIAG s2)
agg = {"CLAIM": 13, "DIR": 7, "TIM_SUB": 2, "OMIT": 3, "E4": 2}
for k, v in agg.items():
    status = "MATCH" if counts.get(k, 0) == v else "MISMATCH"
    print(f"check {k}: recount={counts.get(k,0)} vs s2={v} -> {status}")
    assert counts.get(k, 0) == v

N = 27
rates = {k: counts.get(k, 0) / N for k in agg}
for k, r in rates.items():
    print(f"rate {k}: {counts.get(k,0)}/{N} = {r:.4f}")

scores = json.loads(SCORES.read_text(encoding="utf-8"))
pair_diff = scores["main_caliber_low27"]["pair_diff"]
se = scores["main_caliber_low27"]["SE"]
print(f"pair_diff: {pair_diff} SE: {se}")
print(f"segments: DS={scores['segments']['bazi_DS']['pair_diff']} QM={scores['segments']['qimen_QM']['pair_diff']}")
print(f"qimen direction<1.75: {scores['qimen_direction_attached_read']['count_direction_mean_below_1p75']}/{scores['qimen_direction_attached_read']['n_qimen']}")

# Written lines (N=27): count limits floor for <= lines, ceil for falsification
lines = {
    "CLAIM_main_le": (0.167, math.floor(0.167 * N)),
    "TIM_sub_le": (0.080, math.floor(0.080 * N)),
    "DIR_le": (0.385, math.floor(0.385 * N)),
    "OMIT_le": (0.160, math.floor(0.160 * N)),
    "E4_le": (0.160, math.floor(0.160 * N)),
    "CLAIM_fals_ge": (0.444, math.ceil(0.444 * N)),
}
for k, (rate, cnt) in lines.items():
    print(f"line {k}: rate={rate} count={cnt} (raw={rate*N})")
print("line pair guard >= -1.837 ; falsification <= -2.834")

# Verdicts
print("J1 CLAIM main:", counts["CLAIM"], "<=4?", counts["CLAIM"] <= 4)
print("J2 TIM sub:", counts["TIM_SUB"], "<=2?", counts["TIM_SUB"] <= 2, "(exact-line)" if counts["TIM_SUB"] == 2 else "")
print("J3 DIR guard:", counts["DIR"], "<=10?", counts["DIR"] <= 10)
print("J4 OMIT guard:", counts["OMIT"], "<=4?", counts["OMIT"] <= 4)
print("J5 E4 guard:", counts["E4"], "<=4?", counts["E4"] <= 4)
print("J6 pair guard:", pair_diff, ">=-1.837?", pair_diff >= -1.837)
print("J7 CLAIM fals:", counts["CLAIM"], ">=12?", counts["CLAIM"] >= 12)
print("J8 pair fals:", pair_diff, "<=-2.834?", pair_diff <= -2.834)
falsified = (counts["CLAIM"] >= 12) or (pair_diff <= -2.834)
print("THREE-STATE:", "FALSIFIED" if falsified else "check other branches")
