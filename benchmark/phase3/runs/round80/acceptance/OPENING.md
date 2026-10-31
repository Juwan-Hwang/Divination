# OPENING（holdout24 于 R80 开封记录）

- 触发：R80 平台三项全立（(a) −1.052／(b) 四护栏全立／(c) −1.597，全立计 27），照 PREREG-r80 §7 于本轮开封 holdout24，并随验收诊断执行 R78-REV1 判读（判读口径照 data/holdout24-seal-log.md §七写死值，N＝27 不顺延）。
- 开封前置复验（主持，2026-10-31，全过，结论已追记封存日志 §十一）：金标 SHA-256 再测 `361617fd80fe7edbb80a85274eda9294e9dd89137bafc0a97a0f9b03cc13aa80` 与封存定版全等（35,095 字节、27 行）；输入卡 27 张逐件在盘；主持第三道复扫（runs/round80/rescan_holdout24_host_r80.py，标记集承 R42 PREREG §5）零硬命中。
- 盲测：3 批（A1 DS-019–024＋QM-021–023／A2 QM-024、025、206、207、307–309＋ZCB-012、013／A3 ZCB-014、015＋GSZ-034、038、041、042、043、046、047），读 runs/round79/kb-snapshot-holdout24（含 calibration 第七节），产物 acceptance/predictions/ 27 件主持验盘齐全。
- 建包：build_acceptance_packets_h24_r80.py（anon 种子 20261089；packet-ours／packet-master 各 27 条；金标 SHA 脚本内断言通过；匿名零泄漏自验通过）。
- 评审：双视四席（judgeO1/O2、judgeM1/M2，冻结评审提示逐字），无 |Δ|≥3 分歧、无仲裁。
- 定稿：analyze_acceptance_h24_r80.py 产 judging/final-scores-h24.json。结果与判读见同目录 REPORT.md 与 DIAG-H24.md。
