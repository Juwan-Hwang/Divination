# ADDENDUM-r74（R74 主持附记，随轮落盘）

## 一、开轮核查登记

- 开轮 HEAD＝e1abeb08（标签 phase3-round73）。快照复核（STAGE-SUMMARY-58 R74 清单第 1 项）：runs/round74/kb-snapshot 自现行活 method/ 生成，21 文件 SHA-256 清单与 runs/round73/kb-snapshot-sha256.txt 逐件比对（同格式归一后）**为空集之差**（键集全等、哈希逐件全等，主持开轮实测），方法零改动登记毕。
- 到货核查：incoming 各目录与 ~/workspace/user/files 均无晚于 R73 收束的新件（以 runs/round73/REPORT.md 为界 find -newer 实查为空），最新入库仍为 wanted-books-4 包。第四批第 2/6/8 条未到，只登记（PREREG §8）。
- W 监测先验路径实查：runs/round38/diagnosis/W-CHARTER.md、runs/round41/diagnosis/DIAG-LR-fresh-h16.md 均在盘（开轮已验）。
- 冻结提示：runs/round74/prompts/BLIND-PROMPT-verbatim.txt、JUDGE-PROMPT-verbatim.txt 自 runs/calib-r17 原件复制，SHA-256＝5be8e1bc5e12dd58b09664a570b8fe098c6305840f22071014d9eab0c8e28d71／93cf7277d6c8429a235a00dbe74eb68542581bf72eec4442e8321884ccc5ad4，与历轮登记全等（开轮已验）。
- manifest：runs/round74/judging/outcome-manifest.json 构建断言全过（build_manifest_r74.py，整件新写），SHA-256＝5434c4cf879b2aefbd77f5e5761757a29c87f7da70e69979e7675cc61594e9ba；新增落实层 `_r74_carryover_notes_addendum`＝R73 定案部分成立 140 件（counts 与 R73 REPORT §一公布分布 11/140/4/1、总 156 断言全等、每件建议非空断言全过）。
- 底本纪律执行：本轮预注册自 round73 完整件体例逐节写定、分三段落盘逐段验尾（字节数递进 8580→15427→23426、§0–§8 小节清单回读验齐）；runs/round65/PREREG.md 截断件未作底本（R66 勘误承继）。method 六壬/奇门两篇历史截断标记承 R66 登记、只登记不处置。
- 数据路径正写登记（承 R70 主持误记判例）：本轮一切派单数据路径以 benchmark/phase3/data/ 为正，数据席产物落 benchmark/phase3/data/case-annotations-r74.json 与 manifest-carryover-r74-addendum.md（PREREG §4 明写）。
- tradition 检查器口径承 R73（STAGE-SUMMARY-58 R74 清单第 1 项）：主持 check_tradition_host_r74.py 未标注关键词集承简繁集＋英文变体集（大小写不敏感），与 R73 初检（flags 0）的可比性在 R74 FREEZE 中登记。
- 目录计数动作定规承 R73 继续执行（PREREG §7 明文写死）；**/tmp 禁令涵盖阅读转储明文重申（承 R72 Y4 自报登记，PREREG §7 已写入派单定式）**。
- 席位编成承 R73 并预拆 S9 面（PREREG §7 防截断工法）：S1＝B01–B03、S2＝B04–B06、S3＝B07–B09、S4＝B10–B12、S5＝B13–B15、S6＝B16–B18、S7＝B19–B20、S8＝B21–B22、S9＝B23＋B25（27 例）、S10＝B24（20 例），共十席 487 例。

## 二、供给登记

本轮开轮无新非六爻面入账（开轮核查如上）；holdout22 绑定缺口非六爻锚点在场 eligible 12 例不变，未组集（PREREG §4）。可选未用 123（六爻 122／非六爻 1＝QM-010）、已用并集 1052 承 R63–R73 盘上定案。

## 三、R61-REV1 判读登记

本轮无新鲜封存验收集（holdout22 未组集），R61-REV1 判读照 PREREG-ADDENDUM-r61 §三顺延登记；本轮 dev 平台读数为 R61-REV1 接入后系列第 13 点，只作方向附读、不作判读、不触发回滚或存档处置。(c) 熔断监视照 PREREG §1 熔断条款执行（单轮 <−2.255 方记熔断事实并上报；未触只登记系列读数）。
