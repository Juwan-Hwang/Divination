# Changelog — MastersDivination Benchmark

## v0.1 — 2026-10-29
- 首版种子集：6 例（六爻纳甲 3、梅花易数 3），源自公版《增删卜易》《梅花易数》原文，逐字抽取。
- 定版统一 Schema（SCHEMA.md + schema.json）：subject + context + master_predictions[] 核心结构，体系盘面降为可选附件。
- dev/test 约七三分（4/2），test 金标封存于 holdout/，splits.json 为划分单一事实源。
- 配套评测脚本 benchmark/evaluation/evaluate.py 与协议 benchmark/PROTOCOL.md（方法无关评分、结果三项、跨体系收敛记号）。
- 已知缺口：八字、紫微、周易文本占、塔罗、占星、现代大师诸卷为空，待四路收集补入后发 v0.2。
