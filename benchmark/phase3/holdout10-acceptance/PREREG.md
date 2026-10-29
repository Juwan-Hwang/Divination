# holdout10 验收预注册（2026-10-30，平台成立后开封）

- 前提：R29 平台三项全立（(a) 全集 −1.014 ≥ −1.371；(b) 护栏逐项过线：bazi −0.190、八字 +0.529、horary −0.480、六壬 dev8 −1.750；(c) 六爻 dev8 −1.642 ≥ −1.93），见 runs/round29/REPORT.md。R29 主判据（冲突裁决增补）判未定、增补已回滚活 method；本验收送验 artifact 为**产出平台证据的 R29 冻结快照**（runs/round29/kb-snapshot，含裁决增补），口径同 R27/holdout9 先例。
- 对象：holdout10 封存 29 例（expansion8＋expansion9 全新 A 级、全 low 污染：易冒六爻 YM 14、六壬指南 LR3 12、滴天髓八字 DS 3），金标封存 SHA-256 dd3f0f741c2cf5be575f7dfb189821783a8b144b3ca7cd130983d21dc32b41f1。开封前实测与封存值逐字一致（2026-10-30 实测），holdout10-seal-log.md 已追加开封笔。
- 方法：R29 冻结快照（runs/round29/kb-snapshot/SKILL.md＋references/）。盲测只读各例 inputs（expansion8/yimao/inputs、expansion8/ditian-sui/inputs、expansion9/liuren-chen{1,2}/inputs），方法自选/混用、不按来源指定主法，每例记 systems_used；盲测提示用冻结模板体例（runs/calib-r17/BLIND-PROMPT.txt，路径按本验收替换）。
- 评审：混编匿名包 58 条（我方 29＋大师原断 29，大师侧以金标 master_predictions 的 statement_excerpt 拼接为 prediction 文本；来源匿名、随机序），冻结量表（runs/calib-r17/JUDGE-PROMPT.txt 逐字）双评审＋分歧仲裁（分歧定义同各轮：|两席 claims+timing 差|≥2 或 pass 不一致），主持角持 host-key 解盲配对。
- 达标三判据（同前，且本集全 low，低污染子集＝全集 29 例）：(i) 全集我方均分＞大师；(ii) 低污染子集配对胜多于负；(iii) 低污染子集配对差为正且超噪声（差/SE≥1）。三项全立 → 达标，以 R29 冻结快照为方法源打包 final-skill-v2（version 2.0.0）＋FINAL-REPORT-v2；任一不立 → holdout10 标已用、写验收报告、转诊断续链。
- 六壬终判附记：本集六壬 12 例为新鲜例，其配对差即六壬段在全新留出集上的又一终判读数，无论总判据成败均在验收 REPORT 中单列。

*主持角，2026-10-30*
