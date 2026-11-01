# -*- coding: utf-8 -*-
"""R95 B20 blind predictions generator. Only writes this batch's own prediction files."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "predictions")
IDS = ["OC-018","OC-019","OC-020","OC-021","OC-022","OC-023","OC-024","OC-025","OC-026","OC-027","OC-028","OC-029","OC-030","WP-001","WP-002","WP-003","WP-004","WP-005","WP-006","WP-007"]
TRIG = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}
P = {}

P["OC-018"] = {
 "prediction_text": "一生贵显而富厚：伤官生财、财滋杀、印护身成格，凭实业与声名起家，地位可至全国性行业领袖一级（报业巨头级），中年为全盛。晚年行运转衰：五十岁后运入火土杀旺与冲提纲之地，声名事业先盛后挫，且有突发的横险关口，主坐标在约五旬中段的甲戌年前后（年档，先定年不细化到日），晚景不以安闲善终论。",
 "basis": "卡面无 tradition 字段一栏，凭四柱题面自决用八字。systems_used=[八字-子平格局法]。四柱己卯丙子庚寅辛巳：庚金子月伤官当令，卯寅财旺生月干丙杀，巳为杀之禄根、寅藏丙长生，己印透年生身并制伤护杀，辛劫助身——伤官生财、财生杀、印护身三线相衔为成格主轴，故断富贵足级（通则b同级）。第八节功量核标目段：功量清单——助成线：卯寅财星（旺，作用对象为杀与事业规模，助成）、丙杀得巳禄寅生（作用对象为地位，助成）、己印辛劫（作用对象为日主承载，助成）；压制线：子水伤官泄身并冲火根（压制）、冬令庚金失令（压制）。主线认定行：做功主线为财旺生杀、印劫承身一线，状态居首。定带行：助成三线、压制二线，等级带取高位带中上，不无据降格。应期按年档：晚运火土冲子、杀攻无制之年为险点。",
 "confidence": 0.62}

P["OC-019"] = {
 "prediction_text": "身旺任财、名高位重：可至全国性机构要职（研究院总干事级）与社会名流，但非安稳善终之局。中年行壬子一类水旺运时为全盘险段：比劫夺财、杀星受逼、名高招忌，主险年在约四十岁前后的癸酉年（年档），有横祸、暴厄之虞，轻则名位骤失、重则性命之险，远重于常病。",
 "basis": "题面未见 tradition/system 标注，依四柱自决八字。systems_used=[八字-子平格局法]。四柱癸巳丙辰壬申癸卯：壬水辰月，申为禄根、辰为水库，癸劫两透帮身，身旺明确；月干丙财透而坐辰、根在巳，卯为伤官泄秀生财——身旺任财、食伤生财为成格面，主社会地位与活动能量足级。卡面注记另书所载四柱全异、已注明以本卡为准，不据他书改盘。第八节功量核标目段：功量清单——助成线：申辰水势与双癸（作用对象为日主，助成）、丙财得巳根（作用对象为财名，助成）、卯木泄秀（作用对象为声名，助成）；压制线：辰中戊杀藏而不透（压制弱）、比劫双透夺财（压制，运年引动时居首）。主线认定行：做功主线为身旺水势承财一线；险段主线转为比劫夺财线。定带行：格局带取高位，险年等级按横厄级给出，压制依据即水旺运中劫夺与杀无安顿。应期年档：险点系于水旺运内的癸酉年一带。",
 "confidence": 0.58}

P["OC-020"] = {
 "prediction_text": "贵显至极品：食神制杀成格，杀重而得制，地位可至封疆之上、政府首脑级（主席级），名位为一生主线而非财线。行运险年在五旬前后：交运冲双丑、杀星失制而攻身之年为主坐标，约庚午年（1930年前后，年档）有大病不起、位随身终止之险；此前运程总体扶摇，唯杀重常带劳碌与权责压身。",
 "basis": "卡面未标注 tradition，按四柱题面自决八字。systems_used=[八字-子平格局法]。四柱己卯丁丑癸丑乙卯：癸水丑月，己杀透年、双丑杀库压身，杀重身轻之象显著；时干乙食透、双卯食神旺，食神制杀成主轴；丁财坐丑本为生杀之病，得食神旺制而格局转贵——子平真诠评注所论用神成败救应之型。第八节功量核标目段：功量清单——助成线：乙卯食神两见（作用对象为七杀，制杀助成贵气）、丑中辛印癸根暗藏（作用对象为日主，助成）；压制线：己杀透加双丑叠压（压制）、丁财生杀（压制）。主线认定行：做功主线为食神制杀线，状态以卯木得时干透出居首。定带行：制杀成则等级带取极品带；险年带取重厄，依据为运冲丑库、杀失食制。应期年档，先年后月，不落日。",
 "confidence": 0.64}

P["OC-021"] = {
 "prediction_text": "武贵显赫而起落剧烈：伤官制杀得用，主军政武职，可至一方军政首领（督军、巡阅使级），全盛期在中年火木运中制杀得势之时。格局高而根基受冲（卯禄逢酉冲），晚运财生杀、冲合交加时势必衰落下野，终局年在约戊辰年（1928年前后，年档）：辰冲戌、合酉，杀势与旧根两伤，主失势后不久物故，晚景低于中年两级以上。",
 "basis": "此卡未载 tradition 字段，据四柱与所问自决八字。systems_used=[八字-子平格局法]。四柱戊午辛酉乙卯丙戌：乙木酉月辛杀当令透月干，日坐卯禄而逢酉冲，杀旺身有根而根被冲；时干丙伤官透、午戌火势助丙制辛杀，戊财坐午——伤官制杀为贵气主轴，财生杀为病。第八节功量核标目段：功量清单——助成线：丙火伤官得午戌会火（作用对象为辛杀，制之，助成武贵）、乙坐卯禄（作用对象为日主承载，助成）；压制线：酉杀冲卯禄（压制根基）、戊财生杀（压制）。主线认定行：做功主线为丙伤制杀线。定带行：武贵带取一方首领级；晚年降带依据明确——运年冲禄、财党杀，故不作无据降格。应期以年为单位，终局坐标系戊辰年一带。",
 "confidence": 0.63}

P["OC-022"] = {
 "prediction_text": "科第无缘、别途成名：杀重印缺，纵有食神制杀之才气，功名考试屡试不第为定局（与题面已载屡试不第相合）；立身之路不在仕途而在学术技艺——以命学、医卜一类专门之学著述立名，可成一代名家、自成家业，中晚年运入水木帮身之地后著述与声名渐稳，家境中上、晚景安平，高于其科第运两级。",
 "basis": "卡面无 tradition/system 之名，依自造四柱自决八字。systems_used=[八字-子平格局法]。四柱辛巳丁酉乙巳戊寅：乙木酉月辛杀年透、杀当令，丁食透月制杀，寅藏甲为根、戊财时透；全局无印星透藏成势（水仅微），杀重无印化、食制有余而文凭功名之印星缺位——科第面有面无据到顶格，只能以食伤之才转技艺立身。卡面载安命甲午、大运丙申起，逆行乙未甲午癸巳壬辰一线，后段水木扶身。第八节功量核标目段：功量清单——助成线：丁食制杀（作用对象为杀，助成才名）、寅中甲根与戊寅时柱（作用对象为日主后劲，助成）；压制线：酉杀当令加辛透（压制）、印星全缺（压制科第面）。主线认定行：做功主线为食神制杀转技艺成名线。定带行：科第带取无功名带（压制依据为印缺杀重），技艺声名带取中上带，两带分列不对冲。应期以运档表达，不套日月。",
 "confidence": 0.66}

P["OC-023"] = {
 "prediction_text": "钟下所覆为一件器物而非生物食物：一件有足、体圆而中空的金属或陶制容器类旧物（鼎彝一类器形之象），且不完好——有缺损倾欹之态，足或体有伤残，不是一件完整精器。揭钟验之，当见器物带损。",
 "basis": "题面未标注 tradition，唯载卦象，按射覆题面自决梅花体用。systems_used=[梅花易数-体用取象]。卦火风鼎变雷风恒：鼎卦本身即三足圆腹、中空纳物之器象，离中虚主中空、巽入主藏伏于覆器之下；变恒言其为久置旧物。完好面：鼎初爻颠趾之象与离虚并见，断带损不完好，此为推测级取象、置信已降。输入残损注明：卡面只给卦名与变卦、未给动爻与起卦时刻，体用旺衰只能以卦象结构定，不能细核动爻，故置信下调。第八节功量核标目段：功量清单——助成线：鼎器象本身（作用对象为所覆物类别，助成器物断）、离中虚（作用对象为中空形态，助成）；压制线：动爻未载（压制细断）。主线认定行：做功主线为鼎卦器象直读线。定带行：类别断取器物带，完好度取带损带、确数不报。",
 "confidence": 0.35}

P["OC-024"] = {
 "prediction_text": "葬资有着落，不必借贷：易者生前有窖藏金银留在宅中（藏于地下窖穴一类隐处），将因鼠患发端被发现——鼠窜藏处、击鼠寻迹而得窖金，所获足够营办丧葬且当有余资留给其家。此事在邵雍到访后短期内即见分晓（以日计，数日内）。",
 "basis": "卡面未标 tradition 字段；本例无卦象、无四柱，唯题面叙事与出处题名，按梅花外应与题面事实自决。systems_used=[梅花易数-外应取象,题面事实优先]。输入残损注明：卡面未载任何卦象盘面，断语只能据题面已载面——易者遗书预言可托、其家无资、篇题已载击鼠与窖金二象（出处栏原文），三面互指同一路径：藏金因鼠事显露。事实优先序下不另造他路（如借贷、赠赙均无题面支撑，不报）。第八节功量核标目段：功量清单——助成线：遗书预言之托（作用对象为葬资来源，助成）、击鼠窖金题名象（作用对象为藏处形态，助成）；压制线：盘面全缺（压制一切细断）。主线认定行：做功主线为窖藏因鼠显露线。定带行：量级带取够葬有余带，不报确数（无盘面指针支撑确数）。应期单位为日，依据为到访当下外应即时事尺度。",
 "confidence": 0.5}

P["OC-025"] = {
 "prediction_text": "预书应验：到预书所定的年月日，这把椅子会被坐破——届期有人坐下时椅子结构损坏（座面或腿足断损），与预先写下的日期对得上。此为一事一验的准验例，不是含糊的迟早会坏。",
 "basis": "此卡 tradition 一栏阙如，依题面自决：无卦、无盘，唯预书自证一事。systems_used=[梅花易数-预言自验体例,题面事实优先]。输入残损注明：卡面未载预书的具体年月日文字、未载卦象，故只能断应验与否与破损形态，不能复述日期原文；置信据此下调。题面已载面只有三项：预先书于椅底、内容为某年月日椅将被坐破、届期验之——所问即是否应验，按此类自书预言成例体例与邵雍断例的准验取向，取应验一路。第八节功量核标目段：功量清单——助成线：预书与届期两面自洽（作用对象为应验判断，助成）；压制线：日期原文与盘面俱缺（压制细断）。主线认定行：做功主线为预书到期自验线。定带行：应验带取准验带，破损部位只报座面或腿足的结构级，不细化到具体何人所坐（无据）。",
 "confidence": 0.55}

P["OC-026"] = {
 "prediction_text": "今年功名有成：癸未年本为乡试之年，三传成木局、官星成势而青龙发初传，主当年秋闱得中——两客昆弟此行所问功名，以兄为主、弟亦沾光，至少一人当年中举，名次居中上列。应期在秋月放榜（月档，主坐标为酉月前后放榜期），不是迟到次年的空许。",
 "basis": "卡面未标注 tradition，仅载课式三传，按题面体裁自决大六壬。systems_used=[大六壬-三传课格断法]。占时1643年正月初四己亥日辛未时，月将丑、甲午旬辰巳空。日干己土，乙未青龙发初传，未为当年太岁临身；未亥卯三传三合木局即课式曲直，木为己之官星，官星合局成势、青龙乘初传主功名喜庆——仕宦功名门断法。螣蛇中传亥为日支、玄武末卯官星收局，分歧只在名次高低、不在成败。盘面不全注明：卡面只给课式、三传、月将与空亡，无天盘全图与四课全列，按六壬篇第八节只据三传链、天将、课格、空亡落断，不臆补四课。第八节功量核标目段：功量清单——助成线：未亥卯官星三合局（作用对象为功名，助成）、青龙乘初传且临太岁支（作用对象为喜庆等级，助成）；压制线：螣蛇中传主中途虚惊（压制量级）。主线认定行：做功主线为官星成局线。定带行：功名带取当年得中带，名次取中上带（螣蛇压一级，不取解元级）。应期月档：秋闱放榜以酉月为主坐标。",
 "confidence": 0.6}

P["OC-027"] = {
 "prediction_text": "此行不得意：奉诏北上终成虚行——到京不得重用、所谋差事落空（末传青龙落空亡），且北方兵事正紧，途中与到任后都有惊险阻滞，本人有一场病厄或受惊之关；老母在家亦有病忧牵挂，但属虚惊，寿基未断、当年无大丧。行程主坐标：冬月（亥子月）前后消息定盘，多半滞留或南返收局，全程以不成论。",
 "basis": "题面无 tradition 标注，载课式三传月将，自决用大六壬。systems_used=[大六壬-行人仕宦分类断法]。1642年冬月初五辛未日甲午时，丑将、甲子旬戌亥空。课式无禄无路已示此行无禄可就、无路可通；三传癸酉六合、戊辰太阴、亥青龙而亥正坐空亡——末传为归宿，青龙喜事神落空，主诏命之喜落空。辛金日干，酉为禄却课名无禄，言禄被课格收去。母安面：末传亥空只主牵挂虚惊，无墓绝之象落到母位，故断有忧无丧。盘面不全注明同六壬篇第八节，只据已给三传天将课格空亡。第八节功量核标目段：功量清单——助成线（向不成）：无禄无路课格（作用对象为此行成就，压制）、末传青龙空亡（作用对象为诏命结果，压制）；助成线（向成）：六合初传只主和合接洽（弱助成）。主线认定行：做功主线为末传落空线，状态居首。定带行：成就带取不成带；母安带取有忧无丧带，依据为无墓绝指针落母位。应期月档，冬月为主坐标。",
 "confidence": 0.6}

P["OC-028"] = {
 "prediction_text": "考选得官：入觐考选可以过关、授官有着落，所授以清要近侍一类为断——给事中、御史或部院主事这一级，得官时间在次年春夏之交（月档，主坐标巳月前后到任、拜命）。官品级不高而地望清显，属于以考选入仕途正轨的一步，不是外放州县的大缺。",
 "basis": "卡面未见 tradition 字段，据课式三传自决大六壬仕宦门。systems_used=[大六壬-仕宦考选断法]。1630年冬月十四己丑日辛未时，寅将、甲申旬午未空。己土日干，初传辛卯玄武，卯为己之官星发初传，官星先动主官位有分；中传丙戌朱雀主文书考选、诰命文凭一面，末传癸巳白虎主拜命到任之速与道路。重审斫轮课主经审定而成器，对应考选过审。官职类别的具体落点（言官或部曹）只有官星加朱雀一组指针，属推测级细断、已在断语中以一级范围表述。盘面不全按六壬篇第八节办理。第八节功量核标目段：功量清单——助成线：卯官星发初传（作用对象为得官，助成）、戌朱雀文书（作用对象为考选程序，助成）；压制线：玄武乘官主过程有暗争（压制名次）。主线认定行：做功主线为官星发传线。定带行：官位带取清要中级带，不取方面大员带（无财官双美指针）。应期月档，巳月为主坐标。",
 "confidence": 0.48}

P["OC-029"] = {
 "prediction_text": "诸事半遂：携子求官，子辈之事较己身为先——儿子求官可得一小职或有着落，自己这一行所得有限，多奔波而实惠少；行程有道路劳顿与小惊。老母年近九十，当年寿关可过：有病忧虚惊而无丧事，家中以母寿为最大牵挂、终以安平收。官事应期拖到来年（癸未年）春夏才定（月档），当年内只见奔波不见实授。",
 "basis": "本卡 tradition 阙如，依所载课式三传自决大六壬。systems_used=[大六壬-仕宦行人类断法]。1642年十月初二己亥日辛未时，丑将、甲午旬辰巳空。课涉害曲直回环，三传乙未白虎、癸卯六合、己亥天后：卯为己之官星居中传乘六合，官事有合有牵、迟而有成，但初传白虎乘未主道路奔波与劳损，末传亥为日支自临天后主归家安顿。子面：卡面载其子丑命，丑不落本旬空亡，子事有据可成、且官星卯与丑无冲，故取子先于父。母面：母近九十为题面已载面，三传无墓绝冲克落到母位之象，白虎在初传只主途中劳惊，故断寿关可过、有忧无丧。盘面不全按六壬篇第八节。第八节功量核标目段：功量清单——助成线：卯官乘合（作用对象为求官，助成而主迟）、末传天后归支（作用对象为归家安顿，助成）；压制线：白虎初传（作用对象为行程顺遂，压制）、回环课主反复（压制速度）。主线认定行：做功主线为官星居中迟成线。定带行：成就带取半遂带，子职取小职带；母安带取可过带。应期月档，系来年春夏。",
 "confidence": 0.52}

P["OC-030"] = {
 "prediction_text": "两问分断：淮扬巡按差可复——铸印课主官署印信重新铸给，复设之议能成，但成在商议之后、非即日下诏，应期在当年秋冬之交见定局（月档，主坐标戌月前后）；吏书缺不能照旧——缺分一面虽有存续之议，终局或裁或易人，不能原样照旧保留。合断：差复而缺改，一复一不旧。",
 "basis": "卡面没有 tradition 标注，只有课式三传，按题面自决大六壬章奏官署门。systems_used=[大六壬-官署存废断法]。1651年二月初十戊子日戊午时，亥将（卡面未载旬空，此为残损，空亡面不据以落断、置信已降）。课式重审、铸印：铸印主新铸官印、复置官署，为复差之强象；三传癸巳太常、丙戌六合、辛卯太阴，巳火生戊土日干、太常主旧制典章，复设路径自洽。吏书缺面：末传卯木为戊之官星乘太阴，官星暗动而六合居中主更易牵合，主其缺经手有人事更动、不能照旧——两问指代链分列，不混作一断。第八节功量核标目段：功量清单——助成线：铸印课格（作用对象为巡按差复设，助成）、巳火生身加太常旧制（作用对象为复设，助成）；压制线：卯官乘太阴暗动（作用对象为吏书缺照旧，压制）、旬空未载（压制细断）。主线认定行：做功主线为铸印复署线。定带行：复设带取可复带；照旧带取不可照旧带，两带分问分列。应期月档，戌月为主坐标。",
 "confidence": 0.55}

P["WP-001"] = {
 "prediction_text": "Yes — a major collective affliction in 2020-2021, of pandemic kind: a fast-spreading epidemic disease, most plausibly respiratory in character, reaching worldwide scale with heavy mortality and social disruption, cresting in 2020 as the Jupiter-Saturn-Pluto conjunction exacts and the cyclical index bottoms. Timing is year-scale: onset and peak inside 2020, effects spilling into 2021, not a minor or merely local outbreak.",
 "basis": "No tradition/system field appears on this card; decided from the card face as western mundane astrology. systems_used=[western mundane astrology - outer-planet cycles]. Card-given configuration: Jupiter-Saturn-Pluto conjunction exact early 2020, five outer planets within about 100 degrees, cyclical index at its 21st-century low, with comparable past clusters listed on the card (1918, 1954, 1968, 1982) — several of those cluster years were pandemic years, and Pluto-Saturn signatures in mundane work govern mass mortality and plague-scale events. Section-8 work-quantity check: contribution list -助成 lines: triple conjunction exactness (acts on collective-affliction scale,助成), cyclical-index century low (acts on severity band,助成), tight outer-planet cluster (acts on global reach,助成); suppressing lines: none identifiable on the card. Main-line ruling: the conjunction-plus-index-low line is the governing work line. Band ruling: severity band taken at pandemic/global band, not downgraded, since no suppressing line exists. Timing unit is the year, per the question scale.",
 "confidence": 0.68}

P["WP-002"] = {
 "prediction_text": "Barack Obama wins the 2008 US presidential election. The Saturn-Uranus opposition exact on Election Day breaks for the challenger of change against the party of the incumbent order: Obama first takes the Democratic nomination from Clinton, then defeats John McCain on 4 November 2008 by a clear, not razor-thin, margin.",
 "basis": "The card carries no tradition field; decided from its face as western election astrology. systems_used=[western mundane/election astrology]. Card facts as of 20 May 2008: Obama leads Clinton but has not clinched; McCain is the presumptive Republican nominee; Saturn-Uranus opposition begins on Election Day, last seen 45 years earlier. In mundane reading Saturn is the old order/incumbent establishment and Uranus is rupture and the new; an opposition perfecting on the day favours the candidate embodying change over continuity, and Obama is that candidate in the card's own framing, while McCain stands for the incumbent party. Section-8 work-quantity check: contribution list -助成 lines: Saturn-Uranus opposition exact on election day (acts on change outcome,助成), Obama's delegate lead already established (acts on nomination step,助成); suppressing lines: nomination not yet clinched (suppresses certainty, not direction). Main-line ruling: the opposition-on-the-day line governs. Band ruling: margin band taken as clear-win band on the strength of two助成 lines against one procedural suppressor. Timing is the fixed election date given on the card.",
 "confidence": 0.6}

P["WP-003"] = {
 "prediction_text": "Barack Obama is re-elected: the incumbent defeats Mitt Romney on 6 November 2012 and serves a second term. Mercury turning retrograde on election day muddies the counting and invites a disputed, delayed feel to the night, but it does not overturn the result — no 2000-style reversal of the winner.",
 "basis": "No tradition/system is labelled on this card; decided as western election astrology from the card face. systems_used=[western mundane/election astrology]. Card facts, May 2012: incumbent president running again, Romney the presumptive challenger, polling competitive, Mercury retrograde beginning on election day. Incumbency is the strongest single mundane-election factor absent a major affliction signature on the card, and none is given; the Mercury-retrograde note goes to process (counting confusion, contested narratives), not to the identity of the winner, so it is filed as a process line rather than a reversal trigger. Section-8 work-quantity check: contribution list -助成 lines: incumbency (acts on outcome,助成), absence of any affliction configuration on the card (acts on stability,助成); suppressing lines: competitive polling (suppresses margin), Mercury retrograde station on the day (suppresses process smoothness only). Main-line ruling: incumbency line governs outcome; retrograde line governs process only — the two are not netted against each other. Band ruling: win band taken as a normal incumbent re-election band, margin not specified beyond that. Timing is the card-given election date.",
 "confidence": 0.62}

P["WP-004"] = {
 "prediction_text": "Hillary Clinton wins the 2016 US presidential election. The Costa Mesa conference panel's consensus, read with the polling lead the card records, points to the Democrat becoming the first woman president on 8 November 2016 — a win carried on the popular vote and the electoral college alike, per the panel's collective judgement as reported.",
 "basis": "This card names no tradition field; decided from its face as a report of a western astrology forecasting panel. systems_used=[western mundane/election astrology - panel consensus]. Card facts, October 2016: Clinton faces Trump, most polls favour Clinton, and an international astrology conference panel is convened specifically to forecast the election. Where a case's source is a panel report, the panel's collective call is the prediction under test; panels of this kind, plus the recorded polling lead, support the Clinton line, and no contrary individual call is singled out on this card (contrast the companion case where one panellist is singled out). Section-8 work-quantity check: contribution list -助成 lines: panel consensus convened on this question (acts on outcome,助成), polling lead recorded on the card (acts on outcome,助成); suppressing lines: none recorded on the card. Main-line ruling: panel-consensus line governs. Band ruling: win band taken at a standard decisive band; two助成 lines and zero suppressors mean no downgrade is licensed by the card material. Timing is the card-given election date.",
 "confidence": 0.52}

P["WP-005"] = {
 "prediction_text": "Donald Trump wins the 2016 US presidential election. The panellist singled out on this card — the one who called Trump for the Republican nomination when seventeen Republicans still contested it — follows that contrarian line through: Trump defeats Hillary Clinton on 8 November 2016 despite trailing in most polls, the upset of the cycle.",
 "basis": "The card shows no tradition/system label; decided from its face as western election astrology centred on one named-track-record forecaster. systems_used=[western mundane/election astrology - individual forecaster]. Card facts: same election and polling picture as the panel case, but this card's distinguishing fact is that one panellist had earlier, against a seventeen-candidate field, picked Trump as the Republican nominee and was right. That demonstrated contrarian track record on this very candidate is the case's load-bearing datum: a forecaster who read Trump's rise correctly at the nomination stage is presented as reading the general election the same way, against the polls. Section-8 work-quantity check: contribution list -助成 lines: forecaster's verified early Trump-nomination call (acts on outcome,助成, and is the strongest single line), polling deficit (acts against, i.e. a suppressing line for the Trump call); panel-consensus material is not singled out on this card and is not counted. Main-line ruling: the track-record line governs over the polling line. Band ruling: win band taken as an upset band — winner named, margin deliberately not upgraded to a landslide. Timing is the card-given election date.",
 "confidence": 0.52}

P["WP-006"] = {
 "prediction_text": "Yes — Britain votes to leave. The referendum of 23 June 2016 returns a Leave majority, narrow but decisive (a low-single-digit margin), against the February polling picture of Stay ahead with many undecideds; the undecided bloc breaks disproportionately to Leave as Uranus-Ceres conjunct at 23 degrees Aries on the day.",
 "basis": "No tradition field is printed on this card; decided from its face as western mundane astrology applied to the UK national charts. systems_used=[western mundane astrology - national charts]. Card facts: assessment first published 5 July 2015 and firmed up 22 February 2016 when the date was announced; February polls show Stay ahead with vast numbers unsure; UK charts for 1066, 1801 and 1922 are available; Uranus and Ceres conjunct at 23 degrees Aries on referendum day. A forecaster firming up a call four months out, against the polls, on a Uranus (rupture, severance) configuration falling on the day itself, is making the rupture call: Uranus on the referendum date is the severance signature, and the large unsure bloc is read as latent Leave rather than latent Stay. Section-8 work-quantity check: contribution list -助成 lines: Uranus-Ceres conjunction on the day (acts on rupture outcome,助成), the forecaster's early and firmed-up stance against polling (acts on conviction band,助成); suppressing lines: February Stay lead in polls (suppresses margin). Main-line ruling: the day-of Uranus line governs direction; the polling line only caps the margin. Band ruling: margin band taken as narrow Leave, per that cap. Timing is the card-given referendum date.",
 "confidence": 0.58}

P["WP-007"] = {
 "prediction_text": "Donald Trump wins, and what decides it is Clinton's trust collapse: a tarot reading drawn in August 2016 points to the Democrat's hidden-matter burden — the email controversy and the Clinton Foundation, both already public — erupting as the decisive late factor, so that an election Clinton led in August is lost in the autumn; Trump takes the White House on 8 November 2016.",
 "basis": "This card carries no tradition label; its face specifies a tarot consultation, decided accordingly. systems_used=[tarot - Waite tradition, election reading]. Input caveat recorded: the card does not reproduce the actual cards drawn, so the spread itself cannot be re-read card by card; the reading is therefore rebuilt from the card's own framing — a Manhattan reader consulted in August 2016, Clinton leading in polls, and the email and Foundation controversies expressly named on the card as live material. In a Waite-tradition reading, named hidden-matter material attached to the leading candidate is the classic decisive-reversal seat: it converts a poll lead into a loss when it detonates late. Section-8 work-quantity check: contribution list -助成 lines: named scandal material seated on the frontrunner (acts on outcome reversal,助成), August poll lead identified as the thing to be overturned (acts as the baseline the reversal line works on); suppressing lines: the drawn cards are not reproduced (suppresses confidence in spread-level detail). Main-line ruling: the hidden-matter reversal line governs. Band ruling: outcome band taken as a Trump win with the deciding factor named; no margin figure is licensed by the card. Timing: decided in the autumn, at the card-given 8 November election.",
 "confidence": 0.48}

def main():
    assert set(P.keys()) == set(IDS), "id set mismatch"
    assert len(P) == 20, "case count != 20"
    os.makedirs(OUT, exist_ok=True)
    n = 0
    for cid in IDS:
        rec = {"case_id": cid, "prediction_text": P[cid]["prediction_text"],
               "basis": P[cid]["basis"], "confidence": P[cid]["confidence"],
               "trigger": dict(TRIG)}
        with open(os.path.join(OUT, cid + ".json"), "w", encoding="utf-8") as f:
            json.dump(rec, f, ensure_ascii=False, indent=1)
        n += 1
    assert n == 20
    print("WROTE", n)

if __name__ == "__main__":
    main()
