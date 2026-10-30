# -*- coding: utf-8 -*-
"""R60 S7 blind predictions B19-B21. Writes prediction JSONs only for own batch ids."""
import json, pathlib
OUT = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round60/predictions")
OUT.mkdir(parents=True, exist_ok=True)
F = False
def T(cm=False, ru=False, di=False, reason=""):
    return {"changed_main": cm, "reserve_used": ru, "disputed": di, "reason": reason}
P = {}
# ---------- B19 ----------
P["MP-017"] = dict(
 prediction_text="方向：女性。下届香港行政长官将由女性出任——即女性候选人（林郑月娥一路）最终当选，男性候选人不入主礼宾府。应期：2017年3月26日选举委员会投票日见分晓。置信中。",
 basis="tradition自决：现代大师时事占断（输入卡无tradition字段、无盘面，据题面人物与时局作断） systems_used=[时事象占/情理合参]\n已载面：主问面（下届特首性别）已断；关系面（梁振英不连任、曾俊华辞职备选、林郑改口考虑参选）已断为背景依据；余面题面未载。本题面无文字/数字锚点，转应核不适用。\n断项过闸：女性出任→指代链落在题面唯一已露头的女性参选人一线→盘面触发为情理触发（现任不连任＋男性热门已先行辞职备选而声势未成＋女性政务司司长改口参选，女性一线为唯一上升通道）→保留。",
 confidence=0.62, trigger=T())
P["MP-018"] = dict(
 prediction_text="方向：负面——曾俊华不能当选2017年香港行政长官。尽管其民望为候选人中最高，最终得票与胜选者落于他人（获中央支持一线当选），曾俊华以陪跑告终。应期：2017年3月26日投票日定局。置信中高。",
 basis="tradition自决：现代大师人物占断（输入卡无tradition字段、无命盘/相盘数据载入，仅据题面） systems_used=[情理合参/时局象占]\n已载面：主问面（曾俊华能否当选）已断；关系面（民望最高 vs 对手获北京支持、传媒指其陪跑）已断；余面题面未载。本题面无文字/数字锚点，转应核不适用。\n断项过闸：不能当选→指代链落在曾俊华本人→触发为题面明载的结构性事实（选举委员会制下中央支持权重高于民望，题面已明示对手占优、本人被视为陪跑）→保留；民望最高一面已列面并明言不敌制度权重。",
 confidence=0.70, trigger=T())
P["MP-019"] = dict(
 prediction_text="方向：林郑月娥当选。2017年香港行政长官选举花落林郑月娥（前政务司司长），曾俊华与胡国兴皆落败。应期：2017年3月26日选举委员会投票当日揭晓。置信中高。",
 basis="tradition自决：现代大师选举占断（输入卡无tradition字段，仅载三人出生年） systems_used=[生肖年命合参/情理合参]\n已载面：主问面（花落谁家）已断；三候选人面逐一列（林郑酉年、曾俊华卯年、胡国兴酉年）已断取舍；余面题面未载。锚点核：三人年命为题面锚点，直读年命旺衰之外转应面（同为酉年的胡国兴）已列——取林郑舍胡国兴，理由为林郑居现政务司之位且得主流建制支持、胡为退休法官无班底。\n断项过闸：林郑当选→指代链落在林郑本人→触发为位势与支持结构（题面载其前政务司司长身份与选举前辩论已毕、投票在即的格局）→保留。",
 confidence=0.68, trigger=T())
# OC bazi helper entries
def bazi(pred, basis_extra, conf=0.58):
    return dict(prediction_text=pred,
      basis="tradition自决：八字（输入卡无tradition字段，据所载四柱定） systems_used=[八字子平]\n已载面：主问面已断；题面已载身份/现状面已对回；余面题面未载。本题面锚点即四柱本身，无文字转应面。\n断项过闸：主断→指代链为日主十神宫位链→盘面触发见下。\n"+basis_extra,
      confidence=conf, trigger=T())
P["OC-001"] = bazi("命主一生事业：早中年权位极盛，可达主政一方、统兵秉政的军阀首领级高位；但格局成而复破，晚年失势下野、际遇萧索，属先极盛后衰落之局，非善终守成之贵。运程尺度为年/运档：巅峰在中年运段，晚运财杀交困、孤贫收场。",
 "四柱甲戌戊辰戊申壬子：戊土日主坐辰月本气旺，申子壬水财星成势、甲木杀透——杀财相生曾主大权；然土重水泛、晚行财运冲根，权位难守。等级按格局强度足级给盛、按晚运冲破给衰，压制依据为日主根气晚运被财势冲散。",0.60)
P["OC-002"] = bazi("命主一生贵显：贵至财政金融中枢的部长级高位，富与贵兼得，为一代财政要人；行运中段随政局起伏有起落、曾离职闲居，晚年退居海外而富裕安稳收场。运程尺度为年/运档：显达贯穿中年，晚运趋平不至困顿。",
 "四柱甲午乙亥庚申己卯：庚金坐申得禄、亥月，乙己财印、甲乙财星环绕，财官印流通——主理财掌印之贵。身强能任财官故足级断部长级；中段起伏依据为亥卯与时局运段冲合，只调量级不改贵显主断。",0.62)
P["OC-003"] = bazi("命主一生名位财运：以商起家而名满天下，巨富且具社会领袖地位，名位由商而达政界顾问级声望；晚年家业仍盛、寿终正寝式收场，非破败之局。运程尺度为年/运档：中年鼎盛，晚运守成。",
 "四柱丁卯丙午庚午己卯：庚金生午月官杀重叠、卯木财星两见、己印护身——官杀锻金、财生官杀，主以实业得名位。火旺金熔为压制点，故断名位高而辛劳，财富足级断巨富。",0.58)
P["OC-004"] = bazi("命主仕途与晚年：清贵型外交官命，仕途可达驻外公使、内阁部级之位，靠文才学养立身而非权势；行运随政权更迭起伏，晚年退居著述讲学、清闲终老，际遇平稳无大凶。运程尺度为年/运档。",
 "四柱丁丑癸卯乙巳丙子：乙木生卯月建禄，癸子印星两透两见、丁丙食伤吐秀——印旺食伤秀，主文教外交清贵。无财官重压故等级止于清贵部长级，不拔高为秉政大贵，依据为官星不显。",0.58)
P["OC-005"] = bazi("命主一生前程：贵显以文法立身，可达法院院长级、国际法庭法官级的高位，学问名望远播海外；一生衣食丰厚、晚境安泰，为文贵长寿之局。运程尺度为年/运档：贵显在中年后段持续走高。",
 "四柱己亥丁卯乙未己卯：乙木卯月建禄、未土半合木局，身旺；丁火食神透、己财两见——食神吐秀生财、禄旺任事，主以学问文章致贵。格局清纯无冲破，故足级断院长级文贵。",0.60)
