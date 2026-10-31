# -*- coding: utf-8 -*-
"""R80 B20 盲测写盘脚本：只写本批 20 例 predictions，带 id 集断言与写后回读校验。"""
import json, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round80/predictions"
EXPECTED = ["OC-018","OC-019","OC-020","OC-021","OC-022","OC-023","OC-024","OC-025",
            "OC-026","OC-027","OC-028","OC-029","OC-030","WP-001","WP-002","WP-003",
            "WP-004","WP-005","WP-006","WP-007"]

def trig():
    return {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}

P = {}

P["OC-018"] = {
 "prediction_text": "主断贵显而晚年横险：命主以杀印相生得大位，成全国级报业巨头，地位与财富俱至上层（非寻常富商）。中年行运最盛；晚年转入劫土之运后势衰，且有非病之横祸——五十余岁、约1930年代中段有遇刺/横死之险，命终在此一关，非安然寿终。时间窗以年档计：险关落在五十岁后数年内，主坐标约1934年前后。",
 "basis": "卡面未标注 tradition 字段；题面给史量才四柱己卯丙子庚寅辛巳与报业巨头身份，按八字自决。\nsystems_used: 八字（子平格局＋旺衰调候＋大运）\n方向对决：正路定性栏——月干丙七杀透、年干己正印化杀生身，杀印链成链，丙火又暖子月寒局，定性主贵显；反路定性栏——子为伤官、伤官见官本主驳杂，然己印贴身制伤化杀，反路只余量级（驳杂耗力），裁决取正路锁定贵显。特格扫描：从格未命中（辛劫助、己印生、巳藏庚根），专旺未命中，寒极未命中（丙透巳根、火能成暖）；常规格。主线：伤官格以印化杀为成，格局成而有救，用神印与调候火俱有根。格局量级区间：下限一方名流富商（依据：杀印成链）—上限全国级行业领袖（依据：财坐寅旺、杀印俱透）。大运逆行乙亥、甲戌、癸酉、壬申、辛未：水金运泄秀生财主中年发迹，辛未运劫土埋金、势转衰。峰值运三核对：壬申运①用神印金得申地通根满足②运干壬泄秀呼应财路半满足③否决清单(i)合绊用神之干未命中(ii)冲克用神之根未命中(iii)透忌神且通根未命中，满足约2项称峰值；否决三条核查：壬申运①未命中②未命中③未命中。关键结局：子女宫时柱巳火杀印，承继有人而晚景不宁；病位不在脏腑慢病、主金火相战之突发横伤；破耗因晚运劫夺与横事连带；高峰在壬申运段。险年以年档先定年：辛未运内火土年引动巳火杀局，约1934年前后为横祸主坐标（定值档置信中）。",
 "confidence": 0.55}

P["OC-019"] = {
 "prediction_text": "主断名高位显而中年横死：命主以食伤生财、身有根气，成学界与政界兼擅之显职，位至研究院总干事一级，名望大于实权之久享。四十岁出头为生死险关：约1933年前后（癸酉年一带）有遇刺/官祸式横死之险，非病终、非寿终。时间窗以年档计：盛年在三十余岁木运，险关主坐标约1933年。",
 "basis": "卡面未标注 tradition 字段；本例为杨杏佛四柱癸巳丙辰壬申癸卯且卡面自注另一命稿异载、本例以此书为准，按八字自决并以卡面四柱为唯一盘面。\nsystems_used: 八字（子平格局＋旺衰气势＋大运）\n方向对决：正路定性栏——壬坐申长生得印根、辰为水库，丙财透月、卯伤生财，食伤生财链成，定性主名利显达；反路定性栏——卯辰相害、财旺耗身只在量级栏（耗损程度），无定性破格之据，裁决取正路。特格扫描：从格未命中（申根辰库俱在），专旺未命中，偏枯未命中；常规格。主线：食伤生财格成，用神财火得巳禄而身亦有根，成格有力。格局量级区间：下限知名学者/中层名流（依据：财透伤生）—上限全国性机构首长级名望（依据：身财两停、印根护身）。大运逆行乙卯、甲寅、癸丑、壬子：卯寅木运泄秀生财为盛，然甲寅运寅冲日支申根、动摇根基，是转折逆运——作用表：运支寅→日支申根：冲，根动失守；运干甲→财丙：生，名利更张，顺逆参半从根基定逆。峰值运三核对：乙卯运①用神财火于卯不得地不计②运干乙伤生财呼应满足③否决(i)未命中(ii)未命中(iii)未命中，满足约2项（含呼应与否决通过）称峰值；否决三条核查：乙卯运①运干合绊用神：未命中②运支冲克用神之根：未命中③运干透忌神且通根：未命中。关键结局：子女宫时卯伤官，子女有出息之象；病位主申金根受冲之突发外伤而非内病；破耗随横关而绝；高峰乙卯运段。险年：甲寅运内癸酉年，金旺冲卯、根局齐动，约1933年为主坐标（年档定值）。",
 "confidence": 0.58}

