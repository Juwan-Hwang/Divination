# Manifest 承接册附则（R85）——R84 定案承接对勘（平台侧空集落实／验收侧空集对勘；_r82 层 3 件第四轮对勘·仍未见落实）＋R85 定案承接建议汇编（MH/AS 立条 4 件／平台评审新定案部分成立 12 件构成 _r85 层）

## 卷首说明

- 本附则为 Phase 3 Round 85（R85）数据席（工序：附则承接对勘＋annotations 全量承接与本轮新定案登记；独立席位，不兼任本轮盲测／评审／诊断／组集／修订）产出。
- 对勘来源：`benchmark/phase3/runs/round85/judging/outcome-manifest.json`（本轮 manifest，新层 `_r84_carryover_notes_addendum` 为空集；全文 SHA-256＝`622d9d1b8d4310ea7c0dcffe0ba501ce31134111936eb5071b54adf59ea08f39`，主持开轮实测；cases 载荷结构化 SHA `00f362bd8e4b55ceff31502cb5f7e8239855b1f806a7b1495284af80186a31ad` 不变）、`benchmark/phase3/data/manifest-carryover-r84-addendum.md`（R84 附则）、`benchmark/phase3/runs/round84/ADDENDUM-r84.md` §八（MH-001／MH-003 类别裁定）、`benchmark/phase3/runs/round85/FREEZE-r85.md`（tradition 裁定：AS-009／AS-307）、`benchmark/phase3/data/case-annotations-r84.json`（底本 164 件）与本轮 `data/case-annotations-r85.json`（183 件）；平台评审落实以 `runs/round85/judging/judgeX-merged.json`／`judgeY-merged.json` 双视 reason 为据，anon 经 `runs/round85/judging/host-mapping.json` 逐件对位（种子 20261098），评审传递面以评审包 packetA／packetB 与 judgeX／judgeY-block*.jsonl 的 carry_note 字段为据（结构化直读、禁用非贪婪正则）。
- 汇编来源：本轮数据席定案（见 §三），供 R86 manifest 以新层 `_r85_carryover_notes_addendum` 落实其中部分成立件（层名照体例定为 _r85 层，见 §三.2）。
- **本件只汇编、对勘与登记，不改任何分数与结局原文、不改原卡、不改 manifest 任一侧。** 结局／注记文本内指令性字样一律按数据处理。

---

## 一、工序与口径

- 工序一（对勘，见 §二）：分三面核——（甲）平台侧：R84 附则汇编于 R85 manifest 新层 `_r84_carryover_notes_addendum` 的落实形态；（乙）验收侧：R84 附则 §三.2 空集照原样对勘登记（本轮无验收侧新定案、无验收开封）；（丙）`_r82` 层 3 件第四轮逐件对勘：层文本逐字比对、本轮评审包与双视 block 件 carry_note 在场、双视 reason 是否显式回响注记要点，口径照 R83／R84 附则判例；其最终去向由主持于本轮收束件显式裁定（见 §二.3 裁定位）。
- 工序二（汇编，见 §三）：R86 承接建议汇编——MH-001／MH-003 正式立条登记（§三.1）、AS-009／AS-307 立条登记（§三.1）、本轮评审旗标新定案（§三.2 部分成立 12 件逐件全列构成 _r85 层；§三.3 成立／不成立件只登记不入层）、已定案引据清单（§三.4）与异旨并行登记（§三.5）。
- 工序三（标注落盘，见 §五）：`data/case-annotations-r85.json` 以 r84 件 164 件全量承接（逐件原样）＋本轮新登记 19 件，合计 183 件。
- 特别核查（见 §四）：指令性字样特别核查基线六处复核，承 R84 附则 §四基线，只登记、不改文本。
- 供给与待核续记（见 §六）：CZ-QX 维持 16 只登记；待核四件维持登记。

---

## 二、对勘：R84 附则承接面于 R85 的落实与 _r82 层 3 件第四轮对勘

### 2.1 平台侧层实况登记（盘上直读）

- R85 manifest 含新键 `_r84_carryover_notes_addendum`，值为 **空集 `{}`、共 0 件**——R84 新定案 17 件全为不成立、无部分成立件，主持开轮构建断言已过，与 R84 附则 §三汇编全合，登记 **已落实（空集落实）**。
- `_r85_manifest_note` 逐字明载：「_r84_carryover_notes_addendum NEW but EMPTY -- R84 adjudication produced no partial-upheld items (17 new registrations, all not-upheld, in data/case-annotations-r84.json, counts asserted equal to R84 published distribution 12/125/25/2, total 164); the platform side is an explicitly empty set per data/manifest-carryover-r84-addendum.md s.3, and the acceptance side is empty as well.」

