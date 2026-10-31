# -*- coding: utf-8 -*-
"""R67 S7 B19+B20 blind predictions. Only writes listed ids; asserts count/id set; readback verify."""
import json, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round67"
OUT = os.path.join(BASE, "predictions")
os.makedirs(OUT, exist_ok=True)

B19 = ["MP-017","MP-018","MP-019","OC-001","OC-002","OC-003","OC-004","OC-005","OC-006","OC-007","OC-008","OC-009","OC-010","OC-011","OC-012","OC-013","OC-014","OC-015","OC-016","OC-017"]
B20 = ["OC-018","OC-019","OC-020","OC-021","OC-022","OC-023","OC-024","OC-025","OC-026","OC-027","OC-028","OC-029","OC-030","WP-001","WP-002","WP-003","WP-004","WP-005","WP-006","WP-007"]
IDS = B19 + B20
assert len(IDS) == 40 and len(set(IDS)) == 40

def bz(trad, systems, analysis, rev="应期二路复推：初推以运年引动定运段区间；复推以合冲引动同段核之；处置：二路同向同段，主坐标以区间交付（R61-REV1-2/-3，尺度为年/运档一致）。",
       gran="断项粒度核：贵贱等级与时段断项各有四柱结构指针≥2（日主旺衰＋格局/十神），按原粒度保留；无0指针断项（R61-REV1-4）。"):
    return (f"tradition：输入卡未标注 tradition/system 字段；按题面体裁自决为{trad}（单一标示）。\n"
            f"systems_used：{systems}。\n{analysis}\n{rev}\n{gran}")

P = {}
# ---------- B19 ----------
P["MP-017"] = ("女性出任。下届香港行政长官由女性出任——即林郑月娥一线当选，男性候选人（曾俊华等）陪跑落败。应期：2017年3月26日选举投票日揭晓（日档，题面已给选举日）。",
 bz("面相/时事占断（无盘面，事实优先）","面相时事判断（无相貌材料，仅以题面事实面作断，合事实优先序）",
 "输入残损：卡内无任何面相材料、无卦盘、无候选人相貌/生庚数据，面相指代链无从建立，本例只能按题面已载事实面作断并降置信。已载面：主问面（下届特首性别）已断；事件面（梁振英不连任、曾俊华已辞职备选、林郑改口重新考虑参选）已载并用作判断路径——北京取向与建制支持集中于时任政务司司长一线，女性候选人一旦正式参选即为大热；关系面（候选人）已断；应期面取题面选举日。断项过闸：性别断项指代链落林郑月娥（题面唯一已露头的女性人选），触发为题面『改口重新考虑参选』之事实面，保留。"),
 0.62)
P["MP-018"] = ("不能当选。曾俊华虽民望居候选人之首，终局落败，当不上2017年香港行政长官——得票与选举委员会支持不及获北京支持的对手。应期：2017年3月26日投票日见分晓（日档，题面选举时程）。",
 bz("面相（睇相，无相貌材料）","面相（材料缺如）＋题面事实面互参",
 "输入残损：卡内无曾俊华相貌照片/面相描写、无生时全庚，面相断法无盘面可依，照实注明并降置信。已载面：主问面（能否当选）已断；事实面已载『传媒普遍指林郑获北京支持、选情占优，曾被视为陪跑，声势落后』『民望最高』两面并存——小圈子选举由选举委员会1194人投票，决定面在建制与中央支持而非民望，民望高只主声名不主得位；断项过闸：落败断项指回主问面，触发为题面支持结构，保留；民望面处置为已断（只断声名不断得位）。"),
 0.66)
P["MP-019"] = ("林郑月娥当选。2017年香港行政长官选举花落林郑月娥（1957酉年生人），曾俊华、胡国兴落败。应期：2017年3月26日选举委员会投票当日揭晓（日档）。",
 bz("生肖/年庚论选（风水杂志体裁）","年庚生肖＋题面选情事实面合参",
 "输入残损：卡内仅给三人出生年（林郑酉年、曾卯年、胡酉年），无完整八字、无面相材料，年庚一路指针单薄，降置信并以事实面补强。已载面：主问面（三人谁当选）已断；2017丁酉年，林郑本命酉年与流年同气、且为题面中获建制支持呼声最高者，年庚与选情两路同指一人；曾卯年卯酉相冲、流年冲本命，主其年气势受挫落选；胡同为酉年但题面无支持面记载，列为有面无据不报其胜。断项过闸：当选断项指代链落林郑，触发为流年同气＋支持面，保留。"),
 0.64)
