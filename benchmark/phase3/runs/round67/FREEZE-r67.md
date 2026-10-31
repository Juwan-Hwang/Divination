# FREEZE-r67（R67 平台盲测冻结登记，主持盘上验盘）

## 一、验盘结果

- 主持验盘脚本 runs/round67/verify_predictions_host_r67.py 输出：want 487、files 487、missing []、extra []、bad []——**487/487 全过**（case_id 一致、五字段齐、confidence ∈[0,1]、trigger 四键结构齐且三布尔为 bool）。
- trigger 主持复算：changed_main **44**／reserve_used **64**／disputed **72**（与各席回传分项之和逐项全等：44＝3+3+10+3+2+3+13+0+3+4、64＝4+4+4+13+6+4+10+0+10+9、72＝6+1+21+7+4+5+16+0+6+6；将填入 analyze_r67.py 的 host_expected，定稿时断言对勘）。
- 席位构成：原派九席中 S4 回传因模型输出上限截断而报错，主持即时查盘为 0/60、间隔复查确认全缺后按判例拆单补派全新席 S4b（B10–B11，40 例）与 S4c（B12，20 例）完成；其余八席一次落盘。各席回传字节数与主持盘上逐批复算逐项全等（S1 82,136／S2 85,937／S3 100,695／S4b 112,313／S4c 59,678／S5 113,358／S6 152,791／S7 60,960／S8 103,312／S9 97,180）。**本轮无通配删除事件**（R64 判例连续第三轮零事故）。各席隔离自报均为只读允许面（batches.json、本批 inputs-dev12 输入卡、kb-snapshot、prompts 原件），无禁读接触、无隔离事件。输入残损逐例在 basis 注明并降置信（AS-301–307 无盘面、BQ 卡 chart_complete=false 仅卦名/变卦、BZ-301/302 无四柱、LR-001 无课盘、MP 全批无盘面材料、LY-036/LY-626 装卦 OCR 行序错乱、YY2-004 本卦名缺字、OC-009 四柱未载、WP 批无星盘附载、YM-004 未记月建诸例），照常例只登记。

## 二、tradition 复核（主持裁定，含 R67 声明组数加扫）

- check_tradition_host_r67.py 初检：direct 365／none-labelled 103／flags 19。19 件逐件定性：**全为 NONE 型**（输入卡（inputs-dev12）无 tradition/system 字段、各席 basis 首行据题面体裁自决且与 host-meta 及案例系列一致；其中 MP-001–016 等件以繁体「未標註」字形注明未标注、未命中复核脚本的简体关键词表，故列 flags，非标示缺失）。
- **声明组数加扫（R67 新增，承 R66 BZ-303/304 教训与 STAGE-SUMMARY-51 第 5 项）**：逐件扫 basis 内行首 tradition 声明组——多组声明文件 **0** 件、互斥冲突组 **0** 件。本轮各席均为单一标示，无 R66 型双组误标，**误标批为零，不重测**。BZ-303/304 本轮由 S2 按卡面 fengshui 单一标示作断（卡自带字段），复核一致。
- 措辞登记两件（不重测）：BZ-021 basis 首行作「tradition: bazi（八字；卡面 tradition=bazi）」、ZY-003 作「tradition: yijing（与卡面一致）」——两例 inputs-dev12 卡面实无 tradition/system 字段，括号内「卡面」措辞不实；惟标示值（bazi／yijing）与 host-meta 及体裁逐一全等、作断体系无误，属席位措辞瑕疵，只登记备后续派单注记（注明未标注者不得虚称卡面载有）。分段口径以 host-meta 为准、不以席位 basis 标签计分（承 R55/R62–R66 判例）。

## 三、冻结状态

- 预测集自本件提交起冻结；评审包以种子 20261073 由 build_judge_packets_r67.py 构建（断言全过：batches id 集与预测集全等、overlay 16/16 逐字、anon 唯一 487/487、双视 JSONL 块 [122,122,122,121] 合计 487、host-meta 键集全等）。
- 方法快照：runs/round67/kb-snapshot（开轮自活 method 生成；与 round66 快照逐文件 diff 为空集，PREREG §0 已登记）。本轮为 R61-REV1 接入后系列第 6 点。