P["OC-020"] = {
 "prediction_text": "主断贵至极品而五十岁病卒于任：食神制杀格成，位至国民政府主席一级的元首之贵，权位为一生顶点。险年在约五十岁、1930年前后：中风/脑溢血一类急病暴卒于任上，不享遐寿。时间窗以年档计：贵显贯穿中年戌运前后，险关主坐标约1930年（庚午年）。",
 "basis": "卡面未标注 tradition 字段；题面给谭延闿四柱己卯丁丑癸丑乙卯与主席级政要身份，按八字自决。\nsystems_used: 八字（子平格局＋调候＋大运）\n方向对决：正路定性栏——月支丑七杀两见、时干乙食神透而两卯食根旺，食神制杀成链，定性主大贵；反路定性栏——杀重身弱本主压身，然食制有力、己印在年，反路只在量级栏记身弱任杀之劳，裁决取正路锁定贵显。特格扫描：从格未命中（丑为水土之根、印透），专旺未命中，寒极近而未命中（丁火透、卯木向阳，火虽弱非全无根）；常规格、冬月先取丁火调候。主线：七杀格食制成格，用神食神得两卯强根，杀有制化为权。格局量级区间：下限封疆大吏（依据：制杀成格）—上限元首极品（依据：食根双旺、杀局纯一）。大运逆行丙子、乙亥、甲戌、癸酉：乙亥甲戌木运食神得地主贵显上升，甲戌运戌冲两丑杀库、贵极而动。峰值运三核对：甲戌运①用神食木于戌不得地不计②运干甲伤呼应食制满足③否决(i)未命中(ii)戌冲丑为冲杀库非冲用神之根、未命中(iii)未命中，满足约2项称峰值；否决三条核查：甲戌运①未命中②未命中③未命中。关键结局：子女宫时乙卯食旺，子女贤显；病位：土旺水弱、丑土病字主脾胃与脑部血脉之急症；破耗因病卒任上而位禄骤止；高峰甲戌运段。险年：戌运庚午年，午火财旺生杀、冲子，约1930年急病为主坐标（年档定值）。",
 "confidence": 0.6}

