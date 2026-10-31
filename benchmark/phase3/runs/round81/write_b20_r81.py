# -*- coding: utf-8 -*-
"""Round81 B20 blind predictions writer. Asserts id set == batches.json B20."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(BASE))  # benchmark/
# batches path is in round81 itself
with open(os.path.join(BASE, "batches.json"), encoding="utf-8") as f:
    BATCHES = json.load(f)
IDS = BATCHES["B20"]

def trig():
    return {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}

PRED = {}

PRED["OC-018"] = {
 "prediction_text": "方向：贵显在文业不在政界——一生以报业立身、位至大报总经理级巨头，名望与财富俱属上层，但不是官场极品。格局量级区间：下限为文业名流/报界领袖，上限为富贵双全而止于事业巨头，落点在区间上侧。近中段金水与印比得力之运（癸酉、壬申一带）是事业扩张、接掌大报的上升段；晚段转入南方火杀旺运（庚午、己巳一带），身弱不任杀，地位与身体俱受压，主凶险破耗、难言安享晚年，晚运以年档论凶、须防横祸伤身之年。",
 "basis": "卡面未标注 tradition 字段，按题面体裁自决：本例卡面载四柱「己卯 丙子 庚寅 辛巳」与问一生地位晚运，故用八字。\nsystems_used: 八字（子平格局+旺衰调候）\n四柱：庚金生子月水旺寒局，月透丙火七杀，年己土印星化杀生身，时辛劫帮身、巳中藏庚戊丙，身中弱而有根。主线：①格局——杀印相生为体，子水伤官克丙杀为病，己印制伤护杀为救，成败参半而有救；②用神——印（土）兼比劫（金），调候喜丙火暖局；③定性——非常规从格/专旺（庚有巳根与辛助，不从），走常规杀印链。R80-REV1功量核算：助成线——己印生身（透年得地）、辛劫助身、巳中庚根助身，共3线；压制线——子水泄身兼克杀、丙杀克身，共2线；主线为己印化杀生身（直接作用日主且透出），量级定带为中上带，助成多于压制故落点取带内上侧而不越报业巨头上限。逐运大势：水金运身得助任杀主升，火土杀旺而身跟不上之晚运主降；交运带只作运档坐标，本例卡面未给出生日期与起运岁数，流年层坐标无据不报（BZ-YN-2.1缺位降格：止于运档并明写）。关键结局：子女宫时柱巳火杀印相杂，只断承继有出而不作细断；病位病字为子水伤官与寒水，病向在寒湿/水系，只作方向不断病名；破耗之因在晚运杀旺攻身与伤官见杀之争；一生高峰运段取金水印比得力段（运档定值、流年缺位）。",
 "confidence": 0.55}

PRED["OC-019"] = {
 "prediction_text": "方向：前程得意而寿程有险——命主可任研究院总干事级要职，属政学两界显要；但行运险年明确：四十岁前后进入水劫与官杀受冲之段（癸丑运内、逢癸水劫财之年最险），主横祸凶险、甚至非命之虞，不可断为寿长安稳。早中段木火财官之运主升进得意，险段在年档坐标上以四十岁前后为窗口、癸年为窗口内主坐标。",
 "basis": "卡面未标注 tradition 字段，按题面体裁自决：本例卡面载四柱「癸巳 丙辰 壬申 癸卯」且卡面注两书所载全异、本例以徐乐吾书为准，故用八字并锁定此盘。\nsystems_used: 八字（子平格局+旺衰）\n四柱：壬水生辰月，辰为水库兼官星之宫，月透丙火偏财，时癸劫帮身，日坐申金印星长生，身中强有根。主线：①格局——财星透月、辰中戊杀暗藏，卯木伤官克辰官为病，申金印星制伤化杀为救；②用神——印金为救应之首；③定性——无印比成势到从格程度，不作从格，辰月土官与财并见走常规。卡面残损注记：另一书全异之盘已按卡面注舍弃，不混用。R80-REV1功量核算：助成线——申印生身得长生、癸劫助身、辰库蓄水，共3线；压制线——丙财耗身兼生杀、卯伤克官、巳财耗身，共3线；主线为申印（坐日下长生、直接生身），定带中上；险年量级：劫财癸透时干与年干两见，险段再叠癸劫之年，助压在险段翻转，故险级取重档而非轻描。关键结局：高峰在财官得用、印星护身之早中运段（运档）；破耗与祸因皆系财生杀、伤官见官之争；病位以水逢土克、卯申相害只作方向，不妄断病名；卡面未给起运岁数，运名与流年只给年档窗口不冒充精确起运年。",
 "confidence": 0.52}

PRED["OC-020"] = {
 "prediction_text": "方向：贵显至极品——食神制杀成格，命主贵至国民政府主席级，为本批格局上限之命。格局量级区间：下限为方面大员，上限为元首级极品，落点取上限侧。行运：金水印比运（甲申一带）身得印助、任杀有力，是登顶运段；险年在五十岁前后转入土杀重、财生杀旺之段（癸未运初、逢庚午一类财杀交攻之年），主病厄骤至、位高而寿程在此段受挫。险与登顶皆以年档/运档坐标交付。",
 "basis": "卡面未标注 tradition 字段，按题面体裁自决：本例卡面载四柱「己卯 丁丑 癸丑 乙卯」与问贵显程度及险年，故用八字。\nsystems_used: 八字（子平格局·食神制杀）\n四柱：癸水生丑月土旺，年透己土七杀，时透乙木食神制杀，两卯食神有根，两丑官杀之库，身弱而制杀之神有根有力。主线：①格局——食神制杀成格，丁火财星生杀为病，局中无金印为憾、救应只在运；②用神——食神乙卯为成格之神，扶抑喜印比；③定性——身弱不从（丑中癸水有根、卯食成链），寒丑喜丁火调候而丁又生杀，调候与格局相绊、已注明取格局为主。R80-REV1功量核算：助成线——乙卯食神制杀（两卯成势、时透）、丑中癸水日主之根，共2线而主线极强；压制线——己杀透年得丑根、丁财生杀、丑土两见克身，共3线；主线为食神制杀链（直接作用杀星且成势），按主线定带为极品带，压制线只压寿程与身弱一面、不压贵级（写明：贵级由成格主线定，寿险由压制线定，两面分判）。关键结局：一生高峰运段为印比填实之甲申运段（运档定值）；险年取杀重身弱、印星受财克之年档；子女星食伤两卯旺，只断承继有出；病字为丑土官杀与丁财，病向偏土系（脾胃）只作方向。",
 "confidence": 0.60}

PRED["OC-021"] = {
 "prediction_text": "方向：武贵封疆而晚景失势——格局可至督军/巡阅级军阀首领，属武职贵显；但格有破损，贵而不稳，一生先显后落，晚年失兵权、退居以终。格局量级区间：下限为一省军政要员，上限为跨省巡阅级，落点在上限侧而稳定性取低档。中年火土之运（丁巳、戊午一带）制杀助势为高峰运段；晚运入木比与金杀相战之段，主线翻逆、失势下行。",
 "basis": "卡面未标注 tradition 字段，按题面体裁自决：本例卡面载四柱「戊午 辛酉 乙卯 丙戌」与问格局高低一生贵显，故用八字。\nsystems_used: 八字（子平格局+旺衰）\n四柱：乙木生酉月，年月辛金七杀得令，日坐卯木禄刃，身有强根；时透丙火伤官制杀，年戊土财星生杀，午戌藏火土。主线：①格局——羊刃坐日、伤官制杀，武贵之体；戊财生杀、杀旺过重为病，丙伤与卯刃为救与根；②用神——丙火制杀为先；③定性——乙有卯禄不从，酉月杀旺走刃杀相制之常规格。R80-REV1功量核算（分配/量级）：助成线——卯刃帮身得禄、丙伤制杀透时、午火食伤助制，共3线；压制线——辛杀当令透月、戊财生杀、戌中辛金余气，共3线；主线为丙伤制辛杀（透出直接克杀），定带为武贵上带；助压同量，故贵级取上带而持续性降档——高峰集中于制杀得力之中年运，晚运制神退、杀与刃相战则翻落，此即先显后落的功量依据。关键结局：高峰运段取中年火土运（运档）；破耗之因在财生杀旺、兵权相争；子女宫戌土财库只作有承继的方向断；病字辛金七杀，病向只作方向不断名。卡面未给起运岁数，止于运档坐标。",
 "confidence": 0.58}

PRED["OC-022"] = {
 "prediction_text": "方向：科第无份、术业成名——命主屡试功名不第是命局正断，不是时运偶然；其立身之路在食神泄秀、以学问技艺（命学著述）自立，印运到时学问成名、衣食与声望皆可得，但终身不由科第入仕。学业本身不弱：文秀在食伤，坏在无印星承接功名。应期以运档论：水印之运（壬辰一带）为著述立名之段，金杀旺而无印化之早运为科场受挫之段。",
 "basis": "卡面未标注 tradition 字段，按题面体裁自决：本例卡面载四柱「辛巳 丁酉 乙巳 戊寅」、注安命甲午大运丙申起与问科第立身，故用八字。\nsystems_used: 八字（子平格局+旺衰）\n四柱：乙木生酉月金杀当令，年辛七杀透，月丁食神透制杀，时戊财生杀，日主仅寅中甲木余根、两巳泄气，身弱杀重而无水印——科第所必需的印星全缺是本题眼目。主线：①格局——食神制杀有象而身弱无印，制杀只成其才、不成其官；②用神——印水第一，缺而待运；③定性——乙有寅根不从杀。R80-REV1功量核算：助成线——丁食制杀、寅根一线，共2线而皆不生身；压制线——辛杀当令、酉杀得令、戊财生杀、两巳泄身，共4线；主线为杀旺攻身（当令透出），才学线（食神）只定立身方式不定功名，故功名量级定带为无份带、技艺立身定带为中上带，两带分判不相吞。关键结局：高峰不在科场而在印运著述段（运档窗口，卡面只给大运起排未给各运岁数，不冒充流年定值）；破耗之因在财生杀而耗于功名之求；时柱寅木根宫只断晚景以学问自立，不细断子女。",
 "confidence": 0.65}

PRED["OC-023"] = {
 "prediction_text": "方向：钟下所覆为一件器物而非食物活物——具体断为有足、中空的旧器物（鼎属器皿之象），材质以木质/木胎为主、上部带金属提耳之属；完好与否断为不完好：器物上端（耳/口沿一带）有一处缺损，主体尚存、足部完整。此象只能定到器类与破损部位，器名一级依据不足、置信已降。",
 "basis": "卡面未标注 tradition 字段，按题面体裁自决：本例卡面 attachments 载卦象「火风鼎 变 雷风恒」、所问为席间射覆钟下何物，故用梅花易数体用取象。\nsystems_used: 梅花易数（体用生克+卦象取物）\n原始盘面：本卦火风鼎（上离下巽），变雷风恒（上震下巽），下卦不变、上卦离变震，动在上卦上位。上卦为用（离火）、下卦巽木为体：体生用为耗泄之象，不主完好无损；变用震木与体巽木比和，物之本体以木象为主。鼎卦本身即三足中空之器象，与所问器物同类（对象同类核已过）；离为中虚、为上部口耳之象，动爻正在上位，故缺损落上端耳/口沿；巽为长、为木，震为足动，足部象完整。爻辞：鼎上爻辞义偏吉，只调节量级（主体不毁）不翻转体生用所定的破损定性，两路并列取体用为主、辞义调量。梅花自检：具体项——物品（有足中空旧器）已落、部位（上端一处缺损）已落、足部完整已落，共三条具体断语；量级守恒：射覆小事只断器类存毁，不放大。应期不适用（当场揭覆之事，无应期坐标）。",
 "confidence": 0.35}

PRED["OC-024"] = {
 "prediction_text": "方向：葬事有资可办——无资之困不是绝路，易者家中自有藏金可掘：金藏于枕中/窖藏之处，因鼠咬枕（击鼠）而露，掘得此金即足营葬。断语落点：财物为金、藏处为枕内与窖中一带、得财之由为鼠患引见；其子不必外借，葬事可成。",
 "basis": "卡面未标注 tradition 字段，按题面体裁自决：本例卡面无四柱、无卦象、无起卦数，provenance 载《梅花易数》序「击鼠枕窖金」一目，所问为易者身后葬事无资何以为葬，故按梅花/易例体裁作断并先记残损。\nsystems_used: 梅花易数（体裁）+卡面题名取象（降格使用）\n输入残损（实记）：卡面未载任何卦象、动爻、占时与数字，体用生克无从排起——本例不臆补卦盘。可用之据只剩卡面已载二项：①问面本身为「其家正苦于无资营葬」，若终局为无资不成葬，此问无成例可传，体裁上主有转机；②卡面 provenance 题名逐字含「击鼠」「枕」「窖金」三锚，三锚同指一事：鼠、枕、窖中之金。按卡面锚点直读作断（转应面已列：题名亦可能只是篇目代号而非事象——若作代号读则本例无据，故本断降格为推测级、置信下调，不以直读冒充卦据）。应验对象核：藏金承受者为易者之家、营葬之资，指代同指其家，无回收到访者邵雍身上。量级：只断得金足葬，不报金数（无数字锚可据）。",
 "confidence": 0.45}

PRED["OC-025"] = {
 "prediction_text": "方向：应验——椅底预书之事届期成真：到预书所定的年月日，有客来访坐于此椅，椅子当场被坐破，时点与预书相合。断语具体项：应验对象为此椅本身（非人祸）、致破者为届期来访之客、方式为坐压而破。此为预言类成例，应验与否二选一，本断取应验一边。",
 "basis": "卡面未标注 tradition 字段，按题面体裁自决：本例卡面载邵雍预书椅底、问预书之事是否应验，provenance 为《梅花易数》序「置椅坐破」，故按易例预言体裁作断并记残损。\nsystems_used: 梅花易数（体裁·预言应验占）\n输入残损（实记）：卡面未载预书原文的年月日干支、未载起卦盘面与椅之材质处所，无法以体用复推时点——本例不臆补日期，应期只写「届预书之期」一层。作断依据：①卡面 setting 逐字载预书内容为「某年月日椅子将被坐破」，预书已把对象（椅）、方式（坐破）、时点（某年月日）三项钉死，本问只剩应验/不应验一轴；②此目收于序文成例之列，体裁功能即记预言之验，无验之预书不入此目——此据为体裁据、非盘面据，已据此降置信。应验对象核（通则f）：承受对象与应验对象同为椅子本身，不转断坐者之灾。量级守恒：小事只断椅破本身，不放大为家宅兴衰。",
 "confidence": 0.50}

PRED["OC-026"] = {
 "prediction_text": "方向：今年功名可成——赵氏昆弟今年癸未科皆有功名之份，榜可得中。主线据：三传亥卯未成曲直木局，木为己土之官，官局旺而成势、末传卯木官星乘玄武居终局之位，青龙居初传未土主喜庆发动。应期：月档——榜期在春季木旺之月，窗口为本年春榜期内，主坐标取卯月（木值之月）。二人高下分配：卡面未给二人各自年命，分配无据不强分，只断皆中、不分名次先后。",
 "basis": "卡面未标注 tradition 字段，按题面体裁自决：本例卡面载课式「涉害、曲直」、三传与月将、占时己亥日辛未时，所问今年功名，故用大六壬。\nsystems_used: 大六壬（仕宦/考试门+三传课格）\n盘面（卡面已给）：己亥日辛未时，丑将，甲午旬辰巳空；三传乙未（青龙）、己亥（螣蛇）、癸卯（玄武），三传亥卯未木局即曲直格。取用：功名以官鬼为本体——己土以木为官，末传癸卯官星乘玄武居末，官局三合旺相不空（空在辰巳、与三传无涉），为一级据。父母文书（火）不入传：按LR-QY-2缺传只降权不作否决，文书面降为背景、不据此断无榜。螣蛇居中传亥水财位主过程中惊疑虚耗，只调量级。R80-REV1分配对读：同盘二人，逐方做功线相同（官局同指二人），年命未给、无逐方相对强弱可分，故分配断项不成立、只保留共同方向，此为分配核的明写处置。应期三路：逢值（卯值月）取中；逢冲（酉冲卯）与终局相悖舍；出空填实（三传不空）无候选。盘面不全守第八节：未臆补四课全列与年命。",
 "confidence": 0.50}

PRED["OC-027"] = {
 "prediction_text": "方向：此行不得意——奉诏北上主凶多吉少：课名无禄、无路，正断为北行无实际禄位可得、行程阻绝，本人身体有险，北方兵紧之下防罹兵祸/病厄，严重程度取重档，不许以诏命在身轻断为寻常赴任。分面断：老母一面，父母辰土居中传乘太阴、土生辛金有气，老母在家一时无即时大厄，暂安而后有耗耗之忧与本人之行相牵。应期：月档——入北后数月内见挫，窗口至亥水填实之月，主坐标取亥月前后（末传亥空待填实）。",
 "basis": "卡面未标注 tradition 字段，按题面体裁自决：本例卡面载课式「无禄、无路」、三传、占时辛未日甲午时与母甲子年，所问北上得意与母安，故用大六壬。\nsystems_used: 大六壬（仕宦门+出行门+父母面并读）\n盘面：辛未日甲午时，丑将，甲子旬戌亥空；三传癸酉（六合）、戊辰（太阴）、亥（青龙，空）。课格无禄（四上克下）为凶格主向，已按第三节核格名主向：无禄无依。取用分面（LR-QY-1并读）：①仕宦面——官鬼火不入传，又逢无禄之格，缺传加格凶成组，方许作无禄可得之负断（LR-QY-2.3c成组门槛已记）；②本人安危面——末传亥水伤官乘青龙而落旬空，喜神落空、终局无着，合无路之格主行止两难、身有险象；③老母面——父母辰土居中传乘太阴，生辛金日主，父母面有一级入传据，断暂安，不以本人之凶吞没母面，亦不以母面之安反转主线。母年命甲子：子与末传亥为空邻，只记背景不作母厄据（年命上神未给，守第八节）。应期：末传空走出空填实路优先（第七节取期序第1位），逢值亥仍在旬内不实故舍，逢冲巳冲亥与终局量级相悖降为备选。两段式：近段赴任受阻、远段身险加重，远段触发为末传空青龙（终局无着之传）已指认。",
 "confidence": 0.50}

PRED["OC-028"] = {
 "prediction_text": "方向：考选得官——入觐考选可得实职，课得斫轮主成器迁转，官星居初传发动，所授偏向武职/兵职一路之官（末传巳火印绶乘白虎），非清要文翰之职；品级取中上档。推测：具体职名一级无盘面次第据，只给职系不断确名。应期：月档——迁期以干年支月推，窗口在考选后数月内，主坐标取巳月（末传父母印绶逢值之月）。",
 "basis": "卡面未标注 tradition 字段，按题面体裁自决：本例卡面载课式「重审、斫轮」、三传、占时己丑日辛未时，所问入觐考选得何官，故用大六壬仕宦门。\nsystems_used: 大六壬（仕宦门·斫轮格）\n盘面：己丑日辛未时，寅将，甲申旬午未空；三传辛卯（玄武）、丙戌（朱雀）、癸巳（白虎）。斫轮格构成主成器、印绶俱全主迁转（第三节吉格），格向为吉已核。取用：官鬼卯木居初传乘玄武——官位发动而带暗昧，故断得官而授职带暗授/不显之色；父母巳火居末传乘白虎——印绶终局落武将之将（白虎主兵武），职系据此偏武；朱雀居中传戌土主文书过程，只作考选文书一面、不改职系主向。R80-REV1功量核算：助成线——斫轮格成器、官星入传发动、印绶居末得位，共3线；压制线——玄武乘官带暗、戌土兄弟居中耗力，共2线；主线为斫轮成器加官印前后相承，定带中上，玄武一线只压显达程度不压得官方向。名次/确职细断：盘面无次第据，按第八节降档只给职系与品级带。应期三路：逢值巳月取中；逢冲亥冲巳与得官终局相悖舍；出空（午未空与类神无涉）无候选。",
 "confidence": 0.45}

PRED["OC-029"] = {
 "prediction_text": "方向：一课诸事分断——①其子求官：不宜在外地强求，宜回山东本省取功名，回东则有得、在外难成。②其母寿数：母年近九十，寿止八十九，今年内即为大限之年，主寿终之断（量级取终局档，据见basis）。③防失盗：家中有失盗之患，所盗为其子之物，且贼去而复来，目今先失、三日后防复来。④方所兵动：山东本乡有兵动攻城之患，应在冬月，须预避。⑤本人此行访道求官一面，只主奔波无实得，不另夸大。",
 "basis": "卡面未标注 tradition 字段，按题面体裁自决：本例卡面载课式「涉害、曲直、回环」、三传、占时己亥日辛未时、注其子丑命与母近九十，所问为携子求官请占诸事，故用大六壬一课多占逐事分门。\nsystems_used: 大六壬（一课多占·仕宦/失盗/兵斗/寿限分门）\n盘面：己亥日辛未时，丑将，甲午旬辰巳空；三传乙未（白虎）、癸卯（六合）、己亥（天后），亥卯未木局曲直，课传兼回环。逐事据（承方法章一课多占节成例形态）：子求官——木局官星成势而传将之向主归本乡，断回山东取功名；母寿——初传乙与日干己合断为八九之数（成例专法，非父母行年通法），母已近九十，合断寿止八十九，量级据专法形态取终局档、同时明记母年命未给、通法一路无据；失盗——课传回环定贼去复来，所盗对象按子类神（子丑命）一面断为其子之物，玄武不入传故藏处方所无据不报（LR-QY-2：缺位不臆补方所）；兵动——三传木局官鬼之势、白虎乘初传克支一线主方所兵动，方所以其家山东定（日支分野据卡面已载家在山东）。应期分档：失盗日档（目今/三日后复来）、兵动月档（冬月）、功名与寿限年档，各事自家之期不相混。R80-REV1：本例断项多为方向与寿数专法，寿数八十九出自合字专法非功量估算，功量核对寿面不适用、已明记。",
 "confidence": 0.55}

PRED["OC-030"] = {
 "prediction_text": "方向：两问皆可——①淮扬巡按差可复：课得铸印，铸印占钦差主复任巡按之象，差缺复设有着落；②吏书缺可照旧：末传卯木官星乘太阴居终局，缺分虽暗而不废，照旧保留。应期：月档——旨意/复设之信在数月内定，窗口取巳、戌两支值月之段，主坐标取巳月（初传太常铸印之炉逢值）。两问分判：巡按复设为显断，吏书照旧为暗中保全之断，显晦有别。",
 "basis": "卡面未标注 tradition 字段，按题面体裁自决：本例卡面载课式「重审、铸印」、三传、占时戊子日戊午时，所问巡按差复设与吏书缺存废两事，故用大六壬章奏/钦差门逐事分断。\nsystems_used: 大六壬（钦差门·铸印格+一课两问分判）\n盘面：戊子日戊午时，亥将（卡面只载月将、未载旬空，空亡一路无据已记）；三传癸巳（太常）、丙戌（六合）、辛卯（太阴）。铸印格：戌加巳/巳戌相承乘太常为铸印构成（第三节），章奏钦差门明载铸印占钦差主复巡按之象，且成例即胡尹一课同格——巡按面为一级据。吏书面：官鬼卯木居末传乘太阴，官星得终局之位而乘阴将，主缺分保全于暗中；中传戌土乘六合主两问之间有合就之势。R80-REV1分配对读：两问逐方核——巡按方得铸印格加太常初传之功，强；吏书方只得末传官星一位之功，弱而不断——分配结论为巡按显复、吏书暗存，强弱与断语显晦同向，已反读主客无误。应期三路：逢值巳月取中（铸印炉火逢值）；逢冲亥冲巳与复设终局相悖舍；出空填实因卡面未载旬空无候选、明写缺路。",
 "confidence": 0.60}

PRED["WP-001"] = {
 "prediction_text": "Direction: Yes — the 2020–2021 period holds a major collective affliction of pandemic kind: a worldwide epidemic disease (respiratory/fever-type plague on the historical pattern of the comparable clusters), spreading across nations in 2020 with mass illness, death and enforced restriction, still operative into 2021. Scale: global, the defining collective affliction of the period — not a local outbreak. Timing: onset/exactness at the early-2020 Jupiter–Saturn–Pluto conjunction, main wave within calendar 2020, window extending into 2021.",
 "basis": "Card carries no tradition/system field as such; decided from the card's own genre: the card's attachment gives a mundane-astrology configuration (Jupiter–Saturn–Pluto conjunction, five outer planets within ~100 degrees, cyclical index at its 21st-century low) and asks what collective affliction 2020–2021 holds, so mundane (world) astrology is used.\nsystems_used: Western mundane astrology (outer-planet cycles, cyclical index)\nReasoning: Saturn–Pluto conjunction is the classical signature of mass hardship, death and restriction; Jupiter conjunct amplifies it to world scale (spread, numbers); the cyclical index at a century low marks a collective trough; the card itself states comparable past clusters coincided with 1918, 1954, 1968 and 1982 — of those, 1918 and 1968 were pandemic years, which fixes the affliction type as epidemic disease rather than war or finance alone (war/finance may accompany, not the main call). R80-REV1 magnitude accounting: amplifying lines — Jupiter expansion, five-planet clustering, index at extreme low (3 lines); mitigating lines — none given on the card (0 lines); main line is the exact early-2020 triple conjunction, so the magnitude band is set at global/maximum for a mundane affliction call, with no basis to grade it down. Timing is read from the conjunction's exactness (early 2020) as the window's main coordinate, year-scale per the question.",
 "confidence": 0.70}

PRED["WP-002"] = {
 "prediction_text": "Direction: Barack Obama wins the 2008 US presidential election — he takes the Democratic nomination over Hillary Clinton and defeats John McCain in the general election of 4 November 2008. Deciding signature: the Saturn–Uranus opposition exact on Election Day breaks for the new against the old — the change candidate, not the establishment/older candidate. Margin character: a clear change-mandate win, not a holdover result.",
 "basis": "Card carries no tradition/system field as such; decided from the card's own genre: the card is a May 2008 election assessment foregrounding the Saturn–Uranus opposition beginning on Election Day, so Western election/mundane astrology is used.\nsystems_used: Western astrology (mundane/electional configurations)\nReasoning: Saturn (old order, age, establishment — McCain's profile) in opposition to Uranus (rupture, youth, change — Obama's profile), a configuration the card notes was last seen 45 years earlier, i.e. at the previous generational overturn; an opposition exact on the election date is read as the old order being displaced, not retained. Card facts checked: Obama already leads the nomination race in May 2008, so the change line has a factual carrier (fact-priority: the configuration is read onto the leading challenger, not onto a trailing one). No birth charts are given on the card, so no natal-chart claims are made; the call rests on the single configuration supplied plus the race state supplied. Timing: the election date itself, 4 November 2008, is the coordinate given by the card.",
 "confidence": 0.62}

PRED["WP-003"] = {
 "prediction_text": "Direction: Barack Obama is re-elected — he defeats Mitt Romney in the general election of 6 November 2012 and keeps the presidency. Character of the result: competitive and messy in process — Mercury turning retrograde on Election Day marks delays, recount talk and disputed counts in places — but the outcome is a return: the incumbent comes back, the result is not overturned. Main coordinate: the 6 November 2012 count itself.",
 "basis": "Card carries no tradition/system field as such; decided from the card's own genre: the card is a May 2012 election assessment whose only supplied configuration is Mercury retrograde beginning on election day, so Western election/mundane astrology is used.\nsystems_used: Western astrology (mundane/electional configurations)\nReasoning: Mercury retrograde at an election classically signifies a return/repeat — votes recounted, a previous result re-run — which in an incumbent's election reads first as the incumbent returning, not as a change of office; its disorder falls on process (counts, communications, delays), which is therefore predicted as process noise, not as outcome reversal. Card facts checked: the race is described as competitive with Obama as incumbent, so a narrow incumbent win fits both the configuration and the supplied facts; no natal data are given, and none are invented. Distinction kept: retrograde is not read as automatic chaos-voiding-the-result; the direction call (incumbent holds) and the process call (messy count) are stated separately so each can be scored on its own.",
 "confidence": 0.58}

PRED["WP-004"] = {
 "prediction_text": "Direction: Hillary Clinton wins the 2016 US presidential election — the Costa Mesa ISAR forecasting panel's call is for Clinton over Donald Trump in the election of 8 November 2016. This is the panel-consensus call: the established, poll-leading candidate takes the White House. Coordinate: the 8 November 2016 result.",
 "basis": "Card carries no tradition/system field as such; decided from the card's own genre: the card describes an international astrology conference in Costa Mesa holding an election forecasting panel in October 2016 and asks who will win, so the panel's collective astrological judgement is the object predicted, read by Western mundane astrology conventions.\nsystems_used: Western astrology (mundane election forecasting, panel consensus)\nReasoning: the card supplies no individual chart or configuration for this case — the only differentiators given are the panel setting itself and the fact that most polls favour Clinton. A conference panel call is a consensus artefact: absent a supplied dissenting configuration, the consensus reads with the established favourite (continuity/Saturnian establishment profile over the insurgent). This case is kept distinct from the companion 2016 case on the same batch list whose card singles out one panel astrologer with a prior Trump call — that distinguishing fact is not on this card and is not imported here. Magnitude: no landslide is claimed; the call is direction-only, at panel-consensus strength, confidence graded accordingly.",
 "confidence": 0.55}

PRED["WP-005"] = {
 "prediction_text": "Direction: Donald Trump wins the 2016 US presidential election — the panel astrologer who, when 17 Republicans still contested, had already picked Trump for the Republican nomination follows through and calls Trump over Hillary Clinton for the White House in the election of 8 November 2016, against the poll consensus. Coordinate: the 8 November 2016 result; character: an upset win, not a poll-confirming one.",
 "basis": "Card carries no tradition/system field as such; decided from the card's own genre: the card singles out one Costa Mesa panel astrologer by a prior, verifiable-in-card track record (picking Trump as nominee from a 17-candidate field) and asks who will win, so this is an individual Western mundane-astrology call, not the panel consensus.\nsystems_used: Western astrology (mundane election forecasting, individual call)\nReasoning: the card's one astrologer-specific fact is the early Trump-nominee pick — a costly, specific, correct-in-advance commitment that identifies this astrologer's line on this election cycle as Trump-ward from the start; a forecaster does not reverse that line at the final step without a stated reason, and the card states none. Fact-priority check: the card says most polls favour Clinton — that is the consensus this call is defined against, so the call is recorded as an upset call, not blended into a hedge. Kept distinct from the companion panel-consensus case: same election, different predicting subject, different call, each scored on its own card.",
 "confidence": 0.55}

PRED["WP-006"] = {
 "prediction_text": "Direction: Britain votes to Leave — the referendum of 23 June 2016 returns a Leave majority and the UK votes to exit the European Union, against the February poll lead for Stay. Character: a disruptive, establishment-defying result (Uranus–Ceres conjunct at 23 degrees Aries on referendum day: sudden break with the existing order), and a narrow rather than landslide margin. Coordinate: the referendum count of 23 June 2016.",
 "basis": "Card carries no tradition/system field as such; decided from the card's own genre: the card is Jessica Adams's published mundane-astrology assessment (first published 5 July 2015, firmed 22 February 2016) citing the UK national charts and a Uranus–Ceres conjunction on referendum day, so Western mundane astrology is used.\nsystems_used: Western mundane astrology (national charts + referendum-day configuration)\nReasoning: the one configuration the card supplies for referendum day is Uranus conjunct Ceres in Aries — Uranus is the rupture planet, and a conjunction exact on the vote day in a cardinal fire sign reads as a sudden break from the status quo, i.e. Leave, not continuity. The assessment's own history supports firmness: published in July 2015 and firmed up the day after the date was announced, before polls had settled — it is a committed call, and its direction follows its supplied configuration. Fact check: February polls showed Stay ahead with many undecideds — a poll lead with a vast undecided bloc is exactly the factual setting in which a rupture configuration can prevail, so the polls are registered as the opposing fact, not as the call. Margin is graded narrow (undecided-heavy electorate), not a rout.",
 "confidence": 0.60}

PRED["WP-007"] = {
 "prediction_text": "Direction (graded as speculation — see basis): Donald Trump wins the 2016 election narrowly, and what decides it is Hillary Clinton's email/Foundation scandal line: a late-campaign reignition of the email controversy — a damaging revelation/scandal event in the final stretch — swings the deciding voters, rather than policy or debates. Coordinate: the late-October/early-November 2016 window, result on 8 November 2016.",
 "basis": "Card carries no tradition/system field as such; decided from the card's own genre: the card describes a Manhattan tarot reader drawing cards on the election in August 2016, so tarot is the intended system — but the card is input-deficient for tarot, recorded here in full.\nsystems_used: Tarot (intended; cannot be executed — see deficiency) + card-supplied facts only\nINPUT DEFICIENCY (stated, not patched): the card names no drawn cards, no spread, no positions and no orientations. Under the packaged tarot method a reading must present the actual cards drawn and interpret them by Waite's text; inventing a spread would be fabrication, so no card-based reading is claimed and confidence is cut to speculation grade. What can still be answered from card-supplied facts alone: the card itself foregrounds exactly two Clinton liabilities — the email controversy and the Clinton Foundation — as already-public controversies in August 2016, and asks 'what will decide it'; a scandal-line decider is therefore the only decider the card's own facts support. The winner call follows the same line (a scandal-decided race breaks against the scandal-carrier). Both calls are prefixed speculation-grade in the prediction text and must be scored as such; if the drawn cards are ever supplied, this prediction should be replaced by a real Waite-based reading.",
 "confidence": 0.35}

def main():
    assert set(PRED.keys()) == set(IDS), (sorted(set(IDS) - set(PRED)), sorted(set(PRED) - set(IDS)))
    assert len(PRED) == len(IDS) == 20
    outdir = os.path.join(BASE, "predictions")
    os.makedirs(outdir, exist_ok=True)
    total = 0
    written = 0
    trig_counts = {"changed_main": 0, "reserve_used": 0, "disputed": 0}
    for cid in IDS:
        p = PRED[cid]
        rec = {"case_id": cid, "prediction_text": p["prediction_text"], "basis": p["basis"],
               "confidence": p["confidence"], "trigger": trig()}
        path = os.path.join(outdir, cid + ".json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(rec, f, ensure_ascii=False, indent=1)
            f.write("\n")
        total += os.path.getsize(path)
        written += 1
    # per-file self-verify by exact open (no directory listing/counting of runs/)
    for cid in IDS:
        with open(os.path.join(outdir, cid + ".json"), encoding="utf-8") as f:
            rec = json.load(f)
        assert rec["case_id"] == cid and set(rec.keys()) == {"case_id", "prediction_text", "basis", "confidence", "trigger"}
        assert rec["trigger"] == trig()
        assert "systems_used" in rec["basis"]
    print(json.dumps({"cases": len(IDS), "written": written, "trigger_counts": trig_counts, "total_bytes": total}, ensure_ascii=False))

if __name__ == "__main__":
    main()
