# holdout14 封存日志

- 2026-10-30T05:03:11+00:00 封存：40 例（全新 A/A-low；low 污染 38 例＋污染例外 2 例 PU-003/PU-008（high，主持裁定准入、验收须分层报告）：六壬 16＝断案 DA 8＋辨疑 BY 5＋粹言 CY 3、六爻 9＝卜筮全书备选建档 BQ-026…034、测字 CZ 13（余量全取）、八字 2＝PU 例外 2），金标 SHA-256 609732c12630e0b7668dd62bb722625f80e94bf6aa2c94b995a5597c29c529b8，状态未开封。构成推导、选择规则、资格准据、例外注记、判语剥离登记与成色限度见 holdout14/SEALED.md 与 holdout14/BUILD-LOG.md；备选建档见 expansion12/bushi-quanshu-beixuan/BUILD-NOTES.md；封存前编号唯一性审计见 runs/round36/audit-ids-holdout14-report.json。

- 2026-10-30 开封：R36 平台三项全立（analyze_r36.py 实测，见 runs/holdout14-acceptance/OPENING.md），开封前 sha256sum 与封存值逐字一致（主持实测），按 runs/round36/PREREG.md §3 开封验收；送验 artifact＝runs/round36/kb-snapshot。状态：已开封、验收执行中。

- 2026-10-30 验收定稿：未达标（主口径 low 38：我方 3.276 vs 大师 4.888、配对差 −1.612（SE 0.281）、W/T/L 6/1/31，三判据全不立；全集 40 并列 −1.512），见 runs/holdout14-acceptance/REPORT.md。状态：已开封、已用尽。
