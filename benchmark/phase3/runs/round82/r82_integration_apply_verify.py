#!/usr/bin/env python3
"""R82-REV1 integration apply + verify (integration seat only).
Extracts section-10 text and SKILL (r) pointer verbatim from the proposal,
appends them to the live method, then verifies against kb-snapshot.
"""
import hashlib, os, sys

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
PROP = os.path.join(BASE, "runs/round82/revision/PROPOSAL-R82-REV1.md")
CAL = os.path.join(BASE, "method/references/calibration.md")
SKILL = os.path.join(BASE, "method/SKILL.md")
SNAP = os.path.join(BASE, "runs/round82/kb-snapshot")

def sha(b): return hashlib.sha256(b).hexdigest()

prop = open(PROP, encoding="utf-8").read()

# --- extract section 10 verbatim: from heading to the R82-REV1-7 paragraph end,
# bounded by the following "\n\n---\n" separator in the proposal.
start = prop.index("## 十、具体断项反向限定扫查与主张范围收束核")
end_marker = "\n\n---\n"
end = prop.index(end_marker, start)
section = prop[start:end]
assert section.startswith("## 十、具体断项反向限定扫查与主张范围收束核（R82 干预 R82-REV1，跨体系断项范围机制）")
assert "（集成登记：提案 runs/round82/revision/PROPOSAL-R82-REV1.md" in section
assert "**R82-REV1-7（留痕与缺痕处置）**" in section
assert section.rstrip().endswith("不改五段格式。")
section = section.rstrip("\n")
print(f"section chars={len(section)} lines={section.count(chr(10))+1}")

# --- extract SKILL (r) pointer line verbatim
pline = None
for line in prop.splitlines():
    if line.startswith("- (r) 断项范围限定："):
        pline = line
        break
assert pline is not None and "第十节，R82-REV1，自集成之次轮起算效力" in pline
print(f"pointer: {pline}")

cal_old = open(CAL, "rb").read()
skill_old = open(SKILL, "rb").read()
print(f"PRE  calibration sha={sha(cal_old)} bytes={len(cal_old)}")
print(f"PRE  SKILL       sha={sha(skill_old)} bytes={len(skill_old)}")

# --- apply (guarded against double-apply)
cal_old_t = cal_old.decode("utf-8")
if "## 十、具体断项反向限定扫查与主张范围收束核" not in cal_old_t:
    assert cal_old_t.endswith("\n") and not cal_old_t.endswith("\n\n")
    cal_new_t = cal_old_t + "\n" + section + "\n"
    open(CAL, "w", encoding="utf-8").write(cal_new_t)
    print("calibration: appended section 10")
else:
    print("calibration: already integrated, skip")

skill_old_t = skill_old.decode("utf-8")
if pline not in skill_old_t:
    qline_start = skill_old_t.index("- (q) ")
    qline_end = skill_old_t.index("\n", qline_start) + 1
    skill_new_t = skill_old_t[:qline_end] + pline + "\n" + skill_old_t[qline_end:]
    open(SKILL, "w", encoding="utf-8").write(skill_new_t)
    print("SKILL: inserted (r) after (q)")
else:
    print("SKILL: already integrated, skip")

# --- verify
cal_new = open(CAL, "rb").read()
skill_new = open(SKILL, "rb").read()
print(f"POST calibration sha={sha(cal_new)} bytes={len(cal_new)}")
print(f"POST SKILL       sha={sha(skill_new)} bytes={len(skill_new)}")

# snapshot file-set comparison (21 files)
snap_files = []
for root, _dirs, files in os.walk(SNAP):
    for f in files:
        snap_files.append(os.path.relpath(os.path.join(root, f), SNAP))
snap_files.sort()
diff_files, same_files = [], []
for rel in snap_files:
    live = open(os.path.join(BASE, "method", rel), "rb").read()
    snap = open(os.path.join(SNAP, rel), "rb").read()
    (diff_files if sha(live) != sha(snap) else same_files).append(rel)
print(f"snapshot files={len(snap_files)} differ={diff_files} same={len(same_files)}")
assert diff_files == ["SKILL.md", "references/calibration.md"], diff_files

# strip-back: removing appended section / (r) line must reproduce snapshot bytes exactly
snap_cal = open(os.path.join(SNAP, "references/calibration.md"), "rb").read().decode("utf-8")
snap_skill = open(os.path.join(SNAP, "SKILL.md"), "rb").read().decode("utf-8")
cal_stripped = cal_new.decode("utf-8").replace("\n" + section + "\n", "", 1)
assert cal_stripped == snap_cal, "calibration strip-back mismatch"
skill_stripped = skill_new.decode("utf-8").replace(pline + "\n", "", 1)
assert skill_stripped == snap_skill, "SKILL strip-back mismatch"
print("strip-back calibration: EXACT MATCH with snapshot")
print("strip-back SKILL: EXACT MATCH with snapshot")

# section in live file must equal proposal-extracted section verbatim
live_cal_t = cal_new.decode("utf-8")
assert live_cal_t.endswith(section + "\n")
# (r) must sit immediately after (q)
lines = skill_new.decode("utf-8").splitlines()
qi = next(i for i, l in enumerate(lines) if l.startswith("- (q) "))
assert lines[qi + 1] == pline
print("(r) immediately after (q): OK")

liuren_live = sha(open(os.path.join(BASE, "method/references/chinese-liuren.md"), "rb").read())
liuren_snap = sha(open(os.path.join(SNAP, "references/chinese-liuren.md"), "rb").read())
assert liuren_live == liuren_snap
print(f"liuren unchanged sha={liuren_live}")
print("ALL CHECKS PASSED")
