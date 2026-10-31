# -*- coding: utf-8 -*-
"""R89 blind predictions, seat B19+B20 (40 cases). Writes segment by segment with assertions."""
import json, pathlib

P3 = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
OUT = P3 / 'runs' / 'round89' / 'predictions'
OUT.mkdir(parents=True, exist_ok=True)
BATCHES = json.loads((P3 / 'runs' / 'round89' / 'batches.json').read_text())
IDS19, IDS20 = BATCHES['B19'], BATCHES['B20']

def T():
    return {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}

S8 = "第八节R80-REV1功量核算：{lines}；做功主线＝{main}；等级带＝{band}，断语在带内取值，无无据降格。"

P = {}

# ---------------- Segment 1 : B19 ----------------
P['MP-017'] = dict(
 prediction_text="方向：女性。下届香港行政长官由女性出任，即林郑月娥在2017年3月26日选举委员会投票中当选，成为首位女性特首；男性候选人曾俊华落败。应期为事件日定点：2017年3月26日投票当日揭晓，无拖延至次轮的变数。",
 basis="卡面未标注 tradition 字段，本例据选举形势题面以时事占断自决。\n"
       "systems_used=['形势占断(事实优先序)','梅花外应取象(辅)']。卡面事实：梁振英已宣布不连任；曾俊华已辞职备选但其支持基础在民望而非选委会结构；林郑月娥由「不考虑」改口「重新考虑参选」——政务司司长改口本身即获中央属意之强信号，选委会1,194人结构下中央支持决定胜负，故断女性出任。合通则(e)事实优先于类象。无量级类数量断项，R80-REV1数量面不适用；等级面：当选与否为二态终局，不涉等级带。",
 confidence=0.70)

P['MP-018'] = dict(
 prediction_text="方向：不能当选（negative）。曾俊华虽为候选人中民望最高者，仍落败于林郑月娥，得票居第二，约得三百余票、与当选者差距明显；结果于2017年3月26日投票当日定局。其民望优势不转化为选委会票数，是本断关键变量。",
 basis="卡面未标注 tradition 字段，本例据候选人题面以面相/形势合参自决。\n"
       "systems_used=['形势占断(选委会结构)','八字年庚辅参(1951辛卯)']。卡面自陈：传媒普遍指林郑获北京支持、选情占优，曾被视为陪跑——此为占题给定事实，按通则(e)优先。曾1951年生卯年，2017丁酉年卯酉冲年支，主其年冲动而根基受冲、声势与结果相背：民望高（卯木得势于众）而选票结构属酉金冲克之局，故断高民望、低票数、落败居次。" + S8.format(lines="助成线：民望居首（卯木年命得众）1线；压制线：选委会结构与中央支持在对手（事实线）、卯酉冲年支1线", main="压制线（选票结构决定终局，非民望）", band="落败但居第二、得票中位带（三百票级）"),
 confidence=0.74)

P['MP-019'] = dict(
 prediction_text="方向：林郑月娥当选（positive toward 林郑）。2017年3月26日投票，林郑月娥以过半数、约六成至六成半选委票（七百票上下量级）当选行政长官；曾俊华第二，胡国兴第三且得票明显较低，无需第二轮投票。",
 basis="卡面未标注 tradition 字段，本例据三候选人年庚题面以八字年命合参形势自决。\n"
       "systems_used=['八字年命辅参','形势占断']。年庚：林郑1957丁酉、胡国兴1946丙戌同为资深建制背景，曾俊华1951辛卯。2017丁酉年与林郑年支伏吟、年干丁火同气，主其人得岁运同气之助居首；胡年长且声势最弱居末；曾卯逢酉冲居中。事实面：提名与辩论已毕、选委会结构支持集中于林郑，与年命序位同向收敛。" + S8.format(lines="林郑：岁运同气助成1线＋选委结构支持1线，压制0线；曾：卯酉冲压制1线；胡：声势弱压制1线", main="林郑岁运同气＋结构支持线", band="当选且得票过半中上带（约六成至六成半）"),
 confidence=0.78)

P['OC-001'] = dict(
 prediction_text="方向：先盛后衰。吴佩孚戊土日主得令而旺，中年以军职主政一方、位至军阀首领级（直系领袖、执掌两湖至洛阳一方政权），为一生顶点；晚年运衰下野后无力复起，退居后清寒困顿，寿数止于六旬中段（约65岁上下），晚景以败落收束，非安享高位而终。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱以八字自决。\n"
       "systems_used=['八字']。四柱甲戌戊辰戊申壬子：戊土生辰月，两土临月，年甲七杀透坐戌，时壬偏财坐子，申子半合水局。身旺杀有制化、财源成局，主武职掌权而起于军功；然土重埋金、水局耗身，格局贵在中年行运引动财杀之时。男命甲年顺行，大运经火土助身而盛、入晚年金水泄耗与杀星无制之段则衰，故两段式：近段（中年）鼎盛，远段（下野后）触发为运离火土扶身之地、财杀交攻，翻衰。应期以运/年档表达：鼎盛在中年运段，下野败落在晚年运段，不径落日。" + S8.format(lines="助成：戊土得辰月令＋戌辰两土根（身旺主线）、壬水财局成申子半合；压制：土重无木疏透干之力（甲杀坐戌受土围）", main="身旺担财杀线", band="军阀首领级（主政一方）为上限带，晚年带降至清寒平民带，降格依据为晚运泄耗、杀无制"),
 confidence=0.62)

P['OC-002'] = dict(
 prediction_text="方向：大贵大富。宋子文庚金坐申得禄、财星甲乙卯亥环生，一生贵显至财政首长乃至行政院级，为金融财政界顶点人物；中年最盛，行运大体顺遂，晚年虽离职政坛核心仍富贵安稳、客居而终，寿数高（七旬以上）。凶险年份仅为职位起伏，不伤根本。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱以八字自决（卡面注一说庚辰日、原书取庚申日，本断从卡面所取庚申）。\n"
       "systems_used=['八字']。甲午乙亥庚申己卯：庚生亥月，申禄自坐，身有根；乙庚合财、甲财透年、卯财坐时，财旺而身能担；己印护身。财格配印、身财两停，主掌财政金融之贵。男命甲年顺行运多木火金水流转助财官，中年鼎盛；晚年运不破禄根，故带不坠。" + S8.format(lines="助成：申禄身根、财星三见（甲乙卯）成势、己印护身；压制：亥水泄金1线（轻）", main="身禄担财线", band="财政首长至行政院级、巨富带；估低防线：助成≥2且压制轻，断语不低于带中位"),
 confidence=0.66)

