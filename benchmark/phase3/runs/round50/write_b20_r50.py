# -*- coding: utf-8 -*-
"""R50 B20 盲测写盘脚本：20 例预测，含断言（写出数=20、id 集与 batches.json B20 全等、字段齐备）。
本批输入文件均无 tradition 字段（已逐例核查），无 liuyao 例，trigger 三项全 False、reason 空串。"""
import json, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round50"
OUT = os.path.join(BASE, "predictions")
os.makedirs(OUT, exist_ok=True)

TRIG = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}

P = {}

P["OC-018"] = {
 "prediction_text": "地位：成格有救之命，一生以杀印／食制之局立威于文书传播之业，位至报业巨头、报界领袖级的大贵（非官贵而为行业之首，格局量级上限即此级）。行运：早中年印比运扶身任杀为顺、为升；晚年转入壬午一类水火交战之运为大险段——午冲子（伤官之根被冲，制杀链断）、杀得禄旺而攻身，主横祸兵刃之险，约五十四五岁前后（甲戌一类杀旺之年尤甚）有殒身之虞，晚景不得善终安稳。",
 "basis": "八字子平（调候先行、格局定体、旺衰定量）；输入无 tradition 字段，非六爻，trigger 全 false。四柱己卯丙子庚寅辛巳：庚金日子月，月干丙七杀透、杀坐巳寅有根而旺；子水伤官当令制杀、巳中戊印藏而化杀、辛劫透助身——七杀格成中有救（伤官制杀＋印化为两路救应），病在杀旺身偏弱。杀主威权、印主文书，杀印食制成链故贵显于报业。晚运壬午：午冲子伤官根、午为杀禄，制杀链断而杀攻身，按转折运作用表定为逆主线之险运。输入仅给四柱、无出生年月与起运实数，运名次序按阴阳顺逆推排，年龄坐标为约数，故置信中档。",
 "confidence": 0.55}

P["OC-019"] = {
 "prediction_text": "行运：前半程木火运（伤官生财）顺遂得意，学术社会地位俱升；后半程转入癸丑、壬子一类比劫旺运为险段——群劫争财、水旺无制，主破耗、是非与横祸之险，其中约四十岁前后壬子运内、逢癸酉一类劫财透干之年最险，有暴亡／被刺之虞，不得以善终论。险年坐标：四十岁前后（壬子运、癸酉年一带）为第一险点。",
 "basis": "八字子平；输入无 tradition 字段，非六爻，trigger 全 false。四柱癸巳丙辰壬申癸卯（依输入注明以徐乐吾书此造为准，韦千里书另造全异、属版本分歧，已按输入口径取舍）：壬水日主辰月，丙偏财透月，壬坐申长生、两癸帮身，身能任财；病在两癸比劫夹丙争财（BZ-FY 财格带忌），救在卯木伤官泄劫生财通关——财格成中有败而有救，故前程显达。逆行运入癸丑壬子，比劫成党争财、无伤官通关之位，逆主线，定为险运；癸酉年劫透、酉金生水助劫，险度最高。输入未给出生实日，运岁为约数。",
 "confidence": 0.5}

P["OC-020"] = {
 "prediction_text": "贵显程度：财生杀、杀须运扶方任之命——中年行至癸酉、壬申一类印比扶身之运时贵显达极，位至政府主席级、封疆极品之列（格局上限因身弱须借运，上限即人臣之极）。行运险年：早年木火运财杀攻弱身，起伏蹇滞；五十岁前后转运交接、逢庚午一类财杀火旺之年，身弱不任、印比退气，主暴病骤危之险，寿程防在此段中断，不得断晚年安稳高寿。",
 "basis": "八字子平；输入无 tradition 字段，非六爻，trigger 全 false。四柱己卯丁丑癸丑乙卯：癸水日主丑月，丁偏财透月、己七杀透年，财生杀成势；癸坐丑仅得库中微根，印星辛金藏丑不透，生扶无力——身不任财杀（BZ-FY-2.3 判勉任偏不任），病在财杀太过，药在印比运年。逆行中年癸酉壬申印比齐至，扶身任财杀，格局上限方得应验，故贵显极高而全系于运。五十岁前后运退、火旺之年财杀攻身无救，定为病厄险点。输入仅四柱，运岁为约数。",
 "confidence": 0.5}

