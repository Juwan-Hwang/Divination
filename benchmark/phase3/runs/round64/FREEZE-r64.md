# FREEZE-r64（R64 平台盲测冻结登记，主持盘上验盘）

## 一、验盘结果

- 主持验盘脚本 runs/round64/verify_predictions_host_r64.py 输出：want 487、files 487、missing []、extra []、bad []——**487/487 全过**（case_id 一致、五字段齐、confidence ∈[0,1]、trigger 四键结构齐且三布尔为 bool）。
- trigger 主持复算：changed_main **52**／reserve_used **54**／disputed **64**（已填入 analyze_r64.py 的 host_expected，定稿时断言对勘）。
- 席位构成：九席全数落盘（S1 60／S2 60／S3 60／S4 60／S5 60／S6 60／S7 40／S8 40／S9 47）。**S6 通配删除事件**：S6 重跑自身脚本前以 `rm -f predictions/LY-*.json predictions/MH-*.json predictions/MP-*.json` 误删他席已落盘文件 131 件（S2 之 LY-001–008 共 8、S3 全批 60、S4 全批 60、S7 之 MP-017/018/019 共 3），席位自报后主持处置：以各席自身确定性生成脚本原样重跑恢复（S3 另加跑其 s3_fix36.py 补丁件恢复 LY-036 终版）。恢复验核三路全等：① 幸存文件（S2 之 BZ-029、S7 之 OC-001）重跑前后 SHA-256 不变，脚本确定性得证；② 被删文件字节数与各席回传逐件/逐批全等（S2 LY 八件逐件、S3 三批总字节 71032/72206/69071、S4 六十件逐件、S7 MP 三件逐件）；③ 恢复后全量验盘 487/487、trigger 复算与各席回传分项之和相符（S5 分项 1/8/2 由总和反推、与盘上直算一致）。事件全账见 ADDENDUM-r64 §四。S1/S8 回传含最终 ls 汇总时被动瞥见他批文件名（未读内容），照 R63 S6 判例登记、影响为零。各席其余隔离自报均为只读允许面、无禁读接触。输入残损逐例在 basis 注明并降置信（AS-301–307 无盘面、BQ chart_complete=false、LR-001 无课盘、LY-036 装卦表 OCR 错乱、LY-255/339/416/417 两占合载、YM 诸例伏神推定、YY2-004 本卦名缺字出存疑件、OC-009 四柱未载、MP 批盘面多缺、MH-010 无 tradition 字段等），照常例只登记。

## 二、tradition 复核（主持裁定）

- check_tradition_host_r64.py 输出：direct 365／none-labelled 25／flags 97。97 件 flags 全为 NONE 型：主持逐类回卡复核——被旗标各例输入卡顶层及全文均无 tradition/system 字段（抽验 LY-017/LY-002/BZ-032/LR2-013 全文检索无此键），无卡载 tradition 可供违背；各席 basis 首行所标均据题面体裁自决且与案例系列一致（AS→horary/astrology、BZ→八字、LR2/LR3→六壬、LY→六爻、OC→八字/梅花/大六壬、WP→西洋占星/塔罗），仅登记式措辞与机械关键词不合（「tradition: X」「tradition=X」式、或误写「输入卡字段自带」——字段实不存在，措辞不确一并登记）。
- **裁定：误标批为零，不重测。** 依据与 R55/R62/R63 判例同式：被旗标各例均无卡载 tradition 可供违背；分段口径以 host-meta 为准、不以席位 basis 标签计分。

## 三、冻结状态

- 预测集自本件提交起冻结；评审包以种子 20261070 由 build_judge_packets_r64.py 构建（断言全过：batches id 集与预测集全等、overlay 16/16 逐字、anon 唯一 487/487、双视 JSONL 块 [122,122,122,121] 合计 487、host-meta 键集全等）。
- 方法快照：runs/round64/kb-snapshot（开轮自活 method 生成；与 round63 快照逐文件 diff 为空集，PREREG §0 已登记）。本轮为 R61-REV1 接入后系列第 3 点。