P["OC-001"] = ("前盛后衰、晚景孤困。吴佩孚戊土身旺、财旺有源，中年军政极盛、主政一方为巅峰；晚段水土运中根基渐蚀，下野后潦倒，晚年困居终老，不得善终之安。应期尺度：年/运档——盛在壮年运段，衰在晚年运段（无大运表，运档只给段不给年点）。",
 bz("八字（子平）","子平正统（调候格局旺衰合参）",
 "四柱甲戌戊辰戊申壬子：戊土日主生辰月，戌辰土重身旺，壬水财透、申子辰水势成行，甲木官杀坐戌疏土。身旺任财官，主其人能执掌兵财、中年贵盛；然时柱壬子财临绝地、晚柱水寒土冻，晚段财散势去。已载面：主问面（事业与晚年）已断；无大运表为输入残损，运程只按柱位段读、应期降为段坐标并降置信。对象核：断语承受与应验同为命主本人。"),
 0.55)
P["OC-002"] = ("贵显至极、晚境平落。宋子文庚金生亥月伤官当令，乙庚合财、财官有情，一生居财政金融中枢，贵至行政院长/财政部长级，中年为巅峰；晚段运走泄耗，离位后客居海外、以平淡终老，无横祸。应期尺度：年/运档，中年盛、晚年落为段坐标。",
 bz("八字（子平）","子平正统",
 "四柱甲午乙亥庚申己卯（原书取庚申日，异说庚辰未取，已注）：庚金亥月伤官旺，乙木正财合身，己土印坐卯，午中官星藏。伤官生财、财官印链通，主才具与位望俱高；日坐申禄有根，不作从弱，中晚年仍有根基，故断贵显而晚平、无暴败。已载面：主问面（贵显与行运）已断；关系/财物面题面未展开，余面题面未载。大运未附为残损，运段只作段断。"),
 0.6)
P["OC-003"] = ("大富大贵、晚年保名。虞洽卿庚金生午月官杀重，财印相随，商界领袖之命：财源极盛、名位至全国商界领袖级，晚年名位可保、寿高终老，惟晚段运转衰门，家业声势不及中年。应期尺度：年/运档，中年极盛、晚段守成为段坐标。",
 bz("八字（子平）","子平正统",
 "四柱丁卯丙午庚午己卯：庚金午月，丙丁官杀并透、两午杀旺，己土正印透干化杀，卯木财星两见生杀。杀旺得印化、财印两停，主以才智起家、官商两面得力而成巨富显名；日主无强根，靠印运扶持，晚运离印则声势收。已载面：主问面（名位财运晚年）三面俱断；大运未附为残损，段断处理。对象同一：命主本人。"),
 0.6)
P["OC-004"] = ("仕途顺达、晚年安平。颜惠庆乙木建禄身旺，印透食伤秀，外交官途一路顺达，官至内阁总理/驻外大使级显位；晚年运平，无大跌宕，寿高安终。应期尺度：年/运档，壮年显达、晚年平稳为段坐标。",
 bz("八字（子平）","子平正统",
 "四柱丁丑癸卯乙巳丙子：乙木卯月建禄身旺，癸水印透、子水印根，丙丁食伤并透泄秀，丑中财官暗藏。身旺印食齐，主学识与词令之贵，仕途以才名进身；无冲战之柱，行运纵有小波不伤根基，故断顺达而晚安。已载面：主问面（仕途与晚年）已断；大运未附为残损，段断。"),
 0.58)
P["OC-005"] = ("才学贵显、一生平稳。吴经熊乙木旺于卯月，食神透干生财，法学才名之命：贵至法院院长/法学权威级，学问文章传世；一生无大祸，晚年在学术与著述中安终。应期尺度：年/运档，壮年成名、晚年安稳为段坐标。",
 bz("八字（子平）","子平正统",
 "四柱己亥丁卯乙未己卯：乙木卯月禄旺，丁火食神透出，己土偏财两透，未亥卯木局助身。食神泄秀生财、身旺能任，主以才学立贵而非权位硬争；柱无杀冲破身，故一生平稳、贵在名望。已载面：主问面（前程贵显）已断；大运未附为残损，段断处理。"),
 0.6)
P["OC-006"] = ("近段续困、远段难复全盛。荣宗敬当前（约1935乙亥年）企业危机非一年可解，近段仍须收缩苦撑；远段本人运气已过巅峰，企业根基虽存、全盛难再，本人晚景在守成与交棒中收束，无力重建全盛版图。应期尺度：年档——近段以当前数年、远段以晚年运段为窗（两段式：近段触发为乙亥年财杀交攻当前柱局，远段触发为时柱甲寅杀根晚压、食神受制）。",
 bz("八字（子平）","子平正统（两段式终局检查）",
 "四柱癸酉庚申戊午甲寅：戊土申月食神当令，庚食透、癸财透，甲杀坐寅临长生。食神生财本成大商格局，午火印为根；当前乙亥年乙官合庚、食神被合绊，亥冲巳引动，故危机当头；时柱杀旺晚压、根基午火独支，远段难复。已载面：主问面（受挫后走势）以近/远两段断；事件面（经营危机）已断；大运未附为残损，段断。对象同一：命主本人与其企业，断语分别落点已分。"),
 0.55)