### 2.2 验收侧对勘登记

- R84 附则 §三.2 验收侧为 **空集**（R84 验收侧无新定案）；本轮（R85）无开封、无验收侧新定案，验收侧承接面仍为空集，照原样对勘登记，无落实件、无出入。

### 2.3 _r82 层「未见落实」3 件于 R85 传递面（逐件对勘，第四轮·仍未见落实 3）

- 层实况：R85 manifest `_r82_carryover_notes_addendum` 仍 **3 件**（LY-406／LY-446／LY-524），层文本与 `case-annotations-r84.json` 对应条 `manifest_carry_suggestion` **逐字全等 3/3**，出入 0 件。
- 评审传递面：3 件 carry_note 全数以 `[R82-addendum]` 段入 R85 评审包与双视 block 件（LY-406／LY-446／LY-524 均在 packetA／packet1 与 judgeX-block1.jsonl／judgeY-block1.jsonl，逐件结构化直读断言 3/3 在场；LY-524 carry 另含 [R65-addendum] 等段、总长 411 字）。

| # | case_id | anon_id（R85） | 评审 reason 逐字据（节录） | 结论 |
|---|---|---|---|---|
| 1 | LY-406 | P3-20b9f3cc | X：「断父母病先危后安、戌日转愈；结局果于甲戌日出空即愈，戌日正合」；Y：「父母病愈合，甲戌出空即愈与戌日主坐标合」——双视均按甲戌出空即愈之主结局评分，未见「截断／逗号」字样 | 仍未见落实 |
| 2 | LY-446 | P3-30014974 | X：「断有雨主坐标酉日；结局酉日天变、戌日而雨，雨合而落雨日晚一档」；Y：「有雨合，酉日天变与化神值日部分应，实雨在戌日故 timing 部分合」——双视均按酉日天变、戌日而雨之主结局评分，未见「截断／逗号」字样 | 仍未见落实 |
| 3 | LY-524 | P3-16c57905 | X：「断附子可用子病可愈；结局次日曰愈合愈向，惟所用药与附子对应未明、子日坐标无从核」；Y：「附子可用、子病向愈合，次日愈近子日见效坐标与旬窗」——双视均按次日愈之主结局评分，未见「截断／逗号」字样；X 所载「附子对应未明」属 R64 并行旧旨之回响、非本层注记要点 | 仍未见落实 |

- 对勘结论：**已落实 0 件**、**仍未见落实 3 件**（LY-406／LY-446／LY-524），第四轮同型延续：注记已入层、入评审包与 block 件 carry_note，但双视 reason 只按主结局常规评分、未载注记所限定之逗号收尾疑截断要点。
- 数据席建议（只建议、不代替裁定）：PREREG §0 明定 carry_note／editor_note 为登记性数据、不作量表外加减分依据——reason 不回响与该明文口径并不相悖，「未见落实」判据与评审包指令之间存在口径张力。建议主持二选一明裁：(a) 以「登记性注记不要求 reason 回响」口径澄清结案，本项自 R86 起不再滚动对勘；或 (b) 明示改立落实判据（如要求 reason 触及主结局外注记要点者须自下一轮评审派单明文写入），再照新判据对勘。
- **主持裁定位（留空，待主持于本轮收束件 REPORT／ADDENDUM-r85／STAGE-SUMMARY-70 显式裁定后回填登记）**：＿＿＿＿＿＿（裁定原文与出处由主持收束件为准，本席不预填。）

---

## 三、R86 承接建议汇编：R85 本轮新定案

- 落实键名预告：自 R86 manifest 起，平台部分成立件以 `_r85_carryover_notes_addendum` 键名落实（本附则 §三.2 逐件全列 12 件）；不成立／成立件只登记不入层；验收侧本轮无新定案。

### 3.1 MH-001／MH-003 正式立条与 AS-009／AS-307 立条登记

