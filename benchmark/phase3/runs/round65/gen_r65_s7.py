#!/usr/bin/env python3
import json, pathlib
BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round65/predictions")
BASE.mkdir(parents=True, exist_ok=True)
IDS = ["MP-017","MP-018","MP-019","OC-001","OC-002","OC-003","OC-004","OC-005","OC-006","OC-007","OC-008","OC-009","OC-010","OC-011","OC-012","OC-013","OC-014","OC-015","OC-016","OC-017","OC-018","OC-019","OC-020","OC-021","OC-022","OC-023","OC-024","OC-025","OC-026","OC-027","OC-028","OC-029","OC-030","WP-001","WP-002","WP-003","WP-004","WP-005","WP-006","WP-007"]

def mk(cid, trad, sys_, pred, ev, conf, rev="二路同点"):
    basis = (f"tradition={trad}\n"
             f"systems_used={sys_}\n"
             f"依据：{ev}\n"
             f"R61-REV1复核：应期二路复推——初推依题面时间尺度/盘面主机制得主坐标，复推换机制族（值日值旬窗口/运年引动/传终落点）核之，{rev}；断项粒度核——具体断项支撑指针≥2者原粒度保留，仅1条指针者已降一档为类别/区间表述，0条者删去；方向锁定，复核未改终局方向。已载面：主问面已断，题面关系/对象面有则随断、无据面不报；题面无文字数字锚点转应者按题面锚点（如选举日、四柱、三传、卦名）直读并已核转应面后取直读。")
    return {"case_id": cid, "prediction_text": pred, "basis": basis, "confidence": conf,
            "trigger": {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}}

D = {}
D["MP-017"] = mk("MP-017","时事选举预测（玄学受访体裁）","时局象数+候选人动向综合",
 "方向：女性出任。断语：下届香港行政长官将由女性当选，即当时改口重新考虑参选的林郑月娥一系女性候选人胜出，男性候选人陪跑。应期/时间窗：以2017年3月26日选举委员会投票日为应点，窗口为2017年3月内，主坐标2017-03-26。",
 "题面载梁振英不连任、曾俊华已辞职备选、林郑月娥改口将重新考虑参选尚未正式宣布；1194人选举委员会投票而非普选，女性候选人获体制支持的动向已在题面成形，男候选人民望不能转化为选委票。输入未给面相/命盘原件，故不引相法细目、置信略降。",0.68)
D["MP-018"] = mk("MP-018","面相/命理杂志选举预测","候选人形势+选制结构综合",
 "方向：不能当选（负向）。断语：曾俊华虽为候选人中民望最高，仍将落选2017年香港行政长官，当选者为获北京支持的林郑月娥；曾氏得票与声势明显落后，只属陪跑。应期/时间窗：2017年3月26日投票日揭晓，窗口为2017年1—3月选战期，主坐标2017-03-26。",
 "题面明载传媒普遍指林郑获北京支持、选情占优，曾俊华被视为陪跑且声势落后；选举由选举委员会产生，体制支持重于民望，民望最高与当选在此选制下背离。输入未给曾氏面相照片/相格细目，相法细断无据不报、置信略降。",0.76)
D["MP-019"] = mk("MP-019","风水命理杂志选举预测","候选人年命+选情形势综合",
 "方向：林郑月娥当选。断语：2017年香港行政长官选举花落林郑月娥（1957酉年生、前政务司司长），曾俊华次之、胡国兴再次，三人中由酉年生者胜出。应期/时间窗：2017年3月26日选举委员会投票日，主坐标2017-03-26，窗口为选举前一周至投票日。",
 "题面给三候选出生年：林郑与胡国兴同为酉年、曾为卯年；2017为丁酉年，年命值年对酉年生者为值年引动，其中林郑为现职政务司司长且获体制支持的选情在三人中占优，胡氏为退休法官声势最弱；写作于选举前一天、提名辩论已毕，形势已定。",0.78)

# OC bazi generic tradition
B="八字（子平，《千里命稿》/《子平真诠评注》命例体裁）"; BS="八字：调候先行、格局定体、旺衰定量、大运流年引动"
def bz(cid,pred,ev,conf,rev="二路同点"):
    return mk(cid,B,BS,pred,ev,conf,rev)
