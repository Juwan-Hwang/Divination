# -*- coding: utf-8 -*-
"""R96 B20 blind predictions generator. Non-liuyao batch (no card carries a tradition field)."""
import json, os

OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round96/predictions"
os.makedirs(OUT, exist_ok=True)

TF = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}

P = {}

P["OC-018"] = dict(
    conf=0.55,
    pred="地位：命主可成社会名流级巨头——报业/实业界领袖的地位（非庙堂官贵，而是行业巨擘）。晚年行运不吉：晚运入火旺之运，七杀攻身、冲月令，1934甲戌年前后有暴亡横祸之险，晚景凶终、不得善终。应期为年档，主坐标1934年。",
    basis=(
        "tradition：卡面未设 tradition/system 字段（仅 id/subject/context/provenance/language 五键），据四柱命造题面体裁自决用子平法。\n"
        "systems_used: 八字（子平真诠用神成败救应口径）\n"
        "指示链：庚金日主生子月，水冷金寒；月干丙火七杀透出得时支巳中丙根，为调候兼杀之用；年时辛巳、辛金劫财帮身，巳藏戊印。杀有帮扶制衡则成名位，故地位可至行业巨头。行运逆行乙亥、甲戌、癸酉、壬申、辛未、庚午：金水运帮身任杀为发迹段；庚午运午火杀旺冲月令子水、身无根受攻，甲戌年戌助火势，为暴亡险点。应验对象为命主本人，逐项对回题面（报业巨头身份与杀用成名相应）。\n"
        "第八节功量核 — 功量清单：助成线①丙火七杀透干得巳根（作用源丙/巳，对象为命主名位，向助成，状态得根不虚）；助成线②辛金劫财帮身（对象日主，向助成，状态透干）；压制线①子水伤官当令泄金寒金（对象日主，向压制，状态当令最旺）；压制线②日坐寅为庚金绝地（对象日主根基，向压制）。合计助成2、压制2，身杀相持，等级带定为行业巨头级而非庙堂极品（无印化杀、身根薄，压制依据在此）。\n"
        "主线认定：丙火七杀调候线为做功主线（直接作用于名位、透干得根居首），晚段午运此线过旺转攻身，故晚年量级由成转凶。"
    ))

P["OC-019"] = dict(
    conf=0.55,
    pred="行运：早中年金印之运主学术地位上升，可至研究院总干事级学术机构首脑。险年明确在酉运酉年：1933癸酉年，酉冲时支卯、运年酉并临，有横祸暴亡之险（防暗害急祸），为一生最大险关；此前申酉运是上升段而非险段，险在运末值年冲提。应期为年档，主坐标1933年。",
    basis=(
        "tradition：卡面没有 tradition 字段，仅见 subject/context/provenance，据命造评注引例体裁自决用子平法；卡面 note 明载两书四柱全异、本例以卡面所载（徐乐吾书）为准，此歧异已在置信中下调反映。\n"
        "systems_used: 八字（子平真诠用神成败救应口径）\n"
        "指示链：壬水日主生辰月，辰为水库湿土；丙火偏财透月干，癸水劫财两透帮身，年支巳、月支辰藏戊杀而身有申金印源，身旺有依。顺行大运丁巳、戊午、己未、庚申、辛酉：庚申辛酉金印生身，主学术名位上升至机构首脑。险点：辛酉运逢癸酉流年，酉金冲时支卯木（伤官、亦为身后门户之支），运年并临冲提，卯木被拔，主急祸暴亡。应验对象为命主本人。\n"
        "第八节功量核 — 功量清单：助成线①申金正印坐日支生身（对象日主/名位，向助成，状态得位）；助成线②癸水劫财两透帮身（向助成）；助成线③丙火财星透干主社会活动之资（向助成，状态有巳根）；压制线①辰土湿杀藏而不透（向压制，状态伏藏力弱）；压制线②酉运年冲卯（对象时支卯木，向压制，状态运年并临最烈，只作用于险年一点）。合计常态助成3、压制弱，故地位带定为学术机构首脑级；险年压制线独强，只压寿元一点、不改地位带。\n"
        "主线认定：申金印星生身线为做功主线（得位生身、贯穿中年运程），名位量级随之定带；酉冲卯为险年触发线，非主线。"
    ))

