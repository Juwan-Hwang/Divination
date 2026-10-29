# LEAK-CLEANUP-ERRATA — Phase 3 輸入面泄漏清理登記（數據角）

日期：2026-10-29。觸發：主持角抽查裁定（Round 1 評分開始前必須完成）。執行範圍：三路 expansion 的 `inputs.jsonl`、zengshan 的 `build_cases.py`（setting/comment 同步，防再生）、`benchmark/phase3/inputs/` 與 `benchmark/phase3/holdout3-inputs/` 中對應新案例 packet（LY-2xx、LY-3xx、AS-2xx）。dev2 沿用例不在範圍，未動。

清理規則（照主持角硬性口徑）：inputs 側只保留占問當時已知事實（何人、何時占、問何事、卦象/盤面、求測者當時處境事實）；刪除大師斷語、斷語摘要、由斷語反推的應期/日期引文、「初斷/再占之斷」的內容（再占事實本身保留）；asked_at 若原為據斷語推得，改記「原文未明記」或只保留原文直書/占時事實的月日；setting 改寫為純事實敘事，改寫依據只取原 setting 中斷語之前的事實敘事成分，不新編事實。被刪的盤面描述（旺衰、沖合、生克）在 attachments 的裝卦/卦名/動爻欄位中完整保留，無資訊損失。

標記口徑：**substantive**＝刪去了斷語/應期/結果內容；**cosmetic**＝僅刪去與 attachments 重複的盤面描述、無內容的出處引文形式，或格式調整，未刪任何斷語內容。形態：(a) zengshan setting/comment 混入斷語；(b) bushi asked_at 引斷語應期；(c) lilly 英文字段混入斷語措辭。

金標側一字未動（清理前後 SHA-256 核對一致）：expansion 三路 answers.jsonl、data/dev-new-answers.jsonl、holdout3/test_gold.jsonl。

## 一、zengshan 路（《增刪卜易》，LY-201–259，共 59 例逐例人讀 setting + notes.comment）

### 1a. setting 修訂

