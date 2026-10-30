# holdout21 封存日志（R58 建集数据席，2026-10-31）

**本集已按附则建成、已封存（T＝25），本轮不开封。** 授权文本：`runs/round58/PREREG-ADDENDUM.md`（选集 25 例写死＋建集/验封口径，本任务唯一授权文本）。配套口径：holdout20 封存定式（`data/holdout20-seal-log.md` 体例与检查清单）、`runs/round42/PREREG.md` §5（内容级断语扫描标记集）。
产物：`holdout21/inputs/` 25 张输入卡；`holdout21/test_gold.jsonl` 25 行金标；构建脚本 `runs/round58/build_holdout21_r58.py`（本轮新写唯一名，内含资格断言/例数/id 集/零复用/字段白名单/扫描断言）；构建报告 `runs/round58/build-holdout21-report-r58.json`。本席只建卡与封存：不作断、不评分、未开封验收、未做 git 操作。
**金标 SHA-256：`ea4d9315bfffd2f02fc7aed8f9e6a2ac04924bfa89d4545e08830287e447fb72`**（构建脚本 hashlib 输出、脚本外独立 `sha256sum` 实测、本日志落盘后回读复算，三读一致；**待主持以独立 sha256sum 再行复核**，主持复核一致后方为封存定版读数）。
**回退规则未触发**：25 例资格断言全过（见 §二），无一例停例、无替补；附则 §二 QW 补录前置已由补录件完成（5／5 成功、无顺位替补需求，见 §五）。

## 一、构成表（附则 §一写死，逐源/逐体系计数）

| 来源 | 例数 | 占比 | 入选 id |
|---|---|---|---|
| 王虎应《六爻卦例说真》 | 6 | 24.0% | GSZ-003、GSZ-005、GSZ-009、GSZ-015、GSZ-016、GSZ-017 |
| 王虎应《六爻分类占验技法》（二轮） | 6 | 24.0% | WHY-072、WHY-073、WHY-074、WHY-075、WHY-078、WHY-079 |
| 曲炜《详批命例精解》 | 5 | 20.0% | QW-013、QW-014、QW-015、QW-016、QW-017 |
| 杜新会《奇门遁甲现代实例精解》 | 5 | 20.0% | QM-001、QM-002、QM-003、QM-004、QM-005 |
| 张志春《神奇之门——奇门遁甲大解谜》 | 3 | 12.0% | QM-006、QM-007、QM-008 |
| 合计 | 25 | 100% | 非夷坚 25 |

| 体系 | 例数 | 占比 |
|---|---|---|
| liuyao（六爻） | 12 | 48.0% |
| bazi（八字） | 5 | 20.0% |
| qimen（奇门） | 8 | 32.0% |

- 构成复核（承附则 §一）：六爻 12（48%）≤50%；非六爻 13 ≥13；非夷坚 25；单源最大 6（24%）≤50%。全例 A 级、contamination＝low、锚点在场（资格断言见 §二）。
- **例级零复用**：本席脚本复核——已用并集 **952 id**（phase2 splits2 之 holdout2 29；holdout3–20 各 test_gold.jsonl 仅取 id 字段 540；holdout2–20 inputs 与 *-inputs 目录卡 id 381；dev 池＝data/master-baseline-dev9.json 键集＋inputs-dev9/10/11/12 与 inputs 目录卡 id 488；四源并集去重后 952），选例 25 id 逐 id **零命中**（只对 id 集，未打开任何已封存集金标正文做内容比对）。逐源计数与方法登记于构建报告 `zero_reuse_recheck`。

## 二、资格断言结果（逐例，缺一不可）

25 例逐例断言全过（脚本断言：任一例不过即中止建集；本轮无中止、无替补）：

- **GSZ-003/005/009/015/016/017**：台账（SUPPLY-MINING-guaishuo-r57.json）逐例 grade＝A、pollution＝low、anchor_presence＝present、eligible_net＝true、master_prediction 逐字非空、outcome_record 非空——6／6 过。
- **WHY-072/073/074/075/078/079**：台账（SUPPLY-MINING-wanghuying-r57-r2.json）同上六项——6／6 过。
- **QW-013/014/015/016/017**：台账（SUPPLY-MINING-quwei-r56.json）pollution＝low、anchor_presence＝present、filters 四项（verbatim_transcribable／independent_outcome／separable／pollution_non_high）全 pass、outcome_record 非空；grade A 承附则 §一「全例 A 级」（台账无 grade/eligible_net 字段，同源 QW-001–012 已于 holdout20 以 A 级建卡）；master_prediction 以补录件（data/holdout21-gold-supplement.md）逐字为准、5 例全非空，且补录件断语字数自检与登记字数相符（含换行口径：QW-013 2151、QW-014 3305、QW-015 3069、QW-016 3649、QW-017 1550）；台账 outcome_record 各段逐段见于补录件结局块、交叉核对一致——5／5 过。
- **QM-001–008**：复核件（QM-REVIEW-r58.json）逐例 eligible_optional＝true、pollution_reviewed＝low、anchor_reviewed＝present，且台账（SUPPLY-MINING-qimen-r56.json）pollution＝low、anchor_presence＝present、master_prediction_verbatim 逐字非空、outcome_record 非空——8／8 过。（QM-009 pollution＝mid、QM-010 未入附则选集，均未入本集。）

