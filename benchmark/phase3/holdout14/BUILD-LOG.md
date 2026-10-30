# holdout14 BUILD-LOG — 组建日志（R36 数据角，2026-10-30）

组建脚本：`runs/round36/build_holdout14_r36.py`（唯一名，盘上验收）；备选建档脚本：`runs/round36/build_bushi_beixuan_r36.py`；审计脚本：`runs/round36/audit_ids_holdout14_r36.py`＋`runs/round36/audit-ids-holdout14-report.json`；组建事实：`runs/round36/build_holdout14_facts_r36.json`。本轮未作断、未评分、未 git 提交。

## 一、任务一·卜筮全书备选建档（定数 9/9 全入）

按 `runs/round36/data-verify/CENSUS-LY.md` §五所载位置，回原书底本 PDF 对应页图（200dpi）逐字视觉转录建档（转录源为页图原文，非 BUILD-REPORT 一行摘要），落 `expansion12/bushi-quanshu-beixuan/`（cases.jsonl 9 行＋BUILD-NOTES.md）。字段照 expansion7 BQ 既有 schema（subject/question/chart(hexagram)/master_predictions/outcome/outcome_grade/contamination/provenance 俱全）。新 id BQ-026…BQ-034 续 BQ 序、按备选-01…09 顺序；建档前查 POOL-IDS 无撞号，全树审计见 §六。逐例一行：

| 新 id | 备选 | 例（对象＋占时＋事项） | 课式完整度 | 定入/不入 |
|---|---|---|---|---|
| BQ-026 | 备选-01 | 乡人＋癸巳日＋卜官事·恒卦（两边和释） | 卦名＋断象级（无全盘） | 入 |
| BQ-027 | 备选-02 | 占者＋五月乙未日＋占财·泰之大畜（果无望） | 卦名＋断象级（无全盘） | 入（边界复核：四要素齐备、结局系独立应验句可分离核验，同批 BQ-013 四字结局判 A 先例；从严降 B 之议登记不采，详 BUILD-NOTES §三） |
| BQ-028 | 备选-03 | 注家本人＋八月庚申日＋卜中秋月·家人之观（果应大雨） | 卦名级（动爻未列） | 入 |
| BQ-029 | 备选-04 | 占者＋五月丁丑日＋占晴·屯之无妄（晴而阴滞） | 卦名＋断象级（无全盘） | 入 |
| BQ-030 | 备选-05 | 占者＋辛未日＋占晴·损之小畜（发风而晴） | 卦名＋断象级；未记月份 | 入 |
| BQ-031 | 备选-06 | 占者＋五月甲戌日＋久晴占雨·屯卦（有雨不多） | 卦名＋断象级（静卦） | 入 |
| BQ-032 | 备选-07 | 占者＋乙亥日＋卜种水田·既济之屯（种不成） | 卦名＋断象级；未记月份 | 入 |
| BQ-033 | 备选-08 | 占者＋辛亥日＋卜田·观之讼（田卖与他人） | 卦名＋断象级；未记月份 | 入 |
| BQ-034 | 备选-09 | 占者＋癸巳日＋卜田·颐之噬嗑（田主自种不得成） | 卦名＋断象级；未记月份 | 入 |

Y＝9。同页关系：印刷229 连举四例中姤之乾已收 BQ-023、不重复；BQ-026 与 BQ-004 同则对照、三键以卦名与结局相分。

## 二、供给与储备账（盘上实测）

| 源 | 文件 | 盘上实数 | 可封存口径 | 实测 |
|---|---|---|---|---|
| 断案 DA | expansion12/liuren-duanan/cases-a.jsonl＋cases-b.jsonl | 167 | holdout_eligible=true | 162 |
| 辨疑/预测学 BY/YX | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl | 126 | review.verdict=seal | 111（BY 108＋YX 3） |
| 粹言 CY/CYJ | expansion12/liuren-cuiyan/cases-munong.jsonl（61）＋cases-juan5.jsonl（75） | 136 | holdout_eligible=true | 119 |
| 测字 CZ | expansion12/online-routes/cases.jsonl | 33 | HOST-RULINGS-3 资格生效（全 33） | 33；扣除 holdout12 用 8＋holdout13 用 12 后余 **13** |
| 六爻 BQ 备选 | expansion12/bushi-quanshu-beixuan/cases.jsonl（本轮新建档） | 9 | outcome_grade=A＋low＋holdout_eligible | **9** |
| 八字 PU | expansion12/natal-batch2/cases-reviewed.jsonl | 92 | 八字原生 seal 未用 0、改判可封存 0（CENSUS-BZ 总账）；PU-003/008 仅按主持例外裁定准入 | **2（例外）** |

八字缺口如实登记：CENSUS-BZ 已证八字可封存新增为 0；本集八字 2 例即例外 2 例，无更多八字供给，不以他体系例冒充。

