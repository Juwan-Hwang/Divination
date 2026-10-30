import json, pathlib
OUT = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round58/predictions")
OUT.mkdir(parents=True, exist_ok=True)
F = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}
P = {}
def add(cid, pred, basis, conf):
    P[cid] = {"case_id": cid, "prediction_text": pred, "basis": basis, "confidence": conf, "trigger": dict(F)}

BZ = "体系：八字子平（据输入卡自带四柱作断，tradition 以卡内字段为准）\n"
# MP
add("MP-017","断为女性出任。2017年3月26日选举委员会投票，林郑月娥当选下届香港行政长官，成为首位女性特首；男性候选人（曾俊华、胡国兴）陪跑落败。应期：日档，2017年3月26日开票日（定值）。",
 "体系：时事占断（输入卡无盘面、无相格、无卦象，仅据卡内情境作断，输入残损）\n卡内事实：梁振英已宣布不连任；曾俊华已辞职备选；林郑月娥由不参选改口重新考虑——改口本身即获支持信号最强之一人，且其为政务司司长、管治班子之首，建制票源根基远胜辞职备选者。按事实优先序取此象：下届特首为女性。无占具可凭，具体断语密度只能落到人物与日期，故降置信。",0.55)
add("MP-018","断为不能当选。曾俊华民望虽为候选人之冠，但选举由1,194人选举委员会决定，北京支持与建制票源在林郑月娥一方；2017年3月26日投票结果为林郑当选，曾俊华得票居次落败。应期：日档，2017年3月26日（定值）。",
 "体系：时事占断（输入卡无相格/盘面数据，仅据卡内情境作断，输入残损）\n卡内事实已明言传媒普遍指林郑获北京支持、选情占优，曾俊华被视为陪跑、声势落后；民望与选委会票源方向相反时，决定结果者为票源而非民望。按事实优先序断其败选。无占具可凭，降置信。",0.62)
add("MP-019","断为林郑月娥当选。2017年丁酉年，酉金当令：林郑月娥1957年酉年生，与流年同气得令、最旺；曾俊华1951年卯年生，卯酉相冲、根气受冲主败；胡国兴1946年酉年生虽同气而年高退气、法官背景票源最薄。故花落林郑，2017年3月26日当选。应期：日档，选举日3月26日（定值）。",
 "体系：生肖流年占断（据输入卡自带三人出生年作断）\n丁酉年酉为值年旺神：同气者（酉年林郑）得令占先，卯年生者逢卯酉冲为最不利之象，胡国兴酉年同气但1946年生、年事与票源俱弱，只作陪衬。三路以流年同气/相冲定主坐标，取林郑。卡内无完整八字与相格，降置信。",0.6)
# OC bazi
add("OC-001","戊土日主生辰月、土旺成势，申金食神泄秀生壬水之财，财旺有源：主军政发迹、统兵一方，至军阀首领、主政一方之位，中年辛未、壬申运食伤生财为一生高峰。晚运转甲戌、乙亥，官杀克身而财党耗气，势力尽失、下野寓居，清贫守节、孤寒病困而终，寿在六旬中段。格局量级区间：下限方面军政长官—上限主政一方之首领，断至首领级，依据为身旺任财、食神生财成链。",
 BZ+"甲戌 戊辰 戊申 壬子：戊土得令得地身旺，申为食神、壬财透时，申子半合水局财气流通。男命甲年顺行，运己巳、庚午、辛未、壬申、癸酉、甲戌、乙亥。峰值运三核对：壬申运①财星得申子之根得地②运干壬即财星透出呼应③否决三条核查：壬申①运干合绊用神未命中②运支冲克用神之根未命中③运干透忌神且通根未命中，满足3项为峰值；辛未次之。晚年甲乙木官杀运克旺土而无火印通关，逆主线主失势。子女：时柱壬子财居时，子息以财官论有后而晚景不赖其养。病位：土旺水弱，脾胃与肾水之疾为病字落处。",0.6)
add("OC-002","庚金日主生亥月、寒金喜火，乙木正财合身、卯亥半合财局，己土正印透出生身救应：财印相随之贵格。主金融财政之权位，至部长、院长级贵显，富而多金；中年行金水、火土运财官印齐到为高峰。晚年退居海外安享，富贵善终，寿至七旬以上。格局量级区间：下限财政要职—上限部院首长，断至部院级，依据为财旺生官（午中丁官）、印星有根救身。",
 BZ+"甲午 乙亥 庚申 己卯：庚金坐申有根，亥月食神泄气、财星成势，身偏弱而己印贴身相生，破格有救。男命甲年顺行：丙子、丁丑、戊寅、己卯、庚辰、辛巳、壬午、癸未。峰值以庚辰、辛巳运印比扶身任财官为高；早年丙丁官杀运名位先显。病位：金寒水冷，肺与寒湿之疾；破耗之因在财多身弱之运被劫耗。子女：时柱己卯印财，子息成器。",0.58)
