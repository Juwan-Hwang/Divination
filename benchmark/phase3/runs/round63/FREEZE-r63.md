# FREEZE-r63（R63 平台盲测冻结登记，主持盘上验盘）

## 一、验盘结果

- 主持验盘脚本 runs/round63/verify_predictions_host_r63.py 输出：want 487、files 487、missing []、extra []、bad []——**487/487 全过**（case_id 一致、五字段齐、confidence ∈[0,1]、trigger 四键结构齐且三布尔为 bool）。
- trigger 主持复算：changed_main **87**／reserve_used **54**／disputed **39**（已填入 analyze_r63.py 的 host_expected，定稿时断言对勘）。
- 席位构成：原派九席中八席一次落盘（S1 60／S2 60／S3 60／S4 60／S6 60／S7 60／S8 40／S9 27）；**S5（B13–B15）回传截断、盘上零落盘**，主持间隔复查确认真未落盘后照 R61 S4 判例拆单批补派全新席 S5a（B13 20）／S5b（B14 20）／S5c（B15 20），三席均一次落盘（事件账 ADDENDUM-r63 §四）。原 S5 席在 round63 内遗留中间件四件（dump_r63_s5.py、inputs_r63_s5.txt、analyze_r63_s5.py、analysis_r63_s5.txt）随冻结提交留痕，不作任何分数依据。各席隔离自报均为只读允许面、无禁读接触；S6 两处轻微越界自报（round63 根目录一次 ls 仅见目录名、/tmp 空目录 mkdir 无写入）主持核算影响为零（ADDENDUM-r63 §四）。输入残损逐例在 basis 注明并降置信（AS-301–307 无星盘、BQ chart_complete=false、LR-001 无课盘、LY-036 仅卦名与空亡、LY-255/339/416/417 两占合载、YM 诸例伏神推定、YY2-004 本卦名缺字出「无断」件、OC-009 四柱未载、MP 批盘面全缺等），照常例只登记。

## 二、tradition 复核（主持裁定）

- check_tradition_host_r63.py 输出：direct 365／none-labelled 109／flags 13。13 件 flags 全为 WP-001–013：输入卡均无 tradition 字段，席位 basis 首行以英文自述「no tradition field on card (noted as absent); decided from the card's genre」——与 R55 WP-001–007 旗标同型（英文自决留痕未中中文登记式关键词而被机械旗标），逐件内容与口径均为「无字段＋据题面体裁自决」，与 S7 回传自报一致。
- **裁定：误标批为零，不重测。** 依据与 R55/R62 判例同式：被旗标各例均无卡载 tradition 可供违背；分段口径以 host-meta 为准、不以席位 basis 标签计分。

## 三、冻结状态

- 预测集自本件提交起冻结；评审包以种子 20261069 由 build_judge_packets_r63.py 构建（断言全过：batches id 集与预测集全等、overlay 16/16 逐字、anon 唯一 487/487、双视 JSONL 块 [122,122,122,121] 合计 487、host-meta 键集全等）。
- 方法快照：runs/round63/kb-snapshot（开轮自活 method 生成；与 round62 快照逐文件 diff 为空集，PREREG §0 已登记）。本轮为 R61-REV1 接入后系列第 2 点。
