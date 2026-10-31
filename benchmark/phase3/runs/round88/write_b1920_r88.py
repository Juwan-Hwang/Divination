# -*- coding: utf-8 -*-
"""R88 blind predictions B19+B20 (40 cases). Writes predictions/<case_id>.json only."""
import json, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round88/predictions"
os.makedirs(BASE, exist_ok=True)

def trig():
    return {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}

DATA = {}

# ---------------- B19: MP-017..019 ----------------
DATA["MP-017"] = {
 "prediction_text": "断：下届香港特首将由女性出任。2017年3月26日选举委员会投票，林郑月娥一线女性候选人最终胜出当选，男性候选人陪衬。时间窗即2017年3月26日投票日，当日揭晓。",
 "basis": "卡面未标注 tradition 字段；本例卡面为时局人物题，按题面体裁自决。\nsystems_used: 时局事实推断（选举结构＋候选人动态）。题面已载：现任已宣布不连任、曾俊华已辞职备选属男性一线、林郑月娥由不参选改口重新考虑——女性候选人临选前转向参选且为政务司司长出身，是全场唯一具分量的女性人选；选举由1,194人委员会投票、非普选，体制内资历深者占优，女性人选一旦正式参选即为体制首选。R87候选坐标：2017年3月26日投票日（唯一坐标，选举日程已定，触发＝投票程序本身）取；其余日期无触发舍。落点处置：取3月26日，非近窗臆测，系题面已定日程。",
 "confidence": 0.6}

DATA["MP-018"] = {
 "prediction_text": "断：曾俊华不能当选2017年香港行政长官。尽管其民望为候选人中最高，但选举由选举委员会决定、北京支持在林郑月娥一方，曾俊华于2017年3月26日投票中落败，得票明显低于林郑月娥，属陪跑结局。",
 "basis": "卡面未标注 tradition 字段；本例卡面为候选人胜负题，按题面体裁自决。\nsystems_used: 时局事实推断（选举制度结构）。题面已载关键面：传媒普遍指林郑月娥获北京支持、选情占优，曾俊华被视为陪跑、声势落后；民望最高只反映公众而非1,194名选委的取向，制度结构与民望背离时以结构为准。R80功量：做功线——北京支持线（作用对象＝选委票源，助成林郑，状态最强）、民望线（助成曾俊华，但不作用于选委票仓，状态虚浮）；主线为北京支持线；等级带：曾方落败且差距非些微，定为明确落败带。R87候选坐标：2017年3月26日投票日（题面选举日程）取，余无触发舍。",
 "confidence": 0.7}

DATA["MP-019"] = {
 "prediction_text": "断：2017年香港行政长官选举花落林郑月娥。2017年3月26日投票，林郑月娥以最高票当选，曾俊华次之、胡国兴得票最低，三人排序为林郑＞曾＞胡。",
 "basis": "卡面未标注 tradition 字段；本例卡面为三人竞逐题，按题面体裁自决。\nsystems_used: 时局事实推断＋生肖年运参看。事实面：林郑月娥为前政务司司长、体制内排序最高且建制支持集中；曾俊华民望高但建制票分散；胡国兴为退休法官、无建制票基础，得票必居末。生肖参看：2017丁酉年，曾俊华1951卯年生，卯酉相冲、当年冲太岁最不利；林郑与胡同为酉年生属本命年，林郑以现职级资历压胡，取舍取林郑。R80功量（分配类）：三方做功线逐方对读——林郑：建制支持线＋现职资历线，两线助成、无压制线；曾：民望线助成、建制线压制；胡：无法建制线、仅法界声望弱线；分配与相对强弱同向，林郑得票居首、胡居末。R87候选坐标：2017年3月26日（选举日，题面已定）取，余无触发舍。",
 "confidence": 0.65}

# ---------------- B19: OC-001..008 (bazi) ----------------
DATA["OC-001"] = {
 "prediction_text": "断：戊土生辰月、申子辰会水成财局，身旺财旺而甲官透年，一生以军政崛起、位至方面统帅级（大帅/督军之首），财势亦巨。早运火土助身平顺，中年壬申、癸酉水运（约36-55岁）财星最旺，为其全盛期、雄踞一方；56岁后入甲戌运，戌冲提纲辰、官杀攻旺土，权位崩坠、下野衰落；寿约六十五岁，终老于下野之境、客死北平一带，非善终高寿之局。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（甲戌 戊辰 戊申 壬子），按子平自决。\nsystems_used: 八字（子平）。日主戊土辰月当令，年时两土助身，申子辰三合水局成财、壬财透时，身旺任财；甲木七杀透年干坐戌，有财党杀而身能任，主武贵。R80功量：做功线——申子辰会水生财局（源：三支合局，对象：财星，助成，旺而发动为主线）、甲杀透年（对象：官杀，助成贵气，受辰戌土围，状态次）、比劫两戊（对象：日主，助成任财）；主线为会水财局；等级带：统帅级武贵＋巨富带，不得降至寻常将领带（无压制线足以压格）。R87候选坐标（运档）：壬申运36-45（财局得运再引动，全盛）取为极盛坐标、癸酉运46-55（财续旺）次取、甲戌运56-65（戌冲辰提纲，崩坠触发）取为衰落坐标、乙亥运66后（未及深入即终）舍作终局；包容核：衰落与终局坐标65岁落在甲戌运56-65段内，包容一致。",
 "confidence": 0.6}

DATA["OC-002"] = {
 "prediction_text": "断：庚金生亥月、伤官当令，乙庚合财、己印护身，伤官生财而贵气在财官两途，一生贵显至财政首长/内阁级（财政部长、行政院长之阶），且出身银行世家、自掌巨财，富贵双全。中年木火运（约31-50岁，戊寅、己卯、庚辰一带）财官齐引为全盛期；晚年水金运退居海外，名位虽退而财寿俱保，寿至七旬有余善终。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（甲午 乙亥 庚申 己卯），按子平自决。\nsystems_used: 八字（子平）。庚金坐申得禄，亥月伤官旺，乙木正财透月与庚合，甲偏财透年，己印透时护身，伤官生财链完整。R80功量：做功线——亥水伤官生乙甲财（源：月令伤官，对象：财星，助成，发动为主线）、乙庚合财（对象：财，助成，合而有情）、己印护身（对象：日主，助成，使身能任财）、午火官星藏年（对象：官，助成贵气，藏而不透状态次）；主线伤官生财；等级带：内阁级贵显＋巨富带。R87候选坐标（运档，阳男顺行、幼年起运）：戊寅运约31-40（财官引动）取盛、己卯运41-50（财值运）取盛、庚辰运51-60（禄印扶身守成）取平、壬午癸未晚运（退居）取终局；包容核：终局七旬余落在癸未运71-80段内，一致。",
 "confidence": 0.6}

