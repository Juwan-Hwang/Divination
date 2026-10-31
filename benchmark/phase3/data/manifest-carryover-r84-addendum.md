# Manifest 承接册附则（R84）——R83 定案承接对勘（平台侧空集落实／验收侧 11 件金标层登记落实；_r82 层 3 件仍未见落实）＋R84 定案承接建议汇编（平台侧 FREEZE 不成立新立 17 件／验收侧空集）

## 卷首说明

- 本附则为 Phase 3 Round 84（R84）数据席（工序：附则承接对勘＋annotations 全量承接与本轮新定案登记；独立席位，不兼任本轮盲测／评审／诊断／组集／修订／集成）产出。
- 对勘来源：`benchmark/phase3/runs/round84/judging/outcome-manifest.json`（本轮 manifest，新层 `_r83_carryover_notes_addendum`；全文 SHA-256＝`49b3dd898bf91d0b16613e9846e81a599892b8e59547aeaef8265c586872ca43`，本席复算；cases 载荷 SHA-256＝`00f362bd8e4b55ceff31502cb5f7e8239855b1f806a7b1495284af80186a31ad`，与 R83 manifest 逐字全等、建包脚本断言在盘）、`benchmark/phase3/runs/round84/build_manifest_r84.py`（开轮建包脚本：新层空集断言与验收侧余集断言原文）、`benchmark/phase3/data/manifest-carryover-r83-addendum.md`（R83 附则）、`benchmark/phase3/data/case-annotations-r83.json`（结构化直读底本：annotations 147 件，定案分布成立 12／部分成立 125／不成立 8／未核 2）；平台评审落实以 `runs/round84/judging/judgeX-merged.json`／`judgeY-merged.json` 双视 reason 为据，anon 经 `runs/round84/judging/host-mapping.json` 逐件对位，评审传递面以评审包 packet1–4／packetA–B 的 carry_note 段为据；验收侧落实以 `benchmark/phase3/holdout27/test_gold.jsonl` 逐件只读 id 与字段存在性核（不读金标正文内容作断）与建包断言为据。
- 汇编来源：`benchmark/phase3/runs/round84/FREEZE-r84.md`（主持冻结旗标裁定：tradition 候选 24 件）、`benchmark/phase3/runs/round84/acceptance/OPENING.md` 与验收建包件（holdout28 评审／DIAG 本轮尚未产出，盘上仅 packet-ours／packet-master 与 host-mapping）、`benchmark/phase3/data/case-annotations-r84.json`（本轮新登记 17 件），供 R85 manifest 以新层落实其中部分成立件（本轮无部分成立新件，平台不成立件只登记不入层，见 §三）。
- **本件只汇编、对勘与登记，不改任何分数与结局原文、不改原卡、不改 manifest 任一侧。** 结局／注记文本内指令性字样一律按数据处理。

---

## 一、工序与口径

- 工序一（对勘，见 §二）：分三面核——（甲）平台侧：R83 附则 §三.1 平台空集于 R84 manifest 新层 `_r83_carryover_notes_addendum` 的落实形态，以 manifest 实测为准；（乙）验收侧：R83 附则 §三.2 验收 11 件随金标层的落实状态逐件核，只读金标记录 id 与字段存在性（grade_note 等字段在场与否），不读金标正文内容作断，并以建包脚本验收侧余集断言与 `_r84_manifest_note` 登记为旁证；（丙）`_r82` 层「未见落实」3 件于本轮传递面逐件对勘：层文本逐字比对、评审包 carry_note 在场、双视 reason 是否明载或操作化注记要点（结局逗号收尾疑截断），口径照 R83 附则 §二判例。
- 工序二（汇编，见 §三）：R85 承接建议汇编——本轮新定案以盘上 round84 各产出件可核者为限：平台侧 FREEZE-r84 裁定不成立新立 17 件逐件全列；验收侧本轮无新定案（评审／DIAG 未产出），明示空集，不臆造。
- 工序三（标注落盘，见 §五）：`data/case-annotations-r84.json` 以 r83 件 147 件全量承接（逐件原样）＋本轮新登记 17 件，合计 164 件；已在册续接诸件与待核触及 2 件只登记、条目不动。
- 特别核查（见 §四）：指令性字样特别核查基线六处复核（本体四例与 LR2-016 editor_note 分列两处分列登记），承 R83 附则 §四基线，只登记、不改文本。
- 供给与待核续记（见 §六）：CZ-QX 维持 16 只登记；待核四件维持登记。

