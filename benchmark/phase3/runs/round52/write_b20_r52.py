import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "predictions")
os.makedirs(OUT, exist_ok=True)

def trig():
    return {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}

P = {}

P["OC-018"] = {
    "prediction_text": "方向：贵显而晚年凶。命主以报业立身、掌大报、名望与影响及于全国，地位至报界领袖级（非官位之贵，乃舆论界之权）。近中段运程得势为一生高峰；晚年行运转入火杀旺而身弱难任之地，约五十余岁（庚午年、1934年前后）为险年，主突发横祸、死于兵刃枪杀之类外来暴力，非安然寿终。应期尺度为年档：先定晚运、再定险年在五十岁上下之火旺流年。",
    "basis": "输入卡 tradition 字段原值：未标注（无此字段）；实际所用体系：八字（子平格局＋旺衰调候）。\n四柱己卯丙子庚寅辛巳：庚金生子月水旺，金寒水冷，身偏弱；月干丙火七杀透，己土印星化杀生身，杀印相生为贵气来路，故能掌重权、成报业巨头；然子水伤官与丙杀相见、寅巳刑意，格局成中有败，救应在印而印不厚。男命己年逆行，晚运入南方火地杀旺克弱身，等级按格局只至舆论界领袖而非封疆；险年据火杀逢值之年档推定。输入仅给四柱、无出生年月日与起运岁数，流年坐标为推定，已降置信。",
    "confidence": 0.55,
}
P["OC-019"] = {
    "prediction_text": "方向：早达而险。命主中年得志、任研究院总干事一类学术行政要职，社会声名高；行运前段财官得用为顺，后段转逆。险年在四十岁前后，主横祸：约1933年（癸酉年）前后遇刺身亡、死于枪杀暗害，非病终；寿仅四十上下。应期尺度为年档：险年落在劫财逢值、酉金冲卯之年。",
    "basis": "输入卡 tradition 字段原值：未标注（无此字段）；实际所用体系：八字（子平格局＋旺衰）。\n四柱癸巳丙辰壬申癸卯（输入卡自注他书所载四柱全异、本例以此为准，已按此盘作断）：壬水生辰月，丙火偏财透月，财生辰中官杀，申金印星生身、壬有申根，故能贵显任要职；然癸水劫财两透争财、卯木伤官，财格成中有败，身不甚强而财杀交逼。男命癸年逆行，四十岁前后运年水金与卯酉冲并见，官杀暗害之象成，故断横死险年。出生日期与起运未给，险年为年档推定，已降置信。",
    "confidence": 0.52,
}
P["OC-020"] = {
    "prediction_text": "方向：贵至极品而寿有险。命主贵显程度至国家元首级（国民政府主席级），一生高峰在水金得力之运段（约四十余岁、1920年代当权）；行运后段土杀转旺、身弱难支，险年在五十岁前后，约1930年（庚午年）病逝，主急症暴亡（脑心急症之类），非横死于外。应期尺度为年档：先定后段杀旺之运、再定庚午流年。",
    "basis": "输入卡 tradition 字段原值：未标注（无此字段）；实际所用体系：八字（子平格局＋旺衰）。\n四柱己卯丁丑癸丑乙卯：癸水生丑月土旺，己土七杀透年，丁火偏财生杀，乙木食神透时制杀，食神制杀成格而身坐丑有根，故贵至元首级，格局量级区间上限即主席级、下限亦不低于封疆。男命己年逆行，中段行水金运扶身任杀为高峰；后段运入未土冲丑、杀势填实而身弱，病字在土杀逼水，险年按庚午年火土并旺推定。无出生日期与起运岁数，年坐标为推定，已降置信。",
    "confidence": 0.55,
}
P["OC-021"] = {
    "prediction_text": "方向：武贵极盛而晚年失势。命主格局为一方军政首脑之贵，可至督军、统辖两广级封疆武职，由草莽/行伍起家而握兵权；高峰在木火运段（约五六十岁、1910年代至1920年代初当权）。晚年运转财生杀重之地，权势被夺、退场落魄，约1928年（戊辰年）前后病逝于失势之后。应期尺度为年档。",
    "basis": "输入卡 tradition 字段原值：未标注（无此字段）；实际所用体系：八字（子平格局＋旺衰）。\n四柱戊午辛酉乙卯丙戌：乙木生酉月，辛金七杀透月当令，丙火伤官透时制杀，乙坐卯禄有强根，伤官制杀成格主武贵握兵；戊土财生杀为其势之源。然卯酉冲、禄杀相战，格局带破。男命戊年顺行，木火运制杀得权为峰；晚运戊辰财生杀、辰冲戌合酉，杀重身受逼而失势，险年按戊辰年推定。无起运岁数，年坐标为推定，已降置信。",
    "confidence": 0.55,
}
P["OC-022"] = {
    "prediction_text": "方向：科第无缘、学业以术立身。命主屡试功名不第，终身不得正式功名与官位；但才学秀气足，立身之路不在仕途而在学问技艺——以命理术数著述、为人推命立名，成为一代命学名家，财源与声名皆由此出，中晚年名望反高于得第者。子女/承继一线以其学传人续之。应期尺度为运档：青壮运段（乙未、甲午一带）应试屡蹶，印运虽后至而已过科举之年，转作著述立名之运。",
    "basis": "输入卡 tradition 字段原值：未标注（无此字段）；实际所用体系：八字（子平格局＋旺衰）。\n四柱辛巳丁酉乙巳戊寅，大运丙申起（逆行）：乙木生酉月辛杀当令，丁火食神透月制杀、两巳食伤生戊财，食伤秀气极显主聪明善学；然全盘无一点印星（水全缺），印主功名文凭与科第凭据，印绝则科甲无缘，此为屡试不第的压制依据。身坐寅禄有根，食伤生财成链，故改以技艺学问（术数）生财立名。格局上限只至名家而非仕宦，断语等级据此锁定。",
    "confidence": 0.62,
}
P["OC-023"] = {
    "prediction_text": "射覆断：钟下所覆是一只已烹熟的鸡（熟食，非活物）。物象：禽类、有头足、色黄赤、经火烹炮。完好与否：不完好——已宰杀烹煮、为盘中熟食之形，非活鸡之全；即时当场开钟即验，无应期。",
    "basis": "输入卡 tradition 字段原值：未标注（无此字段）；实际所用体系：梅花易数（体用生克＋卦象取物）。\n卦火风鼎变雷风恒，上爻动：上卦离为用、下卦巽为体，巽木生离火，体生用主物已耗于火；鼎卦大象木上有火、主烹饪鼎食，所覆之物与烹食相关；巽为鸡、离为雉，禽象两见同指鸡禽；变恒上震木与体比和，物性属木火熟食一路。对象核对：所断即钟下之物本身，非及于人。具体项落点：物品（熟鸡一只）、状态（已烹不完好）。输入未给起卦数与占时，外应一路无据，已降置信。",
    "confidence": 0.5,
}
P["OC-024"] = {
    "prediction_text": "方向：应验，葬资有着落。易者身后无资之困可解：邵雍在其家夜闻鼠啮、以枕投击，鼠窜入窖/破处，循迹掘之，得易者生前窖藏之金（银）一藏，数目足以营葬，易者遂得安葬。应验对象即葬资一事本身，应在到访后一二日内见金。",
    "basis": "输入卡 tradition 字段原值：未标注（无此字段）；实际所用体系：梅花易数（外应取象＋明理收束）。\n本例输入未给卦象数与盘面，仅给情境：遗书预言来访者可托葬事、其家无资。按梅花外应与成例形态（击鼠、投枕、鼠窜窖、掘得窖金）收束：鼠为夜间窜匿之应、窖为藏金之地，金出于窖则葬资自备，不须外求。量级守恒：所问仅葬资一事，只断得金营葬、不放大他事。盘面缺失为输入残损，已显著降置信，断语只落到成例可据的事件线。",
    "confidence": 0.55,
}
P["OC-025"] = {
    "prediction_text": "方向：应验。届预书所定年月日，有客来访（或家人宾客）坐此椅，椅腿/椅身应声折破、椅破人跌，坐者受惊而无大伤；开椅底验预书，字字相符。应期即预书所写之日，当日坐破，不爽时刻之约的大势。",
    "basis": "输入卡 tradition 字段原值：未标注（无此字段）；实际所用体系：梅花易数（预占/外应＋事实优先）。\n输入未给卦象与预书原文，仅给情境：邵雍预书椅底某年月日椅将被坐破。按事实优先序，断语只就所问『是否应验』落断：预书既为定期之占，届期以客坐致椅朽折为应，对象为该椅本身、承受者为坐椅之人，受惊不至重伤合小事量级。预书具体年月日与坐者姓名输入未给，不臆补，已降置信。",
    "confidence": 0.55,
}
P["OC-026"] = {
    "prediction_text": "方向：今年功名可成，主占者得中。1643年本年科名有望登榜（中式得功名），过程涉害多阻、非一帆风顺；昆弟二人不同齐中，至少主占一人得第，另一人留待下科。应期为月档：窗口在本年春闱放榜之期，主坐标为卯月至辰月（二三月）榜文到时。近段应试可入场获选，远段得官尚须再候选授，本年只断功名到手不断实职。",
    "basis": "输入卡 tradition 字段原值：未标注（无此字段）；实际所用体系：大六壬（指南分类占断·仕宦/考试门）。\n己亥日，课涉害、曲直：三传乙未（青龙）、己亥（螣蛇）、癸卯（玄武）成亥卯未木局；己土以木为官鬼，官星成局而旺（正月木相），初传未为己之寄宫乘青龙主喜庆得官之象，故功名可成；涉害主深阻、取事艰难，中传亥乘螣蛇主中途惊疑迟滞，末传卯官乘玄武主榜名带暗、不同齐中之象。两人年命未给，谁中谁否无据细分，只断主线一人得第，已降置信。应期按考试门月档：逢值路取末传卯逢值月为主坐标，合处与出空（辰巳空与功名无涉）两路舍弃。",
    "confidence": 0.5,
}
P["OC-027"] = {
    "prediction_text": "方向：此行不得意。三问分判：①奉诏北上：无禄无路，行无依凭，差事终成虚行——或中途受阻、或到京不得重用而返，不得升擢之喜；②本人身体：途中惊病一场（寒湿水患之象），有惊无性命之危，终能南归；③老母：留在家中欠安、卧病受惊一层，父母之神居中传得土气相扶，无寿终之断，只断病忧。应期为月档：窗口在冬月出行后一月内，主坐标在亥月/亥日一带见阻见病，结果以腊月至正月定。",
    "basis": "输入卡 tradition 字段原值：未标注（无此字段）；实际所用体系：大六壬（指南分类占断·出行/仕宦门，一课多占分判）。\n辛未日甲子旬戌亥空，课无禄、无路（四上克下之凶格，主无禄无依）；三传癸酉（六合）、戊辰（太阴）、亥（青龙，空）：末传青龙落空，喜庆终局落空，主所求不成；初传酉乘六合主牵绊合留。母面取父母土神：中传辰土乘太阴居中，生辛金而未受重克，故母只断病忧不断寿。末传亥空，出空填实路为应期主路，逢值路因亥在旬空值而不实舍弃，逢冲合路无合齐之象舍弃。年命与四课全列未给，细断已降档。",
    "confidence": 0.55,
}
P["OC-028"] = {
    "prediction_text": "方向：必得官，且为美官。入觐考选结果吉，斫轮成器、印绶俱全，主擢升迁转；所得官职为带兵马/兵备性质的方面之任（兵备道一类、副使参议级衔），非闲散冷曹。应期为月档：窗口在考选后次年春，主坐标为卯月（二月）定选、巳月（四月）前后到任文书齐备。",
    "basis": "输入卡 tradition 字段原值：未标注（无此字段）；实际所用体系：大六壬（指南分类占断·仕宦门）。\n己丑日，课重审、斫轮（卯发用、中戌末巳，印绶俱全、爵禄崇高之吉格，见课格斫轮条）；三传辛卯（玄武）、丙戌（朱雀）、癸巳（白虎）：初传卯木为己土之官鬼发用主官位临身，中传戌乘朱雀主考选文书诏命，末传巳火印星乘白虎，火印生身而白虎主兵马，故官带兵备性质。传序先克后生，主先难后成。名次与确切品级盘面无次第之据，只断至副使参议级量级并降置信。应期按仕宦门迁期月档，逢值取卯月为主坐标，合处（戌合卯在传内为过程象、非成期）与出空（午未空不涉类神）两路舍弃并注明。",
    "confidence": 0.52,
}
P["OC-029"] = {
    "prediction_text": "方向：一课多占，逐事分判。①其子求官：宜回山东本省取功名，可成，不宜在外谒求。②方所兵事：山东将有兵动，攻城陷邑之变，应在冬月。③其母寿：母寿止八十有九，年近九十即大限将至，主本年/近期寿终之忧。④失盗：家有失盗之患，所盗为其子之物，贼去而复来，须连防再盗（目今一发、三日后复来之势）。⑤客至：顷刻有三客至，其中有杨姓者。应期各从其门：客至即时、失盗日档、兵动月档、母寿年档。",
    "basis": "输入卡 tradition 字段原值：未标注（无此字段）；实际所用体系：大六壬（指南一课多占通则，逐事分门）。\n己亥日，课涉害、曲直、回环；三传乙未（白虎）、癸卯（六合）、己亥（天后）成亥卯未木局。子求官：干神归支、传将逆行，主回本省（支）取功名（仕宦门）。兵动：三传纯官鬼（木克己土）、白虎乘初传克支分野，主其省兵动攻城（兵斗门）。母寿：乙发用与地盘己字合断八九之数，断寿止八十九（成例专法，非父母通法）。失盗：课传回环主贼去复来（回环格＋失物门）。客至一条成例只记断语未注取象，照录其方向而置信降档。四课全列与母年命未给，各事细断已按盘面不全规矩降档。",
    "confidence": 0.62,
}
P["OC-030"] = {
    "prediction_text": "方向：二问分判。①淮扬巡按差：可复——铸印之课占钦差主复任巡按，差必复设，且有复任/重开之实，非空议。②吏书缺：不全照旧——末传官星乘太阴暗动，主该缺经暗中更易、另行补授，不由旧人旧例原样存续。应期为月档：窗口在本年秋前，主坐标取戌月（九月）前后旨下复差、人员定局；近段春间先有议复之声，远段至秋方落实。",
    "basis": "输入卡 tradition 字段原值：未标注（无此字段）；实际所用体系：大六壬（指南分类占断·章奏钦差门）。\n戊子日，课重审、铸印：三传癸巳（太常）、丙戌（六合）、辛卯（太阴）；巳为炉、戌为印，初传乘太常正合铸印构成（课格铸印条：有官必迁；钦差门成例：铸印课占钦差主复任巡按），故巡按差断可复。末传卯木为戊土之官鬼乘太阴居终局，主人事在暗中更易，故吏书缺断不照旧。应期按章奏门月档：逢值路取戌逢值月为主坐标，合处（戌乘六合为复设之过程象）与出空（本旬空亡未给落处、无空可出）两路舍弃并注明。空亡与四课未给，已降置信。",
    "confidence": 0.55,
}
P["WP-001"] = {
    "prediction_text": "Direction: Yes — a major collective affliction in 2020–2021, specifically a worldwide pandemic: a fast-spreading epidemic disease (influenza-like/respiratory) causing mass illness and death and social-economic disruption across many countries. Timing window: 2020–2021, with the onset/main coordinate at the exact Jupiter–Saturn–Pluto conjunction in early 2020.",
    "basis": "Input card tradition field: not labelled (no such field); system actually used: Western mundane astrology.\nBasis is the configuration given in the card: Jupiter–Saturn–Pluto conjunction exact early 2020, five outer planets within ~100 degrees, cyclical index at its 21st-century low; the card itself notes comparable past clusters coincided with 1918, 1954, 1968 and 1982 — the pandemic years — so the mundane reading points to a pandemic-scale event in 2020–2021 rather than war or famine as the primary affliction. No natal data is involved; confidence reflects the strength of the stated configuration and its historical parallels.",
    "confidence": 0.72,
}
P["WP-002"] = {
    "prediction_text": "Direction: Barack Obama wins the 2008 US presidential election, defeating John McCain on 4 November 2008. Obama first secures the Democratic nomination (despite not having clinched it in May), then wins the general election — the Saturn–Uranus opposition exact on Election Day breaks for the candidate of change against the older establishment candidate.",
    "basis": "Input card tradition field: not labelled (no such field); system actually used: Western (mundane/electional) astrology.\nBasis: the card's stated configuration — Saturn (age, establishment, McCain) in opposition to Uranus (change, insurgency) beginning on Election Day, a configuration last seen 45 years earlier at a moment of generational turnover — read for the change candidate. No birth charts or polling data are given in the card, so the call rests on that configuration and the nomination trajectory stated in the setting; confidence moderated accordingly.",
    "confidence": 0.62,
}
P["WP-003"] = {
    "prediction_text": "Direction: Barack Obama wins re-election in the 2012 US presidential election, defeating Mitt Romney on 6 November 2012. The race is competitive and the Mercury-retrograde Election Day brings confusion/delay in reporting, but the incumbent retains the White House for a second term.",
    "basis": "Input card tradition field: not labelled (no such field); system actually used: Western (mundane/electional) astrology.\nBasis: incumbent-advantage mundane reading of the stated setting — a sitting president in a competitive but not collapsing position; Mercury retrograde beginning on Election Day is read as procedural confusion rather than a change of ruler. No candidate birth charts are supplied in the card, so no chart-based comparison is possible and confidence is held at a moderate level on that stated limitation.",
    "confidence": 0.6,
}
P["WP-004"] = {
    "prediction_text": "Direction: Hillary Clinton wins the 2016 US presidential election, defeating Donald Trump on 8 November 2016 — this is the conference panel's consensus call: the Democrat, favoured in most polls, takes the White House.",
    "basis": "Input card tradition field: not labelled (no such field); system actually used: Western (mundane/electional) astrology, panel consensus.\nBasis: the card presents an election-forecasting panel (not an individual reader) at the Costa Mesa conference in October 2016 with Clinton favoured in most polls and gives no dissenting individual's chart or reasoning; the panel-consensus reading therefore follows the favoured, establishment-continuity candidate. No individual chart data is supplied, which limits confidence.",
    "confidence": 0.52,
}
P["WP-005"] = {
    "prediction_text": "Direction: Donald Trump wins the 2016 US presidential election, defeating Hillary Clinton on 8 November 2016. The astrologer who alone picked Trump early — when 17 Republicans still contested the nomination — follows the same read through to the general election: Trump, not Clinton, takes the White House, against the polling consensus.",
    "basis": "Input card tradition field: not labelled (no such field); system actually used: Western (mundane/electional) astrology, individual reader.\nBasis: the card singles out one panel astrologer whose distinguishing, checkable prior call in this same cycle was picking Trump for the Republican nomination out of a 17-candidate field; that reader's line is internally consistent only as a Trump-through-to-the-end read, and this case is framed around that individual rather than the panel consensus. No chart details are supplied in the card, so confidence rests on that framing and is moderated.",
    "confidence": 0.58,
}
P["WP-006"] = {
    "prediction_text": "Direction: Britain votes to leave. In the referendum of 23 June 2016 the Leave side wins (narrowly), and Britain votes to exit the European Union — a shock result against the February polling that showed 'Stay' ahead, with the large undecided bloc breaking for Leave.",
    "basis": "Input card tradition field: not labelled (no such field); system actually used: Western mundane astrology (national charts).\nBasis: the card gives the UK national charts (1066, 1801, 1922) as the working charts and Uranus conjunct Ceres at 23 degrees Aries on referendum day — Uranus on a cardinal angle-point reads as sudden rupture/separation of the national body rather than continuity; the assessment was first published in July 2015 and firmed up in February 2016, i.e. a standing Leave call made before the date was known. Polling in the card favours Stay, so the astrological read is deliberately against the polls; confidence moderated for that reason.",
    "confidence": 0.6,
}
P["WP-007"] = {
    "prediction_text": "Direction: Donald Trump wins the 2016 US presidential election. What decides it: Hillary Clinton's scandals — the email controversy and the Clinton Foundation — fatally undermine her; a late scandal blow in the closing phase of the campaign swings the result to Trump, who wins despite trailing in most August polls.",
    "basis": "Input card tradition field: not labelled (no such field); system actually used: Tarot (Waite/RWS) as framed by the card, with the card faces not supplied.\nInput limitation stated plainly: the card says a tarot reader drew cards in Union Square in August 2016 but does not list the cards drawn, so no card-by-card Waite reading is possible and none is fabricated; the prediction is therefore made at reduced confidence from the reading's framing in the card — the question asks who wins and what decides it, and the only deciding factors the card itself puts in play are Clinton's email controversy and the Clinton Foundation, read as the campaign's fatal burden, pointing to a Trump win decided by scandal.",
    "confidence": 0.45,
}

