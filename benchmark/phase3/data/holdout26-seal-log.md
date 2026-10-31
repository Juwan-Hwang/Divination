# holdout26 封存日志（R81 组集封存席，2026-10-31）

**本集已按增补件建成、已封存（T＝27），本轮不开封。** 授权文本：`runs/round81/PREREG-ADDENDUM-r81.md`（组集构成写定，承主预注册 `runs/round81/PREREG.md` §4）。配套口径：holdout25 封存定式（`data/holdout25-seal-log.md` 体例）、`runs/round42/PREREG.md` §5（内容级断语扫描标记集）。
产物：`holdout26/inputs/` 27 张输入卡（合计 37,487 字节）；`holdout26/test_gold.jsonl` 27 行金标（38,627 字节）；构建脚本 `runs/round81/build_holdout26_r81.py`（本轮新写唯一名，内含全部资格断言/选集写定/五要素复核/零复用/字段白名单/扫描断言；适配自 holdout25 构建脚本与 holdout20 WHY 建卡段后已 grep 残留轮次字面量逐处查——round80/holdout25 字样仅存于脚本头「承先例/范本」实指引用与字段白名单对齐基准（holdout25 卡实读），无误伤）；构建报告 `runs/round81/build-holdout26-report-r81.json`（66,192 字节）；独立复扫脚本 `runs/round81/scan_holdout26_r81.py` 与结果 `runs/round81/scan-holdout26-result-r81.json`（7,213 字节）。探查中间件（只读）：原书页图渲染与裁切件 `runs/round81/why-pages/`（WHY 原书 pp.12–19 渲染页与裁切）、`runs/round81/ds-pages/`（DS 原书 PDF127-128/131-132 渲染页）、语义通读转储脚本 `runs/round81/dump_cards_holdout26_r81.py` 及转储件 `runs/round81/dump-cards-holdout26-r81.txt`，均在本轮目录内，未用 /tmp。本席只建卡与封存：不作断、不评分、未开封任何集、未做 git 操作。
**金标 SHA-256 双读一致**：构建脚本 hashlib 输出 `2d5bad70747e0d02d6df5d4d8ee1dc6fcc0ac751bfc52aa4877dfe074df98e97`；本席落盘后独立 `sha256sum` 实测同值 `2d5bad70747e0d02d6df5d4d8ee1dc6fcc0ac751bfc52aa4877dfe074df98e97`（全文 64 位）。双读一致为定版候选；主持再以独立 sha256sum 第三读复核一致后方为封存定版（本席只报双读，第三读留位主持，见 §八）。
**泄题列单先行标出（详见 §一.1）**：入选标旗 1 件——DS-033（subject 承台账逐字，其命主身份描述含「金融业超级富翁/庄家」财富量级字样），照增补件逐字规格入卡、卡面原样保留、未自改一字，提请主持裁处；排除登记 1 件——ZCB-003（维持排除、未入选，本轮无测字段额）。
**裁处登记先行标出（详见 §五）**：WHY-005/WHY-006 结局对调订正 1 组——台账 outcome_record 经本席回原书逐字核对为两例互换（原书印刷 p16 应验段属 WHY-005、p17 应验段属 WHY-006），金标已按原书对调还原并逐件登记，提请主持验封复核裁处。
**递补未触发**：增补件写定 27 例逐例资格断言全过（见 §二），递补链（DS 段 DS-040 起、开悟段 QM-044 起、GSZ 段 GSZ-079 起、WHY 段 WHY-008 起）全程未动用，T＝27 足额，构成限度已断言（见 §一）。

## 一、构成表（增补件 §一写定实成，逐源/逐体系计数）

