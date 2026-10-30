import json, pathlib
out = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round56/predictions")
out.mkdir(parents=True, exist_ok=True)
T = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}
P = {}

P["OC-018"] = {
 "prediction_text": "方向：贵显至报业最高层而晚运逆转、终局凶险。史量才以文字/报业得大位，地位峰值在中年壬申运（金水助身任财杀、印劫得力），辛未运仍掌权但渐受政权压力；终局两运转逆：辛未运后段已现劫争与杀压，入庚午运为最低谷——庚比争、午火杀旺冲子水伤官，杀旺攻弱身，主被权势所害、横祸/暗杀之险而非安然善终。应期尺度为运/年档：窗口在庚午运初交运带（约五十五岁前后），窗口内主坐标取甲戌年一类杀印交战、戌动寅巳之年（定值置信低，运档为定值层）。子女承继不稳，报业基业身后难由子孙完整承守；病/祸位主金水受火克，肺与心血之患并列，终局之厄以祸大于病。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：八字子平（真诠格局+滴天髓旺衰合参）。四柱己卯丙子庚寅辛巳，庚金子月伤官当令，丙杀透月、己印透年成杀印链，然子水伤官克丙、庚身仅巳中根与辛劫己印，属成中有败。病药链：病＝子水伤官克丙杀兼泄身（月令）；药＝己土印化杀生身、巳中丙庚根；扶抑取向＝身弱杀旺喜印劫、忌火杀再旺。特格扫描：从格/专旺/寒极均未命中（庚有巳根印劫）。大运己阴男逆行：乙亥甲戌癸酉壬申辛未庚午；峰值三核对壬申运①申为庚禄根得地②干壬泄秀生财呼应财杀链③否决三条逐项未命中，满足度最高定峰值，庚午运干支火杀冲子、逆主线定低谷。输入残损：仅给四柱、无公历生日与出生地，起运岁数无法精算，应期止于运档+流年候选并降置信。",
 "confidence": 0.52}

P["OC-019"] = {
 "prediction_text": "方向：以学问/学术行政贵显，然中年运入险境、有横祸早逝之险。杨杏佛壬水得申根、癸比帮身，杀印相生主研究院总干事一类学术行政高位，峰值在癸丑运后段至壬子运前段（水得势任杀、名位上升）；险年不在晚年而在壬子运内：子水比劫旺冲巳火财、刑卯伤官，官杀土被水木交战，主因政治/社会活动招祸，突发横祸（枪杀之象重于病亡）。应期尺度运/年档：窗口壬子运（约四十岁前后），主坐标取酉年一类金印透而酉冲卯、子酉破之年（流年层为候选定值）。一生高峰即险运同段，贵而不能久享，子嗣承继之力薄。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：八字子平。卡面四柱癸巳丙辰壬申癸卯（卡内注他书另载全异，本例以卡面为准）。壬日辰月七杀当令，丙财透月生杀，申金印为根化杀生身，成杀印相生而财党杀为病。病药链：病＝丙火偏财党杀（月干，得巳根）；药＝申金印化杀、癸比助身；扶抑＝喜金水、忌木火土再党杀攻身。特格未命中（壬有申根癸助）。大运癸阴男逆行：乙卯甲寅癸丑壬子辛亥；木运泄秀主学问，癸丑壬子水运任杀主位升亦主祸伏。峰值核对：壬子运①子为壬旺地②干壬比呼应③否决：子冲巳（病字丙之根）非冲用神根、未合绊用干、未透忌得根，定为峰而带险。残损：无公历生日出生地，起运岁数不精算，降置信。",
 "confidence": 0.52}

