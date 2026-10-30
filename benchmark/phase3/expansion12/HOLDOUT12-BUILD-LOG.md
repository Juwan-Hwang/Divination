# HOLDOUT12-BUILD-LOG — holdout12 建集日志（数据角）

## ⚠️ 置顶停手报告（选择规则触发：某源实数与主持给定 N 不符）

**停手源：CZ（测字）**

- 任务给定口径：`expansion12/online-routes/cases.jsonl` 中 `holdout_eligible=true`，N=33，k=8。
- 盘上实数（2026-10-30 本轮逐行解析实测）：文件共 **33** 行（CZ-001…CZ-033），但 `holdout_eligible=true` 者 **0 例**；33 例该字段**全为 false**。
- 差异：按给定过滤口径实数 0 vs 给定 N=33，**差 33 例**。
- 字段为 false 的盘上原因（各例 `notes.comment` 原文口径一致）：「测字为本库新体系：预注册 §二.4 新体系前置未满足（测字 references 章节未建），本例仅入储备账、不入 holdout12 封存集，故 holdout_eligible=false；待主持建章后另行裁定。」
- 相关盘上事实（仅登记，不作裁定）：测字断法章节现已存在——`benchmark/phase3/method/references/chinese-cezi.md`（261 行，STAGE-SUMMARY-16 §一.4 记为消化批次建立）。但 `cases.jsonl` 的 `holdout_eligible` 字段未经任何后续文件翻转，资格是否因建章完成而生效，属主持裁定事项。
- 数据角处置（按派单写死规则）：**停手**。不自行改 k、不自行翻转/推定 CZ 资格、不以文件总行数 33 冒充「holdout_eligible=true 实数 33」。因 CZ 缺口 8 例（k=8）无法按规则入选，holdout12 全集（49 例）不成立，本轮**未抽样、未建输入卡、未产金标**，`benchmark/phase3/holdout12-inputs/` 与 `benchmark/phase3/holdout12/` 均未创建。
- 待主持裁定后方可续建：① CZ 33 例资格是否生效（生效则请主持明确以何种口径/文件为准据，数据角据此重跑全集）；或 ② 另行给定 CZ 的 k 与来源口径。

## 一、各源计数核对（本轮实测，逐行解析 JSONL）

| 源 | 给定过滤口径 | 给定 N | 盘上实数 | 给定 k | 核对 |
|---|---|---|---|---|---|
| DA | `expansion12/liuren-duanan/cases-a.jsonl`＋`cases-b.jsonl` 中 `holdout_eligible=true`（a 90＋b 72） | 162 | **162** | 9 | ✔ 一致 |
| BY | `expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl` 中 `review.verdict=seal` 且 id 以 BY 开头 | 108 | **108** | 9 | ✔ 一致 |
| 粹言（CY＋CYJ 合并） | `expansion12/liuren-cuiyan/cases-munong.jsonl`（56）与 `cases-juan5.jsonl`（63）中 `holdout_eligible=true` | 119 | **119** | 9 | ✔ 一致 |
| 千里命稿 | `expansion12/natal-batch2/cases-reviewed.jsonl` 中 `review.verdict=seal`（实数 id：QM-005、QM-006、QM-007、QM-008、QM-010、QM-018、QM-020、QM-021、QM-022、QM-023、QM-024、QM-027、QM-028、QM-029、QM-030、QM-031、QM-032、QM-035，皆 QM- 前缀） | 18 | **18** | 8 | ✔ 一致 |
| NL | `expansion12/natal-leftovers/cases.jsonl` 中 id∈{NL-001, NL-002, NL-005, NL-006, NL-031, NL-043, NL-049}（7 例逐一在盘） | 7 | **7** | 5 | ✔ 一致 |
| CZ | `expansion12/online-routes/cases.jsonl` 中 `holdout_eligible=true` | 33 | **0**（文件总行数 33，字段全 false） | 8 | ✘ **不符，见置顶报告** |
| HZ-001 | `expansion12/huangjince-huozhulin/cases.jsonl` 该例（文件 1 例，`holdout_eligible=true`） | 1 | **1** | 1 | ✔ 一致 |

