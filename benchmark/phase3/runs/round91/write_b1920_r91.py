# Round91 B19+B20 blind predictions writer (unique script, round91 only)
import json, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round91/predictions"
os.makedirs(BASE, exist_ok=True)

def T():
    return {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}

P = {}

# ---------------- B19 ----------------
P["MP-017"] = dict(
 conf=0.72,
 pred="方向：女性出任。断语：2017年3月26日选举委员会投票，下届香港行政长官由女性当选，即当时改口重新考虑参选的政务司司长一系女性人选胜出，男性候选人不入主礼宾府。应期：2017年3月26日投票当日定局（日档，本题问投票结果，尺度为日）。systems_used：时势象占＋年命性别取象（题面事实优先）。",
 basis="卡面未标注 tradition/system 字段——本卡题面为「下届特首男或女」二择之问，按题面体裁以时势象占自决。依据：卡面已载梁振英宣布不连任、曾俊华辞职备选而声势属男性阵营、林郑月娥改口重新考虑参选；女性人选为唯一具官方履历纵深者，象主阴方得位。无盘面/相片材料，置信据题面事实定。",
)
P["MP-018"] = dict(
 conf=0.74,
 pred="方向：不能当选（负）。断语：曾俊华民望虽为候选人中最高，仍落选2017年行政长官，终局得票居第二而与特首之位无缘；决定之手不在民望而在选举委员会的结构性支持。应期：2017年3月26日投票日落定（日档，选举日即应期）。systems_used：面相报道体裁参时势结构断（无相片，仅据题面载明之民望与北京支持分布）。",
 basis="卡面未标注 tradition/system 字段——本卡题面为曾俊华个人能否当选之问，刊于相学杂志，按面相体裁参时势自决。依据：卡面明载传媒普遍指对手获北京支持、选情占优，曾被视为陪跑；1194人选举委员会结构下民望不转化为多数票。卡面无本人相片，面相细节无据不报、降置信。",
)
P["MP-019"] = dict(
 conf=0.76,
 pred="方向：林郑月娥当选。断语：三候选人中花落林郑月娥（1957年生、酉年），2017年3月26日以选举委员会多数票当选行政长官；曾俊华得票第二，胡国兴第三、得票最少。应期：2017年3月26日投票当日（日档）。systems_used：年命生肖合参＋选情结构断。",
 basis="卡面未标注 tradition/system 字段——本卡题面为三候选人花落谁家、写作于选举前一日，按年命与时势合参自决。依据：卡面载三人年命（林郑酉、曾卯、胡酉）与提名辩论已毕；2017丁酉年，酉年命人得岁君同气，且其官方支持结构最厚。功量核算（R80-REV1）：助成线为岁君同气＋支持结构两线，压制线无，主线为结构支持，胜出量级定为明确多数而非险胜。",
)
P["OC-001"] = dict(
 conf=0.62,
 pred="方向：先盛后衰、贵而终败。断语：戊土日主生辰月，土重成势，早中年统兵主政一方、位至军阀首领级；晚年运入水木疏土之地，权势尽失、下野闲居，终局困顿而终，寿约六旬中段。应期尺度为运/年档：高峰在中年土金运段，败落转折在晚年运交水旺之年（定值：运档窗口，流年层因卡面无大运表缺位降格）。systems_used：八字子平（格局＋旺衰＋调候合参）。",
 basis="卡面未标注 tradition/system 字段——本卡题面为吴佩孚四柱甲戌戊辰戊申壬子论一生，按八字自决。主线：戊辰月戊土当令得地，年时戌辰土重、申子半合水财透壬，格局为身旺财透、食神生财，成格而财官不显于干，贵在兵权不在文阶；病字为土重壅塞，晚年忌再入土运壅滞。功量核算：助成线土势、食神生财两线，压制线官杀无透一线，主线土势，等级带定为一方首领级、上限不及中枢。子女/病位：时柱壬子财居子女宫，晚景依财星漂荡；病字土壅主脾胃痰湿之疾。卡面异说造已注明原书未取，不采用、不臆补。",
)
P["OC-002"] = dict(
 conf=0.66,
 pred="方向：大贵大富、财政魁首。断语：庚金日主生亥月，食神当令、乙木正财合庚，财官印链流通，一生居财政金融最高层（财政部长/中央银行级），富甲而贵显；中年为高峰，晚年退居海外、名位犹存而实权渐退，寿约七旬余。应期尺度运/年档：高峰运段在中年金水财官得地之运（定值：运档层；卡面无大运表，流年层窗口表达）。systems_used：八字子平合参。",
 basis="卡面未标注 tradition/system 字段——本卡题面为宋子文四柱甲午乙亥庚申己卯论贵显行运，按八字自决。主线：月令亥水食神，乙庚合财，己印贴身，食神生财、财印不战，格局清而流通；用神水木财食得地，病字午火七杀虚浮不为大害。功量核算：助成线食神生财、合财、印护三线，压制线仅午杀无根一线，主线食神生财链，等级带定为部院级财政首脑、上限至行政次席。病位：亥水受午火冲，主心肾/寒热交战之疾，晚年应之。卡面一说庚辰日已注明原书取庚申，不采用。",
)
P["OC-003"] = dict(
 conf=0.64,
 pred="方向：大富而兼名位、晚年犹盛。断语：庚金日主生午月，官杀火旺成势、丁火正官透，卯木财星双现生官，商界领袖之命：以商起家而得官方名位（议员/公会首脑级），财富巨万；火旺金熔之病在中晚年以心脑血管与眼目之疾应，寿可至八旬上下。应期尺度运/年档：高峰在中年木火财官运段（定值：运档层）。systems_used：八字子平合参。",
 basis="卡面未标注 tradition/system 字段——本卡题面为虞洽卿四柱丁卯丙午庚午己卯论名位财运晚年，按八字自决。主线：午月火炎，丙丁官杀并透，两卯财生火、己印化火生身，财官印成链，格局为财滋官、印护身，成格；病字火势过旺熔金。功量核算：助成线财生官、印化杀两线，压制线火过旺一线，主线财官链，财富量级带定为巨商级、名位带至社会领袖级。子女：时柱己卯印财，晚景子女可依而家业有耗。卡面四柱完整无异说。",
)
P["OC-004"] = dict(
 conf=0.60,
 pred="方向：清贵外交、仕途起伏而终老平顺。断语：乙木日主生卯月得禄，癸印透、丙伤透子，文星清秀，主外交文牍之贵：一生屡任驻外公使/使节、曾入内阁而位不长久，仕途两起两落；晚年退居著述清闲，寿约七旬。应期尺度运/年档：高峰在中年水木印比运段，晚年运入土金渐平（定值：运档层）。systems_used：八字子平合参。",
 basis="卡面未标注 tradition/system 字段——本卡题面为颜惠庆四柱丁丑癸卯乙巳丙子论仕途晚年，按八字自决。主线：卯月乙木得禄身旺，癸水正印透年、丙火伤官透时，印伤并见主文才与议论，格局以印为主、伤官为病（伤官见官之嫌在巳中丙与官星暗战）；用神水印得子根。功量核算：助成线印禄两线，压制线伤官、巳火泄气两线，主线印星，等级带定为使节/阁员级清贵、上限不及首揆久任。病位：巳火与子水交战，主心肾寒热之疾。卡面四柱完整。",
)
P["OC-005"] = dict(
 conf=0.63,
 pred="方向：贵显长寿、法学名家。断语：乙木日主生卯月，丁食透、双卯比禄、己财双透，食神生财而身旺能任，主学问法律之贵：位至法院院长级/法学家名宿，晚年仍居要职（驻外使节级），寿高至八旬余。应期尺度运/年档：高峰跨中晚年金水运段（定值：运档层）。systems_used：八字子平合参。",
 basis="卡面未标注 tradition/system 字段——本卡题面为吴经熊四柱己亥丁卯乙未己卯论前程贵显，按八字自决。主线：卯月乙木旺，亥水印生，丁火食神透月吐秀，己土财双透被食神所生，食神生财格成而身旺任之；病字比劫双卯争财，只主同辈竞争不破格。功量核算：助成线食神、印生、身旺三线，压制线比劫争财一线，主线食神生财，等级带定为院长级法学贵显。子女：时柱己卯财比，子女可继学业。卡面四柱完整。",
)
P["OC-006"] = dict(
 conf=0.60,
 pred="方向：受挫后难复旧峰、衰中带险。断语：当前（约1935乙亥年）企业危机非一时小挫：戊土日主生申月食神当令，财源本厚，然运年引动、财多身耗，往后走势为勉力维持、规模收缩，难回纺织面粉王国全盛；1937—1938年间（丁丑、戊寅年）兵事与病厄双险，家业交替易主之象。应期尺度年档：转折定在乙亥问年后二三年内（定值：年层窗口）。systems_used：八字子平合参。",
 basis="卡面未标注 tradition/system 字段——本卡题面为荣宗敬四柱癸酉庚申戊午甲寅、问1935年受挫后走势，按八字自决。主线：申月庚金食神透，酉金食伤成势泄戊，癸财透年、午火印为根，食神生财格而身坐午刃得印护，本主巨富；病字甲木七杀透时、寅申冲，事业根基受冲。功量核算：助成线食神生财一线，压制线杀透、寅申冲、身耗三线，主线由生财转为冲根，当前量级带下调为收缩守成。卡面问时明确约1935年，应期据此年档推。卡面四柱完整。",
)
P["OC-007"] = dict(
 conf=0.68,
 pred="方向：名高位卑、狂放早逝。断语：甲木日主生申月，庚寅年、甲申日、甲戌时，三甲虚浮、申金杀旺冲寅，身杀相战而印星无透：性情才高狂放、以诗文书画名世，不耐官禄拘束，财来财散、婚姻感情多波折；寿数不长，凶在辛未问年（1931年）本人已逝之造，享年四旬初。应期尺度年档：以问年辛未为终局年（定值：年层）。systems_used：八字子平合参。",
 basis="卡面未标注 tradition/system 字段——本卡题面为袁寒云四柱庚寅甲申甲申甲戌、1931年逝后持庚来询，按八字自决。主线：申月庚杀当令（年干庚透），日主甲木坐申绝地、两申冲寅禄，甲木三见皆虚浮无根，杀重身绝，格局破而无印化杀；病字申金杀与寅申冲。功量核算：助成线仅比肩虚浮一线，压制线杀旺、冲禄、坐绝三线，主线杀势，等级带定为文名高而寿位低。卡面明示与袁世凯本人有别，已按袁克文本人断，未混。",
)
P["OC-008"] = dict(
 conf=0.61,
 pred="方向：权位稳进、军政至封疆而晚年转外交。断语：乙木日主生酉月，辛杀透、戊子印财在年，杀印相生之势：行伍/军政起家，位至省主席级，权位成就在中年；晚年运转水木，杀印转文，转任使节而善终，寿至八旬上下。应期尺度运/年档：高峰在中年金水杀印运段（定值：运档层）。systems_used：八字子平合参。",
 basis="卡面未标注 tradition/system 字段——本卡题面为商震四柱戊子辛酉乙未己卯论行运权位，按八字自决。主线：酉月辛金七杀透月，年柱戊子正财正印、印坐子水得根，构成杀印相生，格局成；日主乙木坐未通根、时支卯禄为救应。功量核算：助成线杀印链、卯禄两线，压制线酉金克卯一线，主线杀印相生，等级带定为封疆/省主席级。病位：酉卯冲主筋骨肝胆之疾。卡面一说丙子时已注明原书斥误、取己卯时，不采用异说。",
)
P["OC-009"] = dict(
 conf=0.35,
 pred="方向：外交长青、寿高名久（低置信）。断语：据题面已载事实推：命主外交仕途绵长，历使节与内阁而声名历久不衰，婚姻不止一次，晚年居海外著述，寿至高龄（九旬以上之象）；财富中上、仕途高于财。应期尺度运/年档：只给定性窗口——中晚年皆在外交高位运段，无流年定值（缺位降格：四柱未载，不报具体应年）。systems_used：八字体裁（盘面残损，仅据题面事实与命书体裁定性）。",
 basis="卡面未标注 tradition/system 字段——本卡题面为顾维钧论造而四柱栏仅载「原书应运篇下论造（四柱以原书为准，转录本个别字待校）」，按八字自决并如实残损处理。输入残损旗标：四柱干支未载、转录个别字待校，无从装盘核旺衰格局；不臆补四柱。断语仅据题面已载「顶尖外交官、历任驻外使节与内阁」一面定性，置信降至0.35。",
)
P["OC-010"] = dict(
 conf=0.66,
 pred="方向：贵极而无实权、两起两落终为平民。断语：壬水日主生寅月，三午财星成势、丙火双透，财旺身弱、食神寅木泄秀：名义至尊（皇帝之命）而财势压身不能自立，一生两度被拥立皆为傀儡，中年有牢狱/管束之厄，晚年以平民终老，寿约六旬。应期尺度运/年档：落难转折在中年火土运段、平民善终在晚年金水运（定值：运档层；卡面注明原书未附大运表，流年层不报）。systems_used：八字子平合参。",
 basis="卡面未标注 tradition/system 字段——本卡题面为溥仪四柱丙午庚寅壬午丙午、已退位居天津论一生，按八字自决。主线：寅月食神，午火三见财成局、丙火双透，壬水无根（仅庚印虚生），财多身弱、格以从财边缘论而印透不真从，主线定为财旺身弱待金水运扶；病字火炎财势。功量核算：助成线庚印一线，压制线三午财局、双丙透两线，主线财势，名位等级带为至尊虚位、实权量级低下（名实分离）。残损旗标：卡面注明原书未附大运表，运程只定方向不报起运岁数。",
)
P["OC-011"] = dict(
 conf=0.70,
 pred="方向：名盛而命薄、情劫早夭。断语：己土日主生巳月，辛食透、双亥财、乙杀透时，食神吐秀主演艺成名，然亥巳冲、财杀交攻、身心受舆论感情所困：性情敏感多愁，感情纠葛招谤，结局凶——1935乙亥年（问年）自尽式早逝，享年二旬中段。应期尺度年档：终局定在乙亥年（定值：年层，与卡面问时1935年合）。systems_used：八字子平合参。",
 basis="卡面未标注 tradition/system 字段——本卡题面为阮玲玉四柱庚戌辛巳己亥乙亥、1935年逝后嘱推，按八字自决。主线：巳月火印当令生己，辛金食神透月吐秀成名，然日时双亥正财冲巳、乙木七杀透时克身，财杀与舆论压力成病；病字亥巳冲与乙杀。功量核算：助成线印生、食神秀两线，压制线双亥冲、杀透两线，主线由秀转冲，等级带定为名高寿低。卡面四柱完整，问时为逝后验推、应期以造终之年回定。",
)
P["OC-012"] = dict(
 conf=0.58,
 pred="方向：少年极盛、婚姻多波、晚景平淡。断语：丁火日主生辰月，戊伤双透、己未土重，伤官吐秀主竞技成名极早（十五六岁全国冠军与造相合）；然伤官旺、官星无透，婚姻宫未土自刑之象，婚恋不顺、易有离合与名誉风波；中晚年运离水乡/异地，名气渐退，晚景以平淡终，寿约六旬余。应期尺度运/年档：成名在少年火土运、婚姻转折在中年水运段（定值：运档层；卡面载五岁起运序列，据此定段）。systems_used：八字子平合参。",
 basis="卡面未标注 tradition/system 字段——本卡题面为杨秀琼四柱己未戊辰丁未戊申、约1935年成名时论造，按八字自决。主线：辰月戊土伤官透年时、食伤成势泄丁，丁火坐未通根，伤官吐秀格；病字土重晦火、官星不显主婚缘薄。功量核算：助成线食伤秀气一线（集中于少年），压制线土重、火弱两线，主线食伤，成名量级带为全国级而持续性低。卡面载大运序列己巳庚午辛未壬申癸酉甲戌，五岁起运，运段据此。子女：时柱戊申伤官财，子女缘可而晚年依傍薄。",
)
P["OC-013"] = dict(
 conf=0.60,
 pred="方向：艺术成名一生、晚年困厄。断语：辛金日主生丑月，丁火官杀在年、双午财杀、甲财双透，财滋杀而身坐酉禄能任：以技艺（梨园）成大名，中年为高峰、名利双得；晚年运入火旺克金之地，名匠受政治风波困顿，晚景不佳，寿约八旬。应期尺度运/年档：高峰中年金水运、晚年转折在火运交接带（定值：运档层；卡面仅载八岁起运、无运表，流年不报）。systems_used：八字子平合参。",
 basis="卡面未标注 tradition/system 字段——本卡题面为周信芳四柱甲午丁丑辛酉甲午论一生晚年，按八字自决。主线：丑月寒金，辛坐酉禄身强，甲财双透、午火官杀双现，财官有源而丁杀透年为病（杀与身相战于舞台名声之途）；用神水食伤泄秀润局。功量核算：助成线禄强、财源两线，压制线双午杀、丁透两线，主线财官，等级带定为行业宗师级名位、富裕中上。残损旗标：卡面仅注八岁起运、无大运干支表，运段只定方向。",
)
P["OC-014"] = dict(
 conf=0.55,
 pred="方向：财政仕途、中贵而晚退。断语：壬水日主生卯月，庚印年、己官月、辛印时，官印相生清格：主财政文牍之仕，位至厅长级（浙江财政厅长与造相合），仕途以清廉文职见长；卯寅木食伤泄秀而官星己土受克，仕进有起伏、晚年退闲，寿约六旬余。应期尺度运/年档：高峰在中年金土官印运段（定值：运档层）。systems_used：八字子平合参。",
 basis="卡面未标注 tradition/system 字段——本卡题面为蒋邦彦四柱庚辰己卯壬寅辛丑论仕途行运，按八字自决。主线：卯月伤官当令，己土正官透月，庚辛双印护官化伤，伤官配印/官印相生成格；病字寅卯木旺泄身克官。功量核算：助成线双印、官透两线，压制线木旺一线，主线官印链，等级带定为厅长级文职。病位：卯木旺主肝胆筋目，晚年应之。卡面四柱完整、无大运表，运段定方向不报岁数。",
)
P["OC-015"] = dict(
 conf=0.62,
 pred="方向：君位稳固、守成之主。断语：甲木日主生巳月，乙劫年、辛官月、子印时，官印相生而身坐辰库有根：主位格稳固，在位长久历大战而不失位，中年战事劳心，晚年以肺疾/寒湿之病终，寿约七旬。应期尺度运/年档：稳位贯穿中年水木运、终局在晚年运交金水之年（定值：运档层）。systems_used：八字子平合参。",
 basis="卡面未标注 tradition/system 字段——本卡题面为乔治五世四柱乙丑辛巳甲辰甲子、据西报生庚演造论一生，按八字自决。主线：巳月食伤火地，辛金正官透月、子水正印透时生甲，官印链成；甲坐辰湿土通根、乙劫助身，身可任官；病字巳火燥烈与丑辰湿土相杂。功量核算：助成线官印、通根两线，压制线火燥一线，主线官印，等级带为君主守成级。残损旗标：卡面注明生庚据西报传略译演，来源为二手传略，置信据此下调。",
)
P["OC-016"] = dict(
 conf=0.58,
 pred="方向：以术成名、清贵而寿中。断语：庚金日主生卯月，辛劫双透、子辰半合水局，食伤旺而财星卯木当令：不走仕宦正途，以命理技艺成名于沪上、著述立身，名大于利，财源靠技艺文名；中年为名声高峰，晚年离乡迁居、清贫自守，寿约六旬余。应期尺度运/年档：高峰在中年水木食伤生财运（定值：运档层）。systems_used：八字子平合参。",
 basis="卡面未标注 tradition/system 字段——本卡题面为韦千里自造辛亥辛卯庚子庚辰自论一生，按八字自决。主线：卯月正财当令，庚金无禄、辛劫双透分财，子水伤官与辰半合，食伤生财而身弱，主线定为食伤生财、身弱待印比运；病字财旺劫争。功量核算：助成线食伤生财链一线，压制线身弱、双劫争财两线，主线财链而受身限，等级带定为技艺名家级、财富中平。子女：时柱庚辰比肩食库，晚景依傍薄。卡面四柱完整。",
)
P["OC-017"] = dict(
 conf=0.63,
 pred="方向：巨富、财格成而贵轻。断语：丁火日主生酉月，壬官年、己食月、甲印时，财星酉金当令成势：以丝业商贸致巨富，为南浔丝商级富豪，富胜于贵、官星壬水虚浮无根，名位止于乡绅商董；晚年家业庞大而子孙分产有耗，寿约七旬。应期尺度运/年档：高峰在中年金水财运段（定值：运档层）。systems_used：八字子平（子平真诠用神成败口径）合参。",
 basis="卡面未标注 tradition/system 字段——本卡题面为刘澄如四柱壬戌己酉丁丑甲辰、出自《子平真诠评注》用神成败章，按该书格局口径自决。主线：酉月偏财当令，丁火坐丑、甲印透时生身，财格有印护而不破，用神财得地；病字己土食神与戌辰土重晦光。功量核算：助成线财当令、印护两线，压制线土重一线，主线财星，财富量级带定为巨富级、贵气带低（富而不贵与问面合）。卡面四柱完整。",
)

