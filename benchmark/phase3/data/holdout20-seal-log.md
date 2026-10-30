# holdout20 封存日志（R56 建集数据席，2026-10-31）

**本集已按裁定建成、已封存（T＝25），本轮不开封。** 裁定件：`runs/round56/PREREG-ADDENDUM-1.md`（选集写死：QW-001–012、WHY-003/015/021/030/067、YJ2-012、YJ-001、YJ-004、YJ-006、CZ2-001/002/003、CZ2-006；R56 平台已先行全立，本集封存于平台判读之后，开封轮为封存后首个平台全立轮、最早 R57）。配套口径：`runs/round42/PREREG.md` §5（内容级断语扫描三道与标记集原文）、holdout19 先例（`data/holdout19-seal-log.md` 体例）。
产物：`holdout20/inputs/` 25 张输入卡；`holdout20/test_gold.jsonl` 25 行金标；构建脚本 `runs/round56/build_holdout20_r56.py`（本轮新写唯一名，内含例数/id 集/零复用/字段白名单断言）；构建报告 `runs/round56/build-holdout20-report-r56.json`。本席只建卡与封存：不作断、不评分、未开封验收、未做 git 操作。
**金标 SHA-256：`de1d72f264d19572595b55da4efdf7e36b361dc07f35474c7bc1046a0872f218`**（构建脚本 hashlib 输出与脚本外独立 `sha256sum` 实测双读一致；**待主持以独立 sha256sum 再行双读复核**，主持复核一致后方为封存定版读数）。
**回退规则未触发**：ADDENDUM-1 未设构成回退规则，本集 25 例均有登记逐字结局文本可建卡，构成维持裁定原案 T＝25，未入选库存（QW 锚点在场余 5＋partial 17、WHY 净入账余 35 等）留后续集。**但金标断语面有一项实质限度，见 §五.1——17 例 master_prediction 无逐字来源、置 null，开封前须主持补录，此项不属构成回退、属开封前置。**

## 一、构成表（裁定写死，逐源/逐体系计数）

| 来源 | 例数 | 占比 | 入选 id |
|---|---|---|---|
| 曲炜《详批命例精解》 | 12 | 48.0% | QW-001–QW-012 |
| 王虎应《六爻分类占验技法》 | 5 | 20.0% | WHY-003、WHY-015、WHY-021、WHY-030、WHY-067 |
| 《夷坚志》 | 4 | 16.0% | YJ2-012、YJ-001、YJ-004、YJ-006 |
| 《春渚紀聞》 | 4 | 16.0% | CZ2-001、CZ2-002、CZ2-003、CZ2-006 |
| 合计 | 25 | 100% | 非夷坚 21 |

| 体系（逐卡登记口径） | 例数 | 占比 |
|---|---|---|
| bazi（八字） | 12 | 48.0% |
| liuyao（六爻） | 5 | 20.0% |
| mengzhan（梦占） | 6 | 24.0% |
| fangji（方技） | 1 | 4.0% |
| xiangshu（相墓） | 1 | 4.0% |

- **体系构成口径标旗**：上表从逐卡候选登记逐字（YJ-001/YJ-004/YJ-006 登记 mengzhan、YJ2-012 登记 fangji、CZ2-001/002/003 登记 mengzhan）；ADDENDUM-1 §二体系构成行作「六爻 9（36%）、梦占 3（12%）」，与逐卡登记不一致（该行似将夷坚 4 例计入六爻）。本席不改逐卡登记、不改裁定文，差异如实标旗，提请主持知悉裁处（见 §五.2）；四限度按下述逐卡口径与裁定口径两读均合。
- 四限度复核（承 ADDENDUM §二）：(1) 例级零复用——本席脚本复核：已用并集 **926 id**（holdout2 29＝phase2/splits2.json；holdout3–19 金标仅取 id 字段 515；dev9 487＝data/master-baseline-dev9.json 键集），选例 25 id 逐 id **零命中**（只对 id 集，未打开任何已封存集金标正文做内容比对；holdout19 金标正文未开、仅取其 id）。(2) 单体系 ≤50%：bazi 48.0% 恰守内（裁定口径六爻 36% 亦守内）；单源 ≤50%：曲炜 48.0% 恰守内；非夷坚 21 ≥13；总量 25 ≥25。(3) 仅锚点在场例入选（QW/WHY 承各开采台账 anchor_presence=present 断言通过；YJ/CZ2 承 STOCK-ANCHOR-r53 在场标记与 CZ2-006 R54 γ 补证入账）。(4) 全集口径：25 例全 A 级、全 low 污染（入账口径承各开采台账与候选卡判级，脚本逐例断言通过）；登记性限度承 ADDENDUM §二：QW 为作者自选「断准」集、结局命主自报无第三方核实（选择偏倚明示，逐例载金标 grade_note）；WHY 为现代案例书、名案污染已从严定级、本集只取 low；本集无奇门例、无测字例（CZ-QX 计数维持 4、不结算）、无六壬例（冻结与 W 监测不受影响）。

