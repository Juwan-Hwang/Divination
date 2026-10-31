#!/usr/bin/env python3
"""R83 disposal executor for R82-REV1 (calibration section 10).

Basis: runs/round83/acceptance/JUDGMENT-R82-REV1-r83.md section 3 (verdict:
falsified, J7 line crossed). Actions, and only these:
  1. calibration.md section 10: append one invalidation-registration
     paragraph at the end of the section (after R82-REV1-7, before the
     section 11 heading), following the measured precedent form of
     sections 5/6/7/9 (registration paragraph at section end; body text
     untouched byte for byte).
  2. SKILL.md: delete the whole (r) pointer line (points to section 10).
Verification: pre-state hashes must equal the kb-snapshot-holdout28
baseline; post-state diffs vs baseline must be exactly the two actions;
strip-back of the registration paragraph must reproduce the baseline
calibration byte for byte; SKILL line-set difference must be exactly
the (r) line.
"""
import difflib
import hashlib
import os
import sys

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
CAL = BASE + "/method/references/calibration.md"
SKILL = BASE + "/method/SKILL.md"
SNAP = BASE + "/runs/round83/kb-snapshot-holdout28"
SNAP_CAL = SNAP + "/references/calibration.md"
SNAP_SKILL = SNAP + "/SKILL.md"

REGISTRATION = (
    "**失效登记（R83 判读，runs/round83/acceptance/JUDGMENT-R82-REV1-r83.md §二）**："
    "本节判读口径（METHOD-INTEGRATION-r82 写定）已于 R83 以 holdout27 验收诊断（DIAG-H27，N＝27）执行判读："
    "CLAIM 主码率 0.481（13/27，主指标线 ≤0.167／计数上限 4）未达、"
    "TIM 实质主码率 0.074（2/27，副指标线 ≤0.080／计数上限 2）达标（恰压线）、"
    "DIR 主码率 0.259（7/27，护栏线 ≤0.385／计数上限 10）护栏未破、"
    "OMIT 主码率 0.111（3/27，护栏线 ≤0.160／计数上限 4）护栏未破、"
    "E4 主码率 0.074（2/27，护栏线 ≤0.160／计数上限 4）护栏未破、"
    "总配对差 −1.111（护栏线 ≥−1.837）护栏未破——判读**证伪**"
    "（证伪线一 J7 触发：CLAIM 主码率 0.481 ≥0.444、计数 13 ≥证伪计数 12；"
    "证伪线二 J8 未触：总配对差 −1.111 未达 ≤−2.834）；"
    "SKILL (r) 指针照证伪条款删除回滚。"
    "本节条文自 R84 起标失效存档、不再强制执行，原文保留备查；"
    "后续修订须基于再下一份聚合诊断另行提案、另立编号。"
)


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def read_bytes(path):
    with open(path, "rb") as f:
        return f.read()