| 来源 | 例数 | 占比 | 入选 id |
|---|---|---|---|
| 段建业《段氏理象学》 | 9 | 33.3% | DS-031、DS-032、DS-033、DS-034、DS-035、DS-036、DS-037、DS-038、DS-039 |
| 张志春《开悟之门》 | 9 | 33.3% | QM-034、QM-035、QM-036、QM-037、QM-038、QM-039、QM-040、QM-042、QM-043 |
| 王虎应《六爻卦例说真》 | 5 | 18.5% | GSZ-069、GSZ-074、GSZ-075、GSZ-077、GSZ-078 |
| 王虎应《六爻分类占验技法》 | 4 | 14.8% | WHY-004、WHY-005、WHY-006、WHY-007 |
| 合计 | 27 | 100% | 非夷坚 27；测字定额 0、不取例（可选存量 0，见 §一.1） |

| 体系 | 例数 | 占比 |
|---|---|---|
| bazi（八字） | 9 | 33.3% |
| qimen（奇门） | 9 | 33.3% |
| liuyao（六爻） | 9 | 33.3% |
| cezi（测字） | 0 | 0% |

- 构成限度逐项断言（脚本内硬断言、全过）：总量 T＝27 ≥25；单体系最大 9/27＝33.3% ≤50%（计数 ≤13）；单源最大 9/27＝33.3% ≤50%（计数 ≤13；WHY 与 GSZ 分属两书）；非夷坚 27 ≥13；非六爻 18 ≥13；多源构成（四源并存）；污染 low 27/27；仅锚点在场例入选（资格断言见 §二）；与已用并集逐 id 交集＝∅（见下）。
- **例级零复用**：已用并集盘上 id 集实算 **1085 id**（dev 池＝`data/master-baseline-dev9.json` 键集 487＋inputs-dev9/10/11/12 与 inputs 目录卡 id 后 488；phase2 splits2 之 holdout2 29；holdout3–25 各 test_gold.jsonl 仅取 id 字段 673（逐集：h3 27／h4 25／h5 25／h6 23／h7 1／h8 28／h9 28／h10 29／h11 25／h12 49／h13 40／h14 40／h15 40／h16 40／h17 40／h18 30／h19 25／h20 25／h21 25／h22 27／h23 27／h24 27／h25 27）；holdout2–25 inputs 与 *-inputs 目录卡 id 514；顶层 inputs6–10 目录卡 id 412（与上多有重合）；五源并集去重后 1085，与主持开轮实算 1085 及组集席第一阶段复算（STOCK-RECOUNT-h26）一致），选例 27 id 逐 id **零命中**（只对 id 集，未打开任何已封存集金标正文做内容比对）。另按派单口径对 holdout25 之 27 id 单列对勘：零交集（该 27 id 本已含于 1085 并集内）；本集封存后已用并集将为 1085＋27＝1112。逐源计数与方法登记于构建报告 `zero_reuse_recheck`。

### 一.1 泄题列单、剔除/递补与特殊登记（全程）

**入选标旗（照逐字规格入卡、卡面原样保留、提请主持裁处，1 件）**：

1. **DS-033（段氏）**：subject 承台账 input_side.subject 逐字「「L总」，金融业超级富翁/庄家（化名，未具名）」——命主身份描述含财富量级字样；该例断语/结局方向（限年停业、牢狱标志）未载于卡面，身份成色至多构成方向暗示。本席不得自改，照录标旗；主持如裁改写 subject 或换例，递补序为 DS 段同源下一例 DS-040（未预核其入选形态，裁处时另核）。

**排除登记（未入选，1 件）**：

2. **ZCB-003（维持排除）**：台账资格全过、id 未入已用并集，但已经 holdout22 主持裁处判为断语/结局事实入卡并换例剔除；本轮承 PREREG §4 与 STOCK-RECOUNT-h26 §四，裁处未撤销、维持排除。本轮构成无测字段额，本无取例，只登记、不翻案。测字可选存量 0（合格 15－已用 14－本件 1）。

**递补登记（0 件）**：增补件写定四段名单逐例资格断言全过（§二），同段同源递补链未触发；跨段递补未发生。

**已用剔除（逐 id，同名即剔）**：写定名单本身即 STOCK-RECOUNT-h26 之 eligible 未用名单，与已用并集 1085 逐 id 对勘零命中，无写定例因同名被剔之事。

## 二、资格断言结果（逐例，缺一不可）

27 例逐例断言全过（脚本硬断言：任一例不过即中止建集；本轮中止零、递补零）：

