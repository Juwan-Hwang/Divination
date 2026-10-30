# INPUT-HYGIENE-SCAN — inputs-dev11 输入卫生债计数（R39 数据角·件三）

执行：数据角（只计数登记，**不改任何卡**）。范围：`benchmark/phase3/inputs-dev11/` 全部 **487 卡**（488 项含 BUILD-MANIFEST.md，非卡不计）。背景：R38 盲测自报 AS-304/AS-306 输入卡 provenance 自带原占者断语线索；本件逐卡定界同类债务，是否剥离待 R39 预注册裁决，本件不裁决、不动手。

## 口径（先定界，后计数）

- **检查字段**：全部非题面字段——`provenance.*`（book/work/edition/url/page/chapter/claimed_source）、`context.setting`、`context.asked_at`、`context.attachments` 中非课式字段（note/chart_note/source/secondhand/chart_excerpt）、`notes.*`、`master` 等。题面字段不查：`context.question`、`subject.*`、课式本体（卦象/四柱/课式/爻象等纯数据附件）。
- **命中定义**：非题面字段含**原占者断语内容**或**结局方向性文本**（胜负方、死亡、登位、具体名次/日期等可据以答题的方向信息）。
- **强命中**：断语内容或结局方向被实质给出（可据以压缩盲测作答空间）。
- **弱命中**：只给断语/验证之存在性、主题、类型或残片段（如出处标题只提主题不给方向、asked_at 引断语干支片段定日期、前提性断语概要），方向信息残缺或非本卡金标。
- **不计命中**（纯出处著录/题面复述）：书名与体例词（《占验指南》《经验卦例》《四柱预测学》、source_locator 中「占验例第X」、凡例「所验之占」等）；chapter 标题复述占题（如 Lilly 章题「what manner of death…」「占出狱」「占回奏吉凶」——系问题而非答案）；setting 复述所问之事（如「shall the money be recovered?」式背景）；占时已知前提（如病危、命主已逝后验盘之「逝」为来询前提而非所断——其中仅给类型提示者计弱命中，见 OC-007/011）；编辑性污染警告（如 MH-001/003 notes 仅言「过于著名、评分降权」，无断语/结局，不计）。

方法：两支脚本（本目录 `scan_inputs_hygiene_r39.py` 模式网＋`scan_inputs_hygiene_broad_r39.py` 宽网，共 462 行候选）逐卡提取非题面字段，再逐条人工裁定；AS/WP 现代卡与全部强/弱命中卡均回原卡满文复核。计数单位：**卡**（一卡多字段命中仍计 1 卡，字段数另计）。

## 结论先行

| 口径 | 卡数 | 字段命中数 |
|---|---|---|
| **强命中** | **15** | 20 |
| **弱命中** | **25** | — |
| **命中总计** | **40 / 487** | — |
| 未命中 | 447 | — |

R38 自报两例（AS-304、AS-306）均复核成立且属强命中（形态 F1）。

## 强命中清单（15 卡）

### 形态 F1：出处标题／URL slug 直载断语方向（9 卡，13 字段）

| 卡 | 命中字段 | 命中文本（摘） |
|---|---|---|
| AS-304 | provenance.book、provenance.url | Timesnownews URL：`…who-predicted-kamala-harris-would-win-the-us-elections-become-the-first-brahmin-woman-president-with-306-seats…`（断语全文方向：Harris 胜、306 席） |
| AS-306 | provenance.book | PRWeb URL：`trump-will-be-crowned---indian-origin-us-based-astrologer-predicted-this-in-june-2024`（Trump 胜） |
| WP-002 | provenance.url | Washington Times URL slug：`its-in-the-stars-for-obama`（星象利 Obama） |
| WP-003 | provenance.work、provenance.url | 标题『Panel of Astrologers Predicts Obama Victory』＋同 slug URL |
| WP-006 | provenance.work、provenance.url | 标题『How Astrology Predicts a Brexit』，work 内并引其 2015 年『GOODBYE EU』帖（脱欧方向） |
| WP-007 | provenance.url | thetab URL slug：`new-york-psychic-predicted-trump-winning-election` |
| WP-008 | provenance.work、provenance.url | 标题『LS polls: Odds in PM Modi's favour, say clairvoyants』＋同 slug URL（利 Modi） |
| WP-009 | provenance.url | sportzwiki URL slug：`team-india-wont-win-the-tournament-says-famous-astrologer-greenstone-lobo…`（印度不胜） |
| WP-012 | provenance.url | Israel Hayom URL slug：`the-us-will-fall-apart-mystics-weigh-in-on-2020-presidential-election`（选后美国分崩一说，即本卡第三问方向） |