| id | 形態 | 改前關鍵句 | 改後 setting | 標記 |
|---|---|---|---|---|
| LY-201 | — | （原文即純事實：問終身財福；丑年占卦） | 未改 | 未改（復查結論：無斷語成分） |
| LY-202 | a | 求測者在庠，因家寒意欲行醫，問財福如何；野鶴見卦中官父兩旺，反斷其將來成名 | 求測者在庠，因家寒意欲行醫，問財福如何 | substantive |
| LY-203 | a | 問財福；世臨白虎化出旺財生世，其人目不識丁、農生度日 | 其人目不識丁、農生度日，問財福 | cosmetic |
| LY-204 | a | 生意人占財福，野鶴以前卦財生官旺勸其問名，命再占合斷 | 生意人先占財福，後再占問功名出仕 | substantive |
| LY-205 | a | 問終身財福，自言功名之念已滅；野鶴見官父兩旺，反斷其顯貴中舉 | 問終身財福，自言功名之念已滅 | substantive |
| LY-206 | a | 問終身財福；世與日月三合，外卦以為吉，野鶴獨斷世爻變鬼化回頭克，須防不測 | 問終身財福 | substantive |
| LY-207 | — | （原文即純事實：求測者原是武蔭、已任裨官，因病告退，問將來還有功名否） | 未改 | 未改（復查結論：無斷語成分） |
| LY-208 | a | 問終身功名有無；日月作財生世，白虎臨金官持世，野鶴斷入武途可以立功 | 問終身功名有無 | substantive |
| LY-209 | a | 壽元章占例，問公之壽；卦中多鬼搖發 | 壽元章占例，問公之壽 | cosmetic |
| LY-210 | a | 問壽元；世爻未土月拱日克，巳火動而生世 | 問壽元 | cosmetic |
| LY-211 | a | 問壽元；世化申金回頭生，戌土未土動而克世 | 問壽元 | cosmetic |
| LY-212 | a | 漢口；求測者欲渡江索債，因屢取不得欲與之廝鬧，野鶴見卦斷辰時出空被克必有危亡之禍，苦留之過辰時 | 漢口；求測者欲渡江索債，因屢取不得欲與之廝鬧 | substantive |
| LY-213 | a | 求測者夢一身之血入河洗之，占其兆；野鶴斷破財兼防木害，勸出外避、勿貪幼婦，其人以年歲逼未能遠去 | 求測者夢一身之血，入河洗之，占其兆 | substantive |
| LY-214 | a | 占防患，前後三占：初占、再占世臨子孫值旬空，斷事不結、反覆；三占乃斷結期 | 占防患，前後三占 | substantive |
| LY-215 | a | 問流年吉凶；野鶴斷今秋險厄、宜往外避 | 問流年吉凶 | substantive |
| LY-216 | a | 此公知僕役變心、意欲處治而尚無實迹，故占之；野鶴斷另有附從者，勸其出外自能免禍 | 此公知僕役變心、意欲處治而尚無實迹，故占之 | substantive |
| LY-217 | a | 問已定何罪；木鬼臨白虎，世臨月建 | 問已定何罪 | cosmetic |
| LY-218 | a | 同日分占父母壽元：先占父壽得姤，又占母壽得大壯之升；三十餘載後復遇其人核驗 | 同日分占父母壽元：先占父壽，又占母壽 | cosmetic |
| LY-219 | a | 問父親壽元；亥水父臨月破又被未土相傷 | 問父親壽元 | cosmetic |
| LY-220 | a | 問兄弟和好與得濟否；弟兄臨月建，未土爻動相生又化出兄爻 | 問兄弟和好與得濟否 | cosmetic |
| LY-221 | a | 問夫妻能否偕老；滿盤俱是財爻，世爻變出之未土與世相合為正妻 | 問夫妻能否偕老 | cosmetic |
| LY-222 | a | 求測者三十七歲有子、已十八，因亂失散，至今無所出，問子嗣；野鶴斷失散之子將歸 | 求測者三十七歲有子、已十八，因亂失散，至今無所出，問子嗣 | substantive |
| LY-223 | a | 問子是否易養；亥水子孫臨月建、兄動相生，表面極旺，野鶴獨斷子爻變鬼主凶 | 問子是否易養 | substantive |
| LY-224 | a | 問本經能否發達，初占斷宜改經；再占易經又斷宜再更；三占書經，斷此經相宜、下科高發 | 問本經能否發達，前後三占：初占本經、再占易經、三占書經 | substantive |
| LY-225 | a | 為子占從師可否；子孫動而化克，野鶴斷不宜從之，求測者不聽 | 為子占從此師可否 | substantive |
| LY-226 | a | 問會試能否及第；寅木旺官持世，申日沖之為暗動，日辰會成財局生世 | 問會試能否及第 | cosmetic |
| LY-227 | a | 問鄉試；初占得兌卦六沖，世父皆旺，野鶴不敢決之命再占，再占官星持世、父旺，與前卦相合乃許吉 | 問鄉試，前後兩占 | substantive |
| LY-228 | a | 問能否得差；子孫持世且世爻旬空，初斷不得 | 問能否得差 | substantive |
| LY-229 | a | 問升遷；卯木旺官持世，子水財動相生 | 問升遷 | cosmetic |
| LY-230 | a | 問何日補官；寅木財爻生助午火官鬼克世，為助鬼傷身之象，幸辰土生申金、午火貪生忘克 | 問何日補官 | substantive |
| LY-231 | a | 在任者占流年平安，自憂世爻變鬼；野鶴斷自身不妨、須防孝服 | 在任者占流年平安，自憂世爻變鬼 | substantive |
| LY-232 | a | 出具文書伸冤以保全功名；父母持世、月建文書生旺，唯子孫申金動而傷官 | 出具文書伸冤，問能否保全功名 | cosmetic |
| LY-233 | a | 占者先經占會試許之必中，又問可能鼎甲否，指其事而占；野鶴斷中鼎甲但非今科 | 會試後指占，問可能鼎甲否 | substantive |
| LY-234 | a | 子占父何時起用；內卦寅木父母旺而化出子水之官 | 子占父何時起用 | cosmetic |
| LY-235 | a | 問借貸能否得財；兄爻持世、卦中無財，唯卯日即是財星、應爻未土旺而生世 | 問借貸能否得財 | cosmetic |
| LY-236 | a | 問求財；野鶴分斷久遠之財無、目下之財明日必得 | 問求財 | substantive |
| LY-237 | a | 出行謁見貴人，問能否得見；官星持世而旬空 | 出行謁見貴人，問能否得見 | cosmetic |
| LY-238 | a | 囤貨問何時得價；卯木財爻得子月生而有根，目下被申金動而克制 | 囤貨，問何時得價 | cosmetic |
| LY-239 | a | 問貨於何時可脫；亥水財爻得酉日生、寅月合，求測者聞某處得價欲移貨往賣，野鶴勸速行 | 問貨於何時可脫；求測者聞某處得價，欲移貨往賣 | substantive |
| LY-240 | a | 問借貸；卯木財爻化退、酉金兄動亦化退，幸財臨日辰旺而不退 | 問借貸 | substantive |
| LY-241 | a | 以鵪鶉相鬥占勝負；子孫持世臨日辰，父爻動而化亥水制之，唯亥水月破 | 以鵪鶉相鬥，占勝負 | cosmetic |
| LY-242 | a | 男子自占婚；酉官持世，戌土財爻動而生世，世應相生 | 男子自占婚 | cosmetic |
| LY-243 | a | 女家代占男；卯木旺官持世主婚成，然財爻被回頭克又逢丑土之克，不能生官 | 女家代占婚 | substantive |
| LY-244 | a | 女占夫、夫妻不和，問將來如何；子孫持世為克夫之象，應爻為夫而逢子丑作合 | 女占夫、夫妻不和，問將來如何 | substantive |
| LY-245 | a | 求測者妾多無子，問何命之女能有子；野鶴斷其命元無子、與女命無干，勸多積陰德，兼看八字同斷無子 | 求測者妾多無子，問何命之女能有子 | substantive |
| LY-246 | a | 問妻孕平安兼孕之男女；野鶴先正分占之法，幸此卦兩事俱現 | 問妻孕平安，兼問孕之男女 | cosmetic |
| LY-247 | a | 問僕人何日回；此卦若問在外吉凶主不歸，今問歸期則以世空速至斷之 | 問僕人何日回 | substantive |
| LY-248 | a | 問伯父何日來；父母為用神而克世，初斷七月必到 | 問伯父何日來 | substantive |
| LY-249 | a | 問遠行之父何日回；占日即午日，午火父爻克世 | 問遠行之父何日回 | cosmetic |
| LY-250 | a | 妻占夫在外是否還往他省；官為用神被申金動克，日月生扶夫爻 | 妻占夫在外，問是否還往他省去、兼問何日到 | cosmetic |
| LY-251 | a | 問子近病；官鬼酉金動而變子孫午火，本為夭折之兆，幸子孫值旬空 | 問子近病 | substantive |
| LY-252 | a | 問子病；官鬼午火持世為憂疑之象，子日沖去憂心 | 問子病 | cosmetic |
| LY-253 | — | （原文即純事實：府中老先生仆倒狂言不知人事，醫者議用人參提氣，又慮痰上難治，子占父病問喫人參好否） | 未改 | 未改（復查結論：無斷語成分） |
| LY-254 | a | 患楊梅瘡，問某醫可用否；子孫申金持世而應爻卯木、巳火克世，求測者不聽仍延此醫 | 患楊梅瘡，問某醫可用否 | substantive |
| LY-255 | a | 一官連任不得升遷疑衙宇不利，諸所疑俱占不現爻，又卜後溝從後流宜否；初占斷即此處不宜、宜改東流，再占修溝後功名 | 一官連任不得升遷，疑衙宇不利；占衙宇後溝從後流宜否，又再占修溝之後何如 | substantive |
| LY-256 | a | 占墳地可用否；世爻戌土春休囚，化出午火子孫回頭生世，日月世爻成三合 | 占墳地可用否 | cosmetic |
| LY-257 | a | 占墳地可用否；世臨月建日辰生本為吉，唯外卦反吟、世與子孫俱受沖克，野鶴斷不宜用，地主已買成仍葬之 | 占墳地可用否 | substantive |
| LY-258 | a | 此地屢掘逢石無處導穴，央野鶴到冢下點穴；世在四爻斷穴在中段、午火持世斷枯焦紅花處，設灑錢禱告之法驗之 | 此地屢掘逢石，無處導穴，央野鶴到冢下點穴 | substantive |
| LY-259 | a | 問以父柩附葬祖塋可否；世爻子水被克，斷不宜附葬，求測者仍附葬之 | 問以父柩附葬祖塋可否 | substantive |

