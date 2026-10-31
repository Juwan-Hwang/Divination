# FREEZE-r88 — R88 平台盲测冻结登记

- 冻结时点：2026-11-01（Asia/Shanghai）。方法快照 runs/round88/kb-snapshot（与 holdout31 封存快照 21/21 全等；与 R87 平台快照差异恰 {SKILL.md, references/calibration.md}，登记为 R87-REV1 接入后系列第 1 点，见 PREREG §0/§1）。
- 盲测席：13 席分批执行（每席两批约 40 例、B25 单批 7 例），冻结盲测提示逐字（prompts/BLIND-PROMPT-verbatim.txt，SHA-256 5be8e1bc…d71 与 calib-r17 定本全等）。
- 主持验盘（verify_predictions_host_r88.py，输出 verify-predictions-host-r88.json）：want 487、files 487、missing 0、extra 0、bad 0（JSON 可解析、五字段齐、case_id 一致、confidence∈[0,1]、trigger 三布尔为 bool 全过）。
- trigger 主持复算（全 487 例 prediction 文件）：changed_main 12、reserve_used 32、disputed 40；reason 非空 191 例。已回填 analyze_r88.py 的 host_expected（断言标配）。
- tradition 首行初检：旗标候选 1 件，主持回读原卡裁定如下——
  - AS-301：卡面顶层确载 tradition＝astrology，席位 basis 首行误称「卡面未标注 tradition 字段」——留痕失实一件。席位断语本身按现代占星作出（与卡面体系一致），失实仅在首行留痕；冻结照预测原样不改，登记备查，不补派、不改分面。
- 声明组互斥加扫：候选 0 件。
- 席位自报登记：B03+B04 席曾对 kb-snapshot 子目录做一次文件名列举（方法源、非 runs 预测/评分目录，属派单许可范围）；B15+B16 席 LY-523 写后自查订正 basis 旬空推算一处（方向与主坐标未变，已自报）；各席残损登记（YY2-004 无装卦、LR-001 无盘、AS-301–307 无盘面、BQ 全批 chart_complete=false 等）均已入各例 basis 并降置信，照冻结提示口径处理。
- 冻结后预测文件只读：后续评审只读 predictions/ 与 judging/ 数据包；任何改动须作废重冻并登记。
