# R52 平台盲测冻结记录（主持验盘）

- 冻结时点：2026-10-31（Asia/Shanghai），冻结提交见标签 `phase3-round52-blind-frozen`。
- 覆盖：batches.json 25 批 487 例，预测文件 487/487 在盘，缺 0、多 0、坏 0（`verify_predictions_host_r52.py` 输出 HOST VERIFY OK 487/487）。
- 字段验：逐例 case_id 与文件名一致；prediction_text / basis / confidence / trigger 及 trigger 四子字段（changed_main / reserve_used / disputed / reason）全齐；confidence 均在 0–1。
- trigger 主持复算（全 487 例）：changed_main＝39、reserve_used＝39、disputed＝82（以主持脚本复算为准，席位分批自报仅作旁证）；已填入 `analyze_r52.py` 的 host_expected。
- tradition 逐批复核（R50 误标教训的本轮执行）：主持以输入卡 tradition/system 字段对 487 例 basis 首行逐例程序化对勘（`check_tradition_host_r52.py`）。365 例卡面有 tradition/system 且 basis 首行直合；122 例卡面无 tradition/system 字段，席位均在 basis 首行如实声明「未标注」并自述实际所用体系（其中 WP-001…007 共 7 例为英文同义表述 "not labelled"，程序初筛标出后主持逐例复核为同口径、无误标）。MH-001/MH-003 本轮卡面 system＝meihua、席位作断梅花，首行直合（R51 的字段口径差本轮不复现）。LR-001 卡面无盘面、席位声明无盘可依未起用任何一法，属卡面残损事实、非误标。
- 隔离事项留痕：个别席（B22 等）开工时对 `runs/round52/` 做过一次顶层 `ls`，仅见目录名、未打开任何 predictions/judging/final-scores/splits 内容，主持核算影响为零（承 R51 B14 先例口径）。
- 冻结后预测只读：后续任何改动须以 revert/新轮方式进行，不许原地改写。
