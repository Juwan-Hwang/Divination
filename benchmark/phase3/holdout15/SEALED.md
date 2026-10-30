# holdout15 封存说明（2026-10-30，R38 主持封存）

- 构成：40 例，全新、从未入任何 dev/holdout。体系与来源：测字 20（《字触》卷二外部为主＋卷三晰部 4＋卷四几部 1，ZC 系列）、六壬 20（《六壬辨疑》正文占验 BYZ 12、《大六壬预测学》YXS 8）。六爻、八字新鲜 A-low 本轮为 0（易林补遗 B 存账 10 例经主持裁决改判 0 例；八字已核来源全数关账），如实登记。
- 构成推导（R38 PREREG §4 写死口径＋主持裁定）：总量 40（区间 40–50 ✔）；单体系最大 50%（测字 20/40、六壬 20/40，恰在 ≤50% 上限）；单源最大《字触》20/40＝50%（恰在上限；辨疑 30%、预测学 20%）；全 low（40/40，无污染例外）；粹言干支级 0 例。建成条件「非六壬已核可封存 ≥20」由测字 A-low 37 例覆盖（入选 20、余 17 例留存量）。
- 选择规则：各源合格集内按既有顺序依次取例，无按难度/结局/预期分数挑选。测字取 zichu-cases-r38.jsonl 中 holdout_eligible 按 id 序前 20；辨疑取 seal_eligible 按 id 序前 12；预测学取 seal_eligible 按 id 序 8 例，但经补录对勘发现 YXS-015 台账 outcome 串例误植（出自紧邻例六、本例验证明言「尚待验证」），主持裁决撤销其入选资格，由下一顺位 YXS-016 递补（递补例已经补录对勘、outcome 与原书相符）。
- 资格准据：ZC 以 runs/round38/data-verify/ZICHU-EXTRACTION.md 入封四项核为准；BYZ/YXS 以 STOCK-BIANYI-YUCE.md 入封四项核为准；六壬 20 例的大师断语与课式经补录席回源补齐（liuren-enrich-r38.jsonl＋liuren-enrich-yxs016.jsonl，ENRICH-NOTES.md），成色：全课式/图式全载 20/20（chart_complete_revised=true）。
- 等级：40 例全 A-low（分级轴 A＋污染 low）。
- 主持修正登记（逐例，详见 BUILD-LOG）：BYZ-008 subject 首字台账「离」→原书「寓」；YXS-014 asked_at 台账「抽酉时」→原书「抽卯时，月将卯」；BYZ-005 outcome 人名台账「唐枭台」vs 原书「唐皋台」，金标照台账原文保留、差异登记备核。
- 六壬段 DA 实指面构成注记（PREREG §4）：入选六壬 20 例中，他人实指占问 4 例——BYZ-004（占友被掳）、BYZ-005（占观察张济山动静）、BYZ-014（占同寓熊海洲病）、YXS-011（妻卜夫投资）；余 16 例为自占、机构占或事占（题材构成逐例见 BUILD-LOG）。
- 输入卫生：建卡白名单组装（grade_note/contamination/outcome/master 类字段不入卡，脚本断言禁键扫描零命中）；判语卫生：金标 outcome 照源文，ZC grade_note 中的评审提示性文字不进金标 outcome 字段（在 grade_note 内）。
- 封存前审计（build_holdout15_r38.py 断言全过）：40 例 id 无一命中 inputs-dev11 文件名集、holdout3–14 金标 id 集、POOL-IDS；三键（对象＋占时＋占题）入选内两两 0 撞；数据角三键去重对勘（与 CZ 已用 33 例等排除集）0 撞在案（ZICHU-EXTRACTION §二、STOCK-BIANYI-YUCE 对勘节）。
- 金标：holdout15/test_gold.jsonl，SHA-256 `dfa4a9b87a9165e9dacbeb66450395f83b529d1805240b3f8190be365a81a15a`，登记于 data/holdout15-seal-log.md。输入卡在 benchmark/phase3/holdout15-inputs/（40 张）。
- 开封条件：R38 平台判据三项全立后按 PREREG §3 开封（本轮平台已全立，见 runs/round38/REPORT.md）；开封前验金标 SHA 与封存值逐字一致。
