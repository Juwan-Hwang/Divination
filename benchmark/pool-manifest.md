# 统一池清单（benchmark/pool-manifest.md）— Round 1 数据角产出

- 日期：2026-10-29。角色：数据角（只管统一汇总、去重、划分、封存与清单；不作断、不评分）。
- 依据：benchmark/PROTOCOL.md（含五角分离与论文级方法学修订）、masters-dataset/SCHEMA.md、Round 1 预注册（benchmark/iterations.md，主持角已写定，本角未改动）、知识库冻结快照（benchmark/runs/round1/kb-snapshot/MANIFEST.sha256，主持角已冻结，本角未改动）。
- 证据保全：本轮全部产出只写工作区文件，未执行任何 git 提交/回退；提交与 round1 标签由主持角在轮末统一办理。

## 一、总数对账

统一池 = 50（chinese-divination）+ 45（chinese-natal）+ 15（western）+ 10（modern-masters 占例 C）+ 12（modern-masters 公开预测 P）+ 2（种子独立例 LY-01、LY-03）= **134 例**，与主持角对账预期一致，未凑数、未增删。

| tradition 组 | 总数 | dev | test |
|---|---|---|---|
| liuyao（含种子 LY-01/LY-03、modern 六爻 LY-101–LY-105） | 43 | 30 | 13 |
| meihua | 10 | 7 | 3 |
| yijing | 4 | 3 | 1 |
| bazi（含 modern 八字 BZ-101–BZ-105） | 47 | 33 | 14 |
| ziwei | 3 | 2 | 1 |
| horary | 15 | 10 | 5 |
| modern-prediction（P 类整体一组；tradition 字段写原体系，tags 加 modern_prediction） | 12 | 8 | 4 |
| **合计** | **134** | **93** | **41** |

dev/test ≈ 69.4% / 30.6%。direction 分布（全池）：positive 77、negative 38、mixed 18、neutral 1。

## 二、去重日志

- 种子 LY-02 ≡ chinese-divination LY-001；MH-01 ≡ MH-001；MH-02 ≡ MH-002；MH-03 ≡ MH-003：重复只计一例，以分卷版为正本，种子版仅记 alias（alias 说明已并入正本记录的 notes.comment）。旧 holdout 金标 MH-03 的内容已并入 MH-003 统一记录。
- 种子 LY-01（候文书·贲静卦）、LY-03（占官升迁·困之兑）经全文检索在分卷中无同例，作为独立例保留，金标分别据 benchmark/cases/answer/LY-01.md、holdout-answer/LY-03.md 与旧统一记录（data/dev.jsonl 的 LY-01、holdout/test_gold.jsonl 的 LY-03）合并转入。
- 旧 data/dev.jsonl（4 例种子 dev）、旧 holdout/test_gold.jsonl（2 例种子 test）、旧 splits.json（6 条）已按任务整体替换为本轮全量版本，种子金标内容均已并入对应统一记录，无内容丢失。

## 三、划分（一次冻结）

- 方法：按 tradition 组分层，每组 test 配额 = int(n×0.3+0.5)；组内以随机种子 **20261029**（random.Random(20261029)，组内 id 排序后 shuffle）抽取。划分自此冻结，写入 masters-dataset/splits.json 为单一事实源，不得因成绩挪动。
- 强制指定（覆盖随机，已逐条验明）：LY-01→dev、LY-03→test、LY-001→dev、MH-001→dev、MH-002→dev、MH-003→test。
- famous 9 例（MH-001/002/003/005/006、ZY-001–004）最终 dev 6 例（MH-001、MH-002、MH-006、ZY-001、ZY-002、ZY-004）、test 3 例（MH-003、MH-005、ZY-003），未全在一边。随机初抽后 famous test 仅 2 例，做了一次同组对调：MH-005（famous）dev→test 与 MH-009 test→dev 对调（同属 meihua 组，不改变组内 test 配额）。

## 四、编码复核更正（数据整理，非评分）

主持角草拟的旧结构 direction 编码（natal 45、western 15、modern C 10、modern P 12，共 82 例）已逐条对照原文 verdict 复核。**更正 1 条**：

