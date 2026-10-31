#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R74 数据席承接附则编制脚本：汇编 R73 定案部分成立 140 件，
与 runs/round74/judging/outcome-manifest.json 的 _r74_carryover_notes_addendum 层逐件对勘。
不一致只登记、不静默改任一侧。数据源结构化直读，禁正则截断式抽取。"""
import json, pathlib
from collections import Counter

P3 = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "data/case-annotations-r73.json"
MANIFEST74 = P3 / "runs/round74/judging/outcome-manifest.json"
OUT = P3 / "data/manifest-carryover-r74-addendum.md"

src = json.loads(SRC.read_text(encoding="utf-8"))
man = json.loads(MANIFEST74.read_text(encoding="utf-8"))
anns = src["annotations"]
recount = Counter(a["disposition"] for a in anns)
assert recount == Counter(src["counts"]["verdicts"]), (recount, src["counts"])
assert src["counts"]["verdicts"] == {"成立": 11, "部分成立": 140, "不成立": 4, "未核": 1}
partial = [a for a in anns if a["disposition"] == "部分成立"]
assert len(partial) == 140
assert all(a["manifest_carry_suggestion"].strip() for a in partial)

layer = man["_r74_carryover_notes_addendum"]
assert isinstance(layer, dict)
ids_src = [a["case_id"] for a in partial]
set_equal = set(ids_src) == set(layer.keys())
mismatches = []
for a in partial:
    cid = a["case_id"]
    if cid not in layer:
        mismatches.append((cid, "manifest 层缺键"))
    elif layer[cid] != a["manifest_carry_suggestion"]:
        mismatches.append((cid, "文本不全等"))
extra = sorted(set(layer.keys()) - set(ids_src))
n_equal = 140 - len(mismatches)
print("set_equal", set_equal, "text_equal", n_equal, "/140", "mismatches", mismatches, "extra", extra)

upheld = [a["case_id"] for a in anns if a["disposition"] == "成立"]
rejected = [a["case_id"] for a in anns if a["disposition"] == "不成立"]
pending = [a["case_id"] for a in anns if a["disposition"] == "未核"]

lines = []
lines.append("# Manifest 承接册附则（R74）——R73 定案承接建议汇编")
lines.append("")
lines.append("## 卷首说明")
lines.append("")
lines.append("- 本附则为 Phase 3 Round 74（R74）数据席（议程一：承接附则编制；与本轮盲测／评审／诊断席互不兼任）产出；汇编来源为 `benchmark/phase3/data/case-annotations-r73.json`（R73 定案正本：annotations 156 件，定案分布成立 11／部分成立 140／不成立 4／未核 1）。")
lines.append("- counts 断言结果：通过。本席以原档 `counts.verdicts` 与 `annotations[].disposition` 双路复算，均为成立 11／部分成立 140／不成立 4／未核 1、总 156，与原档 counts 逐项一致；部分成立 140 件每件 `manifest_carry_suggestion` 非空断言亦通过。")
if set_equal and not mismatches and not extra:
    lines.append("- 对勘结果：140/140 全等（详见「对勘记录」）。对勘对象为 `benchmark/phase3/runs/round74/judging/outcome-manifest.json` 的 `_r74_carryover_notes_addendum` 层（本席只按精确文件名打开该文件、只读该层与 `cases` 载荷），逐件以全文字符串相等比对本附则转录的 `manifest_carry_suggestion`；不一致者登记于对勘记录，不静默改任一侧（本轮不一致 0 件、多键 0 件）。")
else:
    lines.append(f"- 对勘结果：集合全等={set_equal}、文本全等 {n_equal}/140、不一致 {len(mismatches)} 件、多键 {len(extra)} 件（详见「对勘记录」勘误登记）。对勘对象为 `benchmark/phase3/runs/round74/judging/outcome-manifest.json` 的 `_r74_carryover_notes_addendum` 层；不一致只登记、不静默改任一侧。")
lines.append("- **本附则自 R75 manifest 起落实**；本轮（R74）manifest 不据本附则改动。")
lines.append("- **本件只汇编与对勘，不改任何分数与结局原文。**")
lines.append("- 汇编范围：R73 定案中部分成立 140 件，逐件全列于第一节（顺序照原档 `annotations` 排列）；每件的承接注记建议文本照 `case-annotations-r73.json` 该件 `manifest_carry_suggestion` 字段原文录入，不改写（其中「自 R74 起」等表述为原档原文，落实轮次按卷首上一条读作自 R75 起，不回溯改动 R74）。每件定案要旨照原档 `finding` 字段、原旗标要旨照原档 `flag` 字段、与既有承接册／附则条目的关系照原档 `relation` 字段录入。")
lines.append("- 成立 11 件、不成立 4 件、未核 1 件不入正文逐件节，只在文末列 case_id 清单。")
lines.append("- 承接只标注、不改任何既往或本轮分数、不改结局原文、不改原卡。")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 一、部分成立件承接汇编（定案档位：部分成立，140 件，逐件全列）")
lines.append("")
for i, a in enumerate(partial, 1):
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
lines.append("## 二、对勘记录")
lines.append("")
lines.append("- 对勘源：`benchmark/phase3/runs/round74/judging/outcome-manifest.json` 的 `_r74_carryover_notes_addendum` 层，共 140 件。")
if set_equal and not mismatches and not extra:
    lines.append("- 逐件对勘：140 件 case_id 集合与本附则汇编集合全等；每件注记文本与 `case-annotations-r73.json` 对应件 `manifest_carry_suggestion` 全文字符串相等，140/140 全等。")
    lines.append("- 不一致登记：0 件；附则侧与 manifest 侧均未作任何改动（不静默改任一侧）。")
    lines.append("- 勘误：无。")
else:
    lines.append(f"- 逐件对勘：集合全等={set_equal}；文本全等 {n_equal}/140。")
    for cid, kind in mismatches:
        lines.append(f"- 勘误登记：{cid}——{kind}。附则侧录文：「{next(a['manifest_carry_suggestion'] for a in partial if a['case_id']==cid)}」；manifest 侧录文：「{layer.get(cid, '（缺键）')}」。两件交叉核对后登记于此，不静默改任一侧。")
    for cid in extra:
        lines.append(f"- 勘误登记：manifest 层多键 {cid}，附则汇编集合无此件；只登记、不改任一侧。")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 三、不入正文清单（照 R73 定案档位）")
lines.append("")
lines.append(f"- 成立 11 件：{'／'.join(upheld)}")
lines.append(f"- 不成立 4 件：{'／'.join(rejected)}")
lines.append(f"- 未核 1 件：{'／'.join(pending)}")
lines.append("")
OUT.write_text("\n".join(lines), encoding="utf-8")
print("WROTE", OUT, OUT.stat().st_size)
