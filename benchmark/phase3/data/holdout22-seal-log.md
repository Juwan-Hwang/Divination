# holdout22 封存日志（R76 组集封存席，2026-10-31）

**本集已按附则建成、已封存（T＝27），本轮不开封。** 授权文本：`runs/round76/PREREG-ADDENDUM-r76.md` §三（组集写定，本任务唯一授权文本）。配套口径：holdout21 封存定式（`data/holdout21-seal-log.md` 体例与检查清单）、holdout20 封存日志（附条件改写与补录先例）、`runs/round42/PREREG.md` §5（内容级断语扫描标记集）。
产物：`holdout22/inputs/` 27 张输入卡；`holdout22/test_gold.jsonl` 27 行金标；构建脚本 `runs/round76/build_holdout22_r76.py`（本轮新写唯一名，内含全部资格断言/选集规则/五要素复核/三键对勘/零复用/字段白名单/扫描断言）；构建报告 `runs/round76/build-holdout22-report-r76.json`。本席只建卡与封存：不作断、不评分、未开封验收、未做 git 操作。
**金标 SHA-256：`1e299bdaf10724bf2ba66d1f4933fdcbeee11b5970f978df975872bb7164ae6a`**（构建脚本 hashlib 输出与脚本外独立 `sha256sum` 实测双读一致；**待主持以独立 sha256sum 再行复核**，主持复核一致后方为封存定版读数）。
**偏离登记（先行标出，详见 §一.1 与 §二）**：附则 §一「新 id 命名空间（DS-／QM-011 起／ZCB-）与已用并集 1052 按 id 零复用为构造性成立」对 **DS 号段经盘上实测证伪**——holdout10 金标已有 DS-001/DS-002/DS-003（任铁樵《滴天髓阐微》例，与本批段氏例同名异例）。本席以 §三构成限度「与已用 1052 id 零复用」（硬限）为准，对该 3 id 逐 id 剔除、按登记序递补 DS-010/DS-011/DS-012，DS 仍取 9 例、T 仍 27。此为对规则 1 字面「前 9」的唯一偏离，提请主持知悉裁处。
**回退规则未触发**：六爻合格例充足（首检 5 例中 4 例合格，见 §二），无 QM→DS 递补，T＝27 足额。

## 一、构成表（附则 §三写定，逐源/逐体系计数）

| 来源 | 例数 | 占比 | 入选 id |
|---|---|---|---|
| 段建业《段氏理象学》 | 9 | 33.3% | DS-004、DS-005、DS-006、DS-007、DS-008、DS-009、DS-010、DS-011、DS-012（DS-001–003 经零复用剔除递补，见 §一.1） |
| 张志春《开悟之门》 | 4 | 14.8% | QM-011、QM-012、QM-013、QM-014 |
| 刘文元《奇门启悟》 | 3 | 11.1% | QM-201、QM-202、QM-203 |
| 石建国《奇门遁甲最新实例解析》 | 3 | 11.1% | QM-301、QM-302、QM-303 |
| 《字触补》（《四库未收书辑刊》陆辑第拾捌册） | 4 | 14.8% | ZCB-001、ZCB-002、ZCB-003、ZCB-004 |
| 王虎应《六爻卦例说真》 | 4 | 14.8% | GSZ-022、GSZ-023、GSZ-024、GSZ-026 |
| 合计 | 27 | 100% | 非夷坚 27 |

| 体系 | 例数 | 占比 |
|---|---|---|
| qimen（奇门） | 10 | 37.0% |
| bazi（八字） | 9 | 33.3% |
| cezi（测字） | 4 | 14.8% |
| liuyao（六爻） | 4 | 14.8% |

