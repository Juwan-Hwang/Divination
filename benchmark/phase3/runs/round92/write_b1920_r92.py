# -*- coding: utf-8 -*-
"""Round92 B19+B20 blind predictions writer. Only writes prediction JSONs."""
import json, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round92/predictions"
os.makedirs(BASE, exist_ok=True)

DATA_B19 = []
DATA_B20 = []

def add(lst, cid, text, basis, conf):
    if "第八节" not in basis and "功量清单" in basis:
        basis = basis.replace("功量清单", "【第八节功量核（R80-REV1）】功量清单", 1)
    if "第八节" not in basis and "残损例清单" in basis:
        basis = basis.replace("残损例清单", "【第八节功量核（R80-REV1）】残损例清单", 1)
    lst.append({"case_id": cid, "prediction_text": text, "basis": basis,
                "confidence": conf,
                "trigger": {"changed_main": False, "reserve_used": False,
                            "disputed": False, "reason": ""}})

# ---------------- B19 ----------------
add(DATA_B19, "MP-017",
"方向：女性。断语：下届香港行政长官由女性出任，即当时已改口考虑参选的女性前政务司司长一脉胜出，男性候选人（已辞任财政司司长者）得选举委员会票数不及。应期：事件型，窗口为2017年3月26日投票日，主坐标即投票当日揭晓。置信：中。",
"卡面未载 tradition/system 字段（未标注）；systems_used：时事形势参断（无卦象/相格数据载于卡面）。卡面事实：梁振英已宣布不连任；曾俊华已辞任备选；林郑月娥改口将重新考虑参选、尚未正式宣布——女性候选人中唯此人具司长级班底与建制支持面。输入残损：卡面无任何占具数据（无卦、无相格、无出生数据），仅据问时形势作断，置信已降。功量清单：作用源＝女性候选人改口参选之势头线→对象＝特首之位归属，向＝助成（女性方），状态＝问时正发动；作用源＝男性候选人民望/辞任先行线→对象同上，向＝助成（男性方），状态＝已发动但选举委员会票源结构受制。主线认定：女性方势头线直接作用于归属且问时新发动、势头居首，为主线。定带：女性胜出带内取中位——胜出明确，票差不作夸大。",
0.58)

add(DATA_B19, "MP-018",
"方向：负（不能当选）。断语：曾俊华民望虽为候选人中最高，终不能当选2017年行政长官；得票居第二，败于获中央支持的对手。应期：2017年3月26日投票日揭晓。置信：中高。",
"卡面未标注 tradition/system；systems_used：形势参断兼相理取向（卡面未载相格细目）。卡面事实：传媒普遍指对手获北京支持、选情占优，曾俊华被视为陪跑、声势落后；民望高与选举委员会1,194人小圈子票源结构相悖——民望线不入票源。功量清单：作用源＝对手之建制支持线→对象＝曾俊华胜算，向＝压制，状态＝问时已成势、居首；作用源＝曾氏民望第一线→对象同上，向＝助成，状态＝旺而与票源结构不接。主线认定：建制支持线直接作用于小圈子投票结果且状态居首，为主线，取向压制。定带：败选带——居第二而败，不至票数崩盘。",
0.66)

add(DATA_B19, "MP-019",
"方向：林郑月娥当选。断语：2017年行政长官选举花落林郑月娥（1957酉年生），得票过半数门槛当选；曾俊华（1951卯年）居次，胡国兴（1946酉年）得票最少。应期：2017年3月26日投票当日。置信：中高。",
"卡面 tradition/system 未标注；systems_used：命年流年参断（卡面仅载三人出生年）兼形势。卡面事实：选举为2017丁酉年3月26日；林郑酉年生与流年丁酉同气、且具建制支持；曾俊华卯年生，卯酉相冲，流年冲命年主其势受冲；胡国兴年高而票源最窄。输入有限：卡面仅给出生年、无完整四柱，作断以命年＋形势为据，置信已酌降。功量清单：作用源＝林郑命年酉与流年酉同气线→对象＝林郑胜算，向＝助成，状态＝得令居首；作用源＝曾氏命年卯受流年酉冲线→对象＝曾氏胜算，向＝压制，状态＝冲动已成；逐方对读：林郑助成最强、曾次之受冲、胡票源最弱。主线认定：林郑同气助成线为主线。定带：林郑过半当选带，曾次、胡末之分配与逐方强弱同向。",
0.68)

add(DATA_B19, "OC-001",
"方向：一生先极盛后衰落。断语：吴佩孚以军权贵显，位至北洋首领级、主政一方为其极峰（中年）；晚年下野后权势尽失，境遇凋落，清贫孤介以终，不得善终之荣。应期（运档）：权位极峰在中年金水运段（约四十至五十余岁），晚年入木火运段转衰，下野后十年内势尽。置信：中高。",
"卡面未载 tradition/system（未标注）；systems_used：八字（子平，《千里命稿》应运篇论造口径）。四柱甲戌戊辰戊申壬子：戊土日主生辰月土旺，甲木七杀透年、壬水财透时，坐申食神。杀得财生、食神制杀，主统兵掌权之贵；然土重木弱，杀根不固，贵势难久持。功量清单：线1 甲木七杀（年干，得壬财生）→对象＝权位等级，向＝助成，状态＝透出而根浅；线2 申金食神（日支）→对象同上，向＝助成（食神制杀成贵），状态＝得地；线3 戊土比劫重重（月干、辰戌）→对象＝杀星之用，向＝压制（土重木折），状态＝旺相居首于晚运。主线认定：早中年线1、2合力为主线定贵带至首领级；晚年线3压制成主导，贵带回落。定带：极峰首领级、晚景平民清寒带，两段各按其运内主线取值。",
0.64)

add(DATA_B19, "OC-002",
"方向：一生大贵大富、善终。断语：宋子文贵显至财政首脑级，掌全国财政金融，富与贵俱足为一生极格；中年为权位极峰，晚年退居海外，权位渐退而富贵得全，寿终正寝。应期（运档）：极峰在中年土木运段（约三十至五十岁），晚年金水运段退居而安。置信：中高。",
"卡面 tradition 未标注；systems_used：八字（子平）。四柱甲午乙亥庚申己卯（原书取庚申日，异说庚辰未取，卡面已注）：庚金生亥月伤官旺，坐申禄身有根，乙木正财透而合庚，己土正印透时。伤官生财、财印并透，主财政天才得位。功量清单：线1 乙木财星（月干，亥卯半合木局助之）→对象＝富贵等级，向＝助成，状态＝旺相；线2 己土印星（时干）→对象＝权位，向＝助成，状态＝透出有根；线3 亥水伤官（月支）→对象＝官星之忌，向＝压制（伤官见官之隐患），状态＝旺而受印制。主线认定：线1财线直接作用于富贵对象且旺相居首，为主线。定带：富贵俱极带上位；伤官隐患只压晚年权位续航、不压富带。",
0.66)

