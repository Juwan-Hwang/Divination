# holdout22 开封记录（R77 验收开封）

## 一、开封闸门

R77 平台三项全立（runs/round77/final-scores.json analysis_r77，主持复算）：(a) 全集配对差 −1.150（SE 0.107，n＝487）≥−1.371，余量 ＋0.221；(b) 四护栏全立——八字全集 ＋0.138（线 −0.449，余量 ＋0.587）、八字 natal ＋1.202（线 ＋0.290，余量 ＋0.912）、西占 horary −0.420（线 −0.760，余量 ＋0.340）、六壬 dev8 −2.514（SE 0.574，n＝18；线 −2.600，余量 ＋0.086）；(c) 六爻 dev8 −1.869（SE 0.132，n＝246）≥−1.93，余量 ＋0.061，熔断（<−2.255）未触。归因护栏：八字全集 ＋0.138 不 <−0.816，BZ-FY 不证伪；六壬合并段 −2.000（n＝30）不 <−2.550，无继续恶化事实。平台全立计数 24→**25**。照 R77 PREREG §2 写死闸门：当轮开封 holdout22。

## 二、开封前置复验（主持执行，三项全过）

1. **金标 SHA 独立复测**：holdout22/test_gold.jsonl 实测 SHA-256＝`e10fc3f6e3bbef6514016e1bdb9a8aacb7456e44e80f0b564c5593ab7e3489cd`，与封存定版（data/holdout22-seal-log.md §九.3）逐字全等。
2. **输入卡在盘核**：holdout22/inputs 27 张逐件在盘（DS 9／QM 10／ZCB 4／GSZ 4，与封存构成一致）。
3. **主持第三道复扫（验封）**：以独立脚本 runs/round77/acceptance/rescan_inputs_h22_host_r77.py（标记集逐字承 R42 PREREG §5：逐字片段 L1 12 词＋内容级 L2 8 词＋禁用键名 12 词，与封存第二道同集）对 27 张输入卡全字段递归复扫——**零命中**（cards scanned 27、cards with hits 0）。验封通过；本结论同步 append 追记入 data/holdout22-seal-log.md（补 §四第三道留位）。

## 三、验收执行口径（照 PREREG §2 写死）

- 盲测：全新席 3 批（9/9/9）读**封存快照** runs/round76/kb-snapshot-holdout22（不读平台快照），输入卡 holdout22/inputs；冻结盲测提示逐字（runs/round77/prompts/BLIND-PROMPT-verbatim.txt，路径按验收渲染）。
- 评审：双匿名包 packet-ours／packet-master 各双视（种子 20261084），冻结评审提示逐字；分歧 |Δtotal|≥3 独立仲裁替换均值。
- 三判据（R42 PREREG §8）：(i) 我方均分＞大师均分；(ii) 低污染子集配对胜多于负；(iii) 低污染子集配对差＞0。本集全 low，三判据对全集 27 判读。
- R61-REV1 判读随验收诊断执行（PREREG §2 写死计数换算：TIM ≤2／CLAIM ≤3／合计 ≤6／OMIT ≤4／总配对差 ≥−1.366；证伪 TIM/CLAIM ≥8 或总差 ≤−1.722 → 回滚）。
- 达标 → 打包 final-skill-v2（2.0.0）＋FINAL-REPORT-v2.md 收官回报；未达标 → 标已用、DIAG-H22 诊断、续链 R78。