- 构成限度逐项核验（承附则 §三）：单体系最大 奇门 10/27＝37.0% ≤50%；单源最大 段氏一书 9/27＝33.3% ≤50%；非六爻 23 ≥13；非夷坚 27 ≥13；仅锚点在场（资格断言见 §二）；与已用 id 零复用（见下）。
- **例级零复用**：本席脚本复核——已用并集盘上 id 集实算 **977 id**（phase2 splits2 之 holdout2 29；holdout3–20 各 test_gold.jsonl 仅取 id 字段 540；holdout21 金标 id 25；holdout2–21 inputs 与 *-inputs 目录卡 id 406；dev 池＝data/master-baseline-dev9.json 键集＋inputs-dev9/10/11/12 与 inputs 目录卡 id 488；五源并集去重后 977），选例 27 id 逐 id **零命中**（只对 id 集，未打开任何已封存集金标正文做内容比对；holdout10 仅取其 id 与例目字段定位 DS 撞号，未作内容比对）。与承 R59 定案加法口径 1052（dev 487＋holdout2–20 540＋holdout21 25，跨源未去重）的关系：两口径计数方法不同（去重/未去重），零复用以逐 id 对实算并集零命中为准。逐源计数与方法登记于构建报告 `zero_reuse_recheck`。

### 一.1 DS 撞号剔除与递补登记（偏离规则 1 字面，提请主持裁处）

- 事实：`holdout10/test_gold.jsonl` 载 DS-001（滴天髓阐微·卷一通神论·知命章，王姓男子例）、DS-002（干支总论例）、DS-003（卷四六亲论·岁运章，生员例），与段氏台账 DS-001–003（序言门人断例/理法例）同名异例、内容互不相涉。段氏台账 dedup 以四柱 8 字连写对勘（内容层），未以 id 对已用并集，故未检出此撞号；附则 §一据此误判 DS 号段构造性零复用。
- 处置：DS 候选（eligible∧present∧low 共 62 例）先逐 id 对已用并集滤已用，剔除 DS-001/DS-002/DS-003，按 DIGEST 登记序取未用前 9＝DS-004–DS-012。构成（八字 9）、T＝27、四限度均不变。
- 同造合并组（DS-011/DS-033）核验：递补后 DS-011 入选、DS-033 未取，至多取 1 之限守合。
- DS-047（medium）不在候选（污染滤先行），排除规则守合（与撞号无关）。

## 二、资格断言结果（逐例，缺一不可）

27 例逐例断言全过（脚本断言：任一例不过即中止建集；本轮中止零、构成替补仅 §一.1 之 id 递补）：

- **DS-004–012**：台账（SUPPLY-MINING-duanshi-r76.json）逐例 eligible_net＝true、anchor_status＝present、contamination_pre＝low、filters 四项全 pass、master_assertion/outcome 逐字非空——9／9 过（原 DS-001–003 资格本身亦过，剔除仅因 id 撞号，见 §一.1）。
- **QM-011–014（开悟）**：台账逐例 anchor_status＝present、contamination_pre＝low、separable＝true、stem_check 天地盘双 ok、断语/结局非空——4／4 过。**盘上复算注记**：stem_check 天地盘全合者实算 **38 例**（未全合 14 例：QM-017/026/033/041/050/051/053/054/056/057/059/060/061/062），与附则 §一「42／10」差 4；登记序前 4（QM-011–014）两读一致、选集不受影响，差异如实登记待主持知悉。
- **QM-201–203（启悟）**：台账逐例 anchor_status＝present、contamination_pre＝low、separable＝true、断语/结局非空——3／3 过（登记序前 3）。
- **QM-301–303（石建国）**：同上四项——3／3 过（登记序前 3）。**QM-308 注记条件未触发**：QM-308（震宫八神一字未读出）不在前 3、未入选，附则「如入选须单列注记」之条件不成立，此处登记备核。
- **ZCB-001–004**：台账逐例 eligible＝true、anchor_status＝present、contamination_pre＝low、separable＝true、断语/结局非空——4／4 过（eligible∧present∧low 共 15 例中登记序前 4；mid 之 ZCB-016–019 不取，守规则 4）。
- **GSZ-022/023/024/026（六爻）**：台账逐例 grade＝A、pollution＝low、anchor_presence＝present、eligible_net＝true、断语/结局非空，且逐 id 属可选未用池（GSZ 净入账 63 − holdout21 用 6 ＝ 57）成员；并逐例回原书（《六爻卦例说真》文字版 PDF，pdftotext 文字层提取件 `runs/round76/gsz-book-r76.txt`）复核锚点五要素——4／4 全在场：
  - GSZ-022（第四章例七）：本卦风水涣/变卦天水讼；动爻 子孙未土动；世 兄弟巳火、应 子孙辰土；六爻全列六亲纳支；丁丑年甲申月乙未日（月建甲申、日辰乙未）——全在场。
  - GSZ-023（第四章例八）：雷泽归妹变地泽临；动爻 官鬼午火动；应 父母戌土、世 父母丑土；六亲纳支全列；丁丑年丙午月辛丑日——全在场。
  - GSZ-024（第四章例九）：泽地萃变火地晋；动爻 父母未土/兄弟酉金两动；应 兄弟酉金、世 官鬼巳火；六亲纳支全列；丁丑年丙午月己亥日——全在场。
  - GSZ-026（第五章例二）：天雷无妄变风水涣；动爻 子孙午火/兄弟寅木/父母子水；世 子孙午火、应 父母子水；六亲纳支全列；丙子年丙申月壬午日——全在场。
  - **换例登记**：登记序首例 **GSZ-020 不合格、已换下**——动爻缺如：原书第四章例五离卦六爻无动爻、变卦空，原书自注「为什么没断死，就因为内因无动爻来克世」；余四要素在场，唯动爻缺一，照规则 6「缺一即换下一例」换下，依次取 GSZ-022/023/024/026 足 4。合格足额，QM→DS 递补回退未触发。

