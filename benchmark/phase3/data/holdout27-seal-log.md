# holdout27 封存日志（R82 组集封存席，2026-10-31）

**本集已按增补件建成、已封存（T＝27），本轮不开封。** 授权文本：`runs/round82/PREREG-ADDENDUM-r82.md`（组集构成写定，承主预注册 `runs/round82/PREREG.md` §4 与存量复算件 `runs/round82/STOCK-RECOUNT-h27.md`）。配套口径：holdout26 封存定式（`data/holdout26-seal-log.md` 体例）、`runs/round42/PREREG.md` §5（内容级断语扫描标记集）。
产物：`holdout27/inputs/` 27 张输入卡（合计 36,532 字节）；`holdout27/test_gold.jsonl` 27 行金标（40,283 字节）；构建脚本 `runs/round82/build_holdout27_r82.py`（本轮新写唯一名，内含全部资格断言/选集写定/五要素复核/零复用/字段白名单/扫描断言；适配自 holdout26 构建脚本与 holdout20 WHY 建卡段后已 grep 残留轮次字面量逐处核——round81/holdout26 字样仅存于脚本头「承先例/范本」实指引用、字段白名单对齐基准（holdout26 卡实读）与 holdout26 之 27 id 单列零复用对勘，无误伤；适配中途曾有一版 KW 段跨度替换误伤致区块重复，该版未运行、已自原件重做并以计数断言验毕，盘上现行版为重做后定稿）；构建报告 `runs/round82/build-holdout27-report-r82.json`（63,749 字节）；独立复扫脚本 `runs/round82/scan_holdout27_r82.py` 与结果 `runs/round82/scan-holdout27-result-r82.json`（7,135 字节）。探查中间件（只读）：原书页图渲染与裁切件 `runs/round82/why-pages/`（WHY 原书 PDF 第 9–12 页 150dpi 全页渲染与 300dpi 渲染及半叶裁切/缩放读图件）、语义通读转储脚本 `runs/round82/dump_cards_holdout27_r82.py` 及转储件 `runs/round82/dump-cards-holdout27-r82.txt`，均在本轮目录内，未用 /tmp。本席只建卡与封存：不作断、不评分、未开封任何集、未做 git 操作。
**金标 SHA-256 双读一致**：构建脚本 hashlib 输出 `81b1d7c4df8428cb014f6054ac113f24c288f7257fc6437f934ca8ba35ac1295`；本席落盘后独立 `sha256sum` 实测同值 `81b1d7c4df8428cb014f6054ac113f24c288f7257fc6437f934ca8ba35ac1295`（全文 64 位）。双读一致为定版候选；主持再以独立 sha256sum 第三读复核一致后方为封存定版（本席只报双读，第三读留位主持，见 §八）。
**泄题列单先行标出（详见 §一.1）**：入选标旗 **0 件**——逐卡语义通读后无成就量级/方向暗示字样须标旗者；附带登记 2 件（QM-044 包内现金数额、QM-048 购地「花巨资」，均问事前提事实、不作标旗）；排除登记 1 件——ZCB-003（维持排除、未入选，本轮无测字段额）。**照录标旗 1 件（非卡面、系授权文本数）**：增补件 §三「六爻面余 62（GSZ 14＋WHY 57）」分项和为 71、与总数 62 不合，本席照录提请主持勘误（见 §一.1 与 §八）。
**递补未触发**：增补件写定 27 例逐例资格断言全过（见 §二），递补链（DS 段 DS-050 起、开悟跨位 QM-210 起、GSZ 段 GSZ-091 起、WHY 段 WHY-012 起）全程未动用，T＝27 足额，构成限度已断言（见 §一）。

## 一、构成表（增补件 §一写定实成，逐源/逐体系计数）

