# holdout23 封存日志（R78 组集封存席，2026-10-31）

**本集已按附则建成、已封存（T＝27），本轮不开封。** 授权文本：`runs/round78/PREREG-ADDENDUM-r78.md`（组集封存唯一授权文本，承主预注册 `runs/round78/PREREG.md` §4/§7）。配套口径：holdout22 封存定式（`data/holdout22-seal-log.md` 体例）、`runs/round42/PREREG.md` §5（内容级断语扫描标记集）。
产物：`holdout23/inputs/` 27 张输入卡；`holdout23/test_gold.jsonl` 27 行金标（34,143 字节）；构建脚本 `runs/round78/build_holdout23_r78.py`（本轮新写唯一名，内含全部资格断言/选集规则/五要素复核/零复用/字段白名单/扫描断言；适配自 holdout22 构建脚本后已 grep 残留轮次字面量逐处查——round76/holdout22 字样仅存于「承 holdout22 先例/裁处」与台账路径（runs/round76/digestion、gsz-book-r76.txt）等实指引用，无误伤）；构建报告 `runs/round78/build-holdout23-report-r78.json`（47,483 字节）；独立复扫脚本 `runs/round78/scan_holdout23_r78.py` 与结果 `runs/round78/scan-holdout23-result-r78.json`。本席只建卡与封存：不作断、不评分、未开封验收、未做 git 操作。
**金标 SHA-256：`301d37d56c6b5fe88ad5d0f6bc022b3efba5bdbb443fee8e6cce7c7741cbe55e`**（构建脚本 hashlib 输出与脚本外独立 `sha256sum` 实测**双读一致**；待主持以独立 sha256sum 第三读复核，复核一致后方为封存定版读数）。
**泄题列单先行标出（详见 §一.1）**：挂起待主持裁处 2 件——DS-015（原书章节题「差命」含命造质量断语，未入选、DS-019 递补）、ZCB-003（承 holdout22 主持 §九.1 既有裁处，未入选、登记序递补足额）；入选标旗 5 件（DS-013/DS-014 章节分类题、ZCB-006/ZCB-007/ZCB-011 拆分过程原文内断语性短语），均照附则逐字规格入卡、原样登记提请主持复验裁处，本席未自改一字。
**跨源递补未触发**：GSZ 合格例充足（首检 6 例中 5 例合格，见 §二），无 GSZ→开悟递补，T＝27 足额。

## 一、构成表（附则 §一写定，逐源/逐体系计数）

| 来源 | 例数 | 占比 | 入选 id |
|---|---|---|---|
| 段建业《段氏理象学》 | 6 | 22.2% | DS-013、DS-014、DS-016、DS-017、DS-018、DS-019（DS-015 泄题挂起、DS-019 递补，见 §一.1） |
| 张志春《开悟之门》 | 5 | 18.5% | QM-015、QM-016、QM-018、QM-019、QM-020 |
| 刘文元《奇门启悟》 | 2 | 7.4% | QM-204、QM-205 |
| 石建国《奇门遁甲最新实例解析》 | 3 | 11.1% | QM-304、QM-305、QM-306 |
| 《字触补》（《四库未收书辑刊》陆辑第拾捌册） | 6 | 22.2% | ZCB-006、ZCB-007、ZCB-008、ZCB-009、ZCB-010、ZCB-011（ZCB-003 挂起，见 §一.1） |
| 王虎应《六爻卦例说真》 | 5 | 18.5% | GSZ-028、GSZ-030、GSZ-031、GSZ-032、GSZ-033 |
| 合计 | 27 | 100% | 非夷坚 27 |

| 体系 | 例数 | 占比 |
|---|---|---|
| qimen（奇门） | 10 | 37.0% |
| bazi（八字） | 6 | 22.2% |
| cezi（测字） | 6 | 22.2% |
| liuyao（六爻） | 5 | 18.5% |

- 构成限度逐项断言（脚本内硬断言、全过）：总量 T＝27 ≥25；单体系最大 奇门 10/27＝37.0% ≤50%；单源最大 DS／ZCB 各 6/27＝22.2% ≤50%；非夷坚 27 ≥13；非六爻 22 ≥13；多源构成（六源并存，双源以上新源条件满足）；污染 low 27/27；仅锚点在场例入选（资格断言见 §二）；与已用并集逐 id 交集＝∅（见下）。
- **例级零复用**：已用并集盘上 id 集实算 **1004 id**（dev 池＝`data/master-baseline-dev9.json` 键集 487＋inputs-dev9/10/11/12 与 inputs 目录卡 id 后 488；phase2 splits2 之 holdout2 29；holdout3–22 各 test_gold.jsonl 仅取 id 字段 592（逐集：h3 27／h4 25／h5 25／h6 23／h7 1／h8 28／h9 28／h10 29／h11 25／h12 49／h13 40／h14 40／h15 40／h16 40／h17 40／h18 30／h19 25／h20 25／h21 25／h22 27）；holdout2–22 inputs 与 *-inputs 目录卡 id 433；顶层 inputs6–10 目录卡 id 412（与上多有重合）；五源并集去重后 1004），选例 27 id 逐 id **零命中**（只对 id 集，未打开任何已封存集金标正文做内容比对；holdout22/test_gold.jsonl 亦仅取 id 列，作 ZCB 已用集准据，见 §二 ZCB 条）。逐源计数与方法登记于构建报告 `zero_reuse_recheck`。