## 二、逐例规格执行与成色/残损自评

输入卡字段白名单（全 25 卡断言通过）：{id, tradition, subject, context, question, setting, provenance, redistributable, license_status, anchors}；anchors 为体系锚点字段（八字：birth_info_verbatim/gender/pillars/day_master 全列；六爻：asked_at＋chart 本卦/变卦/动爻/六爻全列；梦占/方技/相墓：锚点类型与在卡位置登记，锚点本体逐字载于 context）；断语/结局/判级/污染字段一律不入输入卡、只入金标。

- QW-001–QW-012（bazi）：台账 input_fields 逐字建卡（嵌套子字段经字段映射摊平、子字段文本逐字，映射口径逐例登记于构建报告 field_mapping_notes）；四柱全列＋性别＋出生年月日时原文俱载，锚点可独立复排。成色：TXT 转录本、转录出处不明、繁简混排、个别转录误字照录（DIGEST-bazi-quwei-r56 登记）；QW-006 结局成色薄（可核事件仅职位调整/升职/肝肾病症数项）、QW-010 结局成色受限（命主未成年，可核事件仅 1998 父母离婚、2002 评上班长及幼年肺炎等少年期事项），均逐字承台账 outcome_note 载入金标 grade_note。QW-010 输入侧附条件改写见 §四。
- WHY-003/015/021/030/067（liuyao）：台账 input_fields 逐字建卡；卦盘全列（本卦/变卦/动爻/世应/六亲纳支/月建日辰），锚点在场。转录为 visual（扫描本多模态读图转录）。台账无 context/setting/provenance 独立字段：context 由 asked_at＋书名组写、setting/provenance 由台账 source 逐字承接（组写口径逐例登记于构建报告）；台账 subject 为空，卡内 subject 作「求测者（台账 subject 为空、原书未具名）」。五例均无 WHY-060 类转录置信待核注记（入选例逐例核过 pollution_note 皆为空、anchor_missing 皆为空；WHY-060 未入选本集）。
- YJ2-012（fangji）：候选卡直建（runs/round49 夷坚卡），transcription=online-verbatim；谶语断语与结局逐字完具；卡内 context 已逐字载马象锚点本体。
- YJ-001/YJ-004/YJ-006（mengzhan）：候选卡（runs/round47 夷坚卡）context 为嵌套 dict，context/question 取其 question 子字段逐字（梦象全叙即在该子字段、为锚点本体），setting 由 asked_at＋setting 子字段逐字拼接，subject/provenance 嵌套子字段摊平逐字；断语/结局逐字完具。YJ-001 结局「暨揭榜。果如妻言。」为应验式短句、候选卡判 A 附保留（结局无名次复述字面），grade_reason 逐字承接金标 grade_note。
- CZ2-001/CZ2-002/CZ2-003（mengzhan）：候选卡直建（runs/round51 春渚卡，维基文库在线文本、online-verbatim）；梦象全叙及梦中题字/告语逐字载于 context，断语/结局逐字完具。CZ2-001 输入侧附条件改写见 §四。
- CZ2-006（xiangshu）：候选卡直建（runs/round53 春渚卡）；断语逐字、结局为四代丑年登第逐项记载。锚点成色限度如实登记：主导锚点为所相先墓本身（弁山之麓、载于卡），源文未载墓地形细节，锚点成色弱于 CZ2-004（墓图），候选卡 notes 已登记、R54 γ 补证入账裁定已悉；占者佚名一节承 R53 裁定口径。CZ2-006 输入侧附条件改写见 §四。

## 三、剥离登记（输入卡卫生）

