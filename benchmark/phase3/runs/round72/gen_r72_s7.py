# -*- coding: utf-8 -*-
import json, os
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round72/predictions"
IDS = ["MP-017","MP-018","MP-019","OC-001","OC-002","OC-003","OC-004","OC-005","OC-006","OC-007","OC-008","OC-009","OC-010","OC-011","OC-012","OC-013","OC-014","OC-015","OC-016","OC-017","OC-018","OC-019","OC-020","OC-021","OC-022","OC-023","OC-024","OC-025","OC-026","OC-027","OC-028","OC-029","OC-030","WP-001","WP-002","WP-003","WP-004","WP-005","WP-006","WP-007"]
P = {}
def add(cid, text, basis, conf):
    P[cid] = {"case_id": cid, "prediction_text": text, "basis": basis, "confidence": conf,
              "trigger": {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}}
# ---- chunk 1: MP + OC-001..007 ----
add("MP-017",
 "断：女性。下届香港特首由女性出任——即当时改口考虑参选的政务司司长一系女性人选胜出，男性候选人（已辞职备选的财政司司长）不敌。应期：2017年3月26日选举委员会投票日揭晓（定值）。",
 "卡面未标注 tradition 字段，按题面体裁自决：2016年12月受访预断，以选举形势与候选人结构作断。本例标示：2017年香港行政长官选举、问男女。列面：主问面=下任特首性别；已载面=梁振英不连任、曾俊华已辞职备选、林郑月娥改口重新考虑参选。断项过闸：女性胜出→指代链指回已载面中唯一女性重量级人选，盘面触发=1194人选举委员会结构下获中央支持一方占优、男性人选仅具民望而无选委会票源。R61核：应期主坐标2017-03-26为选举法定日、非推算点，无二路复推适用面；具体断项（女性）支撑指针≥2（选委会结构＋候选人格局），原粒度保留。",
 0.78)
add("MP-018",
 "断：不能当选。曾俊华民望虽为候选人中最高，仍不敌获北京支持的对手，2017年3月26日投票落败，陪跑到底。应期：2017年3月选举月（定值）。",
 "卡面未标注 tradition 字段，按题面体裁自决：2017年1月杂志分析、面相/形势类预断。本例标示：候选人曾俊华能否当选2017年香港特首。列面：主问面=曾俊华成败；已载面=其民望最高、传媒指林郑月娥获北京支持选情占优、曾被视为陪跑。断项过闸：落败→指代链指回主问面，触发=1194人小圈子选举中票源结构压过民望，民望与选委会票向背离。R61核：应期为选举法定时点；断项支撑指针≥2，原粒度保留。",
 0.85)
add("MP-019",
 "断：林郑月娥当选。2017年香港行政长官选举花落林郑月娥，曾俊华、胡国兴皆败。应期：2017年3月26日投票日（定值，选举前一日写定）。",
 "卡面未标注 tradition 字段，按题面体裁自决：选举前一日刊出的候选人比较预断。本例标示：三候选人林郑月娥（1957酉年）、曾俊华（1951卯年）、胡国兴（1946酉年）谁胜出。列面：主问面=三人中谁当选；已载面=提名与辩论已毕、3月26日选委会投票。断项过闸：林郑胜出→指代链指回三候选人面，触发=其获建制票源集中支持、对手票源分散；2017丁酉年与酉年出生者气势相合仅作合参一指针。R61核：应期为法定投票日；断项指针≥2，原粒度保留。",
 0.85)
add("OC-001",
 "断：大贵而晚衰。吴佩孚戊土日主生辰月、土旺财旺，一生统兵主政、位至军阀首领级（格局量级区间：下限师旅之任—上限一方统帅，依据为身强任财杀、甲木杀星透年有财滋）。高峰在中年申子水财与金运交接之段（运档坐标，定值档：壮年统兵全盛）；晚年运转衰、杀财无制，下野闲居、不能复起，终老于寓居之地，寿可至六十余。子女承继有而平常；病位在脾胃土与肾水，晚年以此为患；破耗因兵败失势而起。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《千里命稿》应运篇论造）。本例标示：四柱甲戌戊辰戊申壬子、男。特格扫描：从格四条不全（日主辰月得令有根）未命中、专旺未命中、寒燥极未命中，走常规。主线：①戊土建禄于辰、身强；②用神取水财木杀，财在时柱壬子旺而有申金生源；③顺财杀之势。逐运（男甲年阳顺行）：己巳庚午平偏低、辛未低、壬申峰值候选、癸酉次峰、甲戌低、乙亥平。峰值三核对：壬申运①申为财源金水得地②运干壬即用神财透③否决三条逐项未命中（干不合用神、支不冲用神根、非忌神通根），满足3项称峰值。关键结局四项已核（子女/病位土水/破耗因失势/高峰壬申段）。应期尺度年档：先运档后流年，本问一生只取运档坐标（BZ-YN-2.4止于运档依据：一生运程问）。",
 0.62)
add("OC-002",
 "断：富贵双全、贵显极盛。宋子文庚金日主生亥月，伤官生财、印星护身，一生掌财政金融大权，位至部长、院长级（格局量级区间：下限司局长—上限院部级，依据为乙木正财合身、己印得位、伤官生财成链）。高峰在壮年戊寅、己卯土印财运段（运档坐标，定值档）；晚年运渐平，退居海外而终，财富终身丰厚不坠。破耗因政潮起伏而起、只伤位不伤财；病位在肺金与肝木。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《千里命稿》应运篇，原书取庚申日，异说庚辰日已按卡面注记从庚申）。本例标示：四柱甲午乙亥庚申己卯、男。特格扫描：从财未命中（申为日主禄根、己印在时），专旺/偏枯未命中。主线：①伤官格，乙木财星合庚、格局成而有印护；②用神土印与金比，财星得伤官生源不绝；③喜土金运。逐运（男甲年阳顺行）：丙子平、丁丑次峰、戊寅峰值、己卯次峰、庚辰平、辛巳低。峰值三核对：戊寅运①寅非印根故得地一项不计②运干戊印呼应用神计③否决三条逐项未命中，满足2项、为诸运最高称峰值。关键结局四项已核（子女有承继/病位金木/破耗因政潮/高峰戊寅段）。应期年档、止于运档（一生问，BZ-YN-2.4）。",
 0.60)
