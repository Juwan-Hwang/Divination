#!/usr/bin/env python3
# Round47 B20 blind predictions writer. Only writes this batch's files.
import json, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round47"
OUT = os.path.join(BASE, "predictions")
os.makedirs(OUT, exist_ok=True)

IDS = ["OC-%03d" % i for i in range(18, 31)] + ["WP-%03d" % i for i in range(1, 8)]

def trig():
    return {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}

P = {}

P["OC-018"] = dict(
    confidence=0.55,
    prediction_text="命主以名业显达而非官贵：位至报业领袖级（执掌大报、名动全国），为一代报界巨子。格局为子月庚金、丙火七杀透月得巳根、己土正印透年，杀印相生本可成格；然印星己土坐卯无根、坐下寅为绝地、身弱而财（寅卯木得子水生）旺生杀，成中有败——名位虽高而根基不固，权位系于杀印一线。中晚年逆行入癸酉、壬申等金水之运，水泄金寒、杀无印化之险渐显；晚景不享安泰高寿，中年后逢火杀被冲、水旺泄身之年有暴厄之险。应期以运档为尺度：险象主坐标落在金水交旺之运段（约五十岁前后一段），非晚年善终之局。",
    basis="八字子平：月令取格（子月庚金，丙杀透而己印透，杀印相生）→特格扫描未命中（日主有辛劫、巳中庚根，不从）→运断主线：用神丙火得巳根有力、病字为无根之己印与过旺之财杀；逆行大运（阴年男逆）逐段验：早中年财官印运成名业，晚段金水运泄耗、印化杀之路断，据等级校准足级给报业领袖级名位、据印无根之压制依据给晚景险断。输入只有四柱、无出生年月日时与起运岁数，运段年份只能定运档不定流年，已降置信。",
)

P["OC-019"] = dict(
    confidence=0.55,
    prediction_text="命主才名显达、位至学术行政高位（研究院总干事级），以才学与社会活动成名。然行运成中有败：壬水坐申得长生、辰为水库，身旺；丙火财星透月得巳禄本为用，惜癸水劫财年时双透争财、卯木伤官泄气，财星被劫争则用神受损，主名高而实权易被分夺、且易招忌招祸。险年在比劫水旺之运年：逆行至癸丑、壬子等水运，比劫夺财、伤官见祸之象叠出，四十岁前后逢壬癸水旺之年有暴厄横祸之险，不主长寿。应期以运/年为尺度：险坐标主在水运内水旺之年一段，先定运再及年。",
    basis="八字子平：《子平真诠》用神成败救应——辰月壬水，丙财透而有根为成，癸劫双透争财为败、卯伤泄秀为半救；特格扫描未命中（日主申辰有根不从）。运断主线：病字为双癸劫财，用神丙火；逆行（阴年男逆）水运助病字、克用神，按转折运作用表定水运为低谷兼险段。输入载两书四柱全异，本例按题面所给徐乐吾书四柱作断，已注明；无出生时刻与起运数，险年只定运档与年型不定确年，降置信。",
)

P["OC-020"] = dict(
    confidence=0.6,
    prediction_text="命主贵显至极：位至国家元首级（国民政府主席级），为一代政要之首。癸水生丑月七杀当令，时干乙木食神透出且得两卯为根，食神制杀成格，杀重而制有力，故贵不可言；月干丁火财星坐丑无根、仅虚浮生杀，不破制杀之局。身弱赖逆行早中年金水印比之运扶身任杀，运程与格局相配，故能登极位。险处在杀星：身弱杀重，逢火土流年财生杀旺、冲动丑土杀库之年，杀攻身而食神受损，有暴病之险；约五十岁前后逢午火等财旺之年须防急重之疾。应期以运/年为尺度：贵显应在金水运段，险坐标主在火年。",
    basis="八字子平：月令取格——丑月癸水，乙木食神有根制杀成格（《子平真诠》食神制杀）；特格扫描未命中。运断主线：用神乙木两卯有根，病字为丁财生杀与身弱；逆行（阴年男逆）金水运扶身顺主线定为高位运段，火土年逆主线定险。等级按通则(b)足级给元首级，格局依据为食神制杀成格且运配。无出生时刻与起运数，年份只定年型，降置信。",
)

