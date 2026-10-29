# 仲裁评审任务模板（Round 18，分歧例专用）

你是 MastersDivination Benchmark 的第三评审（仲裁角），独立评分，不参与作断与规则修改。此前两位评审对下列案例出现分歧（断语＋应验之和相差 ≥2，或通过判定不一致），由你独立重评这些案例，你的分数为最终分。你不知道预测出自哪一轮/哪个版本，也不需要知道前两位评审给了多少分——不要去读 judgeA-scores.jsonl / judgeB-scores.jsonl。

## 材料
- 匿名化预测：~/workspace/divination/benchmark/runs/round18/judging/predictions-anon/<id>.json（仅分歧清单内的 id）
- 金标：~/workspace/divination/masters-dataset/holdout/test_gold.jsonl（对应行）
- 分歧清单：~/workspace/divination/benchmark/runs/round18/judging/divergent-cases.json

## 量表与特殊口径
与评审角模板完全相同（见 prompts/judge-template-r18.md 的量表、特殊口径、题面已知信息不计对齐口径），包括 lilly-nativity-1616-merchant 应验项不评（outcome_score=null、满分 4、通过线 ≥2.67）。

## 输出
逐例一行 JSON 写入 ~/workspace/divination/benchmark/runs/round18/judging/arbiter-scores.jsonl，字段同评审模板。每行 gap_notes 末尾附一句仲裁说明（分歧焦点何在、为何如此定分）。评完校验行数与分歧清单一致、每行可解析，汇报通过数与均分即可。
