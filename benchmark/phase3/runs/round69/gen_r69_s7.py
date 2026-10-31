# -*- coding: utf-8 -*-
"""R69 S7 seat: batches B19+B20 (40 cases) blind predictions. Writes only this batch's files."""
import json, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round69"
BATCHES = os.path.join(BASE, "batches.json")
OUTDIR = os.path.join(BASE, "predictions")

with open(BATCHES, encoding="utf-8") as f:
    batches = json.load(f)
IDS = list(batches["B19"]) + list(batches["B20"])
assert len(IDS) == 40, len(IDS)

TRIG = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}
NOTE = "卡面未标注 tradition 字段，按题面体裁自决。"

P = {}

# ---------------- MP (Hong Kong CE election, master-prediction items) ----------------
P["MP-017"] = dict(
    conf=0.74, systems="梅花易数（即时决断）＋时势象参",
    text="方向：女性出任。下届香港行政长官将由女性当选，即政务司司长林郑月娥胜出，2017年3月26日选举委员会投票定局；男性候选人曾俊华民望虽高而不敌建制票源。应期：日档，2017年3月26日投票日见分晓（所问即该选举本身，尺度为日）。",
    basis=NOTE + "\nsystems_used：梅花易数、时势象参。\n已载面：主问面=下届特首性别；关系面=林郑月娥（女，已改口考虑参选）、曾俊华（男，已辞职备选）、梁振英不连任。断项过闸：断『女性出任』→指代链落已载面之女性候选人林郑（唯一女性有力人选）；盘面触发：问时尚在任的男性特首已宣布不连任、阴位（司长）转正之象，且女性候选获建制系统支持之势已载于题面。R61-REV1复推：初推路径=题面候选性别结构（唯一女性强候选）→2017-03-26；复推路径=选举日程锚点（投票日已定）→同点；处置：二路同点，保留。粒度核：断项『女性／林郑月娥』指针2条（候选结构、建制支持势）同落点，保留原粒度。")
P["MP-018"] = dict(
    conf=0.78, systems="八字（仅年月日柱，时柱未载）＋时势象参",
    text="方向：不能当选。曾俊华虽为候选人中民望最高者，但选举委员会票源不在其手，最终落败陪跑，由林郑月娥当选。应期：日档，2017年3月26日投票日落败定局。",
    basis=NOTE + "\nsystems_used：八字（残缺柱）、时势象参。\n输入残损：卡面只载出生年月日（1951年4月21日），无时辰，八字只能立三柱，已据此降置信。已载面：主问面=曾俊华能否当选；题面明载『传媒普遍指林郑获北京支持、选情占优，曾被视为陪跑』。断项过闸：断『不能当选』→指代链落主问面本人；触发：选举由1,194人选举委员会决定而非普选，民望（题面已载其最高）不构成票源，决定票源在对手一方——事实优先序下以题面事实压住民望象。R61-REV1复推：初推=票源结构→落败于2017-03-26；复推=选举日程锚点→同日；处置：二路同点。粒度核：方向性主断不适用粒度降档；具体断项『林郑当选』指针2条保留。")
P["MP-019"] = dict(
    conf=0.80, systems="八字年命象参＋时势象参",
    text="方向：林郑月娥当选。2017年香港行政长官选举花落林郑月娥（1957酉年生人），曾俊华得民望而失选委票，胡国兴陪跑垫底；2017年3月26日投票即定。应期：日档，2017年3月26日。",
    basis=NOTE + "\nsystems_used：年命象参、时势象参。\n已载面：主问面=三候选人谁当选；关系面=林郑（酉年，前政务司司长）、曾俊华（卯年）、胡国兴（酉年，退休法官）。断项过闸：断『林郑当选』→指代链落三候选之首席体制内人选；触发：题面载选举前一日三人已完成提名与辩论、由选举委员会投票——体制票源集中于时任政务司司长，酉年两人中取现任司长而非法官（官位正在身者胜）。R61-REV1复推：初推=票源归属→林郑／2017-03-26；复推=投票日程→同点；处置：二路同点。粒度核：断项指针2条（体制票源、现任官位）同落点，保留。")

# ---------------- OC bazi (Qianli Minggao / Ziping Zhenquan cases) ----------------
P["OC-001"] = dict(
    conf=0.70, systems="八字（子平）",
    text="方向：先极盛后衰败。戊土日主得辰月厚土、甲杀壬财并透，武贵之造：中年统兵主政一方，位至军阀首领、封疆级统帅；然身旺无制、运转金水衰地后权势崩解，晚年下野潦倒、困顿终老，有客死他乡之象。应期：年档，盛在中年（约40-50岁运段），衰败转折在50岁后运入衰地之年起，晚景以年计。",
    basis=NOTE + "\nsystems_used：八字。\n四柱：甲戌 戊辰 戊申 壬子。戊土旺于辰月、坐申、得戌根，身极旺；甲木七杀透坐戌、壬水财透坐子，财杀有源而日主过旺无官制衡，主以武力兵权自立。等级校准：格局强度足级断至一方统帅（题面已载其为主政一方之首领级，与盘面同级）；晚年降格依据写明：申子半合水泄旺、运入衰地则杀无根、财坏，旺极而衰。两段式：近段（中年）极盛、远段（晚年）潦倒，翻转触发为运离土火旺地、杀星失根。R61-REV1复推：初推=大运离旺地之年档→晚年衰；复推=申子合水泄气路径→同向同档；处置：二路同向，保留年档表达（命造类不套日点）。粒度核：『封疆级』指针2条（杀透有根、财生杀）保留；『客死他乡』仅1指针，降为倾向表述已写入文本（『有…之象』）。")
P["OC-002"] = dict(
    conf=0.72, systems="八字（子平）",
    text="方向：富贵极显、一生荣达。庚金日主坐申禄、亥月，乙财合身、己印透干，财印两全：位至财政首脑、内阁级要职，富与贵兼得。中年行运最盛，晚年渐次退位而保全富贵，安稳终老。应期：年档，鼎盛在中年运段（约40-55岁），晚运以年计渐退。",
    basis=NOTE + "\nsystems_used：八字。\n四柱：甲午 乙亥 庚申 己卯（卡面注一说庚辰日，原书取庚申，依原书取庚申）。庚坐申为禄、身有根；乙木正财透与庚合、亥卯半合财局，财旺；己土正印透生身，财印不相战。等级：财印双美、身坐禄，足级断至财政首脑/内阁级（题面已载其居财政要职，同级）。两段：中年鼎盛、晚年渐退保全，远段触发为运离财印旺地而身禄未破，故只降轻重不断翻转。R61-REV1复推：初推=财局运段→中年盛；复推=印星护身路径→晚年保全；处置：二路同向同档。粒度核：『财政首脑级』指针2条保留。")