### 一.1 泄题列单与剔除/递补登记（全程）

**挂起待主持裁处（未入选，2 件）**：

1. **DS-015（挂起）**：台账资格全过、id 未入已用并集，但其台账 source 含原书第六章章节题「差命·例五」——「差命」为对该命造质量的断语性判定，属节题含断语事实（泄题）。本席不得自行改题或动金标，挂起列单；定额按登记序递补 **DS-019**（source 章节题为「第二节三·例四」、无断语字样）。裁处选项（提请主持定）：承 holdout22 DS-011 节题中性化裁处先例，中性化该章节题后补入 DS-015 并撤 DS-019；或维持挂起定版。
2. **ZCB-003（挂起）**：台账资格全过、id 未入已用并集（holdout22 金标与 inputs 盘上实读均无此 id；封存日志构成表与诊断件编号曾载之，系 delta 换例前旧表——附则 §二.5 差异在此登记：**以金标文件为准，ZCB-003 从未实际入封 holdout22**）。但其 input_side 拆分过程锚点原文末句含结论句「故知丁艱。此斷以理也」，已经 holdout22 主持裁处（本日志同目录 `holdout22-seal-log.md` §九.1）判为断语/结局事实入卡并换例剔除。本轮承该裁处挂起，不自行改题、不动金标，是否永不再用或附条件处置由主持定；定额按登记序以 ZCB-006 起递补足 6。

**已用剔除（逐 id，同名即剔）**：DS-001–DS-012 共 12 例（DS-001/002/003 见于 holdout10 金标、DS-004–012 见于 holdout22 金标/卡）；开悟 QM-011–QM-014（holdout22）；启悟 QM-201–QM-203（holdout22）；石建国 QM-301–QM-303（holdout22）；ZCB-001/002/004/005（holdout22 金标盘上实读）；GSZ 净池 63 中已用 10 例 GSZ-003/005/009/015/016/017（holdout21）与 GSZ-022/023/024/026（holdout22）。以上均按登记序递补、无一入选。

**资格滤除（非已用、非泄题）**：DS-047（contamination medium，附则明示排除）；开悟 QM-017（stem_check 天盘未合，附则 §二.3 未全合不入选；登记序在 QM-016 与 QM-018 之间）；ZCB-016–019（contamination mid，附则明示不取，其余不合资格例未至定额不逐列）；GSZ-020（五要素动爻缺如，见 §二，换下一例）。

**入选标旗（照逐字规格入卡、提请主持复验裁处，5 件）**：

- **DS-013**：setting/provenance 承台账 source 逐字，含原书章节分类题「做功等级大的四柱」；**DS-014**：含「普通四柱」。二者为原书第六章分类学章节名（与 DS-015「差命」同章分类体系），语义为分类标签而非具体结局事实陈述；本席照逐字保留并标旗——若主持裁为同 DS-015 口径，递补序为 DS-020、DS-021（资格已预核：eligible∧present∧low∧四滤全 pass∧未用）。
- **DS-013 subject**「匿名乾造（执法部门高官）」为台账 input_side.subject 逐字（身份描述，与 holdout22 DS-004「新闻机构工作者，篇中后揭」同类），照录标旗。
- **ZCB-006**：卡面拆分过程原文含断语性短语「其必以酒溺乎」（独立复扫短片段核命中「從墓田，其必以酒溺乎」）；**ZCB-007**：含「言午為許，神已許之矣」（短片段核全句命中）；**ZCB-011**：含「子勿死，邊吉乃周字也」（即金标断语全文，片段扫描已分类登记）。三件均为台账 input_side 拆分过程原文之一部——附则 §三明定测字 input_side 逐字入卡、字形拆分过程为输入侧锚点原文，断语与拆语同源同文（与 holdout22 ZCB-001/002/004 同型、与 §一.1 ZCB-003 之别在于该例已经主持裁处在案）；本席照规格入卡并逐件标旗，主持如裁换例，递补序为 ZCB-012、ZCB-013（资格已预核）。