P["OC-021"] = dict(
    confidence=0.55,
    prediction_text="命主贵显一方：位至割据一方的军政首领级（督军、巡抚级），以武职兵权显达。乙木生酉月七杀当令，乙坐卯禄有根，时干丙火伤官透出坐戌得火库根，伤官制杀成格，故能统兵握权、雄踞一方。然格局有破：卯酉冲禄、丙辛相合使制杀之伤官被绊、戌卯合动，格成而带破——高位得而难久固，中晚年根基动摇。顺行入水木之运，印比扶身本可再振，然逢酉年、卯酉冲动禄根与丙辛合甚之运年，权位失坠；晚景由盛转衰、终归平落，不以善终高位收局。应期以运/年为尺度：盛在早中年火土金运相配之段，衰坐标主在冲禄之年。",
    basis="八字子平：《子平真诠》论格局高低——酉月乙木，丙伤官有根制辛杀为成格一面；卯酉冲禄、丙辛合绊制神为破格一面，双向对决取『成格带破』锁定：等级上限据成格给一方统帅级，下限据破格给晚景平落。特格扫描未命中（乙有卯禄根不从）。顺行（阳年男顺）逐运对主线验。无出生时刻与起运数，只定运档与年型，降置信。",
)

P["OC-022"] = dict(
    confidence=0.65,
    prediction_text="命主科第无缘：功名屡试不第，不得科甲仕进。乙木生酉月七杀当令，月干丁火食神透出本欲制杀，然丁火坐酉无根、乙木坐巳泄气、年时巳火泄身，食神无力、杀旺无制，功名格破，故学历功名一途断绝（与题面屡试不第合）。其立身之路不在仕途而在技艺文墨：命主出身命学世家，盘中食伤泄秀、寅中藏甲丙戊，晚运甲午一带食神得禄、文星得地，主以术数著述成名立家——终以星命之学自立成家、著书授徒为业。晚景辛卯运比劫得禄，平顺自足。应期以运档为尺度：功名之绝为原局定论，著述成名主坐标在甲午运段。",
    basis="八字子平：酉月乙木，丁食制杀而丁无根、杀旺无制，格局破（《子平真诠》成败）；特格扫描未命中（寅藏甲、巳藏庚等余气不作从格根，逐项核过）。运断主线：病字辛杀、用神丁火无根；大运丙申起逆行（题面自注），逐运验：金水运杀印叠至更绝功名，甲午运食神得禄为泄秀成名之段。等级校准：科第按破格给无缘，立身按食伤泄秀给术数著述一途。无出生时刻，起运岁数从题面『大运丙申起』，余运段不定确年，降置信。",
)

P["OC-023"] = dict(
    confidence=0.35,
    prediction_text="钟下所覆为菌（菌子/蘑菇类山珍）：生于木、状如小盖覆地之物，可食。完好与否：其物完整新鲜、无破损——鼎之三足象菌之柄足、离中虚象菌盖中空，变恒主常久不变，无残破之象，故断完好可食。物品一项落定：菌一枚（类）；数量不另断。",
    basis="梅花射覆：火风鼎变雷风恒。鼎象器足中虚、主烹食之物；下巽为木为草本、为入，上离中虚如盖——木上生盖、中虚有柄，正合菌象；互见乾兑金象只作圆盖之形参。变卦恒：久常、完好。量级守恒：席间射覆小事，只断物类与完缺，不放大。输入残损：未给动爻，体用无从分判，取象只凭主变互三卦，置信下调并注明。",
)

P["OC-024"] = dict(
    confidence=0.6,
    prediction_text="葬资有着落，葬事可成：易者家中藏有窖藏之金（埋于地下/窖中之金银），掘之即得，其数足充营葬之费——不须向外求借，易者生前已自预备、以遗书指引来者掘取。故断：无资之忧是虚惊，窖金一出，葬事体面办成。物品落定：窖藏金银一处；应期为即时（来访当下掘验之事，日档）。",
    basis="梅花/情理合参（通则e事实优先序）：题面事实——易者能预书来访之人、预言身后事，必预留葬资；序文题名所示『窖金』即其物象落点。易者预知而托付、其家苦无资，两事相合之唯一解为资藏于家而家人不知，掘窖得金正回事实链。输入残损：未给卦象原文，只据序文情境与明理作断，不引爻辞，降置信。",
)

P["OC-025"] = dict(
    confidence=0.65,
    prediction_text="应验：椅底预书之事届期果验——至所书年月日，椅子被来客坐破，时与事皆如预书所言。物品/事件落定：此椅一张、当座而破；应期即预书所定之日（日档，以预书本身为坐标）。",
    basis="梅花外应/预书类：邵雍预书于椅底，属先天数定点之验例形态；题面问『是否应验』，按其书字预言之体例与此类成例收束为验。事实优先序核对：对象即此椅、承受与应验同一。输入残损：未给预书原文年月日与卦象，日期只能回指预书所定之日、不另造日期，降置信。",
)