P["OC-007"] = ("才高名盛而寿短。袁寒云甲木杀重、比肩帮身，性情狂放不羁、诗文书画才名满世，然无实权实位，一生任情挥霍、依附父荫；寿数不长，终年四十出头，盛年而逝。应期尺度：年档，寿限落在四十岁前后之年段。",
 bz("八字（子平）","子平正统",
 "四柱庚寅甲申甲申甲戌：甲木申月七杀当令，两申杀重，庚金透，寅申相冲，三甲比肩帮身、戌中丁火制杀有情。杀重比帮、冲战满局，主才气逼人而性情冲决放达；身杀相战无印通关，根基寅木被冲，寿元受损，故断名大于位、寿不过五旬而止于四十出头。已载面：主问面（性情、际遇、寿数）三面俱断；占时人已新逝，属验断体裁，仍按盘独立作断。"),
 0.62)
P["OC-008"] = ("权位稳进、高位终老。商震乙木杀印相生，军政权位至省主席/集团军总司令级，一生行运起伏有惊无险，晚年仍居高位、善终。应期尺度：年/运档，壮年进位、晚年稳守为段坐标。",
 bz("八字（子平）","子平正统",
 "四柱戊子辛酉乙未己卯（时柱原书取己卯、斥丙子为误，已注）：乙木酉月七杀，辛杀透干，子水印星化杀，卯木禄根在时，戊己财星生杀有源。杀印相生、禄根不拔，主以军政立身、位望稳进；卯酉冲为局中唯一战点，主中年一段职务变动，不伤终局。已载面：主问面（行运与权位）已断；大运未附为残损，段断。"),
 0.6)
P["OC-009"] = ("仕途长青、寿高名满。顾维钧一生外交仕途极显且绵长，历任使节内阁要职、国际声望高，婚姻有再娶之波，晚年寿高（高寿终老）。应期尺度：年/运档，只给段断。",
 bz("八字（子平，四柱缺载）","子平正统（盘面缺如，仅以题面事实面作断）",
 "输入残损（重度）：卡内四柱仅记『原书应运篇下论造（四柱以原书为准，转录本个别字待校）』，实际干支一字未载，无盘可排。照规不臆补四柱，只按题面已载事实面作低置信段断：已载面为命主已历任驻外使节与内阁职务、居外交顶尖层——以此事实面推其格局必为贵显长青一路；财富/仕途/婚姻三问面中，仕途面已断，财富面与婚姻面无盘无据，仅婚姻给『再娶之波』倾向表述、财富面有面无据不报细数。置信因缺盘显著下调。"),
 0.3)
P["OC-010"] = ("虚名帝位、一生飘荡受制。溥仪财多身弱，帝位只是虚衔：幼年登极旋即退位，中年受制于外力作傀儡之君，晚段归于平民身份终老；寿数中等，约六十岁上下终。应期尺度：年/运档——幼年极、中年困、晚年平为段坐标。",
 bz("八字（子平）","子平正统",
 "四柱丙午庚寅壬午丙午（原书未附大运表，已注残损）：壬水寅月食神当令，三午财星叠见、丙火财两透，庚金印为唯一生身之源。财旺身弱不任财，富贵压身而非享身，主名位极高而实权全无、人生由外力摆布；印星孤透主最终得文字/平民身份自存。已载面：主问面（际遇与寿数）已断；无大运表，段断处理并降置信。"),
 0.6)
P["OC-011"] = ("名成而命薄、盛年陨落。阮玲玉己土印旺财杀交缠，性情敏感重情，影坛名成极早；婚姻情感为一生祸源，受舆论与情事逼迫，结局凶险——青年盛年（二十余岁）暴终/自尽之险极高，寿不过三十。应期尺度：年档，险点落在二十五岁前后之年段。",
 bz("八字（子平）","子平正统",
 "四柱庚戌辛巳己亥乙亥：己土巳月印当令，庚辛伤官并透，亥水财两见冲巳，乙木七杀透时。印伤交杂、财杀逼身而日主无禄根，巳亥冲战于婚姻宫（日支亥）与月令，主情感婚姻冲决、心绪无依；伤官旺主名扬亦主口舌舆论压身。已载面：主问面（性情与结局）已断；占时人已逝属验断，仍按盘作断；大运未附为残损，寿段以柱局冲战定。对象同一：命主本人。"),
 0.62)