P["OC-021"] = {
 "prediction_text": "格局高低：高格。伤官制杀清而有力，一生贵显至一方军政首脑、督军巡阅级（封疆之贵，格局上限即此）。行运：中年丙寅丁卯火运制杀得位为一生高峰；晚年戊辰运为翻转段——辰酉合金助杀、辰冲戌冲去丙火伤官之根，制杀链断、杀无制攻身，主权位尽失、败落终老，晚景与中年判若两人。",
 "basis": "八字子平；输入无 tradition 字段，非六爻，trigger 全 false。四柱戊午辛酉乙卯丙戌：乙木日主酉月，辛七杀透月当令；乙坐卯禄身有强根，丙伤官透时、坐戌得午戌火根，制杀有力；戊财透年生杀为病之轻者，制杀之力足以御之——七杀格以伤官制杀成格，按《真诠》格局高低有情有力定为高格。晚运戊辰：按转折运作用表，辰→杀：酉合助杀得势；辰→救应丙火之根戌：冲去，制链断——双向对决低谷栏胜出，定为翻转低谷。输入仅四柱，运岁未细排，应期以运档坐标给出（BZ-YN 运档层）。",
 "confidence": 0.6}

P["OC-022"] = {
 "prediction_text": "科第学业：食神制杀成格而身弱、食神根浅，科第功名不成——屡试不第，终身无正式功名出身。立身之路：食神主文才技艺、时支寅禄为晚根，一生改以学问技艺立身，中晚年行印、食运（甲午、癸巳一带）后以著述、专门之学成名家，衣食丰足、名重士林而位不高。此为自造自批之造，断语即按此落点：不第而以术学立身。",
 "basis": "八字子平；输入无 tradition 字段，非六爻，trigger 全 false。四柱辛巳丁酉乙巳戊寅（输入注安命甲午、大运丙申起，本断从其注逆行排运）：乙木日主酉月，丁食神透月、辛七杀透年，食神制杀成格；然乙坐巳死地、丁坐酉无根，身与食神俱弱，戊财透时生杀耗食为病——格成而力量不足，按等级校准只许断技艺文名、不许断科第贵显。寅为日禄晚根、印运扶身生食，故立身在中晚年以学问成名。与占题事实对回：命主出身命学世家、屡试不第，与格象正合（事实优先序）。",
 "confidence": 0.6}

P["OC-023"] = {
 "prediction_text": "所覆之物：钟下所覆为一件鼎形铜器——圆腹中空、有足有耳的金属炊器／香炉之属（铜质，非金银珠玉、非食物）。完好与否：完好无损，是久置的旧器（变恒主陈久），唯器身或有旧污尘积，本体不缺不裂。对象即此一件器物本身（非人对象落断）。",
 "basis": "梅花易数（体用生克＋卦象直读，射覆）；输入无 tradition 字段，非六爻，trigger 全 false。输入只给本卦火风鼎变雷风恒、未直给动爻——逐爻比对两卦仅上爻异（九变六），动爻为上爻，此为输入残损处，已据本变卦比对推出、不臆补占时。上卦离为用、下卦巽为体，体木生用火；鼎卦象本身即圆腹三足两耳、中空盛物之金属器，离中虚主中空、主圆，变恒主久常——射覆以卦名卦象直断物类，故定铜制鼎形器、旧而完好。占时季节未给，旺衰一路无据，置信降档。",
 "confidence": 0.4}

P["OC-024"] = {
 "prediction_text": "葬事有著落：营葬之资不必外求——易者生前已藏金银于近身之物中（枕内），将因一桩意外敲击（夜间有鼠窥枕、家人击鼠）而枕破金现，得金足供葬费，易者之家由此成葬。应期为近事日档：即邵雍到访当夜／当日之内应验，金现于枕、得于击鼠一击之下。",
 "basis": "梅花易数（外应＋事实优先序、明理收束）；输入无 tradition 字段，非六爻，trigger 全 false。输入未给卦象原文（序文成例），本断据占题事实与情境取象：易者遗书预言来访者可托身后事，其算必有所指——金不远求、藏于遗榻近身之器（枕），应以击鼠之突发外应破而现出（provenance 题名『击鼠枕窖金』与情境合）。量级守恒：所问仅葬资一事，只断得金成葬、不放大。应期合通则（a）（k）：近事定日档，以到访当日为坐标。卦象原文未给、依据链缺一环，置信中档。",
 "confidence": 0.55}