add(DATA_B19, "OC-003",
"方向：一生名位财运俱盛、晚年渐退。断语：虞洽卿以商起家而成商界领袖，名位（商会首脑、社会名流）与财运同高；晚年声望仍在而实业渐收，终老于避难之地（客死异乡之象）。应期（运档）：盛年在中年水木运段，晚年金水运段持盈渐退。置信：中。",
"卡面 tradition 未标注；systems_used：八字（子平）。四柱丁卯丙午庚午己卯：庚金生午月，丙丁官杀并透、双午杀旺，己土印星透时化杀，卯木财星两见。杀旺身弱得印化，主以声望权力立名；财星生杀、印星化杀，商而兼政之格。功量清单：线1 己土印星（时干）→对象＝名位等级，向＝助成（化杀生身），状态＝透出居时、为救应；线2 丙丁双午官杀→对象＝日主，向＝压制，状态＝旺极；线3 卯木财星（年时）→对象＝财运，向＝助成，状态＝两见有根。主线认定：线1化杀线为成格主线，名位带定于领袖级；线2压制使身弱不任久劳，晚带回落一档。定带：名财俱盛带，晚年退而不败。",
0.60)

add(DATA_B19, "OC-004",
"方向：仕途清贵、晚年退隐平淡。断语：颜惠庆以资深外交官显名，位至驻外公使、内阁总长级，政府首脑仅属暂摄而非久任；晚年退出政坛，退隐终老。应期（运档）：显达在中年金水运段，晚年火土运段退居。置信：中。",
"卡面 tradition 未标注；systems_used：八字（子平）。四柱丁丑癸卯乙巳丙子：乙木生卯月建禄身旺，癸水偏印透月，丙火伤官透时，子水印根在时支。身旺印伤并透，主文才外交之清贵；伤官透时主仕路有起伏、高位不久。功量清单：线1 卯木禄神（月支）→对象＝日主强度，向＝助成，状态＝当令居首；线2 癸水印星（月干）→对象＝仕途清贵，向＝助成，状态＝透出；线3 丙火伤官（时干，巳根）→对象＝官星久任，向＝压制，状态＝透时主晚段。主线认定：线1、2合为清贵主线，定带公使/总长级；线3压制久任之量，首脑级只作暂摄带。定带：清贵高位带，晚年退隐带。",
0.58)

add(DATA_B19, "OC-005",
"方向：一生清贵显达、高寿善终。断语：吴经熊以法学著述与司法、外交职任显名，位至法院院长级并使节之任；食神吐秀主学术声名远播，晚年印运安享，寿高而终。应期（运档）：显达自中年木火运段起，晚年水印运段安泰。置信：中高。",
"卡面 tradition 未标注；systems_used：八字（子平）。四柱己亥丁卯乙未己卯：乙木生卯月、双卯禄旺身强，丁火食神透月吐秀，己土偏财两透，未为木库。食神生财、禄旺有库，主才学成名、衣禄丰足；无官杀混杂之压，清贵而久。功量清单：线1 丁火食神（月干，禄旺生之）→对象＝声名等级，向＝助成，状态＝得旺身生扶、居首；线2 己土财星（年时两透）→对象＝衣禄，向＝助成，状态＝食神生财成线；线3 亥水印星（年支）→对象＝晚年安泰，向＝助成，状态＝藏支待运引。主线认定：线1吐秀线为主线。定带：清贵显达带上位，晚年安泰高寿带。",
0.64)

add(DATA_B19, "OC-006",
"方向：当前受挫可勉渡而元气大伤、终难复全盛。断语：荣宗敬此次企业危机不至倾覆，印运扶身可支撑渡过、保住基业大半；然财杀交攻之局未改，往后再难回复全盛规模，数年内防本人大限（健康骤变）。应期（运档）：转机在本运后段（约一二年内见支撑落地），衰减在其后一运内成定局。置信：中。",
"卡面 tradition 未标注；systems_used：八字（子平）。四柱癸酉庚申戊午甲寅：戊土生申月，庚金食神透、癸水财透年、甲木七杀透时，坐午印根。食神生财本为富格，然身偏弱而时上杀星得寅根，危机时点（约1935乙亥年）财杀并旺攻身；所行印比之运扶身，故可渡而伤元。功量清单：线1 午火印星（日支）兼行运印气→对象＝日主存续，向＝助成，状态＝得地为救；线2 甲木七杀（时干，寅根，亥年财生）→对象＝基业，向＝压制，状态＝旺而发动；线3 癸水财星（年干）→对象＝基业，向＝压制（财滋杀），状态＝透出。主线认定：问时线2压制线状态居首定危机之重，线1救应线定其不覆。定带：渡险保业带（保大半、失全盛），本人寿程带下压一档并注明压制依据为杀财攻身。",
0.55)

add(DATA_B19, "OC-007",
"方向：才高而贵不成、寿短。断语：袁寒云（袁克文）性情狂放恃才，一生以文人狂士名世而功名断绝、贵气（显宦之子）不得其用；生活放旷耗身，寿数不长，约四十出头而终。应期（运档）：凶在中年土运段（四十岁前后），无晚年可言。置信：中高。",
"卡面 tradition 未标注；systems_used：八字（子平）。四柱庚寅甲申甲申甲戌：甲木生申月七杀当令、双申冲寅禄根，三甲比肩透干，戌土财星在时。杀重身弱、无印星化杀（全局无水），比肩只帮身不化杀——贵而不显、才而无成之局；申寅冲动主漂泊动荡，戌财滋杀耗身主寿程受压。注：命主为袁克文，与袁世凯本人有别（卡面已明）。功量清单：线1 申金七杀（月日两见）→对象＝日主与功名，向＝压制，状态＝当令双见、居首；线2 三甲比肩→对象＝日主，向＝助成，状态＝透干而根（寅）被冲；线3 戌土财星→对象＝杀星，向＝助成（财滋杀、反压日主），状态＝坐时。主线认定：线1杀线为主线，功名带压至无成、寿带压至中年而止。定带：文名带中上、功名带无、寿带短促。",
0.66)