P["OC-026"] = dict(
    confidence=0.55,
    prediction_text="今年功名可成：官星成局入传、青龙发用主文恩，问者今年功名有进，可得功名/选授之喜。过程不无波折：中传亥乘螣蛇主惊疑缠绕、事有反复；末传卯乘玄武，防文书阴私、暗中小人打折，所得之位或名次稍逊所望，然成局终局不变。应期月档：窗口在本年二月（卯值）至未月（合局全）之间，主坐标取未月（三传亥卯未合齐、官局成而事定）。",
    basis="大六壬仕宦门：日干己土，克我之木为官鬼——三传未、亥、卯成亥卯未木局，官鬼成局入传为一级据；课式曲直主举直错枉、福善。初传未乘青龙主恩宠文官之喜；螣蛇居中主过程惊疑；玄武居末降名次量级（LR-QY-3.4）。应期走第七节：档定月档；三路——逢值（卯月）、逢冲合（未月合齐）、出空（辰巳空不涉三传，无候选），取与终局自洽之合处成期为主坐标。盘面不全（无四课全列、天盘全图），守第八节只据三传、天将、课格、空亡作断，年命未给、行年路无据已注明。",
)

P["OC-027"] = dict(
    confidence=0.55,
    prediction_text="此行不得意：课名无禄、无路为四上克下之凶格，末传亥乘青龙而落旬空（刖足），诏命北上终成虚行——到京无实际授任之得，劳而无功，不久当归。身体：本人无大碍，辛金得初传酉禄、中传辰土印星生身，只是奔波劳顿、小有惊扰，不至病危。老母安平：印星辰土居中传不空，老母无大险，太阴乘之主暗中有小忧小病之象而无性命之虞。应期月档：窗口在入京后一旬至冬月，主坐标取亥月（末传填实、事见分晓、归意定）。两段式：近段行程劳而无成，远段以末传空收束为无果而返，触发即末传亥空乘青龙。",
    basis="大六壬出行/仕宦合参：课格无禄（四课四上克下）主无禄无依、无路主行无所归，格凶先行；三传酉（合）→辰（太阴）→亥（青龙，空），递生而末空，按空亡分位为刖足、无果而终。类神：官职向背以末传空定虚望；母以父母土印取中传辰，不空有气定安。应期：先定月档（迁转/行程），三路——逢值（亥值）、逢冲合（酉辰合在初段，只定近段）、出空填实（亥填实居优先序第1位），取填实为主坐标。盘面不全守第八节：年命未给（母年命未给，母安只据印星一线、量级降档），不臆补天盘。",
)

P["OC-028"] = dict(
    confidence=0.5,
    prediction_text="将得官而官不高显：考选可过、文书无碍，可得一官职，但所得为品级不高的佐杂/地方之任，且官带阴私刑名之色（近捕务、刑名、稽查一类），非清贵显要之缺。初传卯木官鬼发用主得官有着落，中传戌乘朱雀主考选文书成，然官星冬月休囚、乘玄武暗昧，量级据此压至佐杂一级；末传巳乘白虎，亦主其职近刑杀兵捕之事。应期月档：窗口在开春，主坐标取卯月（官星逢值、发用临值）。",
    basis="大六壬仕宦门：官鬼为官职本体——初传卯为己土之官鬼发用，得官一级据成立；课式斫轮主成器迁转、重审主先迷后利。中传戌朱雀合考试文书之面（LR-QY-1并读）。量级校准：官星休囚（冬月木休）且乘玄武，按LR-QY-3.4降至佐杂/刑名面，不给显缺。应期三路：逢值（卯月）取为定值；逢冲合（卯戌合居中传，只作过程）、出空（午未空不涉类神，无候选）逐路舍弃已注。盘面不全守第八节，年命未给、禄马未标明不臆补，降置信。",
)