## 三、排除清单（入封前扣除，脚本硬断言）

- dev9 全部 487 例：以 benchmark/phase3/inputs-dev11/ 文件名集为准。
- 历次 holdout 已用 id：holdout3–holdout13 各 test_gold.jsonl 的 id 集（仅取 id 字段），共 300 个 id。
- expansion12/POOL-IDS.txt 488 个 id。
- 入选 40 例与 dev9∪历次 holdout 交集为零（脚本断言通过）；与 POOL-IDS 交集亦为零（脚本实测 pool_hits=[]，PU-003/008 不在 POOL-IDS 内）。

## 四、构成推导（主持公式，机械执行）

C＝CZ 余量全取＝13；Y＝任务一合格六爻＝9；B＝2（PU-003/008）；L＝⌊(2/3)×(13＋9＋2)⌋＝⌊16.0⌋＝16；T＝13＋9＋2＋16＝**40**（恰达目标，无缺口、无降报）。六壬 L 内分：DA＝⌈L/2⌉＝8；余 8 按 holdout13 比例（DA8/BY5/CY3@L16）取 BY 5、CY 3；CY≤0.2×T＝8 ✔。

## 五、选取规则与入选清单

规则（防挑题，写死）：每源在合格集内**按源文件既有顺序**依次取例，跳过 §三排除 id，取足配额即止；CZ 与 BQ 为余量全取；PU 为裁定点名 2 例。不看结局、不看预期分数、不作任何替换。替换登记：无替换。

| 源 | 配额 | 入选（按选取序＝文件序） |
|---|---|---|
| DA | 8 | DA-015、DA-016、DA-017、DA-019、DA-020、DA-021、DA-022、DA-023 |
| BY | 5 | BY-007、BY-008、BY-009、BY-010、BY-011 |
| CY（慕农） | 3 | CY-005、CY-006、CY-008 |
| BQ | 9（全取） | BQ-026、BQ-027、BQ-028、BQ-029、BQ-030、BQ-031、BQ-032、BQ-033、BQ-034 |
| PU（例外） | 2 | PU-003、PU-008 |
| CZ | 13（全取） | CZ-018、CZ-019、CZ-020、CZ-022、CZ-023、CZ-024、CZ-026、CZ-027、CZ-028、CZ-030、CZ-031、CZ-032、CZ-033 |

## 六、封存前全树编号唯一性审计（结果与处置）

`audit_ids_holdout14_r36.py` 扫 benchmark/ 下 20,680 个 json/jsonl 文件（排除 runs/ 与 holdout14 自身产出），只查 id 出现位置，不取结局作任何判定。结果：40 例入选 id 无一命中 inputs-dev11 文件名集、POOL-IDS、data/splits 清单或任何其他 holdout 金标。7 例有「源文件外出现」标记，逐一处置如下（均为同源孪生、非冲突）：

- BY-007…011（5）：另一出现为 liuren-bianyi-yuce/cases.jsonl——即 cases-reviewed.jsonl 的复核前原件（REVIEW-G 明载：原记录全字段逐字未动＋review 字段），同一例。
- PU-003、PU-008（2）：另一出现为 natal-batch2/cases.jsonl——复核前原件，同一例。
- 其余 33 例仅出现于各自唯一源文件（BQ 9 例仅见于本轮新建档 cases.jsonl）。

另：三键（对象＋占时＋事项，归一化去空白；BQ 另加卦名以分同则对照例）核对——入选 40 例两两 0 撞、与 holdout12 49 例＋holdout13 40 例三键 0 撞（脚本断言通过）。

## 七、构成验算表

| 维度 | 例数 | 占比 | 口径 | 判定 |
|---|---|---|---|---|
| 总量 | 40 | — | 目标 40 | ✔（无缺口） |
| 来源 DA《大六壬断案》 | 8 | 20.0% | 单源 ≤50% | ✔ |
| 来源 BY《六壬辨疑》 | 5 | 12.5% | 同上 | ✔ |
| 来源 CY《六壬粹言》卷六 | 3 | 7.5% | 同上 | ✔ |
| 来源 BQ《卜筮全书》 | 9 | 22.5% | 同上 | ✔ |
| 来源 PU《袁氏命谱》 | 2 | 5.0% | 同上 | ✔ |
| 来源 CZ《测字秘牒》 | 13 | 32.5% | 同上（最大单源） | ✔ |
| 体系 六壬 | 16 | 40.0% | 单体系 ≤40% | ✔（恰在上限） |
| 体系 六爻 | 9 | 22.5% | 同上 | ✔ |
| 体系 测字 | 13 | 32.5% | 同上 | ✔ |
| 体系 八字 | 2 | 5.0% | 同上 | ✔ |
| 粹言干支级课式例 | 3 | 7.5% | ≤20% | ✔ |
| 六壬全课式原文直载 | 13/16 | — | 断案/辨疑优先 | ✔ |
| 等级 A／A-low | 11／29 | — | 全例 A/A-low（准据计） | ✔ |
| 污染 low／high（例外） | 38／2 | 95.0%／5.0% | 全 low＋逐例注记例外 2（PREREG 条款） | ✔（例外见 §九） |

