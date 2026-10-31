# FREEZE-r65（R65 平台盲测冻结登记，主持盘上验盘）

## 一、验盘结果

- 主持验盘脚本 runs/round65/verify_predictions_host_r65.py 输出：want 487、files 487、missing []、extra []、bad []——**487/487 全过**（case_id 一致、五字段齐、confidence ∈[0,1]、trigger 四键结构齐且三布尔为 bool）。
- trigger 主持复算：changed_main **164**／reserve_used **50**／disputed **95**（与九席回传分项之和逐项全等：164＝2+8+40+32+24+23+0+21+14、50＝5+5+5+8+2+5+0+8+12、95＝4+4+22+10+36+12+0+4+3；将填入 analyze_r65.py 的 host_expected，定稿时断言对勘）。
- 席位构成：九席全数落盘（S1 60／S2 60／S3 60／S4 60／S5 60／S6 60／S7 40／S8 40／S9 47），各席回传字节数与主持盘上逐批复算逐项全等（S1 107,974／S2 75,849／S3 158,869／S4 153,559／S5 134,519／S6 118,075／S7 65,938／S8 77,994／S9 78,785）。**本轮无通配删除事件**（R65 派单明文禁令首轮执行即无事故）。S4 两项隔离自报（开工初期对本轮 predictions 目录一次 ls、输出未显示条目未打开任何文件；cast_iching.py 以 --help 误触随机起卦一卦、未用于任何断语）登记于 ADDENDUM-r65 §四，核算影响为零。其余各席隔离自报均为只读允许面、无禁读接触。输入残损逐例在 basis 注明并降置信（AS-301–307 无盘面、BQ chart_complete=false、LR-001 无课盘、BZ-301/302 无四柱、LY-036 装卦表缺失、LY-255/339/416/417 等两占合载、LY-537 起 OCR 行序错乱诸例、YM 诸例伏神推定、YY2-004 本卦名缺字、OC-009 四柱未载、MP 批盘面多缺、WP 批无星盘附载、MH-010 无 tradition 字段等），照常例只登记。

## 二、tradition 复核（主持裁定）

- check_tradition_host_r65.py 输出：direct 365／none-labelled 0／flags 122。122 件 flags 全为 NONE 型：主持抽验 AS-001/WP-001/MP-017 输入卡顶层无 tradition/system 字段（全量口径与 R64 之 97 flags＋25 none-labelled＝122 为同一群体），各席 basis 首行所标均据题面体裁自决且与案例系列一致（AS→horary/astrology、BZ→八字、LR2/LR3→六壬、LY/YM/YY→六爻、OC→八字/梅花/大六壬、WP→西洋占星/塔罗、MP→现代预测），与 R64 差异仅在各席首行措辞由「未标注」式改为直书 tradition= 式。
- **裁定：误标批为零，不重测。** 依据与 R55/R62/R63/R64 判例同式：被旗标各例均无卡载 tradition 可供违背；分段口径以 host-meta 为准、不以席位 basis 标签计分。

## 三、冻结状态

- 预测集自本件提交起冻结；评审包以种子 20261071 由 build_judge_packets_r65.py 构建（断言全过：batches id 集与预测集全等、overlay 16/16 逐字、anon 唯一 487/487、双视 JSONL 块 [122,122,122,121] 合计 487、host-meta 键集全等）。
- 方法快照：runs/round65/kb-snapshot（开轮自活 method 生成；与 round64 快照逐文件 diff 为空集，PREREG §0 已登记）。本轮为 R61-REV1 接入后系列第 4 点。