- QW 12 例：台账管理与金标侧字段（pollution、pollution_note、anchor_presence、anchor_note、dedup_check、filters、outcome_record）一律不入输入卡（逐例登记于构建报告 strip_register）。
- WHY 5 例：台账管理与金标侧字段（pollution、anchor_presence、anchor_missing、dedup_check、transcription、outcome_type、outcome_record）一律不入输入卡。
- YJ/CZ2 8 例：候选输入卡之管理字段整项剥离（YJ2-012：record_status、notes；YJ-001/004/006：record_status、notes、language；CZ2-001/002/003：无管理字段；CZ2-006：anchor_check）；金标侧字段（master_predictions、outcome、passage_full、grade_suggestion/grade_reason、contamination_suggestion/contamination_reason）一律不入输入卡。逐例剥离项见构建报告 strip_register。
- 脚本以禁用键集对 25 张输入卡全字段递归扫描，管理与断语侧字段零残留（断言通过，落盘后复扫亦零）。

## 四、内容级断语扫描（R42 PREREG §5）执行登记

标记集逐字复制 R42 PREREG §5 常量于构建脚本（LEVEL1 一级 13 项、LEVEL2 二级 9 项、字段名黑名单），脚本头注释引节号。

- **第一道（候选材料制备期）**：25 例候选材料 input_side 全字段递归扫描，命中 6 例、共 6 处；字段名黑名单零命中。逐例处置：① YJ-001/YJ-004/YJ-006 各 1 处，落在管理字段 `notes`（「结局」）——notes 整项剥离不入卡，剥离后复扫零命中；② QW-010 1 处，落在台账 input_fields.context.setting 原文嵌的成色限度句「反馈所及仅少年期事件，非一生结局，入账时如实标此限度」（二级「结局」）——附条件改写：该限度已由金标 grade_note 之 outcome_note 全文承载，输入侧删此句，改写前后对照存证于构建报告 `qw010_rewrite`；③ CZ2-001 1 处，候选卡 question 原文「此任結局如何」（二级「結局」，问句用词、非结局内容）——输入侧改写为「此任後事如何」，对照存证于构建报告 `cz2001_rewrite`，原候选卡不动；④ CZ2-006 1 处，候选卡 question 原文「主何應驗」（二级「應驗」，问句用词）——输入侧改写为「主何吉凶」，对照存证于构建报告 `cz2006_rewrite`，原候选卡不动。
- **第二道（建卡自校验）**：对 25 张输入卡全字段递归扫描（内容级一级/二级标记＋字段名黑名单），**逐卡零命中、合计 0**（逐卡结果在构建报告 scan_stage2_card_selfcheck）；落盘后对盘上文件重行复扫仍零命中。
- **第三道（主持验封）**：非本席执行——留位：主持以独立脚本对 `holdout20/inputs/` 全部输入卡复扫，零命中后于本日志追加「验封通过」与金标 SHA 主持双读结论；本日志不冒充第三道结论。

## 五、异常与提请主持知悉

1. **金标断语缺口（实质限度，开封前置）**：QW/WHY 开采台账（SUPPLY-MINING-quwei-r56.json／SUPPLY-MINING-wanghuying-r56.json）未单列断语逐字字段——QW 之 outcome_record 为断语释义与命主反馈合录（QW-002 等多例仅录反馈段、断语原文未转录入账），WHY 之 outcome_record 仅录应验情况（WHY-030/067 应验文内嵌断语要点括注、已照 outcome_record 逐字并存于金标）。本席对该 **17 例金标 master_prediction 置 null** 并逐例于 grade_note 明示，**不以结局文冒充断语、不臆补**；YJ/CZ2 8 例断语逐字完具（候选金标 statement_excerpt）。**本集在此状态下不得径行开封判读**：请主持裁定补录路径（自原书逐例补录断语逐字后重算金标 SHA 并在本日志追加补录记录，或另行裁定判读口径），补录/裁定落盘后方许开封。
2. **体系构成口径冲突（标旗）**：ADDENDUM-1 §二体系构成行（六爻 9/梦占 3）与逐卡候选登记（六爻 5/梦占 6/fangji 1）不一致，详见 §一标旗；四限度两读均合，不影响封存成立，提请主持知悉。
3. WHY 5 例 subject/context 为台账缺项下的组写（见 §三与构建报告 field_mapping_notes），非逐字原文，已逐例登记组写口径；输入判读时请知悉此成色。

## 六、封存状态与开封条件（承 ADDENDUM-1 §四）