### 形态 F2：出处页位字段载断语条目（1 卡，1 字段）

| 卡 | 命中字段 | 命中文本 |
|---|---|---|
| WP-013 | provenance.page | `Roundup items 7 (Labour Wins the 2024 UK Election)`（16 条预测中第 7 条内容直载：工党胜） |

### 形态 F3：setting 直载断语内容（3 卡，3 字段）

| 卡 | 命中字段 | 命中文本（摘） |
|---|---|---|
| BZ-301 | context.setting | 「2011年，李居明公开预言民国111年（2022年）国民党走向灭亡阶段」——本卡所问即该公开预言，setting 复述断语全文 |
| ZY-003 | context.setting | 「占史断『必速出』，穆姜自断相反——本例金标以穆姜自断为准」——双断语俱载且明示金标取舍，本轮最重一例 |
| LY-506 | context.setting | 「初占母病，斷語轉指初生子有災；八月子驚風後再占子病」——含初占断语转指＋八月惊风应验事件（对初占为结局、对再占为前提，一字段双载） |

### 形态 F4：setting 直载结局事实（1 卡，1 字段）

| 卡 | 命中字段 | 命中文本（摘） |
|---|---|---|
| BZ-016 | context.setting | 「清雍正帝第四子弘历……其后来为帝之事于命例语境中作为已知贵造引用」——结局（后为帝）与身份线索直载；卡内已自带「盲测时不得给身份」注记，属已知债、本件只登记 |

### 形态 F5：asked_at／note 载断语时点与结局日期（1 卡，2 字段）

| 卡 | 命中字段 | 命中文本（摘） |
|---|---|---|
| AS-015 | context.asked_at | `(the death Lilly timed from the figure fell on 8 October following)`——断语所定死亡时点且明言已届期发生 |
| AS-015 | context.attachments.note | `…the timing of the wife's death are the two points Lilly states unambiguously`——断语要点（妻死时点）在 note 复述 |

## 弱命中清单（25 卡）

### 形态 W1：出处标题／URL 仅主题或既往断语、无本卡方向（5 卡）

| 卡 | 字段 | 说明 |
|---|---|---|
| AS-302 | provenance.book、provenance.url | slug `british-astrologer-who-predicted-coronavirus`：载其**既往**新冠预言（成名事），本卡所问为 2020-10 后六个月走向，方向未给 |
| AS-303 | provenance.book、provenance.url | slug `…predicts-date-of-world-war-3`：只给断语主题（三战日期），日期值未给；其 asked_at/page「事前，Moneycontrol 于结果前报道」为编辑注记、不计 |
| AS-307 | provenance.book | slug `…heres-who-we-predict-will-win-the-2024-race`：宣布赢家预测存在，赢家名未在 slug 给出 |
| WP-004 | provenance.url、provenance.page | 标题『Astrologers predict who is going to win White House race』：无方向 |
| WP-005 | provenance.work、provenance.url | 同上标题（经 Prothom Alo 转载）：无方向 |

### 形态 W2：asked_at 引断语／应验片段定日期（10 卡）

| 卡 | asked_at 形态 |
|---|---|
| LY-027 | 引断语「辰月克之，申日生之」 |
| LY-028 | 「（據斷語）」字样，无引文 |
| LY-029 | 引断语「又逄月沖」 |
| LY-030 | 「（據斷語…）」字样，无引文 |
| LY-031 | 引断语「未土卯月克之」 |
| LY-032 | 引断语「墓於辰日」 |
| LY-033 | 「（斷語及應驗涉立春、正月）」——并及应验存在 |
| LY-035 | 「（據斷語）」字样，无引文 |
| LY-036 | 据**应验**「果於本月」定月——应验片段入 asked_at，本组最重 |
| LY-314 | 「同卦再驗例為七月庚辰日」——再验例存在性与日期 |

