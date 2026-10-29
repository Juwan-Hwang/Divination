# Phase 3 扩充 — Lilly《Christian Astrology》Book II 新收案例分级与筛选日志

数据角（二路）交付说明。本目录只收录整理，不作断、不评分。

## 文件与 schema

- `inputs.jsonl` / `answers.jsonl`：各 15 行，id 为 **AS-201 – AS-215**，按 Book II 章节顺序排列。
- schema 与 `masters-dataset/western/` 既有条目完全一致（已逐行解析校验，并与既有首条做键集对照）：inputs = `id, system, subject{who, background, question, moment}, chart_data{ascendant?, key_positions, note}, source{book, chapter, url, version}, notes{cross_ref, …}, license_status, redistributable`；answers = `id, master_predictions[{master, system, verdict, reasoning_points[], outcome, source{book, chapter, url}}], license_status, redistributable`。`system` 字段沿既有 western 文件口径填 `horary`（与任务书 tradition=horary 同义，既有条目即用 `system` 键）；`master` 均为 William Lilly。
- 底本：1647 初版 OCR（`masters-dataset/western/auxiliary/christian-astrology-vol1-3_djvu.txt`），断语与结局均逐例回原文行段核对；1852 Zadkiel 版（`sources/western/lilly-introduction-to-astrology-1852.pdf`，含 33 幅图目录）与第二份 djvu OCR（`christian-astrology-1647-original_djvu.txt`）用于互证与系统扫描索引。
- 英文节录照 OCR 文本录入（长 s 按通行转写作 s）；明显 OCR/印刷讹误不擅改原文，统一在对应条目的 `notes.ocr_note` 标注（见 AS-203、AS-205、AS-209、AS-210）。盘面数据只录 Lilly 散文中断语明言者，原文无者不编造（如 AS-205 上升星座字形在 OCR 中已 corrupt，未断言）。

## 分级口径

- **结局可得性 A**：书内有可与断语分离的具体结局事件记录（死亡日期、返家日、婚事成、马匹归家等可独立陈述的事件）。
- **结局可得性 B**：只有作者自述式评语（"all this proved true" 类总括自证），结局不可与断语分离 —— **不收**，仅在筛选日志登记。
- **污染分层**：涉及英国内战著名事件/名人（国王、王后、Rupert、Essex、Laud 等，模型先验可直接"知道"结局）标**高**；普通市民私人问卜标**低**；拿不准从严标高。

## 逐例分级表（收录 15 例，全部 A 级）