## 八、逐例入封四项核验（①新鲜 ②A 级双全可分离 ③低污染 ④断语＋结局俱全）

准据：BY 以 review 的 grade_final／contamination_final／verdict 为准；PU 以 CENSUS-BZ 分级轴改判 A-low＋主持例外裁定为准（③以例外注记代低污染，逐例标「例外」）；DA/CY/BQ/CZ 以源行 outcome_grade／contamination 为准（CZ 资格另据 HOST-RULINGS-3）。①由排除集零交集断言＋§六审计＋三键核对共同成立；④由脚本逐例断言（master_predictions 首条 statement_excerpt 非空、outcome.description 非空）全数通过。

| id | 源 | 等级（准据） | 污染 | ① | ② | ③ | ④ |
|---|---|---|---|---|---|---|---|
| DA-015 | 断案 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| DA-016 | 断案 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| DA-017 | 断案 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| DA-019 | 断案 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| DA-020 | 断案 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| DA-021 | 断案 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| DA-022 | 断案 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| DA-023 | 断案 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| BY-007 | 辨疑 | A-low（grade_final） | low | ✔ | ✔ | ✔ | ✔ |
| BY-008 | 辨疑 | A-low（grade_final） | low | ✔ | ✔ | ✔ | ✔ |
| BY-009 | 辨疑 | A-low（grade_final） | low | ✔ | ✔ | ✔ | ✔ |
| BY-010 | 辨疑 | A-low（grade_final） | low | ✔ | ✔ | ✔ | ✔ |
| BY-011 | 辨疑 | A-low（grade_final） | low | ✔ | ✔ | ✔ | ✔ |
| CY-005 | 粹言 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| CY-006 | 粹言 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| CY-008 | 粹言 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| BQ-026 | 卜筮全书备选 | A | low | ✔ | ✔ | ✔ | ✔ |
| BQ-027 | 卜筮全书备选 | A（边界复核维持，见 §一） | low | ✔ | ✔ | ✔ | ✔ |
| BQ-028 | 卜筮全书备选 | A | low | ✔ | ✔ | ✔ | ✔ |
| BQ-029 | 卜筮全书备选 | A | low | ✔ | ✔ | ✔ | ✔ |
| BQ-030 | 卜筮全书备选 | A | low | ✔ | ✔ | ✔ | ✔ |
| BQ-031 | 卜筮全书备选 | A | low | ✔ | ✔ | ✔ | ✔ |
| BQ-032 | 卜筮全书备选 | A | low | ✔ | ✔ | ✔ | ✔ |
| BQ-033 | 卜筮全书备选 | A | low | ✔ | ✔ | ✔ | ✔ |
| BQ-034 | 卜筮全书备选 | A | low | ✔ | ✔ | ✔ | ✔ |
| PU-003 | 袁氏命谱 | A-low（CENSUS-BZ 分级轴改判；金标 review 字段照源保留 B/dev-only，封存等级以改判＋裁定为准） | **high（例外）** | ✔ | ✔ | 例外 | ✔ |
| PU-008 | 袁氏命谱 | A-low（同上） | **high（例外）** | ✔ | ✔ | 例外 | ✔ |
| CZ-018 | 测字 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| CZ-019 | 测字 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| CZ-020 | 测字 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| CZ-022 | 测字 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| CZ-023 | 测字 | A | low | ✔ | ✔ | ✔ | ✔ |
| CZ-024 | 测字 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| CZ-026 | 测字 | A | low | ✔ | ✔ | ✔ | ✔ |
| CZ-027 | 测字 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| CZ-028 | 测字 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| CZ-030 | 测字 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| CZ-031 | 测字 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| CZ-032 | 测字 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| CZ-033 | 测字 | A-low | low | ✔ | ✔ | ✔ | ✔ |

## 九、例外注记登记（位置索引）

- PU-003、PU-008 污染 high 例外：本日志 §二、§七、§八＋`holdout14/SEALED.md`「污染与例外注记（逐例）」段（明载验收时分层报告要求：low 38 例为主口径、两例单独列报）＋金标行内 contamination／contamination_rationale／grade_note／review 原文照存。改判依据：`runs/round36/data-verify/CENSUS-BZ.md` (a) 节与 `supply-bz-r36.json` B_cases_rereviewed 前两条。

## 十、逐例判语卫生处置（PREREG §6①(2)，剥离登记）