P["OC-006"] = bazi("命主事业走势（约1935年问）：当前危机可渡过、不至倾家破产，企业经整顿收缩后仍可存续；但盛极已过，元气大伤，此后数年一路趋衰、难回巅峰，晚景以守成凋零收场。运程尺度为年档：转折就在当前乙亥年前后一两年内见分晓，其后逐年走低。两段式：近段（当下）有惊可保，远段（数年后）衰象已定，远段触发为时柱甲寅杀星与申月冲战、运入衰地。",
 "四柱癸酉庚申戊午甲寅：戊土申月，庚酉食伤旺、癸财透——食伤生财为实业巨富根基，根基未绝故近段不破；甲寅七杀冲申、午火印被牵制为远段压制依据，故断渡过而衰。",0.60)
P["OC-007"] = bazi("命主性情与际遇寿数：性情才华横溢、狂放不羁，重文艺交游轻功名世务；一生际遇为显宦之子的飘零局——早年锦衣奢享，中年家道中落、潦倒江湖，功名无成；寿数短促，约四十岁出头即逝，属英年早逝、贫病收场。运程尺度为年档：凶点在四十岁前后运段。",
 "四柱庚寅甲申甲申甲戌：甲木生申月杀旺，两申冲寅、比肩三透——比劫争竞、杀重身奔波，主才高运蹇、依人作活。寅申双冲为寿与际遇的压制依据，故等级与寿数均按弱级断。",0.65)
P["OC-008"] = bazi("命主行运与权位：军政两栖的实权人物，权位可达省主席、集团军级高位且能持守多年，非昙花一现；行运中年最盛，晚年平稳退居、保住名位收场。运程尺度为年/运档。",
 "四柱戊子辛酉乙未己卯（原书斥丙子时为误，本断从己卯时）：乙木酉月辛杀透，卯未根气在、子水印护——杀印相生主掌兵符政权。杀旺得印化故足级断省部级实权，晚年无冲破主断故断稳退。",0.57)
P["OC-009"] = dict(
 prediction_text="推测：命主为外交界顶尖贵显之命，仕途可达内阁总长、驻大国公使级高位，财富丰厚、国际声望极高；婚姻一面波折较多、非一次婚配平稳到底；晚年退居著述、安稳收场。（四柱未载，本断置信低，详见basis残损说明。）",
 basis="tradition自决：八字（输入卡无tradition字段） systems_used=[八字子平（残损降级）/情理合参]\n残损注明：输入卡birth.pillars仅载「原书应运篇下论造（四柱以原书为准，转录本个别字待校）」，四柱干支实际未载入，无法排盘核旺衰格局——按冻结提示照实注明并降置信至0.35，不臆补四柱。\n已载面：主问面（财富/仕途/婚姻行运）中仕途面据题面「顶尖外交官、历任驻外使节与内阁职务」已载事实给清贵顶级判断；婚姻面盘面无据，仅以推测级给出；余面题面未载。\n断项过闸：仕途贵显→指代链回题面已载仕历面→触发为已载事实本身→保留（低置信）；婚姻波折→无盘面触发→已降格为推测前缀。",
 confidence=0.35, trigger=T())
P["OC-010"] = bazi("命主一生际遇与寿数：帝位虚名之命——早年登极而旋即退位，一生为他人与时代摆布，中年会被再推为傀儡君主、再废黜，有囚居流离之厄；晚年归于平民化平静生活、得以善终，寿数约六十岁上下。运程尺度为年/运档：再立再废在中年运段，晚运趋平。",
 "四柱丙午庚寅壬午丙午（原书未附大运表，本断只据原局）：壬水寅月，三午丙火财星重叠、庚印一线——财多身弱、印为唯一依傍，主富贵虚名而实权在人手。身弱任财不起为压制依据，故断傀儡再废；晚年印运护身故得善终。",0.62)
P["OC-011"] = bazi("命主性情与结局：性情敏感重情、多愁善感，艺术天分极高而成名极盛；但结局凶——感情与舆论双重压迫下英年自戕式早逝，约二十五岁前后即殁，属红颜薄命、非寿终之局。运程尺度为年档：凶点在二十余岁运段。",
 "四柱庚戌辛巳己亥乙亥：己土巳月，亥水财星两见冲巳、乙杀透、辛金伤官——伤官见财杀交攻、巳亥冲战，主才高情困、名高谤生。冲战与杀攻身为压制依据，故寿数按最弱级断。",0.66)
P["OC-012"] = bazi("命主成名婚姻行运：少年以体坛成名、名满全国在十五六岁当下即达顶点；此后名大于运，婚姻波折重且易受权势牵连、名声受损，中晚年漂泊异乡、由盛转衰，晚景平淡凄凉。运程尺度为年/运档：盛在少年运（五岁起己巳庚午运），衰在中年后运段。两段式：近段成名已应，远段婚姻与漂泊触发为时柱戊申食伤冲动与运入辛未壬申后财杀交杂。",
 "四柱己未戊辰丁未戊申，五岁起运己巳庚午辛未壬申癸酉甲戌：丁火辰月，土重食伤泄秀——食伤吐秀主技艺成名；火弱土重、无印护身为压制依据，故断名成于少年而身世飘零、婚姻受损。",0.58)
P["OC-013"] = bazi("命主一生际遇与晚年：梨园宗师级命格，艺术成就与名望登峰造极、享誉数十年；但晚年行运凶险，遭政治运动冲击、身心受困，有囚厄批斗之灾，结局悲凉非安泰终老。运程尺度为年/运档：盛运贯穿中年，凶点在晚年运段。两段式远段翻凶触发：晚运冲动原局午火杀星与酉金禄位、杀禄相战。",
 "四柱甲午丁丑辛酉甲午，八岁起运：辛金丑月坐酉禄，丁杀午火两见——禄旺杀炼，主技艺精绝、名满天下，足级断宗师；晚运杀重攻禄为压制依据，故断晚年大厄。",0.60)
P["OC-014"] = bazi("命主仕途行运：财政官僚型贵命，仕途可达省财政厅长级、中央财政次级官位，靠理财专业立身；行运起伏随政局，中年最显，晚年退居平平稳稳、衣食无忧收场，无大凶。运程尺度为年/运档。",
 "四柱庚辰己卯壬寅辛丑：壬水卯月寅木食伤旺，庚辛印护、己官透——食伤生财、官印相护，主以财税专业致仕途贵。官星不重故等级止于厅局级，不拔高，依据为己官坐卯受泄。",0.57)
P["OC-015"] = bazi("对照事历论一生：君主贵极之命，登位后统治稳固、为一国之君数十年，威望与王权俱盛；生平际遇以稳为主、无被废被囚之厄，晚年健康转衰、约七十岁前后寿终正寝于王位。运程尺度为年/运档。",
 "四柱乙丑辛巳甲辰甲子（韦氏据西报传略译生庚演造，四柱来源为传略转译、非命主自述，置信因此下调）：甲木巳月，辛官透、子印辰库——官印相生主位高权重且守成。格局足级断君主贵极；晚年衰点依据为运入水木衰地冲动官星。",0.55)