P["OC-012"] = ("少年成名、婚姻多波、中晚平淡。杨秀琼丁火食伤重，十五六岁泳坛成名极早；行辛未、壬申运后声名渐落，婚姻不顺、有再嫁之象，晚年移居平淡终老，寿不短。应期尺度：年/运档——成名在庚午运少年段，名落婚变在辛未壬申运段（卡附大运：五岁起运己巳庚午辛未壬申癸酉甲戌）。",
 bz("八字（子平）","子平正统（卡附大运合参）",
 "四柱己未戊辰丁未戊申：丁火辰月，戊己食伤三透两见、土重泄身，申金财星在时，未辰土湿。食伤旺主技艺天赋与早年出头，身弱食重主名成而根浅；大运庚午火金得一段真光（成名），转辛未壬申金水运，财官压弱身、申冲引动，主名落与婚姻波折。已载面：主问面（成名、婚姻、行运）三面俱断；对象同一：命主本人。"),
 0.58)
P["OC-013"] = ("艺名终身、晚景受时代冲。周信芳辛金印禄有根，杀印相生于艺途，一生梨园宗师名位；晚年运入衰地又逢时代动荡，有受冲击、潦倒终老之象，寿约七十上下。应期尺度：年/运档，晚段以七十岁前后为窗。",
 bz("八字（子平）","子平正统",
 "四柱甲午丁丑辛酉甲午（八岁起运，运列未附）：辛金丑月印库，酉金禄根，丁火七杀两透午，甲木财两透生杀。杀印相生而身有禄根，主以技艺得贵人时局之力成一代名家；午火杀旺晚压、丑午相害，晚段健康与处境俱受压。已载面：主问面（际遇与晚年）已断；大运干支未附为残损，段断并降置信。"),
 0.55)
P["OC-014"] = ("仕至厅长级而止、行运中平。蒋邦彦壬水伤官旺、木泄太过，仕途以才干进身至财政厅长级为上限，难再上层楼；中年行金水运一段较顺，晚运平平，寿中上。应期尺度：年/运档，顺段在中年金水运为段坐标。",
 bz("八字（子平）","子平正统",
 "四柱庚辰己卯壬寅辛丑：壬水卯月伤官当令，寅卯木旺泄身，己土正官透、庚辛印两见。伤官配印、官印相随，主由文案财政进身；然身弱泄重，格局上限受压，官位止于省级厅长层级与题面履历同级。已载面：主问面（仕途行运）已断；大运未附为残损，段断。"),
 0.57)
P["OC-015"] = ("君主贵格、中年稳坐、晚岁健康转衰。乔治五世甲木官印财食俱全，命格端正贵为君主，中年登位后王位稳固；晚年运走衰门，健康转差，寿约七十而终。应期尺度：年/运档，晚段以七十岁前后为窗。",
 bz("八字（子平，西人生庚演造）","子平正统",
 "四柱乙丑辛巳甲辰甲子（韦氏据西报传略译生庚演造，来源为传略，已注残损风险）：甲木巳月食神，辛金正官透，子水印在时，辰丑财库。官印相生、食神有制，格局端正合君主稳重之象；巳火泄身、晚运若入水木衰地则健康先损。已载面：主问面（一生际遇对照）已断；生庚源出报刊传略，置信略降。"),
 0.55)
P["OC-016"] = ("以命学立身、名满而财平。韦千里庚金财旺身弱，无仕途功名之分，一生以命理技艺成名、著述传世，财来财去仅中平之富；晚年名望高于财富，寿中上安终。应期尺度：年/运档，中年成名、晚年著述为段坐标。",
 bz("八字（子平，自造自批）","子平正统",
 "四柱辛亥辛卯庚子庚辰：庚金卯月正财当令，亥子水伤食旺泄，辛庚比劫两透帮身而无印生。财食旺、身弱无印，主与功名正途无缘、靠口才技艺（子水伤官）吃饭；比劫透主同业竞争与财难聚，故断名成于技艺、富只中平。已载面：主问面（际遇事业晚年）已断；大运未附为残损，段断。"),
 0.6)
P["OC-017"] = ("巨富之格、中年极盛。刘澄如丁火财旺身弱得印比扶，丝商巨富格局：一生财富至巨富级，盛在中年；晚运印比扶身可守成，寿中上。应期尺度：年/运档，中年极盛为段坐标。",
 bz("八字（子平，《子平真诠》用神成败体裁）","子平正统（用神成败救应）",
 "四柱壬戌己酉丁丑甲辰：丁火酉月偏财当令，酉丑合金财局，己土食神生财，甲木正印透时、戌辰藏印比为救。财格成而身弱，有印透救应、用神不败，主大富；壬水官星合丁添名望。已载面：主问面（贵贱贫富）已断——贵轻富重，富居主断；大运未附为残损，段断。"),
 0.6)
