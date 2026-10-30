# STRIP-LOG — inputs-dev12 输入卫生剥离逐字段登记（R39 数据角，PREREG §4.1 执行）

- 依据：`runs/round39/PREREG.md` §4.1；`runs/round39/data-verify/INPUT-HYGIENE-SCAN.md` 强命中清单（15 卡／20 字段，形态 F1–F5）逐字执行。
- 底本：`benchmark/phase3/inputs-dev11/`（487 卡）；产物：`benchmark/phase3/inputs-dev12/`（487 卡＋BUILD-MANIFEST.md）。
- 构建脚本：`runs/round39/data-verify/build_inputs_dev12_strip_r39.py`（原文文本级替换：每处旧值在文件内恰出现 1 次才许替换，断言全过；其余字节逐字不变）。
- 校验脚本：`runs/round39/data-verify/verify_inputs_dev12_strip_r39.py`，结果见文末。
- 口径：只对下表 20 个命名字段动手；弱命中 25 卡一律未动；题面字段（见文末字段集定义）零改动。
- **pending：无。** 全部 20 字段在扫描件中归类明确、无题面归属疑义；其中 3 处处置附理由登记（AS-015、LY-506、BZ-301／BZ-016），供主持复核，不作 pending 挂起。

## 逐卡逐字段（原文 → 替换文）

### AS-304 · F1（2 字段）

- 字段 `provenance.book`
  - 原文：其X（推特）账号原文，后经 Timesnownews 报道引录 https://www.timesnownews.com/viral/what-happened-to-the-astrologer-who-predicted-kamala-harris-would-win-the-us-elections-become-the-first-brahmin-woman-president-with-306-seats-article-115083422
  - 替换文：其X（推特）账号原文，后经 Timesnownews 报道引录（链接略，标题含断语已剥离）
  - 说明：保留来源类型（X 账号原文）与报道方（Timesnownews）纯著录；内嵌 URL slug 直载断语全文（胜方＋席位），整链剥离。注：该 URL 与 `provenance.url` 字段同值，构建时先处理 book、再处理 url，每步出现次数断言均为 1。
- 字段 `provenance.url`
  - 原文：https://www.timesnownews.com/viral/what-happened-to-the-astrologer-who-predicted-kamala-harris-would-win-the-us-elections-become-the-first-brahmin-woman-president-with-306-seats-article-115083422
  - 替换文：（链接略，标题含断语已剥离）

### AS-306 · F1（1 字段）

- 字段 `provenance.book`
  - 原文：其YouTube视频（2024-06-02）；PRWeb 2024-11通稿 https://www.prweb.com/releases/trump-will-be-crowned---indian-origin-us-based-astrologer-predicted-this-in-june-2024-302299787.html
  - 替换文：其YouTube视频（2024-06-02）；PRWeb 2024-11通稿（链接略，标题含断语已剥离）
  - 说明：保留视频与通稿的著录日期（2024-06-02／2024-11，属来源发表日期、非结局日期）；PRWeb 链 slug 直载断语（Trump 胜），整链剥离。

### WP-002 · F1（1 字段）

- 字段 `provenance.url`
  - 原文：https://twt-assets.washtimes.com/news/2008/may/20/its-in-the-stars-for-obama-4575-5/
  - 替换文：（链接略，标题含断语已剥离）
  - 说明：`provenance.work`（The Washington Times, news report, 20 May 2008）为中性著录、不在清单内，未动。

### WP-003 · F1（2 字段）

- 字段 `provenance.work`
  - 原文：Astrology News Service, 'Panel of Astrologers Predicts Obama Victory', May 2012 (New Orleans)
  - 替换文：Astrology News Service, news report, May 2012 (New Orleans)
  - 说明：保留机构名、来源类型、年月与地点；标题直载断语方向（Obama 胜），以来源类型词替换标题。
- 字段 `provenance.url`
  - 原文：https://astrologynewsservice.com/news/panel-of-astrologers-predicts-obama-victory/
  - 替换文：（链接略，标题含断语已剥离）

### WP-006 · F1（2 字段）