- **MH-001／MH-003**：类别已经 ADDENDUM-r84 §八主持裁定「不成立（旗标不成立＋措辞不精确附注）」，本轮正式立条补入 annotations（disposition＝不成立、registered_round＝85 并注明裁定轮次 84；R84 anon 对位 MH-001＝P3-90cec36f、MH-003＝P3-c177fb77）。裁定逐字：「卡面 tradition 字段确未载、另有 system＝meihua，首行只称 tradition 未标注、未提 system 字段；所自决体系（梅花）与卡面 system 值一致，无虚称卡面值，不影响断语。」
- **与 R84 附则 §三.1 表述之出入登记（只登记、不改原文）**：r84 附则 §三.1 记两件为「主持未予定案类别（非不成立、非部分成立），本席不臆造类别、不立件，只登记备查」，系 R84 数据席落笔时点之登记；ADDENDUM-r84 §八为主持其后之在后裁定，类别以 §八为准。本轮附则只在此登记该出入与准据关系，**不改 r84 附则原文**。
- **AS-009**：FREEZE-r85 裁定同型「不成立（旗标不成立＋措辞不精确附注）」（卡面 tradition＝horary，席位误称「未见 tradition 字段」后自决 horary，与卡面一致），本轮立条（registered_round＝85、裁定轮次 85；R85 anon＝P3-f8ea061f）。
- **AS-307**：FREEZE-r85 裁定同型「不成立（旗标不成立＋措辞不精确附注）」（卡面 tradition＝astrology，席位误称「未标注 tradition 字段」后按题面自决占星向，与卡面一致），本轮立条（registered_round＝85、裁定轮次 85；R85 anon＝P3-7db40262）。按：本册既有 AS-307 条为 R80 平台旗标定案（部分成立、registered_round＝80，针对 R80 本轮发生），与本轮条各轮独立、并行不悖，既有条目不动；本轮条为同例再发之第二条，annotations 总数按条目计。
- 四件共同承接注记：只登记不入层（不成立件不入 `_r85_carryover_notes_addendum`）；结局原文照录不改。

### 3.2 本轮新定案部分成立 12 件逐件全列（构成 _r85 层，自 R86 manifest 起落实）


- **AS-004**（anon P3-2731c0de）：新登记：自 R86 起承接本 R85 标注：按「结局主断面有载、系外部史实核验（结局内已自注）、时点一层未载，部分成立」登记；结局原文照录不改。
- **OC-026**（anon P3-886a859b）：新登记：自 R86 起承接本 R85 标注：按「功名实绩（授职）有载、与登科断面类型错位、同断另一人结局未载，部分成立」登记；结局原文照录不改。
- **LR3-107**（anon P3-9a3e5b3d）：新登记：自 R86 起承接本 R85 标注：按「身份与官非面有载、品性/来意断面未载，部分成立」登记；结局原文照录不改。
- **YY2-003**（anon P3-9b39d405）：新登记：自 R86 起承接本 R85 标注：按「寿终事实与月日明载、年份阙如，部分成立」登记；结局原文照录不改。
- **YM-068**（anon P3-f7692e36）：新登记：自 R86 起承接本 R85 标注：按「结局仅残句、堕井事实有载、寻回/方位面无完整记载，部分成立」登记；结局原文照录不改。
- **LY-443**（anon P3-e4daec52）：新登记：自 R86 起承接本 R85 标注：按「转晴终局有载、雪止面未明载，部分成立」登记；结局原文照录不改。
- **YM-059**（anon P3-297df262）：新登记：自 R86 起承接本 R85 标注：按「擢升终局明载、方位对应语义含混，部分成立」登记；结局原文照录不改。
- **LY-203**（anon P3-3a47bcc9）：新登记：自 R86 起承接本 R85 标注：按「结局仅单年灾害记录、终身财福面无对应记载、尺度不齐，部分成立」登记；结局原文照录不改。
- **LY-028**（anon P3-55f16c28）：新登记：自 R86 起承接本 R85 标注：按「主结局明载、「甲月」字样疑讹，部分成立」登记；结局原文照录不改。
- **LY-231**（anon P3-8890f42c）：新登记：自 R86 起承接本 R85 标注：按「终局有载、「丁艱」口径两读，部分成立」登记；结局原文照录不改。
- **LY-539**（anon P3-9b6727c3）：新登记：自 R86 起承接本 R85 标注：按「雨止终局明载、日名干支不全，部分成立」登记；结局原文照录不改。
- **LY-517**（anon P3-c50858bb）：新登记：自 R86 起承接本 R85 标注：按「成面明载、终局名敗身喪并载、成败并存，部分成立」登记；结局原文照录不改。

