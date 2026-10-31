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