- **DS-031–039**：台账（SUPPLY-MINING-duanshi-r76.json）逐例 eligible_net＝true、anchor_status＝present、contamination_pre＝low、filters 四项全 pass、master_assertion/outcome 逐字非空——9/9 过。同造合并组核验：台账同造合并组唯一卡 DS-033 在本段入选、同组至多取 1 之限不触（本段仅此一例属该组）；入选 9 例四柱（pillars_verbatim）互异（戊午庚申丁巳癸卯／丙午辛卯丁卯丙午／戊申己未癸巳己未／庚辰乙酉癸卯庚申／乙未壬午甲子甲戌／戊戌己未辛卯辛卯／壬子辛亥丁巳辛亥／丁巳庚戌辛丑己亥／壬寅戊申辛巳戊戌）、无同造重复。
- **QM-034/035/036/037/038/039/040/042/043（开悟）**：台账逐例 anchor_status＝present、contamination_pre＝low、separable＝true、stem_check 天盘与地盘**双 ok（全合）**、断语/结局非空——9/9 过。台账注记登记：QM-035 notes 载第二局盘面干集以第一局字段代表校验及以年命为主断之口径冲突登记；QM-039 notes 载第一局盘面兑7/艮8 两宫字序未完全厘清、字段以第二局盘面为校验代表、第一局局头无误列入挂起待精核——二例注记全文逐例载于各例金标 grade_note，QM-039 第一局盘面四宫未厘清字样照台账 input_side 逐字入卡（anchors.board_verbatim）。
- **GSZ-069/074/075/077/078（六爻）**：台账逐例 grade＝A、pollution＝low、anchor_presence＝present、eligible_net＝true、断语/结局非空，且属建卡口径未用名单（STOCK-RECOUNT-h26 §一.6 五要素复核通过 24 例）成员；并逐例回原书文字层（`runs/round76/gsz-book-r76.txt`）以构建脚本同一 five_elements 函数复核锚点五要素——5/5 全在场：
  - GSZ-069（第十一章例一）：本卦火地晋/变卦泽地萃；动爻 官鬼己火动、父母未土动；世 兄弟酉金、应 父母未土；六爻全列六亲纳支；庚辰年庚辰月己酉日（原文「已酉」）——全在场。
  - GSZ-074（第十二章例一）：山雷颐变离为火；动爻 妻财戌土（世）动、妻财辰土动；世 妻财戌土、应 父母子水；六亲纳支全列；丁丑年癸丑月己巳日（原文「已巳」）——全在场。
  - GSZ-075（第十二章例二）：天风姤（原文作「天风逅」）变泽风大过；动爻 父母戌土动；世 父母丑土、应 官鬼午火；六亲纳支全列；戊寅年卯月丁巳日——全在场。
  - GSZ-077（第十二章例四）：风水涣变天水讼；动爻 子孙未土动；世 兄弟巳火（原文「已火」）、应 子孙辰土；六亲纳支全列；戊寅年甲寅月己酉日（原文「已酉」）——全在场。
  - GSZ-078（第十二章例五）：天水讼变风水涣；动爻 兄弟午火（世）动；世 兄弟午火、应 父母寅木；六亲纳支全列；戊寅年戊午月乙酉日——全在场。
- **WHY-004/005/006/007（六爻）**：台账（SUPPLY-MINING-wanghuying-r56.json）逐例属 counts 净入账名单（net_eligible_A_low_present 40 例）成员、pollution＝low、anchor_presence＝present、anchor_missing 为空、outcome_record 非空——4/4 过。断语台账未单列字段（缺口整段），已回原书逐字补录后封（见 §五）。

## 三、逐例规格执行与剥离登记（输入卡卫生）