## 三、逐例规格执行与剥离登记（输入卡卫生）

输入卡字段白名单（全 27 卡断言通过）：{id, tradition, subject, context, question, setting, provenance, redistributable, license_status, anchors}；脚本以禁用键集对 27 张输入卡全字段递归扫描，管理与断语/结局/判级/污染字段零残留（断言通过，落盘后复扫亦零）。provenance 全 27 卡含「用户经学校图书馆提供」、redistributable 全 false（六爻例 provenance 照其台账 source 逐字承接，内含同一提供口径）。

- **DS 9 例**：anchors＝pillars 四柱全列＋pillars_verbatim＋gender（台账 input_side 逐字）；subject←input_side.subject 逐字；setting←台账 source 逐字；context/question 为组写（台账无该二字段：context 作「《段氏理象学》命例（类型）；四柱载于 anchors」、question 作「就此四柱命造求测（原书命例体例，无独立问句原文载录）」，组写口径逐例登记于构建报告）。剥离：anchor_status/anchor_note/contamination_*/separable/transcription/dedup/filters/eligible_net/verdict_note/composition_type/master_assertion/outcome 不入卡。本书为从业者自选案例集、「断准」选择偏倚承台账 contamination_note 逐例载入金标 grade_note。
- **开悟 QM 4 例**：anchors＝board_verbatim（input_side 盘面段逐字）＋stems_tianpan/stems_dipan＋stem_check；context←input_side 盘面之前段逐字；question←input_side 原文子串（脚本断言子串在场）；subject 为组写（据 input_side 与 caster 组写，口径登记于构建报告）；setting←source＋caster 组写。剥离：topic/anchor_status/contamination_pre/separable/transcription/dedup/master_assertion/outcome 不入卡。
- **启悟 QM 3 例**：anchors＝cast_time_verbatim＋board/boards 全载逐字（局式逐字：header_verbatim＋九宫 palaces＋center_palace_5；QM-203 双局并载）；subject←querent、question/context←input_side 逐字；setting←source＋cast_time 组写。剥离：anchor_status/contamination_*/separable/transcription*/dedup/notes/master_assertion/outcome 不入卡。**一处书目处置**：卡面 setting/provenance 引节名时略去篇名「分類占斷篇」（该篇名含内容级一级标记字样「占斷」、属书目信息而非断语内容，承 h20 第一道命中处置口径）；金标 provenance 仍载全节名，处置逐例登记于构建报告 field_mapping_notes。
- **石建国 QM 3 例**：anchors＝cast_time＋ganzhi＋chart_header＋chart 全载逐字；subject←querent、question/context←input_side 逐字；setting←source＋cast_time/ganzhi 组写。剥离同启悟组。
- **ZCB 4 例**：anchors＝character＋split_process_verbatim（台账 input_side 逐字——字形拆分过程为附则 §三明列之输入侧锚点原文）；context 同 input_side 逐字；subject/question 为组写（口径登记于构建报告；ZCB-002 question 为 input_side 原文句）；**题面定位中性化**：setting/provenance 只载卷/叶/PDF 页定位，一律不载原书条题（条题如「兌卦失金釵」「王字（富陽占者斷督學丁艱）」含断语/结局指向，承 holdout21 QM-004 裁处剔除改中性定位）；剥离：title/anchor_*/contamination_*/separable/eligible/cz_qx_*/dedup/transcription/master_assertion/outcome 不入卡。
- **ZCB-004 附条件改写（1 例，承 holdout20/21 先例）**：台账 input_side 末段「定期則「口為四字[?]……其不足四年乎，今年為戊子，至四年為辛卯，夕字卯字偏傍亦相合也」」整段为应期断语（断语内容）、非字形拆分本身，输入侧删此段；改写前后对照存证于构建报告 `rewrites`，原台账不动；删后片段/标记复扫零新增命中（见 §四）。
- **GSZ 4 例**：anchors＝asked_at＋台账 input_fields.chart 全列逐字（本卦/变卦/动爻/六爻全列）；context 由 asked_at＋书名组写、setting/provenance 由台账 source 逐字承接（承 holdout20/21 组写先例，口径逐例登记于构建报告）；台账 subject 为空，卡内 subject 作「求测者（台账 subject 为空、原书未具名）」。剥离：pollution*/anchor_presence/anchor_missing/dedup_check/filters/outcome_type/outcome_record/master_prediction 不入卡。
- **标旗二件（提请主持知悉）**：① DS-011 的 setting 含原书节题「商海沉浮，女强人命运多舛」（台账 source 逐字，属书目著录；语义为泛指、非具体结局事实），本席照逐字保留并在此标旗。② ZCB-003 的拆分过程原文末句含断者推理结论语「故知丁艱。此斷以理也」，系台账 input_side 拆分过程原文之一部、与拆语同条同文不可分，承 §三「字形拆分过程等锚点原文」为输入侧载荷保留，逐卡登记于此（与 §四 ZCB-004 拆语命中同口径）。