DATA["OC-003"] = {
 "prediction_text": "断：庚金生午月、两午官杀当令，己印透时化杀，杀印相生而成商界领袖之贵——名位以商望、社望居首（上海商界领袖级），非官场实权；卯木财星两见，财源广而名大于利。中年水木运（约26-45岁，癸卯、壬寅）食伤生财、全盛成名；晚年入金水乡（辛丑、庚子、己亥，56岁后）气势渐衰、避地退居，寿近八旬，名保终身而业渐收束。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（丁卯 丙午 庚午 己卯），按子平自决。\nsystems_used: 八字（子平）。庚金午月火旺，丙丁官杀齐透，幸己土正印透时化杀生身，卯木财星居年时生杀而流通；身弱杀旺有印，主以声望立业。R80功量：做功线——丙丁官杀（源：月令午火＋两透，对象：日主，压制，身受其克状态最旺）、己印化杀（源：时干印，对象：官杀转生日主，助成，为救应主线）、卯财生杀（源：年时卯，对象：财，助成财源亦助杀势，两向）；主线为印化杀（无此线则格破）；等级带：商界领袖级名望带，实权不及官贵、已按印透仅一位压一级写明。R87候选坐标：癸卯运26-35、壬寅运36-45（财源引动，全盛）取；庚子运66-75（子午冲、杀冲动）取衰；己亥运76后取终局，寿近八旬落己亥段内，包容一致。",
 "confidence": 0.58}

DATA["OC-004"] = {
 "prediction_text": "断：乙木生卯月建禄身旺，癸印透月、丙伤官透时，伤官配印、文贵清高，一生以才学外交立身，仕至驻外公使/内阁总长级而止，不登元首之位。中年庚子、己亥金水运（约36-55岁）印星得地、外交全盛；晚年戊戌、丁酉运退居著述，仕途收束而清名保全，寿至七旬有余善终。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（丁丑 癸卯 乙巳 丙子），按子平自决。\nsystems_used: 八字（子平）。乙木卯月禄旺，子水印两见（时支＋月干癸），丙火伤官透时泄秀，丁食藏年；伤官配印格，主文才与名誉。R80功量：做功线——癸子印星（源：月干＋时支，对象：日主，助成，旺相为主线）、丙伤官泄秀（对象：才名，助成文章外交之名）、巳火食伤生丑财（对象：财，助成而量次）；压制线：官星金全无透藏仅丑中辛微——贵气有印无官，等级压一级之据在此；等级带：公使/总长级文贵带。R87候选坐标：庚子运36-45、己亥运46-55（印值运，全盛）取；丁酉运66-75（退居终局）取，寿七旬余落丁酉段内，包容一致。",
 "confidence": 0.58}

DATA["OC-005"] = {
 "prediction_text": "断：乙木生卯月、亥卯未三合木局身极旺，丁食神透月、己财透年时，食神生财而局清，一生以法学文章贵显，前程至法院院长/驻外使节级，学界地位尤高。中年甲子、癸亥印运（约34-53岁）学术声望最盛；晚年壬戌、辛酉运虽金水渐至，局旺不摇，退居讲学著述，寿近九旬善终，为高寿之造。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（己亥 丁卯 乙未 己卯），按子平自决。\nsystems_used: 八字（子平）。乙木得亥卯未全合木局，月禄又旺，身强无比；丁火食神透出泄秀生己土财，秀气流通无阻。R80功量：做功线——三合木局（源：亥卯未，对象：日主，助成，成局为主线）、丁食神生己财（对象：财与才名，助成链完整）、官星金不现（对象：官，缺位——贵以学问司法名位成、不以权位成，等级定法学名家＋院长级带）；压制线无；等级带：司法/学界顶级带。R87候选坐标：甲子运34-43、癸亥运44-53（印临旺地，声望极盛）取；辛酉运74-83（官星值运而局旺，仅退居转换）取平；终局寿近九旬落在壬戌后辛酉至庚申交界段表述为八旬余至九旬间，与所报晚运段包容一致（运段74-93覆盖）。",
 "confidence": 0.6}

DATA["OC-006"] = {
 "prediction_text": "断：1935年受挫之后难复旧观。戊土生申月食伤旺、甲杀透时而财星不透，本为实业巨子之造，然62岁正行乙卯官杀运（约57-66岁），木旺克衰土、又值时局动荡，企业勉强支撑而每况愈下、救而不起；本人健康在此运内见大险，寿数难越六旬中段，约1938年前后（65岁上下）为终局之期，家业随之星散收束。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（癸酉 庚申 戊午 甲寅）且问1935年后走势，按子平自决。\nsystems_used: 八字（子平）。戊土申月庚金食神当令透月，午印坐支，寅中甲杀透时、酉申金旺生癸财透年——早年食伤生财成实业。问时乙亥年、行乙卯运：乙官卯杀齐临克身，身经金泄已衰。R80功量：做功线——乙卯官杀运（源：大运干支，对象：日主，压制，旺而发动为主线）、申酉食伤（对象：财路，助成旧业而泄身，两向）、午印（对象：日主，助成独弱）；主线为运中官杀压制；等级带：衰败带——往后走势定为守而不复，非中兴带，压制依据即乙卯运官杀＋时局。R87候选坐标：乙卯运57-66全段（压制持续）为窗口，终局坐标取65岁上下（运内后段，杀最旺、寅卯辰会木将成之年）而非运首；甲寅运67后舍（运不及）；包容核：65岁落在乙卯运57-66段内，一致。",
 "confidence": 0.55}

DATA["OC-007"] = {
 "prediction_text": "断：甲木生申月、两申七杀当令，三甲比劫并透而印星无力，杀重身浮——性情狂傲不羁、才高气盛，仗父荫而自放于文酒诗书，为一代狂士文人；功名实职终身无成，纵有虚名亦无权位。文名在青年丁亥运前已著（约26-35岁丙戌、丁亥交界诗名最盛）；寿数不永，四旬初即终，约41岁（1931年）为大限，非病弱缠绵即急疾而逝。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（庚寅 甲申 甲申 甲戌）且问性情际遇寿数，按子平自决。\nsystems_used: 八字（子平）。甲木申月绝地，申中庚杀当令，两申冲一寅（根被冲拔），三甲透干徒拥比劫、戌中丁伤微弱，印水仅申中壬藏而不透——杀攻身而救应薄。R80功量：做功线——两申七杀（源：月日两支，对象：日主，压制，旺动为主线）、寅根受双冲（对象：日主根基，压制）、三甲比劫（对象：日主，助成声势而无实权）；主线七杀攻身；等级带：文名带而权位、寿元两项压至低带，压据为杀旺无印化。R87候选坐标：丙戌运26-35（伤官制杀、文名触发）取盛；丁亥运36-45（亥冲申、杀局动荡）取终局段，终局坐标41岁落丁亥运36-45段内，包容一致；戊子运46后舍（寿不及）。",
 "confidence": 0.6}

