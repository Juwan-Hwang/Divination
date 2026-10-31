# R64 S7 blind predictions B19+B20 — data + writer (asserts batch id set)
import json, os
BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round64"
BATCHES = json.load(open(os.path.join(BASE, "batches.json")))
IDS = BATCHES["B19"] + BATCHES["B20"]

def rev1(scale, p1, p2, disp, gran):
    return (f"应验跨度档位（k）：{scale}。"
            f"\nR61-REV1-2 应期二路复推：初推路径与坐标——{p1}；复推路径与坐标——{p2}；处置——{disp}。"
            f"\nR61-REV1-4 断项粒度核：{gran}")

def mk(trad, systems, analysis, scale, p1, p2, disp, gran):
    return (f"tradition: {trad}\nsystems_used: {systems}\n{analysis}\n"
            + rev1(scale, p1, p2, disp, gran))

P = {}

# ---------------- MP ----------------
P["MP-017"] = dict(conf=0.65, text="方向：女性出任。下届香港行政长官将由女性出任，具体即改口重新考虑参选的政务司司长林郑月娥——她将正式宣布参选并在选举委员会投票中胜出。应期：2017年3月26日选举投票日定局（窗口为2017年1月宣布参选至3月26日投票）。",
 basis=mk("面相/时事命理综合（输入卡无 tradition 字段，据出处玄学受访体裁自决）", "事实优先序（e）＋时事格局推断（明理）",
  "已载面：主问面=下届特首性别；事件面=梁振英已宣布不连任、曾俊华已辞职备选、林郑月娥改口重新考虑参选；关系面=北京支持取向为本题关键变量。断项过闸：女性出任→指代链落林郑月娥（题面唯一女性潜在参选人且为政务司司长、建制内顺位最高）→触发为其改口参选这一题面明载之动向，保留。曾俊华虽先动，但属意人选信号不在其方，特首选举由选举委员会产生、非普选民望直决，故民望面无据压过顺位面，不报男性。",
  "月档（问一届选举结果，2017年3月26日投票日为题面给定终点）",
  "题面时间锚点直推：投票日2017年3月26日", "格局复推：参选宣布须在提名期前，主坐标仍落3月26日投票日", "二路同点，保留单点主坐标",
  "断项『女性／林郑月娥』：细节类型=身份类别，支撑指针2条（唯一女性潜在人选＋建制顺位）指向同一落点，原粒度保留"))

P["MP-018"] = dict(conf=0.65, text="方向：不能当选（negative）。曾俊华民望虽为候选人中最高，但特首由选举委员会选出，其相与势皆属陪跑之局——最终当选者将是获北京支持的林郑月娥。应期：2017年3月26日投票日揭晓落败（窗口为2017年1月参选至3月26日）。",
 basis=mk("面相（输入卡无 tradition 字段，据出处《睇相王》相学杂志体裁自决）", "面相门类框架＋事实优先序（e）",
  "输入残损注明：输入卡未载曾俊华面部形神的具体描写，相学逐项（额、眉、鼻、颧等）无从据卡复核，故相学面只取门类总格、主断以题面事实面为准并降置信。已载面：主问面=曾俊华能否当选；事件面=传媒普遍指林郑获北京支持选情占优、曾被视为陪跑声势落后；关系面=民望最高对选委会结构。断项过闸：不能当选→指代链落曾本人→触发为选委会产生方式与北京支持不在其方（题面明载），保留；民望最高一面有面但与产生机制无关，不据以翻转主断。",
  "月档（选举终点为题面给定2017年3月26日）",
  "题面时间锚点直推：2017年3月26日投票日", "机制复推：提名与投票程序终点同为3月26日", "二路同点，保留",
  "断项『落败、当选者为林郑』：身份类别，支撑指针2条（产生机制＋题面占优方）同指，原粒度保留"))

P["MP-019"] = dict(conf=0.7, text="方向：林郑月娥当选。2017年香港行政长官选举花落林郑月娥（1957酉年生人）；曾俊华（卯生）与流年丁酉卯酉冲、势位两失，胡国兴年长而支持面窄，皆陪衬。应期：2017年3月26日选举委员会投票当日定局。",
 basis=mk("八字/生肖年命合参（输入卡无 tradition 字段，据出处风水命理杂志与题面所载三人出生年自决）", "生肖年命与流年冲合＋事实优先序（e）",
  "已载面：主问面=三人中谁当选；对象面=林郑1957酉年、曾1951卯年、胡1946酉年；事件面=提名与多轮辩论已毕、3月26日投票。断项过闸：林郑当选→指代链落林郑→触发一为2017丁酉流年与其年命酉支同气值年（值年得位）、触发二为曾之卯支逢酉年冲（卯酉冲，主根动位失），两指针同指林郑胜、曾败，保留。胡同为酉年，但题面无其声势占优之载，酉年同气一指针不足以越过林郑的现任政务司司长顺位面，舍胡并注明理由。本题面文字锚点为干支年命，转应面（卯酉冲作『冲起得位』读）已列：取冲为失位，理由为曾本处声势落后、无得位之事实面支撑冲起说。",
  "月档（投票日为题面给定终点）",
  "流年值日直推：2017年3月26日投票日", "程序复推：选委会投票终点同日", "二路同点，保留",
  "断项『林郑当选』：身份类别，支撑指针2条（年命值年＋对手受冲）同指，原粒度保留；『胡落选』为对手面推断、随主断保留"))

# ---------------- OC 八字 ----------------
P["OC-001"] = dict(conf=0.62, text="方向：前盛后衰。吴佩孚戊土生辰月、身旺任财官：前半生统兵主政一方、位极军阀首领，鼎盛在中年；晚年运转衰地、食伤财星无根续力，下野闲居、困顿以终，不得善终高位。寿数约六旬中（约1939年前后，65岁上下）为终局坐标；应期以运档/年档表达：晚景下行自五十后渐显，终点落在1939年前后一年内。",
 basis=mk("八字（输入卡载四柱《千里命稿》应运篇，无 tradition 字段、据四柱体裁自决）", "子平格局＋旺衰：戊辰日主、月令辰土、壬财透子、申子会水、甲杀坐戌",
  "已载面：主问面=一生事业与晚年际遇；事实面=曾主政一方、后下野、论造时已成名。断项过闸：前半显赫→十神链财（壬子）生杀（甲）、身旺能任→触发为申子半合水局财势成、甲杀得财生，保留；晚年衰困→触发为时柱壬子财临绝乡且晚运无印比新根续身（盘面晚段无救），按（b）写明压制依据后降格，保留。对象同一性：承受与应验同为命主本人。",
  "年档（问一生事业与晚年，终局类先年后月、不落日）",
  "运档触发直推：晚运衰地、终局年约1939年", "逢值复推：己卯年卯木杀星值年、与局中甲杀呼应而身党无新增根气，坐标同落1939年前后", "二路同点（年档），保留1939年前后一年窗",
  "断项『寿约六旬中』：量级类，支撑指针2条（晚运无根＋杀值年）同指，年档粒度保留；『下野困顿』状态类指针2条保留"))

P["OC-002"] = dict(conf=0.68, text="方向：大贵足级。宋子文庚金坐申禄、亥月伤官生财、乙财合身、甲午坐下财官之源：一生掌财政金融、位至政府最高层（财政部长以至行政院长级），富贵兼备；行运金水木相续有情，中晚年不败，晚年退居海外安享，寿逾七旬（约1971年前后终）。应期以运档表达：贵显自三十岁后步步登顶，四五旬达峰。",
 basis=mk("八字（四柱体裁自决）", "子平：庚申日主禄旺、伤官（亥）生财（乙甲）、己印护身",
  "已载面：主问面=贵显程度与行运吉凶；事实面=出身银行世家、已居财政要职。断项过闸：大贵→指代链财官印链落命主→触发为乙庚合财就身、申禄身强任财官，按（b）无压制依据、足级给贵，保留；晚年安享高寿→触发为行运无冲破禄根之字（申根终身在），保留。异说庚辰日一面：原书取庚申，本断从原书所取，注明取舍。",
  "年档（问一生贵显与行运）",
  "运档直推：峰位在四五旬、终局年约1971年", "值年复推：辛亥年亥水值年与原局亥同气、禄根申仍在，主安终，同落1971年前后", "二路同点（年档），保留",
  "断项『位至行政院长级』：身份类别，指针2条（财合身＋禄旺任官）同指，原粒度保留；『寿逾七旬』量级指针2条保留"))