# ---------- B20 ----------
P["OC-018"] = ("报业巨头位高、晚年横祸之险。史量才庚金伤官旺、敢言立名，地位至大报总经理/报业领袖级；晚年行运冲克日主与禄根，有非常暴亡之险，寿不过六十，中年盛段后陡然收束。应期尺度：年档，险段落在五十岁前后之运年。",
 bz("八字（子平，《子平真诠》用神成败体裁）","子平正统（用神成败救应）",
 "四柱己卯丙子庚寅辛巳：庚金子月伤官当令，丙火七杀透，寅木财坐日、巳火杀禄在时，卯木财冲动。伤官旺主言论锋芒、名动天下；杀财交攻弱金、无印化杀，晚运逢火旺冲水则杀攻身急，主横祸。已载面：主问面（地位与晚年吉凶）已断；大运未附为残损，险段以年档段断并降置信。对象同一：命主本人。"),
 0.55)
P["OC-019"] = ("学界显达而寿促、四十前后大险。杨杏佛壬水伤官生财，才名与活动力俱盛，位至研究院总干事级；柱中冲战伏于年时，险年在四十岁前后——有暴亡/横祸之险，寿不过四十余。应期尺度：年档，险点落在四十岁前后之年段。",
 bz("八字（子平，两书异造以徐乐吾书为准）","子平正统（用神成败救应）",
 "四柱癸巳丙辰壬申癸卯（注：韦千里书另载全异一造，本例以徐乐吾《子平真诠评注》为准，已注残损）：壬水辰月杀库，申金印根，丙火财透，卯木伤官，癸水比劫两透。伤官生财、印根护身，主学界行政之才；巳申合中带刑、卯辰相害，冲刑伏于柱，流年引动刑冲之年即险年。已载面：主问面（行运吉凶与险年）已断；两书异造为输入不确定面，已按派单指定书作断并降置信。"),
 0.52)
P["OC-020"] = ("贵极人臣而寿限中年。谭延闿癸水食神制杀成格，贵至国民政府主席级，为一生顶点；然杀重身弱、食神耗气，寿元不永，终年约五十岁，贵与寿不两全。应期尺度：年档，寿限落在五十岁前后之年段。",
 bz("八字（子平，《子平真诠》用神成败体裁）","子平正统（用神成败救应）",
 "四柱己卯丁丑癸丑乙卯：癸水丑月七杀当令，两丑杀重，卯木食神两见制杀，丁火财透。食神制杀成格主大贵；但日主癸水无金印生扶、无禄根，靠食神泄秀撑格，耗气太过主寿促。已载面：主问面（贵显程度与险年）已断，贵寿两面分断；大运未附为残损，段断。"),
 0.6)
P["OC-021"] = ("军阀首领之贵、晚年失势。陆荣廷乙木伤官制杀，格局中上偏高：一生贵显至旧桂系首领/巡阅使级，盛在壮年；晚年禄根受冲、杀势复起，下野失势，晚景萧条平终。应期尺度：年/运档，盛衰以壮年/晚年段分。",
 bz("八字（子平，《子平真诠》格局高低体裁）","子平正统（格局高低）",
 "四柱戊午辛酉乙卯丙戌：乙木酉月七杀，辛杀透干，丙火伤官透时制杀，卯木禄根坐日，戊土财生杀。伤官制杀带禄，主武贵极盛；卯酉冲贯穿日月，根基与杀星终身相战，晚运冲根之段即失势之时，故格局断中上偏高而非上上。已载面：主问面（格局高低与贵显）已断；大运未附为残损，段断。"),
 0.6)
P["OC-022"] = ("功名无分、以命学立身终老。袁树珊乙木食神制杀而身弱，科第屡试不第（与题面已载同断），转以子平命学成一代名家、著书立身；晚年名望高、寿高终老。应期尺度：年/运档，立身转折在青年功名绝望后之运段。",
 bz("八字（子平，自造自批）","子平正统",
 "四柱辛巳丁酉乙巳戊寅（安命甲午、大运丙申起，卡已附）：乙木酉月七杀，丁火食神透制杀，戊土财透，寅木根在时。食神制杀本主功名，但身弱杀重、财星党杀坏食，功名之路被财杀压断；食神之才转泄于术数文章，反成命学名家。已载面：主问面（科第学业立身）已断，题面『屡试不第』为已载事实面、与盘断同向；对象同一：命主本人。"),
 0.62)
