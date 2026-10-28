# SOURCES — 中方占卜类（六爻／梅花／周易文本占）出处与核查记录

收集日期：2026-10-29。纪律：只收能在典籍原文中逐字核到的案例；核不到原文者不入 jsonl，登记于 `pending.md`。
结构：`inputs.jsonl` 只含 subject＋context（attachments 为卦象附件）与 provenance；`answers.jsonl` 含同 id 的 master_predictions（大师、体系、原断节录、direction、依据要点）與 outcome。split 划分由基准统一管理，本卷不自标。

## 总量

| 体系 | 例数 | id 段 | 主要来源 |
|---|---|---|---|
| liuyao（六爻） | 36 | LY-001 – LY-036 | 《增删卜易》26 例（LY-001–026）、《卜筮正宗》10 例（LY-027–036） |
| meihua（梅花易数） | 10 | MH-001 – MH-010 | 《梅花易数》卷一成例 |
| yijing（周易筮占·史传） | 4 | ZY-001 – ZY-004 | 《左传》庄公二十二年、闵公元年、襄公九年、昭公七年 |

## 来源一：《增删卜易》（LY-001 – LY-036 中的前 26 例）

- 作者：野鹤老人著，李文辉（觉子）增删。清初成书，古籍公版（license_status: public-domain，redistributable: true）。
- 核对本：维基文库《增删卜易》全本，URL：https://zh.wikisource.org/wiki/增刪卜易 ；本机抓取本（action=raw）：`~/workspace/divination/sources/chinese/zengshan-buyi-wikisource.txt`，逐例与此本原文核对（含卦盘六爻，inputs 中 chart_lines_top_to_bottom 自上爻至初爻照录，左为本卦、右为变卦）。
- 已知瑕疵（照实标注）：
  1. 维基文库本页自标 Textquality 25%、未排版未校对，个别字形有讹（如「𨿽」为「雖」之异体/讹字、「𨿽然」等），节录照原文录入，未擅改；待与校正本（如郑同校《校正全本增删卜易》，华龄出版社）对校后修订，已登记 pending。
  2. 卷之二自「增删黄金策千金赋章第三十四」起，维基文库本未标章界，本卷 LY-016 – LY-024 的章名归属系按通行本体制与内容（千金赋句下注断）判定，已在各条 provenance.page 中注明「据通行本体例判定」。
  3. LY-006、LY-007、LY-013、LY-016、LY-018 五例，原书只附装卦而未直书卦名，卦名由装卦（世应、六亲、动爻）推得，已在各条 casting 的 hexagram 字段注明「卦名原文未直书，据所附装卦推得」。
- 本轮收录范围：卷之二理论诸章（月破、飞伏神、进神退神、随鬼入墓、两现、黄金策千金赋、天时）中的完整占验——每例均同时具备：所问、月日、卦象、断语、应验四要素。卷之三、四各门类占例尚多，未及逐例核完，登记 pending 增补。

## 来源二：《卜筮正宗》（LY-027 – LY-036）

- 作者：王洪绪辑，康熙四十八年（1709）成书。古籍公版（public-domain，redistributable: true）。
- 归属说明：《凡例》自述「是书十三、十四卷，有十八问皆吾师所授及余所占验」——十八问答附占验诸例，或为王洪绪自占、或为其师杨广含所授占验，逐例不可分，本卷 master 统一记「王洪绪（辑录，含师杨广含传授及自占验）」。
- 核对本：华夏大易学社（cnddy.com）在线全本 https://www.cnddy.com/1759.html ，2026-10-29 在线逐段核对「十八问答附占验」（第一问至第五问部分）。ctext 未用（禁止抓取，且本轮只在线读核 cnddy 本）。
- 已知瑕疵：该在线本的装卦表为双栏排版经 OCR/转录后行序错乱，逐爻装卦未能可靠还原。故 LY-027 – LY-036 只录可由卦名、卦宫、空亡、用神与断语互证的信息，逐爻表不录（inputs 各条 attachments.chart_note 已注明）；补全需可靠校本，登记 pending。

## 来源三：《梅花易数》（MH-001 – MH-010）

- 传世文本托名宋·邵雍（康节）。邵雍真著（《皇极经世书》《伊川击壤集》）无此书，宋人书目不见著录，通行本系后世（明）編集流传——归属存疑照实标注：各条 notes.tags 含 `disputed`，master 记「邵雍（传世文本托名）」。按收集纪律，现代建构/伪托而为后世大师实际奉行者照收，只标真伪。
- 核对本：维基文库《梅花易数》https://zh.wikisource.org/wiki/梅花易數 ；本机抓取本：`~/workspace/divination/sources/chinese/meihua-yishu-wikisource.txt`。本轮只收卷一「象数易理篇之二」成例十则（观梅、牡丹、邻夜扣门借物、今日动静、西林寺牌额、老人有忧色、少年有喜色、牛哀鸣、鸡悲鸣、枯枝坠地），均有起卦过程、断语、应验原文。
- 污染提示：观梅占、牡丹占、邻夜扣门借物占、西林寺牌额占、老人有忧色占过于著名，模型可能已经背诵，MH-001/002/003/005/006 已标 notes.tags `famous`，评分时应降权。