add(DATA_B19, "OC-008",
"方向：军政显达、长寿善终。断语：商震行运得杀印相生之用，权位至省主席级并晋上将之阶，后段转任外交使节；晚年运入火地制杀得宜，安享高寿而终。应期（运档）：显达在中年金水运段，晚年火运段退居使节、寿终八十余。置信：中。",
"卡面 tradition 未标注；systems_used：八字（子平）。四柱戊子辛酉乙未己卯（时柱原书取己卯，一说丙子时原书斥误，卡面已注）：乙木生酉月，辛金七杀透月，子水印星在年，戊己财星两透，卯禄未库为根。杀旺而印化、禄根不拔，军政得位之格；财星滋杀为其量之压。功量清单：线1 辛金七杀（月干，酉令）→对象＝权位，向＝助成（杀印成格之杀源），状态＝当令；线2 子水印星（年支）→对象＝权位，向＝助成（化杀），状态＝藏支得年位；线3 戊己财星→对象＝日主，向＝压制（财滋杀耗身），状态＝两透。主线认定：线1、2杀印线合为主线定权位带至省主席/上将级；线3只压身不压格。定带：权位高带，寿带长。",
0.58)

add(DATA_B19, "OC-009",
"方向：仕途长青清贵、婚姻与财富俱有波折后得丰厚、高寿善终。断语：顾维钧外交生涯极长，历任使节与内阁要职而不坠，晚年转任国际司法之职安享荣名；婚姻有再娶之象，所娶得力而财富随之丰厚；寿数高。应期（运档）：显达贯穿中壮年多运，晚年清望运段善终。置信：低（四柱残损）。",
"卡面 tradition 未标注；systems_used：八字（子平）为问，然输入残损：卡面 birth.pillars 仅载『原书应运篇下论造（四柱以原书为准，转录本个别字待校）』，四柱干支实字未载——本例无法按柱作柱级推断，不臆补四柱。仅据卡面给定事实（命主为顶尖外交官、已历任驻外使节与内阁职务）与所问三面（财富、仕途、婚姻）作低置信轮廓断，置信已显著下调。残损例清单只列可指认之事实线：线1 历任使节与内阁职务之既成仕历→对象＝仕途等级，向＝助成，状态＝卡面明载已成；线2 （无柱）财星/妻星状态不可指认→对象＝财富与婚姻，向＝不定，状态＝无据。主线认定：线1为唯一可指认主线，仕途带定长青高位；财富婚姻两面无柱级做功线，只作轮廓带、不定量。定带：仕途高带；财婚两面不定带、明写无据。",
0.40)

add(DATA_B19, "OC-010",
"方向：位极而实权受制、三起三落、晚归平民。断语：溥仪命带帝座之象却身弱不任财官，一生为他人所推戴（傀儡之象多于实权），中年有幽禁牢狱之灾，末段废为平民终老，寿约六十出头。应期（运档）：最险在中年财杀运段（三十至五十岁间幽禁之事），晚年印运得安而平凡。置信：中高。",
"卡面 tradition 未标注；systems_used：八字（子平）。四柱丙午庚寅壬午丙午（原书未附大运表，卡面已注）：壬水生寅月食神泄气，三午财星成群、丙火财星两透，庚金偏印透月为唯一救应。财旺身弱、印孤——位象极尊而身不任之，主为人所制；食神生财主其性柔顺随流。功量清单：线1 丙午财星群（三午两丙）→对象＝帝位之实，向＝压制（身弱不任财），状态＝成群旺极居首；线2 庚金偏印（月干）→对象＝日主，向＝助成，状态＝孤透无根（寅中藏甲克之）；线3 寅木食神→对象＝性情取向，向＝助成（顺随），状态＝当令。主线认定：线1财群压制线为主线——位带极尊、权带近无，两带分开取值。定带：名位带极顶、实权带极低、中年幽禁带、晚景平民带。",
0.66)

add(DATA_B19, "OC-011",
"方向：早年成名而结局悲惨、寿短。断语：阮玲玉性情柔弱多感，电影声名极早极盛；一生致命伤在感情与婚姻——夫星暗而受冲、舆论人言压迫，二十余岁即有自毁之厄，不得善终。应期（运档）：凶在青年火土运段内（二十五岁前后）应验，无中晚年运程可论。置信：中高。",
"卡面 tradition 未标注；systems_used：八字（子平）。四柱庚戌辛巳己亥乙亥：己土生巳月印旺，辛金食神透月，乙木七杀透时，双亥财星冲巳印。印被财冲、杀透时上——名成而根地受冲，主精神依托被毁；食神透主演艺天分，财旺生杀主情事牵累致祸。功量清单：线1 双亥财星冲巳印→对象＝日主根基与名声之护，向＝压制，状态＝双冲发动、居首；线2 乙木七杀（时干，亥水生之）→对象＝婚姻与终局，向＝压制，状态＝透时得生；线3 辛金食神（月干）→对象＝声名，向＝助成（演艺成名），状态＝透出。主线认定：线1冲印线为主线定终局带。定带：声名带极高（青年）、寿带极短、婚姻带凶。",
0.66)

add(DATA_B19, "OC-012",
"方向：少年极盛、中晚年渐衰、婚姻波折。断语：杨秀琼十五六岁泳坛成名即为一生极峰，其后声名逐运递减；婚姻不美，有多嫁/为人妾室之象，中晚年漂泊异地，晚景平平。应期（运档）：极峰在己巳、庚午两运（约五至二十五岁），辛未运起渐退，壬申癸酉运名利俱淡。置信：中。",
"卡面 tradition 未标注；systems_used：八字（子平）。四柱己未戊辰丁未戊申：丁火生辰月，戊己食伤两透两见、申金财星在时，身弱泄重。食伤旺主技艺表现与早慧，官杀（夫星水）不透只藏辰未——婚姻星暗弱。大运卡面已给：五岁起己巳、庚午、辛未、壬申、癸酉、甲戌——巳午火运扶身生食伤，故少年极盛；后运金水泄克交加而衰。功量清单：线1 己巳庚午火运→对象＝少年声名，向＝助成，状态＝问时正值、居首；线2 戊己食伤群→对象＝日主元气，向＝压制（泄身太过），状态＝四见旺极；线3 夫星水不透藏库→对象＝婚姻等级，向＝压制，状态＝暗藏无力。主线认定：少年段线1为主线定极峰带；全局线2、3定中晚与婚姻之带。定带：少年声名带极高、中晚平带、婚姻带低且波折。",
0.60)

