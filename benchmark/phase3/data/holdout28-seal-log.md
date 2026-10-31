# holdout28 封存日志（R83 组集封存席，2026-10-31）

**本集已按增补件建成、已封存（T＝27），本轮不开封。本集为存量内最后一集**（取用后非六爻 eligible 余 1，见 §一.1）。授权文本：`runs/round83/PREREG-ADDENDUM-r83.md`（组集构成写定，承主预注册 `runs/round83/PREREG.md` §4 与存量复算件 `runs/round83/STOCK-RECOUNT-h28.md`）。配套口径：holdout27 封存定式（`data/holdout27-seal-log.md` 体例）、`runs/round42/PREREG.md` §5（内容级断语扫描标记集）。
产物：`holdout28/inputs/` 27 张输入卡（合计 38,974 字节）；`holdout28/test_gold.jsonl` 27 行金标（42,736 字节）；构建脚本 `runs/round83/build_holdout28_r83.py`（本轮新写唯一名，内含全部资格断言/选集写定/五要素复核/零复用/字段白名单/扫描断言；适配自 holdout27 构建脚本后已 grep 残留轮次字面量逐处核——round82/holdout27 字样仅存于脚本头「承先例/范本」实指引用、字段白名单对齐基准（holdout27 卡实读）与 holdout27 之 27 id 单列零复用对勘，无误伤；适配与构建中三处定点处置逐件登记于 §三/§五：DS-060 断语段内缺口回原书补录、启悟 section 篇首省略承先例、QM-211 台账编辑括注删除）；构建报告 `runs/round83/build-holdout28-report-r83.json`（67,501 字节）；独立复扫脚本 `runs/round83/scan_holdout28_r83.py` 与结果 `runs/round83/scan-holdout28-result-r83.json`（7,137 字节）。探查中间件（只读）：WHY 原书页图渲染与裁切件 `runs/round83/why-pages-h28/`（WHY 原书 PDF 第 12、18、23、24、25 页 200dpi 全页渲染及半叶裁切读图件）、DS-060 原书页图件 `runs/round83/ds-pages-h28/`（段氏原书 PDF 第 242–243 页 200dpi 渲染与缩放读图件）、语义通读转储脚本 `runs/round83/dump_cards_holdout28_r83.py` 及转储件 `runs/round83/dump-cards-holdout28-r83.txt`，均在本轮目录内，未用 /tmp；页图件只留本轮目录内未跟踪、不入封存产物。本席只建卡与封存：不作断、不评分、未开封任何集、未做 git 操作。
**金标 SHA-256 双读一致**：构建脚本 hashlib 输出 `e985d5d1552a8583e22297e4e9ee08cc47c3fb797056ec1f8819489d481e3675`；本席落盘后独立 `sha256sum` 实测同值 `e985d5d1552a8583e22297e4e9ee08cc47c3fb797056ec1f8819489d481e3675`（全文 64 位）。双读一致为定版候选；主持再以独立 sha256sum 第三读复核一致后方为封存定版（本席只报双读，第三读留位主持，见 §八）。
**泄题列单先行标出（详见 §一.1）**：入选标旗 **0 件**——逐卡语义通读后无成就量级/方向暗示字样须标旗者；附带登记 2 件（QM-210 借贷 50 万元与年底偿还承诺、QM-211 借贷 20 万元与年利率/期限，均问事前提事实、不作标旗）；排除登记 1 件——ZCB-003（维持排除、未入选，本轮无测字段额）。
**递补未触发**：增补件写定 27 例逐例资格断言全过（见 §二），递补链（DS 段 DS-063、GSZ 段 GSZ-101 起、WHY 段 WHY-025 起；QM 段无递补）全程未动用，T＝27 足额，非六爻实成 16 ≥13，构成限度已断言（见 §一）。

## 一、构成表（增补件 §一写定实成，逐源/逐体系计数）

| 来源 | 例数 | 占比 | 入选 id |
|---|---|---|---|
| 段建业《段氏理象学》 | 13 | 48.1% | DS-050、DS-051、DS-052、DS-053、DS-054、DS-055、DS-056、DS-057、DS-058、DS-059、DS-060、DS-061、DS-062 |
| 刘文元《奇门启悟》 | 2 | 7.4% | QM-210、QM-211 |
| 杜新会《奇门遁甲现代实例精解》（旧池） | 1 | 3.7% | QM-010 |
| 王虎应《六爻卦例说真》 | 6 | 22.2% | GSZ-091、GSZ-092、GSZ-093、GSZ-098、GSZ-099、GSZ-100 |
| 王虎应《六爻分类占验技法》 | 5 | 18.5% | WHY-012、WHY-016、WHY-022、WHY-023、WHY-024 |
| 合计 | 27 | 100% | 非夷坚 27；测字定额 0、不取例（可选存量 0，见 §一.1） |