- holdout20 自本日志落盘起封存；本轮不开封、不作任何验收预演。金标只许评审角于开封轮打开。
- 开封条件（写死）：(1) 开封轮＝封存后首个平台全立轮（最早 R57）；开封轮预注册先行（本集现无已知污染口径冲突例；§五.1 断语补录/裁定须于开封前完成并登记）。(2) 开封执行照 R56 PREREG §3：全新盲测席（方法自选/混用、每例记 systems_used；本集无奇门例、不受奇门章节接入影响）→双视评审→仲裁→E3/E4/E5 诊断。(3) 三判据照 R42 PREREG §8：全集均分＞大师、低污染配对胜多于负、低污染配对差为正（本集全 low，三判据同集判读）；达标→打包 final-skill-v2（2.0.0）＋FINAL-REPORT-v2.md 收官；未达标→标已用、诊断后续链。
- 本回传不作封存依据，以盘上文件＋主持验封（第三道扫描＋金标 SHA 双读）为准；§五.1 补录若致金标字节变动，须重算 SHA 并在本日志追加记录、原 SHA 作废留痕。

## §六 补录记录（R56 并入数据席，2026-10-31）

- **补录来源与口径**：断语逐字文本来自补录件 `runs/round56/digestion/SUPPLY-GOLD-SUPPLEMENT-r56.json`（摘要 `digestion/SUPPLY-GOLD-SUPPLEMENT-r56.md`），由 R56 补录席自原书补录——QW 12 例出曲炜《详批命例精解》（TXT 文本层逐字，transcription=verbatim）、WHY 5 例出王虎应《六爻分类占验技法》（扫描本多模态读图转录，transcription=visual）；补录席不作断、不评分。并入由本轮新写脚本 `runs/round56/merge_gold_supplement_r56.py` 执行：对 17 例（QW-001–012、WHY-003/015/021/030/067）逐例把金标 `master_prediction` 由 null 改为补录逐字文本，并在该行 `grade_note` 末尾追加补录登记句（逐例 transcription/confidence 见下表）；其余 8 例与全部其他字段（outcome_record、pollution、grade 等）一字不动。脚本断言全过：改前 17 例 master_prediction 全为 null、改后 25 例全非空、行数 25、id 集不变、outcome_record 逐行与改前哈希一致。
- **17 例逐例 transcription/confidence**：

| case_id | transcription | confidence |
|---|---|---|
| QW-001 | verbatim | 0.95 |
| QW-002 | verbatim | 0.95 |
| QW-003 | verbatim | 0.95 |
| QW-004 | verbatim | 0.95 |
| QW-005 | verbatim | 0.95 |
| QW-006 | verbatim | 0.95 |
| QW-007 | verbatim | 0.95 |
| QW-008 | verbatim | 0.95 |
| QW-009 | verbatim | 0.9 |
| QW-010 | verbatim | 0.9 |
| QW-011 | verbatim | 0.95 |
| QW-012 | verbatim | 0.95 |
| WHY-003 | visual | 0.95 |
| WHY-015 | visual | 0.95 |
| WHY-021 | visual | 0.95 |
| WHY-030 | visual | 0.88 |
| WHY-067 | visual | 0.95 |

- **金标 SHA-256 变更**：旧 SHA `de1d72f264d19572595b55da4efdf7e36b361dc07f35474c7bc1046a0872f218` → 新 SHA `763df064302a4156599985afc3224340f9cc73f953f0f8404f4cb68322586137`（并入脚本 hashlib 输出与脚本外独立 `sha256sum` 实测双读一致；旧 SHA 作废留痕）。
- **挂起两项**：(1) WHY-003 应验后回卦补解未计入断语——原书印刷 p14 页首应验后回卦补解一段（释巳时散雾起风之应期）属应验后解说，补录时未计入断语，挂起待裁。(2) WHY-030 一字置信 0.8——断语「求求懷」首字字形作「求」、连用词义存疑，该字置信约 0.8（全例 confidence=0.88），该行 grade_note 已另注此项。
- **状态变更**：「已建集、待补录」→「封存成立（待主持第三道验封＋SHA 双读定版）」。§五.1 断语补录前置至此完成；第三道验封（主持对输入卡内容级复扫）与金标 SHA 主持双读仍待主持执行，本席不冒充其结论。
- **开封条件**：承 ADDENDUM §四不变（开封轮＝封存后首个平台全立轮、最早 R57；开封执行与三判据照原条）。