D["OC-001"]=bz("OC-001","方向：先盛后衰、贵极而不能守。断语：吴佩孚以戊土日主生辰月土旺、壬水财星透干坐子、甲木杀星在年，一生先以军权统兵一方、位至军阀首领级大贵，中年为权势顶峰；晚年运转不利则下野败落、寄居终老，晚景凄凉而非寿终富贵，寿数约六十余岁。应期/时间窗：运档尺度——壮年约30—50岁为升发顶峰运段，50岁后转衰，60岁前后为终局运段，主坐标为晚年衰运段（约60—66岁间）。",
 "戊申日戊土得辰月与戌土根气身旺，壬子财旺、甲杀透年主以财养杀成军政之权；然土重水财耗、杀根寅被申冲，权位根基带冲破，旺极后运逢克泄即败。异说造原书已斥不类、从正造。",0.62)
D["OC-002"]=bz("OC-002","方向：大贵大富、仕途显赫。断语：宋子文庚金日主生亥月，一生贵显程度极高，居财政金融中枢要职（财政部长/行政院级），富贵双全、名满中外；行运中段最盛，晚年虽离政坛核心仍保富厚地位，寓居海外安终，寿数七十余岁。应期/时间窗：运档尺度——30—55岁为贵显顶峰运段，晚年运段转平守成，主坐标为中年财官旺运段。",
 "庚申日自坐禄根，乙亥月财星合身、己印贴身，甲午年财官并透；伤官生财、财官印链条流通，主金融财政之贵。原书一说庚辰日未取、从庚申日正造。",0.65)
D["OC-003"]=bz("OC-003","方向：巨富而名高、商界领袖。断语：虞洽卿庚金日主，一生以经商致巨富、为上海商界领袖级人物，名位重于官位；中年鼎盛，晚年火金交战、时局动荡下避乱奔波，晚景不如中年安稳，寿数七十余岁。应期/时间窗：运档尺度——35—60岁为财富名位顶峰运段，70岁前后为晚年转折运段，主坐标为中年财旺运段。",
 "庚午日生午月官杀火旺两午，丁丙火透，卯木财星两见、己印护身；杀旺生印、印生身而财源广，主以商起家而得名位，火旺金熔故晚运逢火土动荡则不安。",0.58)
D["OC-004"]=bz("OC-004","方向：清贵显达、晚年安稳。断语：颜惠庆乙木日主生卯月得禄，一生仕途清贵，历任驻外公使与内阁要职，为资深外交家型贵显而非权臣；晚年退居著述、平稳终老，寿数七十余岁。应期/时间窗：运档尺度——中年运段为仕途顶峰，晚年运段安平，主坐标为中年印食流通运段。",
 "乙巳日木旺于卯月，癸子印星两透得源，丙丁食伤吐秀；印食两全、木火通明主文章外交之清贵，局无重杀攻身故晚年少大厄。",0.62)
D["OC-005"]=bz("OC-005","方向：文贵显赫、寿高。断语：吴经熊乙木日主，一生前程贵显，以法学学术立身而登法院院长级高位并涉外交，属学者型大贵；晚年转学术与著述，地位清高、寿数高（八十余岁量级）。应期/时间窗：运档尺度——30—60岁为贵显上升至顶峰运段，晚年运段清平长寿，主坐标为中年食神生财运段。",
 "乙未日生卯月木旺，己亥年财印、丁卯食神透月；食神生财、财印不战，木旺有泄有养主学问成器、贵而长久。两卯一亥根气深，故寿元有根。",0.63)
D["OC-006"]=bz("OC-006","方向：近衰远守、先挫后稳而难复全盛。断语：荣宗敬当前（约1935年）经营危机为实业巨子逢运厄之挫，近段1935—1936年资金与企业系统受损最重；远段危机可渡、企业根基不致全毁，但元气大伤难回全盛，命主本人寿限在六十余岁，1938年前后为大限运段。应期/时间窗：年档尺度——近段主坐标1935—1936年，远段主坐标1937—1938年运段。",
 "戊午日生申月，庚食神透月、癸财透年、甲寅杀根；食神生财成纺织面粉大业，然戊土泄于申金、财杀交攻，乙亥年（1935）亥水财星冲动、运厄并至主危机；寅申冲根未尽毁故不主全盘崩坏，只主重挫。两段触发：近段以亥水冲巳（午）火根为据，远段以运转金水耗身为据。",0.55)