add(DATA_B19, "OC-013",
"方向：一生以技艺成盖世名望、晚景凄凉。断语：周信芳（麒麟童）京剧艺术成一代宗师之名，中年为极峰；晚年运入克身之乡，名匠遭时局之劫，晚景困顿、不得安闲善终。应期（运档）：极峰在中年金水运段，晚年最后一两运转衰，凶在七十余岁后。置信：中。",
"卡面 tradition 未标注；systems_used：八字（子平）。四柱甲午丁丑辛酉甲午：辛金生丑月印库，坐酉禄身旺，丁火七杀透月，甲木财星两透。身旺杀透得禄刃抗之，主以刚烈技艺压场成名；财星两透滋杀，晚运若逢火木，杀力转盛克身。卡面注八岁起运、未列运干支，运段细节以略断处理并降置信一档。功量清单：线1 酉金禄神（日支）→对象＝日主与技艺，向＝助成，状态＝坐禄居首；线2 丁火七杀（月干）→对象＝声名形态，向＝助成（杀主威严唱功之压场），状态＝透出；线3 甲木财星两透→对象＝晚年日主，向＝压制（财滋杀），状态＝两见待运引。主线认定：线1禄线为成名主线；晚段线3引动后压制转主。定带：声名带宗师级、晚景带凄凉。",
0.58)

add(DATA_B19, "OC-014",
"方向：仕途清贵至厅长级而止、上行有顶。断语：蒋邦彦以财政专业显达，官至省财政厅长级即为其格之顶，再上受制；行金水运则顺遂升转，行土运则伤官见官之滞与险并见，晚年渐退、中上善终。应期（运档）：显达在中年金水运段，土运段为仕路险段。置信：中。",
"卡面 tradition 未标注；systems_used：八字（子平）。四柱庚辰己卯壬寅辛丑：壬水生卯月伤官当令，寅卯木旺泄身，庚辛印星两透为救，己土正官透月。伤官配印成格主才干清贵；然官星己土坐卯受伤官之克——伤官见官之结构压其上行之顶。功量清单：线1 庚辛印星（年时两透）→对象＝仕途等级，向＝助成（配印成格），状态＝两透居力；线2 卯木伤官（月支当令）→对象＝官星己土，向＝压制，状态＝当令居首于官面；线3 己土官星（月干）→对象＝权位，向＝助成，状态＝透而受克。主线认定：格成主线为线1，定带厅长级；线2为封顶压制线，带顶由此定。定带：仕途带厅长级封顶，晚年中上善终带。",
0.58)

add(DATA_B19, "OC-015",
"方向：君主贵命、守成而终。断语：乔治五世位极人君，中年即位，一生以稳重守成巩固王位于大战之世；晚年健康转衰，寿约七十而终，王位传嗣平稳。应期（运档）：即位在中年运段初，大战考验在其在位中段，晚年最后一运体衰。置信：中。",
"卡面 tradition 未标注；systems_used：八字（子平）。四柱乙丑辛巳甲辰甲子（韦氏据西报传略译生庚演造，卡面已注）：甲木生巳月食神泄秀，辛金正官透月，子水印星在时，两甲比肩帮身。官印相生、食神有制，主守成之君格；身偏弱而官印两全其位。功量清单：线1 辛金官星（月干，得巳中庚根）→对象＝王位等级，向＝助成，状态＝透出当令之月；线2 子水印星（时支）→对象＝王位存续，向＝助成（官印相生），状态＝坐时待运；线3 巳火食神（月支）→对象＝日主元气，向＝压制（泄弱身），状态＝当令。主线认定：线1、2官印线合为主线定王位带；线3定晚年体衰之量。定带：位带极顶、业带守成、寿带约七十。",
0.58)

add(DATA_B19, "OC-016",
"方向：以术数立身、名大于利、高寿而晚境清。断语：韦千里（命师自造）一生以命理著述与为人推命成名，中年为声名极峰；财星虽旺而身弱不任，财来财去难聚大富；晚年运入官杀之乡境遇转清苦，寿数不短，约七十余终。应期（运档）：极峰在中年水木运段，晚年火土运段清淡。置信：中。",
"卡面 tradition 未标注；systems_used：八字（子平）。四柱辛亥辛卯庚子庚辰：庚金生卯月正财当令，双辛劫财、双庚比劫帮身，子水伤官、亥水食神泄秀。身弱财旺、比劫帮身夺财并见——以技艺（食伤泄秀）求财之命，名成而财聚不住；辰为水库湿土能生金为晚根。功量清单：线1 卯木财星（月支当令，亥卯半合）→对象＝财富等级，向＝压制（身弱不任财），状态＝当令居首；线2 庚辛金群→对象＝日主，向＝助成（帮身），状态＝四见；线3 子亥食伤→对象＝声名，向＝助成（泄秀成名），状态＝两见。主线认定：声名面线3为主线定带中高；财富面线1压制为主定带聚不住。定带：名带高、财带中下、寿带长。",
0.56)

add(DATA_B19, "OC-017",
"方向：大富而贵不足。断语：刘澄如以丝业致巨富，富甲一方（地方首富级）；官印受财势所困，贵显之途不显，一生以富掩贵；晚运得印扶则家业可守，子孙承业。应期（运档）：致富在中年财运段，晚年印比运段守成。置信：中。",
"卡面 tradition 未标注；systems_used：八字（子平，《子平真诠评注》论用神成败救应章引例）。四柱壬戌己酉丁丑甲辰：丁火生酉月偏财当令，己土食神透月生财，壬水正官合丁，甲木正印透时为救。财旺身弱、食神生财成富格之主线；官星合身而受财围，印星居时为晚救——富格成、贵格败中有救。功量清单：线1 酉金财星（月支当令，丑酉半合金）→对象＝财富等级，向＝助成，状态＝当令居首；线2 己土食神（月干）→对象＝财富，向＝助成（生财成线），状态＝透出；线3 壬水官星合丁＋甲印居时→对象＝贵显，向＝压制（官受合困）兼晚救，状态＝官透受合、印迟发。主线认定：线1、2富线合为主线定巨富带；贵面压制线定其贵不足。定带：富带地方首富级、贵带低、晚年守成带。",
0.62)