| uid | source | 草拟 | 改为 | 依据 |
|---|---|---|---|---|
| BZ-102 | modern C02（徐乐吾同字异序对造） | positive | **mixed** | 一例两造方向相反：徐乐吾本人「寿超花甲」为正、其亲戚「早早走人（夭折）」为负，positive 只覆盖一造；以原文 verdict 为准改为 mixed |

其余 81 条与原文一致，保留草拟编码。复核中确认的口径（非更正，备评审角知悉）：

- modern P 的 direction 按任务定义为「大师预测对对象而言的方向」，与应验 hit/miss 无关：如 BZ-304（P07）预测「5–6 月恢复正常」属对对象的乐观（正向）预测，虽事后落空仍记 positive。P09–P12 四例选举预测均以「预测所断言获胜方」为受益对象记 positive（与草拟一致）。
- western 按「所问命题被肯定/否定」编码：如 AS-004 命题「国王已攻取剑桥」被断为不实，记 negative。
- natal 中 ren-014、ren-015、wei-016 等「一生成就与一域重大缺憾并存」者记 mixed，与 ren-007、wei-019 等「成就为主、仅小疵」者记 positive 的边界，逐例对照 verdict 后维持草拟。

金标结构化处理说明：

- natal 与 modern C 的 key_assertions 取 reasoning_points；western 的 key_assertions 由数据角自 verdict 原文提炼 1–3 条具体断语（只提炼、不改写关键信息）；modern P 取 statement 中的具体主张 1–3 条。
- outcome 字符串一律转 {description, verified_by}：verified_by 据来源填「原书自载」「公开史实」「汇编转录自载」等；western AS-004 无原书应验后记，verified_by 如实标「外部史实核对（原书节录未另载应验后记）」。
- chinese-divination 的 reasoning_points 与 key_assertions 经逐例核对完全相同，统一记录中只保留 key_assertions，不丢信息。
- 命理卷与 modern 八字例无具体问事，context.question 为结构占位（「断此命造（一生格局、吉凶与运程）」/「断此命盘（格局与吉凶）」），context.setting 存原 life_context / context_at_prediction 全文。
- 为合 schema.json 类型要求，chinese-divination 记录中 subject.gender 的 null 值已去除该键（原卷未记性别者本就无此信息）。

## 五、特别标注

- **紫微 3 例（ZW-001–ZW-003）**：原笔记未载结局，outcome.description 一律如实记「原笔记未载结局」、verified_by 记「原笔记未载」，并在各例 notes.comment 注明「outcome 项只能按格局断法对齐评」。ZW-003 原笔记所载「夫已过世」为求测时已知事实、非预测应验，未计入 outcome，已在 comment 注明。
- **retrodiction**：BZ-105（modern C05，邵伟华测过去回溯例）已按任务在 notes.tags 加 `retrodiction`。LY-101（modern C06）原卷 context 自述为回溯初检例，但任务只指定 C05 加标，故未加 tag，仅在其 notes.comment 与 context 中如实保留原卷说明。
- **盲测身份脱敏（仅输入面）**：BZ-016（ren-016）、BZ-019（xu-003）为乾隆同造，原卷注记明言「盲测时只能给四柱与时代背景、不得给身份」。两例均在 dev：其盲测输入文件（及一切输入面）已隐去姓名（subject 改记「清代皇子（身份依原卷注记于盲测输入中隐去）」）、改写 context.setting、并去掉 BZ-016 出处书名中「（乾隆皇帝造）」字样；统一记录（dev 金标侧）保持全量不动。
- **近重复观察（未擅自去重，报主持角）**：BZ-021（natal wei-001）与 BZ-101（modern C01）同为韦千里断蒋介石造、出自《千里命稿》，由两卷分别收集，断语节录详略不同。主持角已确认的去重名单不含此对、且 134 总数按两例计，故本角保留两例并在此登记，是否合并请主持角裁定。另 BZ-016 与 BZ-019 为跨大师同造（任铁樵/徐乐吾），原卷已标 cross_system，属有意保留。

## 六、盲测输入自检（benchmark/runs/round1/inputs/，dev 93 例）

