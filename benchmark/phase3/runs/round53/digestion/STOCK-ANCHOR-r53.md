# STOCK-ANCHOR-r53 · 存量库存 24 例主导锚点在场标记（R53 数据席·存量锚点标记专席）

- 任务口径：PREREG-r53 §2(i) 第 2 条与 §5①；锚点分类承 DIAG-H19-fresh-r52 §0.5（并 PREREG §2(i) 第 1 条分类表），在场读法承 DIAG §0.5–0.7。
- 范围：现库存 24 例（非梦占 18＋梦占 6，承 SUPPLY-ACCOUNTING-r52 §二）。只标记、不改任何既有文件、不作断、不评分；未打开任何 judging／final-scores／金标文件。24 例卡件全部在历轮 `digestion/cards-mining-*/inputs/` 侧按确切文件名定位，无一例须据 holdout 组集工作件。
- 锚点类别写定（承 §0.5）：梦占＝梦象符号；易占／筮＝卦象；六壬＝课式；遁甲＝局式／值符值使与日期干支；择日＝所择日辰干支；禄命＝四柱／推命盘面；相术＝相貌部位（相墓为其墓相对应面＝墓之方位山势／形局；听声占＝声象质地）；方技＝谶语原文／占式；扶乩＝乩判原文（无乩判入卡设计者以所请刺激文本为组成部分）。`shushu`（数术）于 §0.5 与 PREREG 分类表均未单列，本件按其推算所据写定为「推算盘面／数式（类禄命盘面）」，仅及本件标记口径。
- 状态读法（承 §0.5）：锚点本体已载入输入卡→**在场**；锚点组成部分已在卡内出现而本体／决定性属性未给→**部分在场**（须注明所缺成分及是否决定性属性）；锚点本体或其定位要件未给→**不在场**。承 §0.7：部分在场而所缺为决定性属性者按不在场同格——状态栏照实记「部分在场」，决定性判定栏标注「按不在场同格」，组集选择上与不在场同等排除（PREREG §2(i) 第 2 条）。

## 逐例标记表