## 来源四：《左传》周易筮占（ZY-001 – ZY-004）

- 《左传》为先秦史籍，公版（public-domain，redistributable: true）。provenance.url 指向维基文库《春秋左氏传》。
- 核对路径：四例引文（占辞、断语、追记应验）在收集时经三种彼此独立的公开转录交叉核对一致——公开《左传》全文转录（360doc 藏本）、易学网《春秋占筮书》（毛奇龄）所引内传原文、学术论文/讲义所引原文。未逐字比对纸本《十三经注疏》，此点照实说明。
- ZY-001 另有跨文献互证：《史记·田敬仲完世家》同载陈敬仲占筮，已在 notes.cross_ref 标注，供跨体系/跨文献验证。
- ZY-003 为同占两断（一从一否）名例：占史断「必速出」（positive）、穆姜自断「必死于此」（negative），结局从穆姜断；answers 中两条 prediction 并录，金标方向以穆姜条为准。
- 四例均为史传名例，notes.tags 含 `famous`，评分应降权。

## 逐例出处表

| id | 体系 | 所问（节） | 书 | 卷/章 | URL |
|---|---|---|---|---|---|
| LY-001 | liuyao | 占將來有官否 | 《增刪卜易》 | 卷之二·月破章第二十七 | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-002 | liuyao | 占父何日歸 | 《增刪卜易》 | 卷之二·月破章第二十七 | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-003 | liuyao | 占子病 | 《增刪卜易》 | 卷之二·飛伏神章第二十八 | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-004 | liuyao | 占父病 | 《增刪卜易》 | 卷之二·飛伏神章第二十八 | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-005 | liuyao | 占鄉試 | 《增刪卜易》 | 卷之二·進神退神章第二十九 | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-006 | liuyao | 占求婚成否 | 《增刪卜易》 | 卷之二·進神退神章第二十九 | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-007 | liuyao | 占父有信至已起程，我去迎之可能遇否 | 《增刪卜易》 | 卷之二·進神退神章第二十九 | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-008 | liuyao | 占病 | 《增刪卜易》 | 卷之二·進神退神章第二十九 | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-009 | liuyao | 占母血崩一年有餘 | 《增刪卜易》 | 卷之二·進神退神章第二十九 | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-010 | liuyao | 占試中否 | 《增刪卜易》 | 卷之二·進神退神章第二十九 | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-011 | liuyao | 占母路隔千里何時來 | 《增刪卜易》 | 卷之二·進神退神章第二十九 | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-012 | liuyao | 占開金銀器皿店 | 《增刪卜易》 | 卷之二·進神退神章第二十九 | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-013 | liuyao | 占夫病（妻占夫，夫命癸亥） | 《增刪卜易》 | 卷之二·隨鬼入墓章第三十 | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-014 | liuyao | 占求財 | 《增刪卜易》 | 卷之二·兩現章第三十二 | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-015 | liuyao | 占升遷 | 《增刪卜易》 | 卷之二·兩現章第三十二 | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-016 | liuyao | 占訟 | 《增刪卜易》 | 卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，維基文庫本此段未標章名） | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-017 | liuyao | 占升遷 | 《增刪卜易》 | 卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上） | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-018 | liuyao | 占地下忽然起五色之光，疑有古窖（藏財） | 《增刪卜易》 | 卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上） | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-019 | liuyao | 占小舟過關恐盤阻 | 《增刪卜易》 | 卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上） | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-020 | liuyao | 占財 | 《增刪卜易》 | 卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上） | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-021 | liuyao | 占何日雨 | 《增刪卜易》 | 卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上） | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-022 | liuyao | 占身病（自占） | 《增刪卜易》 | 卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上） | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-023 | liuyao | 占母病 | 《增刪卜易》 | 卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上） | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-024 | liuyao | 占子病（續 LY-023） | 《增刪卜易》 | 卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上） | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-025 | liuyao | 因連日雪，占何日晴 | 《增刪卜易》 | 卷之二·天時章第三十五 | https://zh.wikisource.org/wiki/增刪卜易 |
| LY-026 | liuyao | 因連日晴，占何日雨 | 《增刪卜易》 | 卷之二·天時章第三十五 | https://zh.wikisource.org/wiki/增刪卜易 |
| MH-001 | meihua | 觀梅占：二雀爭枝墜地，佔其兆 | 《梅花易數》 | 卷一·象數易理篇之二（占例） | https://zh.wikisource.org/wiki/梅花易數 |
| MH-002 | meihua | 牡丹占：花盛如此，亦有數乎 | 《梅花易數》 | 卷一·象數易理篇之二（占例） | https://zh.wikisource.org/wiki/梅花易數 |
| MH-003 | meihua | 鄰夜扣門借物占：借何物 | 《梅花易數》 | 卷一·象數易理篇之二（占例） | https://zh.wikisource.org/wiki/梅花易數 |
| MH-004 | meihua | 今日動靜如何 | 《梅花易數》 | 卷一·象數易理篇之二（占例） | https://zh.wikisource.org/wiki/梅花易數 |
| MH-005 | meihua | 西林寺牌額占：寺額「林」字無兩勾，占其兆 | 《梅花易數》 | 卷一·象數易理篇之二（占例） | https://zh.wikisource.org/wiki/梅花易數 |
| MH-006 | meihua | 老人有憂色占 | 《梅花易數》 | 卷一·象數易理篇之二（占例） | https://zh.wikisource.org/wiki/梅花易數 |
| MH-007 | meihua | 少年有喜色占 | 《梅花易數》 | 卷一·象數易理篇之二（占例） | https://zh.wikisource.org/wiki/梅花易數 |
| MH-008 | meihua | 牛哀鳴占 | 《梅花易數》 | 卷一·象數易理篇之二（占例） | https://zh.wikisource.org/wiki/梅花易數 |
| MH-009 | meihua | 雞悲鳴占 | 《梅花易數》 | 卷一·象數易理篇之二（占例） | https://zh.wikisource.org/wiki/梅花易數 |
| MH-010 | meihua | 枯枝墜地占 | 《梅花易數》 | 卷一·象數易理篇之二（占例） | https://zh.wikisource.org/wiki/梅花易數 |
| LY-027 | liuyao | 占弟病，業已臨危 | 《卜筮正宗》 | 卷十三、十四·十八問答附占驗·第一問（三傳克用） | https://www.cnddy.com/1759.html |
| LY-028 | liuyao | 占弟被訟，吉凶何如 | 《卜筮正宗》 | 卷十三、十四·十八問答附占驗·第一問（三傳克用） | https://www.cnddy.com/1759.html |
| LY-029 | liuyao | 一人占自病 | 《卜筮正宗》 | 卷十三、十四·十八問答附占驗·第一問（三傳克用） | https://www.cnddy.com/1759.html |
| LY-030 | liuyao | 占開店 | 《卜筮正宗》 | 卷十三、十四·十八問答附占驗·第二問（回頭克） | https://www.cnddy.com/1759.html |
| LY-031 | liuyao | 占父官事 | 《卜筮正宗》 | 卷十三、十四·十八問答附占驗·第二問（回頭克） | https://www.cnddy.com/1759.html |
| LY-032 | liuyao | 妻占夫近病 | 《卜筮正宗》 | 卷十三、十四·十八問答附占驗·第三問（原神） | https://www.cnddy.com/1759.html |
| LY-033 | liuyao | 一人自占近病 | 《卜筮正宗》 | 卷十三、十四·十八問答附占驗·第三問（原神） | https://www.cnddy.com/1759.html |
| LY-034 | liuyao | 占嬸病 | 《卜筮正宗》 | 卷十三、十四·十八問答附占驗·第四問（三合成局） | https://www.cnddy.com/1759.html |
| LY-035 | liuyao | 占父何日歸 | 《卜筮正宗》 | 卷十三、十四·十八問答附占驗·第四問（三合成局） | https://www.cnddy.com/1759.html |
| LY-036 | liuyao | 占升選 | 《卜筮正宗》 | 卷十三、十四·十八問答附占驗·第五問（反吟） | https://www.cnddy.com/1759.html |
| ZY-001 | yijing | 陳敬仲（陳公子完）之前程國祚 | 《左傳》 | 莊公二十二年 | https://zh.wikisource.org/wiki/春秋左氏傳 |
| ZY-002 | yijing | 畢萬仕晉之前程 | 《左傳》 | 閔公元年 | https://zh.wikisource.org/wiki/春秋左氏傳 |
| ZY-003 | yijing | 穆姜遷東宮後能否得出 | 《左傳》 | 襄公九年 | https://zh.wikisource.org/wiki/春秋左氏傳 |
| ZY-004 | yijing | 衛國立嗣：立元（孫圉）還是立絷（孟絷） | 《左傳》 | 昭公七年 | https://zh.wikisource.org/wiki/春秋左氏傳 |
## 版权总说明

本卷全部案例出自公版古籍（清及清以前成书的刻本系统、传世托名文本、先秦史籍），license_status 一律 `public-domain`、redistributable `true`。现代转录平台（维基文库录入者整理、cnddy 在线录入）仅作核对路径引用；维基文库文本依其站点条款为 CC BY-SA，本卷节录的均为古籍原文短节录并注明出处。