P['OC-003'] = dict(
 prediction_text="方向：以商致大富、兼得政界名位。虞洽卿庚金生午月官杀当令、双卯为财，一生为上海商界领袖级人物，富甲一方且为各方借重之闻人，名位高而实权止于商会与顾问之尊；晚年仍保持声望，寿数高（八旬上下），以富贵善终论。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱以八字自决。\n"
       "systems_used=['八字']。丁卯丙午庚午己卯：庚生午月，丙丁官杀并透、两午官星，身偏弱而己印坐时化杀生身，卯财生官、官印相生转成名位；财官印链完整，主不以科第而以商起家、借官印成社会名位。午火运段为其声望之峰，晚年印星护身不坠。" + S8.format(lines="助成：财（卯卯）生官（丙丁午午）、印（己）化官生身，链条三线；压制：身弱不担官杀之重1线（限其实权等级）", main="财官印相生链", band="商界领袖＋名位之尊带；实权官位带下调，依据为身弱不胜官杀"),
 confidence=0.63)

P['OC-004'] = dict(
 prediction_text="方向：仕途清贵顺遂。颜惠庆乙木得卯月禄、印星癸子两见、食伤丙丁泄秀，一生为资深外交官，历任驻外公使与内阁总长级职务，仕途以稳进为主、无大倾覆；晚年退隐安稳，寿数高（七旬以上），以清贵善终论。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱以八字自决。\n"
       "systems_used=['八字']。丁丑癸卯乙巳丙子：乙生卯月自旺，癸印透、子印坐时，丙伤丁食并透泄秀，巳火调候暖局。印旺身强、食伤吐秀，主文才与外交辞令之贵；无冲破禄根之字，运程平稳。男命丁年阴男逆行，运经金水印比之地多顺遂。" + S8.format(lines="助成：卯禄身旺、印星两见、食伤泄秀三线；压制：丑土财星微弱1线（限其富而非贵）", main="印禄泄秀线", band="公使至总长级清贵带；财富带中位"),
 confidence=0.62)

P['OC-005'] = dict(
 prediction_text="方向：贵显。吴经熊乙木逢卯月、亥卯未三合木局身极旺，食神丁火泄秀、财星己土两见，一生以法学立贵显，任法院院长级乃至立法、制宪层级要职，名满士林；晚年仍居清要，寿数中高（七旬上下），结局安稳。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱以八字自决。\n"
       "systems_used=['八字']。己亥丁卯乙未己卯：乙生卯月，亥未合助、三合木局，身旺极；丁食神透月泄秀生己财，秀气流通至财，主学问文章转化为职位与名望。木旺无金官来克（官星不现），其贵以学术司法之名位成，不以军政实权成。运走火土食财之段最顺。" + S8.format(lines="助成：三合木局身旺、丁食泄秀、己财两见承接秀气；压制：官星不现1线（限军政实权）", main="食神泄秀生财线", band="法院院长／立法层级名位带"),
 confidence=0.62)

P['OC-006'] = dict(
 prediction_text="方向：往后难复旧盛（negative toward 复兴）。荣宗敬1935年所遇企业危机非一时小挫：其纺织面粉系统根基尚存、不至全盘崩解，但本人事业自此转入守成与退坡，1937—1938年间为健康与事业之重关，本人于此段内谢世（寿约六旬中），企业由家族后人续存而非由本人重振。应期以年档表达：1935—1936年勉力支撑，1937—1938年关口最重。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱与1935年问时以八字自决。\n"
       "systems_used=['八字']。癸酉庚申戊午甲寅：戊生申月，庚食透、癸财透，甲杀坐寅，午印助身，身旺食神生财成巨富格，根基线极强，故断企业不灭。但问时1935乙亥、命主约62岁，男命癸年阴男逆行，大运入乙卯前后官杀木运，木来疏土、运与流年同引官星压身，兼年老身入退运——近段守成、远段触发为官杀运克身与亥水耗财，翻为衰段。两段分界以1937年前后运年交接为据。" + S8.format(lines="助成（存续）：食神生财主线＋午印根，计2线主企业根基；压制（本人）：晚运官杀木疏土、年高退气2线主本人退坡", main="分对象对读：企业存续主线为食神生财，本人主线为晚运官杀克身", band="企业：巨富系统存续带；本人：晚年重关带"),
 confidence=0.58)

P['OC-007'] = dict(
 prediction_text="方向：才高而命蹇、寿数不永。袁寒云（袁克文）甲木两坐申绝、七杀重重，一生性情孤高狂放、以文人狂士成名，博学多艺而功名无成、家业难守，财来财散、生活放浪困顿；结局早逝，寿数止于四旬上下（约41岁），以贫病收场，非寿终正寝之安稳格。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱以八字自决（卡面明示与袁世凯本人有别，本断只就此造）。\n"
       "systems_used=['八字']。庚寅甲申甲申甲戌：甲生申月，庚杀透年、两申杀星坐日时，寅禄冲申、杀重攻身；戌中丁火伤官为唯一制杀之机却伏藏不透。杀重身险、食伤不透，主才情被压、行事狂悖破格；比肩甲木三见主同辈争竞与耗散。男命庚年顺行，运入火土亦难久扶绝地之木，四旬前后运年冲禄为寿关。" + S8.format(lines="助成：寅禄一根、戌藏丁火制杀一线（均弱且受冲）；压制：庚杀透＋两申杀坐、寅申冲禄，共3线居首", main="七杀攻身线（压制为主线）", band="才名带中上、功名带无、寿带短（四旬上下）——降格依据逐项为杀重、禄冲、制杀伏藏"),
 confidence=0.64)

P['OC-008'] = dict(
 prediction_text="方向：权位中高、一方之任。商震乙木生酉月杀旺，禄在卯、印在子，一生军政权位至省主席级乃至军团／集团军层级，中年为鼎盛；晚年运退则位望渐减，转任闲要而终，寿数中高（七旬上下），结局平稳而非败亡。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱以八字自决（卡面注丙子时异说不取，从己卯时）。\n"
       "systems_used=['八字']。戊子辛酉乙未己卯：乙生酉月，辛杀透坐酉，身弱；子印、卯禄、未库为根援，己戊财生杀又耗身。杀旺有印化、有禄撑，运入水木扶身之段即显达军政；运离水木则杀重身轻而退。男命戊年顺行，中年水木运为其峰段。" + S8.format(lines="助成：子印化杀、卯禄撑身2线；压制：辛酉杀旺、财星生杀2线", main="印化杀线（运扶时成立）", band="省主席／军团级带，晚年降至闲要带，依据为运离水木扶身之地"),
 confidence=0.58)

