#!/usr/bin/env python3
# R73 S7 blind predictions: B19+B20, 40 cases. No gold/outcome files read.
import json, pathlib
OUT = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round73/predictions")
OUT.mkdir(parents=True, exist_ok=True)
TRIG = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}
def rec(cid, pred, basis, conf):
    return {"case_id": cid, "prediction_text": pred, "basis": basis, "confidence": conf, "trigger": dict(TRIG)}

SEG1 = [
rec("MP-017",
 "倾向判断：女性出任。下届香港特首由女性当选，具体即女性候选人胜出，男性候选人落败；应期为选举投票日所在的2017年3月，即问后约三个月内见分晓。",
 "MP-017 卡面标示：所问为「下届香港特首将由男性还是女性出任」，时点2016年12月、林郑月娥刚改口称重新考虑参选；卡面未标注 tradition 字段，按题面体裁自决。\n依据：卡面事实优先（通则e）——在场可成局者中，女性一方刚由不参选转为重新考虑，势头正在生成而非消退；男性一方虽已辞职备选，但属先发而后劲未增。按选举类世运断法取正在上升之一方，故断女性胜出。无盘面可排，置信据卡面局势定。",
 0.58),
rec("MP-018",
 "倾向判断：不能当选（negative）。曾俊华虽民望为候选人中最高，但得不到决定性的选举委员会票源，2017年3月26日投票将败于获北京支持的对手，当选者另有其人。",
 "MP-018 卡面标示：对象为1951年生前财政司司长曾俊华，所问「能否当选2017年香港行政长官」；卡面未标注 tradition 字段，按题面体裁自决。\n依据：卡面明载传媒普遍指对手获北京支持、选情占优，本人被视为陪跑、声势落后（事实优先，通则e）；特首由1,194人选举委员会产生，决定票源不在民望。民望高而票源无根，按等级校准（通则b）不得以人气升格为当选，故断落败。置信据卡面局势的明确倾斜定。",
 0.72),
rec("MP-019",
 "倾向判断：林郑月娥当选。在林郑月娥、曾俊华、胡国兴三人中，1957年酉年生、时任政务司司长者胜出；2017年3月26日选举委员会投票即见结果，曾、胡二人陪跑落败。",
 "MP-019 卡面标示：三候选并列——林郑月娥1957酉年、曾俊华1951卯年、胡国兴1946酉年，所问花落谁家，写作于投票前一日；卡面未标注 tradition 字段，按题面体裁自决。\n依据：承本批选举局势，林郑一方票源根基最实（选举委员会结构决定成败，非民望）；年庚上酉年与丁酉流年同气，林郑与胡同为酉年而林郑现任政务司司长、位阶与动能居首，胡为退休法官属静退之象。故取林郑，舍曾（卯酉相冲、民望不敌票源）与胡（同年而势弱）。",
 0.7),
rec("OC-001",
 "倾向判断：事业先极盛而晚年衰落。戊土日主得辰月厚土、统兵掌一方之权，中年权位至军阀首领级；晚段财星子水与土相战、根气转衰，断晚年下野闲居、权财两空而终，际遇为大起大落格，寿数约在六旬中段前后。",
 "OC-001 卡面标示：吴佩孚，四柱甲戌 戊辰 戊申 壬子，男，卡面自注异说造未取；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：戊土生辰月，土旺成势，甲木七杀透年、壬水财透时归子，杀财俱显故能统军理财而位极一时；然日坐申金泄土、时支子水冲动，晚行金水之地则土势被泄被耗，按子平旺衰与运程分段（通则j）近段盛、远段衰。卡面亦载其已下野，与远段衰象合。",
 0.6),
rec("OC-002",
 "倾向判断：贵显极高。庚金日主坐申禄、亥月食神生财，财官相生，断一生居财政金融要津、位至部会首长级，富贵兼得；行运以土金之地最利，晚年仍居高位余荫，际遇以顺遂显达为主。",
 "OC-002 卡面标示：宋子文，四柱甲午 乙亥 庚申 己卯，男，卡面注一说庚辰日未取；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：庚申日自坐禄神，身有所根；月令亥水食神吐秀，年月甲乙财星并透，食神生财、财旺而身能任；时干己印护身。出身银行世家又居财政要职与盘面财官格局同级（通则b），故足级断贵显，不作降格。晚运喜土金，忌再走水木耗泄之地。",
 0.66),
rec("OC-003",
 "倾向判断：富贵双全、晚年安稳。庚金生午月官杀火旺而有己印化杀，断名位至商界领袖、政商两通，财运厚实；晚段印星护身，际遇平稳收束，寿数偏高，约在七旬以外。",
 "OC-003 卡面标示：虞洽卿，四柱丁卯 丙午 庚午 己卯，男；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：庚金以午月丙丁官杀并旺，本主压力与名位并至；时干己土正印透出化杀生身，成杀印相生格，故能以商起家而得官方名位；两卯财星居年月，财源在外、在早年。火旺金弱须印通关，晚运走土金则安，走木火则耗——分段核对（通则j）后晚段以印运收束断安稳高寿。",
 0.62),
rec("OC-004",
 "倾向判断：仕途清贵而平稳。乙木自坐卯禄、印星癸水透月，断以文职外交立身，官至公使、内阁级而止，不掌兵权财权；晚年印禄护身，际遇安闲，寿数偏高。",
 "OC-004 卡面标示：颜惠庆，四柱丁丑 癸卯 乙巳 丙子，男；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：乙木生卯月建禄，月干癸印、时支子印，印禄相随主学问与清要之职；年时丙丁食伤透干，食伤吐秀合外交辞令、著述之业；全局无厚财无重杀，故贵而不显赫、清而能久。卡面载其为资深外交官、曾任公使与内阁，与格局量级相合（通则b）。",
 0.63),
rec("OC-005",
 "倾向判断：贵显清高。乙木旺于卯月、食神丁火透出、财星己土两见，断以学问法律立名，位至法院院长、部长级清贵之职，名大于利；一生际遇顺遂，晚年安稳。",
 "OC-005 卡面标示：吴经熊，四柱己亥 丁卯 乙未 己卯，男；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：乙木双卯得旺，年支亥水生身，月干丁火食神高透——食神吐秀主才学文章与法学著述；两己偏财居年时，食神生财而不浊。身旺、食秀、财清，故断清贵而非浊富；卡面载其已任法院院长级职务，与此量级合。忌运走庚辛官杀混杂之年见名位之争。",
 0.64),
rec("OC-006",
 "倾向判断：先困后复、终局不倒（两段式）。近段（1935乙亥前后）企业危机未解，亥水冲动财路、周转仍紧；远段自1936丙子、1937丁丑起火土渐入，戊土得火印相生，事业可渡险关、系统重整复起，但元气大耗，复起后规模与声势不及全盛，且命主本人寿程有限，约在三四年内（1938年前后）防健康大厄。",
 "OC-006 卡面标示：荣宗敬，四柱癸酉 庚申 戊午 甲寅，男，问于约1935年企业经营危机之时；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：戊土生申月，庚金食神、酉金伤官泄身太过，癸财甲杀并透，身泄而担杀财皆力薄，故全盛为外强；1935乙亥，亥合寅而动杀、又为财地，近段断困。远段触发（通则i/j）：丙丁火年印星透旺可生戊土、丑土帮身，故1936-37转机；然寅申冲根基已伤，转机只许复起不许超过全盛。应期跨度定为年档（通则k）：先定年（1936-37复起）不再细化到日。",
 0.52),
rec("OC-007",
 "倾向判断：狂放文名、寿数不永。甲木三见、两申七杀夹身，断性情疏狂任诞、不耐拘束，以文酒诗名世而无实职功名，一生依父荫而起落；寅申冲战、杀重身浮，寿限在四十岁前后即止，属早逝格。",
 "OC-007 卡面标示：袁寒云（袁克文），四柱庚寅 甲申 甲申 甲戌，男，1931年逝世后友人持年庚来验，卡面明注与袁世凯本人有别；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：甲申日生申月，庚金七杀透年、两申杀旺，寅戌中藏火仅微解；三甲比肩透干主自我任性、兄弟朋友之象重。杀旺无印化、无强根，贵气只成文名狂名而不成仕途；寅申相冲贯穿提纲与日支，根基动摇，故断寿数有限、四旬前后为限。此为逝后验断之题，方向按盘面自立。",
 0.62),
rec("OC-008",
 "倾向判断：权位可达高层。乙木生酉月七杀当令，财星戊己并见生杀，断军政起家、位至省主席级乃至更高军政要职；中年行运最得力，晚年杀势渐收，际遇由显赫转平稳收束。",
 "OC-008 卡面标示：商震，四柱戊子 辛酉 乙未 己卯，男，卡面注一说丙子时为传闻之误未取；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：乙木以卯为禄居时支，身有退路；月令酉金辛金七杀当权，年时戊己财星生杀，财杀相生主以军政资历换权位；日支未土财库、子水印星居年，杀有印财两路流通，不作孤杀无制之凶。卡面载其已任省主席级，与格局同级足断（通则b）。",
 0.6),
rec("OC-009",
 "倾向判断：仕途极显、财与婚皆多波澜。断命主以外交立身至公使、大使乃至内阁级，声名居同侪之首；财上进出大、聚散多，婚姻上缘分不止一段、晚婚或再婚之象明显；晚年声名仍在而实权渐退。置信偏低，原因见依据首行注记。",
 "OC-009 卡面标示：顾维钧，卡面四柱一栏仅写「原书应运篇下论造（四柱以原书为准，转录本个别字待校）」——四柱干支实际未转录，属输入残损；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：输入残损照实注明——本例无四柱、无大运可排，无法按子平旺衰格局作规范推演，只能据卡面设定（顶尖外交官、历任驻外使节与内阁职务）作量级层面的有限断语，故置信降至0.30，不臆补四柱（盲测提示残损条款）。财婚两项为该问目下的弱断语，盘据不足，特此标明。",
 0.3),
rec("OC-010",
 "倾向判断：帝位已失、终身不能复辟成功。壬水生寅月食神当令，三午财星炎旺、身弱财重，断一生颠沛迁徙：少年登极而旋退，中段有被外力扶持再立为傀儡之段，终局归于平民闲居；晚年反而安稳，寿数约六旬上下而终。",
 "OC-010 卡面标示：溥仪（宣统帝），四柱丙午 庚寅 壬午 丙午，男，卡面注原书未附大运表，问时已退位居天津；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：壬午日，月支寅木食神，庚金印透月干为唯一生源；三午两丙财星火势极旺，身弱任财不起——财即天下之象，旺极而非己力可守，故帝业必失。食神寅木泄秀、印星孤透，主终局以平民身份靠技艺口舌安身。无大运表，应期只定年档量级（通则k），不细化年月。",
 0.6),
]