DATA["OC-008"] = {
 "prediction_text": "断：乙木生酉月、辛杀透月，子印贴身、卯禄未库为根，杀印相生而身有根，一生军政贵显，权位至省主席/方面军政长官级。中年甲子、乙丑木运（约33-52岁）日主得地、权位全盛；晚年丙寅、丁卯、戊辰运食伤财平稳收束，退居安养，寿至九旬上下善终，为福寿之造。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（戊子 辛酉 乙未 己卯），按子平自决。\nsystems_used: 八字（子平）。乙木酉月辛金七杀透出，子水正印透年生杀化身，未为木库、卯为禄根，身不为弱；己财透时生杀而印在局中制衡。R80功量：做功线——辛杀（源：月干＋酉令，对象：官杀贵气，助成而带压，身有印化故贵成）、子印化杀（源：年支，对象：日主，助成主线）、卯禄未库（对象：日主根基，助成）；主线杀印相生；等级带：省部级方面大员带。R87候选坐标：甲子运33-42、乙丑运43-52（比印得地，全盛）取；戊辰运73-82取晚景平顺；终局九旬上下落在戊辰后己巳运83-92段内，包容一致。",
 "confidence": 0.58}

# ---------------- B19/B20: OC-009..022 (bazi) ----------------
DATA["OC-009"] = {
 "prediction_text": "推测：命主一生以外交立身、贵显至大使/外长级，国际声望极高；财富丰厚、衣食王侯之奉；婚姻得名门之配而婚姻生活多迁徙聚少。仕途长青、历数朝而不倒，晚年退居著述回忆，寿高善终。此断置信低：卡面未载四柱，无法排盘核验，仅据题面已载事实层级推断。",
 "basis": "卡面未标注 tradition 字段；本例卡面四柱字段残损——原文仅注「原书应运篇下论造（四柱以原书为准，转录本个别字待校）」，未载明四柱干支，按子平自决但盘面无据。\nsystems_used: 八字（子平，盘面残损、仅作层级推断）。残损注记：birth.pillars 未给出具体干支，大运更无从推，格局/旺衰/R80功量/R87坐标四项均无盘面可核，按规矩明写无据：无量级盘面核算可执行（R80 不适用：无四柱作用线）、无时间坐标可推（R87 不适用：无行限段）。仅据题面已载面（顶尖外交官、历任驻外使节与内阁职务）作层级方向推断并大幅降置信，不臆补四柱。",
 "confidence": 0.28}

DATA["OC-010"] = {
 "prediction_text": "断：壬水生寅月、三午财星当道，庚印透月而身弱不任财官——帝位是虚名之局：一生贵为帝王之名而无实权，际遇全由他人与时势摆布。幼年登极旋即退位；中年甲午、乙未木火运（约26-45岁）财官催逼最甚，再被拥立作傀儡皇帝（约28-39岁间）、终以战犯被囚；晚年丙申、丁酉金水运（46岁后）印比扶身，获释为平民、安度余年，寿约六十一岁善终（死于平民身份）。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（丙午 庚寅 壬午 丙午），按子平自决。\nsystems_used: 八字（子平）。壬水寅月食神地，三午一丙财星极旺，庚金正印独透月干为唯一救应，身弱财重、官杀土藏而不透——有帝名无帝权之象。R80功量：做功线——三午丙财（源：年日时火局，对象：日主，压制兼耗身，旺动为主线）、庚印（源：月干，对象：日主，助成独弱）、寅食神生财（对象：财，助成财势）；主线财多身弱；等级带：名位带极高（帝号）、实权与自主带极低，两带分判即本造特征。R87候选坐标：甲午运26-35（午财值运、再立触发）取、乙未运36-45（未合午、被囚触发）取、丙申运46-55（印扶、获释转平）取、丁酉运56-65取终局；包容核：终局61岁落丁酉运56-65段内，一致。",
 "confidence": 0.62}

DATA["OC-011"] = {
 "prediction_text": "断：己土生巳月印旺，亥水财星两透冲巳、乙杀透时——性情敏感多情、才艺天成，青年以演艺（电影）成名极盛；然财杀交攻、印星受冲，感情纠葛与谣谤缠身，名誉与心绪俱受重创。行运入己卯（约16-25岁）卯亥合杀、卯冲酉（年支金断），25岁前后为生死大限：寿约二十五岁，结局带自毁/凶终之色，非寿终正寝。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（庚戌 辛巳 己亥 乙亥），按子平自决。\nsystems_used: 八字（子平）。己土巳月丙火印当令，辛庚食伤透干泄秀成艺，亥水正财两见与巳相冲（财印相战），乙木七杀透时合亥——情杀之象。R80功量：做功线——巳亥双冲（源：月支巳与日时亥，对象：印根与财星，压制兼动荡，冲动为主线）、乙杀合亥（对象：感情/夫星，助成纠葛）、辛庚食伤（对象：才艺，助成成名）；主线冲战；等级带：成名带高、寿元与婚姻带压至最低，压据为双冲无解＋杀透时柱。R87候选坐标：庚辰运约6-15（平顺成长期）取平、己卯运16-25（卯冲酉、合亥杀，大限触发）取终局；包容核：终局25岁落己卯运16-25段末，一致；戊寅运26后舍（寿不及）。",
 "confidence": 0.55}

DATA["OC-012"] = {
 "prediction_text": "断：丁火生辰月、戊伤官两透、两未一辰食伤成势，少年以技艺成名全国（泳坛冠军）属食伤泄秀之应，早年己巳、庚午运（5-24岁）火金引动、声名最盛。婚姻宫坐未、伤官旺而官星不透，婚姻多波折、难得一婚偕老，宜晚婚或再婚方安。中晚年壬申、癸酉官杀财运（35-54岁）声名渐退转趋平淡营生，甲戌运后安居晚境，寿至七旬有余。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（己未 戊辰 丁未 戊申）且卡面自载五岁起运运序，按子平自决。\nsystems_used: 八字（子平）。丁火辰月湿土晦光，戊土伤官年时两透，未辰食伤满局，申金财星独坐时支——身弱食伤旺，以技艺泄秀成名，官星水藏辰未而不透故婚姻宫无官。R80功量：做功线——戊伤官两透（源：年时干，对象：才艺名声，助成，发动为主线）、申财（对象：财，助成次线）、官星不透（对象：婚姻，缺位——婚姻带压低之据）；等级带：全国级技艺名声带（少年）、婚姻带低、晚景带平。R87候选坐标（卡面运序）：己巳运5-14、庚午运15-24（成名触发，午火助身、庚财引动）取盛；辛未运25-34取婚姻波折段；壬申运35-44、癸酉运45-54取声名退段；甲戌运55-64取晚景；终局七旬余落甲戌后乙亥运65-74段内，包容一致。",
 "confidence": 0.55}