def main():
    cal_before = read_bytes(CAL)
    skill_before = read_bytes(SKILL)
    snap_cal = read_bytes(SNAP_CAL)
    snap_skill = read_bytes(SNAP_SKILL)

    print("PRE calibration sha256:", sha256_bytes(cal_before), "bytes:", len(cal_before))
    print("PRE SKILL sha256:", sha256_bytes(skill_before), "bytes:", len(skill_before))
    print("SNAP calibration sha256:", sha256_bytes(snap_cal), "bytes:", len(snap_cal))
    print("SNAP SKILL sha256:", sha256_bytes(snap_skill), "bytes:", len(snap_skill))
    if cal_before != snap_cal:
        print("ABORT: live calibration != snapshot baseline")
        return 1
    if skill_before != snap_skill:
        print("ABORT: live SKILL != snapshot baseline")
        return 1
    print("PRE-STATE == SNAPSHOT BASELINE for both files: OK")

    # --- Action 1: calibration section 10 registration paragraph ---
    text = cal_before.decode("utf-8")
    sec10_start = text.index("## 十、")
    sec11_start = text.index("## 十一、")
    sec10_text = text[sec10_start:sec11_start]
    if "失效登记" in sec10_text:
        print("ABORT: section 10 already carries an invalidation registration")
        return 1
    anchor = "\n## 十一、"
    if text.count(anchor) != 1:
        print("ABORT: section-11 heading anchor not unique")
        return 1
    idx = text.index(anchor)
    new_text = text[:idx] + "\n" + REGISTRATION + "\n" + text[idx:]
    # sanity: registration sits inside section 10 span
    nsec10 = new_text[new_text.index("## 十、"):new_text.index("## 十一、")]
    if REGISTRATION not in nsec10:
        print("ABORT: registration not inside section 10")
        return 1
    cal_after = new_text.encode("utf-8")

    # --- Action 2: SKILL (r) line deletion ---
    stext = skill_before.decode("utf-8")
    lines = stext.split("\n")
    r_idx = [i for i, ln in enumerate(lines) if ln.startswith("- (r) ")]
    if len(r_idx) != 1:
        print("ABORT: (r) pointer line count != 1:", len(r_idx))
        return 1
    r_line = lines[r_idx[0]]
    print("R-LINE:", r_line)
    if "references/calibration.md 第十节" not in r_line or "R82-REV1" not in r_line:
        print("ABORT: (r) line does not point to section 10 / R82-REV1")
        return 1
    s_idx = [i for i, ln in enumerate(lines) if ln.startswith("- (s) ")]
    if len(s_idx) != 1 or "第十一节" not in lines[s_idx[0]]:
        print("ABORT: (s) pointer line not uniquely found / not section 11")
        return 1
    new_lines = lines[:r_idx[0]] + lines[r_idx[0] + 1:]
    skill_after = "\n".join(new_lines).encode("utf-8")

    # write both
    with open(CAL, "wb") as f:
        f.write(cal_after)
    with open(SKILL, "wb") as f:
        f.write(skill_after)

    # --- Post verification ---
    cal_now = read_bytes(CAL)
    skill_now = read_bytes(SKILL)
    assert cal_now == cal_after and skill_now == skill_after
    print("POST calibration sha256:", sha256_bytes(cal_now), "bytes:", len(cal_now))
    print("POST SKILL sha256:", sha256_bytes(skill_now), "bytes:", len(skill_now))

    # strip-back: remove inserted paragraph -> baseline bytes
    stripped = cal_now.decode("utf-8").replace("\n" + REGISTRATION + "\n", "", 1)
    print("STRIP-BACK calibration == baseline:", stripped.encode("utf-8") == snap_cal)

    # SKILL line-set diff: exactly the (r) line removed, order preserved
    old_lines = snap_skill.decode("utf-8").split("\n")
    now_lines = skill_now.decode("utf-8").split("\n")
    removed = [ln for ln in old_lines if ln not in now_lines]
    added = [ln for ln in now_lines if ln not in old_lines]
    print("SKILL removed lines:", removed)
    print("SKILL added lines:", added)
    print("SKILL order preserved:", [ln for ln in old_lines if ln != r_line] == now_lines)
    print("SKILL (s) line retained:", any(ln.startswith("- (s) ") for ln in now_lines))

    # unified diffs vs baseline
    print("=== DIFF calibration (baseline -> live) ===")
    for ln in difflib.unified_diff(
        snap_cal.decode("utf-8").split("\n"),
        cal_now.decode("utf-8").split("\n"),
        lineterm="", n=1,
    ):
        print(ln)
    print("=== DIFF SKILL (baseline -> live) ===")
    for ln in difflib.unified_diff(
        snap_skill.decode("utf-8").split("\n"),
        skill_now.decode("utf-8").split("\n"),
        lineterm="", n=1,
    ):
        print(ln)

    # full method tree vs snapshot, scoped to snapshot file set
    diffs = []
    for root, _dirs, files in os.walk(SNAP):
        for fn in files:
            sp = os.path.join(root, fn)
            rel = os.path.relpath(sp, SNAP)
            lp = os.path.join(BASE + "/method", rel)
            if not os.path.exists(lp) or read_bytes(lp) != read_bytes(sp):
                diffs.append(rel)
    print("SNAPSHOT-SET differing files (live vs baseline):", diffs)
    print("DISPOSAL DONE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