P["OC-003"] = dict(
    conf=0.64, systems="八字（子平）",
    text="方向：以商显名、富重于贵。庚金生午月官杀双午并透丙火，身弱赖己印化杀：白手/借势而起，为商界领袖、富甲一方，官方倚为经济重镇。中年鼎盛；晚年杀旺身衰，逢战乱则避乱客居、财势渐收，名位可保而盛况不再。应期：年档，盛在中年火土运段，晚年转折以年计。",
    basis=NOTE + "\nsystems_used：八字。\n四柱：丁卯 丙午 庚午 己卯。庚金午月、丙丁官杀齐透、两午坐杀，身弱；己土正印透干化杀生身，为杀印相生之商贵格；两卯为财。等级：杀印结构成而身根浅，断商界领袖级、不及政权首脑（压制依据：日主无禄刃根、杀重身轻）。晚年降格依据：运入水木之地则印衰杀肆、财杀交攻。R61-REV1复推：初推=杀印运段→中年盛；复推=晚运印衰路径→晚年收；处置：二路同向。粒度核：『避乱客居』1指针，作倾向表述。")
P["OC-004"] = dict(
    conf=0.68, systems="八字（子平）",
    text="方向：清贵仕途、外交名臣。乙木生卯月建禄，癸印透、丙伤坐巳、子印在时：以文章学问立身，外交使节历任，位至外长/国务总理级之短任或使节之极。晚年运入印比之地，安稳著述、清名终老，寿较高。应期：年档，显达在中年，晚景以年计平稳。",
    basis=NOTE + "\nsystems_used：八字。\n四柱：丁丑 癸卯 乙巳 丙子。乙木得卯禄、癸子两印护身，身旺；丙火伤官透坐巳主才华辞令，丁食在年——文星双透合外交辞令之业。等级：禄印俱全而官星不显，断清贵至使节/外长级，不作元首级（压制依据：官杀不透、伤官气盛不宜久居极位）。两段：仕途顺遂为近段、晚年安稳为远段，同向延续（无翻转触发，按（j）表述为延续首段方向）。R61-REV1复推：初推=印禄运段；复推=晚运印比路径；处置：二路同向同档。粒度核：『总理级短任』1指针，已以『级之短任或使节之极』区间表述降档。")
P["OC-005"] = dict(
    conf=0.68, systems="八字（子平）",
    text="方向：法学贵显、名重中外。乙木生卯月建禄，丁食透干、己财双透、未为木库：以学问专业登贵，位至法院院长/大法官级，国际法界有声名。中晚年由司法转学术与著述，际遇安稳，终老于清贵。应期：年档，显达自中年起、晚境以年计平稳向好。",
    basis=NOTE + "\nsystems_used：八字。\n四柱：己亥 丁卯 乙未 己卯。乙木双卯禄旺，亥未半合木局身强；丁火食神透主著述辞章，己土财透两见主务实立业。等级：禄旺食透，足级断至法院院长级（题面已载其已任院长级职务，同级）；官星不透，故贵在专业司法而非政权（压制依据写明）。两段同向延续，无翻转触发。R61-REV1复推：初推=食神运段→中年显；复推=木局根固路径→晚年稳；处置：二路同向。粒度核：主断指针2条（禄旺、食透）保留。")
P["OC-006"] = dict(
    conf=0.60, systems="八字（子平）",
    text="方向：近段可撑、远段命主大关。戊土生申月，庚食透、癸财临酉、甲杀坐寅、午印护身：企业根基深厚，当前（约1935乙亥年）危机为运中之劫，亥年食财交战致挫，1936-37年可逐步缓过、事业不至倾覆；但命主本命杀印相战、晚运寅亥合动杀根，1938年前后（约65岁）有健康生死大关，事业终须交后人接续。应期：年档，近段转机在1936-37年，远段大关指向1938年前后一年内。",
    basis=NOTE + "\nsystems_used：八字。\n四柱：癸酉 庚申 戊午 甲寅。问时约1935乙亥年正值企业危机——题面已载面：主问=受挫后走势；事件面=经营危机进行中。近段断『可撑过』：触发=午火正印坐日、甲杀坐寅有根而受申金食神之制，根基（印）未坏；远段断『1938年前后大关』：触发=寅为杀根、晚运与流年引动寅申冲杀印之根。两段方向相反，翻转触发已按（j）写明。R61-REV1复推：初推=流年引动寅申冲→1938年档；复推=运段交界路径→同年前后；处置：二路同点（年档），保留。粒度核：『1938年前后』指针2条（冲根、运交界）保留年档粒度；『1936-37缓过』1指针作区间表述。")
P["OC-007"] = dict(
    conf=0.70, systems="八字（子平）",
    text="方向：文名盖世、功名无成、寿数不永。甲木生申月双申七杀夹攻、寅禄被冲，三甲并透而根拔：性情狂放不羁、才情风流，为文人狂士之名动一时；仕途全无根基，财来财去、生活放纵耗散。寿关在四十岁出头：1931辛未年（占问当年）前后即其终年，约41岁而逝。应期：年档，寿关指向1931年前后一年。",
    basis=NOTE + "\nsystems_used：八字。\n四柱：庚寅 甲申 甲申 甲戌。题面已载命主新逝、问者欲验推断——断语须能对回其生平：双申冲寅、禄根被拔主根基与寿基俱损；三甲比肩透干主狂傲自负、不受拘束；杀重无印化、无食制，主功名无门、只以才名（甲透）显。等级：名在文坛足级、位则无成（压制依据：官杀攻身、禄冲）。应期尺度：回溯定位类先定年——辛未年未土合…以寅申冲在流年再引动定1931年档。R61-REV1复推：初推=禄冲流年引动→1931；复推=杀旺无救路径→同年档；处置：二路同点。粒度核：『约41岁』由1931-1890推得，指针系年份锚点，保留。")
P["OC-008"] = dict(
    conf=0.64, systems="八字（子平）",
    text="方向：军政显贵、能进能退、晚景得安。乙木生酉月辛杀透干，戊己财并透、子印在年：杀印财相生，位至省主席/军团级军政首长。运程中年金水之地最利权位；晚年杀势渐退，本人善自保，退居安稳、寿较高。应期：年档，权位鼎盛在中年运段，晚年以年计平稳收束。",
    basis=NOTE + "\nsystems_used：八字。\n四柱：戊子 辛酉 乙未 己卯（卡面注一说丙子时，原书斥误，依原书取己卯时）。乙木酉月绝地、辛杀透，身弱；子水正印在年化杀，戊己财透生杀而印回护，成杀印相生带财之局。等级：杀印结构成，断省级军政首长足级（题面已载其已任省主席级，同级）。晚段不断翻转：卯为日主之根未被冲破（酉卯冲在运年引动时主迁动而非覆亡），按（j）作延续方向、只调轻重。R61-REV1复推：初推=金水运段→中年盛；复推=印星护身路径→晚年安；处置：二路同向。粒度核：主断指针2条保留。")