# ---------------- B20 ----------------
add(DATA_B20, "OC-018",
"方向：名位极盛而终局横夭。断语：史量才以报业成一代巨头，地位声望俱极；然伤官锋芒太露、杀星透而运入火乡，中年后与权贵冲突致祸，五十四五岁前后有遇刺/非命之厄，不得善终。应期（运档）：凶在五十岁前后行运入火土之段。置信：中。",
"卡面 tradition 未标注；systems_used：八字（子平，《子平真诠评注》引例）。四柱己卯丙子庚寅辛巳：庚金生子月伤官当令，丙火七杀透月，寅木财星坐日，辛金劫财帮身。伤官旺主言论锋芒，杀透无印化、赖辛劫与巳中庚根撑身——名高谤至、与权相抗之局；财生杀旺为晚段压线。功量清单：线1 丙火七杀（月干，寅巳助之）→对象＝人身终局，向＝压制，状态＝透月得势居首于晚段；线2 子水伤官（月支当令）→对象＝声望形态，向＝助成（锋芒成名）兼招忌，状态＝当令；线3 辛巳金根→对象＝日主，向＝助成，状态＝一透一藏、力薄。主线认定：终局面线1为主线定横夭带；声名面线2定极盛带。定带：名位带极盛、寿带中年横折。",
0.60)

add(DATA_B20, "OC-019",
"方向：才学显名而中年横夭。断语：杨杏佛以学界与研究院职务显名，位至总干事级；惜中年运入财杀之乡，身弱难任，四十岁前后有横祸之险（非命之厄），英年而折。应期（运档）：凶在四十岁前后一运之内。置信：中。",
"卡面 tradition 未标注；systems_used：八字（子平）。四柱癸巳丙辰壬申癸卯——卡面明注：韦千里《千里命稿》另载癸巳甲寅壬辰庚子，两书全异，本例以徐乐吾《子平真诠评注》本为准作断，此分歧在 basis 留痕、不混用。壬水生辰月水库，申金印星长生，癸水比劫两透帮身，丙火财星透月，卯木伤官在时。身有根有帮本可任事，然财星透而运入火土则财杀攻身；伤官在时主晚段言行招忌。功量清单：线1 申金印星（日支长生）＋双癸帮身→对象＝日主强度，向＝助成，状态＝有根居力；线2 丙火财星（月干）→对象＝中年终局，向＝压制（财引杀机），状态＝透出待运旺；线3 卯木伤官（时支）→对象＝仕途顺逆，向＝压制（伤官见官之忌），状态＝坐时。主线认定：早中年线1主线定显名带；中年线2待运成主定横夭带。定带：名位带总干事级、寿带四十前后横折。",
0.55)

add(DATA_B20, "OC-020",
"方向：大贵极显而寿程受限。断语：谭延闿位至国民政府主席级，贵显为一生之极；食神制杀成格而杀重身弱，五十一二岁前后运岁并临有骤终之象（病卒），贵而不寿。应期（运档）：极峰在四十余岁运段，凶在其后一运之初。置信：中。",
"卡面 tradition 未标注；systems_used：八字（子平，《子平真诠评注》引例）。四柱己卯丁丑癸丑乙卯：癸水生丑月七杀当令、双丑杀库，丁火财星透月，乙木食神透时、双卯食根。食神制杀成格得大贵；然身弱无印（全局无金），杀重财滋，寿元之根薄。功量清单：线1 乙卯食神（时干双卯根）→对象＝贵显等级，向＝助成（制杀成格），状态＝透时根固居力；线2 丑土七杀（月日两见当令）→对象＝寿程，向＝压制，状态＝双见旺极；线3 丁火财星（月干）→对象＝杀星，向＝助成（财滋杀、反压日主），状态＝透出。主线认定：贵面线1为主线定主席级带；寿面线2为主线定寿限带。定带：贵带极顶、寿带五十出头骤终。",
0.62)

add(DATA_B20, "OC-021",
"方向：一时极贵、晚势倾覆。断语：陆荣廷以军功成旧桂系首领，统辖两广为其极峰，格局属军阀大贵；然杀旺财滋、根基系于一时之运，六十岁前后失势下野，晚景衰落以终。应期（运档）：极峰在中年木火运段，倾覆在六十岁前后运转之交。置信：中。",
"卡面 tradition 未标注；systems_used：八字（子平，《子平真诠评注》论用神格局高低章引例）。四柱戊午辛酉乙卯丙戌：乙木生酉月七杀当令，辛金杀透，坐卯禄根抗杀，丙火伤官透时，戊土财星透年。禄刃抗杀、伤官助势——格局高低章所论：格成于抗杀而根在禄，运去禄伤则格破。功量清单：线1 卯木禄神（日支）→对象＝格局存立，向＝助成，状态＝坐禄居首；线2 辛酉七杀（月干月支当令）→对象＝权位，向＝助成（杀为权柄）兼压身，状态＝当令；线3 戊土财星（年干，戌库）→对象＝杀星，向＝助成（财滋杀）兼耗身，状态＝透出。主线认定：线1、2合为成格主线定两广首领带；禄根受运冲之年即格破之年。定带：极峰带军阀首领级、晚景带衰落下野。",
0.60)

add(DATA_B20, "OC-022",
"方向：科第无缘、转以术数立身。断语：袁树珊出身命学世家，聪颖好学而功名屡试不第，科第之路断绝；一生改以命理著述与为人推命立身成家，清名有而厚禄无，寿数不短。应期（运档）：功名之挫贯穿青年至中年应试各运段，立身转机在中年运入印比之段。置信：中高。",
"卡面 tradition 未标注；systems_used：八字（子平，命主自造自批）。四柱辛巳丁酉乙巳戊寅（安命甲午、大运丙申起，卡面已注）：乙木生酉月七杀当令，丁火食神透月制杀，双巳食伤根，戊土财透时，寅木禄根。食神制杀本主贵，然制杀太过反伤官星之用、且杀为功名之星受制——学优而仕蹇；寅禄与食伤主以技艺著述自立。卡面事实『屡试功名不第』与此结构同向。功量清单：线1 丁巳食神群（月干双巳）→对象＝官杀（功名星），向＝压制（制杀过当），状态＝三见居首；线2 辛酉七杀（月干支）→对象＝功名等级，向＝助成（本为功名之源），状态＝当令而受制；线3 寅木禄根→对象＝立身之本，向＝助成，状态＝坐时。主线认定：线1压制线为功名面主线定科第无带；线3定转业立身带。定带：功名带无、术业名带中高、衣禄带清平。",
0.64)

