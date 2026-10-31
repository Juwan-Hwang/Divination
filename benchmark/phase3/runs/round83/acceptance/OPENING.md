# OPENING · holdout27 开封登记（R83 主持）

- 开封条件：R83 平台三项全立（全立计 30），照 data/holdout27-seal-log.md §七写死条件「封存后首个平台全立轮当轮开封」于 R83 开封（前置复验三项与结论已追记封存日志第十节）。
- 前置复验三项全过：金标 SHA-256 主持开封复测＝封存定版 `81b1d7c4df8428cb014f6054ac113f24c288f7257fc6437f934ca8ba35ac1295`（40,283 字节，无漂移）；输入卡 27 张在盘逐件、无多余；主持第三道复扫已于验封时零命中、开封复核无新增命中面。
- 盲测：三席读封存时点快照 `runs/round82/kb-snapshot-holdout27` 作断（A 席 DS 9／B 席开悟 QM 9／C 席 GSZ 5＋WHY 4），各节形态以快照原文为准，27/27 冻结后验盘登记。
- 建包：`build_acceptance_packets_h27_r83.py`（金标 SHA 断言 `81b1d7c4df8428cb014f6054ac113f24c288f7257fc6437f934ca8ba35ac1295`；packet-ours／packet-master 各 27、anon 集互斥、host-mapping 54 条，前缀 H27O-／H27M-）；评审 anon 种子 20261095。
- 评审：双视各评两包（judgeO1/O2＝我方双视、judgeM1/M2＝大师双视），冻结评审提示逐字；分歧 |Δtotal|≥3 独立仲裁替换均值、无仲裁席与盲测/评审兼任。
- 判定：三判据照 R42 PREREG §8（全 low，低污染子集＝全集 27，分开登记表述）；诊断 DIAG-H27 与 R82-REV1 判读照封存日志 §七写死口径随验收执行（N＝27 不顺延，计数线 ≤ 口径、恰压线计达标）。第十节三态处置于本集判读后、且 holdout28 已封存之后执行（定点基线＝runs/round83/kb-snapshot-holdout28）。
