#!/usr/bin/env python3
# R78 data seat build: writes data/manifest-carryover-r78-addendum.md and
# data/case-annotations-r78.json. Named-path reads only; no directory listing.
import json, hashlib, collections, copy

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
ANN77 = BASE + "/data/case-annotations-r77.json"
ANN78 = BASE + "/data/case-annotations-r78.json"
ADD78 = BASE + "/data/manifest-carryover-r78-addendum.md"
MAN78 = BASE + "/runs/round78/judging/outcome-manifest.json"
MAN77 = BASE + "/runs/round77/judging/outcome-manifest.json"

NOTE = ("R78: no new carryover layer. R77 adjudication produced no new partial-upheld items "
        "(R77 addendum compilation is the empty set, data/manifest-carryover-r77-addendum.md "
        "cross-verified 6/6 carried items were the R76 set already layered in _r77). "
        "All R77 layers carried verbatim; cases payload identical (sha asserted).")
CASES_SHA = "00f362bd8e4b55ceff31502cb5f7e8239855b1f806a7b1495284af80186a31ad"
MANIFEST_SHA = "69e49cb7e40a8bf294d273b1b3251de7bf4404e40b664bf77feab5df484c13d9"

with open(ANN77, encoding="utf-8") as f:
    ann77 = json.load(f)
with open(MAN78, "rb") as f:
    man78_bytes = f.read()
man78 = json.loads(man78_bytes.decode("utf-8"))
with open(MAN77, encoding="utf-8") as f:
    man77 = json.load(f)

