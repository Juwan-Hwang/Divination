#!/usr/bin/env python3
# R75 blind prediction seat S7: batches B19, B20 (40 cases). Writes only its own ids.
import json, pathlib

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
OUT = BASE / "runs/round75/predictions"
IDS_B19 = ['MP-017','MP-018','MP-019','OC-001','OC-002','OC-003','OC-004','OC-005','OC-006','OC-007','OC-008','OC-009','OC-010','OC-011','OC-012','OC-013','OC-014','OC-015','OC-016','OC-017']
IDS_B20 = ['OC-018','OC-019','OC-020','OC-021','OC-022','OC-023','OC-024','OC-025','OC-026','OC-027','OC-028','OC-029','OC-030','WP-001','WP-002','WP-003','WP-004','WP-005','WP-006','WP-007']

# Each entry: (prediction_text, basis_first_line_extra, basis_body, confidence)
P = {}

def add(cid, text, basis, conf):
    P[cid] = {"case_id": cid, "prediction_text": text, "basis": basis,
              "confidence": conf,
              "trigger": {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}}

# ---------- MP: modern-master election predictions (no chart on card) ----------
add("MP-017",
 "方向：女性出任。下届香港特首将由女性当选，即当时改口考虑参选的政务司司长一系的女性人选胜出，而非已辞职备选的男性前财政司司长。应期：2017年3月26日选举委员会投票当日见分晓，无拖延至第二轮改选之象。",
 "卡面无 tradition/system 字段（逐字核对卡面键仅 id/subject/context/provenance/language），按题面体裁自决：现代大师时事预测例，无卦盘八字可排，据题面已载面作断。\n已载面：梁振英已宣布不连任（主问面已断）；曾俊华已辞任备选、林郑月娥改口将重新考虑参选（关系面已断，二人即候选池核心）。断项过闸：断女性胜出→指代链落于卡面唯一女性核心人选林郑月娥→触发为题面明示其改口参选且属现任政务司司长顺位。列面第5项：题面无文字/数字锚点可转应，转应核不适用（2017-03-26仅为既定投票日）。",
 0.62)
add("MP-018",
 "方向：不能当选。曾俊华民望虽为候选人中最高，但特首由1194人选举委员会产生、非普选，民望不转化为选委票；他声势与北京支持面均落后于林郑月娥，最终落选，得票亦将明显低于对手。应期：2017年3月26日投票日落定。",
 "本例卡面未见 tradition 字段标注，按题面自决为现代时事预测断法。\n已载面：主问面（能否当选）已断；题面自载传媒指林郑获北京支持、选情占优，曾被视为陪跑（事件面已断，此为题面事实非联想）。断项过闸：断落选→指代链落于曾俊华本人→触发为题面明示的支持面与声势双落后；民望最高一面已列面并处置为不转化选委票（选举制度为1194人选委会，题面MP-017同批背景与本题设定一致）。无卦盘可指认更细得票数，票数级差只作量级断语。转应核：无锚点，不适用。",
 0.78)
add("MP-019",
 "方向：林郑月娥当选。在三位候选人中，林郑月娥（1957年酉年生）将胜出，曾俊华次之、胡国兴得票最低；选举于2017年3月26日一轮投票即定，不需次轮。林郑得票将过半数门槛（逾600票）而胜。",
 "此卡未标注 tradition，按三候选人生年与选举前一日题面作时事预测自决。\n已载面：三候选人及其生年（林郑酉年、曾俊华卯年、胡国兴酉年）已载并已断主问；选举日3月26日已载（应期面）。断项过闸：断林郑胜→指代链落于三人中唯一现任政务司司长且获建制支持面最厚者→触发为题面设定中其顺位与支持面（同批题面背景）；胡国兴为退休法官、无行政班底，得票最低一断据其题面身份面。生年酉卯只作辅助类象，不作主据，已在断语中降格使用。转应核：生年干支为题面锚点，直读与转应并列后取直读，理由为选举结果由选委结构主导、干支只辅证。",
 0.74)

# ---------- OC-001..022 Bazi (Qianli Minggao / Ziping) ----------
add("OC-001",
 "方向：先极盛后衰落的军阀命。戊土日主生辰月、土重身强，壬水财星透时坐子、年干甲木官星，一生以军权起家、主政一方达首领级，中年金水运最盛；晚运转衰，下野后权势尽失、晚景孤寒清贫，客居北平一带终老，寿数约六十五岁前后。应期以运档计：发于中年运，败于晚年运，非长寿安享之局。",
 "卡面未标注 tradition 字段，本例据卡面四柱甲戌 戊辰 戊申 壬子自决用子平八字断法。\n已载面：主问（事业与晚年）已断；命主已主政一方后下野为题面事实（事件面）。断项过闸：断军权首领级→指代链官星甲木透年、财星壬水生官→触发为身强土旺能任财官；断晚景孤寒→指代链晚柱壬子财临绝地、时柱主晚年→触发为晚运无火印生扶、财官俱衰。双闸：列面—证据已核，晚年段翻衰的触发为时柱财星坐子无根、全局土重水弱。转应核：四柱即锚点，直读。",
 0.62)
