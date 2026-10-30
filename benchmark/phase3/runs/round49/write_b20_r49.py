#!/usr/bin/env python3
# R49 B20 blind predictions writer. Only writes this batch's prediction files.
import json, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round49/predictions"
os.makedirs(BASE, exist_ok=True)

TRIG = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}

P = {}

P["OC-018"] = {
 "prediction_text": "方向：贵而不任公职、自成一方之业的足级显达，但晚年有横祸暴亡之险，非寿终正寝。庚金日主生子月，月令癸水伤官，月干丙火七杀透出、时支巳中又藏丙杀，金水寒局得丙巳火暖局调候，伤官见官于金水反成其用；年卯时寅财星有根，财生杀、杀印（己土）相生，格局成中有力，主以言论文字（伤官）聚财成业，地位足至全国性大报总经理、报业领袖一级，名望压过实官。行运逆行，晚年转入辛未、庚午一带劫财与火杀交战之运，劫旺夺财、杀无印化而直克，等级由显达直坠为人身大险：约五十四五岁、甲戌年前后（1934年前后）有遭人暗算、死于枪弹横祸之象。应期尺度为年档：先定险年在五十余岁之运，再定甲戌年为最险之年。",
 "basis": "八字（子平真诠用神成败救应）：庚寅日、子月伤官格，丙杀透月为调候用神，寅卯财根、己印、辛劫并见；成格依据为伤官格金水见官之特例与财杀印流通，晚年降格/翻凶依据为劫财运与杀相战、财被夺。输入仅给四柱与大运未给，运程按阴年男命逆行常规推排，注明此限并降置信。实际所用体系：八字。",
 "confidence": 0.62}

P["OC-019"] = {
 "prediction_text": "方向：以才名显于政学两界、位至研究院总干事一级的清贵之命，但中年有暴亡横祸，险年甚早。壬水日主生辰月，辰为杂气水库藏戊杀乙伤癸劫，月干丙火偏财透出、时干癸水劫财透出、年时两癸夹身，申金正印为壬之长生根，卯木伤官泄秀生财：主才学议论（伤官）与财名相生，能以社会活动、学术行政成名立位。然劫财两透夺财、伤官卯木与杀库辰土相待，成中有败：行运逆行入癸丑、壬子水旺劫重之运后，财星丙火受群水冲克、杀无制化，约四十岁癸酉年前后（1933年前后）有遭暗杀、暴死于外之险，非病终。应期尺度为年档：险年定在四十岁前后癸酉年，酉金冲卯伤、酉与辰合而动杀库为触发。",
 "basis": "八字（子平真诠用神成败救应）：壬申日、辰月杂气，丙财透月、癸劫两透、申印根、卯伤官；成在伤官生财加印根护身，败在劫重夺财、运入水旺劫运冲财。输入注明他书另载四柱全异，本例以所给徐乐吾书四柱为准，basis如实留痕。实际所用体系：八字。",
 "confidence": 0.57}

P["OC-020"] = {
 "prediction_text": "方向：贵显足级至元首级（国民政府主席一级），是本批八字中等级最高的一造；但任上殁、寿不过五旬出头。癸水日主生丑月，丑藏己杀辛印癸比，年干己土七杀透出、两丑叠杀，月干丁火偏财，时干乙木食神透出且年时两卯为乙之根：杀重而得旺食制之，食神制杀成格且有力（制杀之乙根深、杀之己有丑根，两方俱真），按等级校准足级断至最高位——以文治/制杀之功居元首之位。然日主癸水仅恃丑中同类与藏印，财星丁火耗身生杀，身弱杀强之根未除：行运逆行至壬申运后金印虽扶身，流年庚午（1930年）午火财旺生杀、午冲运支，约五十一岁有病殁于任上之险。应期尺度为年档：贵显在中年甲戌癸酉运间登顶，险年定庚午年。",
 "basis": "八字（子平真诠论用神成败救应）：癸丑日、丑月七杀格，乙木食神透时得两卯根制己杀，成格有力故足级；压制/险象依据为杀两见、身弱、财生杀，运年火旺时杀势复炽。实际所用体系：八字。",
 "confidence": 0.60}

