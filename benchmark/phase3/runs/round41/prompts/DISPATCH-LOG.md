# R41 派单记录（主持留档，2026-10-30）

派工文体例：盲测席同一模板——冻结盲测提示（runs/calib-r17/BLIND-PROMPT.txt）逐字套用（替换：轮次 R41、输入 inputs-dev12、方法 runs/round41/kb-snapshot、预测写 runs/round41/predictions/）＋PREREG §8 随单附件一（trigger 条款原文）与附件二（主持注记原文）＋本批 id 清单（与 runs/round41/batches.json 同源生成、不一致以盘上为准）＋隔离纪律（逐 id 精确打开、禁 glob、禁列他目录、自报不罚）。数据/诊断席派工文见各席任务原文（本日志记其产物路径）。

## 前置与并行席
- 六壬新鲜段诊断席 75d4b557 → runs/round41/diagnosis/DIAG-LR-fresh-h16.md
- 字触续核数据席 S1 3c9017e2 → runs/round41/data-verify/ZC-CENSUS-R41.md＋zc-candidates-r41.jsonl
- 断案/辨疑数据席 S2 ac836cf5 → runs/round41/data-verify/DA-BYZ-POOL-R41.md＋da-byz-candidates-r41.jsonl
- 粹言数据席 S3 64d21957 → runs/round41/data-verify/YXS-POOL-R41.md＋yxs-candidates-r41.jsonl

## 平台盲测席（25 批，487 例）
- B01 146f188f｜B02 19fe15db｜B03 a0021eee｜B04 8aaddbe6｜B05 18be4583｜B06 3a4cf0a4
- B07 bd495eef｜B08 3edaad7f｜B09 8e2c6df6｜B10 d52a0f42｜B11 241f20e4｜B12 f611b884
- B13 78cf4d69｜B14 d2122595｜B15 b26ccd24｜B16 979ea12a｜B17 10f2493e｜B18 75592b9c
- B19 0a6e5215｜B20 195e0b09｜B21 d99d74c2｜B22 b976bbc2｜B23 06ac64d7｜B24 07988796｜B25 521f9bd4

## 平台评审席（双视 8 席）与 holdout17 组集席
- JX1 7702f8ed｜JX2 411f1496｜JX3 f29ecea2｜JX4 24628817
- JY1 7c090f5b｜JY2 73217d2c｜JY3 bcebf4d2｜JY4 a0a9aa9e
- H17-BUILD 2f207cb3
- 平台仲裁 ARB 2fe254c1（YM-030／LY-526 两例）
- W 监测席 WM41 a0c2900d

## holdout17 验收席（目录 runs/holdout17-acceptance/）
- 盲测 H17-CZ bbf8eed8｜H17-LR 54934638
- CY 卡污染补救席 91d65a04（剥离断语 309 字＋封存日志勘误）
- 盲测补测 H17-CY d3aa342d（全新席，剥离后重测）
- 评审 JO1 f133b0e6｜JO2 fa930d0a｜JM1 5d152393｜JM2 071394e2