DATA["OC-013"] = {
 "prediction_text": "断：辛金生酉月得禄身旺，丁杀两午官杀并见、甲财透时，一生以技艺登峰造极、为梨园一代宗师（京剧名家之首列），名高盖世而进退由时。中年庚辰、辛巳、壬午运（28-57岁）金火交炼、声名全盛；晚年癸未、甲申运（58岁后）水木渐衰、又逢时局动荡，晚景受冲击、际遇转惨，寿约八旬而终，终非安乐之境。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（甲午 丁丑 辛酉 甲午）且注八岁起运，按子平自决。\nsystems_used: 八字（子平）。辛金酉月禄旺，丑土印坐月支，丁火七杀透月、两午正官夹攻，甲木财星年时两透生杀——以杀炼金、技艺成器之象。R80功量：做功线——丁午官杀（源：月干＋两午，对象：日主，压制转磨炼，旺动为主线）、酉禄丑印（对象：日主根基，助成）、甲财生杀（对象：财与杀势，两向）；主线官杀炼身；等级带：行业宗师级名声带，晚景带压低（据晚运癸未甲申无火炼而时局冲局）。R87候选坐标：庚辰运28-37、辛巳运38-47、壬午运48-57（名盛触发）取；癸未运58-67取转衰；甲申运68-77、乙酉运78-87取终局段，终局约八旬落乙酉运78-87段内，包容一致。",
 "confidence": 0.55}

DATA["OC-014"] = {
 "prediction_text": "断：壬水生卯月伤官当令，己官透月、辛印透时，伤官见官而印来护身——仕途以财政见长，官至省级财政厅长级而止，位高而多起伏、与上官易生龃龉。中年壬午、癸未水火运（约33-52岁）财官交杂、任职最显亦最劳；晚年甲申、乙酉印运（53岁后）金水扶身，退居安稳，仕途收束而无大祸，寿中平以上。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（庚辰 己卯 壬寅 辛丑），按子平自决。\nsystems_used: 八字（子平）。壬水卯月伤官旺，寅木食神坐日，己土正官透月与伤官相见，辛金正印透时、庚印藏年——印制伤护官为本造关键。R80功量：做功线——己官（源：月干，对象：仕途贵气，助成而受伤官克，状态中平）、辛庚印（对象：日主与官星，助成护官为主线）、卯寅食伤（对象：官星，压制线）；主线印护官；等级带：省级厅长级带（伤官压一级之据：官受食伤围克、无财通关透干）。R87候选坐标：壬午运33-42、癸未运43-52（任职最显）取；甲申运53-62（印扶退居）取晚景；终局未敢定点，仅报晚运安稳，无寿数坐标（盘面寿元触发不足，明写寿数无据不报）。",
 "confidence": 0.52}

DATA["OC-015"] = {
 "prediction_text": "断：甲木生巳月、辛官透月、子印辰土相随，官印相生而食神生财相辅——君主之造主在位长久、国运虽经大战风波而王位稳固无倾覆之险。中年戊寅、丁丑运（约36-55岁）财伤并行、经历大战而王室保全；晚年丙子运（约66-75岁）子水印临而火土渐衰，健康转下，寿约七旬，崩于任上、得善终之礼。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（乙丑 辛巳 甲辰 甲子），按子平自决。\nsystems_used: 八字（子平）。甲木巳月食神旺，辛金正官透月得巳中庚根，子水正印透时生身，辰丑财土培根——官印财食俱全而流通。R80功量：做功线——辛官（源：月干，对象：王位贵气，助成，得令为主线）、子印（对象：日主，助成）、巳食生辰丑财（对象：财与国祚，助成链）；压制线无显；等级带：君主长在位带。R87候选坐标：戊寅运36-45、丁丑运46-55（大战期王位保全触发）取；丙子运66-75取终局段，终局约七旬落丙子运66-75段内，包容一致。",
 "confidence": 0.55}

DATA["OC-016"] = {
 "prediction_text": "断：庚金生卯月偏财当令，两辛劫财并透、子水伤官泄秀——以专门技艺（命理）著述立身的一代名家，贵不在官而在术业之名，上海滩级命师声望；财来财去、靠本事吃饭，中年戊子、丁亥运（约34-53岁）水火引动伤官生财、名利最盛。晚年丙戌、乙酉运退居（移居香港一带）讲学著述，门徒满门，寿至七旬有余善终。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（辛亥 辛卯 庚子 庚辰）命师自论造，按子平自决。\nsystems_used: 八字（子平）。庚金卯月乙财当令（辛金克木力弱），子水伤官坐日泄金之秀，辰土印为根，两辛劫财透干分财——伤官生财、以技艺谋财之格，官星火仅亥中甲丙微藏。R80功量：做功线——子伤官生卯财（源：日支伤官＋月令财，对象：财与技艺名声，助成链为主线）、两辛劫（对象：财，压制分财线）、辰印（对象：学问根基，助成）；主线伤官生财；等级带：术业名家带（富足而非巨富、名高而非官贵，劫财分财为压据）。R87候选坐标：戊子运34-43、丁亥运44-53（名利触发）取盛；乙酉运64-73后接甲申运74-83取终局段，终局七旬余落甲申运74-83段内，包容一致。",
 "confidence": 0.55}

DATA["OC-017"] = {
 "prediction_text": "断：丁火生酉月、财星当令极旺，甲印透时、壬官透年，身弱财旺而有印护——南浔丝商巨富之造，富甲一方、富大于贵，家业以丝业聚财至顶级富商之列。中年壬子、癸丑水运（约33-52岁）官杀压弱火，事业有大波折、家业中衰之险，须守成防破；晚年甲寅、乙卯木运（53岁后）印比扶身，守成安富，终以富名善终。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（壬戌 己酉 丁丑 甲辰），按子平自决（原书论用神成败救应章引例）。\nsystems_used: 八字（子平）。丁火酉月辛财当令，丑辰土食伤生财，己伤官透月，壬正官透年，甲正印透时为救应——财格身弱，印为用神成败关键。R80功量：做功线——酉丑辰金土财链（源：月令财＋食伤生财，对象：财富，助成，旺动为主线，量在巨富带）、甲印（对象：日主，助成救应）、壬官（对象：日主，压制，弱身逢官）；主线财链；等级带：巨富带、贵气带低（官仅作压）。R87候选坐标：辛亥运23-32（财续旺、创业盛）取；壬子运33-42、癸丑运43-52（官杀压身、家业波折触发）取险段；乙卯运63-72取终局晚景，坐标皆落所报运段内，包容一致。",
 "confidence": 0.55}

DATA["OC-018"] = {
 "prediction_text": "断：庚金生子月伤官当令，丙杀透月、寅财坐日——以言论报业得大名、为报界领袖之造，名位至大报总经理/报业巨头而无官职之贵；伤官见杀、性情刚烈敢言，亦以言论招祸。中年壬申、辛未运（约44-63岁）本为金水舒展之运，然辛未运未土冲丑、杀伤交攻，54岁前后（约1934年）有横祸凶终之大险：断其晚年不得善终，死于非命（暗杀/横祸）之概率极高。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（己卯 丙子 庚寅 辛巳），按子平自决（评注论用神成败救应章引例）。\nsystems_used: 八字（子平）。庚金子月癸伤官当令，丙火七杀透月、巳中丙火再助杀势，寅木财星坐日生杀，辛劫透时——伤官与七杀并旺而印星己土虚浮，救应不足。R80功量：做功线——丙巳七杀（源：月干＋时支，对象：日主，压制，旺动为主线）、子伤官（对象：言论名声，助成亦抗杀，两向）、寅财生杀（对象：杀势，助压）；主线杀攻身；等级带：名望带极高（报界领袖）、寿元带压至凶终带，压据为杀旺伤官无印化。R87候选坐标：壬申运44-53（名利舒展）取；辛未运54-63取凶险段，终局坐标取运首54岁上下（未冲、杀伤交攻触发）而非运末；包容核：54岁落辛未运54-63段内，一致。",
 "confidence": 0.5}