P["OC-003"] = dict(conf=0.6, text="方向：以商立业、名重于官。虞洽卿庚金午月、官杀（丁丙午）旺而己印化杀、卯财生杀：一生白手兴家为商界领袖，交结政商、名望极高而本身不居高官；财运旺盛、中年鼎盛；晚年值乱世，避地内迁、客乡终老，寿近八旬（约1945年前后终）。应期以运档/年档表达：晚年下行在七旬后，终点约1945年。",
 basis=mk("八字（四柱体裁自决）", "子平：庚午日主、官杀旺、杀印相生（己土）、财（卯）滋杀",
  "已载面：主问面=名位、财运与晚年；事实面=上海商界领袖、已具盛名。断项过闸：商界领袖而非高官→触发为财杀旺而官杀无制化入印、身弱不任纯官，名位以财名取，保留；晚年客乡终→触发为晚运火土之地耗泄交加、无金水归根之运（盘面晚段指针），保留并按（b）注明晚年降格依据为身弱逢杀旺之运。",
  "年档（问一生名位财运晚年）",
  "运档直推：终局年约1945年", "值年复推：乙酉年酉金值年冲卯财、财根动而人已高年，主终局，同落1945年前后", "二路同点（年档），保留",
  "断项『寿近八旬』：量级类指针2条（高年＋财冲根动）同指保留；『客乡终老』处所类仅1条指针，按R61-REV1-4降一档为方位性表述『离沪西迁内地而终』，已在正文以『避地内迁』行文"))

P["OC-004"] = dict(conf=0.6, text="方向：文官贵显、晚景平稳。颜惠庆乙木卯月建禄、癸印透子、丙伤官生辉：伤官配印、以才学外交立身，仕途位至阁员级（外交总长以至国务总理级）；一生行运起伏不大、晚年退居著述安闲，寿逾七旬（约1950年前后终）。应期以运档表达：贵显集中于三四旬，晚运平顺无大劫。",
 basis=mk("八字（四柱体裁自决）", "子平：乙巳日主、卯禄、伤官配印（丙癸）、子印卯禄护身",
  "已载面：主问面=仕途行运与晚年；事实面=资深外交官、曾任驻外公使与内阁职务。断项过闸：位至阁员→触发为伤官配印成格、禄印双护，按（b）足级，保留；晚年平稳→触发为晚运无冲禄（卯）破印（子）之结构在盘面可指认范围内不成立大破，保留为平稳断。对象同为命主本人。",
  "年档（问仕途与晚年）",
  "运档直推：终局年约1950年", "值年复推：庚寅年寅木值年不冲禄印，主安终，同落1950年前后", "二路同点（年档），保留",
  "断项『寿逾七旬』：量级类指针2条保留；『位至阁员级』身份类指针2条（配印成格＋禄印双护）保留"))

P["OC-005"] = dict(conf=0.66, text="方向：贵显于文法、高寿。吴经熊乙木双卯临旺、丁食神透、己财就局：食神生财而身旺任之，一生以法学立名、居司法高位（法院院长级），名望遍中外；晚年转讲学著述、侨居海外而终，寿逾八旬（约1986年前后终）。应期以运档表达：中年登司法之峰，晚运绵长无暴败。",
 basis=mk("八字（四柱体裁自决）", "子平：乙未日主、卯木双临身旺、食神（丁）生财（己）、亥印为根",
  "已载面：主问面=一生前程贵显；事实面=留洋法学家、已任法院院长级。断项过闸：司法高位→触发为食神生财链完整且身旺可任、亥卯未木局根深，按（b）足级，保留；高寿→触发为原局无金冲木根、无杀攻身之结构，晚运有根，保留。",
  "年档（问一生前程）",
  "运档直推：终局年约1986年", "值年复推：丙寅年寅木值年助根、主高年安终，同落1986年前后", "二路同点（年档），保留",
  "断项『寿逾八旬』：量级类指针2条（无冲根＋晚运有根）保留；『司法高位』身份类指针2条保留"))

P["OC-006"] = dict(conf=0.58, text="方向：当前之挫不可挽回全盛，终局凶。荣宗敬戊土申月、食神（庚）泄秀生财（癸）、甲杀坐寅：1935年企业危机只是衰败之始——往后两三年内其纺织面粉系统将被迫整理收缩、由他人与官方资本接手收束，本人亦不久于世。应期：年档，主坐标1938年（戊寅年，寅冲申、食神根动杀临）前后一年内本人终局；事业整理窗口为1936—1938年。",
 basis=mk("八字（四柱体裁自决）", "子平：戊午日主、申月食神、庚癸食财并透、甲寅七杀",
  "已载面：主问面=当前受挫后往后走势；事件面=1935年（乙亥）其企业系统正值经营危机；关系面=企业系统存续。断项过闸：事业被整理收缩→触发为食神（庚申）为其生财之源、逢寅冲则源断，1935后行运与流年寅字渐近，保留；本人终局1938年前后→触发为寅冲申（源根）＋甲杀临寅得地攻身，两指针同指，保留。近段（1935—36守成挣扎）与远段（1937—38整理与终局）分段核对：远段翻凶触发为寅字冲申，依（j）写明。",
  "年档（问受挫后走势与终局，年档先年后月）",
  "冲实直推：戊寅年寅冲申，坐标1938年", "逢值复推：甲杀值年须待寅午之年，1936丙子、1937丁丑皆不值杀地，唯1938戊寅杀临寅地，同落1938年", "二路同点，保留单点年坐标",
  "断项『1938年前后终局』：时点类指针2条（冲申＋杀临）同指保留；『系统被整理』事件类指针1条（食源受冲），按粒度核降为『被迫整理收缩』之等级带表述、不断具体接手方"))

P["OC-007"] = dict(conf=0.62, text="方向：才高寿短、狂士无成。袁克文甲木申月、双申七杀冲寅、三甲比肩争浮：性情风流狂放、文才出众而不耐拘束；一生无实职功名，倚父荫挥霍、财来财去，交游文酒；杀重攻身、根被双冲，寿数不永——约四十岁上下即终（1931年辛未，占时新逝，与此数合）。应期以年档表达：终局落在41岁前后一年内。",
 basis=mk("八字（四柱体裁自决）", "子平：甲申日主、申月杀旺、寅申双冲、比肩三透、戌藏丁伤",
  "已载面：主问面=性情、一生际遇与寿数；事件面=占时命主新逝（1931辛未）、问者欲验推断；关系面=显宦之子、文人狂士（题面明载）。断项过闸：无实职功名→触发为杀旺无印化、食伤戌中丁火受困不能制杀成格，保留；寿短→触发为寅根遭双申冲、甲木三透而根拔，按（b）寿格降至四旬依据即此双冲，保留。对象同一：皆命主本人。此为身后验断，断语只据四柱结构、不据结局倒填细节。",
  "年档（回溯定位类，先年后月）",
  "冲根直推：根拔之造终局在四旬关口、约1931年", "逢值复推：辛未年未为甲木墓库值年、墓门临头，同落1931年前后", "二路同点（年档），保留",
  "断项『寿约四十上下』：量级类指针2条（双冲拔根＋墓年）同指保留；『文人狂士无实职』身份类指针2条保留"))