## 二、资格断言结果（逐例，缺一不可）

27 例逐例断言全过（脚本硬断言：任一例不过即中止建集；本轮中止零）：

- **DS-013/014/016/017/018/019**：台账（SUPPLY-MINING-duanshi-r76.json）逐例 eligible_net＝true、anchor_status＝present、contamination_pre＝low、filters 四项全 pass、master_assertion/outcome 逐字非空——6/6 过。同造合并组核验：台账同造重出 2 组已各合并为单卡（DS-011、DS-033，各为其组唯一卡），本轮入选不含该二卡，至多取 1 之限未触发；入选 6 例四柱（pillars_verbatim）互异、无同造重复。
- **QM-015/016/018/019/020（开悟）**：台账逐例 anchor_status＝present、contamination_pre＝low、separable＝true、stem_check 天盘与地盘**双 ok（全合）**、断语/结局非空——5/5 过。盘上复算：全合者 38 例、未全合 14 例（QM-017/026/033/041/050/051/053/054/056/057/059/060/061/062，承 holdout22 复算登记）；已用滤除 QM-011–014 后登记序前 5 即本轮入选。
- **QM-204/205（启悟）**：台账逐例 anchor_status＝present、contamination_pre＝low、separable＝true、断语/结局非空——2/2 过（已用滤除 QM-201–203 后登记序前 2）。
- **QM-304/305/306（石建国）**：同上四项——3/3 过。**台账注记单列（附则 §二.4）**：QM-304 注记含「分析第3条另记『张某讲98年5月结婚了』与结局『今年夏天结婚』月份表述略异（5月/夏天），并记」及断语前句为现状断之登记；QM-305 注记为断法实证登记；QM-306 注记含已事断语不计入断语字段之登记。三例均无 QM-308 型转录疑字注记（QM-308 震宫八神一字未读出，未入选，条件不触发，登记备核）。
- **ZCB-006–011**：台账逐例 eligible＝true、anchor_status＝present、contamination_pre＝low、separable＝true、断语/结局非空——6/6 过（eligible∧present∧low 共 15 例；已用 4 例与挂起 ZCB-003 剔除后登记序前 6）。
- **GSZ-028/030/031/032/033（六爻）**：台账逐例 grade＝A、pollution＝low、anchor_presence＝present、eligible_net＝true、断语/结局非空，且属可选未用池（GSZ 净入账 63 − 已用并集命中 10 ＝ 53）成员；并逐例回原书文字层（`runs/round76/gsz-book-r76.txt`）复核锚点五要素——5/5 全在场：
  - GSZ-028（第五章例四）：本卦地天泰/变卦雷天大壮；动爻 兄弟丑土动；世 兄弟辰土、应 子孙酉金；六爻全列六亲纳支；丁丑年乙巳月丁巳日（月建乙巳、日辰丁巳）——全在场。
  - GSZ-030（第五章例六）：风天小畜变水天需；动爻 兄弟卯木动；世 父母子水、应 妻财未土；六亲纳支全列；庚辰年壬午月已酉日——全在场。
  - GSZ-031（第五章例七）：泽火革变泽天夬；动爻 官鬼丑土动；世 兄弟亥水、应 子孙卯木；六亲纳支全列；戊寅年己未月己巳日己巳时——全在场。
  - GSZ-032（第五章例八）：地雷复变震为雷；动爻 兄弟丑土动；世 妻财子水、应 兄弟丑土；六亲纳支全列；戊寅年庚申月辛卯日——全在场。
  - GSZ-033（第六章例一）：风天小畜变风水涣；动爻 妻财辰土动、父母子水（世）动；世 父母子水、应 妻财未土；六亲纳支全列；丙子年壬辰月已亥日——全在场。
  - **换例登记**：登记序首例 **GSZ-020 不合格、已换下**——动爻缺如：原书第四章例五离卦六爻无动爻、变卦空（与 holdout22 同例同处置）；余四要素在场，唯动爻缺一，照附则 §二.6「缺一即换下一例」换下，依次取 GSZ-028/030/031/032/033 足 5。跨源递补（GSZ 不足→开悟递补）未触发。

## 三、逐例规格执行与剥离登记（输入卡卫生）

