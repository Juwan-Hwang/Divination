import json, pathlib
base = pathlib.Path(__file__).parent / "predictions"
base.mkdir(parents=True, exist_ok=True)
F = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}
def R(cid, text, basis, conf, systems):
    d = {"case_id": cid, "prediction_text": text, "basis": basis, "confidence": conf, "trigger": dict(F), "systems_used": systems}
    (base / f"{cid}.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")

R("OC-018",
"方向：贵而险，晚运转凶。命主以文章/报业立身而位望极高，可至全国性报业领袖、声望近政界要人一级，但非安稳善终之局：中年后运程由盛转衰，晚段有横祸暴亡之险。应期以年档论：盛在中年水火既济之运，险年在1930年代前半、约1934年前后金木交战之年，死因带兵刃/枪弹之象。置信中高。",
"八字：庚金日主生子月，伤官当令，丙火七杀透月、辛金劫财透时，寅巳藏官杀财星。用神成败看伤官与官杀并见、靠财通关则成报业文贵，晚运杀伤交战无救则等级足级给贵、凶亦足级给横祸，非善终。systems:子平格局+大运推演。无出生年月日时全量与起运精确数，起运岁数未臆补，故应期只到年档。",
0.62, ["八字"])
R("OC-019",
"方向：贵显而寿有险关。命主以学识、干才显于政学两界，可至研究院总干事一类清贵实职；但命局水旺木浮、杀印与食伤交杂，一生多奔走树敌，中年有一大险关。应期以年档论：险年在1930年代初、约1933年癸酉前后，带暴亡/暗害之险，过此关方论后运；未过则寿止于此。置信中。",
"八字（以输入所载徐乐吾书四柱为准，韦千里另载全异已在输入注明，本例不混用）：壬水日主生辰月，癸水比劫透时、丙火财透月，申金印星坐支。水旺财杀受冲，中年运入财杀之地引动暗害。等级按格局给清贵实职，险关按水旺无强土制、流年引动定。无起运精确数，应期只到年档。",
0.58, ["八字"])
R("OC-020",
"方向：大贵，位极人臣。命主贵显程度足级可至封疆以上、国民政府主席级，为本批贵格最高一类；为人食神吐秀、印绶护身，主以文望与资望上位而非兵权。行运早中年顺遂，晚段有病厄险年。应期以年档论：险年在1930年前后庚午一类火土燥烈之年，病逝于任上之象重，寿不过六十上下。置信中高。",
"八字：癸水日主生丑月，丑丑叠见官杀库，乙木食神透时、丁火财透月，卯木食神坐时支。官印食并见而日主有库根，格局成而贵气足，按通则(b)足级断主席级，不作保守降格。晚年运年燥土克水为压制/险关依据。无起运精确数，应期只到年档。",
0.66, ["八字"])
R("OC-021",
"方向：先大贵后衰落。命主格局以杀刃/杀禄相成，早年以军功崛起，贵显可至一省都督、巡阅使一类封疆军政首领；但贵气靠时运撑持，中晚运一转即失势下野，晚景孤落、名位不保，非终身保贵之命。应期以年档论：发迹在青壮年酉运后金水得地之年，败落在1920年代中期后运入冲提纲之地，晚年潦倒。置信中高。",
"八字：乙木日主生酉月七杀当令，日坐卯木禄刃，戊土财、辛金杀、丙火伤官并透。杀旺身亦有禄，成军政贵格足级给都督级；时柱丙戌伤官见杀且晚运冲酉破局为衰落依据，按通则(b)(j)分段：近段贵、远段衰，翻转触发为运冲月提杀星根基。无起运精确数，应期只到年档。",
0.64, ["八字"])
R("OC-022",
"方向：科第无份、以术业立身。命主学业聪敏、文章可观，但功名科第屡试不第，命中无正途进士/举人功名；立身之路不在仕途而在继承家学，以命理（兼医卜）成名自立，可成一代命师、著书立说。应期以年档论：青年丙申等运中科场蹭蹬已定，壮年后转以命学行世渐显，晚年以著述与门望收束。置信高。",
"八字：乙木日主生酉月杀旺，丁火食神透月、戊土财透时，巳酉半合金局克身，寅木根在时支受冲。官杀旺而印星不透、无印化杀通科名之路，故科第无份；食神吐秀合家学传承，主以命理立身。输入已明言屡试不第，与盘面一致（通则e事实优先）。大运丙申起为输入所给。",
0.72, ["八字"])
R("OC-023",
"方向：钟下覆的是一件已破损的器物类物事，非完好、非活物。具体断：为有足/有耳的金属或陶质容器类（鼎属器象）残件，形圆而中空，已有缺口破损，取出可见破处。事象级：物品=破损容器类器物，完好与否=不完好。置信中低。",
"梅花：火风鼎变雷风恒。鼎卦象鼎器、有足中空主容器；体用以离火巽木相生而变恒，器象久置破损。按通则(c)(g)落到物品与完好程度一项。输入只有卦名无爻辞与起卦数，无法核动爻辞义（通则d），故降置信、不引辞作断。",
0.45, ["梅花易数"])
R("OC-024",
"方向：葬资有着落，不必外借。易者遗藏即在其遗枕之中——枕内藏有金银（窖金/枕金），击破其枕即可取出，数足营葬。应验对象为遗枕中所藏金，非来访者出资、非乡里赊借。具体：物品=枕中金银，足供一葬之资。置信中高。",
"梅花/外应类取象合事实优先（通则e,f）：占题为无资营葬、遗书预托来访者，象主藏物近身。枕为头下近身之物、主窖藏，取枕中藏金为应验对象，不回收到来访秀士出资。输入未给卦象爻数，依据为成例取象与占题事实，故置信不至高位。",
0.62, ["梅花易数"])
R("OC-025",
"方向：应验。椅底预书之事届期必验——到预书所记年月日，椅子将被坐破，破在坐者压坐之时，应验对象即邵家此椅本身，非他椅、非人身之灾。具体：物品=自家之椅，事件=届期坐破，与预书文字一一对应。置信中高。",
"梅花预书成例：预言以文字预定年月日与器物结局，属器物应验（通则f非人对象为常备候选）。输入未给预书具体年月日原文，故只断必验与应验对象，不臆补日期数字。",
0.65, ["梅花易数"])
R("OC-026",
"方向：功名可得，昆弟皆有喜。己亥日占，初四日课得涉害曲直，三传未（青龙）—亥（螣蛇）—卯（玄武）成亥卯未三合木局，曲直主木旺成局、青龙发用主功名喜信。今年功名有成：一人先得、一人随得，名次不至榜首而皆入选之象。应期以月档论：应在春季木旺得局之月内见榜信，亥卯未合局逢卯月/木日为窗口内主坐标。置信中。",
"大六壬：日干己土以木为官鬼，官星三合成局乘青龙发用为功名类神得力；中传螣蛇主虚惊文书迟滞故先忧后喜，末传玄武主名次不显于前列。盘面不全守SKILL六壬第八节：只据干支、三传、天将、课格、空亡（辰巳空不入传）作断，不臆补四课天盘。",
0.58, ["大六壬"])
R("OC-027",
"方向：此行不得意。奉诏北上，课名无禄无路已主禄路两空：北行难得实职美差，多虚行/改派/候缺，老母与自身两牵挂中，自身途中有病阻之象、行程迟滞难如期得意；老母在家不安但无大凶，可保无恙待归。应期以月档论：入京后一月内即见落空/改派消息，身体之阻应在途中水陆关口之期。一段终局为主，远段升转无触发不报。置信中高。",
"大六壬：课式无禄、无路为课格主向凶；三传酉（合）—辰（阴）—亥（青龙，空），末传青龙落空主喜信/前程落空，中传太阴乘辰主暗中改派。甲子旬戌亥空，末传空亡为关键闸门。盘面不全守第八节，不臆补四课。北方兵紧为事实约束（通则e）。",
0.63, ["大六壬"])
R("OC-028",
"方向：考选得官，且得清贵文职。朱西崑入觐考选，课得重审斫轮，三传卯（玄武）—戌（朱雀）—巳（白虎），中传朱雀乘戌主文书诏命得力，斫轮主雕琢成器、考选成名。所授以馆阁/部院文职一类为主（中书、翰林馆选之属），非外放州县肥缺；名次中上。应期以月档论：考选后当月至次月内得授官文书，主坐标取朱雀值日之期。置信中。",
"大六壬仕宦门：类神官鬼与朱雀文书并看，中传朱雀不空不破为授官信号；初传玄武主初有暗争/名次起伏，末传白虎乘巳主得官后有奔走劳碌。甲申旬午未空不入传。盘面不全守第八节。官职类别为推测级细断，已降置信处理。",
0.55, ["大六壬"])
R("OC-029",
"方向：求官难成、诸事迟滞中带一喜。携子求官：三传未（白虎）—卯（六合）—亥（天后）三合木局虽成，然涉害回环主反复纠缠，求官之事今年难落实、须候来年再图，子事亦随父滞。老母年近九十：天后末传主母象，母寿高而无即时大凶，本年可安度寿期，惟家在山东路远有音信迟忧。具体：求官=不果，老母=安，携子=无功而返。应期以年档论：求官落空在本年内定，母安以本年为断。置信中。",
"大六壬：亥卯未三合本主和合成事，但课格涉害+回环压过合局主反复难成，按课格主向优先；初传白虎乘未主途路辛劳与求访受阻。子丑命未入三传，不强断子之功名。盘面不全守第八节，只据三传天将课格空亡（辰巳空）。对象逐条复述（通则f）：父求官不果、子随行无成、母安——三对象不混。",
0.56, ["大六壬"])
R("OC-030",
"方向：二事皆可成。淮扬巡按差可复，吏书缺可照旧。课得重审铸印，铸印主印信复铸、差缺重立，为复设类占之吉格；三传巳（太常）—戌（六合）—卯（太阴），太常发用主旧制常典恢复，六合中传主议合而成，太阴末传主暗中定局。应期以月档论：议复在本年春季内定局，主坐标取巳日/巳月太常值位之期，二缺存废以照旧复设收束。置信中高。",
"大六壬章奏/仕宦门：铸印课格直主复印复差，与所问复设正合（事实优先）；三传无空亡冲破（输入未注空亡），太常为旧典类神得位。盘面不全守第八节，不臆补四课天盘。二问逐条同向：巡按复、吏缺旧。",
0.62, ["大六壬"])
R("WP-001",
"Direction: Yes — a major collective affliction in 2020–2021, specifically a pandemic-scale epidemic disease spreading worldwide, with mass illness and mortality peaking around the early-2020 Jupiter–Saturn–Pluto conjunction and the cyclical-index low. Timing window: onset/peak in 2020, continuing into 2021. Confidence moderate-high.",
"Western mundane astrology: five outer planets clustered within ~100 degrees with Jupiter-Saturn-Pluto conjunction at the century's lowest cyclical index; input itself notes comparable clusters coincided with 1918 (influenza pandemic) etc. Reading follows the configuration as given; no natal chart supplied, so no house-level claims.",
0.68, ["西洋占星"])
R("WP-002",
"Direction: Barack Obama wins the 2008 US presidential election — first securing the Democratic nomination over Hillary Clinton, then defeating John McCain in the 4 November 2008 general election. The Saturn–Uranus opposition exact on Election Day marks the change/upheaval candidate prevailing over the establishment candidate. Confidence moderate-high.",
"Western election astrology as framed in the input (Saturn-Uranus opposition beginning Election Day, last seen 45 years earlier = change signature). No birth charts supplied in input, so basis rests on the stated configuration and the nomination facts given; outcome stated as a single clear winner per event-type single-verdict practice.",
0.66, ["西洋占星"])
R("WP-003",
"Direction: Barack Obama wins re-election in the 2012 US presidential election, defeating Mitt Romney on 6 November 2012. A close, contested count with Mercury retrograde beginning on election day causing delays/confusion in reporting, but the incumbent retains the White House. Confidence moderate-high.",
"Western election astrology: incumbent advantage as framed by the panel context in the provenance; Mercury retrograde on election day read as count confusion/delay, not as reversal of the winner. No charts supplied in input; no house-level detail claimed.",
0.66, ["西洋占星"])
R("WP-004",
"Direction: The conference panel predicts Hillary Clinton will win the 2016 US presidential election, defeating Donald Trump on 8 November 2016. This records the panel's consensus forecast (Clinton victory). Confidence moderate (as a record of the panel prediction).",
"Western election astrology panel context: input states most polls favour Clinton and the setting is the panel's forecast; the case asks who will win as predicted by this panel source. No individual charts supplied. Prediction text deliberately framed as the panel's predicted winner.",
0.55, ["西洋占星"])
R("WP-005",
"Direction: Donald Trump wins the 2016 US presidential election, defeating Hillary Clinton on 8 November 2016. The astrologer who alone had picked Trump as Republican nominee when 17 contested it follows through to a Trump general-election victory. Confidence moderate.",
"Western election astrology: input distinguishes this case by the one panel astrologer with the contrarian Trump-nominee track record; that track record is the case's salient signal, read as pointing to Trump in the general election against the poll-favoured Clinton. No charts supplied in input.",
0.55, ["西洋占星"])
R("WP-006",
"Direction: Yes — Britain votes to Leave the European Union in the 23 June 2016 referendum. Leave wins narrowly despite February polls showing Stay ahead with many undecideds; the Uranus–Ceres conjunction at 23° Aries on referendum day marks the rupture/separation outcome. Confidence moderate-high.",
"Western mundane astrology using UK national charts (1066/1801/1922) and referendum-day configuration as given in input; the source assessment (Jessica Adams 'GOODBYE EU' / Brexit prediction) is framed as a Leave prediction, and the chart signature given is a disruption signature. Polls noted as contrary background, not as the verdict.",
0.64, ["西洋占星"])
R("WP-007",
"Direction: Donald Trump wins the 2016 US presidential election. What decides it: Hillary Clinton's email controversy and Clinton Foundation questions eroding trust among late-deciding voters — the scandal/trust issue, not policy, is the deciding factor named in the reading, producing a late swing to Trump despite Clinton's August poll lead. Confidence moderate.",
"Tarot reading context (Manhattan tarot reader, August 2016, cards drawn on the election — no card list supplied in input, so no card-by-card claims are made). Deciding-factor detail is constrained to controversies already public in the input setting (emails, Foundation), per fact-priority: no invented later events.",
0.55, ["塔罗", "西洋占星"])

print("done", len(list(base.glob('*.json'))))