P["OC-020"] = {
 "prediction_text": "方向：贵显至最高位（主席级），但身弱任重、贵盛不久，中年后运入壬申虽仍居高位，险年在该运火旺之年，主病逝于任上之象。谭延闿癸水生丑月官杀土重，两丑一己压身，赖丑中辛印暗生、乙食神制杀、丁财虽生官却亦主政务财权；格局上限至封疆/主席级（区间下限督抚、上限主席级，依据官旺成势而印藏食制），峰值运为壬申运（申金印得地、壬水助身任官，否决三条逐项未命中）。险点：庚午一类流年午火财旺生杀、冲动水根，身弱不胜财官，主心血/脾胃土压水之病发于任上。应期运/年档：窗口壬申运（约四十三至五十三岁段），主坐标午火流年。晚景无更长行运可享，身后名高而家业承继平常。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：八字子平。四柱己卯丁丑癸丑乙卯，癸日丑月正官/杀土当令，身弱（癸仅丑中余气、无水透、金印藏丑），乙食透时制杀、丁财透月。病药链：病＝丑己土官杀太过压身（月令兼日支）；药＝丑中辛金印化官生身、乙木食神制杀；扶抑＝喜金水扶身化杀，忌火土财官再旺。格局量级区间：下限封疆（官旺食制）—上限主席级（官势成、印食救应齐），落点取上限侧因卡面身份与运助。特格未命中（非从杀：有印藏食制、日主有余气根）。大运己阴男逆行：丙子乙亥甲戌癸酉壬申；水金运渐升，壬申定峰值（三核对：申印得地、壬干助身呼应、否决未命中）。残损：无生日出生地，起运不精算降置信。",
 "confidence": 0.55}

P["OC-021"] = {
 "prediction_text": "方向：军政贵显至督军/封疆级而终局落拓。陆荣廷乙木自坐卯禄，酉月辛杀旺，丙伤官透时制杀、戊财生杀，少年壬戌癸亥甲子水印运生身任杀主从军崛起，乙丑丙寅运为峰值段（丙寅运寅禄得地、丙伤制杀得用，否决三条未命中，主掌一省军政）；丁卯运翻凶：卯禄逢酉冲、丁食泄身生财党杀，翻转触发为运支卯与月支酉正冲日禄根，主失势、退居、病困而终。应期运/年档：窗口丁卯运（约六十至七十岁段），主坐标取辰年一类辰酉合绊杀、辰戌冲财库之年。格局区间下限方面大员、上限封疆，不至再上；破耗因财杀交战与兵权争夺而起，晚年财势大减。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：八字子平。四柱戊午辛酉乙卯丙戌，乙日酉月七杀当令透辛，自坐卯禄被卯酉冲，丙伤透时制杀为成格主线，戊财透年生杀为病。病药链：病＝戊土财党杀兼卯酉冲禄；药＝丙火伤官制辛杀、戌中丁辛制化；扶抑＝喜火制杀、水印生身，忌金土再旺。特格未命中（乙有卯禄寅气，非从杀）。大运戊阳男顺行：壬戌癸亥甲子乙丑丙寅丁卯戊辰；逐段方向：水印三运吉升、乙丑平升、丙寅吉峰、丁卯凶（冲禄触发已写明）、戊辰平而困。峰值三核对丙寅：①寅为乙木根地②丙干即药透出呼应③否决未命中。残损：无生日出生地，起运岁数不精算降置信。",
 "confidence": 0.55}

P["OC-022"] = {
 "prediction_text": "方向：科第不成、不由仕宦立身，以学问技艺（命学著述）成名立身。袁树珊乙木生酉月杀旺，两巳火泄、丁食透月，全局无水印——印星文书全缺为科名硬伤，屡试不第之局；食神制杀主以才学口才立业，戊财透时主以技艺求财于市。行运：丙申乙未运杀伤交战、功名蹭蹬；甲午运泄秀著述渐显；癸巳运印星癸水始透为一生学问峰值段（癸印得巳中戊制而力有限，定次峰/学峰而非官峰），主编著、授徒、名播命坛；壬辰运印临辰库，晚景以著述师名收束，寿名俱可保而官位终无。应期运档定值：科名之败贯穿丙申至乙未两运，成名窗口甲午至癸巳运。子女以官杀为子星，杀旺有子而缘分劳心；病位主木被金克、火泄，肝胆筋目与心火之患。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：八字子平。四柱辛巳丁酉乙巳戊寅，卡面注安命甲午、大运丙申起（与辛阴男逆行合）。乙日酉月杀旺，丁食制杀，无印化杀且无印主文书科名，此为格局成中有败：成在食制得技艺之名，败在印缺杀重、科第无门。病药链：病＝辛酉金杀太过（年干月支）；药＝丁巳火食伤制杀；缺药之药＝水印全缺无化杀之路；扶抑＝喜火制、水印迟来为学峰，忌金土。特格未命中（乙有寅根）。逐运方向：丙申凶平（伤官见杀申冲寅根）、乙未平、甲午吉（泄秀）、癸巳吉（印透）、壬辰平吉、辛卯凶平（杀比交战冲酉）。残损：无公历生日，起运岁数从卡面丙申起运序论、不精算年龄。",
 "confidence": 0.6}