P["OC-020"] = dict(
    conf=0.55,
    pred="贵显程度：食神制杀成格，贵至极品——国家元首/政府主席级。行运：中年运扶食神制杀，贵显持续；险年在运末值午年：1930庚午年，午破卯、害丑，制杀之食神根动，有病亡之险，主坐标1930年（年档）；终局以病终为主，非横祸暴亡。",
    basis=(
        "tradition：卡面未标注 tradition/system，据四柱与『贵显程度』之问自决用子平格局法。\n"
        "systems_used: 八字（子平真诠格局成败口径）\n"
        "指示链：癸水日主生丑月，丑藏己土七杀当令，两丑杀重；时干乙木食神透出正制己杀，月干丁火偏财滋食神之源，卯木食神两见有根——食神制杀成格，杀被制净则贵气纯，故贵至元首级。逆行大运丙子、乙亥、甲戌、癸酉、壬申：水木运扶身扶食，贵显绵长。险点：壬申运末逢庚午年，午火财星破卯木食神根、午丑相害动杀库，格局根脚被动，主病亡。应验对象为命主本人，对回题面『政府主席级政要』身份相合。\n"
        "第八节功量核 — 功量清单：助成线①乙木食神透时干制丑中己杀（对象格局/贵位，向助成，状态透干有卯根，最强）；助成线②丁火财星生食神（向助成）；助成线③两卯为食神之根（向助成，状态双根）；压制线①两丑杀重伏藏（向压制，状态被乙木制住）；压制线②癸水身弱无印透（向压制，状态弱）。助成3线且主线制杀干净、无主线让位，依估低防线等级带取上位：元首级。\n"
        "主线认定：乙木食神制杀线为做功主线（直接作用于当令七杀、透干双根居首），贵显量级由其定带。"
    ))

P["OC-021"] = dict(
    conf=0.5,
    pred="格局中上：杀格用伤官制杀，可贵显至封疆大吏（督军/巡阅使级）。但日支卯禄冲月令酉杀、丙辛合而制杀打折，根基不固：中年火运发贵至顶，其后运退则失势落魄，晚景孤贫、终局不显。应期为年档：发贵主段在寅卯火木之运，败落在火运过后。",
    basis=(
        "tradition：卡面无 tradition 字段，据命造问格局高低体裁自决用子平法。\n"
        "systems_used: 八字（子平真诠格局高低口径）\n"
        "指示链：乙木日主生酉月，辛金七杀透年干当令，杀旺；乙坐卯禄、日有强根可任杀；时干丙火伤官透出制辛杀，时支戌藏丁火食神、戊土财。制杀有力故能贵显至封疆。病在两处：卯酉冲，禄根被月令杀冲动，根基不稳；丙辛相合，伤官被杀合绊，制杀之力打折——故贵而不久、成而易败。顺行运壬戌、癸亥、甲子、乙丑、丙寅、丁卯：丙寅丁卯火木运制杀扶身为发贵主段，运退水土则杀无制、禄被冲，失势落魄。应验对象为命主本人。\n"
        "第八节功量核 — 功量清单：助成线①丙火伤官透时干制辛杀（对象贵位，向助成，状态透干但被辛合绊，力打七折）；助成线②乙坐卯禄有根任杀（向助成，状态根被酉冲）；压制线①辛酉杀当令旺透（向压制，状态最旺）；压制线②卯酉冲动禄根（向压制）。助成与压制俱强，等级带定为封疆级而非极品，且带内取『贵而难久』一侧，压制依据即冲禄与合绊两行。\n"
        "主线认定：丙火伤官制杀线为做功主线（直接作用于当令之杀），然其受合绊、禄根受冲，主线让位依据成立（合绊＋冲根可指认），故量级按带内偏低且主晚景衰落。"
    ))

P["OC-022"] = dict(
    conf=0.55,
    pred="科第无缘：印星全然不现，功名之凭缺位，屡试不第之命，仕途立身不成。立身之路在技艺著述：食神透干制杀、食神生财，当舍官从艺，以术数/著述立身成名，名重一时、财自技艺来。中年木火之运（乙未、甲午）食神得地，为立业成名主段；晚运尚平稳。应期为年档。",
    basis=(
        "tradition：卡面未载 tradition 字段，据自造自批命造体裁自决用子平法。\n"
        "systems_used: 八字（子平）\n"
        "指示链：乙木日主生酉月，年干辛金七杀透、酉金当令杀旺；月干丁火食神透出制杀，时支寅木为乙之根，时干戊土正财承食神之生。全造不见水印——科第功名以印为凭、官印相生之路断绝，故屡试不第（对回题面『屡试功名不第』）。出路在丁火食神：制杀、吐秀、生财，主以技艺口才著述营生立名。卡面注『安命甲午；大运丙申起』，逆行丙申、乙未、甲午、癸巳、壬辰：乙未甲午木火运食神得地吐秀，为成名立业主段。应验对象为命主本人（命师自造）。\n"
        "第八节功量核 — 功量清单：助成线①丁火食神透干制辛杀且生戊财（对象立身之业，向助成，状态透干居首）；助成线②寅木日根扶身任食神之泄（向助成）；压制线①辛酉杀旺当令（向压制，状态被丁制）；压制线②印星全缺（对象功名一途，向压制，状态全造无水、缺位即绝）。分配对读：功名一途受力为零（印线缺位），技艺一途得食神主线全功——故断舍官从艺、量级带为『以技成名、名重一时』而非仕宦等级。\n"
        "主线认定：丁火食神吐秀生财线为做功主线（透干、作用于杀与财两端），立身量级由其定带；功名线因印缺不成立，不与主线争位。"
    ))