## 四、断语扫描三道执行登记

- **第一道（脚本逐字子串扫描）**：每例 master_prediction 与 outcome_record 的特征片段（标点分句整句（≥8 字）＋去空白 12 字滑动窗口全集）对该例输入卡全文本逐字子串扫描——**结局片段 27 例合计零命中；断语片段非测字 23 例零命中**（均脚本硬断言）；落盘后对盘上文件重行仍同。**测字 4 例**：ZCB-001/002/003 断语片段零命中；**ZCB-004 断语片段命中 7**，逐 fragment 登记于构建报告 `cezi_hit_classification`——全部为字形拆分语引文内含语（「下為口字，上為外字偏傍，是口外矣」诸窗口及「日在于西為夕，其西域乎」），逐字见于台账 input_side 拆分过程锚点原文：测字断语与拆语同源同文（断者拆字之语即断语首段），此命中属 §三明列锚点原文载荷、非结局/断语正文泄漏；其中「其西域乎」为拆语内方位推断语，一并标明提请主持知悉。另行 h20 第二道口径卫生自校验（R42 PREREG §5 内容级一级/二级标记＋字段名黑名单＋禁用键集，全字段递归）——27 卡逐卡零命中、合计 0（启悟篇名命中已于建卡前处置，见 §三）。
- **第二道（语义级抽查，10 例 ≥8）**：组集席逐例通读输入卡确认无结局/断语泄漏——名单：DS-004、DS-011、QM-011、QM-014、QM-201、QM-203、QM-301、ZCB-001、ZCB-004、GSZ-022。逐卡结论：仅含问事、背景与锚点（四柱/局式/卦象/字形拆分过程），无断语正文、无结局陈述；标旗二件见 §三（DS-011 节题泛指语、ZCB-003 拆分过程结论语），ZCB-004 改写后卡已无定期应期段（见 §三）。
- **第三道（主持验封）**：非本席执行——留位：主持以独立脚本对 `holdout22/inputs/` 全部输入卡复扫（逐字片段＋内容级标记），零命中后于本日志追加「验封通过」与金标 SHA 主持双读结论；本日志不冒充第三道结论。
- **建后逐卡回读自检（本席分内）**：落盘后逐卡回读重行片段扫描＋标记扫描＋禁用键扫描＋字段白名单核，27／27 全过（逐卡结果在构建报告 `scan_reread_selfcheck`）。

## 五、断语逐字核验与补录登记（金标）