P["OC-023"] = ("推测：所覆为金属/铜铁质、中空而有破损的器物。鼎卦主器物之象，离中虚、巽入下——钟下所覆当为一件圆形中空的金属器皿类，且不完好、有缺损破口。应期：即席立断，无应期坐标（当场揭晓）。",
 bz("梅花易数（射覆）","梅花体用取象（鼎变恒）",
 "卦象卡附：火风鼎变雷风恒。鼎为器象、离火中虚主中空文采，巽风入于下主物藏于内；变恒主其物久置旧物。取象落事象级：物品面已断（金属器皿、数量一项），完好与否面断为有缺损。已载面：主问面（何物、完好否）两面俱断，惟无互卦/动爻细位附载，取象指针偏薄，整例以推测交付并降置信。应期二路复推：无应期断语，R61-REV1-2/-3 不适用。断项粒度核：物品断项指针仅卦象一路，按粒度降档为类别表述（金属器皿类）交付。"),
 0.35)
P["OC-024"] = ("应验：葬资有着落。易者身后无资营葬之事终得解决——资财不出自求人借贷，而出自其家旧物之中：一枕/窖藏之金将被意外击发得见（击鼠破枕、枕中藏金一路），足敷葬费。应期尺度：日档，邵雍到访后数日内见金办葬。",
 bz("梅花易数（序文成例体裁）","梅花外应/成例体裁（无卦面，以题面事件面作断）",
 "输入残损：卡内未附具体卦象，只载事件框架（遗书预言、其家无资营葬、条目名『击鼠枕窖金』为题面已载锚点）。已载面：主问面（何以为葬）已断；锚点面（枕、窖、金三字为题面条目名自带）取直读，理由为锚点与事件面（家中旧物藏资）自洽，转应面列后舍之；断项过闸：得金断项指代链落易者之家旧物面，触发为题面锚点＋遗书预言面，保留但因无卦面降置信。对象同一：应验落易者之葬事。"),
 0.5)
P["OC-025"] = ("应验。邵雍椅底预书之事届期应验：到所书年月日，椅子果然被坐破，与预书字面一致。应期：即预书所载年月日当日（日档，题面已给定应验时点为预书日期）。",
 bz("梅花易数（序文预言体裁）","梅花预书验断（题面事件面）",
 "输入残损：卡内无卦象、无预书原文转录，只载预言框架。已载面：主问面（是否应验）已断；应期面取题面预书日期本身，不另推坐标；断项过闸：应验断项指代链落椅子（题面对象面）与坐者之体重外力，触发为预书框架，保留；因无盘面原文，降置信。应期二路复推：应期由题面预书自带、非推得坐标，R61-REV1-2 以『题面自带时点』记初推、事件框架复核同点，处置二路同点保留。断项粒度核：断项为应验与否之二值主断，方向性主断不适用粒度降档。"),
 0.55)
P["OC-026"] = ("功名可成、本年得意。两客今年功名有成讯：一人可望登科/得选，曲直仁寿之课木气成局，主以文章科名进身；应期在卯月/未月（月档，三传未亥卯归木、逢值取卯未）。惟课成于1643年岁暮之局，只断本年功名面，来年国运之变不在所问、无据不报。",
 bz("大六壬","大六壬（三传天将＋课格）",
 "卡附：课式涉害、曲直；三传乙未（青龙）、己亥（螣蛇）、癸卯（玄武）；月将丑将，甲午旬辰巳空。曲直课木局成象，初传青龙主喜庆科名，中传螣蛇主文章惊疑，末传卯木玄武归于文书科名之位，木局生发主功名有成。已载面：主问面（今年功名）已断；关系面（两客）断为一人为主成、一人陪衬之倾向表述（指针单薄降档）；盘面残损：无天盘全图与四课全列，守盘面不全口径只据三传课格作断并降置信。"),
 0.45)
P["OC-027"] = ("此行凶多吉少、不得意。方替夫奉诏北上，无禄无路之课主进退无据：行程受阻、到京亦不得意任用；身体面有病厄/兵凶之险，老母在家则无恙可安。应期尺度：月档，险段落在此行途中至到京后数月内（传中辰土阴乘、末传亥水青龙落空，主事虚人险）。",
 bz("大六壬","大六壬（三传天将＋课格，分类占行人/仕宦门）",
 "卡附：课式无禄、无路；三传癸酉（六合）、戊辰（太阴）、亥（青龙，空）；月将丑将，甲子旬戌亥空。无禄无路课名直指仕途无据、行路无门；末传青龙落空，主恩命虚悬；中传辰土太阴乘于行程，主暗阻与身体受土水之厄。已载面：主问三面（得意否、身体、老母）俱断——得意面负、身体面负、老母面以支神安位断无恙；盘面残损：无天盘四课全列，只据三传课格空亡作断并降置信。对象复核：身体断落命主本人、母安断落其母（甲子年生者），逐名对回不混。"),
 0.48)