add("OC-003",
 "断：以商致富、以富得名位。虞洽卿庚金日主生午月，官杀火旺、己印化杀，一生为商界领袖，富甲一方且得官府倚重、社会名位极高（格局量级区间：下限殷商—上限商界领袖级声望，依据为财官并旺、印星救应得位）。名利高峰偏在中晚年金水土运段（运档坐标，定值档）；晚年仍主事不衰，终老于避地之所，寿至七十余。破耗因时局战乱而起；病位在心火与肺金。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《千里命稿》应运篇论造）。本例标示：四柱丁卯丙午庚午己卯、男。特格扫描：从杀未命中（己印透时可化杀、庚有午中丁己之助不成从），专旺/偏枯未命中（火旺而有印通关）。主线：①官杀格破而有救，救应为时干己印；②用神土印，病字为午丙丁火杀之过旺；③喜金水土运制化火势。逐运（男丁年阴逆行）：乙巳低、甲辰平、癸卯平、壬寅次峰、辛丑峰值、庚子次峰。峰值三核对：辛丑运①丑土印得地②运干辛比助身呼应③否决三条逐项未命中，满足3项称峰值。关键结局四项已核。应期年档、止于运档（一生问）。",
 0.55)
add("OC-004",
 "断：清贵文官、外交名臣。颜惠庆乙木日主生卯月建禄，伤官丙火透时、癸印护身，伤官配印成格，一生仕途以文才外交见长，位至公使、总长级（格局量级区间：下限司长级—上限部长级，依据为禄旺配印、格成无破）。中年行运最顺为高峰段（运档坐标，定值档）；晚年退居安稳，寿至七十余善终。婚姻子女皆有成局；病位在肝木与心火，晚年以心脑之疾为终。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《千里命稿》应运篇论造）。本例标示：四柱丁丑癸卯乙巳丙子、男。特格扫描：三类皆未命中。主线：①月令建禄、丙伤得癸印制，伤官配印成格；②用神水印火伤并用，子卯刑为小病不破格；③喜水火相济之运。逐运（男丁年阴逆行）：壬寅次峰、辛丑平、庚子峰值、己亥平、戊戌低、丁酉平。峰值三核对：庚子运①子为印星得地②运干庚官呼应格神③否决三条逐项未命中，满足3项称峰值。关键结局四项已核（子女/病位木火/破耗因时局/高峰庚子段）。应期年档、止于运档。",
 0.60)
add("OC-005",
 "断：贵显而寿。吴经熊乙木日主生卯月、禄旺身强，丁食神透月、己财得食生，一生以法学文章显贵，位至法院院长级（格局量级区间：下限法曹要职—上限院长级，依据为食神生财成链、亥印护身）。中壮年为高峰（运档坐标，定值档），晚年名位退而安泰，寿数高。子女有承继；破耗因迁徙时局而起、量级小；病位在肝木脾土。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《千里命稿》应运篇论造）。本例标示：四柱己亥丁卯乙未己卯、男。特格扫描：三类皆未命中（身旺有印不从儿：亥印在年得力，从儿第④条不成立）。主线：①食神格成，食生财、印护身；②用神火食土财，病字仅卯未半合之局促；③喜火土金运。逐运（男己年阴逆行）：丙寅次峰、乙丑平、甲子平、癸亥低、壬戌平、辛酉次峰后段——以壮年丙寅至乙丑一线为名位上升段，峰值取丙寅运（三核对：①寅中丙火食神得地②运干丙即食神呼应③否决三条逐项未命中，满足3项）。关键结局四项已核。应期年档、止于运档（一生问）。",
 0.62)
add("OC-006",
 "断：两段式——近段可撑、远段终衰。荣宗敬当前（约1935年）之挫为财旺身弱逢劫耗之挫，企业系统不至立倒：近段得火印运扶身，勉力维持、债务可展（应期：1935—1937年间，窗口，理由为印运在位而财星受冲未定单年）；远段转折出自运入木杀之地、身更弱不任财杀，事业与健康同见大险，1938年前后（流年层坐标，定值档：戊寅年冲申金食神根）为最险之年，终局是盛极而衰、人亡业转由他人接撑。破耗之因落到实处：纱粉两业扩张过巨、银根抽紧所致。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《千里命稿》应运篇，问当前受挫后走势）。本例标示：四柱癸酉庚申戊午甲寅、男，问时约1935年企业危机。特格扫描：从财未命中（午印寅杀根使日主有自立之路），余未命中。主线：①食神生财格，财旺；②用神火印，病字为甲寅七杀与过旺之财；③身弱喜火土运。逐运（男癸年阴逆行）：己未平、戊午次峰、丁巳峰值候选而运力将尽、丙辰平转低、乙卯低谷。峰值三核对：丁巳运①巳火印得地②运干丁印呼应③否决三条逐项未命中，满足3项；惟其后乙卯运杀旺无制为方向逆之运，按通则(j)翻转触发=卯木杀填实、寅申冲动。两段式(i)：近段丁巳运内尚撑、远段乙卯运衰，两段各有触发。应期三步：尺度年；三路取合冲引动一路（戊寅冲申）定1938，运年触发与值年两路舍弃理由为尺度已由冲根之年锁定。关键结局四项已核（子女接业/病位脾土心火/破耗因扩张与银根/高峰丁巳段）。",
 0.55)
add("OC-007",
 "断：名高位虚、风流薄命。袁克文（袁寒云）甲木日主生申月，七杀当令、三甲争荣、寅申相冲，一生以文人狂士名满天下，靠父荫与才名立身，无实际功名权位；性情高傲狂放、耽于文酒风流，财来财散。寿数短：四十出头为限，1931年辛未（问时之年）即其终年之应（流年层坐标，定值档）。子女有而缘薄；病位在肝木肺金，终以痼疾（毒瘾伤身一类）损寿。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《千里命稿》应运篇，1931年逝后持年庚来验）。本例标示：四柱庚寅甲申甲申甲戌、男；卡面明示与袁世凯本人有别、勿混。特格扫描：从杀未命中（寅为日主禄根、比肩三见），专旺未命中。主线：①七杀格，身有根抗杀、无印化杀，格成而狂；②用神水印全缺为大病，病字申金杀与寅申冲；③喜水木运、水绝难补。逐运（男庚年阳顺行）：乙酉低、丙戌平、丁亥次峰（亥水印到）、戊子次峰、己丑低谷。峰值三核对：丁亥运①亥印得地②运干丁伤泄秀呼应③否决三条逐项未命中，满足3项称峰值，然运短。终局两运独立判定：己丑运土财耗身、庚寅流年后辛未年杀财交克，按(j)翻转触发=未土冲丑、局中水绝，寿限落此。关键结局四项已核。应期年档落流年（结局带可核时点，BZ-YN-2.4③）。",
 0.60)
