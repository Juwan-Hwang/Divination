# Phase 3 第六轮扩数（expansion6）· 现代西方一路 BUILD-REPORT

- 执行：数据角（现代西方占星／卜卦／塔罗），2026-10-29（Asia/Shanghai）
- 落盘：`benchmark/phase3/expansion6/modern-west/`（`cases.jsonl` 16 例＋`inputs/WP-001…016.json` 盲测面 16 份）
- 新例：**16 例 ＝ A 级 13 例 ＋ B 级 3 例**（目标 A 级 12–20 例，落在目标区间下沿；宁缺毋滥，未为凑数放宽标准）
- 纪律：未读取任何 holdout 的 `test_gold.jsonl`；未修改既有文件；未提交 git（主持角统一提交）。全部来源为公开网页／期刊转录，未登录、未绕付费墙。

## 1. 新例清单

### A 级（13 例，holdout_eligible=true，contamination 全部 high——皆著名公共事件，逐例已标）

| id | 大师 | 对象 | 断语（方向） | 结局 | 时间戳证据 |
|---|---|---|---|---|---|
| WP-001 | André Barbault | 2020–21 全球疫情风险 | 2020–2021 恐有新疫情（negative） | COVID-19，WHO 2020-03-11 宣布大流行（命中） | 《L'Astrologue》第177期，2012 年第一季（2011-06-08 写就） |
| WP-002 | UAC 2008 预测专家组（七人） | 2008 美国大选 | 共识选 Obama 胜（positive） | Obama 胜（命中） | 《华盛顿人报》2008-05-20 当日报道 |
| WP-003 | UAC 2012 预测专家组 | 2012 美国大选 | 一致选 Obama 连任（positive） | Obama 连任（命中） | Astrology News Service 2012 年 5 月会议报道 |
| WP-004 | Edith Hathaway | 2016 美国大选 | 「Clinton 会赢，我给 100%」（positive） | Trump 胜（**落空**） | 《洛杉矶时报》2016 年 10 月 ISAR 会议报道（Prothom Alo 2016-11-08 转载） |
| WP-005 | Aleksandar Imsiragic | 2016 美国大选 | 「Trump 前景不妙」（positive＝Clinton 胜） | Trump 胜（**落空**） | 同上 |
| WP-006 | Jessica Adams | 2016 英国脱欧公投 | 英国将投票离开 EU（positive） | Leave 51.9% 胜（命中；苏格兰独立子断未应） | 本人网站 2015-07-05 首发、2016-02-22 定稿帖 |
| WP-007 | Uversa Oumbajuah（塔罗） | 2016 美国大选 | Trump 将胜、选情极近；选前将爆 Clinton 电邮／基金会负面消息（positive） | Trump 胜；2016-10-28 Comey 信件公开（主断与子断命中；「Trump 任内遇刺」子断落空，已登记） | The Tab 2016-08-26 当期报道（结局前两个多月） |
| WP-008 | Bejan Daruwalla | 2019 印度大选 | 「Modi 会抢尽风头／会赢」（positive） | BJP 303 席，Modi 连任（命中） | ANI 通讯 2019-03-30（投票开始前） |
| WP-009 | Greenstone Lobo | 2019 板球世界杯·印度队 | 「印度队今年拿不了世界杯」（negative） | 印度半决赛出局，英格兰夺冠（命中） | Sportzwiki 2019-04-26（开赛前） |
| WP-010 | Pandit Upendra Shastri | 2020 美国大选 | Biden 星盘更强、将入主白宫（positive） | Biden 胜（命中） | Gulf News 2020-10-28 |
| WP-011 | Acharya Umesh Tiwari | 2020 美国大选 | Trump「将是统治者」、困境将消解（positive） | Trump 落选（**落空**；与 WP-010 同篇对位） | Gulf News 2020-10-28 |
| WP-012 | Pavel Karlin | 2020 美国大选及后续 | 四项断语仅一项应（mixed）：得票最多者错、Biden 终掌总统职对、Biden 病重不久任错、美国将分裂错 | 见左 | Israel Hayom 2020-11-02（选前一日） |
| WP-013 | Jessica Adams | 2024 英国大选 | 「这是工党的胜利」（positive） | 工党 411 席大胜（命中） | 本人 Substack 2024-06-18 帖（其两处年末回顾逐字引述＋2024-05-23 选战专文旁证；原帖本轮未独立复抓，见 cases 内 grade_note，如主持角要求直抓原页可降 B） |