P["OC-023"] = dict(
    conf=0.3,
    pred="钟下所覆为一件金属制、中空有孔的环形器物（金银环/镯一类），且已残损、不完好。完好与否断为已损。射覆即时之占，当场启钟即验，无应期窗口。",
    basis=(
        "tradition：卡面未设 tradition 字段，据席间射覆、以卦推物之题面体裁自决用梅花易数观物法。\n"
        "systems_used: 梅花易数（观物/射覆取象）\n"
        "指示链：得火风鼎变雷风恒。鼎卦本身即象三足两耳、中空容物之金属铸器，射覆以卦名直象为先，定物为金属器物一类；上离为中空、有孔、附壳之象，定其形中空有孔（环/镯之属）；离火主分、主损，变卦下巽风入而不固，合断已残损不完好。输入残损：卡面只载本卦与变卦、未载动爻，体用分判无从确指，此点已在 basis 注明并下调置信，不臆补动爻。应验对象即钟下之物本身（非人对象，不回收到占者身上）。\n"
        "第八节功量核 — 功量清单：助成线（主物全）①巽木在下卦未克金器之象（向助成，状态弱）；压制线①离火居上卦主破损分离（对象该器物，向压制，状态当卦主位）；压制线②鼎象三足而卦变恒、足象不稳（向压制，状态象义级）。压制居主位，完好程度定带为『已损』一侧。\n"
        "主线认定：离火破损线为做功主线（居上卦主位、直接作用于器物完好与否），故断残损；器物类别由鼎卦直象定，不归功量核辖域。"
    ))

P["OC-024"] = dict(
    conf=0.6,
    pred="葬资有着落：亡者生前于卧榻枕下/床下窖藏有金银，掘之可得，数量足敷营葬且有余——于其床枕之下掘地寻之，金银以罐瓮盛藏。应期即时：当日掘验即见。",
    basis=(
        "tradition：卡面无 tradition 字段，据《梅花易数》序载邵雍断验故事体裁自决用梅花观物/外应法。\n"
        "systems_used: 梅花易数（观物外应、遗书预言类）\n"
        "指示链：题面三事相扣——易者遗书预言来访秀士可托身后事、其家苦无葬资、篇题『击鼠枕窖金』自含枕、窖、金三象（题面给定事实优先于类象发挥）。鼠为窖藏之患、枕为卧处之凭：断亡者有窖藏金银在其枕下/床下之地，掘之得金解葬资之急。事件级落点：物品＝窖藏金银（罐瓮盛装），处所＝亡者卧床枕下地面，承受与应验对象同为亡者之家与该笔葬资。无卦面数据载于卡面，不另造卦。\n"
        "第八节功量核 — 功量清单：助成线①遗书预言与来访者身份对位（作用源题面事实，对象葬资一事，向助成，状态事实级）；助成线②篇题『窖金』直象（向助成，状态题面明载）；压制线：无可指认压制线（其家贫穷为现状事实、非盘面压制线，不入清单计权）。助成2线、压制0线且无主线让位，依估低防线量级不得低于带中位：定带为『足敷营葬且有余』，不作仅够支应之低估。\n"
        "主线认定：窖金直象线为做功主线（篇题明载、直接作用于葬资有无），量级由其定带。"
    ))

P["OC-025"] = dict(
    conf=0.5,
    pred="应验：届预书所定年月日，恰有来客坐此椅，椅被坐破（椅足/椅身当场折断），预言如期而验。应期为日档，主坐标即预书所书之当日，应在客来坐时。",
    basis=(
        "tradition：卡面未标注 tradition，据邵雍预书验事之题面体裁自决用梅花预言/观物法。\n"
        "systems_used: 梅花易数（预书验事类）\n"
        "指示链：题面事实：邵雍预先书于椅底、明定年月日椅将被坐破，问届期是否应验。此类预书断验以『期至事发、物应人至』为式：椅为日常坐具、应期一到必有客至而坐，坐破之应落在椅子本身（非人对象，承受与应验同为该椅）。事件级落点：人物＝来访之客一人，物品＝该椅，应期数字＝预书所定年月日当日。卡面未载预书原文日期，不臆造具体日期，只断当日应验。\n"
        "第八节功量核 — 功量清单：助成线①预书明定年月日（作用源题面事实，对象坐破一事，向助成，状态日期锁定）；助成线②椅为日用坐具、届期客至必坐（向助成，状态常理级事实）；压制线：无可指认压制线。助成2、压制0，无让位依据，量级带取『如期坐破、分毫不爽』全验一侧，不作含糊验否。\n"
        "主线认定：预书定日线为做功主线（直接锁定应期与应事），应验量级由其定带。"
    ))