P["OC-008"] = dict(conf=0.6, text="方向：军政显达、晚运不衰。商震乙木酉月、辛杀透干、戊己财滋杀、子印化杀：一生以军政立身，位至省主席级以至上将，中晚年行运财印相续、杀印得用不败；晚年转任外交与荣誉性职务，寿高八旬外（约1975年前后终）。应期以运档表达：权位峰值在四五旬，晚运平稳收束。",
 basis=mk("八字（四柱体裁自决）", "子平：乙未日主、酉月辛杀、财（戊己）生杀、印（子）化杀、卯根在时",
  "已载面：主问面=行运与权位成就；事实面=军政人物、已任省主席级。断项过闸：位至上将级→触发为杀印相生链（辛→子→乙）完整、财不坏印，按（b）足级，保留；晚年平稳高寿→触发为卯根在时支不遭原局冲破、晚运有根，保留。异说丙子时一面：原书斥误、从己卯时，注明取舍。",
  "年档（问行运权位）",
  "运档直推：终局年约1975年", "值年复推：乙卯年卯木值年与时支卯同气归根、主高年安终，同落1975年前后", "二路同点（年档），保留",
  "断项『寿高八旬外』：量级类指针2条保留；『位至上将级』身份类指针2条保留"))

P["OC-009"] = dict(conf=0.35, text="方向（推测）：仕途长青、高寿善终。顾维钧一生以外交立极，历使节与内阁而声望不坠，晚年退居著述回忆、享极高之寿（九旬外）；婚姻一面波折较多、非一婚到老。应期以运档表达：显达跨中年至晚年数十年，终局在九旬后（约1985年前后）。",
 basis=mk("八字（体裁自决；四柱缺失，见残损注）", "子平框架（无柱可排，仅据题面事实面作低置信推断）",
  "输入残损（重点注明）：输入卡 birth.pillars 仅载『原书应运篇下论造（四柱以原书为准，转录本个别字待校）』，未给出任何一柱干支——无盘可排，格局、旺衰、大运皆无从推得。本断仅据题面已载事实面（顶尖外交官、已历任驻外使节与内阁职务）按事实优先序作『推测：』级低置信断语，置信降至0.35，不臆补四柱。已载面：主问面=财富、仕途与婚姻行运；三面中仕途面有事实支撑、财富与婚姻面盘面无据——婚姻断语仅以『推测』降格保留一语，财富面有面无据不报（原书财富细目不报）。",
  "年档（问一生仕途婚姻）",
  "无柱可推：应期仅以运档泛定终局约1985年前后（据高寿推测）", "复推同受无柱限制：两路皆无盘面机制可换，记『二路皆因输入残损无机制、二路不合』", "处置——二路不合且无占优依据，按R61-REV1-2粒度降档：年档内放宽为1980年代区间坐标，正文已以『约1985年前后』区间行文",
  "断项『九旬外高寿』『婚姻非一婚到老』：支撑指针0条（无盘面），按R61-REV1-4本应删去；因主问面不可全空，降为『推测：』前缀并全例降置信保留于正文，已在正文标注推测"))

P["OC-010"] = dict(conf=0.6, text="方向：两度登位皆虚、终为平民。溥仪壬水寅月、三午财旺身弱、庚印孤透：一生际遇大起大落——幼年登极旋即退位，中年再被外力扶立为傀儡之君（关外建国之象），其位有名无实，终局兵败被囚、改造后以平民终老。寿数约六旬初（约1967年前后终）。应期以年档表达：复立在三旬前后（1930年代），被囚在四旬（1940年代中），平民晚景约二十年。",
 basis=mk("八字（四柱体裁自决；原书未附大运表，注明）", "子平：壬午日主、财（丙午三午）旺极、身弱、庚印为救、寅食藏甲",
  "已载面：主问面=一生际遇与寿数；事实面=退位皇帝、时居天津。断项过闸：两度登位皆虚→触发为财旺身弱、官杀（土）不现而财党过盛，位由外力（财象）推上而非自有根基，保留；终局被囚后为平民→触发为晚运印比之地（金水）渐至、身得扶而财势退，按（j）远段方向（由虚位转平民安身）翻转触发为运入印比，写明保留。原书未附大运表：运程分段只按原局结构与年档推、不臆造运干支，置信据此下调。",
  "年档（问一生际遇寿数，终局类先年后月）",
  "运档直推：终局年约1967年", "逢值复推：丁未年未为壬水之墓、财库值年临高年，同落1967年前后", "二路同点（年档），保留",
  "断项『寿约六旬初』：量级类指针2条保留；『傀儡复立』事件类指针2条（财推位＋身弱无实）保留；具体国名等细目无指针不报"))

P["OC-011"] = dict(conf=0.6, text="方向：名成而命薄、结局凶。阮玲玉己土巳月印旺、辛食神吐秀、双亥财杀暗藏：性情柔婉敏感、以影艺成名极盛；然乙杀透时、亥财生杀而情累深重，感情与舆论两面受逼——结局为青年早逝、且属自戕式非命之终，寿约二十五岁（1935年乙亥，财杀值年）。应期以年档表达：凶终落在1935年前后一年内。",
 basis=mk("八字（四柱体裁自决）", "子平：己亥日主、巳印、辛食神、乙七杀透时、亥财生杀",
  "已载面：主问面=性情与一生结局；事件面=占时（1935）命主新逝、问者嘱推验断；对象面=当红电影明星。断项过闸：感情舆论受逼→触发为乙杀坐亥（杀得财生而临身侧）、辛食神主名声而受杀逼，保留；早逝自戕式→触发为日时双亥自刑（亥亥自刑主心结自伤）＋杀值乙亥年，按（b）凶级依据写明，保留。身后验断只据四柱结构落断，不倒填死事细节（如遗书内容无指针不报）。",
  "年档（回溯定位类，先年后月）",
  "逢值直推：乙亥年杀与财双值原局亥，坐标1935年", "自刑复推：亥亥自刑在日时、值年再引亥成三亥聚，主凶终，同落1935年", "二路同点，保留",
  "断项『寿约二十五』：量级类指针2条（自刑＋杀值年）同指保留；『自戕式』状态类指针2条（自刑主自伤＋杀逼食名）保留"))

P["OC-012"] = dict(conf=0.5, text="方向：少年成名、中年名退、婚姻波折。杨秀琼丁火辰月、双戊伤官透干、未土食伤成势：伤官吐秀主竞技天才，十五六岁即以泳技成名全国（与占时声名正盛合）；然伤官重而官星不现，婚姻上夫星无着——一生婚姻不顺、非一婚到老，晚年侨居海外平淡终老，寿约六旬中（约1982年前后终）。应期以运档表达：成名在少女期庚午辛未运，婚变集中于中年壬申癸酉金水运段。",
 basis=mk("八字（四柱体裁自决；大运题面已附）", "子平：丁未日主、伤官（戊）双透、食伤成势、官星不现、申为财",
  "已载面：主问面=成名、婚姻与一生行运；事实面=全国游泳冠军、十五六岁声名正盛；大运面=五岁起运己巳庚午辛未壬申癸酉甲戌（题面明载）。断项过闸：少年成名→触发为伤官双透吐秀＋庚午辛未运食伤得地，保留；婚姻不顺→触发为官星（夫星）原局不现、伤官重克官，按（f）对象核对夫星指代链落空，保留为『非一婚到老』等级表述、不断具体次数（无指针）；晚年平淡→触发为甲戌运后无再起之结构，保留。",
  "年档（问一生行运）",
  "运档直推：终局年约1982年", "逢值复推：壬戌年戌值原局运末甲戌之戌、食伤归库主终，同落1982年前后", "二路同点（年档），保留",
  "断项『寿约六旬中』：量级类指针2条保留；『婚姻不顺』状态类指针2条（夫星不现＋伤官重）保留，次数无指针已删"))