合计口径：除 CZ 外六源给定量 9＋9＋9＋8＋5＋1＝41 例的计数基础均已核实无误；CZ 的 8 例因资格口径未定无法成立，总集 49 例未组。

## 二、本轮未执行事项（因停手规则）

- 抽样（idx=floor(i*N/k)）：未执行（CZ 口径未定，全集抽样不启动，避免产出半成品集被误用）。
- 六壬 27 例课式复原：未执行。
- 输入卡 `benchmark/phase3/holdout12-inputs/`：未创建（盘上计数 0）。
- 金标 `benchmark/phase3/holdout12/test_gold.jsonl`：未创建（盘上计数 0）。
- 三键（对象＋时间＋事项）两两无撞核对、逐例 fidelity、逐例卫生处置登记：随建集一并顺延，主持裁定 CZ 口径后与全集同轮补齐。

## 三、续建条件

主持对 CZ 资格口径作出裁定（生效与否及准据文件）后，数据角按原写死规则一次性重跑：计数复核 → 抽样 → 课式复原 → 建卡（输入卫生） → 金标 → 本日志补齐入选清单／替换登记／三键核对／逐例 fidelity／逐例卫生处置。


---

# 续建段（主持裁定三后，2026-10-30）
准据：HOST-RULINGS-3.md——CZ-001…033 入封资格生效，CZ 合格集＝online-routes/cases.jsonl 全部 33 例（源文件 holdout_eligible=false 系抽例时点状态，不作过滤）。前任停手记录保留于上文原文，未改动。
## 续一、各源计数复核（本轮逐行解析实测，与派单 N 全合，无出入，未触发停手）
- DA：N=162，k=9，抽样下标 idx=[0, 18, 36, 54, 72, 90, 108, 126, 144]，入选=['DA-001', 'DA-028', 'DA-049', 'DA-069', 'DA-089', 'DA-111', 'DA-143', 'DA-166', 'DA-193']
- BY：N=108，k=9，抽样下标 idx=[0, 12, 24, 36, 48, 60, 72, 84, 96]，入选=['BY-001', 'BY-013', 'BY-026', 'BY-040', 'BY-052', 'BY-065', 'BY-082', 'BY-095', 'BY-108']
- CY：N=119，k=9，抽样下标 idx=[0, 13, 26, 39, 52, 66, 79, 92, 105]，入选=['CY-001', 'CY-015', 'CY-028', 'CY-041', 'CY-057', 'CYJ-011', 'CYJ-024', 'CYJ-037', 'CYJ-051']
- QM：N=18，k=8，抽样下标 idx=[0, 2, 4, 6, 9, 11, 13, 15]，入选=['QM-005', 'QM-007', 'QM-010', 'QM-020', 'QM-023', 'QM-027', 'QM-029', 'QM-031']
- NL：N=7，k=5，抽样下标 idx=[0, 1, 2, 4, 5]，入选=['NL-001', 'NL-002', 'NL-005', 'NL-031', 'NL-043']
- CZ：N=33，k=8，抽样下标 idx=[0, 4, 8, 12, 16, 20, 24, 28]，入选=['CZ-001', 'CZ-005', 'CZ-009', 'CZ-013', 'CZ-017', 'CZ-021', 'CZ-025', 'CZ-029']
- HZ：N=1，k=1，抽样下标 idx=[0]，入选=['HZ-001']
合计 9＋9＋9＋8＋5＋8＋1＝49 例。千里命稿入选 QM-005、QM-007、QM-010、QM-020、QM-023、QM-027、QM-029、QM-031 按入选序改编 QL-001…QL-008，金标与输入卡均加 source_id 存原 QM 号。

