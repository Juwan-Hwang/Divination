#!/usr/bin/env python3
# R86 数据席：manifest-carryover-r86-addendum.md 生成（逐件清单自 case-annotations-r86.json 结构化直读）
import json
BASE = "/home/hatch/workspace/divination/benchmark/phase3"
d = json.load(open(f"{BASE}/data/case-annotations-r86.json"))
new = [a for a in d["annotations"] if a["registered_round"] == 86]
plat_p = [a for a in new if a["disposition"] == "部分成立" and not a["case_id"].startswith(("CYJ-", "ZW-", "DS-"))]
# acceptance partials are exactly the CYJ/ZW ones among new partials minus platform ZW none; use counts lists instead
cp = d["counts"]["new_cases_r86"]
plat_p_ids = cp["部分成立_platform"]; plat_n_ids = cp["不成立_platform"]
acc_p_ids = cp["部分成立_acceptance"]; acc_n_ids = cp["不成立_acceptance"]
by = {a["case_id"]: a for a in new}
def line(cid):
    a = by[cid]
    return f"- **{cid}**（anon {a['anon_id']}）：{a['manifest_carry_suggestion']}"
def line_n(cid):
    a = by[cid]
    return f"- **{cid}**（anon {a['anon_id']}）：{a['finding']}"

head = """# Manifest 承接册附则（R86）——R85 定案承接对勘（平台侧 12 件落实／验收侧空集对勘；_r82 层 3 件结案登记）＋R86 定案承接建议汇编（双面：平台侧 47 件／验收侧 8 件，其中部分成立 50 件构成 _r86 层）

## 卷首说明

- 本附则为 Phase 3 Round 86（R86）数据席（工序：附则承接对勘＋annotations 全量承接与本轮新定案登记；独立席位，不兼任本轮盲测／评审／诊断／组集／修订）产出。
- 对勘来源：`benchmark/phase3/runs/round86/judging/outcome-manifest.json`（本轮 manifest，新层 `_r85_carryover_notes_addendum` 12 件；全文 SHA-256＝`641703398e1f2e8496a7df1a896ac77ab41254d0f0a8c8ed0d3104d8a06f072e`，主持开轮实测；cases 载荷结构化 SHA `00f362bd8e4b55ceff31502cb5f7e8239855b1f806a7b1495284af80186a31ad` 不变）、`benchmark/phase3/data/manifest-carryover-r85-addendum.md`（R85 附则）、`benchmark/phase3/data/case-annotations-r85.json`（底本 183 件）与本轮 `data/case-annotations-r86.json`（238 件）。
- 平台侧定案来源：`benchmark/phase3/runs/round86/FREEZE-r86.md`（tradition 初检候选 0、声明组候选 0，主持裁定本轮无 tradition／CLAIM 旗标候选需逐件回读裁定）＋平台 predictions（`runs/round86/predictions/`）basis 中残损／卡面不合／多卦合卡三类留痕，逐件回原卡（`benchmark/phase3/inputs-dev12/`）与 R86 manifest 结局原文定案，anon 经 `runs/round86/judging/host-mapping.json` 逐件对位（种子 20261099）。
- 验收侧定案来源：`benchmark/phase3/runs/round86/acceptance/DIAG-H29.md` §5 旗标候选节（F1–F5）＋验收 predictions（`runs/round86/acceptance/predictions/`）basis 留痕，逐件回 holdout29 输入卡（`benchmark/phase3/holdout29/inputs/`）与金标原文（`holdout29/test_gold.jsonl`）定案，anon 经 `acceptance/judging/host-mapping.json`（ours 面）逐件对位（种子 20261100）。
- **本件只汇编、对勘与登记，不改任何分数与结局原文、不改原卡、不改 manifest 任一侧。** 结局／注记文本内指令性字样一律按数据处理。

---

## 一、工序与口径

- 工序一（对勘，见 §二）：（甲）平台侧：R85 附则汇编部分成立 12 件于 R86 manifest 新层 `_r85_carryover_notes_addendum` 的落实形态逐件验合；（乙）验收侧：R85 附则验收侧空集照原样对勘登记；（丙）`_r82` 层 3 件：已经 R85 主持裁定结案（PREREG-r86 §6①），本轮不再滚动对勘，只作在册登记。
- 工序二（汇编，见 §三／§四）：R87 承接建议汇编——平台侧新定案（§三：部分成立 45 件逐件全列构成 _r86 层平台面；不成立 2 件只登记不入层；引据与筛检分列）＋验收侧新定案（§四：部分成立 5 件逐件全列；不成立 3 件只登记）。
- 工序三（标注落盘，见 §六）：`data/case-annotations-r86.json` 以 r85 件 183 件全量承接（逐件原样）＋本轮新登记 55 件，合计 238 件。
- 特别核查（见 §五）：指令性字样特别核查基线六处复核，承 R85 附则 §四基线，只登记、不改文本。
- 供给与待核续记（见 §七）：CZ-QX 维持 16 只登记；待核四件维持登记。

---

## 二、对勘：R85 附则承接面于 R86 的落实与 _r82 层结案登记

### 2.1 平台侧层实况登记（盘上直读）

- R86 manifest 含新键 `_r85_carryover_notes_addendum`，共 **12 件**（AS-004／OC-026／LR3-107／YY2-003／YM-068／LY-443／YM-059／LY-203／LY-028／LY-231／LY-539／LY-517），与 R85 附则 §三.2 定版清单逐件全等；层注记文本与 `case-annotations-r85.json` 对应条 `manifest_carry_suggestion` 逐件捕获验合（落盘脚本结构化直读断言全过），登记 **已落实 12／12**。
- `_r86_manifest_note` 逐字明载该层派生口径（R85 部分成立∧registered_round＝85∧平台侧，验收侧空集断言已过）。

### 2.2 验收侧对勘登记

- R85 附则验收侧为 **空集**（R85 无开封、无验收侧新定案）；R86 manifest 验收侧承接面仍为空集，照原样对勘登记，无落实件、无出入。本轮验收侧新定案（holdout29 于 R86 开封）自 §四汇编、自 R87 起承接。

### 2.3 _r82 层 3 件结案登记（不再滚动对勘）

- 层实况：R86 manifest `_r82_carryover_notes_addendum` 仍 3 件（LY-406／LY-446／LY-524），层文本与在册条目原样保留。
- 结案口径：PREREG-r86 §6① 明载「_r82 层 3 件已经 R85 主持裁定结案（登记性注记不要求 reason 回响）」——R85 附则 §二.3 数据席建议 (a) 口径已经主持采纳结案。本轮照此登记结案，**不再滚动对勘**；注记在 manifest 层与 annotations 之保留只作在册登记。

---

## 三、R87 承接建议汇编（平台侧）：R86 本轮新定案

- 落实键名预告：自 R87 manifest 起，平台部分成立件以 `_r86_carryover_notes_addendum` 键名落实（本附则 §三.1 逐件全列 45 件）；不成立件只登记不入层；验收侧见 §四（落实形态承 §四卷首注记）。

### 3.1 本轮新定案部分成立 45 件逐件全列（构成 _r86 层平台面，自 R87 manifest 起落实）

"""