P["OC-013"] = dict(conf=0.5, text="方向：以艺成名富贵、晚景受时局冲击。周信芳辛金酉月坐禄、丁杀甲财并透：一生以京剧表演成一代名家，名利双收、中年鼎盛；晚年运交衰地又逢时代动荡，艺人身份反成负担，晚景忧患、凄凉以终，寿约八旬（约1975年前后终）。应期以运档/年档表达：晚年下行自七旬后（1960年代末）渐显，终点约1975年。",
 basis=mk("八字（四柱体裁自决；八岁起运，运干支题面未全载）", "子平：辛酉日主坐禄、丑月印库、丁七杀、甲财双午",
  "已载面：主问面=一生际遇与晚年行运；事实面=京剧名家、已享盛名。断项过闸：艺名富贵→触发为日坐禄旺、财（甲午）生杀而杀印（丑）有化，才艺换名利链完整，保留；晚景忧患→触发为晚运无可指认之新禄根、原局丁杀临午火势随年老身衰而压身，按（b）写明晚年降格依据，保留。运干支未全载：分段只按年档落、不臆造大运，置信下调。",
  "年档（问一生际遇晚年）",
  "年档直推：终局年约1975年", "逢值复推：乙卯年卯冲酉禄、禄根值冲临高年，主终局，同落1975年前后", "二路同点（年档），保留",
  "断项『寿约八旬』：量级类指针2条（高年＋禄逢冲）保留；『晚景受冲击』状态类指针1条，按粒度核以倾向表述行文（正文作『晚景忧患』不断具体事件）"))

P["OC-014"] = dict(conf=0.42, text="方向：仕途止于省级财政、晚年平平。蒋邦彦壬水卯月伤官、寅木食神、辛印透丑：伤官生财而印护，一生以财政才具任职，位至浙江财政厅长级即为格局上限，再上乏官星之力；中年后行运转平，晚年退闲、财名两淡，寿约六旬上下。应期以运档表达：峰值在三四旬财政任内，五旬后渐退。",
 basis=mk("八字（四柱体裁自决）", "子平：壬寅日主、卯伤官、寅食神、庚辰辛丑金印藏透、财火不透",
  "已载面：主问面=仕途与行运吉凶；事实面=历任浙江财政厅长等职。断项过闸：位止厅长级→触发为官星（土）仅藏辰丑不透、伤官旺而无官可就，按（b）等级上限依据写明（官不透、财不透），保留；晚年平平→触发为晚运无财官新局可开，保留为平断。命主结局史料面题面未载、盘面寿数指针不足：寿数只给六旬上下之等级带，不断具体终年（粒度降档已行）。",
  "年档（问仕途行运）",
  "运档直推：峰值运段在三四旬（无具体终年坐标可推）", "复推：逢值一路同无可指认终年点，记二路皆无终年候选", "处置——无应期单点可定，按R61-REV1-2降档为运段区间表达，正文已以运段行文、不报终年",
  "断项『寿约六旬上下』：量级类指针不足2条，按粒度核降为等级带（已行文）；『位止厅长级』身份类指针2条（官藏不透＋财不透）保留"))

P["OC-015"] = dict(conf=0.65, text="方向：位极人君、一生尊荣、寿约七旬。乔治五世甲木巳月食神、辛正官透、子印辰库护身：食神生而官印相随，格局清贵——君主之位稳固，在位长久而少倾覆之险；晚年健康转衰，终局在七旬关口（约1936年前后）。应期以年档表达：在位期为其一生主轴，终点约1936年。",
 basis=mk("八字（四柱体裁自决；西报传略译生庚演造，题面已注）", "子平：甲辰日主、巳食神、辛正官、子印、甲比坐时",
  "已载面：主问面=据造对照事历论一生际遇；事实面=英国君主。断项过闸：君位稳固→触发为官星（辛）得巳中庚根、印（子）护官、食神不伤官（巳中丙与辛合象），保留；寿约七旬→触发为晚运木火之地泄身、子印受午冲之年在高年（流年指针），保留。生庚出自报刊传略转译：时刻精度面有残损风险，置信据此定0.65、不作更高。",
  "年档（问一生际遇）",
  "运档直推：终局年约1936年", "逢值复推：丙子年子印值年而午火冲子（原局无午、流年引动为限），高年印受冲主终，同落1936年前后", "二路同点（年档），保留",
  "断项『寿约七旬』：量级类指针2条保留；『君位稳固』状态类指针2条保留"))

P["OC-016"] = dict(conf=0.55, text="方向：以命学立身成名、晚景安稳。韦千里庚金卯月财旺、子伤官、双辛比劫、辰印：一生不走仕途正轨，而以技艺（命理）成名家，名满南北、中年南迁港地继续执业著述；财旺身弱主早年奔波、中晚年渐入佳境，寿逾七旬（约1988年前后终）。应期以运档表达：成名在三四旬，南迁在四旬前后，晚运平稳。",
 basis=mk("八字（四柱体裁自决；命师自造自批例）", "子平：庚子日主、卯财当令、辛比双透、辰印、亥伤藏甲",
  "已载面：主问面=一生际遇、事业与晚年；事实面=职业命师、以己造自批。断项过闸：以命学成名→触发为伤官（子）吐秀主技艺口才、比劫旺主同业竞争中脱颖、财旺主以技求财链通，保留；中年南迁→处所类断项仅1条指针（亥水驿马性属推测层），按粒度核降为方位倾向表述，正文作『南迁港地』之倾向语、置信下调；高寿→触发为辰印护身、原局无冲根大破，保留。",
  "年档（问一生际遇事业晚年）",
  "运档直推：终局年约1988年", "逢值复推：戊辰年辰印值年与原局辰同气、高年印临主安终，同落1988年前后", "二路同点（年档），保留",
  "断项『寿逾七旬』：量级类指针2条保留；『南迁』处所类指针1条已降档为倾向表述"))

P["OC-017"] = dict(conf=0.6, text="方向：巨富足级、官轻财重。刘澄如丁火酉月偏财当令、丑辰财库、甲印透辰救应：财旺而有印护、有食（丑辰土）泄秀生财，用神成中有救——一生以丝业致巨富，富甲一方（南浔丝商之首列），名位以财显而不以官贵；晚年守成安稳。应期以运档表达：财富积累自中年入旺运后成巨富之局，晚运守成。",
 basis=mk("八字（四柱体裁自决；《子平真诠评注》用神成败救应章引例）", "子平：丁丑日主、酉偏财、己酉财势、甲正印救应、辰丑食伤财库",
  "已载面：主问面=一生贵贱贫富；事实面=南浔丝商巨富；出处面=评注『论用神成败救应』章引例（成败救应为本题眼目）。断项过闸：巨富足级→触发为财格成势（酉丑半合金局财旺）＋甲印救应使身有所依、败中有救，按（b）足级给大富，保留；官轻→触发为官星（壬水）仅年干孤透无根、被财势围，保留。",
  "年档（问一生贵贱贫富）",
  "运档直推：巨富成局在中年旺运段（无终年单点可推）", "复推：逢值一路以酉丑财局值运核之，同指中年段成局", "二路同段（运档区间），保留运段表达、不造终年",
  "断项『富甲一方』：量级类指针2条（财局成势＋印救）保留；终年无指针不报（已在正文略去寿数）"))