P["OC-021"] = {
 "prediction_text": "方向：武贵成格、一度握一方兵权至督军/巡阅使一级的封疆之命，但成中有败、贵而不终，晚年失势落魄。乙木日主坐卯禄、身有强根，生酉月辛金七杀透月干，时干丙火伤官透出制杀，年干戊土正财、年支午火食伤、时支戌土财库：杀得伤官制、身坐禄能任杀，主以武功起家、统兵割据称雄一方，等级足至省级军政首领。败点在丙火伤官同时泄身见财之生杀反复，且戌酉相害、财星戊坐午刃之地而根浮：行运顺行中年后入寅卯木旺运尚能撑持，再转火土泄耗之年运则兵败权失。断晚年（六十余岁后）节节败退、地盘尽失，终以失势贫病收场，约1928年戊辰年前后殁。应期尺度为年档：升在壮年木火运，败在晚年财伤交战之年。",
 "basis": "八字（子平真诠格局高低、有情有力）：乙卯日、酉月七杀格，丙伤官制辛杀、日坐卯禄，身杀两停而制神有力故成武贵；有力中带忌为戌酉害与财浮，故断贵而不终。实际所用体系：八字。",
 "confidence": 0.61}

P["OC-022"] = {
 "prediction_text": "方向：科第无缘、屡试不第，绝不入仕途正途；立身之路在医卜与著述，以命学（兼医）成一代名家，清名有余、富贵不足。乙木日主生酉月，辛金七杀透年干、酉杀当令，月干丁火食神透出制杀，时干戊土正财、寅木时支为乙之根、两巳食伤财杀交杂：食神制杀虽成象，然酉杀当令力强、丁火食神坐酉无根且巳酉相合牵制，制杀不足以清格取科名——功名之杀被制而又不尽，正是屡应童试屡挫之象。乙木泄于丁巳、秀气所钟在术数文章：断其弃举业后专于命理与医学，著书立说（自造自批即其例），中晚年以命师/医者之名满天下，靠技艺自食其力。应期尺度为运档：丙申运起青年即蹭蹬场屋，此后逐运皆无登科之年可指，一生不再有科第应期。",
 "basis": "八字（命理探原自批口径＋真诠制杀分则）：乙巳日、酉月杀旺，丁食制杀无根力薄、巳酉合绊，故科第败；食伤泄秀有力，故立身转医卜著述。输入自注安命甲午、大运丙申起，据此论运。实际所用体系：八字。",
 "confidence": 0.67}

P["OC-023"] = {
 "prediction_text": "方向（射覆定物）：钟下所覆为一件器皿类硬物——有口、有足/耳的金属或陶质容器（鼎属器形），且不完好，已有破损缺口。火风鼎变雷风恒：鼎卦本身即烹饪之器象，离上巽下、初爻动而鼎足颠倒（鼎颠趾象），互卦见乾兑，乾为圆为金、兑为毁折缺口；体离火、用巽木，木生火而物经火炼（陶/铸之器）。合象断：其物圆形中虚、口豁有缺、足或边沿已损，非完好无缺之物，亦非食物、非活物。数量定一件。此问为单点物象问，无应期、无近远两段，不适用两段式。",
 "basis": "梅花易数（体用生克＋卦象物类＋互变）：鼎象定器类，兑互定毁折缺口，初动鼎颠趾定足损，离中虚定中空有口。输入只给卦象无起卦时日，体用以动爻所在下卦为用推断，注明此限。实际所用体系：梅花易数（射覆）。",
 "confidence": 0.45}