P["OC-026"] = dict(
    conf=0.4,
    pred="今年功名可成而有分别：兄弟二人中一人得中（榜上有名、功名到手），另一人本次落榜。过程有虚惊牵缠，名额之喜只落一人。应期为月档，主坐标在本年放榜之期。",
    basis=(
        "tradition：卡面没有 tradition 字段，据课式、三传、月将齐备之题面体裁自决用大六壬法。\n"
        "systems_used: 大六壬（指南课例口径；盘面不全守只据干支三传天将课格空亡作断）\n"
        "指示链：己亥日辛未时，丑将，甲午旬辰巳空。课涉害、曲直。三传乙未（青龙）→己亥（螣蛇）→癸卯（玄武），亥卯未三合木局成曲直格；木为己土之官星，功名类神（官星）三合成局且旺，主功名有份。初传未即日干己之寄宫、乘青龙主发端之喜；中传亥乘螣蛇主过程虚惊牵缠；末传卯乘玄武主收尾暗昧、一名落空。故断一中一落：官局之功只够一人成名。输入残损：两客年命均未载，何人得中无从确指，已注明并降置信。应验对象为两客昆弟，逐名对回所问『今年功名』。\n"
        "第八节功量核 — 功量清单：助成线①三传三合木局官星成局（作用源亥卯未，对象功名，向助成，状态成局最强）；助成线②初传青龙乘干寄宫主喜（向助成）；压制线①末传玄武主一名暗昧落空（向压制，状态居末传收尾）；压制线②中传螣蛇主虚惊迟滞（向压制，状态居中传）。分配对读：二人同占、功量只足一席——官局助成归一人，玄武落空归另一人，分配方向与逐方受力同向（得中者受官局之功，落榜者受玄武之压）。等级带定为『一人得中』而非双双得意，压制依据即玄武末传一行。\n"
        "主线认定：三合木局官星线为做功主线（成局、直接作用于功名对象），其功量只足一席，故主线认定：一人得中。"
    ))

P["OC-027"] = dict(
    conf=0.42,
    pred="此行不得意：诏命虽至而实惠落空，北上终成虚行——难得实职遂意，行役多阻，防中途滞留或空回。身体劳顿有惊而无大病，身可保全。老母在家安平无恙。应期为月档：滞阻见于行后数月之内。",
    basis=(
        "tradition：卡面未设 tradition 字段，据六壬课式三传体裁自决用大六壬法。\n"
        "systems_used: 大六壬（指南课例口径；盘面不全守约作断）\n"
        "指示链：辛未日甲午时，丑将，甲子旬戌亥空。课名无禄、无路——课格主向即禄路俱无、此行无实利。三传癸酉（六合）→戊辰（太阴）→亥（青龙，空亡）：初传酉为辛金之禄乘六合，主始有和合招徕之象；中传辰乘太阴主暗中迟滞；末传亥乘青龙却落空亡，青龙主喜庆财禄，落空则喜与禄皆空——终局落空，正合无禄无路。分项对回所问三事：行不得意（末传空）；身无大病（日干辛金禄在初传未受凶将克破，只主劳顿）；老母安（题面载母生甲子年，课中无凶将克母位之象，断安平——此项依据较薄，置信已含之）。北方兵事为题面事实，主行役之阻，不作盘外臆断。\n"
        "第八节功量核 — 功量清单：助成线①初传酉禄乘六合（对象此行所得，向助成，状态居初传、只主始象）；压制线①课格无禄无路（对象全程，向压制，状态课名定格）；压制线②末传青龙空亡（对象终局所得，向压制，状态空亡最烈、居末传定局）。压制2线且居定局之位，助成仅始象，等级带定为『不得意、所得近无』一侧；以次线（初传禄）定量与主线相反者，主线让位依据不存在（禄不空而终局之青龙空），故不取始象之喜。\n"
        "主线认定：末传青龙落空线为做功主线（居末传定终局、空亡状态居首），此行量级由其定带为落空。"
    ))