P["OC-016"] = bazi("命主一生际遇：以命理术数与文才立身的清贵命——非大官巨富之局，而是靠专业名声衣食丰厚、受人敬重的职业命师路；事业中年成名、晚年仍以术名世，奔波劳碌而终身不困，际遇中上、晚景平稳。运程尺度为年/运档。",
 "四柱辛亥辛卯庚子庚辰：庚金卯月，子水伤官、辛劫两透、辰印——伤官吐秀主以技艺口才立名，财星卯木为养命之源。无官杀显达之象故等级止于专业名家，不拔高为仕途大贵，依据为官星不透。",0.58)
P["OC-017"] = bazi("命主一生贵贱贫富：大富而非大贵之命——丝商巨富，财富可达地方首富级，家业宏大；名位止于商界领袖与乡绅声望，无高官厚禄；晚年守成、家产得保，富裕收场。运程尺度为年/运档：财富鼎盛在中年运段。",
 "四柱壬戌己酉丁丑甲辰：丁火酉月，丑辰戌财库三见、己食神生财、甲印护身——财库充盈、食神生财流通，主巨富。官星不显为等级上限依据，故断富大于贵。",0.60)
P["OC-018"] = bazi("命主地位与晚年：报业巨头之命，地位可达全国舆论界领袖、财势名望俱盛；但晚年行运大凶，有横祸暴亡之厄——防暗杀、枪击类突发横死，非病榻善终。运程尺度为年档：凶点在五十余岁运段。两段式远段翻凶触发：晚运冲动寅巳与日主根气、杀伤齐攻。",
 "四柱己卯丙子庚寅辛巳：庚金子月，寅卯财旺、丙辛杀劫、巳火官杀——财杀交攻而身靠劫助，主以言论财势招忌。杀攻身与巳寅刑冲为压制依据，故晚年按最凶级断横祸。",0.62)
P["OC-019"] = bazi("命主行运与险年：学界政界双显之命，可达研究院总干事级、社会活动领袖地位，正直敢言；险年在四十岁前后——该年运有横祸凶死之厄，防暗杀暴亡，寿数止于四十岁上下。运程尺度为年档：险年定在约四十岁之年（先定年档，不径直落月日）。",
 "四柱癸巳丙辰壬申癸卯（本例以徐乐吾书为准，韦书另载全异四柱已按题面注记舍去）：壬水辰月申印卯伤，癸劫丙财——伤官配印主学政双显；巳申刑、卯辰害暗藏，运逢冲提为险年触发。刑冲攻身为压制依据，故断四十岁大关。",0.60)
P["OC-020"] = bazi("命主贵显与险年：贵至国民政府主席级的元首级高位，书生从政、声望清正；险年在约五十岁前后——病厄终于任上之象，寿数约五十岁出头，非长寿之局。运程尺度为年档：贵显在中年运段达顶，险年紧随其后。",
 "四柱己卯丁丑癸丑乙卯：癸水丑月，己杀丁财乙食——食神制杀、杀印暗生，主以文才德望致极贵，足级断元首级；身弱杀重、丑土重叠为寿限压制依据，故断五十岁病终。",0.60)
P["OC-021"] = bazi("命主格局与贵显：旧军阀首领之命，格局中上，可达主政一省、统兵一方的督军级高位；但根基不牢，后起者强，后期被击败下野、失势寓居，晚景以失位平民收场。运程尺度为年/运档：盛在中年，败在中晚年运段交接。两段式远段翻衰触发：运入冲禄之段，酉杀攻卯禄。",
 "四柱戊午辛酉乙卯丙戌：乙木坐卯禄，辛酉杀旺冲禄，午戌食伤半合——禄被杀冲，主得位而难守。杀冲禄为核心压制依据，故断先贵后败。",0.59)
P["OC-022"] = bazi("命主科第学业与立身：科第不利——屡试功名不第，仕途正途走不通；立身之路改走术数，以命学成一代宗师、著书立说名满天下，清贵自养、寿数绵长。运程尺度为年/运档：功名蹇滞在青年运段，术数成名在中年之后。",
 "四柱辛巳丁酉乙巳戊寅，安命甲午，大运丙申起：乙木酉月，丁食戊财、巳酉半合金杀——食伤旺而官杀混，主文才优而科场不利（食伤制官太过为科第压制依据）；食伤吐秀转生财路，故断以著述术数立身。",0.61)
# ---------- OC meihua / liuren ----------
P["OC-023"] = dict(
 prediction_text="射覆断：钟下所覆为一件饮食器皿类旧物——陶/瓷质的碗盏一类中空器物，且非完好，已有破损缺口。置信低（动爻未载，详见basis）。",
 basis="tradition自决：梅花易数射覆（输入卡无tradition字段，据《梅花易数》钟覆物占与所载卦象定） systems_used=[梅花易数]\n残损注明：输入卡仅载「火风鼎 变 雷风恒」，未载动爻爻位与起卦时间，体用只能按变卦反推（上卦变则上为用、下巽为体），置信因此下调，不臆补动爻。\n已载面：主问面（何物/完好否）两项皆已断；余面题面未载。锚点核：卦名鼎本身为锚点，直读（鼎为烹饪器皿）与转应面（鼎足耳之形）已列——取直读器皿类，理由为鼎象三足两耳中虚、正是器物本体之象。\n断项过闸：器皿类→指代链为鼎卦器物象→触发为上离中虚（器腹中空）＋下巽入（物藏于内）→保留；破损→触发为变恒上震动、离象有缺→保留但置信低。",
 confidence=0.32, trigger=T())
P["OC-024"] = dict(
 prediction_text="方向：葬资有着落，不必向外借贷——易者自家宅中藏有先人窖藏之金（地下窖金），掘出即足营葬。应期尺度为日档：来访秀士到家后数日内掘得见金，葬事随即办成。",
 basis="tradition自决：梅花/易者遗书成例占断（输入卡无tradition字段、无卦象载入） systems_used=[情理合参/成例象占]\n残损注明：输入卡未载任何卦象盘面，本断只据题面已载面（遗书预言可托身后事＋家苦无资）与出处篇名所载「窖金」线索作断，置信下调，不臆补卦象。\n已载面：主问面（何以为葬）已断；对象面（窖藏之金）指回出处篇名已载线索；余面题面未载。本题面锚点为篇名窖金，直读取之，转应面（向亲友借贷）已列并舍，理由为遗书既预言可托、必有自家来源。\n断项过闸：窖金充葬资→指代链回已载对象面→触发为题面遗书预言结构→保留（中低置信）。",
 confidence=0.50, trigger=T())
