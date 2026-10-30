# holdout16 开封记录（R40 主持）

- 开封依据：R40 预注册 §7「平台判读全立且已封存才开封」——平台三项全立定稿于提交 a1263114（(a) −1.193 ≥ −1.371；(b) 四线全立；(c) −1.763 ≥ −1.93、熔断未触；两归因护栏未触发）。
- 封存凭据：标签 phase3-holdout16-sealed（提交 dbabc6ac）；封存时金标 SHA-256 = 2040c63e3d3ba6481a84507880eba27a2aae6b7e8b8f78c1327a84c4c35f3e10。
- 开封复验（2026-10-30，主持 sha256sum 直读）：holdout16/test_gold.jsonl SHA-256 = 2040c63e3d3ba6481a84507880eba27a2aae6b7e8b8f78c1327a84c4c35f3e10，与封存值一致，金标未动。
- 构成：40 例 = 测字 ZC 20 + 六壬 20（辨疑 BYZ 10 + 预测学 YXS 3 + 断案 DA 7），口径见 runs/round40/PREREG.md §3。
- 验收体例：三判据照既例（(i) 我方均分 > 大师；(ii) 配对胜多于负；(iii) 配对差 > 0 且 diff/SE ≥ 1）；CZ-QX 护栏同轮结算（PREREG §3：测字段配对差 < −1.963 判证伪回滚；≥ −1.613 只记未见恶化）。
- 盲测方法：runs/round40/kb-snapshot 冻结版（与平台轮同一冻结快照）；提示逐字套用 calib-r17 BLIND-PROMPT 模板（仅替换轮次与路径键）。