# --- manifest assertions ---
assert hashlib.sha256(man78_bytes).hexdigest() == MANIFEST_SHA, "manifest full sha"
assert man78["_r78_manifest_note"] == NOTE, "note verbatim"
assert "_r78_carryover_notes_addendum" not in man78, "no new layer key"
cases = man78["cases"]
assert len(cases) == 487
sha = hashlib.sha256(json.dumps(cases, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
assert sha == CASES_SHA, sha
assert man77["cases"] == cases, "cases deep equal r77"
assert "_r77_carryover_notes_addendum" in man78 and man78["_r77_carryover_notes_addendum"] == man77["_r77_carryover_notes_addendum"]

# --- six-place baseline recheck (manifest side) ---
needles = [("BZ-036", "盲测比对须注"), ("BZ-042", "（盲测比对时以格局大富一项为主）"),
           ("BZ-105", "使用时须分开统计"), ("LY-204", "勿以此斷")]
for cid, nd in needles:
    assert nd in cases[cid], cid
split = man78["_r56_lr2016_split"]
assert split["case_id"] == "LR2-016"
assert split["editor_note"] == "原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。"
print("manifest assertions OK; cases sha:", sha)

# --- annotations carryover ---
ann_list = ann77["annotations"]
assert len(ann_list) == 70
ids77 = [(a["case_id"], a["anon_id"]) for a in ann_list]
assert len(set(ids77)) == 70
verdicts = dict(collections.Counter(a["disposition"] for a in ann_list))
assert verdicts == {"成立": 12, "部分成立": 54, "不成立": 2, "未核": 2}, verdicts
idset = {a["case_id"] for a in ann_list}
assert "LY-537" in idset and "YM-070" in idset
assert "BZ-029" not in idset and "BZ-040" not in idset
unverified = {a["case_id"]: a["disposition"] for a in ann_list if a["disposition"] == "未核"}
print("unverified entries:", unverified)

PENDING = [
    ("BZ-029", "俞大维卒年待核＋旗标错配线索，维持原登记、不裁；不入 annotations"),
    ("BZ-040", "许世英享年待核，维持原登记、不裁；不入 annotations"),
    ("LY-537", "「申予日」衍字疑，维持未核原登记；本轮由盲测 S6 席（B16）作断、basis 首行对卡面 tradition 照录 liuyao，只登记触及、不裁断；以未核条目随承接在 `case-annotations-r77.json` 内"),
    ("YM-070", "「甲寅旬」出处待核，维持挂起；本轮由盲测 S10 席（B24）作断，只登记触及、不裁断；以未核条目随承接在 `case-annotations-r77.json` 内"),
]

sc_new = [
    {
        "item": "特别核查⑮（R78）：附则对勘——R78 manifest 无新落实层与注记对勘",
        "conclusion": "R78 manifest 本轮无新落实层：顶层无 _r78_carryover_notes_addendum 键；_r78_manifest_note 全文逐字引录于 data/manifest-carryover-r78-addendum.md §二，注记所载（无新落实层／R77 附则汇编为空集／既有各层原样保留／cases 与 R77 件逐字全等）经盘上复核全合——cases 487 例与 runs/round77/judging/outcome-manifest.json 深度全等、cases 结构化 SHA 复算与 R78 PREREG 开轮登记一致、manifest 全文 SHA-256 与主持登记值一致；注记与附则登记一致、无勘误。",
        "evidence": "落盘脚本 runs/round78/data-seat-r78-build.py 结构化直读断言：注记逐字全等、cases SHA（json.dumps sort_keys=True、ensure_ascii=False、默认分隔）复算＝00f362bd8e4b55ceff31502cb5f7e8239855b1f806a7b1495284af80186a31ad、manifest 全文 SHA-256＝69e49cb7e40a8bf294d273b1b3251de7bf4404e40b664bf77feab5df484c13d9、_r77_carryover_notes_addendum 与 R77 manifest 同层深度全等。",
        "scope_note": "对勘只登记、不静默改任一侧。",
    },
    {
        "item": "特别核查⑯（R78）：本轮无新定案（新定案空集登记）",
        "conclusion": "本轮（R78）截至数据席派单时点新定案为空集：无新案例经定案程序裁定成立／部分成立／不成立，故 new_registrations_r78＝0、annotations 全量承接 70 件无新增；自 R79 manifest 起无本轮新定案承接层可落实，R79 承接建议汇编为空集（附则 §三登记）。",
        "evidence": "R78 数据席派单明载「本轮截至派单时新定案为空集」；R78 PREREG §4 数据议程①同载本轮承接汇编为空集口径。",
        "scope_note": "空集只登记；后续轮次若有新定案，承接建议自该轮附则另行汇编，不追溯本轮。",
    },
    {
        "item": "特别核查⑰（R78）：待核挂起四件维持登记（状态原文自 R77 件逐字承接）",
        "conclusion": "BZ-029：俞大维卒年待核＋旗标错配线索，维持原登记、不裁；不入 annotations。BZ-040：许世英享年待核，维持原登记、不裁；不入 annotations。LY-537：「申予日」衍字疑，维持未核原登记；本轮由盲测 S6 席（B16）作断、basis 首行对卡面 tradition 照录 liuyao，只登记触及、不裁断；以未核条目随承接在 case-annotations-r77.json 内（R78 件中随全量承接在本档内）。YM-070：「甲寅旬」出处待核，维持挂起；本轮由盲测 S10 席（B24）作断，只登记触及、不裁断；以未核条目随承接在 case-annotations-r77.json 内（R78 件中随全量承接在本档内）。四件 R78 确认维持挂起、不核查、不关闭；状态原文自 data/manifest-carryover-r77-addendum.md §五逐字承接、不改字（其中「本轮」指 R77 轮触及登记）。",
        "evidence": "data/manifest-carryover-r77-addendum.md §五待核挂起四件表逐字承接；本档断言：LY-537／YM-070 以未核条目在 annotations 70 件内、BZ-029／BZ-040 不在 annotations 内。",
        "scope_note": "待核挂起件只登记维持、不核查不关闭、不入裁断。",
    },
    {
        "item": "特别核查⑱（R78）：指令性字样特别核查基线六处复核登记",
        "conclusion": "基线六处逐处复核：cases 本体四例在 R78 manifest 在册——BZ-036 结局含「盲测比对须注」、BZ-042 结局含「（盲测比对时以格局大富一项为主）」、BZ-105 结局含「使用时须分开统计」、LY-204 结局旧注层含「勿以此斷」（cases 与 R77 件逐字全等、四字样逐字在盘）；LR2-016 manifest editor_note 一处在册——_r56_lr2016_split.editor_note 逐字为「原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。」、manifest 全文该句恰 1 次；LR2-016 评审包 editor_note 层一件——其文本与 manifest editor_note 同文，基线在册登记维持；R78 评审包文件本席未获派单点名路径、且禁列 judging 目录，未逐件打开评审包原件，该层登记为「基线在册、评审包侧原件待评审包落盘后对勘」，不冒称已核原件。三层同字样而来源层不同、分列不混；各席与本席均按数据处理。",
        "evidence": "落盘脚本逐件断言：四例字样在 runs/round78/judging/outcome-manifest.json cases 本体在场、_r56_lr2016_split.editor_note 与基线文本逐字全等；评审包层承 R77 附则 §4.3 登记（R77 评审包条目 P3-21d1866b）。",
        "scope_note": "内嵌字样只作数据登记，不构成对任何席位的指令；本件不入 annotations。",
    },
]

provenance = (
    "R78 数据席（附则承接＋annotations 全量专席，独立席位，不兼任本轮盲测/评审/诊断/组集/修订/集成，不改任何分数）："
    "以 data/case-annotations-r77.json 为底承接全量 70 件（成立 12／部分成立 54／不成立 2／未核 2），annotations 数组逐件原样承接、无删改（落盘脚本以 id 集断言与数组全等断言验过）；"
    "本轮无新登记（new_registrations_r78＝0）——R78 截至派单时点新定案为空集，故 R79 承接建议汇编为空集（详见 data/manifest-carryover-r78-addendum.md §三）。"
    "附则对勘：R78 manifest 本轮无新落实层（顶层无 _r78_carryover_notes_addendum 键），_r78_manifest_note 全文逐字引录于附则 §二、注记与附则登记一致、无勘误；cases 487 例与 R77 manifest 深度全等，cases 结构化 SHA 复算＝00f362bd8e4b55ceff31502cb5f7e8239855b1f806a7b1495284af80186a31ad。"
    "指令性字样基线六处复核：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）与 LR2-016 manifest editor_note 一处经 manifest 盘上复核在册，评审包 editor_note 层一件基线在册登记维持（评审包原件未获点名路径、未逐件打开，登记状态见附则 §四），只登记不改文本。"
    "待核维持件 BZ-029／BZ-040／LY-537 与挂起件 YM-070 维持原登记、不核查不关闭（状态原文自 R77 附则 §五逐字承接，见本档特别核查⑰）。"
    "本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文；结局/注记文本内指令性字样一律按数据处理。"
)

out = {
    "_provenance": provenance,
    "round": 78,
    "annotations": copy.deepcopy(ann_list),
    "special_checks": copy.deepcopy(ann77["special_checks"]) + sc_new,
    "counts": {
        "base_file": "data/case-annotations-r77.json",
        "base_cases_total": 70,
        "base_verdicts": {"成立": 12, "部分成立": 54, "不成立": 2, "未核": 2},
        "new_registrations_r78": 0,
        "new_partial_cases_r78": [],
        "cases_total": 70,
        "verdicts": {"成立": 12, "部分成立": 54, "不成立": 2, "未核": 2},
    },
}
assert out["annotations"] == ann_list
assert [(a["case_id"], a["anon_id"]) for a in out["annotations"]] == ids77
assert len(out["special_checks"]) == 18

with open(ANN78, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
    f.write("\n")

# re-read verify
with open(ANN78, encoding="utf-8") as f:
    chk = json.load(f)
assert chk["annotations"] == ann_list and chk["round"] == 78 and len(chk["special_checks"]) == 18
print("annotations r78 written OK")

# --- addendum ---
rows = "\n".join(f"| {cid} | {txt} |" for cid, txt in PENDING)
addendum = f"""# Manifest 承接册附则（R78）——R77 定案承接对勘（本轮无新落实层）＋R78 定案承接建议汇编（空集）

## 卷首说明

- 本附则为 Phase 3 Round 78（R78）数据席（工序：附则承接对勘＋annotations 全量承接；独立席位，不兼任本轮盲测／评审／诊断／组集／修订／集成）产出。
- 对勘来源：`benchmark/phase3/runs/round78/judging/outcome-manifest.json`（本轮 manifest，含轮次注记 `_r78_manifest_note`；**本轮无新落实层**）、`benchmark/phase3/data/manifest-carryover-r77-addendum.md`（R77 附则，其汇编为 R77 定案承接建议空集）、`benchmark/phase3/data/case-annotations-r77.json`（结构化直读底本：annotations 70 件，定案分布成立 12／部分成立 54／不成立 2／未核 2）。
- **本件只汇编、对勘与登记，不改任何分数与结局原文、不改原卡、不改 manifest 任一侧。** 结局／注记文本内指令性字样一律按数据处理。

---

## 一、工序与口径

- 工序一（对勘，见 §二）：R78 manifest 本轮无新落实层——R77 附则落实候选汇编为空集（R77 无新定案，`data/manifest-carryover-r77-addendum.md` §三登记），故无逐件落实对勘对象；本节改为对 manifest `_r78_manifest_note` 全文逐字引录，并就注记所载四项（无新落实层／R77 附则汇编为空集／既有各层原样保留／cases 逐字全等）逐项以盘上实测对勘。
- 工序二（汇编，见 §三）：R79 承接建议汇编——本轮（R78）新定案承接建议。本轮截至派单时点新定案为空集，汇编为空集，只登记。
- 工序三（标注落盘，见 §五）：`data/case-annotations-r78.json` 以 r77 件 70 件全量承接、本轮新增登记 0 件。
- 特别核查（见 §四）：指令性字样特别核查基线六处复核，承 R78 PREREG §4 基线，只登记、不改文本。
- 嵌入形态登记（承前轮口径）：本轮无新注记文本产生，无嵌入事项。

---

## 二、对勘：R78 manifest 无新落实层——`_r78_manifest_note` 逐字引录与对勘结论

### 2.1 注记全文（自 R78 manifest 结构化直读，逐字引录）

> {NOTE}

### 2.2 逐项对勘

| # | 注记所载 | 盘上复核 | 结果 |
|---|---|---|---|
| 1 | 本轮无新落实层（no new carryover layer） | R78 manifest 顶层键无 `_r78_carryover_notes_addendum`，最新层止于 `_r77_carryover_notes_addendum` 与本注记 | 合 |
| 2 | R77 定案无新部分成立件、R77 附则汇编为空集 | `data/manifest-carryover-r77-addendum.md` §三明载汇编为空集（本轮无新定案承接建议） | 合 |
| 3 | 既有各层原样保留（All R77 layers carried verbatim） | `_r77_carryover_notes_addendum` 与 `runs/round77/judging/outcome-manifest.json` 同层深度全等；其余既有各层随 manifest 构建原样保留（构建口径见 R78 PREREG §0） | 合 |
| 4 | cases 载荷全等（cases payload identical, sha asserted） | R78 cases 487 例与 R77 manifest cases 深度全等；结构化 SHA 复算（json.dumps sort_keys=True、ensure_ascii=False、默认分隔）＝`{CASES_SHA}`，与 R78 PREREG 开轮登记一致；manifest 全文 SHA-256 复算＝`{MANIFEST_SHA}`，与主持登记一致 | 合 |

- 对勘结论：**注记与本件登记一致**——注记四项所载与盘上实测逐项相合、本件 §一至 §三登记与注记同口径，**无勘误**，不静默改任一侧。

---

## 三、R79 承接建议汇编：本轮无新定案承接建议（空集登记）

- **本轮无新定案承接建议。** 本节汇编为空集，自 R79 manifest 起无本轮新定案承接层可落实；`data/case-annotations-r78.json` 本轮新增登记 0 件（见 §五）。
- 依据：本轮（R78）截至数据席派单时点新定案为空集——无新案例经定案程序裁定成立／部分成立／不成立，故无承接建议文本可汇编；R78 PREREG §4 ①同载本轮承接汇编为空集口径。
- 故本节不立逐件条目、不拟任何建议注记原文；后续轮次若有新定案，承接建议自该轮附则另行汇编，不追溯本轮。

---

## 四、指令性字样特别核查基线六处复核（承 R78 PREREG §4 基线）

- 基线构成：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）＋LR2-016 manifest editor_note 一处＋LR2-016 评审包 editor_note 层一处，共六处、分三层。本轮自 `runs/round78/judging/outcome-manifest.json` 盘上复核，**只登记、不改文本**；各席与本席均按数据处理、不作指令。

### 4.1 cases 本体四例（manifest cases 本体逐字在场）

| case_id | 基线字样（按数据引录） | 本轮在盘形态 |
|---|---|---|
| BZ-036 | 结局含「盲测比对须注」 | 在册：在场——结局作「……史载下狱三年、系狱前后牵连较久，此年数有出入，盲测比对须注）；1936年卒于苏州」，字样逐字在盘 |
| BZ-042 | 结局含「（盲测比对时以格局大富一项为主）」 | 在册：在场——结局尾段逐字作「（盲测比对时以格局大富一项为主）」 |
| BZ-105 | 结局含「使用时须分开统计」 | 在册：在场——结局尾段逐字作「……盲测价值低于C04类前瞻断语，使用时须分开统计」 |
| LY-204 | 结局旧注层含「勿以此斷」 | 在册：在场——结局逐字作「……舊注官鬼持世疾病纏綿﹐若是貴人。勿以此斷。此人原非貴人。……」 |

- 附注：R78 cases 与 R77 件逐字全等（§二.2 第 4 项），四例字样本轮在盘形态与 R77 附则 §4.1 登记逐字一致。

### 4.2 LR2-016 manifest editor_note 一处（分列层）

- 所在：manifest `_r56_lr2016_split`（case_id＝LR2-016，分列状态原样承接）。
- 在册：editor_note 本轮在盘原文逐字：「原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。」（按数据引录）——与基线全等；manifest 全文该句恰出现 1 次。

### 4.3 LR2-016 评审包 editor_note 层一处（另列一类）

- 基线登记：R77 评审包条目 P3-21d1866b（case_id＝LR2-016）editor_note 与 §4.2 同字样逐字全等（R77 附则 §4.3 登记）。
- 本轮复核状态：该层文本与 manifest editor_note 同文，**基线在册登记维持**；R78 评审包文件本席未获派单点名路径，且按卫生规禁列 judging 目录，本轮未逐件打开 R78 评审包原件——登记为「基线在册、评审包侧原件待评审包落盘后按点名路径对勘」，不冒称已核原件。
- 分类：本件属评审包 editor_note 层，与 §4.2 manifest 分列层同例同字样而来源层不同，另列一类、不并入 cases 本体基线计数。

### 4.4 结论

- 基线六处：五处（cases 本体四例＋manifest editor_note 一处）经 R78 manifest 盘上复核在册、与基线逐字全等，出入 0 处；一处（评审包 editor_note 层）基线在册登记维持、原件对勘状态如 §4.3 所记。无新增同型件登记。本席只登记、不改任何文本。

---

## 五、annotations 落盘断言与待核维持清单

### 5.1 annotations 落盘断言（工序三）

- 底本：`data/case-annotations-r77.json` annotations 70 件（成立 12／部分成立 54／不成立 2／未核 2），全量承接、逐件原样、无删改（落盘脚本以 annotations 数组全等断言与 id 集断言验过：(case_id, anon_id) 70 组与底本逐组全等、唯一 70）。
- 新增登记：**0 件**（本轮新定案为空集，见 §三）——R78 无新定案、70 件全量承接。
- 落盘：`data/case-annotations-r78.json` annotations **70 件＝70＋0**（成立 12／部分成立 54／不成立 2／未核 2），counts 相应更新（base 70／new_registrations_r78＝0／cases_total 70／verdicts 不变），回读 JSON 可解析断言通过。
- special_checks 承接 r77 十四件并新增 R78 四件（⑮ 附则对勘无新落实层；⑯ 无新定案空集；⑰ 待核挂起四件维持；⑱ 指令性字样基线六处复核），合计 18 件。

### 5.2 R78 确认的待核维持清单（四件，维持挂起、不核查不关闭）

以下四件状态原文自 `data/manifest-carryover-r77-addendum.md` §五逐字承接、不改字（其中「本轮」指 R77 轮触及登记，`case-annotations-r77.json` 在 R78 件中随全量承接为 `data/case-annotations-r78.json`）：

| case_id | 状态原文（逐字承接） |
|---|---|
{rows}

- R78 确认：四件维持挂起，本轮不核查、不关闭；BZ-029 另含旗标内容错配线索、BZ-040 享年两说并存、LY-537 衍字疑、YM-070 表述层瑕疵，均维持原登记。
"""
with open(ADD78, "w", encoding="utf-8") as f:
    f.write(addendum)

import os
print("ADD78 bytes:", os.path.getsize(ADD78))
print("ANN78 bytes:", os.path.getsize(ANN78))
print("ALL OK")