add("OC-003","庚金日主生午月、火旺官杀当令，丁丙官杀齐透，己土正印贴身化杀生身，卯木财星生官：杀印相生、财官印流通之格。主政商两栖、商界领袖之名位，富贵双全，中年印比运任杀为高峰。晚年名望不坠，虽经战乱资财有损，仍以尊荣终，寿近八旬。格局量级区间：下限巨商—上限政商领袖，断至领袖级，依据为杀印相生格成、印星得卯午之气。",
 BZ+"丁卯 丙午 庚午 己卯：庚金无根身弱，官杀火旺攻身，己印为唯一救应且坐卯受木耗，格成而救应不厚，故贵在借官府之势的商界领袖而非自握兵权。男命丁年阴年逆行：乙巳、甲辰、癸卯、壬寅、辛丑、庚子、己亥、戊戌。峰值运三核对：辛丑运①印星己土得丑库通根②运干辛为比肩扶身呼应③否决：①合绊用神未命中②冲克用神之根——丑未无涉、未命中③透忌神且通根未命中，满足3项为峰值。病位：火旺金熔，肺与心血之疾。",0.57)
add("OC-004","乙木日主生卯月得禄、木旺成势，癸丙两透：印星生身、伤官吐秀，文贵之格。主外交仕途贵显，至驻外公使、内阁总长级，以才学语言立名。中年行庚辛官星运、印官相生为高峰。晚年退隐著述，清贵安闲，印旺主寿，寿至八九旬善终。格局量级区间：下限高级外交官—上限阁员级，断至阁员级，依据为月令禄格成、印伤两不相碍。",
 BZ+"丁丑 癸卯 乙巳 丙子：乙木卯月建禄，子癸印星两见，巳丙伤官泄秀生财（丑土），气势流通。男命丁年逆行：壬寅、辛丑、庚子、己亥、戊戌、丁酉、丙申。峰值以庚子运官印相生、子印得地为高。病位：木旺水弱，肝与目、筋骨之疾轻浅。子女：时柱丙子伤官印并，子息以文显。破耗因伤官运中言行招忌而小损，无大破。",0.58)
add("OC-005","乙木日主生卯月建禄，丁火食神透出生己土之财，亥卯未三合木局身旺任财食：食神生财、秀气流通之格。主以法学才学贵显，至法院院长级司法高位，中年木火运食伤吐秀为高峰。晚年转学术著述、名望益高，富贵善终，寿至八旬以上。格局量级区间：下限司法高官—上限法院院长级，断至院长级，依据为禄格身旺、食神生财成链无破。",
 BZ+"己亥 丁卯 乙未 己卯：乙木两卯一亥根重，丁食己财两见于年月时，格局清纯。男命己年阴年逆行：丙寅、乙丑、甲子、癸亥、壬戌、辛酉、庚申。峰值以丙寅运食神得禄、木火通明为高；晚年金运官星到位名位收束不败。病位：木旺土弱，脾胃之疾为病字。子女：时柱己卯财坐禄，子息有成。",0.57)
add("OC-006","往后走势：危而可渡、盛而难复。此造戊土生申月、食伤金旺泄气生癸水之财，甲木七杀坐寅为权，午火印星为救：企业危机在乙亥、丙子年前后（约1935—1937）最深，被迫收缩、借贷重组，靠合伙与子弟支撑不至全倒；但本人元气已伤，丁丑、戊寅年（1937—1938）为寿关，病逝于五旬末至六旬初之数，企业由后人续营而规模大减。应期：年档，先定运（当时运交乙丑、甲子之交）再定年，主坐标1937—1938（定值）。",
 BZ+"癸酉 庚申 戊午 甲寅：戊土申月食神当令，酉伤庚食齐见，财杀并旺而身偏弱，午印贴身为救应。问时约1935年乙亥，正值经营危机。男命癸年逆行：己未、戊午、丁巳、丙辰、乙卯、甲寅、癸丑——中年丙辰、乙卯运官印扶身曾经大盛，至甲寅、癸丑运杀财耗身转衰。病位：土弱金旺水耗，脾胃与肺、肾之疾，终局之病从土弱受克推出。破耗之因：食伤生财过度扩张、财星被运冲耗。峰值在丙辰运（已过），此后无峰。",0.55)
add("OC-007","甲木日主生申月、庚金七杀透出，双申冲寅、杀重身弱无印化杀：性情孤傲狂放、才高不羁。富贵之子而功名无成，仕途之路断绝，一生以诗文书画、风流韵事名世，财来财去、纵情耗身。杀攻身而无救，主寿短：终年在四旬初，辛未年（1931）前后即其寿关，应验于新逝之时。应期：年档，主坐标1931年前后（定值）。",
 BZ+"庚寅 甲申 甲申 甲戌：甲木寅根被双申冲去，日主失根；甲木比肩三见只作孤高之性、不成帮身之势（申金当令克木）。无水印通关，七杀攻身为全命之病，病字即庚申金，落年月主长上环境与自身筋骨肺系。格局量级：贵公子之出身、文人狂士之终局，官位无份。子女：时柱甲戌比肩坐财库，子息缘薄。",0.62)
add("OC-008","乙木日主生酉月、辛金七杀透出当令，子水印星化杀，卯木禄根与未土木库护身：杀印相生而有根。主军政权位，至省主席、上将级成就，中年金水运杀印齐到为高峰。卯酉冲主一生迁动、职位屡易而终能自保；晚年退居安闲，印旺有根主寿长，寿至八旬上下善终。格局量级区间：下限高级军政长官—上限省主席级，断至省主席级，依据为杀印相生、禄根未被冲尽（未为木库收卯）。",
 BZ+"戊子 辛酉 乙未 己卯：乙木酉月杀旺，子印贴年化杀，时卯为禄、日支未为库，根气两存故非从杀。男命戊年阳年顺行：壬戌、癸亥、甲子、乙丑、丙寅、丁卯、戊辰、己巳。峰值运三核对：癸亥运①用神印星水得亥禄得地②运干癸即印星透出呼应③否决：①合绊用神未命中②冲克用神之根未命中③透忌神且通根未命中，满足3项为峰值。病位：金木相战，肝胆筋骨之疾。",0.57)