金标逐例核 outcome 字段：含抽例判语尾句（OC-023 型：(a) 相合度裁决句／(b) 应验段出处·可分离·转录元注记）者 8 例，尾句逐字移至金标顶层 `extractor_verdict_tail` 字段，outcome.description 仅余事件文本（剥离后非空，脚本断言）；除此 8 例外金标与各源文件原行逐字一致（独立比对 0 不符）：

| id | 剥离尾句（逐字，即 extractor_verdict_tail 值） | 型 |
|---|---|---|
| CZ-018 | （成婚日期与所断尽合） | (a) |
| CZ-020 | ——经营品类、路线、前次亏折、本次合伙均获具体确认。 | (a) 类确认总括 |
| CZ-022 | （原文作『次以二人同至』，『以』疑为『日』之讹，转录照原文，校记于此） | (b) 转录校记 |
| CZ-023 | （与所断豹尾对应）（原在句末全角句号之前，剥离后事件句以「……箕水豹值日。」收束） | (a) |
| CZ-027 | （榜文公布后与所断合） | (a) |
| CZ-028 | ——议婚地点（都中、非本郡、远隔五百余里）与对象门第（大贵）获具体确认。成婚结局未载。 | (a)＋覆盖注记 |
| PU-003 | （结局为道教传说性质，书内具体可分离） | (b) |
| PU-008 | （结局为传说性质，书内可分离，无确切卒年） | (b) |

复核保留（不剥离，逐例登记）：CZ-019（括注「和平分店之约，无官司」为事件释义、无相合裁决）、CZ-026（「对方多次控告均不被受理，事遂平息」）、CZ-030（「舍亲确为广东惠潮道，道员」）、CZ-031（「十余日后复来报称果然」）、CZ-032（「事已成且果得利，所谋为盐院事」）、CZ-033（「病人确已疯瘫四年，近日足疾来问」）——均为事件内容转述括注，无判语/出处/覆盖注记成分，照源逐字保留。DA/BY/CY/BQ 各例 outcome 为原书案验/应验原文，无抽例判语检出。

## 十一、逐例课式 fidelity 与输入卫生处置

建卡一律白名单字段组装：grade_note／review／contamination／method_hint／extractor_verdict_tail 类字段不入卡（40 卡禁键扫描零命中，脚本断言）。

- DA 8 例：原文直载——课盘原文与三传自 liuren-duanan/scratch-archive/cases_raw.json 对应案号原文直录（评注续行已滤除、只留盘列，◎⊙旬空标记保留于课盘原文）；context_at_prediction 原文为空，未填。
- BY 5 例：原文直载——课式标题/三传/四课/天地盘自《六壬辨疑》排印本 PDF 页图逐字直录（数据角 2026-10-30 视觉转录，200dpi）：BY-007＝课例九（PDF p166–167）、BY-008＝课例十（p167）、BY-009＝课例十一（p167–168）、BY-010＝课例十二（p168）、BY-011＝课例十三（p168–169）。排印本玄武省作「元」：三传天将按全称记、四课与天地盘天将行照原字。BY-010 四课天将行第三字照原字作「龙」（他例作「青」），只登记不改字。
- CY 3 例：仅干支（复原不能）——原书有课盘列但转录底稿未录盘、页图字迹不足以逐字可靠转录；仅录干支/月将/占时，例头月将已含于 asked_at。
- BQ 9 例：照 expansion7 inputs 体例建卡（subject/context{question, asked_at, setting=question, attachments{casting_method, hexagram, chart_excerpt, chart_complete, completeness_basis}}/provenance/language），仅占问背景＋卦象，无断语/结局字段。
- PU 2 例：四柱/性别自源行 chart 入 attachments；context_at_prediction 原文为空，未填。
- CZ 13 例：沿原 context 建卡；attachments 原 method_hint 为大师拆字取象理据（断语侧信息），已剔除、仅留所测字；setting/question/asked_at 为占时信息，原文保留。

## 十二、产出（盘上实数）

- 金标 benchmark/phase3/holdout14/test_gold.jsonl：40 行；与各源文件原行逐字一致（脚本外独立比对：32 例全等，8 例仅 §十登记的尾句移位差异），SHA-256 `609732c12630e0b7668dd62bb722625f80e94bf6aa2c94b995a5597c29c529b8`。
- 输入卡 benchmark/phase3/holdout14-inputs/：40 个 JSON，逐一解析合法，id 集与金标全等。
- 登记：benchmark/phase3/holdout14/SEALED.md、data/holdout14-seal-log.md（SHA 两处一致）。
- 缺口登记：总量 40 恰达目标、无缺口；八字供给已核尽（原生＋改判可封存为 0，本集 2 例为例外裁定准入，见 §二/§九），测字余量 13 已全取用尽，六爻 BQ 备选 9 已全数建档用尽。