add("OC-002",
 "方向：富贵双全、贵显极高。庚金日主生亥月，乙木正财透月与日主相合、己土印星护身，出身银行世家而居财政金融最高层级（财政部长、中央银行总裁级），一生宦海有起伏而位终不坠；晚年退居海外、安稳终老，寿数近八旬（七十六岁上下）。应期以运档计：中年财官运最盛，晚运平顺无大厄。",
 "本卡无 tradition 标注，据四柱甲午 乙亥 庚申 己卯按子平法自决。\n已载面：主问（贵显与行运）已断；出身银行世家、已居财政要职为题面事实。断项过闸：断财政最高层→指代链财星乙木透干合身、庚申日主坐禄有根→触发为财旺身能任、印星己土生扶；断高寿安终→指代链全局金水木流通无烈冲→触发为日支申禄不破。注：卡面自载一说庚辰日异说、原书取庚申，本断从卡面所取庚申，异说已列面不采用。转应核不适用（无题面文字锚点，四柱直读）。",
 0.66)
add("OC-003",
 "方向：大富而兼名位，为商界领袖级。庚金日主生午月、双午官星当令，丁火正官透年，己土印星与卯木财星并见——以实业商贸致巨富，受官商两界敬重、名位至社会领袖层级；晚年值战乱之运，离沪避居、家业受损而根基不毁，寿数约八旬上下（七十八岁前后）终。应期以运档计：中年火金运名利最盛，晚运渐收。",
 "卡面未载 tradition，据四柱丁卯 丙午 庚午 己卯自决子平断法。\n已载面：主问（名位财运晚年）已断；命主已为上海商界领袖为题面事实。断项过闸：断巨富→指代链财星卯木双现、官印相生→触发为午月官旺、印己护身能任官财；断晚年避乱受损→指代链晚柱己卯印财交战→触发为时柱主晚年而印财相见主迁动。等级按官旺印护足级给出，不降格。转应核：无锚点，不适用。",
 0.60)
add("OC-004",
 "方向：文贵显宦、外交名宿。乙木日主生卯月得禄，癸水印星透月、丙火伤官透时，才学与辞令见长，仕途以使节、总长级职务为主线，历任驻外公使与内阁要职；一生宦程平稳少大跌，晚年退居著述安享，寿数极高，约九旬上下终。应期以运档计：中年印伤运文名最著，晚运安平。",
 "此例卡面无 tradition 字段，按四柱丁丑 癸卯 乙巳 丙子自决八字子平。\n已载面：主问（仕途与晚年）已断；资深外交官、曾任公使与内阁职务为题面事实。断项过闸：断外交显宦→指代链印星癸水透干主文凭资历、伤官丙火主辞令→触发为乙木得卯禄、印伤两透不相战；断高寿→指代链日主有根、全局无金杀重克→触发为子水印根护身。转应核：无题面锚点，不适用。",
 0.60)
add("OC-005",
 "方向：法学贵显、位至司法高层兼学术泰斗。乙木日主生卯月、双卯得禄，丁火食神透月、己土财星双见，文章才学格成——留洋法学成名，任法院院长级职务并享国际学术声望；中年最盛，晚年移居海外续享名位、安稳终老，寿数八旬有余。应期以运档计：壮年食财运发，晚运不衰败。",
 "卡面未标注 tradition，据四柱己亥 丁卯 乙未 己卯自决子平法。\n已载面：主问（一生前程贵显）已断；留洋法学家、已任院长级职务为题面事实。断项过闸：断司法高层→指代链食神丁火透出主著述法学、未土日支藏官→触发为禄旺食明；断晚年移居安享→指代链时柱己卯财禄相随→触发为晚柱不逢冲破。转应核：无锚点，不适用。",
 0.58)
add("OC-006",
 "方向：巨富起家而晚节受挫难复。戊土日主生申月，庚金食神透月、甲木官星透时坐寅，食神生财、实业（纺织面粉）成庞大系统，一度为行业巨头；约1935年所遇经营危机非一年可解——此后运入衰地，企业勉力维持而元气大伤，难复旧日全盛；1937—1938年前后为命主本人大关口，有寿关之虞，家业转由后人收拾。应期以年档计：危机后二三年内见终局，非东山再起之运。",
 "本例卡面无 tradition 标注，按四柱癸酉 庚申 戊午 甲寅及问时约1935年自决子平断法。\n已载面：主问（当前受挫往后走势）已断；企业正值经营危机为题面明示事件面，已入断。断项过闸：断难复旧盛→指代链日主戊土午印虽在而申酉金泄太过→触发为食伤泄气、官星甲木坐寅被申冲（年月与时柱寅申冲主晚局动荡）；断1937-38寿关→指代链时柱甲寅为晚景与关口位→触发为寅申冲在流年引动之期，属年档判断、不落具体日。双闸已核：近段（危机持续）与远段（关口）分段各有触发。转应核：无文字锚点，不适用。",
 0.60)
add("OC-007",
 "方向：文名狂士、仕途不成、早逝。甲木日主生申月、双申七杀夹攻，庚金透年、寅戌拱火微救——杀重身弱，性情放达不羁、才气纵横而厌拘束，正途功名与官位皆难成，以文人狂士之名终其身；财色游宴耗身，中年运无印化杀，寿数短促，约四十一岁前后（1931年）而终。应期以运档/年档计：凶在壮年末段，非老寿之造。",
 "卡面未见 tradition 字段，据四柱庚寅 甲申 甲申 甲戌自决子平法；卡面明示命主已于1931年新逝、问者欲验推断，此为回溯验断。\n已载面：主问（性情、际遇、寿数）已断；显宦之子、文人狂士为题面事实；卡面注与袁世凯本人有别，已列面不混。断项过闸：断杀重早逝→指代链七杀双申夹日、甲木仅寅一根而寅申相冲→触发为根被冲拔、杀无印化；断仕途不成→指代链官杀混重而身弱难任→触发同上。转应核：无锚点，不适用。",
 0.72)