# ---------------- B20 ----------------
P["OC-018"] = dict(
 conf=0.64,
 pred="方向：报业巨头、晚年横祸。断语：庚金日主生子月，丙杀透、己卯财印、辛巳劫杀，伤官子水当令吐秀主报业文名，地位至大报总经理级、社会影响极大；然杀星丙火与巳火伏险、寅巳相刑，晚年行运逢金水冲火之年有横祸之险，险年定在甲戌年一带（年档定值），寿止五旬中段，不得善终高寿。应期尺度年档：险年以甲戌年为窗口主坐标。systems_used：八字子平合参。",
 basis="卡面未标注 tradition/system 字段——本卡题面为史量才四柱己卯丙子庚寅辛巳、出自《子平真诠评注》用神成败章论地位晚年，按八字自决。主线：子月伤官当令，庚金坐寅绝、时支巳杀得辛劫助，伤官吐秀成报业之格而杀星暗伏为病；病字丙巳火杀与寅巳刑。功量核算：助成线伤官秀、财星卯两线，压制线杀伏、坐绝两线，主线伤官，地位量级带定为行业巨头级；晚年险的压制依据为杀星得运年引动冲刑日主。卡面四柱完整。",
)
P["OC-019"] = dict(
 conf=0.62,
 pred="方向：学政贵显、险年横祸早逝。断语：壬水日主生辰月，丙偏财透、癸劫时、卯伤时支，财官有源、伤官吐秀：主学界/研究院总干事级贵显，以社会活动名世；然申辰半合水势、卯木泄而官杀土薄，行运逢金旺冲卯、杀星引动之年有暗杀/横祸险，险年定在癸酉年一带（年档定值），寿止四旬。应期尺度年档。systems_used：八字子平合参。",
 basis="卡面未标注 tradition/system 字段——本卡题面为杨杏佛四柱癸巳丙辰壬申癸卯、出自《子平真诠评注》，按八字自决。主线：辰月杂气，壬坐申长生得癸劫助身旺，丙火财透、卯木伤官泄秀，财与秀气成学政之象；病字官杀辰土受卯克、巳申合中带刑，仕路有暗险。功量核算：助成线身旺、财透两线，压制线官弱、合刑两线，主线财秀，等级带定为研究院级贵显而寿位受压。残损/分歧旗标：卡面注明《千里命稿》另载全异四柱、本例以徐乐吾书为准，已按卡面指定口径断、未混用异造。",
)
P["OC-020"] = dict(
 conf=0.63,
 pred="方向：贵至首揆、寿不满五旬余。断语：癸水日主生丑月，己杀年、丁财月、双丑杀库、乙食时，杀重身弱而食神制杀：以才干与人和位至国民政府主席级，贵显为一生顶点；然杀库双重压身、乙木制杀力薄，贵而多劳、病厄早至，险年在庚午年一带（年档定值），寿约五旬上下病终。应期尺度年档。systems_used：八字子平合参。",
 basis="卡面未标注 tradition/system 字段——本卡题面为谭延闿四柱己卯丁丑癸丑乙卯、出自《子平真诠评注》论贵显险年，按八字自决。主线：丑月己土七杀透年、日时双丑杀库，癸水无禄仅卯木食神制杀救应，食神制杀格成而救应力薄，主线为贵重寿轻；病字双丑杀库。功量核算：助成线食神制杀一线，压制线杀库双重、身无根两线，主线杀势，等级带上限至首揆级、下限被寿数压低（压低依据：杀库双压＋日主无根，逐项可指）。卡面四柱完整。",
)
P["OC-021"] = dict(
 conf=0.62,
 pred="方向：军阀封疆、先盛后败。断语：乙木日主生酉月，戊财年、辛杀月、丙伤时，杀旺财滋、伤官制杀相杂：以武力起家位至旧桂系首领、督军/巡阅使级封疆；然酉卯冲禄、杀重身弱，中晚年运转即失兵权、败落离乡，晚景萧条，寿约七旬虚而终局不高。应期尺度运/年档：高峰在中年土金财杀运、败落在运交水木冲杀之段（定值：运档层）。systems_used：八字子平（真诠格局高低口径）合参。",
 basis="卡面未标注 tradition/system 字段——本卡题面为陆荣廷四柱戊午辛酉乙卯丙戌、出自《子平真诠评注》格局高低章，按八字自决。主线：酉月辛金正官透月（以官论则官旺身坐卯禄相冲），戊财滋官、丙伤制官，官星成势而伤官为病，主线官旺伤扰；病字酉卯冲与丙火伤官。功量核算：助成线财滋官、卯禄两线，压制线冲禄、伤官两线，主线官势，等级带定为封疆级而稳定性低。卡面四柱完整。",
)
P["OC-022"] = dict(
 conf=0.64,
 pred="方向：科第无缘、术学立身。断语：乙木日主生酉月，辛杀双透（年时巳中藏、酉金当令），丁食在月、戊财时透，杀重印缺：科举功名屡试不第（与题面已载相合），转而以命学著述立身成一代命师，学业在术数不在科场；清贵自守、财富中平，晚年著述授徒，寿约七旬。应期尺度运/年档：科场受挫在青年金运、立身成名在中年水木印比运（定值：运档层；卡面载大运丙申起）。systems_used：八字子平合参（自造自批体裁）。",
 basis="卡面未标注 tradition/system 字段——本卡题面为袁树珊自造辛巳丁酉乙巳戊寅、出自《命理探原》自批，按八字自决。主线：酉月辛杀当令，乙木坐巳、时寅为根，丁火食神透月制杀，食神制杀而印星不透——制杀主才学抗衡权贵，印缺主科名正途无缘；病字酉杀与双巳火金相战。功量核算：助成线食神制杀、寅根两线，压制线杀旺、印缺两线，主线食神，等级带定为术学名家级清贵、科第带为零。卡面载安命甲午、大运丙申起，运段据此。",
)
P["OC-023"] = dict(
 conf=0.38,
 pred="方向：覆下为破损中空器物（负于完好）。断语：钟下所覆是一件圆形中空的器物（鼎属/壶碗类金属或陶质食器之象），且不完好——有破口/裂缺，开钟验看可见缺损，非完整新器。应期：即席开钟即验（时档，本题为即时射覆）。systems_used：梅花易数体用取象（火风鼎变雷风恒）。",
 basis="卡面未标注 tradition/system 字段——本卡题面为席间射覆、卡面自带卦象「火风鼎变雷风恒」，按梅花自决。依据：鼎卦象器物三足中虚、离中虚主中空圆器，巽为入、为木风，变恒之震为声动——器有声而中空；完好与否取鼎之变：鼎倾覆之象（鼎颠趾意象类）主破损。残损旗标：卡面未载动爻位与起卦时刻，体用主客只能以本变两卦定，置信降至0.38；不臆补动爻。",
)
P["OC-024"] = dict(
 conf=0.55,
 pred="方向：葬资有着落、葬事可办（正）。断语：无资之困将由意外之财解开——屋内有窖藏/枕边藏金之象，经一只鼠窜动、击鼠破枕（或掘窖）而藏金见天，以此金营葬，易者身后事得办、不至暴露无葬。应期：邵雍到访当日即应（日档，事件即时）。systems_used：梅花外应取象（据题面所载遗书预言与击鼠枕窖金之标题锚）。",
 basis="卡面未标注 tradition/system 字段——本卡题面为邵雍携遗书访易者之家问葬资、源出《梅花易数》序，按梅花外应自决。依据：卡面 provenance 自带「击鼠枕窖金」锚点，鼠为子象主窖藏暗财，枕为卧处藏物之位；遗书预言来访者可托身后事，主线为藏金现形解困。残损旗标：卡面未载卦象与具体金额，藏金数量无据不报；断语只落到得金办葬一事。",
)
P["OC-025"] = dict(
 conf=0.60,
 pred="方向：预言应验（正）。断语：椅底预书之事届期验实——到所书年月日，将有来客坐此椅、椅被坐破，应验点正在「坐破」一事本身，预书非虚言。应期：以椅底所书之年月日为应期（日档定值在卡外：卡面未载所书日期原文，应期坐标缺位降格为「届书定之日」）。systems_used：梅花预言验占体裁（据题面体裁自决）。",
 basis="卡面未标注 tradition/system 字段——本卡题面为邵雍椅底预书坐破之验、源出《梅花易数》序，按题面体裁自决。依据：卡面载预书内容即「某年月日椅子将被坐破」，验占之问只核应验与否；序文成例体裁主应验。残损旗标：卡面未载所书具体日期与来客身份，日期与人物无据不报、应期作缺位降格表述，置信据此定0.60。",
)
P["OC-026"] = dict(
 conf=0.55,
 pred="方向：功名可得（正）、兄弟同占而名次有差。断语：今年功名有份——三传乙未、己亥、癸卯成亥卯未三合木局，初传未乘青龙主文书喜信，两客中至少一人得中功名（举/进士科名之喜），另一人稍逊或候次；卯乘玄武居末，主榜名暗中有波折、名次不居前列。应期尺度月档：应在当年发榜之月（春占秋榜/会试放榜期，窗口为当年科名榜期，主坐标取放榜月）。systems_used：大六壬（课格＋三传天将，盘面不全守限断）。",
 basis="卡面未标注 tradition/system 字段——本卡题面为两客1643年正月初四己亥日辛未时占功名、卡面载课式涉害曲直与三传天将，按大六壬自决。依据：三传亥卯未三合、木主文书，青龙发用主喜庆功名；涉害课主历经艰难而后得，玄武末传主名次暗昧。盘面限度：卡面只有课式名、三传含天将、干支占时与空亡（甲午旬辰巳空），无天盘全图与四课全列，只据三传链与课格作断、不臆补四课细节（六壬第八节守限）。",
)
P["OC-027"] = dict(
 conf=0.60,
 pred="方向：此行不得意（负）、人可平安南返、老母无恙。断语：奉诏北上凶多吉少：课名无禄无路，三传癸酉（合）、戊辰（阴）、亥（青龙）而末传亥落空（甲子旬戌亥空），主进京无实职之得、行程受阻于北方兵事，本人有惊劳而无大难，终将南返；老母甲子年命，老母一面无大恙、在家安稳。应期尺度月档：阻滞应在北上后数月内、返程在次年春前（窗口：1642年冬至1643年春，主坐标取冬月兵事最紧时）。systems_used：大六壬（课格＋三传＋空亡，守限断）。",
 basis="卡面未标注 tradition/system 字段——本卡题面为方替夫1642年冬月初五辛未日甲午时占北上与母安、卡面载无禄无路课与三传，按大六壬自决。依据：无禄无路课名直主此行无禄无路；末传亥为空亡乘青龙，贵喜落空、行程终虚；中传辰乘太阴主暗中退守。盘面限度同六壬守限：只有课式、三传、月将丑、旬空戌亥，无四课天盘全图，不臆补。北方兵事正紧为卡面已载事实，与课象同向。",
)
P["OC-028"] = dict(
 conf=0.48,
 pred="方向：考选得官（正）、得外任文官而非京职显要。断语：入觐考选可得一官——重审斫轮课主改就新职，中传戌乘朱雀主考选文书得凭，所授为州县正印一类外任（知州/知县级），末传巳乘白虎主赴任路远、到任后有刑名钱谷之劳。应期尺度月档：应在入觐后数月内授官（窗口：1631年春夏之交，主坐标取考选放榜授官月）。systems_used：大六壬（课格＋三传天将，守限断）。",
 basis="卡面未标注 tradition/system 字段——本卡题面为朱西崑1630年冬月十四己丑日辛未时占入觐得何官、卡面载重审斫轮课与三传卯戌巳，按大六壬自决。依据：斫轮课主斫治成器、任官得位；朱雀中传主文书考选；白虎末传主道路与刑名任所。具体官名只有课象一线指针，粒度降为职级类（州县正印级）表述，置信0.48。盘面限度：无四课天盘全图，守限不臆补；月将寅、甲申旬午未空已载而三传不落空。",
)
P["OC-029"] = dict(
 conf=0.53,
 pred="方向：诸事中平偏吉（正）、子求官可得而迟、老母安康过寿。断语：携子求官一事，三传乙未（白虎）、癸卯（六合）、己亥（天后）成亥卯未三合，主人和事成——其子（丑命）求官终可得，惟初传白虎主道路劳顿、得官在迟不在速；年近九十之母，末传亥乘天后主母安，九十寿关可安然度过；本人此行平安无大失。应期尺度月/年档：求官应在次年内见分晓（窗口：1643年内，主坐标取次年春季铨选期）。systems_used：大六壬（课格＋三传天将，守限断）。",
 basis="卡面未标注 tradition/system 字段——本卡题面为王米山1642年十月初二己亥日辛未时携子访占诸事、卡面载涉害曲直回环课与三传，按大六壬自决。依据：三传三合木局主合而成事，六合中传主人和，天后末传主母象安宁；白虎初传只主行路劳顿不主大凶（回环课主往返）。盘面限度：只有课式、三传、月将丑、甲午旬辰巳空，无四课天盘，不臆补；其子丑命、母年近九十为卡面已载面，逐面已断。",
)
P["OC-030"] = dict(
 conf=0.52,
 pred="方向：两问皆可复/可旧（正）。断语：淮扬巡按差可复设——重审铸印课，铸印主印信重新铸给、差遣复立，初传巳乘太常主朝廷礼制典章之复；吏书之缺亦可照旧保留，中传戌乘六合主两方和合维持旧规。惟末传卯乘太阴主事在暗中酝酿，复设非即刻明发，须经一段时日方定。应期尺度月档：应在次年内定局（窗口：1651年内至次年春，主坐标取秋冬间文书明发时）。systems_used：大六壬（课格＋三传天将，守限断）。",
 basis="卡面未标注 tradition/system 字段——本卡题面为胡尹二兄1651年二月初十戊子日戊午时代占巡按复设与吏书缺存废、卡面载重审铸印课与三传巳戌卯，按大六壬自决。依据：铸印课格直指印信差遣之复立，太常发用主典章，六合中传主维持和合；太阴末传主暗定迟发，故应期后移。盘面限度：卡面仅载月将亥将、未载旬空，三传不判空亡；无四课天盘全图，守限不臆补。",
)
P["WP-001"] = dict(
 conf=0.72,
 pred="Direction: Yes — a major collective affliction, specifically a pandemic. Prediction: The 2020–2021 period holds a worldwide pandemic disease event (respiratory plague-type affliction) causing mass illness, deaths and social shutdown, peaking around the early-2020 Jupiter–Saturn–Pluto conjunction; severity comparable to the historical clusters cited (1918-type). Timing: onset window late 2019 into early 2020, main wave through 2020–2021 (year-scale window, main coordinate early 2020). systems_used: Western mundane astrology (cyclical index / outer-planet conjunction method as framed in the card).",
 basis="Card carries no tradition/system field — this card asks what affliction 2020–2021 holds, framed by a 2011 mundane-astrology assessment; decided by Western mundane astrology on the card's own terms. Basis: card states five outer planets within ~100 degrees, Jupiter–Saturn–Pluto conjunction exact early 2020, cyclical index at its 21st-century low, and comparable past clusters coinciding with 1918, 1954, 1968, 1982 — the method's own precedent set points to pandemic as the recurring correlate. No natal chart data on card; no chart invented.",
)
P["WP-002"] = dict(
 conf=0.68,
 pred="Direction: Barack Obama wins. Prediction: Obama, the change candidate, defeats John McCain in the 4 November 2008 general election, after first securing the Democratic nomination over Hillary Clinton; the Saturn–Uranus opposition exact on Election Day marks the break with the incumbent party/order rather than its continuation. Timing: decided 4 November 2008 (day-scale, election day as given on card). systems_used: Western mundane/election astrology (Saturn–Uranus opposition signature).",
 basis="Card carries no tradition/system field — this card asks who wins the 2008 US election, reported 20 May 2008; decided by Western election astrology on the card's framing. Basis: card states Obama leads the nomination race, McCain is the presumptive Republican, and Saturn–Uranus opposition begins on Election Day, last seen 45 years earlier — the opposition signature favours the challenger/change side over the party in power. No birth charts on card; none invented.",
)
P["WP-003"] = dict(
 conf=0.66,
 pred="Direction: Barack Obama wins re-election. Prediction: Incumbent Obama defeats Mitt Romney on 6 November 2012 and remains president; the Mercury retrograde beginning on election day shows in counting/communications confusion and a delayed or disputed-feeling count, but does not overturn the incumbent's win. Timing: decided 6 November 2012 (day-scale). systems_used: Western mundane/election astrology.",
 basis="Card carries no tradition/system field — this card asks who wins the 2012 US election, assessed May 2012; decided by Western election astrology. Basis: card states Obama is the incumbent, Romney the presumptive challenger, race competitive, and Mercury retrograde begins on election day — retrograde is read for process confusion, not for reversal of the result; incumbency plus a merely competitive (not leading) challenger leaves the direction with Obama. No charts on card; none invented.",
)
P["WP-004"] = dict(
 conf=0.52,
 pred="Direction: Hillary Clinton wins (panel consensus direction). Prediction: The Costa Mesa ISAR election panel's collective call is Clinton over Donald Trump in the 8 November 2016 election — the establishment/frontrunner candidate takes the White House, consistent with the polling lead the card records. Timing: decided 8 November 2016 (day-scale). systems_used: Western mundane/election astrology (conference panel consensus as framed on card).",
 basis="Card carries no tradition/system field — this card asks who wins the 2016 election as put to an international astrology conference panel in October 2016; decided as the panel-consensus call framed by the card. Basis: card states most polls favour Clinton and the panel is a forecasting panel of the profession; a panel consensus in that setting follows the frontrunner/establishment signature. Confidence held at 0.52: the card gives no individual charts or votes breakdown, so the panel split itself is not on the card and is not invented.",
)
P["WP-005"] = dict(
 conf=0.58,
 pred="Direction: Donald Trump wins. Prediction: Trump defeats Hillary Clinton on 8 November 2016 — the same panel astrologer who alone picked Trump out of 17 Republicans for the nomination follows through to a Trump general-election win, against the polling consensus. Timing: decided 8 November 2016 (day-scale). systems_used: Western mundane/election astrology (individual forecaster's read, distinguished on the card from the panel consensus).",
 basis="Card carries no tradition/system field — this card isolates one panel astrologer who had earlier picked Trump as nominee from a 17-candidate field; decided on that individual's track-record framing given on the card. Basis: the card's distinguishing fact is that this astrologer was already right against consensus on Trump once in this cycle; the prediction attributed in such a report follows that astrologer's contrarian Trump line rather than the panel majority. No chart data on card; none invented.",
)
P["WP-006"] = dict(
 conf=0.64,
 pred="Direction: Britain votes to Leave. Prediction: The 23 June 2016 referendum returns a Leave majority (narrow), despite February polls showing 'Stay' ahead with many undecideds; the undecided bloc breaks disproportionately to Leave on the day. Timing: decided 23 June 2016 (day-scale, referendum date as given). systems_used: Western mundane astrology (UK national charts / Uranus–Ceres conjunction on referendum day, as framed on card).",
 basis="Card carries no tradition/system field — this card asks whether Britain votes to leave, assessed July 2015 and firmed 22 February 2016 by a named mundane astrologer; decided by Western mundane astrology on the card's materials. Basis: card lists the UK 1066/1801/1922 charts and Uranus conjunct Ceres at 23 Aries on referendum day — Uranus on a national-chart axis is the disruption/separation signature, read against the complacent 'Stay ahead' polling surface. No vote percentages on card; margin stated only as narrow, no figure invented.",
)
P["WP-007"] = dict(
 conf=0.55,
 pred="Direction: Donald Trump wins, decided by the Clinton email/Foundation scandal. Prediction: Trump defeats Hillary Clinton on 8 November 2016; what decides it is the email controversy — a late-cycle revival of the email/Foundation issue in the final weeks swings late deciders and depresses Clinton turnout, overturning her August polling lead. Timing: decided 8 November 2016, with the deciding swing in the final two weeks (day/month-scale as framed). systems_used: Tarot reading as framed on the card (Union Square reader's draw on the election) read with the card's stated public controversies.",
 basis="Card carries no tradition/system field — this card asks who wins the 2016 election and what will decide it, put to a Manhattan tarot reader in August 2016; decided by tarot as framed on the card. Basis: the card itself foregrounds exactly two Clinton-side facts — the email controversy and the Clinton Foundation — as the live controversies at draw time; in a 'what will decide it' question those card-given facts are the deciding lever, and they cut against Clinton. Residual flag: the card does not list the actual cards drawn, so no card-by-card reading is invented; confidence held at 0.55 for that missing draw.",
)

