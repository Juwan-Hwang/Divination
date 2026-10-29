# Phase 3 第二輪擴數（expansion2）總說明（數據角，2026-10-29）

## 產出總覽

- 新增 **84 例**，全部六爻（liuyao）、全部 **A 級**、全部低污染：
  - 《增刪卜易》第二輪（source=zengshan2）59 例：LY-401–459（卷二 50＋卷三/卷四補遺 9），見 `zengshan/GRADING.md`、`zengshan/build_cases2.py`。
  - 《卜筮正宗》第二輪（source=bushi2）25 例：LY-321–345（第十一至十七問），見 `bushi/GRADING.md`、`bushi/build_cases2.py`。
  - Lilly 第二輪複核新增 0 例，見 `lilly/REVIEW.md`。
- 分池（算法見 `../splits4.json` 與 `pool_and_seal.py`）：holdout4 **25 例**（增刪 17＋卜筮 8），金標封存於 `../holdout4/test_gold.jsonl`，SHA-256 `4c5c989cb37c774ce78e3ecb8c2c96b6d4a333fdbd99a35c4d0105006219c147`，封存時間 2026-10-29T15:30:06+08:00，狀態未開封（見 `../holdout4-seal-log.md`、`../holdout4/SEALED.md`）；dev-add 59 例並入 dev 池，**dev4 共 200 例**（dev3 141＋59）。清單：`../roster4-additions.jsonl`、`../splits4.json`；dev-add 金標副本 `dev-add-answers.jsonl`（格式同第一輪 data/dev-new-answers.jsonl，是否另入 phase3/data 由主持角決定）。
- inputs 泄漏自查：`input-check2.txt`（84 例零實質泄漏）。

## 來源清單與合法性

| 來源 | 取得方式 | 合法性 | 本輪用量 |
|---|---|---|---|
| 《增刪卜易》維基文庫全本 | 本地已存 `sources/chinese/zengshan-buyi-wikisource.txt`（公版古籍，維基文庫為合法全文渠道） | 合法 | 卷一/卷二通讀＋卷三/卷四復核，收 59 例 |
| 《卜筮正宗》cnddy 在線全本 | https://www.cnddy.com/1759.html 在線逐頁讀核（2026-10-29，只在線讀、未批量抓取；原書清康熙刊本屬公版） | 合法（在線讀） | 第十一至十七問，收 25 例 |
| Lilly《Christian Astrology》1647 初版 | 本地已存 OCR 全文（archive.org 公版掃描） | 合法 | 全文結局標記詞複核，收 0 例 |
| 《火珠林》維基文庫全本 | https://zh.wikisource.org/zh-hant/火珠林 在線讀 | 合法全文，但**無合格式成例**：內容為規則與「假如/假令」式假設例示，無占時、無事後應驗記錄，收 0 例 | 登記不用於建卡 |
| 《卜筮全书》 | 維基文庫無全文；檢索僅見商業/來歷不明下載站 | 無合法全文 | **只登記不用** |
| 《易冒》 | 無維基文庫/Gutenberg/GitHub 合法全文命中（僅 Scribd 等） | 無合法全文 | **只登記不用**（《增刪卜易》內引易冒評語不作易冒成例） |
| ctext | 僅在線讀渠道，本輪未用其建卡 | — | 未用 |
| 現代帶時間戳公開預言（來源 d） | — | — | 本輪未新增：無現成可在一輪內嚴謹取得的「時間戳＋獨立客觀結局」材料，為免湊數登記未收，既有現代例（AS-301+ 等）不動 |

## 逐例分級表（84 例）