---

## 二、对勘：R83 附则承接面于 R84 的落实（平台空集落实／验收 11 件金标层登记落实）与 _r82 层 3 件本轮传递面（仍未见落实 3）

### 2.1 平台侧层实况登记（盘上直读）

- R84 manifest 含新键 `_r83_carryover_notes_addendum`，值为 **空集 `{}`、共 0 件**——主持开轮已落实为空集，与 R83 附则 §三.1「平台侧空集」建议全合，登记 **已落实（空集落实）**。
- `_r84_manifest_note` 逐字明载：「_r83_carryover_notes_addendum NEW but EMPTY -- R83 adjudication partial-upheld items (11, registered_round == 83 in data/case-annotations-r83.json, counts asserted equal to R83 published distribution 12/125/8/2, total 147) are all acceptance-side holdout27 cases, not dev-manifest cases; the platform side is an explicitly empty set per data/manifest-carryover-r83-addendum.md s.3.1, and the 11 acceptance-side items are carried by the gold/acceptance note layer per that addendum.」
- 平台 notes 为 `{}` 的实测旁证：11 件部分成立件（registered_round＝83）逐件核对 R84 manifest cases（487 件）成员资格，**全数非成员**（名单见 §2.2），建包脚本 `build_manifest_r84.py` 以「notes == {} 且 acceptance_side == 预期 11 件集」断言落盘。

### 2.2 验收侧 11 件随金标层的落实状态（逐件核，只读 id 与字段存在性）

- 核查面：`holdout27/test_gold.jsonl` 金标记录在盘与否、字段存在性（grade_note／editor_note）；11 件另经 `runs/round84/acceptance/judging/host-mapping.json` 复核——holdout28 验收包为 27 件新集（DS-050 起），11 件不在其中，其承接面即 holdout27 金标层本身，无平台／本轮验收评审传递面。

| # | case_id | 金标记录在盘 | grade_note 字段 | editor_note 字段 | 落实状态登记 |
|---|---|---|---|---|---|
| 1 | DS-040 | 在盘 | 存在 | — | 金标层在场，登记落实 |
| 2 | DS-048 | 在盘 | 存在 | — | 金标层在场，登记落实 |
| 3 | QM-052 | 在盘 | 存在 | 存在 | 金标层在场，登记落实 |
| 4 | QM-058 | 在盘 | 存在 | 存在 | 金标层在场，登记落实 |
| 5 | GSZ-079 | 在盘 | 存在 | — | 金标层在场，登记落实 |
| 6 | GSZ-088 | 在盘 | 存在 | — | 金标层在场，登记落实 |
| 7 | GSZ-081 | 在盘 | 存在 | — | 金标层在场，登记落实 |
| 8 | GSZ-084 | 在盘 | 存在 | — | 金标层在场，登记落实 |
| 9 | WHY-008 | 在盘 | 存在 | — | 金标层在场，登记落实 |
| 10 | WHY-009 | 在盘 | 存在 | — | 金标层在场，登记落实 |
| 11 | WHY-010 | 在盘 | 存在 | — | 金标层在场，登记落实 |

- 对勘结论（验收侧）：**11/11 金标层在场、登记落实**——R83 标注所凭的金标注记字段全数在盘未漂移，建包脚本验收侧余集断言恰为此 11 件、`_r84_manifest_note` 明载由金标／验收注记层承接。本席只核 id 与字段存在性，未读金标正文内容作断。

### 2.3 _r82 层「未见落实」3 件于 R84 传递面（逐件对勘，仍未见落实 3）