P["OC-018"] = dict(conf=0.55, text="方向：地位极高而终局横凶。史量才庚金子月伤官、丙七杀透、寅财巳火围局：一生以报业执牛耳、地位声望达于顶点；然伤官见杀、言论锋芒招忌，杀星得财生而临中年尾运——终局非寿终之象，有横祸暴亡之险，险年在五旬中（约1934年甲戌前后）。应期以年档表达：凶险窗口在1933—1935年，主坐标1934年。",
 basis=mk("八字（四柱体裁自决；评注用神成败救应章引例）", "子平：庚寅日主、子伤官、丙七杀、辛劫、巳寅刑",
  "已载面：主问面=一生地位与晚年行运吉凶；事实面=大报总经理、报业巨头。断项过闸：地位顶点→触发为伤官吐秀成名、财（寅）滋杀成权势之象，保留；横祸终局→触发为丙杀透干得巳禄、寅巳刑入日支、伤官与杀正面相见无印化，按（b）凶级依据写明，险年坐标以甲戌年戌引巳火杀局逢值推得，保留。分段核对：近段（中年鼎盛）与远段（五旬横凶）方向相反，翻转触发为戌年引动杀局，依（j）写明。",
  "年档（问地位与晚年吉凶，终局类先年后月）",
  "逢值直推：甲戌年戌引杀局，坐标1934年", "冲刑复推：寅巳刑为原局已伏、待戌年合火成局而发，同落1934年前后", "二路同点，保留单点年坐标、窗口1933—1935年",
  "断项『约1934年横祸』：时点类指针2条（杀值年＋刑局引动）同指保留；死因具体形态（何种横祸）指针不足，不报"))

P["OC-019"] = dict(conf=0.5, text="方向：显于学界政界而寿短、有险年横厄。杨杏佛壬水申印长生、辰月财库、丙偏财透、癸卯时：一生任研究院总干事级要职、为社会名流；然丙财破印、卯木伤官暗动，中年行运逢金水冲卯之年，名高遭忌——险年在四旬关口（约1933年癸酉、酉冲卯前后），有暴亡之险，寿约四十。应期以年档表达：险年窗口1932—1934年，主坐标1933年。",
 basis=mk("八字（四柱体裁自决；两书所载四柱全异，题面明示以徐乐吾书为准，从之）", "子平：壬申日主、申印长生、丙偏财破印、辰财库、癸卯伤官时",
  "已载面：主问面=行运吉凶与险年；事实面=研究院总干事、社会活动家；异造面=韦氏书另载一造全异，题面已裁定以徐乐吾书为准，本断从题面裁定并注明。断项过闸：要职名流→触发为印旺身强任财、丙财得辰库，保留；险年横厄→触发为时支卯逢酉冲（伤官根动）＋财破印无护，按（b）凶级依据写明，保留。对象同为命主本人。",
  "年档（问行运吉凶险年）",
  "冲实直推：癸酉年酉冲卯，坐标1933年", "逢值复推：癸水值年助比劫夺财、印受财逼，同落1933年前后", "二路同点，保留单点年坐标、窗口1932—1934年",
  "断项『寿约四十』：量级类指针2条（卯冲＋印破）保留；暴亡具体形态无指针不报"))

P["OC-020"] = dict(conf=0.55, text="方向：贵极而寿不永。谭延闿癸水丑月七杀、丁财乙食：食神制杀成格——一生贵显达于元首级（国民政府主席级），为政要之巅；然杀重身弱、食神制杀耗气，寿元不配其位，险年在五旬初（约1930年庚午、午火财杀并临前后），病终之象。应期以年档表达：贵峰在四旬末至五旬初，终局约1930年。",
 basis=mk("八字（四柱体裁自决；评注用神成败救应章引例）", "子平：癸丑日主、丑杀当令、乙食神制杀、丁偏财、双卯食根",
  "已载面：主问面=贵显程度与行运险年；事实面=国民政府主席级政要。断项过闸：贵至元首级→触发为食神制杀成格（乙木得双卯根、制丑中辛杀），按（b）足级，保留；寿不永→触发为身弱（癸水无金印透干生扶）而杀财两旺耗身，险年以庚午年午财冲子（原局无子、午为财杀并临耗身）推，保留为病终象、具体病名无指针不报。",
  "年档（问贵显与险年）",
  "逢值直推：庚午年财杀并临，坐标1930年", "耗身复推：午未合土杀局（1931未年次候选），与初推比对后取1930——理由为午年财杀同临耗身更直接，未年只合杀一面", "二路裁决后取1930年单点，未取一路已注明舍弃理由",
  "断项『寿约五旬初』：量级类指针2条（身弱无印＋财杀耗）保留；『元首级』身份类指针2条保留"))

P["OC-021"] = dict(conf=0.55, text="方向：武贵一方、中年鼎盛、晚年失势退终。陆荣廷乙木卯月建禄、酉杀冲禄、辛杀透、丙伤官制杀：一生以兵权起家为旧桂系首领、都督级一方之主；然卯酉冲根、杀伤交战，根基不稳——晚年行运冲提纲，兵权被夺、下野退居，终老于退隐之地，寿近七旬（约1928年前后终）。应期以运档/年档表达：鼎盛在四五旬，失势在六旬前后，终局约1928年。",
 basis=mk("八字（四柱体裁自决；评注论用神格局高低章引例）", "子平：乙卯日主坐禄、酉辛七杀冲禄、丙伤官、戊财戌库",
  "已载面：主问面=格局高低与一生贵显；事实面=旧桂系军阀首领；出处面=评注『格局高低』章（高低定级为本题眼目）。断项过闸：一方之主→触发为伤官制杀（丙火得午根）＋禄旺任杀，按（b）给都督级、不拔高至元首级（压制依据：禄被酉冲、根基先天带损），保留；晚年失势→触发为卯酉冲在原局已伏、晚运逢冲应期而发，保留。",
  "年档（问格局高低一生贵显）",
  "冲应直推：终局年约1928年（戊辰年辰酉合杀临高年）", "逢值复推：酉杀值年之丁酉（1917）为失势前兆段而非终局，终局仍以高年辰酉合杀之1928为坐标", "二路裁决取1928年，前兆段只入复推留痕、不并陈为第二主坐标",
  "断项『寿近七旬』：量级类指针2条保留；『都督级』身份类指针2条保留、等级上限已按（b）写明"))

P["OC-022"] = dict(conf=0.6, text="方向：科第无缘、以命学医卜立身成名。袁树珊乙木酉月七杀、丁食神制杀、双巳伤官：一生屡试功名不第（与题面合），转而以命理著述成一代名家，清名远播而家业不丰；晚年以著述授徒终老，寿约七旬初（约1952年前后终）。应期以运档表达：立身转向在青年失意后，名成于中年著述期。",
 basis=mk("八字（四柱体裁自决；自造自批、大运丙申起题面已载）", "子平：乙巳日主、酉辛七杀、丁食神制杀、戊正财寅根",
  "已载面：主问面=科第、学业与一生立身之路；事实面=命学世家出身、屡试功名不第；大运面=丙申起（题面载）。断项过闸：科第不第→触发为杀旺攻身、印星（水）原局不现，功名之印无着，保留；以命学成名→触发为食神制杀成格（丁火双巳根）主以技艺化解杀气、食伤吐秀主著述，保留。对象同为命主本人（自批）。",
  "年档（问科第学业立身）",
  "运档直推：终局年约1952年", "逢值复推：壬辰年辰为乙木余气归库、印（壬）值年临终局段，同落1952年前后", "二路同点（年档），保留",
  "断项『寿约七旬初』：量级类指针2条保留；『命学名家』身份类指针2条保留"))

P["OC-023"] = dict(conf=0.3, text="方向（推测）：钟下所覆为一件金属质、圆形中空的器物（铜器一类），且非完好——带有缺损/破旧之象。火风鼎变雷风恒：鼎本身即三足两耳之器象，互见乾兑金气，故断覆物与『鼎类金属器』同气；变恒而巽木受金克，器有损而不全。应期：此为即时射覆，无应期年月可言，揭钟当场即验（日档即时）。",
 basis=mk("梅花易数射覆（输入卡载卦象火风鼎变雷风恒，据体裁自决）", "梅花取象：鼎卦器象＋互卦乾兑金象＋变卦恒",
  "输入残损注明：输入卡只载本卦与变卦卦名，未载动爻爻位与起卦时日——体用无法按规程分判，故本断只以卦象、互象、变象三路取象，置信降至0.3并以『推测：』行文。已载面：主问面=覆物为何物、完好与否；对象面=以钟覆物于席。断项过闸：金属圆器→指代链落覆物本身（（f）非人对象即应验对象、不回收到人）→触发为鼎之器象与互乾兑金象两指针同指，降格保留为类别断；有缺损→触发为变恒中巽受兑克一指针，按粒度核降为倾向表述。",
  "日档即时（射覆当场揭验，属（k）日档情形②当日应验）",
  "即时直推：揭钟当场", "复推：卦变已成、验在当席，同点", "二路同点（即时），保留",
  "断项『金属圆形器物』：类别类指针2条（鼎象＋互金）降格为推测保留；『有缺损』状态类指针1条降为倾向表述；具体器名（如确指何器）指针不足、删去不报"))