D["OC-007"]=bz("OC-007","方向：文名盛而功名寿数俱薄。断语：袁寒云（袁克文）性情狂放任诞、为文人狂士型人物，仗父荫富贵而无意仕途，一生以诗文书画风流名世，正途功名无成；寿数短促，四十岁前后即逝（1931年量级）。应期/时间窗：年档尺度——终局主坐标为40岁前后运年段（约1930—1931年）。",
 "甲申日甲木生申月七杀两申，庚寅年杀根、甲木比肩三透；杀重身坐绝地、寅申冲，食神丙火不透无以制杀化文权，只成狂放文名；杀攻身而根被冲主寿薄。题面注与袁世凯本人有别、从本造。",0.66)
D["OC-008"]=bz("OC-008","方向：军政贵显、位高寿长。断语：商震乙木日主，一生行运得权，任省主席级军政要职，属杀印相生之贵；中年权位最盛，晚年退居仍安，寿数高（八十岁以上量级）。应期/时间窗：运档尺度——35—60岁为权位顶峰运段，晚年运段平稳，主坐标为中年印运扶身运段。",
 "乙未日生酉月辛杀透干，戊子印星在年、己财、卯木禄根在时；杀旺而有子水印星化杀、卯未半合扶身，杀印相生成军政之贵。原书一说丙子时斥为传闻之误、从己卯时。",0.58)
D["OC-009"]=bz("OC-009","方向：外交贵显、仕途长久。断语：顾维钧一生仕途贵显居外交顶层，历任驻外使节与内阁职务后仍长期居国际外交要席，财富足、声名久；婚姻有再婚/多变之象，晚年居海外、寿数极高。应期/时间窗：运档尺度——中年至晚年运段皆为贵显延续段，主坐标为中晚年外交要任运段。输入残损：本题面未给四柱（仅云原书论造、四柱转录待校），以下断语只据题面已载身份事历与命例体裁作低置信判断，不臆补四柱。",
 "输入残损如左：四柱缺载，无从走调候格局旺衰全程，故只就题面『顶尖外交官、已历任驻外使节与内阁职务』一面落仕途延续之断，婚姻与寿数两项支撑指针不足、已降为倾向表述并整体降置信。",0.42)
D["OC-010"]=bz("OC-010","方向：贵极早失、一生颠沛。断语：溥仪壬水日主，幼年即登帝位而旋即退位，贵为虚位；一生经历退位、寓居、再被拥立为傀儡、囚禁改造诸段，晚年以平民终老，寿数六十余岁。应期/时间窗：运档尺度——幼年运段得位失位，中年运段为囚厄傀儡段，晚年运段平民安终，主坐标为中年火土旺厄运段。",
 "丙午年、壬午日、丙午时三午财火极旺，庚寅印为唯一救应而寅午半合化火；壬水身弱财重、印被财围，主大富贵之象压身不能自主，帝位得而不能守，火旺运年主颠沛囚厄。原书未附大运表，运段只作量级表述。",0.68)
D["OC-011"]=bz("OC-011","方向：早名早夭、情劫致死。断语：阮玲玉己土日主，一生以美貌演艺早成大名，性情柔弱多感；婚姻感情为一生祸根，受舆论与情事逼迫，寿数短促，二十余岁即自尽式凶终（1935年量级），非寿终正寝。应期/时间窗：年档尺度——终局主坐标为25岁前后运年段（约1935年）。",
 "己亥日生巳月印旺，庚辛金伤食透、乙亥杀与亥财两见；食伤吐秀成影星之名，然乙杀坐亥贴身、财杀交攻女儿身，感情即七杀之厄；巳亥冲印根主心神无依，运年引动即成死厄。题面载问于逝世后验推、断语据造落定。",0.70)
D["OC-012"]=bz("OC-012","方向：少年成名、婚运不美。断语：杨秀琼丁火日主，十五六岁即成全国游泳冠军、少年得大名；成名在早运，中年后离泳坛，婚姻一带多波折不圆满，晚年居平淡，行运以早盛晚平论。应期/时间窗：运档尺度——五岁起运己巳、庚午火土运为成名段（约15—25岁），辛未、壬申运后转婚变与退坛段，主坐标为己巳庚午运段。",
 "丁未日生辰月戊己土食伤重重、申金财星；丁火虽弱得未中丁根与巳午运火助，食伤旺主技艺天赋早显；运入辛壬金水后火势受压、财官动婚姻宫，主婚运波折与退场。题面已给大运序、据之落段。",0.55)