| 来源 | 例数 | 占比 | 入选 id |
|---|---|---|---|
| 段建业《段氏理象学》 | 9 | 33.3% | DS-040、DS-041、DS-042、DS-043、DS-044、DS-045、DS-046、DS-048、DS-049 |
| 张志春《开悟之门》 | 9 | 33.3% | QM-044、QM-045、QM-046、QM-047、QM-048、QM-049、QM-052、QM-055、QM-058 |
| 王虎应《六爻卦例说真》 | 5 | 18.5% | GSZ-079、GSZ-081、GSZ-084、GSZ-086、GSZ-088 |
| 王虎应《六爻分类占验技法》 | 4 | 14.8% | WHY-008、WHY-009、WHY-010、WHY-011 |
| 合计 | 27 | 100% | 非夷坚 27；测字定额 0、不取例（可选存量 0，见 §一.1） |

| 体系 | 例数 | 占比 |
|---|---|---|
| bazi（八字） | 9 | 33.3% |
| qimen（奇门） | 9 | 33.3% |
| liuyao（六爻） | 9 | 33.3% |
| cezi（测字） | 0 | 0% |

- 构成限度逐项断言（脚本内硬断言、全过）：总量 T＝27 ≥25；单体系最大 9/27＝33.3% ≤50%（计数 ≤13）；单源最大 9/27＝33.3% ≤50%（计数 ≤13；WHY 与 GSZ 分属两书）；非夷坚 27 ≥13；非六爻 18 ≥13；多源构成（四源并存）；污染 low 27/27；仅锚点在场例入选（资格断言见 §二）；与已用并集逐 id 交集＝∅（见下）。
- **例级零复用**：已用并集盘上 id 集实算 **1112 id**（dev 池＝`data/master-baseline-dev9.json` 键集 487＋inputs-dev9/10/11/12 与 inputs 目录卡 id 后 488；phase2 splits2 之 holdout2 29；holdout3–26 各 test_gold.jsonl 仅取 id 字段 700（逐集：h3 27／h4 25／h5 25／h6 23／h7 1／h8 28／h9 28／h10 29／h11 25／h12 49／h13 40／h14 40／h15 40／h16 40／h17 40／h18 30／h19 25／h20 25／h21 25／h22 27／h23 27／h24 27／h25 27／h26 27）；holdout2–26 inputs 与 *-inputs 目录卡 id 541；顶层 inputs6–10 目录卡 id 412（与上多有重合）；五源并集去重后 1112，与主持开轮实算 1112 及供给复算席 STOCK-RECOUNT-h27 一致），选例 27 id 逐 id **零命中**（只对 id 集，未打开任何已封存集金标正文做内容比对）。另对 holdout26 之 27 id 单列对勘：零交集（该 27 id 本已含于 1112 并集内）；本集封存后已用并集将为 1112＋27＝1139。逐源计数与方法登记于构建报告 `zero_reuse_recheck`。

### 一.1 泄题列单、剔除/递补与特殊登记（全程）

**入选标旗（0 件）**：入选 27 例卡面经逐卡语义通读（见 §四），无成就量级/方向暗示字样（h26 DS-033 型）须照录标旗者。DS 9 例 subject 承台账逐字、仅载身份/场合/出生信息，无财富量级或结局方向字样；开悟 9 例 subject 为组写、只及求测者与所问之事。

**附带登记（不作标旗，2 件）**：

1. **QM-044**：context 承台账 input_side 逐字，载失物包内物品清单（大哥大、金穗卡、行车证件、欠款条几万元、现金四千三百元）——系所问失物本身之前提事实（求测时点已知、为占问对象构成），所问能否找到/何时找到之结局未载，不作标旗、只登记。
2. **QM-048**：context 承台账逐字，载科迪公司「花巨资买了一块地皮」与争地经过——系官司之争执标的与前提事实，「巨资」只及其自家购地支出、与断语所断官司胜负方向无涉，不作标旗、只登记。

**排除登记（未入选，1 件）**：

3. **ZCB-003（维持排除）**：台账资格全过、id 未入已用并集，但已经 holdout22 主持裁处判为断语/结局事实入卡并换例剔除；本轮承 PREREG §4 与 STOCK-RECOUNT-h27 §四，裁处未撤销、维持排除。本轮构成无测字段额，本无取例，只登记、不翻案。测字可选存量 0（合格 15－已用 14－本件 1）。

