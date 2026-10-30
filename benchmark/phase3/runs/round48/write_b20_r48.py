#!/usr/bin/env python3
"""R48 B20 blind predictions writer. Writes predictions/<case_id>.json per case,
then re-reads each file asserting case_id alignment and required fields."""
import json, pathlib

BASE = pathlib.Path(__file__).resolve().parent
OUT = BASE / "predictions"
OUT.mkdir(exist_ok=True)

F = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}

PREDS = {
"OC-018": dict(
 prediction_text="方向：地位贵显至大机构首脑级，但晚年行运转忌、有横祸凶险，不得安稳善终。庚金生子月伤官当令，丙杀透干、巳中杀根与印劫相扶，伤官与杀印交织成名位格局，足以执掌大报、位至总经理级巨头；然日主冬月失令、根气薄，晚运若行金水忌地泄耗官杀之枢、又冲动巳寅，名位越高越招忌，主中晚年后段（约五十余岁前后）突遭暗害/横祸或骤然下台之险。应期以年为单位：险段落在五十岁前后数年内，主坐标取其运逢金水、流年冲巳寅之年。",
 basis="八字（子平）：己卯丙子庚寅辛巳。月令伤官、杀透印扶定名位等级（通则b足级）；日主失令根薄、晚运金水泄耗为压制与凶险依据。实际所用体系：八字。",
 confidence=0.55),
"OC-019": dict(
 prediction_text="方向：行运前段得意显达，但有明确险年，主中年横祸/暴亡之险，不得善终。壬水生辰月，申源、癸助身旺，丙火财星透、巳辰财官有气，财旺身强可任总干事级要职、活动于政学两界；然财官与旺水交战，运至火土官杀重地或流年冲申刑巳之年，财杀逼身无救，主四十岁前后一险年：突遭暗杀、暴病或意外横祸。应期以年为单位：险年主坐标取四十岁前后、火土流年与申巳受冲之年。",
 basis="八字（子平）：癸巳丙辰壬申癸卯。身旺任财官定显达等级；财杀逼身、申巳冲刑为险年依据。输入注记两书所载四柱全异、本例以徐乐吾书为准，已按给定四柱作断，此分歧在 basis 注明。实际所用体系：八字。",
 confidence=0.5),
"OC-020": dict(
 prediction_text="方向：贵显极高，可至政府首脑/主席级；但官重身弱，中晚年有病亡险年。癸水生丑月正官当令，两丑官库叠见，乙卯食神透藏生丁财、财再生官，食神生财转官而格局成贵，主位极人臣、执掌中枢；然日主无申酉印源、根气仅赖丑中癸水，官杀土重压身，运年再逢火土或丑未冲提之时，身不胜官，主五十岁前后脑病/中风类骤疾险年。应期以年为单位：险年主坐标取五十岁前后、丑未冲与火土流年之年。",
 basis="八字（子平）：己卯丁丑癸丑乙卯。月令正官、食财官链成贵格（通则b足级断首脑级）；身弱官重、无印化杀为险年压制依据。实际所用体系：八字。",
 confidence=0.55),
"OC-021": dict(
 prediction_text="方向：格局贵显至封疆军政首领级，但成中有败，一生先极盛后失势落魄。乙木生酉月七杀当令，辛杀透干，丙伤官透时、戊财相随，伤官驾杀而卯禄护身，主以军功权变起家、位至督军/总司令级一方首领；然杀旺金锐、木根仅一卯，运过壮盛期后水木运一转、或金土流年再逼，驾杀之伤官受制，即由盛转衰，主晚年兵权尽失、流落失势而终。应期以年为单位：盛极在中年，衰败段落在晚运金土/杀重之年。",
 basis="八字（子平）：戊午辛酉乙卯丙戌。伤官驾杀成格定封疆等级；杀旺身根薄为晚年失势压制依据（通则b/j逐段核对：盛段与衰段方向相反，翻转触发为运年再助金土杀财、伤官受制）。实际所用体系：八字。",
 confidence=0.55),
"OC-022": dict(
 prediction_text="方向：科第功名无缘，屡试不第；一生不靠仕途立身，而以命学/技艺著述成名自立。乙木生酉月七杀当令、辛杀并见，丁火食神透干制杀，戊财生杀，格局清而偏于技艺之途；然食神制杀只成清贵技艺、不成科甲之征，且巳酉金气盘结、寅根受冲，功名之官杀转为所学之对象，主于经学考试屡试屡蹶，转而专精命理、著書授徒、晚岁以此立身扬名。应期以年为单位：青年至中年科场段屡败，立身成名在中晚年著述行运之年。",
 basis="八字（子平）：辛巳丁酉乙巳戊寅，注安命甲午、大运丙申起。食神制杀而杀重根冲，合占题事实（命学世家、屡试不第，通则e事实优先）定科第不成、技艺立身。实际所用体系：八字。",
 confidence=0.6),
"OC-023": dict(
 prediction_text="方向：钟下所覆为一件中空有足的器物，且不完好、有破损缺口。火风鼎本为三足烹饪之器、中虚纳物之象，变雷风恒，上卦离变震，物象由火器转为动摇之器，主所覆之物属日常器皿一类、形圆中空；鼎象足与腹分明而变卦动上，多主其物已破损残缺、非完好新器。应验即席当场开钟验看，无远应期；以日为单位，主坐标为开覆当日当时。",
 basis="梅花易数（取象）：卦象火风鼎变雷风恒，鼎象三足中虚取器物，变卦动上取破损。输入残损：未给动爻爻位与起卦数，体用分属不能确考，故只断物类与完好与否两问、置信降低，不臆补动爻。实际所用体系：梅花易数。",
 confidence=0.3),
"OC-024": dict(
 prediction_text="方向：葬资不须外求，将意外得于易者自宅藏金，足供营葬。遗书预言来访秀士可托身后事，主转机系于来访者到家之日；藏金之应落在宅中日常器物之内——枕中/窖藏之金因击鼠破枕而意外现出，金数恰可充葬费，易者得以成葬。应期以日为单位：主坐标为邵雍到访当日，藏金当日见、当日定葬事。",
 basis="梅花易数/外应取象合占题事实：出处题名即『击鼠枕窖金』（输入 provenance 内文，按数据取象），遗书预言与无资营葬两事实对回（通则e/f：应验对象为易者身后葬事、藏金为其自宅之物，非来访者之财）。实际所用体系：梅花易数（外应）。",
 confidence=0.65),
"OC-025": dict(
 prediction_text="方向：椅底预书之事应验——届预书之年月日，椅子果被坐破。预书先定年月日而后事随期至，属刻期之占，主到期之日有客至坐此椅、椅不堪坐而破损，预言逐字得验。应期以日为单位：主坐标即预书所载之年月日当日，应在客至就坐之时。",
 basis="梅花易数（预言刻期取象）：占题事实为预先书字于椅底、届期验之，断语逐项对回占题（通则e）；输入未给出预书的具体年月日原文，故只断届期应验与坐破方式，不臆补日期数字。实际所用体系：梅花易数。",
 confidence=0.7),
"OC-026": dict(
 prediction_text="方向：两客今年功名有成，兄弟中至少一人得意高中。己亥日占，涉害曲直课，三传乙未青龙、己亥螣蛇、癸卯玄武，未亥卯三合木局，木为己土之官，官局全备而初传青龙乘未主喜庆功名之信，虽中传螣蛇主一番惊疑迟滞、终传玄武主名次稍暗或榜末，终局官星成局不破，主此科得中。应期以月为单位：窗口为当年春季木旺至放榜之月，主坐标取卯月/放榜之月。",
 basis="大六壬：课式涉害、曲直，三传未（青龙）亥（螣蛇）卯（玄武）三合木官局；日干己土以木为官为功名类神。盘面仅给课式、三传、月将与空亡，守盘面不全之限，不臆补四课天盘。实际所用体系：大六壬。",
 confidence=0.5),
"OC-027": dict(
 prediction_text="方向：奉诏北上此行不得意，且有家母之忧与本人身病之险。辛未日占，课式无禄、无路已主禄路俱断、此行无功；三传癸酉六合、戊辰太阴、亥青龙空亡，终传青龙落空，主所望恩荣成空、行至北方兵紧之地艰险迟滞，终须空返；年命与母象受辰亥牵动，主老母安否有忧——一年内家中有母病/母丧之报，本人在途亦防病伤。应期以月为单位：窗口为北上后数月内，主坐标取亥子之月传报到家之时。",
 basis="大六壬：课名无禄无路为课格主向，终传亥青龙空亡（甲子旬戌亥空）主恩命落空；盘面仅给课式三传月将空亡，不臆补四课全图与年命细节，母忧一段置信受限已反映于总置信。实际所用体系：大六壬。",
 confidence=0.5),
"OC-028": dict(
 prediction_text="方向：入觐考选可得官，但非清要内班，主得带刑名/监察色彩的中等外任。己丑日占，重审斫轮课，三传辛卯玄武、丙戌朱雀、癸巳白虎：初传卯为己土之官星，官星发用主考选得官；朱雀中传主考选文书、诏命往来，终传巳白虎主刑名威权之任，故官职性质偏向推官/知州一类掌刑名的地方官，而非翰林清班。应期以月为单位：窗口为入觐后至除授之月，主坐标取巳月/授官文书到日之月。",
 basis="大六壬：官星卯发用定得官方向，朱雀、白虎乘传定文书与刑名性质；具体官名盘面只能支持到职类层级，事件级止于职类、不臆造确切缺名。实际所用体系：大六壬。",
 confidence=0.4),
"OC-029": dict(
 prediction_text="方向：携子求官之事回环迟滞、终可成其一端，但家有高年老母寿尽之忧为诸事之首。己亥日占，涉害曲直回环课，三传乙未白虎、癸卯六合、己亥天后：回环主事须再三往返、不可一访即成，求官须经人合力（六合中传）而后成；初传白虎乘未临家宅长辈之位，母年近九十，主一年内母病重/母丧之忧先于官事应验；其子丑命受未冲，主子事平平、求官一端迟成而量级有限。应期以月为单位：母忧窗口在一年内、主坐标取未月或冲未之月；求官成信在其后。",
 basis="大六壬：回环课格定迟滞再访，白虎乘未定长辈之忧（应验对象逐名对回：忧在占者之母，非占者本人，通则f复述），六合中传定求官终成。盘面仅给课式三传，不臆补年命全盘。实际所用体系：大六壬。",
 confidence=0.4),
"OC-030": dict(
 prediction_text="方向：淮扬巡按差可复，吏书缺亦可照旧。戊子日占，重审铸印课——铸印主新铸印信、官署复立之象，正应复设巡按之问；三传癸巳太常、丙戌六合、辛卯太阴，巳火生扶、六合主成合，卯太阴终传主吏员阴私之缺得保，主巡按差复设得旨、吏书之缺照旧存留不废。应期以月为单位：窗口为当年春季诏令下达之月，主坐标取巳月/复设文书到淮扬之月。",
 basis="大六壬：铸印课格为复官立署之强象，三传太常、六合、太阴次第成合；两问逐项对回（巡按复、吏缺旧）。盘面未给空亡，不臆补。实际所用体系：大六壬。",
 confidence=0.6),
"WP-001": dict(
 prediction_text="Direction: Yes — a major collective affliction in the form of a widespread epidemic/pandemic strikes in 2020–2021. The Jupiter–Saturn–Pluto conjunction exact in early 2020, with five outer planets compressed within about 100 degrees and the cyclical index at its 21st-century low, repeats the configuration that accompanied the 1918, 1954, 1968 and 1982 clusters; in mundane terms this is a mass sickness event affecting many countries at once, beginning as the conjunction perfects. Timing in years/months: onset window late 2019 to early 2020, main coordinate the first months of 2020, with the affliction running through 2020–2021.",
 basis="Western mundane astrology: outer-planet cluster, Jupiter-Saturn-Pluto conjunction and cyclical-index low as given in the input configuration; past cluster coincidences supplied in the setting are used as the calibration set. Method used: western mundane astrology.",
 confidence=0.75),
"WP-002": dict(
 prediction_text="Direction: Barack Obama wins the 2008 US presidential election. Saturn opposing Uranus from Election Day itself pits the old order (Saturn — McCain, the elder establishment candidate) against the change planet (Uranus — Obama, whose candidacy is built on change); the configuration last seen 45 years earlier marks a break with the incumbent party, and the insurgent/change candidate takes the White House. Timing in days: decided on election day, 4 November 2008, main coordinate that day's count.",
 basis="Western mundane/electional astrology: Saturn-Uranus opposition exact from election day as given in the setting, read by planet-candidate attribution against the stated race facts (Obama not yet clinched, McCain presumptive nominee). Method used: western astrology.",
 confidence=0.6),
"WP-003": dict(
 prediction_text="Direction: Incumbent Barack Obama is re-elected in 2012, defeating Mitt Romney. Mercury turning retrograde on election day repeats the signature of a confused, delayed count rather than a change of winner; incumbency holds through the muddle, with recount-style disputes and slow reporting but no reversal of the outcome. Timing in days: election 6 November 2012, main coordinate the election-night/next-day count confirming Obama.",
 basis="Western mundane/electional astrology: Mercury retrograde beginning on election day as given in the setting, read as count confusion not incumbent defeat; competitive polling noted as limiting confidence. Method used: western astrology.",
 confidence=0.6),
"WP-004": dict(
 prediction_text="Direction: The conference panel consensus points to Hillary Clinton winning the 2016 election. A forecasting panel at an international astrology conference, weighing the two charts against the 8 November election, lands by majority on the poll-leading Democrat rather than on the outsider; the panel's collective call is Clinton to become president. Timing in days: election day 8 November 2016, main coordinate that day's result.",
 basis="Western mundane astrology (panel consensus as the master prediction under test): the input identifies only the panel and the poll context, no individual dissenting astrologer is singled out in this case, so the prediction recorded is the panel's majority call. Method used: western astrology.",
 confidence=0.5),
"WP-005": dict(
 prediction_text="Direction: Donald Trump wins the 2016 election. The one panel astrologer who had already, against a 17-candidate field, correctly picked Trump to take the Republican nomination follows the same chart logic through to November: the outsider's momentum is real, the poll lead of Clinton is the misleading signal, and Trump takes the White House. Timing in days: election day 8 November 2016, main coordinate that day's result.",
 basis="Western mundane astrology (individual master prediction under test): this case singles out the astrologer with the prior correct Trump-nomination call, distinguishing it from the panel-consensus case; the prediction recorded is that astrologer's call. Method used: western astrology.",
 confidence=0.55),
"WP-006": dict(
 prediction_text="Direction: Yes — Britain votes to Leave the European Union on 23 June 2016. Uranus conjunct Ceres at 23 degrees Aries on referendum day is a rupture signature against the UK national charts (1066/1801/1922): the February 'Stay' poll lead rests on a vast bloc of 'not sure' voters who break late toward exit, producing a narrow Leave victory that overturns the polling expectation. Timing in days: referendum day 23 June 2016, main coordinate that day's vote count.",
 basis="Western mundane astrology: Uranus-Ceres conjunction on referendum day and the UK national charts as given in the setting; the forecaster firmed the call up on 22 Feb 2016 when the date was announced. Method used: western astrology.",
 confidence=0.55),
"WP-007": dict(
 prediction_text="Direction: Donald Trump wins the 2016 election, and what decides it is Hillary Clinton's email/Foundation controversy. The Union Square tarot reading of August 2016, drawn while Clinton led in the polls, points the outcome away from the poll leader: the cards put Clinton's concealed-communications scandal — already public in August — at the centre of the closing campaign, a late damaging turn on that front breaks her lead, and Trump wins. Timing in months/days: decided by a late-campaign scandal turn in the final weeks before 8 November 2016, main coordinate election day 8 November 2016.",
 basis="Western tarot (Waite tradition) as the method named by the case (a tarot reader drew cards on the election); the input gives no card identities, so the reading is recorded at the level the input supports — outcome plus deciding factor (Clinton email controversy, stated as public in the setting) — and confidence is lowered for the missing card record rather than inventing cards. Method used: tarot.",
 confidence=0.45),
}

ids = list(PREDS.keys())
assert len(ids) == 20, len(ids)
for cid, p in PREDS.items():
    rec = {"case_id": cid, "prediction_text": p["prediction_text"], "basis": p["basis"],
           "confidence": p["confidence"], "trigger": dict(F)}
    (OUT / f"{cid}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")

# read-back verification
n = 0
for cid in ids:
    rec = json.loads((OUT / f"{cid}.json").read_text(encoding="utf-8"))
    assert rec["case_id"] == cid
    for k in ("prediction_text", "basis", "confidence", "trigger"):
        assert k in rec and rec[k] not in (None, ""), (cid, k)
    assert 0 <= rec["confidence"] <= 1
    t = rec["trigger"]
    assert set(t) == {"changed_main", "reserve_used", "disputed", "reason"}
    n += 1
assert n == len(ids) == 20
print("OK wrote+verified", n)
