# FREEZE-r66（R66 平台盲测冻结登记，主持盘上验盘）

## 一、验盘结果

- 主持验盘脚本 runs/round66/verify_predictions_host_r66.py 输出：want 487、files 487、missing []、extra []、bad []——**487/487 全过**（case_id 一致、五字段齐、confidence ∈[0,1]、trigger 四键结构齐且三布尔为 bool）。
- trigger 主持复算：changed_main **67**／reserve_used **42**／disputed **51**（与各席回传分项之和逐项全等：67＝2+1+31+2+2+4+22+0+3+0+0、42＝2+4+3+3+1+5+5+0+6+13+0、51＝3+3+10+15+6+3+2+0+7+2+0；将填入 analyze_r66.py 的 host_expected，定稿时断言对勘）。
- 席位构成：原派九席中 S5 回传报错（模型输出截断）且盘上产出为零，主持查盘确认全缺后按判例拆单补派全新席 S5b（B13–B14，40 例）与 S5c（B15，20 例）完成；其余八席一次落盘。各席回传字节数与主持盘上逐批复算逐项全等（S1 103,488／S2 81,575（含重测件，见 §二）／S3 152,935／S4 234,784／S5b 93,223／S5c 49,321／S6 93,980／S7 82,517／S8 90,868／S9 123,952）。**本轮无通配删除事件**（R64 判例连续第二轮零事故）。S2 一次 `ls round66/` 顶层列表仅见子目录名（含 judging 目录名本身、未进入未列内容），登记于 ADDENDUM-r66 §四，核算影响为零。其余各席隔离自报均为只读允许面、无禁读接触。输入残损逐例在 basis 注明并降置信（AS-301–307 无盘面、BQ 卡面六亲名目与纳甲不合诸例、LR-001 无课盘、BZ-301/302 无四柱、BZ-303/304 无盘面仅题面锚点、LY-036 装卦表缺失、LY-537 起 OCR 行序错乱诸例、YM 诸例伏神推定、YY2-004 本卦名缺字、OC-009 四柱未载、MP 批盘面多缺、WP 批无星盘附载、MH-010 无 tradition 字段等），照常例只登记。

## 二、tradition 复核（主持裁定）

- check_tradition_host_r66.py 初检：direct 363／none-labelled 8／flags 116。逐件定性：114 件为 NONE 型（输入卡无 tradition 字段、各席 basis 首行据题面体裁自决且与案例系列一致）；**2 件为实标矛盾**——BZ-303、BZ-304 输入卡自带 tradition＝fengshui，原 S2 产出 basis 含两组首行标示（首组误作 bazi、次组与正文实断均为 fengshui），首行标示与卡载字段矛盾。
- **裁定**：BZ-303、BZ-304 两件作废，由全新重测席（RE1）全盲重测覆盖（未打开作废件、只读两张输入卡与快照）；作废件移存 runs/round66/voided-tradition-bz303-304/（SHA-256：BZ-303 3acb0c98…bce8f、BZ-304 072811cf…7252）。重测件 basis 首行单一标示 tradition＝fengshui、与卡面一致，trigger 三项全 false（非六爻），复算总数不变。错误限于该两件的首行模板残留：同席 BZ-301/302 为同式双组标示但两组均为 bazi、与卡面一致，不构成矛盾；其余各席抽查无同型矛盾。**复检：direct 365／none-labelled 8／flags 114（全为 NONE 型）——误标批为零，不再重测。** 分段口径以 host-meta 为准、不以席位 basis 标签计分（承 R55/R62–R65 判例）。

## 三、冻结状态

- 预测集自本件提交起冻结；评审包以种子 20261072 由 build_judge_packets_r66.py 构建（断言全过：batches id 集与预测集全等、overlay 16/16 逐字、anon 唯一 487/487、双视 JSONL 块 [122,122,122,121] 合计 487、host-meta 键集全等）。
- 方法快照：runs/round66/kb-snapshot（开轮自活 method 生成；与 round65 快照逐文件 diff 为空集，PREREG §0 已登记）。本轮为 R61-REV1 接入后系列第 5 点。