| id | 来源（卡面 provenance） | 体系 | 锚点类别 | 状态 | 所缺成分及决定性判定 | 卡件路径 | 判定依据（据卡原文一句） |
|---|---|---|---|---|---|---|---|
| YJ2-008 | 《夷坚志》·甲志卷四·邵南神术 | yizhan | 卦象 | 不在场 | 卦名／卦象／爻象全缺；本体即决定性属性，全缺即不在场（卡中「入城不出口」为筮得断语性表述、非卦象本体，不构成组成部分在场） | benchmark/phase3/runs/round49/digestion/cards-mining-yijian-r49/YJ2-008-input.json | context 仅记「邵南自筮得入城不出口」「通夕细推自断死期」，全卡未载任何卦名或爻象 |
| YJ2-011 | 《夷坚志》·丙志·杨抽马 | fangji | 谶语原文／占式 | 不在场 | 谶语原文与占式全缺；本体即决定性属性，全缺即不在场 | benchmark/phase3/runs/round49/digestion/cards-mining-yijian-r49/YJ2-011-input.json | setting 自记「断法原文未名（望诊式直断＋符治）」，context 仅记女「暴得疾，更数医不効」与受杖后以符治之之约，无谶语、无占式 |
| YJ2-012 | 《夷坚志》·丙志·杨抽马 | fangji | 谶语原文／占式（占式＝观马物象） | 在场 | 无 | benchmark/phase3/runs/round49/digestion/cards-mining-yijian-r49/YJ2-012-input.json | context 逐字载占象本体及其决定性形色属性：「新得一马，黑体而白鼻」，杨望才即据此马象「索马并警告」 |
| YJ2-013 | 《夷坚志》·甲志卷十七·倪辉方技 | shushu | 推算盘面／数式（类禄命盘面） | 不在场 | 盘面／数式及其所据生年干支全缺；本体即决定性属性，全缺即不在场（「入恶限」为推算结论性表述、非盘面本体） | benchmark/phase3/runs/round49/digestion/cards-mining-yijian-r49/YJ2-013-input.json | context 仅记「倪辉自推明年运限」，setting 仅称「数术自推……本段称入恶限」，全卡未载任何盘面、数式或生年干支 |
| CZ2-004 | 《春渚紀聞》卷二·張鬼靈相墓術 | xiangshu | 相貌部位之墓相对应面＝墓之方位山势／形局 | 不在场 | 此墓方位、山势、形局全缺，连墓址亦未载；本体即决定性属性，全缺即不在场（壁間一圖仅为指涉、图中内容未转录入卡，不构成组成部分在场） | benchmark/phase3/runs/round51/digestion/cards-mining-chunzhu-r51/inputs/CZ2-004.json | context 仅记周君「指壁間一圖問之」及鬼靈「方位山勢不差……亦可言其粗」之通则语，图中方位山势无一字载于卡内 |
| CZ2-005 | 《春渚紀聞》卷二·張鬼靈相墓術 | xiangshu | 相貌部位之墓相对应面＝墓之方位山势／形局 | 部分在场 | 组成部分在场：墓址定位（富春白昇嶺）已载；所缺＝墓形山势／方位／形局描述，为决定性属性（相墓之断全系于形局）→按不在场同格 | benchmark/phase3/runs/round51/digestion/cards-mining-chunzhu-r51/inputs/CZ2-005.json | context 仅记「其先墓在富春白昇嶺」「延張鬼靈至墓下，視之」，墓之山势方位形局无一字描述 |
| YJ4-001 | 《夷坚志》·丙志卷十七·王铁面 | xiangshu | 相貌部位 | 不在场 | 受相者相貌部位及其特征全缺；本体即决定性属性，全缺即不在场 | benchmark/phase3/runs/round51/digestion/cards-mining-yijian-r51/YJ4-001-input.json | context 仅记周元特「邀王廷至局中相见」及同席者姓名官职，全卡无一周元特相貌部位或特征 |
| YJ4-002 | 《夷坚志》·丙志卷十七·王铁面 | xiangshu | 相貌部位 | 不在场 | 受相者相貌部位及其特征全缺；本体即决定性属性，全缺即不在场 | benchmark/phase3/runs/round51/digestion/cards-mining-yijian-r51/YJ4-002-input.json | context 仅记「莫子蒙适在坐，请王廷相」，全卡无一莫子蒙相貌部位或特征 |
| YJ4-003 | 《夷坚志》·丙志卷十七·王铁面 | xiangshu | 相貌部位 | 不在场 | 受相者相貌部位及其特征全缺；本体即决定性属性，全缺即不在场（卡中「入蜀十年持使者节、还朝未半年」为履历、非相貌成分） | benchmark/phase3/runs/round51/digestion/cards-mining-yijian-r51/YJ4-003-input.json | context 仅记何希深「适在坐，请王廷相」及其仕履，全卡无一何希深相貌部位或特征 |
| YJ4-004 | 《夷坚志》·丙志卷十七·王铁面 | xiangshu | 相貌部位 | 不在场 | 受相者相貌部位及其特征全缺；本体即决定性属性，全缺即不在场 | benchmark/phase3/runs/round51/digestion/cards-mining-yijian-r51/YJ4-004-input.json | context 仅记「徐吉卿宫观在衢，王廷见之而相」，全卡无一徐吉卿相貌部位或特征 |
| YJ4-005 | 《夷坚志》·丙志卷十七·王铁面 | xiangshu | 相貌部位 | 不在场 | 受相者相貌部位及其特征全缺；本体即决定性属性，全缺即不在场 | benchmark/phase3/runs/round51/digestion/cards-mining-yijian-r51/YJ4-005-input.json | context 仅记王廷「见通判毛钦望而相」，全卡无一毛钦望相貌部位或特征 |
| YJ4-006 | 《夷坚志》·丙志卷十七·王铁面 | xiangshu | 相貌部位 | 不在场 | 受相者相貌部位及其特征全缺；本体即决定性属性，全缺即不在场（「方入院」为行止、非相貌成分） | benchmark/phase3/runs/round51/digestion/cards-mining-yijian-r51/YJ4-006-input.json | context 仅记「金山寺主僧方入院，王廷见之而相」，全卡无一主僧相貌部位或特征 |
| YJ4-007 | 《夷坚志》·丙志卷十七·王铁面 | xiangshu | 相貌部位 | 不在场 | 受相者相貌部位及其特征全缺；本体即决定性属性，全缺即不在场 | benchmark/phase3/runs/round51/digestion/cards-mining-yijian-r51/YJ4-007-input.json | context 仅记王浚明「请相，妻宋氏窥于屏间闻之」，全卡无一伉俪相貌部位或特征 |
| YJ4-008 | 《夷坚志》·丙志卷五·叶议秀才 | xiangshu | 相貌部位（手纹） | 部分在场 | 组成部分在场：部位定位「手纹」已载（柴生相手纹、视手纹而相）；所缺＝手纹纹路形态（线条走向／深浅等纹理特征），为决定性属性（手相之断全系于纹理）→按不在场同格 | benchmark/phase3/runs/round51/digestion/cards-mining-yijian-r51/YJ4-008-input.json | subject／context 仅记柴生「能相手纹」「视叶议手纹而相」，叶议手纹的具体纹路无一字描述 |
| YJ4-009 | 《夷坚志》·丁志卷六·和州毛人 | xiangshu | 相貌部位 | 不在场 | 受相者相貌部位及其特征全缺；本体即决定性属性，全缺即不在场（卡中「遍体长黑毛」为相者毛人兄弟自身特征、非受相者锚点成分） | benchmark/phase3/runs/round51/digestion/cards-mining-yijian-r51/YJ4-009-input.json | context 仅记黄达如「邀毛人兄弟问相，大毛人相之」，全卡无一黄达如相貌部位或特征 |
| YJ4-010 | 《夷坚志》·丁志卷六·和州毛人 | xiangshu | 相貌部位 | 不在场 | 受相者相貌部位及其特征全缺；本体即决定性属性，全缺即不在场（「以钱数报寿」为报断方式、非相貌成分） | benchmark/phase3/runs/round51/digestion/cards-mining-yijian-r51/YJ4-010-input.json | context 仅记「呼子女出见，逐一问寿，毛人以钱数报寿」，全卡无一黄氏子女相貌部位或特征 |
| YJ4-011 | 《夷坚志》·丁志卷六·叶德孚 | ming | 四柱／推命盘面 | 不在场 | 四柱（出生年月日时干支）与推命盘面全缺；本体即决定性属性，全缺即不在场（卡中「七月二日」为谒韩慥问命之谒见日、非生辰，不构成四柱成分） | benchmark/phase3/runs/round51/digestion/cards-mining-yijian-r51/YJ4-011-input.json | context 仅记叶德孚得将仕郎、参选与「以七月二日谒韩慥问命」，全卡未载任何出生干支或盘面 |
| YW5-001 | 《阅微草堂笔记》·卷十二·槐西杂志二(5) | liuren | 课式 | 部分在场 | 组成部分在场：占时粗定位（当日晨起一课）已载；所缺＝日时干支、月将、四课、三传、神将等课式本体，为决定性属性（六壬主断全系于课式）→按不在场同格 | benchmark/phase3/runs/round52/digestion/cards-mining-yuewei-r52/YW5-001-input.json | context／setting 仅记李鹭汀「善六壬，惟晨起自占一课」「以当日晨课所占告其妾」，全卡未载任何干支与课式 |
| YJ-001 | 《夷坚志》·甲志卷四·胡克己梦 | mengzhan | 梦象符号 | 在场 | 无 | benchmark/phase3/runs/round47/digestion/cards-mining-yijian/YJ-001-input.json | context.question 逐字载梦象全叙：「梦棘闱晨启、独先入坐堂上」 |
| YJ-004 | 《夷坚志》·乙志卷四（与王龟龄梦同条） | mengzhan | 梦象符号 | 在场 | 无 | benchmark/phase3/runs/round47/digestion/cards-mining-yijian/YJ-004-input.json | context.question 逐字载梦象及榜字：「梦解榜揭于楼上、榜曰『陈七』」 |
| YJ-006 | 《夷坚志》·丁志卷一（许亢父子事） | mengzhan | 梦象符号 | 在场 | 无 | benchmark/phase3/runs/round47/digestion/cards-mining-yijian/YJ-006-input.json | context.question 逐字载梦象全叙：「吾梦父子持伞行雨中，已而大风起，吹三伞皆半裂飞去」 |
| CZ2-001 | 《春渚紀聞》卷二·吴觀成二夢 | mengzhan | 梦象符号 | 在场 | 无 | benchmark/phase3/runs/round51/digestion/cards-mining-chunzhu-r51/inputs/CZ2-001.json | context 逐字载梦象及梦中题字：「夢一黃衣人云：『上司有牒。』……紙背有題云：『富陽知縣第一將。』」 |
| CZ2-002 | 《春渚紀聞》卷二·銀盤貯首夢 | mengzhan | 梦象符号 | 在场 | 无 | benchmark/phase3/runs/round51/digestion/cards-mining-chunzhu-r51/inputs/CZ2-002.json | context 逐字载梦象全叙：「夢身乘大舟，滿舟皆人首也，內有銀盤貯數首者……內一首乃鄉人錢塘令朱子美之首也」 |
| CZ2-003 | 《春渚紀聞》卷二·金甲撞鐘夢 | mengzhan | 梦象符号 | 在场 | 无 | benchmark/phase3/runs/round51/digestion/cards-mining-chunzhu-r51/inputs/CZ2-003.json | context 逐字载梦象及梦中告语原文：「夢高樓中懸大金鐘，有金甲人立鐘傍，視國華擊鐘而言曰：『二十七甲復一擊，云係第七科。』」 |

