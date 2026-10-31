#!/usr/bin/env python3
"""R82 R81-REV1 disposal verification (execution seat self-check).
Compares live method/ against kb-snapshot-holdout27/ (snapshot file set only).
Asserts: diff set == {references/calibration.md}; SKILL.md identical;
removing the inserted Sec.9 disposal paragraph restores snapshot calibration
byte-for-byte; Sec.8 and Sec.10 identical; liuren chapter identical.
"""
import hashlib
from pathlib import Path

BASE = Path("/home/hatch/workspace/divination")
LIVE = BASE / "benchmark/phase3/method"
SNAP = BASE / "benchmark/phase3/runs/round82/kb-snapshot-holdout27"

def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

snap_files = sorted(p.relative_to(SNAP) for p in SNAP.rglob("*") if p.is_file())
diffs, missing = [], []
for rel in snap_files:
    lp = LIVE / rel
    if not lp.is_file():
        missing.append(str(rel))
    elif sha(lp) != sha(SNAP / rel):
        diffs.append(str(rel))
print(f"snapshot file set: {len(snap_files)} files")
print(f"missing in live: {missing}")
print(f" differing files: {diffs}")
assert not missing, missing
assert diffs == ["references/calibration.md"], diffs

# SKILL identical incl. (q) line verbatim
live_skill = (LIVE / "SKILL.md").read_text(encoding="utf-8")
snap_skill = (SNAP / "SKILL.md").read_text(encoding="utf-8")
assert live_skill == snap_skill
q_live = [l for l in live_skill.splitlines() if l.startswith("- (q)")]
q_snap = [l for l in snap_skill.splitlines() if l.startswith("- (q)")]
assert q_live == q_snap and len(q_live) == 1
print("(q) line verbatim (live == snapshot):", q_live[0])

# calibration: remove inserted paragraph -> byte-for-byte snapshot
live_cal_b = (LIVE / "references/calibration.md").read_bytes()
snap_cal_b = (SNAP / "references/calibration.md").read_bytes()
live_cal = live_cal_b.decode("utf-8")
snap_cal = snap_cal_b.decode("utf-8")
marker = "**失效登记（R82 判读，runs/round82/acceptance/JUDGMENT-R81-REV1-r82.md §2）**"
assert live_cal.count(marker) == 1 and marker not in snap_cal
start = live_cal.index("\n\n" + marker)
end = live_cal.index("\n\n## 十、", start)
inserted = live_cal[start + 2:end]
restored = live_cal[:start] + live_cal[end:]
assert restored == snap_cal, "removal does not restore snapshot"
print("inserted paragraph restores snapshot byte-for-byte when removed: OK")
print("inserted paragraph:")
print(inserted)

def section(text: str, head: str, nxt: str | None) -> str:
    s = text.index(head)
    e = text.index(nxt) if nxt else len(text)
    return text[s:e]

sec8_l = section(live_cal, "## 八、", "## 九、")
sec8_s = section(snap_cal, "## 八、", "## 九、")
sec10_l = section(live_cal, "## 十、", None)
sec10_s = section(snap_cal, "## 十、", None)
assert sec8_l == sec8_s, "section 8 differs"
assert sec10_l == sec10_s, "section 10 differs"
print("section 8 (R80-REV1, in force) verbatim identical: OK")
print("section 10 (R82-REV1, pending) verbatim identical: OK")

sec9_l = section(live_cal, "## 九、", "## 十、")
sec9_s = section(snap_cal, "## 九、", "## 十、")
assert sec9_l == sec9_s + inserted + "\n\n" or sec9_l.replace(inserted, "").replace("\n\n\n", "\n\n") == sec9_s
print("section 9: live == snapshot + inserted paragraph only: OK")

# liuren frozen chapter
assert sha(LIVE / "references/chinese-liuren.md") == sha(SNAP / "references/chinese-liuren.md")
print("chinese-liuren.md identical:", sha(LIVE / "references/chinese-liuren.md"))

for name, p in [("calibration.md", LIVE / "references/calibration.md"), ("SKILL.md", LIVE / "SKILL.md")]:
    print(f"POST {name}: sha256={sha(p)} bytes={p.stat().st_size}")
for name, p in [("calibration.md", SNAP / "references/calibration.md"), ("SKILL.md", SNAP / "SKILL.md")]:
    print(f"SNAP {name}: sha256={sha(p)} bytes={p.stat().st_size}")
print("ALL DISPOSAL CHECKS PASSED")