输入卡字段白名单（全 27 卡断言通过）：{id, tradition, subject, context, question, setting, provenance, redistributable, license_status, anchors}（开工先回读 holdout25 任一卡（DS-025）实读字段集对齐、断言一致后写定；键序与 holdout22–25 卡一致）；脚本以禁用键集对 27 张输入卡全字段递归扫描，管理/断语/结局/master/gold/outcome/answer/判级/污染类键零残留（断言通过，落盘后复扫亦零）。provenance 全 27 卡含「用户经学校图书馆提供」、redistributable 全 false。逐例 present_basis（来源定位）即各卡 provenance：DS 9 例＝台账 source（书名＋章章节次＋印刷页/PDF页）；开悟 9 例＝台账 source（下编章章节次＋印刷页）；GSZ 5 例＝台账 source（书名＋章/例）；WHY 4 例＝台账 source（书名＋章/例＋印刷页）。逐例剥离与字段映射全量登记于构建报告 `strip_register`／`field_mapping_notes`，体例如下：

- **DS 9 例**：anchors＝pillars 四柱全列＋pillars_verbatim＋gender（台账 input_side 逐字）；subject←input_side.subject 逐字；setting←台账 source 逐字；context/question 为组写（台账无该二字段，口径同 holdout22–25 并逐例登记）。剥离：anchor_status/anchor_note/contamination_*/separable/transcription/dedup/filters/eligible_net/verdict_note/composition_type/master_assertion/outcome 不入卡。本书「断准」自选偏倚承台账 contamination_note 逐例载入金标 grade_note。
- **开悟 QM 9 例**：anchors＝board_verbatim（input_side 盘面段逐字；QM-035/QM-039 两局盘面全载）＋stems_tianpan/stems_dipan＋stem_check；context←input_side 盘面之前段逐字；question←input_side 原文子串（脚本断言子串在场；QM-040 例外：原文未逐字引问句，question 为组写、已逐例登记）；subject 为组写（据 input_side 与 caster 组写，登记于构建报告）；setting←source＋caster 组写。剥离：topic/anchor_status/contamination_pre/separable/transcription/dedup/master_assertion/outcome 不入卡。QM-035/QM-039 台账 note 逐例载入金标 grade_note。
- **GSZ 5 例**：anchors＝asked_at＋台账 input_fields.chart 全列逐字（本卦/变卦/六爻全列）；context 由 asked_at＋书名组写、setting/provenance 由台账 source 逐字承接（承 holdout22–25 先例）；台账 subject 为空，卡内 subject 作「求测者（台账 subject 为空、原书未具名）」。剥离：pollution*/anchor_presence/anchor_missing/dedup_check/filters/outcome_type/outcome_record/master_prediction 不入卡。
- **WHY 4 例**：anchors＝asked_at＋ben_gua＋bian_gua＋moving_lines＋chart_lines_top_to_bottom（台账 input_fields.chart 全列逐字）；subject 同 GSZ 口径；context 由 asked_at＋书名组写、setting/provenance 由台账 source 逐字承接（承 holdout20 先例）。剥离：pollution/anchor_presence/anchor_missing/dedup_check/transcription/outcome_type/outcome_record 不入卡。

**删除/改写清单（全程逐字登记）**：

1. **节题/问题中性化改写（0 件）**：入选 27 例节题（setting）与 question 逐例核查——GSZ/WHY question 承台账逐字、均只及所问之事；KW question 为原文子串或登记组写；DS question/setting 为组写与台账 source 逐字——无一含结局事实，无中性化改写件，登记于构建报告 `hygiene_question_scan` 与 `deletion_register`。
2. **「求测例/求测例题」类编辑装置残段删除（0 件）**：入选 27 例 question 逐例字面扫描（求测例/求測例/求测例题/求測例題）零匹配，无删除件。
3. **双人例 question 中与所问无关之第二人结局字样删除（0 件）**：入选例中多人面例（QM-036 三人办手续、QM-040 朋友之子、QM-042 同事之子、QM-043 职工之女、GSZ-077 朋友的女儿）question 均只及所问之事本身，无第二人无关结局字样，经语义级逐卡通读核查（见 §四），无删除件。
4. 除上述外本席对卡面未作任何删改；标旗件 DS-033 卡面原样保留（见 §一.1），待主持裁处。

## 四、断语扫描三道执行登记