### 1b. notes.comment 修訂（comment 位於 inputs.jsonl 內、同屬輸入面；packet 文件不含 comment）

| id | 形態 | 改前關鍵句 | 改後 comment | 標記 |
|---|---|---|---|---|
| LY-203 | a | 斷語與應驗同段敘述，節錄以占時沖克之理為斷、子年災變為驗 | 原文斷語與應驗同段敘述，詳見金標側 | substantive |
| LY-208 | a | 應驗時點為「不出五載」的 bounded 記載 | （空） | substantive |
| LY-210 | a | 斷語原指亥年不利，實際卒於戌年，原文自釋為應在巳火入墓之年——斷驗年份不合之例如實收錄，不迴避 | 斷驗年份不合之例，原文有自釋，詳見金標側 | substantive |
| LY-212 | a | 趨避例：本人因被留而倖免，應驗為當日江船覆沒事件；裝卦初爻原文有缺字符號，照錄 | 裝卦初爻原文有缺字符號，照錄 | substantive |
| LY-218 | a | 應驗中「子年」承斷語丙子年 | （空） | substantive |
| LY-228 | a | 本例初斷與結果表面相反，原文隨即自釋（子孫未出空故得差、世空故中途死），斷語與自釋一併節錄、如實收錄 | 本例初斷與結果表面相反，原文有自釋，詳見金標側 | substantive |
| LY-234 | a | 應驗主句為「果應於寅年」；同段另記「後終於未年」為次級應驗，一併見於原文 3337 行 | 應驗詳見金標側（原文 3337 行） | substantive |
| LY-240 | a | 原文應驗句止於「果於辰日」，句似未完，照錄不補 | 原文應驗句句似未完，照錄不補（內容見金標側） | substantive |
| LY-245 | a | 斷驗關係特殊：大師斷無子，求測者嗣後行善積德而連生二子，原文以陰功釋其轉變——斷語、勸善與結果俱為原文自載，如實收錄並標 mixed | 本例斷驗關係特殊，詳見金標側 | substantive |
| LY-248 | a | 斷語原指七月必到，實際亥月方到——斷驗月份不合之例如實收錄，原文自釋附於斷語節錄 | 本例斷驗月份不合，原文有自釋，詳見金標側 | substantive |
| LY-251 | a | 應驗分兩段：近病果在出空之日而愈（主應驗）；原文同句續記「辰年占卦至午年出花而死」為遠期應驗，一併見於原文 3967 行 | 應驗分近、遠兩段，詳見金標側（原文 3967 行） | substantive |
| LY-254 | a | 應驗分兩段：巳日變癥、服解藥至申日其病如常，俱見原文 4152 行 | 應驗分兩段，詳見金標側（原文 4152 行） | substantive |
| LY-255 | a | 初占應驗「後開溝見許多屍體白骨」見原文 4336 行；再占斷未年高升、實際申年升任，原文自釋「應申年者，值官之年也」——斷驗年份不合之例如實收錄 | 本例斷驗年份不合，原文有自釋，詳見金標側（初占應驗見原文 4336 行） | substantive |
| LY-258 | a | 原文同段另記即時應驗「果得原錢於紅花之下，掘之周圍僅有丈予，皆泥土也，予皆石塊」（「丈予」「予皆」疑為「丈餘」「餘皆」之訛，照錄），outcome 取其遠期應驗句 | 原文「丈予」「予皆」疑為「丈餘」「餘皆」之訛，照錄；原文同段另記即時應驗，outcome 取其遠期應驗句，詳見金標側 | substantive |
| LY-259 | a | 原文應驗段「數月後不斷曰﹕腰疼欲死」語意欠通，疑有訛字，照錄；outcome 為原文 4511 行應驗全段 | 原文應驗段有語意欠通處，疑有訛字，照錄；outcome 為原文 4511 行應驗全段 | substantive |