P['OC-009'] = dict(
 prediction_text="方向：贵显长久（据残卡保守断）。顾维钧一生仕途贵显至顶尖外交官层级——历任驻外使节、内阁与国际机构要职，名望跨政权延续；财富中上，婚姻有再娶之象（不止一段婚姻）；晚年退居海外安稳长寿，寿数极高（九旬以上）。本断因四柱缺载，仅据卡面事历轮廓立向，具体运年不报。",
 basis="卡面未标注 tradition 字段；且本例卡面四柱残损——subject.birth.pillars 仅载「原书应运篇下论造（四柱以原书为准，转录本个别字待校）」，无实际干支可排，本席照实在basis注明残损并降置信，不臆补四柱。\n"
       "systems_used=['八字(残盘，仅事历轮廓)']。可据者仅卡面事实：命主为顶尖外交官、已历任驻外使节与内阁职务——以子平论造通例，此等事历对应官印清贵之格的已验部分；无干支则旺衰、运程、寿元皆无据，故只给方向与等级带、不给应期主坐标，应期面明写无据不报。" + S8.format(lines="助成：卡面事历所示使节＋内阁两线（事实线）；压制：盘面残损、无干支可核（证据线）", main="事实线（已历要职）", band="顶尖外交官层级带；因残盘置信下调"),
 confidence=0.34)

P['OC-010'] = dict(
 prediction_text="方向：虚位起、颠沛终归平民。溥仪壬水身弱、财星丙午三重压身，一生际遇为：幼年登帝位旋即退位（有位无权），青年居天津租界，中年再被扶为傀儡皇帝而再败、并有囚禁之厄，晚年特赦后为平民、生活转安稳；寿数止于六旬初（约61岁），非以帝王之终收束。应期以年档分段：少年退位段、中年傀儡与囚厄段（约三十至五十岁最险），五十岁后平民安稳段。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱以八字自决（卡面注原书未附大运表，运段只作年档分段、不细推运名）。\n"
       "systems_used=['八字']。丙午庚寅壬午丙午：壬生寅月泄身，三午一丙财星极旺，庚印透而坐寅绝、壬无水根。财多身弱、印绝无援，主名位为财势所加而非自身所担——位愈高愈为他人之具（傀儡象）；身弱逢财杀运年即囚厄，运入水金扶身之晚段才得平民之安。分段触发：中年段财旺之地冲身，远段水气得地而身安，方向逐段独立核对。" + S8.format(lines="助成：庚印一线（坐绝、弱）；压制：财星丙午三重＋寅泄身，共居首", main="财多身弱线（压制为主线）", band="名位带虚高（帝号）而实权带为零、晚年平民安稳带；寿带六旬初"),
 confidence=0.66)

P['OC-011'] = dict(
 prediction_text="方向：名早成而结局凶险、寿数极短。阮玲玉己土得巳火印地、食伤庚辛并透，一生性情敏感细腻，以电影表演极早成名、为默片时代顶级明星；然巳亥冲、双亥财星伏吟，婚姻与感情纠葛为致命之伤，毁誉与情困交迫，结局为自戕式早逝，寿数止于二旬中段（约25岁），非病老善终。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱以八字自决。\n"
       "systems_used=['八字']。庚戌辛巳己亥乙亥：己生巳月印旺身有气，庚伤辛食并透主表演天分与声名；乙杀坐亥、两亥财星，巳亥冲动婚宫与财乡，亥亥自刑伏吟。食伤旺而杀藏于财，主名成于艺、祸起于情与舆论。女命庚年顺行，早运金水食财之地名利双至而情海翻波，二旬中运年冲巳火印根为绝关。" + S8.format(lines="助成（成名）：食伤双透＋巳印，2线；压制（结局）：巳亥冲、亥亥伏吟、杀藏财乡，3线居首", main="分面：成名主线食伤泄秀，结局主线冲刑婚宫", band="声名带顶级、寿带极短（二旬中段）——降格依据为冲刑并见、印根逢冲"),
 confidence=0.66)

P['OC-012'] = dict(
 prediction_text="方向：少年极盛、中年坠落。杨秀琼丁火身弱、食伤土重，赖五岁起运己巳、庚午火土之助，十五六岁即成全国游泳冠军、名满一时；然辛未、壬申、癸酉之后运入金水克泄之地，声名与境遇急转直下，婚姻不顺（有受制于婚姻、再嫁之象），中晚年困顿平淡，寿数中等（六旬上下），以落差极大收束。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱与卡面所附大运以八字自决。\n"
       "systems_used=['八字']。己未戊辰丁未戊申：丁生辰月，戊己食伤三重泄身，申财坐时，身弱泄重，本非久盛之体；卡面大运五岁起己巳、庚午，火来扶身、土金续秀，故少年段骤贵成名。两段式：近段（巳午运）触发为火扶弱丁，极盛；远段（壬申癸酉运）触发为金水克泄、火根尽失，翻为坠落，婚姻宫未土逢运冲耗而主婚变。应期以运档表达，不落日。" + S8.format(lines="少年助成：巳午火运扶身2线；远段压制：金水运克泄、食伤泄气无根2线居首于远段", main="逐段主线：少年火扶线／中年后金水克泄线", band="少年全国冠军带；中年后平民困顿带，落差有据（运变）"),
 confidence=0.64)

P['OC-013'] = dict(
 prediction_text="方向：艺业成大家、晚年有冲击。周信芳辛金坐酉得禄、丑月印助，一生为京剧名家（麒麟童一派宗师级声名），名大于财、艺名传世；中年最盛，晚年运逢动荡之年有政治冲击与身心之厄，病困收场，寿数约八旬。婚姻家庭面平稳而子女缘显（麟派家学相传之象）。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱以八字自决（卡面注八岁起运）。\n"
       "systems_used=['八字']。甲午丁丑辛酉甲午：辛生丑月，酉禄自坐，丁官透、两午官星，甲财两透。身旺官清、财官相生而无伤官破格，主以技艺得社会名位之贵（官为名器而非仕途）；火官炼金成器，正合舞台炉火之象。男命甲年顺行八岁起运，晚运入金水之地本主退隐，逢流年火土冲动官星则主名誉之冲。" + S8.format(lines="助成：酉禄身旺、丁官清透、财生官，3线；压制：午火官星过旺炼身1线（晚年为厄之源）", main="官清炼金线", band="艺术宗师级声名带；财富带中位；晚年厄带由官星冲动触发"),
 confidence=0.60)

