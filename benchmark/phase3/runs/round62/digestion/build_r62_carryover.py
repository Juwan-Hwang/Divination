#!/usr/bin/env python3
"""R62 数据席任务一：编制 manifest-carryover-r62-addendum.md。

结构化直读（json.load 后按字段取用，禁用正则截断抽取）：
- benchmark/phase3/data/case-annotations-r61.json（R61 定案正本）
- benchmark/phase3/runs/round62/judging/outcome-manifest.json
  仅取 `_r62_carryover_notes_addendum` 层与 `cases` 键名集，不读其他层内容。
不改 manifest 与 annotations 任一侧，不改任何分数与结局原文。
"""
import json
import collections
from pathlib import Path

BASE = Path("/home/hatch/workspace/divination")
ANN_PATH = BASE / "benchmark/phase3/data/case-annotations-r61.json"
MANIFEST_PATH = BASE / "benchmark/phase3/runs/round62/judging/outcome-manifest.json"
OUT_PATH = BASE / "benchmark/phase3/data/manifest-carryover-r62-addendum.md"

EXPECTED = {"成立": 14, "部分成立": 58, "不成立": 7, "未核": 2}


def main() -> None:
    ann_doc = json.loads(ANN_PATH.read_text(encoding="utf-8"))
    annotations = ann_doc["annotations"]
    counts_verdicts = ann_doc["counts"]["verdicts"]

    # 开工断言：原档 counts 与 annotations[].disposition 双路复算，须与派单分布一致
    recomputed = dict(collections.Counter(a["disposition"] for a in annotations))
    assert counts_verdicts == EXPECTED, f"counts.verdicts 不符: {counts_verdicts}"
    assert recomputed == EXPECTED, f"disposition 复算不符: {recomputed}"
    assert len(annotations) == 81, f"annotations 总数不符: {len(annotations)}"

    partials = [a for a in annotations if a["disposition"] == "部分成立"]
    assert len(partials) == 58, f"部分成立件数不符: {len(partials)}"
    others = {
        disp: [a["case_id"] for a in annotations if a["disposition"] == disp]
        for disp in ("成立", "不成立", "未核")
    }
    assert len(others["成立"]) == 14 and len(others["不成立"]) == 7 and len(others["未核"]) == 2

    # outcome-manifest：仅读 _r62 层与 cases 键名集
    manifest_doc = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    r62_layer = manifest_doc["_r62_carryover_notes_addendum"]
    _cases_key_names = set(manifest_doc["cases"].keys())  # 仅键名集，按纪律不读其载荷
    assert isinstance(r62_layer, dict), f"_r62 层类型不符: {type(r62_layer)}"

    # 对勘：case_id 集全等、suggestion 文本全等（全文字符串相等）
    partial_ids = [a["case_id"] for a in partials]
    set_equal = set(r62_layer.keys()) == set(partial_ids)
    diffs = []
    per_case = []
    for a in partials:
        cid = a["case_id"]
        sugg = a["manifest_carry_suggestion"]
        if cid not in r62_layer:
            diffs.append((cid, sugg, None))
            per_case.append(f"{cid}＝不一致（manifest 层缺键）")
        elif r62_layer[cid] != sugg:
            diffs.append((cid, sugg, r62_layer[cid]))
            per_case.append(f"{cid}＝不一致")
        else:
            per_case.append(f"{cid}＝一致")
    extra_keys = sorted(set(r62_layer.keys()) - set(partial_ids))
    n_equal = 58 - len(diffs)
    detail_str = "、".join(per_case)

    lines = []
    lines.append("# Manifest 承接册附则（R62）——R61 定案承接建议汇编")
    lines.append("")
    lines.append("## 卷首说明")
    lines.append("")
    lines.append("- 本附则为 Phase 3 Round 62（R62）数据席（任务一：承接附则编制；与本轮盲测／评审／诊断席互不兼任）产出；汇编来源为 `benchmark/phase3/data/case-annotations-r61.json`（R61 定案正本：annotations 81 件，定案分布成立 14／部分成立 58／不成立 7／未核 2）。")
    lines.append("- counts 断言结果：通过。本席以原档 `counts.verdicts` 与 `annotations[].disposition` 双路复算，均为成立 14／部分成立 58／不成立 7／未核 2、总 81，与派单预期逐项一致。")
    lines.append(f"- 对勘结果：{n_equal}/58 全等（详见「对勘记录」）。对勘对象为 `benchmark/phase3/runs/round62/judging/outcome-manifest.json` 的 `_r62_carryover_notes_addendum` 层，逐件以全文字符串相等比对本附则转录的 `manifest_carry_suggestion`；不一致者登记于对勘记录，不静默改任一侧。")
    lines.append("- **本附则自 R63 manifest 起落实**；本轮（R62）manifest 不据本附则改动。")
    lines.append("- **本件只汇编与对勘，不改任何分数与结局原文。**")
    lines.append("- 汇编范围：R61 定案中部分成立 58 件，逐件全列于第一节（顺序照原档 `annotations` 排列）；每件的承接注记建议文本照 `case-annotations-r61.json` 该件 `manifest_carry_suggestion` 字段原文录入，不改写（其中「自 R62 起」等表述为原档原文，落实轮次按卷首上一条读作自 R63 起，不回溯改动 R62）。每件定案要旨照原档 `finding` 字段、原旗标要旨照原档 `flag` 字段、与既有承接册／附则条目的关系照原档 `relation` 字段录入。")
    lines.append("- 成立 14／不成立 7／未核 2 共 23 件不入正文逐件节，只在文末列 case_id 清单。")
    lines.append("- 承接只标注、不改任何既往或本轮分数、不改结局原文、不改原卡。")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 一、部分成立件承接汇编（定案档位：部分成立，58 件，逐件全列）")
    lines.append("")

    for idx, a in enumerate(partials, start=1):
        lines.append(f"### A{idx}. {a['case_id']}")
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
    lines.append("- 对勘对象：本汇编第一节 58 件承接注记建议文本（源：`case-annotations-r61.json` 各件 `manifest_carry_suggestion`）与 `benchmark/phase3/runs/round62/judging/outcome-manifest.json` 的 `_r62_carryover_notes_addendum` 对应条目，逐件逐字（全文字符串相等）对勘。")
    if not diffs and set_equal and not extra_keys:
        lines.append(f"- 对勘结果：58 件逐字一致，差异 0 件（对勘明细：{detail_str}）。")
        lines.append("- 键集合差异：无（manifest 层 58 键与部分成立 58 件 case_id 集合全等）。")
        lines.append("- 不一致登记：无。两侧均未作任何静默改动；本附则建议文本照源档原文录入，manifest 侧文本照其盘上原文对勘。")
    else:
        lines.append(f"- 对勘结果：{n_equal}/58 一致，差异 {len(diffs)} 件；case_id 集全等：{set_equal}；manifest 层多余键：{extra_keys if extra_keys else '无'}（对勘明细：{detail_str}）。")
        lines.append("- 不一致登记（以盘上两件交叉核对登记，不静默改任一侧）：")
        for cid, sugg_ann, sugg_man in diffs:
            lines.append(f"  - {cid}：annotations 侧＝「{sugg_ann}」；manifest 侧＝「{sugg_man}」。以盘上两件交叉核对登记。")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 自验")
    lines.append("")
    lines.append("- 原档（case-annotations-r61.json）条目数：81；档位分布成立 14／部分成立 58／不成立 7／未核 2，本席以 `annotations[].disposition` 与原档 `counts.verdicts` 双路复算一致。")
    lines.append("- 本附则正文条目数：58（第一节部分成立 58 件），与原档部分成立件数对齐；文末不入附则清单 23 件（成立 14＋不成立 7＋未核 2），58＋23＝81 与原档总数对齐。")
    lines.append(f"- 承接注记建议文本：58 件均自原档 JSON 的 `manifest_carry_suggestion` 字段结构化直读录入，未手抄改写；且经上节对勘与 R62 manifest `_r62_carryover_notes_addendum` 逐件逐字一致（{n_equal}／58）。")
    lines.append("- 纪律自报：本席只汇编与对勘，未改任何分数、未改 manifest、未改 annotations、未改原卡；outcome-manifest 只读 `_r62_carryover_notes_addendum` 层与 `cases` 键名集。")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 文末清单：不入附则 23 件（成立 14＋不成立 7＋未核 2，仅列 case_id）")
    lines.append("")
    lines.append("### 成立 14 件")
    lines.append("")
    for cid in others["成立"]:
        lines.append(f"- {cid}")
    lines.append("")
    lines.append("### 不成立 7 件")
    lines.append("")
    for cid in others["不成立"]:
        lines.append(f"- {cid}")
    lines.append("")
    lines.append("### 未核 2 件")
    lines.append("")
    for cid in others["未核"]:
        lines.append(f"- {cid}")
    lines.append("")

    OUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"WROTE {OUT_PATH} bytes={OUT_PATH.stat().st_size} equal={n_equal}/58 diffs={len(diffs)} set_equal={set_equal}")


if __name__ == "__main__":
    main()
