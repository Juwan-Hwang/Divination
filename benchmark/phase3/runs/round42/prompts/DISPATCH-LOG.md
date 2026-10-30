# R42 派单记录（主持留档，2026-10-30）

派工文体例：盲测席同一模板——冻结盲测提示（runs/calib-r17/BLIND-PROMPT.txt）逐字套用（替换：轮次 R42、batches benchmark/phase3/runs/round42/batches.json、输入 inputs-dev12、方法 runs/round42/kb-snapshot、预测写 runs/round42/predictions/）＋PREREG §9 随单附件一（trigger 条款原文）与附件二（主持注记原文）＋隔离纪律（逐 id 精确打开、禁 glob、禁列他目录、自报不罚）。派单路径一律写全 benchmark/phase3/ 前缀。

## 前置席（数据/研究）
- R1 枚举口径研究席 446a2edf → runs/round42/diagnosis/AGENDA-ENUM-R42.md（已回盘验收入库 39e0456b）
- D1 字触补核席 adfca3de → runs/round42/data-verify/ZC-RECHECK-R42.md＋zc-candidates-r42.jsonl（Z 定案 35，已入库 8db19ac1）
- D2 六壬供给席 be71951d → runs/round42/data-verify/SUPPLY-R42.md（余 287 定案、CYJ-062 补勘复原辛巳，已入库 d7eabeec）
- D3 建卡席 a375b1a4 → 构成门拦截（测字新鲜实核 15）＋§5 扫描脚本与第一道（已入库 f2adf3a7，含主持裁定 HOST-RULING-H18-COMPOSITION：C＝15/L＝15/T＝30）
- D4 建卡续行席 0449a567 → holdout18 组集（T＝30，裁定构成）

## 平台盲测席（25 批，487 例）
- B01 c529944e｜B02 65457bba｜B03 dfae07bc｜B04 875ec129｜B05 12830384｜B06 e9766980
- B07 1059d3d9｜B08 fb1d521a｜B09 3c459418｜B10 fcc9c149｜B11 58e8b1e7｜B12 42fc5283
- B13 d6f88ac2｜B14 dc946fb3｜B15 84dd1b98｜B16 14967f8b｜B17 8c476db9｜B18 73296544
- B19 84a3c5aa｜B20 3d835b80｜B21 e8a0225e｜B22 dca7f73c｜B23 8c9af5f0｜B24 7c5a4f2c
- B25 c1a2f804

## 补测与验盘（2026-10-30 主持追加）
- B05 原席（12830384）回传报 20/20 写盘，主持全量验盘实测该批 20 例（DT-001–007、LR-001、LR2-013–024）盘上不存在、其余 467 例全过——文件未落盘属实，原因未明（该席一 exec 结果为 failed/unknown）。处置：全新席 B05R（92cb582e）重测该批 20 例，隔离自报无事项；复验 487/487 全过（case_id 全对位、字段齐备、bad＝0），trigger 终校计数 changed_main 45／reserve_used 48／disputed 70。
- BZ-303/304 专项复核（B04 写位自纠件）：两文件 case_id 与文件名对位、内容与各自输入对位（303＝香港地运、304＝庚子疫情），BZ-304 basis 留有覆正说明——自纠属实、判读维持。
- 元数据级接触自报两件（B21、B07）：均系写盘后以目录列表闪现他批文件名、未读内容、断语已先行落盘——影响为零、判读维持，收束时入 REPORT ADDENDUM 核算。
- holdout18 主持第三道验封：scan_verify_host_r42.py 对 30 输入卡复扫零命中；金标 SHA 主持独立 sha256sum＝7d3ce871…与封存日志双读一致——封存主持侧确认成立。

## 待派（平台盲测全数回盘验盘后）
- 评审包构建（主持脚本：manifest 承 round41 验 487 键集＋overlay 16/16、anon 种子 20261042、host-meta 承接）
- 平台评审双视 8 席（JX1–4／JY1–4）、仲裁席（按需）、分析脚本（runs/round42 内新写唯一名）
- W 监测席（平台定稿后，DIAG-LR-weight-dev42）
- holdout18 验收席（平台全立后：盲测 2 席＋评审 4 席，体例承 h17）

## 评审与验收席（2026-10-30 主持追加二）
- 平台评审双视 8 席：JX1 b082ea1c｜JX2 35c0c4a8｜JX3 390f9c11｜JX4 ba5c113e｜JY1 9e05f9d5｜JY2 b13090cf｜JY3 fd1e7d6a｜JY4 4b734a50；仲裁 1 例（YM-030）64b9f5f6。平台三项全立，提交 2e44de9f。
- W 监测席（第五轮）f47793a4 → diagnosis/DIAG-LR-weight-dev42.md（附读，冻结维持）。
- holdout18 验收盲测：ACZ b862dc8b（测字 15）｜ALR 373a486f（六壬 15）；验收评审 JO1 c5e8b43f｜JO2 3fa74cfd｜JM1 85c64204｜JM2 ef558245，双侧零争议无仲裁。验收未达标，holdout18 标已用。
