# Round 18 test 留出集开封日志（test-seal-log）

- 开封时间：2026-10-29 08:11（Asia/Shanghai）。
- 开封对象：masters-dataset/holdout/test_gold.jsonl，41 例（splits.json 中 split=test 全集）。此为该封存集自 2026-10-29 Round 1 封存以来**首次开封**（此前历轮均未开封，见 runs/round1/test-seal-log.md 与 runs/round3/test-seal-log-addendum.md）。
- 开封人角色：评审角（Judge A 与 Judge B，两名相互独立的评审 agent）——按 PROTOCOL「test 金标只许评审角在阶段验收轮开封」执行；主持角与盲测角全程未读取金标内容，盲测 41 例预测在开封前已全部落盘并校验（runs/round18/predictions/，开封前完成）。
- 裁定依据：主会话（代表用户）按用户「持续推进直到认为可以为止」的授权作出的 Round 18 裁定（采纳乙＋丁，认定 dev 总分期望已进入 4.3–4.7 平台带、跳过零改动复现轮、直接一次性留出集验收），裁定全文已于执行前登记于 benchmark/iterations.md「Round 18 裁定登记」节，并见 runs/round18/preregistration.md。
- 开封范围与纪律：金标仅供本轮双评审打分与分歧仲裁；预测已匿名化（judging/predictions-anon/，无轮次/版本信息）；金标内容不得用于任何规则修改。本日志与裁定、预注册一并构成开封的完整审计链。