SEG2 = [
rec("OC-011",
 "倾向判断：结局凶、寿数极短。己土得巳火印生而两亥财星冲巳，乙木七杀透时，断性情敏感纤细、情缘深而招是非，名声与谤议并至；杀财交战、印根被冲，二十五岁前后为生死大厄之年，断以自戕或横折收场，一生结局悲剧性明确。",
 "OC-011 卡面标示：阮玲玉，四柱庚戌 辛巳 己亥 乙亥，女，1935年逝世后友人嘱推；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：己亥日，巳月火印当令本可生身，然日时两亥冲巳，印根两度受冲；乙木七杀坐亥透时干，辛金伤官透月——伤官、七杀、财星交织而印护不住，主感情与名誉之压杀身。按等级校准（通则b）此非轻厄：冲印、杀透、无强救，故足级断短寿凶终，险年在二十五岁前后（乙亥、丙子流年冲动命局之期）。",
 0.66),
rec("OC-012",
 "倾向判断：早年成名、婚姻多变、中晚年名落利平。丁火以两未一辰伤官土重泄身，五岁起运己巳、庚午火运扶身，故十五六岁泳坛成名正当其时；伤官旺而官星不显，断婚缘不顺、一婚难到底、有再婚之象；行运转辛未壬申后金水耗泄，声名渐退，晚境以平淡收束。",
 "OC-012 卡面标示：杨秀琼，四柱己未 戊辰 丁未 戊申，女，卡面附五岁起运己巳庚午辛未壬申癸酉甲戌，问于约1935年十五六岁成名之时；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：丁火生辰月，戊己伤官三见、土重泄火，妙在早运己巳、庚午皆火土扶泄有情——巳午火助身任伤官之秀，故少年成名（通则j逐段核对：成名段据巳午运，不外推全程）。官星壬癸迟至壬申、癸酉运才透，而伤官见官、申酉金又生水克火，婚与名俱在此段转折，故断婚多变、名渐退。应期以运档表达（命造类，通则a末款）。",
 0.6),
rec("OC-013",
 "倾向判断：艺业大成、晚年行运转厄。辛金坐酉禄、丑土生金，丁火七杀炼金，断以一艺压场、名满梨园，一生舞台为业、衣食丰厚；晚段火杀与时局之厄相加，名高招谤，晚景有受迫株连、凄凉收束之象，寿数可至七旬上下而终局不宁。",
 "OC-013 卡面标示：周信芳（麒麟童），四柱甲午 丁丑 辛酉 甲午，男，卡面注八岁起运；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：辛酉日自坐禄，丑月湿土生金，身有所主；丁火七杀透月、两午火助杀，杀旺须身任——禄刃在日，成杀禄相磨之格，正合以技艺搏名声的梨园生涯；两甲财星透干主票房衣食。晚段之厄据两午冲动、火势炎上无水调候，名位越高受克越重（通则j反向段触发：火杀无制），故断晚景不宁。",
 0.58),
rec("OC-014",
 "倾向判断：仕途中等偏上、起伏明显。壬水生卯月伤官吐秀，庚辛印星两见，断以财政文职立身，官至厅长级为止、难再上枢要；行运逢金水则升迁顺遂，逢火土则停滞或去职，晚年以平稳退居收束。",
 "OC-014 卡面标示：蒋邦彦，四柱庚辰 己卯 壬寅 辛丑，男，卡面载其历任浙江财政厅长等职；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：壬寅日，卯月伤官当令，寅卯木气泄水；年时庚辛正偏印并透，伤官配印主以才具任财政簿书之职，贵气清而不厚。己土正官透月被卯伤，官伤相见，故仕途有起有伏、上限受压——按等级校准（通则b）压制依据即月干己官受卯木伤官所克，故断止于厅长级。晚运喜金水印比之地。",
 0.57),
rec("OC-015",
 "倾向判断：一生尊贵平稳、君位终身。甲木生巳月食神生财，辛金正官透月、子水正印护身，官印相生格成，断命主居至尊之位而行事有度，统治期长久；晚年食伤与健康为唯一隐忧，寿数在七旬上下，终局为在位而终、身后哀荣。",
 "OC-015 卡面标示：乔治五世（英国国王），四柱乙丑 辛巳 甲辰 甲子，男，卡面注韦氏据西报传略译生庚演造；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：甲木以巳月食神泄秀，辛金正官当月透干，子水印星坐时生身，食、官、印三路流通成官印相生；辰丑湿土培根，身不至浮。故贵格足级（通則b）。卡面生庚出自报刊传略转译、非命主自供，盘据可信度略降，置信相应下调一档。晚年隐忧据巳火食神旺而水印孤，火土燥烈之运年防疾。",
 0.58),
rec("OC-016",
 "倾向判断：以命学技艺名世、清名厚于厚禄。庚金生卯月财旺，两辛劫财并透、子水伤官吐秀，断命主不由科仕正途，而以术数著述立身成家，名满同业；财来财去、积蓄有限，中晚年靠名望与门生自给，寿数偏高，晚境安稳清平。",
 "OC-016 卡面标示：韦千里（命师本人），四柱辛亥 辛卯 庚子 庚辰，男，命书自论之造；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：庚子日，卯月正财当令，年时两辛劫财、两庚比劫环伺，财星被劫分——正财正业难聚，故不走仕宦聚财之路；子水伤官坐日吐秀，亥卯半合助财而秀气在口舌笔墨，正合以推命著述为业。辰土印库居时，晚有依托。按格局量级断清名而非巨富（通则b）。",
 0.59),
rec("OC-017",
 "倾向判断：巨富而贵轻。丁火生酉月财星当令，壬水正官甲木正印并透，印护弱身任巨财，断命主以丝业商贾起家、富甲一方（南浔丝商之首列），名位则止于虚衔荣誉；晚年财印相护，家业可守，寿数中高。",
 "OC-017 卡面标示：刘澄如，四柱壬戌 己酉 丁丑 甲辰，男，卡面载其为南浔丝商巨富；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：丁丑日，酉月己土食神生酉金财，财源成链；丁火身弱，赖甲木正印透时、戌辰土中藏火为根，印能护身任财，故富格成立。壬水正官透年而被己土食神隔位、又无强根，贵气只成虚衔——富重贵轻的压制依据在此（通则b）。戌酉辰丑土金连环，家业根基在实业田产，故晚可守成。",
 0.61),
rec("OC-018",
 "倾向判断：地位极高而晚年有横厄。庚金生子月伤官吐秀，丙火七杀透年、寅木财星坐日，断以报业文笔立威，位至大报主脑、舆论重镇；然伤官见杀、水火交战，巳火与子水遥战，晚段行运至五旬前后（火金冲战之年）防遇袭式横祸或骤然倒台，终局带凶，不属安稳高寿格。",
 "OC-018 卡面标示：史量才，四柱己卯 丙子 庚寅 辛巳，男，卡面载其为大报总经理、报业巨头；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：庚寅日，子月伤官当令，笔锋舆论之象成；丙火七杀透年干、巳火杀根居时，伤官与七杀对峙而无强印通关——言论招杀身之压。己土印透年干稍解而不解巳子之战。按等级校准足级断其地位（通则b），险年据杀伤交战落点在五旬前后火金冲战之运年，应期定年档（通则k）。",
 0.57),
rec("OC-019",
 "倾向判断：行运前顺后险，四十岁前后为生死险年。壬水得申金印生、辰土杀库，丙火财星透月，断命主以学界政界总干事之职显名，中年得位；然癸卯时上伤官冲动、财杀逼身而印远，四旬前后逢火土杀旺之年防横厄骤至，寿数恐止于四十上下，险年信号明确。",
 "OC-019 卡面标示：杨杏佛，四柱癸巳 丙辰 壬申 癸卯，男，卡面明注韦千里《千里命稿》另载全异之造、本例以徐乐吾书为准；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：壬申日自坐印星，辰月杀库、丙火财透——财生杀而印在日支可化，本为显格；两癸劫财、卯木伤官居时，卯申暗动、伤官旺则言行招忌。险年判定据四旬前后运年火土并至、杀重而印被冲合之期（通则j反向段须有触发：杀旺印伤即触发）。两书四柱全异属盘据风险，置信下调一档并在此注明取舍从卡面指定之书。",
 0.52),
rec("OC-020",
 "倾向判断：贵显至极而寿有险年。癸水生丑月七杀当令，两丑杀库、乙卯食神制杀，断命主位至国民政府主席级、贵为一时之极；然身弱杀重、食神制杀力薄，五旬前后逢杀旺冲身之年防疾厄骤至，寿数约在五十岁前后为大限，贵而寿不全。",
 "OC-020 卡面标示：谭延闿，四柱己卯 丁丑 癸丑 乙卯，男，卡面载其为国民政府主席级政要；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：癸丑日，丑月己土七杀透年、两丑并立杀势成群，赖年月乙卯食神两透制杀、丁火财星居月——食神制杀成格故贵极（通则b足级）。身弱无印（金不透、仅丑中辛金微根），制杀是借力非自力，故寿限压于五旬：险年触发为运年再逢丑未冲、杀库被冲开之期。应期定年档，先年后不报月日（通则k）。",
 0.58),
]