P["OC-023"] = {
 "prediction_text": "方向：钟下所覆为已烹熟的禽类食物（一只烧/煮熟的鸡一类熟食），且已非完好全形——经烹割剖开、肉形残缺（鼎折足覆餗之象，主已动用/残损而非生鲜完整之物）。数量为一物一禽，应验对象即钟下食物本身，不落到席间任何人身上。此为射覆即时占，无应期年月可言，应点即开钟当场验看（日档即时）。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：梅花易数体用取象（托名文本、体系照用）。卡面仅给卦象火风鼎变雷风恒，未给动爻与起卦方式，残损已注并降置信：鼎为烹器之象，下巽为鸡为长形禽物，上离火主烹烧，合为禽物经火烹于鼎；变恒主其物久置已定形。鼎九四『鼎折足，覆公餗』辞义主倾覆残损（已核辞义方向为凶/损，与残缺断同向，不引吉辞反断），故断不完好。体用细分因动爻未给无法确指何卦为体，此路无据已明写，断语只据鼎/巽/离三象合参落到物品与数量（自检：具体项＝物品熟禽一物、时点即时开钟，共二项以上）。",
 "confidence": 0.3}

P["OC-024"] = {
 "prediction_text": "方向：葬资有着落、不须向外告借——亡易者生前自藏一笔金银，藏处在其日常卧处枕下与屋中窖藏一带，访者指出藏处、其家掘取即足营葬。应验对象为亡者之家与这笔藏金；应期为即时/日内档：到访当日检枕、启窖即得（窗口当日，主坐标检枕之时）。数量为一笔足以办葬的金（非巨富之财，量级守恒于一场葬事）。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：梅花易数外应/遗书预言类推断。输入残损严重：卡面未给任何卦象、动爻、外应物象，梅花体用一路无从起算，已如实注明并大幅降置信；仅可据者为占题事实链——遗书预言来访者可托身后事（主此事必有解法落在亡者自留之物上）与卡面出处题名所含『枕窖金』三字（按卡面数据读，不作外部金标），合断藏金在枕/窖。断语具体项：物品＝藏金一笔、时点＝当日、对象＝亡者之家。无卦可引辞，未引爻辞作断。",
 "confidence": 0.32}

P["OC-025"] = {
 "prediction_text": "方向：应验。椅底预书所定年月日届期，椅子被来客坐破——应验对象是椅子本身（非人对象，不回收到坐者或邵雍身上），破损方式为坐压而破（一人坐之、一椅破损，数量各一）。应期即预书原文所定的那一日（日档，主坐标为预书所书之日当天），不早不晚。坐者只受虚惊、无伤人之断（量级守恒：日常器物小事只断器破，不放大为人身灾伤）。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：梅花易数预书验占（以占题事实与预言结构作断）。输入残损：卡面未给预书的具体年月日文字、未给卦象，应期只能指回『预书所定之日』本身、无法另报日期，已注明降置信。事实优先序：占题明言预先书于椅底、届期验之，此类预书成例的结构主应验，且应验对象定位复核——承受对象（预言所指）与应验对象（象所指）同为此椅，通则(f)同一性成立。断语具体项：物品＝椅一、人物＝坐客一人、时点＝预定之日。",
 "confidence": 0.58}

P["OC-026"] = {
 "prediction_text": "方向：今年功名可成——两客中主客得中/得名（昆弟同占，榜上见名以一人为正、一人陪衬得次级名分之象），过程涉害艰难、非一帆风顺。初传未乘青龙主喜庆得地、中传亥乘螣蛇主榜前惊疑虚惊、末传卯官星乘玄武主名成而暗昧（名次不高、榜名居后段）。应期月档：窗口本年春季（木旺之季），主坐标卯月放榜/得信（初末木局逢卯值）。曲直木局官星成势是成名主据，涉害只压量级不翻方向。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：大六壬（指南仕宦/考试门）。己亥日己土，官鬼为功名类神：三传未亥卯成曲直木局即纯官之势，初传未藏乙官乘青龙（一级据：入传乘吉将），末传卯官乘玄武降一档作名次暗昧。课式涉害主涉险迟滞。应期三路：逢值（卯值月）取为主坐标；逢冲合（亥卯未合局已成、合处即卯）同指卯不另取；出空填实（辰巳空不涉官星卯）此路无候选已明写。盘面不全守第八节：无四课全列与年命，两客年命未给，昆弟分判只到主次层级、名次细数无据不报，降置信。",
 "confidence": 0.5}

