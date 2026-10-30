# holdout11 开封记录（照 runs/round32/PREREG.md §4）

- 开封前验金标：`sha256sum holdout11/test_gold.jsonl` ＝ `e0d43559b2f915dcbbd2b7275efbf8f5259f12fbd0985dd0f68a3749aac81d40`，与封存值（data/holdout11-seal-log.md）逐字一致 → 开封成立，本记录同步追加于 seal-log。
- 开封条件：R32 平台三判据全立（(a) −1.009 ≥ −1.371；(b) 四护栏全过；(c) 合读 −1.748 ≥ −1.93 且熔断完好），见 runs/round32/REPORT.md（be46d3e，标签 phase3-round32）。
- 送验 artifact：runs/round32/kb-snapshot（SHA 清单 runs/round32/EVIDENCE.sha256，开封前已验冻结）。
- 构成：25 例单一六爻、全 A-low；验收结论只对六爻/全池口径发言；低污染子集＝全集。
- 盲测：2 批混编（种子 20261032，batches.json；席位不知来源构成），只给 inputs（YB 取 expansion10 两批 inputs、ZG 取 expansion11/bushi-zhengzong/inputs），方法用送验快照，冻结盲测提示逐字套用＋PREREG §6 派单卫生（trigger 条款原文＋主持注记随单）。
- 评审：我方包与大师基线包各独立双评审＋|Δtotal|≥3 仲裁（冻结评审提示逐字）；大师基线包的 prediction_text 由金标 master_predictions 的 statement_excerpt＋key_assertions＋timing_claim 原文构成，outcome 取金标 outcome.description。
- 达标三判据（§4）：(i) 全集我方均分＞大师均分；(ii) 配对胜多于负；(iii) 配对差＞0 且差/SE≥1。三项全过 → 打包 final-skill-v2（2.0.0）＋FINAL-REPORT-v2 收官；未达标 → 本集标已用、转诊断、继续循环。