- 层实况：R84 manifest `_r82_carryover_notes_addendum` 仍 **3 件**（LY-406／LY-446／LY-524），层文本与 `case-annotations-r83.json` 对应条 `manifest_carry_suggestion`（同文亦载 R82 附则 §三）**逐字全等 3/3**，出入 0 件。
- 评审传递面：3 件 carry_note 全数以 `[R82-addendum]` 段入 R84 评审包（LY-406 packet3／packetB、LY-446 packet4／packetB、LY-524 packet1／packetA，逐件断言 3/3 在场）。

| # | case_id | anon_id（R84） | 评审 reason 逐字据（节录） | 结论 |
|---|---|---|---|---|
| 1 | LY-406 | P3-970ac2e1 | X：「父母病可愈且出空即愈与甲戌出空即愈合;主坐标丑日与甲戌日支不合,出空机理合」；Y：「父病可愈而迟与出空即愈合；丑日坐标误、实愈甲戌日」——双视均按甲戌出空即愈之主结局评分，未见「截断／逗号」字样 | 仍未见落实 |
| 2 | LY-446 | P3-f8cef3fe | X：「果酉日天变、戌日而雨，有雨合；主坐标酉日正应天变、雨落次日，近合。」；Y：「果酉日天变、戌日而雨，财化雨神雨至全合，方向断语满分；应期主坐标酉日正为天变之日、雨落次日，给1.5。」——双视均按酉日天变、戌日而雨之主结局评分，未见「截断／逗号」字样 | 仍未见落实 |
| 3 | LY-524 | P3-15490c7b | X：「次日愈合；所服附子与结局干姜汤对应未明，子日近次日」；Y：「附子对证可用、次日愈全合；子日即应与次日愈近合」——双视均按次日愈之主结局评分，未见「截断／逗号」字样；双视所载「附子对应未明」属 R64 并行旧旨、非本层注记要点 | 仍未见落实 |

- 对勘结论：**已落实 0 件**、**仍未见落实 3 件**（LY-406／LY-446／LY-524），与 R83 对勘结论同型延续：注记已入层、入评审包 carry_note，但双视 reason 只按主结局常规评分、未载注记所限定之逗号收尾疑截断要点；本席只登记事实，不改分数，是否在后续轮次强化评审口径留主持。

---

## 三、R85 承接建议汇编：R84 本轮新定案

- 落实键名预告：自 R85 manifest 起如有平台部分成立件，以 `_r84_carryover_notes_addendum` 键名落实；本轮平台新定案全为不成立（只登记不入层）与登记不作违规件，验收侧无新定案，本节汇编以登记清单形态呈上。

### 3.1 平台侧（FREEZE-r84 tradition 旗标裁定 24 件）

- 裁定总登记：候选 24 件——**不成立 22 件**（检查器模式误报）、**措辞不精确登记不作违规 2 件**（MH-001／MH-003）、claim 组候选 0 件；「无一件虚称卡面所无之值，无一件出现第二组矛盾 tradition 声明」（FREEZE-r84 冻结口径逐字）。
- 不成立 22 件处置分两路：不在册 17 件按 R80 LR3-004／LR3-104 与 R83 LY-001／ZY-001 判例**新立不成立条目入册**（逐件全列于下，只登记不入层）；已在册 5 件（BQ-025／LY-436／LY-437／YY-006／OC-029）其在册条目为其他旨、本事项与之无关、**条目不动只登记**（承 R76 OC-029 例）。

#### 新立 17 件逐件全列（disposition 均为「不成立」，registered_round＝84）

- 组 A（卡面 tradition＝六爻、首行逐字照录、仅句式未中检查器模式）——裁定逐字：「卡面有值且首行已逐字照录、仅句式未中检查器模式：……（卡面 tradition＝六爻，首行均作「卡面 tradition 字段逐字照录：六爻」）」（FREEZE-r84）：
  - BQ-017（anon P3-358fc4d0）、BQ-018（P3-01916bf9）、BQ-019（P3-242c9e63）、BQ-020（P3-96467944）、BQ-022（P3-ea04cf3b）、BQ-023（P3-159ece83）、BQ-024（P3-60668a3a）