输入卡字段白名单（全 27 卡断言通过）：{id, tradition, subject, context, question, setting, provenance, redistributable, license_status, anchors}（键序与 holdout22 卡实读字段集一致）；脚本以禁用键集对 27 张输入卡全字段递归扫描，管理/断语/结局/master/gold/outcome/answer/判级/污染类键零残留（断言通过，落盘后复扫亦零）。provenance 全 27 卡含「用户经学校图书馆提供」、redistributable 全 false（六爻例 provenance 照其台账 source 逐字承接，内含同一提供口径）。逐例 present_basis（来源定位）即各卡 provenance：DS 6 例＝台账 source（书名＋章章节次＋印刷页/PDF页）；开悟 5 例＝台账 source（下编章章节次＋印刷页）；启悟 2 例＝台账 source（书名＋节名＋印刷页/PDF页）；石建国 3 例＝台账 source（书名＋章节＋印刷页/DjVu页）；ZCB 6 例＝《字触补》卷/叶＋合集 PDF 页；GSZ 5 例＝台账 source（书名＋章/例）。逐例剥离与字段映射全量登记于构建报告 `strip_register`／`field_mapping_notes`，体例如下：

- **DS 6 例**：anchors＝pillars 四柱全列＋pillars_verbatim＋gender（台账 input_side 逐字）；subject←input_side.subject 逐字；setting←台账 source 逐字；context/question 为组写（台账无该二字段，口径同 holdout22 并逐例登记）。剥离：anchor_status/anchor_note/contamination_*/separable/transcription/dedup/filters/eligible_net/verdict_note/composition_type/master_assertion/outcome 不入卡。本书「断准」自选偏倚承台账 contamination_note 逐例载入金标 grade_note。
- **开悟 QM 5 例**：anchors＝board_verbatim（input_side 盘面段逐字）＋stems_tianpan/stems_dipan＋stem_check；context←input_side 盘面之前段逐字；question←input_side 原文子串（脚本断言子串在场；QM-020 例外：原文未逐字引问句，question 为组写、已逐例登记）；subject 为组写（据 input_side 与 caster 组写，登记于构建报告）；setting←source＋caster 组写。剥离：topic/anchor_status/contamination_pre/separable/transcription/dedup/master_assertion/outcome 不入卡。
- **启悟 QM 2 例**：anchors＝cast_time_verbatim＋board 全载逐字；subject←querent、question/context←input_side 逐字；setting←source＋cast_time 组写。**书目处置（承 holdout22 口径）**：卡面 setting/provenance 引节名时略去篇名「分類占斷篇」（含内容级一级标记字样「占斷」、属书目信息），金标 provenance 仍载全节名，逐例登记于构建报告。剥离同 holdout22 启悟组。
- **石建国 QM 3 例**：anchors＝cast_time＋ganzhi＋chart_header＋chart 全载逐字；subject←querent、question/context←input_side 逐字；setting←source＋cast_time/ganzhi 组写；实例题（「父亲测儿子婚事」「预测找工作」「女大学生谈恋爱」）为叙事性标题、无结局事实（与 holdout22 QM-301「少收的贷款能找回」之结局型题名有别），照台账逐字保留并在此登记备核。剥离同启悟组。
- **ZCB 6 例**：anchors＝character＋split_process_verbatim（台账 input_side 逐字——字形拆分过程为附则明列之输入侧锚点原文）；context 同 input_side 逐字；subject/question 为组写（逐例登记）；setting/provenance 只载卷/叶/PDF 页定位，一律不载原书条题（条题如「死字（盧江太守未仕時）」「周字（吳某冤獄夢）」含指向，承 holdout22 中性化口径）。剥离：title/anchor_*/contamination_*/separable/eligible/cz_qx_*/dedup/transcription/master_assertion/outcome 不入卡。本轮无附条件改写（holdout22 ZCB-004 型定期断语段在本轮 6 例 input_side 中不存在）。
- **GSZ 5 例**：anchors＝asked_at＋台账 input_fields.chart 全列逐字（本卦/变卦/六爻全列）；context 由 asked_at＋书名组写、setting/provenance 由台账 source 逐字承接（承 holdout22 先例）；台账 subject 为空，卡内 subject 作「求测者（台账 subject 为空、原书未具名）」。剥离：pollution*/anchor_presence/anchor_missing/dedup_check/filters/outcome_type/outcome_record/master_prediction 不入卡。

## 四、断语扫描三道执行登记

