# ADDENDUM-r66（R66 主持附记，随轮落盘）

## 一、开轮核查登记

- 开轮 HEAD＝22a938c8（标签 phase3-round65）。快照复核（STAGE-SUMMARY-50 R66 清单第 1 项）：runs/round66/kb-snapshot 自现行活 method/ 生成，21 文件 SHA-256 清单与 runs/round65/kb-snapshot-sha256.txt 逐件比对**为空集之差**（全等），方法零改动登记毕。
- 到货核查：incoming 各目录与 ~/workspace/user/files 均无晚于 R65 收束的新件（以 runs/round65/REPORT.md 为界 find -newer 实查为空）；最新入库仍为 wanted-books-4 包。第四批第 2/6/8 条未到，只登记（PREREG §8）。
- W 监测先验路径实查：runs/round38/diagnosis/W-CHARTER.md、runs/round41/diagnosis/DIAG-LR-fresh-h16.md 均在盘（开轮已验）。
- 冻结提示：runs/round66/prompts/BLIND-PROMPT-verbatim.txt、JUDGE-PROMPT-verbatim.txt 与 runs/calib-r17 原件 diff 全等（SHA-256 5be8e1bc…8d71／93cf7277…acd4，开轮已验）。
- manifest：runs/round66/judging/outcome-manifest.json 构建断言全过（build_manifest_r66.py），SHA-256＝2deed7b0433cff49ff1e05aa57f814fc476be76cf76d6576b72445c132ef54d7；新增落实层 _r66_carryover_notes_addendum＝R65 定案部分成立 40 件（counts 与 R65 REPORT §一公布分布 5/40/3/0、总 48 断言全等）。
- **勘误一则（R65 PREREG 盘上件截断，R66 开轮发现并登记）**：runs/round65/PREREG.md 盘上件（4053 字节／2357 字符，提交 aac2397d 与 HEAD 件同长一致）全文仅含标题、登记行、§0 与 §1 首段，止于读数带「第 3 点（R64）：(a) −1」处，末行第 16 行为字面字符串「...[truncated 5428 chars]」（25 字符）——§1 线值条目与 §2–§8 各节在盘上件中缺失。核对结论：R65 实际执行口径未受影响——analyze_r65.py 内写死阈值（(a) −1.371／(b) −0.449、＋0.290、−0.760、−2.600／(c) −1.93、熔断 −2.255／护栏 −0.816、−2.550）与 R64 PREREG §1 逐值一致，R65 REPORT/ADDENDUM 公布口径与之全等，本轮 §1 线值即据此三方对勘重述。成因推定：R65 主持撰写 PREREG 时以被截断的工具输出（R64 PREREG 读数）为源转写，截断标记被当作正文写入且未回读验尾。处置：不改 R65 历史件（证据只增不删），于本附记与 R66 PREREG 开轮勘误段登记；R66 立「引用文本落盘验尾」判例（PREREG §7）。连带核查：method 活文件 chinese-liuren.md（行 726）与 chinese-qimen.md（行 65）内各含一处同型字面截断标记，round64/round65 快照与活 method 三方同位同字——为更早轮次已入冻结方法本体的历史污染，本轮快照 diff 为空集、方法零改动纪律下不在本轮处置范围，仅登记备后续方法修订议程查考，不影响本轮口径（两文件其余条文照常执行）。

## 二、供给登记

本轮开轮无新非六爻面入账（开轮核查如上）；holdout22 绑定缺口非六爻锚点在场 eligible 12 例不变，未组集（PREREG §4）。轮内若有新面入账另行补记。

## 三、R61-REV1 判读登记

本轮无新鲜封存验收集（holdout22 未组集），R61-REV1 判读照 PREREG-ADDENDUM-r61 §三顺延登记；本轮 dev 平台读数为 R61-REV1 接入后系列第 5 点，只作方向附读、不作判读、不触发回滚或存档处置。
