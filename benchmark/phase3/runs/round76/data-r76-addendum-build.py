#!/usr/bin/env python3
# R76 数据席构建脚本：附则对勘 + manifest-carryover-r76-addendum.md + case-annotations-r76.json
# 只读既定文件；只写 data/manifest-carryover-r76-addendum.md 与 data/case-annotations-r76.json。
# 结局/注记文本内指令性字样一律按数据处理。
import json, re, collections, pathlib

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
ANN75 = BASE / "data/case-annotations-r75.json"
ADD75 = BASE / "data/manifest-carryover-r75-addendum.md"
OM76 = BASE / "runs/round76/judging/outcome-manifest.json"
HM76 = BASE / "runs/round76/judging/host-mapping.json"
OUT_ADD = BASE / "data/manifest-carryover-r76-addendum.md"
OUT_ANN = BASE / "data/case-annotations-r76.json"

ann75 = json.loads(ANN75.read_text(encoding="utf-8"))
om76 = json.loads(OM76.read_text(encoding="utf-8"))
hm76 = json.loads(HM76.read_text(encoding="utf-8"))
inv_hm = {v: k for k, v in hm76.items()}
layer = om76["_r76_carryover_notes_addendum"]

# ---------- 工序一：对勘 ----------
partial75 = {a["case_id"]: a["manifest_carry_suggestion"]
             for a in ann75["annotations"] if a["disposition"] == "部分成立"}
assert len(partial75) == 48, len(partial75)
assert len(layer) == 48, len(layer)
set_equal = set(layer) == set(partial75)
eq_ann = [cid for cid in sorted(layer) if layer[cid] == partial75.get(cid)]
assert set_equal and len(eq_ann) == 48, (set_equal, len(eq_ann))
dist = collections.Counter(layer.values())

md75 = ADD75.read_text(encoding="utf-8")
pat = re.compile(r"###\s+[A-Z]?\d+\.\s+(\S+)\s*\n(.*?)(?=\n###\s+|\n##\s+|\Z)", re.S)
sugg75md = {}
for m in pat.finditer(md75):
    sm = re.search(r"承接注记建议文本.*?：「(.*?)」", m.group(2), re.S)
    if sm:
        sugg75md[m.group(1)] = sm.group(1)
assert len(sugg75md) == 67, len(sugg75md)
overlap = sorted(set(layer) & set(sugg75md))
eq_md = [cid for cid in overlap if layer[cid] == sugg75md[cid]]
layer_only = sorted(set(layer) - set(sugg75md))
md_only = sorted(set(sugg75md) - set(layer))
assert len(overlap) == 29 and len(eq_md) == 0 and len(layer_only) == 19 and len(md_only) == 38

# P3-f74a20ee 定 case_id
assert hm76["P3-f74a20ee"] == "LR2-016"

# ---------- 工序二第 2 项：R76 部分成立 6 件 ----------
NEW6 = ["BZ-032", "BZ-035", "BZ-036", "BZ-037", "BZ-038", "BZ-041"]
SUGG76 = ("主持裁定续接：自 R77 起承接本 R76 标注：按「卡面无 tradition/system 字段、"
          "basis 首行虚称『卡面 tradition＝bazi』（R69 型）、方法实质八字、不作废不重测」登记；"
          "结局原文照录不改。")
FINDING76 = ("主持 FREEZE-r76.md §二裁定（R76 本轮旗标定案）：回原卡——卡面无 tradition/system 字段；"
             "R76 prediction basis 首行统一虚称「卡面 tradition＝bazi」——虚称措辞一层属实（R69 型）；"
             "但方法实质为八字、tradition 值与体裁一致、无 value 误标，虚称不影响方法实质。"
             "主持裁定不作废、不重测。故部分成立。本席按主持裁定登记、不重裁；"
             "与本例既有定案（若有）各旨独立、并行不悖。")
FLAG76 = ("主持 tradition 复核（FREEZE-r76.md §二）：卡面无 tradition/system 字段、"
          "basis 首行称「卡面 tradition＝bazi」；方法实质八字，主持裁定部分成立、不作废不重测")