## 续二、替换登记

无替换。六壬 27 例中：DA 9 例原文（cases_raw.json）均有完整课盘列式；BY 9 例原文 PDF 均有课盘列式；CY/CYJ 9 例原文页图均有课盘列（CYJ 例头仅记时支、无月将，属 fidelity 降级而非「原文亦无列式」），均不满足派单唯一替换条件（课式完全无从复原且原文亦无列式），故不顺延。

## 续三、三键无撞核对

49 例以（对象 subject＋占时 asked_at＋事项 question）归一化（去空白）两两比对：0 撞。另核：49 个 id 与 expansion12/POOL-IDS.txt 及 inputs-dev10/ 既有 id 均无重合。

## 续四、逐例课式 fidelity（仅六壬 27 例）
- DA-001：原文直载（断案 scratch-archive/cases_raw.json 原文课盘列式直录于课盘原文，三传据盘右列六亲干支天将录出）
- DA-028：原文直载（断案 scratch-archive/cases_raw.json 原文课盘列式直录于课盘原文，三传据盘右列六亲干支天将录出）
- DA-049：原文直载（断案 scratch-archive/cases_raw.json 原文课盘列式直录于课盘原文，三传据盘右列六亲干支天将录出）
- DA-069：原文直载（断案 scratch-archive/cases_raw.json 原文课盘列式直录于课盘原文，三传据盘右列六亲干支天将录出）
- DA-089：原文直载（断案 scratch-archive/cases_raw.json 原文课盘列式直录于课盘原文，三传据盘右列六亲干支天将录出）
- DA-111：原文直载（断案 scratch-archive/cases_raw.json 原文课盘列式直录于课盘原文，三传据盘右列六亲干支天将录出）
- DA-143：原文直载（断案 scratch-archive/cases_raw.json 原文课盘列式直录于课盘原文，三传据盘右列六亲干支天将录出）
- DA-166：原文直载（断案 scratch-archive/cases_raw.json 原文课盘列式直录于课盘原文，三传据盘右列六亲干支天将录出）
- DA-193：原文直载（断案 scratch-archive/cases_raw.json 原文课盘列式直录于课盘原文，三传据盘右列六亲干支天将录出）
- BY-001：原文直载（辨疑 PDF 页图课盘直录：课式标题/三传/四课/天地盘；排印本玄武省作「元」，三传天将按全称记、四课与天地盘天将行照原字）
- BY-013：原文直载（辨疑 PDF 页图课盘直录：课式标题/三传/四课/天地盘；排印本玄武省作「元」，三传天将按全称记、四课与天地盘天将行照原字）
- BY-026：原文直载（辨疑 PDF 页图课盘直录：课式标题/三传/四课/天地盘；排印本玄武省作「元」，三传天将按全称记、四课与天地盘天将行照原字）
- BY-040：原文直载（辨疑 PDF 页图课盘直录：课式标题/三传/四课/天地盘；排印本玄武省作「元」，三传天将按全称记、四课与天地盘天将行照原字）
- BY-052：原文直载（辨疑 PDF 页图课盘直录：课式标题/三传/四课/天地盘；排印本玄武省作「元」，三传天将按全称记、四课与天地盘天将行照原字）
- BY-065：原文直载（辨疑 PDF 页图课盘直录：课式标题/三传/四课/天地盘；排印本玄武省作「元」，三传天将按全称记、四课与天地盘天将行照原字）
- BY-082：原文直载（辨疑 PDF 页图课盘直录：课式标题/三传/四课/天地盘；排印本玄武省作「元」，三传天将按全称记、四课与天地盘天将行照原字）
- BY-095：原文直载（辨疑 PDF 页图课盘直录：课式标题/三传/四课/天地盘；排印本玄武省作「元」，三传天将按全称记、四课与天地盘天将行照原字）
- BY-108：原文直载（辨疑 PDF 页图课盘直录：课式标题/三传/四课/天地盘；排印本玄武省作「元」，三传天将按全称记、四课与天地盘天将行照原字）
- CY-001：仅干支（复原不能）：原书有课盘列但转录底稿未录盘、页图字迹不足以逐字可靠转录；仅录干支，例头未载月将
- CY-015：仅干支（复原不能）：原书有课盘列但转录底稿未录盘、页图字迹不足以逐字可靠转录；仅录干支＋月将（例头载）
- CY-028：仅干支（复原不能）：原书有课盘列但转录底稿未录盘、页图字迹不足以逐字可靠转录；仅录干支＋月将（例头载）
- CY-041：仅干支（复原不能）：原书有课盘列但转录底稿未录盘、页图字迹不足以逐字可靠转录；仅录干支＋月将（例头载）
- CY-057：仅干支（复原不能）：原书有课盘列但转录底稿未录盘、页图字迹不足以逐字可靠转录；仅录干支＋月将（例头载）
- CYJ-011：仅干支（复原不能）：原书有课盘列但转录底稿未录盘、页图字迹不足以逐字可靠转录；仅录干支，例头未载月将
- CYJ-024：仅干支（复原不能）：原书有课盘列但转录底稿未录盘、页图字迹不足以逐字可靠转录；仅录干支，例头未载月将
- CYJ-037：仅干支（复原不能）：原书有课盘列但转录底稿未录盘、页图字迹不足以逐字可靠转录；仅录干支，例头未载月将
- CYJ-051：仅干支（复原不能）：原书有课盘列但转录底稿未录盘、页图字迹不足以逐字可靠转录；仅录干支，例头未载月将