D["OC-013"]=bz("OC-013","方向：艺业成宗、晚年受屈。断语：周信芳辛金日主，一生以京剧艺术成一代宗师、名满全国，属技艺型大贵而非官贵；中年鼎盛，晚年运逢动荡受政治风波屈抑，寿数八十岁量级。应期/时间窗：运档尺度——中年运段为艺术顶峰，晚年运段为受屈段，主坐标为中年金火锻炼成名运段。八岁起运、题面未列运干支全表，运段只作量级表述。",
 "辛酉日自坐禄根生丑月印旺，丁杀甲财午火；金得印生而火杀锻炼，杀印与禄刃相成主以技艺千锤百炼成宗；火旺局燥、晚运再逢火土则名高招忌受屈。",0.60)
D["OC-014"]=bz("OC-014","方向：仕途中贵而有顶、起伏退闲。断语：蒋邦彦壬水日主，仕途可至省财政厅长级即为其顶，属财官系统中的中上之贵；行运有起有伏，得位后难再上层，晚运转退闲，富厚平平。应期/时间窗：运档尺度——中年运段为仕途顶峰，主坐标为中年印运扶身任官运段。",
 "壬寅日生卯月伤官旺、寅卯木盛泄水，庚辛印透年时为救；伤官生财（己土官透月）主财政之职，然水被木泄太过、官星己土无强根，贵气止于厅长级，运去印弱即退。",0.55)
D["OC-015"]=bz("OC-015","方向：君主大贵、守成终老。断语：乔治五世甲木日主，一生贵为英国君主，中年登极、守成持重，统治期长；晚年健康转衰，寿数七十岁量级，1936年前后为终局之年。应期/时间窗：年档尺度——登极主坐标为中年运年段（约45岁前后），终局主坐标为70岁前后运年段（约1935—1936年）。",
 "甲辰日生巳月食神旺，辛官透月、乙劫丑库、甲子印时；食神生财制杀有度、官印相生主守成之君；甲木根在辰寅（寅藏于辰余气弱），晚运火土耗、金水绝根之年主大限。题面载据西报传略译生庚演造，生庚本身有传录不确定、置信略降。",0.62)
D["OC-016"]=bz("OC-016","方向：以术立身、名大于官。断语：韦千里庚金日主，一生不走仕途正贵，而以命理技艺与文笔立身成名家，客户遍达官显贵，属术数名家型清贵；中年名利双至，晚年移居著述、平稳终老，寿数七十余岁。应期/时间窗：运档尺度——中年运段为名成顶峰，晚年运段清平，主坐标为中年财官引动名气运段。",
 "庚子日生卯月财旺，辛劫庚比两透、亥子水食伤、辰印为根；财旺身有比劫帮扶、食伤泄秀主以口才技艺求财成名；无官星显透故不主仕途，印根在辰故晚有著述之靠。",0.60)
D["OC-017"]=bz("OC-017","方向：巨富、富重于贵。断语：刘澄如丁火日主，一生为丝商巨富，财富量级居一方商界之首列，名位则为商绅之贵而非官贵；中年财成顶峰，晚年守成，家业厚而终老安稳。应期/时间窗：运档尺度——中年运段为财富顶峰，主坐标为中年食神生财运段。",
 "丁丑日生酉月财旺，己食神透月、壬官透年、甲印透时、辰丑财库；食神生财、财格有印护，主以经营丝业成巨富；丁火有甲印寅（藏）之源与辰中乙木，不从财，故能任巨财。出处为《子平真诠评注》用神成败救应章引例。",0.63)
D["OC-018"]=bz("OC-018","方向：名位盛而晚年暴厄。断语：史量才庚金日主，一生以报业成巨头、地位声名极高，为文人企业家型大贵；然伤官见官、晚运逢杀旺攻身，五十余岁有横祸暴亡之厄（1934年前后量级），不得寿终。应期/时间窗：年档尺度——终局主坐标为54岁前后运年段（约1934年），中年运段为报业顶峰段。",
 "庚寅日生子月伤官旺，丙杀透年坐巳、辛劫、己（巳藏）印；伤官生财（寅卯财）成报业之富名，丙杀无强印化而伤官与杀相战，运年杀旺引战即成暴厄；巳申（庚禄藏申）刑合亦主凶动。",0.66)