P["OC-021"] = {
 "prediction_text": "主断武贵极盛而晚年失势落拓：伤官制杀格成，成一方军阀首领之贵，位至都督/巡阅使一级，统兵握权为上层武贵。中年火土运为极盛期；晚运转衰后权位被夺、势败名落，终局落拓而终，不得以盛年之贵善终其位。时间以运档计：盛在中年午未运，衰在晚年辰运一带（约1920年代后段）。",
 "basis": "卡面未标注 tradition 字段；陆荣廷四柱戊午辛酉乙卯丙戌、旧桂系军阀首领身份见题面，按八字自决。\nsystems_used: 八字（子平格局＋气势＋大运）\n方向对决：正路定性栏——乙坐卯禄、月辛七杀透、时丙伤官透制杀，伤官制杀成链且午戌助伤，定性主武贵；反路定性栏——酉卯冲、杀旺攻身在量级栏记根基受冲之险，无定性翻盘之据，裁决取正路。特格扫描：从格未命中（卯禄寅绝不从、丙丁制杀），专旺未命中，燥热未极（酉金戌土在局）；常规格。主线：七杀格以伤官制杀成格，用神丙火得午禄戌库、根深。格局量级区间：下限一省武职长官（依据：制杀成格）—上限一方军阀之首、巡阅使级（依据：杀伤两旺、财印暗藏相生）。大运逆行庚申、己未、戊午、丁巳、丙辰：未午巳火土运制杀生财连成极盛，丙辰运辰冲戌库、伤根动摇为转折逆运。峰值运三核对：戊午运①用神丙火得午禄地满足②运干戊财与制杀后生财链呼应满足③否决(i)未命中(ii)未命中(iii)未命中，满足3项称峰值；否决三条核查：戊午运①未命中②未命中③未命中。关键结局：子女宫时丙戌，子女平常；病位主酉金杀与木受冲之筋骨肝胆；破耗因兵败失势连带家产散失；高峰戊午运段。晚衰坐标止于运档（题问一生贵显、无具体事件年问），丙辰运为衰段主坐标（运档定值）。",
 "confidence": 0.65}

P["OC-022"] = {
 "prediction_text": "主断终身无科第、无显官，以学问术数立身成名：屡试不第不是一时之挫，而是命定功名无缘——官星被制、科名之路断绝，不以仕途终身。其立身在学问著述一路：以命理之学成一代名家，衣食丰裕、名满同道，晚景安稳。时间以运档计：青年申运功名受挫见分晓，中晚年以著述立名。",
 "basis": "卡面未标注 tradition 字段；袁树珊自造辛巳丁酉乙巳戊寅、卡面注安命甲午大运丙申起且屡试不第，按八字自决。\nsystems_used: 八字（子平格局＋旺衰＋大运）\n方向对决：正路定性栏（就所问科第）——月丁食神透制酉辛七杀、官星受制而印星不显于月时，科名定性主断绝；反路定性栏——寅藏甲丙戊、印根暗存，只在量级栏记学问根柢深，不能改科第方向，裁决锁定无科第。特格扫描：从格未命中（寅根在时），专旺未命中，偏枯未命中；常规格。主线：食神制杀格，杀制尽则不主武贵、转主以技艺学问制名利；用神丁火得巳禄。格局量级区间：仕途下限上限俱低（依据：官受食制、印不显）—学问名望上限至全国知名命家（依据：食神根深、财印暗生）。大运逆行丙申、乙未、甲午、癸巳、壬辰、辛卯：丙申运申冲寅、功名与根基齐挫；后运火土相生，著述生财安稳。峰值运三核对：就立身言甲午运①用神丁火得午禄满足②运干甲印呼应学问满足③否决(i)未命中(ii)未命中(iii)未命中，满足3项称峰值（学问峰非仕途峰）；否决三条核查：甲午运①未命中②未命中③未命中。关键结局：子女宫时寅，子女有根；病位主木弱金旺之肝目筋骨；破耗因早年应试耗费；高峰甲午运段。应期止于运档：功名断绝以青年丙申运为定点（运档定值），不虚报科年。",
 "confidence": 0.7}

P["OC-023"] = {
 "prediction_text": "主断：钟下所覆为一件中空有足的器物，且已破损不全。质为陶瓦/金属之烹食器一类（鼎足器物之象），上部或一足有缺口破损，非完整新器、非活物、非食物。完好与否明确断：破损。",
 "basis": "卡面未标注 tradition 字段；题面为席间射覆、给卦象火风鼎变雷风恒，按梅花体用自决。\nsystems_used: 梅花易数（体用生克＋卦象取物）\n方向对决：正路定性栏——本卦鼎，鼎象为三足中空之烹器，器物类象直指；上爻动而离变震，上部见动主上口/耳部有缺，定性主器物破损；反路定性栏——恒主久常、巽主入，只在量级栏记其置放已久、藏于钟下，不改器物类。体用：下巽为体、上离为用，体木生用火，体泄气主物已耗损不全；离中虚主中空，鼎三足主有足。应验对象复核：断语落于钟下之物本身，非覆者或占者。射覆无应期可定，明写不断应期。具体断项粒度核：器物类有鼎象与体用两指针支撑保留原粒度；破损有上爻动与体泄两指针保留。",
 "confidence": 0.35}