- **第一道（构建脚本内扫描断言）**：(a) 逐字片段扫描——每例 master_prediction 与 outcome_record 的特征片段（标点分句整句（≥8 字）＋去空白 12 字滑动窗口全集）对该例输入卡全文本逐字子串扫描：**结局片段 27 例合计零命中；断语片段非测字 21 例零命中**（均脚本硬断言）；落盘后对盘上文件重行仍同。**测字 6 例**：ZCB-006/007/008/009/010 断语片段零命中；**ZCB-011 命中 1**（「子勿死，邊吉乃周字也」），逐 fragment 登记于构建报告 `cezi_hit_classification`——为台账 input_side 拆分过程锚点原文内含语（梦神告语即该例占问事件与拆法本身），已在 §一.1 标旗。(b) 内容级标记扫描（R42 PREREG §5 一级/二级标记集，脚本常量与该节逐字一致）＋字段名黑名单＋禁用键集，全字段递归——27 卡逐卡零命中、合计 0（启悟篇名命中已于建卡前按书目处置，见 §三）。
- **第二道（封存席独立复扫，交卷前执行）**：独立脚本 `runs/round78/scan_holdout23_r78.py`（不 import 构建脚本，按显式 id 清单逐件精确打开盘上卡与金标）重行标记/字段名/禁用键/白名单/片段五项——**全过：标记 0、字段名 0、禁用键 0、结局片段 0、非测字断语片段 0**，结果落 `runs/round78/scan-holdout23-result-r78.json`。该脚本附加短片段核（断语 ≥8 字连续子串在卡面出现者逐条登记、仅信息登记）：命中 4 例——ZCB-006「從墓田，其必以酒溺乎」、ZCB-007「言午為許，神已許之矣」、ZCB-009「虞去上半，下男字也」（纯拆字语）、ZCB-011「子勿死，邊吉乃周字也」；其中断语性 3 件已并入 §一.1 标旗。**语义级通读**：本席已逐卡通读全部 27 张输入卡，结论为仅含问事、背景与锚点（四柱/局式/卦象/字形拆分过程），无结局陈述、无断语正文（标旗件除外，见 §一.1）；QM-019 context「专业课已经通过」为问事前已发生之背景事实（所问为文化课考试），非所问结局，登记备核。
- **第三道（主持验封）**：非本席执行——留位：主持以独立脚本对 `holdout23/inputs/` 全部输入卡复扫（标记集承 R42 PREREG §5），零命中后于本日志追加「验封通过」与金标 SHA 主持第三读结论；本日志不冒充第三道结论。

## 五、断语逐字核验与补录登记（金标）

- **补录（台账非逐字、回原书逐字补录，1 例）**：**ZCB-006**——台账 master_assertion 作「田者墓田象也……（胡氏）其必以酒溺乎。」（19 字），以「……」省略中句、非逐字；本席回原书《字触补》卷二·外部叶14（合集 PDF560 下半）读 200dpi 渲染页图逐字补录为「田者墓田象也。胡氏肆立水傍，而從墓田，其必以酒溺乎。」（全文 24 字，标点为本席转录标点、字本体逐字），补录前后对照与出处逐例载金标 editor_note；台账 outcome「後胡氏果醉墮水死」与页图逐字合、照台账。渲染证据件：`runs/round78/zcb006-p560-r78-560.png`。
- **逐字照台账（26 例）**：DS 6 例（台账视觉转录逐字断语、filters 首滤「断语逐字可录」pass，多段以／分隔为台账摘录分隔符，逐例载金标 grade_note）；开悟 5 例、启悟 2 例、石建国 3 例（台账逐字转录、无摘写/省略标记——本席逐例检索「……」类缺口标记零命中）；ZCB-007–011（原书断语短句逐字，台账 transcription confidence 逐例载金标 grade_note）；GSZ 5 例（文字版 PDF 文字层 verbatim，断语与原书文字层对勘合）。**限度登记**：开悟 5 例本席未另读原书页图复核逐字性（与 holdout22 对 QM-011/014 之页图核有别），其金标 editor_note 已逐例载明「逐字性以台账视觉转录口径为准」，提请主持知悉；如主持要求页图复核，页位已逐例载于卡面 provenance。

## 六、验收快照登记（封存时点活 method）

- 快照目录：`runs/round78/kb-snapshot-holdout23/`（自 `benchmark/phase3/method` 全目录复制于封存时点）。**时点锚定**：本复制在本轮任何 method 集成（R78-REV1）之前完成，复制时点活 method 无本轮改动，快照即封存时点方法；验收盲测读此快照原件。
- 文件数：**21**；逐文件 SHA-256 清单：`runs/round78/kb-snapshot-holdout23-sha256.txt`（21 行），清单文件 SHA-256＝`f95fc69d9766228d2bc4043a542bd264344cf838e0e6e6c1e807974621c2d57c`；本席已以 `sha256sum -c` 对清单全量复验，21/21 OK。
- 与 R78 开轮快照（`runs/round78/kb-snapshot/`）差异自核：**零差异**（21 件哈希全同——本轮开轮后、封存前活 method 无改动，与 PREREG §3「封存先于集成」顺序一致）。

## 七、封存状态与开封条件（承附则与 PREREG §2，写死）