- 字段 `provenance.work`
  - 原文：Jessica Adams, 'How Astrology Predicts a Brexit', jessicaadams.com, 22 February 2016 (referencing her 5 July 2015 'GOODBYE EU' post)
  - 替换文：Jessica Adams, blog post, jessicaadams.com, 22 February 2016 (referencing her 5 July 2015 post)
  - 说明：保留作者、站点、日期纯著录；正题与所引 2015 年帖题均载脱欧方向，一并以来源类型词／中性指称替换。
- 字段 `provenance.url`
  - 原文：https://stg.jessicaadams.com/2016/02/22/how-astrology-predicts-a-brexit/
  - 替换文：（链接略，标题含断语已剥离）

### WP-007 · F1（1 字段）

- 字段 `provenance.url`
  - 原文：https://thetab.com/us/2016/08/26/new-york-psychic-predicted-trump-winning-election-50290
  - 替换文：（链接略，标题含断语已剥离）

### WP-008 · F1（2 字段）

- 字段 `provenance.work`
  - 原文：ANI via Business Standard, 'LS polls: Odds in PM Modi's favour, say clairvoyants', 30 March 2019
  - 替换文：ANI via Business Standard, news report, 30 March 2019
  - 说明：保留通讯社／刊载方、来源类型与日期；标题直载断语方向（利 Modi），剥离。
- 字段 `provenance.url`
  - 原文：https://www.business-standard.com/amp/article/news-ani/ls-polls-odds-in-pm-modi-s-favour-say-clairvoyants-119033000747_1.html
  - 替换文：（链接略，标题含断语已剥离）

### WP-009 · F1（1 字段）

- 字段 `provenance.url`
  - 原文：https://sportzwiki.com/cricket/icc-cricket-world-cup-2019-team-india-wont-win-the-tournament-says-famous-astrologer-greenstone-lobo/
  - 替换文：（链接略，标题含断语已剥离）

### WP-012 · F1（1 字段）

- 字段 `provenance.url`
  - 原文：https://www.israelhayom.com/2020/11/02/the-us-will-fall-apart-mystics-weigh-in-on-2020-presidential-election/
  - 替换文：（链接略，标题含断语已剥离）
  - 说明：slug 中「the-us-will-fall-apart」即本卡第三问方向，剥离；`provenance.work` 中性著录未动。

### WP-013 · F2（1 字段）

- 字段 `provenance.page`
  - 原文：Roundup items 7 (Labour Wins the 2024 UK Election)
  - 替换文：Roundup items 7
  - 说明：按口径保留页位编号本身（Roundup 第 7 条），仅删除括号内直载断语的条目标题（工党胜）。

### BZ-301 · F3（1 字段）

- 字段 `context.setting`
  - 原文：2011年，李居明公开预言民国111年（2022年）国民党走向灭亡阶段；当时国民党正值马英九执政、无明显存亡危机
  - 替换文：2011年，李居明就民国111年（2022年）国民党未来走向作出公开预言；当时国民党正值马英九执政、无明显存亡危机
  - 处置理由：断语方向（走向灭亡阶段）删除；「曾作公开预言」之存在性保留——本卡 `context.question` 本身即「公开预测：中国国民党之未来走向（2022年）」，预言存在属所问前提而非答案；后半句为占时背景（执政状态），属前提，未动。

### ZY-003 · F3（1 字段）

- 字段 `context.setting`
  - 原文：穆姜（魯宣公夫人）與叔孫僑如謀亂事敗，被遷於東宮軟禁；始往而筮之，問能否速出。占史斷「必速出」，穆姜自斷相反——本例金標以穆姜自斷為準，史官之斷同錄於 predictions 第二條供對照
  - 替换文：穆姜（魯宣公夫人）與叔孫僑如謀亂事敗，被遷於東宮軟禁；始往而筮之，問能否速出。
  - 说明：双断语（占史断语＋穆姜自断方向）与金标取舍指示全数删除；仅留事件前提与所问本身（与 `context.question` 同旨）。

### LY-506 · F3（1 字段，一字段双载）