- **逐字核验通过（照台账，23 例）**：DS 9 例（台账视觉转录逐字断语、filters 首滤「断语逐字可录」pass；多段以／分隔为台账摘录分隔符，逐例载金标 grade_note）；QM-201/202/203 第二局、QM-301–303（台账逐字引文/断语，无摘写标记；启悟/石建国转录 confidence＝high）；ZCB-001–003（原书断语短句逐字，台账 transcription confidence 0.92/0.85/0.82 逐例载金标 grade_note）；GSZ 4 例（文字版 PDF 文字层 verbatim；断语与原书文字层对勘合，如 GSZ-026 断语「二爻寅木月破为幽门、十二指肠溃疡」见原书第五章例二断卦思路原文）；**QM-011、QM-014 经本席读原书页图逐字核**：QM-011 与《开悟之门》印刷 207 页「断：」（1）–（4）逐段合、QM-014 与印刷 215 页断语引文逐字合，照台账（核验登记逐例载金标 editor_note）。
- **补录（台账非逐字、回原书逐字补录，4 例）**：补录断语逐例载金标 editor_note（原因/出处页/字数），台账 outcome 均与原书对勘一致、照台账：
  - **QM-012（补录断语全文 195 字）**：台账为分析文摘写（删「乙+辛龙逃走，凶」「辛+丙，测病不愈」等句、改「综上所述分析」为「综上分析」等）；补录自《开悟之门》印刷 210–211 页（PDF238–239）分析（1）–（4）全文，本席读渲染页图逐字。
  - **QM-013（补录断语全文 204 字）**：台账为摘写，且括注误植 A 例（母鸡）分析（2）内容充 B 例（公鸡）分析（4）；补录自印刷 211–212 页（PDF239–240）分析（1）–（4）全文，本席读渲染页图逐字。
  - **QM-203（补录断语全文 343 字）**：台账第一局断语以「……」省略中段一句（61 字：「你剛才說從懷孕到現在六個多月，那麽到下個月也就是七個多月，按理說是沒到生孩子的時候，但我的奇門盤中反映出來的資訊就是下個月你要生小孩的，而且還要剖腹產。」）；补录自《奇门启悟》印刷 202 页（PDF102–103 跨页）第一局断语全文；第二局台账已逐字、与印刷 203–204 页合，照台账。
  - **ZCB-004（补录断语全文 89 字）**：台账为问答摘写摘要（嵌问句、删拆语主干）；补录自《字触补》卷二·外部叶 8–9（合集 PDF553 下半–557 上半，页图 hi-557）墨字董字名字条后段原文断语诸段逐字、以；分隔（分隔符为本席登记，逐例载金标 editor_note）；outcome 与原书对勘（「至是果驗」、辛卯应期）一致，照台账。

## 六、跨书同案再核结果（规则 5）

- 对勘对象：本轮 QM 入选 10 例（QM-011–014、QM-201–203、QM-301–303）与 R56 既有 QM 池 QM-001–010，逐例以占事＋占时＋占者三键对勘（键表逐例登记于构建报告 `triple_key_crosscheck_qm`）。
- 结果：**零同案命中，无剔除、无递补**。占者一键即不交：R56 池占者为杜新会/张志春/王建国，本轮占者为吕常文/刘文元/石建国；占时与占事亦逐例互异。
- 附注：开悟台账 dedup_note 载本书疾病例二 B 与 QM-006 同案、已出局不入池——该例不在本轮入选 4 例内（入选为例一/例三 A/例三 B/例四），不影响本核。

## 七、验收快照登记（封存时点活 method）

- 快照目录：`runs/round76/kb-snapshot-holdout22/`（自 `benchmark/phase3/method` 全目录复制于封存时点，即附则 §二集成后文本）。
- 文件数：**21**；逐文件 SHA-256 清单：`runs/round76/kb-snapshot-holdout22-sha256.txt`（21 行）；本席已以 `sha256sum -c` 对清单全量复验，21／21 OK。
- 与 R76 开轮快照（`runs/round76/kb-snapshot/`）差异自核：恰为三件——`references/chinese-cezi.md`、`references/chinese-qimen.md`、`references/chinese-bazi-ziwei.md`（与附则 §二集成口径一致），其余 18 件哈希全同，逐件登记于构建报告 `kb_snapshot`。

## 八、封存状态与开封条件（承附则 §三，写死）