- **第一道（构建脚本内扫描断言）**：(a) 逐字片段扫描——每例 master_prediction 与 outcome_record 的特征片段（标点分句整句（≥8 字）＋去空白 12 字滑动窗口全集）对该例输入卡全文本逐字子串扫描：**结局片段 27 例合计零命中；断语片段 27 例合计零命中**（脚本硬断言）；落盘后对盘上文件重行仍同。(b) 内容级标记扫描（R42 PREREG §5 一级/二级标记集，脚本常量与该节逐字一致）＋字段名黑名单＋禁用键集，全字段递归——27 卡逐卡零命中、合计 0。
- **第二道（封存席独立复扫，交卷前执行）**：独立脚本 `runs/round81/scan_holdout26_r81.py`（不 import 构建脚本，按显式 id 清单逐件精确打开盘上卡与金标）重行标记/字段名/禁用键/白名单/片段五项——**全过（pass＝true、failures＝[]）：标记 0、字段名 0、禁用键 0、结局片段 0、断语片段 0**，结果落 `runs/round81/scan-holdout26-result-r81.json`。该脚本附加短片段核（断语 ≥8 字连续子串在卡面出现者逐条登记、仅信息登记）：**命中 1 例 2 条**——QM-035 之「这次技术移民加拿」「次技术移民加拿大」，系该例断语转述问事时复现 question 原文问句（问事本身、非断语内容），只登记、不作命中论。**语义级通读**：本席已逐卡通读全部 27 张输入卡（转储 `runs/round81/dump-cards-holdout26-r81.txt`），结论为仅含问事、背景与锚点（四柱/局式/卦象），无结局陈述、无断语正文（标旗件除外，见 §一.1）；附带登记三件备核：DS-033 subject 身份成色字样已入 §一.1 标旗；QM-035 context 载其 1997–1998 年两次申请与面试未过之已事背景（求测时点之前提事实，所问本次面试结局未载）；QM-039 context 与盘面载失踪已事背景（出差未达、已报案），所问安危/能否找到结局未载——二例均不作标旗、只登记。
- **第三道（主持验封）**：非本席执行——留位：主持以独立脚本对 `holdout26/inputs/` 全部输入卡复扫（标记集承 R42 PREREG §5），零命中后于本日志追加「验封通过」与金标 SHA 主持第三读结论；本日志不冒充第三道结论。

## 五、断语逐字核验与补录登记（金标）

- **补录 6 例**（断语缺口先回原书逐字补录后封，逐件登记出处）：
  1. **DS-032**：台账 master_assertion 含「……」摘录缺口（略去断语首句前段、结局句与贼捕神原理段）。回原书《段氏理象学》第六章第三节一·例二页图（印刷 pp.103-104／PDF127-128，130dpi 渲染读图，件存 `runs/round81/ds-pages/`）逐字补齐断语句群：「命局本身比劫太旺，丙辛合制财星，财星太弱缺乏效率，所以他本人并无大的财命。这里运用了贼捕神原理：以木火为捕神，金水为贼神。原局捕神旺，喜欢大运流年贼神出现。另外，他局中制辛金靠的是丙火，丙火是劫财，所以他靠的是合伙求财，而且他这个财得的很容易，就像天上掉馅饼，因为劫财替他取财了，不用费自己什么力。」结局句（整个午运中就发了两年的财……）不重复入断语、仍载 outcome_record（台账逐字）。
  2. **DS-035**：台账 master_assertion 自「制印得权」起录、含「……」缺口。回原书第六章第三节五A·例一页图（印刷 pp.107-108／PDF131-132）逐字补齐全段断语：「未为财星，也是比劫羊刃库，子未穿，制了子水印星，制印得权，是当官的命。甲生午月是无根之木，死木可以制去子水，羊刃库制印是掌兵权的。」结局句仍载 outcome_record。
  3. **WHY-004**：台账未单列断语字段。回原书《六爻分类占验技法》第一章例二（印刷 p14，扫描本 PDF 第 8 页右叶，150dpi 渲染读图，件存 `runs/round81/why-pages/`）逐字补录〔判斷〕全段（繁体照原书），全文载金标 master_prediction 与构建报告 `gold_supplement`。
  4. **WHY-005**：同上，第一章「金空則鳴」例一（印刷 pp.15-16，PDF 第 8 页左叶—第 9 页右叶）〔判斷〕全段逐字补录。
  5. **WHY-006**：同上，第一章「金空則鳴」例二（印刷 p17，PDF 第 9 页左叶）〔判斷〕全段逐字补录。
  6. **WHY-007**：同上，第一章「順風和逆風」例一（印刷 p18，PDF 第 10 页右叶）〔判斷〕全段逐字补录。
  WHY 四例补录体例承 R56 补录席（SUPPLY-GOLD-SUPPLEMENT-r56）：断语以〔判斷〕起、繁体照原书、应验段不入断语。逐字性以本席 visual 读图转录口径为准，页图件在盘备主持复核。