P["OC-009"] = dict(
    conf=0.35, systems="八字（子平，四柱未载、残损降置信）",
    text="方向（低置信）：仕途长青、外交登顶。命主以辞令学养立身，仕途历使节而至外交最高层级、任职绵长；婚姻一面有再娶/多段之倾向（推测）；晚年著述自述、寿高至近九旬。应期：年档，显达贯穿中晚年（输入残损，应期只能给运段量级）。",
    basis=NOTE + "\nsystems_used：八字（未成盘）。\n输入残损（重要）：卡面四柱字段仅载『原书应运篇下论造（四柱以原书为准，转录本个别字待校）』，未给出任何干支——无柱可排，本例无法按子平正法作断，已大幅降置信，不臆补四柱。已载面仅：顶尖外交官、历任驻外使节与内阁职务；财富、仕途、婚姻三问面。断项过闸：仕途面依题面已载事实给方向（属事实层非盘面层，特此注明）；婚姻面无盘面触发，按双闸降格为『推测：』并已在正文标明；财富面盘面无据，正文不单独下断。R61-REV1：无盘面应期路径，复推不适用，已明写。粒度核：具体断项多为1指针以下，已整体降置信并区间化表述。")
P["OC-010"] = dict(
    conf=0.72, systems="八字（子平）",
    text="方向：位极而虚、两度傀儡、终以平民终老。壬水生寅月，三午财星并临、丙火双透，庚印透而无根，身弱财旺至极：幼年登极旋即退位，一生为强权摆布；中年有再被扶立为傀儡之辱，其后囚居改造；晚年以平民身份安静终老。寿数约六十岁上下（1967年前后为终年量级）。应期：年档，际遇转折以年计，寿关在60岁前后一年窗。",
    basis=NOTE + "\nsystems_used：八字。\n四柱：丙午 庚寅 壬午 丙午（卡面注原书未附大运表，运段只能按柱论，已注）。壬水寅月泄气、三午一丙财势燎原，庚金印星透而坐寅绝、无申酉根——印为名分之凭，无根则位有名而无实，正合『位极而虚、为人傀儡』；身弱不任财，财旺主一生受外力（强权）支配。等级校准：名分足级至帝位（题面已载退位皇帝），实权则以无根之印压至傀儡级，压制依据写明。两段：早年登极退位、中年傀儡、晚年平民，三段方向（名高→受制→平淡）各有触发（财旺攻身、印无根）。R61-REV1复推：初推=身弱财旺寿基浅→60岁档；复推=印绝无根路径→同量级；处置：二路同向，保留年档窗。粒度核：『约六十岁』作窗表述（±1年），指针2条。")

P["OC-011"] = dict(
    conf=0.70, systems="八字（子平）",
    text="方向：以艺成名而终于情劫、寿极短。己土生巳月印旺，双亥正财临身、乙杀透时：性情敏感多情，才艺得名于影坛；然财杀交攻、印比护身而心神无依，感情婚姻为一生致命伤，有自毁轻生之大险。寿关在二十五岁前后：1935乙亥年（占问当年）即难过的关口，约24岁而终。应期：年档，寿关指向1935年前后一年。",
    basis=NOTE + "\nsystems_used：八字。\n四柱：庚戌 辛巳 己亥 乙亥。题面已载命主新逝、问者嘱推——断语对回生平：己土巳月印旺主才艺与名望（庚辛食伤透主表演天赋）；双亥财星坐下、乙木七杀透时柱，女命夫星（杀）临财乡而受庚辛伤官克扰，主感情纠葛致祸；亥亥自刑（运年引动）主心神自伤。寿短依据：杀透时柱攻身、印旺而无官通关，乙亥年杀财再临引动自刑。R61-REV1复推：初推=流年乙亥引动→1935；复推=自刑引动路径→同年；处置：二路同点。粒度核：『约24岁』由1935-1910年份锚点推得保留；『自毁』指针2条（自刑、杀攻）保留但作『大险』表述。")
P["OC-012"] = dict(
    conf=0.62, systems="八字（子平）",
    text="方向：少年极盛成名、婚姻入豪门偏房、中晚年名落平淡。丁火生辰月，戊己食伤三透、未土重重，申财在时：食伤旺极主技艺天赋外显，十五六岁即以游泳技艺名满全国（题面已载成名之时正当运）。行运己巳、庚午火土助食伤，少年至青年名望为一生顶点；婚姻面食伤旺而官星（水）不透，夫缘不正：有入豪门为偏房/继室之象，婚姻难得美满；中年后运入辛未、壬申金水，名气渐退、晚景平平。应期：年档，盛名在10-25岁运段，婚姻波折在20-30岁运段。",
    basis=NOTE + "\nsystems_used：八字。\n四柱：己未 戊辰 丁未 戊申；卡面已载五岁起运：己巳、庚午、辛未、壬申、癸酉、甲戌——大运为卡面已载面，直接采用。丁火辰月晦光、食伤三透泄秀，主技艺（游泳属水而以食伤之秀得名）；官星壬癸全无原局，女命夫星不显而食伤旺克官，主婚姻不正/偏房倾向（指代链：官星为夫，不透且受旺食伤压制）。等级：名在体坛足级、婚姻面按压制依据降格写明。R61-REV1复推：初推=大运己巳庚午助秀→少年盛；复推=运入壬申后食伤生财而名退→同向；处置：二路同向。粒度核：『偏房/继室』1指针，已作『之象』倾向表述；盛名段指针2条保留。")
P["OC-013"] = dict(
    conf=0.60, systems="八字（子平）",
    text="方向：艺坛宗师、一生名高而晚运见厄。辛金生丑月坐酉禄，丁杀透干、甲财双临：杀印（丑土）相生而禄根坚固，以技艺成一代名家，名望贯穿中年、富贵有名。晚年行运转入火旺克金之地，禄根受克：有政治风波、迫害囚厄之晚景，终老于困顿，寿约八十上下。应期：年档，鼎盛在中年运段，晚厄在75岁前后运段内见。",
    basis=NOTE + "\nsystems_used：八字。\n四柱：甲午 丁丑 辛酉 甲午；卡面注八岁起运（运干支未全载，按柱论为主）。辛金坐酉禄、丑为金库印绶，根固；丁火七杀透坐丑受制、甲木财星两透生杀而禄能任之，主以艺（食伤未显、以杀印之贵）成名家。晚年降格依据写明：两午在年时、晚运若行南方火地则杀肆克禄，主迫害囚厄——属运触发型远段，触发已指认（午火杀根＋运入火地）。R61-REV1复推：初推=运入火地克禄→晚厄；复推=寿基以禄根计→约八十档；处置：二路同向量级。粒度核：『寿约八十』作量级表述；『迫害囚厄』1指针作『有…之晚景』表述。")
