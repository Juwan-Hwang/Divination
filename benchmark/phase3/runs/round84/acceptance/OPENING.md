# OPENING · holdout28 开封登记（R84 主持）

- 开封条件：R84 平台三项全立（全立计 31；(a) −1.084／(b) 四护栏全立／(c) −1.821，analyze_r84 定稿），照 data/holdout28-seal-log.md §七写死条件「封存后首个平台全立轮当轮开封」于 R84 开封。
- 前置复验三项全过（结论已追记封存日志 §十）：金标 SHA-256 开封再测＝封存定版 `e985d5d1552a8583e22297e4e9ee08cc47c3fb797056ec1f8819489d481e3675`（42,736 字节、27 行，无漂移）；输入卡 27 张在盘逐件；主持第三道复扫（开封轮，runs/round84/host_opening_scan_h28_r84.py）零命中。
- 盲测：三席读封存时点快照 `runs/round83/kb-snapshot-holdout28` 作断（A 席 DS 13／B 席 GSZ 6＋WHY 5／C 席 QM 3），各节形态以快照原文为准；C 席奇门 3 例须执行快照 calibration 第十一节并在 basis 留其四行留痕（护栏丁执行面）。27/27 冻结后主持验盘登记。
- 建包：`build_acceptance_packets_h28_r84.py`（金标 SHA 断言 `e985d5d1552a8583e22297e4e9ee08cc47c3fb797056ec1f8819489d481e3675`；packet-ours／packet-master 各 27、anon 集互斥、host-mapping 54 条，前缀 H28O-／H28M-）；评审 anon 种子 20261097。
- 评审：双视各评两包（judgeO1/O2＝我方双视、judgeM1/M2＝大师双视），冻结评审提示逐字（runs/round84/prompts/JUDGE-PROMPT-verbatim.txt；claims 经 host-mapping 回读 acceptance/predictions 全文核验）；分歧 |Δtotal|≥3 独立仲裁替换均值、仲裁席与盲测/评审不兼任。
- 判定：三判据照 R42 PREREG §8（全 low，低污染子集＝全集 27，分开登记表述）；诊断 DIAG-H28 与 R83-REV1 判读照封存日志 §七写死口径随验收执行（段 n＝3 计数口径、恰压线计达标、判读一次性不顺延）。第十一节三态处置于本集判读后、且 holdout29 组集裁定（本轮 expansion 核查后裁定，见 REPORT）落定后执行；无 holdout29 封存时定点基线＝runs/round84/kb-snapshot。