- _r85 层合计 **12 件**：AS-004／OC-026／LR3-107／YY2-003／YM-068／LY-443／YM-059／LY-203／LY-028／LY-231／LY-539／LY-517。各件注记文本自其 annotations 条 `manifest_carry_suggestion` 全文逐字捕获（结构化直读），R86 建包时逐件验闭合。

### 3.3 本轮新定案成立／不成立件（只登记不入层）

- 成立 2 件（重点核·同例重复对）：LY-015／LY-320——全卡对勘同日（未月甲午日）、同卦（地水師之風水渙）、逐爻全等、结局叙事几近同文，分见《增刪卜易》与《卜筮正宗》，同例跨书重复入集属实。去重**只建议不执行**：建议保留 LY-015 为正例、LY-320 标注同例重复，处置待主持裁定；本席不删卡、不改分。
- 不成立 1 件：OC-023——结局「开钟视之，乃玉绦环，果已破损」与所问两面（何物／完好与否）一一对应明载，器形材质错位属本轮断语层误差、非结局数据瑕疵。

### 3.4 已定案·引据清单（在册同旨或历轮附则已定案，只登记、不重复立条）


- LY-533：在册已定案（部分成立，registered_round＝75）。
- BQ-025：在册已定案（部分成立，registered_round＝75）。
- LR3-112：在册已定案（部分成立，registered_round＝75）。
- LY-513：在册已定案（成立，registered_round＝75）。
- LY-240：在册已定案（部分成立，registered_round＝75）。
- YY-023：在册已定案（部分成立，registered_round＝75）。
- LY-206：在册已定案（成立，registered_round＝75）。
- LY-216：在册已定案（部分成立，registered_round＝75）。
- LY-329：在册已定案（部分成立，registered_round＝79）。
- LY-504：在册已定案（部分成立，registered_round＝75）。
- LY-506：在册已定案（部分成立，registered_round＝75）。
- LY-205：在册已定案（部分成立，registered_round＝75）。
- BQ-021：在册已定案（部分成立，registered_round＝79）。
- AS-015：在册已定案（部分成立，registered_round＝75）。
- BZ-104：在册已定案（部分成立，registered_round＝79）。
- LY-524：在册已定案（部分成立，registered_round＝82）。
- LY-529：在册已定案（部分成立，registered_round＝75）。
- LY-036：在册已定案（部分成立，registered_round＝75）。
- LY-525：在册已定案（部分成立，registered_round＝79）。
- LR3-002：在册已定案（部分成立，registered_round＝79）。
- LY-628：在册已定案（部分成立，registered_round＝75）。
- LR3-101：在册已定案（部分成立，registered_round＝75）。
- LY-212：在册已定案（成立，registered_round＝75）。
- LY-105：在册已定案（部分成立，registered_round＝81）。
- LY-104：在册已定案（部分成立，registered_round＝75）。
- LY-510：在册已定案（部分成立，registered_round＝75）。
- LY-413：在册已定案（部分成立，registered_round＝79）。
- LY-259：历轮附则／承接层已定案（部分成立口径）。
- LY-516：在册已定案（部分成立，registered_round＝75）。
- LY-623：在册已定案（部分成立，registered_round＝79）。
- LY-430：在册已定案（成立，registered_round＝75）。
- LY-251：历轮附则／承接层已定案（部分成立口径）。
- LY-614：在册已定案（部分成立，registered_round＝75）。
- LY-436：在册已定案（成立，registered_round＝75）。
- LR2-023：在册已定案（部分成立，registered_round＝75）。
- BQ-001：在册已定案（部分成立，registered_round＝75）。
- LY-437：在册已定案（成立，registered_round＝75）。
- BZ-036：在册已定案（部分成立，registered_round＝76）。
- BZ-037：在册已定案（部分成立，registered_round＝76）。
- LY-220：在册已定案（部分成立，registered_round＝75）。
- AS-210：历轮附则／承接层已定案（部分成立口径）。
- LY-627：在册已定案（部分成立，registered_round＝75）。
- LY-011：在册已定案（部分成立，registered_round＝79）。
- LY-222：在册已定案（成立，registered_round＝75）。
- LY-540：在册已定案（部分成立，registered_round＝75）。
- LY-441：在册已定案（部分成立，registered_round＝75）。
- LY-629：在册已定案（部分成立，registered_round＝75）。
- LY-458：在册已定案（成立，registered_round＝75）。
- LY-508：在册已定案（成立，registered_round＝75）。
- LY-531：在册已定案（部分成立，registered_round＝75）。
- LY-207：在册已定案（部分成立，registered_round＝75）。
- LY-418：在册已定案（部分成立，registered_round＝75）。
- LY-434：在册已定案（部分成立，registered_round＝79）。
- LY-523：在册已定案（部分成立，registered_round＝79）。
- LY-411：在册已定案（部分成立，registered_round＝79）。
- LY-528：在册已定案（部分成立，registered_round＝81）。
- AS-301：历轮附则／承接层已定案（部分成立口径）。
- LY-445：在册已定案（部分成立，registered_round＝75）。
- BZ-105：在册已定案（部分成立，registered_round＝81）。
- LY-227：在册已定案（部分成立，registered_round＝75）。
- YM-030：在册已定案（部分成立，registered_round＝75）。
- LR2-022：在册已定案（部分成立，registered_round＝75）。
- BZ-304：在册已定案（部分成立，registered_round＝75）。
- YY2-004：在册已定案（部分成立，registered_round＝75）。
- LY-538：在册已定案（部分成立，registered_round＝79）。
- LY-023：在册已定案（成立，registered_round＝75）。
- OC-009：在册已定案（部分成立，registered_round＝81）。
- LY-234：历轮附则／承接层已定案（部分成立口径）。
- LY-602：在册已定案（部分成立，registered_round＝81）。
- YM-067：历轮附则／承接层已定案（部分成立口径）。
- LY-526：历轮附则／承接层已定案（部分成立口径）。
- AS-209：在册已定案（部分成立，registered_round＝79）。
- YM-043：历轮附则／承接层已定案（部分成立口径）。
- LY-103：历轮附则／承接层已定案（部分成立口径）。
- LY-255：在册已定案（部分成立，registered_round＝79）。
- LY-433：在册已定案（成立，registered_round＝75）。
- LY-429：在册已定案（不成立，registered_round＝84）。
- LY-425：在册已定案（部分成立，registered_round＝75）。

