# FREEZE-r68（R68 平台盲测冻结登记，主持盘上验盘）

## 一、验盘结果

- 主持验盘脚本 runs/round68/verify_predictions_host_r68.py 输出：want 487、files 487、missing []、extra []、bad []——**487/487 全过**（case_id 一致、五字段齐、confidence ∈[0,1]、trigger 四键结构齐且三布尔为 bool）。
- trigger 主持复算：changed_main **45**／reserve_used **52**／disputed **61**（与各席回传分项之和逐项全等：45＝3+0+2+24+7+0+0+2+7、52＝4+6+1+7+14+4+0+5+11、61＝4+4+2+5+11+13+0+15+7；将填入 analyze_r68.py 的 host_expected，定稿时断言对勘）。
- 席位构成：九席一次派单全部一次落盘，无拆单补派。各席回传字节数与主持盘上逐批复算逐项全等（S1 75,314／S2 83,203／S3 115,682／S4 140,555／S5 95,744／S6 102,948／S7 40,875／S8 79,226／S9 82,846）。**本轮无通配删除事件**（R64 判例连续第四轮零事故）。隔离自报：S1 曾对 runs/round68/ 父目录做一次 ls（仅见 judging 目录名、未列其内容、未打开任何 judging/predictions/金标文件），主持核算影响为零、只登记（ADDENDUM-r68 §四）；其余各席自报均为只读允许面（batches.json、本批 inputs-dev12 输入卡、kb-snapshot、prompts 原件），无禁读接触。输入残损逐例在 basis 注明并降置信（AS-301–307 与 BQ 批无盘面／chart_complete=false、BZ-301–304 无四柱、LR-001 无课盘、LR3-107 课式首字残泐、LY-036 装卦残损、LY-537–543 与 LY-626–629 装卦表 OCR 错乱或未能可靠还原、LY-417 四卦名仅两盘装卦、MP 全批无盘面材料、OC-009 四柱未载、WP 批无星盘附载、YY2-004 本卦名缺字、YM-004 未记月建诸例），照常例只登记。

## 二、tradition 复核（主持裁定，含 R68 声明组数加扫）

- check_tradition_host_r68.py 初检：direct 365／none-labelled 122／flags **0**。R68 派单措辞注记（PREREG §7：未标注者如实写未标注、不得虚称卡面载有 tradition 字段）本轮生效——R67 的 19 件 NONE 型 flags 本轮归零，BZ-021/ZY-003 式括号措辞不实零出现；全部无字段卡均由各席于 basis 首行如实注明未标注并按题面体裁自决。
- **声明组数加扫（承 R67）**：逐件扫 basis 内行首 tradition 声明组——多组声明文件 **0** 件、互斥冲突组 **0** 件。**误标批为零，不重测**。
- 分段口径以 host-meta 为准、不以席位 basis 标签计分（承 R55/R62–R67 判例）。

## 三、冻结状态

- 预测集自本件提交起冻结；评审包以种子 20261074 由 build_judge_packets_r68.py 构建（断言全过：batches id 集与预测集全等、overlay 16/16 逐字、anon 唯一 487/487、双视 JSONL 块 [122,122,122,121] 合计 487、host-meta 键集全等）。
- 方法快照：runs/round68/kb-snapshot（开轮自活 method 生成；与 round67 快照逐文件 diff 为空集，PREREG §0 已登记）。本轮为 R61-REV1 接入后系列第 7 点。