P["OC-027"] = {
 "prediction_text": "方向分三线：①北上此行不得意——无禄无路凶格加末传亥青龙落空（刖足无果），主诏命虽至而行程无功：或中途受阻、或到而不得其位，终须南返，窗口本冬内、主坐标亥月后出空交丑月见定局（月档）。②身体：辛金得酉比辰印之助，无大病之断，但水泄金寒主劳顿惊扰、途中防寒病小恙，量级止于病扰不至危。③老母：父母辰土居中传乘太阴，土印不空主母在家尚安，太阴暗昧主有病忧牵挂而无危亡之象；应验对象逐名对回——行之成败落方替夫本人，母安一线落其母，不相混。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：大六壬（仕宦+出行门，一课多占分线）。辛未日辛金，课式无禄（四上克下、无禄无依）、无路皆凶格主向；三传酉（兄弟六合）辰（父母太阴）亥（伤官青龙、甲子旬亥空），末空为刖足。仕宦类神官鬼不入传（二级以下），只作虚望背景不作得官据，合LR-QY-2缺传降权。母线取父母辰入传乘太阴为据。应期：落空者先取出空填实（亥出甲子旬、丑月填实向）为主坐标，逢值亥月因仍在空期舍之，逢冲合无合路无候选已明写。盘面不全：年命与母年命均未给，行年路无据已注，降置信。",
 "confidence": 0.52}

P["OC-028"] = {
 "prediction_text": "方向：考选得官，且得京职言路一类——斫轮成器、印绶俱全之格，主入觐考选后授给事中一类科道文书官（朱雀居中传主文书言责），非外任州县。过程重审先迷后利：初传卯官乘玄武主初时暗昧有人情阴私之扰，中传戌朱雀主文书定局，末传巳印乘白虎主授命带兵/刑名色彩而官终得。应期月档：窗口寅卯之月，主坐标卯月（初传卯官逢值定授）。等级为京官中级言官，不至部堂大位（量级守恒于考选初授）。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：大六壬（仕宦/选举门）。己丑日己土，官鬼卯木为类神居初传（一级据），课式斫轮按方法篇构成『卯发用而中戌末巳，印绶俱全、爵禄崇高』与本盘三传卯戌巳逐位合；重审主先迷后利。朱雀乘戌居中主文书言责，故官职落科道言官层级，具体官名细断在盘面不全时已降一档为类别断。应期三路：逢值卯月取主坐标；逢冲合（卯戌合在传内主定局、合处仍指卯戌不另立坐标，作合参舍为备选已注）；出空填实（午未空不涉三传）无候选已明写。盘面不全守第八节，无四课全列与年命，降置信。",
 "confidence": 0.5}

P["OC-029"] = {
 "prediction_text": "方向逐事分判（一课多占）：①顷刻客至：即时有三客至，其中有杨姓者（此线取象无注文，只作低置信事件报）。②其子求官：不宜在外求，宜回山东本省取功名（干神归支、传将逆行主归乡得名）。③方所兵动：三传纯官鬼、虎鬼克支，主山东有兵动、攻城陷邑之变，应期冬月（月档）。④母寿：母年近九十，寿止八十九——以发用乙与地盘己合断八九之数，主寿限即在八十九岁之年（年档），为诸事中最重一线。⑤失盗：已有失盗之事，所盗为其子之物，且课传回环主贼去而复来——目今防盗，三日内贼复至（日档，主坐标三日）。总方向：家门多事之课，子功名一线独吉，余线以兵变与母寿为凶重。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：大六壬一课多占（方法篇第六节第13条逐事分门，本盘形态与该条成例形态同构）。己亥日，涉害曲直回环；三传未（白虎）卯（六合）亥（天后）成亥卯未木局，于己土日为纯官鬼——按一象多用分判：纯官专主方所兵动不作子求官之官旺断；回环格专主失盗贼复来不作他事吉断；母寿用发用合字专法（乙己合断八九）为例外专法已注明，一般父母年命路因母年命只给甲子年、寿数由此合断。应期逐事各从其门档位：客至即时、失盗日档、兵动月档、母寿年档。盘面不全守第八节，客至一线取象无据已标低置信。",
 "confidence": 0.6}

