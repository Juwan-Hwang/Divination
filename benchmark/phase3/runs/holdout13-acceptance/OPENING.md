# holdout13 开封记录（2026-10-30）

- 开封依据：R35 平台判据三项全立（runs/round35/analyze_r35.py 实测：(a) 全集 −1.148 ≥ −1.371；(b) 护栏全过——八字 −0.164 ≥ −0.449、natal +0.692 ≥ +0.290、horary −0.150 ≥ −0.760、六壬 dev8 −1.986 ≥ −2.593；(c) 新口径单轮 −1.758 ≥ −1.93、熔断未触发），按 runs/round35/PREREG.md §3 开封。
- 金标验核：开封前 sha256sum holdout13/test_gold.jsonl ＝ 75c5349d6184d5cace454dadb790433eabac731f38884b889cd1f9bd67aab483，与 SEALED.md 及 data/holdout13-seal-log.md 封存值逐字一致（2026-10-30 主持实测）。
- 送验 artifact：runs/round35/kb-snapshot（与现行活 method 及 R34 快照零差异，EVIDENCE-kb-snapshot.sha256 在案）。
- 构成与限度（SEALED.md 照引）：40 例（六壬 16＝DA 8/BY 5/CY 卷六 3、八字 12＝QL 10/NL 2、测字 CZ 12、六爻 0——有界普查实得 0、缺位登记），全 A/A-low、全 low（低污染子集＝全集）；粹言 3 例课式仅干支级；QL-030 输入卡删后事词一条（金标不动）。验收结论只对本集构成所及口径发言：**本集无六爻例，六爻执行水平不在本轮验收覆盖内**。
- 执行：盲测 3 批混编（batches.json，按源 stride 混编、来源构成对席位不言明），冻结盲测提示（轮次 R35-acceptance），输入只给 holdout13-inputs/；评审我方/大师双包各独立双评审＋|Δtotal|≥3 仲裁；达标三判据照 R35 PREREG §3（全集口径＝低污染口径，本集全 low）。
