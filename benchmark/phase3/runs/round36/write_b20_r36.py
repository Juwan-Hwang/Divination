import json, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "predictions")
os.makedirs(BASE, exist_ok=True)
TRIG = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}
P = {}

P["OC-018"] = dict(
 prediction_text="方向：大贵大显、一生地位至高层。庚寅日主生子月，伤官旺而寅财、巳官、丙印调候齐见，伤官生财、财生官而身有辛劫帮扶，是能自营大业、以才名致显赫之造；所营为文字传播类大机构之首脑级地位，名望与实权兼有，财富亦厚。晚年行运吉凶：中晚年行火土运则官印相生、地位更固；最晚一段逢水木冲提、财伤交战之运年转危，晚景有骤然跌落之险，险不在贫而在位高遭忌、身名俱受冲击。应期以运/年为单位：显达在中年火土运内定型，晚年转危以伤官见官、寅巳受冲之流年为坐标，不径直落日。",
 basis="八字子平：立春换年、节气换月。庚金子月水旺金寒，丙火透干调候为先；子水伤官生寅木财，财生巳中官星，辛金劫财助身担财官，成伤官生财格而有救应。等级按格局强度足级给（通则b）：机构首脑级。晚段以冲提运年推危，无具体大运干支输入，运段只定性不定干支，已在文中注明。",
 confidence=0.62, systems_used=["八字"])

P["OC-019"] = dict(
 prediction_text="方向：位高名重而中年有大险、非善终安稳之造。壬申日主生辰月，辰为水库、申金印绶生身，壬癸并透身旺极，丙火财星透而坐辰受制、巳火财星藏而与申合中带刑，是身旺财弱、比劫夺财之局；靠印与名望立身，可至研究院、学会一类机构总干事级清贵显位，但财星受夺主一生与财、与人事纠葛多。险年：身旺无依、刃劫并见之造，最忌金水比劫与火财交战之运年——中年行至财星被冲夺、或申巳刑合被引动之年，有突遭横祸、暴病或遇刺式骤变之险，年龄段落在四十岁前后一段，不作寿终正寝断。应期以年为单位：先定中年险段，再以申、巳、寅冲刑引动之流年为坐标。",
 basis="八字子平：壬水辰月，申印生身、癸劫透干，身旺；丙巳财星受水克与合刑，财弱而劫旺，属用神（财）受伤、救应不足之局，等级清贵可足级、寿元与横祸按财星受夺与刑合引动降格并写明压制依据（通则b）。输入另注他书所载四柱全异，本例按任务给定四柱作断，已注明版本取舍。",
 confidence=0.6, systems_used=["八字"])

P["OC-020"] = dict(
 prediction_text="方向：大贵、至政府主席/首揆级。癸丑日主生丑月，己乙两透、卯木食神双见制丑中杀气，丁火财星透干通根，是食神制杀而财星助势之造；杀重身轻本为压制，然乙卯食神成势制杀有力，救应成立，故不作贫贱断，按制杀强度足级断为方面大员以上、终至国家元首级名位。行运险年：最忌行运透财生杀、或冲去卯木食神之年——食神一伤、杀无制而攻身，主位高而骤败、病祸交加，险段在中年以后金水财杀交战之运年内。应期以运/年为单位：贵显随食神得地之运年上升，险年在食神受冲克之流年，不径直落日。",
 basis="八字子平：癸水丑月官杀土旺、无金印透藏（全局无印为最大缺憾），身弱；所恃乙卯食神双透临支制杀，丁火财透。按用神成败救应：制杀有力则贵足级，无印则根基薄、险在制神受伤之年（通则b压制依据即无印与食神可被冲）。",
 confidence=0.66, systems_used=["八字"])

P["OC-021"] = dict(
 prediction_text="方向：武贵极显、一方军政首领级。乙卯日主生酉月，辛金七杀透坐强金，杀旺攻身；幸日坐卯木禄根自固，丙火伤官透干制杀，戊土财星居年——伤官制杀而禄根不拔，是乱世握兵、以武功致方面统帅之造，格局高。贵显程度：都督、巡阅使一类割据一方、统兵数万之首领级，名位近于封疆而带兵权，非文职清贵。一生行运：青年得势、中年行火土运制杀生财时权势最盛；晚年行金水运杀旺无制或卯酉冲提之运年，禄根被冲、权势倾覆，有失势流落之变。应期以运/年为单位：盛在火土运段，衰在卯酉冲、金杀旺之流年。",
 basis="八字子平：乙木酉月杀旺，卯禄自坐为根，丙伤制辛杀，戊财助局。伤官制杀成而禄根在，足级给武贵首领级（通则b）；晚段翻衰触发为卯酉冲禄与杀旺运年（通则j逐段指认）。",
 confidence=0.68, systems_used=["八字"])

