#!/usr/bin/env python3
"""R87-REV1 integration: append calibration section 12 + SKILL pointer (t).
Extracts the transferable text verbatim from PROPOSAL-R87-REV1.md section 3
(subsections 一..六), demoting '### ' headings to bold labels (r83 style).
Asserts pre-hashes, strip-back exactness, and snapshot diff == {calibration, SKILL}.
"""
import hashlib
import pathlib
import sys

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
PROP = BASE / "runs/round87/revision/PROPOSAL-R87-REV1.md"
CAL = BASE / "method/references/calibration.md"
SKILL = BASE / "method/SKILL.md"
SNAP = BASE / "runs/round87/kb-snapshot"
METHOD = BASE / "method"

PRE_CAL_SHA = "4fd06d43aac209c88f8b8a2e06ae6fbb1bc214c01b82e8855edb7147a369b27c"
PRE_SKILL_SHA = "e07df83cdbcc2ae4893defb6fb83e9abe1af3a52e545f93e0de6aae61b2cda04"

POINTER = "- (t) 应期坐标落点对位：凡断语含时间坐标，坐标写定前先列所选路径的候选坐标全集并逐点标触发，所选坐标须有该点触发对位，取近窗首候选须与次近有触发候选比较占优，命造类事件坐标须落在所报行限段内（正本见 references/calibration.md 第十二节，R87-REV1，自集成之次轮起算效力）"

HEADER = """## 十二、应期坐标落点对位核（R87 干预 R87-REV1，跨体系坐标落点机制，现行）

（集成登记：提案 runs/round87/revision/PROPOSAL-R87-REV1.md；自集成之次轮起算效力，照 R59／R61／R78／R80／R81／R82／R83 先例。判读口径全文见本节「五、判读口径」部分，照提案 §3 五写死，本节不另改写。）
"""


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    cal_old = CAL.read_bytes()
    skill_old = SKILL.read_bytes()
    assert sha(cal_old) == PRE_CAL_SHA, f"cal pre-hash mismatch: {sha(cal_old)}"
    assert sha(skill_old) == PRE_SKILL_SHA, f"skill pre-hash mismatch: {sha(skill_old)}"
    print(f"PRE cal {len(cal_old)}B sha={PRE_CAL_SHA}")
    print(f"PRE skill {len(skill_old)}B sha={PRE_SKILL_SHA}")

    prop = PROP.read_text(encoding="utf-8")
    start_marker = "## 3. 条文全文（集成源；入 calibration 第十二节）"
    end_marker = "## 4. 三维可区分论证"
    i = prop.index(start_marker) + len(start_marker)
    j = prop.index(end_marker)
    region = prop[i:j].strip("\n")
    assert region.startswith("### 一、适用面"), region[:40]
    for key in ["R87-REV1-1", "R87-REV1-2", "R87-REV1-3", "R87-REV1-4", "R87-REV1-5",
                "R87-REV1-6", "≤0.120", "≥−2.670", "≤−3.170", "≥0.320", "holdout31"]:
        assert key in region, f"missing key in extracted region: {key}"
    # demote ### headings to bold labels
    lines = []
    for ln in region.splitlines():
        if ln.startswith("### "):
            lines.append(f"**{ln[4:].strip()}**")
        else:
            lines.append(ln)
    body = "\n".join(lines).strip("\n")

    addition = "\n" + HEADER + "\n" + body + "\n"
    cal_new = cal_old + addition.encode("utf-8")
    # strip-back (in memory): removing the exact addition restores pre-state
    assert cal_new[: len(cal_old)] == cal_old
    assert cal_new[len(cal_old):].decode("utf-8") == addition
    stripped = cal_new[: len(cal_old)]
    assert sha(stripped) == PRE_CAL_SHA
    print("cal strip-back: PASS (pure suffix append, prefix == pre-image)")

    skill_text = skill_old.decode("utf-8")
    s_line_start = skill_text.index("- (s) 奇门用神落宫定性复核与应期取径明示")
    s_line_end = skill_text.index("\n", s_line_start) + 1
    insert_at = s_line_end
    skill_new_text = skill_text[:insert_at] + POINTER + "\n" + skill_text[insert_at:]
    skill_new = skill_new_text.encode("utf-8")
    # strip-back: remove the inserted pointer line exactly once
    stripped_skill = skill_new_text.replace(POINTER + "\n", "", 1)
    assert stripped_skill == skill_text and sha(stripped_skill.encode("utf-8")) == PRE_SKILL_SHA
    assert skill_new_text.count(POINTER) == 1
    print("skill strip-back: PASS ((t) removed -> pre-image exact; (t) follows (s))")

    CAL.write_bytes(cal_new)
    SKILL.write_bytes(skill_new)
    print(f"POST cal {len(cal_new)}B (+{len(cal_new)-len(cal_old)}) sha={sha(cal_new)}")
    print(f"POST skill {len(skill_new)}B (+{len(skill_new)-len(skill_old)}) sha={sha(skill_new)}")

    # snapshot diff: every snapshot file vs method counterpart
    diffs = []
    for f in sorted(SNAP.rglob("*")):
        if f.is_file():
            rel = f.relative_to(SNAP)
            counterpart = METHOD / rel
            if not counterpart.exists() or sha(counterpart.read_bytes()) != sha(f.read_bytes()):
                diffs.append(str(rel))
    print("snapshot diff set:", diffs)
    assert diffs == ["SKILL.md", "references/calibration.md"], diffs
    print("snapshot diff == integration set {SKILL.md, references/calibration.md}: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