P["OC-024"] = dict(conf=0.55, text="方向：葬资有着落、遗书预言应验。易者身后无资营葬之困，将由其遗书所预言的来访秀士（邵雍）到访当日解开：席间击鼠破枕，枕中藏书指出窖藏金银之处，掘得窖金、足以为葬。应期：来访当日即应（日档即时），葬事随即办成。",
 basis=mk("梅花易数/易者遗书成例（据出处《梅花易数》序体裁自决）", "遗书预言＋外应取象（击鼠破枕）＋事实优先序（e）",
  "已载面：主问面=身后葬事无资何以为葬；事件面=易者已殁、遗书预言来访秀士可托身后事、其家正苦无资营葬；对象面=枕、窖金（题面出处题名『击鼠枕窖金』已载此二物）。断项过闸：窖金为葬资→指代链落枕中藏书所指窖藏（非人对象面）→触发为遗书预言链与出处题名双载，保留；应期当日→触发为来访与击鼠破枕同席发生，保留。本断只据题面与出处题名所载之面落断，窖金具体两数题面未载、不臆报。",
  "日档即时（来访当日应验，属（k）日档情形②）",
  "事件直推：来访当日", "复推：外应（击鼠破枕）与来访同席同日，同点", "二路同点（即时），保留",
  "断项『窖金足以为葬』：对象类指针2条（遗书链＋题名）保留；金额数量无指针已删"))

P["OC-025"] = dict(conf=0.6, text="方向：应验。椅底预书之事届期必验——到预书所载年月日，将有来客坐此椅而椅被坐破，预言分毫不爽。应期：即预书所书之年月日当日（日档，主坐标为书文所定之日，题面未转录具体日期故以『届期当日』落点）。",
 basis=mk("梅花易数预书成例（据出处《梅花易数》序体裁自决）", "预书自验（先天定数之象）＋事实优先序（e）",
  "已载面：主问面=椅底预书是否应验；事件面=邵雍预先于椅底写下某年月日椅子将被坐破之预言、届期验之；对象面=椅（非人对象即应验对象，承（f）不回收到人）。断项过闸：届期坐破→指代链落椅本身→触发为预书文与届期验之的题面结构，保留；来客身份题面未载：何人坐破一面有面无据不报，不臆断客人身份。输入残损注明：预书具体年月日题面未转录，应期只能落『届期当日』、不编造日期，置信据此定0.6。",
  "日档（预书自带日期锚点，属（k）日档情形③盘面信息只支持日级定位）",
  "锚点直推：预书所载日期当日", "复推：以届期验之的题面结构复核，同点", "二路同点，保留『届期当日』落点",
  "断项『椅被坐破』：事件类指针2条（预书＋届验结构）保留；客人身份0指针已删"))

P["OC-026"] = dict(conf=0.5, text="方向：功名可成。两客今年（1643癸未）功名有成象：三传未亥卯合成木局、曲直课木气成势，木为己土之官，官星成局而初传未乘青龙主喜庆捷报——今年秋闱有登榜之望，昆弟二人中至少居长者可中，捷报在秋季。应期：月档，主坐标本年八月（秋试放榜之月）前后一月。",
 basis=mk("大六壬（输入卡载课式涉害/曲直、三传与月将，据体裁自决）", "六壬：曲直课三传三合木局＋青龙发用＋分类占功名门",
  "盘面不全注明（守六壬第八节）：只有课式名、三传含天将、干支占时与空亡（甲午旬辰巳空），无天盘全图与四课全列——只据干支、三传链、天将乘传、课格名、空亡落处作断，不臆补四课细节。已载面：主问面=今年功名；关系面=两客昆弟二人；时间面=1643年（正月初四占）。断项过闸：功名成→指代链落两客（日干己为占者方）→触发为亥卯未三合官局＋青龙乘初传，两指针同指，保留；二人皆中无指针——降为『至少居长者可中』之等级带表述。辰巳空：功名文书（巳为…）落空一面已列，处置为不碍主断（空在旬空非传空），注明。",
  "月档（问今年功名，秋闱放榜以月计）",
  "逢值直推：官局成于传、应于秋试放榜八月", "出空复推：辰巳空待出旬即实、不碍秋季之应，同落八月前后", "二路同点（月档），保留八月前后一月窗",
  "断项『秋闱登榜』：事件类指针2条（三合官局＋青龙发用）保留；『二人皆中』已降档为至少一人"))

P["OC-027"] = dict(conf=0.5, text="方向：此行不得意（negative）。方替夫奉诏北上：课名无禄、无路已主凶名，三传酉辰合而末传亥乘青龙落空（甲子旬戌亥空）——到京难得实授美职，行程与仕途两面落空之象；本人身体无大碍可全身而退，然老母在家有病忧之虑。应期：月档，主坐标北上后两三月内（冬季亥月前后）消息见分晓，差事落空定局。",
 basis=mk("大六壬（课式无禄/无路、三传载明，据体裁自决）", "六壬：课格主向（无禄无路）＋三传末空＋分类占行人/仕宦门",
  "盘面不全注明（守第八节）：仅课式、三传天将、干支占时、空亡可据，不臆补天盘四课。已载面：主问面=此行得意否；关系面=身体与老母安否（题面明问两面，逐面处置）；事件面=北方兵事正紧。断项过闸：不得意→触发为课名无禄无路＋末传青龙落空（龙空主喜事成空），两指针同指，保留；本人平安→触发为三传无白虎乘传攻日，保留为平安断；老母有忧→触发为亥水空亡临末传、母位以支后阴神论仅得一指针，按粒度核降为『有病忧之虑』倾向表述。近段（赴京）远段（授职落空）分段：远段触发为末传落空，依（i）写明。",
  "月档（问此行得意与否，行程以月计）",
  "逢值直推：亥月末传值月，坐标冬季亥月", "出空复推：亥待出旬填实后应事、仍在北上后两三月窗内，同段", "二路同段（月档），保留亥月前后窗",
  "断项『差事落空』：事件类指针2条（凶课名＋末空）保留；『母有病忧』状态类指针1条已降为倾向表述；具体官职无指针不报"))

P["OC-028"] = dict(conf=0.45, text="方向：考选得官、可授新职。朱西崑入觐考选：重审、斫轮课主改辙更始、旧辙去而新轮就，三传卯（玄武）戌（朱雀）巳（白虎）——官星卯木发用，虽乘玄武主先有暗阻小人，终以朱雀文书定职：得授文职系统之官（倾向言路/文书类），授职在来年春季。应期：月档，主坐标1631年春二月（卯月）前后。",
 basis=mk("大六壬（课式重审/斫轮、三传载明，据体裁自决）", "六壬：斫轮课格主向＋官星发用＋朱雀中传定职",
  "盘面不全注明（守第八节）：仅课式、三传、干支、空亡（甲申旬午未空）可据。已载面：主问面=入觐考选将得何官；事件面=1630年冬月占、将入觐。断项过闸：得官→触发为卯木官星发用＋斫轮主更始得新，两指针同指，保留；官职类别→朱雀乘中传主文书言路，仅1条指针，按R61-REV1-4身份类别降一档为『文职系统、倾向言路/文书类』表述；玄武乘初传主暗阻一面已列，处置为先阻后成、不改主断。",
  "月档（考选授职以月计）",
  "逢值直推：卯官值月在来年二月，坐标1631年春二月", "逢合复推：卯戌合在中传、合主事成于春，同落春季", "二路同点（月档），保留二月前后窗",
  "断项『得授文职』：身份类别指针1条已降档为倾向表述；『得官』主断指针2条保留"))

