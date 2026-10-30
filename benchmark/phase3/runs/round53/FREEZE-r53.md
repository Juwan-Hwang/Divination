# R53 平台盲测冻结记录（主持验盘）

- 冻结时点：2026-10-31（Asia/Shanghai），冻结提交见标签 `phase3-round53-blind-frozen`。
- 覆盖：batches.json 25 批 487 例，预测文件 487/487 在盘，缺 0、多 0、坏 0（`verify_predictions_host_r53.py` 输出 HOST VERIFY OK 487/487）。
- 字段验：逐例 case_id 与文件名一致；prediction_text / basis / confidence / trigger 及 trigger 四子字段（changed_main / reserve_used / disputed / reason）全齐；confidence 均在 0–1。
- trigger 主持复算（全 487 例）：changed_main＝111、reserve_used＝62、disputed＝88（以主持脚本复算为准，席位分批自报仅作旁证）。changed_main 计数较 R52（39）显著为高，系各席 reason 自释口径不一（冻结方法文本无成文定义、定义债在案），只登记、不作跨轮比较读数。
- tradition 逐批复核（R50 误标教训的本轮执行）：主持以输入卡 tradition/system 字段对 487 例 basis 首行逐例程序化对勘（`check_tradition_host_r53.py`）。365 例卡面有 tradition/system 且 basis 首行直合；115 例卡面无 tradition/system 字段、席位在 basis 首行如实声明「未标注」并自述实际所用体系；余 7 例（WP-001…007）为英文同义表述 "not labelled on the input card"，程序初筛标出后主持逐例复核为同口径、无误标（与 R52 同例同判）。合计 365＋115＋7＝487，误标 0。
- 隔离事项留痕：个别席（B09、B10）写盘时对本轮 predictions 目录做过一次目录级 `ls`，仅见文件名列表（与 batches.json 公开 id 相同）、未打开任何他批预测内容；B21 开工时 ls 时目录为空。主持核算影响为零（承 R51 B14 先例口径）。
- 冻结后预测只读：后续任何改动须以 revert/新轮方式进行，不许原地改写。