| id | 來源 | 問題 | 斷語方向 | 結局分級 | 污染 | 應驗時點明確 |
|---|---|---|---|---|---|---|
| LY-401 | zengshan2 | 占後遇功名 | mixed | A | low | 是 |
| LY-402 | zengshan2 | 占自陳何如 | negative | A | low | 是 |
| LY-403 | zengshan2 | 占本年冬今得關差否 | positive | A | low | 是 |
| LY-404 | zengshan2 | 占功名始得出仕否 | positive | A | low | 是 |
| LY-405 | zengshan2 | 占病 | negative | A | low | 是 |
| LY-406 | zengshan2 | 占父母近病 | positive | A | low | 是 |
| LY-407 | zengshan2 | 占病 | negative | A | low | 是 |
| LY-408 | zengshan2 | 占妻母病 | negative | A | low | 是 |
| LY-409 | zengshan2 | 占出行（出） | positive | A | low | 是 |
| LY-410 | zengshan2 | 占兄何日歸來 | positive | A | low | 是 |
| LY-411 | zengshan2 | 占官府升否（衙役代占） | positive | A | low | 是 |
| LY-412 | zengshan2 | 占母路隔千里何時來 | mixed | A | low | 是 |
| LY-413 | zengshan2 | 占會試能連捷否 | positive | A | low | 是 |
| LY-414 | zengshan2 | 占病（壬申命） | positive | A | low | 是 |
| LY-415 | zengshan2 | 占已定重罪可蒙赦免否 | positive | A | low | 是 |
| LY-416 | zengshan2 | 占迎請父王靈柩允否 | positive | A | low | 是 |
| LY-417 | zengshan2 | 占女病 | positive | A | low | 是 |
| LY-418 | zengshan2 | 占求財 | positive | A | low | 是 |
| LY-419 | zengshan2 | 母占子何日脫厄 | positive | A | low | 是 |
| LY-420 | zengshan2 | 占鄉試 | positive | A | low | 是 |
| LY-421 | zengshan2 | 占官運 | mixed | A | low | 是 |
| LY-422 | zengshan2 | 占年運 | negative | A | low | 是 |
| LY-423 | zengshan2 | 占妻病 | positive | A | low | 是 |
| LY-424 | zengshan2 | 占月令（本月運限） | mixed | A | low | 是 |
| LY-425 | zengshan2 | 占候選何時得缺 | negative | A | low | 是 |
| LY-426 | zengshan2 | 占開店貿易 | negative | A | low | 是 |
| LY-427 | zengshan2 | 占父任雲南何時得信 | negative | A | low | 是 |
| LY-428 | zengshan2 | 占關差得否 | mixed | A | low | 是 |
| LY-429 | zengshan2 | 占病 | mixed | A | low | 是 |
| LY-430 | zengshan2 | 占掣籤何處（抽籤分發何地） | negative | A | low | 是 |
| LY-431 | zengshan2 | 占主人目下災悔否（家人代占防害） | positive | A | low | 是 |
| LY-432 | zengshan2 | 占功名（先代尊長占病、本人占功名，兩念反應） | positive | A | low | 是 |
| LY-433 | zengshan2 | 占功名（父命子占將來有功名否） | negative | A | low | 是 |
| LY-434 | zengshan2 | 占流年（實問援例成否） | positive | A | low | 是 |
| LY-435 | zengshan2 | 占何時得財（閒問古窖） | negative | A | low | 是 |
| LY-436 | zengshan2 | 占本月月令 | negative | A | low | 是 |
| LY-437 | zengshan2 | 占小廝病 | negative | A | low | 是 |
| LY-438 | zengshan2 | 占防漲水沖去麥子（兼問陰晴） | positive | A | low | 是 |
| LY-439 | zengshan2 | 占本日陰晴 | positive | A | low | 是 |
| LY-440 | zengshan2 | 因連日雪占何日晴 | positive | A | low | 是 |
| LY-441 | zengshan2 | 占本日陰晴 | mixed | A | low | 是 |
| LY-442 | zengshan2 | 因連日雨占何日晴 | mixed | A | low | 是 |
| LY-443 | zengshan2 | 久雪占晴 | positive | A | low | 是 |
| LY-444 | zengshan2 | 因晴占何日雨 | negative | A | low | 是 |
| LY-445 | zengshan2 | 占何日雨（三占合斷） | positive | A | low | 是 |
| LY-446 | zengshan2 | 占何日雨 | positive | A | low | 是 |
| LY-447 | zengshan2 | 占何日晴 | negative | A | low | 是 |
| LY-448 | zengshan2 | 占何日雨（連占合斷） | negative | A | low | 是 |
| LY-449 | zengshan2 | 占何日晴 | mixed | A | low | 是 |
| LY-450 | zengshan2 | 占甲午日臨造此日有雨否 | mixed | A | low | 是 |
| LY-451 | zengshan2 | 占夢（前夫叫去已隨去） | negative | A | low | 是 |
| LY-452 | zengshan2 | 占通鄉避亂（往何方避） | positive | A | low | 否 |
| LY-453 | zengshan2 | 占兄弟還有（有無） | mixed | A | low | 否 |
| LY-454 | zengshan2 | 占道考 | positive | A | low | 否 |
| LY-455 | zengshan2 | 占歲考 | positive | A | low | 否 |
| LY-456 | zengshan2 | 占缺得否 | negative | A | low | 否 |
| LY-457 | zengshan2 | 占往楚買豆得利否 | positive | A | low | 是 |
| LY-458 | zengshan2 | 占母在外何時來 | negative | A | low | 否 |
| LY-459 | zengshan2 | 自占登舟一路平安否 | mixed | A | low | 是 |
| LY-321 | bushi2 | 占谋望求财 | mixed | A | low | 是 |
| LY-322 | bushi2 | 占师近病 | positive | A | low | 是 |
| LY-323 | bushi2 | 占己悔婚可复成否 | positive | A | low | 是 |
| LY-324 | bushi2 | 占友父病 | negative | A | low | 是 |
| LY-325 | bushi2 | 占姑病 | negative | A | low | 是 |
| LY-326 | bushi2 | 姑占弟妇怀孕足月因有病生产平安否 | positive | A | low | 是 |
| LY-327 | bushi2 | 占寻穴地 | positive | A | low | 是 |
| LY-328 | bushi2 | 占侄有事被害否 | positive | A | low | 否 |
| LY-329 | bushi2 | 占开店 | negative | A | low | 是 |
| LY-330 | bushi2 | 占往买卖求得 | negative | A | low | 否 |
| LY-331 | bushi2 | 占赌钱 | negative | A | low | 否 |
| LY-332 | bushi2 | 占会试 | positive | A | low | 否 |
| LY-333 | bushi2 | 占子久病 | negative | A | low | 是 |
| LY-334 | bushi2 | 有同乡人占借贷 | negative | A | low | 否 |
| LY-335 | bushi2 | 占廷师训子 | negative | A | low | 是 |
| LY-336 | bushi2 | 占夫病 | negative | A | low | 是 |
| LY-337 | bushi2 | 占妾近病 | negative | A | low | 是 |
| LY-338 | bushi2 | 占一冬生意 | positive | A | low | 是 |
| LY-339 | bushi2 | 占自去寻父回（两卦合断） | positive | A | low | 是 |
| LY-340 | bushi2 | 占父远出何日回 | positive | A | low | 是 |
| LY-341 | bushi2 | 占仆近出何日回 | positive | A | low | 是 |
| LY-342 | bushi2 | 占今日有人还银否 | positive | A | low | 是 |
| LY-343 | bushi2 | 占父在乱军中吉凶 | negative | A | low | 否 |
| LY-344 | bushi2 | 占子久出何日回 | positive | A | low | 是 |
| LY-345 | bushi2 | 占子嗣多否 | negative | A | low | 否 |

