# R36 natal 低基线 5 例回源核查裁定（round36 §6② 数据角）

- 性质：**数据角核查**（只核金标 master_predictions 完整性与 outcome 对应关系，不作断、不评新分）。依据 `benchmark/phase3/runs/round36/PREREG.md` §0 时序（先裁决、后建包）、§6② 与 `benchmark/phase3/runs/round35/diagnosis/DIAG-BZ-exposure.md` §五（5 例名单：MP-003、MP-015、MP-002、MP-018、OC-006，大师基线 total≤1.25）。
- 体例：照 `benchmark/phase3/expansion12/pending-verify/VERDICTS.md`——成立（记录错位/缺失致基线失真）→记 errata 并提 overlay；不成立→销号记回源证据；歧义→如实登记。
- 回源路径：基线分数出处 `benchmark/phase3/data/master-baseline-dev9.json`（仅存 {src, total}）→ 建包记录 `data/master-baseline-dev9-BUILD.md`（dev9＝dev8＋75 例；再上溯 dev7/dev8 BUILD）→ 基线评审包与逐席分数（MP-003/015/018：`data/dev7-baseline-build/`；MP-002/OC-006：`holdout8-acceptance/judging/`，src=holdout8-acceptance）→ 金标源记录 `benchmark/phase3/expansion6/modern-cn/cases.jsonl`（MP 四例）与 `benchmark/phase3/expansion6/classical-other/cases.jsonl`（OC-006）→ 原书/原文层（TVBS 原报道页、《千里命稿》算准网在线本，本轮实抓核对；MP-015/MP-018 原文为在线存档、盘上以 cases 记录＋provenance 指针为准，限度逐例登记）。
- 题面对应以 `benchmark/phase3/inputs-dev11/<id>.json` 为准。

## 汇总

| 例 | 大师基线 total | 裁决 | 一句话依据 |
|---|---|---|---|
| MP-003 | 0.0 | **不成立（销号）** | 曼樺断「2020 年不会出来选总统」，TVBS 原文逐字在案；韩国瑜实际参选并赢初选——原断本身全反，非记录失真 |
| MP-015 | 0.0 | **不成立（销号）** | 盧恒立断拜登 2024 好转、特朗普赢面很低，三项断言俱全；实际拜登退选、特朗普胜选——原断本身全反 |
| MP-002 | 1.0 | **不成立（销号）** | 曼樺断蔡英文「没当官的格、硬选民进党必输」，TVBS 原文逐字在案；实际蔡以 817 万票连任——原断本身全反；total 1.0 系仲裁 timing 口径（见逐例） |
| MP-018 | 0.5 | **不成立（销号）** | 梁善行断曾俊华劣势下戏剧当选，断言单一而明确；实际 365 票落选——原断本身落空；节录省略号与作者归属推定已在源记录自注，不影响断言集 |
| OC-006 | 1.25 | **不成立（销号）** | 韦千里断荣宗敬「挫折无足忧、丙子丁丑大振旗鼓」，《千里命稿》原文逐字在案；实际未再大振、1938 年卒——原断近期乐观部分本身落空，基线低分如实 |

**成立 0 例、歧义 0 例、未能回源 0 例。故同目录 `overlay-proposals.json` 为空数组 `[]`（照 round35 data-verify 先例）；§0 时序所需的「裁决先行」已完成，本 5 例无 errata、无 overlay 新增，建包可按现行 16 条 overlay 为底继续。既有各轮分数一概不回改。**

共同附带发现（不入裁决、与 §6① 审计互证）：MP-003、MP-015 的**基线评审包版** outcome_record 尾句带判语（MP-003「『不会参选』断言落空（16 年大运说无从单独证伪，不计）」、MP-015「两项核心断言皆反」），OC-006 的 holdout8 包版 outcome 尾句「断语的近期乐观断言与结局仅部分相合」同型——三句所述与同条事件文本一致、两席评审 reason 均以事件本身立论，未见尾句致失真；且现行 R35 manifest 中 MP-003/MP-015 已由 overlay 剥离为纯事件句（OC-006 尾句仍在，已登记于 `PREDICATE-HYGIENE-AUDIT.md` A 类）。

---

## 一、MP-003 — 不成立（销号）

