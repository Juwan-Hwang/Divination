# R40 派单记录（主持留档，2026-10-30）

派工文体例：每席同一模板——冻结盲测提示（runs/calib-r17/BLIND-PROMPT.txt）逐字套用（替换：轮次 R40、输入 inputs-dev12、方法 runs/round40/kb-snapshot、预测写 runs/round40/predictions/）＋PREREG §8 随单附件一（trigger 条款原文）与附件二（主持注记原文）＋本批 id 清单（与 runs/round40/batches.json 同源生成、不一致以盘上为准）＋隔离纪律（逐 id 精确打开、禁 glob、禁列他目录、自报不罚）。数据/诊断席派工文见各席任务原文（本日志记其产物路径）。

## 前置席（已定稿）
- A 层聚合诊断席 3e2513c0 → runs/round40/diagnosis/DIAG-LR-A-layer.md（提交 bd03cf44）
- 供给核验数据席 2946dbd9 → runs/round40/data-verify/SUPPLY-VERIFY-R40.md/.json（提交 aa534de7）

## holdout16 组集数据席
- ccc291a7 → holdout16/inputs、holdout16/test_gold.jsonl、data/holdout16-seal-log.md、runs/round40/build-holdout16/

## 平台盲测席（25 批，487 例）
- B01 c63fc32d｜B02 14f39aad｜B03 6ea8908b｜B04 9efa15c0｜B05 560efb68｜B06 732c5107｜B07 2f3f883d｜B08 1fb7bbb8｜B09 7ce119f7
- B10 9e75ea26｜B11 8e42758a｜B12 d8289915｜B13 0d4aee81｜B14 91910470｜B15 f6bfbac1｜B16 b77ecf84｜B17 5bef795d
- B18 08e0f728｜B19 24c77c69｜B20 6f034f2b｜B21 9e6abe59｜B22 316bed0f｜B23 06fd521a｜B24 025cf345｜B25 2e36b448
