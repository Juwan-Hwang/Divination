# inputs10 BUILD-REPORT（LY-6xx 组）— C 轨输入补录（数据角，2026-10-30）

范围：inputs9 普查待补 44 例中的 LY-601–625 共 **25 例**（差集，见下）全量补录 ＋ LY-036 变卦名冲突 **1 例裁决版**，合计产出 **26 个 inputs10 文件**。仅新建 inputs10/ 下文件；inputs8、inputs9、roster、method、runs 未动一字；原书只读（维基文库本在线读、校正全本 PDF 仅 pdftoppm 渲染至 /tmp 读图）。体例与分级口径承 inputs9 BUILD-REPORT：直载＝原书明载；推算复原＝由已载卦名/动爻/日期以标准纳甲确定性推得；不可补＝保持 null 并注明已查何处。本报告为本批全部文字产出之一（另一为各文件 notes.completion_grade；LY-036 另有 notes.adjudication）。

## 差集清单（定法与结果）

- 定法：LY-601–LY-625 全集（25 例）与 inputs9/ 目录文件清单作差集。inputs9 共 49 个文件（47 例补录＋BUILD-REPORT＋ERRATA），其中 LY-6xx 仅 LY-626、LY-627、LY-628、LY-629 四例，不在 601–625 段内。
- 结果：**差集＝25 例全量**：LY-601、LY-602、LY-603、LY-604、LY-605、LY-606、LY-607、LY-608、LY-609、LY-610、LY-611、LY-612、LY-613、LY-614、LY-615、LY-616、LY-617、LY-618、LY-619、LY-620、LY-621、LY-622、LY-623、LY-624、LY-625，无一已被 inputs9 覆盖。本批 25 例全部产出补录文件。

## 方法

1. **回原出处**：25 例来源均为《增删卜易》维基文库本（录入者整理本），逐例按 inputs8 provenance.page 所注章次回该本渲染页定位例首与装卦表（本地 sources/chinese/zengshan-buyi-wikisource.txt 卷一只存转录占位符、无章内正文，故以同一维基文库本在线渲染页为据，与 inputs8 建档出处一致）。
2. **装卦复核引擎**：承 inputs9 法写标准纳甲推算程序（定宫、纳甲地支、世应、六亲配本宫五行、本变卦爻象差定动爻、旬空、伏神）。先对本批 23 例 inputs8 既有逐爻表做反验：**23/23 逐爻全合**（含六亲、地支、爻象、世应、动爻记号、变卦栏）；引擎可信后才用于 palace/kongwang/hidden_lines 推算与 LY-620/621 全盘推算复原。
3. **逐例核对**：25 例例首（月日、占题、本变卦名）与出处原文逐字核对全合；23 例既有逐爻表与原书装卦表逐行核对全合，未改动一字。LY-606 例首作「同日」，承前例 LY-605「卯月戊寅日」，与 inputs8 asked_at 一致，已在该例 completion_grade 注明。
4. **补入字段口径**（与 inputs9 补 LY-626–629 同法）：palace 由本卦按标准八宫定宫（推算复原，原书未标宫名）；kongwang 由直载日干支按旬空规则推得（推算复原）；date_ganzhi 照例首直载另立盘面日期键（与 asked_at 同值）；moving_lines 自原书装卦表动爻记号直载并经爻象差复核（静卦 4 例作「無動爻（靜卦）」）；hidden_lines 仅在本卦六亲缺一味且本宫首卦取位唯一时按伏神规则推算复原（11 例），缺两味者取位不唯一、不补（3 例，同 inputs9 LY-307 先例），六亲俱全者无伏神（11 例）。

## 逐例表