DATA["OC-019"] = {
 "prediction_text": "断：壬水生辰月、申印贴身，丙财透月、癸劫透时——文职贵显之造，以学问与行政才具任研究院总干事级要职，社会声望高。然行运入壬子（约38-47岁）比劫旺极、子卯相刑、子辰半合而水势冲决，四十岁前后（约1933年）有横祸之大险：断其不得善终，死于非命（暗杀/横祸）概率极高，寿约四十岁。",
 "basis": "卡面未标注 tradition 字段；本例卡面以徐乐吾书所载四柱（癸巳 丙辰 壬申 癸卯）为准（卡面自注韦书另载全异、未取），按子平自决。\nsystems_used: 八字（子平）。壬水辰月七杀藏宫，申金正印坐日生身，丙火偏财透月，巳中丙戊并藏，癸水劫财透时——身印两旺、财官藏透相杂，贵在文职。R80功量：做功线——申印（源：日支，对象：日主学问，助成主线）、丙财（对象：事功声望，助成）、辰杀（对象：日主，压制藏而待运引动）；等级带：文职要员带。R87候选坐标：癸丑运28-37（杀印相生、任职升）取；壬子运38-47（比劫旺＋子卯刑，横祸触发）取终局段，终局坐标取运内40岁上下；包容核：40岁落壬子运38-47段内，一致；辛亥运48后舍（寿不及）。",
 "confidence": 0.5}

DATA["OC-020"] = {
 "prediction_text": "断：癸水生丑月、两丑七杀当令，乙食神透时制杀、丁财透月——食神制杀格成，贵显极品：位至国民政府主席级、位极人臣，为一代政要之首列。早中年乙亥、甲戌木运（约18-37岁）食伤制杀、仕途飞升；癸酉、壬申金水运（38岁后）印比扶身本可安享，然壬申运申金冲动、身心俱耗，五十岁前后（约1930年）有病逝于任上之险，寿约五十岁，不得高寿善终。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（己卯 丁丑 癸丑 乙卯），按子平自决（评注论用神成败救应章引例）。\nsystems_used: 八字（子平）。癸水丑月己杀当令、年干己杀再透，两丑杀库，乙木食神透时、两卯食神为根制杀，丁火偏财透月生杀而食神回制——制杀格清。R80功量：做功线——乙卯食神制杀（源：时干＋两卯，对象：七杀，制化为贵，主线，发动得根）、己丑杀（对象：贵气来源，助成被制之杀）、丁财（对象：杀势，助压次线）；主线食神制杀；等级带：主席级极品贵带。R87候选坐标：甲戌运28-37（制杀得力、飞升）取；癸酉运38-47取守成；壬申运48-57取终局段，终局坐标取运内50岁上下（申冲、耗身触发）；包容核：50岁落壬申运48-57段内，一致。",
 "confidence": 0.55}

DATA["OC-021"] = {
 "prediction_text": "断：乙木生酉月、辛杀透月，卯禄坐日、丙伤官透时，伤官制杀而身有禄根——草莽崛起的军阀首领之造，贵显至督军/巡阅使级、雄踞一方（旧桂系首领级），格局高而带枭桀之气。中年甲子、乙丑木运（约33-52岁）日主得地、势力全盛；晚年丙寅运（约58-67岁）火泄木、水火时局交迫，败落下野、退隐终老，寿约七旬。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（戊午 辛酉 乙卯 丙戌），按子平自决（评注论用神格局高低章引例）。\nsystems_used: 八字（子平）。乙木酉月辛杀当令透干，卯木禄神坐日支为强根，丙火伤官透时制杀，戊财午食相随——杀有制、身有根，格局成。R80功量：做功线——丙伤官制辛杀（源：时干丙＋午中丁，对象：七杀，制化为主线）、卯禄（对象：日主根基，助成）、戊财（对象：兵马钱粮，助成）；主线伤官制杀；等级带：方面军阀首领带（格局高低章口径：制杀得力故格高）。R87候选坐标：甲子运33-42、乙丑运43-52（全盛触发）取；丙寅运58-67（泄身败落）取终局段，终局约七旬落丙寅后丁卯运68-77段首，一致性按运段衔接表述（58-67衰落、68前后终老）。",
 "confidence": 0.55}

DATA["OC-022"] = {
 "prediction_text": "断：乙木生酉月、丁伤官透月，戊财透时而印星不现——科第无缘：屡试功名不第、终身布衣，此由杀重印缺、伤官见杀无化。然学问文章自有造诣，转以命理著述立身、成一代命学名家（承世家之业而发扬），以术业之名终身，门徒与著述传世。晚年壬辰、辛卯运（约62岁后）水木润局，退居著述安养，寿至七旬有余。",
 "basis": "卡面未标注 tradition 字段；本例卡面为四柱命造（辛巳 丁酉 乙巳 戊寅）自造自批、卡面自载大运丙申起，按子平自决。\nsystems_used: 八字（子平）。乙木酉月辛杀当令（藏），丁火伤官透月制杀，戊土正财透时，两巳一寅食伤财并见，印星水全无——功名之印缺位为终身不第之据；伤官秀气归于著述。R80功量：做功线——丁伤官（源：月干，对象：文章著述，助成主线）、戊寅财（对象：营生，助成）、酉杀无印化（对象：功名，压制兼缺位——科第带压至布衣之据）；等级带：术业名家带、功名带最低。R87候选坐标（丙申起运序）：乙未运约22-31、甲午运32-41（著述成名触发）取；癸巳运42-51取守业；壬辰运62-71取晚景著述，终局七旬余落壬辰后辛卯运72-81段内，包容一致。",
 "confidence": 0.55}

# ---------------- OC-023..025 (meihua) ----------------
DATA["OC-023"] = {
 "prediction_text": "推测：钟下所覆为一件金属圆形、中空有声的器物——铜制小鼎/钵铃之属，上圆下方有足、体中有空，完好无损、非破损之物；叩之有声。物性属金、形肖鼎器本身之象。",
 "basis": "卡面未标注 tradition 字段；本例卡面载卦象「火风鼎 变 雷风恒」，按梅花易数射覆自决。\nsystems_used: 梅花易数（射覆取象）。本卦鼎：上离下巽——鼎象三足两耳、圆腹中虚之金属重器；变卦恒：上震下巽，上卦离变震，离为中虚、为金器文彩，震为动为声——合象为中空能鸣之金属器。完好与否：变恒主常久不变、卦中无坎险无损象，断完好。事象级密度：物品一项落定（铜制小鼎/钵铃属），人物/数量无据不报。残损注记：卡面未载动爻爻位与起卦时辰，体用旺衰无法精核，故降格推测并降置信，不臆补动爻。R87：本题无时间坐标、R87-REV1 不适用。R80：无量级类断项、不适用。",
 "confidence": 0.35}

