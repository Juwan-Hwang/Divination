# SEALED — holdout4 金标封存说明

- 本目录 `test_gold.jsonl` 为 holdout4 共 25 例的完整金标（master_predictions + outcome），组建时间 2026-10-29T15:30:06+08:00（Asia/Shanghai）。
- **只许评审角在 Phase 3 验收轮开封时读取**；盲测角、修订角、数据角在本文件落盘后均不得再读。
- 开封须在 `benchmark/phase3/holdout4-seal-log.md` 追加一笔（时间、依据、开封人角色、范围）后方可进行。
- 金标 SHA-256：`4c5c989cb37c774ce78e3ecb8c2c96b6d4a333fdbd99a35c4d0105006219c147`。
- 封存状态以 seal log 为准；本文件落盘时状态为「未开封」。