- 组 B（卡面 tradition＝liuyao、首行明引原值、仅句式未中检查器模式）——裁定逐字：「卡面有值且首行已逐字照录、仅句式未中检查器模式：……（卡面 tradition＝liuyao，首行均明引 liuyao 原值）」（FREEZE-r84）：
  - LY-221（anon P3-6ebc98bf）、LY-421（P3-9c935969）、LY-429（P3-2363fe44）、LY-515（P3-dc7a3b29）、YY-015（P3-e4c61738）、YY-017（P3-5f453d4b）、YY-018（P3-c1f79fae）、YY-020（P3-3172aa63）
- 组 C（卡面无 tradition／system 字段、首行如实写明未载）——裁定逐字：「卡面无 tradition／system 字段且首行如实写明未载：AS-014、OC-019、OC-029（首行明写「未载／未见／无 tradition 字段」，检查器因 tradition 字样命中）」（FREEZE-r84；OC-029 已在册、条目不动，只在此逐字引录中并列）：
  - AS-014（anon P3-98ed13e8）、OC-019（P3-b66afb08）
- 17 件共同承接注记文本（原文，逐件载于各条 `manifest_carry_suggestion`）：「只登记不入层：自 R85 起承接本 R84 标注（不成立＝检查器模式误报，不入 _r84_carryover_notes_addendum 承接层）；结局原文照录不改。」
- AS-014 特别注记：本轮新立系 FREEZE-r84 tradition 事项，与 R83 附则所记 AS-014 双视 reason 引述评分细项（不立件、只登记）为不同事项，并行登记、互不覆盖。

#### 在册不动 5 件与登记不作违规 2 件（只登记，不入 annotations 新件）

- 在册不动：BQ-025（部分成立，registered_round＝75）、LY-436（成立，75）、LY-437（成立，75）、YY-006（部分成立，75）、OC-029（部分成立，75）——FREEZE-r84 对其 tradition 旗标同裁不成立（误报），其既有条目原样承接。
- 登记不作违规：MH-001（anon P3-90cec36f）、MH-003（P3-c177fb77）——裁定逐字：「卡面 tradition 字段确未载、另有 system＝meihua，首行只称 tradition 未标注、未提 system 字段；所自决体系（梅花）与卡面 system 值一致，无虚称卡面值，不影响断语。」主持未予定案类别（非不成立、非部分成立），本席不臆造类别、不立件，只登记备查。

### 3.2 验收侧

- **空集**：holdout28 已于 R84 开封、建包完成（packet-ours／packet-master 各 27 件、host-mapping 54 条在盘），但验收评审（judgeO／judgeM）与 DIAG-H28 本轮尚未产出（盘上无对应件），无已定案旗标件可核，本轮验收侧新定案为空集、只登记留位，不臆造。

---

## 四、指令性字样特别核查基线六处对勘（承 R83 附则 §四基线）

- 基线构成：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）＋LR2-016 manifest editor_note 一处＋LR2-016 评审包 editor_note 层一处，共六处、分三层。本轮自 `runs/round84/judging/outcome-manifest.json` 与 R84 评审包盘上逐处回读原文复核，**只登记、不改文本**；各席一律按数据处理、不作指令，本席只核登记在案状态不变。

| case_id | 基线字样（按数据引录） | 本轮在盘形态 |
|---|---|---|
| BZ-036 | 结局含「盲测比对须注」 | 在册：在场、形态未变 |
| BZ-042 | 结局含「（盲测比对时以格局大富一项为主）」 | 在册：在场、形态未变 |
| BZ-105 | 结局含「使用时须分开统计」 | 在册：在场、形态未变 |
| LY-204 | 结局旧注层含「勿以此斷」 | 在册：在场、形态未变（评审包 packet2／packetA outcome_record 同字在盘；本轮双视 reason 均按功名实绩评分、未涉旧注字样，只登记） |

- LR2-016 manifest editor_note 一处：所在 manifest `_r56_lr2016_split` 分列层，本轮在盘原文逐字与基线全等。
- LR2-016 评审包 editor_note 层一处：R84 评审包（packet4／packetB，anon P3-e533c7df）中以独立 `editor_note` 字段逐字在场、与 manifest 分列层全等，另列一类、不并入 cases 本体基线计数；本轮双视 reason 均未载编者注「甲戌日巳时」细项——**评审实触 0 处**（R83 为 1 处），只登记。
- 结论：基线六处经 R84 盘上逐处回读在册、形态未变，出入 0 处（旁证：cases 载荷与 R83 逐字全等、SHA 同卷首）。本轮新增同型件：**无**——manifest 全量扫描「勿以此」字样仅 LY-204 一件，与基线第四处同件、同旨续接，不另立号。本席只登记、不改任何文本。