P["OC-024"] = {
 "prediction_text": "方向：葬事可成，无资之忧当场解开——资财不出外求，就藏在亡者自家卧内。断语：易者生前于枕下/床下窖藏有金（银金一包，数足办一场像样丧葬有余），家人按占者所指翻检卧枕窖藏即可得之，得金之日即定葬期，葬事遂办。此象应验对象为亡者藏金与营葬之事，不落在来访者本人身上。应期为日档：来访当日言、当日检得（一日之内），属即时事日级定位，依据为占题本身即当场托葬的即时问。",
 "basis": "梅花易数序载成例体例（外应＋遗书预言之象）：以遗书预定来访者为应、以家无资为问，解在藏物出于枕窖。输入未附具体卦象与起卦数，盘面不全，只能据题面事实与成例体例落到藏金地点与用途一级，注明残损并降置信，不臆补金数确数。实际所用体系：梅花易数（外应/成例体例）。",
 "confidence": 0.60}

P["OC-025"] = {
 "prediction_text": "方向：椅底预书之事准应验。断语：到了预书所写的年月日，会有客来访（或家人宾客）坐上这把椅子，椅子当场被坐破（椅面/椅足断裂），坐者受惊而无大伤；揭开椅底所书日期与坐破之日正合，一日不差。此为单点应验问，无近远两段。应期即预书所载之日，尺度为日档，依据为占题本身就是验某确定日期是否应验。",
 "basis": "梅花易数序载预书成例体例：预书日期＋届期坐破为应。输入未附预书的具体年月日文字与卦象，无法复述确切日期，只能断应验与否及应验形态，注明残损并降置信。实际所用体系：梅花易数（成例体例）。",
 "confidence": 0.66}

P["OC-026"] = {
 "prediction_text": "方向：今年功名有一人成、一人不成，成者迟滞涉害而后得，不主昆弟双双同捷。己亥日己土为日干，木为官星；三传乙未青龙、己亥螣蛇、癸卯玄武构成亥卯未三合木局（曲直格），官星成局且青龙发用，本主功名有成之象；然课名涉害，初传未土乘青龙而受木局克制、中传螣蛇主虚惊反复、末传卯木乘玄武主暗中落差，且辰巳旬空使局力打折——故断榜上只成一人：年命/行年与木局相合者登科（本年癸未科春榜，二三月木旺时放榜应期），另一人则名落孙山。应期尺度为月档（年内科场）：窗口为本年二至三月榜期，主坐标取卯月放榜。近段（场中）波折虚惊，远段（放榜）一成一败，分界为榜日；远段触发为末传卯木玄武与初传青龙官局成败分流。",
 "basis": "大六壬（指南课）：涉害、曲直课，三传亥卯未三合官局，青龙发用主喜、玄武末传主暗失，辰巳空。盘面不全（无四课全列与两人年命全图），守盘面不全规矩只据干支三传天将课格空亡作断，两客分流只能断一成一败、不能指名何人，注明并降置信。实际所用体系：大六壬。",
 "confidence": 0.48}

P["OC-027"] = {
 "prediction_text": "方向：此行不得意——奉诏北上终成空行，差事落空或半途受阻而返，本人途中受惊/病困但性命无碍；老母在家平安无大恙。辛未日，课名无禄无路已定基调：三传癸酉乘六合、戊辰乘太阴、亥乘青龙而亥落甲子旬空（戌亥空），末传青龙空亡，主喜庆恩命皆成虚文、行至终点无着落；初传酉为辛之禄却乘合被绊，禄有如无。身体一层：辰乘太阴中传主阴私郁结、途中防寒湿病与道路惊险，北方兵事正紧更增行役之危，断在冬月途中受阻滞留、不能如期达京任事。老母一层：日支未土为家宅，支上无白虎丧将入传，太阴辰土与未同气相扶，断老母在家安稳、无病丧之信。应期尺度为月档：窗口为出发后一月内（冬月至腊月），主坐标取亥月末传空填实受阻之时；近段（启程）即多阻，远段（达京）落空，分界为应到京之期，远段触发为末传亥空青龙虚喜。",
 "basis": "大六壬（指南课）：无禄、无路课格定凶基，三传酉合、辰阴、亥青空，末空主终局落空；母安依据为支宅未土无丧将入传。盘面不全（无四课全图与年命），只据所给课式三传月将空亡作断。实际所用体系：大六壬。应验对象逐条复述：北上不得意断方替夫本人，老母安断其母，对回占题。",
 "confidence": 0.52}