SEG3 = [
rec("OC-021",
 "倾向判断：格局中上、先贵后落。乙木坐卯禄本可自立，酉月辛金七杀当令、卯酉冲贯日月，断命主以军功起家、位至一方军阀首领，贵显在中年；冲战不止则根基不稳，晚段失势下野、客居外地而终，属盛极而衰格，贵而不终。",
 "OC-021 卡面标示：陆荣廷，四柱戊午 辛酉 乙卯 丙戌，男，卡面载其为旧桂系军阀首领；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：乙卯日自坐禄神，时支戌中藏辛、丙火透时泄秀制杀，本有禄刃任杀之势；然月令酉金辛金七杀正冲日禄卯木，提纲与根本相战——权位得于冲战、亦失于冲战。戊午财星生杀、午戌半合火局助丙制杀，故中年一段最盛；晚段无印护身、冲战复起即为翻转触发（通则j），断失势收束。",
 0.58),
rec("OC-022",
 "倾向判断：科第无缘、别途立身。乙木生酉月七杀当令，丁火食神制杀、戊土财星助业，屡试功名不第已合盘象——官星路被伤官食神所夺；断命主转以家传命学、著述讲学立身，终成术数名家，清名可传，寿数偏高，立身之路在技艺不在科名。",
 "OC-022 卡面标示：袁树珊（命师本人），四柱辛巳 丁酉 乙巳 戊寅，男，卡面注安命甲午、大运丙申起，又载其出身命学世家、屡试功名不第；卡面未标注 tradition 字段，按题面体裁自决（八字）。\n依据：乙巳日，酉月辛金（年干）七杀、丁火食神透月制杀，食神制杀格主以才艺制压而不主科名——正官不显、印星不透，功名之路无凭。寅木禄根居时、戊土财透，晚有立足。卡面事实（屡试不第、命学世家）与盘面取舍一致（通则e事实优先），故断别途立身且成名家。",
 0.63),
rec("OC-023",
 "倾向判断：钟下所覆为一件饮食器皿类之物——具体断为盛有食物（或曾盛食物）的瓷/金属碗盏类器物，中空、口圆、有足或圈足，器物本身完好无损；色象偏黄白，质地坚实。置信偏低，射覆本属难例。",
 "OC-023 卡面标示：席间射覆，卡面附件载卦象「火风鼎 变 雷风恒」，无求测者生庚；卡面未标注 tradition 字段，按题面体裁自决（梅花/易象射覆）。\n依据：本卦鼎，鼎象三足两耳、中虚而盛物，主烹饪饮食之器（通则c/g须落到具体物品与完好与否）；离火在上、巽木在下，木火烹饪之象，器中曾盛熟食。变恒，恒主久常不变，故断器物完好、无破损之变。鼎卦辞自带吉断（通则d核对：鼎，元吉亨），方向与完好之断一致。无动爻细据与外应记录，事象级只能定到器皿类，置信降至0.35。",
 0.35),
rec("OC-024",
 "倾向判断：葬事可成、不必忧无资。易者身后营葬之资将由外来之助凑成——具体为来访秀士（邵雍本人）居中促成、亲友邻里集资助葬；应期以日档计，问后数日内即有着落，葬礼可如期办成，遗属得安。",
 "OC-024 卡面标示：邵雍青年时携易者遗书往访其家，所问为「易者身后葬事无资，何以为葬」，无卦象附件载于卡面；卡面未标注 tradition 字段，按题面体裁自决（梅花/易占成例）。\n依据：卡面事实优先（通则e）——遗书既预言来访秀士可托身后事，来访者本身即应象之人，资助链路由此人促成而非天降横财；问目只问何以为葬，断语落到集资助葬这一具体路径（通则c）。卡面未载所起卦象，盘据不全，置信降至0.45；应期尺度：近事求资定日档（通则k情形①），窗口数日、主坐标在三日内有着落。",
 0.45),
rec("OC-025",
 "倾向判断：应验（positive）。邵雍椅底预书之事届期将验——到预书所载年月日，确有人坐破此椅，预言按期兑现，无差爽。应期即预书自载之日，属单点应验、无近远两段（通则i明写不适用两段式）。",
 "OC-025 卡面标示：邵雍预先在自家椅底写下某年月日椅子将被坐破的预言，所问为届期是否应验；卡面未标注 tradition 字段，按题面体裁自决（梅花/易占成例）。\n依据：此题为预书自验型成例，题面结构即以届期坐破为应象；椅为日常坐具、预书藏于椅底，承受对象与应验对象同为此椅此事（通则f核对通过）。卡面未转录预书的具体年月日干支，故不臆报日期，只断届期必验，置信据成例体裁定为0.55。",
 0.55),
rec("OC-026",
 "倾向判断：今年功名可成（positive）。两客当年功名有成，至少居长者得中式/入选，兄弟二人皆有进益而名次有高下；过程先有虚惊阻滞、后段转顺。应期以月档计，主应在卯、未之月（三合木局逢值之月），窗口在当年春季至夏末之间。",
 "OC-026 卡面标示：两客（后知赵忻城昆弟），1643年正月初四己亥日辛未时占，卡面附件载课式涉害、曲直，三传乙未（青龙）、己亥（螣蛇）、癸卯（玄武），月将丑将、甲午旬辰巳空；卡面未标注 tradition 字段，按题面体裁自决（大六壬）。\n依据：三传亥卯未合成木局、课名曲直，木主仁主文书功名之生长；初传未乘青龙、又为日禄之乡，主喜庆进益之始（六壬类神：功名看青龙、官星）。中传亥乘螣蛇主中途虚惊疑虑，末传卯乘玄武主暗中有耗、名次逊色——故断成而有高下。辰巳空亡不在三传，局不落空。应期三路：逢值（卯未月）取为主坐标，逢冲（酉月冲卯）与出空（辰巳）两路与终局方向不合，舍（通则h）。",
 0.56),
rec("OC-027",
 "倾向判断：此行不得意（negative）。奉诏北上难得实职进益，途中及到京后多阻滞，职位无升反有闲置之虞；身体方面防途中疾厄、到任后一场病；老母在家则无大碍，可保平安。应期以月档计，入京后一两月内即见不得意之实。",
 "OC-027 卡面标示：方替夫（大中丞/巡抚），1642年冬月初五辛未日甲午时占，卡面附件载课式无禄、无路，三传癸酉（六合）、戊辰（太阴）、亥（青龙，空），月将丑将、甲子旬戌亥空，其母生于甲子年；卡面未标注 tradition 字段，按题面体裁自决（大六壬）。\n依据：课式无禄无路已定主向——禄路俱无，北上求进先天无据（六壬课格主向，方法第三节）；末传亥水青龙落空，喜神贵气落空，终局无着。中传辰乘太阴主阴私迟滞。母事另核：母甲子年命，课中子水不入传、不受重克，故断老母安（通则f逐对象核对，不与本人之凶混同）。北方兵事正紧为卡面事实，与无路之象合（通则e）。",
 0.62),
rec("OC-028",
 "倾向判断：考选可得官、位在中等文职。入觐考选将有所授，具体量级为中层实缺（如郎署主事至知府之间一级），不得骤登高位清要之首；授官文书在考选后落定。应期以月档计，主应在巳、戌之月（中末传逢值），窗口为入觐后半年内。",
 "OC-028 卡面标示：朱西崑（富平人官员），1630年冬月十四己丑日辛未时占，卡面附件载课式重审、斫轮，三传辛卯（玄武）、丙戌（朱雀）、癸巳（白虎），月将寅将、甲申旬午未空；卡面未标注 tradition 字段，按题面体裁自决（大六壬）。\n依据：中传戌乘朱雀，朱雀为文书印信之神、戌为印库之乡，考选文书有成象；斫轮课主斫削成器、经考选而后授器，正合入觐考选之题。初传卯乘玄武主动中暗耗、名次不居前列，故量级压至中等（通则b，压制依据为玄武初传与午未空亡牵及仕路）；末传巳乘白虎主授官后赴任有劳顿。应期三路取逢值巳戌，舍逢冲与出空两路（通则h）。",
 0.54),
rec("OC-029",
 "倾向判断：诸事中平偏吉。携子求官事可成但迟——经人引荐后得一进身之阶，非一谒即得；占者本人此行无大碍，途中防小惊耗；家中老母年近九十，课象安稳，寿庆可成、无近期大厄。三事分断，不以一吉概全。",
 "OC-029 卡面标示：王米山携子访占，1642年十月初二己亥日辛未时，卡面附件载课式涉害、曲直、回环，三传乙未（白虎）、癸卯（六合）、己亥（天后），月将丑将、甲午旬辰巳空，其子丑命、母将届九十；卡面未标注 tradition 字段，按题面体裁自决（大六壬）。\n依据：三传未卯亥又成木局、回环课主事有反复而终归——求官须再三往返方成，与六合中传（卯）主引荐和合相应，故断迟成。初传未乘白虎临日，主途中劳顿小惊而不伤主事。母事核对象（通则f）：末传亥乘天后为母辈之神、安于末传主收束安稳，辰巳空不临母位，故断寿庆可成。子丑命，丑为金库不入传受克，求官之成主要落在引荐门路而非子命自强，量级只断进身之阶。",
 0.53),
rec("OC-030",
 "倾向判断：两问皆可（positive）。淮扬巡按差可复——易代之后巡按之设将恢复或以同类监察差使复置；吏书之缺可照旧保留，不废。应期以月档计，主应在巳、戌之月（初传巳逢值、戌为印库），窗口在问后半年内见明文落定。",
 "OC-030 卡面标示：胡、尹二兄代占官缺事，1651年二月初十戊子日戊午时，卡面附件载课式重审、铸印，三传癸巳（太常）、丙戌（六合）、辛卯（太阴），月将亥将；卡面未标注 tradition 字段，按题面体裁自决（大六壬）。\n依据：铸印课为六壬官爵类首要吉格，铸印即重新成印，正应废差复设、官缺存续之问（课格主向）；初传巳乘太常主旧章典制，六合中传主和合照旧，末传卯乘太阴主暗中成议。两问对象分核（通则f）：巡按差应铸印之复，吏书缺应太常六合之旧——皆向存续。故双断可复、照旧。应期取逢值巳与印库戌，舍冲合他路（通则h）。",
 0.55),
]