| id | 案例 | 章节 | 结局分级 | 污染 | 书内结局事件（摘） |
|---|---|---|---|---|---|
| AS-201 | 绅士六问（长寿/方位/生涯/已往/将来/应期） | Book II 六问盘（1852 Fig. 2） | A | 高 | 1646 年 3 月尚在世；赴爱尔兰立功获胜；子女教育协议问卜后离英前已订；约 3¾ 年后屡经险阵、得王党荣职，终被议会判永不得终老英格兰 |
| AS-202 | 兄弟出门在外（生死/音信/归期） | Book II 三宫章（1852 Figs. 7–8） | A | 低 | 问卜当日约下午四时送信人到门报平安；次周二兄弟返家 |
| AS-203 | 孕妇问胎儿性别与产期 | Chap. XLII（Fig. 11） | A | 低 | 生男（"and so it proved"）；次年 7 月 11 日分娩 |
| AS-204 | 病医问病（何病/可治否/何部位） | Chap. XLV | A | 低 | 与病人面谈症状逐项吻合；次年 8 月 14 日病逝 |
| AS-205 | 病人问生死与病因（1645-07-16 盘） | Chap. XLVI | A | 低 | 病情描述"all which was true"；1645 年 7 月 28 日病逝（断"不过十至十二日"） |
| AS-206 | 女问能否嫁意中人 | Chap. LX（pp.389–390；Fig. 15） | A | 低 | 月亮所象之人居中撮合，"produced the Marriage to effect, to the content of both parties" |
| AS-207 | 问坎特伯雷大主教（Laud）死法 | Chap. LXXII（pp.419–420） | A | 高 | 次年约 1 月 10 日被斩首（断：非绞死、更体面的死法、六七周内） |
| AS-208 | 问 Rupert 王子战局与结局 | Chap. LXXXV | A | 高 | 对 Essex 果未获胜（"nor did he"）；1646 年牛津被围降后一度在议会掌握之中——Lilly 自认拘押断语"an errour in part"，结局为混合，如实收录 |
| AS-209 | 王问爱尔兰援军 + 王后进军与会合 | Chap. LXXXV 次章 | A | 高 | 爱尔兰军果至、终在 Nantwich 被 Fairfax 歼灭；王后果于 1643 年 7 月约 14 日在 Warwickshire 与王会合；4 月 Nottingham 附近损兵 |
| AS-210 | 绅士问能否得官职 | Chap. LXXXVI（Fig. 28） | A | 低 | 三周内得职，并发现所托"太阳人"朋友为伪（面有大疤、发色黑） |
| AS-211 | Henley 附近失马问可否找回 | Chap. XCIII（pp.467–468） | A | 低 | 马三日后自行归家、果曾全程向西（断归期为一二日内，迟一日，Lilly 自记） |
| AS-212 | 问是否中巫蛊 | Chap. XCIV（pp.468–470） | A | 低 | 断非巫蛊乃隐疾；依嘱改医约三周痊愈 |
| AS-213 | 越狱囚犯问去向与可否再捕 | Chap. XCV（Fig. 29） | A | 低 | 果向东逃、潜伏一夜；周五得信、周日被官府再捕 |
| AS-214 | 夫人问囚中丈夫何时获释 | Chap. XCVI（Fig. 30） | A | 低 | 实际问卜前一日已获释：驻军被议会军上校攻下，丈夫得资助遣归 |
| AS-215 | Essex 伯爵最后一次西征出师盘（1644） | Book II 出师盘（p.473；Fig. 31） | A | 高 | 初胜、断语被讥；9 月 8 日传 9 月 2 日已尽弃军械投降、仅得士兵保全性命（Lostwithiel） |

**计数：收录 15 例 — A 级 15、B 级 0；污染高 5（AS-201、207、208、209、215）、污染低 10。**

## pending 第 3 条补核（丈夫在海外例的归期断语）——已解决，不另立新例

既有条目 `lilly-horary-husband-at-sea`（Chap. LXXI）在原 pending 中记"归期断语待补核"。经查 1647 OCR（vol1-3 本第 25788–25829 行），同一章妻亡断语之后确有完整的丈夫归期一段，原先并非缺失、只是未收录进该条目。原文要点（照录）：

- 方位："I judged the man absent was in the South west of England, in some Harbour, because [Jupiter] was angular."
- 初闻：断二三日内得音信（月亮距水星之体约一度强、星座游动）——"[so she did]. But... the report she heard of her Husband was false (for she heard he was in Town,) but it was not so."
- 确讯：水星与木星在双子座疾趋于合，合相在次年 5 月 5 日，"about that time she would have certaine newes of her Husband, if happily he came not then home."
- 结局："The second Week in May the Woman did hear certaine newes from her Husband, but he came not home till the second Week in July, he had been severall Voyages in the West parts, was taken prisoner by the Kings Forces, and at time of her question asked, was at Barnstaple"（OCR 作 "Barflablo"）。

建议（供主持角后续修订既有条目时采用，本次未改动 `masters-dataset/` 任何文件）：把该条目的断语补上上述归期三断与结局。另请注意口径：既有条目将丈夫的 significator 写作太阳（那是同章"妻亡"子断的取法）；**归期子断用的是木星（七宫主、居十宫）**，修订时两个子断的取象须分开标注，勿混。

## 筛选日志