**照录标旗（授权文本数，提请主持勘误，1 件）**：

4. **增补件 §三六爻余数**：增补件载「六爻面余 62（GSZ 14＋WHY 57，台账净资格口径另计）」，其分项 GSZ 14＋WHY 57 合为 **71**，与总数 62 不合。本席按 STOCK-RECOUNT-h27 复算核：建卡口径六爻取用前 80（GSZ 19＋WHY 61），本集取 9（GSZ 5＋WHY 4）后余 **71**（GSZ 14＋WHY 57），分项与增补件所列逐项一致、仅总数 62 与分项和不合。本席照录不自改，提请主持裁处（勘误总数或注明口径）。

**递补登记（0 件）**：增补件写定四段名单逐例资格断言全过（§二），递补链未触发（DS 段 DS-050 起顺延、开悟段同源无递补／跨位 QM-210→QM-211→QM-010、GSZ 段 GSZ-091 起顺延、WHY 段 WHY-012 起顺延）；跨段递补未发生。

**已用剔除（逐 id，同名即剔）**：写定名单本身即 STOCK-RECOUNT-h27 之建卡口径 eligible 未用名单（DS 名单跳过 DS-047——其 contamination_pre＝medium、本不在 eligible 集），与已用并集 1112 逐 id 对勘零命中，无写定例因同名被剔之事。

**存量见底预警（承增补件 §三，登记）**：本集取用后非六爻 eligible 余 **17**（DS 14／QM 3＝启悟 2＋旧池 QM-010 1，开悟已取尽归 0），仅再够一集 T＝27 的非六爻 ≥13 下限（取 13 后余 4）；其后新鲜封存集组集将系于新供给（第五批未到各件或新开采面）。六爻面余 71（GSZ 建卡口径 14＋WHY 57；增补件总数作 62，见上照录标旗）。测字段存量 0 维持。此预警只登记、不改本集构成与任何线值。

## 二、资格断言结果（逐例，缺一不可）

27 例逐例断言全过（脚本硬断言：任一例不过即中止建集；本轮中止零、递补零）：

- **DS-040/041/042/043/044/045/046/048/049**：台账（SUPPLY-MINING-duanshi-r76.json）逐例 eligible_net＝true、anchor_status＝present、contamination_pre＝low、filters 四项全 pass、master_assertion/outcome 逐字非空——9/9 过。入选 9 例四柱（pillars_verbatim）互异（戊申甲寅辛卯癸巳／壬子戊申丁亥己酉／壬子甲辰甲申庚午／癸亥乙丑戊辰癸丑／甲辰丁卯辛未丁酉／乙巳丁亥丙戌己丑／丁酉癸丑壬辰丙午／己酉壬申丙辰戊戌／丙辰丁酉己卯己巳）、无同造重复。台账注记登记：DS-044 verdict_note 载婚姻「名存实亡」为同场言明断语、命主沉默未答，不计入本卡结局，本卡结局以木材生意确认与命主当场落泪为准——全文载于该例金标 grade_note。
- **QM-044/045/046/047/048/049/052/055/058（开悟）**：台账逐例 anchor_status＝present、contamination_pre＝low、separable＝true、stem_check 天盘与地盘**双 ok（全合）**、断语/结局非空——9/9 过。开悟 eligible 未用恰 9 例、本集取全。台账注记登记：QM-052 note 载第二局盘面已经 200dpi 复读核清（坤2 地盘干为壬）、stems 以第二局为校验代表、第三局干集未另列字段，本卡以第二、三局建池（首局格局原书自承被袁校长弄丢）；QM-058 note 载盘面巽4/离9 两宫神名原印同作「天」、疑排印误照录——二例注记全文逐例载于各例金标 grade_note，盘面照台账 input_side 逐字入卡（anchors.board_verbatim）。
- **GSZ-079/081/084/086/088（六爻）**：台账逐例 grade＝A、pollution＝low、anchor_presence＝present、eligible_net＝true、断语/结局非空，且属建卡口径未用名单（STOCK-RECOUNT-h27 §一.6 五要素复核通过 19 例）成员；并逐例回原书文字层（`runs/round76/gsz-book-r76.txt`）以构建脚本同一 five_elements 函数复核锚点五要素——5/5 全在场：
  - GSZ-079（第十二章例六）：本卦乾为天/变卦水天需；动爻 父母戌土（世）动、官鬼午火动；世 父母戌土、应 父母辰土；六爻全列六亲纳支；已卯年戊辰月丙午日（原文「已卯」）——全在场。
  - GSZ-081（第十三章例一）：雷天大壮变火天大有；动爻 兄弟戌土动；世 父母午火、应 妻财子水；六亲纳支全列；戊寅年戊午月甲寅日——全在场。
  - GSZ-084（第十三章例四）：雷天大壮变火天大有；动爻 兄弟戌土动；世 父母午火、应 妻财子水；六亲纳支全列；戊寅年癸亥月戊寅日——全在场。
  - GSZ-086（第十四章例一）：火山旅变艮为山；动爻 妻财酉金（应）动；世 子孙辰土、应 妻财酉金；六亲纳支全列；丙子年壬辰月乙酉日——全在场。
  - GSZ-088（第十四章例三）：天山遁变天地否；动爻 兄弟申金动；世 官鬼午火、应 兄弟申金；六亲纳支全列；已卯年已巳月庚辰日（原文「已卯年已巳月」）——全在场。