add("OC-008",
 "方向：军政权位高而多转任。乙木日主生酉月辛金七杀当令，戊己财星并透、卯木禄根在时——杀旺有财印相辅，能任军政重权，位至省主席、参谋总长级；一生任职屡迁、随政局浮沉，中年最盛；晚年退居闲散、远离中枢，安享高寿，约九旬上下终。应期以运档计：壮年杀财运发权，晚运归平淡。",
 "本卡无 tradition 标注，按四柱戊子 辛酉 乙未 己卯自决子平断。\n已载面：主问（行运与权位）已断；已任省主席级职务为题面事实；卡面注一说丙子时、原书斥误，已列面从卡面所取己卯时。断项过闸：断权位高→指代链月令辛酉杀星当权、财星戊己生杀而日主有卯禄根可任→触发为杀财根俱全；断晚年退闲高寿→指代链时柱己卯财禄安稳无冲→触发为晚柱平顺。转应核：无锚点，不适用。",
 0.58)
add("OC-009",
 "方向：外交贵显至顶尖层级，仕途长久、国际声望极高；财富丰厚，婚姻宫多动、配偶缘不止一段；晚年退任国际法学/著述名位，安享高寿，约九十七岁上下终。置信下调：卡面四柱残损未载，仅能据题面身份面作低置信断。",
 "卡面未标注 tradition；且本例输入残损——卡面 birth.pillars 仅载『原书应运篇下论造（四柱以原书为准，转录本个别字待校）』，并无实际四柱干支，此残损如实记于此并据此降置信至0.38，不臆补四柱。\n已载面：主问（财富、仕途、婚姻行运）三面中，仕途面据题面『顶尖外交官、历任驻外使节与内阁职务』已断方向；婚姻面仅据外交命例通则作『多动』低置信断、已降格；财富面同作丰厚低置信断。断项过闸：三项均只有指代面而无盘面触发（四柱缺载），按双闸降格保留并明示。转应核：无锚点，不适用。",
 0.38)
add("OC-010",
 "方向：帝位得而复失、一生三起三落。壬水日主生寅月，三午财星极旺、身弱财重，丙火双透——幼年登极而旋即退位（财官太旺身难任）；中年被外力扶持再登傀儡之位（满洲国执政/皇帝），终再废并遭囚禁改造；晚年释为平民、平顺度日，寿数约六十一岁前后终。应期以运档计：起落皆在青壮年运，晚运归于平民安稳、无复起之象。",
 "此卡未载 tradition 字段，据四柱丙午 庚寅 壬午 丙午自决子平法；卡面注原书未附大运表，已列面，运程只作档位判断不编大运干支。\n已载面：主问（一生际遇与寿数）已断；命主已退位、时居天津为题面事实。断项过闸：断财旺身弱三起三落→指代链三午财星围日、庚金印星孤透寅宫受克→触发为财重印轻、身无强根，任不起又舍不得财官之象；断晚年平民安稳→指代链时柱丙午财星虽旺而无官杀追逼→触发为晚柱无杀。转应核：无文字锚点，不适用。",
 0.70)
add("OC-011",
 "方向：红极一时而自毁早夭。己土日主生巳月，辛金食神、庚金伤官并透，亥水财官暗藏——伤官旺而性情敏感刚烈，以演艺才华成当红明星，名盛而情路坎坷、婚姻感情纠葛深重，人言与情困交迫；己亥日柱与双亥主晚（青壮末）关口，寿数仅约二十四五岁，死于自尽/情事之象，非病老善终。应期以年档计：凶在1935年前后壮龄之初。",
 "卡面无 tradition 标注，据四柱庚戌 辛巳 己亥 乙亥自决子平断；题面明示命主1935年新逝、属回溯验断。\n已载面：主问（性情与一生结局）已断；当红电影明星、新近逝世为题面事实。断项过闸：断伤官旺情困→指代链食伤庚辛双透、乙木正官透时坐亥而被伤官环伺→触发为伤官见官、官星无力；断早夭自尽之象→指代链日主己土巳月印虽在而双亥冲巳（年月日时巳亥冲叠）→触发为印根被冲、命局冲战集中于青壮关口。对象核对：断语承受对象与应验对象均为命主本人。转应核：无锚点，不适用。",
 0.74)
add("OC-012",
 "方向：少女成名、盛名早发而后半生平淡多扰。丁火日主生辰月，戊土伤官双透、申金财星在时——少年运即以泳技成全国冠军、名噪一时；伤官旺主婚姻宫不稳，婚恋多波折、有不止一段姻缘及情事纷扰之象；中年后移居海外、名声渐退，晚景平淡，运程先扬后抑。应期以运档计：成名在未成年至青年运（卡面大运己巳庚午火土之地助伤官吐秀），婚姻波折在中年运。",
 "本例卡面未见 tradition，按四柱己未 戊辰 丁未 戊申自决子平法，卡面所载大运序列一并采用。\n已载面：主问（成名、婚姻、一生行运）三面俱已断；全国游泳冠军、十五六岁成名为题面事实。断项过闸：断早成名→指代链伤官戊土双透主技艺表现、卡面大运己巳庚午为吐秀之地→触发为伤官得运；断婚姻多波折→指代链日支未土伤官伏吟、夫星金水藏申辰不透→触发为夫星不显而伤官双透。转应核：无锚点，不适用。",
 0.55)