其餘 zengshan 各例 comment 逐例人讀結論：LY-202、211、214、217、220、222、224、225、227、230、231、233、235、246、247、253 等含 comment 者均為卦名推定/裝卦訂正/訛字/占題出處等校勘說明，無斷語與應驗內容，未改；其中 LY-209 的「據…斷語「公之壽」補題」、LY-214/224/227 的「斷語見原文 X 行」、LY-247 的「斷語全句見原文 3866 行前段…巳火又是財爻」均屬只指出處、不引斷語內容類，照主持角口徑不算泄漏。LY-240 的 comment 原引應驗句片段「果於辰日」，屬應期內容，已按 substantive 併入 1b（其原 comment 同步於 build_cases.py 一併改）。

## 二、bushi 路（《卜筮正宗》，LY-301–320，共 20 例逐例人讀 asked_at + setting）

setting 20 例逐例人讀結論：全為問題與求測者處境事實（如 LY-301「人在客外，為在家之妻占安否」、LY-313「仆逃走並盜去財物，問能否拿獲」——「拿獲」為問題本身用字），無一例含斷語，全部未改。修訂全在 asked_at：

| id | 形態 | 改前 asked_at | 改後 asked_at | 標記 |
|---|---|---|---|---|
| LY-301 | b | 原文未明記月日（斷語稱目下寅卯皆克、交辰月） | 原文未明記月日 | substantive |
| LY-302 | b | 戌日（據斷語「戌日沖之」；月建原文未明記） | 戌日（月建原文未明記） | cosmetic |
| LY-303 | b | 原文未明記月日（應期己巳日，據斷語） | 原文未明記月日 | substantive |
| LY-304 | b | 原文未明記占日（斷語以次日甲寅為應期） | 原文未明記月日 | substantive |
| LY-305 | b | 原文未明記月日（旬空申酉；危期乙酉日，據斷語） | 原文未明記月日 | substantive |
| LY-306 | b | 原文未明記月日（空亡寅卯；初斷庚申可見） | 原文未明記月日 | substantive |
| LY-307 | b | 未月（據斷語「月建未土父母爻」；日辰原文未明記） | 未月（日辰原文未明記） | cosmetic |
| LY-308 | b | 原文未明記月日（日辰辰土，據斷語；初斷在甲寅旬乙卯日） | 原文未明記月日 | substantive |
| LY-309 | b | 原文未明記月日（空亡午未；斷應巳年） | 原文未明記月日 | substantive |
| LY-310 | b | 原文未明記月日（空亡午未；斷卯日得信、未日歸） | 原文未明記月日 | substantive |
| LY-311 | — | 原文未明記月日（空亡辰巳） | 未改 | 未改（復查結論：括號內僅空亡盤面事實或原文明記日期，無斷語內容） |
| LY-312 | b | 原文未明記月日（空亡午未；月建生世，據斷語） | 原文未明記月日（空亡午未） | cosmetic |
| LY-313 | b | 原文未明記月日（空亡子丑；斷許甲子日拿獲） | 原文未明記月日 | substantive |
| LY-314 | — | 第一例原文未明記月日；同卦再驗例為七月庚辰日（原文明記） | 未改 | 未改（復查結論：括號內僅空亡盤面事實或原文明記日期，無斷語內容） |
| LY-315 | b | 原文未明記月日（空亡辰巳；斷今秋、次歲辰年） | 原文未明記月日 | substantive |
| LY-316 | b | 原文未明記月日（空亡寅卯；斷後至寅年卯月） | 原文未明記月日 | substantive |
| LY-317 | b | 寅月、申日（據斷語「月建寅，日建申」） | 寅月、申日 | cosmetic |
| LY-318 | b | 原文未明記月日（空亡辰巳；斷辰月建可見） | 原文未明記月日 | substantive |
| LY-319 | b | 未月（據斷語「未土月建為用」；應期甲辰日） | 未月（日辰原文未明記） | substantive |
| LY-320 | b | 卯年（據斷語「今歲是卯年」；月日原文未明記） | 卯年（月日原文未明記） | cosmetic |