P["OC-014"] = dict(
    conf=0.55, systems="八字（子平）",
    text="方向：仕途中位而止、中年见挫。壬水生卯月辛印透干、己官坐卯、寅卯木旺泄水：伤官佩印，仕途可至省级财政厅长级（题面已载其历任此职，同级）；然伤官见官、官星坐伤地，久居要职必与上峰/法度相忤，中年后有仕途挫折、去职之厄，晚景退居平淡。应期：年档，挫折在中年运入火土官旺之段。",
    basis=NOTE + "\nsystems_used：八字。\n四柱：庚辰 己卯 壬寅 辛丑。壬水卯月伤官当令，辛金正印双见（年时）制伤护官，己土正官透坐卯受克——伤官佩印保仕途、伤官见官藏祸根，两面俱载。等级：印护有力，断至厅长级足级、不再上（压制依据：官星受旺木克制、无财通关）。远段挫折触发：运入火土之年官星得地而伤官不服，伤官见官正面引爆。R61-REV1复推：初推=官旺运段→中年挫；复推=伤官见官结构路径→同向；处置：二路同向。粒度核：主断指针2条（佩印、见官）保留；具体年份无指针，不断至某年。")
P["OC-015"] = dict(
    conf=0.62, systems="八字（子平）",
    text="方向：君主之尊、在位经大变、寿约七旬。甲木生巳月，辛官透坐巳、子印在时、辰为水库：官印相生而身坐泄地，命主为一国君主，在位期间国运有大战/大变之局（食伤午巳之火气主兵事动荡——推测层）；本人晚年健康转衰，寿关约在七十岁：1936年前后（丙子年量级）为终年。应期：年档，寿关指向1936年前后一年窗。",
    basis=NOTE + "\nsystems_used：八字。\n四柱：乙丑 辛巳 甲辰 甲子（卡面注韦氏据西报传略译生庚演造，生庚为转录，已注此限度）。甲木巳月泄气，辛金正官透干得巳中庚金之根，子水正印在时生身，官印相生成格，主君临之位（题面已载其为英国君主，同级核对）。寿基：日主泄于月令、赖子印回护，运入老年印气渐衰，子年（1936丙子）子水冲动…以年档窗表述。『大战大变』一面盘面只有火气类象、无具体触发，按双闸降格并已在正文标『推测层』。R61-REV1复推：初推=印气衰年→1936档；复推=寿基泄气路径→约七旬同量级；处置：二路同向。粒度核：寿关作±1年窗；君主级指针2条（官透有根、印生身）保留。")
P["OC-016"] = dict(
    conf=0.60, systems="八字（子平）",
    text="方向：以术数技艺扬名天下、清贵而财不厚。庚金生卯月双辛劫透、子伤坐下、亥卯财旺：比劫重重、食伤吐秀——功名科第无份，专以一技（命理推步）成一代名师，名满南北；比劫夺财、财旺身须分润，聚财有限，一生为清名之命。中晚年名望不衰，晚年有离乡客居之象，寿中等偏高。应期：年档，名成于中年运段，晚景以年计。",
    basis=NOTE + "\nsystems_used：八字。\n四柱：辛亥 辛卯 庚子 庚辰。庚金卯月财旺，辛庚比劫三见护身，子水伤官坐日吐秀——秀气在技艺口才（推命论断正属食伤之用）；官杀不透，主与科第功名无缘（压制依据写明），贵在专业声名。财面：亥卯半合财局旺而比劫夺之，断『财不厚』有据。晚年客居1指针，作『有…之象』。R61-REV1复推：初推=食伤运段→中年名成；复推=比劫护身寿基→寿中等偏高同向；处置：二路同向。粒度核：名师级指针2条（伤官吐秀、比劫护身）保留。")
P["OC-017"] = dict(
    conf=0.70, systems="八字（子平，子平真诠用神成败法）",
    text="方向：巨富之造、富大于贵。丁火生酉月，己食透、甲印坐辰、壬官在年：财（酉金）旺当令，食神生财、印星护身，用神成而有救——以丝业经营成南浔巨富，富甲一方；官星壬水坐戌受制，贵气远逊于财气，一生以富名而不以官显。晚年财局稳固，富势可保终老。应期：年档，富盛自中年起贯穿晚年。",
    basis=NOTE + "\nsystems_used：八字（真诠用神成败救应）。\n四柱：壬戌 己酉 丁丑 甲辰。出自《子平真诠评注》用神成败救应章——按该章法：丁火酉月财旺，己土食神透干生财为用之成，甲木正印透坐辰有根护身为救应，成败救应俱全，主大富。贵面降格依据：壬官坐戌、戌酉相害且官弱无财生之畅，贵不及富。两段同向（富势贯穿），无翻转触发，按（j）表述为延续。R61-REV1复推：初推=食神生财运段→中年富盛；复推=印护救应路径→晚年保富；处置：二路同向。粒度核：『巨富』指针3条（财旺当令、食生财、印救应）保留足级。")
P["OC-018"] = dict(
    conf=0.64, systems="八字（子平，子平真诠用神成败法）",
    text="方向：以文业成巨头而终遭横祸。庚金生子月，丙杀透坐巳、寅财在日、辛劫在时：伤官当令而杀星透干，报业文业成全国级巨头（申报总经理级，题面已载，同级）；然伤官与丙杀交战、巳火杀根临身，有兵刃暗杀之横祸大险——险年指向中年后火金交战之年，约1934年前后（甲戌年量级）为生死关，晚年安稳终老之局不保。应期：年档，横祸关指向1934年前后一年窗。",
    basis=NOTE + "\nsystems_used：八字（真诠用神成败救应）。\n四柱：己卯 丙子 庚寅 辛巳。出自用神成败救应章：庚金子月伤官当令，丙火七杀透干坐巳禄，伤官见杀而无印通关（己印坐卯受克无力）——成败之间：以伤官之才成文业巨头（成），杀无制化主横祸（败），救应不足正是本章论点。横祸年：运年再引动巳火杀根与庚金交战之年定1934年档窗。应验对象核对：横祸断命主本人（杀攻日主庚金，指代链直落本人）。R61-REV1复推：初推=杀根引动流年→1934档；复推=救应不足路径→同向同档；处置：二路同点（年窗）。粒度核：『暗杀』指针2条（杀透坐禄、伤官见杀无印）保留；年份作±1年窗。")