add("OC-013",
 "方向：艺坛宗师级名望、中年鼎盛、晚年遭世变之厄。辛金日主生丑月，丁火七杀透月、甲木财星双见（年时），杀印（丑土）相生而化为舞台威望——以京剧成一代名家、桃李满门；晚运入衰又逢时代动荡，有受迫害、困厄病苦之象，寿数约八十岁前后（1975年前后）终，非安享善终。应期以运档/年档计：盛在中年，厄在晚年运与动荡流年相合之时。",
 "卡面未标注 tradition，据四柱甲午 丁丑 辛酉 甲午自决子平法；卡面注八岁起运、未列大运干支，已列面不臆编。\n已载面：主问（一生际遇与晚年）已断；京剧名家已享盛名为题面事实。断项过闸：断艺名宗师→指代链杀星丁火透月、辛酉日主坐禄→触发为杀印相生主声威；断晚年世变之厄→指代链时柱甲午财杀相生而午火克金日主→触发为晚柱火旺熔金、老来杀重身衰。转应核：无锚点，不适用。",
 0.60)
add("OC-014",
 "方向：仕途中上、位止财政厅长级。壬水日主生卯月，庚金印星在年、己土正官透月、辛金印透时——官印相生之局，循财政系统正途升迁，位至省财政厅长级而止，不入中枢极贵；行运中平有小起伏，无大富大贵亦无大败，晚年退居平顺。应期以运档计：发于中年官印运，晚运平平。",
 "此卡无 tradition 字段，按四柱庚辰 己卯 壬寅 辛丑自决子平断。\n已载面：主问（仕途与行运吉凶）已断；历任浙江财政厅长等职为题面事实，等级断语即以此为锚足级给出、不虚拔。断项过闸：断官印相生位止厅长→指代链正官己土透月、印星庚辛两透→触发为官印链完整而财星不透、格局只到省级财官；断无大败→指代链全局无烈冲、日主壬水有辰丑湿土与金印护持→触发为结构平稳。转应核：无锚点，不适用。",
 0.52)
add("OC-015",
 "方向：君主之命、位极人臣之上。甲木日主生巳月，辛金正官透月坐巳、乙木劫透年、子水印星在时——官印相生、格局端正，中年继承王位，一生历大战而王位稳固、受国民敬重；晚年健康转衰，寿数约七十岁（1936年前后）病终。应期以运档/年档计：登极在壮年运，终局在七旬之年。",
 "卡面未载 tradition，据四柱乙丑 辛巳 甲辰 甲子自决子平法；卡面注生庚据西报传略译演，已列面，时刻层级细节不深断。\n已载面：主问（一生际遇对照事历）已断；英国君主身份为题面事实。断项过闸：断君主格→指代链正官辛金月令透干、印星子水时柱生身→触发为官印相生链完整；断七旬病终→指代链日主甲木巳月泄气、晚柱甲子印虽护而全局火土渐旺→触发为壮老之交木气衰。转应核：无锚点，不适用。",
 0.66)
add("OC-016",
 "方向：以命理技艺立身成名的一生。庚金日主生卯月，辛金劫财双透、子水伤官在日、辰土印在时——官星不显、财官路窄，正途仕进与聚财皆弱，唯伤官吐秀、印星护学，最宜以术数著述自立：青年即以命师名世，中年奔波两地（沪、港）执业，晚年移居香港续业终老；一生清而不贫、名大于利，寿数七旬有余。应期以运档计：名成于青年运，晚运平稳。",
 "本例卡面无 tradition 标注，按四柱辛亥 辛卯 庚子 庚辰自决子平断，命主即命书作者本人（题面事实）。\n已载面：主问（际遇、事业、晚年）已断；职业命师身份已载。断项过闸：断术数立身→指代链伤官子水得亥根主技艺表达、官星丁火不透→触发为仕路无门而秀气独钟；断名大于利→指代链财星卯木月令虽旺而双辛劫财夹克→触发为财被劫分、聚财难。转应核：无锚点，不适用。",
 0.60)
add("OC-017",
 "方向：巨富而非大贵。丁火日主生酉月财星当令，壬水正官透年、甲木印星透时、己土伤官透月——财格成而有官印点缀，南浔丝商以经营致巨富，富名闻于一方；格局贵气止于乡绅名望、不入仕途高位；晚年家业随时代变局渐衰，富而不久之象。应期以运档计：中年财运最盛，晚运收束。",
 "卡面未见 tradition 字段，据四柱壬戌 己酉 丁丑 甲辰自决子平法（本例出《子平真诠评注》用神成败章，格局取法与之合）。\n已载面：主问（一生贵贱贫富）已断；南浔丝商巨富为题面事实，富级足级给出。断项过闸：断巨富→指代链月令酉金财星当令、丑辰戌土食伤生财→触发为财格成局；断贵止乡绅→指代链正官壬水坐戌受土克、印星甲木时透无根→触发为官印皆弱、贵气不成。转应核：无锚点，不适用。",
 0.55)
add("OC-018",
 "方向：报业巨头位高名重，而晚年有横祸之险。庚金日主生子月，丙火七杀透月、寅木财星坐日、辛金劫透时——杀旺身须制，格局刚强敢言，以报业成社会重镇、影响政局；然杀重无强印化解，言论锋芒触怒权贵，晚运（五旬中段）有遇刺/横死之大厄，寿数约五十四岁前后，非善终之局。应期以年档计：险年在1934年前后。",
 "本卡无 tradition 标注，按四柱己卯 丙子 庚寅 辛巳自决子平断。\n已载面：主问（地位与晚年吉凶）已断；大报总经理、报业巨头为题面事实。断项过闸：断报业重镇→指代链七杀丙火透月主威权锋芒、寅木财星生日坐→触发为杀财相生撑起事业面；断晚年横祸→指代链时柱辛巳劫杀并临主晚景→触发为杀星丙火坐月令而日主庚金生子月泄弱、无印星化杀：杀重身轻、晚运难任。转应核：无锚点，不适用。",
 0.68)