- holdout23 自本日志落盘起封存；本轮不开封、不作任何验收预演。金标只许评审角于开封轮打开。
- **开封条件（写死）：封存后首个平台全立轮当轮开封（最早 R79）**。开封前主持复验：金标 SHA-256 与本日志定版全文对勘（三读）、输入卡 27 张在盘逐件、主持第三道复扫零命中，结论追记本日志、不另立新档。验收盲测读封存时点快照（§六）；三判据照 R42 PREREG §8（我方均分＞大师均分；低污染子集配对胜多于负；低污染子集配对差＞0；本集全 low，低污染子集＝全集，仍分开登记表述）。
- 本回传不作封存依据，以盘上文件＋主持验封（第三道扫描＋金标 SHA 三读）为准；金标字节若有任何后续变动，须重算 SHA 并在本日志追加记录、原 SHA 作废留痕。
- 中间件登记：ZCB-006 补录渲染件 `runs/round78/zcb006-p560-r78-560.png` 留 runs/round78/ 内备查；GSZ 五要素复核用原书文字层 `runs/round76/gsz-book-r76.txt` 为既有件、本轮只读。

## 八、主持裁处（R78 主持裁处执行席，2026-10-31）

本节为封存后主持裁处之执行登记，以 append 追加，原 §一–§七一字未动。执行脚本 `runs/round78/amend_holdout23_r78.py`、登记件 `runs/round78/amend-holdout23-register-r78.json`。前置核验：动手前金标 SHA-256 实测 `301d37d56c6b5fe88ad5d0f6bc022b3efba5bdbb443fee8e6cce7c7741cbe55e`，与封存日志 §首定版读数及主持给定值一致；快照 `kb-snapshot-holdout23` 未动。本席只执行裁处：不作断、不评分、未开封验收、未做 git 操作。

### 八.1 五项裁处执行

1. **DS-013 节题中性化——已执行**（逐字对照见 §八.2）。`holdout23/inputs/DS-013.json` 的 setting 与 provenance 各 1 处（全卡共 2 处），删原书第六章小节题全文「做功等级大的四柱」（连同其前「、」），定位只留「第六章第一节二」与「例六」，其余字串一字不动（承 holdout22 §九.4 DS-011 体例）；subject「匿名乾造（执法部门高官）」照裁处不动。金标 DS-013 行一字未动（未动行逐行字节无损自检通过）。
2. **DS-014 节题中性化——已执行**（逐字对照见 §八.2）。同法删节题全文「普通四柱」（连同其前「、」），setting 与 provenance 各 1 处，定位只留「第六章第一节二」与「例五」；金标 DS-014 行一字未动。
3. **DS-015 中性化补入、DS-019 退出——已执行**。按台账 `runs/round76/digestion/SUPPLY-MINING-duanshi-r76.json` 之 DS-015 记录逐字、承 `build_holdout23_r78.py` DS 建卡规格建卡（字段白名单与键序同现 DS 各卡；subject←input_side.subject 逐字；anchors←input_side pillars/pillars_verbatim/gender 逐字；context/question 组写口径同现 DS 各卡）与金标行（master_prediction/outcome_record 自台账 master_assertion/outcome 逐字取录）。节题「差命」在卡面出现处共 2 处——setting 1 处、provenance 1 处（均承台账 source），逐处全文删除（连同其前「、」）、只留章节定位「第六章第一节二」与「例五」（逐字对照见 §八.2）；卡面其余字段经逐字段检索无该题字串，中性化后全卡「差命」子串零残留。**金标侧 provenance 照台账原登记、不中性化**（含「差命」原样，承 holdout22 §九.1「金标侧 provenance 照原登记」口径）。同步精确删除 DS-019 输入卡文件（精确路径 `holdout23/inputs/DS-019.json`，非通配删除）与金标 DS-019 行；金标行序照 id 序重整（27 行，未动 26 行原始行文逐字无损、仅行序与一删一增）。DS-015 资格复断言全过（eligible_net＝true、anchor_status＝present、contamination_pre＝low、filters 四项全 pass、断语/结局逐字非空）。
4. **ZCB-006／ZCB-007／ZCB-011 照建不动、标旗维持——已登记**。三卡与对应金标行一字未动（在未动行字节无损自检范围内）。裁处理由（主持原文，原样记入）：「拆分过程原文系附则明列之输入侧锚点载荷，与 holdout22 ZCB 四例同口径；ZCB-011 语出梦中神告、属叙事内谶语即待释之占象本身；ZCB-003 之排除系其已有专门裁处在案，与此三件情形有别。」
5. **本节即裁处第 5 项之执行**：1–4 项全文要点、逐处改前/改后逐字对照（§八.2）、构成全表更新（§八.3）、DS-015 零复用复核结论（§八.3）均已落本节。