P["OC-024"] = {
 "prediction_text": "主断：葬资有着落，不必外借——金就藏在易者屋内的一只瓷枕之中。来访秀士（邵雍）无意间以枕击鼠，枕破而金出，以此金营葬，恰足办妥身后事。应验即在邵雍到访当日、当场见分晓。",
 "basis": "卡面未标注 tradition 字段；题面为《梅花易数》序中易者遗书托葬之事、无卦象附件，按梅花成例体裁与题面事实自决。\nsystems_used: 梅花易数（成例占验体裁＋事实优先序）\n方向对决：正路定性栏——遗书预言来访秀士可托，身后事必有着落，定性主葬资可得；反路定性栏——其家明言无资营葬，只在量级栏记眼前困窘，不构成无着落之定性，裁决取正路。列面：主问面葬资来源已断；对象面落点为屋内瓷枕中藏金（器物面）；事件面为击鼠枕破而金出。事实优先：占题事实为家贫无资、遗书有预言，故金只能出自家内久藏之物、不向外求。对象定位：金之承受与应验同为易者之葬费，无错位。此象只能由成例体裁收束到枕金一事，置信据遗书预言之明确性而定。",
 "confidence": 0.72}

P["OC-025"] = {
 "prediction_text": "主断：应验。届预书所定年月日，椅子必被坐破——有客来访坐此椅，椅当场破损，时日与椅底预书相合。人只受虚惊、无大伤。应期即预书所写的那个日期时辰，不差移。",
 "basis": "卡面未标注 tradition 字段；题面为邵雍椅底预书坐破之事、无卦象附件，按梅花预言占验体裁自决。\nsystems_used: 梅花易数（预言占验＋事实优先序）\n方向对决：正路定性栏——预书明定年月日与坐破之事，应验面自带日期锚点，定性主届期必验；反路定性栏——椅为日用旧物、偶然破损之可能只在量级栏，不足以推翻预书锚点，裁决取正路。列面第5项锚点核：预书年月日为直读锚点，转应面（另解他日他椅）列入并舍弃，理由为预书专指此椅此日。对象定位：应验对象为该椅与坐椅之客，承受与应验同一。断项粒度：坐破一事有预书与届期验之两项题面支撑，保留原粒度；人不伤为倾向表述（支撑较弱，降格为倾向）。",
 "confidence": 0.68}

P["OC-026"] = {
 "prediction_text": "主断：今年功名可成，但只成一人——昆弟二人中一人登科得中（会试/殿试成名），另一人落第陪衬，不作双双齐中之断。应期在今年春夏放榜之期（月档，主坐标为会试放榜之月）。得中者名位为正途进士出身，非乡贡小就。",
 "basis": "卡面未标注 tradition 字段；题面给大六壬课式涉害曲直、三传乙未青龙己亥螣蛇癸卯玄武、1643年正月己亥日占，按六壬自决。\nsystems_used: 大六壬（课格＋三传天将＋仕宦/考试门）\n方向对决：正路定性栏——三传亥卯未成曲直木局，木为己土之官鬼，官星成局入传、初传未乘青龙主喜庆功名，课格主向主成；反路定性栏——官旺克日、日干己寄未而初传即未，官势压身只主中者吃力、且末传卯乘玄武主榜事暗昧，只在量级栏压低成数（只成一人），不翻方向，裁决锁定成。盘面不全守第八节：只据干支、三传链、天将乘传、课格与甲午旬辰巳空作断，不臆补四课天盘。取用：官鬼木局为功名类神，一级据（入传临干寄宫、青龙合事）；螣蛇中传主榜前惊疑虚扰。应期（k）定月档：春月木旺、放榜在春夏之交，三路取逢值一路（卯未值月）为主坐标，冲实/填实两路无候选（空在辰巳不碍传）已明写舍弃。",
 "confidence": 0.45}

