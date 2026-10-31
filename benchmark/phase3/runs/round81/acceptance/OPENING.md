# OPENING · holdout25 开封登记（R81 主持）

- 开封条件：R81 平台三项全立（全立计 28），照 PREREG §2 与 data/holdout25-seal-log.md §七写死条件当轮开封。
- 前置复验三项全过（封存日志 §十二）：金标 SHA-256 主持复测＝封存定版 `52cda7c156d5575ee2edb12e787ae0ee6b80add85e14be9fd2d108b76e21f3ad`；输入卡 27 张在盘；主持第三道复扫零命中。
- 盲测：三席读封存时点快照 `runs/round80/kb-snapshot-holdout25` 作断，27/27 冻结（标签 phase3-round81-acceptance-blind-frozen）。
- 建包：`build_acceptance_packets_h25_r81.py`（金标 SHA 断言通过；packet-ours／packet-master 各 27、anon 集互斥、host-mapping 54 条）；评审 anon 种子 20261091。
- 评审：双视各评两包（judgeO1/O2＝我方双视、judgeM1/M2＝大师双视），冻结评审提示逐字；分歧 |Δtotal|≥3 独立仲裁。
- 判定：三判据照 R42 PREREG §8；诊断 DIAG-H25 与 R80-REV1 判读照 PREREG §2 写死口径随验收执行。
