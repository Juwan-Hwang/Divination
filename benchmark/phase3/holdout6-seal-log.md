# holdout6 封存日誌

## 2026-10-29T18:34:19+08:00 封存（數據角，expansion4）
- 新例總數：29（《增刪卜易》卷一 25 例＋《卜筮正宗》續收 4 例）
- 合格池（A∩low∩雙完整）：23 例 → holdout6 23 例（不足 25，全取，不放寬標準）
- dev-add：6 例（答案存 expansion4/dev-add-answers.jsonl）
- 排序鍵：sha256("phase3-round4-20261029:<id>") 十六進制升序
- 金標：benchmark/phase3/holdout6/test_gold.jsonl
- 金標 SHA-256：f0efd8a947e00714cfea169ea78d7600dba9bb7ad0dcd2beb2d35f9b1ad0417a
- 狀態：未開封

## 2026-10-29 开封（主持角，Phase 3 主持链）
- 开封前金标 SHA-256 实测与封存值逐字一致：f0efd8a947e00714cfea169ea78d7600dba9bb7ad0dcd2beb2d35f9b1ad0417a。
- 开封事由：dev6 平台已成立（R19/R20 两点，见 runs/round20/REPORT.md），按 R20 预注册执行一次性验收。
- 方法＝R19 版（现行 method 逐字冻结）；23 例全 low 污染、双完整。
- 设计（同 holdout5）：混编匿名包 H6- 前缀（我方断语 23＋大师原断 23、来源匿名、顺序随机种子 20261029），冻结量表双评审＋分歧仲裁，主持角解盲配对。
- 达标三判据（须同时成立）：(i) 全集我方均分＞大师；(ii) 低污染配对胜多于负；(iii) 低污染配对差为正。本集全 low，(ii)(iii) 即全集配对口径。
- 状态：已开封（验收进行中；无论结果如何本集自此标「已用」）。