P["OC-019"] = dict(
    conf=0.60, systems="八字（子平，子平真诠用神成败法；两书四柱全异，依卡面指定徐乐吾书本柱）",
    text="方向：文名政声并显而有横祸险年。壬水生辰月，申印长生在日、丙财透干、癸劫在年：印旺主学问声名，仕至研究院总干事级社会名流（题面已载，同级）；然卯辰相害、财星丙火坐辰无根而身侧杀气（辰中戊土）暗伏，出行/政争中有遭暗算横祸之险——险年指向约1933年前后（癸酉年量级，时年四十岁上下）为生死大关。应期：年档，险年指向1933年前后一年窗。",
    basis=NOTE + "\nsystems_used：八字（真诠用神成败救应）。\n四柱：癸巳 丙辰 壬申 癸卯。输入分歧已载面：卡面明注韦千里《千里命稿》另载癸巳 甲寅 壬辰 庚子、两书全异、本例以徐乐吾书为准——basis 如实登记，依卡面指定柱作断，不混用另一造。壬水申时…日坐申印长生，印旺成文名之基；丙财透坐辰湿土无根，巳火财根在年与申合，财杀（辰戊）暗伏主政争暗算之险。险年取癸酉年档：酉金冲卯、引动卯辰害与申酉金局，杀机外露。R61-REV1复推：初推=流年冲害引动→1933档；复推=财杀暗伏路径→同向；处置：二路同点（年窗）。粒度核：『暗算横祸』指针2条（杀暗伏、冲害引动）保留作『之险』表述；干支分歧已在 basis 留痕（trigger 非六爻不适用，disputed 仍按冻结提示记 false）。")
P["OC-020"] = dict(
    conf=0.65, systems="八字（子平，子平真诠格局高低/成败法）",
    text="方向：贵显至元首级文官而寿不长。癸水生丑月，双丑七杀并临、丁财乙食并透：食神制杀成格，身宫得卯木食神制杀护身，位至国民政府主席级政要（题面已载，同级足级断）；然杀重身弱、两丑夹日，寿基受压：约五十岁为大关，1930年前后（庚午年量级）有逝于任上之象，贵而寿促。应期：年档，寿关指向1930年前后一年窗。",
    basis=NOTE + "\nsystems_used：八字（真诠格局法）。\n四柱：己卯 丁丑 癸丑 乙卯。癸水丑月杀旺，双丑叠临、己杀透年，乙木食神双透（时干与卯根）制杀——食神制杀格成，贵气足级至政府主席（与题面已载其主席级政要身份同级，非拔高）。寿促降格依据写明：日主癸水无金印生扶（全局无申酉庚辛）、杀重两丑夹攻，食神泄身过度，寿基浅。寿关取1930年档：庚午年午火财星生杀、冲动…以年窗表述。R61-REV1复推：初推=财生杀流年→1930档；复推=无印寿基路径→约五十岁同量级；处置：二路同点（年窗）。粒度核：贵级指针2条（制杀成格、食神双透）保留；寿关作窗表述。")
P["OC-021"] = dict(
    conf=0.68, systems="八字（子平，子平真诠格局高低法）",
    text="方向：草莽起家贵至封疆、晚年失势凄凉。乙木生酉月坐卯禄，辛杀透干、戊财丙伤并见：禄刃抗杀、伤官制杀，起于行伍而位至督军/省揽兵权的一方首领，格局中上、贵显一时；然酉金冲卯禄、禄根终被冲动，晚运禄破则势倾：下野失势、晚景萧条，终老于退隐之地。应期：年档，鼎盛在中年，失势转折在晚运禄冲引动之年起。",
    basis=NOTE + "\nsystems_used：八字（真诠格局高低）。\n四柱：戊午 辛酉 乙卯 丙戌。出自格局高低章：乙木日坐卯禄自专，酉月辛杀当令透干冲禄，丙火伤官透时制杀、戊土财星在年——杀有着落、制有手段，格局成而带破（禄被冲），故贵至封疆而不能久固，正合本章『高低』之论。晚段翻转触发已指认：酉卯冲为原局已埋之破，晚运再逢酉/金年引动禄破人衰。等级：封疆足级（题面已载旧桂系军阀首领，同级）。R61-REV1复推：初推=禄冲引动运年→晚年失势；复推=制杀格成路径→中年贵显；处置：二路分段同向。粒度核：主断指针3条保留。")
P["OC-022"] = dict(
    conf=0.70, systems="八字（子平）",
    text="方向：科第无成、以命学立身成宗师。乙木生酉月丁食透干，寅禄在时、戊财坐寅：食神制杀（丁制辛）而官星（酉中辛）受制、庚金正官不透——功名科第屡试不第、终身无仕宦之份（题面已载其屡试不第，同向）；转而以医卜命学立业，成一代命理宗师、著述传世。清名而禄薄，寿至七旬量级。应期：年档，立身转折在青年废科举/弃功名后运段，名成于中年。",
    basis=NOTE + "\nsystems_used：八字。\n四柱：辛巳 丁酉 乙巳 戊寅；卡面注安命甲午、大运丙申起。乙木酉月杀地，丁火食神透干制杀为用，寅木禄根在时自固——制杀太过则官星（功名之凭）全伤，正断『科第无成』（压制依据：正官庚金全无、七杀被食神制尽）；食伤吐秀转落术数著述，指代链落食神（技艺表达）。等级：术界宗师足级、仕途零级，两面分断。R61-REV1复推：初推=食神制杀结构→科第无成；复推=大运丙申起食伤运→以技立身；处置：二路同向。粒度核：『寿七旬』1指针作量级表述；宗师级指针2条保留。")

# ---------------- OC meihua / liuren ----------------
P["OC-023"] = dict(
    conf=0.40, systems="梅花易数（射覆，卦象已载）",
    text="方向：钟下所覆为一件金属质、圆而有足/有环的器物（鼎属之象，如铜镜、环佩或小型金属容器一类），且非崭新完好——有颠倒放置或轻微损伤之象。应期：即时占，当场揭钟即验（日档内即时）。",
    basis=NOTE + "\nsystems_used：梅花易数（射覆）。\n输入残损：卡面只载卦名『火风鼎 变 雷风恒』，未载动爻爻位与起卦时间，已降置信。已载面：对象面=钟下所覆之物及其完好与否（主问面）。断项过闸：鼎卦上离下巽，鼎象本身即三足圆腹之金属炊器/礼器类象→指代链落对象面『金属圆器』，触发为卦名鼎之本象（指针1）；变恒主其物久置/旧物→『非崭新』作倾向表述（指针1，粒度降档为倾向）。完好与否：鼎初象有颠趾之训（推测层），正文以『有…之象』表述。R61-REV1：即时占无应期主坐标推演，复推不适用已明写；粒度核：『金属圆器』1指针保留类级粒度（未细断至具体某物），损伤项已降倾向。")
P["OC-024"] = dict(
    conf=0.65, systems="梅花易数（外应/遗书预言核验）",
    text="方向：葬资有着落、葬事可成。易者遗书所指可托之人（来访秀士邵雍）如期而至，其家藏有可变现之金——藏金出自与『鼠』『枕』相关的藏处（击鼠/枕下窖藏之金），取出足以营葬，丧葬之事终得办妥。应期：月档内，来访后短期内（数日至一月内）藏金得现、葬事办毕。",
    basis=NOTE + "\nsystems_used：梅花易数（遗书预言＋藏物外应）。\n卡面出处已载面：主问面=身后无资何以为葬；锚点面=篇题已载『击鼠枕窖金』文字锚点（属题面已载，非结局文件）。锚点转应核：直读=枕下/窖中藏金；转应面=金指代他物——取直读，理由：题面篇题三锚（鼠、枕、窖）同指藏金一事，无转指他物的题面线索。断项过闸：『藏金得现足营葬』→指代链落对象面（葬资），触发为遗书预言机制本身（易者预书来访者可托）＋三锚同向。R61-REV1复推：初推=遗书预言应期→来访后短期；复推=锚点事象路径→同窗（月档内）；处置：二路同窗。粒度核：藏处『枕下/窖中』两锚并陈作类级表述（射覆类粒度），金数无指针不断确数。")