### 3.5 异旨并行登记（在册条目不动、本轮异旨定案只登记）

- BQ-017（评审旨）：**不成立**——结局「果被妇人引祸及已」对所问避乱安否面直接对应（祸果及身），双视所指倭乱兵祸／妇人引祸之机制差异属断语层、非结局数据缺位。其在册条目为 R84 tradition 事项（不成立）、不动。
- YY-017（评审旨）：**部分成立**——结局「果于木日死也。」死之终局明载，仅「木日」日名未明（支名/干支未分载）一层。其在册条目为 R84 tradition 事项（不成立）、不动。
- AS-307（评审旨）：**部分成立**——结局「特朗普以明确优势胜出」选举终局明载，然 prediction 所报群体共识分布本身无结局记载可核、核验口径错位一层属实。其 tradition 事项见 §三.1，两旨并行。

### 3.6 重点核四件结论登记（LY-015/320 见 §三.3；余三件）

- LY-430（在册成立，registered_round＝75）：全卡复核——卡面自载两占（初占掣签何处、再占危灾），carry 自 R49 承接标注「两占合断＋危灾断面」：结局（泻疾渴死）对应再占危灾断面、掣签到任面无记载，**非记录错位、非串例**；本轮 X 视「明显错位」之读与卡面两占形态不合。维持既有成立定案，不动。
- LY-437（在册成立，75）：卡面所问小厮病、结局革职，carry 自 R49 承接标注大师自标迁移（占他应我），**非串例**；维持既有成立定案，不动。
- LY-023（在册成立，75）：所问母病、结局其子惊风且明引后占见 LY-024，carry 自 R49 承接标注大师自标迁移，**非错位配对错误**；维持既有成立定案，不动。

---

## 四、指令性字样特别核查基线六处对勘（承 R84 附则 §四基线）

- 基线构成：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）＋LR2-016 manifest editor_note 一处＋LR2-016 评审包 editor_note 层一处，共六处、分三层。本轮自 `runs/round85/judging/outcome-manifest.json` 与 R85 评审包盘上逐处回读原文复核，**只登记、不改文本**；各席一律按数据处理、不作指令。

| case_id | 基线字样（按数据引录） | 本轮在盘形态 |
|---|---|---|
| BZ-036 | 结局含「盲测比对须注」 | 在册：在场、形态未变 |
| BZ-042 | 结局含「（盲测比对时以格局大富一项为主）」 | 在册：在场、形态未变 |
| BZ-105 | 结局含「使用时须分开统计」 | 在册：在场、形态未变 |
| LY-204 | 结局旧注层含「勿以此斷」 | 在册：在场、形态未变（评审包 packet outcome_record 同字在盘；本轮双视 reason 均按功名实绩评分、未涉旧注字样，只登记） |