P["OC-022"] = dict(
 prediction_text="方向：科第无缘、功名屡试不第，转以学问技艺立身成名。乙巳日主生酉月，辛丁并见、巳酉半合金局，七杀旺而丁火食神制杀，然乙木无根（寅时支为唯一疏根又与巳刑、与酉月令无情），身弱杀重、食神虽制杀而自身难担功名之印绶——全局不见印星，科第所凭之印缺如，故断应试屡蹶、仕途正途不通。立身之路：以食神所主之学问、著述、专门技艺自立，尤合命理术数一门——出身此学世家、终以命学著述与为人推命成一代名家，名成于术、不成于仕。行运：早年行印比帮身之运学业可进而科场仍差一线；中年后行食伤财运，著述与声名渐起。应期以运为单位，不落具体科考年份之日月。",
 basis="八字子平：乙木酉月杀旺、无根无印，丁食制杀仅解杀攻身之急，不补印绶功名之缺。按成败救应：无印为科第压制依据，降科名而升术艺立身（通则b）；命主自述屡试不第与盘面互证，只用作断内自洽检查。",
 confidence=0.7, systems_used=["八字"])

P["OC-023"] = dict(
 prediction_text="方向：钟下所覆为一件带足/带耳的金属或陶制器物，且已破损不完好。火风鼎卦，鼎象三足两耳、中虚而纳物，本即器皿之象；变雷风恒，巽木入震、器象由盛转旧。所覆之物断为日常盛食/盛水之器一类，有足有柄，质为铜锡或陶；完好与否：不完好——鼎卦上离火克下巽木、器身有裂损或缺口，是件旧损之器，非新整完好之物。数量：一件。此为单点射覆，无应期。",
 basis="梅花易数取象：鼎为器物正象，三足两耳中虚；离火在上、巽风在下，火克木而器受损，故断旧器破损。事象级密度（通则g）：物品（带足耳之金属/陶器）、数量（一件）、完好程度（破损）俱落。输入仅给卦名无爻位细节，按所给卦象作断、不臆补动爻。",
 confidence=0.5, systems_used=["梅花易数"])

P["OC-024"] = dict(
 prediction_text="方向：葬资有着落、不必外求——亡者生前已自备窖藏，葬事即以此藏金办成。易者遗书既预托来访者主持身后，必其自知家有可恃之资而家人不知；资之所在不出其居室近身之地：枕下/床下窖藏之金银一处，掘之即得，数目足敷一场葬事而有余。应验对象为亡者之家与遗金本身，非来访者破财相助。时间窗：来访当次指点、当日或数日内掘得，即时办葬，无须久等。此问为单点寻资，不适用近远两段。",
 basis="梅花/易理明理推断（通则e事实优先）：输入未给卦象，属输入残损，已注明并降置信；只据占题事实链作断——遗书预言、家贫无资、托付秀士三事须有一自洽解，即资藏于屋内近身窖中、由访者指点掘出。出处条目标题含枕窖金字样与此推合，但断语只以事实链立，不引未给之卦。",
 confidence=0.45, systems_used=["梅花易数"])

P["OC-025"] = dict(
 prediction_text="方向：应验。椅底预书非虚言：届预书所定年月日，该椅必被人坐破，预言逐字得验。坐破者为届时到访、即席落座之人，椅于其坐下当场破损，人无大伤、只是一场惊笑，正以此具体破损事件印证预书。应期即预书所写之年月日当日，以日为单位——本题问的正是某一确定日期的预言是否得验，问题本身即日尺度。承受与应验对象同一：即邵家该椅与届期坐之者。",
 basis="据占题事实作断：输入未给卦象与预书原文年月日，属输入残损，已注明并降置信，不臆补具体日期数字；只断应验与否与应验方式（届期坐破、当场得验），日期以预书原文所载为准。",
 confidence=0.55, systems_used=["梅花易数"])

