# R57 盲测冻结记录（FREEZE-r57）

- 冻结时点：平台盲测 12 席全数落盘后，主持逐席验盘毕。
- 验盘（主持脚本 runs/round57/verify_predictions_host_r57.py，盘上实测）：want 487、files 487、missing []、extra []、bad []——**487/487 全过**（case_id 一致、五字段齐备、confidence∈[0,1]、trigger 三布尔＋reason 齐备）。
- trigger 主持复算：changed_main **158**、reserve_used **39**、disputed **85**（以主持复算为准，席位自报只作对照）。
- tradition 复核（check_tradition_host_r57.py）：卡面有 tradition/system 值者 365 例与 basis 首行全合、**误标 0**；无字段卡 122 例中 33 例标注格式命中检查器标记词、89 例为标注格式变体（basis 首行均明写字段缺失与自决依据，如「输入卡未单列tradition字段」「输入未设tradition字段」「无独立tradition字段」「以system字段载」等），逐条目检无一例与卡面冲突——**误标批为零**，不触发重测。
- 隔离自报汇总（各席回传）：均为文件名级/目录名级接触（round57 根目录 ls 见 judging 目录名、B15B16 对 predictions 目录仅计数 ls、B13B14 写盘前对 predictions 空目录 ls 一次），无一例打开禁读内容，影响核算为零，照例只登记。
- 方法源：各席均读 runs/round57/kb-snapshot（与活 method 及 round56 快照逐文件全等，§0）。
- 冻结后进入评审建包（种子 20261059）；本冻结提交打标签 phase3-round57-blind-frozen。