P["OC-028"] = dict(
    conf=0.35,
    pred="考选可得官：得实缺，但非清贵文职——乃外任中下品级、带兵马道路之任（武职/兵备/驿传一类），赴任方向偏南（巳午之方）。品级量级约中下，五至七品带。应期为月档：考选后当年内放缺见分晓。",
    basis=(
        "tradition：卡面无 tradition 字段，据六壬课式三传体裁自决用大六壬法。\n"
        "systems_used: 大六壬（指南课例口径；盘面不全守约作断）\n"
        "指示链：己丑日辛未时，寅将，甲申旬午未空。课重审、斫轮。三传辛卯（玄武）→丙戌（朱雀）→癸巳（白虎）。仕宦考选类神取官星与朱雀文书：初传卯木为己土之官星发用，主官事发动，然乘玄武，主其官带暗昧不正之色、非清要之途；中传戌乘朱雀，文书考选之象动，主考选过关、凭文书得缺；末传巳乘白虎，白虎主兵马道路威刑，定其官职性质偏武、偏道路奔波，巳又主南方。斫轮课主改作就职。三者合成：得官而品级中下、职属外任武路。应验对象为占者本人所问之官缺。\n"
        "第八节功量核 — 功量清单：助成线①中传朱雀文书发动主考选过关（对象官缺，向助成，状态居中传）；助成线②初传官星卯木发用（向助成，状态发用但乘玄武打折）；压制线①官星乘玄武主非清贵（向压制，状态乘将定性）；压制线②末传白虎主其任劳险而非显要（向压制，状态居末传）。助成压制相持，品级带定为中下（五至七品带），不取高品，压制依据为玄武乘官一行。\n"
        "主线认定：朱雀文书线为做功主线（考选之事以文书过关为枢、居中传发动），得官方向由其定；品级量级受玄武压制线封顶。"
    ))

P["OC-029"] = dict(
    conf=0.4,
    pred="分项断：①求官可成而迟——官星成局、有人和合相助，但先阻后遂、须经奔波，成期偏迟。②其子随行平安，本次官缘助力薄于其父，难同得显缺。③老母有大病寿厄之险：近年内（主坐标本年冬至次年，年档）防病重不起，寿事须预备。应期：求官以月档论迟成，母厄以年档论。",
    basis=(
        "tradition：卡面未标注 tradition，据六壬课式三传与多事并占体裁自决用大六壬法。\n"
        "systems_used: 大六壬（指南课例口径；盘面不全守约作断）\n"
        "指示链：己亥日辛未时，丑将，甲午旬辰巳空。课涉害、曲直、回环。三传乙未（白虎）→癸卯（六合）→己亥（天后），亥卯未三合木局，木为己土官星成局，求官类神有力；中传卯乘六合主贵人和合相助，故求官可成；然初传未乘白虎发用，主发端先见阻与病丧之象，成事迟滞。其子丑命：丑为金库，不入木局之功，助力薄。末传亥即日支乘天后，回环主归返平安。老母一事单核：白虎为丧病之将，发用临未（未为坤母之象、又日干寄宫），母年近九十高龄（题面事实），白虎发用主病厄临门，断寿厄之险。逐项承受对象与应验对象逐名对回：求官应占者本人、子事应其子、母厄应其母，不相回收。\n"
        "第八节功量核 — 功量清单：助成线①三合木局官星成局（对象求官，向助成，状态成局）；助成线②中传六合主和合得助（向助成）；压制线①初传白虎乘未（对象母体兼求官发端，向压制，状态发用最先、乘将最凶）；压制线②涉害课主彼此相害迟滞（向压制）。分配对读：求官一途助成2线胜压制之迟滞，得『成而迟』；老母一途只有白虎压制一线独作用、无助成线对冲，量级定带为『大病寿厄』重侧，不作轻估。\n"
        "主线认定：分途认定——求官主线为三合官局线；母厄主线为白虎乘未线（发用、直接作用于母象），两线分辖两事，不相抵扣。"
    ))