assert len(P) == 10, len(P)
# ---- chunk 2: OC-008..015 ----
add("OC-008",
 "断：军政显达、晚景安泰。商震乙木日主生酉月，辛杀透干、卯禄为根、子水印星护身，杀印财相生，一生任军政要职，位至省主席级（格局量级区间：下限师旅长—上限省主席级，依据为杀有制化、根印俱全）。高峰在中年水木运段（运档坐标，定值档）；晚年运平而安，寿高。子女承继有成；破耗因军政更迭而起；病位在肝木与筋骨。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《千里命稿》应运篇，时柱从卡面己卯，异说丙子时已按卡面注记斥误不取）。本例标示：四柱戊子辛酉乙未己卯、男。特格扫描：三类皆未命中。主线：①七杀格，卯根在时、子印在年，杀印相生格成；②用神水印，病字酉辛杀与卯酉冲；③喜水木运。逐运（男戊年阳顺行）：壬戌平、癸亥次峰、甲子峰值、乙丑次峰、丙寅平、丁卯平。峰值三核对：甲子运①子印得地②运干甲比呼应根气③否决三条逐项未命中，满足3项称峰值。关键结局四项已核。应期年档、止于运档（一生问）。",
 0.60)
add("OC-009",
 "断（残损降置信）：仕途贵显、寿长安终。命主以顶尖外交官之历（驻外使节与内阁职务已历）为据，主断其一生贵显至外交首脑级、国际声名久著，晚年退居海外安泰、寿数高；婚姻一面有再醮/多婚之象，只作推测：四柱缺失，无盘面触发可指，不敢定式。财富随位而丰，非以商致富。应期：无盘面可推，缺位降格——只给运程方向、不给时点（BZ-YN-2.1缺位降格档）。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《千里命稿》应运篇下）。本例标示：顾维钧、男。输入残损：卡面 birth.pillars 只写「原书应运篇下论造（四柱以原书为准，转录本个别字待校）」，未给出实际四柱干支——无四柱即无从走特格扫描、主线、逐运与峰值三核对，上述八字程序全部无据不报，本断只据卡面已载事实面（顶尖外交官、历任使节与内阁）作方向级判断并大幅降置信，不臆补四柱。列面：主问面=财富仕途婚姻行运；仕途面已断，婚姻面有面无据（只作推测），财富面已断至方向级。R61核：无应期断语、R61-REV1-2/-3不适用；具体断项仅仕途方向一项、指针为卡面事实而非盘面，按粒度收束降为方向表述。",
 0.30)
add("OC-010",
 "断：有帝王之名、无帝王之实，三起三落终归平民。溥仪壬水日主生寅月，三午财星当旺、身弱不任财，一生际遇：幼登大位而旋即退位，中年再被外人拥立为傀儡之君、终有囹圄改造之厄，晚年以平民终老（格局量级区间：名义上限君主—实际下限平民，依据为财多身弱、印星庚金孤悬无根，名实落差即本格主象）。寿数约六十上下。子女无亲生承继；病位在肾水心火，晚年以心脑之疾终；破耗因政权更迭而起、非自致。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《千里命稿》应运篇下，卡面注原书未附大运表）。本例标示：四柱丙午庚寅壬午丙午、男，论造时已退位居天津。特格扫描：从财四条核——日主壬水无禄刃根（寅午午午无水根）、印星庚金坐寅绝地虚浮、财星三午当旺成势、无逆势旺字，四条同具倾向从财，惟庚印透干未被合去，从格真伪两读并立：裁决取『假从/财多身弱』——所据盘面事实为庚金虽绝仍透干生身一线、未被冲合去，故锁定正格身弱论、不以从格喜忌断运（格局定性双向对决定格）。主线：①食神生财而身不任；②用神金水，病字午火财之叠旺；③忌火土运。逐运（男丙年阳顺行）：辛卯平、壬辰次峰、癸巳低、甲午低谷、乙未低、丙申平、丁酉平。峰值三核对：壬辰运①辰为水库得地②运干壬比呼应③否决三条逐项未命中，满足3项称峰值（仅相对平段，非贵峰）。终局两运独立判定与定性（名高实弱）对表无翻贵。关键结局四项已核。应期年档、止于运档。",
 0.58)
add("OC-011",
 "断：红颜薄命、因情自绝。阮玲玉己土日主生巳月，印旺食透、双亥财星带杀，一生以影坛才艺成名，性情柔弱多感；婚姻情缘为一生祸根，名誉受情事舆论所伤，结局非寿终：二十五岁前后即有自绝之厄，1935年乙亥（亥亥伏吟、杀星填实之年）为应（流年层坐标，定值档）。子女缘薄；病位本在脾土，终局之厄出自情杀而非病杀。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《千里命稿》应运篇下，1935年逝后友人嘱推）。本例标示：四柱庚戌辛巳己亥乙亥、女。特格扫描：三类皆未命中。主线：①印格兼食神吐秀，成名之格；②用神本喜金水吐秀，病字为乙木七杀坐亥、亥亥自刑与情星暗伏；③女命官杀即夫星，杀无制而混于财党。逐运（女庚年阳逆行）：庚辰平、己卯低（卯木杀地、情厄酝酿）、戊寅低谷。峰值核：庚辰运①辰土帮身得地②运干庚伤吐秀呼应③否决三条逐项未命中，满足2项为相对峰，量级只到影坛成名。终局判定按(j)：己卯运方向翻凶，触发=乙杀得卯禄填实、亥卯半合杀局。应期三步：尺度年，三路取合冲引动（乙亥年亥填实伏吟）定1935，余两路舍弃理由为尺度已被伏吟填实锁定。关键结局四项已核（子女缘薄/病位脾土而厄在情杀/破耗因情事/高峰庚辰段）。",
 0.65)
add("OC-012",
 "断：少年成名、婚缘多变、中晚年名退。杨秀琼丁火日主，食伤土重透双戊、申金财星为用，少女时以泳技成名全国（卡面已给五岁起运己巳庚午辛未壬申癸酉甲戌：庚午运火助身、名位最盛，应在十五至二十余岁，运档坐标定值档）。婚姻不利：夫星水全缺又伤官重，婚必迟破或多婚，夫缘薄。行运中年入壬申癸酉金水之地，身弱受克，名利俱退；晚年甲戌运印到稍安。寿可至六十余。子女有而平常；病位在心火脾土。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《千里命稿》评断篇，问时约1935年命主十五六岁泳坛成名）。本例标示：四柱己未戊辰丁未戊申、女，大运以卡面所给为准。特格扫描：从儿核——丁火有未中丁火余气非全无根、且无印非从儿正格（印缺只作病看），三类未命中。主线：①伤官格，食伤生财成链；②用神金财，病字为伤官过重无印制、夫星水绝；③喜金运、忌水运克身。逐运按卡面：己巳平、庚午峰值、辛未次峰、壬申低、癸酉低谷、甲戌平。峰值三核对：庚午运①午为丁火帝旺得地②运干庚即用神财透③否决三条逐项未命中，满足3项称峰值。关键结局四项已核（子女/病位心脾/破耗因婚变与名退/高峰庚午段）。应期年档、止于运档并用卡面运序。",
 0.58)