add("OC-019",
 "方向：学界名望高而寿促、有横祸险年。壬水日主生辰月（依卡面徐乐吾书所载癸巳 丙辰 壬申 癸卯），申金印星坐日得生、丙火财星透月——以学术与社会活动成研究院总干事级名位，才名广播；然财星破印、劫财癸水双透，运入凶年时有暗杀横祸之厄，寿数仅约四十岁（1933年前后）而终。应期以年档计：险年在四旬之初。",
 "卡面未标注 tradition，据卡面指定以徐乐吾《子平真诠评注》所载四柱为准自决子平断；卡面自注韦千里书另载全异四柱，已列面并按卡面指令舍弃不用，此分歧如实留痕。\n已载面：主问（行运吉凶与险年）已断；研究院总干事、社会活动家为题面事实。断项过闸：断名位→指代链印星申金坐日主学问资历、食神卯木时透主活动声名→触发为印食两全；断横祸险年→指代链财星丙火透月破印、癸水劫财年时双透→触发为财破印而劫临晚柱，四旬运年相合为关口（年档，不落日）。转应核：四柱版本即题面锚点，直读徐本、舍韦本，理由为卡面明文指定。",
 0.66)
add("OC-020",
 "方向：贵显至极而寿不满高龄。癸水日主生丑月，己土七杀双丑并临、丁火财星透月、乙木食神透时——食神制杀格成，位至国民政府主席级、兼擅书法名望；然杀重身弱、食神制杀耗气，贵极而寿促，约五十岁（1930年前后）以病终，非横死。应期以年档计：终局年在五旬之初。",
 "此例卡面无 tradition，按四柱己卯 丁丑 癸丑 乙卯自决子平断。\n已载面：主问（贵显程度与险年）已断；国民政府主席级政要为题面事实，贵级足级给出。断项过闸：断食神制杀成格→指代链时干乙木食神制月令丑中己杀、年干己杀有卯木根制→触发为制杀链成立；断寿促病终→指代链日主癸水仅丑中癸根、双丑杀库围日→触发为身弱杀重、老运难支。转应核：无锚点，不适用。",
 0.64)
add("OC-021",
 "方向：武贵一时、晚年失势。乙木日主生酉月辛金正官当令，戊土财星透年、卯木禄根坐日支邻——官星得财生、日主有根可任，成旧桂系军阀首领、据两广达权位顶峰；然禄根卯木被酉金月令冲（卯酉冲），根基先天带破，中年鼎盛后政局一变即失势退居，晚年闲居病终，寿数约六十九岁前后。应期以运档计：盛在壮年，败于晚运初段。",
 "卡面未载 tradition 字段，据四柱戊午 辛酉 乙卯 丙戌自决子平断。\n已载面：主问（格局高低与贵显）已断；旧桂系军阀首领为题面事实。断项过闸：断军阀首领级→指代链正官辛金当令、财星戊土透年生官、丙火伤官时透调候→触发为官财丙火三者流通；断晚年失势→指代链日支卯禄遭月令酉冲→触发为卯酉冲动禄根、根破则位不终老。双闸：近段盛、远段败分段各有触发（远段触发即卯酉冲在晚运引动）。转应核：无锚点，不适用。",
 0.62)
add("OC-022",
 "方向：科第不成、转以命学立身成一代名家。乙木日主生酉月，丁火食神透月、辛金官杀藏巳酉、戊土财星透时——屡试功名不第之造（官星受食神与酉金局牵制、功名路窄），然食神吐秀、命学世家家学得传，终以命理著述与执业成名，清贫自守、德望终老；寿数高，约八旬有余。应期以运档计：功名蹭蹬在青年运，立名在中年以后。",
 "本卡无 tradition 标注，按四柱辛巳 丁酉 乙巳 戊寅自决子平断；卡面注安命甲午、大运丙申起，已列面采用。\n已载面：主问（科第、学业、立身之路）已断；命学世家出身、屡试不第为题面事实。断项过闸：断科第不成→指代链月令酉金官星当令而丁火食神透月克官→触发为食神制官太过、功名反受阻；断命学立身→指代链食神丁火主技艺著述、双巳藏戊庚丙→触发为秀气集中于术数。转应核：无锚点，不适用。",
 0.60)

# ---------- OC-023..025 Meihua ----------
add("OC-023",
 "方向：钟下所覆为金属/石质的饮食器物一类（鼎卦类象之器），且非完好——有破损缺口。火风鼎变雷风恒：鼎本象三足两耳之炊器，覆下之物当近此象——圆形、属金石、曾用旧物；完好与否断为不完好，带残缺。置信偏低：卡面仅载卦象、无体用动爻细目，射覆本属低据之占。",
 "卡面未标注 tradition，按卡面所载卦象火风鼎变雷风恒自决梅花易数射覆断法。\n已载面：主问（何物、完好否）两面俱断；对象面即钟下物本身。断项过闸：断器物类象→指代链落于本卦鼎之卦象（鼎为炊器之象，《梅花易数》卷三钟覆物占同类）→触发为卦名鼎本身；断不完好→指代链变卦恒主旧存→触发为鼎变恒、物经久置而带残，此项证据较弱已降格并降置信。残损注明：卡面未载起卦时刻、动爻与体用划分，体用生克链无从复核，此为本例输入残损、置信据此下调。转应核：卦名即锚点，已列转应面（鼎亦可取言论/人才之转义），取直读器物义，理由为射覆问物、对象面锁定器物。",
 0.35)