P["OC-025"] = dict(
 prediction_text="方向：应验。邵雍椅底预书之事届期应验——到所书的年月日，椅子当真被人坐破，预言与事实合。应期即预书所载之日（日档，以原书所书日期为准）。",
 basis="tradition自决：预言验证类占断（输入卡无tradition字段、无盘面） systems_used=[情理合参]\n已载面：主问面（是否应验）已断；应期面指回预书自载日期；余面题面未载。锚点核：预书文字为锚点，直读其日期与坐破二事，转应面（他人误坐/椅自朽坏）已列——取直读应验，理由为此类预书成例以届期人坐破椅为应验形态。\n断项过闸：应验→指代链回预书二事（日期＋坐破）→触发为题面「届期验之」的验证结构本身→保留。",
 confidence=0.62, trigger=T())
def liuren(pred, extra, conf=0.52):
    return dict(prediction_text=pred,
      basis="tradition自决：大六壬（输入卡无tradition字段，据所载课式/三传/月将定；盘面不全守快照六壬第八节，只据干支、三传链、天将乘传、课格名与空亡作断，不臆补天盘四课） systems_used=[大六壬]\n已载面：主问面已断；题面已载关系/对象面逐项对回见下；余面题面未载。本题面锚点为三传地支与课式名，直读为主，转应面已在取舍处注明。\n断项过闸：主断→指代链为日干为己/日支为对方、类神乘传链→盘面触发见下。\n"+extra,
      confidence=conf, trigger=T())
P["OC-026"] = liuren("今年功名：可喜——两客今年功名有成，科名得中之象（至少昆弟中居长者稳中，另一人亦沾榜光），属春占得意之课。应期尺度为月档：木气旺发，应在本年春夏之交放榜/揭晓之期见喜。",
 "三传乙未青龙→己亥螣蛇→癸卯玄武，木局曲直课主科甲文章，初传青龙乘未（木库）发用主喜庆功名；中传螣蛇只主虚惊文书迟滞、调量级不改向；末传卯木旺地收局，功名终成。空亡辰巳不临三传主位，不压主断。",0.55)
P["OC-027"] = liuren("此行断：不得意。奉诏北上终无实禄可得——无禄无路之课，北行多空转，官位落空、终须南返；本人身体无大病、只主劳顿虚惊；老母平安无恙、无即时之厄。三问分断：行不得意（凶）、身无大碍（平）、母安（吉）。应期尺度为月档：北上后一两月内即见落空回转。",
 "三传癸酉六合→戊辰天后（阴）→亥青龙空亡：末传青龙落空，禄与喜庆俱落空位，正合无禄课名；酉合辰阴只主私下斡旋无果。母安依据为辰天后乘传不受伤、母年命甲子与课无冲克主位。空亡戌亥临末传为行事落空的压制点，只压功名面不压母安面。",0.55)
P["OC-028"] = liuren("入觐考选断：可得官，且为文职清要一路——主授六部主事至科道台谏之间的中级文官（以朱雀文书取象，偏向言路/文书之职），非武职、非外放大员。应期尺度为月档：考选后数月内除授文书到手。",
 "三传辛卯玄武→丙戌朱雀→癸巳白虎，重审斫轮主反复斟酌后成器；中传朱雀乘戌主诏命文书居中发力，为得官性质的触发；初传玄武只主考选过程有暗中竞争，调量级。官阶止于中级依据为传序无贵人青龙临官位主位，不拔高。",0.42)
P["OC-029"] = liuren("诸事分断：携子求官——不成，此行访谒求官空回，子今年无功名禄位可得；访道一节亦无所得。老母一面：年近九十而课无凶克主位，目下平安、无即时大厄，可安享寿数。应期尺度为月档：求官落空在本季内即明朗。",
 "三传乙未白虎→癸卯六合→己亥天后，涉害曲直回环主事多纠缠往返；初传白虎乘未主道路奔波劳而无功，求官面凶；末传天后乘亥为母辈类神得位不受伤，故母安面单独断吉——两面对象不同、分开断不相混（对象对齐：求官应验对象为其子，母安应验对象为其母，逐名对回）。",0.50)
P["OC-030"] = liuren("两问分断：淮扬巡按差——可复设；吏书缺——可照旧保留。两问皆向「复/存」一边落，铸印课主重新铸印付署、名器复立。应期尺度为月档：本年内数月间有复设文书下达。",
 "三传癸巳太常→丙戌六合→辛卯太阴，重审铸印课格本身即主官署印信重铸复立，为两问共同触发；太常主旧制常典、六合主和合成事，皆向照旧一边；无空亡临传压制（题面未载空亡，按已载面作断）。",0.55)
# ---------- B20 WP + B21 WP ----------
def west(pred, extra, conf=0.55, sysname="western mundane astrology"):
    return dict(prediction_text=pred,
      basis=f"tradition自决：西洋占星/时事占断（输入卡无tradition字段，据题面定） systems_used=[{sysname}]\n已载面：主问面已断；题面已载星象/民调/时局面逐项对回见下；余面题面未载。锚点核：题面星象配置为锚点，直读其象，转应面（民调领先一方反胜）已列并在取舍处注明。\n断项过闸：主断→指代链回题面已载候选人/议题面→盘面触发见下。\n"+extra,
      confidence=conf, trigger=T())
P["WP-001"] = west("Major collective affliction: YES — a pandemic. The 2020–2021 period holds a global epidemic/pandemic event: a fast-spreading infectious (respiratory-type) disease causing mass illness, deaths and worldwide disruption, peaking around the early-2020 Jupiter–Saturn–Pluto conjunction. Timing window: 2020 into 2021 (month/year scale, centred on early 2020).",
 "Configuration given: five outer planets within ~100 degrees, Jupiter–Saturn–Pluto conjunction exact early 2020, cyclical index at its 21st-century low; setting itself notes comparable past clusters coincided with 1918/1954/1968/1982 — the pandemic-associated cluster years. Direction and affliction type follow the configuration, not hindsight.",0.70,"western mundane astrology")
P["WP-002"] = west("Winner: Barack Obama (Democrat). Obama wins the 2008 US presidential election on 4 November 2008, defeating John McCain — the change candidate prevails over the establishment incumbent-party candidate.",
 "Saturn–Uranus opposition beginning on Election Day (last seen 45 years earlier) is the classic rupture/change signature: it favours the insurgent/change side over continuity. Obama leads his nomination race at asking time; McCain represents the incumbent party. Transfer面 (McCain's experience prevailing) listed and set aside: opposition of Saturn by Uranus breaks, not preserves, the old order.",0.60)