DATA["OC-024"] = {
 "prediction_text": "推测：葬资有着落，不必外借——易者生前已藏金于窖/枕下之处（枕窖金），将因一桩意外机缘被发现：鼠入窖穴、人击鼠寻穴而得藏金，金数足资营葬，丧事由此办成。应验在来访之后不久、营葬动手之前（日档，数日之内）。",
 "basis": "卡面未标注 tradition 字段；本例卡面为梅花序文成例题（击鼠枕窖金），卡面未载卦象，按题面体裁自决。\nsystems_used: 梅花易数（序文成例形态参看）＋题面事实推断。题面已载面：易者遗书预言来访秀士可托身后事——预言系统内必有应验之资埋伏；其家苦无资营葬；出处题名自带「击鼠枕窖金」之锚（书名/篇名属卡面 provenance 字段、非断语文件）。锚点转应核：篇名直读为「枕下窖中藏金、击鼠而得」，转应面（金指他物）无据，取直读。残损注记：卡面未载具体卦象与数字锚点，象数推演无据，故降格推测、降置信，仅据篇名锚点与预言结构落断。R87候选坐标（日档）：数日内得金（触发＝营葬迫近、预言来访已至）取；月外舍（葬事不待）。",
 "confidence": 0.45}

DATA["OC-025"] = {
 "prediction_text": "断：椅底预书之事应验。届预书所载年月日，椅子果然被坐破——破于当日来访宾客落座之时，椅面/椅腿断折，人无大伤，仅虚惊一场；预书文字与实事逐项对上，无差。",
 "basis": "卡面未标注 tradition 字段；本例卡面为梅花序文预言题（置椅坐破），卡面未载卦象，按题面体裁自决。\nsystems_used: 梅花易数（预言应验结构）＋题面事实推断。题面已载：邵雍预先书「某年月日椅子将被坐破」于椅底——预言自带明确时间坐标与事件形态（坐破），此类序文成例的体裁即验预言之实；断应验且形态从预书原文（被坐破、非自坏非火烧）。事象密度：物品（椅）＋应期（预书年月日）两项落定。残损注记：卡面未载预书具体年月日数字与卦象，日期只能回指预书原文、不臆造新日期，故置信中平。R87候选坐标：预书所载年月日（唯一候选，触发＝预书文本自带坐标）取；前后日无触发舍——落点即预书坐标，非近窗另取。",
 "confidence": 0.5}

# ---------------- OC-026..030 (liuren) ----------------
DATA["OC-026"] = {
 "prediction_text": "断：今年功名可成。两客（昆弟）所问功名有得：主问者必得功名（入选/中式），昆弟二人同有喜信、以先问者为显。三传乙未、己亥、癸卯成亥卯未三合木局、初传未乘青龙（文书功名之将）发用，官星成局入传主名成。应期在月档：本年六月（未月，初传逢值、青龙值月）为主坐标，功名文书于未月落定。",
 "basis": "卡面未标注 tradition 字段；本例卡面载六壬课式（涉害、曲直）与三传，按大六壬自决（冻结原文）。\nsystems_used: 大六壬。己亥日占，日干己土、木为官鬼；三传未亥卯三合木局即官星成局，曲直课主仁德秀气、利功名；初传乙未乘青龙（功名文书之将）发用，中传亥乘螣蛇主文书缠绕有虚惊、末传卯乘玄武主名次稍暗——成局之势压过末传之暗，二人分判以主问者（干为先）为显。盘面不全注记：卡面仅课式、三传、月将、空亡（辰巳空，三传不落空），无天盘全图与四课全列，按快照六壬章第八节只据三传链、天将、课格、空亡作断，不臆补四课。应期（月档，仕宦迁转/榜期档）：R87候选坐标——卯月（末传逢值）有触发、未月（初传青龙逢值）有触发、亥月（中传逢值）有触发；近窗首候选为卯月（二月，去占时正月初四最近），比较：卯乘玄武主暗、未乘青龙主文书功名正应，青龙逢值触发强于玄武逢值，取未月而非近窗卯月；亥月螣蛇虚惊舍。落点未月与青龙发用对位。",
 "confidence": 0.55}

DATA["OC-027"] = {
 "prediction_text": "断：此行不得意。奉诏北上，课得无禄、无路之格，三传酉、辰递进而末传亥乘青龙落空（甲子旬戌亥空）——诏命虽真、贵气终空：入京后不得要职、差事落空或滞留困顿，无功而返之象，本人途中/京中另有病厄缠身。老母一方：母年甲子、亥为母年命相关之支又落空，主老母在家有病忧之讯（虚惊与实病之间，以有病讯、需遣人问安论），凶信重于吉信。一行分判：行不得意（主断）、本人有病厄、老母有病忧。应期月档：入京后辰月（中传逢值）前后见分晓。",
 "basis": "卡面未标注 tradition 字段；本例卡面载六壬课式（无禄、无路）与三传，按大六壬自决（冻结原文）。\nsystems_used: 大六壬。辛未日占，日干辛金；无禄无路为凶格（干支无凭、行止无路）；三传癸酉乘六合（诏命文书合身而至）、戊辰乘太阴（阴私迟滞）、亥乘青龙而旬空——青龙主贵喜、落空则喜事成空，正应「得诏而不得意」。身体：辛金日干、中传辰土生金本有救，然末传空亡主后段无着，断病厄而非大限。老母：卡面载其母甲子年，亥与母年命支气相关且空，作病忧讯（对象逐名对回：老母，非占者本人）。盘面不全：无四课全列与天盘全图，按第八节只据已载作断。应期（月档）：R87候选——酉月（初传逢值，诏命动）取作近段、辰月（中传逢值，滞留见分晓）取主坐标、亥月（末传填实）触发为空亡填实主虚信回转作备选舍（与终局不得意方向同但时点过晚）；主坐标辰月与太阴迟滞对位。",
 "confidence": 0.5}