## 汇总

三档计数（全库存 24 例）：

| 状态 | 计数 | 例 |
|---|---|---|
| 在场 | 7 | YJ2-012、YJ-001、YJ-004、YJ-006、CZ2-001、CZ2-002、CZ2-003 |
| 部分在场 | 3 | CZ2-005、YJ4-008、YW5-001（三例所缺均为决定性属性，全部按不在场同格） |
| 不在场 | 14 | YJ2-008、YJ2-011、YJ2-013、CZ2-004、YJ4-001、YJ4-002、YJ4-003、YJ4-004、YJ4-005、YJ4-006、YJ4-007、YJ4-009、YJ4-010、YJ4-011 |

分段附记（只作构成登记）：梦占 6 例全部在场；非梦占 18 例中在场 1（YJ2-012）、部分在场 3（均为决定性缺失）、不在场 14。

## holdout20 可选集（PREREG §2(i) 选择口径：在场＋部分在场非决定性缺失）

部分在场 3 例所缺均为决定性属性，无一例入可选集；可选集即在场 7 例：

- YJ2-012（fangji，《夷坚志》·丙志·杨抽马）
- YJ-001（mengzhan，《夷坚志》·甲志卷四·胡克己梦）
- YJ-004（mengzhan，《夷坚志》·乙志卷四）
- YJ-006（mengzhan，《夷坚志》·丁志卷一）
- CZ2-001（mengzhan，《春渚紀聞》卷二·吴觀成二夢）
- CZ2-002（mengzhan，《春渚紀聞》卷二·銀盤貯首夢）
- CZ2-003（mengzhan，《春渚紀聞》卷二·金甲撞鐘夢）

排除登记（随本件公开备查）：不在场 14 例与部分在场决定性缺失 3 例（CZ2-005、YJ4-008、YW5-001）依 PREREG §2(i) 第 2 条不得选入 holdout20，被排除例仍留库存作他用；本标记不追溯改判、不撤销任何入账、不动任何已封存／已用集。

— 完 —