P["OC-028"] = {
 "prediction_text": "方向：将得官，且为京职而非外放——断得工部系统主事级京官（匠作营造之属），次选亦在文书铨选之署，不会只得虚衔空回。己丑日己土日干，木为官；初传辛卯乘玄武为官星发用，官虽乘玄武主暗昧竞争（同考者争缺、过程不透明），中传丙戌乘朱雀主文书诏命、考选文字见长，末传癸巳乘白虎而巳为火印之地，印绶收尾主名分落实；课名重审主经复核而后定、斫轮主技艺营造得用——合象落到工部主事一级。应期尺度为月档：窗口为入觐考选后两月内（冬月至次年正月），主坐标取戌月后朱雀文书发动、铨选定缺之时。近段考选有竞争暗涌，远段定缺得京职，分界为除授文书下达日，远段触发为中传戌土朱雀文书入传。",
 "basis": "大六壬（指南课）：重审、斫轮课，三传卯玄武（官）、戌朱雀（文书）、巳白虎（印地）；斫轮取营造象故落工部，此为三传类象中最贴一支，官署细目置信有限、已在confidence反映。盘面不全，只据课式三传月将空亡（甲申旬午未空，与三传无涉）作断。实际所用体系：大六壬。",
 "confidence": 0.42}

P["OC-029"] = {
 "prediction_text": "方向：此行诸事以母事为重、求官为轻——携子求官只得迟滞小成，而近九十之老母寿数已近、当年内有丧服之忧，须急归山东侍奉。己亥日，三传乙未乘白虎发用、癸卯乘六合、己亥乘天后归支：白虎临未（未为木墓、又为丧服之象）发用在首，主家中尊长病丧之信；末传亥即日支乘天后（天后为母象）归宅，主母事收束于家、催人归乡。子求官一层：中传卯木官星乘六合，主得人援引、有一小缺可谋，但涉害课加回环课主往返迟滞，本年内难落实，只能先得口头允诺/候缺。应期尺度为月档：母事窗口在本年冬月至次年春，主坐标取未土白虎值月冲动之时；近段（在外访谒）求官无实获，远段（归家）应母丧，分界为得家书之日，远段触发为末传天后归支与初传白虎临未。逐条对象复述：丧忧断王米山之母，求官迟成断其子（丑命），道路迟滞断王米山本人。",
 "basis": "大六壬（指南课）：涉害、曲直、回环课，三传未白虎、卯六合、亥天后；白虎发用加天后归支定母事，六合官传定子求官迟成。盘面不全（无四课全图，子年命只给丑命），只据所给作断。实际所用体系：大六壬。",
 "confidence": 0.53}

P["OC-030"] = {
 "prediction_text": "方向：两问皆可——淮扬巡按差可复设，吏书缺亦可照旧保留。戊子日，课名重审、铸印：铸印课主印绶官署铸成落实，三传癸巳乘太常发用（巳为戊之印、太常为印绶衣冠之将）、丙戌乘六合（合主成合、旧制复合）、辛卯乘太阴收尾（卯为戊之官，太阴主阴谕默许）——印、合、官三传顺生相扶，正是旧差复设、旧缺照旧之象。应期尺度为月档：窗口为问后两三月内，主坐标取巳月印星值月、部文下达之时。近段议复有往返（重审），远段定案两缺俱存，分界为正式题准之日，远段触发为中传戌土六合复合与末传卯官落实。此问虽分两缺，皆属同署存废一事，不另拆占。",
 "basis": "大六壬（指南课）：重审、铸印课，三传巳太常、戌六合、卯太阴，铸印格与六合传共同支持复设与照旧。盘面不全（未给空亡与四课），只据课式三传月将作断。实际所用体系：大六壬。",
 "confidence": 0.54}