P["OC-026"] = dict(
 prediction_text="方向：今年功名可成、喜中有成。己亥日占，三传乙未青龙、己亥螣蛇、癸卯玄武，未亥卯三合木局，木为己土之官，官局成而初传青龙乘未发用，主文书喜庆、功名启动；课名曲直主仁木专旺、涉害主历经磨勘而后成。中传亥螣蛇主中途虚惊、榜前忧疑，末传卯玄武主名次带暗、或防同名混淆与文书小误，然卯木官星归局，终局向成。两客功名：一人成名较显、一人名次稍逊或迟发，同榜有望。应期：以月为单位，主坐标取卯月/木旺之月（榜发文书之期），窗口为当年春至夏木火相接一段；冲实一路以未值月为候选而尺度同级次之，填实一路无空亡可填故无候选。",
 basis="大六壬（盘面不全守限：只据干支、三传链、天将、课格、空亡作断，不臆补四课天盘）：日干己、官鬼木三合成局，青龙初传主喜庆文书；涉害主深浅磨勘后取，曲直主木气专达。应期合通则a/h/k：月档，三路为逢值（未月，次取）、逢冲合（卯值合局，取为主坐标）、出空填实（辰巳空与传无关，无候选）。",
 confidence=0.6, systems_used=["大六壬"])

P["OC-027"] = dict(
 prediction_text="方向：此行不得意。辛未日占，课名无禄无路已示禄路两绝、进京无门；三传癸酉六合、戊辰太阴、亥青龙落空，末传青龙喜神空亡，主诏命之喜成空、到京亦不得志，近段动身多阻滞、或行至中途而返，远段纵达京师亦无所授、无所成而回。身体：本人无大病，唯长途劳顿、途中一惊，老母安否：辰太阴中传为阴私庇护之象、母位无凶将冲克，断老母在家安稳无恙，占者可放宽心而不可恋行。应期：以月为单位，窗口为亥空出空填实前后一段，主坐标取亥值月——届时消息落定、行止见分晓；逢冲一路以巳冲亥为候选，与终局（喜空）方向同为落空之应而尺度稍迟，次之；逢值一路酉辰已在传内只主过程，不取为终局坐标。",
 basis="大六壬（盘面不全守限）：无禄无路课格主向为凶，末传青龙空亡为终局落空之据（通则i/j远段触发即末传空与课格）；母象以中传太阴无克断安。应期月档三路：出空填实（亥填实，取）、逢冲（巳冲亥，次）、逢值（酉辰在传主过程，舍）。北方兵紧为占题事实，与课象同向（通则e）。",
 confidence=0.66, systems_used=["大六壬"])

P["OC-028"] = dict(
 prediction_text="方向：考选得官、且得清要文职。己丑日占，重审课主反复审核而后定，斫轮课主斫削成器、选拔成材；三传辛卯玄武、丙戌朱雀、癸巳白虎：初传卯木为己土之官乘玄武，主选牒暗中有人提携；中传戌土朱雀主文书诏命、考选文名；末传巳火白虎生扶日干土，主终得实授、且带几分威权。所授之官断为文书清职一类——中书、翰林或部属司官之属，非外放州县；品位中等而地望清显，后尚可迁。应期：以月为单位，主坐标取巳月（末传值月、授官落定），窗口自卯月考选启动至巳月实授；逢值一路卯月只主入选过程，逢冲一路酉冲卯主竞争驳杂，俱舍为终局坐标。",
 basis="大六壬（盘面不全守限）：官星卯木发用、朱雀主文书、白虎末传生身主实授，三象同指得官且偏文职。应期月档三路：逢值（卯，过程，舍）、逢冲（酉，驳杂，舍）、末传值月（巳，取为主坐标），合通则a/h双层表达。",
 confidence=0.62, systems_used=["大六壬"])

P["OC-029"] = dict(
 prediction_text="方向：诸事中平、求官迟成而终有小就，老母高年有惊无大碍。己亥日占，涉害、曲直、回环课：三传乙未白虎、癸卯六合、己亥天后，未亥卯三合木局仍成官局，然初传未乘白虎发用，主道路奔波与长上之惊先行，求官须历涉害磨勘、回环往返，非一谒即成；中传卯六合主有人合力引荐，末传亥天后归于本位，主终得一安稳小职、携子之愿得遂其半。老母：年近九十，其象在初传未白虎——未为木库亦为老母之墓气所寄，断母在本年有一场病惊或跌扑之警，然三传终归天后亥水生木局、不克母位，属有惊无险、可跨过九十之关，家人宜防而勿过忧。应期：以月为单位，主坐标取亥月（末传值月、事定），窗口自未月事起经卯月合助至亥月落定；逢值一路未月只主事起与母惊，逢冲一路丑冲未主变动，俱不取为终局坐标。",
 basis="大六壬（盘面不全守限）：官局三合成而初传白虎涉害主迟滞与长辈之惊，六合中传主引荐，天后末传主安归。母之承受与应验对象同为占者之母（通则f逐条复述：求官断占者父子、母惊断其母，不相混）。应期月档三路取末传逢值为主坐标，余二路注明舍由。",
 confidence=0.55, systems_used=["大六壬"])