add("OC-009","输入残损，只能作低置信方向断：命主仕途贵显至外交首长、国际舞台之位，财富因仕途与婚姻而厚，婚姻不止一段、配偶带助益；晚年退居海外，长寿善终，寿在九旬上下。此断仅据卡内事实（已历任驻外使节与内阁职务、顶尖外交官）顺其势推，不敢细断运程与病位。",
 "体系：八字子平（据输入卡作断）\n输入残损如实注明：本卡四柱字段只写「原书应运篇下论造（四柱以原书为准，转录本个别字待校）」，未给出可用四柱——无四柱即无法排盘、定格局、排大运，凡格局、峰值运、病位、应期一概无据不报、不臆补。仅按卡内既成事实（顶尖外交官、历任使节与内阁）作方向性收束，故置信大幅下调。",0.35)
add("OC-010","壬水日主生寅月、食神泄气，三午财星当旺、火炎土燥，庚金印星孤透无根：财多身弱、印又受财坏。主帝位早失，一生随政治势力浮沉、身不由己：少年退位出宫，中年再被扶作傀儡之君而再败，家产名器尽散；晚年经改造为平民，反得安稳数年，寿终六旬初。病位：火炎水涸，心肾不交、泌尿与血液之疾为终局之病。格局量级：虚位之贵、无权之命，富贵皆他人所予亦由他人收回。",
 BZ+"丙午 庚寅 壬午 丙午：壬水寅月失令，三午一丙财势炎上，庚印坐寅受克、无申酉根，救应无力——不从财（印透有心向旧位），作财多身弱论。男命丙年顺行：辛卯、壬辰、癸巳、甲午、乙未、丙申、丁酉。青年壬癸比印运尚得庇护，中年甲午、乙未食财运被大势力借用而再起再败，晚年丙申、丁酉印根稍到方得平民之安。子女：时柱丙午财居时，子息平常。原书未附大运表，运名按顺行月柱推排、起运岁数无据不报。",0.6)
add("OC-011","己土日主生巳月、印旺身强，辛金食神透出吐秀，两亥财星冲巳：主姿容才艺出众、少年成名影坛，食神生财、名利早发。然巳亥冲为全命之病：婚姻感情为祸根，夫星乙木七杀坐亥虚浮、情路多折，易受人言与情事所困。财星冲印、盛年无依，断为早夭之命：寿仅二旬中段，1935年前后乙亥、甲戌之年即寿关，死于感情人言之逼。应期：年档，主坐标1935年（定值）。",
 BZ+"庚戌 辛巳 己亥 乙亥：己土巳月印令身旺，辛食透干，亥财两见冲巳火印——印为靠山被冲，靠山不稳。女命庚年阳年逆行：庚辰、己卯、戊寅、丁丑——青年己卯、戊寅运杀旺攻入感情宫位，冲提加剧。病位兼情志：土旺水冲，脾胃与肾水、神志郁结之象。子女：时柱乙亥杀财，子息缘未及显。格局量级：名高寿短，名望上限为当红影星、寿数下限被冲局压至二旬。",0.6)
add("OC-012","丁火日主生辰月、戊土伤官两透，土重泄火，申金财星为出路：五岁起运己巳、庚午火运扶身，少年即成名——泳坛冠军在己巳、庚午运内（十五六岁）达个人高峰。辛未运后火势渐退，壬申、癸酉运财官齐来而身弱难任：婚姻不美、易陷妾室侧室之议与人言，名声由体坛转入交际场，中年以财与依附他人过活。甲戌运晚景平淡，寿至六旬上下。婚姻断语依据：伤官旺而官星（壬癸水）藏而不透、迟至中运才现，夫星弱而迟，主婚迟且不顺。",
 BZ+"己未 戊辰 丁未 戊申：丁火辰月晦火，戊伤官年月时三见，土多火弱，申金财星泄土生水官为流通之路。女命己年阴年顺行，卡内已给运序：己巳、庚午、辛未、壬申、癸酉、甲戌。峰值运三核对：庚午运①用神火得午禄得地②运干庚为财星、非扶身之干，只半呼应③否决：①合绊用神未命中②冲克用神之根未命中③透忌神且通根未命中，满足2项且先到，与己巳同级并列取先到己巳为峰值、庚午称次峰。病位：土重火弱，脾胃与心、目之疾。",0.58)