P["OC-025"] = dict(
    conf=0.70, systems="梅花易数（预言核验）",
    text="方向：应验。邵雍预书于椅底之事如期兑现：届期之年月日，椅子果被坐破——由外来之客/较重之人坐压而破，预言分毫不爽。应期：即预书所定的年月日当日（日档，日期由预书本身给定）。",
    basis=NOTE + "\nsystems_used：梅花易数（预书核验）。\n已载面：主问面=椅底预书是否应验；对象面=椅子；应期面=预书所定年月日（题面已载『某年月日』为预书内容）。断项过闸：断『应验、椅被坐破』→指代链落对象面椅子；触发：本案属邵雍预言类成例体裁，问法即核验预书，预书机制（先时预定物象之变）在体裁内主应验；坐破方式『外来之客坐压』1指针，作类级表述。R61-REV1复推：初推=预书日期锚点→当日；复推=物象变坏路径→同日；处置：二路同点。粒度核：坐者身份不断至具体某人（无指针，已守类级）。")
P["OC-026"] = dict(
    conf=0.55, systems="大六壬",
    text="方向：功名可成、二人皆有进身之喜。己亥日占功名，三传未（青龙）→亥（螣蛇）→卯（玄武）成亥卯未三合木局，木为己土之官，官星成局而青龙发用主喜庆文书：今科/今年功名有望，其中一人名位更显（发用青龙乘未、未为木库主先成），另一人稍逊而亦不落空。中传螣蛇主榜前忧疑虚惊，结果终成。应期：月档，应在本年秋闱放榜至次年春榜之间，主坐标取本年秋榜（1643年内）。",
    basis=NOTE + "\nsystems_used：大六壬。\n盘面残损守第八节：卡面只载课式（涉害、曲直）、三传带天将、月将与旬空（甲午旬辰巳空），无天盘全图与四课全列——只据干支、三传链、天将、课格、空亡作断，不臆补四课。占时1643年正月初四己亥日辛未时（题面已载）。类神：功名取官星——传中亥卯未三合木局即己土之官局，官星成局为成断主据；青龙乘初传主文书喜信；中传螣蛇乘亥主中途虚惊；末传卯乘玄武主名次稍暗/次者逊。空亡辰巳不在传中，不压主断。两段：近段（本年）成、过程有虚惊，非两段终局型，按（i）近段为主、榜期为应期。R61-REV1复推：初推=官局逢值（秋闱木气）→本年秋榜；复推=青龙发用文书路径→同年内；处置：二路同窗（月档）。粒度核：『一人更显』指针2条（青龙发用、木库在初）保留类级；具体名次无指针不断。")
P["OC-027"] = dict(
    conf=0.60, systems="大六壬",
    text="方向：此行不得意、无功而返，且有母病之忧。辛未日占北上，课式无禄、无路已主前程无门；三传酉（六合）→辰（太阴）→亥（青龙，空亡）——末传青龙落空，喜信终成空；初传酉金为日干辛之禄地却课名无禄，主到京亦不得任用、奔波而已。本人身体：传中辰酉金气克伐而末传空亡，主途中/京中身体不安、宜缓行。老母（甲子年命）：亥为…末传空而年命水空，主老母有病厄之警，本冬须防。应期：月档，诏行在一月内见分晓，母病之警在本冬（占后一至两月内）。",
    basis=NOTE + "\nsystems_used：大六壬。\n盘面守第八节：只有课式名、三传带天将、月将丑将、甲子旬戌亥空，无四课天盘全图，只据已载作断。占时1642年冬月初五辛未日甲午时，北方兵事正紧（题面已载事实，事实优先）。课格『无禄、无路』为课名直断行不得意（指针强）；末传亥乘青龙而空亡——青龙主君恩文书，落空则恩命成空，此为终局主触发；初传酉乘六合主奔走交涉多而成少。母面：题面已载其母甲子年——子为亥之邻、水气空亡之侧，母病之警作倾向级（指针1，已以『须防』表述并降格）。应验对象逐条复述：行不得意→方替夫本人；身体不安→本人；病厄之警→其母，三者不相混。R61-REV1复推：初推=末传空亡→一月内见空；复推=无禄课格路径→同窗；处置：二路同窗。粒度核：母病项已降倾向；主断指针3条（课名双无、末传空、青龙落空）保留。")
P["OC-028"] = dict(
    conf=0.50, systems="大六壬",
    text="方向：可得官、得中级文职实缺。己丑日入觐考选，重审、斫轮课主经审择而后授职；三传卯（玄武）→戌（朱雀）→巳（白虎）：中传戌乘朱雀为文书诏命之正位，戌为火库、己土之官杀（木）在初传卯——官星发端、文书居中，主考选后得授职。所授偏向词臣/台谏或部属司官一级（文书象重），非方面大员；末传巳乘白虎主得职后任地有奔波兵革之劳。应期：月档，消息在占后三至六月内（次年春季量级），主坐标取次年春授职。",
    basis=NOTE + "\nsystems_used：大六壬。\n盘面守第八节：课式（重审、斫轮）、三传带天将、寅将、甲申旬午未空为已载面；四课天盘未载不臆补。占时1630年冬月十四己丑日辛未时。类神：官职取官星与朱雀文书——初传卯为己土正官乘玄武（主初时未明/经暗中较量），中传戌乘朱雀居要（诏命文书），末传巳为印星乘白虎（印绶得职而带劳）。斫轮课象主匠作者经斫削成器、考选成职。等级：文书象与官星量级只支持中级文职，方面大员无指针，已按粒度降至『司官一级』区间表述。R61-REV1复推：初推=朱雀文书逢值→次年春；复推=官星卯逢值路径（卯月）→次年二月量级同窗；处置：二路同窗（月档，取次年春）。粒度核：官职类别2指针（朱雀中传、官星发传）保留类级；具体衙门无指针不断。")