说明：W2 所引多为干支生克片段（定月日用），不含吉凶断语全文；其债在「字段自承日期系从断语/应验反推」，与 F5 同族而轻。

### 形态 W3：setting 断语／验证存在性或类型提示（6 卡）

| 卡 | 字段 | 说明 |
|---|---|---|
| AS-002 | context.setting | 引 Lilly 自述 `I have seen the experience of my judgment`：自承已见应验，方向未给 |
| AS-012 | context.setting | `he pressed his suit for the parsonage despite Lilly's advice`：暗示 Lilly 劝阻方向，未明言 |
| BZ-104 | context.setting | 「邵就其四柱对其父作出关于未来年份的断语」：断语存在性，内容未给 |
| BZ-105 | context.setting | 「邵先就其柱中断其过去两个年份的经历以验盘……属『测过去』的回溯验证」：案例类型提示 |
| OC-007 | context.asked_at、context.setting | 「命主逝世后，友人持年庚来询／问者欲验推断」：逝后验盘类型（死亡系来询前提） |
| OC-011 | context.asked_at、context.setting | 同上（当红电影明星新近逝世、友人嘱推验断） |

### 形态 W4：setting 前提性断语／结局对比概要（3 卡）

| 卡 | 字段 | 说明 |
|---|---|---|
| BZ-035 | context.setting | 「与崇祯造同为曲直从旺，一清一浊，结局悬殊」：结局对比框架，方向归属未在文本内明示（李鸿章身份本身在 subject/setting 为已知前提） |
| OC-024 | context.setting | 「遗书预言来访秀士可托身后事」：前提性**他人**预言（易者遗书），非本卡占者之断，然其内容即故事机枢 |
| OC-025 | context.setting | 「邵雍预先在椅底写下某年月日椅子将被坐破的预言，届期验之」：预书内容概要，关键日期已以「某年月日」隐去 |

### 形态 W5：chart_excerpt 后验之理片段（1 卡）

| 卡 | 字段 | 说明 |
|---|---|---|
| BQ-024 | context.attachments.chart_excerpt | 「注家后验之理：『孟月四爻……正临怪爻发动』（螣蛇鬼动）」：注家事后释理片段入输入附件，仅卦理机枢、无结局文 |

## 形态分类计数汇总

| 形态 | 卡数 | 备注 |
|---|---|---|
| F1 出处标题/URL 直载断语方向 | 9 | 强 |
| F2 出处页位载断语条目 | 1 | 强 |
| F3 setting 直载断语内容 | 3 | 强（LY-506 兼载应验事件） |
| F4 setting 直载结局事实 | 1 | 强 |
| F5 asked_at/note 载断语时点与结局日期 | 1 | 强 |
| W1 出处仅主题/既往断语 | 5 | 弱 |
| W2 asked_at 引断语/应验片段 | 10 | 弱 |
| W3 setting 存在性/类型提示 | 6 | 弱 |
| W4 setting 前提性断语/对比概要 | 3 | 弱 |
| W5 chart_excerpt 后验片段 | 1 | 弱 |
| **合计** | **40** | 强 15＋弱 25；余 447 卡未命中 |

## 限度与未计说明

- 现代公开预测卡（AS-301–307、WP-001–013、BZ-301/304）出处即新闻/博客标题与 URL，slug 化标题是 F1/W1 两形态的系统性来源；古籍卡债务则集中在 asked_at 反推注记（W2）与 setting 转述（F3/F4/W3/W4）。
- 同一卡在 provenance.book 与 provenance.url 双载同一 URL 者按 1 卡计（字段数另计，强命中 15 卡共 20 字段）。
- 本件只计数登记：未改任何卡、未提剥离方案；强命中 15 卡（尤其 ZY-003 明示金标取舍、LY-506 断语＋应验同载、BZ-016 身份＋结局同载）建议主持在 R39 预注册裁决时优先处理，裁决口径不在本件。
- 过程文件：`scan_inputs_hygiene_r39.py`、`candidates_hygiene_r39.jsonl`（模式网候选 36 行）、`scan_inputs_hygiene_broad_r39.py`、`broad_candidates_r39.jsonl`（宽网候选 462 行），同目录存档，裁定结果以本件为准。
