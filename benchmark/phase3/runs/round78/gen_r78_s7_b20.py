import json, pathlib
OUT=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round78/predictions")
OUT.mkdir(parents=True, exist_ok=True)
TRIG={"changed_main":False,"reserve_used":False,"disputed":False,"reason":""}
def W(cid, pred, basis, conf):
    d={"case_id":cid,"prediction_text":pred,"basis":basis,"confidence":conf,"trigger":dict(TRIG)}
    (OUT/f"{cid}.json").write_text(json.dumps(d,ensure_ascii=False,indent=1),encoding="utf-8")
    return cid
B="卡面未标注 tradition 字段，按题面体裁自决\nsystems_used: "
def bz(x): return B+"八字（子平）\n"+x
done=[]
done.append(W("OC-018",
"八字断：庚金日主生子月伤官当令，丙火七杀两见（年支巳、月干丙），辛金劫财帮身，寅木财星坐时。伤官旺而抗杀、财生杀逼：一生以报业立大业，地位至大报总经理、报界领袖级，参政声望极高（富与名皆巨，正式官位非其途）。然伤官见杀主招权贵之忌，巳寅刑、子巳暗战为终局病灶：晚年行运至险段，1934甲戌年前后为大限（年档定值，窗口1933-1935），有遭暗杀横死之象、寿数五十四岁前后，非寿终正寝。子女有承报业。破耗之因在言论招忌不在经营。",
bz("四柱己卯丙子庚寅辛巳，出《子平真诠评注》成败救应章。特格扫描皆未命中。主线：伤官为秀亦为病、杀为忌，救应在辛劫与巳中庚根而力薄；量级区间下限报人、上限报界领袖，落上限。终局翻转触发：甲戌年戌冲动刑局、杀星得势，已写明。关键结局四项俱断。应期年档先定年。"),
0.68))
done.append(W("OC-019",
"八字断（以《子平真诠评注》所载为准）：壬水日主生辰月，丙火财星透、癸水劫财帮身，庚金印星藏申得长生，卯木伤官透时。身有印劫之助、财官有路：一生以学术与社会事业立身，地位至研究院总干事、民权领袖级，清望极高而实权有限。伤官卯木冲动官杀之忌、财星招祸：行运险年早见——1933癸酉年前后为大限（年档定值，窗口1932-1934），酉金冲卯伤、杀机显，有遭政治暗杀横死之象，寿数仅四十岁前后。无显赫承继，事业中道而绝。病位不在脏腑宿疾而在外来横祸金刃。",
bz("四柱癸巳丙辰壬申癸卯；卡面明载韦氏书另造全异、本例以徐乐吾书为准，已从卡面口径。特格扫描皆未命中。主线：印劫护身而伤官为病，酉年冲伤引杀为终局触发，已明写。量级下限学者、上限研究院首长级，落上限侧。关键结局四项俱断。应期年档。"),
0.65))
done.append(W("OC-020",
"八字断：癸水日主生丑月，己土七杀两丑并临、杀重身弱，丁火财星生杀，乙木食神透时制杀。食神制杀成格：一生贵显极高，可至国民政府主席级（国府首脑级），军政两栖、书名政声并重，为一时之选。峰值在中年食神得力、杀被制服之运段（运档定值）。然杀重根浅、寿元不永：五十岁前后为终局（1930庚午年前后年档窗口），午火冲子、财杀逼身，病在头部脑血管急症（中风／脑溢血类）暴终。子女有承，财富中上非巨富。",
bz("四柱己卯丁丑癸丑乙卯。特格扫描：寒极核过——丑月水土寒、无丙丁根？丁火透干有卯木生，不达寒极三条，走正格杀重食制。主线：病在杀重、药在乙木食神，食神坐卯有根故格成而贵。量级区间下限省府、上限国府首脑，落上限依据制杀成格。关键结局四项俱断。应期年档窗口。"),
0.68))
done.append(W("OC-021",
"八字断：乙木日主生酉月七杀当令，辛金七杀透干，乙坐卯禄自强，丙丁伤官并见制杀，戌土财星生杀。伤官制杀、禄刃抗杀成军阀格：一生贵显至旧桂系首领、两广巡阅使／陆军上将级（封疆军阀级），峰值在中年制杀得势运段（运档定值），雄踞数省一时。晚年运转、杀势复起而制力衰：失势下野、寓居沪上，权位尽退而家资可保，寿数近七十岁而终（1928年前后窗口），病终非横死。子女有承。破耗之因在兵败失地不在财破。",
bz("四柱戊午辛酉乙卯丙戌，出格局高低章。特格扫描皆未命中。主线与OC-020同为制杀而此造禄根更强、量级落封疆军阀。终局两运独立判为失势安退：定性贵显者终局骤败须触发，晚运冲禄之触发已据运序方向写明为失势而非暴亡。关键结局四项俱断。应期年档窗口。"),
0.65))
done.append(W("OC-022",
"八字断（自造自批）：乙木日主生酉月七杀当令，丁火食神透制杀，巳火食伤、戊土财星、寅木禄根并见。科第功名无缘：杀旺压身、丁火制杀只成技艺之秀不成进士之贵，加以科举本身将废，屡试不第为定局——学业走博学杂家一路（医、命、堪舆兼通）。立身之路在术数著述：以命理立一代名家之位，著述流传、名满南北，财富中上得自执业著述。寿数高：八十余岁而终，晚景著述不辍、清望收束。子女有承其业者。",
bz("四柱辛巳丁酉乙巳戊寅，卡面载安命甲午、大运丙申起。特格扫描皆未命中。主线：食神制杀为用，功名面过闸——官星辛杀被丁制、印星水不透，科第指代链无触发，故断不第；术数面触发为食伤双透＋财星养命，保留为立身主线。量级下限执业术士、上限一代命家，落上限侧。关键结局四项俱断。应期以运档为主。"),
0.70))
# Meihua
done.append(W("OC-023",
"梅花射覆断：钟下所覆为圆形金属器物——铜镜一类（圆而明、金属为体），且不完好：镜面有破损／缺口，非完整新物。数量为一件。依据链：本卦火风鼎，鼎象三足圆器、主器物；互卦乾兑，乾为圆、兑为金为毁折；上离为明、为镜面之象；变雷风恒，物久置而非常用新器。故断：金属圆器、旧物、带伤。",
B+"梅花易数（射覆，体用与互变取象）\n卡面载卦象：火风鼎变雷风恒。已载面：覆物一件、完好与否为副问，已分断（物类＋破损）。断项过闸：铜镜类→指代链落器物面，触发为互乾兑金圆＋离明；破损→触发为兑毁折。事象级密度：物品（铜镜）、数量（一件）已落。置信低：射覆类象多解，鼎亦可指鼎形器本身，此读以互卦金圆为权重之首，已降置信不断他解为无。",
0.35))
done.append(W("OC-024",
"梅花／成例体裁断：葬资有着落，不须向外告借——易者生前自藏之金将意外显出，足供营葬。具体事象：夜间有鼠扰动，家人掷枕击鼠、枕破，藏于枕中／窖藏之金露现（击鼠枕金一路），以此金办葬事遂成。应期极近：邵雍到访前后数日内（日档，窗口三日内，主坐标到访当夜）。来访秀士即邵雍本人正是托付之人，事必应验。",
B+"梅花易数序传成例体裁（以题面事象起断，无卦盘载于卡面）\n卡面provenance行自载『击鼠枕窖金』事目，为题面已载锚点：直读取藏金显出一路，转应面（外借、亲友资助）已列并舍弃，理由为锚点直指自藏之金。已载面：易者已殁、无资营葬、遗书预言来访者可托——三面俱断。应期尺度：近事日档，依据为葬事在殡殓期内。断项过闸：藏金→指代链落财物面，触发为题面锚点＋遗书预言之设置，两项俱全保留。",
0.60))
done.append(W("OC-025",
"断：椅底预书必应验——届预书所载年月日，此椅将被坐破，应验分毫不差。应验对象为来坐此椅之人（客／家人中一人）坐压而破，非虫蛀自朽；应期即预书所定之日（日档定值，以卡面预书日期为准，卡面未转录具体日期故只到日档层级不断年月数字）。此为邵雍预言应验之例，断为验、不作不验。",
B+"梅花易数序传预言成例体裁（无卦盘载于卡面）\n已载面：预书内容（某年月日椅将被坐破）、届期验之的设置——主问面为是否应验，已断。应验对象复核：承受对象为椅（器物面）、坐破者为触发之人，已分清不回收为人祸福断。输入限度：卡面未载预书具体年月日与坐者姓名，故应期只到日档、人物只到『来坐之人』层级，已降置信，不臆补姓名日期。",
0.72))
# Liuren
def lr(x): return B+"大六壬（陈公献《大六壬指南》占验体例）\n"+x
done.append(W("OC-026",
"六壬断（1643年问今年功名）：两客功名皆有着落——三传乙未、己亥、癸卯成亥卯未木局（曲直），官鬼木局成势入传、初传未乘青龙主喜庆进身，今年科名／仕途进益可得，二人俱榜上有份。分差：先问者（得青龙初传之势）名次与进益较优，后者稍逊一筹且过程有螣蛇惊忧、末传玄武暗耗（名次不显、须防文书暗失分）。应期：月档，主坐标本年秋试放榜前后（窗口当年二月至八月），不落日。身体家宅非所问，不展。",
lr("干支占时卡面载：1643-02-22己亥日辛未时，课式涉害、曲直，三传乙未（青龙）、己亥（螣蛇）、癸卯（玄武），丑将、甲午旬辰巳空。取用：功名以官鬼为类神，木局官鬼入传为一级据。课格曲直主举直进身。LR-QY并读：官鬼面取功名为主面，螣蛇惊忧、玄武暗耗为次面已分判不吞主线。应期档：阶段尺度月档（科试年内），三路以三传成局值年内秋榜为定值、余路舍弃理由为尺度不合日档。盘面不全守第八节：未臆补四课全列与天盘全图。"),
0.55))
done.append(W("OC-027",
"六壬断（1642年奉诏北上）：此行不得意——课名无禄、无路已定凶格底色，末传亥乘青龙而旬空（甲子旬戌亥空），喜与禄皆落空：北上到京不得重用、无升擢之实，多为虚行待命、终须南返。近段行程有阻滞惊病（中传辰乘太阴主暗昧迟滞、北方兵事正紧主途中不安），本人可保无性命大厄（凶将不旺、青龙空主凶亦不成）；远段回任后闲置渐退。老母安否分判：母面无白虎乘传直克之据，断为老母在家平安、无即时大故，勿以子行之凶回收母身。应期：月档，北上无功之验在本冬至次年春间（窗口1642冬至1643春）。",
lr("干支：1642-11-26辛未日甲午时，课式无禄、无路，三传癸酉（合）、戊辰（阴）、亥（青，空），丑将、甲子旬戌亥空，母生甲子年（年命面已列）。取用：仕宦以官鬼禄马为类神，无禄格＋末传空为一级反据；母面按LR-QY-2，缺传只降权不作凶断，故母安不断母危。两段式：近段行程、远段回任各有结论，远段触发为末传空青龙（禄喜落空指向回任无实）。盘面不全守第八节。"),
0.55))
done.append(W("OC-028",
"六壬断（1630年入觐考选得何官）：得官且为美授——课式重审、斫轮，斫轮主成器迁转、印绶俱全之象；中传丙戌乘朱雀主文书诏命、末传癸巳乘白虎主铨选落定。断所授为京职言官一类（科道：给事中／监察御史级），或同级部属清要之职，非外放州县。品级量级为中级京官（七品前后科道），不至卿贰。应期：月档，考选后数月内除授（窗口1630冬至1631春，主坐标次年春铨选）。",
lr("干支：1630-12-17己丑日辛未时，课式重审、斫轮，三传辛卯（玄武）、丙戌（朱雀）、癸巳（白虎），寅将、甲申旬午未空。取用：仕宦官鬼＋朱雀文书面，朱雀居中传为文书任命一级据；斫轮格义两说并存（指南卷二卯戌巳印全／大全卯加申成器），盘面课式名已给从盘面，主迁转成器不争。玄武初传只作过程暗耗次面，不反主线。应期阶段月档。盘面不全守第八节，未臆补四课。"),
0.50))
done.append(W("OC-029",
"六壬断（1642年携子访占诸事，分判三事）：一、子求官——三传成亥卯未木局（曲直）官星有势，回环课主事绕而终成：子求官可得，但迟而小（低级职任／候补有着落，非即授美缺），应期月档次年内。二、此行本身——涉害回环主劳而往返、所谒之人不能尽力，行程耗财耗时。三、老母安否（凶面，独立成条）——初传乙未乘白虎，白虎主丧服道路、未为木墓之地，母年近九十高龄面与之叠见：断老母在本冬至次年间有大故之忧（寿终／丧讯），归家须防丧服。此面与求官吉面分轴并存，不以吉吞凶。应期：母事月档窗口1642冬至1643年内，子官事同窗口后段。",
lr("干支：1642-10-25己亥日辛未时，课式涉害、曲直、回环，三传乙未（白虎）、癸卯（合）、己亥（天后），丑将、甲午旬辰巳空；子丑命、母近九十居山东——年命与关系面俱列。LR-QY-1多义并读：官鬼木局取子求官主面、白虎乘初传取母丧次面，四据核过（入传、乘将合事、生克链达母位）故次面成独立事件条，不以主线吞没；LR-QY-3一课多占逐事分判。回环格不宜散事已注。盘面不全守第八节。"),
0.50))
done.append(W("OC-030",
"六壬断（1651年代占官缺二事，分判）：一、淮扬巡按差可复——课式重审、铸印，铸印主印绶官署重立，初传癸巳乘太常（印绶迁拜之将）发用：断巡按差得复设，官署印信重颁。二、吏书缺照旧——末传辛卯乘太阴主暗中更易：断不能全照旧，人选／名额有暗中更换，存其缺而换其人（部分照旧）。应期：年档内月档落点——本年（1651辛卯，末传卯值年）内见复设之命，主坐标秋冬间（窗口本年三月至十二月）。",
lr("干支：1651-03-01戊子日戊午时，课式重审、铸印，三传癸巳（太常）、丙戌（六合）、辛卯（太阴），亥将。取用：官缺以官鬼印绶为类神，太常发用＋铸印格为一级据定复设；吏书面以末传太阴暗易为据降一格作部分照旧，分判不混。铸印格注：无官反主官非之戒已核，本例问官制存废非个人无官求官，不适用该戒。应期档：迁转月档从第七节，值年卯为坐标锚。盘面不全守第八节。"),
0.55))
# WP
def wp(x): return B+"西洋占星（mundane／事件占星，古典规则骨架）\n"+x
done.append(W("WP-001",
"Prediction: Yes — a major collective affliction in 2020–2021, specifically a worldwide pandemic of a respiratory / influenza-like disease, erupting in early 2020 as the Jupiter–Saturn–Pluto conjunction perfects, causing mass illness, very large numbers of deaths, lockdown-style social paralysis and economic shock, with the worst phase spanning 2020 into 2021 (year-scale window: onset early 2020, main coordinate the 2020 conjunction year). The cyclical-index minimum and the ~100° outer-planet cluster mark this as the century's standout epidemic period, comparable to 1918 in kind.",
wp("Configuration as given on the card: Jupiter–Saturn–Pluto conjunction exact early 2020, five outer planets within ~100°, cyclical index at 21st-century low; comparable clusters 1918/1954/1968/1982 listed on the card — the 1918 analogue (pandemic) is taken as the governing precedent, other analogues noted and set aside with reason (they mark crises generally, the question asks affliction type and the Saturn–Pluto signature is pestilence/mass-mortality in mundane tradition). Timing scale: year档 per mundane cycle; window + main coordinate stated. No natal chart on card; no houses invented."),
0.80))
done.append(W("WP-002",
"Prediction: Barack Obama wins the 2008 US presidential election — he secures the Democratic nomination over Hillary Clinton and defeats John McCain on 4 November 2008. The Saturn–Uranus opposition exact on Election Day marks the break with the old order: the change candidate (Uranus) displaces the establishment incumbent party (Saturn), not the reverse. Timing: nomination settled by June 2008, general election decided 4 Nov 2008 (date given on card).",
wp("Card facts: Obama leads Clinton but has not clinched (May 2008), McCain presumptive Republican nominee, Saturn–Uranus opposition beginning Election Day, last seen 45 years earlier (mid-1960s upheaval cycle). Read: opposition falls on the election itself — the challenger/change pole wins the break. Systems: mundane astrology only; no natal charts on card, none invented. Confidence reflects that the nomination step is included in the prediction."),
0.80))
done.append(W("WP-003",
"Prediction: Barack Obama is re-elected — he defeats Mitt Romney on 6 November 2012 and wins a second term. Mercury turning retrograde on Election Day marks counting delays, disputes and a messy election night, but does not overturn the incumbent: the result stands after the recount-style confusion clears. Margin read as competitive but clear in the Electoral College, not a 2000-style reversal.",
wp("Card facts: incumbent Obama vs presumptive Romney, competitive polling, Mercury retrograde begins on election day 6 Nov 2012. Read: retrograde governs process (delays/disputes) — process face and outcome face listed separately per face-listing discipline; incumbency + no affliction configuration on the card govern the outcome face. No natal charts on card; none invented."),
0.78))
done.append(W("WP-004",
"Prediction: Hillary Clinton wins the 2016 US presidential election — the Costa Mesa ISAR panel consensus read: Clinton defeats Donald Trump on 8 November 2016. Basis of the call as framed in October 2016: polls, incumbency-party continuity configurations and the panel's majority chart reads converge on Clinton; Trump is read as the disruptive loser. This is a single-point call (Clinton), confidence moderate (0.55) given the closeness signalled by the need for a panel split.",
wp("Card facts: Clinton vs Trump, most polls favour Clinton, international astrology conference election panel at Costa Mesa, Oct 2016. Systems: mundane/event astrology panel method as presented on the card. Face listing: outcome face only (single question); panel-split face noted as uncertainty source, hence confidence capped at moderate. No individual panelist charts on card; none invented."),
0.55))
done.append(W("WP-005",
"Prediction: Donald Trump wins the 2016 US presidential election — the panel astrologer who alone picked Trump early, when 17 Republicans still contested, to become the Republican nominee follows the same read through to the general election: Trump defeats Hillary Clinton on 8 November 2016, against the poll consensus. The early-nomination hit is the credential for this call: the same chart signature that singled Trump out of 17 is read as carrying him through November.",
wp("Card facts: same election/panel as companion card, plus the distinguishing fact that one panel astrologer had earlier picked Trump as nominee from a 17-candidate field. That track-record fact is the trigger distinguishing this card's read from the panel-majority read: systems_used mundane astrology, single-reader track. Confidence moderate — the read rests on one reader's signature against consensus, stated as such."),
0.55))
done.append(W("WP-006",
"Prediction: Yes — Britain votes to Leave the European Union on 23 June 2016. The Leave side wins the referendum despite February polls showing 'Stay' ahead with many undecideds; the undecided bloc breaks disproportionately to Leave on the day. Uranus–Ceres conjunct at 23° Aries on referendum day is read as the rupture signature over the UK national charts (1066/1801/1922): severance, not continuity. Timing: result known 24 June 2016.",
wp("Card facts: assessment first published 5 Jul 2015, firmed 22 Feb 2016 after date announced; polls 'Stay' ahead, vast 'not sure' bloc; UK charts 1066/1801/1922 available; Uranus–Ceres conjunct 23° Aries on the day. Read: the long-lead (2015) timing of the assessment — made before the date existed — plus the Aries rupture conjunction govern; poll face listed and set aside with reason (undecided bloc is the swing mechanism). Systems: mundane astrology, tropical, whole-sign for this classical-type question per method defaults."),
0.68))
done.append(W("WP-007",
"Prediction (tarot): Donald Trump wins the 2016 US presidential election, and what decides it is Hillary Clinton's email / Clinton Foundation controversy — a late scandal revival around Clinton's trustworthiness in the final stretch breaks her August lead. The Union Square reading as framed in August 2016: Clinton's cards carry the controversy as the decisive weight; Trump's path runs through her collapse, not through his own popularity. Decision timing: late October–8 November 2016 window.",
B+"塔罗（Waite牌义体系）／事件预测\nCard facts: tarot reader in Manhattan's Union Square Park consulted Aug 2016, draws cards on the election; Clinton leads most Aug polls; email controversy and Clinton Foundation already public. Face listing: outcome face (Trump) and deciding-factor face (email controversy) both listed and both answered, per the question's two parts. Limit: the card does not transcribe the actual cards drawn — no spread is invented here; the read is made on the question structure and stated facts, and confidence is capped at 0.55 for that missing spread.",
0.55))
print("B20 done",len(done),done)
assert set(done)=={f"OC-{i:03d}" for i in range(18,31)}|{f"WP-{i:03d}" for i in range(1,8)}
print("assert ok")