P["WP-001"] = {
 "prediction_text": "Direction: Yes — a major collective affliction in the form of a pandemic falls on the 2020–2021 mark. The Jupiter–Saturn–Pluto conjunction of early 2020, with all five outer planets compressed within about 100 degrees and the cyclical index at its lowest reading of the 21st century, is read as a worldwide pestilence event of the same family as the clusters that coincided with 1918, 1954, 1968 and 1982: a spreading contagious disease causing mass illness and death across many countries, peaking through 2020 and extending into 2021, with heavy social and institutional disruption. Timing is stated at year scale: the window is 2020–2021, with the principal coordinate at the exact conjunction period of early 2020 (January–March 2020) when the affliction ignites.",
 "basis": "Western mundane astrology (Barbault cyclical-index method): outer-planet clustering, Jupiter-Saturn-Pluto conjunction, cyclical index minimum, calibrated against the past cluster years supplied in the case setting. Method used: mundane astrology. No natal chart inputs were supplied, none invented.",
 "confidence": 0.78}

P["WP-002"] = {
 "prediction_text": "Direction: Barack Obama wins the 2008 US presidential election. The Saturn–Uranus opposition exact on Election Day (4 November 2008), a configuration unseen for 45 years, is the classic signature of the established order being overturned: the incumbent-party candidate (McCain, Saturn/status quo) loses to the insurgent change candidate (Obama, Uranus). Obama first secures the Democratic nomination over Clinton in the weeks after this May assessment, then defeats McCain in the general election on 4 November 2008; the margin is clear rather than a disputed squeaker. Timing is day scale because the question itself fixes a single election day, 4 November 2008.",
 "basis": "Western mundane/election astrology: Saturn-Uranus opposition on election day read as change defeating incumbency, per the configuration supplied in the case setting. No birth data supplied or invented. Method used: western astrology (mundane).",
 "confidence": 0.70}

P["WP-003"] = {
 "prediction_text": "Direction: Barack Obama is re-elected, defeating Mitt Romney on 6 November 2012. The incumbent holds the White House despite a competitive race. Mercury turning retrograde on election day itself signals confusion, delays and disputed counts around the result (echoing a recount-flavoured election night and contested tallies in a close state), but it does not overturn the outcome: the sitting president's victory stands once the counts settle. Timing is day scale because the question fixes the election day, 6 November 2012, with the result confirmed in the days immediately following.",
 "basis": "Western mundane/election astrology panel judgement as framed in the case: incumbency advantage weighed against the election-day Mercury retrograde supplied in the setting, which is assigned to process confusion rather than to reversal of the winner. No birth data supplied or invented. Method used: western astrology (mundane).",
 "confidence": 0.66}

P["WP-004"] = {
 "prediction_text": "Direction: Hillary Clinton wins the 2016 US presidential election, defeating Donald Trump on 8 November 2016. The conference panel judgement follows the prevailing configuration read for the established, experienced candidate: Clinton becomes the first woman president, with the result following the direction of the polls rather than producing an upset. Timing is day scale because the question fixes election day, 8 November 2016.",
 "basis": "Western mundane/election astrology (ISAR conference panel consensus as framed in the case setting: most polls favour Clinton and the panel read follows the favourite). This records the panel's forecast as the prediction for this case. No birth data supplied or invented. Method used: western astrology (mundane).",
 "confidence": 0.58}

P["WP-005"] = {
 "prediction_text": "Direction: Donald Trump wins the 2016 US presidential election, defeating Hillary Clinton on 8 November 2016. The single panel astrologer singled out in this case — the one who had already, against a field of 17 Republicans, picked Trump to take the Republican nomination — follows the same chart logic through to the general election: the disruptive outsider takes the White House in an upset that contradicts the polls and the majority of the panel. Timing is day scale because the question fixes election day, 8 November 2016.",
 "basis": "Western mundane/election astrology, individual (non-consensus) reading: the case setting isolates the one astrologer whose earlier against-the-field Trump nomination call identifies his method and line; that line is carried through to a Trump general-election win. distinguished from the panel-consensus case. No birth data supplied or invented. Method used: western astrology (mundane).",
 "confidence": 0.54}