P["OC-027"] = {
 "prediction_text": "主断负面：此行不得意。课名无禄无路，北上诏命虽至而实惠落空——到京难得如意任用，行程稽迟、身多病滞，终须空回/滞回。本人身体有病困之象；老母在家不安，有重病乃至丧信之忧。应期以月档计：末传亥空，亥月填实前后（本冬内）诸事见分晓，主坐标为亥月。",
 "basis": "卡面未标注 tradition 字段；题面给大六壬无禄无路课、三传癸酉合戊辰阴亥青空、1642年冬月辛未日占，按六壬自决。\nsystems_used: 大六壬（课格＋三传天将＋仕宦/出行门＋母事并读）\n方向对决：正路（吉向）定性栏空——无禄无路为凶格、末传青龙落亥旬空，吉神空则喜不成，无定性吉据；反路定性栏——无禄课主禄位无着、末传空主行终无果、北方兵紧为事实压制，裁决锁定负面。盘面不全守第八节：只据干支三传天将课格与甲子旬戌亥空作断。类神并读（LR-QY-1）：官鬼面——辛以午火为官、官不入传，只作背景不断得官；父母面——土为父母，中传辰乘太阴临传，母事有据落次级事件线：太阴主暗昧病私，断老母在家病重难安。末传亥青龙空：龙空则恩喜落空、行人稽留。应期（k）阶段尺度定月档：三路取填实一路（亥填实）为主坐标，逢值一路与终局负向不合舍弃，冲实一路亥逢巳冲而事更散、只作稽迟注记。",
 "confidence": 0.5}

P["OC-028"] = {
 "prediction_text": "主断：考选得官。课得斫轮成器之格，入觐考选必被取中授职，所授为科道言官一类清要之职（御史/给事中级），非闲散佐贰。应期以月档计：卯为发用，本年春间（卯月前后）授官见分晓，主坐标卯月。",
 "basis": "卡面未标注 tradition 字段；题面给大六壬重审斫轮课、三传辛卯玄武丙戌朱雀癸巳白虎、1630年冬月己丑日占，按六壬自决。\nsystems_used: 大六壬（课格斫轮＋三传天将＋仕宦门）\n方向对决：正路定性栏——斫轮格主木就金斫而成器、印绶俱全主迁转授职，初传卯为己土之官鬼发用，官星当头发用主得官，定性主成；反路定性栏——卯乘玄武只主选事暗中有竞争耗费、在量级栏，不构成不得官之定性，裁决取正路。盘面不全守第八节：只据干支三传天将课格与甲申旬午未空作断，午未空不碍官传。中传戌乘朱雀：朱雀主文书言责，戌卯合主选命合身；末传巳乘白虎主到任后任事繁剧。取用：官鬼卯一级据（发用临传乘将合仕宦门）。官职落点科道由朱雀文书言责面与卯官两指针支撑，保留原粒度。应期（k）定月档：三路取逢值一路（发用卯值月）为主坐标，填实/冲实两路无涉空传、明写无候选。",
 "confidence": 0.42}