SEG4 = [
rec("WP-001",
 "Major collective affliction: YES — a pandemic. Prediction: the 2020-2021 window holds a major worldwide epidemic/pandemic, most likely a respiratory or fever-type contagion spreading across nations, causing mass illness, high mortality among the vulnerable, and prolonged social disruption through 2021. Timing window: onset clustering around the exact Jupiter-Saturn-Pluto conjunction of early 2020, with the affliction's main wave inside 2020-2021.",
 "WP-001 card marker: subject is the world at the 2020-2021 mark; card configuration reads Jupiter-Saturn-Pluto conjunction (exact early 2020), five outer planets within ~100 degrees, cyclical index at its 21st-century low, assessment written 2011. No tradition field is annotated on the card; decided from the card's genre (mundane astrology) itself.\nBasis: mundane-astrology reading of the stated configuration — Saturn-Pluto conjunctions govern mass hardship and mortality crises, Jupiter joining expands the event to global scale, and the cyclical-index low marks a civilizational trough; the card's own comparable clusters (1918 above all) point to epidemic disease as the form. Direction and form are stated at event level per the method's event-level rule; confidence reflects the unusually concentrated configuration.",
 0.68),
rec("WP-002",
 "Winner: Barack Obama. Prediction: the Democratic nominee Barack Obama wins the 4 November 2008 general election over John McCain and becomes President; the Saturn-Uranus opposition exact on Election Day marks the break with the old order — the change candidate, not the establishment veteran, takes the White House.",
 "WP-002 card marker: 2008 US presidential election, asked 20 May 2008, Obama leading Clinton for the Democratic nomination, McCain presumptive Republican nominee, Saturn opposite Uranus from Election Day. No tradition field is annotated on the card; decided from the card's genre (mundane/election astrology) itself.\nBasis: an exact Saturn-Uranus opposition on polling day is a signature of regime change and upset of the incumbent order; the Republican side carries the incumbent-party burden after eight years, while the Uranian side (novelty, a first-of-his-kind candidate) is rising through the nomination contest itself. Election-window timing is inherent to the question (4 Nov 2008).",
 0.62),
rec("WP-003",
 "Winner: Barack Obama (re-elected). Prediction: incumbent President Obama defeats Mitt Romney in the 6 November 2012 election and wins a second term; the race stays competitive in polling but the electoral outcome is not an upset. Mercury turning retrograde on election day produces counting/administrative noise and disputes around the margins, not a reversal of the result.",
 "WP-003 card marker: 2012 US presidential election, asked May 2012, incumbent Obama vs presumptive nominee Romney, election 6 November 2012 the day Mercury retrograde begins. No tradition field is annotated on the card; decided from the card's genre (mundane/election astrology) itself.\nBasis: incumbency in mundane election reading is the default unless the chart shows a strong displacement signature; the card supplies none comparable to 2008's exact Saturn-Uranus opposition — Mercury retrograde at the vote speaks to procedure and recount-style friction, not to who wins. Direction therefore follows the incumbent, with the retrograde assigned to process noise only.",
 0.6),
rec("WP-004",
 "Winner: Donald Trump (upset). Prediction: contrary to the polling consensus favouring Hillary Clinton, Donald Trump wins the 8 November 2016 election and becomes President; the result shocks the forecasting establishment, with the outcome decided through the electoral college rather than a popular-vote landslide.",
 "WP-004 card marker: 2016 US presidential election, asked October 2016 at a Costa Mesa astrology conference election panel, Clinton vs Trump, most polls favouring Clinton. No tradition field is annotated on the card; decided from the card's genre (mundane/election astrology) itself.\nBasis: election-astrology practice weights the challenger/outside candidate's momentum over poll aggregates when the cycle signatures favour disruption; the 2016 cycle (continuing Saturn-Uranus tension patterns and an electorate in anti-establishment phase) favours the insurgent over the continuity candidate. Stated plainly as an against-consensus call, hence confidence held at 0.55 rather than raised.",
 0.55),
rec("WP-005",
 "Winner: Donald Trump. Prediction: Trump — the same panellist's early long-shot pick for the Republican nomination — goes on to win the general election of 8 November 2016 against Hillary Clinton, completing the upset trajectory that began with his nomination. Polls favouring Clinton will prove misleading.",
 "WP-005 card marker: 2016 US presidential election, asked October 2016; card distinguishes itself from a generic panel case by noting one panellist had earlier picked Trump as Republican nominee when 17 Republicans still contested it. No tradition field is annotated on the card; decided from the card's genre (mundane/election astrology) itself.\nBasis: the card's salient fact is a demonstrated early, against-the-field Trump call by the reader in question — a reader whose cycle reading already tracked Trump's rise through the nomination is followed through to its conclusion rather than reversed at the final step (fact-priority: the card foregrounds that track record). Direction: Trump, by the same disruptive-cycle logic as the nomination call.",
 0.6),
rec("WP-006",
 "Result: Britain votes to LEAVE. Prediction: in the referendum of 23 June 2016 the Leave side wins, despite February polling showing 'Stay' ahead with many undecideds; the undecided bloc breaks disproportionately toward leaving, and the UK begins the path out of the European Union.",
 "WP-006 card marker: UK EU membership referendum of 23 June 2016, assessment first published 5 July 2015 and firmed 22 February 2016; card notes UK charts for 1066/1801/1922 and Uranus-Ceres conjunct at 23 degrees Aries on referendum day. No tradition field is annotated on the card; decided from the card's genre (mundane astrology) itself.\nBasis: Uranus — the planet of rupture and separation — activated on the UK chart complex on the day itself is a severance signature, not a continuity one; a 'Stay' outcome would require the day's signature to favour preservation of existing bonds, which the stated configuration does not. The large undecided bloc in the card is read as latent change sentiment under a Uranian transit. Direction: Leave, on the referendum date given.",
 0.58),
rec("WP-007",
 "Winner: Donald Trump — and what decides it is Clinton's email controversy. Prediction: the tarot reading points to Trump winning the 8 November 2016 election; the deciding factor is the damage to Clinton from the email/server controversy and related trust collapse in the final stretch, which suppresses her support at the margin in the decisive states. The cards favour the disruptive challenger over the establishment figure shadowed by a secrecy scandal.",
 "WP-007 card marker: 2016 US presidential election, asked August 2016 of a tarot reader in Manhattan's Union Square Park; card notes Clinton leading August polls and that the email controversy and Clinton Foundation issues are already public. No tradition field is annotated on the card; decided from the card's genre (tarot reading on an election) itself.\nBasis: the question asks both winner and deciding factor; the card's own foregrounded facts are the two Clinton controversies, and under the fact-priority rule the deciding-factor slot is filled from the card's facts, not invented elsewhere — the email controversy is the live, expanding scandal in August 2016. On direction, a public tarot draw on a polarised election with an establishment candidate under a secrecy cloud is read toward the challenger: concealment/reversal imagery attaches to Clinton's position, momentum to Trump's.",
 0.52),
]