P["OC-030"] = {
 "prediction_text": "方向分两问：①淮扬巡按差可复——铸印课占钦差主复任巡按，初传巳乘太常为印绶炉火、中传戌乘六合为印体合就，主差复设且有人得任其事；②吏书缺可照旧——中末六合、太阴主旧缺经一番暗中更动后仍照旧存留，不废缺、亦不升格，属『名虽议改、终归照旧』。应期月档：窗口春季辰巳之月，主坐标巳月（初传巳印逢值、铸印炉火得值而印成）。两问总方向皆偏成，巡按复设一线证据强于吏书照旧一线。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：大六壬（章奏/钦差门）。戊子日戊土，课式铸印按方法篇构成戌加巳发用乘太常主有官必迁、占钦差主复任巡按（方法篇第12门钦差细断明载此格此用）；三传巳（太常，官鬼/印链）戌（六合）卯（太阴，戊日官星居末），官星入传乘太阴作照旧暗存之据（二级据降档使用）。应期三路：逢值巳月取主坐标；逢冲合（戌卯六合在传主合就、合处指卯戌与主线同向作备选舍注）；出空填实（卡面未给旬空落处）此路无据已明写。盘面不全守第八节：无四课全列、空亡未给，吏书一线只到方向层级，降置信。",
 "confidence": 0.58}

P["WP-001"] = {
 "prediction_text": "Direction: Yes — a major worldwide pandemic in 2020–2021. A fast-spreading respiratory, influenza-like infectious disease will become the defining collective affliction of the period, with mass illness and elevated mortality across many countries, beginning as the Jupiter–Saturn–Pluto conjunction perfects in early 2020. Timing (year scale): window 2020–2021, main coordinate early 2020 (the exact conjunction). Social/economic shutdown-level disruption accompanies it, not a minor seasonal outbreak.",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：Western mundane astrology (outer-planet cycles / cyclical index). Card-given configuration only: five outer planets within ~100 degrees, Jupiter–Saturn–Pluto conjunction exact early 2020, cyclical index at its 21st-century low, and the card's own comparanda clusters (1918, 1954, 1968, 1982) which the setting links to pandemic-type years (1918 influenza explicitly in the historical series). No natal chart is involved; input is complete for a mundane-cycle judgement as framed. Confidence reflects the configuration's extremity (lowest index of the century) per the card.",
 "confidence": 0.7}

P["WP-002"] = {
 "prediction_text": "Direction: Barack Obama wins the 2008 US presidential election (defeating John McCain). The Saturn–Uranus opposition perfecting on Election Day reads as the old order (Saturn, the older establishment candidate) broken by the change candidate (Uranus): an insurgent, first-of-his-kind winner rather than the continuity choice. Timing: decided on election day, 4 November 2008 (day scale, the date is given in the card). Margin read as clear rather than a disputed recount outcome.",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：Western mundane/election astrology. Input residual noted: no candidates' natal charts are given in the card, so the judgement rests only on card facts — Obama's momentum in the nomination race, McCain as presumptive establishment nominee, and the Saturn–Uranus opposition beginning on Election Day, a configuration the card itself flags as last seen 45 years earlier (a generational turnover signature). Confidence lowered for the missing charts, per astro reference input requirements.",
 "confidence": 0.58}

P["WP-003"] = {
 "prediction_text": "Direction: Barack Obama is re-elected in 2012, defeating Mitt Romney. Mercury turning retrograde on election day (6 November 2012) reads as a repeat/return signature — the incumbent returns to office — with counting and reporting delays and post-election disputes over details, but not a reversal of the result itself. Timing: election day 6 November 2012 (day scale, given), result confirmed after a slower-than-normal count within the retrograde window.",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：Western mundane/election astrology. Input residual: no natal charts for either candidate are given; judgement rests on card facts only — incumbency, a competitive but not leading challenger position in polling, and Mercury retrograde beginning on election day, classically a 'return to the previous state / recount' signature applied here to the incumbent's return. Confidence lowered for missing charts.",
 "confidence": 0.58}