- holdout22 自本日志落盘起封存；本轮不开封、不作任何验收预演。金标只许评审角于开封轮打开。
- **开封条件（写死）：封存后首个平台全立轮开封（最早 R77）**；该验收集即 R61-REV1 判读集（N＝27 ≥20），判读照 PREREG-ADDENDUM-r61 §三定版口径逐字执行（门槛以附则 §三引文为准，本件不改）；验收快照锚定本封存时点活 method（§七快照）。
- 本回传不作封存依据，以盘上文件＋主持验封（第三道扫描＋金标 SHA 双读）为准；金标字节若有任何后续变动，须重算 SHA 并在本日志追加记录、原 SHA 作废留痕。
- 中间件登记：原书文字层提取件 `runs/round76/gsz-book-r76.txt`（六爻五要素复核用）留 runs/round76/ 内备查。

## 九、主持裁处与 delta 重建（R76 主持裁处 delta 修正席，2026-10-31）

本节为封存后主持裁处之执行登记，以 append 追加，原 §一–§八一字未动。执行脚本 `runs/round76/delta_holdout22_r76_hostseat.py`、登记件 `runs/round76/delta-holdout22-register-r76-hostseat.json`、原书叶面渲染件 `runs/round76/delta-r76-hostseat/`（PDF557/558 页 300dpi 渲染与裁切图）。前置核验：动手前金标 SHA-256 实测 `1e299bdaf10724bf2ba66d1f4933fdcbeee11b5970f978df975872bb7164ae6a`，与主持第三读一致；快照 `kb-snapshot-holdout22` 未动（其 SHA 清单文件哈希改前改后一致）。本席不开封、不作断、不评分、未做 git 操作。

### 九.1 三项裁处执行

1. **ZCB-003 换例（剔除 → ZCB-005）——已执行**。裁处理由：ZCB-003 输入卡锚点原文含结论句「故知丁艱」，属断语/结局事实入卡。处置：精确删除 `holdout22/inputs/ZCB-003.json` 与 `holdout22/test_gold.jsonl` 中 ZCB-003 行（精确路径/精确行操作，非通配删除）；以台账 `runs/round76/digestion/SUPPLY-MINING-zichubu-r76.json` 之 ZCB-005 记录（eligible＝true∧anchor_status＝present∧contamination_pre＝low∧separable＝true，本席复断言通过）按与原测字四例同一规格建卡建标（详见 §九.2）。测字构成仍 4 例：ZCB-001、ZCB-002、ZCB-004、ZCB-005；T 仍 27。
2. **DS-011 卡面中性化——已执行**（逐字对照见 §九.4）。`holdout22/inputs/DS-011.json` 的 setting 与 provenance 各 1 处，删第八章小节题全文「商海沉浮，女强人命运多舛」，定位只留「第八章第一节六」，其余字串一字不动；subject 之「女企业家」为输入侧事实，保留未动。原题全文只留本日志登记（本节对照与 §三标旗①）。金标 DS-011 行除行序重整外一字未动（金标侧 provenance 照原登记）。
3. **QM-301 卡面中性化——已执行**（逐字对照见 §九.4）。`holdout22/inputs/QM-301.json` 中实例题「少收的贷款能找回」全卡共 2 处（setting 1 处、provenance 1 处），逐处删该题名全文、保留下编第七章「钱物丢失预测」实例一之定位部分；全卡其余字段经检索无该题名字串，question「刚才卖货时少收了顾客500元钱，看货款能不能找回来」为输入侧问句原文、非题名字串，一字未动。金标 QM-301 行除行序重整外一字未动。

### 九.2 ZCB-005 建卡与金标断语逐字核验登记