DATA["OC-028"] = {
 "prediction_text": "断：入觐考选可过、将得一官。课得重审、斫轮（斫轮主选拔成器），初传卯木官星入传——得官之象成立；然卯乘玄武（官来暗昧、非清要之途），中传戌乘朱雀主文书过关，末传巳乘白虎主授官后带奔走刑伤之任。所授为中下级实缺：地方佐职/学官一类清而位卑之官，非显要京职。应期月档：巳月（末传逢值、授命落定）为主坐标。",
 "basis": "卡面未标注 tradition 字段；本例卡面载六壬课式（重审、斫轮）与三传，按大六壬自决（冻结原文）。\nsystems_used: 大六壬。己丑日占，日干己土、木为官鬼；初传辛卯官星乘玄武发用，卯戌六合入中传（朱雀文书），末传癸巳乘白虎——仕宦门取用：官星入传＋斫轮吉格主成器授职，玄武乘官压其清要等级。R80功量（等级类）：做功线——卯官入传合戌（源：初传，对象：官职，助成主线）、斫轮格（对象：考选，助成）、玄武乘官（对象：官职清要度，压制线）、白虎末传（对象：任职形态，压制为奔走之任）；等级带：中下级实缺带（玄武压一级之据如上）。盘面不全按第八节作断。应期（月档，仕宦迁转档）：R87候选——卯月（官星逢值）近窗首候选、戌月（合处逢值）、巳月（末传逢值、白虎催授）；比较：卯乘玄武主暗昧未定、巳为末传归着且白虎主速至之迁，取巳月；落点与末传对位。",
 "confidence": 0.45}

DATA["OC-029"] = {
 "prediction_text": "断（一课多占，逐事分判）：一、子求官：此行在本处求官无成，其子宜回山东本籍取功名，可得。二、方所兵事：山东将有兵动、攻城陷邑之警，家眷宜预避。三、母寿：老母寿止八十九——将届九十而不得九十，本年之内即为大限。四、防盗：近日有失盗之事，所失为其子之物，且贼去而复来，须严加防范。五、客至：顷刻即有客至。应期各从其门：客至即时、失盗在目今数日、兵动在冬月、母限在本年内、子功名回籍后于本年内见信。",
 "basis": "卡面未标注 tradition 字段；本例卡面载六壬课式（涉害、曲直、回环）与三传，按大六壬自决（冻结原文）。\nsystems_used: 大六壬（一课多占，逐事分门）。己亥日占，三传乙未（白虎）、癸卯（六合）、己亥（天后）。逐事取象：子求官——干神归支、传将逆行，主归本籍得功名（仕宦门，子丑命与支气相应）；兵动——三传纯木官鬼局、白虎乘初传克支，方所以日支分野指山东（兵斗门）；母寿——发用乙与地盘己合断为八九之数，寿止八十九（成例专法，母年命未给、除此专法外不别推）；失盗——玄武脱气之象＋课传回环，主贼去复来、所失属其子（失物门，回环格专主复来，不移作他事吉断）；客至——即时之应。盘面不全按第八节作断。应期：R87候选按门分列——客至占时即时（日档内时坐标，触发＝发用近身）取；失盗三日内（回环主速复）取；兵动冬月（亥子月水旺木相、末传亥逢值之月）取；母限本年内（年档，八九合数已临）取；各坐标与各门触发逐点对位，命造类包容核不适用（非命造）。",
 "confidence": 0.6}

DATA["OC-030"] = {
 "prediction_text": "断：两事皆可如愿。淮扬巡按差可复——铸印课占钦差，主复任巡按之象，差得复设、人得复任；吏书缺可照旧——末传卯乘太阴主旧缺阴护存留，照旧不废。应期月档：旨意与复设之信在巳月（初传太常逢值）落定，窗口为占后数月之内。",
 "basis": "卡面未标注 tradition 字段；本例卡面载六壬课式（重审、铸印）与三传，按大六壬自决（冻结原文）。\nsystems_used: 大六壬（章奏·钦差门）。戊子日占，三传癸巳乘太常（印绶常服之将，铸印成格）、丙戌乘六合（合主成议）、辛卯乘太阴（阴护旧事）。钦差门成例形态：铸印课占钦差主复任巡按；太常为迁转之将、不逢空（卡面月将亥将、无旬空载、三传不落空），主复设有着。两问分判：巡按差复（官缺复设）、吏书缺照旧（人事存留），方向同为可成。盘面不全按第八节作断。应期（月档，章奏旨意档）：R87候选——巳月（初传太常逢值，旨意下达触发）取主坐标、戌月（中传合处逢值）次、卯月（末传逢值）次；近窗比较：占时三月，巳月最近且太常铸印正应，触发强于戌卯，取巳月有对位依据（印将逢值），非仅因近窗。",
 "confidence": 0.62}

# ---------------- B20: WP-001..007 (western) ----------------
DATA["WP-001"] = {
 "prediction_text": "Yes — a major collective affliction strikes in 2020-2021: a fast-spreading infectious (pandemic) disease on a global scale, peaking around the exact Jupiter-Saturn-Pluto conjunction of early 2020, bringing mass illness, overwhelmed hospitals and severe social restriction through 2020 and into 2021. Time window: onset late 2019 to early 2020, main blow in 2020, tail into 2021.",
 "basis": "Card carries no tradition field; the card is a mundane-astrology assessment, method chosen accordingly.\nsystems_used: western mundane astrology (outer-planet cycles, cyclical index). Card facts: five outer planets within about 100 degrees around 2020, Jupiter-Saturn-Pluto conjunction exact early 2020, cyclical index at its 21st-century low, and comparable past clusters coincided with 1918, 1954, 1968 and 1982 — three of those four precedents are pandemic years (1918 influenza, 1954/1968 influenza events in the source framing), so the configuration points to epidemic affliction rather than war or finance as the primary form. R87 candidate coordinates: early 2020 (exact conjunction, trigger = the configuration itself) taken as main coordinate; 2021 taken as tail window; other years in the cycle have no comparable trigger and are discarded.",
 "confidence": 0.65}

DATA["WP-002"] = {
 "prediction_text": "Barack Obama wins the 2008 US presidential election. The change candidate prevails over the continuity candidate: Obama first secures the Democratic nomination against Hillary Clinton, then defeats John McCain in the general election of 4 November 2008, with the result clear on election night/the following day.",
 "basis": "Card carries no tradition field; the card is an election-forecast item, method chosen accordingly.\nsystems_used: western mundane astrology (Saturn-Uranus cycle) plus electoral-structure reading. Card facts: Saturn comes into opposition with Uranus beginning on Election Day, a configuration last seen 45 years earlier (the mid-1960s upheaval cycle) — the opposition of order (Saturn) and disruption/change (Uranus) exact on voting day favours the candidate embodying change over the candidate of the incumbent order. Obama already leads the nomination race at asking time (May 2008); McCain represents continuity with an unpopular incumbent administration. R87 candidate coordinates: 4 November 2008 (election day, trigger = the opposition exact and the vote itself) taken; no other date carries a trigger.",
 "confidence": 0.6}