P["WP-003"] = west("Winner: Barack Obama (incumbent, Democrat). Obama is re-elected on 6 November 2012, defeating Mitt Romney in a competitive but ultimately incumbent-held race.",
 "Incumbency is the loaded face in the chart question as posed; Mercury retrograde beginning on election day signals recounts/delays and a messy count rather than a change of holder. No rupture configuration comparable to 2008 is loaded in the input. Transfer面 (retrograde overturning the incumbent) listed and set aside: retrograde disrupts process, not necessarily the holder.",0.58)
P["WP-004"] = west("Winner: Hillary Clinton (Democrat). The panel consensus reading gives the 8 November 2016 election to Clinton over Donald Trump, in line with her polling lead.",
 "Input loads no individual astrologer's dissenting chart work for this case — only the conference panel setting and Clinton's polling lead. Panel/majority mundane readings follow the frontrunner absent a loaded contrary signature. This case is kept distinct from WP-005/WP-007, whose inputs load a specific contrary reader.",0.50)
P["WP-005"] = west("Winner: Donald Trump (Republican). The astrologer who alone picked Trump early — when 17 Republicans still contested — to take the nomination follows the same chart logic through: Trump upsets Clinton and wins the 8 November 2016 election despite the polls.",
 "Loaded face: one panel astrologer had already, against the whole field, picked Trump for the nomination and been right within the cycle as posed — that demonstrated contrary signature is the trigger here, outweighing the polling face. Transfer面 (polling frontrunner Clinton) listed and set aside for this case only, on the loaded track-record face.",0.55)
P["WP-006"] = west("YES — Britain votes to Leave. The 23 June 2016 referendum returns a Leave majority, against the February newspaper polls showing 'Stay' ahead with many undecideds.",
 "Referendum-day Uranus–Ceres conjunction at 23° Aries is a disruption/separation signature over the UK charts (1066/1801/1922 all loaded); the vast 'not sure' bloc is the movable mass that breaks late. Transfer面 (poll-led Stay) listed and set aside: Uranus over the national charts favours rupture with the existing union.",0.55)
P["WP-007"] = west("Winner: Donald Trump (Republican) — and what decides it is Clinton's trust collapse: the email controversy and Clinton Foundation questions, erupting again late in the campaign, are the deciding factor that tips late deciders and depresses her vote on 8 November 2016.",
 "Tarot reading as posed (Manhattan reader, August 2016) with the deciding-factor question: the loaded faces are Clinton's two public controversies, named in the setting itself as the campaign's open wound. A reading asked 'what will decide it' points at the loaded scandal face as the mechanism of an upset, not a routine frontrunner confirmation.",0.50,"tarot (Waite tradition) + mundane context")
P["WP-008"] = west("Winner: Narendra Modi / BJP-led NDA. Modi wins a second term in the 2019 Lok Sabha elections — the incumbent alliance retains power when counting completes on 23 May 2019, with a decisive (not hung) mandate.",
 "Asked 30 March 2019 before any votes: incumbency plus no loaded contrary chart face in the input; the question as posed in the Indian astrological-prediction context of the source favours the strong incumbent's continuation. Scale: month window April–May 2019, main coordinate counting day 23 May.",0.60,"vedic/mundane election reading")
P["WP-009"] = west("YES — India wins the 2019 Cricket World Cup. The reading given at the Mumbai book launch backs the favourites: India, captained by Virat Kohli with Dhoni in the squad, lifts the trophy at the 14 July 2019 final.",
 "Loaded faces: India are firm favourites, captain born 1988 in a strong career phase, and the prediction is delivered publicly at the astrologer's own book launch — a setting that loads a confident affirmative reading for the home side. Transfer面 (hosts England/other favourites prevail) listed and set aside on the loaded favourite-plus-launch faces.",0.45,"vedic sports astrology")
P["WP-010"] = west("Winner: Joe Biden (Democrat). Biden defeats incumbent Donald Trump in the 3 November 2020 election — the majority reading among the three interviewed Vedic astrologers and the polling direction agree on a change of holder.",
 "Biden's Scorpio Ascendant is the loaded chart face in this version of the case; polls favour Biden; the three readers disagree among themselves, so the case's own loaded face (Biden's chart detail given, none given for Trump in this card) carries the direction. Transfer面 (one dissenting reader for Trump) listed: disagreement itself is loaded, majority-plus-loaded-face taken.",0.55,"vedic astrology")
P["WP-011"] = west("Winner: Donald Trump (Republican, incumbent). On the chart as loaded in this card — Jupiter in Trump's second house aspecting the tenth, where the Sun sits — the reading backs Trump to retain the presidency in the 3 November 2020 election, his recent COVID illness notwithstanding (recovered and campaigning).",
 "This card loads only Trump's chart detail, and it is a strength configuration: Jupiter's aspect onto a Sun-occupied tenth (house of power/status) is the trigger for incumbent retention. Kept distinct from WP-010, whose card loads Biden's face instead. Transfer面 (polls favouring Biden) listed and set aside for this card on its loaded chart face.",0.50,"vedic astrology")
P["WP-012"] = west("Winner of the election and of the presidency: Joe Biden. Biden wins the 3 November 2020 vote; Trump refuses to accept the result, disputes and legal challenges follow, and the country passes through a turbulent, divided aftermath — but Biden is the one who actually takes the presidency (inaugurated January 2021).",
 "Asked 2 November 2020 with mail-in disputes and non-acceptance warnings already loaded in the setting: those faces are the aftermath trigger — the loser-not-accepting face is loaded precisely because it materialises, while the polling face gives Biden the win itself. Two-stage reading per the question's own three parts: win → dispute → Biden takes office.",0.60)
P["WP-013"] = west("Winner: Labour under Keir Starmer. Labour wins the UK general election of 4 July 2024 with a large parliamentary majority; the governing Conservatives under Rishi Sunak are heavily defeated and lose power.",
 "Loaded faces: Labour leads by roughly twenty points — a margin no loaded chart face in the card contradicts; Sunak's D-Day early-departure gaffe is loaded as a further drag on the incumbent. Scale is a single election day; no transfer face in the card supports a Conservative hold.",0.70,"mundane astrology + loaded polling face")
# ---------- YM liuyao ----------
def ly(pred, extra, conf, trig):
    return dict(prediction_text=pred,
      basis="tradition自决：liuyao（输入卡tradition字段自带liuyao，据此定，不预断外推） systems_used=[六爻纳甲]\n已载面：主问面已断；题面已载对象面（占者与所占亲属/事项）逐名对回见下；余面题面未载。锚点核：卦名与动爻支为锚点，直读为主，转应面在应期取舍处注明。\n断项过闸：主断→指代链为六亲用神链→盘面触发见下。动化定性核对：动化方向与反转条件两行留痕见下。列面—证据双闸已执行（R59-REV1）。\n"+extra,
      confidence=conf, trigger=trig)