add("OC-013","辛金日主生丑月、印旺土厚，酉金禄根在日，丁火七杀与两午官杀为炼金之火：官印相生、金火锻炼成器之格。主以技艺登峰造极，梨园宗师、一代名家，名望大于实权，中年庚辰、辛巳运金火齐到为高峰。晚运壬午、癸未火土交攻而金气渐耗，又逢世局之变，晚景有受冲击、身名俱困之厄，寿至七旬中后段而终，艺名留后世。格局量级区间：下限名伶—上限梨园宗师，断至宗师级，依据为禄格有根、官印相生无破。",
 BZ+"甲午 丁丑 辛酉 甲午：辛金丑月印令，坐酉禄根，身旺任杀，丁杀透月为炼。男命甲年顺行：戊寅、己卯、庚辰、辛巳、壬午、癸未、甲申、乙酉。峰值以辛巳运比肩禄地、巳酉丑合金为高。病位：金旺火炼，肺与咽喉（以声立命者喉为命脉）之疾。子女：时柱甲午财官，子息有成、传艺有人。破耗之因：晚运财星透动引杀攻身。",0.58)
add("OC-014","壬水日主生卯月、伤官当令，寅卯木旺泄水，庚辛印星两透为救，辰丑土官杀潜藏：伤官佩印之格。主以才学理财入仕，至财政厅长级而止——印星有根故有位，木旺泄身、官星不透故不至极品。中年行金水运扶身任事为高峰；晚年退隐，木火运须防财耗与病，寿至七旬上下平顺而终。格局量级区间：下限地方财政长官—上限厅长级，断至厅长级，依据为伤官佩印成格而官星藏库不透。",
 BZ+"庚辰 己卯 壬寅 辛丑：壬水卯月伤官，寅为食神，木势泄水太过，庚辛双印透干贴身为用。己土正官透月却坐卯受克，官位之格打折。男命庚年顺行：庚辰（伏吟起运按月柱顺排）辛巳、壬午、癸未、甲申、乙酉、丙戌、丁亥。峰值以甲申、乙酉运印星得地扶身为高。病位：水弱木旺，肝肾之疾。子女：时柱辛丑印官，子息守成。",0.55)
add("OC-015","甲木日主生巳月、食神生财，辛金正官透出合身，子水印星与辰土水库为根：官印财食流通之君命格。主继承大位、一国之君，中年登基在位长久，名位至极无可再升。然巳火炎、子水冲午（局中虽无午，运年逢之须防）水火交战，晚年健康以呼吸、肺系与寒热之疾为病，寿至七旬初而崩。格局量级：君主之格，上限即一国元首，依据为官星得禄于巳、印星护身、食财不破官。",
 BZ+"乙丑 辛巳 甲辰 甲子：甲木巳月失令，辛官透月、子印时透，辰为湿土培根，官印相生格成。男命乙年阴年逆行：庚辰、己卯、戊寅、丁丑、丙子、乙亥、甲戌。峰值以戊寅、丁丑运财官印相生段为高。病位：火土燥而水受冲克，肺与呼吸道、肾水之疾。子女：时柱甲子比印，子息承统有人。注：生庚据西报传略转译，精度有限，置信略降。",0.55)
add("OC-016","庚金日主生卯月、财星当令，两辛比肩、子水伤官、亥水食神：身弱财旺、伤官生财。主无祖荫厚财，不走仕途正路，以口才技艺、文书推算之业立身——即以命理为职业的一代名家，名满同业而财聚散无常，中年亥子水运伤官吐秀、名声最盛。晚年移居续业、著述授徒，寿至七旬末至八旬，晚景清贵不富、以名终。格局量级区间：下限职业术士—上限同业宗师，断至同业名家级，依据为伤官生财成链、比肩帮身仅够任财之一半，故名大于富。",
 BZ+"辛亥 辛卯 庚子 庚辰：庚金卯月财令，无申酉根，辰印半合子水反泄，扶身只靠两辛比肩虚浮——身弱财旺定格。男命辛年阴年逆行：庚寅、己丑、戊子、丁亥、丙戌、乙酉、甲申。峰值以戊子运印土扶身、子水吐秀为高。病位：金弱水旺，肺与肾、寒湿之疾。子女：时柱庚辰比印，子息平常。此为命师自造自批，断语按格直断不取其自誉。",0.57)
add("OC-017","丁火日主生酉月、财星当令，戌丑辰三土食伤生财，壬水正官透年、甲木正印透时救身：食神生财格成而有救应。主白手经营丝业成巨富，富甲一方（南浔丝商之首列），财帛量级为地方首富级；中年土金运食伤生财为高峰。晚年印官运守成，家业交子弟，富厚善终，寿至七旬以上。格局量级区间：下限富商—上限地方首富，断至首富级，依据为食伤生财成链、财星得酉令，印星时透护身不破格。",
 BZ+"壬戌 己酉 丁丑 甲辰：丁火酉月失令，己食透月生酉财，戌丑辰食伤成群生财太过，甲印透时、壬官透年为救应与名分。见《子平真诠评注》论用神成败救应章引例：用神（财）成格、救应（印）到位。男命壬年阳年顺行：庚戌、辛亥、壬子、癸丑、甲寅、乙卯。峰值以庚戌、辛亥运财食得地为高。病位：火弱金土旺，脾胃与心之疾。子女：时柱甲辰印坐食库，子息承业。",0.6)