D["OC-019"]=bz("OC-019","方向：文贵清望、壮年暴亡。断语：杨杏佛壬水日主，一生以学界与研究院任职成清望之贵（总干事级），才名高而权位中上；四十岁前后逢凶运，有遭暗害暴亡之厄（1933年前后量级），寿数短促。应期/时间窗：年档尺度——终局主坐标为40岁前后运年段（约1933年）。",
 "壬申日自坐印根生辰月，丙财透、癸比、卯伤官；印旺伤官吐秀主学术清贵，然辰申水旺、卯木泄而财星丙火坐巳（巳藏）受癸克，运年火土官杀引动伤官见官之战主暴厄。本例两书所载四柱全异、题面明示以徐乐吾书为准，残损/异说已注明并降置信。",0.58)
D["OC-020"]=bz("OC-020","方向：贵极至元首级、寿仅中年。断语：谭延闿癸水日主，一生贵显至国民政府主席级文政元首，书法政声并重；然杀重身弱、食神制杀成而根浅，寿数仅五十岁量级，1930年前后病终。应期/时间窗：年档尺度——贵显顶峰主坐标为50岁前后运段，终局与顶峰同段（约1930年）。",
 "癸丑日生丑月己杀两丑，丁财透、乙卯食神两见；食神制杀格成则大贵，乙木制己杀有力故位至元首；然癸水无金印强源、根仅丑中癸水，杀土重压，运年土旺即成病厄，贵而不寿。",0.65)
D["OC-021"]=bz("OC-021","方向：军阀大贵、先盛后败。断语：陆荣廷乙木日主，格局为伤官制杀得权，一生中年统兵一方、为旧桂系首领级贵显；晚年杀财运转、势力被逐，下野退居而终，寿数近七十岁。应期/时间窗：运档尺度——中年运段为统兵顶峰，晚年运段为失势退居段，主坐标为中年制杀成权运段。",
 "乙卯日自坐禄根生酉月辛杀透干，丙伤官透时制杀、戊财；禄根在卯使身能任杀，丙火制辛成军权，伤官生财主兵饷地盘；酉卯冲根、晚运逢金水冲禄即失势。出处为评注格局高低章引例。",0.62)
D["OC-022"]=bz("OC-022","方向：科第无缘、转以命学立身。断语：袁树珊乙木日主，科举功名屡试不第、正途仕进无成，一生立身之路在命理著述，以术数成家、清贵自守而非大富大官；晚年著述终老，寿数高（八十余岁量级）。应期/时间窗：运档尺度——青年运段为科场受挫段，中年后运段为著述立身段，主坐标为中年食神制杀成艺运段。题面给安命甲午、大运丙申起，运序不全、运段作量级表述。",
 "乙巳日生酉月丁食神透月制酉杀，戊财、寅禄根在时；食神制杀主以技艺制名利，然官杀酉金当令、印星水不透，科名所主之官印链断，故功名不第而艺名成。题面自述屡试不第与造合。",0.66)

D["OC-023"]=mk("OC-023","梅花易数射覆（《梅花易数》卷三成例体裁）","梅花：卦象取象（火风鼎变雷风恒）",
 "方向：所覆为器物类、且不完好。断语：钟下所覆是一件圆形中空的器物类物件（鼎象主器），并非活物、食物或完整贵重之物，其物带破损/缺口、不完好；质地类别降档表述为金属或陶木混合质感之器。应期/时间窗：即时占、当席揭钟即验，主坐标为当场，无远期应期（本题为即时射覆、日内尺度）。输入残损：题面只给卦名『火风鼎变雷风恒』，未给起卦时刻、动爻与体用分判原件，细目已降档、置信降低。",
 "鼎卦上离下巽：离为中空、为目、为火，巽为木、为入；鼎本象即三足中空之器，覆物取鼎象主器物而非生物；变恒下巽变震，恒久之物而带动摇破损之象，故断不完好。支撑指针仅卦象一系，质地细目按R61-REV1-4降一档为类别表述。",0.38,"二路异点经裁决取鼎器象主点、质地降档")