mid1 = """
- _r86 层平台面合计 **45 件**：""" + "／".join(plat_p_ids) + """。各件注记文本自其 annotations 条 `manifest_carry_suggestion` 全文逐字捕获（结构化直读），R87 建包时逐件验闭合。
- 定案口径统一说明：45 件均为 basis 三类留痕（残损／卡面不合／多卦合卡）经逐件回原卡核实属实、且主问终局于 R86 manifest 结局明载可核，照 LR3-116／OC-009 判例（残损已自注、结局明载可核）定部分成立；其中与在册旧旨同例者为同例新旨（输入层／卡面层新旨，与结局层或 tradition 层旧旨各旨独立、并行不悖，在册条目不动）。

### 3.2 本轮新定案不成立 2 件（只登记不入层）

"""

mid2 = """
### 3.3 已定案·引据清单（同旨已于历轮定案，只登记、不重复立条）

- LR3-116：在册已定案（部分成立，registered_round＝81；卡面三传天干未载、旬空未载残损旨），本轮 basis 同型留痕同旨。
- OC-009：在册已定案（部分成立，registered_round＝81；四柱未实际给出残损旨），本轮 basis 同型留痕同旨。
- LY-036：在册已定案（部分成立，registered_round＝75；输入卡逐爻动爻俱缺残损旨＋卡面「世爻卯木」与标准世位不合旨，R70／R71 两旨并行在册），本轮 basis 两层留痕同旨。
- LY-322：在册已定案（部分成立，registered_round＝79；卡面 yongshen 文字与装卦世应标记不合旨），本轮 basis 同型留痕同旨。
- YY2-004：在册已定案（部分成立，registered_round＝75；prediction 为残损弃断登记旨），本轮 basis 同型留痕同旨。
- AS-307：残损旨已定案（R68 旨：题面无盘面附件、输入残损已自注，见 R69 manifest 承接层）；本轮 basis 输入残损留痕与之同旨，只引据登记、不另立条（双条并行形态见 §六.2）。
- LY-430：在册已定案（成立，registered_round＝75；两占合断＋危灾断面旨），本轮 basis 两占合断留痕同旨。
- LY-506：在册已定案（部分成立，registered_round＝75；两占合载旨），本轮 basis 两占合卡留痕同旨。

### 3.4 筛检登记（逐件回卡核读后不立旗，只登记）

- 合断体例无异常留痕者：LY-001（初占存疑命再占、两卦合断为原书体例）、LY-004（一家四度占卜、后三卦相同，卡面 setting 明载体例）、LY-204（初占／再占两占分断、卡面明载）、LY-227（初占再占、结局自载再占通则）、LY-255（双占并读、卡面结构注明）、LY-416（初占／再占分列）、LY-432（两卦反应合断、取舍明记）、OC-029（一课多占为六壬通则、卡面明载成例同构）——八件 basis 均无残损／分歧／取舍困难之异常留痕，合断系卡面与大师原法体例，不立旗。
- AS-207 basis「合断斩首」系 Lilly 死法占之断法合参、非多卦合卡，误命中筛除。
- BZ-029–BZ-042（BZ-035 以外）与 BZ-104 basis「残损已计入置信」均指公历生辰／起运岁数未给一层，与 §三.2 OC-018 同为八字命例通例形态，不另立旗（BZ-035 仅以纪年不合一旨立条，见 §三.1）。
- LY-537 basis 本轮仍载逐爻表 OCR 行序同型留痕，与待核事项同件同旨、只登记关联（见 §六.3）。

---

## 四、R87 承接建议汇编（验收侧）：holdout29 本轮新定案

- 验收侧部分成立件之落实形态注记：承 R83 判例（验收侧部分成立件不入 dev manifest 承接层），本节 5 件逐件全列汇编登记，R87 manifest 侧落实形态由主持照判例裁定；annotations 侧已逐件落账（§六）。

### 4.1 本轮新定案部分成立 5 件逐件全列

"""