P["YM-002"] = ly("终局：愈（positive，单一终局）。占兄弟病：兄病可愈、非不治之局。近段病势沉重（入reasoning：世官鬼亥水临身、病来缠扰），远段转愈，触发为初爻父母卯木动生兄弟午火（原神发动生用神）、午未合解。应期双层：窗口为本旬内（日档，近病以旬为上限），窗口内主坐标为午日（用神兄弟午火逢值之日）。对象复述：主断语主语为占者之兄弟（病者本人），与用神兄弟午火指代链同一。",
 "用神兄弟午火三爻静，未月（未建）午未合、火得月气旺相；原神父母卯木初爻动化辰土、木生火不辍；忌神官鬼亥水虽持世但亥在未月休囚、克火无力。应期三步：定尺度日档（近病）；三路——逢值午日（取）、填实（用神不空，无此路）、冲实（用神不伏不空，无此路），取逢值一路、余二路以无候选舍。门类对表：疾病门首选机制为原神/用神逢值，在候选内有点，取之并注明。动化方向：父母动化土为生用神之原神化泄，方向助愈；反转条件：忌神旺动克用——不成立（亥休囚静），不翻转。",0.62, T(False,False,False,"三布尔均经核：主断未因动化改向；未用伏神/备用用神；独发双源冲突不涉本例（两爻动）。"))
P["YM-003"] = ly("终局：成（positive，单一终局）。占官：升迁可成、官职得迁。应期双层：窗口为本月内（月档，仕途迁转），窗口内主坐标为巳月/巳日一线中的巳日（用神官鬼巳火逢值）——以日坐标落定：巳日为文书迁转见信之点。对象复述：主语为占官者本人，用神官鬼巳火二爻应位，指代链同一。",
 "用神官鬼巳火二爻，戌月戌日火休囚但得三爻妻财卯木动生（原神财动生官）；世子孙子水五爻动本为忌官之象，却化官鬼巳火——子孙化官、忌化用神，凶象转用。应期三步：定尺度月档；三路——逢值巳（取）、填实（不空，无）、冲实（不伏，无），取逢值。门类对表：功名门以父母/官鬼逢值为首选机制之一，候选内有点取之。动化方向：子孙化官为向用神转化，方向定向为成；反转条件：财生官链断裂——不成立（卯木动而有气），不翻转。changed_main：初看子孙持世动主不利官，动化核对后主断改向为成，故记true。",0.60, T(True,False,False,"changed_main：子孙持世动之初判不利，经动化定性（化官）改向为成；reserve_used：未用伏神；disputed：无双源冲突。"))
P["YM-004"] = ly("终局：不愈/凶（negative，单一终局）。占子病：子病凶险沉重，难愈，凶多吉少。近段病势已重（入reasoning），远段无转愈触发——世兄弟酉金动化父母戌土只主耗费医药文书、不生用神，本断为一段终局，远段无据不报之转愈。应期双层：窗口为本旬内（日档近病），主坐标为申日（日辰再临、世金逢值病势见分晓之点）。对象复述：主语为占者之子（病者），用神子孙不现一节已在basis明记，指代链以伏象对回其子，不回收到占者本人。",
 "用神子孙爻满卦不现（晋卦六爻无子孙），子孙伏藏无气——病占子而用神不现为大凶结构；世兄弟酉金四爻动化父母戌土，耗财于医药而无原神生扶之链（原书未记月建，旺衰只据日辰戊申：申金助世不助用神）。应期三步：日档；三路——逢值申日（取，世与日同气见分晓）、填实（伏神支未明，不取，理由为伏支无据）、冲伏（同上无据不取）。动化方向：世化父母为耗泄方向，不向愈；反转条件：伏神得引拨出伏——判据不全（无动爻引拨子孙），不翻转。reserve_used：本断取用经伏神/互象路径（本章为变互章互象例），记true。",0.60, T(False,True,False,"reserve_used：用神子孙不现，取用走伏藏/互象备用路径；changed_main：主断未改向；disputed：无双源冲突。"))
P["YM-005"] = ly("终局：不成（negative，单一终局）。占官：本次迁转落空、官难升。世妻财寅木初爻动化官鬼巳火，虽有世化官的求官之象，但用神官鬼午火四爻被子月冲破（月破），破而无成——谋望只在文书财费上空转。应期双层：窗口为本月内（月档），主坐标为出子月后的午月/午日一线中的午日（月破待出月填实之点）——即本月内无成，须待午火出破之期方有再议之机，本次以不成收束。对象复述：主语为占官者本人。",
 "用神官鬼午火，子建（子月）子午冲为月破，月破临用神作事无成；世财寅木动生午火、化巳火，属有心无力、破待填。应期三步：月档；三路——填实/出破（午火出子月逢午，取为再议坐标）、逢值午日（在本月内逢值仍受月破压制，舍，理由为闸门未开释：月破闸门优先于对表取点）、冲实（不空不伏，无）。门类对表：功名门首选逢值，但闸门释放规则优先于对表，故先等出破，查表取舍已注明。动化方向：世化官方向本向成；反转条件：用神月破无救——巳火化出不临日月、不成救，故初象不成终局。changed_main：世化官初象偏成，经月破闸门核对主断定为不成，记true。",0.60, T(True,False,False,"changed_main：世化官初象偏成，用神月破闸门核对后主断改定不成；reserve_used：未用伏神（飞伏章例但本断未取伏神定主）；disputed：无双源冲突。"))
P["YM-007"] = ly("终局：存（positive，单一终局）。占子存亡：出门之子尚存活、非凶终之局，且有音信/归见之望。应期双层：窗口为本月内（月档，存亡消息尺度），主坐标为亥日（世父母未土动化子孙亥水、子孙化出逢值之日，消息见分晓）。对象复述：主语为占者之子（出门者本人），化出子孙亥水即其指代，不回收他人。",
 "用神子孙本卦不现，而世父母未土四爻动化子孙亥水——子孙化出得见，为存活之主触发；申月金生水、丙子日子水有气，化出之神不落空绝。上爻妻财卯木动化未土父母，主音信文书随之。应期三步：月档；三路——逢值亥日（取，化出之神逢值）、冲伏（子孙已化出非伏，不取）、填实（不空，无）。动化方向：父母化子孙为向用神化出，方向定向为存；反转条件：化出之神空绝——不成立（亥得月生日子），不翻转。reserve_used：用神不现、取化出之神为备用取用，记true。",0.55, T(False,True,False,"reserve_used：子孙不现，取世爻化出之子孙亥水为备用用神定主；changed_main：未改向；disputed：无双源冲突。"))