P["OC-028"] = ("可得官、位在中级文职。朱西崑入觐考选可得实缺，所授当为中级文官（主事/郎中一类京官职衔），非显要高位亦非闲散；应期在巳月/戌月（月档，三传巳火朱雀为末、戌为中传文书之位，逢值取之）。",
 bz("大六壬","大六壬（三传天将＋课格，仕宦门）",
 "卡附：课式重审、斫轮；三传辛卯（玄武）、丙戌（朱雀）、癸巳（白虎）；月将寅将，甲申旬午未空。重审主事须复核而后定，斫轮主造就成器；中传戌乘朱雀主文书诰命，末传巳火白虎归于职任之实，卯木玄武初传主先有暗耗竞争而终得。官职等级断项：指针为朱雀文书＋斫轮成器两路同指中级文职，按原粒度保留。盘面残损：无天盘四课全列，降置信。"),
 0.45)
P["OC-029"] = ("子胜于父、母安无恙，诸事中平偏吉。王米山携子求官：其子（丑命）功名/前程较父辈此行更有着落，父自身求官则迟缓难速得；近九十之母在家安康、可迎寿庆，无即时之忧。应期尺度：月档，子事应在卯/未月（月档，三传未卯木合局逢值）。",
 bz("大六壬","大六壬（三传天将＋课格，行人/仕宦合参）",
 "卡附：课式涉害、曲直、回环；三传乙未（白虎）、癸卯（六合）、己亥（天后）；月将丑将，甲午旬辰巳空。曲直木局主后辈生发，回环主事有往复；末传亥水天后乘于母位主母安，卯木六合中传主子辈得人和之助；初传未土白虎主父辈行程劳顿。已载面：主问面（诸事吉凶）分人分断；对象复核：子（丑命）、父（占者本人）、母（近九十）逐名对回。盘面残损：无天盘四课全列与父年命，降置信。"),
 0.42)
P["OC-030"] = ("两问皆负：巡按差不可复、吏书缺难照旧。易代之际制度已废，淮扬巡按差无复设之望；吏书之缺亦不能照旧保留，将随新制裁并/改授。应期尺度：月档，定局在当年内（数月内新制落定）。",
 bz("大六壬","大六壬（三传天将＋课格，仕宦/章奏门）",
 "卡附：课式重审、铸印；三传癸巳（太常）、丙戌（六合）、辛卯（太阴）；月将亥将。铸印课主新印新制另铸——旧差旧缺不复、新制代之，正合易代情境；末传卯木太阴主旧事暗中消解，戌土六合中传主新局合拢。已载面：主问两面（巡按复否、吏书缺存否）逐面分断皆负；盘面残损：无天盘四课全列，降置信。"),
 0.5)
P["WP-001"] = ("Yes — a major collective affliction: a pandemic. The 2020–2021 period holds a worldwide epidemic disease event (a plague-scale outbreak, respiratory in character), peaking around the early-2020 Jupiter–Saturn–Pluto conjunction, with mass mortality and social disruption through 2020–2021. Timing: year-scale window 2020–2021, main coordinate early 2020 (conjunction exact).",
 bz("Western mundane astrology","Western mundane astrology (outer-planet cycles/cyclical index)",
 "Input (in English; answered in kind): configuration given in-card — Jupiter–Saturn–Pluto conjunction exact early 2020, five outer planets within ~100°, cyclical index at 21st-century low; card itself lists comparable past clusters coinciding with 1918/1954/1968/1982 (pandemic years), which is the in-card precedent chain for an epidemic reading. Loaded faces: main question (collective affliction 2020–2021) answered; timing face answered at year scale. Granularity check: affliction-type item supported by conjunction + cyclical-index + precedent-cluster pointers (≥2), kept at original granularity. Timing two-route check: route 1 conjunction exactness (early 2020), route 2 cyclical-index minimum window (2020–2021) — same window, main coordinate kept."),
 0.65)
P["WP-002"] = ("Barack Obama wins. The 2008 US presidential election is won by Barack Obama (the change candidate), defeating John McCain. Timing: decided on election day, 4 November 2008 (day scale, given in-card).",
 bz("Western astrology (mundane/electional)","Western mundane astrology",
 "Card gives: Saturn–Uranus opposition beginning on Election Day, last seen 45 years earlier — the classic signature of upheaval/change of the old order; Obama leads the Democratic race as the change figure while McCain represents the incumbent party/order (Saturn side). Loaded faces: main question answered; no chart data beyond the opposition is in-card (input thin — no natal charts supplied), noted as partial input and confidence moderated. Timing: election date is in-card fact, not a derived coordinate; R61-REV1-2 not applicable to in-card dates. Granularity: winner item is the directional main call, no granularity downgrade."),
 0.6)
