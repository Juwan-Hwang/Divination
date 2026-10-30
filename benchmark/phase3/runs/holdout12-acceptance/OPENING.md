# holdout12 开封记录（2026-10-30）

- 开封依据：R34 平台判据三项全立（runs/round34/analyze_r34.py 实测：(a) 全集 −1.099 ≥ −1.371；(b) 护栏全过——八字 −0.078 ≥ −0.449、natal +0.788 ≥ +0.290、horary −0.400 ≥ −0.760、六壬 dev8 −2.097 ≥ −2.593；(c) 合读 −1.786 ≥ −1.93 且 R34 单轮 −1.766、熔断未触发），按 runs/round34/PREREG.md §3 开封。
- 金标验核：开封前 sha256sum holdout12/test_gold.jsonl ＝ 490679552b5bcbff08df369046f977750900f7396857714a51aa438e16b30c90，与 SEALED.md 及 data/holdout12-seal-log.md 封存值逐字一致（2026-10-30T03:45Z 主持实测）。
- 送验 artifact：runs/round34/kb-snapshot（与 round33 快照逐字一致，EVIDENCE-kb-snapshot.sha256 在案）。
- 构成与限度（SEALED.md 照引）：49 例（六壬 27＝DA 9/BY 9/CY 5/CYJ 4、八字 13＝QL 8/NL 5、测字 CZ 8、六爻 HZ 1），全 A/A-low、全 low（低污染子集＝全集）；粹言 9 例课式仅干支级；HZ-001 的 A 级注记见 SEALED.md。验收结论只对本集构成所及口径发言。
- 执行：盲测 3 批混编（batches.json，stride 混编、来源构成对席位不言明），冻结盲测提示（轮次 R34-acceptance），输入只给 holdout12-inputs/；评审我方/大师双包各独立双评审＋|Δtotal|≥3 仲裁；达标三判据照 R34 PREREG §3。