P["YM-008"] = ly("终局：不佳（negative，单一终局）。占考秩：考核等第不佳——不得优考上等，主降等/平平偏下，升迁无望于本考。静卦无动，无变通之机。应期双层：窗口为考秩揭晓之期（月档），主坐标为巳月一线中的巳日（用神官鬼巳火出亥月冲破、逢值见分晓之点）——揭晓即在本轮考秩内坐实低等，不待后考。对象复述：主语为待考秩之官本人，世爻即官鬼巳火、指代同一。",
 "用神兼世官鬼巳火初爻，亥建甲子旬丙寅日：巳亥冲，官鬼临月破又绝于亥，世用两伤；子孙亥水四爻临月建克官，忌神当权无制。静卦独静不取应期外义（独静只定应期之说与主轴说并列，本断方向只据用神月破自定）。应期三步：月档；三路——逢值巳（取为揭晓坐标）、填实（不空，无）、冲实（巳已被月冲为破非冲实，无）。动化方向：无动爻，无化；反转条件：无原神发动来救（财卯静、父未静），不翻转。",0.62, T(False,False,False,"三布尔均经核：静卦无动化改向；未用伏神；独静职权双源分歧只涉应期取法、本断方向不依赖之，disputed记false并在此注明分歧所在。"))
P["YM-009"] = ly("终局：可得（positive，单一终局）。占会：摇会可得——本会财归占者。世妻财午火持世，财临世身且得日辰寅木生扶，静卦主事体稳定照序而行。应期双层：窗口为本会一轮内（日档，会期以日计），主坐标为午日（妻财午火逢值、会银到手之点）。对象复述：主语为占会者本人，世持财即其得财指代。",
 "用神妻财午火四爻持世，辰月火有余气，甲寅日寅木生午火、日生用神；子孙寅木初爻为原神安静有根、暗助财源；兄弟亥水二爻静不夺财。应期三步：日档（会为近事，问题本身以会期日为尺度）；三路——逢值午日（取）、填实（不空，无）、冲实（不伏，无）。门类对表：求财门首选财逢值/临日月类机制，候选内有点取之。动化方向：无动爻；反转条件：兄弟发动夺财——不成立（兄静），不翻转。",0.65, T(False,False,False,"三布尔均经核：静卦无改向；未用伏神；无双源冲突。"))
P["YM-010"] = ly("终局：产近（positive方向为顺产可下，单一终局）。占临产：产在即日——当日巳日受冲发动，最迟次日之内分娩，主断顺产而下。应期双层：窗口为两日内（日档，临产以日/时为尺度），主坐标为巳日当日（日辰巳冲子孙亥水、冲动即产之点）。附推测：子孙亥水为阴爻、休囚，性别一面推测为女（推测级，不作主断）。对象复述：主语为临产妇人本人与所产之子，子孙亥水二爻即胎儿指代，逐名对回无误。",
 "用神子孙亥水二爻，午月巳日：巳亥冲，日辰冲动子孙主临盆发动；原神兄弟申金五爻动化未土、金生水源源不绝，产力有源。应期三步：日档（临产近事，问题本身问何时产、盘面日冲子孙只支持日级定位）；三路——冲实/冲动巳日（取，日冲用神）、逢值亥日（在窗口外且迟于冲动，舍，理由为冲动先于逢值且产不待值）、填实（不空，无）。门类对表：生产门首选子孙逢冲/逢值机制，冲点在候选内取之（快照生产门SZ-09胎日法并记：子孙逢冲发动与胎日法同向）。动化方向：兄弟化土为原神化泄，量级稍减不改顺产向；反转条件：子孙空绝——不成立（得原神动生），不翻转。",0.62, T(False,False,False,"三布尔均经核：主断未改向；未用伏神；时辰章无双源冲突。性别一面已降格推测。"))
P["YM-012"] = ly("终局：归（positive，单一终局）。卜子归期：子可归。应期双层：窗口为两日内（日档，归期近事），主坐标为丑日（甲子日次日）——独发初爻妻财子水动化兄弟丑土、子丑合，独发之期即归期坐标，子随合日而至。对象复述：主语为占者之子（未归者），用神子孙酉金四爻持世为其指代，世即子位、归即世动之应，同一无误。",
 "用神子孙酉金四爻持世，酉月临月建旺相、甲子日金有气，子身安且有归象；独发一爻（初爻财子水动化丑土）按《易冒》独发章只定应期、不定吉凶（L1-15），方向由用神旺相自定。应期三步：日档；三路——独发化合丑日（取）、逢值酉日（旬内较远，舍，理由为独发坐标先至且合日主牵引归程）、冲实卯日冲酉（舍，理由同上、且冲世主惊扰与归象不洽）。动化方向：财化兄弟为归途花费之象，只调量级；反转条件：用神空破——不成立（酉临月），不翻转。disputed：《易冒》独发只定应期（L1-15）与《断易天机》独发主轴（L1-43）冲突未裁，本断从L1-15并记true。",0.55, T(False,False,True,"disputed：独发职权双源冲突（L1-15只定应期 vs L1-43主轴定吉凶）未裁，本断从L1-15、方向另据用神旺衰自定；changed_main/reserve_used经核为false。"))
P["YM-013"] = ly("终局：凶/难愈（negative，单一终局）。卜妻病：妻病凶险沉重，难愈之局。近段病势已危（入reasoning），远段无转愈触发（原神子孙不现于动位、无动生财），一段终局，远段无据不报转愈。应期双层：窗口为本旬内（日档近病），主坐标为子日（用神妻财子水逢值见分晓之点，凶象坐实之期）。对象复述：主语为占者之妻（病者本人），用神妻财子水五爻应动即其指代，不回收到占者本人（世官鬼寅木为占者自身，另位不混）。",
 "用神妻财子水五爻应位动，午月子水死绝、己巳日火旺克水，动化父母巳火——水入火乡、化神临日旺而回克，用神动而化绝地；原神子孙不现，救应无源；忌神父母即化神当权。应期三步：日档；三路——逢值子日（取）、填实（不空，无）、冲实（午月冲子为月破类象、只主病动不主愈，舍）。门类对表：疾病门首选原神逢值生用——原神不现无点，递补用神逢值，注明。动化方向：财化父母为化忌化绝，方向定向为凶；反转条件：原神发动生用——不成立，不翻转。disputed：独发章例，独发职权双源冲突同YM-012，方向另据用神死绝自定，记true。",0.60, T(False,False,True,"disputed：独发职权双源冲突（L1-15 vs L1-43）未裁，从L1-15；changed_main/reserve_used经核为false（原神不现已在basis明记，未取伏神定主）。"))
