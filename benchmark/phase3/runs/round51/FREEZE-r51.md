# R51 平台盲测冻结记录（主持验盘）

- 冻结时点：2026-10-31（Asia/Shanghai），冻结提交见标签 `phase3-round51-blind-frozen`。
- 覆盖：batches.json 25 批 487 例，预测文件 487/487 在盘，缺 0、多 0、坏 0（`verify_predictions_host_r51.py` 输出 HOST VERIFY OK 487/487）。
- 字段验：逐例 case_id 与文件名一致；prediction_text / basis / confidence / trigger 及 trigger 四子字段（changed_main / reserve_used / disputed / reason）全齐；confidence 均在 0–1。
- trigger 主持复算（全 487 例）：changed_main＝92、reserve_used＝87、disputed＝94；与 25 席回传分批计数逐批加总一致；已填入 `analyze_r51.py` 的 host_expected。
- tradition 逐批复核（R50 误标教训的本轮执行）：主持以输入卡 tradition/system 字段对 487 例 basis 首行逐例程序化对勘，485 例直合；MH-001、MH-003 两例为字段口径差——输入卡 tradition 字段为空、system 字段为 meihua，盲测席据 casting_method 自决梅花并在 basis 首行注明，实际所用体系与卡面一致，不构成误标，无须重测覆盖。
- 隔离事项留痕：B14 席开工时一次 `ls -R` 列出 round51/judging/ 下两个脚手架文件名（host-meta、outcome-manifest），仅文件名、未打开未读内容、无案例信息，主持核算影响为零；详见本轮 PREREG-ADDENDUM（收束时落盘）。
- 冻结后预测只读：后续任何改动须以 revert/新轮方式进行，不许原地改写。