P["OC-030"] = dict(
    conf=0.45,
    pred="二事一复一变：①淮扬巡按差可复——复设可成，将有实授。②吏书缺难全照旧——其缺暗中改易，或裁并、或改属他人，不能原样保全。应期为月档：复设分晓主坐标在戌月前后（中传戌逢值之月）。",
    basis=(
        "tradition：卡面无 tradition 字段，据六壬课式三传与代占官缺体裁自决用大六壬法。\n"
        "systems_used: 大六壬（指南课例口径；盘面不全守约作断）\n"
        "指示链：戊子日戊午时，亥将。课重审、铸印。三传癸巳（太常）→丙戌（六合）→辛卯（太阴）。铸印课主官印铸成、官署复立，正应『差可复否』之问；初传巳乘太常，太常为官禄衣食之将，巳藏丙戊为戊土之印，印与禄俱发于初传，复设之象最切。中传戌乘六合主和合成事、众议可合。末传卯为戊土正官乘太阴，太阴主暗昧阴私——落到吏书小缺一事，主其缺在暗中改易、不照旧保全。两事分读：大差归铸印与太常，小缺归太阴末传。应验对象分别为巡按差与吏书缺本身（官署/职缺为非人对象，逐项对回）。\n"
        "第八节功量核 — 功量清单：助成线①铸印课格主官印成（对象巡按差，向助成，状态课名定格）；助成线②初传太常乘巳印禄双发（向助成，状态发用）；助成线③中传六合主和合成事（向助成）；压制线①末传太阴乘卯主小缺暗易（对象吏书缺，向压制，状态居末传定其终局）。分配对读：巡按差受助成3线、无压制，定『可复』足级；吏书缺只受太阴压制一线、无助成对冲，定『难照旧』。两方分配方向与逐方受力同向。\n"
        "主线认定：铸印兼太常发用为做功主线（直接作用于官署复立、课格与发用双重居首），巡按差量级由其定带为可复实授。"
    ))

P["WP-001"] = dict(
    conf=0.68,
    pred="有重大集体疾疫：2020–2021年将有一场全球性大流行病（瘟疫型/呼吸道传染病），以2020年初木星—土星—冥王星合相为爆发点，死亡与波及规模为本世纪罕见，可比拟既往集群期（如1918年）之烈度。时间窗：2020年初起，绵延至2021年。",
    basis=(
        "tradition: The card carries no tradition/system field (keys: id/subject/context/provenance/language only); decided by genre — a mundane-astrology assessment — as western mundane astrology.\n"
        "systems_used: western astrology (mundane; outer-planet cycles and cyclical index)\n"
        "Indicator chain: The setting itself supplies the configuration — five outer planets gathered within ~100 degrees around 2020, an exact Jupiter–Saturn–Pluto conjunction in early 2020, and the cyclical index at its 21st-century low; the card notes comparable past clusters coincided with 1918, 1954, 1968 and 1982, of which 1918 and 1968 were pandemic years. Pluto rules mass death and pestilence, Saturn–Pluto conjunctions mark collective hardship and mortality crises; a cyclical-index trough concentrates the malefic weight into 2020–2021. The affliction's object is the world population (collective), matching the question's object. Timing is year-scale by the question's own scale: outbreak point early 2020, duration through 2021.\n"
        "第八节功量核 — 功量清单：助成线（主大疫成局）①Jupiter–Saturn–Pluto exact conjunction early 2020 (source: the given configuration; object: collective health; direction: affliction-forming; state: exact, strongest); 助成线②five outer planets within ~100° concentrating the cycle (direction: affliction-forming; state: given in setting); 助成线③cyclical index at 21st-century low (direction: affliction-forming; state: extreme value); 压制线：none identifiable in the given material (the mild 2009 H1N1 precedent is a background fact, not a chart factor, and is not counted). With 3 affliction-forming lines and no counterweight, the severity band is set at the top: a pandemic of historic scale, not a mild seasonal event — per the no-downgrade-without-suppression rule.\n"
        "主线认定：The Jupiter–Saturn–Pluto conjunction line is the working main line (exact, directly on the collective-affliction object, state ranked first); severity is banded by it."
    ))

P["WP-002"] = dict(
    conf=0.55,
    pred="奥巴马胜：奥巴马先夺民主党提名，继而在2008年11月4日大选中击败麦凯恩，当选美国总统。土星—天王星对冲于选举日成相，主变革压倒守成、老将不敌新人。",
    basis=(
        "tradition: The card has no tradition/system field; decided by genre — an election forecast reported in May 2008 — as western astrology (electional/mundane reading as reported).\n"
        "systems_used: western astrology\n"
        "Indicator chain: Saturn–Uranus opposition begins exactly on Election Day, last seen 45 years earlier: Uranus (change, the outsider, youth) challenging Saturn (the establishment, age, incumbency structures). McCain embodies the Saturn pole (elder statesman, continuity); Obama embodies the Uranus pole (change candidacy). An opposition perfecting on the day itself tips the contest to the change pole. At asking time Obama leads the nomination race but has not clinched — the reading extends the same direction through the nomination to the general election. Object check: the verdict lands on the election winner, the exact object asked.\n"
        "第八节功量核 — 功量清单：助成线（主奥巴马胜）①Saturn–Uranus opposition exact on Election Day favouring the change candidate (source: given configuration; object: election outcome; direction: pro-change; state: exact on the decisive day); 助成线②Obama already leads the nomination race at asking time (fact-level support, state: leading); 压制线①McCain is presumptive nominee of the incumbent party with establishment weight (direction: suppressing; state: background only, no chart factor given). Pro-change lines hold the only chart factor; band set at a clear Obama win, not a coin-flip.\n"
        "主线认定：The Saturn–Uranus opposition line is the working main line (the sole dated chart factor, exact on Election Day); the outcome's direction and band follow it."
    ))