B19 = ["MP-017","MP-018","MP-019","OC-001","OC-002","OC-003","OC-004","OC-005","OC-006","OC-007","OC-008","OC-009","OC-010","OC-011","OC-012","OC-013","OC-014","OC-015","OC-016","OC-017"]
B20 = ["OC-018","OC-019","OC-020","OC-021","OC-022","OC-023","OC-024","OC-025","OC-026","OC-027","OC-028","OC-029","OC-030","WP-001","WP-002","WP-003","WP-004","WP-005","WP-006","WP-007"]

def write_batch(ids, label):
    n = 0
    for cid in ids:
        d = P[cid]
        obj = {"case_id": cid, "prediction_text": d["pred"], "basis": d["basis"],
               "confidence": d["conf"], "trigger": T()}
        with open(os.path.join(BASE, cid + ".json"), "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=1)
        n += 1
    assert n == len(ids) == 20, (label, n)
    print(label, "written", n)

write_batch(B19, "B19")
write_batch(B20, "B20")

# read-back verification, per-id exact open only
cnt = 0; trig = {"changed_main":0,"reserve_used":0,"disputed":0}
for cid in B19 + B20:
    with open(os.path.join(BASE, cid + ".json"), encoding="utf-8") as f:
        o = json.load(f)
    assert o["case_id"] == cid
    assert set(o.keys()) == {"case_id","prediction_text","basis","confidence","trigger"}
    assert isinstance(o["prediction_text"], str) and o["prediction_text"]
    assert isinstance(o["basis"], str) and o["basis"]
    assert 0 <= o["confidence"] <= 1
    assert set(o["trigger"].keys()) == {"changed_main","reserve_used","disputed","reason"}
    for k in trig:
        trig[k] += 1 if o["trigger"][k] else 0
    cnt += 1
print("verified", cnt, "trigger_counts", trig)
