# ADDENDUM-r90 — R90 主持增补件

日期：2026-11-01（Asia/Shanghai）。与 REPORT.md 配套；本件各项为对 R91 的执行口径与登记，不改 R90 PREREG 已写死事项。

## 一、R89 预适配验收工具缺陷登记（R90 开轮查获）

- 对象：runs/round89/build_acceptance_packets_h32_r89.py 与 analyze_acceptance_h32_r89.py（R89 为 holdout32 预适配的验收工具）。
- 缺陷：builder 的 CASE_IDS 为 holdout31 集 id（DA-047 段与 GSZ-107–110）、GOLD_SHA256 为旧值 4b431214…、docstring 误称 holdout30；analyze 的分段断言误写 WHY＝10／GSZ＝4（h32 实为 WHY 14／GSZ 0）。
- 影响：两件从未运行（R89 验收目录为空），且 builder 的金标 SHA 断言会在运行时拦截——零产物受影响。R90 验收工具已按 data/holdout32-seal-log.md 在 runs/round90/acceptance/ 重建（CASE_IDS 真值 28、GOLD_SHA256＝f5a8ae01…、SEED＝20261108、断言 WHY＝14／GSZ＝0），运行断言全过。
- 判例增补：**跨轮预适配工具在启用轮必须以当轮封存日志逐值复核（id 集、哈希、种子、分段断言四项），不得以「已预适配」为由免检**。

## 二、种子链注记

- 链：R89 平台 anon-seed 实测 20261105；R89 曾为验收预留 20261106——未启用、无落盘件，照 PREREG-r89 ADDENDUM §五在链上计过；R90 平台 20261107、R90 验收 20261108。后续轮次沿链递增，不得回用 20261106。

## 三、评审量表冻结口径订正（请 R91 落字执行）

- 事实：Phase 3 两条评审线（平台 axis2 与验收 axis2）的 operative 量表同为 runs/round1/prompts/judge-axis2.md（direction／claims／timing 各 0–2、total 为和、pass≥4），自 Round 1 冻结、历轮实盘与全部基线/线值均在此量表。calib-r17 整体 0–10 分 JUDGE 文本为早期口径，R90 主持误以其派单致两批评审作废重派（REPORT §六.1）。
- R91 起 PREREG 冻结提示节须**并列登记三份文本及适用线**：BLIND（盲测两线）、judge-axis2（平台与验收两条评审线）、calib-r17 整体分 JUDGE（注明历史适用范围与「不得用于 Phase 3 平台/验收派单」）。派单前回盘通读所派线的量表定本全文（R84 判例扩至量表件）。

## 四、§5 裁定转 R91 执行口径

- 紫微供给工序自 R91 起为正式工序：首批 #1 天纪定点复核＋#2 许铨仁《钦天四化》定点转录（书 p.26–27）当轮启动并落进度登记；工序推进与 eligible 实测计数逐轮入当轮数据增补件。
- h34 组集判据不变：紫微面实测 eligible ≥9 才组集。holdout34 若因第十三节判读归属与本判据联动顺延，顺延只登记、不改判据。
- （丙）限度复审维持条件后备：（甲）工序毕且 ZW eligible 仍不足时，另行立项讨论，本件不预决。

## 五、执行面裁记两件（承 REPORT §六.5）

1. 验收盲测席引用已存档第十二节纪律核坐标一事：DIAG-H32 §3 实测字样痕迹 5/28、坐标改动可核记录 0/5——裁记为**执行面注记**：验收效力不因此受影响；但 R91 起盲测派单须明文「存档节条文不作执行依据、快照内注记以现行/存档标记为准」，防再发。
2. 平台评审 X1（axis2）/tmp 转储自报：已删除并自查无残留，登记裁记在案；往后各轮派单禁 /tmp 条维持逐字。

## 六、并集与集状态（R90 收束定版）

- 已用并集 **1304**（口径：dev 池＋历轮已开封验收集＋已封存集）。holdout32 已开封验收毕（未达标）转已用；holdout33 封存待开封（最早 R91 全立轮）；holdout34 未组集（判据见 §四）。
- annotations 承接基数更新为 **362 件**（case-annotations-r90.json）；待核四件（BZ-029、BZ-040、LY-537、YM-070）维持；CZ-QX 维持 16；W 监测至第五十三轮恒不可判定（六壬章冻结）。
