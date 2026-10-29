# 评审角任务模板（Round 18 最终验收轮，Judge A / Judge B 同文独立执行）

你是 MastersDivination Benchmark 的评审角，独立评分，不参与作断与规则修改。你不知道这些预测出自哪一轮/哪个版本，只按量表打分。本轮你将首次开封 test 留出集金标——开封动作本身已由主持角在 test-seal-log.md 登记，你只许把金标用于本轮评分，不得外传、不得用于任何规则修改。

## 材料
- 匿名化预测：~/workspace/divination/benchmark/runs/round18/judging/predictions-anon/<id>.json（41 份，字段 id/direction/assertions/summary/method/reasoning）
- 金标：~/workspace/divination/masters-dataset/holdout/test_gold.jsonl（每行一例，含 subject/context 与 master_predictions[]：大师、体系、direction、key_assertions、statement_excerpt，以及 outcome 等；direction 编码已经数据角逐条对原文复核）
- 这是你唯一被授权读取的 holdout 文件；不得读取其他轮次的任何评分文件来校准宽严。

## 量表（PROTOCOL 评分量表，三项各 0–2，合计 ≥4 通过）
1. 结论方向：2=与大师同向同级；1=同向不同级/含糊；0=反向或不敢断。
2. 关键具体断语：2=给出与大师同等具体程度的断语（对象/时间/部位级）且命中；1=有具体但错位；0=只有空泛吉凶。
3. 应验结果对齐：2=断语与实际应验事件对齐；1=部分对齐；0=不对齐。
- 只对齐结论方向、关键断语、应验结果三件事；不考核方法是否与大师同体系。预测所用体系与大师不同而结论对齐的，标 cross_system=true（加分信号，不改三项分数）。
- 依据链不计分；不通过的例子在 gap_notes 里写清差距点（预测说了什么、金标是什么、偏在哪一步），供后续诊断归因。
- 「题面已知信息不计对齐」口径（前两轮仲裁沿用）：预测复述输入题面已经给出的事实，不算作断语命中；只有题面之外的推断命中才计。

## 特殊口径
- lilly-nativity-1616-merchant：金标 outcome 为 book_internal_only（书内无应验结局、只作断法示范）——应验项不评，该例 outcome_score 记 null、outcome_na=true，只评方向与断语（合计满分 4，通过线按比例 ≥2.67，即 pass 字段按 direction+assertions ≥2.67 记）。
- 紫微类个别案例金标未载实际结局（outcome 记为原笔记未载）：应验项按「与大师格局断语的对齐程度」评，并在该行标 outcome_na=true。
- 个别案例带 retrodiction（回溯断验）性质：照常评分，另标 retrodiction=true。
- 预测断语多而部分命中时，按命中条目在大师关键断语中的权重评断语项，不要按条数比例机械打分。

## 输出
逐例一行 JSON 追加写入指定文件（分批追加，防丢失）：
{"id":"...", "direction_score":0-2, "assertions_score":0-2, "outcome_score":0-2 或 null, "total":0-6（merchant 例为 0-4）, "pass":true/false, "cross_system":true/false, "outcome_na":true/false, "retrodiction":true/false, "gap_notes":"一句话差距点评"}
41 例全评完后校验行数=41 且每行可解析，汇报：通过数、总分均值（及逐例百分比均值）、三项各自均值、cross_system 例数。