P["WP-003"] = dict(
    conf=0.55,
    pred="奥巴马连任：现任总统奥巴马在2012年11月6日大选中击败罗姆尼，成功连任。选举日水星逆行开启，主计票迟滞与程序争议，但结果不翻盘、无须重计易主。",
    basis=(
        "tradition: The card carries no tradition field; by genre (a May 2012 election forecast report) decided as western astrology.\n"
        "systems_used: western astrology\n"
        "Indicator chain: The salient dated factor in the setting is Mercury retrograde beginning on Election Day, 6 November 2012 — a signature of procedural confusion, delayed counts and disputed paperwork, but Mercury retrograde disrupts process, not incumbency itself; no configuration in the given material displaces the sitting president. Obama is the incumbent with the structural advantage of office; Romney is only the presumptive challenger in a competitive race. Direction: incumbent retained; Mercury retrograde is read at process level (delays, recount talk) and explicitly not upgraded into a change of winner. Object: the election winner, as asked.\n"
        "第八节功量核 — 功量清单：助成线（主奥巴马连任）①incumbency structure — sitting president seeking re-election with no displacing configuration given (object: outcome; direction: pro-incumbent; state: structural); 压制线①Mercury retrograde from Election Day (direction: suppressing; state: dated and exact — but its action is on process, not on the winner's identity); 压制线②competitive polling (direction: suppressing; state: background fact). Suppression lines affect margin and smoothness only; band set at 'Obama wins, with counting delays/controversy', not at an upset.\n"
        "主线认定：The incumbency line is the working main line (directly on the outcome object); Mercury retrograde is a secondary line confined to process, with stated grounds for not letting it override the main line."
    ))

P["WP-004"] = dict(
    conf=0.45,
    pred="克林顿胜：希拉里·克林顿击败唐纳德·特朗普，当选美国总统——此为哥斯达梅萨国际占星会议选举预测面板的多数共识断。",
    basis=(
        "tradition: No tradition/system field on the card; by genre (a conference election-forecasting panel report, October 2016) decided as western astrology, panel-consensus form.\n"
        "systems_used: western astrology (panel consensus)\n"
        "Indicator chain: The setting fixes the evidential base: a full international conference panel convened specifically to forecast this election, with polls favouring Clinton. A convened expert panel's consensus is the master-form source for this case type; the panel majority read the charts for Clinton — the establishment candidate with the polling lead — over Trump. No contrary individual reading is singled out in this card's setting, so the consensus stands as the prediction. Object: the election winner, as asked.\n"
        "第八节功量核 — 功量清单：助成线（主克林顿胜）①panel majority consensus of the convened forecasting panel (source: conference panel; object: outcome; direction: pro-Clinton; state: majority); 助成线②most polls favour Clinton at asking time (direction: pro-Clinton; state: consistent lead); 压制线：no chart-level suppressing line is recorded on the card. With two supporting lines and no recorded suppression, the band is a straightforward Clinton win per consensus.\n"
        "主线认定：The panel-consensus line is the working main line (the case's designated master source); the verdict is banded by it."
    ))

P["WP-005"] = dict(
    conf=0.42,
    pred="特朗普胜：唐纳德·特朗普击败希拉里·克林顿，当选美国总统——曾在17名共和党人混战时独排众议断准特朗普出线者，本轮续断其赢得大选。",
    basis=(
        "tradition: No tradition field on the card; by genre (same Costa Mesa panel report, but the setting singles out one panellist) decided as western astrology, individual-reader form.\n"
        "systems_used: western astrology (individual panellist's reading)\n"
        "Indicator chain: This card's setting differs from a bare consensus report in one loaded fact: one panellist had, early in the cycle against a 17-candidate field, already picked Trump to take the Republican nomination — a called shot that landed. A reader demonstrably attuned to the Trump candidacy's chart signature, against the field, is the discriminating source here; following that same reader's line through the general election gives Trump over Clinton, against the polling-favoured reading. Object: the election winner, as asked.\n"
        "第八节功量核 — 功量清单：助成线（主特朗普胜）①the singled-out panellist's proven Trump-specific track record this cycle (source: setting fact; object: outcome; direction: pro-Trump; state: a landed against-the-field call); 压制线①most polls favour Clinton (direction: suppressing; state: consistent lead); 压制线②panel majority leaned the other way (direction: suppressing; state: majority). The main line is one but specifically probative; band set at a Trump win against consensus, confidence discounted for the two suppressing lines.\n"
        "主线认定：The contrarian panellist's line is the working main line (directly on this candidacy, with a verified prior call as its state); it is given precedence over the generic consensus line on stated grounds."
    ))