- **核查范围**：以 1852 版 33 幅图目录为索引逐幅扫 Book II 全部图例，并补查 1647 版独有章节（尤其 XCII–XCVI 一带与疾病诸章），合计核过约 40 幅盘/章。
- **收录**：15 例（上表），均满足四要件：背景与时刻（盘题或章内可考；时刻原文不载者如实在 moment 字段注明"Not stated"，未编造）、问事、Lilly 断语原文节录、书内自记结局。
- **弃例与主因**：
  1. **无书内结局记载**（最主要弃因）：长老会存废问（Chap. LXXX，出版时未决）、哲人石/点金盘（仅断语与健康告诫）等——断语完整但书中无应验记录，按硬性标准不收。
  2. **B 级（结局不可分离）**：应许嫁妆盘（Fig. 23）结局仅"all this proved true, as I experimentally have it from the querents own Mouth"一句总括自证；问今生有无子女盘（Fig. 10）仅问卜当场体征核对、终身无子未在书内验证——均登记为 B，不收。
  3. **结局未发生/未记载**：夫妻孰先死盘（pp.406–407）仅记妻当前病况，无死亡结局。
  4. **非 Lilly 1647 原书**：安特卫普围城盘（Fig. 22）、占星命运盘（Fig. 24）、查理立旗/死期盘（Figs. 32–33）系 1852 版编者 Zadkiel 后加（1830 年代及 1649 年后材料），非 1647 Book II 内容，不收。
  5. **已收录不重复**：丈夫在海外例（Chap. LXXI）已在既有 western 集内，本次仅补核 pending 第 3 条（见上节），不立新例。
  6. **只有规则无完整个案**：如国王/官员被逐与归返章（Chap. LXXXIII）、疾病危期规则（Chap. XLVII）等纯规则章节，无完整问卜+断语+结局链，不收。
- **讹误登记汇总**：AS-203 证言计数 1647 作八男四女、1852 作七男（从 1647）；AS-205 盘题年份 OCR 一作 1643、同书 XLVII 章两引作 1645（从 1645 并标注）；AS-209 会合年份印作 "1443"（1643 之误印，照录并标注）；AS-210 结局"within lefs three weeks"系长 s 的 OCR 形，1852 作"within three weeks"（两读并录）。

## 主持裁定修訂（2026-10-29）

**口徑**：盲測輸入面不得含結局——inputs 側 subject/context 文本只許含問卜時已知之事（背景、問題、問卜時刻）與盤面資料，不得含問卜之後實際發生的結局事件或其時點；金標側（answers、本文件分級表）本就含結局，照舊不動。數據角按此裁定修復建池時發現的 AS-207，並對其餘 Lilly 14 例與六爻兩路（增刪 59 例、卜筮 20 例）全部新例的 inputs 側 subject/context 全文做結局性措辭掃描（died/beheaded/executed/recovered/果於/應驗/結果等句式）＋逐例人眼複核，共再發現並修復 14 例。**修復合計 15 例、16 個字段**；每例同步改 expansion 源條目與已生成的 phase3 單文件（benchmark/phase3/inputs/ 或 holdout3-inputs/，Lilly 單文件中 subject.background→context.setting、subject.moment→context.asked_at），其餘字段一字未動，逐例比對一致。Phase 3 尚未產生任何預測，修復不污染任何分數；其中 holdout3 的 4 例（AS-201、AS-203、AS-214、LY-258）只改其盲測輸入單文件，未讀、未動金標封存（holdout3/test_gold.jsonl）與 splits/roster。

### Lilly 路（9 例，10 字段）

- **AS-207** `subject.moment`：改前「Not stated in the chapter; he was beheaded about the tenth of January following the question.」→ 改後「Not stated in the chapter.」原書未載問卜時刻，只保留此事實，刪去被斬首的結局分句（本次裁定的觸發例）。
- **AS-201** `subject.background`：刪「Lilly verified part of the judgment in March 1646, the querent being yet alive at that date.」→ 只留「He propounded six demands at once.」1646 年 3 月尚在世是第一問（壽數）的結局原文。
- **AS-201** `subject.moment`：刪「; the judgment was still being verified in March 1646」→「Not stated in the chapter (no dated figure heading is given in the text).」
- **AS-203** `subject.moment`：刪「; she was delivered the eleventh of July following the question」→「Not stated in the chapter.」7 月 11 日分娩是產期問的結局兼應期答案。
- **AS-204** `subject.moment`：刪「; he died the fourteenth of August following」→「Not stated in the chapter.」8 月 14 日病逝是結局事件與時點。
- **AS-209** `subject.moment`：刪「, and the meeting judged followed about three or four months after the figure」→ 保留「Not stated in the chapter; the figure precedes the crossing of 11 April 1643 referred to in the judgment.」會合於三四個月後是會合問的結局時點；保留句只錨定本盤與 4 月 11 日的先後、且明言出自斷語。
- **AS-210** `subject.background`：「He employed as his friend a solar man, who proved false.」→「He employed as his friend a solar man.」刪「其後證實為偽」——朋友為偽是結局中發現之事。
- **AS-211** `subject.moment`：刪「; the horse came home on Wednesday or Thursday the 13th or 14th of January following」→「Not stated in the chapter.」馬於 1 月 13/14 日歸家是結局兼應期。
- **AS-214** `subject.moment`：刪「; in fact he had been released, and the garrison where he was prisoner taken, the same day before the question was asked」→「Not stated in the chapter.」丈夫已獲釋正是所問的答案本身。
- **AS-215** `subject.background`：刪「; he prospered in the beginning and the prediction was derided, before the surrender of his army at Lostwithiel」→ 以「...judged by Lilly for posterity.」收尾。初勝、斷語被譏、Lostwithiel 投降皆為西征結局敘述。