| 体系 | 例数 | 占比 |
|---|---|---|
| bazi（八字） | 13 | 48.1% |
| qimen（奇门） | 3 | 11.1% |
| liuyao（六爻） | 11 | 40.7% |
| cezi（测字） | 0 | 0% |

- 构成限度逐项断言（脚本内硬断言、全过）：总量 T＝27 ≥25；单体系最大 13/27＝48.1% ≤50%（计数 ≤13）；单源最大 13/27＝48.1% ≤50%（计数 ≤13；WHY 与 GSZ 分属两书）；非夷坚 27 ≥13；非六爻 16 ≥13；多源构成（五源并存）；污染 low 27/27；仅锚点在场例入选（资格断言见 §二）；与已用并集逐 id 交集＝∅（见下）。
- **例级零复用**：已用并集盘上 id 集实算 **1139 id**（dev 池＝`data/master-baseline-dev9.json` 键集 487＋inputs-dev9/10/11/12 与 inputs 目录卡 id 后 488；phase2 splits2 之 holdout2 29；holdout3–27 各 test_gold.jsonl 仅取 id 字段 727（逐集：h3 27／h4 25／h5 25／h6 23／h7 1／h8 28／h9 28／h10 29／h11 25／h12 49／h13 40／h14 40／h15 40／h16 40／h17 40／h18 30／h19 25／h20 25／h21 25／h22 27／h23 27／h24 27／h25 27／h26 27／h27 27）；holdout2–27 inputs 与 *-inputs 目录卡 id 568；顶层 inputs6–10 目录卡 id 412（与上多有重合）；五源并集去重后 1139，与主持开轮实算 1139 及本席开工复算 STOCK-RECOUNT-h28 一致），选例 27 id 逐 id **零命中**（只对 id 集，未打开任何已封存集金标正文做内容比对）。另对 holdout27 之 27 id 单列对勘：零交集（该 27 id 本已含于 1139 并集内）；本集封存后已用并集将为 1139＋27＝1166。逐源计数与方法登记于构建报告 `zero_reuse_recheck`。

### 一.1 泄题列单、剔除/递补与特殊登记（全程）

**入选标旗（0 件）**：入选 27 例卡面经逐卡语义通读（见 §四），无成就量级/方向暗示字样（h26 DS-033 型）须照录标旗者。DS 13 例 subject 承台账逐字、仅载身份/场合/断者信息，无财富量级或结局方向字样；启悟/旧池 3 例 subject 承台账 querent 逐字。

**附带登记（不作标旗，2 件）**：

1. **QM-210**：question 承台账逐字，载朋友借贷 50 万元周转、答应今年年底之前全部偿还并给较高利息——系所问「敢不敢借／年底能否按期还款」本身之前提事实（求测时点已知、为占问对象构成），所问结局未载，不作标旗、只登记（承 holdout27 QM-044 失物清单先例）。
2. **QM-211**：question 承台账逐字，载借贷 20 万元、一年后连本带利一次还清、年利率 20%——系所问「敢不敢放／一年后回收顺利否」之前提条款，所问结局未载，不作标旗、只登记。

**排除登记（未入选，1 件）**：

3. **ZCB-003（维持排除）**：台账资格全过、id 未入已用并集，但已经 holdout22 主持裁处判为断语/结局事实入卡并换例剔除；本轮承 PREREG §4 与 STOCK-RECOUNT-h28 §四，裁处未撤销、维持排除。本轮构成无测字段额，本无取例，只登记、不翻案。测字可选存量 0（合格 15－已用 14－本件 1）。

**递补登记（0 件）**：增补件写定五段名单逐例资格断言全过（§二），递补链未触发（DS 段 DS-063、GSZ 段 GSZ-101 起顺延、WHY 段 WHY-025 起顺延；QM 段无递补）；跨段递补未发生；非六爻实成 16 ≥13，组集成立、无停建登记。

**已用剔除（逐 id，同名即剔）**：写定名单本身即 STOCK-RECOUNT-h28 之建卡口径 eligible 未用名单子集，与已用并集 1139 逐 id 对勘零命中，无写定例因同名被剔之事；递补链全名单（DS-063、GSZ 八例、WHY 八例）亦经并集对勘零命中（构建脚本断言）。

**存量见底定案（承 PREREG §4 与增补件 §四，登记）**：**本集为存量内最后一集**。本集取用后 eligible 余量逐项（盘上复算实值，承 STOCK-RECOUNT-h28 §五）：DS **1**（DS-063）／QM **0**（启悟与旧池取尽、开悟与石建国本已归 0）／GSZ 建卡口径 **8**（GSZ-101、103、104、105、107、108、109、110）／WHY **52**（一轮 22＋二轮 30）／非六爻合计 **1**／六爻建卡口径余 60／总余 61。非六爻余 1＜13——非六爻 ≥13 之限度自此不可由现存量满足；其后新鲜封存集组集系于 PREREG §5 expansion 池资格核查工序（自 R84 起开）之产出，或待用户书目（紫微两本等）。此定案只登记、不改本集构成与任何线值。