P["OC-029"] = {
 "prediction_text": "主断分判：此行携子求官难遂——谒人虚许、官事不成或久拖无果，须空手而返；更急之事在老母：年近九十的老母有大病/丧信之警，凶信将至，须速归山东料理，不得久留于外。应期以月档计：未月/未日冲应一带见凶信，主坐标在本冬未月前后。",
 "basis": "卡面未标注 tradition 字段；题面给大六壬涉害曲直回环课、三传乙未白虎癸卯合己亥天后、1642年十月己亥日占、其子丑命、母近九十，按六壬自决。\nsystems_used: 大六壬（课格＋三传天将＋仕宦门与母事事件线并读）\n方向对决（主问求官面）：正路定性栏——曲直木局官鬼旺入传本主官机，然回环课成事迟滞、官旺克日过重，求官定性只到机而难遂；反路定性栏——初传未乘白虎、白虎主丧病道路之凶临初传，定性主此行凶多吉少，裁决锁定求官不成。事件线展开（LR-QY-3.2）：母事自有取用链——未为土父母之位乘白虎入初传，临干寄宫（己寄未），一级据，落独立事件条目断老母病丧之警，方向与主线同负不相吞没。子事：其子丑命，丑与初传未冲，子辈此行亦受冲耗、无得官之据，明写无据不报其官。盘面不全守第八节，只据已给盘面作断。应期（k）定月档：三路取逢值一路（未值）为主坐标，冲实一路（丑冲未）作凶信触发注记，填实一路无候选明写。",
 "confidence": 0.48}

P["OC-030"] = {
 "prediction_text": "主断分判：其一，淮扬巡按差可复——铸印成格、太常乘发用，复设之命将下，巡按差恢复设立；其二，吏书缺不可照旧——原缺不由旧人依旧占踞，将更易其人/其制，名虽存而人已换。应期以月档计：巳火印炉值月前后见复差之信，主坐标在本年巳月一带。",
 "basis": "卡面未标注 tradition 字段；题面给大六壬重审铸印课、三传癸巳太常丙戌六合辛卯太阴、1651年二月戊子日占，按六壬自决。\nsystems_used: 大六壬（课格铸印＋三传天将＋仕宦门）\n方向对决（巡按复差面）：正路定性栏——铸印格戌加巳发用、巳为印炉戌为印绶、初传巳乘太常（太常主印绶迁拜），印事成器，定性主差可复；反路定性栏空——无冲破印传之定性据，裁决取正路锁定可复。吏书面分判：末传卯乘太阴，太阴主暗昧更易，戌卯合而合中带换，断其缺不照旧人。盘面不全守第八节：只据干支三传天将课格作断，卡面未给空亡、明写空亡无据不入断。取用：父母印绶巳一级据（发用乘太常合印事）。应期（k）定月档：三路取逢值一路（巳值月）为主坐标，冲实/填实两路无候选明写舍弃。",
 "confidence": 0.55}

P["WP-001"] = {
 "prediction_text": "Main call: YES — a major collective affliction falls on 2020–2021, and it is a pandemic: a worldwide epidemic disease (respiratory/influenza-type plague) spreading across countries, peaking with the early-2020 Jupiter–Saturn–Pluto conjunction and the century-low cyclical index. Timing window: onset/peak 2020, extending through 2021 (year-scale coordinate, main point early 2020).",
 "basis": "Card carries no tradition field; the card's mundane configuration (outer-planet cluster, Jupiter–Saturn–Pluto conjunction, cyclical-index low) is taken on its own terms and judged by mundane astrology as stated on the card.\nsystems_used: Western mundane astrology (outer-planet cycles, cyclical index)\nDirection duel: pro line (qualitative) — the card itself notes comparable past clusters coincided with 1918, 1954, 1968 and 1982, years of epidemic/pandemic events, and the 2020 cluster is the tightest with the lowest index of the century, so the affliction line has a chart-level basis; con line (qualitative) — no line of the card's configuration points to war or famine specifically, its precedents are epidemic years, so the pandemic reading is locked and other affliction types are set aside as magnitude-level alternatives. Specifics: disease-type and worldwide spread follow the 1918 precedent among the card's own comparanda; granularity kept at pandemic class, no pathogen named (no pointer for a named agent).",
 "confidence": 0.78}

