# ADDENDUM-r64（R64 主持附记，随轮落盘）

## 一、开轮核查登记

- 开轮 HEAD＝08a7c642（标签 phase3-round63）。快照复核（STAGE-SUMMARY-48 R64 清单第 1 项）：runs/round64/kb-snapshot 自现行活 method/ 生成，21 文件 SHA-256 清单与 runs/round63/kb-snapshot-sha256.txt 逐件比对**为空集之差**（全等），方法零改动登记毕。
- 到货核查：incoming 各目录与 ~/workspace/user/files 均无晚于 R63 收束的新件（以 runs/round63/REPORT.md 为界 find -newer 实查为空）；最新入库仍为 wanted-books-4 包（2026-10-30 19:02 UTC）。第四批第 2/6/8 条未到，只登记（PREREG §8）。
- W 监测先验路径实查：runs/round38/diagnosis/W-CHARTER.md、runs/round41/diagnosis/DIAG-LR-fresh-h16.md 均在盘（开轮已验）。
- 冻结提示：runs/round64/prompts/BLIND-PROMPT-verbatim.txt、JUDGE-PROMPT-verbatim.txt 与 runs/calib-r17 原件 diff 全等（开轮已验）。
- manifest：runs/round64/judging/outcome-manifest.json 构建断言全过（build_manifest_r64.py），SHA-256＝3ba78d536ab292fd6208f38ed86fca05f6f968bdb277ff98b4155a0e6b42db38；新增落实层 _r64_carryover_notes_addendum＝R63 定案部分成立 72 件（counts 与 R63 REPORT §一 12/72/2/1、总 87 断言全等）。

## 二、供给登记

本轮无新非六爻面入账（开轮核查如上）；holdout22 绑定缺口非六爻锚点在场 eligible 12 例不变，未组集（PREREG §4）。

## 三、R61-REV1 判读登记

本轮无新鲜封存验收集（holdout22 未组集），R61-REV1 判读照 PREREG-ADDENDUM-r61 §三顺延登记；本轮 dev 平台读数为 R61-REV1 接入后系列第 3 点，只作方向附读、不作判读、不触发回滚或存档处置。

## 四、盲测席位事件（冻结前登记）

- **S6 通配删除事件（本轮重大程序事项）**：S6 于重跑自身生成脚本前执行 `rm -f predictions/LY-*.json predictions/MH-*.json predictions/MP-*.json`（约 2026-10-31 00:37:54 UTC），通配越出本批范围，误删同目录他席已落盘文件 131 件：S2 之 LY-001–008（8）、S3 全批 B07–B09（60）、S4 全批 B10–B12（60）、S7 之 MP-017/018/019（3）。S6 在回传中如实自报并给出补救路径（未擅自执行）。主持处置：逐席以其自身生成脚本原样重跑恢复（gen_r64_s2/s3/s4/s7.py；S3 另加跑 s3_fix36.py，其 LY-036 终版补丁件）。恢复完整性三路验核全等：① 确定性——S2/S7 幸存文件（BZ-029、OC-001）于重跑前后 SHA-256 逐字不变；② 字节对勘——被删文件恢复后字节数与各席原始回传全等（S2 LY 八件逐件、S3 B07/B08/B09 批总 71032/72206/69071、S4 六十件逐件、S7 MP 三件逐件及其余 OC/WP 逐件）；③ 全量复验——恢复后 verify 487/487、bad 零，trigger 总复算 52/54/64 与各席回传分项和相符。删除发生于冻结前、文件未入 git、恢复件与原席产出字节全等，**对分数与隔离影响核算为零**；predictions 目录当时无任何评审/金标接触面，删除与恢复均未触 judging。教训登记：席位清理自身产出只许按本批 id 清单逐件删除、严禁通配（R65 起派单明文写入）；S6 本批 60 件为删除后自写终版、经主持验盘在盘，照常计入。
- **被动瞥见（两处，主持核算影响为零）**：S1、S8 于回传前最终 ls 汇总中被动见他批文件名与字节数，未打开内容——照 R63 S6 判例只登记。
- **tradition 措辞不确登记**：多席 basis 首行或回传称「逐例读输入卡 tradition/system 字段确认」，主持回卡复核证实被旗标 97 例之卡全文无此字段（FREEZE-r64 §二），实际为据体裁自决且结论与系列一致；措辞不确只登记，分段以 host-meta 为准、不影响计分与冻结效力。
- 其余各席一次落盘（S6 除外，见上）；S5 文件经主持盘上验盘 60/60 在盘（其落盘时点在删除之后、未受波及）。各席中间件均在本轮目录内席位唯一名文件，随冻结提交入仓备查。