- **WHY-008/009/010/011（六爻）**：台账（SUPPLY-MINING-wanghuying-r56.json）逐例属 counts 净入账名单（net_eligible_A_low_present 40 例）成员、pollution＝low、anchor_presence＝present、anchor_missing 为空、outcome_record 非空——4/4 过。断语台账未单列字段（缺口整段），已回原书逐字补录后封（见 §五）。

## 三、逐例规格执行与剥离登记（输入卡卫生）

输入卡字段白名单（全 27 卡断言通过）：{id, tradition, subject, context, question, setting, provenance, redistributable, license_status, anchors}（开工先回读 holdout26 任一卡（DS-031）实读字段集对齐、断言一致后写定；键序与 holdout22–26 卡一致）；脚本以禁用键集对 27 张输入卡全字段递归扫描，管理/断语/结局/master/gold/outcome/answer/判级/污染类键零残留（断言通过，落盘后复扫亦零）。provenance 全 27 卡含「用户经学校图书馆提供」、redistributable 全 false。逐例 present_basis（来源定位）即各卡 provenance：DS 9 例＝台账 source（书名＋章章节次＋印刷页/PDF页）；开悟 9 例＝台账 source（下编章章节次＋印刷页）；GSZ 5 例＝台账 source（书名＋章/例）；WHY 4 例＝台账 source（书名＋章/例＋印刷页）。逐例剥离与字段映射全量登记于构建报告 `strip_register`／`field_mapping_notes`，体例如下：

- **DS 9 例**：anchors＝pillars 四柱全列＋pillars_verbatim＋gender（台账 input_side 逐字）；subject←input_side.subject 逐字；setting←台账 source 逐字；context/question 为组写（台账无该二字段，口径同 holdout22–26 并逐例登记）。剥离：anchor_status/anchor_note/contamination_*/separable/transcription/dedup/filters/eligible_net/verdict_note/composition_type/master_assertion/outcome 不入卡。本书「断准」自选偏倚承台账 contamination_note 逐例载入金标 grade_note。
- **开悟 QM 9 例**：anchors＝board_verbatim（input_side 盘面段逐字；QM-052 第二、三局两局盘面全载）＋stems_tianpan/stems_dipan＋stem_check；context←input_side 盘面之前段逐字；question←input_side 原文子串（脚本断言子串在场；QM-045 例外：原文未逐字引问句，question 为组写、已逐例登记）；subject 为组写（据 input_side 与 caster 组写，登记于构建报告）；setting←source＋caster 组写。剥离：topic/anchor_status/contamination_pre/separable/transcription/dedup/master_assertion/outcome 不入卡。QM-052/QM-058 台账 note 逐例载入金标 grade_note。
- **GSZ 5 例**：anchors＝asked_at＋台账 input_fields.chart 全列逐字（本卦/变卦/六爻全列）；context 由 asked_at＋书名组写、setting/provenance 由台账 source 逐字承接（承 holdout22–26 先例）；台账 subject 为空，卡内 subject 作「求测者（台账 subject 为空、原书未具名）」。剥离：pollution*/anchor_presence/anchor_missing/dedup_check/filters/outcome_type/outcome_record/master_prediction 不入卡。
- **WHY 4 例**：anchors＝asked_at＋ben_gua＋bian_gua＋moving_lines＋chart_lines_top_to_bottom（台账 input_fields.chart 全列逐字）；subject 同 GSZ 口径；context 由 asked_at＋书名组写、setting/provenance 由台账 source 逐字承接（承 holdout20 先例）。剥离：pollution/anchor_presence/anchor_missing/dedup_check/transcription/outcome_type/outcome_record 不入卡。