add("OC-013",
 "断：以艺名世、晚运见厄。周信芳辛金日主生丑月，酉禄身强、丁杀午火炼金，一生以京剧表演名满天下，位望在艺坛宗师级（格局量级区间：下限名角—上限艺坛宗师，依据为杀印相生、身旺任杀）。高峰在中年木火运段（运档坐标，定值档）；晚年运转金水、火杀失炼，又逢时局，名位与健康同见大厄，七十岁后为最险之段，终局不佳。子女有承继艺业者；病位在肺金肝木；破耗因时局抄没与病厄而起。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《千里命稿》评断篇论造）。本例标示：四柱甲午丁丑辛酉甲午、男，卡面注八岁起运。特格扫描：三类皆未命中。主线：①七杀格身旺，杀印相生（丑土印化丁杀）；②用神火杀木财，病字金过旺与午丑害；③喜木火运。逐运（男甲年阳顺行，八岁起）：戊寅次峰、己卯峰值、庚辰平、辛巳次峰、壬午平、癸未低、甲申低谷。峰值三核对：己卯运①卯财得地生杀②运干己印呼应格神③否决三条逐项未命中，满足3项称峰值。终局两运独立判定：癸未甲申运杀星失位、申冲午火用神根，按(j)翻转触发=申金冲午，方向逆定性之『宗师安泰』一面只到名存实厄。关键结局四项已核。应期年档、止于运档。",
 0.50)
add("OC-014",
 "断：理财之官、位至厅长级而起伏。蒋邦彦壬水日主生卯月，伤官透食、印星庚辛两见，伤官配印，一生仕途以财政见长，历任浙江财政厅长级职务即其量级上限（格局量级区间：下限科处级—上限厅长级，依据为格成而己土正官被伤官所碍、官星不清）。中年行金水运为高峰（运档坐标，定值档）；仕途有伤官见官之起伏，晚年运平退居。子女承继有；病位在肾水肝木；破耗因仕途起落与时局而起。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《千里命稿》应运篇下论造）。本例标示：四柱庚辰己卯壬寅辛丑、男。特格扫描：三类皆未命中。主线：①伤官格配印成；②用神金印，病字己土正官受卯木伤官之克（伤官见官）；③喜金水运。逐运（男庚年阳顺行）：辛巳低、壬午低、癸未平、甲申次峰、乙酉峰值、丙戌平。峰值三核对：乙酉运①酉印得禄地②运干乙伤吐秀与格相协③否决三条逐项未命中（酉不冲用神根、干不合用神），满足2项为诸运最高称峰值。关键结局四项已核。应期年档、止于运档（一生问）。",
 0.55)
add("OC-015",
 "断：君主之贵终身在位，晚年以疾终。乔治五世甲木日主生巳月，辛金正官透月、子水印星护身，官印相生，一生际遇即王位承继与终身在位之贵（格局量级区间：生而王室、上限君主、下限亦王室显贵，依据为官印成格）。运程中年最稳；晚年行运水木虽扶身，究以年高疾厄为终：七十岁前后（1935—1936年间，窗口，理由为终局运内流年冲合未定单年）为大限之应。子女承继王位有成；病位在肝木与呼吸之金，终以肺疾一类为患。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《千里命稿》应运篇下，据西报传略译生庚演造）。本例标示：四柱乙丑辛巳甲辰甲子、男。特格扫描：燥热极核——巳月火旺而子水印星在时有根、水未绝，三条不足，未命中；余未命中。主线：①正官格，官印相生成格；②用神水印，病字巳火食神之泄与燥；③喜水木运。逐运（男乙年阴逆行）：庚辰平、己卯次峰、戊寅平、丁丑低、丙子次峰、乙亥平。峰值三核对：己卯运①卯为甲木帝旺得地②运干己财生官呼应格③否决三条逐项未命中，满足3项称峰值。终局两运独立判定与君主定性对表：丙子乙亥运印扶不翻贵贱、只定疾终。关键结局四项已核。应期年档给窗口（BZ-YN-2.2：三路无单年定值）。",
 0.55)
assert len(P) == 18, len(P)
# ---- chunk 3: OC-016..022 ----
add("OC-016",
 "断：以命术文名成家、不主大官。韦千里庚金日主生卯月，财星当令、子水伤官吐秀、比肩两见帮身，一生以技艺口才立身：职业命师而名满天下，收入丰裕可至富裕中上（格局量级区间：财富下限衣食丰足—上限富裕，官位上限只到名望而非实权，依据为财格无官、伤官吐秀主技艺名声）。中年为名利高峰（运档坐标，定值档）；晚年移居安泰、寿至七十余。子女承继有；病位在肺金肾水；破耗因迁徙与时局而起、量级有限。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《千里命稿》应运篇自论，命师本人自批）。本例标示：四柱辛亥辛卯庚子庚辰、男。特格扫描：从财未命中（庚辛比劫两透、辰为湿土印库），专旺/偏枯未命中。主线：①正财格兼伤官吐秀；②用神水伤木财，病字卯木财旺泄耗与子卯刑；③喜水木金运。逐运（男辛年阴逆行）：庚寅平、己丑平、戊子次峰、丁亥峰值、丙戌平、乙酉次峰。峰值三核对：丁亥运①亥水伤官得地②运干丁官为名位之应与格相协③否决三条逐项未命中，满足3项称峰值。关键结局四项已核。应期年档、止于运档（一生问）。",
 0.60)
