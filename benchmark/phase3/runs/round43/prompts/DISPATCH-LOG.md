# R43 派单记录（主持自记；体例承 R42）

## 前置三席

- 数据席（测字全体系普查＋新鲜供给实核）：agent 02099c4d。产出 data-verify/CENSUS-CEZI-R43.md、SUPPLY-R43.md＋7 个 companion id 清单（jsonl）。
- 诊断席（h18 六壬新鲜段分源诊断＋断案单独成节）：agent 043b1cf3。产出 diagnosis/DIAG-LR-fresh-h18.md。
- 研究席（枚举口径 E1–E5 回测）：agent 60cf47fe。产出 diagnosis/ENUM-BACKTEST-R43.md；主持裁决另纸 diagnosis/HOST-RULING-ENUM-R43.md（主持自撰）。

## 平台盲测 25 席（批次沿 R42 batches.json 逐字，487 例）

提示结构承 R42 定式（kb 路径白名单、路径写全 benchmark/phase3/ 前缀、trigger 三布尔原文、主持注记、回传格式）；B05 条款：回传不作落盘证据，冻结前主持逐批按 batches.json id 清单验盘，缺件全新席补测、复验 487/487 全过才许冻结。

- B01 f96de344（20）｜B02 b862f889（20）｜B03 817f1f19（20）｜B04 1b6712aa（20）｜B05 76c45a5b（20）
- B06 ede11ff4（20）｜B07 f8a1b972（20）｜B08 b014e351（20）｜B09 ad233b94（20）｜B10 43d0d129（20）
- B11 76e275af（20）｜B12 a601f7c7（20）｜B13 37b5aaa7（20）｜B14 f146ddfc（20）｜B15 cc405a81（20）
- B16 14f13dbb（20）｜B17 09b3736d（20）｜B18 2d3b2bc7（20）｜B19 fda86739（20）｜B20 8ea082f0（20）
- B21 f0827a24（20）｜B22 a0432807（20）｜B23 7e946389（20）｜B24 1cdfe797（20）｜B25 8722d81b（7）

25/25 批回传、逐批自验全过。主持验盘（verify_predictions_host_r43.py）：487/487 落盘、missing 0、bad 0、trigger 终校 changed_main 62／reserve_used 49／disputed 100（R42 为 45/48/70；trigger 语义无成文定义，计数差异只作附读、不作方法信号）。

写位自纠专项复核（冻结前主持执行）：B17 席 MH-003 内容一度误写 MH-006 路径、B20 席 WP-005 首写 case_id 一度串为 WP-004，两席均自验前自纠；主持复核四件内容与各自 inputs-dev12 输入对位（MH-003＝借物占斧头、MH-006＝老人忧色食鱼、WP-004＝panel consensus、WP-005＝individual panellist），对位属实、四件均以正确内容冻结。B18 席附记 /tmp 同名旧脚本一事记入 REPORT ADDENDUM。

冻结：提交 29355277、标签 phase3-round43-blind-frozen。outcome-manifest 由 build_outcome_manifest_r43.py 生成（487 键集与 R42 全等、overlay 16/16 逐字合并、承 R42 manifest outcomes 逐字）；评审包由 build_judge_packets_r43.py 生成（anon 种子 20261044；块 [122,122,122,121]；host-meta 承 R42 验键集）。

## 平台评审双视（JUDGE-PROMPT 逐字冻结；claims 经 host-mapping 回读 prediction_text 全文；输出覆写回本块文件）

- JX1 cf12fdc4（块 1）｜JX2 d69927cf（块 2）｜JX3 2952fd87（块 3）｜JX4 34aa116f（块 4）
- JY1 d20ec4c5（块 1）｜JY2 2ccd828f（块 2）｜JY3 85a2d339（块 3）｜JY4 fa1590bf（块 4）