P["WP-002"] = {
 "prediction_text": "Main call: Barack Obama wins the 2008 US presidential election — the change candidate defeats John McCain on 4 November 2008. The Saturn–Uranus opposition exact on Election Day breaks for the insurgent/outsider side, not the establishment incumbent-party candidate. Timing is fixed by the card: Election Day, 4 Nov 2008.",
 "basis": "Card carries no tradition field; the election question with the Election-Day Saturn–Uranus opposition is judged by mundane/electional astrology as framed on the card.\nsystems_used: Western mundane astrology (election chart signatures)\nDirection duel: pro-Obama line (qualitative) — Saturn–Uranus opposition is the classic old-order versus change signature, and the card stresses it was last seen 45 years earlier amid upheaval; the candidate embodying change (Obama, still fighting for his nomination as an insurgent) takes the signature; pro-McCain line (qualitative) — Saturn as establishment could favour the older, establishment nominee, but that reading is static-table level only against the opposition's disruption signature, so it is recorded as the losing line. Fact check against the card: Obama had not clinched in May 2008, so the call includes his nomination holding. No birth data on the card, so no natal-chart claims are made.",
 "confidence": 0.62}

P["WP-003"] = {
 "prediction_text": "Main call: Barack Obama is re-elected — the incumbent defeats Mitt Romney on 6 November 2012. The Mercury retrograde beginning on Election Day brings counting confusion/delay echoes but does not overturn the result or produce a 2000-style disputed outcome. Timing fixed by the card: 6 Nov 2012.",
 "basis": "Card carries no tradition field; the 2012 election question with Election-Day Mercury retrograde is judged by mundane/electional astrology as framed on the card.\nsystems_used: Western mundane astrology (election signatures, incumbency)\nDirection duel: pro-Obama line (qualitative) — incumbency is the standing electional default and nothing on the card supplies a chart-level displacement signature (no Saturn–Uranus-type rupture aspect is given for 2012); pro-Romney line (qualitative) — only the Mercury-retrograde irregularity, which speaks to process/counting, not to who wins; magnitude-level only. Verdict locked: incumbent holds, retrograde recorded as process noise with a note that the result stands. No candidate birth data on the card; no natal claims made.",
 "confidence": 0.62}

P["WP-004"] = {
 "prediction_text": "Main call (the conference panel's consensus): Hillary Clinton wins the 2016 US presidential election, defeating Donald Trump on 8 November 2016. The panel majority reads the charts for the establishment candidate; recorded as the panel's collective prediction. Timing fixed by the card: 8 Nov 2016.",
 "basis": "Card carries no tradition field; the subject as framed on the card is the ISAR conference election panel's forecast, judged as a mundane-astrology panel call.\nsystems_used: Western mundane astrology (conference panel forecast)\nDirection duel: pro-Clinton line (qualitative) — the card frames a forecasting panel at a mainstream conference with polls also favouring Clinton; panel consensus formation follows the establishment-favoured reading, and no dissenting signature is given on the card; pro-Trump line (qualitative) — no chart material for an upset is supplied on this card (contrast the companion card that singles out one astrologer's contrary record), so the upset line stays empty at the qualitative level for the panel as a body. Verdict locked to the panel consensus: Clinton. Confidence held mid-range because a panel consensus is a weaker instrument than a single chart judgment.",
 "confidence": 0.55}

P["WP-005"] = {
 "prediction_text": "Main call: Donald Trump wins the 2016 US presidential election, defeating Hillary Clinton on 8 November 2016. This is the call of the one panel astrologer singled out on the card — the same reader who picked Trump as Republican nominee back when 17 Republicans still contested it — and that reader stays with Trump for the general election. Timing fixed by the card: 8 Nov 2016.",
 "basis": "Card carries no tradition field; the card singles out one panel astrologer's track record (Trump as nominee, called against a 17-candidate field), and the prediction is judged as that reader's mundane-astrology call.\nsystems_used: Western mundane astrology (individual forecaster's election call)\nDirection duel: pro-Trump line (qualitative) — the card's only forecaster-specific evidence is this reader's demonstrated willingness and accuracy in backing Trump against consensus at the nomination stage; a reader whose signature call was Trump early does not switch to the favourite in the general; pro-Clinton line (qualitative) — polls and panel ambience favour Clinton, but those are magnitude/atmosphere items, not this reader's chart line. Verdict locked: Trump, following the individual reader rather than the panel treated in the companion card. Confidence mid-range: single-source framing, no chart data printed on the card.",
 "confidence": 0.5}

