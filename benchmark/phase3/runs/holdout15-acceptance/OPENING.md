# holdout15 开封记录（2026-10-30）

- 开封依据：R38 平台判据三项全立（runs/round38/analyze_r38.py 实测：(a) 全集配对差 −1.206 ≥ −1.371；(b) 护栏全过——八字全集 −0.147 ≥ −0.449、natal +0.731 ≥ +0.290、horary −0.720 ≥ −0.760、六壬 dev8 −2.347 ≥ −2.600；(c) 六爻 dev8 单轮 −1.842 ≥ −1.93、熔断未触发），按 runs/round38/PREREG.md §3 开封 holdout15（封存于同日，见 holdout15/SEALED.md）。
- 金标验核：开封前 sha256sum holdout15/test_gold.jsonl ＝ dfa4a9b87a9165e9dacbeb66450395f83b529d1805240b3f8190be365a81a15a，与 SEALED.md 及 data/holdout15-seal-log.md 封存值逐字一致（2026-10-30 主持实测）。
- 送验 artifact：runs/round38/kb-snapshot（R38 方法冻结 cf92136e，含 BZ-FY；EVIDENCE-kb-snapshot.sha256 在案）。
- 构成与限度（SEALED.md 照引）：40 例——测字 20（《字触》ZC）、六壬 20（辨疑 BYZ 12／预测学 YXS 8）；等级全 A-low；污染全 low（无例外，主口径＝全集 40）；单体系/单源最大均 50%（恰上限）；六爻、八字新鲜 A-low 为 0、本集无此二体系，验收结论只对测字＋六壬构成所及口径发言；预测学 8 例中公司/事业类 4 例为最集中题材块；六壬课式为全式/图式直载（线性转录不还原格线对位）；YXS-015 已于封存前因串例误植撤销、不在本集。
- 执行：盲测 3 批混编（batches.json，按源 stride 混编、来源构成对席位不言明），冻结盲测提示（轮次 R38-acceptance），输入只给 holdout15-inputs/，方法用 runs/round38/kb-snapshot；评审我方/大师双包各独立双评审＋|Δtotal|≥3 仲裁；达标三判据照 R38 PREREG §3 既例：(i) 我方均分＞大师均分；(ii) 低污染配对胜多于负；(iii) 低污染配对差＞0（h14 体例并计 diff/SE≥1）。本集全 low，低污染口径即全集 40。
