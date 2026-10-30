# holdout11 封存日志

- 2026-10-29T21:47:13.231477+00:00 封存：25 例（全新 A 级、全 low 污染：《易林补遗》YB-001…YB-022 共 22＋《卜筮正宗》ZG-001…ZG-003 共 3），金标 SHA-256 e0d43559b2f915dcbbd2b7275efbf8f5259f12fbd0985dd0f68a3749aac81d40，状态未开封。选择规则与逐例终裁见 expansion11/HOST-ADJUDICATION.md 与 holdout11/SEALED.md。
- 2026-10-30 开封：金标 SHA-256 实测 e0d43559b2f915dcbbd2b7275efbf8f5259f12fbd0985dd0f68a3749aac81d40，与封存值逐字一致；开封条件＝R32 平台三判据全立（runs/round32/REPORT.md，be46d3e）；送验 artifact＝runs/round32/kb-snapshot；验收记录见 runs/holdout11-acceptance/OPENING.md。状态：已开封、验收进行中。
- 2026-10-30 验收定稿：未达标（三判据全不过：我方 4.020 vs 大师 5.280、配对差 −1.260（SE 0.460）、W/T/L 6/7/12），见 runs/holdout11-acceptance/REPORT.md。状态：已开封、已用。