- LR2-016 manifest editor_note 一处：所在 manifest `_r56_lr2016_split` 分列层，本轮在盘原文逐字与基线全等。
- LR2-016 评审包 editor_note 层一处：R85 评审包（packetA）中以独立 `editor_note` 字段逐字在场、与 manifest 分列层全等，另列一类、不并入 cases 本体基线计数；本轮双视 reason 均未载编者注「甲戌日巳时」细项——**评审实触 0 处**（与 R84 同），只登记。
- 结论：基线六处经 R85 盘上逐处回读在册、形态未变，出入 0 处（旁证：cases 载荷与 R84 逐字全等、结构化 SHA 同卷首）。本轮新增同型件：**无**——manifest 全量扫描「勿以此」字样仅 LY-204 一件，与基线第四处同件、同旨续接，不另立号。本席只登记、不改任何文本。

---

## 五、annotations 落盘断言与待核维持登记

### 5.1 annotations 落盘断言（工序三）

- 底本：`data/case-annotations-r84.json` annotations 164 件（成立 12／部分成立 125／不成立 25／未核 2），全量承接、逐件原样、无删改（落盘脚本以 annotations 数组前 164 件全等断言验过）。
- 新增登记：**19 件**（MH-001／MH-003／AS-009／AS-307 不成立 4 件＋评审旗标新定案 15 件：部分成立 12／成立 2／不成立 1）——落盘 `data/case-annotations-r85.json` annotations **183 件＝164＋19**（成立 14／部分成立 137／不成立 30／未核 2），各新件 `registered_round＝85`、字段完整（落盘脚本逐件断言、引文逐字断言内置），counts 相应更新，回读 JSON 可解析断言通过。
- special_checks 承接 r84 五十三件口径中之前 48 件并新增 R85 五件（㊾ R84 承接对勘；㊿ _r82 层第四轮对勘；51 平台旗标定案总登记；52 指令性字样基线六处复核；53 待核四件维持与 CZ-QX），合计 53 件。
- 异常登记一条：YY2-003 之 Y 视 reason 文本（「父果次年六月相逢，子有下落大体合；然系失散之子归、非再得子嗣，酉年坐标未应」）与本例卡面（卜自己寿命）及结局（四月癸卯日故）全不合、疑串入他例 reason，只登记；本例定案以 X 视 reason 与原卡／结局回读为准，不改任何分数，串入来源留主持核。

### 5.2 R85 确认的待核维持清单（四件，维持挂起、不核查不关闭）

| case_id | 状态登记（承 R84 附则 §五.2 口径续记） |
|---|---|
| BZ-029 | 俞大维卒年待核＋旗标错配线索，维持原登记、不裁；不入 annotations；本轮双视 reason 按主结局常规评分、无待核事项新触及 |
| BZ-040 | 许世英享年待核，维持原登记、不裁；不入 annotations；本轮双视 reason 按主结局常规评分、无新触及；本轮旗标「结局年寿与史实不合」与待核事项同件同旨、只登记关联 |
| LY-537 | 「申予日」衍字疑，维持未核原登记；本轮被双视 reason 触及（X 载「主坐标酉日与申日归仅近合」、Y 明引「原文申予日」），只登记关联、不并案、不改待核状态；以未核条目随承接在 `case-annotations-r85.json` 内 |
| YM-070 | 「甲寅旬」出处待核，维持挂起；本轮被双视 reason 触及（X／Y 均明载结局『同行都下』语义未明），与其在册未核条目同旨、只登记关联；以未核条目随承接在 `case-annotations-r85.json` 内 |

---

## 六、供给台账续记（只登记）

### 6.1 CZ-QX 维持 16

- CZ-QX 维持 **16**，承 R84 附则 §6.1 登记口径由本席承接续记，本轮无增减（旁证：R85 平台定稿 `final-scores.json` liuyao_zh n＝16；holdout29 本轮只组集封存、无测字段开封验收）。

### 6.2 待核四件维持登记（与 §五.2 同口径）

- BZ-029（俞大维卒年，另含旗标内容错配线索）、BZ-040（许世英享年）、LY-537（「申予日」衍字疑）、YM-070（「甲寅旬」挂起）四件维持登记，无盘外独立史源不裁。