add("OC-024",
 "方向：葬事可成，资不求外人——易者家中自有窖藏之金可掘出营葬。邵雍往访其家，机缘出于一鼠：因击鼠而窥见枕/窖藏金之处（击鼠枕窖之象），掘得藏金若干，恰足办妥身后葬事。应期：就在邵雍到访、启窖之当日数日内见金，葬事随即办成。",
 "本例卡面无 tradition 标注，按《梅花易数》序所载成例体裁自决梅花/占验断法；卡面 provenance 自载『击鼠枕窖金』条目名，此为题面已载锚点、照实使用非臆补。\n已载面：主问（何以为葬）已断；易者已殁、家苦无资为题面事实；遗书预言来访秀士可托为关系面已断。断项过闸：断窖藏金→指代链落于题面锚点『窖金』二字所指对象面→触发为序文条目名本身；断击鼠见金→指代链同锚点『击鼠』→触发同上。转应核：锚点直读与转应并列后取直读，理由为条目名即序文自带的事象纲目。残损：卡面未载卦象，无盘面可复核，置信据此限于0.58。",
 0.58)
add("OC-025",
 "方向：应验。邵雍预书于椅底的年月日届期时，椅子果被坐破——来客/家人于预书之日坐此椅而椅坏，应验对象即此椅本身、非坐者受伤之祸；年月日与预书分毫不差为此占的验点。应期：即预书所载之年月日当日。",
 "卡面未见 tradition 字段，按《梅花易数》序预言成例体裁自决。\n已载面：主问（是否应验）已断；预书内容（某年月日椅将被坐破）为题面明示事件面。断项过闸：断应验→指代链应验对象为椅（非人对象，按通则(f)不回收到人身上）→触发为题面设定此占以届期验之为问、序文成例体裁主验；断坐者无伤→指代链同椅面→触发为预书只言椅破不及人。残损：卡面未载预书的具体年月日干支与坐者身份，此二面有面无据不报、已明言。转应核：『坐破』锚点直读，舍转应（不转读为家道破败），理由为预书字面即椅破一事。",
 0.62)

# ---------- OC-026..030 Liuren ----------
add("OC-026",
 "方向：功名可得、非双双落第。1643年正月占，涉害课、曲直格，三传乙未（青龙）—己亥（螣蛇）—癸卯（玄武）成未亥卯三合木局，春月木旺、青龙发用主功名喜信：两兄弟中至少一人是年登科得功名，另一人亦不至全然无名（次等功名/补取之象），优者胜出。应期以月档计：当年春闱至殿试放榜之期（1643年二三月间）见分晓。",
 "此卡未标注 tradition，按卡面课式、三传、月将自决大六壬断法（盘面不全守则：只据干支、三传链、天将、课格、空亡作断，不臆补天盘四课）。\n已载面：主问（今年功名）已断；占时1643年正月初四、己亥日辛未时、甲午旬辰巳空已载。断项过闸：断功名可得→指代链类神取青龙乘初传乙未主科名喜→触发为三传三合木局、曲直格木气成局而春占得令；断一优一次→指代链末传癸卯乘玄武主一名次暗昧稍逊→触发为末传将神之别。残损：卡面无天盘全图与四课全列，年命未载，此三面有面无据不报。转应核：课格名『曲直』为锚点直读木局，不转应。",
 0.50)
add("OC-027",
 "方向：此行不得意。1642年冬月占，课名无禄、无路，三传癸酉（六合）—戊辰（太阴）—亥（青龙，空亡落末传）：奉诏北上终无实职实利可得，行程多阻、终须南返空回；身体一路有惊无大险、可保无恙；家中老母安然无恙，不因此行生变。应期以月档计：数月内（次年春前）即见不得意之实、动返程之念。",
 "卡面无 tradition 标注，按卡面课式三传自决大六壬断法，守盘面不全之则。\n已载面：主问三面（此行得意否、身体、老母安否）俱已逐面断；北方兵事正紧为题面事实已入断（行程有惊之据）。断项过闸：断不得意→指代链课名无禄无路即课格主向、末传青龙落空（甲子旬戌亥空）→触发为禄路双无且发用之喜落空；断母安→指代链老母类神无凶将乘传见载→触发为三传中无白虎玄武冲母位之象，此面证据为消极证据、已在置信中下调。残损：四课天盘未载，不臆补。转应核：课名『无禄无路』锚点直读，理由为课格名即占验指南课式正目。",
 0.56)
add("OC-028",
 "方向：将得官而缺不甚美。1630年冬月占，重审、斫轮课，三传辛卯（玄武）—丙戌（朱雀）—癸巳（白虎）：入觐考选终有授官，文书（朱雀中传）可下，得外任中下级文官一缺（县级正印或佐贰之任），任地近兵刑驿路之气（白虎末传），非清要美缺；应期以月档计：次年春季文书到、赴任见实。",
 "本例卡面未见 tradition，按课式三传自决大六壬仕宦门断法，盘面不全守则照行。\n已载面：主问（将得何官）已断至职级层级；具体州县名号题面未载、无据不报，已明言。断项过闸：断得官→指代链朱雀乘中传丙戌主文书授命→触发为铸官之文书链成立、初传玄武主选途暗竞争而终成；断缺不美→指代链末传白虎乘癸巳→触发为任地气类主兵刑劳碌。残损：四课、天盘、年命未载，职级只断到层级。转应核：课名斫轮直读为造作车轮主成器得用，不转应。",
 0.45)