| case_id | 來源章 | 例首月日 | 本卦→變卦 | 補入字段（分級） | 伏神 |
|---|---|---|---|---|---|
| LY-601 | 卷之一·用神元神忌神仇神章第九 | 辰月戊申日 | 乾爲天→風天小畜 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改） | —（六親俱全，無伏神） |
| LY-602 | 卷之一·元神忌神衰旺章第十 | 酉月辛亥日 | 兌爲澤→雷水解 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改） | —（六親俱全，無伏神） |
| LY-603 | 卷之一·元神忌神衰旺章第十 | 巳月乙未日 | 澤風大過→火風鼎 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改） | —（缺兄弟、子孫兩味，取位不唯一，未補，同 inputs9 LY-307 先例） |
| LY-604 | 卷之一·五行相生章第十一 | 卯月己卯日 | 地雷復→震爲雷 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改）、hidden_lines 推算復原 | 二爻官鬼寅木下伏父母巳火 |
| LY-605 | 卷之一·五行相克章第十二 | 卯月戊寅日 | 澤地萃→天火同人 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改） | —（六親俱全，無伏神） |
| LY-606 | 卷之一·克處逢生章第十三 | 卯月戊寅日 | 天地否→天水訟 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改）、hidden_lines 推算復原 | 初爻父母未土下伏子孫子水 |
| LY-607 | 卷之一·克處逢生章第十三 | 辰月丙申日 | 水火既濟→澤火革 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改）、hidden_lines 推算復原 | 三爻兄弟亥水下伏妻財午火 |
| LY-608 | 卷之一·月將章第十六 | 寅月庚戌日 | 火天大有→（靜卦） | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改） | —（六親俱全，無伏神） |
| LY-609 | 卷之一·月將章第十六 | 酉月丙寅日 | 山風蠱→山水蒙 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改）、hidden_lines 推算復原 | 五爻父母子水下伏子孫巳火 |
| LY-610 | 卷之一·月將章第十六 | 寅月丙申日 | 艮爲山→山雷頤 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改） | —（六親俱全，無伏神） |
| LY-611 | 卷之一·月將章第十六 | 午月丁未日 | 澤水困→雷風恆 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改） | —（六親俱全，無伏神） |
| LY-612 | 卷之一·月將章第十六 | 寅月丁酉日 | 艮爲山→地火明夷 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改） | —（六親俱全，無伏神） |
| LY-613 | 卷之一·月將章第十六 | 午月戊辰日 | 火地晉→（靜卦） | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改）、hidden_lines 推算復原 | 初爻父母未土下伏子孫子水 |
| LY-614 | 卷之一·六神章第十八 | 申月甲辰日 | 水雷屯→震爲雷 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改）、hidden_lines 推算復原 | 三爻官鬼辰土下伏妻財午火 |
| LY-615 | 卷之一·六合章第十九 | 申月丙子日 | 地火明夷→雷山小過 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改）、hidden_lines 推算復原 | 三爻兄弟亥水下伏妻財午火 |
| LY-616 | 卷之一·六合章第十九 | 卯月丁巳日 | 離爲火→坤爲地 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改） | —（六親俱全，無伏神） |
| LY-617 | 卷之一·六沖章第二十 | 午月丙辰日 | 雷風恆→雷地豫 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改）、hidden_lines 推算復原 | 二爻父母亥水下伏兄弟寅木 |
| LY-618 | 卷之一·六沖章第二十 | 酉月乙未日 | 坤爲地→（靜卦） | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改） | —（六親俱全，無伏神） |
| LY-619 | 卷之一·動散章第二十三 | 丑月丁酉日 | 風水渙→坎爲水 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改） | —（缺官鬼、妻財兩味，取位不唯一，未補，同 inputs9 LY-307 先例） |
| LY-620 | 卷之一·卦變生克墓絕章第二十四 | 卯月辛巳日 | 巽爲風→乾爲天 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 推算复原、chart_lines 推算复原（原空表填入） | —（六親俱全，無伏神） |
| LY-621 | 卷之一·卦變生克墓絕章第二十四 | 午月丙寅日 | 離爲火→坎爲水 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 推算复原、chart_lines 推算复原（原空表填入） | —（六親俱全，無伏神） |
| LY-622 | 卷之一·反伏章第二十五 | 卯月己亥日 | 地澤臨→風澤中孚 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改） | —（六親俱全，無伏神） |
| LY-623 | 卷之一·反伏章第二十五 | 申月癸巳日 | 天風姤→雷風恆 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改）、hidden_lines 推算復原 | 二爻子孫亥水下伏妻財寅木 |
| LY-624 | 卷之一·旬空章第二十六 | 辰月乙卯日 | 風火家人→山火賁 | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改）、hidden_lines 推算復原 | 三爻父母亥水下伏官鬼酉金 |
| LY-625 | 卷之一·旬空章第二十六 | 子月辛亥日 | 山天大畜→（靜卦） | palace 推算復原、kongwang 推算復原、date_ganzhi 直载、moving_lines 直载、chart_lines 直载（既有表回原書逐行核對一致、未改） | —（缺父母、子孫兩味，取位不唯一，未補，同 inputs9 LY-307 先例） |

注：各例 moving_lines 全文见各文件；分级分布（25 例＋LY-036 按字段条目计）：直载 74 条、推算复原 65 条、不可补 0 条（本批无保持 null 的盘面字段；「未补」仅伏神双缺 3 例与 LY-614 六神，见存疑）。

## 存疑与未补项（数据角只标示、不臆补）

1. **LY-620 / LY-621 chart_lines 系推算复原**：原书两例均为正文叙述体，仅载月日与本变卦名（巽之乾、離之坎），维基文库本无装卦表；已查同本同章（卷之一·卦变生克墓绝章第二十四）全段，确无逐爻表。两例 palace/kongwang 在 inputs8 原为「原文未記」占位值，本批按补录本身改值填实（同 inputs9 YY2-003 null 填实例），既有 chart_note「逐爻表不錄」与 moving_lines_text「原文未記」按原件不回改纪律保留未动，与新补字段的口径差异已写入两例 completion_grade 的 scope_note，提请主持角知悉。
2. **伏神双缺 3 例未补 hidden_lines**：LY-603（缺兄弟、子孙）、LY-619（缺官鬼、妻财）、LY-625（缺父母、子孙）两味同缺，伏神取位不唯一，保持不补（同 inputs9 出入 7 先例）。
3. **LY-614 六神未录**：原书（六神章第十八）装卦表逐爻另载六神（自上爻起：元武、白虎、勾陈、媵蛇、朱雀、靑龙），inputs8 既有表未录、本批按 inputs9 字段体例未新增六神字段，仅在此标示；六神可由日干支（甲辰日）按起例推得，如后续轮次需要可再补。
4. **LY-624 再占未入**：原书同例再占「暌之損」装卦表在出处原文紧随其后，inputs8 本条只收首占（家人之賁），本批维持原收录范围未扩。
5. **LY-622 与 LY-036 同盘异书**：LY-622（《增删卜易》，卯月己亥日）与 LY-036 裁决所据《卜筮正宗》例034（卯月乙亥日）同为临之中孚、逐爻全合，惟日干支不同，系两书两例，本批分别按各自出处处理，未混同。