### B 级（3 例，holdout_eligible=false，contamination low）

| id | 大师 | 对象 | 结局来源与定级理由 |
|---|---|---|---|
| WP-014 | Robert Zoller | 1991 纽约楼宇服务工会罢工（卜卦／事件盘） | 结局（1991-04-21 罢工）有独立新闻／劳工史记录；但断语在结局前的时间戳仅靠作者自述「五名见证＋赌局」、首刊于 1993 年期刊——按本轮「时间戳无外部印证至多 B」从严定 B |
| WP-015 | Sharon Knight | 遗失钻石耳环卜卦（Skyscript 案例） | 私人事项，断语与结局均只见于从业者本人发表的案例文，无外部印证 |
| WP-016 | John Frawley | 走失猫卜卦（1998，伦敦） | 同上；另注意本轮可得文本为 2026 年二手转述（Ken Saunders，据 Frawley《The Horary Textbook》2005），非原文逐字，日后晋升须回原书重基 |

## 2. 逐来源普查账

- **世运／选举新闻报道（命中最多）**：LA Times（ISAR 2016）、Washington Times（UAC 2008）、Astrology News Service（UAC 2012）、Gulf News（2020 美国、另有 2019 印度 Kaartik Gor 篇未收，见弃例）、ANI／Business Standard（2019 印度）、Israel Hayom（2020）、Sportzwiki／Asian Age（Lobo 2019）、The Tab（2016 塔罗）。此路的优点是时间戳与结局都可独立分离；缺点是事件皆著名，contamination 一律 high。
- **从业者自有站点（带日期存档）**：Jessica Adams 网站／Substack（Brexit 2015/2016、英国 2024）；The Astrology Podcast 转录 Barbault 2012 期刊原文（法文原刊《L'Astrologue》177 期，属带日期印刷期刊，时间戳最硬）。
- **卜卦案例库 Skyscript**：Zoller 罢工文（《The Traditional Astrologer》1993 转载）、Knight 耳环例、Houlding 主持的 cars.html 论坛例（见弃例）。私人卜卦的结构性上限即 B 级：结局只存在于从业者自述。
- **专著（Frawley／Lehman／Dunn）**：公开渠道仅得 Frawley 猫例的二手转述（收为 B 并标注）；Lehman《The Martial Art of Horary Astrology》、Dunn《Horary Astrology Re-examined》无合法公开全文，本轮查无，登记于弃例，不凑数。
- **塔罗**：本轮只找到 1 例满足「 contemporaneous（同期）发表＋结局可核」的塔罗成例（WP-007）。其余塔罗「预测应验」材料均为事后自述或营销页（如从业者个人站的 validated forecasts 列表），无结局前发表证据，全部弃（见 §3）。

## 3. 弃例登记（主因分类）