## 三、逐例规格执行与剥离登记（输入卡卫生）

输入卡字段白名单（全 25 卡断言通过）：{id, tradition, subject, context, question, setting, provenance, redistributable, license_status, anchors}；脚本以禁用键集对 25 张输入卡全字段递归扫描，管理与断语/结局/判级/污染字段零残留（断言通过，落盘后复扫亦零）。input_side 无 outcome、master_prediction 及任何断语/结局类字段。

- **六爻 12 例（GSZ/WHY）**：anchors＝asked_at＋台账 input_fields.chart 全列逐字（六爻锚点：卦象逐字——本卦/变卦/动爻（WHY 台账有 moving_lines、GSZ 台账动爻载于卦爻行内）/六爻全列/伏神（有则））。台账无 context/setting/provenance 独立字段：context 由 asked_at＋书名组写、setting/provenance 由台账 source 逐字承接（承 holdout20 WHY 组写先例，组写口径逐例登记于构建报告 field_mapping_notes）；台账 subject 为空，卡内 subject 作「求测者（台账 subject 为空、原书未具名）」。剥离：pollution/pollution_note/anchor_presence/anchor_missing/dedup_check/filters/outcome_type/outcome_record/master_prediction 不入卡。
- **八字 5 例（QW）**：anchors＝birth 四元组＋sex（birth_info_verbatim/gender/pillars/day_master，承 holdout20 QW 口径）；台账 input_fields 逐字建卡（嵌套子字段经字段映射摊平、子字段文本逐字，映射口径逐例登记于构建报告）。剥离：pollution/pollution_note/anchor_presence/anchor_note/dedup_check/filters/outcome_record 不入卡。成色承台账逐字：作者自选「断准」集、结局命主自报无第三方核实（选择偏倚明示，逐例载金标 grade_note）；QW-017 结局成色薄（outcome_note 逐字承接金标 grade_note）。
- **奇门 8 例（QM）**：anchors＝cast_time_verbatim＋board/boards 全载逐字（奇门锚点：局式逐字——header_verbatim 局式头＋九宫 palaces＋center_palace_5；QM-004 双局并载、QM-003 另载 board_basis＝event_time）。subject←querent，question/context←input_fields 逐字，setting←书名/著者/章节＋起局时间组写。剥离：pollution/pollution_reason/anchor_presence/anchor_note/dedup_check/notes/master_prediction_verbatim/outcome_record 不入卡。
- **QM-007 附条件改写（1 例，承 holdout20 附条件改写先例）**：台账 context 原文嵌伤情细节（尾椎骨摔伤、大小便失禁——张断后由小郑证实者）及台账自带「不入输入侧背景以免泄断」注记句，台账 notes 同旨。本席按台账注记删此细节与注记句：改前 context＝「1996年5月9日下午4点20分，小郑来测侄子摔伤（尾椎骨摔伤、大小便失禁、已手术）之预后与出院时间；伤情细节为张断后由小郑证实者（「从电线杆上掉下来、把尾椎骨摔伤了」），不入输入侧背景以免泄断。」→ 改后＝「1996年5月9日下午4点20分，小郑来测侄子摔伤之预后与出院时间。」改写前后对照存证于构建报告 `qm007_rewrite`，原台账不动；question 原文既载的求测者自述（电线杆摔伤入院、昨天刚做手术）不动。

## 四、断语扫描三道执行登记

- **第一道（脚本逐字子串扫描）**：每例 master_prediction 与 outcome_record 的特征片段（标点分句整句（≥8 字）＋去空白 12 字滑动窗口全集）对该例输入卡全文本逐字子串扫描——**25 例合计零命中**（逐例片段数与结果在构建报告 `scan1_verbatim_fragment`）；落盘后对盘上文件重行仍零命中。另行 h20 第二道口径卫生自校验（R42 PREREG §5 内容级一级/二级标记＋字段名黑名单＋禁用键集，全字段递归）——25 卡逐卡零命中、合计 0。
- **第二道（语义级抽查，9 例 ≥8）**：建集席逐例通读输入卡确认无结局/断语泄漏——名单：GSZ-003、GSZ-016、WHY-072、WHY-079、QW-013、QW-016、QM-001、QM-004、QM-007。逐卡结论：仅含问事、背景与锚点（卦象/四柱/局式），无断语正文、无结局陈述；QW 两卡 context 之「命主事后逐项反馈」为函测形式说明、非结局内容；QM-007 改写后卡已无张断后证实细节（见 §三）。**一处标旗**：QM-004 的 setting/provenance 含原书节题「巳时停电，申时来电」（正文标题作「巳时停电，申时复电」），系台账 source.section 出处著录逐字、属书目信息而非断语正文，本席照台账逐字保留并在此标旗，提请主持知悉裁处。
- **第三道（主持验封）**：非本席执行——留位：主持以独立脚本对 `holdout21/inputs/` 全部输入卡复扫（逐字片段＋内容级标记），零命中后于本日志追加「验封通过」与金标 SHA 主持双读结论；本日志不冒充第三道结论。