- 每例一份 `<uid>.json`，只含 uid、tradition、subject、context（含 attachments）、provenance.book（仅书名）。
- 自检方法与结果：① 全目录 grep 字段名 `outcome`、`direction`、`key_assertions`、`master_predictions`、`statement_excerpt`、`split`——**0 命中**；② 程序逐例比对：各 dev 例 outcome.description 前 12 字片段出现在对应盲测文件者——**0 例**；③ 抽样（每 12 例取 1）比对 key_assertions 前 10 字片段——**0 例**；④ BZ-016/BZ-019 脱敏复查：「弘历」「乾隆」在两文件中均 0 命中。
- 校验总账：全部 JSONL 逐行解析通过；dev+test 金标共 134 条经 masters-dataset/schema.json（JSON Schema draft 2020-12）全量校验 **0 错误**；人工抽查每卷至少 2 例（LY-005、ZY-002、BZ-001、BZ-042、ZW-002、AS-007、AS-013、BZ-102、LY-104、BZ-302、AS-303、LY-01、LY-03），必填字段与原文一致。

## 七、来源链（provenance chain，按分卷）

### 1. chinese-divination（50 例）
- 原始出处：《增删卜易》（野鹤老人著、李文辉增删，清初）、《卜筮正宗》（王洪绪辑，1709）、《梅花易数》（传世托名文本）、《左传》——均为公版古籍。
- 转录方式：以维基文库录入本为核对本逐例与原文核对（《增删卜易》本机抓取本存 sources/chinese/zengshan-buyi-wikisource.txt，卦盘六爻照录；维基文库本自标未排版未校对、个别字形有讹，节录照原文录入未擅改）；《卜筮正宗》经华夏大易学社（cnddy）在线全本逐段在线核对。ctext 按约定禁止抓取，未用。
- 收集/转录者：中方占卜分卷收集 agent（2026-10-29，见本卷 SOURCES.md）。
- 校验记录：分卷内 inputs/answers 同 id 50/50 配对；本轮数据角复核 direction、key_assertions、outcome 三项逐例齐全，reasoning_points 与 key_assertions 逐例相同（已合并），去除 gender:null 以合 schema。

### 2. chinese-natal（45 例）
- 原始出处：《滴天髓阐微》任铁樵批、《子平真诠评注》徐乐吾注、《三命通会》万民英自述、《千里命稿》（1935）与《呱呱集》（1963）韦千里、《天纪》倪海厦讲授。
- 转录方式：任批经「至真斋主《滴天髓新解》」博客逐篇转录核对（只取任批段落，现代新解不入集）；徐注经黄大陆本义评注转录（360doc）核对；《三命通会》自造经 GitHub 公版 PDF 镜像取得原文；韦氏两书经全文 PDF（《呱呱集》为 luckclub 本，原文层逐页核读，白话译文层不用）；紫微 3 例为《天纪》听课笔记转录（非正式出版物，可靠性已逐例标 disputed）。名人卒年/大事以通行史实互核。
- 收集/转录者：中方命理分卷收集 agent（见本卷 SOURCES.md）。
- 校验记录：分卷内 inputs/answers 同 id 45/45 配对；本轮数据角逐条对照 verdict 复核 direction（45 例 0 更正），紫微 outcome 按未载结局处置，disputed 6 例的 tags 与 dispute_note 全量保留。

### 3. western（15 例）
- 原始出处：William Lilly《Christian Astrology》（1647）Book II 卜卦例，公版。
- 转录方式：以 Internet Archive 馆藏 1647 年原版扫描 OCR（auxiliary/ djvu.txt）为底本逐例录入；1647 OCR 字形残缺处以 1852 年 Zadkiel 修订本交叉校对措辞（逐例 source 已注明）；未用 Deborah Houlding 现代重排注释本。
- 收集/转录者：西方分卷收集 agent（见本卷 SOURCES.md）。
- 校验记录：分卷内 inputs/answers 同 id 15/15 配对；本轮数据角自 verdict 提炼 key_assertions（15 例）、逐条复核 direction（0 更正），AS-004 应验来源如实标为外部史实核对。