### 八.2 逐处改动逐字对照（改前／改后）

**DS-013（inputs/DS-013.json，setting 与 provenance 各 1 处）**

- setting 改前：「《段氏理象学》（段建业著，中国商业出版社2011年12月第1版，ISBN 978-7-5044-7457-5）·第六章第一节二、做功等级大的四柱·例六（印刷p.88／PDF112）」
- setting 改后：「《段氏理象学》（段建业著，中国商业出版社2011年12月第1版，ISBN 978-7-5044-7457-5）·第六章第一节二·例六（印刷p.88／PDF112）」
- provenance 改前：「《段氏理象学》（段建业著，中国商业出版社2011年12月第1版，ISBN 978-7-5044-7457-5）·第六章第一节二、做功等级大的四柱·例六（印刷p.88／PDF112）；底本为用户经学校图书馆提供，redistributable=false」
- provenance 改后：「《段氏理象学》（段建业著，中国商业出版社2011年12月第1版，ISBN 978-7-5044-7457-5）·第六章第一节二·例六（印刷p.88／PDF112）；底本为用户经学校图书馆提供，redistributable=false」

**DS-014（inputs/DS-014.json，setting 与 provenance 各 1 处）**

- setting 改前：「《段氏理象学》（段建业著，中国商业出版社2011年12月第1版，ISBN 978-7-5044-7457-5）·第六章第一节二、普通四柱·例五（印刷p.91／PDF115）」
- setting 改后：「《段氏理象学》（段建业著，中国商业出版社2011年12月第1版，ISBN 978-7-5044-7457-5）·第六章第一节二·例五（印刷p.91／PDF115）」
- provenance 改前：「《段氏理象学》（段建业著，中国商业出版社2011年12月第1版，ISBN 978-7-5044-7457-5）·第六章第一节二、普通四柱·例五（印刷p.91／PDF115）；底本为用户经学校图书馆提供，redistributable=false」
- provenance 改后：「《段氏理象学》（段建业著，中国商业出版社2011年12月第1版，ISBN 978-7-5044-7457-5）·第六章第一节二·例五（印刷p.91／PDF115）；底本为用户经学校图书馆提供，redistributable=false」

**DS-015（新建卡 inputs/DS-015.json；改前＝承台账 source 逐字之未中性化串，改后＝卡面实值）**

- 台账 source 原文（金标侧 provenance 据此原登记、不中性化）：「《段氏理象学》（段建业著，中国商业出版社2011年12月第1版，ISBN 978-7-5044-7457-5）·第六章第一节二、差命·例五（印刷p.92／PDF116）」
- setting 改前（未中性化）：「《段氏理象学》（段建业著，中国商业出版社2011年12月第1版，ISBN 978-7-5044-7457-5）·第六章第一节二、差命·例五（印刷p.92／PDF116）」
- setting 改后：「《段氏理象学》（段建业著，中国商业出版社2011年12月第1版，ISBN 978-7-5044-7457-5）·第六章第一节二·例五（印刷p.92／PDF116）」
- provenance 改前（未中性化）：「《段氏理象学》（段建业著，中国商业出版社2011年12月第1版，ISBN 978-7-5044-7457-5）·第六章第一节二、差命·例五（印刷p.92／PDF116）；底本为用户经学校图书馆提供，redistributable=false」
- provenance 改后：「《段氏理象学》（段建业著，中国商业出版社2011年12月第1版，ISBN 978-7-5044-7457-5）·第六章第一节二·例五（印刷p.92／PDF116）；底本为用户经学校图书馆提供，redistributable=false」
- 金标 DS-015 行 provenance（照台账原登记、不中性化）：「《段氏理象学》（段建业著，中国商业出版社2011年12月第1版，ISBN 978-7-5044-7457-5）·第六章第一节二、差命·例五（印刷p.92／PDF116）；底本为用户经学校图书馆提供，redistributable=false」

**DS-019（退出）**

- 输入卡：`holdout23/inputs/DS-019.json` 已以精确路径删除（脚本内 os.remove 精确路径操作，删后存在性断言为不存在）。
- 金标行：`holdout23/test_gold.jsonl` 中 DS-019 行已精确删除；DS-019 自本节起退出本集，§一构成表 DS 行以 §八.3 更新表为准。

### 八.3 构成全表更新与复断言