## 二、资格断言结果（逐例，缺一不可）

27 例逐例断言全过（脚本硬断言：任一例不过即中止建集或按递补链登记；本轮中止零、递补零）：

- **DS-050–062**：台账（SUPPLY-MINING-duanshi-r76.json）逐例 eligible_net＝true、anchor_status＝present、contamination_pre＝low、filters 四项全 pass、master_assertion/outcome 逐字非空——13/13 过。入选 13 例四柱（pillars_verbatim）互异（癸丑庚申庚辰庚辰／壬子丁未戊申己未／己未丙子辛亥甲午／癸巳甲寅甲辰己巳／乙丑乙酉辛亥戊子／壬子癸卯癸卯甲寅／壬申壬寅丙子乙未／庚午甲申甲寅丙寅／己酉丙寅庚午甲申／甲辰庚午庚戌丁亥／庚戌己卯己丑壬申／乙未辛巳壬申庚子／癸亥乙卯戊申丙辰）、无同造重复。断语缺口扫描登记：DS-060 台账摘录段内含「……」省略标记一处，已回原书逐字补入后封（见 §五），余 12 例零命中。
- **QM-210/211（启悟）**：台账（SUPPLY-MINING-qiwu-r76.json）逐例 anchor_status＝present、contamination_pre＝low、separable＝true、断语/结局非空——2/2 过。台账注记登记：QM-210 note 载中宫只印「天禽星 丙」一字同属两集读法、干集完备性通过；QM-211 note 载 2000-10-08 覆测改用大六壬、其应期断语不属本奇门局、金标不采（仅奇门局断语入账）——二例注记全文逐例载于各例金标 grade_note，盘面照台账 input_side.board 逐字入卡（anchors.board）。
- **QM-010（旧池）**：台账（SUPPLY-MINING-qimen-r56.json）anchor_presence＝present、pollution＝low、master_prediction_verbatim/outcome_record 非空，且复核件（QM-REVIEW-r58.json）逐例 eligible_optional＝true、anchor_reviewed＝present、pollution_reviewed＝low——1/1 过。台账注记登记：书中人名小孙/小宋两写并存（司机小孙来电报找到、翻座垫者作小宋），逐字照录不擅改，注记全文载于该例金标 grade_note。
- **GSZ-091/092/093/098/099/100（六爻）**：台账逐例 grade＝A、pollution＝low、anchor_presence＝present、eligible_net＝true、断语/结局非空，且属建卡口径名单（台账 counts 净入账名单∩五要素复核通过集）成员；并逐例回原书文字层（`runs/round76/gsz-book-r76.txt`）以构建脚本同一 five_elements 函数复核锚点五要素——6/6 全在场：
  - GSZ-091（第十四章例五）：本卦雷水解/变卦泽水困；动爻 官鬼申金（应）动；世 妻财辰土、应 官鬼申金；六爻全列六亲纳支；乙亥年丙戌月庚寅日——全在场。
  - GSZ-092（第十四章例六）：水风井变天水讼；动爻 父母子水动、官鬼申金动、官鬼酉金动；世 妻财戌土、应 父母亥水；六亲纳支全列；丁丑年甲辰月甲辰日——全在场。
  - GSZ-093（第十五章例一）：天山遁变水火既济；动爻 父母戌土动、官鬼午火动、父母辰土动；世 官鬼午火、应 兄弟申金；六亲纳支全列；戊寅年甲寅月壬午日——全在场。
  - GSZ-098（第十五章例六）：风地观变水雷屯；动爻 妻财卯木动、父母未土（应）动；世 父母未土、应 父母未土；六亲纳支全列；乙亥年已丑月庚午日（原文「已丑」）——全在场。
  - GSZ-099（第十五章例七）：风天小畜变水天需；动爻 兄弟卯木动；世 父母子水、应 妻财未土；六亲纳支全列；丁丑年丙午月乙酉日——全在场。
  - GSZ-100（第十六章例一）：雷地豫变雷风恒；动爻 兄弟卯木动、子孙巳火动；世 妻财未土、应 子孙午火；六亲纳支全列；丁丑年庚戌月戊戌日——全在场。
- **WHY-012/016/022/023/024（六爻）**：台账（SUPPLY-MINING-wanghuying-r56.json）逐例属 counts 净入账名单（net_eligible_A_low_present 40 例）成员、pollution＝low、anchor_presence＝present、anchor_missing 为空、outcome_record 非空——5/5 过。断语台账未单列字段（缺口整段），已回原书逐字补录后封（见 §五）。

## 三、逐例规格执行与剥离登记（输入卡卫生）