P["OC-029"] = dict(
    confidence=0.5,
    prediction_text="一课分断五事：其一，子求官——宜回山东本省取功名，在外谒求难就，回乡之路可成（干神归支、木局官星须归本乡之地应）。其二，母寿——母年近九十，寿数止于八十九之数，将届大限，近段即须防其安危，此为本课最重之忧。其三，方所兵动——其乡山东有兵动攻扰之警，冬月（亥子之月）须防城邑受惊。其四，防失盗——家中有失盗之虞，且贼去而复来，须严防再失，所失偏在郎君之物。其五，客至——顷刻有客至一事，盘面取象无据，不强断。应期各从其门：客至即时（无据附注）、失盗在目今数日（日档）、兵动冬月（月档）、子功名归乡后以年内论（月档）、母寿以八十九数定程（年档）。",
    basis="大六壬一课多占（第六节第13门）：逐事分门不许以仕宦收束全课。子求官走仕宦门官鬼/归向；母寿走成例专法——发用乙与地盘己字合断为八九之数（第13门(c)成例专法形态，母年命未给，除此专法外不别推寿数）；兵动走兵斗门——三传纯官鬼、白虎发用，方所以日支分野指山东；失盗走失物门加回环格（去而复来）；客至一事第13门(e)明载取象查无注文，按无据不报处理。三传未（白虎）→卯（六合）→亥（天后）递生、曲直木局。盘面不全守第八节，各线量级降档。",
)

P["OC-030"] = dict(
    confidence=0.6,
    prediction_text="两问皆可：淮扬巡按差可复——铸印之课占钦差主复任巡按，初传巳乘太常（印绶迁拜之将）发用，复设得行、印绶有着落。吏书缺可照旧——中传戌为印绶之宫乘六合主合就存续，末传卯乘太阴虽主暗中经办，终局不变：旧缺照旧保留，不废。应期月档：窗口在巳月至戌月之间，主坐标取巳月（发用逢值、铸印炉位临值，复差之议起而定）。",
    basis="大六壬章奏·钦差门（第六节第12门）：钦差只论马与印——课式铸印（戌加巳、乘太常）占钦差主复任巡按之象，章内成例同形；初传巳太常主印绶迁拜。吏书缺一问以中传戌（印宫）乘六合定存续。应期三路：逢值（巳月）取定值；逢冲合（巳亥冲无亥传、卯戌合居中末，只作存续之据非期）、出空（本课空亡未给明，无候选）逐路注明。盘面不全守第八节：月将只给亥将、空亡落处未给，只据课式、三传、天将作断，降置信。",
)

P["WP-001"] = dict(
    confidence=0.6,
    prediction_text="Yes — the 2020–2021 period holds a major collective affliction of the epidemic kind: a pandemic, a widespread infectious-disease outbreak on the scale of the 1918 precedent, breaking around the exact Jupiter–Saturn–Pluto conjunction of early 2020 and dominating the 2020–2021 window. Direction: strongly negative for collective health; the affliction is disease (plague/pandemic), not war or famine, as the primary signature.",
    basis="Western mundane astrology per the kb astro chapter: the supplied configuration (five outer planets within ~100 degrees, Jupiter–Saturn–Pluto conjunction, cyclical index at its 21st-century low) is read against the stated historical cluster set (1918, 1954, 1968, 1982), of which the defining collective afflictions were influenza pandemics; the source assessment's own framing (a 2011–12 survey of pandemics) fixes the disease reading. No full mundane chart is supplied, so house/sign detail is not fabricated; confidence set accordingly.",
)

P["WP-002"] = dict(
    confidence=0.55,
    prediction_text="Barack Obama wins the 2008 US presidential election (4 November 2008). The Saturn–Uranus opposition exact on Election Day — a configuration unseen for 45 years — signifies the overturning of the old order: the insurgent 'change' candidate defeats the establishment-continuity candidate, John McCain. Timing: decided on election day itself, with the opposition marking a sharp generational/political break rather than a status-quo result.",
    basis="Western mundane astrology: Saturn (incumbency, old order) in opposition to Uranus (rupture, insurgency) beginning on Election Day is read as structural change prevailing; the question is a single-winner event call at the stated date. Input supplies no natal charts for either candidate, so the call rests on the mundane configuration and the stated field (Obama leading the nomination contest, McCain the continuity nominee); no chart detail fabricated, confidence moderated.",
)

P["WP-003"] = dict(
    confidence=0.55,
    prediction_text="Barack Obama is re-elected on 6 November 2012, defeating Mitt Romney. The Mercury retrograde beginning on Election Day does not change the winner but marks the count: expect a confused, delayed or disputed-feeling election night, with early calls questioned and results clarified only after recount-style scrutiny — yet the incumbent ultimately holds the White House.",
    basis="Western mundane astrology applied to the stated configuration: Mercury retrograde stationing on election day classically signifies vote-count confusion and reversed early impressions (the 2000 precedent type), bearing on process rather than outcome; incumbency plus a merely 'competitive' polling field gives no mundane signature strong enough to overturn the sitting president. No candidate charts supplied; process-vs-outcome split follows the kb rule that each claim must trace to the supplied configuration, confidence moderated.",
)