## 续五、逐例输入卫生处置
- DA-001：context_at_prediction 为占时已知背景（天气/祈雪无响应），原样用作 setting，无后事内容
- DA-028：context_at_prediction 原文为空，未填
- DA-049：context_at_prediction 原文为空，未填
- DA-069：context_at_prediction 原文为空，未填
- DA-089：context_at_prediction 原文为空，未填
- DA-111：context_at_prediction 原文为空，未填
- DA-143：context_at_prediction 原文为空，未填
- DA-166：context_at_prediction 原文为空，未填
- DA-193：context_at_prediction 原文为空，未填
- BY-001：context_at_prediction 原文为空，未填
- BY-013：context_at_prediction 原文为空，未填
- BY-026：context_at_prediction 原文为空，未填
- BY-040：context_at_prediction 原文为空，未填
- BY-052：context_at_prediction 原文为空，未填
- BY-065：context_at_prediction 原文为空，未填
- BY-082：context_at_prediction 原文为空，未填
- BY-095：context_at_prediction 原文为空，未填
- BY-108：context_at_prediction 原文为空，未填
- CY-001：context_at_prediction 原文为空，未填
- CY-015：context_at_prediction 原文为空，未填
- CY-028：context_at_prediction 原文为空，未填
- CY-041：context_at_prediction 原文为空，未填
- CY-057：context_at_prediction 原文为空，未填
- CYJ-011：context_at_prediction 原文为空，未填
- CYJ-024：context_at_prediction 原文为空，未填
- CYJ-037：context_at_prediction 原文为空，未填
- CYJ-051：context_at_prediction 原文为空，未填
- QL-001：context_at_prediction 原文为空；asked_at 通用回顾框架语（全批一致、无本例结局）保留原文
- QL-002：context_at_prediction 原文为空；asked_at 通用回顾框架语（全批一致、无本例结局）保留原文
- QL-003：context_at_prediction 原文为空；asked_at 通用回顾框架语（全批一致、无本例结局）保留原文
- QL-004：context_at_prediction 原文为空；asked_at 通用回顾框架语（全批一致、无本例结局）保留原文
- QL-005：context_at_prediction 原文为空；asked_at 通用回顾框架语（全批一致、无本例结局）保留原文
- QL-006：subject 原文「某军官（后为绑匪，佚名）」含后事身份（后为绑匪），属结局信息，已删「后为绑匪」改为「某军官（佚名）」（subject 与 question_or_topic 两处同改，question 改为「以某军官（佚名）四柱（辛卯 庚寅 己巳 戊子）论其一生」）；asked_at 通用回顾框架语（全批一致、无本例结局）保留原文
- QL-007：context_at_prediction 原文为空；asked_at 通用回顾框架语（全批一致、无本例结局）保留原文
- QL-008：context_at_prediction 原文为空；asked_at 通用回顾框架语（全批一致、无本例结局）保留原文
- NL-001：context_at_prediction 原文为空；四柱自 question_or_topic 括注提取入 attachments，性别仅在 subject 明示为女者（长女/次女/少妇）记录，其余未记
- NL-002：context_at_prediction 原文为空；四柱自 question_or_topic 括注提取入 attachments，性别仅在 subject 明示为女者（长女/次女/少妇）记录，其余未记
- NL-005：context_at_prediction 原文为空；四柱自 question_or_topic 括注提取入 attachments，性别仅在 subject 明示为女者（长女/次女/少妇）记录，其余未记
- NL-031：context_at_prediction 原文为空；四柱自 question_or_topic 括注提取入 attachments，性别仅在 subject 明示为女者（长女/次女/少妇）记录，其余未记
- NL-043：context_at_prediction 原文为空；四柱自 question_or_topic 括注提取入 attachments，性别仅在 subject 明示为女者（长女/次女/少妇）记录，其余未记
- CZ-001：沿原 context 建卡；attachments 原 method_hint 为大师拆字取象理据（断语侧信息），已剔除、仅留所测字；setting/question/asked_at 为占时信息，原文保留
- CZ-005：沿原 context 建卡；attachments 原 method_hint 为大师拆字取象理据（断语侧信息），已剔除、仅留所测字；setting/question/asked_at 为占时信息，原文保留
- CZ-009：沿原 context 建卡；attachments 原 method_hint 为大师拆字取象理据（断语侧信息），已剔除、仅留所测字；setting/question/asked_at 为占时信息，原文保留
- CZ-013：沿原 context 建卡；attachments 原 method_hint 为大师拆字取象理据（断语侧信息），已剔除、仅留所测字；setting/question/asked_at 为占时信息，原文保留
- CZ-017：沿原 context 建卡；attachments 原 method_hint 为大师拆字取象理据（断语侧信息），已剔除、仅留所测字；setting/question/asked_at 为占时信息，原文保留
- CZ-021：沿原 context 建卡；attachments 原 method_hint 为大师拆字取象理据（断语侧信息），已剔除、仅留所测字；setting/question/asked_at 为占时信息，原文保留
- CZ-025：沿原 context 建卡；attachments 原 method_hint 为大师拆字取象理据（断语侧信息），已剔除、仅留所测字；setting/question/asked_at 为占时信息，原文保留
- CZ-029：沿原 context 建卡；attachments 原 method_hint 为大师拆字取象理据（断语侧信息），已剔除、仅留所测字；setting/question/asked_at 为占时信息，原文保留
- HZ-001：按派单沿其原 context 全文建卡，未改写（setting 为原书问答体结构说明，不含本例结局方向）

## 续六、产出（盘上实数）

- 输入卡 benchmark/phase3/holdout12-inputs/：49 个 JSON（逐一解析合法；全卡扫描无 grade_note／outcome／master_predictions／review 键名）。
- 金标 benchmark/phase3/holdout12/test_gold.jsonl：49 行；非 QL 例与源文件原行逐字一致（脚本比对 0 不符），QL 例改 id 并加 source_id、其余字段逐字保留（含 review 字段）。
- 本轮未做 git 提交、未计算封存哈希（封存由主持执行）。