输入卡字段白名单（全 27 卡断言通过）：{id, tradition, subject, context, question, setting, provenance, redistributable, license_status, anchors}（开工先回读 holdout27 任一卡（DS-040）实读字段集对齐、断言一致后写定；键序与 holdout22–27 卡一致）；脚本以禁用键集对 27 张输入卡全字段递归扫描，管理/断语/结局/master/gold/outcome/answer/判级/污染类键零残留（断言通过，落盘后复扫亦零）。provenance 全 27 卡含「用户经学校图书馆提供」、redistributable 全 false。逐例 present_basis（来源定位）即各卡 provenance：DS 13 例＝台账 source（书名＋章章节次＋印刷页/PDF页）；启悟 2 例＝台账 source（篇章章节次＋印刷页/PDF页，卡面省篇首、见下删除清单第 4 条）；旧池 1 例＝台账 source（书名＋类/例＋印刷页）；GSZ 6 例＝台账 source（书名＋章/例）；WHY 5 例＝台账 source（书名＋章/例＋印刷页）。逐例剥离与字段映射全量登记于构建报告 `strip_register`／`field_mapping_notes`，体例如下：

- **DS 13 例**：anchors＝pillars 四柱全列＋pillars_verbatim＋gender（台账 input_side 逐字）；subject←input_side.subject 逐字；setting←台账 source 逐字；context/question 为组写（台账无该二字段，口径同 holdout22–27 并逐例登记）。剥离：anchor_status/anchor_note/contamination_*/separable/transcription/dedup/filters/eligible_net/verdict_note/composition_type/master_assertion/outcome 不入卡。本书「断准」自选偏倚承台账 contamination_note 逐例载入金标 grade_note。
- **启悟 QM 2 例**：anchors＝cast_time_verbatim＋board（input_side 盘面全量逐字，含九宫 palaces/中宫/局式头）；subject←input_side.querent 逐字；context←input_side.context 逐字（QM-211 尾部台账编辑括注删除，见下删除清单第 5 条）；question←input_side.question 逐字；setting←source.section（省篇首，见下删除清单第 4 条）＋cast_time_verbatim 组写；provenance←source 各字段组写。剥离：anchor_status/contamination_pre/contamination_reason/separable/transcription*/dedup/notes/master_assertion/outcome 不入卡。QM-210/QM-211 台账 notes 逐例载入金标 grade_note。
- **旧池 QM-010**：anchors＝cast_time_verbatim＋board（input_fields 盘面全量逐字）；subject←input_fields.querent 逐字；context/question←input_fields 逐字；setting←source.section＋cast_time_verbatim 组写；provenance←source 各字段组写。剥离：pollution*/anchor_presence/anchor_note/dedup_check/notes/master_prediction_verbatim/outcome_record 不入卡。复核件 anchor_basis/pollution_basis 全文载入金标 grade_note。
- **GSZ 6 例**：anchors＝asked_at＋台账 input_fields.chart 全列逐字（本卦/变卦/六爻全列）；context 由 asked_at＋书名组写、setting/provenance 由台账 source 逐字承接（承 holdout22–27 先例）；台账 subject 为空，卡内 subject 作「求测者（台账 subject 为空、原书未具名）」。剥离：pollution*/anchor_presence/anchor_missing/dedup_check/filters/outcome_type/outcome_record/master_prediction 不入卡。
- **WHY 5 例**：anchors＝asked_at＋ben_gua＋bian_gua＋moving_lines＋chart_lines_top_to_bottom（台账 input_fields.chart 全列逐字）；subject 同 GSZ 口径；context 由 asked_at＋书名组写、setting/provenance 由台账 source 逐字承接（承 holdout20 先例）。剥离：pollution/anchor_presence/anchor_missing/dedup_check/transcription/outcome_type/outcome_record 不入卡。

**删除/改写清单（全程逐字登记）**：

1. **节题/问题中性化改写（0 件）**：入选 27 例节题（setting）与 question 逐例核查——GSZ/WHY question 承台账逐字、均只及所问之事；启悟/旧池 question 承台账逐字；DS question/setting 为组写与台账 source 逐字——无一含结局事实，无中性化改写件，登记于构建报告 `hygiene_question_scan` 与 `deletion_register`。
2. **「求测例/求测例题」类编辑装置残段删除（0 件）**：入选 27 例 question 逐例字面扫描（求测例/求測例/求测例题/求測例題）零匹配，无删除件。
3. **双人例 question 中与所问无关之第二人结局字样删除（0 件）**：入选例中涉他人面例（QM-211 妹妹转介借款人、GSZ-092 老乡失联代问、GSZ-098 某妇女测子、GSZ-100 某男测搞对象、WHY-024 学生请测）question 均只及所问之事本身，无第二人无关结局字样，经语义级逐卡通读核查（见 §四），无删除件。
4. **书目篇名篇首省略（2 件，承先例）**：QM-210、QM-211 台账 source.section 篇首「分類占斷篇」为《奇门启悟》本书篇名（含内容级标记集字面「占斷」），承 holdout22–25 启悟建卡先例（QM-203/205/207/209 卡 setting/provenance 均自章次起），卡面 setting/provenance 省略该篇首、自「第十七章」起录；台账原文全量保留于台账与构建报告，非内容删改，逐件登记于构建报告 `deletion_register`。
5. **台账编辑注记括注删除（1 件）**：QM-211 台账 context 尾部括注「（2000 年 10 月 8 日潘氏姐妹再來問何日能還款，劉改用大六壬起課覆測——其應期斷語不屬本奇門局，金標不採，見 notes。）」为台账编辑注记（含「斷語」「金標不採，見 notes」等管理字样），非原书本文，卡面删除、逐字登记于构建报告 `deletion_register`；事实内核（覆测为六壬、其应期不入本局金标）由台账 notes 全量载入金标 grade_note，不影响金标口径。
6. 除上述外本席对卡面未作任何删改；本轮无标旗件待裁（附带登记 2 件见 §一.1，不动卡面）。

