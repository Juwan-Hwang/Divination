# FREEZE-r72（R72 平台盲测冻结登记，主持盘上验盘）

## 一、验盘结果

- 主持验盘脚本 runs/round72/verify_predictions_host_r72.py 输出：want 487、files 487、missing []、extra []、bad []——**487/487 全过**（case_id 一致、五字段齐、confidence ∈[0,1]、trigger 四键结构齐且三布尔为 bool）。
- trigger 主持复算：changed_main **32**／reserve_used **27**／disputed **57**（与十席回传分项之和逐项全等：32＝2+0+0+9+3+7+0+8+3+0、27＝2+0+0+5+3+4+0+4+3+6、57＝3+3+0+18+5+13+0+9+5+1；将填入 analyze_r72.py 的 host_expected，定稿时断言对勘）。
- 席位构成：十席全部一次派单一次落盘（S9 面按 PREREG §7 预拆为 S9＝B23＋B25、S10＝B24，防截断工法连续第三轮生效、本轮无截断补派）；**本轮无通配删除事件**（R64 判例连续第八轮零事故）。**目录计数定规首轮执行**：本轮派单已明文禁止任何 runs/ 目录列表/计数（承 R71 S5 登记事项、PREREG §7 写死），十席回传均明示未执行目录列表/计数，无 S5 型动作自报。席位会话内 exec 非零退出记录三起（S1、S3、S10）：S3 自报生成脚本首跑因分段断言累计例数与批次边界不符中止于写盘前、修正断言后重跑成功；S1/S10 无自报异常——三席产出均经主持盘上逐件复验完整有效，照 R68 判例记完成、只登记。各席中间件均为本轮目录内席位唯一名文件（gen_r72_s1–s10.py），随冻结提交入仓备查；隔离自报十席均为只读允许面、无禁读接触。输入残损逐例在 basis 注明并降置信（BQ 全例 chart_complete=false 仅卦象节录、AS-301–307 无星盘数据、AS 多例仅 Lilly 散文位置、BZ-301–304 无四柱/盘据、LR-001 无课盘数据、LR3-116 三传天干与旬空未载、LY-026 变爻 OCR 乱码、LY-034 卡面 setting 残存应期字样已注明不采用、LY-036 装卦未能可靠还原、LY-105 二手转录、LY-503 日干支不全、LY-525 月建不全、LY-529–536 原文未明记月日、LY-620/621 逐爻表未列动爻属复原、LY-626 题面盘面月日不一、OC-009 四柱未给、OC-023 动爻未给由变卦反推、YM-004 未记月建、YM-032 性别指针单薄、YY-006 未载月建日辰、YY-023 动爻与装卦不合、YY2-003 卡面空亡与常法不一从卡面落断、YY2-004 本卦名缺字且盘面为 null、MP 全批无卦象/命盘附卡、MH-010 与 MP-001–016 卡面未标注 tradition 已如实标注诸例），照常例只登记。

## 二、tradition 复核（主持裁定，含 R72 声明组数加扫与检查器补英文变体口径登记）

- check_tradition_host_r72.py 初检（**本轮起未标注关键词集已补英文变体**「no tradition field」「bears no tradition」「no tradition indicated」「tradition not stated」「tradition not specified」等、大小写不敏感匹配，承 R71 FREEZE §二登记、STAGE-SUMMARY-56 R72 清单第 1 项）：direct 365／none-labelled 122／flags **0**。
- **与 R71 初检的可比性登记**：R71 初检 flags 7 件全为英文首行变体（WP-001–007「Card bears no tradition field…」）未命中中英关键词集、经主持逐件核实陈述属实裁定不成立；本轮补集后该变体类已被覆盖——none-labelled 由 R71 的 115 升至 122（恰 +7、与 WP 类件数吻合），flags 归零。初检口径差异仅此关键词集再扩充一处（简繁集承 R71 不变），其余检查逻辑逐字承 R71。**措辞不实型旗标连续第二轮归零**。
- **声明组数加扫（承 R67）**：逐件扫 basis 内行首 tradition 声明组——多组声明文件 **0** 件、互斥冲突组 **0** 件。
- 分段口径以 host-meta 为准、不以席位 basis 标签计分（承 R55/R62–R71 判例）。

## 三、冻结状态

- 预测集自本件提交起冻结；评审包以种子 20261078 由 build_judge_packets_r72.py 构建（断言全过：batches id 集与预测集全等、overlay 16/16 逐字、anon 唯一 487/487、双视 JSONL 块 [122,122,122,121] 合计 487、host-meta 键集全等、carry 层十八层计数断言全过含 _r72 层 83）。
- 方法快照：runs/round72/kb-snapshot（开轮自活 method 生成；与 round71 快照逐文件 diff 为空集，PREREG §0 已登记）。本轮为 R61-REV1 接入后系列第 11 点。