mid3 = """
### 4.2 本轮新定案不成立 3 件（只登记不入层）

"""

mid4 = """
### 4.3 筛检登记（验收 basis 留痕经核不立旗，只登记）

- 紫微 13 例（ZW-004–ZW-016）basis 逐例自注锚点稀疏残损（仅命宫主星／紫微落宫／四化等锚点、无出生时辰、无全盘星曜）：DIAG-H29 §0 已定性为池例设计形态——所给锚点即席位与大师共用之断据面、席位已据以产出断语、失分不在锚点缺载、不计 IN。本席照此不立旗（ZW-010／ZW-015 两件另有 F1／F2 专项留痕，已分别于 §四.2／§四.1 定案）。
- DA-025／DA-033／DA-034／DA-035／DA-037 中 DA 三例 basis「课名底本未载（不臆补）」：课名非断据锚点、盘面（四课三传天将空亡）全文在场，DIAG-H29 §3 执行面核查已登记在场，不立旗。
- CYJ 四例 basis 残损注明与 §5 F3 同件同旨，已于 §四.1 逐件定案，不重复登记。

---

## 五、指令性字样特别核查基线六处对勘（承 R85 附则 §四基线）

- 基线构成：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）＋LR2-016 manifest editor_note 一处＋LR2-016 评审包 editor_note 层一处，共六处、分三层。本轮自 `runs/round86/judging/outcome-manifest.json` 与 R86 评审包盘上逐处回读原文复核（落盘脚本逐处逐字断言全过），**只登记、不改文本**；各席一律按数据处理、不作指令。

| case_id | 基线字样（按数据引录） | 本轮在盘形态 |
|---|---|---|
| BZ-036 | 结局含「盲测比对须注」 | 在册：在场、形态未变 |
| BZ-042 | 结局含「（盲测比对时以格局大富一项为主）」 | 在册：在场、形态未变 |
| BZ-105 | 结局含「使用时须分开统计」 | 在册：在场、形态未变 |
| LY-204 | 结局旧注层含「勿以此斷」 | 在册：在场、形态未变 |

- LR2-016 manifest editor_note 一处：所在 manifest `_r56_lr2016_split` 分列层，本轮在盘原文逐字与基线全等。
- LR2-016 评审包 editor_note 层一处：R86 评审包（packetA）中以独立 `editor_note` 字段逐字在场、与 manifest 分列层全等，另列一类、不并入 cases 本体基线计数。
- 结论：基线六处经 R86 盘上逐处回读在册、形态未变，出入 0 处。本轮新增同型件：**无**。本席只登记、不改任何文本。

---

## 六、annotations 落盘断言与待核维持登记

### 6.1 annotations 落盘断言（工序三）

- 底本：`data/case-annotations-r85.json` annotations 183 件（成立 14／部分成立 137／不成立 30／未核 2），全量承接、逐件原样、无删改（落盘脚本以 annotations 数组前 183 件全等断言验过）。
- 新增登记：**55 件**（平台侧 47 件：部分成立 45／不成立 2；验收侧 8 件：部分成立 5／不成立 3）——落盘 `data/case-annotations-r86.json` annotations **238 件＝183＋55**（成立 14／部分成立 187／不成立 35／未核 2），各新件 `registered_round＝86`、字段完整（落盘脚本逐件断言、引文逐字断言内置），counts 相应更新，回读 JSON 可解析断言通过。
- special_checks 承接 r85 五十三件并新增 R86 五件（54 R85 承接对勘与 _r82 结案登记；55 平台旗标定案总登记；56 验收旗标定案总登记；57 指令性字样基线六处复核；58 待核四件维持与 CZ-QX），合计 58 件。

### 6.2 AS-307 双条并行与 LY-015／LY-320 互引登记

- **AS-307 双条并行例外形态照体例续行**：R80 部分成立条与 R85 不成立条并行保留、不合并、不以新条覆盖旧条（本轮 annotations 中 AS-307 仍恰 2 条、逐件原样承接）。本轮 AS-307 无新旗标（FREEZE-r86 tradition 候选 0）；其 basis 输入残损留痕与 R68 已定案残损旨同旨，只引据登记（§三.3）、**不另立第三条**。
- **LY-015／LY-320 同例重复登记承 R85 裁定**：两例互引形态已于 r85 annotations 落账（LY-015 条 finding 明载与 LY-320 同核、LY-320 条 finding 明载与 LY-015 条同核，去重只建议不执行、保留 LY-015 为正例之建议在案），本轮照原样承接、无需补落；FREEZE-r86 登记两例本轮各自独立作断、未参照他例，新鲜集组集排除此对不变（PREREG-r86 §4 前置核查）。

### 6.3 R86 确认的待核维持清单（四件，维持挂起、不核查不关闭）

| case_id | 状态登记（承 R85 附则 §五.2 口径续记） |
|---|---|
| BZ-029 | 俞大维卒年待核＋旗标错配线索，维持原登记、不裁；不入 annotations；本轮无待核事项新证据（basis「残损」字样为命例通例层、与待核无涉） |
| BZ-040 | 许世英享年待核，维持原登记、不裁；不入 annotations；本轮无新证据 |
| LY-537 | 「申予日」衍字疑，维持未核原登记；本轮 basis 仍载逐爻表 OCR 行序同型留痕，只登记关联、不并案、不改待核状态；以未核条目随承接在 `case-annotations-r86.json` 内 |
| YM-070 | 「甲寅旬」出处待核，维持挂起；本轮无新证据；以未核条目随承接在 `case-annotations-r86.json` 内 |

---

## 七、供给台账续记（只登记）

### 7.1 CZ-QX 维持 16

- CZ-QX 维持 **16**，承 R85 附则 §六.1 登记口径由本席承接续记，本轮无增减（旁证：holdout29 无测字例、DIAG-H29 §2 记 CZ-QX 护栏不适用／不增；平台侧无测字段新结算）。

### 7.2 待核四件维持登记（与 §六.3 同口径）

- BZ-029（俞大维卒年，另含旗标内容错配线索）、BZ-040（许世英享年）、LY-537（「申予日」衍字疑）、YM-070（「甲寅旬」挂起）四件维持登记，无盘外独立史源不裁。
"""

parts = [head]
parts += [line(c) for c in plat_p_ids]
parts.append(mid1)
parts += [line_n(c) for c in plat_n_ids]
parts.append(mid2)
parts += [line(c) for c in acc_p_ids]
parts.append(mid3)
parts += [line_n(c) for c in acc_n_ids]
parts.append(mid4)
txt = "\n".join(parts) + "\n"
with open(f"{BASE}/data/manifest-carryover-r86-addendum.md", "w", encoding="utf-8") as fh:
    fh.write(txt)
print("addendum written, chars:", len(txt))