## 四、断语扫描三道执行登记

- **第一道（构建脚本内扫描断言）**：(a) 逐字片段扫描——每例 master_prediction 与 outcome_record 的特征片段（标点分句整句（≥8 字）＋去空白 12 字滑动窗口全集）对该例输入卡全文本逐字子串扫描：**结局片段 27 例合计零命中；断语片段 27 例合计零命中**（脚本硬断言）；落盘后对盘上文件重行仍同。(b) 内容级标记扫描（R42 PREREG §5 一级/二级标记集，脚本常量与该节逐字一致）＋字段名黑名单＋禁用键集，全字段递归——27 卡逐卡零命中、合计 0。构建中两处标记命中均为书目/台账编辑字样（启悟 section 篇首「分類占斷篇」之「占斷」、QM-211 台账括注之「斷語」），已经 §三删除清单第 4/5 条按先例与编辑装置口径处置后归零，逐件登记在案、非断语内容入卡。
- **第二道（封存席独立复扫，交卷前执行）**：独立脚本 `runs/round83/scan_holdout28_r83.py`（不 import 构建脚本，按显式 id 清单逐件精确打开盘上卡与金标）重行标记/字段名/禁用键/白名单/片段五项——**全过（pass＝true、failures＝[]）：标记 0、字段名 0、禁用键 0、结局片段 0、断语片段 0**，结果落 `runs/round83/scan-holdout28-result-r83.json`。该脚本附加短片段核（断语 ≥8 字连续子串在卡面出现者逐条登记、仅信息登记）：**零命中**。**语义级通读**：本席已逐卡通读全部 27 张输入卡（转储 `runs/round83/dump-cards-holdout28-r83.txt`），结论为仅含问事、背景与锚点（四柱/局式/卦象），无结局陈述、无断语正文、无成就量级/方向暗示字样；附带登记者二件（QM-210/QM-211 借贷前提，见 §一.1）均系问事前提事实，所问结局未载，不作标旗。
- **第三道（主持验封）**：非本席执行——留位：主持以独立脚本对 `holdout28/inputs/` 全部输入卡复扫（标记集承 R42 PREREG §5），零命中后于本日志追加「验封通过」与金标 SHA 主持第三读结论；本日志不冒充第三道结论。

## 五、断语逐字核验与补录登记（金标）