方向口徑：positive＝斷語主旨為吉/成且與結局同向；negative＝凶/不成；mixed＝吉凶並陳或先成後敗等。方向只作描述，不參與分池（分池只按 tradition×contamination 分層隨機抽，見 splits4）。

## 去重記錄

比對範圍：既有全部案例 id 與（占時＋卦象＋所占之事）——LY-01、LY-001–036、LY-101/102/104、LY-201–259、LY-301–320、AS-201–215、AS-301+ 現代例、dev 舊池。
- 《增刪卜易》卷二開頭 24 則與舊例 LY-001–026（含 LY-01）逐一按占時核對重合，剔除不另收；另卷三未月癸亥日占定何罪一則與已收 LY-217 為同一例，剔除。
- **同案異本（跨書）**：
  - 開煤例：增刪卷二獨發章版與卜筮第十五問版（LY-318）同卦同事——增刪版撤下不收（詳見 zengshan/GRADING.md），只留第一輪已收的卜筮版。
  - 母占子脫厄：增刪 857 例（本輪收 LY-419）與卜筮第十七問同案，卜筮版僅「果驗」作 B 且不另收。
  - 女病：增刪 808/819 兩占合斷（本輪收 LY-417）與卜筮第十五問同案，卜筮版僅「果驗」，不另收。
  - 流年援例：增刪 1548 例（本輪收 LY-434）與卜筮第十八問同型同案（卜筮版作「果壬申日文書收到」），第十八問整問不收，僅登記互見。
  - 父命子占功名：增刪 1537 例（本輪收 LY-433）與卜筮第十八問同型同案（卜筮版作「此子未戌日而亡」，年份表述互異），僅登記互見。
  - 尋父（LY-339，卜筮第十五問）與迎請父王靈柩（LY-416，增刪卷二）為**不同事件**（尋生父歸 vs 迎靈柩、應申年 vs 應申月、不同卦），非重複。
  - 子脫厄同型：LY-419（增刪）與卜筮第十七問「子何日脫難」卦象、占時、應驗年份均不同，且卜筮版為「果驗」B，不構成重複收錄問題。
