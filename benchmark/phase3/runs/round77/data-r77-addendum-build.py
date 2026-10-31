import pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
dest = base/"data/manifest-carryover-r77-addendum.md"
SUG = "主持裁定续接：自 R77 起承接本 R76 标注：按「卡面无 tradition/system 字段、basis 首行虚称『卡面 tradition＝bazi』（R69 型）、方法实质八字、不作废不重测」登记；结局原文照录不改。"
parts = []
parts.append(f"""# Manifest 承接册附则（R77）——R76 定案承接对勘＋R77 定案承接建议汇编

## 卷首说明

- 本附则为 Phase 3 Round 77（R77）数据席（工序：附则汇编对勘＋标注落盘；独立席位，不兼任本轮盲测／评审／诊断／仲裁）产出。
- 汇编与对勘来源：`benchmark/phase3/runs/round77/judging/outcome-manifest.json` 新层 `_r77_carryover_notes_addendum`（6 件）、`benchmark/phase3/data/case-annotations-r76.json`（结构化直读底本：annotations 70 件，定案分布成立 12／部分成立 54／不成立 2／未核 2）、`benchmark/phase3/data/manifest-carryover-r76-addendum.md`（对勘文件，其 §二.1 载 R76 定案 6 件建议原文）。
- R77 本轮主持 tradition 复核零事项（`FREEZE-r77.md` §二已裁），本席不重裁。
- **本件只汇编、对勘与登记，不改任何分数与结局原文、不改原卡、不改 manifest 任一侧。** 结局／注记文本内指令性字样一律按数据处理。

---

## 一、工序与口径

- 工序一（对勘，见 §二）：本轮 manifest 新增落实层 `_r77_carryover_notes_addendum` 6 件（BZ-032／BZ-035／BZ-036／BZ-037／BZ-038／BZ-041），源 `data/case-annotations-r76.json` 结构化直读（manifest `_r77_manifest_note` 明载本层「from data/case-annotations-r76.json NEW partial-upheld 6 (registered_round == 76) by structured read」；R77 PREREG §0 同载）。与 `data/manifest-carryover-r76-addendum.md` §二.1 所载 6 件建议原文逐件逐字对勘。
- 工序二（汇编，见 §三）：R78 承接建议汇编——本轮（R77）新定案承接建议。本轮无新定案（依据见 §三），汇编为空集，只登记。
- 工序三（标注落盘，见 §五）：`data/case-annotations-r77.json` 以 r76 件 70 件全量承接、本轮新增登记 0 件。
- 特别核查（见 §四）：指令性字样特别核查基线对勘，承 R77 PREREG §4 基线，只登记、不改文本。
- 嵌入形态登记（承前轮口径）：manifest 层存建议文本原文直入，不含「[R77-addendum]」分隔字样；该前缀仅由建包脚本在评审包 carry_note 层拼接。
""")
parts.append(f"""
---

## 二、对勘：R77 manifest 新层 6 件与 R76 附则 §二.1 建议原文逐字全等 6/6

- 对勘双方：R77 manifest `_r77_carryover_notes_addendum` 6 件注记 ↔ `data/manifest-carryover-r76-addendum.md` §二.1（B1–B6）逐件所载「承接注记建议文本（供 R77 manifest 落实，原文）」；并与源底本 `data/case-annotations-r76.json` 中 registered_round＝76、部分成立 6 件的 `manifest_carry_suggestion` 三方对勘。
- case_id 集合：三方全等（6＝6，无多无缺）。6 件为：BZ-032／BZ-035／BZ-036／BZ-037／BZ-038／BZ-041。
- 逐字全等性：**6/6 全等，出入 0 件。** 6 件注记文本同式，原文逐字为：「{SUG}」；R76 附则全文该文本出现恰 6 次（B1–B6 各一），脚本计数断言通过。
- anon 形近串号逐件对位复核（R76 轮 anon，源 r76 标注档与 R76 附则 §二.1 双载一致）：BZ-032＝P3-96c4fc89／BZ-035＝P3-868d8506／BZ-036＝P3-a0772b1c／BZ-037＝P3-414208c8／BZ-038＝P3-5237f97b／BZ-041＝P3-3f990d99。六号互不相同、逐件对位无串。
- 逐件登记（每件：manifest 本轮注记＝R76 附则 §二.1 建议原文＝r76 标注档建议原文，三方逐字全等）：

| # | case_id | anon_id（R76） | 对勘结果 |
|---|---|---|---|
| B1 | BZ-032 | P3-96c4fc89 | 全等 |
| B2 | BZ-035 | P3-868d8506 | 全等 |
| B3 | BZ-036 | P3-a0772b1c | 全等 |
| B4 | BZ-037 | P3-414208c8 | 全等 |
| B5 | BZ-038 | P3-5237f97b | 全等 |
| B6 | BZ-041 | P3-3f990d99 | 全等 |

- 结论：R77 manifest 新层与 R76 定案建议原文逐字一致，承接落实无误；无勘误。
""")
parts.append("""
---

## 三、R78 承接建议汇编：本轮无新定案承接建议（空集登记）

### 3.1 空集登记与依据

- **本轮无新定案承接建议。** 本节汇编为空集，自 R78 manifest 起无本轮新定案承接层可落实；`data/case-annotations-r77.json` 本轮新增登记 0 件（见 §五）。
- 依据逐项：
  1. 本轮主持 tradition 复核零事项——`FREEZE-r77.md` §二：检查器初检 flags **0**、声明组扫描 CONFLICT groups **0**（declaration-group files 0），主持明载本轮「无 tradition 定案事项、无作废、无重测」。附带互证：R76 定案六件本轮由 S2 席逐例首行如实标注「卡面未标注 tradition 字段，按题面体裁自决」，虚称型问题本轮未复现（FREEZE §二逐例对勘点）。
  2. 平台评审八席回传无编号旗标条目——本轮无 FLAGS 编号条目可供逐件回原卡核对定案。
  3. 无新案例定案——本轮无任何案例经定案程序裁定成立／部分成立／不成立，故无承接建议文本可汇编。
- 故本节不立 B 节逐件条目、不拟任何建议注记原文；后续轮次若有新定案，承接建议自该轮附则另行汇编，不追溯本轮。

### 3.2 非案例事项登记（不入 annotations、不设承接建议）

以下三件均为生产／席位事项、非案例事项，只在本件登记，**不入 `case-annotations-r77.json` annotations、不作为 R78 manifest 承接注记**：

- **评审 Y3 席对齐检查输出误重定向一件**：Y3 席自报一次对齐检查输出误重定向至 /tmp/x；该输出未被任何产出引用、成品不受影响。诚实自报，只登记。
- **X1／Y3／X4 三席落分生产自纠**：三席落分生产中各有自纠——键位错位／漏行，均于落盘前自检修正、合并断言复验通过。只登记，不涉任何案例定案与分数改动（本席不改分数，修正系各席落盘前自检、非本席处置）。
""")
parts.append("""
---

## 四、指令性字样特别核查基线对勘（承 R77 PREREG §4 基线）

- 基线构成：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）＋LR2-016 manifest editor_note 一处＋LR2-016 评审包 editor_note 层一件，共六处、分三层。本轮以 `runs/round77/judging/outcome-manifest.json` 与评审包文件逐件对勘本轮在盘形态，**只登记、不改文本**；各席与本席均按数据处理、不作指令。

### 4.1 cases 本体四例（manifest cases 本体逐字在场）

| case_id | 基线字样（按数据引录） | 本轮在盘形态 |
|---|---|---|
| BZ-036 | 结局含「盲测比对须注」 | 在场：结局作「……史载下狱三年、系狱前后牵连较久，此年数有出入，盲测比对须注）；1936年卒于苏州」，字样逐字在盘 |
| BZ-042 | 结局含「（盲测比对时以格局大富一项为主）」 | 在场：结局尾段逐字作「（盲测比对时以格局大富一项为主）」 |
| BZ-105 | 结局含「使用时须分开统计」 | 在场：结局尾段逐字作「……盲测价值低于C04类前瞻断语，使用时须分开统计」 |
| LY-204 | 结局旧注层含「勿以此斷」 | 在场：结局逐字作「……舊注官鬼持世疾病纏綿﹐若是貴人。勿以此斷。此人原非貴人。……」 |

### 4.2 LR2-016 manifest editor_note 一处（分列层）

- 所在：manifest `_r56_lr2016_split`（case_id＝LR2-016，分列状态原样承接，`_r77_manifest_note` 明载「LR2-016 split state preserved」）。
- editor_note 本轮在盘原文逐字：「原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。」（按数据引录）——与基线全等。

### 4.3 LR2-016 评审包 editor_note 层一件（另列一类）

- 所在：R77 评审包条目 **P3-21d1866b**（经 `runs/round77/judging/host-mapping.json` 逐字对位定其 case_id 为 LR2-016；见 `packet1.json` 与 `packetA.json`，两包该条目 editor_note 同文，其 outcome_record 与 manifest cases[LR2-016] 逐字全等）。
- editor_note 本轮在盘原文与 §4.2 同字样逐字全等：「评分时该细项请按未完全复核处理」在同一 editor_note 文本内。
- anon 对位注记：本轮 anon P3-21d1866b 系 R77 种子（20261083）下编号，与 R76 轮评审包同例 anon P3-f74a20ee 分属两轮、勿混；本件以 host-mapping 结构化对位为准，不以形近推断。
- 分类：本件属评审包 editor_note 层，与 §4.2 manifest 分列层同例同字样而来源层不同，另列一类、不并入 cases 本体基线计数。

### 4.4 结论

- 基线六处（四例＋一处＋一件）本轮在盘形态逐件与基线全等，出入 0 处；无新增同型件登记。本席只登记、不改任何文本。
""")
parts.append("""
---

## 五、annotations 落盘断言（工序三）

- 底本：`data/case-annotations-r76.json` annotations 70 件（成立 12／部分成立 54／不成立 2／未核 2），全量承接、逐件原样、无删改（落盘脚本以数组全等断言验过）。
- 新增登记：**0 件**（本轮无新定案，见 §三）。
- 落盘：`data/case-annotations-r77.json` annotations **70 件＝70＋0**（成立 12／部分成立 54／不成立 2／未核 2），counts 相应更新（base 70／new_registrations_r77＝0／cases_total 70／verdicts 不变），回读 JSON 可解析断言通过。
- special_checks 承接 r76 十件并新增 R77 四件（⑪ 对勘 6/6；⑫ 无新定案＋非案例事项；⑬ 待核挂起四件本轮状态；⑭ 指令性字样基线对勘），合计 14 件。
- 待核挂起四件维持登记（承接登记，详见 r77 标注档特别核查⑬）：

| case_id | 本轮状态 |
|---|---|
| BZ-029 | 俞大维卒年待核＋旗标错配线索，维持原登记、不裁；不入 annotations |
| BZ-040 | 许世英享年待核，维持原登记、不裁；不入 annotations |
| LY-537 | 「申予日」衍字疑，维持未核原登记；本轮由盲测 S6 席（B16）作断、basis 首行对卡面 tradition 照录 liuyao，只登记触及、不裁断；以未核条目随承接在 `case-annotations-r77.json` 内 |
| YM-070 | 「甲寅旬」出处待核，维持挂起；本轮由盲测 S10 席（B24）作断，只登记触及、不裁断；以未核条目随承接在 `case-annotations-r77.json` 内 |
""")
with dest.open("w", encoding="utf-8") as f:
    for i, p in enumerate(parts):
        f.write(p); f.flush()
        data = dest.read_bytes()
        tail = dest.read_text(encoding="utf-8").rstrip().splitlines()[-1]
        print(f"part {i+1}: bytes={len(data)} tail={tail[:80]!r}")
print("FINAL", dest, dest.stat().st_size)
txt = dest.read_text(encoding="utf-8")
assert txt.count(SUG) == 1
for h in ["## 一、工序与口径","## 二、对勘","## 三、R78 承接建议汇编","## 四、指令性字样特别核查基线对勘","## 五、annotations 落盘断言"]:
    assert h in txt, h
assert "本轮无新定案承接建议" in txt
print("ADDENDUM ASSERT OK")
