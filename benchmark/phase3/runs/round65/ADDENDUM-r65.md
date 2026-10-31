# ADDENDUM-r65（R65 主持附记，随轮落盘）

## 一、开轮核查登记

- 开轮 HEAD＝98c13133（标签 phase3-round64）。快照复核（STAGE-SUMMARY-49 R65 清单第 1 项）：runs/round65/kb-snapshot 自现行活 method/ 生成，21 文件 SHA-256 清单与 runs/round64/kb-snapshot-sha256.txt 逐件比对**为空集之差**（全等），方法零改动登记毕。
- 到货核查：incoming 各目录与 ~/workspace/user/files 均无晚于 R64 收束的新件（以 runs/round64/REPORT.md 为界 find -newer 实查为空）；最新入库仍为 wanted-books-4 包。第四批第 2/6/8 条未到，只登记（PREREG §8）。
- W 监测先验路径实查：runs/round38/diagnosis/W-CHARTER.md、runs/round41/diagnosis/DIAG-LR-fresh-h16.md 均在盘（开轮已验）。
- 冻结提示：runs/round65/prompts/BLIND-PROMPT-verbatim.txt、JUDGE-PROMPT-verbatim.txt 与 runs/calib-r17 原件 diff 全等（开轮已验）。
- manifest：runs/round65/judging/outcome-manifest.json 构建断言全过（build_manifest_r65.py），SHA-256＝5f9133cd8df0fe1c0fbedadfce7dea46470e1c0ddefeed72a1148424ea6432ad；新增落实层 _r65_carryover_notes_addendum＝R64 定案部分成立 99 件（counts 与 R64 REPORT §一公布分布 12/99/15/3、总 129 断言全等）。

## 二、供给登记

本轮开轮无新非六爻面入账（开轮核查如上）；holdout22 绑定缺口非六爻锚点在场 eligible 12 例不变，未组集（PREREG §4）。轮内若有新面入账另行补记。

## 三、R61-REV1 判读登记

本轮无新鲜封存验收集（holdout22 未组集），R61-REV1 判读照 PREREG-ADDENDUM-r61 §三顺延登记；本轮 dev 平台读数为 R61-REV1 接入后系列第 4 点，只作方向附读、不作判读、不触发回滚或存档处置。

## 四、盲测席位事件（冻结前登记）

- **无通配删除事件**：R65 派单明文写入 R64 三条新判例（禁通配删除／构建 glob 排除本轮产出／旗标落笔前回读结局原文），九席全部逐件处理自身产出，无误删、无覆写他席文件，为该判例立式后首个零事故轮次。
- **S4 隔离自报两项（主持核算影响为零）**：① 开工初期一条复合命令中曾对本轮 predictions 目录执行一次 `ls`（与 kb-snapshot 工具帮助输出同命令），输出未显示任何条目、未打开其中任何文件、未据此做任何判断，此后校验严格按本批 id 逐件精确打开；② 同命令中 cast_iching.py 曾以 `--help` 被运行一次（工具无 help 模式、随机起了一卦），该结果未被用于任何一例断语（本批均为题面已给卦象的历史占例）。照被动瞥见同例登记。
- 其余各席一次落盘、隔离自报均为只读允许面（batches.json、本批 inputs-dev12 输入卡、kb-snapshot），无禁读接触；各席回传字节数与主持盘上逐批复算逐项全等（FREEZE-r65 §一）。各席中间件均在本轮目录内席位唯一名文件，随冻结提交入仓备查。