add(DATA_B20, "OC-023",
"方向：金属器物、不完好。断语：钟下所覆为一件金属所制、中空有足之器物（铜铁器皿一类，如小鼎/香炉之属）；且此物不完好——有折足/残损之象。应期：即席当场揭钟即验，无时间窗外推。置信：低。",
"卡面 tradition 未标注；systems_used：梅花易数（《梅花易数》卷三钟覆物占，卡面载卦象）。卡面给定：火风鼎变雷风恒。鼎卦上离下巽，鼎象本身即三足中空之金属器皿，离为中虚、为金属甲壳之象；鼎卦辞有『鼎折足』之文，变恒主其物存置已久。输入残损：卡面未载动爻，体用生克无从精定，射覆只取卦象类象作断，置信已降。功量清单：线1 鼎卦本象（三足中空之器）→对象＝所覆物类别，向＝助成（定金属器皿类），状态＝卦象全体居首；线2 鼎折足之辞象→对象＝完好程度，向＝压制（定残损），状态＝辞象可指认；线3 变卦恒→对象＝物之新旧，向＝压制（定旧置），状态＝变卦成立。主线认定：线1为主线定类别带。定带：类别带金属器皿、完好带残损。",
0.35)

add(DATA_B20, "OC-024",
"方向：葬资有着落、葬事可办。断语：易者身后无资之困可解——其生前已自藏营葬之资于日常器物之中（枕中窖藏金银之属），来访者击破其枕即可得金充葬费，葬事因此办成。应期：即访当日得资、无待外求。置信：中。",
"卡面 tradition 未标注；systems_used：梅花易数源流成例参断（《梅花易数》序·击鼠枕窖金，卡面载事由）。卡面事实：易者遗书预言来访秀士可托身后事，其家苦于无资营葬——预言本身即指其家内藏有后手；序文成例之主线即『枕中藏金』：资不出其室、藏于卧具。输入有限：卡面未载卦象，作断以序文事理与成例主线为准，置信酌降。功量清单：线1 遗书预言托付线→对象＝葬资着落，向＝助成，状态＝卡面明载；线2 其家无资之现状线→对象同上，向＝压制，状态＝卡面明载。主线认定：线1为主线——预言既出，资必已备于内。定带：葬资带足敷一葬、葬事带可办成。",
0.58)

add(DATA_B20, "OC-025",
"方向：应验。断语：邵雍椅底预书之事届期应验——至预书所定年月日，椅子果被来客坐破，破在坐具本体（椅面/椅脚），预言分毫不爽。应期：即预书所载之年月日当日。置信：中。",
"卡面 tradition 未标注；systems_used：梅花易数源流成例参断（《梅花易数》序·置椅坐破，卡面载事由）。卡面事实：邵雍预先于椅底写下某年月日椅子将被坐破之预言——此类预书成例以届期坐破为验，问『是否应验』主线取验。输入有限：卡面未载预书具体年月日与卦象，日期只对回预书本身、不外推，置信酌降。功量清单：线1 椅底预书线（年月日与坐破两项俱定）→对象＝应验与否，向＝助成（定应验），状态＝卡面明载已预书；线2 （无反证线）日常坐具无破之现状→对象同上，向＝压制，状态＝弱。主线认定：线1为主线。定带：应验带全验（日期与坐破两项俱中）。",
0.58)

add(DATA_B20, "OC-026",
"方向：功名可得。断语：两客今年功名有成——末传卯木官星归终，主其中至少一人得中/得功名进身，另一人亦沾其泽（同榜或候补）；过程先有文书口舌之扰（螣蛇中传）而不碍终局。应期：年档内，主坐标取卯月（二月）放榜/见分晓。置信：中。",
"卡面 tradition 未标注；systems_used：大六壬（《大六壬占验指南》第57课，冻结体照常法作断）。卡面给定：1643年正月初四己亥日辛未时，课式涉害、曲直，三传乙未（青龙）、己亥（螣蛇）、癸卯（玄武），丑将，甲午旬辰巳空。日干己土，卯为其官星居末传——传终归官主功名终成；初传未乘青龙主喜庆发端；曲直课木局成势助官星之旺；中传亥螣蛇主中途虚惊口舌。功量清单：线1 末传卯木官星（玄武乘之）→对象＝功名等级，向＝助成，状态＝居传终、曲直木势助旺、居首；线2 初传未乘青龙→对象＝发端喜庆，向＝助成，状态＝发用；线3 中传亥乘螣蛇→对象＝过程顺逆，向＝压制（虚惊），状态＝居中传、不居终。逐方对读：二人同占一课，官星归一传——得者为主、沾泽者为副，分配与传位同向。主线认定：线1为主线。定带：功名带得中一级（非鼎甲之夸），过程带先扰后成。",
0.52)

add(DATA_B20, "OC-027",
"方向：此行不得意。断语：方替夫奉诏北上终不得意——到京难得实任重用，行程与任事两皆落空之象（末传亥空）；本人途中/到京后防病厄；老母在家尚属无恙、无大碍可虑。应期：月档，此行以数月内（冬季至次年春）见分晓。置信：中。",
"卡面 tradition 未标注；systems_used：大六壬（指南第58课）。卡面给定：1642年冬月初五辛未日甲午时，课式无禄、无路，三传癸酉（六合）、戊辰（太阴）、亥（青龙，空亡），丑将，甲子旬戌亥空。课名无禄无路已定主向不利；末传青龙乘亥而空亡——贵气落空，主终局落空；日干辛金禄于酉（初传）仅主行程得发而无后劲。母事：母生甲子年，年命未见凶传克入，只作尚安轮廓断。功量清单：线1 末传亥水青龙空亡→对象＝此行终局，向＝压制（落空），状态＝空亡居传终、居首；线2 课格无禄无路→对象＝任事之禄，向＝压制，状态＝课名明载；线3 初传酉为日禄乘六合→对象＝行程发端，向＝助成，状态＝发用而后继空。主线认定：线1为主线定终局带。定带：任事带落空、行程带可达而无成、母安带无大碍。",
0.55)

add(DATA_B20, "OC-028",
"方向：得官、文职清要之缺。断语：朱西崑入觐考选可得官，所授为京师部属文职（主事/员外一类清要之缺），品级中等；任命文书经一番周折后落定。应期：月档，主坐标取次年春（巳火印星得值之月前后）授官文书到手。置信：中。",
"卡面 tradition 未标注；systems_used：大六壬（指南第59课）。卡面给定：1630年冬月十四己丑日辛未时，课式重审、斫轮，三传辛卯（玄武）、丙戌（朱雀）、癸巳（白虎），寅将，甲申旬午未空。日干己土，初传卯木官星发用主得官之机；中传戌乘朱雀主文书诏命；末传巳火为己之印星乘白虎，印归传终主官印终得而带一番辛劳周折；斫轮课主雕琢成器。功量清单：线1 初传卯木官星发用→对象＝得官与否，向＝助成，状态＝发用居首；线2 中传戌乘朱雀（文书）→对象＝授官程序，向＝助成，状态＝居中传；线3 末传巳火印星乘白虎→对象＝品级与辛劳，向＝助成兼压制（印成而虎主劳），状态＝居传终。主线认定：线1为主线定得官；线3定其品级带。定带：得官带成、品级带中等文职。",
0.52)