### 4. modern-masters 占例 C（10 例）
- 原始出处：《千里命稿》全文 PDF、《子平真诠》本义（Scribd 影印）、《子平真诠评注》（360doc 转录）、邵伟华《四柱预测学》（1993，Scribd 影印）、邵伟华《周易预测例题解》与王虎应《六爻预测疾病新探》（经《六爻卦例一百例》汇编转录）、王虎应《六爻预测自修宝典》（Scribd 影印）、《六爻疑惑指迷》相关转录（360doc 论坛帖）。
- 转录方式：影印本逐页读录与转录文本节录并存，逐例 provenance 保留原始指针；C06/C09 的 reasoning 内容含汇编编者发挥，已在原卷与本轮 notes 中与大师原文分清；C10 为学生转述的二手转录，已标注。
- 收集/转录者：现代大师分卷收集 agent（见本卷 masters-roster.md）。
- 校验记录：分卷内 inputs/answers 同 id 10/10 配对；本轮数据角复核 direction 并更正 1 条（C02→BZ-102，见第四节），C05 加 retrodiction 标注。

### 5. modern-masters 公开预测 P（12 例）
- 原始出处：大师公开发表文本——占星博客原文（Jessica Adams）、媒体报道（镜报、Moneycontrol、Economic Times、Mothership、UHK、Times Now、HuffPost）、百科条目转述（李居明、袁树珊、韦千里事后追述类）、PRWeb 通稿、预测者 X 账号原文等，逐例 published_in 与 published_at 在卷内已存。
- 转录方式：原文/报道节录，二手转述者逐例标 secondhand（P01、P02、P03、P04、P11、P12）；原卷 outcome_verdict（hit/partial/miss）与 outcome_source 全量保留，其中 outcome_verdict 已并入统一记录 notes.comment 备查（非金标方向字段）。
- 收集/转录者：现代大师分卷收集 agent。
- 校验记录：本轮数据角自 statement 提炼 key_assertions、按「预测对对象而言的方向」逐条复核 direction（12 例 0 更正，口径见第四节）。

### 6. benchmark 种子（独立例 2 + alias 4）
- 原始出处：《增删卜易》用神章等（本地全文 sources/chinese/zengshan-buyi-wikisource.txt）、《梅花易数》卷一。
- 转录方式：自典籍原文逐字抽取为 cases/input、answer、holdout-answer 卡片（未改写关键信息）。
- 收集/转录者：benchmark 种子维护（主会话先行工作）。
- 校验记录：本轮数据角与分卷全文检索对账：4 例重复记 alias（见第二节），LY-01、LY-03 无同例独立保留并转统一结构，排盘据 input 卡照录补入 attachments。

## 八、uid ↔ source 映射表