add("OC-029",
 "方向：此行求官劳而少得，老母有大限之忧。1642年十月占，涉害、曲直、回环课，三传乙未（白虎）—癸卯（六合）—己亥（天后）：携子求官难成美缺、子辈功名官职此行不得实授，宜早归；其母年近九十，初传白虎乘未主丧服之象，近一二年内有寿终之忧，孝养送终为当务。占者本人此行无大碍、平安往返。应期以年档计：母忧在1643—1644年间，子官事此行内（数月）即知不成。",
 "卡面未标注 tradition，按课式三传自决大六壬断法，守不全盘之则；本卡所载年命信息仅其子丑命与母年近九十，余不臆补。\n已载面：主问（诸事吉凶）已分面断：子求官面、老母面、本人行程面俱列。断项过闸：断母有寿忧→指代链老母类神以年命长辈位取、初传乙未乘白虎→触发为白虎乘初传主丧服哭泣之类（六壬分类占亲属门）；断子官不成→指代链末传己亥天后主阴私退藏、无青龙贵人乘传见载→触发为求官链无贵喜落点，此为消极证据已降置信。残损：四课天盘未载。转应核：课名回环直读往返，不转应。",
 0.48)
add("OC-030",
 "方向：巡按差可复、吏书缺可照旧。1651年二月占，重审、铸印课，三传癸巳（太常）—丙戌（六合）—辛卯（太阴）：铸印课主官印铸成、制度落定——淮扬巡按差有复设之机并将成议，吏书之缺亦照旧保留、不废；然太阴末传主事成于暗中、非大张旗鼓，应期以月档计：当年内有正式文书定局，上半年议起、秋前落定。",
 "此卡无 tradition 字段，按课式三传自决大六壬官制存废断法，盘面不全守则照行（卡面月将仅载亥将、旬空未载，此残损如实记并降置信）。\n已载面：主问两面（巡按差可复否、吏书缺可照旧否）俱已断。断项过闸：断巡按可复→指代链课名铸印主官印新铸、太常乘初传癸巳主朝廷典制→触发为课格主向与初传将神同指制度成形；断吏缺照旧→指代链中传丙戌六合主和议维持→触发为六合主合而不散。转应核：课名『铸印』锚点直读，舍转应（不读为虚印空文），理由为太常六合两传同向佐证。残损：空亡未载，应期只到月档。",
 0.52)

# ---------- WP: western astrology / tarot ----------
add("WP-001",
 "Direction: Yes — a major collective affliction, specifically a pandemic. The 2020–2021 window marked by the Jupiter–Saturn–Pluto conjunction (exact early 2020), five outer planets gathered within ~100 degrees and the cyclical index at its 21st-century low carries a large-scale epidemic: a fast-spreading respiratory-type plague causing mass illness, many deaths, and worldwide disruption of travel and daily life, peaking in 2020 and extending into 2021. Timing: onset/peak at the early-2020 conjunction, affliction window 2020–2021 as asked.",
 "The card carries no tradition/system field (keys checked: id/subject/context/provenance/language); decided by card genre as mundane astrology per the snapshot's western-astro reference.\nFaces listed: main question (major collective affliction in 2020–2021) answered; configuration face (Jupiter–Saturn–Pluto conjunction, outer-planet cluster, cyclical-index low) used as the trigger — the card itself notes comparable past clusters coincided with 1918, 1954, 1968 and 1982, years the card links to such events, so the pandemic reading follows the card's own stated pattern rather than free association. Specific disease name is not on the card and is not claimed. Anchor check: the cyclical-index low is read straight, no reversed reading taken, because the card's own comparanda point one way.",
 0.72)
add("WP-002",
 "Direction: Barack Obama wins. The Democrat — Sen. Barack Obama, once nominated — defeats Sen. John McCain in the general election of 4 November 2008. The Saturn–Uranus opposition beginning on Election Day, last seen 45 years earlier, marks a break with the incumbent party and an insurgent/change victory rather than continuity: the younger challenger of the out-party takes the White House. Timing: decided on Election Day, 4 November 2008.",
 "No tradition/system field appears on this card; decided by genre as a western astrology election assessment, the setting being a May 2008 news report of astrologers' forecasts.\nFaces listed: main question answered; the card's stated configuration (Saturn opposite Uranus from Election Day, a configuration last seen 45 years earlier) is the trigger — opposition of the old-order planet to the change planet on the day itself is read for rupture/change of ruling party. The nomination face (Obama leading Clinton but not yet clinched) is listed and answered conditionally in the prediction text ('once nominated'). Anchor check: '45 years earlier' points to the 1963-era upheaval cycle; read straight as a change signature, reversal reading listed and rejected because the opposition falls on Election Day itself.",
 0.66)
add("WP-003",
 "Direction: Barack Obama is re-elected. The incumbent defeats Mitt Romney on 6 November 2012; the race is competitive but the presidency does not change hands. Mercury turning retrograde on Election Day marks counting disputes, delayed/confused returns in places and post-election argument over the result — noise around the count, not a reversal of the outcome. Timing: decided 6 November 2012, with result controversy lingering days after.",
 "This card does not label a tradition field; decided by genre as a western astrology election forecast (Astrology News Service report, May 2012).\nFaces listed: main question answered; Mercury-retrograde-on-Election-Day face answered as process turbulence, explicitly not as an outcome reversal — that distinction is the trigger discipline here (retrograde governs the count/communications, the incumbent's structural advantage governs the result). Polling-competitiveness face listed and reflected in the 'competitive race' wording. Anchor check: Mercury retrograde read straight (delays, disputes), reversed reading (retrograde = challenger wins) listed and rejected for lack of a card-given basis.",
 0.62)