## 五、补录注记承接（QW 断语，附则 §二）

- 断语逐字来源：`data/holdout21-gold-supplement.md`（补录席自源 TXT《详批命例精解》逐例提取，transcription=verbatim、confidence=0.95，5／5 成功）；金标 outcome_record 取台账逐字（与补录件结局块交叉核对一致，见 §二）。
- **成色注记一（行号口径，全 QW 例适用，已逐例登记于金标 editor_note）**：台账 provenance.location 行号为折行计数口径，与源 TXT 物理行号不一致；定位以补录件物理行号＋唯一锚句为准；源文件 SHA-256 与台账登记一致、确为同一文件。金标 provenance 字段并列登记断语出处（补录件物理行号区间）与台账 provenance 原文。
- **成色注记二（QW-016 编号复原，已登记于该行 editor_note）**：QW-016 性格第 8 条原文误标「释：」起头，补录席按断语回收、复原编号「8、」（编号序列 7→9 间缺 8）；建集只登记、不改断语正文，金标 master_prediction 与补录件逐字一致。
- QW-013 条内夹注照录、节次「七、」直跳「九、」等原文形态，均承补录件注记照录，金标不另改。

## 六、验收快照登记（封存时点活 method）

- 快照目录：`runs/round58/kb-snapshot-holdout21/`（自 `benchmark/phase3/method` 全目录复制于封存时点）。
- 文件数：**21**（不含清单文件本身）；逐文件 SHA-256 清单：`runs/round58/kb-snapshot-holdout21/sha256.txt`（21 行）；本席已以 `sha256sum -c` 对清单全量复验，21／21 OK。

## 七、封存状态与开封条件（承附则 §三，写死）

- holdout21 自本日志落盘起封存；本轮不开封、不作任何验收预演。金标只许评审角于开封轮打开。
- **开封条件（写死）：封存后首个平台全立轮开封**；开封轮预注册先行，验收快照锚定本封存时点活 method（§六快照）。开封执行与三判据照 R42 PREREG §8 与附则 §四（达标→打包 final-skill-v2（2.0.0）收官；未达标→标已用、诊断后续链）。
- 本回传不作封存依据，以盘上文件＋主持验封（第三道扫描＋金标 SHA 双读）为准；金标字节若有任何后续变动，须重算 SHA 并在本日志追加记录、原 SHA 作废留痕。

## §五 主持裁处与验封（R58 主持，2026-10-31）

- **QM-004 节题裁处（建集席 §四标旗）**：原书节题「巳时停电，申时来电」（正文标题作「巳时停电，申时复电」）中「申时复电」为结局事实（实际复电时辰），虽属书目著录形态，仍属输入侧结局内容，主持裁定**剔除**：输入卡 QM-004 的 setting 与 provenance 已删去节题引文、改为中性定位（第十六类「故障出在何方」例8＋印刷页 427-429），provenance 内留剔除注记一行。改写前后全文对照存 runs/round58/build-holdout21-report-r58.json 同批主持记录（本节即登记源）。**金标与台账未动**，金标 SHA 不受影响（见下复核）。QM-007 附条件改写（台账注记授权、承 holdout20 先例）主持复核成立，不另裁。
- **主持第三道复扫（扫描③）**：runs/round58/rescan_inputs_h21_host_r58.py 独立实现——金标断语＋结局特征片段（整句＋12 字窗口）对 25 张输入卡全文本 **0 命中**；内容级标记扫描（R42 PREREG §5 口径）**0 命中**；QM-004 三探针（申时来电／申时复电／巳时停电）全数不在卡内。**验封通过。**
- **金标 SHA 主持复核**：sha256sum 盘上实测 ea4d9315bfffd2f02fc7aed8f9e6a2ac04924bfa89d4545e08830287e447fb72，与建集席三读定版一致。
- 开封条件维持写死：封存后首个平台全立轮开封，验收快照锚定 runs/round58/kb-snapshot-holdout21（封存时点方法，21 文件）。

## 八、已用注记（R60 开封验收，2026-10-31）

- holdout21 已于 R60（封存后首个平台全立轮：(a) −1.221／(b) 四护栏全立／(c) −1.808，全立计 19）开封验收毕，**标已用**，不得再作留出验收使用。开封记录：runs/round60/acceptance/OPENING.md；验收报告：runs/round60/acceptance/REPORT.md。
- 验收结论：**未达标**——我方 3.340 vs 大师 4.350、配对差 −1.010（SE 0.356）、W/T/L 4/3/18，三判据全不立（主口径＝封存口径，全例 low 同集判读）。双视最大分差 我方 2.0／大师 1.5，无分歧、无仲裁。
- 后续：E3/E4/E5 同口径诊断（DIAG-H21）与 REV1 写死判读照 R60 PREREG §2/§3 续行；holdout22 构成为下一主线。