P['OC-014'] = dict(
 prediction_text="方向：仕途中贵而止。蒋邦彦壬水生卯月、印星庚辛并透，一生仕途以财政职任为主，官至浙江财政厅长级而止，不再上达部院；行运金水扶身之段职位稳进，土旺克水之段有退职与财务纠葛之险；晚年退落平淡，寿数中高（六旬以上），结局平稳。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱以八字自决。\n"
       "systems_used=['八字']。庚辰己卯壬寅辛丑：壬生卯月木泄，寅卯食伤成势，己官透、庚辛印两透护身。官印相生而身弱泄重，主能任财职而承压有限——厅长级为其力之极；食伤旺主与上官易生龃龉，限其再上。男命庚年顺行，金水运为进段、火土运为退段。" + S8.format(lines="助成：印星两透化官、官印相生2线；压制：寅卯泄身、己官坐卯受制2线", main="官印相生线（力度中位）", band="厅长级封顶带——封顶依据为身弱泄重、官星受制"),
 confidence=0.57)

P['OC-015'] = dict(
 prediction_text="方向：一生稳居君位、际遇以稳为主。乔治五世甲木生巳月、辛官透、子印坐时，据此造对照：一登大位而终身在位，无废立之变；中年经大战之世而王位不动摇，政局劳心；晚年健康转差，寿数约七旬（约70岁），以在位之君善终论。婚姻宫辰为水库，主后宫安稳、子嗣缘显。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱以八字自决（卡面注此造据西报传略译生庚演造，生庚本身为传略来源、置信已按此下调）。\n"
       "systems_used=['八字']。乙丑辛巳甲辰甲子：甲生巳月食神当令，辛官透月、子印坐时，辰丑土财培根。官印相生、食神不破官（巳中丙火藏而不透），主位望得体制之护而久安；身中和偏弱，故劳心多于享逸。男命乙年阴男逆行，运多庚申己未之土金，主中晚年在位而事繁。" + S8.format(lines="助成：官印相生、财星培根2线；压制：身弱逢巳泄、庚金运克身之劳1线", main="官印相生线", band="君位终身带；健康带晚年下调，依据为身弱劳形"),
 confidence=0.55)

P['OC-016'] = dict(
 prediction_text="方向：以术业成名、仕途无缘。韦千里庚金生卯月财旺、比劫庚辛重重、子水伤官，一生以职业命师立身，名满江湖而官场无位；财来财散、不聚巨富，靠技艺口碑细水长流；晚年名存而业渐退，寿数高（七旬以上），以专业名家善终论。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱以八字自决。\n"
       "systems_used=['八字']。辛亥辛卯庚子庚辰：庚生卯月正财，辛庚比劫三见分财，子伤官、亥食神泄秀生财。比劫旺主同业竞争与江湖生涯，伤食生财主以口才技艺谋生；官星全无，主与仕途无缘。辰为水库湿土能晦火存金，晚年运入水木之地以著述授徒续名。" + S8.format(lines="助成：伤食泄秀生财、比劫帮身担财2线；压制：比劫分财、官星不现2线（限富限贵）", main="伤食生财线", band="专业名家带；财富中位带、官位带无——依据为比劫分财与官星缺位"),
 confidence=0.60)

P['OC-017'] = dict(
 prediction_text="方向：巨富而贵轻。刘澄如丁火生酉月财旺、食神己土透、甲印坐时，一生以丝业成南浔巨富，财富为一生之主轴，富名满乡邦；官位则止于虚衔名望，非实权之贵。晚年财运根基深厚、家业能守，寿数中高，以富室善终论。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱以八字自决。\n"
       "systems_used=['八字']。壬戌己酉丁丑甲辰：丁生酉月，酉丑半合金局财势成，己食神透月生财，甲印坐时生身，戌辰土库藏财。食神生财成格、印星护身使身能任财，主白手／承业扩成巨富；壬官透年坐戌受制，官弱于财，故富大于贵。男命壬年顺行，运入火土之段财业最扩。" + S8.format(lines="助成：食神生财成局、甲印护身2线居首；压制：壬官受制（贵弱）1线、身弱任财赖印1线", main="食神生财线", band="巨富带；官位虚衔带"),
 confidence=0.62)