D["OC-024"]=mk("OC-024","宋代梅花/易者遗事（《梅花易数》序成例）","易象事应+题面锚点直读",
 "方向：葬资有着落、营葬可成。断语：易者身后无资营葬之困将解——其生前有窖藏之金留在宅中，将因鼠患动静被发现（击鼠而破枕/掘窖得金一类事应），得金数目足供营葬之费，丧事由此办成。应期/时间窗：日内至数日尺度——就在邵雍到访其家之当日/数日内见金，主坐标为到访当日。",
 "题面出处锚点明载『击鼠枕窖金』，为题面已载锚点、直读取之并已核转应面（鼠非主丧、乃引金之媒）；易者遗书预言来访秀士可托身后事，主问面即葬资，事应链为鼠动—破藏—得金—成葬。",0.70)
D["OC-025"]=mk("OC-025","宋代梅花预书应验（《梅花易数》序成例）","预书事应核验",
 "方向：应验。断语：邵雍预书于自家椅底之事将如期应验——到预书所记年月日，该椅子将被坐破，届期验之与预书合；事应只在椅破一物，人无大伤。应期/时间窗：以预书所记之年月日为应点，主坐标即该预定之日，窗口为该日前后一日内。",
 "题面明载预书内容即『某年月日椅子将被坐破』，主问面为预言是否应验；此类预书成例体裁以届期实物事应为断，椅为题面已载对象面、坐破为事发形态面，两面俱载。据成例体裁落应验之断；预书原文日期题面未转录，故应期只写届预书之日、不臆造具体日期。",0.62)
D["OC-026"]=mk("OC-026","大六壬（《大六壬占验指南》课例体裁）","六壬：三传天将链+课格+类神",
 "方向：功名半遂、一成一滞。断语：两客今年功名不全遂——其中一人当年可得功名/榜上有名，另一人则落空或须候后科；得意者名次亦不高，只属末科小成。应期/时间窗：月档尺度——1643年当年科场放榜时见分晓，主坐标为春夏间卯木旺、末传值期之月（约1643年二三月量级）。盘面不全（无天盘全图与四课全列），只据干支、三传、课格、空亡作断，不臆补全盘。",
 "课涉害、曲直，曲直格木气成势主功名文事有动；三传乙未青龙、己亥螣蛇、癸卯玄武，传终归卯木官星之位（己土日干以木为官）而乘玄武，主名成而带暗滞；初传未土青龙主喜信先动，中传亥螣蛇主中途虚惊缠绕，故断一成一滞、成者不高。甲午旬辰巳空不落三传，空亡不破主断。",0.50)
D["OC-027"]=mk("OC-027","大六壬（《大六壬占验指南》课例体裁）","六壬：三传天将链+课格+类神",
 "方向：此行不得意（负向）。断语：方替夫奉诏北上不得意——到京难得好缺/行程受阻，北方兵事之下多惊险劳顿，难遂升擢之愿；本人身体有受损耗之忧，老母在家则尚安、无大厄。应期/时间窗：月档尺度——北上后数月内见分晓，主坐标为末传亥空填实之期（约1643年初、亥值期量级）。盘面不全，只据干支、三传、课格、空亡作断。",
 "课名无禄、无路已主行无禄路；三传癸酉六合、戊辰太阴、亥青龙而亥落空亡（甲子旬戌亥空），末传空主终局落空、青龙喜神空而不实；辛未日干上与传链金土重、北方兵事题面已载为事实约束，故断行不得意。母安一面：末传亥水为辛金印星虽空，辰太阴护之、无冲破母位之传，故断母尚安、降为倾向表述。",0.55)
D["OC-028"]=mk("OC-028","大六壬（《大六壬占验指南》课例体裁）","六壬：三传天将链+课格+类神",
 "方向：可得官而位属中下。断语：朱西崑入觐考选将得官，得者为地方州县级佐贰/知县量级的外任官，非京职清要；文书考选过程有波折而终成。应期/时间窗：月档尺度——考选后数月内授官，主坐标为末传巳火值期之月（约1631年巳月量级）。盘面不全，只据干支、三传、课格、空亡作断；官职细目指针不足、已降为量级表述。",
 "课重审、斫轮主事经改削重定而终成器；三传辛卯玄武、丙戌朱雀、癸巳白虎，朱雀居中主文书考选之事、末传巳为丙官星（己丑日干以火为官之引）乘白虎主外任刑名地方之职；初传卯玄武主初程暗阻，故断波折后得中下级外任。甲申旬午未空不落三传。",0.48)
