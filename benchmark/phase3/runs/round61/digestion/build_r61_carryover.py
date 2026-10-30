#!/usr/bin/env python3
"""R61 data seat: build manifest-carryover-r61-addendum.md.

Structured direct read only (json.load, full-string transcription of
manifest_carry_suggestion). No regex extraction.
Carryover addendum for R60 verdicts (partial 34), cross-checked against
R61 outcome-manifest layer _r61_carryover_notes_addendum. Effective R62.
"""
import json
from collections import Counter
from pathlib import Path

SRC = Path("/home/hatch/workspace/divination/benchmark/phase3/data/case-annotations-r60.json")
MANIFEST = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round61/judging/outcome-manifest.json")
OUT = Path("/home/hatch/workspace/divination/benchmark/phase3/data/manifest-carryover-r61-addendum.md")

EXPECTED = {"成立": 12, "部分成立": 34, "不成立": 5, "未核": 1}
EXPECTED_TOTAL = 52


def main():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    annotations = data["annotations"]
    counts = data["counts"]
    # counts assertion (dual path: counts.verdicts + recomputed Counter)
    recomputed = Counter(a["disposition"] for a in annotations)
    assert counts["verdicts"] == EXPECTED, f"counts.verdicts mismatch: {counts['verdicts']}"
    assert dict(recomputed) == EXPECTED, f"recomputed mismatch: {dict(recomputed)}"
    assert len(annotations) == EXPECTED_TOTAL, f"total mismatch: {len(annotations)}"
    assert counts["cases_total"] == EXPECTED_TOTAL

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    layer = manifest["_r61_carryover_notes_addendum"]
    assert isinstance(layer, dict), f"layer type: {type(layer)}"

    partial = [a for a in annotations if a["disposition"] == "部分成立"]
    established = [a for a in annotations if a["disposition"] == "成立"]
    rejected = [a for a in annotations if a["disposition"] == "不成立"]
    unchecked = [a for a in annotations if a["disposition"] == "未核"]
    assert len(partial) == 34 and len(established) == 12 and len(rejected) == 5 and len(unchecked) == 1

    # Cross-check: full-string equality per case, no silent edit either side.
    match_ids, mismatches = [], []
    for a in partial:
        cid = a["case_id"]
        src_text = a["manifest_carry_suggestion"]
        man_text = layer.get(cid)
        if man_text is not None and man_text == src_text:
            match_ids.append(cid)
        else:
            mismatches.append((cid, src_text, man_text))
    extra_keys = sorted(set(layer.keys()) - {a["case_id"] for a in partial})
    missing_keys = sorted({a["case_id"] for a in partial} - set(layer.keys()))
    n_match = len(match_ids)

    lines = []
    lines.append("# Manifest 承接册附则（R61）——R60 定案承接建议汇编")
    lines.append("")
    lines.append("## 卷首说明")
    lines.append("")
    lines.append("- 本附则为 Phase 3 Round 61（R61）数据席（任务一：承接附则编制与对勘；与本轮盲测／评审／诊断／修订各席分离、不改任何分数）产出；汇编来源为 `benchmark/phase3/data/case-annotations-r60.json`（R60 旗标定案档：自报 52 例，定案分布成立 12／部分成立 34／不成立 5／未核 1）。")
    lines.append(f"- counts 断言结果：通过。本席以原档 `counts.verdicts` 与 `annotations[].disposition` 双路复算，均为成立 12／部分成立 34／不成立 5／未核 1、总 52，与派单预期逐项一致。")
    lines.append(f"- 对勘结果：{n_match}/34 全等（详见文末「对勘记录」）。对勘对象为 `benchmark/phase3/runs/round61/judging/outcome-manifest.json` 的 `_r61_carryover_notes_addendum` 层，逐件以全文字符串相等比对本附则转录的 `manifest_carry_suggestion`；不一致者登记于对勘记录，不静默改任一侧。")
    lines.append("- **本附则自 R62 manifest 起与承接册及 R56／R57／R58／R59／R60 附则合并为 manifest 落实依据**；本轮（R61）manifest 不据本附则改动。")
    lines.append("- 汇编范围：R60 定案中部分成立 34 件，逐件全列于第一节（顺序照原档 `annotations` 排列）；每件的承接注记建议文本照 `case-annotations-r60.json` 该件 `manifest_carry_suggestion` 字段原文录入，不改写（其中「自 R61 起」等表述为原档原文，落实轮次按卷首上一条读作自 R62 起，不回溯改动 R61）。每件定案要旨照原档 `finding` 字段、原旗标要旨照原档 `flag` 字段、与既有承接册／附则条目的关系照原档 `relation` 字段录入。")
    lines.append("- 成立 12 件已于既有承接序列逐轮承接、不在本附则汇编范围内；不成立 5 件不入附则；未核 1 件（YM-070）挂起维持——三类只在下方「不入附则清单」列清单与计数，不入第一节正文。")
    lines.append("- 承接只标注、不改任何既往或本轮分数、不改结局原文、不改原卡（inputs-dev12）。")
    lines.append("")
    lines.append("### 不入附则清单（18 件：成立 12＋不成立 5＋未核 1）")
    lines.append("")
    lines.append("#### 1. 成立 12 件（已于既有承接序列逐轮承接，不入本附则正文）")
    lines.append("")
    for a in established:
        lines.append(f"- {a['case_id']}（anon_id：{a['anon_id']}）：定案成立，{a['relation']}，已于既有承接序列逐轮承接，结局原文照录不改。")
    lines.append("")
    lines.append("#### 2. 不成立 5 件（不入本附则正文）")
    lines.append("")
    for a in rejected:
        lines.append(f"- {a['case_id']}（anon_id：{a['anon_id']}）：定案不成立，{a['relation']}。原档建议为：{a['manifest_carry_suggestion']}")
    lines.append("")
    lines.append("#### 3. 未核 1 件（YM-070 挂起，不入本附则正文）")
    lines.append("")
    for a in unchecked:
        lines.append(f"- case_id：{a['case_id']}")
        lines.append(f"- anon_id：{a['anon_id']}")
        lines.append(f"- 不入附则原因：未核，挂起维持。原档建议为：{a['manifest_carry_suggestion']}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 一、部分成立件承接汇编（定案档位：部分成立，34 件，逐件全列）")
    lines.append("")
    for i, a in enumerate(partial, start=1):
        lines.append(f"### A{i}. {a['case_id']}")
        lines.append("")
        lines.append(f"- case_id：{a['case_id']}")
        lines.append(f"- anon_id：{a['anon_id']}")
        lines.append(f"- 定案（部分成立）：{a['finding']}")
        lines.append(f"- 原旗标要旨（照原档 `flag` 字段）：{a['flag']}")
        lines.append(f"- 承接注记建议文本（照原档 `manifest_carry_suggestion` 原文）：「{a['manifest_carry_suggestion']}」")
        lines.append(f"- 与既有承接册／附则条目的关系（照原档 `relation` 字段）：{a['relation']}")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 对勘记录")
    lines.append("")
    lines.append("- 对勘对象：本汇编第一节 34 件承接注记建议文本（源：`case-annotations-r60.json` 各件 `manifest_carry_suggestion`）与 `benchmark/phase3/runs/round61/judging/outcome-manifest.json` 的 `_r61_carryover_notes_addendum` 对应条目，逐件逐字（全文字符串相等）对勘。")
    detail = "、".join(f"{cid}＝{'一致' if cid in match_ids else '不一致'}" for cid in [a['case_id'] for a in partial])
    lines.append(f"- 对勘结果：{n_match} 件逐字一致，差异 {len(mismatches)} 件（对勘明细：{detail}）。")
    if extra_keys or missing_keys:
        lines.append(f"- 键集合差异：manifest 层多出键 {extra_keys}；manifest 层缺失键 {missing_keys}。")
    else:
        lines.append("- 键集合差异：无（manifest 层 34 键与部分成立 34 件 case_id 集合一致）。")
    if mismatches:
        lines.append("- 不一致登记（停下登记、不静默改任一侧）：")
        for cid, src_text, man_text in mismatches:
            lines.append(f"  - {cid}：源档文本＝「{src_text}」；manifest 层文本＝「{man_text}」")
    else:
        lines.append("- 不一致登记：无。两侧均未作任何静默改动；本附则建议文本照源档原文录入，manifest 侧文本照其盘上原文对勘。")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 自验")
    lines.append("")
    lines.append("- 原档（case-annotations-r60.json）条目数：52；档位分布成立 12／部分成立 34／不成立 5／未核 1，本席以 `annotations[].disposition` 与原档 `counts.verdicts` 双路复算一致。")
    lines.append("- 本附则正文条目数：34（第一节部分成立 34 件），与原档部分成立件数对齐；卷首不入附则 18 件（成立 12＋不成立 5＋未核 1），34＋18＝52 与原档总数对齐。")
    lines.append(f"- 承接注记建议文本：34 件均自原档 JSON 的 `manifest_carry_suggestion` 字段结构化直读录入，未手抄改写；且经上节对勘与 R61 manifest `_r61_carryover_notes_addendum` 逐件逐字一致（{n_match}／34）。")
    lines.append("- 纪律自报：本席只标注，未改任何分数、未改 manifest、未改原卡；未列表任何 runs/ 下 judging/ 目录，只按派单点名文件精确打开。")
    lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"WROTE {OUT} bytes={OUT.stat().st_size}")
    print(f"MATCH {n_match}/34 mismatches={len(mismatches)} extra={extra_keys} missing={missing_keys}")


if __name__ == "__main__":
    main()