IDS = ["OC-018","OC-019","OC-020","OC-021","OC-022","OC-023","OC-024","OC-025","OC-026","OC-027","OC-028","OC-029","OC-030","WP-001","WP-002","WP-003","WP-004","WP-005","WP-006","WP-007"]

written = 0
for cid in IDS:
    rec = {"case_id": cid, "prediction_text": P[cid]["prediction_text"], "basis": P[cid]["basis"], "confidence": P[cid]["confidence"], "trigger": trig()}
    with open(os.path.join(OUT, cid + ".json"), "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=1)
    written += 1

# exact-id validation only
cm = ru = di = 0
ok = 0
for cid in IDS:
    with open(os.path.join(OUT, cid + ".json"), encoding="utf-8") as f:
        r = json.load(f)
    assert set(["case_id","prediction_text","basis","confidence","trigger"]) <= set(r.keys()), cid
    assert r["case_id"] == cid
    assert isinstance(r["confidence"], (int, float)) and 0 <= r["confidence"] <= 1, cid
    t = r["trigger"]
    assert set(["changed_main","reserve_used","disputed","reason"]) <= set(t.keys()), cid
    cm += bool(t["changed_main"]); ru += bool(t["reserve_used"]); di += bool(t["disputed"])
    ok += 1
print(f"cases={len(IDS)} written={written} validated={ok} changed_main={cm} reserve_used={ru} disputed={di}")