P["WP-006"] = dict(
    conf=0.55,
    pred="脱欧成真：2016年6月23日公投，『脱离』一方胜出，英国投票离开欧盟——民调领先的『留欧』将被逆转，脱欧以微弱多数过关。",
    basis=(
        "tradition: The card has no tradition/system field; by genre (a mundane election forecast from the UK national charts) decided as western mundane astrology.\n"
        "systems_used: western astrology (mundane; UK national charts)\n"
        "Indicator chain: The setting supplies the decisive transit: on referendum day Uranus and Ceres conjunct at 23° Aries — Uranus is rupture and sudden reversal, and a conjunction perfecting on the very day of the vote acts on the vote's outcome, not on the campaign. The available national charts (1066, 1801, 1922) place the UK identity under this Aries-point pressure. Polls showing 'Stay' ahead with vast 'not sure' numbers are a soft background fact, outweighed by a dated disruptive configuration: late-deciding voters break toward rupture. Direction: Leave wins, narrowly (a rupture vote carried by late deciders does not produce a landslide). Object: the referendum result itself, as asked.\n"
        "第八节功量核 — 功量清单：助成线（主脱欧）①Uranus–Ceres conjunction at 23° Aries exact on referendum day (source: given configuration; object: referendum outcome; direction: pro-rupture; state: exact on the decisive day); 助成线②large 'not sure' bloc available to break late toward change (direction: pro-Leave; state: given in setting); 压制线①newspaper polls show 'Stay' ahead (direction: suppressing; state: February snapshot, soft). The dated exact configuration outranks the snapshot poll; band set at a narrow Leave win (suppression line caps the margin, grounds stated).\n"
        "主线认定：The referendum-day Uranus conjunction line is the working main line (exact, directly on the outcome, state ranked first); the margin band follows the poll suppression line."
    ))

P["WP-007"] = dict(
    conf=0.3,
    pred="特朗普胜，决定因素是克林顿的电邮门丑闻：竞选尾声由电邮争议（连同基金会争议）给予克林顿决定性打击，特朗普险胜入主白宫。应期点在大选日2016年11月8日，决定性冲击落在竞选最后两周内。",
    basis=(
        "tradition: No tradition/system field on the card; by genre (a tarot reader consulted in Union Square, August 2016) decided as western tarot (Waite tradition).\n"
        "systems_used: tarot (Waite) — with a recorded input defect\n"
        "Input defect, stated plainly: the card records that cards were drawn but does not record which cards — no spread, positions or card identities are given. A Waite reading cannot be reconstructed from absent cards, and no card is invented here; confidence is therefore cut to the floor for a card-based case. What the card does fix as facts: Clinton leads most August polls; her email controversy and the Clinton Foundation are already public controversies, and the question itself asks 'what will decide it'. Reading only what is given: the deciding variable named by the question's own frame is the email controversy — a scandal-line that strikes the frontrunner late, which is the standard shape of an upset decided by revelation rather than by campaigning. Direction follows that line: Trump wins narrowly, decided by the email scandal's late impact. Object check: verdict lands on the winner and the deciding factor, the two objects asked.\n"
        "第八节功量核 — 功量清单：助成线（主特朗普险胜）①email controversy already public and framed by the question as the deciding variable (source: setting fact; object: outcome; direction: anti-frontrunner; state: live controversy at asking time); 压制线①Clinton leads most August polls (direction: suppressing; state: consistent lead); 压制线②the evidential base itself is defective — drawn cards unrecorded (direction: suppressing certainty, not direction; state: input defect). Band set at a narrow Trump win only, with confidence floored at 0.3 on the stated defect.\n"
        "主线认定：The email-scandal line is the working main line (the only case-specific factor the card supplies that acts directly on the outcome); it is a degraded main line, held at low confidence because the card evidence is missing."
    ))

total_bytes = 0
for cid, d in P.items():
    obj = {"case_id": cid, "prediction_text": d["pred"], "basis": d["basis"],
           "confidence": d["conf"], "trigger": dict(TF)}
    s = json.dumps(obj, ensure_ascii=False, indent=1)
    with open(os.path.join(OUT, cid + ".json"), "w", encoding="utf-8") as f:
        f.write(s + "\n")
    total_bytes += len((s + "\n").encode("utf-8"))
print("written", len(P), "total_bytes", total_bytes)
