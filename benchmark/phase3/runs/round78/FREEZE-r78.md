# FREEZE-r78 · 平台盲测冻结记录（R78 主持验盘）

- 验盘脚本：runs/round78/verify_predictions_host_r78.py（本轮新写唯一名），主持直跑。
- 结果：应到 487、实到 487、缺 0、溢 0、坏件 0；字段集（case_id/prediction_text/basis/confidence/trigger 四键）与 trigger 四键全合，confidence 全在 0–1。
- trigger 主持复算：changed_main **30**／reserve_used **57**／disputed **59**，与十席回传逐席加总逐项吻合（S1 3/16/3、S2 0/0/3、S3 8/5/3、S4 5/7/8、S5 3/9/27、S6 4/3/3、S7 0/0/0、S8 2/7/3、S9 0/4/8、S10 5/6/1）。
- tradition 首行复核（检查器三口径：卡面值逐字照录／未标注如实声明／变体列单）：卡面载 tradition/system 365 例、无标注 122 例，**旗标 0**。检查器首跑 37 旗经主持逐条读原文判明全为检查器误报（「未载」系同行盘面残损语、繁体「未標註」之「標」未入正则），修检查器口径（未[标標][注註]＋值在场优先）后复跑旗标 0；首行模板 64 种，无全批统一套话。声明组数一致性：各席 basis 首行与其回传声明逐席抽验相符。
- 席位异常登记（要点）：BQ 全面 chart_complete=false 残盘作断（S1）；MP-001–016 无占具卡按题面事实定断（S6）；OC-009 无四柱、WP-007 无牌面（S7）；LY-529–536 原文未明记月日（S5）；YY2-004 本卦名缺字、盘面 null 弱断（S9）；BZ-302 无四柱（S2）。均已逐例 basis 注明并降置信，不臆补。
- 隔离：十席均自报未打开 judging/、他轮 predictions、金标/结局/splits；未为查 trigger 定义 grep 全仓；脚本均本轮目录内唯一名；无 /tmp 写入自报。
- 冻结口径：本文件落盘＋提交＋标签 phase3-round78-blind-frozen 后，predictions 不再改动；评审只读冻结件。