- 对象与题面：韩国瑜会不会参选 2020 年总统（2019 年 1 月问，inputs-dev11/MP-003.json；大师 曼樺）。
- 基线链：total 0.0（src=dev7-baseline-build）；双评审 A/B 均 0/0/0（judgeA-part1.jsonl:29、judgeB-part1.jsonl:29，reason 均以「断 2020 不会出来选总统、实则参选并成为候选人」立论）；part-new.jsonl:29 定稿 0.0。
- 金标完整性：基线包 prediction（dev7 packet D7B-MP-003）与源记录 `expansion6/modern-cn/cases.jsonl:3` 的 statement_excerpt **逐字一致**；key_assertions 两条（「2020 年不会出来选总统」「将走 16 年大运」）、timing_claim（2020 年总统大选提名期）俱全，无截断。
- 原文层核对（本轮实抓 TVBS 原报道 https://news.tvbs.com.tw/politics/1063982 ，页内 L4）：「韓國瑜八字帶『金』，需要『水』來潤，剛好他『得水而清』走在庚申日柱，將走16年大運，但2020年並不會出來選總統，主要是他太講義氣，會尊重國民黨內其他大老」——与 excerpt 逐字同（仅标点/繁简渲染差），断语无缺失、无被节录掉的对冲句；cases 另记 ETtoday 2020-01-12 选后盘点独立佐证此断确于选前作出。
- outcome 对应：源记录 outcome（2019 年 4 月表态参选、7 月赢初选成候选人、2020 年 1 月败选）与题面所问（是否参选）直接对应、为公开政治记录；现行 manifest 版已经 overlay 剥离尾句、与上一致。
- 裁决：**不成立**。低分系原断本身方向全反（核心断言「不会参选」被事实直接证伪），记录三面（源记录／基线包／原文）一致、断语完整、结局对应。销号。

## 二、MP-015 — 不成立（销号）

- 对象与题面：2024 龙年拜登与特朗普运势及大选前景（2024 年 2 月 CNN 专访，inputs-dev11/MP-015.json；大师 盧恒立）。
- 基线链：total 0.0（src=dev7-baseline-build）；双评审 A/B 均 0/0/0（judgeA-part2.jsonl:4、judgeB-part2.jsonl:4，reason 均以拜登退选、特朗普胜选与两项核心断言全反立论）；part-new.jsonl:36 定稿 0.0。
- 金标完整性：基线包 prediction（D7B-MP-015）与源记录 `expansion6/modern-cn/cases.jsonl:15` 的 statement_excerpt **逐字一致**；key_assertions 三条（拜登 2024 好转／特朗普 2024 不佳／特朗普赢得竞争可能性很低）、timing_claim（2024 甲辰龙年）俱全。
- 回源限度（如实登记）：CNN 英文原文页建池时未检得，断语靠中天 2024-02-10、搜狐同月转录及华视 2026-02-18 复访报道三方互证（cases grade_note 已自注、证据强度中上）；华视复访中记者以「2024 年也说过拜登运势很好」当面复问、盧本人回应未否认断语存在——断语归属与内容无反证。本轮未再抓在线原文，以盘上 cases 记录＋三方互证账为准，此限度不影响裁决方向（断语若有缺失，只可能缺「特朗普挑战多」一类已计入断言，不存在被漏记的「特朗普将胜」对冲断语的任何记录线索）。
- outcome 对应：拜登 2024-07-21 退选、特朗普 2024-11-05 胜选，与题面（两人运势与竞争前景）直接对应；现行 manifest 版已经 overlay 剥离尾句「两项核心断言皆反」。
- 裁决：**不成立**。低分系原断本身全反，断语集完整、结局对应。销号。

## 三、MP-002 — 不成立（销号）

- 对象与题面：蔡英文 2020 年竞选连任前景、民进党胜负（2019 年 1 月新书发表会，inputs-dev11/MP-002.json；大师 曼樺，与 MP-003 同源同场）。
- 基线链：total 1.0（src=holdout8-acceptance）；大师匿号 H8-020：Judge-A 0/0/0、Judge-B 0/0/2、分歧仲裁 0/0/1 定稿 total 1（final-scores.json pairs.MP-002.master）。**1.0 的构成**：direction/claims 两席与仲裁一致为 0（全反无争议）；timing 一项三读 0/2/1 分歧，仲裁以「结局无可核时点」记 1——holdout8 包版 outcome 只载事件（连任、立院过半）未载日期，此系评审口径内的时点处理，非记录错位（源记录 outcome.source 明确载选举日 2020-01-11 与票数，见下）。
- 金标完整性：holdout8 包 prediction（H8-020）＝源记录 `expansion6/modern-cn/cases.jsonl:2` 的 statement_excerpt 全文＋（与 key_assertions 两条逐字同）＋（与 timing_claim 同），无缺失、无截断。
- 原文层核对（本轮实抓 TVBS 原报道，页内 L12）：「蔡英文則是2016年後就沒大運了，且她不是當官的格，屬於有錢的格，若硬要出來選，民進黨絕對會輸！」与标题「總統蔡英文『沒有當官的格』，若2020硬要選，民進黨必會輸」（L2 同义复述）——与 excerpt 逐字同，断语完整。
- outcome 对应：源记录 outcome.description（参选并以 817 万票史上最高票连任、民进党保住立法院过半）与 holdout8 包版、现行 manifest 版一致，与题面直接对应。
- 裁决：**不成立**。低分系原断本身全反；timing 1 分为仲裁口径产物、已在基线链内可溯，不构成「大师基线失真」。销号。

## 四、MP-018 — 不成立（销号）