- **补录 6 例**（断语缺口先回原书逐字补录后封，逐件登记出处）：
  1. **DS-060**（段内缺口）：台账摘录第二段段内含「……」省略标记一处，回原书《段氏理象学》附录三十二、断例几则·二（印刷 pp.218-219，扫描本 PDF 第 242–243 页，200dpi 渲染读图，件存 `runs/round83/ds-pages-h28/`）逐字补入省略跨度「癸水财星代表丑土跑了，犯了经济问题，不是个丢官罢职的事，」——补后该段为「这个命癸未运走坏了，反了局，2008戊子年一定遇到大麻烦，子卯相破，杀星被破，整个局反了。癸水财星代表丑土跑了，犯了经济问题，不是个丢官罢职的事，应该有牢狱之灾！」；余段照台账摘录逐字（多段以／分隔为台账摘录分隔符）。补录后全文缺口扫描「……」零命中。
  2. **WHY-012**：回原书《六爻分类占验技法》第一章「被測日辰」例二（印刷 p23，扫描本 PDF 第 12 页左叶，200dpi 渲染读图，件存 `runs/round83/why-pages-h28/`）逐字补录〔判斷〕全段：「〔判斷〕卦中有動爻，從動爻入手判斷。卦中子孫發動化官鬼，子孫主晴，官鬼主陰，乃是晴轉陰之象。但是子孫不得日月生扶，不能言旺。而官鬼得日月幫比，比子孫要旺得多，是否是晴天見多雲？參考第二天的干支，次日為庚寅日，官鬼受剋子孫得助，應為晴天，有浮雲。」
  3. **WHY-016**：同上，第二章 例四（印刷 p34，扫描本 PDF 第 18 页右叶）〔判斷〕全段逐字补录（兄弟辰土臨螣蛇發動……故斷丑月有小的地震），全文载金标 master_prediction 与构建报告 `gold_supplement`。
  4. **WHY-022**：同上，第三章 水灾例一（印刷 pp.44-46，例文与卦图在 p45、〔判斷〕在 p46，扫描本 PDF 第 23 页左叶与第 24 页右叶）〔判斷〕全段逐字补录（以官鬼為用神……申月必會發生水災）。
  5. **WHY-023**：同上，第三章 水灾例二（印刷 p46，〔判斷〕跨 p46-47，扫描本 PDF 第 24 页右叶至左叶）〔判斷〕全段逐字补录（以官鬼為用神……水災必在午月發生）。
  6. **WHY-024**：同上，第三章 水灾例三（印刷 pp.47-48，〔判斷〕跨 p47-48、应验段在 p48，扫描本 PDF 第 24 页左叶至第 25 页右叶）〔判斷〕全段逐字补录（以官鬼為用神……以酉月的第一個寅日即丙寅日（九月十六日）為洪水退去的應期），含应期段、无跨页遗漏。
  WHY 五例补录体例承 R56 补录席（SUPPLY-GOLD-SUPPLEMENT-r56）与 holdout27 WHY 四例：断语以〔判斷〕起、繁体照原书、应验段不入断语。逐字性以本席 visual 读图转录口径为准，页图件在盘备主持复核；五例应验段经本席回原书逐例核对与台账 outcome_record 一致（WHY-012 次日晴有浮云、WHY-016 丑月丁巳日太原有感地震、WHY-022 申月大水冲倒郊区房屋与公共汽车、WHY-023 午月长江下游特大洪水、WHY-024 九月四日宣布抗洪胜利/九月十一日湖北结束抗洪），**无结局对调/订正件**（OUTCOME_SWAP 为空集，逐件登记于构建报告）。
- **逐字照台账（21 例）**：DS 12 例（台账视觉转录逐字断语、filters 首滤「断语逐字可录」pass，多段以／分隔为台账摘录分隔符，逐例载金标 grade_note；断语缺口扫描「……」零命中，DS-060 除外、已补录如上）；启悟 2 例＋旧池 1 例（台账逐字转录/verbatim 字段、无摘写/省略标记，断语缺口扫描「……」零命中）；GSZ 6 例（文字版 PDF 文字层 verbatim，断语与原书文字层对勘合）。**限度登记**：启悟 2 例与旧池 1 例本席未另读原书页图复核逐字性，其金标 editor_note 已逐例载明「逐字性以台账视觉转录口径为准」，提请主持知悉；页位已逐例载于卡面 provenance。

## 六、验收快照登记（封存时点活 method）

- 快照目录：`runs/round83/kb-snapshot-holdout28/`（自 `benchmark/phase3/method` 复制于封存时点）。**时点锚定**：封存时点活 method 含 calibration 第八节（R80-REV1，已判读成立现行）、第九节（R81-REV1，已标失效存档）、第十节（R82-REV1，现行待判读）与第十一节（R83-REV1，本轮奇门集成落盘于封存之前，集成登记 `method/METHOD-INTEGRATION-r83.md` 在盘），快照即封存时点方法；验收盲测读此快照原件。method/ 根下 `METHOD-DISPOSAL-r81rev1-r82.md`、`METHOD-INTEGRATION-r78.md`、`METHOD-INTEGRATION-r80.md`、`METHOD-INTEGRATION-r81.md`、`METHOD-INTEGRATION-r82.md`、`METHOD-INTEGRATION-r83.md` 六件为登记件、非快照内容件（快照 21 文件口径承历轮），自快照排除并逐件登记如前列。
- 文件数：**21**；逐文件 SHA-256 清单：`runs/round83/kb-snapshot-holdout28-sha256.txt`（21 行，1,923 字节），清单文件 SHA-256＝`1fee120a5d242cbea5c014e2d0a317fe486d2937ca4869ea85ceb8bbd24fe77a`。第十一节在盘核验：快照 `references/calibration.md` 含「## 十一、奇门用神落宫定性复核与应期取径明示核（R83 干预 R83-REV1，奇门段别机制，现行）」节标题（构建脚本断言通过）；快照 calibration.md SHA-256＝`f84294e6e437d34bedf89c2820ddcab3a76684d3f7a91ff3e2f12a037336e53e`、SKILL.md＝`f311e7aa8f70771da767b13d0f7da03367c414529550263b2095c157b5f63234`，与集成登记件（METHOD-INTEGRATION-r83）改后哈希及本席开工盘上实测活 method 哈希逐字一致；快照 SKILL.md 含 (s) 指针行（构建脚本断言通过）。本席另以 sha256sum 逐件对勘：快照 21 文件与活 method 对应文件（除六件登记件外）**逐件全等**。
- 与 R83 平台快照（`runs/round83/kb-snapshot/`）差异自核：**恰为集成文件集 2 件**——`SKILL.md` 与 `references/calibration.md`（即 R83-REV1 集成内容：calibration 新增第十一节＋SKILL 新增 (s) 指针一行，承 `method/METHOD-INTEGRATION-r83.md` 验合登记），余 19 件哈希全同，与增补件 §四预期逐件相符（构建脚本硬断言通过）。平台快照本身与 holdout27 封存快照之既有差异（第九节失效标记）为平台侧登记，不属本快照差异范围。

