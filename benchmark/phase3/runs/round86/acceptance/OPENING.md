# OPENING · holdout29 开封登记（R86 主持）

- 开封条件：R86 平台三项全立（新系列第 2 点、全立计 33；(a) −1.183／(b) 四护栏全立／(c) −1.759，analyze_r86 定稿），照 data/holdout29-seal-log.md 写死条件「封存后首个平台全立轮当轮开封」于 R86 开封。前置复验结论已追记封存日志开封节。
- 盲测：三席读封存时点快照 `runs/round85/kb-snapshot-holdout29` 作断（A 席六壬 13＝DA 5／CYJ 4／BY 4；B 席紫微 13＝ZW-004–016；C 席八字 DS-063），各篇形态以快照原文为准（六壬章冻结原文、紫微章 R84 集成形态、calibration 现行仅第八节）。27/27 冻结后主持验盘登记。
- 建包：`build_acceptance_packets_h29_r86.py`（金标 SHA 断言 `9eb727a3fd312be04aa475976da09552e4c079ab40657257505779a44aef44bf`；packet-ours／packet-master 各 27、anon 集互斥、host-mapping 54 条，前缀 H29O-／H29M-）；评审 anon 种子 20261100。
- 评审：双视各评两包（judgeO1/O2＝我方双视、judgeM1/M2＝大师双视），冻结评审提示逐字（runs/round86/prompts/JUDGE-PROMPT-verbatim.txt；claims 经 host-mapping 回读 acceptance/predictions 全文核验，大师侧 prediction_text 即金标 master_prediction 原文）；分歧 |Δtotal|≥3 独立仲裁替换均值、仲裁席与盲测/评审不兼任。
- 判定：三判据照 R42 PREREG §8（全 low，低污染子集＝全集 27，分开登记表述）；六壬/紫微两段首次在新鲜集受验，分段读数照实登记、只作诊断附读不改判据。未达标→本集标已用、独立诊断 DIAG-H29 随验收执行，CLAIM 立项照 R86 PREREG §3 于 DIAG-H29 后另行开席。