- **结局对调订正 1 组（提请主持裁处复核）**：**WHY-005／WHY-006 台账 outcome_record 互换**——本席回原书核对：原书印刷 p16 应验段（电视预报晴天、次日上午晴、申时浓云雷声而一滴雨也没下、酉时云散）属 WHY-005（澤風大過例一，其〔判斷〕结论正是「光打雷不下雨」），与台账 WHY-006 所载结局同旨；原书印刷 p17 应验段（上午晴、下午申时转阴、电闪雷鸣、下起了大雨、雨越下越大、一直下到第二天早晨）属 WHY-006（雷風恒例二），与台账 WHY-005 所载结局逐字同。台账两例结局系互换登记。金标已按原书对调还原（WHY-005 结局取台账 WHY-006 文、WHY-006 结局取台账 WHY-005 文，文字仍为台账转录），逐例载于金标 grade_note 与构建报告 `gold_outcome_swap_correction`，提请主持验封复核；如主持裁定不许对调，须回滚该二例 outcome_record 并重算金标 SHA、本日志相应段落作废留痕。
- **逐字照台账（21 例）**：DS 余 7 例（台账视觉转录逐字断语、filters 首滤「断语逐字可录」pass，多段以／分隔为台账摘录分隔符，逐例载金标 grade_note）；开悟 9 例（台账逐字转录、无摘写/省略标记，断语缺口扫描「……」零命中）；GSZ 5 例（文字版 PDF 文字层 verbatim，断语与原书文字层对勘合）。**限度登记**：开悟 9 例本席未另读原书页图复核逐字性，其金标 editor_note 已逐例载明「逐字性以台账视觉转录口径为准」，提请主持知悉；页位已逐例载于卡面 provenance。

## 六、验收快照登记（封存时点活 method）

- 快照目录：`runs/round81/kb-snapshot-holdout26/`（自 `benchmark/phase3/method` 复制于封存时点）。**时点锚定**：封存时点活 method 含 calibration 第八节（R80-REV1，现行形态）与第九节（R81-REV1，集成登记 `method/METHOD-INTEGRATION-r81.md` 在盘、集成本轮已落盘于封存之前），快照即封存时点方法；验收盲测读此快照原件。method/ 根下 `METHOD-INTEGRATION-r78.md`、`METHOD-INTEGRATION-r80.md`、`METHOD-INTEGRATION-r81.md` 为集成登记件、非快照内容件（快照 21 文件口径承历轮），自快照排除并逐件登记。
- 文件数：**21**；逐文件 SHA-256 清单：`runs/round81/kb-snapshot-holdout26-sha256.txt`（21 行，1,923 字节），清单文件 SHA-256＝`aa074eefaf29a8152b242cd2fd028946348e8d8a6290176dda3836d2c8627697`。第九节在盘核验：快照 `references/calibration.md` 含「## 九、初判方向锚定与变更门槛核（R81 干预 R81-REV1，跨体系方向变更治理机制）」节标题（构建脚本断言通过）；快照 calibration.md SHA-256＝`3434c5ca8a1ab18e5040e9278dd286ff004263737b4e6e12f6e4dbd9ae85adef`、SKILL.md＝`6432d7a1b6d5b2f70ca09802c1c45d459fe0ad3db57ef077e211b98a8d280b00`，与集成登记件（METHOD-INTEGRATION-r81）改后哈希逐字一致。
- 与 R81 平台快照（`runs/round81/kb-snapshot/`）差异自核：**恰为集成文件集 2 件**——`SKILL.md` 与 `references/calibration.md`（即 R81-REV1 集成内容：calibration 新增第九节＋SKILL 新增 (q) 指针一行，承 `method/METHOD-INTEGRATION-r81.md` 验合登记），余 19 件哈希全同，与增补件 §四预期逐件相符。