**删除/改写清单（全程逐字登记）**：

1. **节题/问题中性化改写（0 件）**：入选 27 例节题（setting）与 question 逐例核查——GSZ/WHY question 承台账逐字、均只及所问之事；KW question 为原文子串或登记组写；DS question/setting 为组写与台账 source 逐字——无一含结局事实，无中性化改写件，登记于构建报告 `hygiene_question_scan` 与 `deletion_register`。
2. **「求测例/求测例题」类编辑装置残段删除（0 件）**：入选 27 例 question 逐例字面扫描（求测例/求測例/求测例题/求測例題）零匹配，无删除件。
3. **双人例 question 中与所问无关之第二人结局字样删除（0 件）**：入选例中涉他人面例（QM-049 妻为夫求测、GSZ-081 某女代占其子、GSZ-084 某女代占其母、WHY-008 日本学生自测）question 均只及所问之事本身，无第二人无关结局字样，经语义级逐卡通读核查（见 §四），无删除件。
4. 除上述外本席对卡面未作任何删改；本轮无标旗件待裁（附带登记 2 件见 §一.1，不动卡面）。

## 四、断语扫描三道执行登记

- **第一道（构建脚本内扫描断言）**：(a) 逐字片段扫描——每例 master_prediction 与 outcome_record 的特征片段（标点分句整句（≥8 字）＋去空白 12 字滑动窗口全集）对该例输入卡全文本逐字子串扫描：**结局片段 27 例合计零命中；断语片段 27 例合计零命中**（脚本硬断言）；落盘后对盘上文件重行仍同。(b) 内容级标记扫描（R42 PREREG §5 一级/二级标记集，脚本常量与该节逐字一致）＋字段名黑名单＋禁用键集，全字段递归——27 卡逐卡零命中、合计 0。
- **第二道（封存席独立复扫，交卷前执行）**：独立脚本 `runs/round82/scan_holdout27_r82.py`（不 import 构建脚本，按显式 id 清单逐件精确打开盘上卡与金标）重行标记/字段名/禁用键/白名单/片段五项——**全过（pass＝true、failures＝[]）：标记 0、字段名 0、禁用键 0、结局片段 0、断语片段 0**，结果落 `runs/round82/scan-holdout27-result-r82.json`。该脚本附加短片段核（断语 ≥8 字连续子串在卡面出现者逐条登记、仅信息登记）：**零命中**（本轮无 h26 型问句复现短片段）。**语义级通读**：本席已逐卡通读全部 27 张输入卡（转储 `runs/round82/dump-cards-holdout27-r82.txt`），结论为仅含问事、背景与锚点（四柱/局式/卦象），无结局陈述、无断语正文、无成就量级/方向暗示字样；附带登记者二件（QM-044 失物清单与 QM-048 购地前提，见 §一.1）均系问事前提事实，所问结局未载，不作标旗。
- **第三道（主持验封）**：非本席执行——留位：主持以独立脚本对 `holdout27/inputs/` 全部输入卡复扫（标记集承 R42 PREREG §5），零命中后于本日志追加「验封通过」与金标 SHA 主持第三读结论；本日志不冒充第三道结论。