### 增刪卜易路（4 例）

- **LY-215** `context.setting`：刪「，此人竟未出門，至七月初八始東行避之」。七月初八東行是應驗敘述原文片段（初八往東行、地震獨免）。
- **LY-228** `context.setting`：刪「，結果三日內得差而中途身死，原文自釋其理」→ 以「初斷不得」收尾。「結果…」明述結局事件（得差＋中途身死），與金標 outcome 同文。
- **LY-255** `context.setting`：刪「，開溝果見屍骨」。「果見屍骨」是初占的應驗事件。
- **LY-258** `context.setting`：刪「，掘之果然」→ 以「設灑錢禱告之法驗之」收尾。「果然」明示點穴當場應驗結果；設法驗之的程序敘述保留。

### 卜筮正宗路（2 例）

- **LY-301** `context.asked_at`：刪「；應驗在三月」→「原文未明記月日（斷語稱目下寅卯皆克、交辰月）」。「應驗在三月」直接給出應驗時點（果於三月妻去世）；斷語口徑的「交辰月」保留。
- **LY-311** `context.asked_at`：刪「；應驗在本日申時」→「原文未明記月日（空亡辰巳）」。本日申時是其子去世的應驗時點。

### 複核命中而未改（逐項人眼判定，非結局泄漏）

- 詞彙命中屬問題本身或問卜前事實：AS-202 `question` 的 killed/come home 是所問問題用語、其 background 的「no news had been heard for many weeks」是問卜前狀態；AS-213 `question` 的 recoverable 同理；AS-208 的 Edgehill 是問卜前已發生的戰事背景。
- LY-218 `context.setting`「三十餘載後復遇其人核驗」：只言後來復遇核驗，未述父母壽元的任何結局內容、方向或時點，不刪。
- 類別判定（不屬本次口徑）：①大師斷語摘要——增刪 setting 中的「野鶴斷／反斷…」、卜筮 asked_at 中明標「據斷語／斷…」的應期，是原建池口徑的斷語側信息、非結局事件，不動；②求測者聞斷後的處置行為（LY-212 被苦留過辰時、LY-213 未能遠去、LY-225／LY-254 不聽、LY-257 仍葬之、LY-259 仍附葬之）未述所問結局事件本身，不刪；③斷語側敘述如 AS-205 background「persuaded the man to settle his affairs」只記 Lilly 勸告、不含死亡事件與日期，不刪；LY-306 的「弟死太湖」是問卜前提（所問為尸首可見否），不刪。
- notes 字段中的應驗字樣（如 LY-203／208／212／218／234／240／245／251／254／255／259 的 notes.comment）不進入 phase3 盲測單文件（建池時已略去，抽查生成文件確認無 notes 字段），不在輸入面，不改。
- 金標側同字串（answers.jsonl、data/roster3.jsonl 的 outcome_record、data/master-baseline-newdev-packet.json、data/dev-new-answers.jsonl、本文件分級表與逐例結局摘錄）是金標本體，照舊不動。

**補記（同日）**：增刪路建池腳本 `benchmark/phase3/expansion/zengshan/build_cases.py` 內嵌的 LY-215／LY-228／LY-255／LY-258 setting 原文已同步按同一口徑修復（第 139／219／383／401 行），防重跑再生泄漏；改後重跑再生的 inputs.jsonl 與 answers.jsonl 與現行文件逐字節一致。