add("OC-018","庚金日主生子月、伤官当令水冷金寒，丙火七杀透月为权，寅木财星与巳火杀根潜伏：伤官佩杀、才名与权势相激之格。主报业巨头、舆论领袖，地位崇高、影响政局，中年寅卯财运生杀、名位最盛。然伤官见杀、锋芒太露招强权之忌：晚运未及，约五旬中段有横祸之险——死于兵刃暗杀、非病终之命，名高而寿促。应期：年档，险年在火土杀旺之年（甲戌、乙亥之交，约1934年前后）为主坐标（定值）。",
 BZ+"己卯 丙子 庚寅 辛巳：庚金子月伤官旺，丙杀透干得巳根，辛劫合丙（合杀留情而亦绊），寅财生杀。男命己年阴年顺行：丁丑、戊寅、己卯、庚辰、辛巳、壬午、癸未。峰值在戊寅、己卯运财印交至、报业版图最盛之段。病位与祸位同源：病字为丙巳之火杀，落月时两柱，祸不在脏腑在外来兵刃——按（f）核对，承受对象与应验对象同为命主本人。子女：时柱辛巳劫杀，子息受其荫而难承其业。",0.58)
add("OC-019","壬水日主生辰月、申金印星长生有根，丙火财星透月，癸水劫财帮身：身旺任财、财官（辰中戊杀）潜藏之格。主学界政界显达，至研究院总干事、社会领袖级，中年火土运财官到位为高峰。然身旺无制、卯木伤官冲动（时支卯与运年酉金相冲之象），锋芒招忌：约四旬初即有横死之险，死于暗杀兵刃、非寿终。应期：年档，险年主坐标为癸酉年（1933）前后金水冲木之年（定值）。注：卡内已注明两书所载四柱全异、本例以徐乐吾《子平真诠评注》之造为准，版本分歧已在 basis 留痕。",
 BZ+"癸巳 丙辰 壬申 癸卯（以徐乐吾书为准）：壬水申印长生、辰库蓄水，身旺；丙财透月得巳根，财旺可任。男命癸年逆行：乙卯、甲寅、癸丑、壬子、辛亥、庚戌。青年乙卯、甲寅食伤运才名大著，运入癸丑、壬子比劫夺财兼冲动财星，名位虽在而祸机伏。病位/祸位：水旺木浮，祸从外来（杀藏辰中逢冲则发），承受与应验同为本人。子女：时柱癸卯劫伤，子息缘浅。",0.55)
add("OC-020","癸水日主生丑月、己土七杀当令，两丑杀库、丁火财星生杀，乙木食神透时制杀：食神制杀贵格成。主贵显至极，至国民政府主席、行政院长级一国元首之位，中年木火运食神得禄、制杀有力为高峰。然杀重身弱、制杀之食神坐卯受酉冲之险（运年逢酉须防），土杀攻身主寿不长：约五旬初病逝于任上，险年在庚午、辛未年（1930年前后）火土助杀之时。应期：年档，主坐标1930年前后（定值）。",
 BZ+"己卯 丁丑 癸丑 乙卯：癸水丑月杀令，己杀虽藏丑而两丑一己（月干己为土）杀势成群，乙食透时坐卯禄，制杀有力故贵；丁财透月生杀为病之一端。男命己年阴年顺行：戊寅、己卯、庚辰、辛巳、壬午、癸未。峰值运三核对：己卯运①用神乙木食神得卯禄得地②运干己为杀星非呼应用神、只半应③否决：①合绊用神未命中②冲克用神之根未命中③透忌神且通根——己土杀透而丑为其根，命中(iii)，故己卯为伪峰、资格取消；峰值顺延至庚辰运（食神仍有卯根、辰为水库扶身）称峰值。病位：土杀攻水，脾胃与肾、腹疾为终局之病。",0.58)
add("OC-021","乙木日主生酉月、辛金七杀透出当令，丙火伤官透时制杀，卯木禄根坐时：伤官制杀、杀旺有制之军阀格。主以武功起家，至督军、巡阅使、两广之主级贵显，一方之雄；中年木火运制杀得力为高峰。晚运水金杀势复旺而禄根被冲（卯酉冲贯穿全命），失势退居、兵权尽失，寿至六旬中段闲居而终。格局量级区间：下限高级将领—上限一方军阀首领，断至首领级，依据为制杀格成、禄根在时不早失。",
 BZ+"戊午 辛酉 乙卯 丙戌：乙木酉月杀令，辛杀透月，丙伤透时坐戌火库制杀，午火助制，卯禄被酉冲为全命之病——位高而根基终受冲。男命戊年阳年顺行：壬戌、癸亥、甲子、乙丑、丙寅、丁卯、戊辰。峰值以丙寅运伤官得禄、寅午戌火局制杀为高；癸亥、甲子水运印化杀亦显但带迁动。病位：金木交战，肝胆与筋骨、肺之疾。子女：时柱丙戌伤官坐财库，子息难承兵业。",0.57)
add("OC-022","乙木日主生酉月、丁火食神透月制辛金七杀（杀藏酉中），寅木禄根在时，戊土财星生杀为病得丁火食神与寅木疏土救应：食神制杀格。科第之路断：杀旺食制主以技艺学问立身而非功名——屡试不第后专攻命理医卜，成一代命学名家，著述授徒、名满天下士流。中晚年木火运食神得禄为高峰，晚年著述不辍，寿至八旬以上善终。格局量级区间：功名下限为无第、学业上限为同业宗师，断至宗师级，依据为食神制杀成格而官星（正官不现）无缘科甲。",
 BZ+"辛巳 丁酉 乙巳 戊寅（袁树珊自造）：乙木酉月杀令，丁食透月得巳根制杀，寅禄在时，戊财透时生杀被寅木截脚。男命辛年阴年逆行，卡内注大运丙申起：丙申、乙未、甲午、癸巳、壬辰、辛卯、庚寅、己丑。峰值以甲午运食神得午禄、木火通明为高。病位：金木战于肝肺，年老以肺与筋骨之疾收。子女：时柱戊寅财坐禄，子息承其学业家声。",0.6)
