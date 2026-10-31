# OPENING · holdout26 开封登记（R82 主持）

- 开封条件：R82 平台三项全立（全立计 29），照 data/holdout26-seal-log.md 写死条件「封存后首个平台全立轮当轮开封」于 R82 开封（结论已追记封存日志第十节）。
- 前置复验三项全过：金标 SHA-256 主持开封复测＝封存定版 `2d5bad70747e0d02d6df5d4d8ee1dc6fcc0ac751bfc52aa4877dfe074df98e97`；输入卡 27 张在盘；主持第三道复扫（runs/round82/host_scan_h26_r82.py）零命中。
- 盲测：三席读封存时点快照 `runs/round81/kb-snapshot-holdout26` 作断（A 席 DS 9／B 席开悟 QM 9／C 席 GSZ 5＋WHY 4），27/27 冻结后另行提交打标。
- 建包：`build_acceptance_packets_h26_r82.py`（金标 SHA 断言；packet-ours／packet-master 各 27、anon 集互斥、host-mapping 54 条）；评审 anon 种子 20261093。
- 评审：双视各评两包（judgeO1/O2＝我方双视、judgeM1/M2＝大师双视），冻结评审提示逐字；分歧 |Δtotal|≥3 独立仲裁。
- 判定：三判据照 R42 PREREG §8（全 low，低污染子集＝全集 27，分开登记表述）；诊断 DIAG-H26 与 R81-REV1 判读照 METHOD-INTEGRATION-r81 写死口径随验收执行（N＝27 不顺延）。