add(DATA_B20, "OC-029",
"方向：求官可得而迟、家有高年之忧。断语：王米山携子求官，子辈可得一缺而须候补迟延，非即时到手；诸事之中以家母为重忧——老母年近九十，初传白虎临未，主本年内有重病/寿终之忧，须先备家事。应期：年档，官事主坐标在次年春（卯官得值）见缺，母事在本年内应验。置信：中低。",
"卡面 tradition 未标注；systems_used：大六壬（指南第60课）。卡面给定：1642年十月初二己亥日辛未时，课式涉害、曲直、回环，三传乙未（白虎）、癸卯（六合）、己亥（天后），丑将，甲午旬辰巳空；其子丑命。日干己，中传卯木官星乘六合主官事有合可成，末传亥天后主阴助迟成；初传未土乘白虎——未为木库长辈之位、白虎主丧疾，年近九十之母应此象最切。子丑命与中传卯无冲破，子事以得缺迟延断。功量清单：线1 中传卯官乘六合→对象＝子辈官缺，向＝助成，状态＝居中传、合主成而迟；线2 初传未乘白虎→对象＝老母安危，向＝压制（丧疾），状态＝发用居首于家事面；线3 末传亥乘天后→对象＝官事终局，向＝助成（阴助），状态＝居传终。主线认定：官面线1为主线、家事面线2为主线，两面分线定带。定带：官带小缺迟得、母带本年大忧。",
0.48)

add(DATA_B20, "OC-030",
"方向：可复、照旧。断语：淮扬巡按差可望复设（铸印成课、印星发用主官印重铸），吏书之缺亦可照旧保留，不废；惟复设之文迟缓，须经一番议复才落定。应期：月档，主坐标取次年春（卯官得值之月）见明文。置信：中。",
"卡面 tradition 未标注；systems_used：大六壬（指南第64课）。卡面给定：1651年二月初十戊子日戊午时，课式重审、铸印，三传癸巳（太常）、丙戌（六合）、辛卯（太阴），亥将。铸印课主铸印成器、任命得行；初传巳火为戊土日干之印星乘太常（印绶衣冠之将），印发用主复设得据；中传戌六合主议合而成；末传卯木官星乘太阴主事成于暗中议定。功量清单：线1 初传巳火印星乘太常→对象＝巡按差复设，向＝助成，状态＝发用居首；线2 中传戌乘六合→对象＝议复程序，向＝助成，状态＝居中传；线3 末传卯官乘太阴→对象＝落定形态，向＝助成（暗成），状态＝居传终。逐方对读：巡按差面印线最强主复、吏书缺面同课同气主照旧，两方分配与传线强弱同向。主线认定：线1为主线。定带：复设带可复、吏缺带照旧、进程带迟缓。",
0.52)

add(DATA_B20, "WP-001",
    "Direction: Yes — a major collective affliction in the form of a worldwide pandemic. Judgment: The 2020–2021 period holds a global epidemic/pandemic outbreak of disease, spreading across nations and bringing mass illness and mortality, coinciding with the Jupiter–Saturn–Pluto conjunction of early 2020 and the lowest cyclical-index reading of the century. Timing: window 2020–2021, main coordinate early 2020 (conjunction exact). Confidence: moderately high.",
    "Card carries no tradition/system field (not stated); systems_used: western mundane astrology. Card facts: five outer planets gather within ~100 degrees around 2020 with a Jupiter–Saturn–Pluto conjunction; cyclical index at its 21st-century low; comparable past clusters coincided with 1918, 1954, 1968 and 1982 (1918 being a pandemic year). [Section-8 work-quantity check R80-REV1] Work lines: L1 Jupiter-Saturn-Pluto conjunction (exact early 2020) -> object = collective conditions 2020-21, direction = affliction-bearing (supports), state = exact and focal, ranked first; L2 cyclical index at century low -> object same, direction = supports (affliction scale), state = extreme reading; L3 historical cluster parallels incl. 1918 -> object same, direction = supports (epidemic precedent), state = cited on card. Main line: L1. Band set: major global pandemic band (not a minor regional outbreak).",
    0.70)

add(DATA_B20, "WP-002",
    "Direction: Barack Obama wins. Judgment: Sen. Barack Obama wins the 2008 US presidential election on 4 November 2008, defeating Sen. John McCain; the Saturn–Uranus opposition exact on Election Day favours the change candidate (Uranus) over the older establishment figure (Saturn). Timing: single point, election day 4 Nov 2008. Confidence: moderate.",
    "Card tradition/system not stated; systems_used: western mundane/electional astrology. Card facts: Obama leads Clinton for the nomination but has not clinched it; McCain is the presumptive Republican nominee; Saturn opposes Uranus beginning on Election Day, last seen 45 years earlier (a change-of-era signature). [Section-8 R80-REV1] Work lines: L1 Saturn-Uranus opposition exact on election day -> object = outcome allocation, direction = supports Obama (change pole), state = exact on the day, ranked first; L2 Obama's nomination momentum (leads delegate race) -> object same, direction = supports Obama, state = active on card; L3 McCain as elder establishment nominee -> object same, direction = supports McCain under Saturn, state = weakened by opposition aspect. Allocation read-back: Obama line stronger than McCain line, allocation matches relative strengths. Main line: L1. Band set: Obama victory band, margin not overstated.",
    0.60)

add(DATA_B20, "WP-003",
    "Direction: Barack Obama is re-elected. Judgment: Incumbent President Obama defeats Mitt Romney in the 6 November 2012 election and wins a second term; Mercury turning retrograde on election day marks counting disputes, delayed clarity in close states and post-election argument, but does not overturn the result. Timing: election day 6 Nov 2012, result confirmed within the following days. Confidence: moderate.",
    "Card tradition/system not stated; systems_used: western mundane/electional astrology. Card facts: incumbent Obama vs presumptive nominee Romney, polling competitive; Mercury retrograde begins on election day (a signature of recounts/confusion, not by itself of incumbent defeat). [Section-8 R80-REV1] Work lines: L1 incumbency line (sitting president's chart position in mundane practice) -> object = outcome allocation, direction = supports Obama, state = structural, ranked first; L2 Mercury retrograde from election day -> object = process clarity, direction = suppresses (clarity), state = exact on the day; L3 competitive polling -> object = margin, direction = suppresses (margin), state = card-stated. Allocation read-back: Obama retains office; Romney takes the loss side. Main line: L1. Band set: Obama re-election band with narrow/disputed-count texture.",
    0.60)