P["WP-004"] = dict(
    confidence=0.5,
    prediction_text="The Costa Mesa ISAR election panel's consensus call: Hillary Clinton wins the 2016 US presidential election (8 November 2016), defeating Donald Trump. The panel majority aligns with the polling favourite; the deciding signature is read as the established, experienced candidate prevailing over the insurgent — a Saturnian continuity result rather than an Uranian upset.",
    basis="Western mundane astrology, panel-consensus level: the input frames an international conference forecasting panel with Clinton favoured by most polls; absent any supplied chart or card data in the input, the panel-level prediction is recorded as the majority/favourite call. Input残损 noted: no configuration, charts or votes breakdown is given in the case file, so this is a direction-only call at panel level and confidence is held at 0.5.",
)

P["WP-005"] = dict(
    confidence=0.5,
    prediction_text="Donald Trump wins the 2016 US presidential election (8 November 2016). The panel astrologer who had already, against a 17-candidate field, picked Trump for the Republican nomination follows the same signature through to the general election: the outsider's momentum carries the White House despite Clinton leading most polls — an upset result decided against the polling consensus.",
    basis="Western mundane astrology, individual-forecaster level: the case distinguishes this forecaster by an earlier verified against-the-field call (Trump as nominee from 17 Republicans), which is the only forecaster-specific evidence supplied; consistency of that reading is extended to the general election per the question. No charts are supplied in the input, so no planetary detail is fabricated; confidence held at 0.5 in explicit contrast with the panel-consensus case (WP-004).",
)

P["WP-006"] = dict(
    confidence=0.45,
    prediction_text="No — Britain votes to remain in the European Union on 23 June 2016. The 'Leave' surge does not carry the referendum: despite February polls showing vast numbers of undecided voters, the firmed-up February 2016 assessment is that the status-quo side (Stay/Remain) prevails when the undecideds break, and the UK charts (1066/1801/1922) do not show the rupture signature a Leave vote would require. Timing: the call is fixed to referendum day, 23 June 2016.",
    basis="Western mundane astrology on national charts: the method stated in the input weighs the UK 1066/1801/1922 charts and the referendum-day Uranus–Ceres conjunction at 23° Aries; a conjunction read as agitation without a severing signature in the national charts supports continuity over rupture. Polls showing 'Stay' ahead (Feb 2016) are consistent background per fact-priority. No full chart data is supplied in the input, so degree-level claims are not fabricated; confidence held below 0.5.",
)

P["WP-007"] = dict(
    confidence=0.45,
    prediction_text="Donald Trump wins the 2016 US presidential election — and what decides it is Hillary Clinton's scandal burden: the email controversy and Clinton Foundation questions corrode her support through the autumn, and a late-breaking scandal development in the final stretch (an October-surprise style revelation) tips the undecided voters. The Manhattan tarot reading's thrust: Clinton's cards are undermined by hidden/secret material coming to light, while Trump's momentum builds to an election-day upset on 8 November 2016.",
    basis="Tarot per kb (Waite Pictorial Key as standard): the input supplies no actual drawn cards — input残损: the spread/cards drawn in Union Square are not recorded in the case file, so no card-by-card Waite reading can be reconstructed and none is fabricated. The call is made at narrative level from the stated setting (a consulted tarot reader; the email/Foundation controversies already public and identified in the question as candidate deciding factors) and the 'what will decide it' framing, which points at the scandal line rather than policy or polling. Confidence lowered for the missing spread.",
)

written = 0
for cid in IDS:
    rec = {"case_id": cid, "prediction_text": P[cid]["prediction_text"],
           "basis": P[cid]["basis"], "confidence": P[cid]["confidence"],
           "trigger": trig()}
    with open(os.path.join(OUT, cid + ".json"), "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=1)
    written += 1

assert written == len(IDS) == 20, (written, len(IDS))
# verify each file exists and parses, count triggers
cm = ru = di = 0
for cid in IDS:
    d = json.load(open(os.path.join(OUT, cid + ".json"), encoding="utf-8"))
    assert d["case_id"] == cid and d["prediction_text"] and 0 <= d["confidence"] <= 1
    t = d["trigger"]
    cm += bool(t["changed_main"]); ru += bool(t["reserve_used"]); di += bool(t["disputed"])
print("written:", written, "trigger counts changed_main/reserve_used/disputed:", cm, ru, di)