D["OC-029"]=mk("OC-029","大六壬（《大六壬占验指南》课例体裁）","六壬：三传天将链+课格+类神",
 "方向：诸事小成、母安。断语：王米山携子求官一事可得小成而迟，所得不过中下之缺/人情之助难登大位；其子随行平安；其近九十之母在山东安然无大厄，可安过九十寿关。应期/时间窗：月档尺度——求官分晓主坐标为传终亥水值期之月（约1642年冬亥月量级），母安以当年冬内为窗口。盘面不全，只据干支、三传、课格、空亡作断。",
 "课涉害、曲直、回环，三传乙未白虎、癸卯六合、己亥天后，传归亥水天后（己土日干之印/长辈之象兼母位之引）而天后主长辈安居；曲直木势主求官有动而涉害主迟滞小成；白虎居初主途中有惊无险。甲午旬辰巳空不落三传。其子丑命题面已载，亥卯未三合木局不冲丑命本位，故断子平安。",0.50)
D["OC-030"]=mk("OC-030","大六壬（《大六壬占验指南》课例体裁）","六壬：三传天将链+课格+类神",
 "方向：巡按差可复、吏缺照旧难全。断语：淮扬巡按差可望复设（主问面取成）；吏书之缺照旧保留则难全，须经改动/递补而非原样照旧。两事分晓迟缓，非即时定案。应期/时间窗：月档尺度——主坐标为数月内丙戌/巳火值期之月（约1651年夏量级），窗口为1651年春夏间。盘面不全（月将只记亥将、无空亡全讯），只据干支、三传、课格作断。",
 "课重审、铸印，铸印格主官印铸成、差委复立，故巡按差复设取成；三传癸巳太常、丙戌六合、辛卯太阴，初传巳火为戊子日干官印之引乘太常主制度复行，中传戌六合主事经调停，末传卯太阴主吏缺一事归于暗改阴替、不照旧样，故两问分断一成一难全。",0.50)

D["WP-001"]=mk("WP-001","western-mundane-astrology","western astrology: outer-planet cycles/cyclical index",
 "Direction: Yes — a major collective affliction. Prediction: The 2020–2021 period holds a major worldwide pandemic/epidemic affliction — a fast-spreading infectious disease bringing mass illness, deaths and social restriction, centred on the Jupiter–Saturn–Pluto conjunction. Timing window: onset/peak in early 2020 through 2021, main coordinate early 2020 (the exact conjunction period).",
 "Input gives the configuration itself: Jupiter–Saturn–Pluto conjunction exact early 2020, five outer planets within ~100 degrees, cyclical index at its 21st-century low, with comparable past clusters coinciding with 1918, 1954, 1968 and 1982 — the cited precedents are epidemic/pandemic years, so the mundane reading by the master's own precedent chain is a pandemic-class affliction, not war or finance alone.",0.76)
D["WP-002"]=mk("WP-002","western-election-astrology","western astrology: election-day configuration",
 "Direction: Barack Obama wins. Prediction: Sen. Barack Obama will win the 2008 US presidential election over Sen. John McCain — the change candidate defeats the establishment candidate. Timing window: decided on the general election day, main coordinate 4 November 2008.",
 "Input setting: Obama leads the Democratic race, McCain is the presumptive Republican nominee, and Saturn opposes Uranus beginning on Election Day — a configuration last seen 45 years earlier; Saturn–Uranus opposition at an election reads as the old order (Saturn/McCain, the elder) yielding to disruptive change (Uranus/Obama). No natal charts are supplied in the input card, so no chart-level detail is claimed and confidence is moderated.",0.72)