# OC meihua / liuren
add("OC-023","所覆之物为一件破损的金属/陶质器物——具体断为：一只旧的铜（金属）质或陶质的圆形容器类器物（如旧铜器/破碗盏之类），且已破损不全、有缺口。依据收束：鼎卦象为铸器之器，物类属器皿无疑；其不完好——断为破损缺口之器，开钟验看当见其残破。置信受限：卡内未给起卦时间与动爻，体用旺衰无从细核，物性（金属/陶质）两读并存，取金属为主、陶质为副。",
 "体系：梅花易数射覆（据输入卡自带卦象作断）\n卦象：火风鼎 变 雷风恒。鼎为铸器、烹饪之器，上下皆象器皿：上离为中虚、外实之器形，下巽为入、为长形。变恒主其物久置、旧物。按（g）具体断语密度：已落到物品（器皿）与状态（破损有缺口）两项；动爻与起卦时辰卡内未载，体用主客无从判定，故质地两读并列、置信下调，此为输入残损如实注明。",0.4)
add("OC-024","葬资有着落，不必外求：易者生前已自备窖藏——其枕中/卧处藏有金银，另因鼠患点破：有人击鼠（或鼠咬枕）而枕中藏金现形，此金正足营葬。断语落点：财物为枕内藏金（物品明确），得财方式为击鼠见金、就地取于其卧榻之侧，不待亲友筹措，丧事可办。应期：日档，来访后数日内检枕即得（窗口三日内，主坐标来访次日，定值）。",
 "体系：梅花易数旧案（据输入卡情境与出处条目作断）\n出处条目标题即含「击鼠枕窖金」之目：象意为藏金于枕、因鼠显形。按事实优先序：其家苦无资营葬，而易者遗书敢预言托付来访秀士，必自备后手——藏金在其卧处。按（c）（g）：断语落到物品（枕中金）与事件（击鼠见金）两项。卡内未附卦象原文，卦理一层无据不补，置信据此下调。",0.5)
add("OC-025","断为应验。届预书之年月日，椅子将被坐破——坐者为来访之客（或家中子弟）不意坐下、椅腿/椅面应声而坏，人无大伤而椅毁，正合椅底预书。应期：即预书所写之日（卡内未载具体日期，以预书日期为唯一坐标，属回溯/预定日期型，定值在彼日）。此象为小事精验之类：验在器物（椅）不在人身，按（f）应验对象为椅本身，不回收到坐者之灾。",
 "体系：梅花易数旧案（据输入卡情境与出处条目作断）\n出处条目「置椅坐破」即以椅底预书届期坐破为案眼。邵雍预言之体例为先书后验、本案问的正是「是否应验」，按其断例收束为验。卡内未载预书日期与卦象，日期坐标只能回指预书本身、卦理层无据不补，置信下调。",0.5)
add("OC-026","今年功名可成。课得涉害、曲直，三传乙未（青龙）、己亥（螣蛇）、癸卯（玄武）构成亥卯未三合木局、曲直成格，木气专旺向日：功名文书之象成局，主两客中有人（或两人先后）于今年科名得中、榜上有名，纵有涉害之难（竞争、关节阻滞）终能突破。应期：年档，今年放榜之期（秋闱/来年春榜按其科别），主坐标为木旺之春令放榜时（窗口）。功名等级：中式举人/进士之列，非状元鼎甲之格（木局成而火不显，文光不耀至极）。",
 "体系：大六壬（据输入卡自带课式、三传、月将作断）\n1643年正月初四己亥日辛未时，丑将，甲午旬辰巳空。三传未亥卯逆行成三合木局，曲直格主仁主文；初传青龙主喜庆文书，中传螣蛇主虚惊缠绕，末传玄武主暗昧关节——过程有暗阻而结局归木局之成。空亡在辰巳，不空三传，功名类神（朱雀文书虽未乘传，以曲直木局生日干己土之官星丁火论）有气。盘面只有课式、三传、月将与空亡，天盘全图与四课全列卡内未给，按盘面不全守则只据已给作断、不臆补。",0.55)
add("OC-027","此行不得意。课名无禄、无路已定主向：奉诏北上正值北方兵事紧迫，初传癸酉（六合）似有聚合之机，中传戊辰（太阴）主暗昧退藏，末传亥（青龙）落甲子旬空亡——禄路俱断、青龙入空，主入京不得显用、事多掣肘，终须南还/退归。身体：辰土乘阴克日，脾胃与劳顿之疾可忧而无大凶；老母（甲子年生）：母年命与旬空相应，亥为空——主占时牵挂而暂无大故，然行后家中消息迟滞、虚惊一场。应期：月档，北行后一至三月内见阻而定期南还（窗口，主坐标约两月内）。一段终局之外，远段（还乡后复起）盘面无传可指，明言远段无据不报。",
 "体系：大六壬（据输入卡自带课式、三传、月将作断）\n1642年冬月初五辛未日甲午时，丑将，甲子旬戌亥空。课式无禄、无路为凶格主名；三传酉辰亥，末传亥空、青龙乘空，禄马无根。日干辛金为占者本人，辰土生金尚有护身之气，故身体只主劳疾不主大凶；老母甲子年命，子与旬首相应而亥空，只断虚惊不作凶亡（无传直克年命）。盘面不全（无天盘全图、四课全列），按守则只据干支、三传、天将、课格、空亡作断。",0.55)
