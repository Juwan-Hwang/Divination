# R60 盲测冻结记录（FREEZE-r60）

- 冻结时点：平台盲测各席全数落盘后，主持逐席验盘毕。
- 验盘（主持脚本 runs/round60/verify_predictions_host_r60.py，盘上实测）：want 487、files 487、missing []、extra []、bad []——**487/487 全过**（case_id 一致、五字段齐备、confidence∈[0,1]、trigger 三布尔＋reason 齐备）。
- trigger 主持复算：changed_main **42**、reserve_used **54**、disputed **62**（以主持复算为准，席位自报只作对照；analyze 的 host_expected 填此三值）。
- tradition 复核（check_tradition_host_r60.py）：direct 365、none-labelled 67、flags 55。55 件逐件目检全为格式变体、无一例与卡面冲突：均为输入卡无顶层 tradition 字段之例，席位据卡内 context／casting_method／题面自决并在 basis 首行登记（BZ 族自决 bazi、LR/LR2/LR3 族自决 liuren、LY-002/008/017/019/021/022 自决 liuyao、MH-010 自决 meihua、MP-001–016 明写「未载于卡」据题面自决、ZY-003 据 casting_method 自决 yijing），体系判定与卡面内容一致。**误标批为零**，不触发重测。
- 席位构成与事件：原派 9 席中 8 席正常落盘；S3（B07–B09）未落盘未回传、补派 S3b 再截断零落盘，最终拆单批补派 S3c/S3d/S3e 三席补齐（各 20/20 自验通过）；S5 首份回传截断、盘上 60 件完整且复验通过。事件全账见 ADDENDUM-r60 §三，对分数与隔离影响为零。
- 隔离自报汇总（各席回传）：各席均报无隔离接触；输入残损多例均已在各例 basis 注明并降置信（全账见各席回传与 ADDENDUM-r60 §三）。
- 方法源：各席均读 runs/round60/kb-snapshot（REV1 接入后活 method，21 文件；本轮为 REV1 接入后新系列第 1 点，PREREG §0）。
- 冻结后进入评审建包（种子 20261065）；本冻结提交打标签 phase3-round60-blind-frozen。