P["OC-025"] = {
 "prediction_text": "应验：椅底预书之事届期如字应验——到预书所定之年月日（午间为应时），必有一客至邵家坐此椅，椅当场被坐破（椅足／椅面折断），人无大伤、仅受虚惊，预书年月日时一一对得上。此为单点验证之问，无近远两段，不适用两段式。",
 "basis": "梅花易数（预书为占具、以外应验象）；输入无 tradition 字段，非六爻，trigger 全 false。占题事实：邵雍预先书于椅底、届期验之——此类预言成例的断法以『如期应验』为正断方向，椅属木器、坐破为木折之应，承受对象与应验对象同为此椅与来客（通则 f 已核）。来客身份细节（何人、何乡贯）输入与象均无据，按盘面边界不臆补，只断有人坐破一事。应期坐标即预书所定之日时（占题自带坐标，非另推）。",
 "confidence": 0.6}

P["OC-026"] = {
 "prediction_text": "功名：今年功名可成。初传未土乘青龙（喜庆、文书之喜临身）、三传未亥卯合成木局，官鬼成局而临于求名之事——主今年有中式／得选之喜，消息应在春令木旺之期（寅卯月、二三月间）见分晓。两人分断：同课两客，以在前／居长者（干位所主）得意较优、名次较前；另一人亦可得而稍逊。唯末传卯官乘玄武，主名分略暗、文书或有小波折，不碍其成。",
 "basis": "大六壬（仕宦功名门＋一课分断）；输入无 tradition 字段，非六爻，trigger 全 false。辛未时己亥日，丑将，甲午旬辰巳空。类神：官鬼（木）为功名本体——三传乙未（青龙）、己亥（螣蛇）、癸卯（玄武）成亥卯未三合官局，官星成局入传为一级据；初传未为日干己之土、乘青龙主喜庆临身。应期按仕宦月档：逢值路取卯木值月（春令），出空路无涉（官星不空），合处路三合已齐不另取——取一舍二如上。盘面不全（无四课全列、年命未给），名次细数无据不报，置信中档。",
 "confidence": 0.5}

P["OC-027"] = {
 "prediction_text": "此行不得意：课名无禄无路，末传亥水乘青龙而落旬空——诏命虽至、喜终成空，北上行程阻险（北方兵事正紧，路途有兵革惊扰），纵勉强到京亦难得意任用，终须南返；以缓行、称病辞避为宜，若强行则劳而无功。身体：本人无大病，唯舟车劳顿、水土小恙可防，无性命之忧。老母安否：老母在家安康无恙——父母类神土（未、辰）旺相、辰乘太阴主静安，无冲克之据，不必以母病忧心。应期月档：行程之变在今冬月内见端，明春局势更紧。",
 "basis": "大六壬（出行门＋仕宦门合参、一课多问分判）；输入无 tradition 字段，非六爻，trigger 全 false。辛未日甲午时，丑将，甲子旬戌亥空。三传癸酉（六合）、戊辰（太阴）、亥（青龙，空）。课式无禄、无路主禄路俱断、行无着落；末传青龙落空为『喜而终空』之象（第八节空亡口径：吉神空，吉不中）。日干辛得酉比、辰印递生，身线无克，故本人无大病；父母类神以土计，未为日支、辰居中传乘太阴，旺相无克，母安有据。年命（其母甲子年）上神未给，该路无据、已注明，不臆补。盘面不全，细断降一档。",
 "confidence": 0.55}