add("OC-028","入觐考选可得官，且为带文书、诏命色彩之官。课得重审、斫轮，三传辛卯（玄武）、丙戌（朱雀）、癸巳（白虎）：朱雀乘传居中主文书诏命发动，斫轮主雕琢成器、改授新职——断得官成立，品级为中层京官/道府之列，非骤至显要；过程有玄武初传主暗耗迟滞、白虎末传主到任后辛劳道路之苦。应期：月档，入觐后数月内除授，主坐标在巳火得令之夏令前（窗口）。官职性质偏文诰、铨选一路（朱雀所主），非武职。",
 "体系：大六壬（据输入卡自带课式、三传、月将作断）\n1630年冬月十四己丑日辛未时，寅将，甲申旬午未空（空在午未，不碍三传）。日干己土为占者，官星甲乙木：三传卯木为官星乘玄武居初——官先以暗昧迟滞之象来；戌为华盖朱雀主诏文；巳白虎为道路驿马之劳。斫轮课主旧材新琢、改任成器，与考选改授相应。盘面不全，按守则只据已给课式、三传、天将、空亡作断，不臆补四课天盘。",0.55)
add("OC-029","诸事分断：一、携子求官：可成而迟——三传乙未（白虎）、癸卯（六合）、己亥（天后）成亥卯未三合木局，官星木气成局生日干，子（丑命）随行得官之象在局内，主父子此行得人提携、子之官事可成，然白虎初传主道路阻滞与先难后成，须经一番周折。二、老母寿事：母年近九十、家在山东，末传天后乘亥主母、归本日支亥位——母体暂安、寿诞可过，但三合局全动、亥水冲巳（占时外）之象提示来年火旺之年须防母病，一段之内只断今冬安泰，远段母寿无传直指、无据不深断。三、访道求谒：六合中传主和合，谒见可成、得善遇。应期：月档，求官成于木气得令之春令（窗口，主坐标次年二三月）。",
 "体系：大六壬（据输入卡自带课式、三传、月将作断）\n1642年十月初二己亥日辛未时，丑将，甲午旬辰巳空。课式涉害、曲直、回环：三传未卯亥三合木局，日干己土之官星为甲乙木，木局即官局，曲直主成；其子丑命，丑为局外土、随局受生（木局生……土受木克而为官管之象，主以子得职）。母象取天后乘末传亥、与日支同位，主安。空亡辰巳不落三传。盘面不全（无天盘全图、四课、母之年命只知近九十），母寿远段守则不臆断。",0.52)
add("OC-030","两问分断：一、淮扬巡按差可复——课得铸印，印绶铸成之象即官署复设之征，三传癸巳（太常）、丙戌（六合）、辛卯（太阴），巳火为印星（火生己土日干之印……以戊子日论，火为印）乘太常居初传，印气发动、六合中传主和合成事：巡按差将于此后复设成立。二、吏书缺可照旧——末传卯木官星乘太阴，官位暗存不废，吏书之缺照旧保留、原人可留或缺不裁革。应期：月档，复设之命下于火土得令之季（窗口，主坐标约半年内夏秋之交）。两事皆成，唯太阴、太常主迟缓暗办，非雷厉风行之复。",
 "体系：大六壬（据输入卡自带课式、三传、月将作断）\n1651年二月初十戊子日戊午时，亥将。课式重审、铸印：铸印为本案眼——印成则署立。日干戊土，火为印星：初传巳火乘太常（主印绶、公署）发用，中传戌土六合助成，末传卯木为官乘太阴主官缺暗保。代占官缺以日干为问者、日支为所问之署缺合看，印官两全故双成。卡内未给空亡与四课天盘，按盘面不全守则只据课式、三传、天将作断。",0.55)
# WP
add("WP-001","Yes — a major collective affliction in 2020–2021, of pandemic kind. With Jupiter–Saturn–Pluto conjunct in Capricorn in early 2020, the five outer planets compressed within ~100° and the cyclical index at its century low, the period holds a worldwide epidemic disease event: a fast-spreading respiratory-type plague causing mass illness, deaths, lockdown of collective life and economic shock, peaking in 2020 and extending through 2021. Timing: year-scale; window opens early 2020 at the exact conjunction, main coordinate the first half of 2020.",
 "tradition: Western mundane astrology (per input card's configuration)\nThe card's configuration — great conjunction in an earth sign tied to structures, outer-planet compression, cyclical-index minimum, with past clusters coinciding with 1918 (influenza pandemic), 1954, 1968 (flu), 1982 — points by the master's own cited precedents to epidemic affliction rather than war or finance alone. Affliction specified to event level: epidemic disease, global spread, 2020–2021 window. No natal data; mundane configuration only, as given.",0.6)