## 七、封存状态与开封条件（承增补件与 PREREG §2/§4，写死）

- holdout26 自本日志落盘起封存；本轮不开封、不作任何验收预演。金标只许评审角于开封轮打开。
- **本集为 R81-REV1 判读集**：快照锚定封存时点活 method（含 calibration 第八节现行形态与第九节）。**开封条件（写死）：封存后首个平台全立轮当轮开封（最早 R82）**。开封前主持复验：金标 SHA-256 与本日志双读读数对勘（主持另做第三读）、输入卡 27 张在盘逐件、主持第三道复扫零命中，结论追记本日志、不另立新档。验收盲测读封存时点快照（§六）；三判据照 R42 PREREG §8（我方均分＞大师均分；低污染子集配对胜多于负；低污染子集配对差＞0；本集全 low，低污染子集＝全集 27，仍分开登记表述）。
- **R81-REV1 判读口径（照 `method/METHOD-INTEGRATION-r81.md` 与提案 §五写死，判读随本集开封验收之同口径诊断执行）**：判读基线为 holdout24 聚合（DIR 主码率 10/27≈0.370、TIM＋CLAIM 实质合计率 12/27≈0.444、OMIT 主码率 0、E4 主码率 3/27≈0.111、总配对差 −0.935）。N 口径：实成 N≥20 方判读（本集 N＝27），按实成 N 以率线折算计数（计数上限取 ⌊率×N⌋、证伪计数取 ⌈率×N⌉）。主指标 DIR 主码率 ≤0.190（N＝27 时计数 ≤5）；副指标 TIM＋CLAIM 实质合计率 ≤0.444（计数 ≤12；实质口径：TIM 剔除轻级与零级后计，CLAIM 按主码计）；护栏总配对差 ≥−1.837、OMIT 主码率 ≤0.160（计数 ≤4）、E4 主码率 ≤0.148（计数 ≤4），任一护栏破线即判读不成立；证伪 DIR 主码率 ≥0.481（计数 ≥13）或总配对差 ≤−1.870 → 标失效存档＋删 (q) 指针回滚；未达未证伪 → 标失效存档＋保留指针；成立 → 保留生效。附读：本核执行形态计数（方向变更例数、有触发变更例数、无触发恢复例数，分母 N）、E3 A 涉率 ≥0.222（计数 ≥⌈0.222×N⌉）外溢登记、奇门段配对差与段内 direction<1.75 例数照实登记（不构成触发判断）。判读执行轮预注册须逐字重述本口径、不得更改；本判读与第八节判读互不借用。
- 本回传不作封存依据，以盘上文件＋主持验封（第三道扫描＋金标 SHA 第三读）为准；金标字节若有任何后续变动，须重算 SHA 并在本日志追加记录、原 SHA 作废留痕。
- 中间件登记：原书页图渲染/裁切件（`runs/round81/why-pages/`、`runs/round81/ds-pages/`）、语义通读转储脚本与转储件（`runs/round81/dump_cards_holdout26_r81.py`、`dump-cards-holdout26-r81.txt`）留 runs/round81/ 内备查；GSZ 五要素复核用原书文字层 `runs/round76/gsz-book-r76.txt` 为既有件、本轮只读；WHY/DS 原书 PDF（`incoming/wanted-books-4/Book/六爻分类占验技法 (王虎应著).pdf`、`incoming/wanted-books-5/Book/段氏理象学 (段建业著).pdf`）为既有件、本轮只读。