P["WP-004"] = {
 "prediction_text": "Direction: The Costa Mesa conference panel's consensus prediction is Hillary Clinton to win the 2016 US presidential election over Donald Trump. The panel majority aligns with the polling favourite (Clinton); the forecast is a Clinton victory declared on/after election day, 8 November 2016 (day scale, given). This records the panel-as-subject's collective call, which is what the card asks.",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：Western mundane/election astrology (panel consensus as the subject). Input residual: the card gives no charts, no individual panellists' votes and no vote split; the only hard facts are that most polls favour Clinton and that a forecasting panel was held. A conference panel consensus in that setting most plausibly ratifies the frontrunner. Confidence lowered: the panel's exact split is not in the card and cannot be reconstructed from the method references.",
 "confidence": 0.48}

P["WP-005"] = {
 "prediction_text": "Direction: Donald Trump wins the 2016 US presidential election. The subject of this card is the one panel astrologer who, against a 17-candidate Republican field, had already picked Trump for the nomination — the same contrarian read is carried through to the general election: Trump, not the polling favourite Clinton, takes the White House on 8 November 2016 (day scale, given). The astrologer's earlier against-the-field accuracy is the card's signal that this out-of-consensus call is the prediction to record.",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：Western mundane/election astrology (individual forecaster as subject). Distinction from the panel-consensus card: this card's setting singles out one astrologer's demonstrated contrarian hit (Trump as nominee from a 17-person field); per fact-priority, that individual track record, not the majority/polling position, is the operative fact for this case. Input residual: no charts and no quoted wording of the astrologer's general-election call are given, hence confidence held below 0.6.",
 "confidence": 0.52}

P["WP-006"] = {
 "prediction_text": "Direction: Britain votes to Leave the European Union in the referendum of 23 June 2016. Uranus conjunct Ceres at 23 degrees Aries on referendum day reads as a sudden, disruptive break with the existing order — the electorate chooses rupture over continuity, against the February polling lead for 'Stay' and against the large undecided bloc breaking late toward Leave. Timing: the referendum day itself, 23 June 2016 (day scale, given), result known that night/next morning.",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：Western mundane astrology (national charts + election-day transits). Card facts used: referendum date fixed at 23 June 2016, Uranus–Ceres conjunction at 23° Aries on the day (disruption/break signature), UK national charts (1066/1801/1922) available in the original assessment, and the assessment being 'firmed up' in February — a firmed contrarian call against the Stay polling lead. Input residual: the card does not reproduce the national-chart analysis itself, so the judgement rests on the transit signature and the stated firming-up; confidence lowered accordingly.",
 "confidence": 0.55}

P["WP-007"] = {
 "prediction_text": "Direction: Donald Trump wins the 2016 election, and what decides it is Hillary Clinton's email/Foundation controversy. The tarot reader's call, as framed by the card's own question ('what will decide it'), points to the scandal returning as the late decisive blow to Clinton — a damaging revelation/renewed investigation in the final stretch before 8 November 2016 swings the outcome to Trump. Timing: decided in the closing phase of the campaign, late October to election day 8 November 2016 (day/month scale).",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：Tarot (Waite/RWS) as the card's stated method. Input severely residual: the card gives NO drawn cards, spread, positions or reversals — a Waite reading cannot be reconstructed and no card meanings are invented here, per the tarot reference (no reading without the actual draw). The prediction therefore rests only on card facts: the question's own framing asking what will decide it, and the setting's pointed inclusion of the Clinton email controversy and Clinton Foundation as already-public controversies in August 2016 — under fact-priority these are the operative anchors. Confidence substantially lowered for the missing spread.",
 "confidence": 0.42}

for cid, d in P.items():
    d2 = {"case_id": cid, "prediction_text": d["prediction_text"], "basis": d["basis"], "confidence": d["confidence"], "trigger": T}
    with open(out / f"{cid}.json", "w", encoding="utf-8") as f:
        json.dump(d2, f, ensure_ascii=False, indent=1)
print(len(P))