- **建卡规格（同原测字四例）**：字段白名单 {id, tradition, subject, context, question, setting, provenance, redistributable, license_status, anchors}，键序同原四例；context 与 anchors.split_process_verbatim ← 台账 input_side 逐字（字形拆分过程为输入侧锚点原文）；anchors.character＝「因」；subject＝「孟瓶庵与榜前同测二友」、question＝「榜前书因字请测（三人同字分测）」为组写（口径在此登记）；setting＝「《字触补》卷二·外部·叶9（《四库未收书辑刊》陆辑第拾捌册，PDF页557下半）」、provenance 同 setting＋「；用户经学校图书馆提供；redistributable=false」；license_status＝「古籍文本（合集扫描本），内部研究用」；setting/provenance 只载卷叶与 PDF 页定位、不载原书条题（同原四例中性化口径）。剥离：title/anchor_*/contamination_*/separable/eligible/cz_qx_*/dedup/transcription/master_assertion/outcome 不入卡。
- **取原书口径**：任务书作《字触补》在 `incoming/wanted-books-3/` 之合集 PDF 内；台账 meta 登记之 container_file 实为 `incoming/wanted-books-5/Book/四库未收书辑刊 陆辑 拾捌册 (四库未收书辑刊编纂委员会编).pdf`（wanted-books-3/Book 下无此 PDF），本席以台账 meta 为准取原书，该文件 SHA-256 实测 `c692398989c29e04a6964b19191c0ac3f0ac69668fdc2d3cff78d2146ead6b5e` 与台账登记一致。ZCB-005 出处照台账 source 字段：卷二·外部·叶9，PDF页557下半（条末续于 PDF558 上半）。
- **金标断语逐字核验（回原书叶面，300dpi 渲染逐句对勘）——逐字核验通过，不补录**。金标 master_prediction＝「（孟）君必為此科解首矣；（友二）君此科恐無分，或後此有恩科亦必中；（友三）其終於一衿乎。」（全文 44 字），三人三断照原书分列，逐断对勘：
  - 孟瓶庵断「君必為此科解首矣」——原书叶9（PDF557下半）「其人曰此為國中一人之象君必為此科解首矣」，逐字合。
  - 友二断「君此科恐無分，或後此有恩科亦必中」——原书叶9（PDF557下半）「其人曰君此科恐無分或後此有恩科亦必中」（原书无逗号，逗号为转录标点），逐字合。
  - 友三断「其終於一衿乎」——原书叶9续（PDF558上半）「君之扇適加因字正中有困之象其終於一衿乎」，逐字合。
  - 结局「後三君皆如其言」——原书叶9续（PDF558上半）「後三君皆如其言此人惜不傳姓名殆亦高鳳之流亞矣」，台账 outcome 逐字合、照台账。
  - 登记说明：金标中（孟）／（友二）／（友三）标签与分号为三人三断之分列标记（同 DS 例「／」台账摘录分隔符先例），非原书文字；断语本体逐字，故不触发逐字补录，无补录字数。grade_note 照原四例公式组写（锚点 present 依据、污染 low 依据、转录 visual confidence＝0.9、CZ-QX 计数例注记均承台账逐字）。
  - 附注（输入侧）：台账 input_side 作「以徐[?]茶書一因字」，原书叶面该处作「以餘茶書一因字」（餘字清晰）；[?] 为台账未判准标记、非断语字段，输入卡照规格承台账逐字不改，仅此附注。
- **新卡同一套自检（全过）**：字段白名单键序合；禁用键递归扫描零命中；断语片段扫描（标点分句整句≥8字＋去空白12字滑动窗口，对卡全文本逐字子串）零命中；结局片段扫描零命中——无 fragment 需分类登记；内容级一级/二级标记＋字段名黑名单扫描零命中；卡内无「故知…」式结论句（「故知」子串检索零命中）。

### 九.3 新选集与新金标 SHA

- **新选集 id 全表（T＝27，金标行序照 id 序重整后之序）**：DS-004、DS-005、DS-006、DS-007、DS-008、DS-009、DS-010、DS-011、DS-012、GSZ-022、GSZ-023、GSZ-024、GSZ-026、QM-011、QM-012、QM-013、QM-014、QM-201、QM-202、QM-203、QM-301、QM-302、QM-303、ZCB-001、ZCB-002、ZCB-004、ZCB-005。构成：八字 DS 9（DS-004–DS-012）、六爻 GSZ 4（GSZ-022、GSZ-023、GSZ-024、GSZ-026）、奇门 QM 10（QM-011–QM-014、QM-201–QM-203、QM-301–QM-303）、测字 ZCB 4（ZCB-001、ZCB-002、ZCB-004、ZCB-005）。其余 24 例之卡与金标内容一字未动（金标仅行序重整与 ZCB 一删一增；未动行经逐行字节无损自检）。
- **改后两卡复扫**：DS-011、QM-301 改后重行断语/结局片段扫描、标记扫描、禁用键扫描、字段白名单核，均零命中/通过。
- **新金标 SHA-256（双读）**：脚本 hashlib 读数 `e10fc3f6e3bbef6514016e1bdb9a8aacb7456e44e80f0b564c5593ab7e3489cd`；脚本外 `sha256sum` 读数 `e10fc3f6e3bbef6514016e1bdb9a8aacb7456e44e80f0b564c5593ab7e3489cd`；两读一致，成立。原 SHA `1e299bdaf10724bf2ba66d1f4933fdcbeee11b5970f978df975872bb7164ae6a` 自本节落盘起作废留痕（承 §八口径）。开封条件不变（§八写死口径不改）。