1. **时间戳只有事后自述、无结局前发表**（最大宗）：Nicolas Aujula 的 2016 Trump 等「预测」（2018 年后自述）、Kelle Sutliff 2015 Trump 预测（2016-11-11 本人新闻稿回溯）、John Hogue 2016 双向对冲文、Zonkatron 个人站「已验证预测」列表、Greenstone Lobo 2018 法国世界杯冠军（仅 2026 年报道回溯＋赛中含混转帖，无赛前定稿）、Gurmeet Singh 2020 Biden（2021 年自我宣传页回溯）、Adrian Ross Duncan 2020 Biden（播客日期含混、2024 年回溯）。
2. **断语含混／双向对冲、不成可判方向**：Marjorie Orr 2016 美国大选系列（Star4cast，通篇保留两可）、Christeen Skinner 2016（断 Clinton 胜又预埋「就职典礼或有变故」的退路——其主断已由 WP-004/005 同场覆盖，本人单例弃）、Dev Vasishtha 2020 Trump 断（与 WP-011 同篇同向，避免同源三连，弃为同源备选）。
3. **对象／从业者不合口径**：Sally Morgan 2019 皇室婴儿预测（灵媒，非占星／卜卦／塔罗从业者口径，且断语多不可证伪）；Charis Milona 2019 皇室婴儿（只有性格描述、无可判方向断语）；「通灵猫 Phoenix」等动物预测（非从业者）。
4. **专著无公开全文**：Lee Lehman、Barbara Dunn 的卜卦案例集，及 Frawley《The Horary Textbook》原文——公开网络只有书目／节录／二手转述，不登录、不绕付费墙，本轮只收转述可核的猫例（B）并标注重基要求。
5. **金融占星无可核定稿**：Raymond Merriman 年度 Forecast 书的具体断语无公开逐字文本可引（只有书目与访谈泛述），弃。
6. **与既有池重复（三键比对）**：Jessica Adams 的 COVID 疫情／疫苗断（已收 P05/P06）、2024 美国大选的 Prathosh Gopalakrishnan／Jamie Partridge／Kathir Subbiah／HuffPost 专家组（已收 P09–P12）、Kushal Kumar 三战断（P08）——本轮一律回避同大师＋同对象组合；WP-006/013 的 Adams 两例对象分别为 Brexit 与 2024 英国大选，与 P05/P06 三键全异，不重复。masters-dataset/western 的 Lilly AS 系列（16 例）为 17 世纪例，与本路（现代）无交集；phase3 历轮 expansion 的 cases.jsonl 全部为六爻例，无交集。
7. **同篇更优者已收**：Kaartik Gor 2019-05-22 Modi 断（Gulf News，距计票仅一日且与 WP-008 同对象同向，弃，留 WP-008 的选前七周版本）；Seema Midha 等 StarsTell 2019 专家组（团体共识、无个人断语原文，弃）。

## 4. 盲测面自检

- 16 份 `inputs/WP-*.json` 结构照 `inputs6/AS-001.json`：仅 id／subject／context／provenance／language；逐例剔除断语时点之后的信息，不含大师断语与结局。
- 泄漏专项：凡来源标题本身即含断语或结局者（WP-002/007/009/012/014），inputs 内 provenance 已改为中性出处（媒体＋日期），完整标题只留在 cases.jsonl 的金标面。
- 卜卦三例的 attachments 只保留盘面数据（宫位／星体位置／起卦时地），判断性语句未进入盲测面（WP-016 仅注六宫取象规则）。

## 5. 质量风险（给主持角）

1. **contamination 结构性偏高**：A 级 13 例全部 high（著名公共事件）。本路的价值在「时间戳硬＋结局独立＋含 4 例明确落空与 1 例 mixed」的方法学对照，不在低污染；若 holdout 需要 low 污染，须靠其他传统门类一路补，本路 B 级三例为 low 但按规矩不进 holdout。
2. **WP-013 时间戳为作者自引**：已在 grade_note 写明降级条件，主持角可裁。
3. **WP-016 为二手转述**：晋升或引用前须回 Frawley 原书重基。
4. **选举类断语密度高**（13 例 A 中 10 例为选举／公投）：体系多样性有限——这是「带时间戳＋结局独立」双硬约束下公开来源的真实分布，如实报告。

## 6. 与待外部补源登记的关系

- 本路扩数不等外部补源、先行推进；缺全文古籍清单 `~/workspace/divination/WANTED-TEXTS.md` 已交用户经学校数据库查找、登记为「待外部补源」（见 `benchmark/iterations.md` 2026-10-29 登记条目）。用户后续发来清单中任一书全文时，由数据角按既有流程优先处理入池。
