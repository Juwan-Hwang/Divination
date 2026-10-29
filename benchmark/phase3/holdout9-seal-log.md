# holdout9 封存日志

- 2026-10-29T21:55:20.538918+08:00 封存：28 例（expansion7 全新 A 级、全 low 污染：六壬 12＋易隐 8＋卜筮全书 8），金标 SHA-256 be970fda5c4774bc11b45f855656efa2c5c1e9c8af2cb454804512413e8e61dc，状态未开封。选择规则见 SEALED.md 与 build_dev8.py。
- 2026-10-30T01:13+08:00 开封：R27 平台三判据全立后按预注册开封验收（holdout9-acceptance/PREREG.md）；开封前实测金标 SHA-256 be970fda5c4774bc11b45f855656efa2c5c1e9c8af2cb454804512413e8e61dc 与封存值逐字一致。送验方法为 R27 冻结快照（runs/round27/kb-snapshot）。
- 2026-10-30T01:24+08:00 验收完成：未达标（三判据全不立，全集配对差 −0.571、W/T/L 10/3/15，n=28），holdout9 标「已用」，见 holdout9-acceptance/REPORT.md。六壬终判 −1.417（n=12 新鲜例）。