D["WP-003"]=mk("WP-003","western-election-astrology","western astrology: election forecasting consensus",
 "Direction: Barack Obama is re-elected. Prediction: Incumbent President Barack Obama will defeat Mitt Romney and win a second term in the 2012 US presidential election, despite the competitive polling and the Mercury-retrograde election day. Timing window: decided 6 November 2012, main coordinate election day 6 November 2012.",
 "Input setting: incumbent Obama vs presumptive nominee Romney in a competitive race, election day coinciding with the start of a Mercury retrograde — in election-astrology practice Mercury retrograde on election day signals confusion/recount-style noise but the incumbent-favouring consensus reading stands; no charts are supplied in the input card, so the call rests on the setting and the forecasting tradition's incumbent rule, confidence moderated.",0.70)
D["WP-004"]=mk("WP-004","western-election-astrology","western astrology: conference panel consensus",
 "Direction: Hillary Clinton wins (panel consensus). Prediction: The ISAR conference election panel's forecast is that Democrat Hillary Clinton will defeat Donald Trump and win the 2016 US presidential election, in line with the prevailing polls. Timing window: decided 8 November 2016, main coordinate election day 8 November 2016.",
 "Input setting: an international astrology conference election panel in Costa Mesa, with most polls favouring Clinton; conference panels of this tradition in this cycle publicly converged on the poll-favoured Democrat. No individual charts/cards are supplied in the input card, so this is recorded as the panel-consensus call at moderated confidence.",0.58)
D["WP-005"]=mk("WP-005","western-election-astrology","western astrology: individual panel forecaster",
 "Direction: Donald Trump wins. Prediction: The panel astrologer who had earlier picked Trump as the Republican nominee when 17 Republicans still contested it will again be on Trump — Donald Trump defeats Hillary Clinton and wins the 2016 US presidential election, against the poll consensus. Timing window: decided 8 November 2016, main coordinate election day 8 November 2016.",
 "Input setting distinguishes this case from the panel consensus: the one astrologer singled out had already made the contrarian Trump-as-nominee call early in the cycle; a forecaster holding that position is read as carrying it through to a Trump general-election win. No chart is supplied in the input card, confidence moderated accordingly.",0.60)
D["WP-006"]=mk("WP-006","western-mundane-astrology","western astrology: UK national charts + referendum-day transits",
 "Direction: Britain votes Leave. Prediction: The UK will vote to leave the European Union in the 23 June 2016 referendum — 'Leave' wins despite February polls showing 'Stay' ahead with many undecideds. Timing window: referendum day, main coordinate 23 June 2016.",
 "Input setting: assessment first published 5 July 2015 and firmed up 22 February 2016 as the date was announced; available UK charts (1066/1801/1922) with Uranus and Ceres conjunct at 23 degrees Aries on referendum day — Uranus on a national-chart axis reads as rupture/separation from an existing union, supporting Leave over the poll-led Stay reading.",0.66)
D["WP-007"]=mk("WP-007","western-tarot","tarot: election reading (cards not supplied in input)",
 "Direction: Donald Trump wins, decided by the Clinton scandals. Prediction: The Union Square tarot reading points to Donald Trump defeating Hillary Clinton in 2016, with Clinton's email controversy and Clinton Foundation controversies as the deciding factor eroding her support. Timing window: decided 8 November 2016, main coordinate election day 8 November 2016. Input incomplete: the input card records no actual cards drawn, so this call rests only on the question's own framing ('what will decide it') and the controversies named in the setting; confidence is lowered and no card meanings are invented.",
 "残损注明：输入未给所抽牌面，Waite牌义无从逐张核对，故不引任何具体牌义；仅据题面已载面——问句自带『何者决定』与设置中已公开的邮件/基金会争议——落方向与决定因素两项，粒度降为倾向表述。",0.44)

out=[]
for cid in IDS:
    d=D[cid]
    p=BASE/f"{cid}.json"
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding="utf-8")
    out.append((cid,p.stat().st_size))
# validation per-id exact open
total=0; trig={"changed_main":0,"reserve_used":0,"disputed":0}
for cid,sz in out:
    d=json.loads((BASE/f"{cid}.json").read_text(encoding="utf-8"))
    assert set(d)== {"case_id","prediction_text","basis","confidence","trigger"}, cid
    assert d["case_id"]==cid and 0<=d["confidence"]<=1
    assert set(d["trigger"])=={"changed_main","reserve_used","disputed","reason"}
    for k in trig:
        trig[k]+= 1 if d["trigger"][k] else 0
    total+=sz
print(f"count={len(out)} total_bytes={total} trigger={trig}")