## 五、断语逐字核验与补录登记（金标）

- **补录 4 例**（断语缺口先回原书逐字补录后封，逐件登记出处；WHY 段台账未单列断语字段、缺口即整段）：
  1. **WHY-008**：回原书《六爻分类占验技法》第一章「順風和逆風」例二（印刷 pp.18-19，〔判斷〕在 p19，扫描本 PDF 第 10 页左叶，300dpi 渲染读图，件存 `runs/round82/why-pages/`）逐字补录〔判斷〕全段：「〔判斷〕世爻辰土為水庫，在水池或湖邊清理環境垃圾。世爻得日辰比扶旺相，卦中兄弟卯木、寅木兩動剋世，又在巽宮，乃是逆風，外出勞動定受風吹之苦。」
  2. **WHY-009**：同上，第一章「五行」例一（印刷 p20，扫描本 PDF 第 11 页右叶）〔判斷〕全段逐字补录（卦中有動爻出現……因此次日天氣當為雷雨天氣），全文载金标 master_prediction 与构建报告 `gold_supplement`。
  3. **WHY-010**：同上，第一章「五行」例二（印刷 p21，扫描本 PDF 第 11 页左叶）〔判斷〕全段逐字补录（卦中有動爻……本日天氣當為晴轉陰有像霧一樣的濛濛小雨，且有雷聲）。
  4. **WHY-011**：同上，第一章「被測日辰」例一（印刷 pp.21-22，〔判斷〕在 p22，扫描本 PDF 第 12 页右叶）〔判斷〕全段逐字补录（卦中有動爻……父母動而化出兄弟，乃是有風有雨）。
  WHY 四例补录体例承 R56 补录席（SUPPLY-GOLD-SUPPLEMENT-r56）：断语以〔判斷〕起、繁体照原书、应验段不入断语。逐字性以本席 visual 读图转录口径为准，页图件在盘备主持复核；四例应验段经本席回原书逐例核对与台账 outcome_record 一致（WHY-008 湖畔顶风、WHY-009 次日丑时起雨、WHY-010 上午晴未时转阴、WHY-011 次日上午阴九点小雨），**无结局对调/订正件**（OUTCOME_SWAP 为空集，逐件登记于构建报告）。
- **逐字照台账（23 例）**：DS 9 例（台账视觉转录逐字断语、filters 首滤「断语逐字可录」pass，多段以／分隔为台账摘录分隔符，逐例载金标 grade_note；断语缺口扫描「……」零命中）；开悟 9 例（台账逐字转录、无摘写/省略标记，断语缺口扫描「……」零命中）；GSZ 5 例（文字版 PDF 文字层 verbatim，断语与原书文字层对勘合）。**限度登记**：开悟 9 例本席未另读原书页图复核逐字性，其金标 editor_note 已逐例载明「逐字性以台账视觉转录口径为准」，提请主持知悉；页位已逐例载于卡面 provenance。

## 六、验收快照登记（封存时点活 method）