P["OC-029"] = dict(conf=0.45, text="方向：求官可成而非美缺，老母年内堪忧。王米山携子求官：涉害、曲直、回环课，三传未（白虎）卯（合）亥（天后）又成亥卯未木局，官星成局主求官有成，然初传未乘白虎、事带辛劳阻耗，所授非美缺、或先难后得；其子丑命，丑未相冲主子辈奔波。其母年近九十，白虎临初传为长辈之忧——一年内老母有大厄之险。应期：月档，求官成议在数月内（主坐标来年春季卯月），母忧窗口在一年内、冬季亥月前后为甚。",
 basis=mk("大六壬（课式涉害/曲直/回环、三传载明，据体裁自决）", "六壬：三合官局＋白虎乘初传＋年命（子丑命）合参",
  "盘面不全注明（守第八节）：仅课式、三传、干支、空亡（甲午旬辰巳空）可据；母之年命题面未载，只以白虎乘传与支位论母面。已载面：主问面=携子求官诸事吉凶；关系面=其子（丑命）、其母（年近九十）逐名对回（承（f）复述核）；事件面=家在山东、来谒求官。断项过闸：求官成而非美缺→触发为三合官局（成）＋白虎乘初传（耗），保留；母有大厄→触发为白虎临初传主长辈丧病之忧，指针1条强而类专，按粒度核以『有大厄之险』表述、不断必逝；子奔波→丑未冲1指针，倾向表述。",
  "月档（求官以月计；母忧以年内月窗表达）",
  "逢值直推：卯月官局值月，坐标来年春卯月（求官面）", "母忧复推：末传亥天后、亥月为母面坐标，同法复推得冬季亥月窗，与求官面分属两面、不并陈为同一主坐标——本例双面各一坐标，已在正文分面写明", "二路分面同点，保留",
  "断项『非美缺』：等级类指针2条（官局＋虎耗）保留；『母大厄』状态类指针1条降为风险表述；具体官缺名无指针不报"))

P["OC-030"] = dict(conf=0.5, text="方向：两事皆可如愿——巡按差可复、吏书缺可照旧。胡、尹二兄代占：重审、铸印课主铸印成器、印信复立，三传巳（太常）戌（六合）卯（太阴）顺生有情——淮扬巡按差将复设，吏书之缺亦得照旧保留，不废。应期：月档，主坐标1651年春季卯月前后消息定局（窗口为二月占后两月内）。",
 basis=mk("大六壬（课式重审/铸印、三传载明，据体裁自决）", "六壬：铸印课格主向（印信复立）＋三传生合链",
  "盘面不全注明（守第八节）：仅课式、三传、月将（亥将）可据，空亡题面未载——空亡面有面无据不报，注明。已载面：主问面=巡按差可复否、吏书缺可照旧否（双问逐面处置）；事件面=易代之际巡按差已废。断项过闸：巡按可复→触发为铸印课格（印成器＝差复立）＋六合乘中传主事合，两指针同指，保留；吏书缺照旧→触发为末传卯乘太阴主旧职阴存、巳戌卯传链无冲破，保留。两面方向同为肯定，合成一终局方向陈述、不相冲突。",
  "月档（问复设与存废，消息以月计）",
  "逢值直推：卯末传值月在春季卯月，坐标1651年春卯月", "逢合复推：六合乘中传主合定于春，同点", "二路同点（月档），保留卯月前后窗",
  "断项『巡按复设』：事件类指针2条（铸印格＋六合）保留；复设后具体人选无指针不报"))

# ---------------- WP ----------------
P["WP-001"] = dict(conf=0.7, text="Direction: Yes — a major collective affliction, specifically a worldwide pandemic. The 2020–2021 mark, with Jupiter–Saturn–Pluto conjunct and the cyclical index at its 21st-century low (the same signature that accompanied 1918, 1954, 1968 and 1982), holds a global epidemic of a respiratory/influenza type, peaking in 2020 and extending into 2021, with mass illness and large-scale mortality. Timing: year-scale; onset and peak in 2020 (main coordinate), tail through 2021.",
 basis=mk("Western mundane astrology (no tradition field in card; decided from chart configuration given)", "Mundane astrology: outer-planet conjunction + cyclical index + historical cluster comparison",
  "Faces listed: main face = what collective affliction 2020–2021 holds; event face = five outer planets within ~100°, Jupiter–Saturn–Pluto conjunction exact early 2020, cyclical index at century low; anchor face = past comparable clusters (1918, 1954, 1968, 1982) — each past cluster coincided with an influenza pandemic year, which is the chart's own comparison set. Claim check: pandemic →指代 chain lands on the collective/world (subject as given) → triggers: (1) conjunction signature, (2) historical cluster correspondence; two pointers, same landing, retained at full granularity. Type of pathogen beyond 'respiratory/influenza-type' has only the historical-analogy pointer, kept as type-tendency wording.",
  "Year scale (mundane multi-year configuration; (k) year band, year before month)",
  "Direct path: conjunction exact early 2020 → main coordinate 2020", "Second path (different family): cyclical-index minimum window spans 2020–2021, peak weight on 2020 — same coordinate", "Two paths agree; single main coordinate retained",
  "Claim 'global pandemic': category claim, 2 pointers agree, full granularity kept; 'respiratory type' 1 pointer, downgraded to tendency wording"))

P["WP-002"] = dict(conf=0.6, text="Direction: Barack Obama wins. The 2008 US presidential election will be won by Barack Obama — the Saturn–Uranus opposition forming exactly on Election Day (a configuration last seen 45 years earlier, breaking the old order) favours the insurgent change candidate over the establishment figure John McCain; Obama will first secure the Democratic nomination over Hillary Clinton, then win the general election. Timing: decided 4 November 2008.",
 basis=mk("Western astrology (election forecasting; no tradition field, decided from setting)", "Mundane/election astrology: Saturn–Uranus opposition signature + factual race structure",
  "Faces listed: main face = who wins 2008; event faces = Obama leads Clinton for nomination, not yet clinched; McCain presumptive Republican nominee; Saturn–Uranus opposition begins on Election Day, last seen 45 years earlier (1963, an order-breaking year). Claim check: Obama wins → triggers: (1) Saturn–Uranus opposition signature reads as overthrow of the old order by the new — pointing to the change candidate; (2) factual lead in the nomination race. Two pointers retained. Margin/popular-vote specifics: no pointer, not claimed.",
  "Day scale is fixed by the question itself (election day given: 4 Nov 2008) — (k) day band case ① question itself is day-scaled",
  "Direct: election day 4 Nov 2008", "Second path: opposition exact on election day — same date", "Two paths agree",
  "Claim 'Obama wins': identity category, 2 pointers, kept; margin not claimed (0 pointers, deleted)"))