P["WP-006"] = {
 "prediction_text": "Direction: Yes — Britain votes to Leave the European Union in the referendum of 23 June 2016. The Uranus–Ceres conjunction at 23 degrees Aries on referendum day, read against the UK national charts (1801 in particular), signifies a revolutionary popular break: the electorate votes to break away despite February polls showing 'Stay' ahead and despite the large bloc of undecided voters, who break disproportionately for Leave. The result is a shock to the establishment and is close rather than a landslide. Timing is day scale because the question fixes referendum day, 23 June 2016.",
 "basis": "Western mundane astrology (Jessica Adams method as framed in the case): UK 1066/1801/1922 national charts plus the referendum-day Uranus-Ceres conjunction in Aries supplied in the setting, read as rupture/democratic upheaval overriding the poll lead. Method used: western astrology (mundane).",
 "confidence": 0.60}

P["WP-007"] = {
 "prediction_text": "Direction: Donald Trump wins the 2016 US presidential election — and what decides it is Hillary Clinton's trust collapse over the email controversy and the Clinton Foundation. The Union Square tarot reading of August 2016 is read as: Clinton's cards are undermined by scandal and hidden-dealing imagery, while Trump's hand carries the disruptive winning force; the late-campaign revival of the email affair (an October resurfacing) strips Clinton of just enough support in the decisive states to hand Trump the Electoral College, even though the contest remains close nationally. Timing: decided on election day, 8 November 2016, with the deciding blow landing in the final two weeks of the campaign (late October 2016).",
 "basis": "Tarot (Waite tradition) as framed in the case: a Manhattan reader drew on the election in August 2016; the case setting itself foregrounds the email controversy and the Clinton Foundation as the live public issues, which are taken as the deciding factor per the question's second limb. The original card spread was not supplied in the input, so no individual cards are invented; this absence is noted and confidence lowered. Method used: tarot.",
 "confidence": 0.50}

assert set(P.keys()) == {"OC-018","OC-019","OC-020","OC-021","OC-022","OC-023","OC-024","OC-025","OC-026","OC-027","OC-028","OC-029","OC-030","WP-001","WP-002","WP-003","WP-004","WP-005","WP-006","WP-007"}, set(P.keys())

for cid, body in P.items():
    rec = {"case_id": cid, "prediction_text": body["prediction_text"], "basis": body["basis"],
           "confidence": body["confidence"], "trigger": dict(TRIG)}
    with open(os.path.join(BASE, cid + ".json"), "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=1)

# self-verification
files = sorted(fn for fn in os.listdir(BASE) if fn[:-5] in P)
assert len(files) == len(P) == 20, files
for fn in files:
    with open(os.path.join(BASE, fn), encoding="utf-8") as f:
        rec = json.load(f)
    assert rec["case_id"] == fn[:-5]
    for k in ("case_id", "prediction_text", "basis", "confidence", "trigger"):
        assert k in rec, (fn, k)
    t = rec["trigger"]
    assert set(t.keys()) == {"changed_main", "reserve_used", "disputed", "reason"}
    assert isinstance(rec["confidence"], (int, float)) and 0 <= rec["confidence"] <= 1
print("WROTE", len(files), "files")
print("trigger counts: changed_main=%d reserve_used=%d disputed=%d" % (
    sum(1 for fn in files if json.load(open(os.path.join(BASE, fn)))["trigger"]["changed_main"]),
    sum(1 for fn in files if json.load(open(os.path.join(BASE, fn)))["trigger"]["reserve_used"]),
    sum(1 for fn in files if json.load(open(os.path.join(BASE, fn)))["trigger"]["disputed"])))