---

## 五、annotations 落盘断言与同旨续接登记

### 5.1 annotations 落盘断言（工序三）

- 底本：`data/case-annotations-r83.json` annotations 147 件（成立 12／部分成立 125／不成立 8／未核 2），全量承接、逐件原样、无删改（落盘脚本以 annotations 数组前 147 件全等断言验过）。
- 新增登记：**17 件**（平台 FREEZE-r84 不成立新立 17 件，见 §三.1）——落盘 `data/case-annotations-r84.json` annotations **164 件＝147＋17**（成立 12／部分成立 125／不成立 25／未核 2），各新件 `registered_round＝84`、字段完整（落盘脚本逐件断言），counts 相应更新，回读 JSON 可解析断言通过。
- 平台旗标定案构成：FREEZE 候选 24 件（不成立 22 件：新立 17＋在册不动 5；措辞不精确登记不作违规 2 件 MH-001／MH-003、不立件只登记；claim 组 0 件）；cases 载荷与 R83 逐字全等，逗号收尾形态无新增；双视 reason 数据形态注记同旨续接 4 件（LY-434 成否未明字／LY-441 晴否含混／LR2-024 结局总承含混／YM-069 结局残句，均 X 视明载、已在册条目不动；Y 视本轮无同型关键词命中）。待核触及 2 件（LY-537／YM-070，见 §五.2）。本轮 R84 judging 目录内无独立 FLAGS 回传文件，平台候选以 FREEZE 裁定与双视 reason 明载形态注记为全集口径，照实登记；验收侧评审／DIAG 未产出，无验收定案（见 §三.2）。
- special_checks 承接 r83 四十四件并新增 R84 四件（㊺ R83 承接对勘；㊻ 平台旗标定案总登记；㊼ 指令性字样基线六处复核；㊽ 待核四件维持与 CZ-QX），合计 48 件。

### 5.2 R84 确认的待核维持清单（四件，维持挂起、不核查不关闭）

| case_id | 状态登记（承 R83 附则 §五.2 口径续记） |
|---|---|
| BZ-029 | 俞大维卒年待核＋旗标错配线索，维持原登记、不裁；不入 annotations；本轮双视 reason 按主结局常规评分（X 所载「子女病位等未核」属子断语未核、非卒年待核事项）、无待核事项新触及 |
| BZ-040 | 许世英享年待核，维持原登记、不裁；不入 annotations；本轮双视 reason 按主结局常规评分、无新触及 |
| LY-537 | 「申予日」衍字疑，维持未核原登记；本轮被双视 reason 触及（X 明载「申予日与酉日坐标不合且字面含混」、Y 径以结局申日归评分），只登记关联、不并案、不改待核状态；以未核条目随承接在 `case-annotations-r84.json` 内 |
| YM-070 | 「甲寅旬」出处待核，维持挂起；本轮被双视 reason 触及（X／Y 均按结局『同行』语义评分，与在册未核条目同旨），只登记关联、不改待核状态；以未核条目随承接在 `case-annotations-r84.json` 内 |

---

## 六、供给台账续记（只登记）

### 6.1 CZ-QX 维持 16

- CZ-QX 维持 **16**，承 R83 附则 §6.1 登记口径由本席承接续记，本轮无增减（旁证：R84 平台定稿 `final-scores.json` analysis_r84 families.liuyao_zh n＝16；holdout28 本集无测字段）。

### 6.2 待核四件维持登记（与 §五.2 同口径）

- BZ-029（俞大维卒年，另含旗标内容错配线索）、BZ-040（许世英享年）、LY-537（「申予日」衍字疑）、YM-070（「甲寅旬」挂起）四件维持登记，无盘外独立史源不裁。