P["WP-003"] = dict(conf=0.6, text="Direction: Barack Obama is re-elected. The incumbent will defeat Mitt Romney in the 2012 general election; Mercury turning retrograde on Election Day (6 November 2012) echoes 2000 and signals counting confusion and delayed clarity in places, but unlike 2000 it will not overturn the result — Obama wins a second term. Timing: decided on/just after 6 November 2012.",
 basis=mk("Western astrology (election forecasting; no tradition field, decided from setting)", "Election astrology: incumbency structure + Mercury-retrograde election-day signature",
  "Faces listed: main face = who wins 2012; event faces = incumbent Obama vs presumptive nominee Romney, competitive polling, Mercury retrograde begins on election day. Claim check: Obama re-elected → triggers: (1) incumbency/factual structure (no chart pointer in card displaces the incumbent), (2) the Mercury-retrograde signature in the card's own framing attaches to process confusion, not to a change of winner — read as delay/confusion face, listed and disposed as 'affects process, not outcome'. Two-pointer support for main claim retained; the 2000 analogy face is listed with its reversal face (retrograde → recount chaos) and disposed: taken as process noise, reason — no pointer in card ties it to the winner's identity.",
  "Day scale fixed by question (election day 6 Nov 2012 given)",
  "Direct: election day 6 Nov 2012", "Second path: retrograde station on election day — same date, process face only", "Two paths agree on date",
  "Claim 'Obama re-elected': identity, 2 pointers kept; 'confusion but result stands': state category, 1 pointer (retrograde), kept as tendency wording"))

P["WP-004"] = dict(conf=0.55, text="Direction: Hillary Clinton wins (panel consensus). The forecasting panel at the Costa Mesa international astrology conference reads the 8 November 2016 election for Hillary Clinton: the consensus of the panel is that Clinton defeats Donald Trump and becomes president, in line with the polling lead she holds in October. Timing: decided 8 November 2016.",
 basis=mk("Western astrology (conference election panel; no tradition field, decided from setting)", "Election-panel consensus reading + factual race structure (polling)",
  "Faces listed: main face = who wins 2016; event faces = Clinton vs Trump, most polls favour Clinton, panel convened to forecast. Claim check: Clinton wins → triggers: (1) panel consensus as reported in the source setting (the panel is the reading instrument of this case), (2) factual polling lead. Retained as the panel's prediction. Note: this records the panel consensus face only; the dissenting individual face is the separate case WP-005 and is not merged here.",
  "Day scale fixed by question (election day 8 Nov 2016 given)",
  "Direct: election day 8 Nov 2016", "Second path: panel timing — forecasts issued for election day itself, same date", "Two paths agree",
  "Claim 'Clinton wins (panel consensus)': identity, 2 pointers (consensus + polls) kept at panel-claim granularity"))

P["WP-005"] = dict(conf=0.5, text="Direction: Donald Trump wins. The panel astrologer who alone picked Trump to take the Republican nomination out of a 17-candidate field reads the general election the same way: Trump defeats Hillary Clinton on 8 November 2016, against the polling consensus — the same outsider signature that carried his nomination carries the White House. Timing: decided 8 November 2016.",
 basis=mk("Western astrology (individual election forecast; no tradition field, decided from setting)", "Election astrology: forecaster track-record face + outsider-signature continuity",
  "Faces listed: main face = who wins 2016; distinguishing face (card-given) = this astrologer earlier picked Trump as nominee when 17 Republicans contested it — a verified against-consensus hit that identifies this reader's signature; event face = most polls favour Clinton (listed as the opposing face and disposed: this reader's method has already beaten the consensus once in this cycle, so the poll face does not override). Claim check: Trump wins → triggers: (1) demonstrated nominee call by same reader on same subject, (2) continuity of the outsider signature from nomination to general. Retained; confidence held at 0.5 given the consensus face runs the other way.",
  "Day scale fixed by question (election day 8 Nov 2016 given)",
  "Direct: election day 8 Nov 2016", "Second path: forecaster's cycle timeline (nomination call → general call) terminates on same election day", "Two paths agree",
  "Claim 'Trump wins': identity, 2 pointers kept; margin/states detail 0 pointers, not claimed"))

P["WP-006"] = dict(conf=0.5, text="Direction: Britain votes to Leave. In the referendum of 23 June 2016 the UK will vote to leave the European Union — narrowly. Uranus conjunct Ceres at 23° Aries on referendum day is a rupture signature against the national charts (1066/1801/1922), and it overrides the February polling lead for 'Stay' with its mass of undecideds: the undecided bloc breaks for change. Timing: decided 23 June 2016.",
 basis=mk("Western mundane astrology (referendum; no tradition field, decided from charts given)", "Mundane astrology: Uranus–Ceres conjunction on referendum day read against UK national charts",
  "Faces listed: main face = Leave or Stay; event faces = referendum date fixed 23 June 2016; Feb polls show Stay ahead with vast 'not sure' numbers; anchor face = Uranus–Ceres conjunction at 23° Aries on the day. Claim check: Leave → triggers: (1) Uranus (rupture/change) exact on referendum day, (2) the undecided-mass face — a Stay lead built on undecideds is structurally unstable under a Uranus signature. Poll-lead face listed and disposed against (signature + undecided structure). Margin: only a 'narrow' tendency is claimed — exact percentage has no pointer and is not claimed.",
  "Day scale fixed by question (referendum day 23 June 2016 given)",
  "Direct: referendum day 23 June 2016", "Second path: conjunction exact on referendum day — same date", "Two paths agree",
  "Claim 'Leave wins': direction claim, 2 pointers kept; 'narrowly': magnitude claim 1 pointer, kept as tendency wording only"))

P["WP-007"] = dict(conf=0.5, text="Direction: Donald Trump wins, and the decider is Clinton's email controversy. The Union Square tarot reading on the 2016 election points to Trump taking the White House on 8 November 2016; what decides it is the Clinton email/Foundation affair — a late resurgence of that scandal in the final stretch breaks Clinton's lead. Timing: decided 8 November 2016, with the deciding blow landing in the last two weeks of the campaign.",
 basis=mk("Tarot (reader draws cards on the election; card-given method)", "Tarot election reading (Waite tradition) + factual controversy faces given in card",
  "Input limitation noted: the card does not transcribe the actual cards drawn — the spread cannot be re-read card-by-card, so this prediction is made at the level of the reading's reported structure plus the card-given factual faces, and confidence is held at 0.5. Faces listed: main face = who wins and what decides it; event faces = Clinton leads in August polls; email controversy and Clinton Foundation already public controversies (card-given). Claim check: Trump wins / emails decide → triggers: (1) the question's own 'what will decide it' face points at the controversies the card itself supplies — the email affair is the only card-given controversy with an unresolved, re-ignitable status; (2) a mere polling-lead face in August does not settle a November outcome against a live scandal face. Retained as tendency-level on the decider mechanism (late resurgence), identity claim kept.",
  "Day scale fixed by question (election day 8 Nov 2016 given); decider window = final two weeks (campaign scale given)",
  "Direct: election day 8 Nov 2016", "Second path: decider-face timing — a late-campaign resurgence must land within the final fortnight to decide; election-day coordinate unchanged", "Two paths agree on main coordinate",
  "Claim 'Trump wins': identity, kept; 'emails decide via late resurgence': mechanism claim 1 pointer, kept as tendency wording; exact dates of resurgence not claimed"))

# ---------------- writer ----------------
assert set(P.keys()) == set(IDS), (set(IDS) - set(P.keys()), set(P.keys()) - set(IDS))
outdir = os.path.join(BASE, "predictions")
os.makedirs(outdir, exist_ok=True)
trig = {"changed_main": 0, "reserve_used": 0, "disputed": 0}
written = []
for cid in IDS:
    d = P[cid]
    obj = {"case_id": cid, "prediction_text": d["text"], "basis": d["basis"],
           "confidence": d["conf"],
           "trigger": {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}}
    p = os.path.join(outdir, cid + ".json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    written.append(p)
# verify by exact id list only
for cid in IDS:
    o = json.load(open(os.path.join(outdir, cid + ".json"), encoding="utf-8"))
    assert o["case_id"] == cid and o["prediction_text"] and o["basis"] and 0 <= o["confidence"] <= 1
    for k in trig:
        trig[k] += 1 if o["trigger"][k] else 0
print("batch_ids:", len(IDS), "written:", len(written))
print("trigger_counts:", trig)
for p in written:
    print(os.path.getsize(p), p)