說明：substantive 各例刪去的均為斷語應期原文（LY-301 交辰月危期、LY-303 己巳日、LY-304 次日甲寅、LY-305 乙酉日危期、LY-306 初斷庚申可見、LY-308 初斷乙卯日、LY-309 斷應巳年、LY-310 卯日得信未日歸、LY-313 甲子日拿獲、LY-315 今秋/次歲辰年、LY-316 寅年卯月、LY-318 辰月建可見、LY-319 應期甲辰日）。cosmetic 各例（LY-302、307、312、317、320）原括號內僅為占時盤面事實（日辰/月建/年份）的斷語出處引文形式，無應期與結果內容；改後保留占時事實本身、刪引文形式，其中被刪的空亡資訊在 attachments 卦名欄中原樣保留。LY-302、LY-303 為 B 級未入池案例，同樣照單清理。attachments 的 chart_note 為主持角明示不算泄漏的固定說明句，未動；yongshen 為盤面用神設定，未動。

## 三、lilly 路（Christian Astrology，AS-201–215，共 15 例逐例人讀 subject.background / moment / notes）

| id | 形態 | 欄位 | 改前關鍵句 | 改後 | 標記 |
|---|---|---|---|---|---|
| AS-205 | c | subject.background | …Lilly judged both the disease and the event, and persuaded the man to settle his affairs. | A sickness question on the figure of 16 July 1645. | substantive（「persuaded…to settle his affairs」是 Lilly 據死斷採取的行動，直接洩露生死方向與處置） |
| AS-214 | c | subject.background | …she asked when he should be delivered, and was told she need make no friends for his delivery. | Her husband was imprisoned (in a garrison, in time of war); she asked when he should be delivered. | substantive（「was told she need make no friends」為 Lilly 斷語/勸告原文，洩露獲釋方向；此例為逐例人讀新發現，不在主持角原抽查名單） |
| AS-209 | c | subject.moment | Not stated in the chapter; the figure precedes the crossing of 11 April 1643 referred to in the judgment. | Not stated in the chapter. | substantive（11 April 1643 crossing 為斷語中的事件日期，屬應期類內容） |
| AS-209 | c | notes.ocr_note | …a misprint for 1643, the meeting in Warwickshire being historically of 13–14 July 1643… | …a misprint for 1643; it is recorded as printed in the answer file and flagged here, not silently corrected. | substantive（刪去王與王后會面之歷史日期——即本例應期答案） |
| AS-210 | c | notes.ocr_note | The outcome sentence in the 1647 OCR reads 'within lefs three weeks'…the 1852 Zadkiel edition reads 'within three weeks'. | The outcome sentence in the 1647 OCR has a long-s reading ('lefs') where the 1852 Zadkiel edition reads 'less'; both readings are recorded in the answer file. | substantive（刪去應驗句中的 'within three weeks' 應期引文，保留兩版異文校勘資訊） |

