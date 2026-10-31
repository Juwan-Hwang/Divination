# ADDENDUM-r71（R71 主持附记，随轮落盘）

## 一、开轮核查登记

- 开轮 HEAD＝ca708960（标签 phase3-round70）。快照复核（STAGE-SUMMARY-55 R71 清单第 1 项）：runs/round71/kb-snapshot 自现行活 method/ 生成，21 文件 SHA-256 清单与 runs/round70/kb-snapshot-sha256.txt 逐件比对**为空集之差**（键集全等、哈希逐件全等，主持开轮实测），方法零改动登记毕。
- 到货核查：incoming 各目录与 ~/workspace/user/files 均无晚于 R69 收束的新件（以 runs/round69/REPORT.md 为界 find -newer 实查为空；R70 开轮以 round68 为界同查在案、本轮复核仍为空）；最新入库仍为 wanted-books-4 包。第四批第 2/6/8 条未到，只登记（PREREG §8）。
- W 监测先验路径实查：runs/round38/diagnosis/W-CHARTER.md、runs/round41/diagnosis/DIAG-LR-fresh-h16.md 均在盘（开轮已验）。
- 冻结提示：runs/round71/prompts/BLIND-PROMPT-verbatim.txt、JUDGE-PROMPT-verbatim.txt 自 runs/calib-r17 原件复制，SHA-256＝5be8e1bc…8d71／93cf7277…acd4，与历轮登记全等（开轮已验）。
- manifest：runs/round71/judging/outcome-manifest.json 构建断言全过（build_manifest_r71.py，整件新写、无连环替换），SHA-256＝2f9b305722853fdfc8b5d78c26f6c77117284aa6c16840d098fda4c5650def04；新增落实层 `_r71_carryover_notes_addendum`＝R70 定案部分成立 77 件（counts 与 R70 REPORT §一公布分布 11/77/1/2、总 91 断言全等、每件建议非空断言全过）；脚本内残留 r70 字面量经 grep 逐处核对均为有意承接的源指针（round70 manifest 源、case-annotations-r70 源、_r70 层断言），无误伤。
- 底本纪律执行：本轮预注册自 round70 完整件体例逐节写定、分三段落盘逐段验尾（字节数递进 9900→14966→22672、§0–§8 小节清单回读验齐）；runs/round65/PREREG.md 截断件未作底本（R66 勘误承继）。method 六壬/奇门两篇历史截断标记承 R66 登记、只登记不处置。
- 数据路径正写登记（承 R70 主持误记判例）：本轮一切派单数据路径以 benchmark/phase3/data/ 为正，数据席产物落 benchmark/phase3/data/case-annotations-r71.json 与 manifest-carryover-r71-addendum.md（PREREG §4 明写）。
- tradition 检查器补繁体变体（承 R70 FREEZE §二、STAGE-SUMMARY-55 R71 清单第 1/5 项）：主持 check_tradition_host_r71.py 未标注关键词集增补繁体「未標註」「無tradition」「無 tradition」等，补后初检与 R70 口径可比性在 FREEZE-r71 §二登记（本轮开轮先行登记口径变更本身，冻结时执行）。
- 席位编成承 R70 并预拆 S9 面（PREREG §7 防截断工法）：S1＝B01–B03、S2＝B04–B06、S3＝B07–B09、S4＝B10–B12、S5＝B13–B15、S6＝B16–B18、S7＝B19–B20、S8＝B21–B22、S9＝B23＋B25（27 例）、S10＝B24（20 例），共十席 487 例。

## 二、供给登记

本轮开轮无新非六爻面入账（开轮核查如上）；holdout22 绑定缺口非六爻锚点在场 eligible 12 例不变，未组集（PREREG §4）。可选未用 123（六爻 122／非六爻 1＝QM-010）、已用并集 1052 承 R63–R70 盘上定案。

## 三、R61-REV1 判读登记

本轮无新鲜封存验收集（holdout22 未组集），R61-REV1 判读照 PREREG-ADDENDUM-r61 §三顺延登记；本轮 dev 平台读数为 R61-REV1 接入后系列第 10 点，只作方向附读、不作判读、不触发回滚或存档处置。(c) 熔断监视照 PREREG §1 熔断条款执行（单轮 <−2.255 方记熔断事实并上报；未触只登记系列读数）。

## 四、盲测席位事件（冻结前登记）

- **无通配删除事件**：R71 派单明文写入 R64 三判例与 R65/R66/R67/R68 判例及 R70 强化 tradition 措辞注记，各席全部逐件处理自身产出，无误删、无覆写他席文件，为 R64 判例立式后第七个零事故轮次。
- **十席一次落盘、零补派**：S9 面按 PREREG §7 预拆 S9（B23＋B25，27 例）与 S10（B24，20 例）后，本轮无回传截断事件、无拆单补派（防截断预置工法连续第二轮生效，只登记）。各席回传 trigger 分项和与主持复算逐项全等（47/36/74）。
- **S5 目录计数动作（本轮唯一目录级动作，只登记）**：S5 席运行前对本轮 predictions 目录执行一次 `ls | wc -l`（输出仅数字 427、未显文件名、未打开任何文件），其后只按本批 60 个 id 精确写入。目录禁令原文针对 judging/ 目录与读旧件，本动作不涉 judging、不读文件内容，主持核算影响为零；后续轮派单可明文将「predictions 目录计数」列入许动作或禁动作，本轮只登记事实。
- **tradition 复核**：全账见 FREEZE-r71 §二——检查器补繁体变体后 R70 型变体误报归零；初检 flags 7 件全为英文首行变体（WP-001–007），主持逐件核实陈述属实、裁定不成立（不重测、不交定案）；措辞不实型旗标归零；声明组数加扫多组文件 0、冲突 0。
- 各席中间件均为本轮目录内席位唯一名文件（gen_r71_s1–s10.py），随冻结提交入仓备查；S6 脚本一处条件表达式写法、S8 一例运行前自查覆正，均已在 FREEZE §一登记。隔离自报十席均为只读允许面、无禁读接触；输入残损逐例登记见 FREEZE-r71 §一。
