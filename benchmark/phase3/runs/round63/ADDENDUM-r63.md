# ADDENDUM-r63（R63 主持附记，随轮落盘）

## 一、开轮核查登记

- 开轮 HEAD＝b4093f79（标签 phase3-round62）。快照复核（STAGE-SUMMARY-47 R63 清单第 1 项）：runs/round63/kb-snapshot 自现行活 method/ 生成，21 文件 SHA-256 清单与 runs/round62/kb-snapshot-sha256.txt 逐件比对**为空集之差**（全等），方法零改动登记毕。
- 到货核查：incoming 各目录与 ~/workspace/user/files 均无晚于 R62 收束的新件（以 round62/REPORT.md 为界 find -newer 实查为空）；最新入库仍为 wanted-books-4 包（2026-10-30 19:02 UTC）。第四批第 2/6/8 条未到，只登记（PREREG §8）。
- W 监测先验路径实查：runs/round38/diagnosis/W-CHARTER.md、runs/round41/diagnosis/DIAG-LR-fresh-h16.md 均在盘（开轮已验）。
- 冻结提示：runs/round63/prompts/BLIND-PROMPT-verbatim.txt、JUDGE-PROMPT-verbatim.txt 与 runs/calib-r17 原件 diff 全等（开轮已验）。

## 二、供给登记

本轮无新非六爻面入账（开轮核查如上）；holdout22 绑定缺口非六爻锚点在场 eligible 12 例不变，未组集（PREREG §4）。

## 三、R61-REV1 判读登记

本轮无新鲜封存验收集（holdout22 未组集），R61-REV1 判读照 PREREG-ADDENDUM-r61 §三顺延登记；本轮 dev 平台读数为 R61-REV1 接入后系列第 2 点，只作方向附读、不作判读、不触发回滚或存档处置。

## 四、盲测席位事件（冻结前登记）

- **S5 截断与补派**：原派 S5 席（B13/B14/B15，60 例）终局回传因输出截断 errored；主持查盘 0/60，间隔复查仍为 0/60，判定真未落盘，照 R61 S4 判例拆单批补派全新席 S5a（B13）／S5b（B14）／S5c（B15），三席一次落盘 20/20×3。其在 round63 内遗留中间件四件（dump_r63_s5.py、inputs_r63_s5.txt、analyze_r63_s5.py、analysis_r63_s5.txt）随冻结提交留痕备查，不影响分数与隔离；补派三席均自报未复用其任何文件。
- **S6 轻微越界自报（两处，主持核算影响为零）**：① 开工时对 round63 根目录做一次 ls，仅见目录名清单（含 judging 一名），未进入、未列其内容、未打开任何文件；② 曾误执行 mkdir -p /tmp/x（空目录、无任何文件写入），后续脚本与中间文件一律在 round63 内 s6 命名。两处均未接触任何禁读内容，只登记。
- 其余各席一次落盘、回传无截断；隔离自报均为只读允许面、无禁读接触、无全仓 grep 查定义；中间件均在本轮目录内席位唯一名文件（S1 gen、S3 dump/inputs、S4 inputs 汇编、S6 feat 提取件等），随冻结提交入仓备查。

## 五、评审与数据席位事件（定稿前登记）

- 评审八席（X1–X4／Y1–Y4）全部一次落盘、无补派；双视合并分歧 0 例、免仲裁（merge 断言：X 487／Y 487、anon 集全等）。八席旗标共汇编 161 条旗标行（FLAGS-selfreported-r63.md，主持合并，只登记不改分）。
- 数据席两件经主持回读验盘：附则对勘 65/65 全等；旗标定案 counts 与 annotations 双路复算一致（成立 12／部分成立 72／不成立 2／未核 1、总 87）。指令性字样特别核查：LR2-016 编者注为唯一出处，BZ-036／BZ-042 结局自注字样一并登记，各席均按数据处理未服从（case-annotations-r63.json special_checks）。
- W26 诊断席一次落盘（DIAG-LR-weight-dev63.md，17,340 字节），定稿数回 final-scores 复核全符。
