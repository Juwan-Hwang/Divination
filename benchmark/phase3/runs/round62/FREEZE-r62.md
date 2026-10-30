# FREEZE-r62（R62 平台盲测冻结登记，主持盘上验盘）

## 一、验盘结果

- 主持验盘脚本 runs/round62/verify_predictions_host_r62.py 输出：want 487、files 487、missing []、extra []、bad []——**487/487 全过**（case_id 一致、五字段齐、confidence ∈[0,1]、trigger 四键结构齐且三布尔为 bool）。
- trigger 主持复算：changed_main **123**／reserve_used **76**／disputed **122**（已填入 analyze_r62.py 的 host_expected，定稿时断言对勘）。
- 席位构成：S1–S9 九席原派全数一次落盘（60/60/60/60/60/60/60/40/27），无补派、无截断事件。各席隔离自报均为只读允许面、无禁读接触；输入残损逐例在 basis 注明并降置信（AS-301–307 无星盘、BQ chart_complete=false、LR-001 无课盘、LY-255/339/416/417 两占合载、YM 诸例伏神推定、YY2-004 本卦名缺字、OC-009 四柱未载等），照常例只登记。

## 二、tradition 复核（主持裁定）

- check_tradition_host_r62.py 输出：direct 365／none-labelled 114／flags 8。8 件 flags 逐件定性：LY-017／LY-019／LY-021／LY-022／LY-034／LY-103／LY-105 共 7 件为繁体字形变体（「輸入卡無tradition字段，據題面體裁自決」与简体登记式仅字形之差，内容与口径全等）；MP-009 1 件为席位自述「卡内 asked_at 自载『卜卦』、据题面自决归六爻，盘面全缺已注明残损并三项 trigger 全 false 留痕」，与 S6 回传自报一致，属自决留痕而非误标。
- **裁定：误标批为零，不重测。** 依据与 R61 判例同式：被旗标各例均无卡载 tradition 可供违背；分段口径以 host-meta 为准、不以席位 basis 标签计分。

## 三、冻结状态

- 预测集自本件提交起冻结；评审包以种子 20261068 由 build_judge_packets_r62.py 构建（断言全过：batches id 集与预测集全等、overlay 16/16 逐字、anon 唯一 487/487、双视 JSONL 块 [122,122,122,121] 合计 487、host-meta 键集全等）。
- 方法快照：runs/round62/kb-snapshot（开轮自活 method 生成；与 round61 快照之差恰为 SKILL.md＋references/calibration.md 两件＝R61-REV1 集成面，PREREG §0 已登记）。本轮为 R61-REV1 接入后系列第 1 点。