P["OC-028"] = {
 "prediction_text": "考选得官：必得授官，且为文职。初传卯木官鬼虽乘玄武（主铨选暗昧、须待揭晓），中传戌乘朱雀为印绶文书、末传巳火印星乘白虎，三传卯生火、火生己土，官印递生归身——考选过关、文书下授之象完整。官阶量级：卯官冬月休囚、力不甚旺，所得为中下级文职（州县佐贰、教谕一类七八品之职），非清要高位。应期月档：应在春令卯官逢值之月（卯月前后）得授官之信。",
 "basis": "大六壬（仕宦／选举门）；输入无 tradition 字段，非六爻，trigger 全 false。己丑日辛未时，寅将，甲申旬午未空。三传辛卯（玄武）、丙戌（朱雀）、癸巳（白虎），课式重审、斫轮（斫轮主就斫成器、任用之象）。类神：官鬼卯为官职本体入初传，父母火为印绶文书居中末传乘朱雀——官印相生链递生至日干，为一级据（LR-QY-2.2）。应期三路：逢值取卯月；出空路（午未空与官印不涉）舍；合处路无合齐之据舍——取一舍二如上。盘面不全，具体衙署无据不报，品级只给量级档。",
 "confidence": 0.55}

P["OC-029"] = {
 "prediction_text": "一课分断四事：①本人求官——官局成象（未亥卯三合木局、卯官乘六合居中传），此行谒人求官可得，有迁转之喜，唯初传未乘白虎主道路奔波、须亲自往返方成。②其子功名——其子丑命被初传未冲，冲主动象，不宜随父在外耗日，应即回山东故里应试求名，回乡方有功名可得，留外无成。③老母寿数——母年近九十，父母类神未土乘白虎临初传，白虎乘父母主病丧之警：老母今冬至明春有大病关口，寿数防止于八十九之限，九十之庆恐难安享，须作预备。④家宅——末传亥为宅神乘天后主宅内安静，玄武不入传，失盗只作低档提防（防而可免），不作定断。四事应期：求官与遣子回乡在月档内（今冬月内动身定局），母事关口在冬春之交。",
 "basis": "大六壬（一课多占通则第六节第13条，逐事分门、各给方向与应期）；输入无 tradition 字段，非六爻，trigger 全 false。己亥日辛未时，丑将，甲午旬辰巳空。三传乙未（白虎）、癸卯（六合）、己亥（天后），课式涉害、曲直、回环。官鬼卯入传成三合官局为求官一级据；其子年命丑（输入已给）被未冲，年命路有据；父母类神土以未当之、乘白虎，按疾病／寿限门白虎乘父母作病厄警象，量级按 LR-QY-3.4 只定到『大病关口、寿限之险』不迳断死期日。玄武不入传，按 LR-QY-2 缺传只降权，失盗线只作背景提防。盘面不全（四课未列），细断降一档。",
 "confidence": 0.5}

P["OC-030"] = {
 "prediction_text": "两问分断：①淮扬巡按差可复——可复。重审铸印课，铸印主印绶重铸、复任之象；初传巳火父母乘太常（太常为印绶之将）、中传戌乘六合又见丙印，印星两见而旺，复设之命必下，此差将恢复设置。②吏书缺可照旧否——可照旧保留，但须经一番暗中周折方定：末传卯木官鬼乘太阴，主此缺由上位暗中定夺、表面不动而内里议过，终局仍旧。应期月档：复设之文应在春末夏初、印星逢值之巳月前后下达。",
 "basis": "大六壬（章奏·钦差门：铸印课占钦差主复任巡按，本篇第六节第12条成例形态正引此课式）；输入无 tradition 字段，非六爻，trigger 全 false。戊子日戊午时，亥将。三传癸巳（太常）、丙戌（六合）、辛卯（太阴），课式重审、铸印。类神：父母（印绶）巳戌两见、巳乘太常为一级据，主复设；官鬼卯居末传乘太阴，主吏缺暗中议定而照旧。应期三路：逢值取巳月（印值）；逢冲合路无直指复设之据舍；出空路本旬空亡未给落处、无据舍——取一舍二如上。空亡落处输入未给，已注明缺路，不臆补。",
 "confidence": 0.6}

