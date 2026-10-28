# MastersDivination Benchmark（名称已于 2026-10-29 经用户确认）

**版本 v0.1（2026-10-29）· 状态：可发布状态准备中，未经用户点头不对外发布。**

## 任务定义
给定一位被算对象在当时的基本信息与背景（subject + context），预测其结果，并与历史上著名大师（不限体系）在相同情景下做出的原断及实际应验对齐。
- **测的是「与大师原断的一致性」**：本基准不宣称测量超自然准确性，不证明占卜的预测效力；它测的是一个系统（AI 或人）复现大师断法结果的能力。
- **方法无关**：作答可任选或混用任何体系（六爻、八字、占星、塔罗……）。用中国理论算出与西方大师相同的结论，同样算准。
- **跨体系收敛加分信号**：作答体系与大师不同而结论对齐，记为 cross-system convergence，是额外的置信信号。
- **通过标准**：只看最终结果接近程度（结论方向 + 关键具体断语 + 应验对齐），量表见 `../benchmark/PROTOCOL.md`。

## 数据规模（v0.1 种子集）
共 6 例：六爻纳甲 3、梅花易数 3；dev（校准集）4 例、test（留出集）2 例（约七三）。全部逐字抽自公版典籍原文（《增删卜易》《梅花易数》）。后续由四个收集方向（中方占卜/中方命理/西方/现代大师）按 `SCHEMA.md` 扩充；八字、紫微、周易文本占、塔罗、占星等卷在 v0.1 暂缺（无合格成例不凑数，见 DATASHEET 局限）。

## 如何跑评测
1. 作答方读取 `data/dev.jsonl`（校准）或 `data/test_inputs.jsonl`（留出集输入面，无金标），逐例写出 `predictions.jsonl`：每行 `{"id": "...", "direction": "positive|negative|mixed|neutral", "assertions": "自由文本断语", "assertion_score": 0-2（评审判定后填）, "outcome_score": 0-2（评审判定后填）}`。
2. 方向一致率由脚本自动比对；关键断语/应验两项按 PROTOCOL 量表由评审判定后回填分数（判定流程成文于 PROTOCOL）。
3. 运行：`python3 ../benchmark/evaluation/evaluate.py --gold data/dev.jsonl --pred predictions.jsonl`，输出方向一致率、断语对齐率、应验对齐率、按体系/按大师分项与总分。
4. **test 集只在阶段验收时开封** `holdout/test_gold.jsonl` 跑一次，成绩与 dev 分开报告；调规则只许用 dev。

## 数据文件
- `data/dev.jsonl` 校准集全量（开放）
- `data/test_inputs.jsonl` 留出集输入面（无金标）
- `holdout/test_gold.jsonl` 留出集金标（封存，见 holdout/SEALED.md）
- `splits.json` 划分单一事实源；`SCHEMA.md`/`schema.json` 字段规范；`DATASHEET.md` 数据集说明；`CHANGELOG.md` 版本史

## 引用方式
见 `CITATION.cff`。著录：MastersDivination Benchmark Working Group. *MastersDivination Benchmark (v0.1)*. 2026.（名称已于 2026-10-29 经用户确认定稿。）

## 内部版与公开发布版（许可口径）
- **现阶段内部使用，内部版 = 全量**：现代大师等版权内容全量进内部测试集，不因版权/可否再分发而剔除或降级；`redistributable` 与内部收录、划分、评分无关。
- `redistributable` 只用于将来**公开发布版**的导出过滤（公开版 = true 条目全量 + false 条目的元数据形态）。内部全量版与公开过滤版是同一数据集的两种导出。
- 逐条 `license_status` 仍如实填写备查。本包整体公开发布须经用户点头，本轮只做到可发布状态。

## 候选池（四路收集，统一划分中）
- 种子题（本目录 data/）：六爻 3、梅花 3（已划分 dev 4 / test 2）。
- `chinese-natal/`（中方命理卷）、`western/`（西方卷）、`modern-masters/`（现代大师卷：predictions 公开预测 + 占例 inputs/answers）均为候选池，由 benchmark 统一按七三并入 dev/test 并在 splits.json 登记；分卷自身结构按 SCHEMA.md 映射表对齐，不推倒重写。