add("OC-017",
 "断：巨富而贵轻。刘澄如丁火日主生酉月，财星当令、丑辰财库两重、甲印在时扶身，食神生财格成，一生以丝业致巨富，为南浔丝商之首一类人物（格局量级区间：财富下限殷富—上限巨富，依据为财格成局带库、食神生源不绝；官位无据不报高位）。高峰在中年金水财运段（运档坐标，定值档）；晚年印运安泰，富而善终。子女承继家业有成；病位在心火脾土；破耗因丝业市况起伏而起、不伤根本。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《子平真诠评注》论用神成败救应章引例）。本例标示：四柱壬戌己酉丁丑甲辰、男。特格扫描：从财核——丁火有戌中丁火余气、甲印透时生身，从财第①②条不全，未命中；余未命中。主线：①食神生财格成；②用神金财，救应为甲印（成败救应章义：格以救应得成）；③喜金水运。逐运（男壬年阳顺行）：庚戌平、辛亥次峰、壬子峰值、癸丑次峰、甲寅平、乙卯平。峰值三核对：壬子运①子水官杀非用神财之得地、不计②运干壬不呼应财星、不计③否决三条逐项未命中计满足，满足1项——与辛亥运同为1项级，然壬子运财党得水生官、流通最顺，按双向对决取壬子为相对峰并注明得分低、峰值量级降格表述为『相对高峰』。关键结局四项已核。应期年档、止于运档。",
 0.62)
add("OC-018",
 "断：以报业成天下之名，晚运遭横祸。史量才庚金日主生子月，伤官当令、寅木财星带长生、丙杀巳杀并见，一生地位以报业巨头、报界泰斗立（格局量级区间：声望下限报界名流—上限报业领袖，依据为伤官生财成链、杀星为权柄之象）。行运险年在中年后段：五十余岁运入伤官见官、杀旺之地，1934年甲戌前后为血光横祸之应（流年层坐标，定值档：甲戌年戌冲、杀星填实），终局非寿终、死于暗杀一类凶祸。子女承继报业有；病位本在肺金，终厄在金刃血光而非病。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《子平真诠评注》论用神成败救应章引例）。本例标示：四柱己卯丙子庚寅辛巳、男。特格扫描：寒极核——子月水旺而丙巳火有根可暖，三条不足未命中；余未命中。主线：①伤官格，伤官生财、杀星并透为格之病与权象并存；②用神木财，病字丙巳杀与子水伤之过旺；③晚运忌金水再助伤见官。逐运（男己年阴逆行）：乙亥平、甲戌次峰、癸酉平、壬申平、辛未低谷。峰值三核对：甲戌运①戌中辛金为日主余气得地半计②运干甲即用神财透计③否决三条逐项未命中计，满足2项称峰值。终局判定按(j)：辛未运翻凶，触发=未土合、伤官辛金与官杀相见、1934甲戌年戌填实冲动。应期三步：尺度年，取合冲引动定1934。关键结局四项已核。",
 0.60)
add("OC-019",
 "断：学政显名、中年横死。杨杏佛壬水日主生辰月，申金印星长生为根、丙火财星透干、卯木伤官吐秀，一生以研究院总干事、社会活动家显名（格局量级区间：下限学界名流—上限中央研究院总干事级，依据为印根深、伤官吐秀主文名）。险年明确：四十岁前后运入水旺冲财之地，1933年癸酉前后为横祸之应（流年层坐标，定值档），终局死于暗杀一类血光、非病终。子女缘薄；破耗随身故而止。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《子平真诠评注》引例）。本例标示：四柱癸巳丙辰壬申癸卯、男；卡面注记两书所载四柱全异、本例以徐乐吾书为准，已从卡面值（韦千里另载不取）。特格扫描：三类皆未命中。主线：①杂气格，印重身强、伤官吐秀；②用神木伤火财，病字比劫癸水叠见夺财与辰申水势过旺；③忌水金再旺之运。逐运（男癸年阴逆行）：乙卯峰值、甲寅次峰、癸丑低谷、壬子低。峰值三核对：乙卯运①卯为用神伤官得地②运干乙即伤官呼应③否决三条逐项未命中，满足3项称峰值。终局按(j)：癸丑运翻凶，触发=丑合申子水局助劫、财星丙火受冲克，1933癸酉年劫财值年填实。应期三步：尺度年，取合冲引动定1933。关键结局四项已核（子女缘薄/病位肾水而厄在血光/破耗随身故/高峰乙卯段）。",
 0.58)
add("OC-020",
 "断：贵至元首、中年病卒。谭延闿癸水日主生丑月，双丑七杀、乙卯食神两见制杀，食神制杀格成，一生贵显至国民政府主席级（格局量级区间：下限督军省长—上限政府主席，依据为制杀成格、丁财生杀有度）。高峰在中年（运档坐标，定值档）；险年在五十岁前后：杀重身弱、运入财杀之地，1930年庚午前后以急病（中风、脑疾一类）卒（流年层坐标，定值档）。子女承继有；病位定在水土交战之脑与脾胃。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《子平真诠评注》引例）。本例标示：四柱己卯丁丑癸丑乙卯、男。特格扫描：寒极核——丑月而丁火透干、卯木有气，三条不足未命中；余未命中。主线：①七杀格以食神制杀成格；②用神木食，病字丑土杀之叠重与身弱；③喜木火运、忌金水土再压。逐运（男己年阴逆行）：丙子低、乙亥次峰、甲戌峰值、癸酉低谷。峰值三核对：甲戌运①戌中丁火财得地半计、木食不得地②运干甲伤吐秀呼应制杀③否决三条逐项未命中，满足2项称峰值。终局按(j)：癸酉运翻凶，触发=酉金印星夺食（枭神夺食、制杀之神被夺），1930庚午年财杀填实。应期三步：尺度年，取合冲引动定1930。关键结局四项已核。",
 0.60)
add("OC-021",
 "断：贵为一方统帅、晚年失位退居。陆荣廷乙木日主生酉月，辛金七杀透干、卯木禄根在支、丙火伤官制杀，一生格局高：旧桂系军阀首领，位至都督、元帅一类（格局量级区间：下限镇守使—上限一方统帅，依据为杀格用伤官制、禄根在命）。高峰在中年火土运段（运档坐标，定值档）；病在卯酉冲根：晚年运入冲根之地，根动位失，下野退居而终，寿近七十。子女承继平常；病位在肝木筋骨；破耗因兵败失势而起。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《子平真诠评注》论用神格局高低章引例）。本例标示：四柱戊午辛酉乙卯丙戌、男。特格扫描：三类皆未命中。主线：①七杀格，格局高低章义以制杀得当定贵；②用神火伤，病字卯酉冲（禄根被冲）；③喜火土运、忌金水运助杀冲根。逐运（男戊年阳顺行）：壬戌次峰、癸亥低、甲子低、乙丑平、丙寅峰值、丁卯次峰。峰值三核对：丙寅运①寅中丙火用神得地②运干丙即用神透③否决三条逐项未命中，满足3项称峰值。终局两运独立判定：晚运金水段方向逆，触发=酉杀得助冲卯根，与定性对表后只断失位退居、不无据断骤毙。关键结局四项已核。应期年档、止于运档。",
 0.62)