add(DATA_B20, "WP-004",
    "Direction: Hillary Clinton wins. Judgment: The conference panel's collective judgment is that Democrat Hillary Clinton defeats Donald Trump in the 8 November 2016 election, in line with her polling lead. Timing: election day 8 Nov 2016. Confidence: moderate-low.",
    "Card tradition/system not stated; systems_used: western mundane astrology (conference panel consensus as the recorded reading). Card facts: Clinton faces Trump; most polls favour Clinton; the source is the ISAR conference election-forecasting panel report (Oct 2016). Panel-consensus readings in this source tradition follow the majority chart judgment, which tracked the polling-favoured candidate. Input limitation: card gives no individual charts, so the panel majority is taken as the reading; confidence lowered. [Section-8 R80-REV1] Work lines: L1 panel majority judgment -> object = outcome allocation, direction = supports Clinton, state = collective and focal, ranked first; L2 polling lead (card-stated) -> object same, direction = supports Clinton, state = consistent; L3 (no counter-line on card) minority dissent exists by panel format -> object same, direction = suppresses (certainty only), state = unquantified on card. Allocation read-back: Clinton side takes the win allocation. Main line: L1. Band set: Clinton victory band, confidence capped by absent charts.",
    0.55)

add(DATA_B20, "WP-005",
    "Direction: Donald Trump wins. Judgment: The individual panel astrologer singled out in this report — the one who had earlier, against a 17-candidate field, correctly picked Trump to become the Republican nominee — reads the final charts for Trump: Donald Trump defeats Hillary Clinton in the 8 November 2016 election despite her polling lead. Timing: election day 8 Nov 2016. Confidence: moderate-low.",
    "Card tradition/system not stated; systems_used: western mundane astrology (individual astrologer's reading). Card facts distinguishing this case from the panel-consensus case: one panel astrologer had earlier in the cycle, when 17 Republicans still contested the nomination, picked Trump as nominee — the report isolates this reader, whose demonstrated track record on this very race is the operative line; the collective polling lead belongs to the opposing (panel-majority) reading. [Section-8 R80-REV1] Work lines: L1 this reader's prior verified hit on Trump's nomination -> object = outcome allocation, direction = supports Trump, state = track-record line, ranked first for this case; L2 polling lead -> object same, direction = supports Clinton, state = card-stated but attached to the majority reading; L3 panel setting -> object = certainty, direction = suppresses, state = divided panel. Allocation read-back: Trump side takes the win allocation under this reader's line. Main line: L1. Band set: Trump victory band, narrow.",
    0.50)

add(DATA_B20, "WP-006",
    "Direction: Britain votes to leave. Judgment: The 23 June 2016 referendum returns a Leave verdict — Britain votes to leave the European Union, against the February polling lead for 'Stay'; the Uranus–Ceres conjunction at 23 degrees Aries on referendum day marks the disruptive break with the status quo. Timing: referendum day 23 June 2016, result known 24 June. Confidence: moderate-low.",
    "Card tradition/system not stated; systems_used: western mundane astrology (UK national charts 1066/1801/1922 as given on card). Card facts: assessment first published 5 Jul 2015 and firmed up 22 Feb 2016 — i.e., the Leave call was committed before the date was set and held against 'Stay'-leading polls with many undecideds; Uranus conjunct Ceres at 23 Aries on referendum day is the disruptive signature the reading rests on. [Section-8 R80-REV1] Work lines: L1 Uranus-Ceres conjunction on referendum day -> object = outcome allocation, direction = supports Leave (rupture), state = exact on the day, ranked first; L2 early committed assessment (Jul 2015, firmed Feb 2016) -> object same, direction = supports Leave, state = pre-dated and held; L3 February polls 'Stay' ahead -> object same, direction = supports Stay, state = soft (vast undecided bloc on card). Allocation read-back: Leave side stronger under L1+L2. Main line: L1. Band set: Leave victory band, narrow margin.",
    0.55)

add(DATA_B20, "WP-007",
    "Direction: Donald Trump wins, decided by Clinton's scandals. Judgment: The Union Square tarot reading gives the 2016 election to Donald Trump; what decides it is the damage to Hillary Clinton from the email controversy and the Clinton Foundation — scandal, not policy or turnout mechanics, is the deciding factor named by the spread. Timing: election day 8 Nov 2016, with the deciding scandal pressure peaking in the final stretch (late October–early November). Confidence: low-moderate.",
    "Card tradition/system not stated; systems_used: western tarot (street reading as recorded; card-by-card spread not reproduced on the card — input limitation noted, confidence lowered). Card facts: reading drawn August 2016 in Manhattan's Union Square Park; Clinton leads most August polls; her email controversy and the Clinton Foundation are already public controversies, and the question explicitly asks what will decide it — the recorded reading's deciding-factor line attaches to those controversies. [Section-8 R80-REV1] Work lines: L1 scandal line (email + Foundation controversies, card-stated as live) -> object = outcome allocation, direction = suppresses Clinton / supports Trump, state = active and focal in the question, ranked first; L2 August polling lead -> object same, direction = supports Clinton, state = card-stated, pre-dates the deciding late pressure; L3 (spread detail absent) -> object = certainty, direction = suppresses, state = not on card. Allocation read-back: Trump takes the win allocation; Clinton's loss is assigned to the scandal line. Main line: L1. Band set: Trump victory band via scandal-decided mechanism.",
    0.45)

# ---------------- write + assert ----------------
def dump(lst, expect, label):
    assert len(lst) == expect, (label, len(lst))
    ids = [d["case_id"] for d in lst]
    assert len(set(ids)) == expect, (label, "dup")
    for d in lst:
        for k in ("case_id", "prediction_text", "basis", "confidence", "trigger"):
            assert k in d, (d["case_id"], k)
        assert 0.0 <= d["confidence"] <= 1.0
        t = d["trigger"]
        assert t == {"changed_main": False, "reserve_used": False,
                     "disputed": False, "reason": ""}, d["case_id"]
        p = os.path.join(BASE, d["case_id"] + ".json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
    print(label, "written:", len(lst), ids)
    return ids

all_ids = dump(DATA_B19, 20, "B19") + dump(DATA_B20, 20, "B20")
assert len(all_ids) == 40
print("TOTAL", len(all_ids))