- 快照目录：`runs/round82/kb-snapshot-holdout27/`（自 `benchmark/phase3/method` 复制于封存时点）。**时点锚定**：封存时点活 method 含 calibration 第八节（R80-REV1，已判读成立现行）、第九节（R81-REV1，现行待判读）与第十节（R82-REV1，本轮集成落盘于封存之前，集成登记 `method/METHOD-INTEGRATION-r82.md` 在盘），快照即封存时点方法；验收盲测读此快照原件。method/ 根下 `METHOD-INTEGRATION-r78.md`、`METHOD-INTEGRATION-r80.md`、`METHOD-INTEGRATION-r81.md`、`METHOD-INTEGRATION-r82.md` 为集成登记件、非快照内容件（快照 21 文件口径承历轮），自快照排除并逐件登记。
- 文件数：**21**；逐文件 SHA-256 清单：`runs/round82/kb-snapshot-holdout27-sha256.txt`（21 行，1,923 字节），清单文件 SHA-256＝`f08175c74d3784bd3c8b49b31f1174a2fbdd33376ef75efd80fd1af463f9c7fa`。第十节在盘核验：快照 `references/calibration.md` 含「## 十、具体断项反向限定扫查与主张范围收束核（R82 干预 R82-REV1，跨体系断项范围机制）」节标题（构建脚本断言通过）；快照 calibration.md SHA-256＝`9676a64a0ff997e77a76117346e62a37db315af292c0a6411db5a970ce4d6094`、SKILL.md＝`c43cb065341c61c9106e1a79115b5313bf8e9d1f101776f8e3aacca167ae072c`，与集成登记件（METHOD-INTEGRATION-r82）改后哈希逐字一致。本席另以 sha256sum 逐件对勘：快照 21 文件与活 method 对应文件（除四件集成登记件外）**逐件全等**。
- 与 R82 平台快照（`runs/round82/kb-snapshot/`）差异自核：**恰为集成文件集 2 件**——`SKILL.md` 与 `references/calibration.md`（即 R82-REV1 集成内容：calibration 新增第十节＋SKILL 新增 (r) 指针一行，承 `method/METHOD-INTEGRATION-r82.md` 验合登记），余 19 件哈希全同，与增补件 §二预期逐件相符（构建脚本硬断言通过）。

## 七、封存状态与开封条件（承增补件与 PREREG §2/§4，写死）

- holdout27 自本日志落盘起封存；本轮不开封、不作任何验收预演。金标只许评审角于开封轮打开。
- **本集为 R82-REV1 判读集**：快照锚定封存时点活 method（含 calibration 第八节现行形态、第九节与第十节）。**开封条件（写死）：封存后首个平台全立轮当轮开封（最早 R83）**。开封前主持复验：金标 SHA-256 与本日志双读读数对勘（主持另做第三读）、输入卡 27 张在盘逐件、主持第三道复扫零命中，结论追记本日志、不另立新档。验收盲测读封存时点快照（§六）；三判据照 R42 PREREG §8（我方均分＞大师均分；低污染子集配对胜多于负；低污染子集配对差＞0；本集全 low，低污染子集＝全集 27，仍分开登记表述）。
- **R82-REV1 判读口径（照 `method/METHOD-INTEGRATION-r82.md` 与提案 §六写死，判读随本集开封验收之同口径诊断执行）**：判读基线为 holdout25 聚合（CLAIM 主码率 9/27≈0.333、DIR 主码率 10/27≈0.370、TIM 实质主码率 0/27＝0.000、OMIT 主码率 3/27≈0.111、E4 主码率 2/27≈0.074、总配对差 −1.417；次码层只作附读基线分层登记：TIM 次实质 8、CLAIM 次 6）。N 口径：实成 N≥20 方判读（本集 N＝27），按实成 N 以率线折算计数（计数上限取 ⌊率×N⌋、证伪计数取 ⌈率×N⌉）；若实成 N＜20 顺延至其后首个 N≥20 的新鲜封存验收集，线值不变。主指标：CLAIM 主码率 ≤0.167（N＝27 时计数 ≤4）；副指标（位移护栏性质）：TIM 实质主码率 ≤0.080（计数 ≤2；实质口径：TIM 剔除轻级与零级后计）；护栏：DIR 主码率 ≤0.385（计数 ≤10）、OMIT 主码率 ≤0.160（计数 ≤4）、E4 主码率 ≤0.160（计数 ≤4）、总配对差 ≥−1.837，任一护栏破线即判读不成立；证伪线：CLAIM 主码率 ≥0.444（计数 ≥12）或总配对差 ≤−2.834，任一见即证伪。计数线为 ≤ 口径（证伪线为 ≥ 口径），实测恰压线值计达标（证伪线恰压计触线），照实登记。三态处置（写死）：① 主/副同达且护栏全守 → **成立**，第十节条文保留生效、(r) 指针保留；② 未达且未触证伪线 → **未达未证伪**，条文标失效存档、原文保留备查，(r) 指针保留；③ 触证伪线 → **证伪**，条文标失效存档，(r) 指针删除回滚。回滚只改 SKILL 指针与条文失效标记，不动任何预测与分数。附读（只登记）：本核执行形态计数（受扫查非量级断项总数、有限定信号收束例数、无限定未动作例数）、次码层计数分层登记（TIM 次实质、CLAIM 次）、E3-A 涉计数外溢登记、奇门段配对差与段内 direction<1.75 例数、DS 段配对差。判读执行轮预注册须逐字重述本口径、不得更改；禁以 holdout27 同集结果回调第十节条文或本判读任何线值；本判读与第九节判读互不借用（DIR 率归第九节判读集 holdout26、本节只作护栏；CLAIM 率不入第九节判读），成败只处置第十节条文与 (r) 指针，不及第八节与第九节。
- 本回传不作封存依据，以盘上文件＋主持验封（第三道扫描＋金标 SHA 第三读）为准；金标字节若有任何后续变动，须重算 SHA 并在本日志追加记录、原 SHA 作废留痕。
- 中间件登记：原书页图渲染/裁切件（`runs/round82/why-pages/`）、语义通读转储脚本与转储件（`runs/round82/dump_cards_holdout27_r82.py`、`dump-cards-holdout27-r82.txt`）留 runs/round82/ 内备查；GSZ 五要素复核用原书文字层 `runs/round76/gsz-book-r76.txt` 为既有件、本轮只读；WHY 原书 PDF（`incoming/wanted-books-4/Book/六爻分类占验技法 (王虎应著).pdf`）为既有件、本轮只读。