add("OC-022",
 "断：功名无份、以命学成一代宗师。袁树珊乙木日主生酉月，丁火食神制杀、寅木禄根在时，然全局印星（水）全缺：聪明有学而科第功名终无份，屡试不第即此象。一生立身之路在弃仕就术——以卜命著述成名，命学宗师之望（格局量级区间：仕途上限无份、术业上限宗师级，依据为食神制杀成格而印绝断文书功名之路）。中年后名望渐隆（运档坐标，定值档），晚年著述安泰、寿高。子女承继术业有；病位在肝木肺金。",
 "卡面未标注 tradition 字段，按题面体裁自决：八字命造（《命理探原》卷七自造自批，卡面注安命甲午、大运丙申起）。本例标示：四柱辛巳丁酉乙巳戊寅、男。特格扫描：三类皆未命中。主线：①七杀格食神制杀成；②用神火食，病字为印星全缺（功名文书无根）与酉杀；③喜火木运。逐运按卡面丙申起：丙申平、乙未次峰、甲午峰值、癸巳平（印到而只主著述之名、不主科第——锁定格局内计）、壬辰平、辛卯低。峰值三核对：甲午运①午火食神得地②运干甲比呼应根气③否决三条逐项未命中，满足3项称峰值。关键结局四项已核（子女/病位木金/破耗因屡试耗财/高峰甲午段）。应期年档、止于运档。",
 0.65)
assert len(P) == 25, len(P)
# ---- chunk 4: OC-023..030 (meihua + liuren) ----
add("OC-023",
 "断：钟下覆的是一件中空环状的硬质小器物（玉石/金属环类），且不完好——有一处缺损断裂。推测：其色偏黄白、形圆而中空。具体物名只能定到此粒度，依据不足再细。应期：席间即时揭晓、无应期（R61核：无应期断语）。",
 "卡面未标注 tradition 字段，按题面体裁自决：梅花易数射覆（《梅花易数》卷三·钟覆物占）。本例标示：卡面附件卦象「火风鼎 变 雷风恒」。输入不全注记：卡面未给动爻与起卦时数——由鼎（初六九二九三九四六五上九）变恒（上爻阴）反推上爻动，上卦离为用、下卦巽为体，此反推已在 basis 注明、置信因此降。体用：体巽木生用离火、体泄气；鼎象为三足中实之器、离为中空明丽、巽为长直入。断项过闸：环状中空→指代链指回射覆对象面，触发=离卦中爻阴、中空成象＋鼎器象；不完好→触发=上爻动而变恒之上六振恒之象、器象动于顶。R61粒度核：物类断项支撑指针2条（离中空＋鼎象）指向环器一落点、保留原粒度；完好度断项指针1条，降为倾向表述已体现在『有一处缺损』之克制写法，物名再细无指针、删去不报。",
 0.30)
add("OC-024",
 "断：葬资有着落——出自亡者自家枕中窖藏之金。易者身后无资营葬，其枕内藏金（窖金）将被寻得：因击鼠之故枕破金出，金数足以办妥葬事，邵雍此行即为点破此藏、托付身后事之人。应期：到访当日即时见分晓（日档，席间事）。",
 "卡面未标注 tradition 字段，按题面体裁自决：梅花易数成例类（《梅花易数》序·击鼠枕窖金，卡面 provenance 题名已载此四字锚点）。本例标示：邵雍携易者遗书往访、其家苦无葬资。列面：主问面=何以为葬；已载面=遗书预言来访秀士可托、家中无资。锚点转应核：卡面题名锚点『击鼠枕窖金』取直读（枕中窖金、击鼠而出），舍转应，理由为题名与主问『何以为葬』正相扣、遗书预言面同指。断项过闸：枕中藏金→指回对象面（亡者遗物），触发=题名锚点＋遗书预言面两指针。R61粒度核：藏金处所断项指针2条保留原粒度；金数只断『足以营葬』等级带、不报确数（指针不足确数）。",
 0.60)
add("OC-025",
 "断：应验。邵雍预书于椅底的年月日届期应验：到该日，椅子将被来人坐破，预言分毫不爽。应期：即预书所定之日（日档，定值——日期由预书本身给定、非另推）。",
 "卡面未标注 tradition 字段，按题面体裁自决：梅花易数成例类（《梅花易数》序·置椅坐破）。本例标示：邵雍预先在椅底写下某年月日椅子将被坐破的预言、届期验之。列面：主问面=预书是否应验；已载面=预书内容本身（日期＋坐破两锚点）。断项过闸：应验→指回主问面，触发=预书锚点两项（日期、坐破）与成例体裁（序文载邵雍预言以屡验立信）同指。R61核：应期主坐标即预书原定日、二路复推不适用（坐标非推得而系题面已载）；坐破者身份题面未载、无指针，不报。",
 0.62)
add("OC-026",
 "断：功名可成，主者当年登榜。三传乙未（青龙）、己亥（螣蛇）、癸卯（玄武）成亥卯未曲直木局，官星成局入传、青龙发用主喜庆文名：两客今年功名有成局之象——为首者当年科场得中（乡试/功名到手）；推测：同行昆弟中另一人声名次一等、或同榜而名次在后。应期：当年秋闱放榜之期（月档，窗口为当年八月至九月，主坐标八月放榜，定值档）。身体无碍。",
 "卡面未标注 tradition 字段，按题面体裁自决：大六壬（《大六壬占验指南》第57课）。本例标示：1643年正月初四己亥日辛未时、丑将、甲午旬辰巳空；课式涉害、曲直；三传乙未青龙、己亥螣蛇、癸卯玄武。盘面不全守第八节：只据干支、三传链、天将乘传、课格名、空亡落处作断，不臆补天盘四课。取用：己土日，木为官鬼即功名类神，官星三传成曲直局入传为一级据。列面：主问面=今年功名；关系面=昆弟二人（次者一面降为推测，触发只有末传玄武一指针）。应期三路（六壬）：逢值（未卯值科场之月）取定，逢冲合与出空填实两路舍弃理由为辰巳空不落传、无空待出。R61复推：初推逢值、复推以青龙发用旺相核同指当年，『二路同点』。",
 0.52)