add("WP-002","Barack Obama wins the 2008 US presidential election. Saturn opposite Uranus exact on Election Day (4 November 2008) — the 'change' configuration last seen 45 years earlier — breaks for the insurgent/change candidate over the establishment figure; Obama first defeats Clinton for the nomination, then defeats John McCain in the general election. Timing: day-scale, decided 4 November 2008 (fixed value).",
 "tradition: Western mundane/election astrology (per input card)\nCard facts: Obama leads but has not clinched; McCain is the presumptive Republican; Saturn–Uranus opposition begins on Election Day, a configuration associated with upheaval and overturning incumbents/orders. The change signature attaches to Obama (the change-branded candidate) rather than to McCain. No candidate natal charts are given in the card, so the call rests on the mundane configuration plus card facts — confidence set accordingly.",0.58)
add("WP-003","Barack Obama is re-elected, defeating Mitt Romney on 6 November 2012. Mercury turning retrograde on election day signals a repeat/return of the existing state of affairs rather than a change of administration — the incumbent stays. The race looks competitive in polling but the result holds for Obama. Timing: day-scale, 6 November 2012 (fixed value).",
 "tradition: Western mundane/election astrology (per input card)\nCard facts: incumbent president running for re-election, competitive polls, Mercury retrograde beginning on election day. In election-astrology convention Mercury retrograde on the day favours the status quo/incumbent and muddles the challenger's surge. No natal charts given; call rests on incumbency plus the election-day configuration stated in the card.",0.55)
add("WP-004","The conference panel's call: Hillary Clinton wins the 2016 US presidential election, defeating Donald Trump on 8 November 2016. The panel majority at the Costa Mesa ISAR conference reads the charts for the experienced, establishment candidate — Clinton — despite Trump's insurgent campaign. Timing: day-scale, 8 November 2016 (fixed value).",
 "tradition: Western mundane/election astrology — conference panel prediction (per input card)\nCard facts: most polls favour Clinton; an international astrology conference panel is forecasting the race. Panel-consensus readings of this kind follow poll-consistent, establishment-favouring chart readings; the prediction recorded here is the panel's majority call (Clinton), stated as the master prediction this case samples. No individual charts are given in the card; confidence reflects the panel-consensus basis only.",0.5)
add("WP-005","Donald Trump wins the 2016 US presidential election. The astrologer who alone picked Trump — back when 17 Republicans still contested — to take the Republican nomination follows the same chart logic through to November: the outsider breaks the establishment candidate, and Trump defeats Hillary Clinton on 8 November 2016 despite polls favouring her. Timing: day-scale, 8 November 2016 (fixed value).",
 "tradition: Western mundane/election astrology — individual panel astrologer's prediction (per input card)\nThis card is distinguished from the panel-consensus case by one fact: a panel astrologer had earlier, against the whole field, correctly picked Trump as the Republican nominee. That demonstrated contrarian read of Trump's chart is the master signal sampled here; extending it, the same reader calls the general election for Trump. Basis rests on that distinguishing card fact, hence moderate confidence.",0.52)
add("WP-006","Yes — Britain votes to Leave. The referendum of 23 June 2016 returns a Leave majority, against the February polls showing 'Stay' ahead with many undecideds. Uranus conjunct Ceres at 23° Aries on referendum day — a disruption/eruption signature on the UK charts (1066/1801/1922) — breaks the undecided bloc toward rupture rather than continuity. Timing: day-scale, 23 June 2016 (fixed value); the call was firmable in advance (first published July 2015, firmed February 2016).",
 "tradition: Western mundane astrology (per input card — Jessica Adams's published assessment)\nCard facts: polls favour Stay but with vast 'not sure' numbers; UK national charts available; Uranus–Ceres conjunction at 23° Aries on the day. Uranus on referendum day signifies sudden break with the status quo; a large undecided bloc under a Uranus signature resolves as a shock result, not a safe one. The astrologer's long-lead published stance (from July 2015) is read as a settled Leave call.",0.58)
add("WP-007","Donald Trump wins — and what decides it is Hillary Clinton's scandals. The Union Square tarot reading of August 2016 points to the email controversy and the Clinton Foundation questions corroding Clinton's position through the autumn: the deciding factor is not Trump's strength but the trust collapse around Clinton, tipping late-deciding voters. Trump defeats Clinton on 8 November 2016. Timing: day-scale, election day 8 November 2016 (fixed value).",
 "tradition: Western tarot (per input card — a Manhattan tarot reader's drawn reading)\nCard facts: Clinton leads in August polls; the reader draws on the election in August 2016; the email controversy and Clinton Foundation are already public. The case question itself asks 'who, and what will decide it' — the sampled master reading names Trump and assigns the deciding role to Clinton's controversies. The card does not reproduce the actual cards drawn, so no card-by-card Waite exegesis is possible; that input gap is noted and confidence set at moderate-low.",0.48)

ids = ["MP-017","MP-018","MP-019"]+[f"OC-{i:03d}" for i in range(1,31)]+[f"WP-{i:03d}" for i in range(1,8)]
assert set(ids)==set(P), (set(ids)^set(P))
for cid in ids:
    (OUT/f"{cid}.json").write_text(json.dumps(P[cid], ensure_ascii=False, indent=1), encoding="utf-8")
files = [c for c in ids if (OUT/f"{c}.json").exists()]
assert len(files)==len(ids)==40, len(files)
print("written", len(files))