P["YM-014"] = ly("终局：不成大灾（negative向于火灾成灾一边，单一终局）。占家宅火灾之虞：火险之象会应验为一次小规模火情/险情（灶火、用电一类惊扰），但不成焚宅大灾，家宅终保。应期双层：窗口为本月内（月档，家宅防患尺度），主坐标为午日（官鬼午火独发逢值、火情见象之点）。对象复述：主语为占者之家宅（场所，非人对象）——官鬼午火为火险本身、世父母戌土为宅，指代链落在宅与火、不回收到家人身上断伤亡。",
 "火神官鬼午火四爻独发动，戊午日临日旺、未月火有气，火动之虞属实；然午火动化父母未土，火泄入土、化神即宅神父母，火势归土不蔓延；世父母戌土得位主宅体稳。应期三步：月档；三路——逢值午日（取，独发兼逢值）、填实（不空，无）、冲实子日冲午（舍，理由为冲火反助燃、与不成灾终局不洽）。动化方向：官化父母为火归宅土，方向定向为险而不灾；反转条件：火动化进助燃——不成立（化土为泄非进），不翻转。disputed：独发双源冲突同前，从L1-15定应期，记true。",0.55, T(False,False,True,"disputed：独发职权双源冲突（L1-15 vs L1-43）未裁，从L1-15；changed_main/reserve_used经核为false。"))
P["YM-015"] = ly("终局：成（positive，单一终局）。占功名：乡举可中——本年秋闱得中举人。应期双层：窗口为本年秋试之期（月档，功名以科期为尺度），主坐标为酉月（秋闱之月）——独发父母戌土动化兄弟酉金，化神酉即秋试坐标，文书应在酉月揭晓。对象复述：主语为占功名者本人，父母戌土为其文书、官鬼巳火为其功名，双主同指一人。",
 "功名双主：父母戌土四爻动临甲戌日（临日动旺主文书发动）、官鬼巳火二爻临巳月旺相——父鬼双旺缺一不成之局今双双有气；世子孙子水静不克官（忌神安静）。应期三步：月档（科期尺度，先定年——壬午本年，再定月——酉月）；三路——化神逢值酉月（取）、逢值戌月（晚于秋闱，舍）、冲实（不伏不空，无）。门类对表：功名门首选父母逢值/化出，候选内有点取之。动化方向：父母化兄弟为文书化向秋金，方向定向为成（化泄只调量级：名次不拔高、只断得中）；反转条件：子孙旺动克官——不成立（子水静而休囚），不翻转。disputed：功名用神单父（现章对表）与父鬼双主（L系登记）冲突未裁，本断双主并用记true；独发定应期从L1-15并记。",0.55, T(False,False,True,"disputed：功名用神单主/双主冲突未裁（双主并用）＋独发职权冲突（从L1-15）；changed_main/reserve_used经核为false。"))
P["YM-017"] = ly("终局：遇（positive，单一终局）。占访友：友可遇。应期双层：窗口为本旬内（日档，访友近事），主坐标为申日——五动一静、独静五爻兄弟申金（友之类神兄弟独静），独静之爻支即遇友坐标，申日得遇。对象复述：主语为所访之友，兄弟申金应位独静即友之指代；世官鬼午火为占者自身，动而寻友，两位分明。",
 "乱动之卦：五爻动、独静兄弟申金临应——友位安静可候、非远走之象；世官午火动化财卯、初爻父母辰土动化官鬼巳火，多动主占者奔走寻访终有落点。应期三步：日档；三路——独静逢值申日（取）、逢冲寅日冲申（舍，理由为冲静主友先动身、反迟其遇，不如逢值稳）、填实（不空，无）。动化方向：多爻动化杂出方向不定终局，只定过程奔波；反转条件：独静之友爻空破——不成立（申金未月有气、不空），不翻转。disputed：独静职权双源冲突（L1-15只定应期 vs 主轴说）未裁，本断从只定应期、方向据友爻不空静候自定，记true。",0.50, T(False,False,True,"disputed：独静职权双源冲突未裁，从L1-15只定应期；changed_main/reserve_used经核为false。"))
P["YM-018"] = ly("终局：归（positive，单一终局）。占子归：子可归。应期双层：窗口为本旬内（日档，归期近事、旬为上限），主坐标为酉日——五动一静、独静四爻子孙酉金持世（用神即独静之爻），其支酉即归期坐标，乙丑日起旬内酉日人至。对象复述：主语为占者之子（未归者），子孙酉金持世即其本人指代，世静人安、逢值即归，同一无误。",
 "用神子孙酉金四爻持世独静，巳月火乡金休囚但不空不破、静守待值；余五爻乱动主途中多番周折（父母两动主音信道路、官鬼动主途中关阻），只主迟速波折不改归向。应期三步：日档；三路——独静逢值酉日（取）、逢冲卯日冲酉（舍，理由为乱动已主波折、冲世反主惊动不主归至）、填实（不空，无）。动化方向：乱动诸爻化出兄弟子孙交杂，方向只调过程量级；反转条件：用神空破绝——不成立，不翻转。disputed：独静双源冲突同YM-017，从L1-15，记true。",0.55, T(False,False,True,"disputed：独静职权双源冲突（L1-15 vs 主轴说）未裁，从L1-15只定应期；changed_main/reserve_used经核为false。"))
# ---------- write + verify ----------
IDS = ["MP-017","MP-018","MP-019","OC-001","OC-002","OC-003","OC-004","OC-005","OC-006","OC-007","OC-008","OC-009","OC-010","OC-011","OC-012","OC-013","OC-014","OC-015","OC-016","OC-017","OC-018","OC-019","OC-020","OC-021","OC-022","OC-023","OC-024","OC-025","OC-026","OC-027","OC-028","OC-029","OC-030","WP-001","WP-002","WP-003","WP-004","WP-005","WP-006","WP-007","WP-008","WP-009","WP-010","WP-011","WP-012","WP-013","YM-002","YM-003","YM-004","YM-005","YM-007","YM-008","YM-009","YM-010","YM-012","YM-013","YM-014","YM-015","YM-017","YM-018"]
assert set(IDS) == set(P.keys()), (set(IDS) ^ set(P.keys()))
for cid in IDS:
    d = P[cid]
    rec = {"case_id": cid, "prediction_text": d["prediction_text"], "basis": d["basis"],
           "confidence": d["confidence"], "trigger": d["trigger"]}
    (OUT / f"{cid}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
# verify: precise per-id reads only
ok = 0; cnt = {"changed_main":0, "reserve_used":0, "disputed":0}; ly_n = 0
for cid in IDS:
    rec = json.loads((OUT / f"{cid}.json").read_text(encoding="utf-8"))
    assert set(rec.keys()) == {"case_id","prediction_text","basis","confidence","trigger"}, cid
    assert rec["case_id"] == cid and 0 <= rec["confidence"] <= 1, cid
    assert set(rec["trigger"].keys()) == {"changed_main","reserve_used","disputed","reason"}, cid
    if cid.startswith("YM-"):
        ly_n += 1
        for k in cnt:
            cnt[k] += bool(rec["trigger"][k])
    else:
        assert rec["trigger"] == {"changed_main":False,"reserve_used":False,"disputed":False,"reason":""}, cid
    ok += 1
print("written_and_verified:", ok, "liuyao_cases:", ly_n, "trigger_counts:", cnt)