| 来源 | 例数 | 占比 | 入选 id |
|---|---|---|---|
| 段建业《段氏理象学》 | 6 | 22.2% | DS-013、DS-014、DS-015、DS-016、DS-017、DS-018 |
| 张志春《开悟之门》 | 5 | 18.5% | QM-015、QM-016、QM-018、QM-019、QM-020 |
| 刘文元《奇门启悟》 | 2 | 7.4% | QM-204、QM-205 |
| 石建国《奇门遁甲最新实例解析》 | 3 | 11.1% | QM-304、QM-305、QM-306 |
| 《字触补》（《四库未收书辑刊》陆辑第拾捌册） | 6 | 22.2% | ZCB-006、ZCB-007、ZCB-008、ZCB-009、ZCB-010、ZCB-011 |
| 王虎应《六爻卦例说真》 | 5 | 18.5% | GSZ-028、GSZ-030、GSZ-031、GSZ-032、GSZ-033 |
| 合计 | 27 | 100% | 非夷坚 27 |

| 体系 | 例数 | 占比 |
|---|---|---|
| qimen（奇门） | 10 | 37.0% |
| bazi（八字） | 6 | 22.2% |
| cezi（测字） | 6 | 22.2% |
| liuyao（六爻） | 5 | 18.5% |

- 构成限度复断言（脚本内硬断言、全过）：总量 T＝27 ≥25；单体系最大 奇门 10/27＝37.0% ≤50%；单源最大 DS／ZCB 各 6/27＝22.2% ≤50%；非夷坚 27 ≥13；非六爻 22 ≥13；多源构成（六源并存）；污染 low 27/27。
- **DS-015 零复用复核结论**：已用并集按封存日志 §一口径盘上逐 id 复算＝**1004 id**（dev 池＝data/master-baseline-dev9.json 键集＋inputs-dev9/10/11/12 与 inputs 目录卡 id；phase2 splits2 之 holdout2；holdout3–22 各 test_gold.jsonl 仅取 id 字段；holdout2–22 inputs 与 *-inputs 目录卡 id；顶层 inputs6–10 目录卡 id；五源并集去重），DS-015 逐 id **零命中**（预期一致：台账登记序中 DS-015 本在 DS-019 之前、原挂起仅因节题）。本轮选集 27 id 与已用并集交集＝∅。

### 八.4 改后复验登记（本席执行）

- **变更卡逐卡复扫（DS-013／DS-014／DS-015，盘上文件重行）**：断语片段逐字子串扫描（对该例 master_prediction 特征片段：标点分句整句 ≥8 字＋去空白 12 字滑动窗口）零命中；结局片段（outcome_record 同法）零命中；内容级标记扫描（标记集承 runs/round42/PREREG.md §5 一级/二级）零命中；字段名黑名单零命中；禁用键递归扫描零命中；字段白名单与键序核通过——三卡全过。
- **全集 27 卡复扫（第二道口径，本席独立实现重行）**：标记命中 0、字段名命中 0、禁用键命中 0、结局片段命中 0、非测字断语片段命中 0、字段白名单/键序不合 0 卡；测字断语片段命中仅既知一件（ZCB-011：子勿死，邊吉乃周字也），系 §八.1 第 4 项裁处照建不动之锚点原文内含语（封存日志 §四已分类登记），非新增命中。全集复扫结论：零新增命中、通过。
- **新金标 SHA-256（双读）**：脚本 hashlib 读数 `b31afb4e59da75e89be5353d9405554cd3b449563a84b42e76b29ad4fbab60ad`；脚本内 sha256sum 子进程读数 `b31afb4e59da75e89be5353d9405554cd3b449563a84b42e76b29ad4fbab60ad`；两读一致，成立。金标 34272 字节、27 行、行序照 id 序。原 SHA `301d37d56c6b5fe88ad5d0f6bc022b3efba5bdbb443fee8e6cce7c7741cbe55e` 自本节落盘起作废留痕（承 §七口径）；封存定版以主持第三读复核为准。开封条件不变（§七写死口径不改）。

## §九 开封验封结论（R79，平台全立当轮开封）

R79 平台三项全立（(a) −1.063／(b) 四护栏全立／(c) −1.634，熔断未触；全立计数 26），照 R79 PREREG §2 与本日志 §八.5 写死条件当轮开封。前置复验三项全过：① 金标 SHA-256 主持独立 sha256sum 复测＝b31afb4e59da75e89be5353d9405554cd3b449563a84b42e76b29ad4fbab60ad，与 §八.4 定版逐字全等；② 输入卡 27 张逐件在盘、构成与 §八.3 更新表一致；③ 主持第三道复扫（runs/round79/acceptance_rescan_h23_host_r79.py，标记集承 R42 PREREG §5）零命中（承 §四第三道留位）。开封执行记录见 runs/round79/acceptance/OPENING.md；验收结论另记 runs/round79/acceptance/REPORT.md 并于本日志续记标已用（未达标时）或收官（达标时）。