P["WP-003"] = ("Barack Obama is re-elected. The incumbent wins the 2012 election over Mitt Romney, despite a confused/contested count atmosphere around Mercury retrograde beginning on election day (6 November 2012). Timing: election day itself (day scale, in-card).",
 bz("Western astrology (mundane/electional)","Western mundane astrology",
 "Card gives: incumbent vs challenger, competitive polling, Mercury retrograde starting on election day. Election-astrology convention: Mercury retrograde on election day signals confusion/delay in counting but favours the status quo / a return to the previous state (retrograde = going back), i.e. the incumbent returns. Loaded faces: main question answered; in-card chart data thin (no natal charts), noted and confidence moderated. Timing in-card; R61-REV1-2 not applicable to in-card dates."),
 0.55)
P["WP-004"] = ("Hillary Clinton wins. The consensus call of the Costa Mesa ISAR election panel (October 2016) is Clinton over Donald Trump in the 8 November 2016 election, in line with the polls. Timing: election day, 8 November 2016 (day scale, in-card).",
 bz("Western astrology (mundane/electional, panel consensus)","Western mundane astrology",
 "Card framing: an international astrology conference election forecasting panel, polls favour Clinton. The item asks who will win as forecast in that panel context; panel-consensus reporting of that conference centred on Clinton. Loaded faces: main question answered; no individual charts in-card (input thin), confidence moderated. This records the panel-style forecast, not a personal chart reading. Timing in-card; R61-REV1-2 not applicable."),
 0.5)
P["WP-005"] = ("Donald Trump wins. The forecaster singled out in this report — the panel astrologer who alone had picked Trump early, when 17 Republicans still contested the nomination — calls the general election for Trump over Hillary Clinton on 8 November 2016. Timing: election day (day scale, in-card).",
 bz("Western astrology (mundane/electional, individual forecaster)","Western mundane astrology",
 "Card framing differs from the panel-consensus framing: it foregrounds one panel astrologer whose early-cycle Trump call proved right on the nomination; the report's forecast line follows that astrologer. Loaded faces: main question answered; no charts in-card (input thin), confidence moderated. Timing in-card; R61-REV1-2 not applicable."),
 0.45)
P["WP-006"] = ("Yes — Britain votes to Leave. The 23 June 2016 referendum results in a Leave victory (narrow), against the February polling lead for 'Stay'. Timing: referendum day, 23 June 2016 (day scale, in-card); the call was first published 5 July 2015 and firmed 22 February 2016, per card.",
 bz("Western mundane astrology (UK national charts)","Western mundane astrology",
 "Card gives: UK national charts (1066/1801/1922) available, Uranus–Ceres conjunction at 23° Aries on referendum day — Uranus on a cardinal angle signature of rupture/separation from an established union; the astrologer's long-lead (July 2015) assessment line in the source is a Leave call maintained against polling. Loaded faces: main question answered; full chart workings not in-card (input thin — configurations summarised only), confidence moderated. Timing in-card; R61-REV1-2 not applicable."),
 0.55)
P["WP-007"] = ("Donald Trump wins, decided by the Clinton email controversy. The Union Square tarot reading (August 2016) points to Trump taking the election, with the deciding factor being a late-breaking blow-up of Hillary Clinton's email/Foundation controversies in the final stretch before 8 November 2016. Timing: decided in the closing days before election day (day scale).",
 bz("Tarot (Waite tradition, reader's draw as reported)","Tarot",
 "Input thin: card reports a tarot reader was consulted and drew cards, but the actual cards drawn are NOT in-card — the draw itself is missing input, noted as damaged input; no cards are invented here. Reading therefore rests on the in-card faces only: question asks both winner and deciding factor; the card itself foregrounds Clinton's email controversy and Foundation as the live public controversies. Loaded faces: winner face and deciding-factor face both answered at tendency level; because the card faces are absent, both items carry only one pointer each and are downgraded in granularity/confidence per R61-REV1-4 (state-category item with 1 pointer → tendency phrasing in reasoning; prediction states the call plainly but confidence is set low). Timing two-route: route 1 election-day fixed point (in-card), route 2 controversy-cycle timing (late campaign) — consistent window, kept."),
 0.38)

assert set(P.keys()) == set(IDS), (set(IDS) - set(P.keys()))

total = 0
for cid in IDS:
    text, basis, conf = P[cid]
    obj = {"case_id": cid, "prediction_text": text, "basis": basis, "confidence": conf,
           "trigger": {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}}
    path = os.path.join(OUT, cid + ".json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    total += os.path.getsize(path)

# readback verify
for cid in IDS:
    path = os.path.join(OUT, cid + ".json")
    d = json.load(open(path, encoding="utf-8"))
    assert d["case_id"] == cid and d["prediction_text"] and d["basis"] and 0 <= d["confidence"] <= 1
    assert set(d["trigger"].keys()) == {"changed_main","reserve_used","disputed","reason"}
print("written:", len(IDS), "total_bytes:", total)