## LY-036 裁决（变卦名冲突）

- **冲突**：inputs8 作「地澤臨之風澤中孚（坤宮，空亡申酉）」；inputs9 BUILD-REPORT 出入 6 称原书例034 为「临之升卦（地風升）」，据此将 LY-036 列待补待裁。
- **裁决结论：可裁——以《卜筮正宗》校正全本例034 例首与逐爻表为准，本卦地泽临、变卦风泽中孚；inputs8 既有变卦名无误，「地風升」说与校正全本不合。** inputs10/LY-036.json 为裁决版：既有字段一字未改，仅补入例034 逐爻表、动爻、日期与空亡，并附 notes.adjudication 全文。inputs8 与 inputs9 报告均未回改。
- **证据**：
  1. 校正全本（四库存目纳甲汇刊2）卷十三·第五问（反吟）附占验例034，书页210（PDF页225）例首明载：「034 卯月乙亥日，占升選。得臨之中孚卦。」
  2. 同例装卦表逐爻（自上而下）：子孙酉金×化卯、妻财亥水×（应）化巳、兄弟丑土、兄弟丑土、官鬼卯木（世）、父母巳火。上、五两爻阴动变阳，地泽临恰变为风泽中孚——逐爻表与变卦名互证。
  3. 内证一：乙亥日属甲戌旬、旬空申酉，与 inputs8 卦名括注「空亡申酉」合。
  4. 内证二：临为坤宫二世、世在二爻官鬼卯木，与 inputs8 既有 yongshen「世爻卯木、官星为用」合（仅据盘面世位，不涉断语与应验）。
  5. 旁证：《增删卜易》卷之一·反伏章第二十五另载同题同盘一例（卯月己亥日占升迁，得临变中孚，逐爻与例034 全合），证「临之中孚」一型装卦于同时代卜书实有其例；日干支不同，属另一书另一例，不混同。
  6. 「地風升」之来源：本角在校正全本第五问全段（书页210 前后）未觅得任何「临之升」例；其或出在线本转录/转引之误，本角证据不足以断定来源，仅登记「与校正全本不合」，不臆断。
- **补录分级**：chart_lines_top_to_bottom 直载（变卦栏非动爻行由变卦纳甲推得部分属推算复原，已逐项注明）；moving_lines 直载；date_ganzhi 直载（「卯月乙亥日」，inputs8 asked_at 原作月名未记系在线本漏录）；空亡 推算复原（乙亥→申酉，与括注互证）。

## 泄漏扫描（必查项）

- 方法一（结构 diff）：对 26 例逐一做 inputs8↔inputs10 递归字段 diff。结果：**变更只落在盘面字段（context.hexagram 或 LY-036 的 context.attachments）的新增键与 notes.completion_grade（LY-036 另加 notes.adjudication）**；零删除；题面（subject/context.question/setting/asked_at 等）与一切既有字段一字未改。唯二「改值」为 LY-620/621 的 palace、kongwang 由占位值「原文未記」填实（即补录本身，已逐项注明）。
- 方法二（结局词扫描）：以 inputs9 同词表（去世、死于、卒于、痊愈、果验、应验、后来、得财等）扫全部新增盘面字符串与 completion_grade/adjudication 文本：**零命中**。扩展词表另检出 3 处，均为占题本身用词（LY-618 例首「生死如何」、LY-623 例首「平安」，本已载于 inputs8 题面，非结局/断语文本），不构成泄漏。各例断语与应验文字一概未引；LY-036 证据 4 仅引原书对盘面世位的载述，同 inputs9 对 YY2-003 的处理口径。
- 结论：inputs10 不含任何大师断语/应验结局文本，可安全用作盲测输入。

## 纪律核对

- 只新建 inputs10/ 下 27 个文件（26 例 JSON＋本报告）；inputs8、inputs9、roster、method、runs、incoming 未动一字；未 git commit。
- 不作断、不评分：本批无任何预测与分数产出；LY-036 裁决只裁盘面事实（卦名与逐爻表），不涉断语对错。
- 补不到保持原状并注明已查何处：伏神双缺 3 例、LY-614 六神、「地風升」来源 1 项，均已登记如上，无臆补。
