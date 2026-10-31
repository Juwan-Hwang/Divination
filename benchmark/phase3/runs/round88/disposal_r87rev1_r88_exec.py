#!/usr/bin/env python3
"""R88 disposal executor for R87-REV1 (JUDGMENT-R87-REV1-r88, unmet-not-falsified).
Appends exactly one failure-registration paragraph at end of section 12 of
live calibration.md, after a blank line. Asserts baseline equality and
section-12-last anchor before writing; verifies strip-back after.
"""
import hashlib
import pathlib
import sys

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
LIVE_CAL = BASE / "method/references/calibration.md"
LIVE_SKILL = BASE / "method/SKILL.md"
SNAP_CAL = BASE / "runs/round88/kb-snapshot/references/calibration.md"
SNAP_SKILL = BASE / "runs/round88/kb-snapshot/SKILL.md"

PARA = (
    "**失效登记（R88 判读，runs/round88/acceptance/JUDGMENT-R87-REV1-r88.md §4）**："
    "本节判读口径已于 R88 以 holdout31 验收诊断（DIAG-H31，N＝28）执行判读："
    "主指标 TIM 实质主码率 7/28＝0.250（线 ≤0.120）未达、"
    "护栏甲 OMIT 主码计数 1/28 守、护栏乙 CLAIM 主码计数 10/28 守（恰压线）、"
    "护栏丙 DIR 主码计数 10/28 破线（线 ≤0.330／计数 ≤9）、"
    "护栏丁总配对差 −1.652 守（线 ≥−2.670）、护栏戊含时间坐标例留痕齐备 28/28 守——"
    "主指标未达、护栏丙破线、护栏甲乙丁戊守，判读**未达未证伪**；"
    "证伪两线未触（TIM 实质 0.250＜0.320、总配对差 −1.652＞−3.170），SKILL (t) 指针保留。"
    "本节条文自 R89 起标失效存档、不再强制执行，原文保留备查；"
    "本节失效后现行干预仅第八节（第八节为唯一判读成立现行节，其判读成立状态不因本登记改变）；"
    "本登记不使第五、六、七、九、十、十一节复活或改变其存档状态；"
    "后续修订须基于再下一份聚合诊断另行提案、另立编号。"
)

ANCHOR_LAST = (
    "4. **归因分离（写死）**：本提案不以 CLAIM 为对象，CLAIM 计数只入护栏乙；"
    "护栏乙破线只构成未达、不构成对 CLAIM 向任何新立项的授权，CLAIM 向处置仍以 R86 裁定为准。"
    "本提案判读与第八节判读成立状态无关；本节不使第五、六、七、九、十、十一节复活或失效。"
)
SECTION12_HEAD = "## 十二、应期坐标落点对位核（R87 干预 R87-REV1，跨体系坐标落点机制，现行）"


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    live_cal_b = LIVE_CAL.read_bytes()
    live_skill_b = LIVE_SKILL.read_bytes()
    snap_cal_b = SNAP_CAL.read_bytes()
    snap_skill_b = SNAP_SKILL.read_bytes()

    print(f"PRE cal live sha={sha(live_cal_b)} bytes={len(live_cal_b)}")
    print(f"PRE cal snap sha={sha(snap_cal_b)} bytes={len(snap_cal_b)}")
    print(f"PRE skill live sha={sha(live_skill_b)} bytes={len(live_skill_b)}")
    print(f"PRE skill snap sha={sha(snap_skill_b)} bytes={len(snap_skill_b)}")
    assert live_cal_b == snap_cal_b, "BASELINE MISMATCH calibration"
    assert live_skill_b == snap_skill_b, "BASELINE MISMATCH SKILL"
    print("BASELINE_OK")

    text = live_cal_b.decode("utf-8")
    assert text.endswith("\n"), "file must end with newline"
    lines = text.splitlines()
    # Section 12 is the last ## section
    heads = [(i, l) for i, l in enumerate(lines) if l.startswith("## ")]
    assert heads[-1][1] == SECTION12_HEAD, f"last section is not 12: {heads[-1][1]!r}"
    assert lines[-1] == ANCHOR_LAST, f"anchor mismatch: {lines[-1]!r}"
    print(f"ANCHOR_OK last_line_no={len(lines)} section12_start_line={heads[-1][0]+1}")

    suffix = ("\n" + PARA + "\n").encode("utf-8")
    new_b = live_cal_b + suffix
    LIVE_CAL.write_bytes(new_b)
    print(f"APPENDED suffix_bytes={len(suffix)}")

    post_cal_b = LIVE_CAL.read_bytes()
    post_skill_b = LIVE_SKILL.read_bytes()
    print(f"POST cal sha={sha(post_cal_b)} bytes={len(post_cal_b)} lines={len(post_cal_b.decode('utf-8').splitlines())}")
    print(f"POST skill sha={sha(post_skill_b)} bytes={len(post_skill_b)}")

    # strip-back: remove exactly suffix from end
    assert post_cal_b.endswith(suffix), "post file does not end with suffix"
    stripped = post_cal_b[: -len(suffix)]
    print(f"STRIP cal sha={sha(stripped)} bytes={len(stripped)} equal_baseline={stripped == snap_cal_b}")
    assert stripped == snap_cal_b, "STRIP-BACK MISMATCH"
    assert post_skill_b == snap_skill_b, "SKILL CHANGED"
    print("STRIPBACK_OK")
    print("SKILL_UNCHANGED_OK")
    print(f"PARA_BEGIN\n{PARA}\nPARA_END")
    return 0


if __name__ == "__main__":
    sys.exit(main())