逐例人讀未改各例結論（11 例）：
- AS-201：background 僅記六問並提之事實；editorial_note 為 1852 版腳注人名出處，無斷語。未改。
- AS-202：background 為其兄西行、數週無音訊、時值兵亂等占前事實；moment 為占日星曆事實。未改。
- AS-203：background 為所問兩事（男女、產期）本身；chart_data 的 testimonies 計數屬盤面欄位（attachments），不在 subject/context 敘事面，未動。未改。
- AS-204（主持角點名疑似）：人眼核——background 中 'having little judgment in physic' 指 Lilly 自言不諳醫理（judgment＝醫術見識，非斷語），'judged from the figure and afterwards spoke with the patient' 只敘據圖而斷、其後晤病者的過程，全句無病位、可否治、生死等任何斷語內容。判定不算泄漏，未改。
- AS-206：background 為求測者與所欲嫁者之占前情狀事實。未改。
- AS-207：background 為大主教被囚之事實與 Lilly 自述從未謀面。未改。
- AS-208：background 中 Edgehill 之戰結果為占問之前已發生的歷史事實（占時已知）。未改。
- AS-211：background 為馬在 Henley 附近失蹤之事實與所問兩事。未改。
- AS-212：background 為醫者用藥無效、病者轉劇、問者因此疑巫蠱——均占前事實與問者自身懷疑。未改。
- AS-213：background 為囚犯越獄之事實與所問兩事。未改。
- AS-215（主持角點名疑似）：人眼核——background 中 'judged by Lilly for posterity' 只表明此圖由 Lilly 斷存後世，不含 success/loss/betrayal 等任何斷語內容。判定不算泄漏，未改。

## 四、同步位置