| uid | source_id | 分卷 | tradition | master | split |
|---|---|---|---|---|---|
| AS-001 | lilly-horary-1638-absent-son | western | horary | William Lilly | test |
| AS-002 | lilly-horary-1634-tradesman-wealth | western | horary | William Lilly | test |
| AS-003 | lilly-horary-1634-purchase-houses | western | horary | William Lilly | dev |
| AS-004 | lilly-horary-1643-cambridge-rumour | western | horary | William Lilly | dev |
| AS-005 | lilly-horary-1644-ship-preserved | western | horary | William Lilly | dev |
| AS-006 | lilly-horary-ship-lost | western | horary | William Lilly | dev |
| AS-007 | lilly-horary-1644-waller-hopton | western | horary | William Lilly | dev |
| AS-008 | lilly-horary-1643-reading | western | horary | William Lilly | dev |
| AS-009 | lilly-horary-lost-dog | western | horary | William Lilly | dev |
| AS-010 | lilly-horary-fugitive-servant | western | horary | William Lilly | test |
| AS-011 | lilly-horary-marriage-revival | western | horary | William Lilly | test |
| AS-012 | lilly-horary-parsonage | western | horary | William Lilly | dev |
| AS-013 | lilly-horary-1637-stolen-fish | western | horary | William Lilly | dev |
| AS-014 | lilly-horary-theft-youth | western | horary | William Lilly | test |
| AS-015 | lilly-horary-husband-at-sea | western | horary | William Lilly | dev |
| AS-301 | P05 | modern-masters（公开预测） | astrology | Jessica Adams | dev |
| AS-302 | P06 | modern-masters（公开预测） | astrology | Jessica Adams | dev |
| AS-303 | P08 | modern-masters（公开预测） | vedic-astrology | Kushal Kumar | test |
| AS-304 | P09 | modern-masters（公开预测） | vedic-astrology | Prathosh Gopalakrishnan | test |
| AS-305 | P10 | modern-masters（公开预测） | astrology | Jamie Partridge（Astrology King） | test |
| AS-306 | P11 | modern-masters（公开预测） | vedic-astrology | Kathir Subbiah（KT Astrologer） | dev |
| AS-307 | P12 | modern-masters（公开预测） | astrology | 美国占星师群体（HuffPost 2024选举专题受访者） | dev |
| BZ-001 | ren-001 | chinese-natal | bazi | 任铁樵 | dev |
| BZ-002 | ren-002 | chinese-natal | bazi | 任铁樵 | test |
| BZ-003 | ren-003 | chinese-natal | bazi | 任铁樵 | dev |
| BZ-004 | ren-004 | chinese-natal | bazi | 任铁樵 | test |
| BZ-005 | ren-005 | chinese-natal | bazi | 任铁樵 | test |
| BZ-006 | ren-006 | chinese-natal | bazi | 任铁樵 | dev |
| BZ-007 | ren-007 | chinese-natal | bazi | 任铁樵 | dev |
| BZ-008 | ren-008 | chinese-natal | bazi | 任铁樵 | test |
| BZ-009 | ren-009 | chinese-natal | bazi | 任铁樵 | dev |
| BZ-010 | ren-010 | chinese-natal | bazi | 任铁樵 | dev |
| BZ-011 | ren-011 | chinese-natal | bazi | 任铁樵 | dev |
| BZ-012 | ren-012 | chinese-natal | bazi | 任铁樵 | dev |
| BZ-013 | ren-013 | chinese-natal | bazi | 任铁樵 | test |
| BZ-014 | ren-014 | chinese-natal | bazi | 任铁樵 | test |
| BZ-015 | ren-015 | chinese-natal | bazi | 任铁樵 | dev |
| BZ-016 | ren-016 | chinese-natal | bazi | 任铁樵 | dev |
| BZ-017 | xu-001 | chinese-natal | bazi | 徐乐吾 | test |
| BZ-018 | xu-002 | chinese-natal | bazi | 徐乐吾 | dev |
| BZ-019 | xu-003 | chinese-natal | bazi | 徐乐吾 | dev |
| BZ-020 | sanming-001 | chinese-natal | bazi | 万民英（自造自断） | test |
| BZ-021 | wei-001 | chinese-natal | bazi | 韦千里 | dev |
| BZ-022 | wei-002 | chinese-natal | bazi | 韦千里 | dev |
| BZ-023 | wei-003 | chinese-natal | bazi | 韦千里 | dev |
| BZ-024 | wei-004 | chinese-natal | bazi | 韦千里 | dev |
| BZ-025 | wei-005 | chinese-natal | bazi | 韦千里 | test |
| BZ-026 | wei-006 | chinese-natal | bazi | 韦千里 | dev |
| BZ-027 | wei-007 | chinese-natal | bazi | 韦千里 | dev |
| BZ-028 | wei-008 | chinese-natal | bazi | 韦千里 | dev |
| BZ-029 | wei-009 | chinese-natal | bazi | 韦千里 | dev |
| BZ-030 | wei-010 | chinese-natal | bazi | 韦千里 | dev |
| BZ-031 | wei-011 | chinese-natal | bazi | 韦千里 | dev |
| BZ-032 | wei-012 | chinese-natal | bazi | 韦千里 | dev |
| BZ-033 | wei-013 | chinese-natal | bazi | 韦千里 | dev |
| BZ-034 | wei-014 | chinese-natal | bazi | 韦千里 | dev |
| BZ-035 | wei-015 | chinese-natal | bazi | 韦千里 | test |
| BZ-036 | wei-016 | chinese-natal | bazi | 韦千里 | test |
| BZ-037 | wei-017 | chinese-natal | bazi | 韦千里 | test |
| BZ-038 | wei-018 | chinese-natal | bazi | 韦千里 | dev |
| BZ-039 | wei-019 | chinese-natal | bazi | 韦千里 | dev |
| BZ-040 | wei-020 | chinese-natal | bazi | 韦千里 | dev |
| BZ-041 | wei-021 | chinese-natal | bazi | 韦千里 | test |
| BZ-042 | wei-022 | chinese-natal | bazi | 韦千里 | dev |
| BZ-101 | C01 | modern-masters（占例） | bazi | 韦千里 | test |
| BZ-102 | C02 | modern-masters（占例） | bazi | 徐乐吾 | dev |
| BZ-103 | C03 | modern-masters（占例） | bazi | 徐乐吾 | dev |
| BZ-104 | C04 | modern-masters（占例） | bazi | 邵伟华 | dev |
| BZ-105 | C05 | modern-masters（占例） | bazi | 邵伟华 | dev |
| BZ-301 | P01 | modern-masters（公开预测） | bazi | 李居明 | dev |
| BZ-302 | P03 | modern-masters（公开预测） | bazi | 袁树珊 | dev |
| BZ-303 | P04 | modern-masters（公开预测） | fengshui | 苏民峰 | dev |
| BZ-304 | P07 | modern-masters（公开预测） | fengshui | Master SiewLi（萧丽，音译） | dev |
| LR-001 | P02 | modern-masters（公开预测） | liuren | 韦千里 | test |
| LY-001 | LY-001 | chinese-divination | liuyao | 野鶴老人 | dev |
| LY-002 | LY-002 | chinese-divination | liuyao | 野鶴老人 | test |
| LY-003 | LY-003 | chinese-divination | liuyao | 野鶴老人 | dev |
| LY-004 | LY-004 | chinese-divination | liuyao | 野鶴老人 | dev |
| LY-005 | LY-005 | chinese-divination | liuyao | 野鶴老人 | dev |
| LY-006 | LY-006 | chinese-divination | liuyao | 野鶴老人 | dev |
| LY-007 | LY-007 | chinese-divination | liuyao | 野鶴老人 | dev |
| LY-008 | LY-008 | chinese-divination | liuyao | 野鶴老人 | test |
| LY-009 | LY-009 | chinese-divination | liuyao | 野鶴老人 | dev |
| LY-01 | seed:LY-01 | benchmark 种子 | liuyao | 野鹤老人（《增删卜易》） | dev |
| LY-010 | LY-010 | chinese-divination | liuyao | 野鶴老人 | dev |
| LY-011 | LY-011 | chinese-divination | liuyao | 野鶴老人 | test |
| LY-012 | LY-012 | chinese-divination | liuyao | 野鶴老人 | dev |
| LY-013 | LY-013 | chinese-divination | liuyao | 野鶴老人 | dev |
| LY-014 | LY-014 | chinese-divination | liuyao | 野鶴老人 | test |
| LY-015 | LY-015 | chinese-divination | liuyao | 野鶴老人 | dev |
| LY-016 | LY-016 | chinese-divination | liuyao | 野鶴老人 | dev |
| LY-017 | LY-017 | chinese-divination | liuyao | 野鶴老人 | test |
| LY-018 | LY-018 | chinese-divination | liuyao | 野鶴老人 | dev |
| LY-019 | LY-019 | chinese-divination | liuyao | 野鶴老人 | test |
| LY-020 | LY-020 | chinese-divination | liuyao | 野鶴老人 | dev |
| LY-021 | LY-021 | chinese-divination | liuyao | 野鶴老人 | test |
| LY-022 | LY-022 | chinese-divination | liuyao | 野鶴老人 | test |
| LY-023 | LY-023 | chinese-divination | liuyao | 野鶴老人 | dev |
| LY-024 | LY-024 | chinese-divination | liuyao | 野鶴老人 | dev |
| LY-025 | LY-025 | chinese-divination | liuyao | 野鶴老人 | test |
| LY-026 | LY-026 | chinese-divination | liuyao | 野鶴老人 | dev |
| LY-027 | LY-027 | chinese-divination | liuyao | 王洪緒（輯錄，含師授占驗） | dev |
| LY-028 | LY-028 | chinese-divination | liuyao | 王洪緒（輯錄，含師授占驗） | dev |
| LY-029 | LY-029 | chinese-divination | liuyao | 王洪緒（輯錄，含師授占驗） | dev |
| LY-03 | seed:LY-03 | benchmark 种子 | liuyao | 野鹤老人（《增删卜易》） | test |
| LY-030 | LY-030 | chinese-divination | liuyao | 王洪緒（輯錄，含師授占驗） | dev |
| LY-031 | LY-031 | chinese-divination | liuyao | 王洪緒（輯錄，含師授占驗） | dev |
| LY-032 | LY-032 | chinese-divination | liuyao | 王洪緒（輯錄，含師授占驗） | dev |
| LY-033 | LY-033 | chinese-divination | liuyao | 王洪緒（輯錄，含師授占驗） | dev |
| LY-034 | LY-034 | chinese-divination | liuyao | 王洪緒（輯錄，含師授占驗） | test |
| LY-035 | LY-035 | chinese-divination | liuyao | 王洪緒（輯錄，含師授占驗） | dev |
| LY-036 | LY-036 | chinese-divination | liuyao | 王洪緒（輯錄，含師授占驗） | dev |
| LY-101 | C06 | modern-masters（占例） | liuyao | 邵伟华 | dev |
| LY-102 | C07 | modern-masters（占例） | liuyao | 王虎应 | dev |
| LY-103 | C08 | modern-masters（占例） | liuyao | 王虎应 | test |
| LY-104 | C09 | modern-masters（占例） | liuyao | 王虎应 | dev |
| LY-105 | C10 | modern-masters（占例） | liuyao | 王虎应 | test |
| MH-001 | MH-001 | chinese-divination | meihua | 邵雍（傳世文本托名） | dev |
| MH-002 | MH-002 | chinese-divination | meihua | 邵雍（傳世文本托名） | dev |
| MH-003 | MH-003 | chinese-divination | meihua | 邵雍（傳世文本托名） | test |
| MH-004 | MH-004 | chinese-divination | meihua | 邵雍（傳世文本托名） | dev |
| MH-005 | MH-005 | chinese-divination | meihua | 邵雍（傳世文本托名） | test |
| MH-006 | MH-006 | chinese-divination | meihua | 邵雍（傳世文本托名） | dev |
| MH-007 | MH-007 | chinese-divination | meihua | 邵雍（傳世文本托名） | dev |
| MH-008 | MH-008 | chinese-divination | meihua | 邵雍（傳世文本托名） | dev |
| MH-009 | MH-009 | chinese-divination | meihua | 邵雍（傳世文本托名） | dev |
| MH-010 | MH-010 | chinese-divination | meihua | 邵雍（傳世文本托名） | test |
| ZW-001 | ziwei-001 | chinese-natal | ziwei | 倪海厦 | test |
| ZW-002 | ziwei-002 | chinese-natal | ziwei | 倪海厦 | dev |
| ZW-003 | ziwei-003 | chinese-natal | ziwei | 倪海厦 | dev |
| ZY-001 | ZY-001 | chinese-divination | yijing | 周史（周太史） | dev |
| ZY-002 | ZY-002 | chinese-divination | yijing | 辛廖（晉大夫） | dev |
| ZY-003 | ZY-003 | chinese-divination | yijing | 穆姜（自占自斷；占史同占異斷） | test |
| ZY-004 | ZY-004 | chinese-divination | yijing | 史朝（衛太史） | dev |