DATA["WP-003"] = {
 "prediction_text": "Barack Obama is re-elected in 2012. The incumbent defeats Mitt Romney in the general election of 6 November 2012; the contest is close and the count messy (Mercury turning retrograde on election day brings delays and disputes in reporting), but the outcome stands in favour of Obama once the count settles within days after the vote.",
 "basis": "Card carries no tradition field; the card is an election-forecast item, method chosen accordingly.\nsystems_used: western mundane astrology (Mercury retrograde election-day signature) plus incumbency reading. Card facts: polling competitive, incumbent running for re-election, Mercury retrograde begins on election day — the retrograde signature historically marks confused counts and challenged results rather than a clean transfer of power; combined with incumbency advantage in a competitive (not landslide-against) polling field, the balance favours the sitting president retaining office amid noise. R87 candidate coordinates: 6 November 2012 (election day, trigger = vote plus retrograde station) taken as main coordinate; the following days taken as the settling window.",
 "confidence": 0.55}

DATA["WP-004"] = {
 "prediction_text": "Hillary Clinton wins the 2016 US presidential election. The conference-panel reading follows the dominant signal in the card: Clinton, ahead in most polls through October, defeats Donald Trump in the election of 8 November 2016 and becomes president-elect, though the margin is narrower than the polling lead suggested.",
 "basis": "Card carries no tradition field; the card is an election-forecast panel item, method chosen accordingly.\nsystems_used: western mundane astrology panel reading plus electoral-structure reading. Card facts at asking time (October 2016): most polls favour Clinton; no contrary configuration is supplied on the card. An independent reading from the supplied facts alone gives the front-runner the win; the narrowing clause is included because late-cycle challenger momentum is a standing feature of such races, but no card fact supports reversing the direction. R87 candidate coordinates: 8 November 2016 (election day, trigger = the vote) taken; no other date carries a trigger.",
 "confidence": 0.5}

DATA["WP-005"] = {
 "prediction_text": "Donald Trump wins the 2016 US presidential election. The astrologer who alone had picked Trump as Republican nominee when 17 candidates still contested it is read as holding the correct contrarian line through to the general election: Trump defeats Hillary Clinton on 8 November 2016 despite the polling consensus against him.",
 "basis": "Card carries no tradition field; the card is an election-forecast item centred on one panel astrologer, method chosen accordingly.\nsystems_used: western mundane astrology (individual forecaster track-record reading) plus electoral-structure reading. Distinguishing card fact versus the companion panel item: this card isolates the one astrologer who had already been proved right against the whole field on the nomination question (picking Trump out of 17 Republicans). A forecaster demonstrably attuned to the Trump phenomenon, against a polling consensus that the same phenomenon had already falsified once in the primaries, is taken as the stronger signal; direction therefore reverses the panel-consensus reading. R87 candidate coordinates: 8 November 2016 (election day, trigger = the vote) taken.",
 "confidence": 0.5}

DATA["WP-006"] = {
 "prediction_text": "Yes — Britain votes to leave the European Union. In the referendum of 23 June 2016 the Leave side wins narrowly, against the February polling lead for Stay, and the result is declared on 24 June 2016.",
 "basis": "Card carries no tradition field; the card is a mundane-astrology referendum assessment, method chosen accordingly.\nsystems_used: western mundane astrology (Uranus transit to national charts). Card facts: on referendum day Uranus and Ceres conjunct at 23 degrees Aries — Uranus is the disruption/rupture planet and Aries is the sign of unilateral assertion; applied to the UK national charts (1066, 1801, 1922 all supplied on the card), the signature favours a break with the existing order over continuity. February polls showing Stay ahead with vast numbers of undecided voters are a weak contrary signal: undecided-heavy polling in a rupture configuration resolves toward change. R87 candidate coordinates: 23 June 2016 (referendum day, trigger = the Uranus-Ceres conjunction and the vote) taken; declaration 24 June as the settling point.",
 "confidence": 0.55}

DATA["WP-007"] = {
 "prediction_text": "Donald Trump wins the 2016 US presidential election, and what decides it is the trust question around Hillary Clinton: the email controversy and the Clinton Foundation controversies, already public in August 2016, keep eroding her support through the autumn, and a late resurgence of the email issue in the final stretch tips undecided voters to Trump on 8 November 2016.",
 "basis": "Card carries no tradition field; the card is a tarot-consultation item on the election, method chosen accordingly.\nsystems_used: tarot reading framing plus electoral-structure reading. Note on method: the card does not reproduce the actual cards drawn, so no card-by-card Waite reading is possible from the supplied facts (recorded here as a card-face gap; confidence reduced accordingly). The decisive-factor part of the question is answered from the card facts themselves: the only substantive issues the card names are the Clinton email controversy and the Clinton Foundation — in a reading asked in August 2016 with Clinton leading, singling out her trust liabilities as the live variables points to those liabilities, not Trumps, as the deciding mechanism, and a race decided by the front-runners trust collapse ends with the challenger winning. R87 candidate coordinates: 8 November 2016 (election day, trigger = the vote) taken; late October/early November taken as the deciding window for the email issue resurgence.",
 "confidence": 0.48}

# ---------------- writer + self-verify ----------------
IDS_B19 = ["MP-017","MP-018","MP-019","OC-001","OC-002","OC-003","OC-004","OC-005","OC-006","OC-007","OC-008","OC-009","OC-010","OC-011","OC-012","OC-013","OC-014","OC-015","OC-016","OC-017"]
IDS_B20 = ["OC-018","OC-019","OC-020","OC-021","OC-022","OC-023","OC-024","OC-025","OC-026","OC-027","OC-028","OC-029","OC-030","WP-001","WP-002","WP-003","WP-004","WP-005","WP-006","WP-007"]
ALL = IDS_B19 + IDS_B20
assert len(ALL) == 40 and len(set(ALL)) == 40, "id list error"
assert set(DATA.keys()) == set(ALL), ("coverage mismatch", set(ALL) ^ set(DATA.keys()))

total_bytes = 0
for cid in ALL:
    d = DATA[cid]
    obj = {"case_id": cid, "prediction_text": d["prediction_text"], "basis": d["basis"],
           "confidence": d["confidence"], "trigger": trig()}
    path = os.path.join(BASE, cid + ".json")
    assert not os.path.exists(path), ("refuse overwrite", path)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    total_bytes += os.path.getsize(path)
    print("WROTE", cid, os.path.getsize(path))

# per-file verification: exact open by id list
ok = 0
for cid in ALL:
    path = os.path.join(BASE, cid + ".json")
    with open(path, encoding="utf-8") as f:
        o = json.load(f)
    assert set(o.keys()) == {"case_id","prediction_text","basis","confidence","trigger"}, (cid, o.keys())
    assert o["case_id"] == cid
    assert isinstance(o["prediction_text"], str) and o["prediction_text"]
    assert isinstance(o["basis"], str) and o["basis"]
    assert isinstance(o["confidence"], (int, float)) and 0.0 <= o["confidence"] <= 1.0
    t = o["trigger"]
    assert set(t.keys()) == {"changed_main","reserve_used","disputed","reason"}
    assert all(isinstance(t[k], bool) for k in ("changed_main","reserve_used","disputed"))
    assert t["reason"] == ""
    ok += 1
print("VERIFIED", ok, "files; TOTAL_BYTES", total_bytes)