## 八、主持验封（留位，非本席执行）

- **金标 SHA-256 主持第三读**：留位——主持以独立 sha256sum 复测后追记于此，与本日志双读读数（`2d5bad70747e0d02d6df5d4d8ee1dc6fcc0ac751bfc52aa4877dfe074df98e97`，38,627 字节、27 行）对勘，三读一致方为封存定版。
- **第三道（主持独立复扫）**：留位——主持以独立脚本对 27 张输入卡复扫（标记集承 R42 PREREG §5），零命中后追记结论于此。
- **主持裁处待复核两件**：① DS-033 标旗（§一.1）；② WHY-005/006 结局对调订正（§五）。
- 验封通过后由主持统一提交并打标签 `phase3-round81-holdout26-sealed`（本席未做 git 操作）。

## 九、主持验封（R81 主持，2026-10-31）

- **金标 SHA-256 主持第三读**：`2d5bad70747e0d02d6df5d4d8ee1dc6fcc0ac751bfc52aa4877dfe074df98e97`，与构建双读全等——**三读一致，定版**（38,627 字节、27 行）。
- **第三道（主持独立复扫）**：以 R42 PREREG §5 标记集对 27 张输入卡复扫（DS-033 中性化后形态）：**零命中**。三道扫描齐备。
- **主持裁处一（DS-033 标旗）**：subject 原文「金融业超级富翁/庄家」中「超级富翁/庄家」系成就量级字样，对本命例财富面断语构成方向/量级泄漏（与 holdout23 DS-013/014/015 节题中性化先例同型）；「金融业」为行业背景可留。**裁定中性化**：subject 改为「「L总」，金融业从业者（化名，未具名）」，已由主持执行落盘（金标不受影响、SHA 不变）；余字段逐字维持台账入卡形态。
- **主持裁处二（WHY-005/006 结局对调订正）**：复核成立——两例结局与其各自〔判斷〕方向逐字相合（WHY-005 澤風大過例一断「光打雷不下雨」↔ 现载结局雷声无雨、酉时云散；WHY-006 雷風恒例二 ↔ 现载结局申时转阴大雨至次晨），且封存日志 §五载原书页位（p16/p17 应验段归属）与台账互换形态互证。**裁定对调订正成立，维持金标现状**，不回滚。
- **构成与快照复核**：实成 T＝27（DS 9／开悟 QM 9／GSZ 5／WHY 4），递补未触发；零复用与并集 1085 对勘承封存席断言与 STOCK-RECOUNT-h26 复算一致；快照 `runs/round81/kb-snapshot-holdout26/` 21 文件在盘，与平台快照差异恰两件（SKILL.md／calibration.md，R81-REV1 集成差异）承封存席登记与集成登记件对勘一致。
- **验封结论：holdout26 封存成立。** 开封条件照 §八：封存后首个平台全立轮（最早 R82）；本集为 R81-REV1 判读集。

## 十、开封（R82 主持，2026-10-31）

- **开封条件达成**：R82 平台三项全立（全立计 29；(a) −1.053、(b) 四护栏全立、(c) −1.689，analyze_r82 定稿），照本日志写死条件「封存后首个平台全立轮当轮开封」于 R82 开封。
- **前置复验三项全过**：① 金标 SHA-256 主持开封复测＝`2d5bad70747e0d02d6df5d4d8ee1dc6fcc0ac751bfc52aa4877dfe074df98e97`，与封存定版逐字全等；② 输入卡 27 张在盘逐件核；③ 主持第三道复扫（独立脚本 runs/round82/host_scan_h26_r82.py，标记集承 R42 PREREG §5）零命中（结果件 runs/round82/host-scan-h26-result-r82.json）。
- **验收形态**：盲测席读封存时点快照 runs/round81/kb-snapshot-holdout26 作断；评审 anon 种子 20261093；三判据照 R42 PREREG §8（全集 27 均 low，低污染子集＝全集）；R81-REV1 判读随本集验收同口径诊断执行（口径照本日志上文与 METHOD-INTEGRATION-r81 写死，N＝27 不顺延）。