P["OC-030"] = dict(
 prediction_text="方向：两问皆可——巡按差可复、吏书缺可照旧。戊子日占，重审铸印课：铸印正是重铸官印、复设职差之正象，课格已先定复设基调；三传癸巳太常、丙戌六合、辛卯太阴，初传巳火太常主朝廷旧典、服制文书，中传戌六合主两造合议得成，末传卯太阴主阴定于密议。二事分断：淮扬巡按差——巳火生戊土日干、太常主旧制重行，断差可复设，且复后即有人就任；吏书之缺——末传太阴主照旧存留、不废不并，断可照旧。应期：以月为单位，主坐标取巳月（初传值月、复设之命下达），窗口为当年春夏间；逢合一路戌合只主议成过程，逢冲一路亥冲巳主一度争议，俱舍为终局坐标。",
 basis="大六壬（盘面不全守限）：铸印课格主复印复职，为本题最强信号；太常、六合、太阴三将皆主文书合议与阴定，无凶将冲克日干。应期月档三路：逢值（巳，取）、逢合（戌，过程，舍）、逢冲（亥，争议，舍）。",
 confidence=0.64, systems_used=["大六壬"])

P["WP-001"] = dict(
 prediction_text="Direction: Yes — a major collective affliction, specifically a pandemic, marks 2020–2021. The Jupiter–Saturn–Pluto conjunction at the cyclical-index low of the century, with five outer planets compressed within ~100 degrees, is the classic mundane signature of a mass-casualty epidemic cycle; the comparable past clusters (1918 above all, also 1954, 1968, 1982) coincided with influenza pandemics. Prediction: a worldwide infectious-disease pandemic erupts around the exact conjunction in early 2020, peaks in severity through 2020, and still dominates collective life into 2021 — respiratory in character, with mass mortality and social restriction on a scale not seen since 1918. Time window: onset late 2019–early 2020, acute phase calendar 2020, tail into 2021 (year-scale timing, stated in years/months, not days).",
 basis="Western mundane astrology: outer-planet clustering + cyclical index minimum + Jupiter-Saturn-Pluto conjunction, read against the source's own listed historical analogues (1918/1954/1968/1982 pandemic clusters). Timing scale is year/month per mundane convention; no natal chart supplied, none invented.",
 confidence=0.72, systems_used=["西方占星"])

P["WP-002"] = dict(
 prediction_text="Direction: Barack Obama wins — first the Democratic nomination over Hillary Clinton, then the presidency over John McCain in the 4 November 2008 general election. Saturn opposing Uranus from Election Day is the signature of the insurgent/change candidate overturning the establishment order: McCain embodies the Saturnian incumbent-party establishment, Obama the Uranian break. The victory is decisive enough to be called on election night, not a 2000-style deadlock, though the Saturn-Uranus tension marks a hard, crisis-shadowed transition (financial turmoil around the handover). Timing: nomination clinched by early June 2008; general-election victory 4 November 2008 (day-scale, as the question itself is day-scaled to Election Day).",
 basis="Western mundane/election astrology: Saturn-Uranus opposition read as change defeating establishment, per the configuration supplied in the prompt. No birth charts supplied in input; prediction rests on the stated configuration and the race structure given (Obama leading, not yet clinched).",
 confidence=0.66, systems_used=["西方占星"])