add("WP-004",
 "Direction: Hillary Clinton wins. The consensus of the international astrology conference panel at Costa Mesa (October 2016) points to the Democrat, Hillary Clinton, defeating Donald Trump on 8 November 2016, in line with most polls favouring her. Timing: decided on Election Day, 8 November 2016.",
 "The card carries no tradition/system field; decided by genre as a report of a conference panel's astrological election forecast.\nFaces listed: main question answered as the panel's collective call, which is what this card's provenance (a conference forecasting panel report) asks for; the polls-favour-Clinton face is listed and matches the panel direction. This card (WP-004) is the panel-consensus item; the distinct single-astrologer item is WP-005 and is answered separately on its own card facts, not merged. Anchor check: no numeric/verbal anchor on the card beyond the conference setting; reversal check not applicable beyond noting the panel call is a consensus, not a unanimous chart reading.",
 0.55)
add("WP-005",
 "Direction: Donald Trump wins. The panel astrologer who alone had picked Trump to become the Republican nominee back when 17 Republicans still contested it follows through to the general election: Trump defeats Hillary Clinton on 8 November 2016, against the majority of polls. Timing: decided on Election Day, 8 November 2016, as an upset result.",
 "No tradition label appears on this card; decided by genre as a western astrology election forecast, individuated by the card's own distinguishing fact.\nFaces listed: main question answered; the card's distinguishing face — this astrologer had earlier, against the field, correctly picked Trump as nominee from 17 contenders — is the trigger for individuating this prediction from the panel consensus in WP-004: the card supplies that track-record fact precisely to single out this reader's call, and a reader who took Trump over 16 rivals for the nomination is read as staying with Trump for the presidency. Polls-favour-Clinton face listed and answered against (upset). Anchor check: '17 Republicans' is a card anchor read straight as a measure of the earlier against-consensus call.",
 0.58)
add("WP-006",
 "Direction: Britain votes to Leave. In the referendum of 23 June 2016 the Leave side wins and the United Kingdom begins its exit from the European Union, against the February newspaper polls showing 'Stay' ahead with many undecideds. Uranus conjunct Ceres at 23 degrees Aries on referendum day is read as a disruptive rupture of the established order — the undecided bloc breaks toward change. Timing: result on referendum day, 23 June 2016.",
 "This card has no tradition/system field; decided by genre as a mundane/natal-chart astrology assessment (Jessica Adams blog assessment, first published 5 July 2015, firmed 22 February 2016), using the UK national charts (1066, 1801, 1922) the card says are available.\nFaces listed: main question answered; referendum-day configuration face (Uranus–Ceres conjunction at 23° Aries) is the trigger, read straight as disruption/change; polls-ahead-for-Stay face listed and answered against, on the card's own note of the vast 'not sure' bloc. Anchor check: the 23° Aries conjunction read straight; a reversed reading (conjunction = consolidation of the status quo) was listed and rejected, Uranus being the change significator in the snapshot's astro reference.",
 0.60)
add("WP-007",
 "Direction: Donald Trump wins, and the Clinton controversies decide it. The Union Square tarot reading (August 2016) points against the poll leader: Trump's path runs through Hillary Clinton's email controversy and Clinton Foundation questions, which keep eroding her through the autumn and prove decisive in the 8 November 2016 result — a late-breaking scandal/shakeup in the final stretch is what tips it. Timing: decided on Election Day, 8 November 2016, with the deciding damage landing in the final weeks.",
 "The card carries no tradition/system field; decided by genre as a tarot election reading (snapshot western-tarot reference, Waite meanings), the card stating a tarot reader was consulted and drew cards on the election.\nFaces listed: main question and its rider (what will decide it) both answered; the card's stated facts that Clinton's email controversy and the Clinton Foundation are already public controversies are the trigger for naming them as the deciding factor — no other deciding factor is supplied by the card. Polls-lead face listed and answered against, as a tarot reading that merely echoed the polls would make the card's controversy facts pointless. Card-level detail: the card does not reproduce the actual spread drawn, so no individual card meanings are claimed — this input gap is noted here and confidence held at 0.52. Anchor check: no verbal/numeric anchor beyond the named controversies, read straight.",
 0.52)

def write_batch(ids, expect_n):
    assert len(ids) == expect_n, (len(ids), expect_n)
    assert set(ids) == set(i for i in ids)
    for cid in ids:
        card = json.load(open(BASE / f"inputs-dev12/{cid}.json", encoding="utf-8"))
        assert card["id"] == cid
        assert cid in P, cid
        OUT.mkdir(parents=True, exist_ok=True)
        with open(OUT / f"{cid}.json", "w", encoding="utf-8") as f:
            json.dump(P[cid], f, ensure_ascii=False, indent=2)
    # verify by exact re-open of this batch only
    for cid in ids:
        d = json.load(open(OUT / f"{cid}.json", encoding="utf-8"))
        assert d["case_id"] == cid and d["prediction_text"] and d["basis"]
        assert set(d["trigger"]) == {"changed_main", "reserve_used", "disputed", "reason"}
    print(f"batch ok: {len(ids)}")

if __name__ == "__main__":
    write_batch(IDS_B19, 20)
    write_batch(IDS_B20, 20)
    trig = {k: sum(1 for v in P.values() if v["trigger"][k]) for k in ("changed_main", "reserve_used", "disputed")}
    print("total written:", len(P), "trigger counts:", trig)
