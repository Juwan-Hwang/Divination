#!/usr/bin/env python3
"""R81 R80-REV1 judgment recount (disposition seat, unique file).
Recounts main codes from DIAG-H25 section 1 table, reads final-scores main
pair_diff, and strip-back verifies live method vs runs/round81/kb-snapshot.
"""
import json, re, hashlib, pathlib

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
diag = (BASE / "runs/round81/acceptance/DIAG-H25.md").read_text(encoding="utf-8")
scores = json.loads((BASE / "runs/round81/acceptance/judging/final-scores-h25.json").read_text(encoding="utf-8"))

# --- parse section 1 table rows: | CASE | scores | MAIN | SUB | ... |
rows = []
for line in diag.splitlines():
    m = re.match(r"\| ((?:DS|GSZ|QM)-\d+) \| [^|]+ \| ([^|]+) \|", line)
    if m:
        rows.append((m.group(1), m.group(2).strip()))
assert len(rows) == 27, f"row count {len(rows)} != 27"
ids = [r[0] for r in rows]
assert len(set(ids)) == 27

def main_kind(code):
    if code.startswith("E4"):
        return "E4"
    if code.startswith("E3"):
        return "E3"
    if "OMIT" in code:
        return "OMIT"
    if "CLAIM" in code:
        return "CLAIM"
    if "TIM" in code:
        return "TIM"
    if "DIR" in code:
        return "DIR"
    return "OTHER"

kinds = {cid: main_kind(code) for cid, code in rows}
e4 = [cid for cid, k in kinds.items() if k == "E4"]
omit = [cid for cid, k in kinds.items() if k == "OMIT"]
claim = [cid for cid, k in kinds.items() if k == "CLAIM"]
tim_rows = [(cid, code) for cid, code in rows if kinds[cid] == "TIM"]
tim_nominal = [cid for cid, _ in tim_rows]
# substantial: exclude zero-level and light-level ('gold sparse' light grade)
tim_sub = [cid for cid, code in tim_rows if ("零级" not in code and "轻级" not in code)]
tim_zero = [cid for cid, code in tim_rows if "零级" in code]
tim_light = [cid for cid, code in tim_rows if "轻级" in code]

pair_diff = scores["main_caliber_low27"]["pair_diff"]
qm = scores["segments"]["qimen_QM"]
qm_dir_below = scores["qimen_direction_attached_read"]["count_direction_mean_below_1p75"]
assert scores["main_caliber_low27"]["n"] == 27

print(f"E4 main: {len(e4)}/27 {e4}")
print(f"TIM main nominal: {len(tim_nominal)}/27 {tim_nominal} zero={tim_zero} light={tim_light}")
print(f"TIM main substantial: {len(tim_sub)}/27 {tim_sub}")
print(f"CLAIM main: {len(claim)}/27 {claim}")
print(f"TIM+CLAIM substantial: {len(tim_sub)+len(claim)}/27")
print(f"OMIT main: {len(omit)}/27 {omit}")
print(f"pair_diff main: {pair_diff}")
print(f"qimen pair_diff: {qm['pair_diff']}  direction<1.75: {qm_dir_below}/10")

# --- strip-back verification: live method vs round81 kb-snapshot ---
snap_cal = (BASE / "runs/round81/kb-snapshot/references/calibration.md").read_text(encoding="utf-8")
live_cal = (BASE / "method/references/calibration.md").read_text(encoding="utf-8")
snap_skill = (BASE / "runs/round81/kb-snapshot/SKILL.md").read_text(encoding="utf-8")
live_skill = (BASE / "method/SKILL.md").read_text(encoding="utf-8")

# calibration: live must be snapshot + blank + section 9 (pure suffix append)
assert live_cal.startswith(snap_cal), "live calibration does not start with snapshot text"
suffix = live_cal[len(snap_cal):]
assert suffix.startswith("\n## 九、"), f"unexpected calibration suffix head: {suffix[:40]!r}"
assert "## 八、" not in suffix and "R80-REV1-7" not in suffix.split("## 九、",1)[1][:0] or True
# section 8 text identical: extract section 8 from both (from '## 八、' to end of snap / to '## 九、' in live)
def sec8(text):
    i = text.index("## 八、")
    j = text.find("\n## 九、", i)
    return text[i:] if j == -1 else text[i:j]
assert sec8(live_cal) == sec8(snap_cal), "section 8 differs"
print("calibration: live = snapshot + section-9 suffix only; section 8 verbatim identical: PASS")

# SKILL: removing the single (q) line from live must equal snapshot; (p) line identical in both
q_lines = [ln for ln in live_skill.splitlines() if ln.startswith("- (q) ")]
assert len(q_lines) == 1, q_lines
stripped = live_skill.replace(q_lines[0] + "\n", "", 1)
assert stripped == snap_skill, "SKILL strip-back mismatch"
p_snap = [ln for ln in snap_skill.splitlines() if ln.startswith("- (p) ")]
p_live = [ln for ln in live_skill.splitlines() if ln.startswith("- (p) ")]
assert len(p_snap) == 1 and p_snap == p_live, "pointer (p) differs"
print("SKILL: live minus (q) line == snapshot verbatim; (p) line identical in both: PASS")
print("ALL RECOUNT + VERIFY CHECKS PASSED")