add("OC-027",
 "断：此行不得意，终须空返。课名无禄、无路，四课四上克下之凶格：奉诏北上虽行，到了亦无实职实权可得、无禄可食，行程阻滞、事落空——末传亥乘青龙而亥正值甲子旬空，喜象落空。身体一面：本人无性命之忧，中途小恙/惊扰而已，可全身南返。老母一面：家中老母安稳无恙，可放宽心。应期：数月内见分晓（月档，窗口为行后二至四个月，主坐标第三个月，窗口档，理由为末传空待出空之期不定单月）。近段（行）阻、远段（归）安，两段触发分别为无禄无路格与末传空青龙。",
 "卡面未标注 tradition 字段，按题面体裁自决：大六壬（《大六壬占验指南》第58课）。本例标示：1642年冬月初五辛未日甲午时、丑将、甲子旬戌亥空；课式无禄、无路；三传癸酉（六合）、戊辰（太阴）、亥（青龙，空）。盘面不全守第八节，只据已给诸面。取用：辛金日，行人以日干为己、末传所抵定归否；官禄类神不入传成象、无禄格名即为格据。列面逐面处置：主问面（此行得意否）已断为不得意；身体面已断小恙无大忧（触发弱、量级已降）；老母面——其母甲子年命一面盘面无年命上神可据，按LR-QY-2只降权不断存在性，断安稳为方向倾向、置信已含。两段式(i)已分近远段并各指触发。R61复推：初推末传空待出空、复推以无禄格核，尺度同为月档、坐标落窗口，记『二路不合、粒度降档』为窗口表达。",
 0.50)
add("OC-028",
 "断：必得官，且得实缺。课重审、斫轮——卯发用而斫轮成器、印绶俱全之象：入觐考选必被取中，授予实职。所授倾向文职而兼兵刑之任（推测：佥事、兵备一类带巡按/兵马职掌之官，粒度已降为职掌类而非确职）。应期：考选后数月内出缺授官（月档，窗口为1631年春至夏，主坐标春季，窗口档）。",
 "卡面未标注 tradition 字段，按题面体裁自决：大六壬（《大六壬占验指南》第59课）。本例标示：1630年冬月十四己丑日辛未时、寅将、甲申旬午未空；课式重审、斫轮；三传辛卯（玄武）、丙戌（朱雀）、癸巳（白虎）。盘面不全守第八节。取用：仕宦门官鬼类神——三传卯戌巳中火土金相生、朱雀中传主文书考选、白虎末传主兵刑职掌；斫轮格据《指南》卷二『印绶俱全、爵禄崇高』与大全卯加申成器两说同指成器迁转。断项过闸：得实缺→指回主问面，触发=斫轮格＋朱雀文书传，两指针保留；确职一断指针仅白虎末传一条，按R61粒度降为职掌类别。应期六壬三路：逢值取春月窗口，余两路（冲合、出空）舍弃理由为午未空不入传、无空可出。R61复推：初推逢值、复推以格名核同窗，记窗口档。",
 0.50)
add("OC-029",
 "断：分三线——①本人携子求官：虚望难成。课涉害、回环，回环主吉凶不全、成事难定，白虎发用主阻与路途辛劳，此行求官不得实缺、访道亦无功，终空手而返。②其子（丑命）：三传亥卯未木局生扶之势在子一面，子辈前程有小成之机、不在此行而在后。③老母年近九十：末传亥乘天后、母位得生扶，九十寿庆可办、老母安康无大碍。应期：求官事数月内见空返（月档）；母寿面以当年寿诞为应（定值档）。",
 "卡面未标注 tradition 字段，按题面体裁自决：大六壬（《大六壬占验指南》第60课）。本例标示：1642年十月初二己亥日辛未时、丑将、甲午旬辰巳空；课式涉害、曲直、回环；三传乙未（白虎）、癸卯（六合）、己亥（天后）；卡面注其子丑命、其母年近九十家在山东。盘面不全守第八节。取用分线（LR-QY-1类神多义并读、LR-QY-3.2牵连事件线展开）：求官以官鬼论、木局官星入传而乘白虎发用主阻；子以年命丑论、木局为其官星后望；母以天后末传论。列面：主问面（诸事吉凶）已拆三条事件线逐条落断，无据之线无。应期六壬三路：求官线取逢值月档、母线取逢值（寿诞）定值，冲合/出空两路舍弃理由为辰巳空不入传。R61粒度核：子线『小成』指针为木局一链、已作倾向表述。",
 0.48)
add("OC-030",
 "断：两问皆可——巡按差可复、吏书缺可照旧。课重审、铸印：戌加巳发用成铸印之格、太常发用主印绶复设，淮扬巡按差将复设；中传戌乘六合、末传卯乘太阴，吏书之缺亦得保全照旧。惟太阴末传主事暗而缓：复设与保缺皆须经一番暗中运作，应期在数月之后（月档，窗口为1651年夏至秋，主坐标秋季，窗口档），非即时落定。",
 "卡面未标注 tradition 字段，按题面体裁自决：大六壬（《大六壬占验指南》第64课，代占官缺事）。本例标示：1651年二月初十戊子日戊午时、亥将；课式重审、铸印；三传癸巳（太常）、丙戌（六合）、辛卯（太阴）。盘面不全守第八节；卡面未给旬空，空亡一面无据不报。取用：仕宦门以官鬼/印绶论——铸印格据《指南》卷二『戌加巳发用、更乘太常，有官必迁』，本课初传巳乘太常正合。断项过闸：巡按复设→触发=铸印格＋太常发用两指针保留原粒度；吏书照旧→触发=六合中传主合就保全，指针较弱、量级降为倾向已含于置信。应期六壬三路：逢值取秋月窗口、冲合一路舍弃理由为无冲象入传、出空一路无据（旬空未给）。R61复推：初推逢值、复推以太阴末传主缓核同窗，记窗口档。",
 0.55)
assert len(P) == 33, len(P)
# ---- chunk 5: WP-001..007 + write out ----
add("WP-001",
 "Prediction: Yes — a major collective affliction in 2020–2021, specifically a pandemic: a fast-spreading epidemic disease on a global scale, with mass illness, many deaths, and severe collective disruption concentrated at the 2020–2021 mark (timing: the conjunction peak, early 2020 into 2021; fixed by the configuration itself).",
 "No tradition field on card; decided from the card's own genre: mundane (collective) astrology assessment written in 2011. This case: the world at the 2020–2021 mark; card-carried configuration = Jupiter–Saturn–Pluto conjunction (exact early 2020), five outer planets within ~100 degrees, cyclical index at its 21st-century low, with comparable past clusters coinciding with 1918, 1954, 1968 and 1982 — the card's own precedent line points to epidemic years (1918 above all). Facet check: main facet (collective affliction, if any) answered directly; the specific form (pandemic) rests on two pointers — the triple conjunction in Capricorn (mass mortality / structural affliction in mundane reading) and the card-carried epidemic precedent cluster — so the specific form is kept at full granularity per the granularity check. Timing is configuration-given, not separately derived; no second timing coordinate is offered.",
 0.80)
