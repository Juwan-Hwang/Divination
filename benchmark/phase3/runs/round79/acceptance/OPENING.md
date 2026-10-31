# holdout23 开封记录（R79 验收开封）

## 一、开封闸门

R79 平台三项全立（runs/round79/final-scores.json analysis_r79，主持复算）：(a) 全集配对差 −1.063（SE 0.096，n＝487）≥−1.371，余量 ＋0.308；(b) 四护栏全立——八字全集 ＋0.017（线 −0.449，余量 ＋0.466）、八字 natal ＋0.740（线 ＋0.290，余量 ＋0.450）、西占 horary −0.620（线 −0.760，余量 ＋0.140）、六壬 dev8 −1.986（SE 0.500，n＝18；线 −2.600，余量 ＋0.614）；(c) 六爻 dev8 −1.634（SE 0.119，n＝246）≥−1.93，余量 ＋0.296，熔断（<−2.255）未触。归因护栏：八字全集 ＋0.017 不 <−0.816，BZ-FY 不证伪；六壬合并段 −1.783（n＝30）不 <−2.550，无继续恶化事实。平台全立计数 25→**26**。照 R79 PREREG §2 写死闸门：当轮开封 holdout23。本轮为 R78-REV1 接入后系列第 1 点。

## 二、开封前置复验（主持执行，三项全过）

1. **金标 SHA 独立复测**：holdout23/test_gold.jsonl 主持 sha256sum 实测＝`b31afb4e59da75e89be5353d9405554cd3b449563a84b42e76b29ad4fbab60ad`，与封存定版（data/holdout23-seal-log.md §八.4）逐字全等（开轮预核亦同值，三读一致）。
2. **输入卡在盘核**：holdout23/inputs 27 张逐件在盘（DS 6／QM 10／ZCB 6／GSZ 5，与封存日志 §八.3 更新构成一致；DS-015 在、DS-019 不在）。
3. **主持第三道复扫（验封）**：主持独立脚本 runs/round79/acceptance_rescan_h23_host_r79.py（标记集逐字承 R42 PREREG §5）对 27 张输入卡全字段递归复扫——**零命中**（cards scanned 27、hits 0、非测字片段重叠 0、测字段片段重叠 0）。验封通过；本结论同步追记 data/holdout23-seal-log.md §九。

## 三、验收执行口径（照 PREREG §2 写死）

- 盲测：全新席 3 批（9/9/9）读**封存快照** runs/round78/kb-snapshot-holdout23 作断，输入卡 holdout23/inputs；冻结盲测提示逐字（runs/round79/prompts/BLIND-PROMPT-verbatim.txt，路径按验收渲染）。
- 评审：双匿名包 packet-ours／packet-master 各双视（种子 20261087），冻结评审提示逐字；分歧 |Δtotal|≥3 独立仲裁替换均值。
- 三判据（R42 PREREG §8）：(i) 我方均分＞大师均分；(ii) 低污染子集配对胜多于负；(iii) 低污染子集配对差＞0。本集全 low，三判据对全集 27 判读。
- **R78-REV1 判读不在本集执行**（快照锚定集成前、不含第七节）：本集诊断只作聚合轨迹登记（含奇门段 direction<1.75 例数附读与 E3 A 涉率附读）。判读集为 holdout24（已于本轮封存），判读随其开封验收诊断执行。
- 达标 → 打包 final-skill-v2（2.0.0）＋FINAL-REPORT-v2.md 收官回报；未达标 → 标已用、DIAG-H23 诊断、续链 R80。