### 九.4 两卡改动逐字对照（改前／改后）

**DS-011（inputs/DS-011.json，setting 与 provenance 各 1 处）**

- setting 改前：「《段氏理象学》（段建业著，中国商业出版社2011年12月第1版，ISBN 978-7-5044-7457-5）·第六章第一节一·例三（印刷p.85／PDF109）＋第八章第一节六、商海沉浮，女强人命运多舛（印刷pp.137-139／PDF161-163）」
- setting 改后：「《段氏理象学》（段建业著，中国商业出版社2011年12月第1版，ISBN 978-7-5044-7457-5）·第六章第一节一·例三（印刷p.85／PDF109）＋第八章第一节六（印刷pp.137-139／PDF161-163）」
- provenance 改前：「《段氏理象学》（段建业著，中国商业出版社2011年12月第1版，ISBN 978-7-5044-7457-5）·第六章第一节一·例三（印刷p.85／PDF109）＋第八章第一节六、商海沉浮，女强人命运多舛（印刷pp.137-139／PDF161-163）；底本为用户经学校图书馆提供，redistributable=false」
- provenance 改后：「《段氏理象学》（段建业著，中国商业出版社2011年12月第1版，ISBN 978-7-5044-7457-5）·第六章第一节一·例三（印刷p.85／PDF109）＋第八章第一节六（印刷pp.137-139／PDF161-163）；底本为用户经学校图书馆提供，redistributable=false」

**QM-301（inputs/QM-301.json，setting 与 provenance 各 1 处）**

- setting 改前：「奇门遁甲最新实例解析（石建国著）·下编第七章「钱物丢失预测」实例一「少收的贷款能找回」；起局时间：2003年3月26日16点（癸未年乙卯月戊戌日庚申时）」
- setting 改后：「奇门遁甲最新实例解析（石建国著）·下编第七章「钱物丢失预测」实例一；起局时间：2003年3月26日16点（癸未年乙卯月戊戌日庚申时）」
- provenance 改前：「奇门遁甲最新实例解析（石建国著，建筑与风水杂志社（中国神秘文化大系），ISBN 988-98339-8-0）·下编第七章「钱物丢失预测」实例一「少收的贷款能找回」，印刷页245-246（DjVu页256-257）；用户经学校图书馆提供；redistributable=false」
- provenance 改后：「奇门遁甲最新实例解析（石建国著，建筑与风水杂志社（中国神秘文化大系），ISBN 988-98339-8-0）·下编第七章「钱物丢失预测」实例一，印刷页245-246（DjVu页256-257）；用户经学校图书馆提供；redistributable=false」


## 十、开封验封追记（R77 主持，2026-10-31；补 §四第三道留位）

R77 平台三项全立（(a) −1.150／(b) 四护栏全立／(c) −1.869，详 runs/round77/acceptance/OPENING.md），照 PREREG §2 闸门当轮开封。开封前置复验三项全过：① 金标 SHA-256 独立复测＝e10fc3f6e3bbef6514016e1bdb9a8aacb7456e44e80f0b564c5593ab7e3489cd，与 §九.3 定版逐字全等；② 输入卡 27 张在盘、构成与封存一致；③ 主持第三道复扫（脚本 runs/round77/acceptance/rescan_inputs_h22_host_r77.py，标记集逐字承 R42 PREREG §5、与第二道同集）对 holdout22/inputs 全部 27 卡全字段递归复扫，**零命中**。§四第三道（主持开封轮复扫）至此补齐，验封通过，本集自本节起为已开封状态，验收执行记录见 runs/round77/acceptance/。