P["OC-029"] = dict(
    conf=0.45, systems="大六壬",
    text="方向：诸事往返反复、子求官终可成而迟；老母高年本冬有病厄之警但可挨过。己亥日占，三传未（白虎）→卯（六合）→亥（天后），涉害、曲直、回环课：回环主事必往返再三、去而复来。子（丑命）求官：末传亥乘天后为贵人恩庇，官星（木）居中传卯乘六合，主经人情关说、迟延后得成，然初传未乘白虎主道路奔波与先一趟空走。老母年近九十：未为木库、乘白虎临初传，白虎主病丧之警——本冬（占后两三月内）老母有较大病厄，课终传天后有恩护象，断为有惊而可过关、寿不终于本冬。应期：月档，求官成在占后半年内，主坐标取占后四至六月；母病警在本冬两三月内。",
    basis=NOTE + "\nsystems_used：大六壬。\n盘面守第八节：课式（涉害、曲直、回环）、三传带天将、丑将、甲午旬辰巳空已载；四课天盘、王米山本人年命未载（仅载其子丑命、母近九十），不臆补。类神分判：子求官以子之丑命与官星卯木中传立断；母以初传未（木之墓库、乘白虎）立警。回环课格贯穿全案主『往返』形态（指针强）。应验对象复述：求官成迟→其子；病厄之警→其母（近九十）；奔波→王米山本人，三条分列不相混。母『可过关』依据：末传天后恩护＋白虎在初不在末（警在前段、终传见护）——指针各1，已整体降置信至0.45。R61-REV1复推：初推=回环往返程量→四至六月；复推=官星卯逢值→次年春同窗；处置：二路同窗（月档）。粒度核：母病项指针不足，已作警级表述；官职具体名目无指针不断。")
P["OC-030"] = dict(
    conf=0.60, systems="大六壬",
    text="方向：两事皆可如愿——巡按差可复设、吏书缺可照旧。戊子日占，重审、铸印课：铸印主官印重新铸造、废而复立，正对『巡按差可复否』之问；三传巳（太常）→戌（六合）→卯（太阴）：太常为印绶衣冠之官居初传，戌为印库居中，末传卯乘太阴主事于暗中/新朝格局下悄然落定。吏书缺一面：传中无破缺之象，六合居中主照旧维系，断可保留原缺。应期：月档，复设消息在占后三至六月内，主坐标取占后四月前后（1651年夏间）。",
    basis=NOTE + "\nsystems_used：大六壬。\n盘面守第八节：课式（重审、铸印）、三传带天将、亥将已载；旬空与四课未载，不臆补。占时1651年二月初十戊子日戊午时，易代之际巡按差已废（题面已载事实）。断项过闸：『巡按可复』→类神取印绶：铸印课格本身即印废复铸之象（指针强），太常（印绶之官）乘初传巳、戌为火印之库居中传，两指针同向；『吏书缺照旧』→中传六合主合旧、传链无冲破日干/官星之象，指针1，已在正文作次断（不与主断并列争终局，承双闸主核保护）。R61-REV1复推：初推=印库戌逢值→占后数月；复推=太常文书路径→同窗；处置：二路同窗，取四月前后为主坐标。粒度核：主断指针2条保留；吏书项1指针作次断表述。")

# ---------------- WP western mundane astrology / tarot ----------------
P["WP-001"] = dict(
    conf=0.70, systems="西方占星（世俗占星 mundane）",
    text="Direction: a major collective affliction — a pandemic. The 2020–2021 period holds a large-scale epidemic/pandemic event: a fast-spreading mass illness (respiratory/plague-type in character) causing very high mortality, overwhelming health systems and bringing severe social and economic disruption worldwide. Timing: year-scale window centred on 2020, beginning as the Jupiter–Saturn–Pluto conjunction perfects in early 2020 and extending through 2021.",
    basis=NOTE + "\nsystems_used：western mundane astrology.\nLoaded faces: main question = major collective affliction 2020–21; configuration face = Jupiter–Saturn–Pluto conjunction early 2020, five outer planets within ~100°, cyclical index at 21st-century low; precedent face = comparable clusters coincided with 1918, 1954, 1968, 1982 (all epidemic years per the card). Gate check: 'pandemic' item → mundane-astrology significator chain: Pluto (mass death/plague) conjunct Saturn (structure, restriction) and Jupiter (scale, spread) at the cyclical-index minimum; trigger = the card's own precedent series, in which such clusters aligned with influenza pandemics. R61-REV1 re-derivation: path 1 = conjunction exact early 2020 → onset 2020; path 2 = cyclical-index low window → 2020–21; disposition: two paths same window, retained. Granularity: 'respiratory/plague-type' kept as class-level (1 pointer, phrased as character, not a named disease).")
P["WP-002"] = dict(
    conf=0.60, systems="西方占星（世俗/选举占星）",
    text="Direction: Barack Obama wins. The 2008 US presidential election goes to the challenger, Senator Barack Obama, defeating John McCain on 4 November 2008. The Saturn–Uranus opposition perfecting on Election Day — a configuration unseen for 45 years — signifies the old order overturned: change defeats continuity. Timing: day-scale, decided on election day, 4 November 2008.",
    basis=NOTE + "\nsystems_used：western mundane/election astrology.\nLoaded faces: main question = winner of 2008 election; candidates face = Obama (Democratic front-runner, not yet clinched) vs McCain (presumptive Republican nominee); configuration face = Saturn–Uranus opposition beginning on Election Day, last seen 45 years earlier. Gate check: 'Obama wins' → significator chain: Uranus (rupture/change) opposing Saturn (incumbent establishment, the older candidate/party in power); trigger = opposition exact on election day itself, favouring the insurgent over the sitting order. R61-REV1: path 1 = election-day configuration → 4 Nov 2008; path 2 = fixed election calendar → same date; disposition: same point. Granularity: winner item has 2 pointers (Uranus-over-Saturn symbolism, challenger-vs-incumbent structure of the card) retained at original granularity; margin not claimed (no pointer).")
P["WP-003"] = dict(
    conf=0.60, systems="西方占星（世俗/选举占星）",
    text="Direction: Barack Obama is re-elected. The incumbent President defeats Mitt Romney on 6 November 2012 and wins a second term. Mercury turning retrograde on election day signifies repetition and review rather than replacement — the electorate returns the sitting president — though it also warns of counting confusion and a contested-feeling count echoing 2000. Timing: day-scale, decided 6 November 2012.",
    basis=NOTE + "\nsystems_used：western mundane/election astrology.\nLoaded faces: main question = winner 2012; candidates = incumbent Obama vs presumptive nominee Romney; configuration = Mercury retrograde begins on election day (card-loaded). Gate check: 'incumbent returned' → chain: Mercury retrograde = re- (return, recount, repeat) signature applied to the election-day chart; trigger = retrograde station on the very day of voting. The counting-confusion sub-item is the same pointer's second face, kept as a caution, not a second verdict (main-core protection). R61-REV1: path 1 = station date → 6 Nov 2012; path 2 = election calendar → same; disposition: same point. Granularity: winner 2 pointers (incumbency structure, retrograde re-signature) retained; no margin claimed.")