- 字段 `context.setting`
  - 原文：初占母病，斷語轉指初生子有災；八月子驚風後再占子病
  - 替换文：初占母病，其後再占子病
  - 处置理由：初占断语（轉指初生子有災）删除；「八月子驚風」为初占之应验事件（结局事实），删除。再占的所问主题（子病）已由 `context.question`（占母病；再占子病）完整承载，替换文以中性先后叙述保留两占结构；两占时点未受损——`context.asked_at`（未月丁亥日（初占）；酉月丁卯日（再占））为事实日期字段、不在清单内、未动，酉月即原 setting「八月」所指月份信息仍在卡内。

### BZ-016 · F4（1 字段）

- 字段 `context.setting`
  - 原文：清雍正帝第四子弘历，生于王府，断时（任氏注书时）其后来为帝之事于命例语境中作为已知贵造引用——注意：此例为事后引用型成例，盲测时只能给四柱与时代背景，不得给身份
  - 替换文：清雍正帝第四子弘历，生于王府，任氏注书时引此命造为例
  - 说明：结局事实（后来为帝）、贵造定性与「不得给身份」的编辑注记一并删除；保留人物与生地前提及「任氏引为例」的著录性叙述。注：`subject` 内身份表述属题面字段、按零改动口径未动（扫描件已登记此为卡内既有状态，非本轮剥离范围）。

### AS-015 · F5（2 字段）

- 字段 `context.asked_at`
  - 原文：Not stated in the text (the death Lilly timed from the figure fell on 8 October following)
  - 替换文：Not stated in the text
  - 处置与理由（逐字登记）：本字段**事实性占问日期与断语可分离**——原文事实部分即「Not stated in the text」，意为原文未载占问日期，卡内本无事实日期可保；括号内整句为断语所定死亡时点且明言已届期发生（断语时点＋结局日期 8 October），整句删除，不损任何事实日期信息。
- 字段 `context.attachments.note`
  - 原文：Positions partly garbled in the 1647 OCR; the husband's significator being wholly unafflicted and the timing of the wife's death are the two points Lilly states unambiguously.
  - 替换文：Positions partly garbled in the 1647 OCR; the husband's significator being wholly unafflicted is one of the points Lilly states unambiguously.
  - 说明：仅删除承载断语时点的成分（the timing of the wife's death）并作相应单复数衔接（are the two points → is one of the points）；OCR 残损说明与另一要点（夫之主星无克）不在扫描件命中摘录内，逐字保留。

## 汇总

- 剥离：**15 卡／20 字段**（F1：9 卡 13 字段；F2：1 卡 1 字段；F3：3 卡 3 字段；F4：1 卡 1 字段；F5：1 卡 2 字段），与扫描件强命中清单逐项对应。
- 未动：弱命中 25 卡全数保留（理由见 PREREG §4.1 写死登记）；其余 447 卡未命中、逐字复制。
- 附加复扫：对 20 个剥离后字段以断语残片（胜方名＋席位、slug 关键词、必速出、走向灭亡、惊风、后来为帝、8 October、妻死时点语等 25 个片段）回扫，命中 0。

## 校验结果（verify_inputs_dev12_strip_r39.py，原文输出）

```
(1) dev11 cards=487 dev12 cards=487
(1) id sets equal: True; symdiff=[]
(2) deep-diff (card, field) count=20; expected=20
(2) diffs == expected set: True
(2) byte-check: stripped cards byte-identical (bad)=[]; unstripped cards byte-differ (bad)=[]
(3) face-field hash mismatches: 0 []
RESULT: PASS
```

- 校验 (1)：inputs-dev12 与 inputs-dev11 文件名 id 集全等，卡数各 487。
- 校验 (2)：JSON 深比对 diff 恰为上表 20 个（卡，字段），无遗漏、无越界；字节级附带核查：未登记 472 卡与底本逐字一致、登记 15 卡均有差异。（BUILD-MANIFEST.md 非卡，其轮次注记更新为预期内差异，不入卡 diff 口径。）
- 校验 (3)：题面字段逐卡哈希不变（487/487 一致）。**题面字段集定义**（按扫描件口径）：顶层标识键 `id`／`uid`／`source_id`（卡内有者）＋`subject` 整棵子树＋`context.question`＋`context.attachments` 课式本体（attachments 全键扣除非课式字段 `note`、`chart_note`、`source`、`secondhand`、`chart_excerpt` 后的子集）；哈希为该字段组规范 JSON（sort_keys、ensure_ascii=False）的 SHA-256。