- 对象与题面：曾俊华能否当选 2017 年香港行政长官（2017 年 1 月分析、刊《睇相王》2017 年 2 月号，inputs-dev11/MP-018.json；大师 梁善行（玄機閣））。
- 基线链：total 0.5（src=dev7-baseline-build）；Judge-A 0/0/0、Judge-B 0/0/1（timing 差为「结局无可核时点」口径差），part-new.jsonl:39 定稿 direction 0/claims 0/timing 0.5/total 0.5。
- 金标完整性：基线包 prediction（D7B-MP-018）与源记录 `expansion6/modern-cn/cases.jsonl:18` 的 statement_excerpt **逐字一致**；key_assertions 仅一条（「曾俊华在劣势下戏剧性当选特首」）、timing_claim 2017-03-26 俱全。
- 两处源记录自注（不影响裁决、照实登记）：(1) excerpt 中段有省略号「……」——节录的是理据铺陈段，前后两段（「会在声势落后之下，戏剧地胜出」「拙见是曾俊华先生会在劣势下当选」）均为无条件断言，省略部分不存在使断言集增减的记录线索，BUILD-REPORT 第 60 行逐例账亦只记此一断；(2) 作者归属梁善行系据玄机阁存档页末连结推定、无第三方同期互证（grade_note 与 BUILD-REPORT 第 88 行均已明示为归属风险）——归属若误，误在 master 字段，不在断语与结局的对应关系，不属本项「基线失真」口径。
- outcome 对应：林郑月娥 777 票当选、曾俊华 365 票落选，为公开选举记录，与题面直接对应；基线包版与现行 manifest 版 outcome 均为此纯事件句。
- 裁决：**不成立**。低分系原断本身落空（唯一断言即当选、实际落选），断言集完整、结局对应。销号；作者归属推定一节留源记录原注，不另立 errata。

## 五、OC-006 — 不成立（销号）

- 对象与题面：荣宗敬四柱（癸酉 庚申 戊午 甲寅）事业当前受挫后走势（约 1935 年问，《千里命稿》应运篇上，inputs-dev11/OC-006.json；大师 韦千里）。
- 基线链：total 1.25（src=holdout8-acceptance）；大师匿号 H8-042：Judge-A 0.5/1.0/0＝1.5、Judge-B 0.5/0.5/0＝1.0，无仲裁触发，定稿取均值 1.25（final-scores.json pairs.OC-006.master）。分项形态：direction 0.5（乐观终局大半落空）、claims 0.75（「纺织界泰斗／极贵」一断得部分印证、「大振」一断落空）、timing 0（丙子丁丑大振时点未应）——低分内部构成与断语逐项对位，无整例错配迹象。
- 金标完整性：holdout8 包 prediction（H8-042）＝源记录 `expansion6/classical-other/cases.jsonl:6` 的 statement_excerpt＋（key_assertions 三条逐字同）＋（timing_claim 同），俱全。
- 原文层核对（本轮实抓算准网《千里命稿》应运篇上 https://www.suanzhun.net/book/249.html ，页内 L41–L43，荣宗敬造）：「子平真詮所謂殺旺食強而身健。為極等之貴格，宜其致力實業……為我國紡織界之泰斗……現行甲運。似遜於前，明年丙子。後年丁丑。歲運木火相生。或能日升月恆，大振旗鼓。目前挫折。無足憂傷。」——excerpt 为原文的加标点转录，三条断言逐项俱在；唯一节录差：原文「現行甲運，似遜於前」一句未入 excerpt——该句为运程 nuance，不在 key_assertions 内、且方向与已录断语不冲突（甲运逊前与丙丁大振并存于原断），不构成断语缺失致失真。原文另起句交代占时背景（申新七厂被汇丰强行拍卖），与 cases 的 context（申新危机）对应。
- outcome 对应：源记录 outcome（申新系统整顿存续、荣宗敬 1938 年卒于上海、生前未再现大振旗鼓）与 holdout8 包版、现行 manifest 版一致，源为通行史实；题面所问（受挫后走势）与结局（存续但未大振、1938 卒）直接对应。其尾句判语问题属 §6① 卫生范畴（见汇总附带发现），所述「仅部分相合」与事件文本相符。
- 裁决：**不成立**。低分系原断近期乐观部分（无足忧／丙子丁丑大振）本身落空、「泰斗」部分得验的如实计分，断语完整（节录差已登记、不涉断言集）、结局对应。销号。

---

## 附：方法与限制

- 定位方法：以基线 {src, total} 为起点，沿 BUILD 链回基线评审包逐席分数，再以 id 对齐 expansion6 两份 cases.jsonl 金标源记录逐字比对 prediction／key_assertions／timing_claim／outcome 四面，最后回原书原文层（MP-002/003 TVBS 原页、OC-006 算准网应运篇上，本轮实抓逐字核对）。
- 回源完成度：5 例全部完成四面对齐；原文层实抓核对 3 例（MP-002、MP-003、OC-006）；MP-015（CNN 专访转录、三方互证账在 cases）与 MP-018（杂志存档、归属推定注在 cases/BUILD-REPORT）以盘上源记录＋provenance 指针为准，两例的限度已逐例登记，均不改变裁决方向。
- 本次产出仅同目录 `VERDICTS.md` 与 `overlay-proposals.json`（空数组）两文件；未改动任何既有文件、未改任何已定稿分数、未做 git 操作。