- 卜筮第十七問求財、升遷已為 LY-319、LY-320；第十四問侄孫病已為 LY-317；第十五問開煤窟已為 LY-318；第十六問僕何日回與 LY-303（第七問、B 級排除）為不同問不同卦，本輪第十六問版（LY-341）結局具體，收錄並注明。
- Lilly：複核確認無未收新例（見 lilly/REVIEW.md）。

## 被拒來源/案例及理由（彙總）

- 來源級：《卜筮全书》《易冒》無合法全文，只登記不用；《火珠林》有合法全文但只有假設例示、無真實成例；現代預言來源本輪未取得合格材料。
- 《增刪卜易》卷一/卷二未收約 40 餘則：無應驗追記（9 類）、斷驗混敘不可分離判 B、終身泛斷不可分離、月日干支缺損、多卦鏈/多主體不可單例化、只有方法之辨無結局事件、天時章回顧式無事前斷語等；卷三/卷四未收者同口徑（終身泛斷類、無應驗、斷語兩可如占上書「上與不上皆可」、同故事鏈與已收例重合如邑宰例與 LY-233）。明細摘記於 zengshan/GRADING.md。
- 《卜筮正宗》第十一至十七問未收：僅「果驗」總括判 B（11 則）、無結局/結局過簡、結局文義殘缺、非占後應驗、斷曰內自證判 B、已收重複、第十八問整問不收。明細見 bushi/GRADING.md。

## 數據質量風險

1. 卜筮在線本為簡體字形且裝卦表 OCR 錯亂：節錄照頁面簡體錄入（與第一輪繁體錄入的字形不一致，已在各例 edition 注明）；逐爻裝卦不錄，只錄可互證項，斷卦復現只能到卦名/用神層級。
2. 增刪維基文庫本未校對：訛字照錄並注（已未→己未、「戌日丙午日」首字疑「月」訛、「辰日癸巳日」同）；章界（千金賦章）據通行本體例判定並注明。
3. borderline-A 共 5 例（LY-413、424、432、436、459）與斷語兩可例 LY-333：成色已逐例標明，評分時宜心中有數；應期不合例（LY-410、411、418 及卜筮 LY-321 初斷失望後成議又悔議）如實保留，是應期機制層的真實樣本，未作任何挑揀——分池抽樣只按分層隨機，未按結局好壞選例。
4. 多占合斷例 7 例（LY-401、416、417、430、432、445、339）的 inputs setting 含「再占」時序敘述，屬問卜情境本身，泄漏自查已逐例判定（input-check2.txt）。