- expansion/zengshan/inputs.jsonl：setting 56 例、comment 15 例修訂；build_cases.py：setting 56 處、comment 17 處（第一節 15 處＋覆寫節 LY-210/LY-218 短式各 1 處）同步修訂，語法解析通過。LY-240 comment 的應驗引文亦在兩處同步刪除。
- expansion/bushi/inputs.jsonl：asked_at 18 例修訂；expansion/lilly/inputs.jsonl：AS-205/AS-214 background、AS-209 moment 與 ocr_note、AS-210 ocr_note 修訂。
- phase3/inputs/ 與 phase3/holdout3-inputs/ 的新案例 packet：共 75 個欄位同步修訂（setting/asked_at 與 expansion 改後值逐字一致；packet 不含 notes，comment 修訂不涉及 packet）。

## 五、復掃驗證（清理後）

方法：對全部新案例 inputs（expansion 三路 inputs.jsonl 全字段 + inputs/ 與 holdout3-inputs/ 全部新案例 packet 全字段 + build_cases.py 的 setting/comment 行）跑關鍵詞復掃：`野鶴斷|野鶴見|野鶴獨|初斷|初占斷|斷其|分斷|獨斷|據斷語|应期引文形態|judged|judgment`，另加擴展詞 `斷語|應期|危期|勸|許吉|必得|必到|必歸|應驗|果於` 人工核每條命中；並逐例人讀改後 setting/asked_at/background 全文複核。

結論：**setting / asked_at / subject.background 三個敘事欄位內的斷語與應期內容命中＝0**。全部殘餘關鍵詞命中均屬主持角明示的不算泄漏類，逐項如下：
1. bushi chart_note 固定說明句「本條只錄可由卦名、卦宮、空亡與斷語互證的資訊」（20 例 expansion + 對應 packet）——無內容出處說明，主持角明示不算泄漏。
2. lilly chart_data.note 固定句 “Positions as stated in Lilly's prose judgment.”（15 例 + packet 對應欄）——與上同類，只敘位置出處、無斷語內容。
3. zengshan LY-209 question/comment 的「據…斷語補題」、LY-214/224/227 comment 的「斷語見原文 X 行」、LY-203/228/234/240/245/248/251/254/255/258/259 改後 comment 的「詳見金標側」指針句——只指出處或指向金標，不引任何斷語/應驗內容。
4. LY-247 comment 引文止於「此卦若問僕人在外之吉凶者…巳火又是財爻」——僅問題框架與盤面事實（巳火為財爻），斷語結論部分（主不歸/速至）已刪且引文以省略號截斷於結論之前。
5. AS-204 background 的 'judgment in physic / judged from the figure' 與 AS-215 background 的 'judged by Lilly for posterity'、AS-202 章名 'judgment of an absent brother'——見第三節人眼核結論，均無斷語內容。
6. 問題本身用字：LY-313 setting/question 的「拿獲」、AS-203/AS-214 question 的 'delivered' 等——為所問之事，非斷語。
7. zengshan notes.tags 的「應期明確」標籤（expansion 內部池元數據，packet 不含）——僅標示本例金標含明確應期此一事實，不含任何日期/方向內容；如主持角要求連元數據標籤一併去除，數據角可再執行，本輪照原池慣例保留並在此明示。

另以 `果|應驗|outcome|died|delivered|recovered` 做第二輪廣掃：殘餘命中除上述「詳見金標側」指針句與問題原文外無其他內容性命中。清理後逐例人讀（59+20+15＝94 例敘事欄位）確認：每例 inputs 只餘何人、何時占、問何事、卦象/盤面與求測者當時處境事實。

## 六、汇总计数

- 復查例數：zengshan 59、bushi 20、lilly 15，合計 94 例（全部逐例人讀）。
- substantive 例（至少一欄刪去斷語/應期/結果內容）：zengshan 37 例＝LY-202、203、204、205、206、208、210、212、213、214、215、216、218、222、223、224、225、227、228、230、231、233、234、236、239、240、243、244、245、247、248、251、254、255、257、258、259；bushi 13 例＝LY-301、303、304、305、306、308、309、310、313、315、316、318、319；lilly 4 例＝AS-205、209、210、214。三路合計 54 例。
- cosmetic 例（有改動但未刪斷語內容）：zengshan 19 例＝LY-209、211、217、219、220、221、226、229、232、235、237、238、241、242、246、249、250、252、256；bushi 5 例＝LY-302、307、312、317、320；lilly 0 例。合計 24 例。
- 未改例：zengshan LY-201、207、253；bushi LY-311、314；lilly AS-201、202、203、204、206、207、208、211、212、213、215。合計 16 例。54+24+16＝94，與復查總數一致。