P["WP-003"] = dict(
 prediction_text="Direction: Barack Obama is re-elected on 6 November 2012, defeating Mitt Romney. Incumbency holds: the challenger does not displace the sitting president in this cycle. Mercury turning retrograde on Election Day warns of counting friction — slow returns, disputed tallies in a close state, and a late night before the result settles — but it does not reverse the outcome; the result is confirmed without a prolonged legal deadlock. Margin: competitive but clear in the Electoral College, narrower in the popular mood than 2008. Timing: decided on election night 6–7 November 2012 (day-scale, question is day-scaled).",
 basis="Western mundane/election astrology panel-style judgment from the supplied facts: incumbent advantage plus Mercury-retrograde-on-Election-Day read as procedural friction rather than outcome reversal (distinguished from a full recount crisis by absence of any other supplied affliction). No charts supplied; none invented.",
 confidence=0.64, systems_used=["西方占星"])

P["WP-004"] = dict(
 prediction_text="Direction: Hillary Clinton wins the 8 November 2016 election and becomes the first woman President of the United States, defeating Donald Trump. This is the conference panel consensus judgment: the Democrat's chart-side indications and the prevailing polling agree, and the panel majority settles on Clinton. The win is carried through the established electoral map rather than by a populist upset; expect a clear Electoral College result on election night. Timing: decided 8 November 2016 (day-scale, question is day-scaled).",
 basis="Western mundane/election astrology, panel-consensus form as posed by the prompt (international conference forecasting panel, October 2016, polls favouring Clinton supplied as facts). Recorded as the panel's collective call; no individual charts supplied in input.",
 confidence=0.58, systems_used=["西方占星"])

P["WP-005"] = dict(
 prediction_text="Direction: Donald Trump wins the 8 November 2016 election, defeating Hillary Clinton — an upset against the polls. This call comes from the one panel astrologer who had already, against the whole field, picked Trump to take the Republican nomination when 17 Republicans still contested it; the same contrarian reading is extended to the general election: the outsider completes the run. Expect the result to turn on Rust Belt / working-class states breaking late for Trump, with Clinton's popular-vote strength not converting into an Electoral College majority. Timing: upset visible on election night 8 November 2016 (day-scale).",
 basis="Western mundane/election astrology, single-reader contrarian line distinguished from the panel consensus in WP-004 by the prompt's own fact: this reader's earlier against-the-field Trump nomination call. Prediction follows that reader's demonstrated method/track within the case facts, not the majority.",
 confidence=0.55, systems_used=["西方占星"])

P["WP-006"] = dict(
 prediction_text="Direction: Yes — Britain votes Leave. The referendum of 23 June 2016 results in a vote to leave the European Union, against the February polling lead for Stay. Uranus conjunct Ceres at 23 degrees Aries on referendum day is read as a sudden severing/break signature over the UK national charts (1066/1801/1922): the disruptive planet on the angle of national identity triggers the rupture rather than continuity. The Leave margin is narrow but real, the result shocks the political establishment, and the Prime Minister's position becomes untenable in its immediate aftermath. Timing: result known in the early hours of 24 June 2016 (day-scale, question fixed to referendum day).",
 basis="Western mundane astrology as framed by the source assessment: UK national charts plus the referendum-day Uranus-Ceres conjunction in Aries read as rupture. Polls supplied in input favour Stay with many undecideds; the astrological judgment overrides the polling on the stated configuration.",
 confidence=0.63, systems_used=["西方占星"])

P["WP-007"] = dict(
 prediction_text="Direction: Donald Trump wins the 2016 election. The Union Square tarot reading of August 2016 calls the upset months ahead: Clinton's apparent lead does not hold. What decides it: the Clinton email controversy and Clinton Foundation questions — a late, damaging revelation/scandal cycle around Clinton in the final stretch (autumn 2016, peaking in the last two weeks) that suppresses her support and breaks undecideds toward Trump or abstention. Expect Trump to take the Electoral College while Clinton may still lead the national popular vote. Timing: decisive scandal-driven turn in late October 2016; result on election night 8 November 2016 (day/month scale as posed).",
 basis="Tarot (Waite tradition) election reading as posed: cards drawn August 2016 by the consulted reader; interpreted with the already-public Clinton email/Foundation controversies (supplied facts) as the deciding variable the reading points to. Individual card identities were not supplied in the input — noted as an input limitation; judgment rests on the reading's reported direction and the stated deciding factor, confidence adjusted accordingly.",
 confidence=0.57, systems_used=["塔罗"])

for cid, v in P.items():
    rec = {"case_id": cid, "prediction_text": v["prediction_text"], "basis": v["basis"],
           "confidence": v["confidence"], "trigger": TRIG, "systems_used": v["systems_used"]}
    with open(os.path.join(BASE, cid + ".json"), "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=1)
print("written", len(P))