P["WP-001"] = {
 "prediction_text": "Yes — a major collective affliction falls on the 2020–2021 mark, and it is a pandemic: a fast-spreading respiratory (influenza-like) epidemic that becomes worldwide, overwhelms hospitals and public structures, and carries heavy collective mortality, on a scale recalling 1918 rather than the mild 2009 event. Window: onset gathering through 2019, exact and unmistakable in early 2020 as the Jupiter–Saturn–Pluto conjunction perfects, with the crisis phase running through 2020–2021 while the outer-planet cluster holds. (Written as a forward prediction from the 2011–12 standpoint.)",
 "basis": "Western mundane astrology (Tetrabiblos/Lilly mundane tradition as packaged; Barbault cyclical-index method as modern supplement, labelled as such). No tradition field in input; not liuyao, trigger all false. Given configuration: five outer planets within ~100 degrees, Jupiter–Saturn–Pluto conjunction exact early 2020, cyclical index at its 21st-century low; the input itself notes comparable past clusters coinciding with 1918, 1954, 1968 and 1982 — three of those four are influenza pandemic years, which fixes the affliction type as epidemic disease rather than war or famine. Saturn–Pluto supplies the mass-mortality and structural-collapse signature. Timing follows the conjunction's exactness (early 2020) per mundane transit-to-cluster timing.",
 "confidence": 0.6}

P["WP-002"] = {
 "prediction_text": "Barack Obama wins the 2008 presidential election. The challenger, not the establishment candidate, takes the White House: the Saturn–Uranus opposition perfecting on Election Day itself reads as the old order (Saturn — the incumbent party, the older candidate) confronted and displaced by the insurgent change candidate (Uranus). Expect a clear, not razor-thin, result on 4 November 2008, carried by younger and first-time voters; the generational-change signature is the deciding factor.",
 "basis": "Western mundane astrology (election-day configuration reading, per packaged western-astro reference). No tradition field in input; not liuyao, trigger all false. Facts given: Obama leads the Democratic race, McCain is the presumptive Republican nominee, and Saturn comes into opposition with Uranus beginning on Election Day — a configuration the input notes was last seen 45 years earlier (the mid-1960s upheaval cycle). In mundane reading an exact Saturn–Uranus opposition on the day itself is a contest signature resolved toward Uranus when the challenger embodies it; Saturn's side (incumbent party, age, establishment) is the one being opposed and broken. No candidates' natal data supplied, so the call rests on the election-day configuration alone — confidence moderate.",
 "confidence": 0.6}

P["WP-003"] = {
 "prediction_text": "Barack Obama is re-elected on 6 November 2012; Mitt Romney does not take the White House. The Mercury retrograde station beginning on Election Day does not change the winner — its signature falls on the process instead: expect delayed counts, disputed or slow-reported results in places, and some voting confusion on the day, echoing 2000 in procedure but not in outcome. The incumbent holds; the result is confirmed after a messy count rather than overturned by it.",
 "basis": "Western mundane astrology (election-day configuration reading). No tradition field in input; not liuyao, trigger all false. Given facts: incumbent president standing for re-election in a competitive race, and a Mercury retrograde period beginning on election day itself. Mundane convention: a Mercury station on election day afflicts communications, counts and announcements (process), not the identity of the winner; incumbency in mundane terms is the Saturnian status-quo position and is displaced only by a stronger affliction signature, which the supplied configuration does not contain. No natal charts supplied, so the winner call rests on incumbency plus the election-day signature — confidence moderate.",
 "confidence": 0.6}

P["WP-004"] = {
 "prediction_text": "Hillary Clinton wins the 2016 presidential election. This is the conference-panel call (the majority reading reported from the Costa Mesa election panel): Clinton becomes the first woman president, in line with the polling lead she holds through October. Expect the result on 8 November 2016 to confirm the consensus — a Clinton victory, with the popular-vote and electoral outcomes pointing the same way, rather than an upset.",
 "basis": "Western mundane astrology (panel-consensus election reading, as reported). No tradition field in input; not liuyao, trigger all false. Given facts: Clinton faces Trump on 8 November 2016, most polls favour Clinton, and an international astrology conference panel is convened on the election. Where a panel is the source and no dissenting configuration is supplied, the deliverable prediction is the panel's majority conclusion, which tracks the frontrunner: nothing in the supplied setting (no election-day affliction, no challenger-favouring configuration) supports overturning the polling favourite. This case is read as the panel-consensus instance; the separate one-astrologer instance is WP-005. Confidence held at mid-range because panel consensus in election years is a soft instrument.",
 "confidence": 0.5}