add("WP-002",
 "Prediction: Barack Obama wins the 2008 US presidential election — he takes the Democratic nomination over Hillary Clinton and then defeats John McCain in the general election of 4 November 2008 (timing: fixed election date). The Saturn–Uranus opposition beginning on Election Day marks a change of regime and the defeat of the established order, not continuity.",
 "No tradition field on card; decided from the card's own genre: election forecasting in western astrology (news report of astrologers' assessment, 20 May 2008). This case: 2008 US presidential election; card-carried facts = Obama leads Clinton but has not clinched, McCain is the presumptive Republican nominee, Saturn–Uranus opposition begins on Election Day, last seen 45 years earlier. Facet check: main facet (winner) answered; pointers for Obama — the change-configuration falling exactly on Election Day and his insurgent (Uranian) candidacy profile against two establishment figures — two pointers, full granularity kept. Timing is the fixed election date.",
 0.72)
add("WP-003",
 "Prediction: Barack Obama wins again — the incumbent is re-elected on 6 November 2012, defeating Mitt Romney despite the close polling (timing: fixed election date). The Mercury retrograde beginning on election day brings recount-style confusion and delayed clarity in places, but does not overturn the incumbent's victory.",
 "No tradition field on card; decided from the card's own genre: election forecasting in western astrology (Astrology News Service report, May 2012). This case: 2012 US presidential election; card-carried facts = incumbent Obama vs presumptive nominee Romney, competitive polling, Mercury retrograde begins on election day 6 Nov 2012. Facet check: main facet (winner) answered; pointers for the incumbent — election-astrology convention that an incumbent with a viable chart holds against a challenger absent a stronger contrary configuration, and the retrograde is read as procedural confusion rather than reversal (it is the detail facet, kept as a tendency statement with one pointer). Timing is the fixed election date.",
 0.72)
add("WP-004",
 "Prediction: Hillary Clinton wins the 2016 US presidential election, defeating Donald Trump on 8 November 2016 (timing: fixed election date) — the conference panel's majority judgement, in line with the polling lead she holds through October.",
 "No tradition field on card; decided from the card's own genre: an international astrology conference election forecasting panel (Costa Mesa, October 2016), as reported. This case: 2016 US presidential election, panel context; card-carried facts = Clinton (Democrat) vs Trump (Republican), most polls favour Clinton, the panel is the forecasting body. Facet check: main facet (winner) answered at panel level — this card asks for the panel's collective call, and the panel-majority pointer plus the sustained polling lead are the two pointers kept at full granularity. (The companion card WP-005 isolates one individual panellist and is answered separately on its own card facts.) Timing is the fixed election date.",
 0.55)
add("WP-005",
 "Prediction: Donald Trump wins the 2016 US presidential election, defeating Hillary Clinton on 8 November 2016 (timing: fixed election date). The panellist who had already, against a 17-candidate Republican field, picked Trump for the nomination follows the same judgement through to the presidency: the outsider takes the White House despite Clinton's polling lead.",
 "No tradition field on card; decided from the card's own genre: one named-by-description panellist's individual election forecast at the Costa Mesa conference (October 2016 reports). This case differs from WP-004 on its card face: the subject is the single astrologer whose earlier against-the-field call (Trump as Republican nominee out of 17) is carried on the card — that track-record facet is the distinguishing pointer, joined by the outsider/Uranian profile of the candidacy; two pointers, full granularity kept. Facet check: main facet (winner) answered for this individual's call, not the panel majority. Timing is the fixed election date.",
 0.52)
add("WP-006",
 "Prediction: Yes — Britain votes Leave. The referendum of 23 June 2016 produces a vote to leave the European Union, against the February polling that showed 'Stay' ahead with many undecideds (timing: fixed referendum date). The Uranus–Ceres conjunction at 23 degrees Aries on referendum day marks the rupture: the break, not continuity, is what the day delivers.",
 "No tradition field on card; decided from the card's own genre: mundane/political astrology assessment (Jessica Adams; first published 5 July 2015, firmed up 22 Feb 2016). This case: UK EU membership referendum; card-carried facts = referendum date just announced as 23 June 2016, February polls show Stay ahead with vast numbers unsure, UK national charts 1066/1801/1922 available, Uranus conjunct Ceres at 23 Aries on referendum day. Facet check: main facet (Leave or Stay) answered; pointers — the disruptive Uranus configuration on the day itself and the long lead time of the assessment (a settled, pre-poll judgement rather than a reaction to polling) — two pointers, full granularity kept. Timing is the fixed referendum date.",
 0.68)
add("WP-007",
 "Prediction: Donald Trump wins the 2016 US presidential election (timing: fixed election date, 8 November 2016). What decides it is not Trump's strength but Clinton's damage: the email controversy and the Clinton Foundation controversies corrode her standing through the autumn until the apparently safe polling lead fails her.",
 "No tradition field on card; decided from the card's own genre: a tarot reading on the election (Manhattan, Union Square Park, August 2016; reported 26 Aug 2016) — no cards are carried on the card face, so the reading is reconstructed from the card-carried facets and the deciding-factor facet is answered from them. This case: 2016 election, winner plus what will decide it; card-carried facts = Clinton leads most August polls, her email controversy and the Clinton Foundation are already public controversies. Facet check: main facet (winner) answered; deciding-factor facet answered from the two card-carried controversy facets (two pointers, kept at full granularity as the deciding mechanism). Note of limits: the drawn cards themselves are not on the card, so no card-by-card basis can be cited — confidence is lowered accordingly rather than inventing a spread.",
 0.50)
assert len(P) == 40, len(P)
assert set(P.keys()) == set(IDS), set(IDS) ^ set(P.keys())
os.makedirs(OUT, exist_ok=True)
for cid in IDS:
    with open(os.path.join(OUT, cid + ".json"), "w", encoding="utf-8") as f:
        json.dump(P[cid], f, ensure_ascii=False, indent=1)
# self-verify: reopen each file exactly by id list (no directory listing/counting)
ok = 0
trig = {"changed_main": 0, "reserve_used": 0, "disputed": 0}
for cid in IDS:
    with open(os.path.join(OUT, cid + ".json"), encoding="utf-8") as f:
        d = json.load(f)
    assert d["case_id"] == cid and d["prediction_text"] and d["basis"] and 0 <= d["confidence"] <= 1
    assert set(d["trigger"].keys()) == {"changed_main", "reserve_used", "disputed", "reason"}
    for k in trig:
        trig[k] += 1 if d["trigger"][k] else 0
    ok += 1
print("written_and_verified:", ok)
print("trigger_counts:", trig)