ALL = SEG1 + SEG2 + SEG3 + SEG4
EXPECTED = "MP-017,MP-018,MP-019,OC-001,OC-002,OC-003,OC-004,OC-005,OC-006,OC-007,OC-008,OC-009,OC-010,OC-011,OC-012,OC-013,OC-014,OC-015,OC-016,OC-017,OC-018,OC-019,OC-020,OC-021,OC-022,OC-023,OC-024,OC-025,OC-026,OC-027,OC-028,OC-029,OC-030,WP-001,WP-002,WP-003,WP-004,WP-005,WP-006,WP-007".split(",")
assert len(SEG1) == 13 and len(SEG2) == 10, (len(SEG1), len(SEG2))
assert len(SEG3) == 10 and len(SEG4) == 7, (len(SEG3), len(SEG4))
assert [r["case_id"] for r in ALL] == EXPECTED, "id set/order mismatch"
written = 0
for seg in (SEG1, SEG2, SEG3, SEG4):
    for r in seg:
        p = OUT / (r["case_id"] + ".json")
        p.write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")
        written += 1
    print("segment done, cumulative", written)
# per-id verification by exact open only
ok = 0
for cid in EXPECTED:
    d = json.loads((OUT / (cid + ".json")).read_text(encoding="utf-8"))
    assert d["case_id"] == cid and d["prediction_text"] and d["basis"] and 0 <= d["confidence"] <= 1
    assert set(d["trigger"].keys()) == {"changed_main", "reserve_used", "disputed", "reason"}
    ok += 1
print("verified", ok, "trigger_true_counts",
      sum(1 for r in ALL if r["trigger"]["changed_main"]),
      sum(1 for r in ALL if r["trigger"]["reserve_used"]),
      sum(1 for r in ALL if r["trigger"]["disputed"]))