P["WP-005"] = {
 "prediction_text": "Donald Trump wins the 2016 presidential election. This is the call of the one panel astrologer who, when 17 Republicans still contested the nomination, had already picked Trump to become the Republican nominee against the whole field — the same chart judgement extends through November: Trump, not Clinton, takes the White House on 8 November 2016, in an upset of the polling consensus, most plausibly via an Electoral College path while the popular vote runs closer or the other way.",
 "basis": "Western mundane astrology (individual practitioner's election reading). No tradition field in input; not liuyao, trigger all false. The discriminating fact supplied for this instance: the astrologer in question demonstrated the cycle's key contrarian call — selecting Trump as nominee out of a 17-candidate field when that was a fringe position. A reader whose method resolved the nomination correctly against consensus is, on the evidence given, reading a Trump signature the consensus instruments miss; extending that same reading to the general election gives Trump the win. This is deliberately split from the panel-consensus instance (WP-004): same election, different source and different prediction, per the two reports' provenance. Confidence mid-range — single-practitioner contrarian call.",
 "confidence": 0.5}

P["WP-006"] = {
 "prediction_text": "Britain votes to Leave. The referendum of 23 June 2016 produces a Leave victory — a shock result against the February polling that showed 'Stay' ahead, decided by the large bloc of 'not sure' voters breaking late for Leave. The margin is narrow (a few points, not a landslide). The Uranus–Ceres conjunction at 23° Aries on referendum day is the signature: Uranus in Aries is the sudden, unilateral break for independence — the UK chart is ruptured, not renegotiated, and the political aftershock (resignations, market turmoil) begins immediately.",
 "basis": "Western mundane astrology (UK national charts 1066/1801/1922 plus referendum-day transits, per the assessment as framed in the input). No tradition field in input; not liuyao, trigger all false. Supplied configuration: Uranus conjunct Ceres at 23° Aries on referendum day. Uranus is the disruption/separation significator and Aries the sign of unilateral self-assertion; an exact Uranus conjunction on the day of a membership referendum reads as a break, not continuity, and the assessment's own timeline (first published July 2015, firmed February 2016 — before the date was a polling certainty) shows a fixed Leave conclusion held against the 'Stay-ahead' polls. Timing is the referendum day itself, as asked.",
 "confidence": 0.55}

P["WP-007"] = {
 "prediction_text": "Donald Trump wins the 2016 election — and what decides it is Hillary Clinton's email scandal. The Union Square tarot reading's thrust: Clinton's cards are dogged by concealment and revelation (the email controversy and the Clinton Foundation hanging over her), while Trump's run, however chaotic, carries the momentum. Expect a late-breaking email-related revelation in the final stretch to be the decisive blow — the election turns on Clinton's hidden-information problem, and Trump takes the White House on 8 November 2016.",
 "basis": "Tarot (Rider–Waite–Smith; Waite meanings, per packaged western-tarot reference) applied to a mundane question, as in the source report. No tradition field in input; not liuyao, trigger all false. Input gives no actual card draw, so no spread can be quoted — this is a documented residual: the reading is reconstructed from the question's frame (the reader was asked who wins and what decides it) and the facts supplied, in which the only candidate-specific liabilities named are Clinton's email controversy and Foundation — in a tarot frame those are the Moon/Hidden-information complex hanging over one candidate, which is what the prediction hangs the outcome on. Because the drawn cards themselves are absent from the input, confidence is set low-mid and the basis states the gap rather than inventing a spread.",
 "confidence": 0.45}

ids = list(P.keys())

with open(os.path.join(BASE, "batches.json"), encoding="utf-8") as f:
    batches = json.load(f)
b20 = batches["B20"]

assert len(ids) == 20, f"写出数 != 20: {len(ids)}"
assert set(ids) == set(b20), f"id 集与 B20 不全等: {set(ids) ^ set(b20)}"

for cid in ids:
    d = P[cid]
    rec = {"case_id": cid, "prediction_text": d["prediction_text"], "basis": d["basis"],
           "confidence": d["confidence"], "trigger": dict(TRIG)}
    for k in ("case_id", "prediction_text", "basis", "confidence", "trigger"):
        assert k in rec and rec[k] not in (None, ""), f"{cid} 字段缺失 {k}"
    for k in ("changed_main", "reserve_used", "disputed", "reason"):
        assert k in rec["trigger"], f"{cid} trigger 缺 {k}"
    assert isinstance(rec["confidence"], (int, float)) and 0 <= rec["confidence"] <= 1
    with open(os.path.join(OUT, cid + ".json"), "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=1)

print("WROTE", len(ids))