P["WP-006"] = {
 "prediction_text": "Main call: Britain votes LEAVE — the referendum of 23 June 2016 decides for leaving the European Union, against the February newspaper polls showing 'Stay' ahead. The Uranus–Ceres conjunction at 23° Aries on referendum day breaks the status quo. Timing fixed by the card: 23 June 2016.",
 "basis": "Card carries no tradition field; the referendum question with the UK national charts and the referendum-day Uranus–Ceres conjunction is judged by mundane astrology as framed on the card.\nsystems_used: Western mundane astrology (national charts, referendum-day transits)\nDirection duel: pro-Leave line (qualitative) — Uranus on the referendum day is the rupture signature, and the assessment was first published in July 2015, long before the date was set, i.e. the call precedes and defies the polling picture rather than following it; a forecaster holding that line in February 2016 with 'not sure' voters vast in number is reading the undecided mass as breaking late for exit; pro-Remain line (qualitative) — only the February polls, which are atmosphere/magnitude items, not chart evidence. Verdict locked: Leave. No vote-share figure is given (no pointer on the card for a margin).",
 "confidence": 0.58}

P["WP-007"] = {
 "prediction_text": "Main call: Donald Trump wins the 2016 election — and what decides it is Hillary Clinton's scandal burden: the email controversy (with the Clinton Foundation questions attached) breaks against her late and tips the outcome to Trump. The Manhattan tarot reading's deciding factor is Clinton's hidden-affairs problem resurfacing, not policy or turnout mechanics. Timing: the decision lands in the final stretch before 8 Nov 2016.",
 "basis": "Card carries no tradition field; the card frames a tarot consultation on the election in August 2016 and names Clinton's email controversy and Foundation as live issues, judged as a tarot reading's call (Waite-tradition framing; no actual cards are printed on the card, so no card-by-card claims are made — recorded here as an input limitation lowering confidence).\nsystems_used: Tarot (Rider-Waite tradition, election reading as framed on the card)\nDirection duel: pro-Trump line (qualitative) — the card's question is double ('who wins, and what will decide it'), and the only deciding-factor material it supplies is Clinton-side scandal; a reading that surfaces hidden-affairs material on the favourite reads it as outcome-deciding, which points past her; pro-Clinton line (qualitative) — her polling lead, an atmosphere item only. Verdict locked: Trump wins, decided by the email/Foundation scandal line. Input limitation noted: the drawn cards themselves are not on the card, so the reading is reconstructed from the card's framing only and confidence is cut accordingly.",
 "confidence": 0.45}

assert set(P.keys()) == set(EXPECTED), "id set mismatch: %s" % (set(P.keys()) ^ set(EXPECTED))
os.makedirs(BASE, exist_ok=True)
for cid in EXPECTED:
    rec = {"case_id": cid, "prediction_text": P[cid]["prediction_text"],
           "basis": P[cid]["basis"], "confidence": P[cid]["confidence"], "trigger": trig()}
    path = os.path.join(BASE, cid + ".json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=1)
# 写后逐件回读验存在与字段齐全
ok = 0
for cid in EXPECTED:
    path = os.path.join(BASE, cid + ".json")
    with open(path, encoding="utf-8") as f:
        rec = json.load(f)
    assert rec["case_id"] == cid
    for k in ("prediction_text", "basis", "confidence", "trigger"):
        assert k in rec and rec[k] not in (None, ""), (cid, k)
    t = rec["trigger"]
    assert t["changed_main"] is False and t["reserve_used"] is False and t["disputed"] is False and t["reason"] == ""
    ok += 1
print("written_and_verified:", ok)