## 七、封存状态与开封条件（承增补件与 PREREG §2/§4，写死）

- holdout28 自本日志落盘起封存；本轮不开封、不作任何验收预演。金标只许评审角于开封轮打开。
- **本集为 R83-REV1 判读集**：快照锚定封存时点活 method（含 calibration 第八节现行形态、第十节与第十一节）。**开封条件（写死）：封存后首个平台全立轮当轮开封（最早 R84）**。开封前主持复验：金标 SHA-256 与本日志双读读数对勘（主持另做第三读）、输入卡 27 张在盘逐件、主持第三道复扫零命中，结论追记本日志、不另立新档。验收盲测读封存时点快照（§六）；三判据照 R42 PREREG §8（我方均分＞大师均分；低污染子集配对胜多于负；低污染子集配对差＞0；本集全 low，低污染子集＝全集 27，仍分开登记表述）。
- **R83-REV1 判读口径（照 `method/METHOD-INTEGRATION-r83.md` 与提案 §五写死，判读随本集开封验收之同口径诊断执行）**：判读集 holdout28。n＝3 功效处理：奇门段 n＝3，段均分与段配对差在本集只作附读登记、不设判读线、不构成成败或证伪条件；主/副判读改用段内主码计数，全部计数线为 ≤ 口径、恰压线计达标。主指标：奇门段 DIR 主码计数 ≤1（基线：h25 4/10、h26 4/9）；副指标：奇门段 TIM 主码计数 ≤1（基线：h25 2/10、h26 3/9 且实质 3）。护栏甲（防失分换位至 OMIT）：奇门段 OMIT 主码计数 ≤1（基线：h25 1/10、h26 0/9）；护栏乙（防失分换位至 CLAIM）：奇门段 CLAIM 主码计数 ≤1（基线：h25 3/10、h26 2/9）；护栏丙（全集不恶化）：全集总配对差 ≥−1.722；护栏丁（执行面）：奇门段 3 例 reasoning 留痕四行齐备为 3/3，缺痕例不豁免、其 DIR/TIM 主码照常计入主/副指标。附读（不设线）：奇门段配对差与段均分、段 direction＜1.75 附读计数、E5 子类全构成，逐项登记入判读件。三态处置（写死）：① 主/副同达且护栏甲至丁全守 → **成立**，第十一节条文保留生效、(s) 指针保留；② 主/副任一未达或护栏任一破线、且未触证伪线 → **未达未证伪**，条文标失效存档、SKILL 指针处置照历轮未达体例由主持集成件登记；③ 触证伪线 → **证伪**，条文标失效存档，(s) 指针删除回滚。证伪线（任一见即证伪）：(1) 奇门段 DIR 主码计数 ＝3；(2) 奇门段 DIR＋TIM 主码计数 ＝3 且其中 DIR ≥2；(3) 全集总配对差 ≤−1.870。回滚只改 SKILL 指针与条文失效标记，不动任何预测与分数。归因分离（写死）：本判读与第十节判读互不构成对方成败条件；不得以 holdout27 为本判读集、不得借用 holdout27 任何计数作基线或判读来源；第十节在 holdout27 的判读结论不改变本判读口径与计数线，反之亦然；本节不使第八节或第十节复活或失效。判读一次性：只对 holdout28 执行一次，不设顺延判读集、不以 expansion 池未定产出预支后续判读。判读执行轮预注册须逐字重述本口径、不得更改；禁以 holdout28 同集结果回调第十一节条文或本判读任何线值。
- 本回传不作封存依据，以盘上文件＋主持验封（第三道扫描＋金标 SHA 第三读）为准；金标字节若有任何后续变动，须重算 SHA 并在本日志追加记录、原 SHA 作废留痕。
- 中间件登记：WHY 原书页图渲染/裁切件（`runs/round83/why-pages-h28/`）、DS-060 原书页图件（`runs/round83/ds-pages-h28/`）、语义通读转储脚本与转储件（`runs/round83/dump_cards_holdout28_r83.py`、`dump-cards-holdout28-r83.txt`）留 runs/round83/ 内备查，页图件只留盘上未跟踪、不入封存产物；GSZ 五要素复核用原书文字层 `runs/round76/gsz-book-r76.txt` 为既有件、本轮只读；WHY 原书 PDF（`incoming/wanted-books-4/Book/六爻分类占验技法 (王虎应著).pdf`）与段氏原书 PDF（`incoming/wanted-books-5/Book/段氏理象学 (段建业著).pdf`）为既有件、本轮只读。