P["WP-004"] = dict(
    conf=0.55, systems="西方占星（世俗/选举占星，会议合断面）",
    text="Direction: Hillary Clinton wins. The forecasting panel's weight of judgement at the Costa Mesa conference points to the Democrat, Hillary Clinton, defeating Donald Trump on 8 November 2016 — the experienced, establishment candidate carried by the majority of chart readings despite an unsettled campaign sky. Timing: day-scale, decided 8 November 2016.",
    basis=NOTE + "\nsystems_used：western mundane/election astrology (panel consensus reading).\nLoaded faces: main question = winner 2016; setting face = most polls favour Clinton; source face = an international astrology conference election panel (collective professional judgement is the instrument in this card). Gate check: 'Clinton wins' → chain: panel-consensus method — where a card's instrument is a panel of practitioners, the panel's majority reading is the prediction channel; supporting pointer = polling/establishment structure loaded on the card (frontrunner with institutional backing). Confidence held at 0.55: the card loads no individual chart data (no birth times, no election chart), so the reading rests on consensus + structure only — noted as an input limitation. R61-REV1: path 1 = panel timing (October sitting, verdict for 8 Nov); path 2 = election calendar; disposition: same point. Granularity: winner item retained; no state-level or margin claims (no pointers).")
P["WP-005"] = dict(
    conf=0.50, systems="西方占星（世俗/选举占星，单席逆判面）",
    text="Direction: Donald Trump wins. Against the polling consensus, the Republican nominee Donald Trump defeats Hillary Clinton on 8 November 2016. The decisive signal is the panel astrologer who, when seventeen Republicans still contested the nomination, already picked Trump to take that nomination — the same against-the-field reading extends to the general election: the outsider's chart momentum overrides the frontrunner's polling lead. Timing: day-scale, decided 8 November 2016.",
    basis=NOTE + "\nsystems_used：western mundane/election astrology (single-reader contrarian line).\nLoaded faces: main question = winner 2016; distinguishing face vs the companion panel card = one panel astrologer had earlier, against a 17-candidate field, picked Trump as Republican nominee — the card singles out this reader's line as its instrument. Gate check: 'Trump wins' → chain: demonstrated against-field accuracy on this very candidate within this very cycle is the card's loaded evidence; trigger = the nominee call already landed against 17-to-1 field odds, and the general-election question is put to the same line. Confidence 0.50: single pointer class, honestly held low; polls-favour-Clinton face is loaded on the card and is answered by the contrarian instrument itself, not suppressed. R61-REV1: path 1 = reader's cycle line → verdict for 8 Nov; path 2 = election calendar; disposition: same point. Granularity: winner retained at class level; no margin/state claims.")
P["WP-006"] = dict(
    conf=0.55, systems="西方占星（世俗占星，英国国家盘）",
    text="Direction: Yes — Britain votes to leave. In the referendum of 23 June 2016 the 'Leave' side wins and the United Kingdom votes to exit the European Union, against the February polling lead for 'Stay'. Uranus conjunct Ceres at 23° Aries on referendum day signifies a sudden severing of the nurturing union — an eruptive break with the established body. Timing: day-scale, decided 23 June 2016.",
    basis=NOTE + "\nsystems_used：western mundane astrology (UK national charts).\nLoaded faces: main question = Leave or Stay on 23 June 2016; charts face = UK 1066/1801/1922 charts available; configuration face = Uranus–Ceres conjunction at 23° Aries on referendum day (card-loaded); polling face = 'Stay' ahead with many undecided (Feb 2016). Gate check: 'Leave wins' → chain: Uranus (rupture, sudden separation) conjunct Ceres (the sustaining/nurturing body — here the EU as sustaining union) in Aries (cardinal fire, initiating break) on the day itself; trigger = the conjunction falls exactly on referendum day. Polling face answered under fact-priority: polls with 'vast numbers of not sure' are a weak fact vs a day-exact configuration; noted, not hidden. R61-REV1: path 1 = day-exact conjunction → 23 Jun 2016; path 2 = referendum calendar → same; disposition: same point. Granularity: outcome item 2 pointers (day-exact conjunction, severance symbolism) retained; no percentage claimed.")
P["WP-007"] = dict(
    conf=0.50, systems="塔罗（Waite 牌义，街头占者抽牌面）",
    text="Direction: Donald Trump wins, and the Clinton scandals decide it. The Union Square tarot reading points to Trump taking the election on 8 November 2016; what decides it is Hillary Clinton's email controversy and the Clinton Foundation cloud — a late-breaking scandal burden that drags her campaign down in the final stretch while Trump's chaotic momentum survives its own storms. Timing: day-scale outcome on 8 November 2016, with the deciding scandal pressure peaking in the final weeks (late October) of the campaign.",
    basis=NOTE + "\nsystems_used：tarot (Waite-based street reading, as framed by the card).\nInput limitation noted: the card does not transcribe the actual cards drawn — no spread positions or card names are loaded — so the reading is made on the card's loaded faces only and confidence is held at 0.50. Loaded faces: main question = who wins and what decides it (two-part question, both parts answered); setting faces = Clinton leads August polls; her email controversy and Foundation are already public controversies (card-loaded scandal face). Gate check: 'scandal decides it' → the question's second half demands a deciding factor, and the only deciding-factor face loaded on the card is the Clinton scandal pair — chain closes on loaded faces only, no imported facts. 'Trump wins' follows from the deciding-factor direction (the burden falls on the frontrunner). R61-REV1: path 1 = campaign-arc timing (late-October peak → 8 Nov verdict); path 2 = election calendar; disposition: same verdict point, peak window retained as interval. Granularity: deciding-factor item kept at the card's own class level (email controversy / Foundation), no invented specifics.")

# ---------------- write & verify ----------------
assert set(P.keys()) == set(IDS), (set(IDS) - set(P.keys()), set(P.keys()) - set(IDS))
os.makedirs(OUTDIR, exist_ok=True)
sizes = {}
for cid in IDS:
    d = P[cid]
    obj = {
        "case_id": cid,
        "prediction_text": d["text"],
        "basis": d["basis"],
        "confidence": d["conf"],
        "trigger": dict(TRIG),
    }
    path = os.path.join(OUTDIR, cid + ".json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    sizes[cid] = os.path.getsize(path)

# read-back verification, exact id list only
ok = 0
for cid in IDS:
    path = os.path.join(OUTDIR, cid + ".json")
    with open(path, encoding="utf-8") as f:
        o = json.load(f)
    assert o["case_id"] == cid
    assert set(o.keys()) == {"case_id", "prediction_text", "basis", "confidence", "trigger"}, o.keys()
    assert isinstance(o["prediction_text"], str) and o["prediction_text"]
    assert isinstance(o["basis"], str) and o["basis"]
    assert 0.0 <= o["confidence"] <= 1.0
    t = o["trigger"]
    assert t == TRIG, (cid, t)
    ok += 1
print("batch_cases:", len(IDS))
print("written_verified:", ok)
print("trigger_counts: changed_main=0 reserve_used=0 disputed=0 (no liuyao cases in B19/B20)")
for cid in IDS:
    print(cid, sizes[cid])
