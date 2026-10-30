# holdout14 开封记录（2026-10-30）

- 开封依据：R36 平台判据三项全立（runs/round36/analyze_r36.py 实测：(a) 全集 −1.183 ≥ −1.371；(b) 护栏全过——八字 −0.267 ≥ −0.449、natal +0.577 ≥ +0.290、horary −0.210 ≥ −0.760、六壬 dev8 −2.083 ≥ −2.593；(c) 与 R35 合读合并 −1.803 ≥ −1.93、两轮单轮 −1.758／−1.849 均 ≥ −2.255 熔断未触发），按 runs/round36/PREREG.md §3 开封。
- 金标验核：开封前 sha256sum holdout14/test_gold.jsonl ＝ 609732c12630e0b7668dd62bb722625f80e94bf6aa2c94b995a5597c29c529b8，与 SEALED.md 及 data/holdout14-seal-log.md 封存值逐字一致（2026-10-30 主持实测）。
- 送验 artifact：runs/round36/kb-snapshot（方法冻结 459b13f3；EVIDENCE-kb-snapshot.sha256 在案；inputs-dev11 与六爻章与 R35 逐字一致在案）。
- 构成与限度（SEALED.md 照引）：40 例——六壬 16（断案 DA 8／辨疑 BY 5／粹言 CY 3）＝40.0% 恰上限、六爻 9（卜筮全书备选建档 BQ-026…034）、测字 13、八字例外 2（PU-003/008，仅分级轴改判 A-low、污染仍 high，主持裁定例外准入）。等级 A 11／A-low 29；污染 low 38／high 2；单源最大 CZ 32.5%；粹言干支级课式 3 例（占 7.5%）。判语尾句 8 例已于封存时剥离至 extractor_verdict_tail 并逐例登记（BUILD-LOG §十），评审结局文本不含判语尾句。验收结论只对本集构成所及口径发言。
- 分层报告口径（预注册写死）：**low 38 例为主口径**（达标三判据以主口径判读并与全集 40 并列）；PU-003/008 两例单独列报，不以其成色稀释或抬升主口径结论。
- 执行：盲测 3 批混编（batches.json，按源 stride 混编、来源构成对席位不言明），冻结盲测提示（轮次 R36-acceptance），输入只给 holdout14-inputs/，方法用 runs/round36/kb-snapshot；评审我方/大师双包各独立双评审＋|Δtotal|≥3 仲裁；达标三判据照 R36 PREREG §3：(i) 我方均分＞大师均分；(ii) 配对胜多于负；(iii) 配对差＞0 且差/SE≥1。
