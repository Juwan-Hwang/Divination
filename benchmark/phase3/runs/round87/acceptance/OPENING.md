# OPENING · holdout30 开封登记（R87 主持）

- 开封条件：R87 平台三项全立（新系列第 3 点、全立计 34；(a) −1.174／(b) 四护栏全立（八字全集 ＋0.112、natal ＋0.462、horary −0.420、六壬 dev8 −1.847）／(c) −1.821、熔断未触，analyze_r87 定稿），照 data/holdout30-seal-log.md 写死条件「封存后首个平台全立轮当轮开封」于 R87 开封。前置复验结论已追记封存日志开封节（三项全过：金标 SHA 主持复读与三读定版全等、28 卡在盘、主持第三道复扫零命中）。
- 盲测：三席读封存时点快照 `runs/round86/kb-snapshot-holdout30` 作断（A 席六壬 14＝DA 5／CYJ 5／BY 4；B 席六爻 WHY 10；C 席六爻 GSZ 4），各篇形态以快照原文为准（六壬章冻结原文、calibration 现行仅第八节）。CYJ 5 例（CYJ-006–010）为 fidelity 降级形态（课式头在场、盘体未载），照封存登记如实作断并降置信、不臆补盘面。28/28 冻结后主持验盘登记。
- 建包：`build_acceptance_packets_h30_r87.py`（金标 SHA 断言 `09e38d9a5f87d1f81b959094035ff266428ca960c96d4fdc1a082643232adcdc`；packet-ours／packet-master 各 28、anon 集互斥、host-mapping 56 条，前缀 H30O-／H30M-）；评审 anon 种子 20261102。
- 评审：双视各评两包（judgeO1/O2＝我方双视、judgeM1/M2＝大师双视），冻结评审提示逐字（runs/round87/prompts/JUDGE-PROMPT-verbatim.txt；claims 经 host-mapping 回读 acceptance/predictions 全文核验，大师侧 prediction_text 即金标 master_prediction 原文）；分歧 |Δtotal|≥3 独立仲裁替换均值、仲裁席与盲测/评审不兼任。
- 判定：三判据照 R42 PREREG §8（全 low，低污染子集＝全集 28，分开登记表述）；六壬/六爻两段分段读数照实登记、只作诊断附读不改判据。未达标→本集标已用、独立诊断 DIAG-H30 随验收执行；修订议程照 R87 PREREG §4 于 DIAG-H30 后另行开席（DIR 居首与紫微 TIM 年龄坐标形态为候选输入，CLAIM 向不得原样重提）。