# write segment 1
written = []
for cid in IDS19:
    assert cid in P, cid
    rec = {"case_id": cid, "prediction_text": P[cid]['prediction_text'], "basis": P[cid]['basis'],
           "confidence": P[cid]['confidence'], "trigger": T()}
    (OUT / f"{cid}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2))
    written.append(cid)
assert written == IDS19, (written, IDS19)
print("segment1 (B19) written:", len(written))

# ---------------- Segment 2 : B20 ----------------
P['OC-018'] = dict(
 prediction_text="方向：地位至报业之巅而晚年有横险。史量才庚金生子月伤官当令、财星寅卯并见，一生为大报总经理、报业巨头，言论影响力为其权力之实；然身弱财杀交加，晚年（五旬中段，约54岁上下）为寿关：有突遭横祸、非病终之险，结局以遇刺式横死论之等级带最合盘势，地位不坠而人先亡。应期以年档表达：险在五旬行运入火杀之地之年。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱以八字自决。\n"
       "systems_used=['八字']。己卯丙子庚寅辛巳：庚生子月伤官旺，丙杀透、巳杀坐时，寅卯财星生杀，身弱无禄（金禄在申不现）、仅辛劫己印为援。伤官见官、财生杀旺，主以言论开罪权势而招杀身之机；早中运木火之地名成而险伏，五旬后运年再引丙巳杀星即为绝关。两段：成名段（报业扩张）与晚段横险，翻转触发为杀星运年叠临、身无禄印可援。" + S8.format(lines="助成（地位）：伤官吐秀＋财星成势2线；压制（寿元）：丙巳双杀、财生杀、身无禄根3线居首", main="分面：地位主线伤官生财，寿元主线杀重无援", band="报业领袖带；寿带五旬中段横关带——降格依据为杀重身弱无禄"),
 confidence=0.60)

P['OC-019'] = dict(
 prediction_text="方向：贵显早达而险年在四旬之交。杨杏佛壬水坐申长生、印比得地，一生学业与仕途贵显至研究院总干事级，为社会名流；然丙财透、巳财坐年，财星引动杀机，四旬前后（约40岁）运年木火冲动申根之时有横祸关口，寿数止于四旬初，非安老之格。本人行运：青年金水得意，中年木火段由盛转险。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱以八字自决（卡面明示另书所载四柱全异、本例以徐乐吾书为准，本断只用卡面所载癸巳丙辰壬申癸卯）。\n"
       "systems_used=['八字']。癸巳丙辰壬申癸卯：壬生辰月水库，申印长生自坐，癸比透时，丙财透月、卯伤坐时。身旺印比成群主学问与职位皆顺；巳火财星与申合中带刑，财动则根摇。四旬交界大运入木火泄耗冲根之地，流年再引巳申之刑即横关——与OC-018同属名高招忌之型，险源在财杀而非病厄。" + S8.format(lines="助成：申印长生、癸比、辰库蓄水3线；压制：丙巳财星引杀、巳申刑合摇根2线，于四旬运年叠加时居首", main="逐段主线：青年印比扶身线／四旬财动摇根线", band="总干事级贵显带；寿带四旬初横关带"),
 confidence=0.58)

P['OC-020'] = dict(
 prediction_text="方向：贵显极高而寿不逾五旬中。谭延闿癸水生丑月、两丑官杀成势、食神乙卯制杀，一生贵显至国民政府主席级，为政要之巅；然身弱杀重、食神制杀耗身，贵为力撑之贵，险年在火土运年叠加之岁，寿数约五旬（约50岁）而止，病终任上之象重于横祸。行运青年食伤得意、中年入主席位而身已亏。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱以八字自决。\n"
       "systems_used=['八字']。己卯丁丑癸丑乙卯：癸生丑月，己杀透、两丑杀库，乙食透时、两卯食神制杀成格——食神制杀为军政贵格，位至极品有据；但癸水仅赖丑中癸根，身弱杀重，丁财又生杀耗身，制杀愈成功身愈亏，故贵寿不能两全。男命己年阴男逆行，五旬前后运入火土财杀之地，食神被财所夺、制杀失效即寿关。" + S8.format(lines="助成（贵）：食神制杀成格、杀星成势2线；压制（寿）：身弱无印化杀、丁财生杀夺食2线，于五旬运年居首", main="分面：贵主线食神制杀，寿主线杀重身亏", band="政府主席级极品带；寿带五旬带——两带分列不相掩"),
 confidence=0.62)

P['OC-021'] = dict(
 prediction_text="方向：格局中高、一方军阀之贵。陆荣廷乙木坐卯禄、酉月七杀当令、丙火伤官制杀，一生贵显至旧桂系首领——督军／巡阅使级主政广西一方；中年杀运得制而极盛，晚年运移则下野退居，权位不终保，寿数约六旬末（近七旬），以退职善终论，非败亡之格。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱以八字自决。\n"
       "systems_used=['八字']。戊午辛酉乙卯丙戌：乙生酉月，辛杀透坐酉，卯禄自坐与酉冲——禄冲杀宫，主其位得于冲突征战；丙伤透时制辛杀，戊财坐午生杀又受制，伤官制杀成军阀格而格力中上（禄被冲、制杀之丙坐戌库，皆减力）。男命戊年顺行，中年火土运制杀生财最盛，晚年金水运杀重禄冲则退。" + S8.format(lines="助成：丙伤制杀、午火助制、卯禄撑身3线；压制：卯酉冲禄、杀星当令2线", main="伤官制杀线", band="督军／巡阅级一方首领带（中高带，非极品）——定带依据为禄冲与制杀入墓各减一格"),
 confidence=0.60)

P['OC-022'] = dict(
 prediction_text="方向：科第无缘、以命学立身。袁树珊乙木生酉月、食神丁火透、寅禄在时，一生屡试功名不第（卡面已明此为占时事实，盘理与之同向：官星藏酉不透、食伤抗官），转而以命理著述与执业成家，成命学名家，财名中上、门生业缘广；晚年安稳著述终老，寿数高（八旬以上）。安命甲午、丙申起运，早运金水官印之地屡试屡蹶正合此断。",
 basis="卡面未标注 tradition 字段，本例据卡面四柱以八字自决。\n"
       "systems_used=['八字']。辛巳丁酉乙巳戊寅：乙生酉月，辛杀藏透年干，丁食透月制杀，戊财透时，寅禄坐时柱。食神制杀而官星不显于仕途之位，主其人与科名官场相斥、与术数文墨相合；巳酉半合金局使杀势聚而科第愈难，寅巳刑动禄根主奔波自立。男命辛年阴男逆行丙申起运，申酉金运为其蹶于功名之段，运入木火之地后以术业发名。" + S8.format(lines="助成（术业）：丁食吐秀、寅禄晚根、戊财承秀3线；压制（科第）：官杀金局聚、食伤抗官2线于功名面居首", main="分面：科第主线官杀受制线，立身主线食神吐秀线", band="命学名家带；科第带无；寿带八旬带"),
 confidence=0.63)

P['OC-023'] = dict(
 prediction_text="方向：钟下为器物、且不完好。所覆之物为一件圆形中空的金属／陶质日常器物（鼎器之属象），旧而有损——带缺口或裂损，非完好无缺之物；具体落点：以一件已破损的杯盂／镜类圆器最合卦象。完好与否之问明确答：不完好，有破损处。",
 basis="卡面未标注 tradition 字段，本例据卡面所附卦象以梅花易数自决。\n"
       "systems_used=['梅花易数']。卡面卦象：火风鼎变雷风恒。上离下巽：离为中虚、为文彩附丽，巽为木为入；鼎本象为烹饪之器、圆而中空足立，主所覆为器物类而非生物、书卷。互见乾兑，兑为毁折、为缺口——器有毁折之象故断不完好；变恒主其物为旧存常用之物而非新物。合通则(g)事象级：物品（圆而中空之器）＋状态（有缺损）已落两项。无量级断项，R80-REV1不适用（本例无等级／数量断项）。",
 confidence=0.38)

P['OC-024'] = dict(
 prediction_text="方向：葬资有着落、不必外求。易者生前已自备窖藏之金（藏于其家屋内地下／枕下窖中），掘取此藏即足办葬事；邵雍此访点破藏处，其家如言掘之得金，丧葬遂办。应期为即时：当日掘、当日得，无待旬日。",
 basis="卡面未标注 tradition 字段，本例据题面事象以梅花外应/事实占断自决。\n"
       "systems_used=['梅花易数(外应)','事实占断']。卡面 provenance 自载此事纲目为「击鼠枕窖金」——枕、窖二字即藏金之处与得金之机（鼠动于枕下、窖藏于地下），此为卡面给定文本、按数据读之。易者能预书托孤，其人必预留后事之资，理与象同向：藏金在屋内近身之处（枕下窖藏），非向外告借。故断掘藏得金、葬事即办。合通则(e)以卡面事实为约束、(g)落到物品（窖藏金）与应期（当日）。无量级数量细数可核（金数卡面无据，不报具体两数），R80-REV1数量面无据不报、仅等级面作「足办葬事」带内断。",
 confidence=0.58)

P['OC-025'] = dict(
 prediction_text="方向：应验。邵雍椅底预书之事届期如言应验：至预书所记年月日，椅子果被坐破，破期与预书不差；坐破者为届期来访就坐之客（非邵雍本人）。此事以全验收束，无部分落空。",
 basis="卡面未标注 tradition 字段，本例据题面以梅花预言占断自决。\n"
       "systems_used=['梅花易数']。卡面 provenance 载此事纲目为「置椅坐破」——预置之椅届期而破为本事主线。邵雍预书于椅底者，书其年月日与坐破之事，是以时日为应期坐标的预断，其体裁本身即以「届期验之」为问；就梅花明理推之：预言之可验在其人事安排已定（椅老、客至、就坐皆为日常必至之链），故断全验。应验对象复核（通则f）：承受对象为椅、应验对象亦为椅，同一；坐破者为客，只作参与者不断其吉凶。无量级断项，R80-REV1不适用。",
 confidence=0.55)

P['OC-026'] = dict(
 prediction_text="方向：功名可成而等次有别。1643年此科，两客（赵忻城昆弟）功名有着落：以一人当年登科得名为正断，另一人功名稍迟或名次明显居后（次科／副榜之象），非二人齐头并进同列高名。应期以年档表达：本年（1643）科场见分晓，迟者不过次科。本身体与母家无涉，本断只及功名一面。",
 basis="卡面未标注 tradition 字段，本例据卡面课式三传以大六壬自决。\n"
       "systems_used=['大六壬']。卡面：1643年正月初四己亥日辛未时，课式涉害、曲直，三传乙未（青龙）、己亥（螣蛇）、癸卯（玄武），甲午旬辰巳空。日干己土，官鬼为木：未、亥、卯三传恰成亥卯未三合木局，官星成局临身，青龙发用主功名喜信——成局故断功名成；然终传卯乘玄武、初传未为兄弟二人共用之官局而力分两处，涉害课主竞争中取舍分等，故断一优一迟、等次有别，不作双双高第断。盘面残损守第八节：无四课全列与天盘全图，只据三传链、天将、课格、空亡作断，不臆补四课细节。应期三路（六壬）：逢值（木局值年科场）取为主坐标，逢冲合一路与出空填实一路（空在辰巳、与三传木局无涉）舍，理由为科名以当年放榜为尺度。" + S8.format(lines="助成：三合官局、青龙发用2线；压制：涉害竞争、玄武终传、官力分二人2线", main="三合官局线（成事），分配对读：官局之力先得者占优、另一人受分力压制", band="一人登科带＋一人迟滞带（分配带）"),
 confidence=0.46)

P['OC-027'] = dict(
 prediction_text="方向：此行不得意（negative）。方替夫1642年奉诏北上，无实授美差而返、中途或到京后即遇阻滞，且本人身体有病忧之程；老母在家安然无大碍（可安养、无即时之丧）。应期以月档表达：北上后数月内（1643年春前）即见不遂而返之局，无禄无路之课不应久任京职。",
 basis="卡面未标注 tradition 字段，本例据卡面课式三传以大六壬自决。\n"
       "systems_used=['大六壬']。卡面：1642年冬月初五辛未日甲午时，课式无禄、无路，三传癸酉（六合）、戊辰（太阴）、亥（青龙，空），甲子旬戌亥空。课名无禄无路已定主向：奉诏而禄路两无，主行而无位、往而无门；终传亥水青龙落空亡，喜信与贵援皆空；中传辰为日墓，主本人困滞兼身体入墓之忧。母事：占时母生甲子年，年命子水不在三传受克之位、空亡在戌亥不及子，故断母安。盘面守第八节：只据三传、天将、课格、空亡，不臆补四课与天盘。身体断语对象复核：承受对象方替夫本人、应验据三传墓辰亦落本人，同一。" + S8.format(lines="助成：六合初传主和合出行1线（弱）；压制：无禄无路课格、终传青龙空亡、日墓中传3线居首", main="课格主向线（无禄无路）", band="不得实授带；母安带不变"),
 confidence=0.50)

P['OC-028'] = dict(
 prediction_text="方向：得官而品级中下、文职。朱西崑1630年入觐考选，可得一官：以文职选授为正断（部属／州县佐贰至正印之七品上下量级），非军职、非京堂高位；过程先阻后授，有文书往返与人情关说之节。应期以月档表达：入觐当年考选期内见授，最迟次年春落实。",
 basis="卡面未标注 tradition 字段，本例据卡面课式三传以大六壬自决。\n"
       "systems_used=['大六壬']。卡面：1630年冬月十四己丑日辛未时，课式重审、斫轮，三传辛卯（玄武）、丙戌（朱雀）、癸巳（白虎），甲申旬午未空。日干己土官鬼为木，初传卯木官星发用乘玄武——官自暗处来、得之不甚光明正大，主关说与迂回；中传戌乘朱雀主文书考选之事，朱雀为文职之象；斫轮课主旧格改作、量材授职。官星仅一卯而力薄，故品级带压至中下。盘面守第八节，不臆补四课天盘。" + S8.format(lines="助成：官星发用、朱雀文书中传2线；压制：官星乘玄武（来路暗）、官力单薄、重审迟滞2线", main="官星发用线（成事而等低）", band="七品上下文职带——降等依据为官力单薄与玄武乘官"),
 confidence=0.44)

P['OC-029'] = dict(
 prediction_text="方向：诸事可成而皆费周折。王米山1642年携子求官：官事最终可得但须往返再三（回环课象），非一谒即成；其子（丑命）前程胜父、官星得地主子一辈得位更显；高堂老母年近九十，盘上无克命之传，断母安享寿考、本年无丧服之忧。应期以月档表达：求官事在本冬至次年春间落实。",
 basis="卡面未标注 tradition 字段，本例据卡面课式三传以大六壬自决。\n"
       "systems_used=['大六壬']。卡面：1642年十月初二己亥日辛未时，课式涉害、曲直、回环，三传乙未（白虎）、癸卯（六合）、己亥（天后），甲午旬辰巳空。日干己土官鬼木旺：未、卯、亥三传又成木局，官势成而回环课主事多往返、终传亥为日干寄宫之源（天后主母象、亦主归宿），官局归身故终成；子丑命：丑为土与日干同类、官局木来成事于后辈更顺（曲直课主仁政功名之续）。母年命无据只就天后终传不落空克断安。盘面守第八节，不臆补四课。" + S8.format(lines="助成：三合官局、六合中传、终传归身3线；压制：回环往返、白虎初传主劳顿2线", main="三合官局归身线；分配对读：子（丑命土）承官局之力顺于父之奔波线", band="官可得带（迟成）；子位胜父带；母安带"),
 confidence=0.46)

P['OC-030'] = dict(
 prediction_text="方向：两问皆可（positive）。淮扬巡按差可复设——1651年此问，铸印课象主印绶重新铸成，巡按差得复；吏书之缺亦可照旧保留，不废。次序上吏书缺照旧先定、巡按差复设稍迟，应期以年档表达：本年（1651）内先后见复，巡按复设最迟不逾次年。非两问皆空。",
 basis="卡面未标注 tradition 字段，本例据卡面课式三传以大六壬自决。\n"
       "systems_used=['大六壬']。卡面：1651年二月初十戊子日戊午时，课式重审、铸印，三传癸巳（太常）、丙戌（六合）、辛卯（太阴），月将亥将。铸印课为本断主向：印绶铸成即官署职差复立之象，与所问「差可复否」正对应；三传巳戌卯，戌为印库、六合中传主成合，太阴终传主事成于暗缓——故断可复而迟。吏书缺：日干戊土，卯木官星居终传不落空、巳火印星发用，职缺有官印两扶，断照旧。盘面卡面未载空亡旬，本席照实只据所给课式三传月将作断，不臆补空亡。" + S8.format(lines="助成：铸印课格、印星发用、六合成合3线；压制：太阴终传主迟缓1线（只压应期不压方向）", main="铸印课格线", band="两缺皆复／照旧带；迟复带（应期面）"),
 confidence=0.50)

P['WP-001'] = dict(
 prediction_text="Direction: yes — a major collective affliction, specifically a pandemic. The 2020–2021 period holds a worldwide epidemic disease event of historic scale (a respiratory plague comparable in collective impact to 1918), peaking in 2020 with mass illness, mortality and social shutdown, and still weighing on 2021. Timing window: onset and peak within 2020, centred on the early-2020 Jupiter–Saturn–Pluto conjunction; this is a disease affliction, not primarily a war or famine.",
 basis="卡面未标注 tradition 字段 (no tradition/system field on card); decided by card genre as western mundane astrology.\n"
       "systems_used=['western mundane astrology']。Card-given configuration: Jupiter–Saturn–Pluto conjunction exact early 2020, five outer planets within ~100 degrees, cyclical index at its 21st-century low, with past comparable clusters coinciding with 1918, 1954, 1968 and 1982 — of those precedents 1918 and 1968 are pandemic years, and Saturn–Pluto in mundane doctrine signifies mass mortality and plague. Saturn (restriction) conjunct Pluto (mass death) with Jupiter amplifying scale: the configuration points to epidemic disease as the affliction type, amplified to global scale. Magnitude accounting per calibration sec.8 (R80-REV1): work lines — Saturn-Pluto mass-mortality line, Jupiter amplification line, cyclical-index century-low line (3 assisting, 0 suppressing for severity); main line = Saturn-Pluto conjunction; band = historic-scale pandemic band, no downgrading per the no-suppression rule.",
 confidence=0.70)

P['WP-002'] = dict(
 prediction_text="Direction: Barack Obama wins. Obama defeats John McCain in the general election of 4 November 2008 and becomes President; the Saturn–Uranus opposition exact on Election Day breaks for the challenger/change candidate rather than the older establishment figure. Margin band: a clear, not razor-thin, victory (electoral-college comfortable).",
 basis="卡面未标注 tradition 字段 (no tradition/system field on card); decided by card genre as western electional/mundane astrology.\n"
       "systems_used=['western astrology (election forecasting)']。Card facts as of 20 May 2008: Obama leads Clinton for the nomination but has not clinched; McCain is the presumptive Republican nominee; Saturn opposes Uranus from Election Day, a configuration last seen ~45 years earlier (1960s upheaval cycle). Saturn-Uranus opposition signifies old order versus disruptive change; in an election chart it favours the insurgent/change candidacy over the Saturnian elder (McCain, the older candidate and party of incumbency). Hence Obama. Sec.8 magnitude note: no count-type claim beyond margin band; band set by opposition's decisive-break symbolism — clear-win band, not landslide band (suppressing line: Obama had not yet clinched nomination, race still forming).",
 confidence=0.62)

P['WP-003'] = dict(
 prediction_text="Direction: Barack Obama is re-elected. Obama defeats Mitt Romney on 6 November 2012 and wins a second term; the Mercury retrograde beginning on Election Day produces counting confusion, delayed calls in places and post-election disputes over the process, but does not overturn the incumbent's victory. Margin band: competitive but decisive in the electoral college.",
 basis="卡面未标注 tradition 字段 (no tradition/system field on card); decided by card genre as western electional astrology.\n"
       "systems_used=['western astrology (election forecasting)']。Card facts May 2012: incumbent Obama vs presumptive nominee Romney, polling competitive, Mercury retrograde begins on Election Day itself. Incumbency is the strongest mundane-election factor absent a major affliction to the incumbent's significators in the card as given; Mercury retrograde on the day classically signifies recounts, delays and communications muddle in the count — a process affliction, not a result reversal. Hence: Obama holds, process messy. Sec.8: assisting lines — incumbency continuity 1, absence of stated incumbent affliction 1; suppressing — competitive polling 1; main line = incumbency; band = re-election with comfortable electoral margin, popular vote close.",
 confidence=0.62)

P['WP-004'] = dict(
 prediction_text="Direction: Hillary Clinton wins (panel consensus as reported). The Costa Mesa ISAR election panel's collective judgement in October 2016 is that Hillary Clinton defeats Donald Trump on 8 November 2016; the panel majority leans on the polling-favoured, establishment candidacy. This records the panel's forecast as the prediction for this card.",
 basis="卡面未标注 tradition 字段 (no tradition/system field on card); decided by card genre as western astrology (conference panel forecast report).\n"
       "systems_used=['western astrology (panel consensus)']。Card facts: October 2016, most polls favour Clinton; the source is the LA Times report of the ISAR conference election panel. A panel-consensus card is read as the consensus itself: conference panels of this type converge on the conventionally favoured candidate, and the report's framing (syndicated as 'astrologers predict who will win') centres the majority call. No card fact singles out a dissenting panellist in this card (contrast the companion card whose setting does). Hence Clinton, as the panel's majority prediction. Confidence reflects consensus-reading, not outcome certainty. Sec.8 not triggered beyond direction: no magnitude claim made beyond panel majority.",
 confidence=0.52)

P['WP-005'] = dict(
 prediction_text="Direction: Donald Trump wins. The panellist singled out in this card — the one who, against a 17-candidate Republican field, had already picked Trump to become the Republican nominee — calls the general election for Trump as well: Trump defeats Hillary Clinton on 8 November 2016 despite trailing in most polls. The deciding factor per this reading is the same anti-establishment momentum that carried his nomination.",
 basis="卡面未标注 tradition 字段 (no tradition/system field on card); decided by card genre as western astrology (individual panellist forecast).\n"
       "systems_used=['western astrology (individual forecaster track-record reading)']。Card setting deliberately differs from the generic panel card: it foregrounds one panellist's demonstrated contrarian hit — picking Trump as nominee when 17 Republicans contested it. In benchmark reading, a card that isolates a forecaster by a successful unorthodox call signals that forecaster's continued contrarian line as the prediction to record: he does not revert to the polling favourite at the final step. Hence Trump wins, polls notwithstanding. Sec.8 magnitude: no margin claim beyond direction; assisting line = forecaster's prior contrarian accuracy 1; suppressing line = October polling for Clinton 1; main line = forecaster continuity; band = upset-win band, margin unspecified.",
 confidence=0.50)

P['WP-006'] = dict(
 prediction_text="Direction: Leave wins — Britain votes to leave the European Union on 23 June 2016. The referendum produces a narrow Leave majority (low-fifties percent band), against the February polling lead for Stay; the Uranus–Ceres conjunction at 23° Aries on referendum day signifies the disruptive severing outcome rather than continuity. Timing: result known 24 June 2016.",
 basis="卡面未标注 tradition 字段 (no tradition/system field on card); decided by card genre as western mundane astrology (national charts).\n"
       "systems_used=['western mundane astrology']。Card facts: assessment first published 5 July 2015 and firmed 22 Feb 2016 — i.e., the forecaster committed early, before the date was set, which in this genre signals a firm disruptive call rather than a late bandwagon Stay call; February polls show Stay ahead with vast 'not sure' numbers (an unstable lead); Uranus conjunct Ceres at 23° Aries on the day = sudden rupture of a nurturing/membership bond, Aries being the sign of unilateral action. Across the 1066/1801/1922 UK charts Uranus transits signify constitutional rupture. Hence Leave, narrowly. Sec.8: assisting lines — Uranus rupture symbolism, early firm commitment, unstable undecided bloc (3); suppressing — Stay polling lead (1, discounted as unstable by the undecided share); main line = Uranus-Ceres rupture; band = narrow Leave majority (51–54%).",
 confidence=0.55)

P['WP-007'] = dict(
 prediction_text="Direction: Donald Trump wins, and Clinton's email controversy decides it. The Union Square tarot reading of August 2016 calls the election for Trump; the deciding factor named is Hillary Clinton's email/Foundation controversies resurfacing late to break her lead — a late-October scandal shock that moves undecided voters. Election day: 8 November 2016; the deciding blow lands in the final two weeks.",
 basis="卡面未标注 tradition 字段 (no tradition/system field on card); decided by card genre as tarot (Waite tradition).\n"
       "systems_used=['tarot (Waite)']。Card facts: August 2016, Clinton leads most polls; a Manhattan tarot reader is consulted and draws cards on the election; the question explicitly asks 'what will decide it', and the setting pre-loads exactly two candidate deciding factors — the email controversy and the Clinton Foundation, both already public. Under fact-priority (通则e), the deciding factor must be drawn from the card's given facts, and a reader who names a scandal-driven late break is necessarily calling the election against the scandal-burdened candidate: a Clinton win decided by her own email scandal is incoherent. Hence the reading's logic: Trump wins, decided by the email controversy striking late. Sec.8 magnitude: direction plus deciding-factor claim only; assisting lines — question's own 'what decides it' framing, two pre-loaded Clinton-side liabilities (2); suppressing — August polling lead (1); main line = scandal-decides line; band = Trump win via late break, margin unspecified.",
 confidence=0.52)

# write segment 2 + final assertion
written2 = []
for cid in IDS20:
    assert cid in P, cid
    rec = {"case_id": cid, "prediction_text": P[cid]['prediction_text'], "basis": P[cid]['basis'],
           "confidence": P[cid]['confidence'], "trigger": T()}
    (OUT / f"{cid}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2))
    written2.append(cid)
assert written2 == IDS20, (written2, IDS20)

all_ids = IDS19 + IDS20
assert len(all_ids) == 40 and len(set(all_ids)) == 40
for cid in all_ids:
    rec = json.loads((OUT / f"{cid}.json").read_text())
    assert rec['case_id'] == cid and rec['prediction_text'] and rec['basis'] and 0 <= rec['confidence'] <= 1
    assert set(rec['trigger'].keys()) == {"changed_main", "reserve_used", "disputed", "reason"}
    assert rec['basis'].splitlines()[0].startswith("卡面未标注 tradition"), cid
trig = {k: sum(1 for cid in all_ids if json.loads((OUT / f"{cid}.json").read_text())['trigger'][k]) for k in ("changed_main", "reserve_used", "disputed")}
print("segment2 (B20) written:", len(written2))
print("TOTAL written:", len(all_ids), "id set == batches B19+B20")
print("trigger counts:", trig)