## 八、主持验封（留位，非本席执行）

- **金标 SHA-256 主持第三读**：留位——主持以独立 sha256sum 复测后追记于此，与本日志双读读数（`e985d5d1552a8583e22297e4e9ee08cc47c3fb797056ec1f8819489d481e3675`，42,736 字节、27 行）对勘，三读一致方为封存定版。
- **第三道（主持独立复扫）**：留位——主持以独立脚本对 27 张输入卡复扫（标记集承 R42 PREREG §5），零命中后追记结论于此。
- **主持裁处待复核二件**：(1) DS-060 断语段内缺口回原书补录（§五第 1 条）——台账摘录含「……」一处，本席按补录体例逐字补入省略跨度后封，未走递补链（DS-060 资格断言逐项全过、缺口非资格项），请主持复核此处置口径；(2) 启悟 section 篇首省略与 QM-211 台账括注删除（§三删除清单第 4/5 条）——均承先例/编辑装置口径处置并逐字登记，请主持验封时一并复核。
- 验封通过后由主持统一提交并打标签 `phase3-round83-holdout28-sealed`（本席未做 git 操作）。

## 九、主持验封（R83 主持，2026-10-31）

- **金标 SHA-256 主持第三读**：`e985d5d1552a8583e22297e4e9ee08cc47c3fb797056ec1f8819489d481e3675`，与构建双读全等——**三读一致，定版**（42,736 字节、27 行）。
- **第三道（主持独立复扫）**：独立脚本 runs/round83/host_scan_h28_r83.py（标记集承 R42 PREREG §5）对 27 张输入卡复扫：**零命中**（结果件 runs/round83/host-scan-h28-result-r83.json）。三道扫描齐备。
- **构成与快照复核**：实成 T＝27（DS 13／启悟 QM 2／旧池 QM 1／GSZ 6／WHY 5；体系 bazi 13／qimen 3／liuyao 11；全 A／low），递补未触发、入选标旗 0 件，主持逐件复核输入卡 27 张在盘、无多余；快照 runs/round83/kb-snapshot-holdout28（21 文件）与活 method 逐件全等（calibration f84294e6e437d34bedf89c2820ddcab3a76684d3f7a91ff3e2f12a037336e53e、SKILL f311e7aa8f70771da767b13d0f7da03367c414529550263b2095c157b5f63234，主持复测一致），锚定 R83-REV1 集成后时点（含第十一节与 (s) 指针），与本轮平台快照差异恰为该集成集两件。
- **主持裁处（待复核二件）**：(1) DS-060 断语缺口回原书逐字补录后封——补录体例为 PREREG §4 写定口径（金标缺口先逐字补录后封），该例资格断言逐项全过、缺口非资格项，不走递补链处置得当，**认可**；(2) 启悟 section 篇首省略（承 holdout22–25 先例）与 QM-211 台账编辑括注逐字删除登记——均有先例与逐字登记，**认可**。
- **验封结论：holdout28 封存成立——存量内最后一集。** 取用后余量实算：DS 1／QM 0／GSZ 建卡 8／WHY 52／非六爻 1。开封条件照 §七：封存后首个平台全立轮（最早 R84）；本集为 R83-REV1 判读集。

## 十、开封前主持复验（R84 主持，2026-10-31）

- 开封条件成就：R84 平台三项全立（全立计 31；(a) −1.084／(b) 四护栏全立／(c) −1.821，analyze_r84 定稿），照 §七写死口径当轮开封。
- **金标 SHA-256 开封再测**：`e985d5d1552a8583e22297e4e9ee08cc47c3fb797056ec1f8819489d481e3675`（42,736 字节、27 行），与 §九主持第三读定版全等，金标字节未动。
- **输入卡 27 张在盘逐件**：`holdout28/inputs/` 实点 27 张，与封存构成（DS-050–062／QM-210、QM-211、QM-010／GSZ-091、092、093、098、099、100／WHY-012、016、022、023、024）逐 id 相符。
- **主持第三道复扫（开封轮）**：独立脚本 runs/round84/host_opening_scan_h28_r84.py（标记集承 R42 PREREG §5，与验封同集）对 27 张输入卡复扫：**零命中**（结果件 runs/round84/host-opening-scan-h28-result-r84.json）。注：该脚本首跑输出路径残留 round83 字面量、结果件误落 runs/round83/，已定点修正路径并移回 runs/round84/ 后重跑复验零命中，round83 目录内无残留件——此件为主持脚本适配小事故，照实登记，不影响扫描结论（两次运行 hits 均为零）。
- 复验结论：三项全过，holdout28 于 R84 开封验收；验收盲测读封存时点快照 runs/round83/kb-snapshot-holdout28，三判据照 R42 PREREG §8，本集同时为 R83-REV1 判读集（口径照 §七写死）。