## 八、主持验封（留位，非本席执行）

- **金标 SHA-256 主持第三读**：留位——主持以独立 sha256sum 复测后追记于此，与本日志双读读数（`81b1d7c4df8428cb014f6054ac113f24c288f7257fc6437f934ca8ba35ac1295`，40,283 字节、27 行）对勘，三读一致方为封存定版。
- **第三道（主持独立复扫）**：留位——主持以独立脚本对 27 张输入卡复扫（标记集承 R42 PREREG §5），零命中后追记结论于此。
- **主持裁处待复核一件**：增补件 §三六爻余数「62」与分项和 71 不合之照录标旗（§一.1 第 4 条）——请主持勘误或注明口径；本集构成与封存不受其影响。
- 验封通过后由主持统一提交并打标签 `phase3-round82-holdout27-sealed`（本席未做 git 操作）。

## 九、主持验封（R82 主持，2026-10-31）

- **金标 SHA-256 主持第三读**：`81b1d7c4df8428cb014f6054ac113f24c288f7257fc6437f934ca8ba35ac1295`，与构建双读全等——**三读一致，定版**（40,283 字节、27 行）。
- **第三道（主持独立复扫）**：独立脚本 runs/round82/host_scan_h27_r82.py（标记集承 R42 PREREG §5）对 27 张输入卡复扫：**零命中**（结果件 runs/round82/host-scan-h27-result-r82.json）。三道扫描齐备。
- **主持裁处（增补件算术勘误）**：PREREG-ADDENDUM-r82 §三「六爻面余 62（GSZ 14＋WHY 57）」分项和为 71、总数 62 系主持笔误；按 STOCK-RECOUNT-h27 复算与封存后余数实算（GSZ 建卡口径余 14、WHY 余 57，合计 **71**；总存量 115−27＝88＝DS 14＋QM 3＋六爻 71，勾稽一致），**裁定总数订正为 71**，增补件原文不改、勘误以本节与增补件尾部勘误注为准。组集席照录标旗处置得当。
- **构成与快照复核**：实成 T＝27（DS 9／开悟 QM 9／GSZ 5／WHY 4），递补未触发、标旗 0 件；快照 runs/round82/kb-snapshot-holdout27 与活 method 逐件全等（calibration 9676a64a…、SKILL c43cb065…，主持复测一致），与平台快照差异恰两件（R82-REV1 集成差异）。
- **验封结论：holdout27 封存成立。** 开封条件照 §七：封存后首个平台全立轮（最早 R83）；本集为 R82-REV1 判读集。