new_entries = []
for cid in NEW6:
    new_entries.append({
        "anon_id": inv_hm[cid],
        "case_id": cid,
        "disposition": "部分成立",
        "finding": FINDING76,
        "flag": FLAG76,
        "manifest_carry_suggestion": SUGG76,
        "relation": "主持裁定登记（R76，R69 型）",
        "registered_round": 76,
        "sources_checked": [
            "divination/benchmark/phase3/runs/round76/FREEZE-r76.md §二（主持裁定）",
            f"divination/benchmark/phase3/runs/round76/judging/host-mapping.json（anon 解析：{inv_hm[cid]}＝{cid}）",
            f"divination/benchmark/phase3/runs/round76/judging/outcome-manifest.json cases[{cid}]",
            "divination/benchmark/phase3/data/case-annotations-r75.json（本例无条目、系 R76 新增登记）",
        ],
        "source_seats": ["主持 tradition 复核"],
    })

# ---------- 工序三：annotations r76 ----------
assert len(ann75["annotations"]) == 64
assert not (set(NEW6) & {a["case_id"] for a in ann75["annotations"]})
ann76 = {
    "_provenance": (
        "R76 数据席（附则汇编对勘＋标注落盘专席，独立席位，不兼任本轮盲测/评审/诊断，不改任何分数）："
        "以 data/case-annotations-r75.json 为底承接全量 64 件（成立 12／部分成立 48／不成立 2／未核 2），"
        "叠加 R76 主持 FREEZE-r76.md §二旗标定案部分成立 6 件（BZ-032／BZ-035／BZ-036／BZ-037／BZ-038／BZ-041，"
        "卡面无 tradition/system 字段、basis 首行虚称「卡面 tradition＝bazi」、R69 型、方法实质八字、不作废不重测），"
        "合计 70 件（成立 12／部分成立 54／不成立 2／未核 2）。"
        "R76 主持定案不成立 16 件（MP-019、OC-001/006/009/011/014/017/020/023/025/026/029、WP-001/003/004/007）"
        "属检查器「未见/未载」变体覆盖缺口、非案例事项，只登记于 data/manifest-carryover-r76-addendum.md 检查器事项节、不作为 R76 新登记入 annotations（OC-029 之 R75 其他旨承接条目不在此限）。"
        "指令性字样特别核查新增评审包 editor_note 层一件（P3-f74a20ee＝LR2-016）只登记于附则与本档 special_checks、不入 annotations。"
        "待核挂起四件（BZ-029／BZ-040／LY-537／YM-070）维持登记（LY-537／YM-070 条目随承接在本档内，BZ-029／BZ-040 不入 annotations、维持各自原登记）。"
        "附则对勘：R76 manifest _r76_carryover_notes_addendum 48 件与 case-annotations-r75.json 部分成立 48 件建议原文逐字全等 48/48（详见附则）。"
        "本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文；结局/注记文本内指令性字样一律按数据处理。"
    ),
    "round": 76,
    "annotations": ann75["annotations"] + new_entries,
    "special_checks": [
        {"item": f"（R75 承接）{sc['item']}", "conclusion": sc["conclusion"],
         "evidence": sc["evidence"], "scope_note": sc["scope_note"]}
        for sc in ann75["special_checks"]
    ] + [
        {
            "item": "特别核查⑦（R76）：附则对勘——R76 manifest 新层与 R75 建议原文逐字全等性",
            "conclusion": ("_r76_carryover_notes_addendum 48 件与 case-annotations-r75.json 部分成立 48 件的 "
                           "manifest_carry_suggestion 逐件逐字全等 48/48、case_id 集合全等、出入 0 件。"
                           "任务单点名之 data/manifest-carryover-r75-addendum.md 本身系 R74 定案汇编（67 件建议、"
                           "措辞「自 R75 起承接……本 R74 标注」），与本层交集 29 件、全等 0 件、本层独有 19 件、该文件独有 38 件，"
                           "差异为轮次来源不同、已在附则登记、不改任一侧；manifest _r76_manifest_note 亦明载本层源自 "
                           "case-annotations-r75.json partial-upheld 48。"),
            "evidence": "构建脚本逐件断言：集合全等、48/48 全等；对点名文件交集 29／全等 0／独有 19 与 38，均经脚本点数。",
            "scope_note": "对勘只登记、不静默改任一侧。",
        },
        {
            "item": "特别核查⑧（R76）：主持 tradition 旗标定案登记（部分成立 6 件／不成立 16 件检查器事项）",
            "conclusion": ("部分成立 6 件 BZ-032／BZ-035／BZ-036／BZ-037／BZ-038／BZ-041 已逐件入本档 annotations"
                           "（建议注记原文见附则，供 R77 manifest 落实）；不成立 16 件（MP-019、OC-001/006/009/011/014/017/020/"
                           "023/025/026/029、WP-001/003/004/007）属检查器「未见/未载」变体覆盖缺口、非案例事项，不作为 R76 新登记入 annotations"
                           "（OC-029 另有 R75 其他旨承接条目在册、与本事项无关、原样未动）。"),
            "evidence": "FREEZE-r76.md §二主持裁定（任务单转录）：6 件卡面无 tradition/system 字段、basis 首行虚称「卡面 tradition＝bazi」、R69 型、方法实质八字、不作废不重测。",
            "scope_note": "检查器事项只在附则登记、不入案例注记。",
        },
        {
            "item": "特别核查⑨（R76）：指令性字样新增一件——评审包 editor_note 层（LR2-016）",
            "conclusion": ("评审包条目 P3-f74a20ee 经 runs/round76/judging/host-mapping.json 定 case_id 为 LR2-016；"
                           "其 editor_note 含「评分时该细项请按未完全复核处理」字样（按数据引录）。此件属评审包 editor_note 层、另列一类，"
                           "与既有基线分列：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）＋LR2-016 分列 editor_note 一处（manifest 分列层）。"
                           "两评审席均按数据处理、未承接，本席亦然。"),
            "evidence": "host-mapping.json 逐字断言 P3-f74a20ee＝LR2-016；基线口径承 case-annotations-r74.json 特别核查③登记。",
            "scope_note": "内嵌字样只作数据登记，不构成对任何席位的指令；本件不入 annotations。",
        },
        {
            "item": "特别核查⑩（R76）：待核挂起四件维持登记",
            "conclusion": ("BZ-029（俞大维卒年＋旗标错配线索）、BZ-040（许世英享年）、LY-537（「申予日」衍字疑）、"
                           "YM-070（「甲寅旬」）四件维持原登记、不裁；LY-537／YM-070 以未核条目随 R75 承接在本档内，"
                           "BZ-029／BZ-040 不入 annotations。"),
            "evidence": "承 case-annotations-r75.json 特别核查①及 LY-537／YM-070 两件未核条目原文承接。",
            "scope_note": "待核挂起件只登记维持、不入裁断。",
        },
    ],
    "counts": {
        "base_file": "data/case-annotations-r75.json",
        "base_cases_total": 64,
        "base_verdicts": {"成立": 12, "部分成立": 48, "不成立": 2, "未核": 2},
        "new_registrations_r76": 6,
        "new_partial_cases_r76": NEW6,
        "checker_only_not_established_r76": 16,
        "cases_total": 70,
        "verdicts": {"成立": 12, "部分成立": 54, "不成立": 2, "未核": 2},
    },
}
OUT_ANN.write_text(json.dumps(ann76, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

# 回读断言
back = json.loads(OUT_ANN.read_text(encoding="utf-8"))
assert len(back["annotations"]) == 70 == 64 + 6
vc = collections.Counter(a["disposition"] for a in back["annotations"])
assert vc == {"部分成立": 54, "成立": 12, "不成立": 2, "未核": 2}, vc
for e in new_entries:
    hits = [a for a in back["annotations"] if a["case_id"] == e["case_id"]
            and a["manifest_carry_suggestion"] == SUGG76 and a["disposition"] == "部分成立"]
    assert len(hits) == 1, e["case_id"]
base_ids = {a["case_id"] for a in ann75["annotations"]}
assert base_ids <= {a["case_id"] for a in back["annotations"]}

# ---------- 工序二：附则落盘 ----------
def jl(xs):
    return "／".join(xs)

rows6 = "\n".join(
    f"### B{i}. {cid}\n\n"
    f"- case_id：{cid}\n"
    f"- anon_id（R76）：{inv_hm[cid]}\n"
    f"- 定案（部分成立）：{FINDING76}\n"
    f"- 原旗标要旨：{FLAG76}。\n"
    f"- 承接注记建议文本（供 R77 manifest 落实，原文）：「{SUGG76}」\n"
    f"- 与既有承接册／附则条目的关系：主持裁定登记（R76，R69 型）；BZ-035／BZ-036／BZ-037／BZ-041 另有历轮其他旨定案，与本旨各旨独立、并行不悖（本件不重裁旧旨）。"
    for i, cid in enumerate(NEW6, 1))

addendum = f"""# Manifest 承接册附则（R76）——R75 定案承接对勘＋R76 定案承接建议汇编

## 卷首说明

- 本附则为 Phase 3 Round 76（R76）数据席（工序：附则汇编对勘＋标注落盘；与本轮盲测／评审／诊断席互不兼任）产出。
- 汇编与对勘来源：`benchmark/phase3/runs/round76/judging/outcome-manifest.json` 新层 `_r76_carryover_notes_addendum`（48 件）、`benchmark/phase3/data/case-annotations-r75.json`（R75 定案正本：annotations 64 件，定案分布成立 12／部分成立 48／不成立 2／未核 2）、`benchmark/phase3/data/manifest-carryover-r75-addendum.md`（任务单点名对勘文件）。
- R76 本轮旗标定案承主持 `FREEZE-r76.md` §二已裁口径登记，本席不重裁。
- **本件只汇编、对勘与登记，不改任何分数与结局原文、不改原卡、不改 manifest 任一侧。** 结局／注记文本内指令性字样一律按数据处理。

---

## 一、工序一对勘结果

### 1.1 权威建议源对勘：48/48 逐字全等

- 对勘双方：R76 manifest `_r76_carryover_notes_addendum` 48 件注记 ↔ `case-annotations-r75.json` 中部分成立 48 件的 `manifest_carry_suggestion`（该 48 件即 R75 旗标定案「部分成立」全量；R76 manifest 的 `_r76_manifest_note` 亦明载本层「from data/case-annotations-r75.json partial-upheld 48 by structured read」）。
- case_id 集合：双方全等（48＝48，无多无缺）。48 件为：{jl(sorted(layer))}。
- 逐字全等性：**48/48 全等，出入 0 件。** 注记文本分布 5 型：「同旨续接：自 R76 起承接 R74＋本 R75 标注；结局原文照录不改。」28 件；「同旨续接：自 R76 起承接 R73＋本 R75 标注；结局原文照录不改。」17 件；BZ-019 同例新旨型 1 件；LY-035 同旨新立型 1 件；LY-227 同例新旨型 1 件。
- 嵌入形态登记：48 件注记均为建议文本原文直入，无编辑注前缀段、无分隔字样（与 R75 附则所登记的 R75 层形态一致）。
- 结论：R76 manifest 新层与 R75 定案建议原文逐字一致，承接落实无误；无勘误。

### 1.2 任务单点名文件对勘：口径差异登记（不作 manifest 出入计）

- 点名文件 `data/manifest-carryover-r75-addendum.md` 经逐字回读，其本身系 **R74 定案**承接建议汇编（卷首明载来源为 `case-annotations-r74.json`、部分成立 67 件，建议措辞统一为「自 R75 起承接……本 R74 标注」），并非 R75 定案（48 件）的建议汇编。故以其为对勘面时，差异属轮次来源不同，先登记如下，不改任一侧：
  - 交集 case_id：29 件（{jl(overlap)}）；
  - 交集中逐字全等：**0 件**——29 件差异均为轮次措辞差（本层作「自 R76 起……本 R75 标注」、该文件作「自 R75 起……本 R74 标注」），其中 LY-227 本层为 R75 同例新旨文本、与该文件续接文本另有旨别；
  - 本层独有 19 件：{jl(layer_only)}；
  - 该文件独有 38 件：{jl(md_only)}。
- 综合结论（工序一）：以权威建议源（`case-annotations-r75.json`）计，全等 **48/48**、出入清单为空；对点名文件的上述差异为来源轮次口径差，已逐项登记如上，不构成 manifest 承接错误。

---

## 二、R76 本轮旗标定案登记（主持 FREEZE-r76.md §二已裁）

### 2.1 部分成立 6 件——逐件登记建议注记原文（供 R77 manifest 落实）

定案要旨（6 件共通）：卡面无 tradition/system 字段，R76 prediction basis 首行统一虚称「卡面 tradition＝bazi」，属 R69 型虚称；方法实质为八字、不作废、不重测。故部分成立。6 件已逐件入 `data/case-annotations-r76.json` annotations（新增登记 6 件），建议注记原文如下逐件照录：

{rows6}

### 2.2 不成立 16 件——检查器事项登记（不入案例注记）

- 清单（16 件）：MP-019、OC-001、OC-006、OC-009、OC-011、OC-014、OC-017、OC-020、OC-023、OC-025、OC-026、OC-029、WP-001、WP-003、WP-004、WP-007。
- 定性：主持裁定不成立；所涉为检查器「未见／未载」变体覆盖缺口，属检查器事项、非案例事项。
- 处理：只在本件登记为检查器事项；**不入案例注记、不作为 R76 新增登记入 `case-annotations-r76.json` annotations、自 R77 manifest 起亦不为此 16 件旗标事项设案例承接注记。**（按：OC-029 在 annotations 内另有 R75 承接之其他旨条目，系既有承接、与本检查器事项无关、原样未动；其余 15 件不在册。）

---

## 三、指令性字样特别核查新增一件（评审包 editor_note 层，另列一类）

- 新增件：评审包条目 **P3-f74a20ee**，经 `benchmark/phase3/runs/round76/judging/host-mapping.json` 定其 case_id 为 **LR2-016**；其 editor_note 含字样「评分时该细项请按未完全复核处理」（按数据引录）。
- 分类：本件属**评审包 editor_note 层**，另列一类，与既有基线分列——
  - cases 本体基线四例：BZ-036（结局含「盲测比对须注」）、BZ-042（结局含「（盲测比对时以格局大富一项为主）」）、BZ-105（结局含「使用时须分开统计」）、LY-204（结局旧注层含「勿以此斷」）；
  - 分列 editor_note 基线一处：LR2-016（manifest 分列 editor_note 含同一字样，承 R56 分列登记）；
  - 本件（R76 新增一类）：LR2-016 评审包条目 P3-f74a20ee 的 editor_note 层，与上 manifest 分列层同例同字样而来源层不同，故另列、不并入基线计数。
- 附记：两评审席对该字样均按数据处理、未承接；本席亦按数据处理。本件只登记，不入 annotations。

---

## 四、待核挂起四件维持登记

| case_id | 维持事项 |
|---|---|
| BZ-029 | 俞大维卒年待核＋旗标错配线索，维持原登记、不裁；不入 annotations |
| BZ-040 | 许世英享年待核，维持原登记、不裁；不入 annotations |
| LY-537 | 「申予日」衍字疑，维持未核原登记；以未核条目随 R75 承接在 `case-annotations-r76.json` 内 |
| YM-070 | 「甲寅旬」出处待核（其承接条目原文并载「都下」语义未明），维持挂起；以未核条目随 R75 承接在 `case-annotations-r76.json` 内 |

---

## 五、annotations 落盘断言（工序三）

- 底本：`data/case-annotations-r75.json` annotations 64 件（成立 12／部分成立 48／不成立 2／未核 2），全量承接、无删改。
- 新增登记：6 件（本附则 §2.1 部分成立 6 件，BZ-032／BZ-035／BZ-036／BZ-037／BZ-038／BZ-041）。
- 落盘：`data/case-annotations-r76.json` annotations **70 件＝64＋6**（成立 12／部分成立 54／不成立 2／未核 2），回读 JSON 可解析断言通过；6 件新注记逐件可检出（case_id＋建议注记原文＋部分成立档位三项合检，每件恰 1 条）断言通过。
- §2.2 之 16 件旗标事项与 §三之 LR2-016 评审包件均未作为 R76 新增登记入 annotations（逐件核：LR2-016 不在册；16 件中仅 OC-029 因 R75 其他旨承接条目在册，该条目与本检查器事项无关、原样承接未动，其余 15 件不在册）。
"""
OUT_ADD.write_text(addendum, encoding="utf-8")

print("layer_vs_ann75_partial: 48/48 equal, set equal")
print("layer_vs_addendum_r75md: overlap 29, equal 0, layer_only 19, md_only 38")
print("P3-f74a20ee =", hm76["P3-f74a20ee"])
print("annotations: base 64 + new 6 = 70; verdicts", dict(vc))
print("addendum bytes:", OUT_ADD.stat().st_size)
print("annotations bytes:", OUT_ANN.stat().st_size)