## Errata 2026-10-29（主持角裁定）

- **合并理由**：BZ-101（源 modern-masters C01）与 BZ-021（源 chinese-natal wei-001）同为韦千里断蒋介石造、同出《千里命稿》，被两卷重复收集；且 BZ-021 在 dev、BZ-101 在 test——同一案例分跨两侧会污染将来的留出集验收。本轮尚无任何预测与评分产生，现按数据卫生纠错合并。此前第五节「近重复观察」中待裁定的即此对，现已裁定并执行。
- **处置**：BZ-101 alias → BZ-021。已删除 masters-dataset/splits.json 中 BZ-101 条目，并删除 masters-dataset/data/test_inputs.jsonl 与 masters-dataset/holdout/test_gold.jsonl 中 BZ-101 行；dev 侧 BZ-021 记录不动。
- **总数变更**：pool 总数 134 → **133**；dev **93 不变**；test 41 → **40**。
- **两条内容差异说明**：两条为同一案例的不同节录，断语节录详略不同——modern 版（BZ-101）上下文更全（其 context 字段长度大于 BZ-021 版，provenance 页码标注口径亦不同，BZ-021 版标为「应运篇（蒋介石造）」）。合并后**金标以 dev 的 BZ-021 为准合并计分**，BZ-101 不再作为独立案例单独计分。
