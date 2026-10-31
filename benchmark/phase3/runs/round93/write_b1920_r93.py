# -*- coding: utf-8 -*-
"""R93 B19+B20 blind predictions writer. Only writes this batch's own prediction files."""
import json, pathlib

OUT = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round93/predictions")
OUT.mkdir(parents=True, exist_ok=True)

TRIG = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}

P = {}

# ---------------- B19 part 1: MP-017..019, OC-001..009 ----------------
P["MP-017"] = {
"prediction_text": "方向：女性出任。下届香港行政长官将由女性当选，即当时改口考虑参选的政务司司长一系胜出，而非已辞职备选的男性前财政司司长。应期：2017年3月26日选举委员会投票当日见分晓（日档，题目本身以该投票日为尺度）。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：此为时事选举的即时决断问，无盘面附载，只许据题面事实作断（事实优先序）。题面事实：现任已宣布不连任；男性候选声势虽有，但女性候选为时任政务司司长、获体制支持面明显占优，改口参选即信号。已载面表：主问面（男女）已断；候选人面已断；应期面（2017-03-26投票）已断；余面题面未载。做功线清单：女性候选之体制支持线（作用源：政务司司长现职与建制选委结构→作用对象：选举结果，助成，状态最强）；男性候选民望线（助成但选制下权重次之）。主线认定：体制支持线为主线。定带：女性胜出为带内主断，量级止于当选本身、不外推票数。",
"confidence": 0.7}

P["MP-018"] = {
"prediction_text": "方向：不能当选。曾俊华虽为候选人中民望最高者，仍将落败于获北京支持的对手，2017年3月26日投票见分晓（日档）。断语落点：败因不在民望而在选举委员会票源结构，其声势属陪跑之势，终局不过高票落败而已。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：人物竞选成败问，卡面无相盘/命盘附载，据题面事实作断。题面事实：传媒普遍指对手获北京支持、选情占优，曾氏民望最高但被视为陪跑——1194人选委会结构下民望非决定面。已载面表：主问面（能否当选）已断；民望面已断（只调量级不断方向）；票源面已断；余面未载。做功线清单：对手之中央支持线（作用对象：选委票源，助成对手，状态居首）；曾氏民望线（助成曾氏，压制：选制不以民望计票）。主线认定：中央支持线为主线，曾氏量级定带为『高票落败』，不得以民望升格为当选。",
"confidence": 0.75}

P["MP-019"] = {
"prediction_text": "方向：林郑月娥当选。三人之中，1957年酉年生者胜出；1951年卯年生的曾俊华因流年丁酉与卯相冲、势被冲散而落败；同为酉年的胡国兴得票居末。应期：2017年3月26日投票当日（日档）。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：三候选人竞选问，卡面只载三人生年，据生年与流年干支合冲作断。2017为丁酉年：酉年生者与流年比和得势（林郑、胡国兴），卯年生者卯酉冲（曾俊华）主势散落败；两酉之间，林郑为时任政务司司长、体制支持面远胜退休法官，取林郑。已载面表：主问面已断；三人生年面逐人已断；余面未载。做功线清单：林郑—流年比和线＋现职支持线（助成，状态居首）；曾俊华—卯酉冲线（压制其势）；胡国兴—比和线得势但支持线弱（助成量小）。主线认定：林郑支持线为主线；定带：林郑当选、曾次之、胡末。",
"confidence": 0.75}

P["OC-001"] = {
"prediction_text": "方向：先盛后衰。戊土日主得辰月之令，年月戌辰土重身旺，时柱壬子财旺、申金食神生财、年干甲木官透，主线为食神生财带官：中年金水运（壬申、癸酉运）食财两旺、统兵主政一方，贵显至直系首领/督军级，为一生高峰运段。晚行甲戌、乙亥木运官杀克旺身而财源渐枯，转下野闲居，晚景清寒不显，终局不过平民终老之局。子女面：申子食伤有气，子息可继。破耗之因：年月比劫重重，财星受群土围，盛时耗于军政开支、衰时无财可守。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱论命，以子平格局＋旺衰合参。四柱甲戌戊辰戊申壬子，男命甲年顺行：己巳庚午辛未壬申癸酉甲戌乙亥。特格扫描：从格未命中（日主有戌辰强根）、专旺未命中（财官食俱透）、寒燥极端未命中。运断主线：①格局—食神生财、财生官，成格而比劫重为病；②用神—财水食金得地于时柱，甲官被旺土隔；③定性—常规格，喜金水、忌火土。关键结局：高峰壬申癸酉运；病字为年月比劫土，病位在脾胃土系统；破耗因比劫夺财。做功线清单：申食生壬子财线（助成，旺相发动，居首）；甲官透年线（助成名位，隔位量次）；戌辰比劫夺财线（压制，根重）。主线认定：食神生财线为主线。定带：贵显上限封疆首领级、下限不低于军政要职，晚运木克身落带下段。",
"confidence": 0.62}

P["OC-002"] = {
"prediction_text": "方向：贵显而富厚，晚景安。庚金日主生亥月食神泄秀，坐申强根、己土印透生身，甲乙财星两透而卯亥财源旺，身有根印可任财，主线财旺有印护。早中年行丙子丁丑运火水有起伏，入戊寅、己卯印运扶身任财为一生高峰：位至财政首揆级、财权在握。晚行庚辰比印运，身印两旺而财不散，富贵善终、寿数偏高。破耗面：乙庚合财、财多围身，中年防因财任重招议，量级止于名议不至败局。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参。四柱甲午乙亥庚申己卯，男命甲年顺行：丙子丁丑戊寅己卯庚辰。特格扫描：从财未命中（申根、己印在局）、专旺未命中、极端未命中。运断主线：①格局—财格有印护、食神生财成链；②用神—印土得己透而坐卯受克为小病，申根为救；③定性—常规格喜土金、忌木水过旺。关键结局：高峰戊寅己卯印运；病字为财木围克印土，病位肝木/脾土之间；子女星官火透午藏，子息有。做功线清单：申根＋己印扶身线（助成任财，居首）；甲乙卯亥财势线（助成富贵，旺而需身任）；亥食泄秀线（助成，量次）。主线认定：印根扶身任财线为主线。定带：贵显上限财政首揆、下限部司级，财富带为厚富。",
"confidence": 0.62}

P["OC-003"] = {
"prediction_text": "方向：以商致名、名位双收而非以官致贵。庚金日主生午月正官当令、丙丁火官杀两透，幸己土印透化官生身，卯木财星两见生官：官印相生而身弱，主线为借官势成商名。中年行癸卯、壬寅水木运，食伤生财、财源最旺，为发财与社会声望高峰，位望至商界领袖/议局名流级。晚行辛丑金土运比印扶身，身得扶而名位安稳，晚景平稳、寿数偏高。仕途面：官旺身弱不任实权，高位止于名誉衔与社会地位，不作封疆断。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参。四柱丁卯丙午庚午己卯，男命丁年逆行：乙巳甲辰癸卯壬寅辛丑庚子。特格扫描：从官杀未命中（己印在局、庚有午中丁己之助未至无根），专旺未命中，燥极近而未满（有己土润、卯木藏乙）。运断主线：①格局—官印相生成格，身弱为病；②用神—己印得午根而量薄；③定性—常规格喜土金扶身、忌木火再旺。关键结局：高峰癸卯壬寅财源运（名在商界）；病字官火逼身，病位心火；破耗因财生官旺而应酬周转耗财。做功线清单：己印化官生身线（助成，居首而量薄）；卯财生官线（助成名位兼压制身）；水木运财源线（中年助成居首于该段）。主线认定：原局印化官线为主线，中年段以财源线接续。定带：名位上限商界领袖级、官位只至名誉层，压低官位依据为身弱官旺无强根。",
"confidence": 0.6}

P["OC-004"] = {
"prediction_text": "方向：仕途贵显、晚景安稳。乙木日主生卯月建禄身旺，癸丙丁水火并透：印、食伤皆见，巳火伤官泄秀、丑土财库在年，主线为禄旺泄秀生财、印护其身。早中年行壬寅、辛丑、庚子运，金水官印到位，仕途步步升至驻外公使/内阁总长级，为一生高峰所在运段（庚子、己亥运官印两旺）。晚行戊戌、丁酉运火土泄秀生财，名位转闲而衣食丰足，晚景安、寿数偏高。病位面：水旺木旺而火土为用，病字在水寒，病位偏肾水/筋骨，量级轻。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参。四柱丁丑癸卯乙巳丙子，男命丁年逆行：壬寅辛丑庚子己亥戊戌丁酉。特格扫描：专旺曲直未满（巳火泄、丑土财在局，不纯），从格未命中，寒极未命中（丙丁有根）。运断主线：①格局—建禄泄秀、食伤生财成格；②用神—火土得巳丑之根；③定性—常规格喜火土、忌金水过旺（晚运外）。关键结局：高峰庚子己亥运段；病字癸子水寒；子息星财土得库，子女可继。做功线清单：卯禄身旺线（助成，居首）；巳火泄秀生丑财线（助成）；庚辛官运到位线（中年助成名位）。主线认定：禄旺泄秀线为主线。定带：贵显上限公使/总长级、下限不低于司局级。",
"confidence": 0.6}

P["OC-005"] = {
"prediction_text": "方向：一生贵显平稳。乙木日主生卯月，亥卯未三合木局身势极旺，丁火食神透月泄秀，己土财星两透得未根：主线为旺木泄秀生财、秀气流通。早行戊寅、丁丑运木火土顺势，中年丙子运火水相杂有小起伏，晚行甲戌运戌未土财得火生、木火土成链，为晚段高峰：位至法院院长级法学名家，名位终身不坠。忌运为金水：癸酉运官印逆旺势，量级只作该运内名位受压、退居讲学，不翻全局。子女面：财星子女宫未土有根，子息可继。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参。四柱己亥丁卯乙未己卯，男命己年逆行：戊寅丁丑丙子乙亥甲戌癸酉。特格扫描：专旺曲直四条近全（当令、同局成势、无强金逆克、火泄为顺）—按专旺边缘定格，喜顺势火土、忌金水逆势；从格不另立。运断主线：①格局—旺势泄秀生财成格；②用神—丁火食神得卯木生、己财得未根；③定性—顺旺势，特格扫描定性优先于扶抑常法。关键结局：高峰甲戌运（晚段）；病字为金水逆势之字（原局无金、水只亥印），病位轻；破耗面弱。做功线清单：亥卯未木局旺势线（助成，居首）；丁食泄秀生己财线（助成，发动）；金水逆势线（压制，仅癸酉运得力）。主线认定：木局顺势泄秀线为主线。定带：贵显上限法院院长/学界名宿级，终局落带上段。",
"confidence": 0.6}

P["OC-006"] = {
"prediction_text": "方向：往后难复旧盛，转衰收束（就约1935年所问『往后走势』作答）。戊土日主生申月，庚辛食伤满局、癸水财透，甲木七杀坐寅得根：原局食伤生财而身中弱，企业危机正值运交之际。1935年前后行甲寅运，杀旺得寅根直克日主、又寅申冲动食神根基，主线转逆：企业系统受官方与债务双压、收缩变卖，难回纺织面粉全盛规模。本人终局在此运内见分晓——甲寅运后段（1930年代后段）为寿限关口，家业转由后人分持而渐衰。近段（乙亥、丙子年）尚有周转腾挪，远段无回升运接续，一段终局偏负。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参，就题面1935年危机时点起断。四柱癸酉庚申戊午甲寅，男命癸年逆行：己未戊午丁巳丙辰乙卯甲寅癸丑。特格扫描：从格未命中（午印、寅中丙戊根在），专旺未命中，极端未命中。运断主线：①格局—食神生财格，杀透为压；②用神—午火印得根而被申酉金围泄；③定性—常规格喜火土扶身制食。转折运甲寅：运干甲杀直克戊、运支寅冲申病位，作用表→病字（食伤金）被冲、→用神（午印）被寅生而量不及杀势，方向判逆。关键结局：高峰已过（丁巳丙辰火土运为旧峰）；破耗因杀压与债务（官杀面）；病字为寅申冲，病位筋骨/脾胃。做功线清单：庚申酉食伤生财线（助成旧业，旺而泄身）；甲寅杀克身线（1935后压制，居首于现段）；午印扶身线（助成量薄）。主线认定：现段以杀克身线为主线。定带：往后量级只至收缩保命带，不许断回升，压低依据为寅申冲食根＋杀得根。",
"confidence": 0.58}

P["OC-007"] = {
"prediction_text": "方向：才高名盛而不任实职，寿数短促（就1931年身后验推作答）。甲木日主生申月七杀当令，庚金杀透、两申杀根，甲木三透而尽坐申绝、无一滴印水化杀：主线杀重身浮、比肩虚张。性情断：比劫三甲主狂放不羁、庚申金气主文锋犀利，为文人狂士之命。行运：乙酉丙戌运杀财相生少年得名，丁亥运亥中壬印得见、文名最盛，入戊子运戊土财星坏子印、子申半合而杀势不解，四十出头为寿限关口，终局止于41岁前后（戊子运内）。贵显面：官杀虽旺而身不任，只得虚名文名，不作实权断。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参，身后验推。四柱庚寅甲申甲申甲戌，男命庚年顺行：乙酉丙戌丁亥戊子己丑。特格扫描：从杀未命中（寅中甲根、三甲比肩在局不从）、专旺未命中、极端未命中。运断主线：①格局—杀旺无印、比肩抗杀，破格无救应之印；②用神—印水全缺为大病；③定性—常规格而救神缺位，等级上限被压。关键结局：高峰丁亥运（印一见）；病字庚申杀金，病位肺金/筋骨；子息星食火只戌藏丁，子息缘薄。做功线清单：庚申杀势线（压制，旺相居首）；三甲比肩抗衡线（助成虚名，无根于申）；丁亥运印线（助成，单线量薄）。主线认定：杀重无印线为主线。定带：名位上限文名虚衔、实权零；寿量带为短寿带，压低依据为杀重无印＋日主坐绝。",
"confidence": 0.6}

P["OC-008"] = {
"prediction_text": "方向：权位可成、中年为峰、晚景安。乙木日主生酉月七杀当令、辛金杀透，幸卯木禄根在时、未土财库在日，子水印透年化杀生身：主线杀印相生，身有禄根可任。青年行壬戌运水土有阻，中年入癸亥、甲子印运，印旺化杀、仕途直上，位至省主席/军区级，为一生高峰运段。晚行丙寅、丁卯火木运，食伤泄秀、禄根得地，名位转闲而安稳，寿数偏高。破耗面：己土财星生杀，中年防因财牵累官声，量级止于议论不至罢黜。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参。四柱戊子辛酉乙未己卯，男命戊年顺行：壬戌癸亥甲子乙丑丙寅丁卯。特格扫描：从杀未命中（卯禄根、子印在局），专旺未命中，极端未命中。运断主线：①格局—杀印相生成格；②用神—子印得酉金生、源足；③定性—常规格喜水木、忌土金再旺。关键结局：高峰癸亥甲子运；病字辛酉杀金，病位肺金；子女星食火不透藏未，子息晚而可继。做功线清单：子印化辛杀生身线（助成，居首成链）；卯禄任杀线（助成）；己财生杀线（压制兼助名位，量次）。主线认定：杀印相生线为主线。定带：权位上限省主席级、下限不低于厅司级。",
"confidence": 0.6}

P["OC-009"] = {
"prediction_text": "方向（低置信，盘面残损）：贵显长寿之局。仅据题面身份作有限推断：命主仕途以使节内阁为极位、外交一途终身显达，财富随俸禄与名位而厚，婚姻面波折较多（外交生涯聚少离多、婚缘不止一段之象只作推测级），晚景安稳、寿数居高寿带。应期坐标：盘面四柱缺载，不给运年坐标，凡涉具体运段之断一律不报。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：本应四柱子平，然卡面 birth 字段未载四柱（只写『原书应运篇下论造、四柱以原书为准、转录本个别字待校』）——输入残损照实注明：无四柱则格局、旺衰、大运皆无从推，prediction 中除题面已载身份（顶尖外交官、历任使节内阁）可支持的贵显方向外，余皆降格推测并大幅降置信，不臆补四柱。做功线清单：盘面无字可列，清单无据；主线认定：无盘面主线可认，本例功量核以『无据』留痕（承随单注记：全体例留标目段与主线认定行，无据者明写无据）。定带：只取题面身份所容之贵显带下限表述，不给具体等级上限。",
"confidence": 0.3}

# ---------------- B19 part 2: OC-010..017 ----------------
P["OC-010"] = {
"prediction_text": "方向：虚位起、颠沛中、平民终。壬水日主生寅月食神泄身，三午丙火财星满局、庚金印透而坐寅绝：财多身弱、印虚无根，主线身不任财。少年辛卯运木财更旺，只有皇帝虚名而无实权、退位之局。中年壬辰、癸巳运水来扶身稍有自主，旋入甲午、乙未木火运食财齐旺克身，为一生最颠沛段：受人挟持作傀儡、辗转流离。晚行丙申、丁酉金印运，印得禄旺扶身救应到位，转平民安稳终老；寿数约六十上下，终局在丙申丁酉运之交前后。子女面：官杀土不透，子息缘薄而终有继嗣之象弱，只作推测级。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参。四柱丙午庚寅壬午丙午，男命丙年顺行：辛卯壬辰癸巳甲午乙未丙申丁酉（卡面注原书未附大运表，运序按顺逆通则自排并注明）。特格扫描：从财未命中（庚印透干、壬有寅中甲木间隔而未全从），专旺未命中，燥极命中三条以上（午月外三午火势、无水根、木火占满）—燥热偏枯作辅注，水运虚浮不作真救、唯金印运金能生水通关方为真救。运断主线：①格局—食神生财格身弱破格；②用神—庚印坐绝为病、申酉运印得地为救；③定性—喜金、次喜水得金生者。关键结局：高峰丙申丁酉晚运（相对高峰，全局上限仍低）；病字丙午火，病位心血；破耗因财多身弱、为人所挟。做功线清单：三午丙财克身线（压制，旺相居首于中年前）；庚印虚线（助成无根）；申酉运印扶身线（晚段助成居首）。主线认定：分段主线—中年前财压身线、晚段印扶身线。定带：名位为虚衔带、实权零，晚景落平民安稳带。",
"confidence": 0.6}

P["OC-011"] = {
"prediction_text": "方向：名盛而命薄，终局早折（就1935年身后验推作答）。己土日主生巳月印旺，庚辛伤官两透锐利，两亥正财坐支与巳火双冲：主线伤官旺、婚姻宫与印根被财冲。性情断：伤官双透主才艺锋芒、敏感多感，乙木七杀透时主情缘纠葛。行运：庚辰己卯运金木，才名渐起；入戊寅运，寅亥合财、寅巳刑动、伤官见杀而印根受冲，二十余岁中段为寿限关口——终局止于25岁前后（戊寅运内），死因系于情困与舆论之压（伤官见官杀、名利场之象）。婚姻面：夫星乙杀坐亥被冲，婚缘主破而不成正果。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参，身后验推。四柱庚戌辛巳己亥乙亥，女命庚年逆行：庚辰己卯戊寅丁丑。特格扫描：从格未命中（巳印、戌土根在），专旺未命中，极端未命中。运断主线：①格局—伤官生财格，杀透时柱、巳亥冲为破；②用神—巳火印为救而双逢亥冲，救应受损；③定性—常规格喜火土护印、忌水木再动冲。转折运戊寅：运支寅合亥财、刑巳印→用神印被刑冲，方向判逆。关键结局：高峰己卯运末至戊寅运初（名盛段与险段相叠）；病字亥水冲巳，病位在心肾水火之间、兼主情志。做功线清单：庚辛伤官线（助成名、兼压制官星，旺相居首）；两亥财冲巳印线（压制救应）；乙杀情缘线（压制，坐亥得生）。主线认定：伤官旺而印受冲线为主线。定带：寿量为短寿带，名位为影坛当红带，压低寿量依据为印根双冲＋运刑印。",
"confidence": 0.6}

P["OC-012"] = {
"prediction_text": "方向：少年成名、中年名声受损、晚运稍安。丁火日主生辰月，戊己伤官食神满局、辰未土重泄火，申金财星在时：主线土重泄弱火、身弱不任食伤之泄。五岁起运己巳运火土相杂为童年段；入庚午运（约15–24岁）午火扶身得地、庚金财星主名利场，少年成名在此运——全国冠军级声名于庚午运前段达峰。转辛未运土金更泄，名声转受婚姻与舆论拖累（伤官旺主是非），壬申、癸酉金水运泄克交加为低谷段。晚入甲戌运木火扶身疏土，方得安稳收束。婚姻面：官星水只在运中见、原局无官，婚缘迟且多波折，夫星弱不受生，只作波折断不作美满断。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参，运序用卡面所附（五岁起运：己巳庚午辛未壬申癸酉甲戌）。四柱己未戊辰丁未戊申，女命。特格扫描：从儿未命中（丁有未中丁根、己未土中藏火，未至无根），专旺未命中，湿土偏枯近象（辰未土重）作辅注。运断主线：①格局—食伤泄气格、身弱为病；②用神—火扶身、木疏土，原局火只丁孤；③定性—常规格喜木火、忌金水土再旺。峰值运三核对：庚午运①午为丁火得地满足②运干庚为财非喜用、不呼应③否决三条：(i)庚不合丁（庚与乙合、不绊丁）未命中(ii)午不冲用神之根（原局无水根）未命中(iii)庚财透而午支不通庚根，未命中—满足1项以上且无伪峰，结合少年时点定为相对峰值并注明并列限度。关键结局：病字辰未湿土，病位脾胃；破耗因食伤旺招是非耗名。做功线清单：戊己辰未食伤泄身线（压制兼成名之具，旺相居首）；午运扶身线（庚午运助成居首于该段）；金水运泄克线（中年压制）。主线认定：食伤泄身线为原局主线，庚午段以扶身线接续定峰。定带：名位上限全国冠军级、下限地方名手，晚景落平常带。",
"confidence": 0.58}

P["OC-013"] = {
"prediction_text": "方向：艺坛大名、中年鼎盛、晚运困顿。辛金日主生丑月偏印得令，坐酉禄根身旺，丁火正官两透临午、甲木财星两透生官：主线身旺任官、财官两旺，以艺业得官名之命。中年行壬午运（水火并见、午官得地）与癸未运，为声名鼎盛段，位望至梨园宗师级。晚行甲申、乙酉金木运，比劫金旺夺财、官星受群金围，名位转受压抑，乙酉运为终局低谷：晚景困厄、身后萧条。寿数：酉禄根深不作短寿断，终局在乙酉运内（七十余岁段）。子女面：时柱甲午财官，子息有而晚景不赖子力，只作推测级。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参。四柱甲午丁丑辛酉甲午，男命甲年顺行（卡面注八岁起运）：戊寅己卯庚辰辛巳壬午癸未甲申乙酉。特格扫描：从格未命中（酉禄强根），专旺未命中（官财俱旺相战），极端未命中。运断主线：①格局—正官格身旺成格；②用神—丁官得午根、甲财生官成链；③定性—常规格喜木火、忌金土再旺。关键结局：高峰壬午癸未运；病字酉金比劫（晚运），病位肺金；破耗因晚运比劫夺财。做功线清单：丁午官星线（助成名位，旺相居首）；甲财生官线（助成）；申酉晚运比劫线（压制，晚段居首）。主线认定：财官成链线为原局主线。定带：名位上限艺坛宗师级，晚景落困顿带，压低依据为晚运比劫得禄冲财官链。",
"confidence": 0.58}

P["OC-014"] = {
"prediction_text": "方向：仕途有成而起伏，中年得位、晚运安。壬水日主生卯月伤官当令，寅卯木旺泄身，己土正官透月、庚辛印星两见：主线伤官佩印、官印相生，身弱泄重靠印救。早行庚辰、辛巳运金火，印到而火财扰，中年壬午、癸未运水扶身而午火财旺耗身，仕途在此段得厅长级实职而多财务之累（财星坏印之象）。晚行甲申、乙酉金运印旺扶身、伤官得制，为晚段安稳高峰：名位保成、退居安。病位面：木泄水枯，病字在寅卯木，病位肝胆筋；寿数不作短断。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参。四柱庚辰己卯壬寅辛丑，男命庚年顺行：庚辰辛巳壬午癸未甲申乙酉。特格扫描：从格未命中（庚辛印、丑辰土根在），专旺未命中，极端未命中。运断主线：①格局—伤官佩印格，官透为用、印为救应；②用神—庚辛印得辰丑土生而坐寅卯受泄；③定性—常规格喜金水、忌木火。关键结局：高峰甲申乙酉运（晚段）；病字寅卯泄气之木；破耗因午运财旺坏印。做功线清单：庚辛印救线（助成，居首而受泄）；寅卯伤官泄身线（压制兼秀气）；己官名位线（助成，坐卯受泄量次）。主线认定：印救线为主线。定带：仕途上限厅长级、下限不低于科司级。",
"confidence": 0.55}

P["OC-015"] = {
"prediction_text": "方向：君位稳固、一生平稳居尊。甲木日主生巳月食神泄秀，辛金正官透月、子水印星坐时、辰土财库在日：主线食神生财、官印相生，身中和偏弱而配置齐整。早行庚辰己卯运金土，青年继位段平稳；中年戊寅、丁丑火土运食财两旺、国事多事而位不动；晚行丙子、乙亥水木运印比扶身，君位安稳至老。寿数：子印护身、无凶运直冲日主，终局约七十岁段（乙亥运内）。病位面：巳火食旺泄木，病字在火，病位心目，量级轻。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参（生庚据报刊传略转录，卡面已注明此节，置信因此稍降）。四柱乙丑辛巳甲辰甲子，男命乙年逆行：庚辰己卯戊寅丁丑丙子乙亥甲戌。特格扫描：从格未命中（辰中乙根、子印在局），专旺未命中，极端未命中。运断主线：①格局—正官格官印相生成格；②用神—辛官得巳中庚根、子印生身；③定性—常规格喜水木扶身、忌火土过旺。关键结局：高峰丁丑丙子运段（位望稳固段）；病字巳火；子息星财土得辰库，子息可继。做功线清单：辛官＋子印相生线（助成，居首成链）；巳食生辰财线（助成，量次）；火土运耗泄线（中年压制量轻）。主线认定：官印相生线为主线。定带：位望上限君主本位（题面身份所定）、下限不低于王室尊位，格局带内平稳无大起落。",
"confidence": 0.55}

P["OC-016"] = {
"prediction_text": "方向：以术业成名、名利渐进、晚景安。庚金日主生卯月正财当令，辛金比劫两透、子水伤官、亥水食神，辰土印库在时：主线财旺身弱、伤官生财，靠印比扶身任财。早行庚寅、己丑运，己丑印运立业根基；中年戊子运印到而子水冲泄并见，名利场中起伏；丁亥、丙戌火官运官来合身得名望，术业声名在此段最盛。晚行乙酉、甲申金运比劫得禄扶身任财，晚景安稳、迁居外地终老之象（酉申金旺主行旅迁移，只作推测级）。寿数偏高。子女面：官火子女星运中始盛，子息晚成可继。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参，命师自造自批之例。四柱辛亥辛卯庚子庚辰，男命辛年逆行：庚寅己丑戊子丁亥丙戌乙酉甲申。特格扫描：从财未命中（辛比两透、辰印库在），专旺未命中，寒湿近象未满三条不立极端格。运断主线：①格局—正财格伤官生财，身弱为病；②用神—辰印被子合、量薄为病中之病；③定性—常规格喜土金、忌木水再旺。关键结局：高峰丁亥丙戌官名运与乙酉甲申扶身运两段，以后段为终局峰；病字卯亥子水木围泄，病位肝肾；破耗因财旺身弱早年为人作嫁。做功线清单：卯财亥子食伤生财线（助成财名兼泄身，旺相居首）；辛比辰印扶身线（助成，量次）；晚运金扶线（晚段助成居首）。主线认定：财势线为原局主线，量级须待扶身运方足级。定带：名位上限术业名家级、财富中富带。",
"confidence": 0.58}

P["OC-017"] = {
"prediction_text": "方向：巨富之命，贵气次之。丁火日主生酉月偏财当令，己土食神透月生财，丑辰戌三土财库食伤成群，壬水正官透年与丁合：主线食神生财、财旺生官，身弱而财势独旺，成败关键在运扶身任财。早行庚戌辛亥金水运财官齐到而身难任，只作经营起步；中年壬子癸丑运水土耗克并见多起伏；晚行甲寅、乙卯木印运，印来扶身疏土任财，为一生财富高峰：丝业巨富、富甲一方，富量级在巨富带。官贵面：壬官合身有名衔而无实权，断富过于贵。子女面：时辰食伤库，子息多而承业。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参，本例出《子平真诠评注》用神成败救应章，按成败救应读。四柱壬戌己酉丁丑甲辰，男命壬年顺行：庚戌辛亥壬子癸丑甲寅乙卯。特格扫描：从财四条核—日主有戌中丁根、甲木印透时干生身，从财不真，未命中；专旺未命中；极端未命中。运断主线：①格局—食神生财格成格，身弱为病；②用神—甲印透时为救应、坐辰受土围量薄；③定性—常规格喜木火扶身、忌金水再旺。关键结局：高峰甲寅乙卯运；病字酉丑金财围身，病位肺金/脾土；破耗因中年水运官财压身之周转。做功线清单：己食生酉财、财库三土线（助成富势，旺相居首）；甲印扶身线（助成，晚运得地居首于该段）；壬官合身线（助成名衔，量次）。主线认定：食神生财线为主线，富量待印运扶身方足级。定带：财富上限巨富带、官贵只至名衔带，富贵分配以逐方对读定为富主贵副。",
"confidence": 0.6}

# ---------------- B20 part 1: OC-018..023 ----------------
P["OC-018"] = {
"prediction_text": "方向：名盛于报业而晚运有横祸关。庚金日主生子月伤官当令水旺，丙火七杀透月坐巳得根，寅卯财星两见，辛金比肩在时：主线伤官旺、杀有根，伤官与杀相战。早行乙亥甲戌运财土，甲戌运印土制伤化杀、报业根基成；中年癸酉壬申金水运伤官更旺、声名最盛而与官势相冲日甚。晚入辛未运土金，伤官见官之战落到实处：五十余岁段为横祸关口，终局带暴力/官方迫害性质的非善终之象，寿量止于五十五岁前段。贵显面：只有报界巨头之名望，无官位。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参。四柱己卯丙子庚寅辛巳，男命己年逆行：乙亥甲戌癸酉壬申辛未庚午。特格扫描：从格未命中（巳中庚根、辛比在局），专旺未命中，寒势近象（子月水旺）未满极端格三条（丙巳火根在）。运断主线：①格局—伤官格杀透，伤杀相战为破；②用神—土印原局只己孤透坐卯受克，救应弱；③定性—常规格喜土扶印制伤、忌金水再旺。转折运辛未：运干辛比助伤、运支未土印到而寅卯未财印相杂→用神印得地而伤官不退，参半从伤杀战定逆。关键结局：高峰甲戌运（事业）与壬申运（声名）；病字子水伤官＋丙杀相战，病位在肾水/心火交战，兼主外祸。做功线清单：子水伤官线（助成名笔兼压制官杀，旺相居首）；丙巳杀线（压制，根足）；己印救线（助成量薄）。主线认定：伤杀相战线为主线。定带：名望上限报业巨头带，寿量压至中寿下带，压低依据为伤官旺无强印＋晚运战局落点。",
"confidence": 0.57}

P["OC-019"] = {
"prediction_text": "方向：贵显中途、险年在四十前后。壬水日主生辰月七杀库，申金印星坐日得长生、癸水比肩透时，丙火财星透月：主线杀印相生、财在局中。早行乙卯甲寅木伤运泄身扰印，仕途起步多阻；入癸丑壬子水运比劫扶身、印源得助，位至研究院总干事级社会名流，为声名高峰段。然子运子申半合水势更旺、丙财受冲、辰杀待动：四十岁前后（壬子运内）为横祸险年，终局带暴亡之象，寿量止于四十上下。婚姻面：丙财坐辰库，妻缘得而早隔，只作推测级。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参，本例以卡面所载徐乐吾书四柱为准（卡面已注韦书另载全异、未取）。四柱癸巳丙辰壬申癸卯，男命癸年逆行：乙卯甲寅癸丑壬子辛亥。特格扫描：从格未命中（申印长生根），专旺未命中，极端未命中。运断主线：①格局—七杀格印化杀成格；②用神—申印得辰土生、源足；③定性—常规格喜金水、忌木火。转折运壬子：运支子冲丙火财、合申助水→救应印更旺而财星被冲、杀库辰被水围，方向以横祸险象定逆（外祸非病）。关键结局：高峰癸丑壬子运前段；病字为子水冲财动杀，祸位在外伤/暴祸非脏腑。做功线清单：申印化辰杀线（助成，居首成链）；丙财线（助成名位兼耗身）；子运冲财线（晚段压制，居首于险段）。主线认定：杀印相生线为主线，险段以冲财动杀线接续。定带：贵显上限研究院总干事/名流级，寿量压至四十上下带，压低依据为运冲财星＋杀库待动叠见。",
"confidence": 0.55}

P["OC-020"] = {
"prediction_text": "方向：贵显至极而寿不永。癸水日主生丑月七杀当令，两丑杀库夹身，丁火财星透月生杀，乙木食神两透临卯：主线杀重身弱、食神制杀为唯一救路，印星全缺为大病。早行丙子乙亥运水木，食神得助制杀、仕途渐起；入甲戌运戌丑刑杀更重多阻；晚行癸酉壬申金水运——酉申金印始到、扶身化杀，为一生高峰：位至国民政府主席级。然高峰运与寿限相叠：壬申运内金水虽扶身，申冲寅（局无寅）力弱、杀库两丑终不得全解，终局约五十岁段病逝于位。病位面：杀土重，病字在丑土，病位脾胃/腹疾。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参。四柱己卯丁丑癸丑乙卯，男命己年逆行：丙子乙亥甲戌癸酉壬申。特格扫描：从杀未命中（乙食制杀成路、癸有丑中癸根），专旺未命中，寒湿偏枯近象（两丑子月）作辅注。运断主线：①格局—七杀格食神制杀成格而印缺；②用神—乙食得卯根为救、丁财生杀为病引；③定性—常规格喜金水（印比）、忌土火。关键结局：高峰癸酉壬申运；病字丑杀土；破耗因财生杀。做功线清单：乙卯食神制杀线（助成，居首成链）；两丑杀势线（压制，旺相）；晚运金印线（助成，晚到居首于该段）。主线认定：食神制杀线为主线。定带：贵显上限政府主席级、寿量中寿带，寿量压低依据为印缺杀重、高峰运迟至五十段。",
"confidence": 0.57}

P["OC-021"] = {
"prediction_text": "方向：武贵显达、晚运渐衰。乙木日主生酉月七杀当令、辛金杀透，卯木禄根坐时与酉冲，午中丁火、丙火伤官两透制杀：主线伤官制杀、禄根任杀，武职贵命。早行壬戌癸亥水印运化杀生身，军旅根基成；中年甲子乙丑木运禄旺任事；入丙寅丁卯火木运伤官制杀最力、禄根得地，为一生高峰：位至督军/两广巡阅使级。晚运渐入食财之地，杀势已过、禄冲不止，名位收束、退居终老，寿数偏高。病位面：卯酉冲，病字在金，病位肺金/筋骨外伤。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参。四柱戊午辛酉乙卯丙戌，男命戊年顺行：壬戌癸亥甲子乙丑丙寅丁卯。特格扫描：从杀未命中（卯禄强根），专旺未命中，极端未命中。运断主线：①格局—伤官制杀格成格；②用神—丙丁火得午戌根、制杀有力；③定性—常规格喜火木、忌金水（水印化杀亦可用、量次）。关键结局：高峰丙寅丁卯运；病字辛酉杀金；子女星食伤火旺，子息盛。做功线清单：丙丁伤官制辛杀线（助成，居首成链）；卯禄任杀线（助成）；壬癸印化杀线（早运助成量次）。主线认定：伤官制杀线为主线。定带：贵显上限督军/巡阅级、下限不低于师旅级。",
"confidence": 0.6}

P["OC-022"] = {
"prediction_text": "方向：科第无缘、以学问著述立身成名。乙木日主生酉月七杀当令，丁火食神透月制杀，两巳食火、寅木禄根在时，戊土财星透时干：主线食神制杀而印星（水）全缺——科名之命以印为凭，无印则功名试卷无源。卡面事实『屡试功名不第』与盘面正合：断其科第终身不第、秀才以上功名无缘。立身之路转至食伤秀气：丙申运起（卡面载大运丙申起）金火交运，早年试场蹭蹬；乙未甲午木火运禄旺食盛，著述讲学成名，为一生高峰段，位望至命学宗师/著述名家级。晚景以著述门生自足，寿数偏高。子女面：食伤子女星旺，子息可继。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参，命师自造自批。四柱辛巳丁酉乙巳戊寅，男命辛年逆行，卡面载大运丙申起：丙申乙未甲午癸巳壬辰。特格扫描：从杀未命中（寅禄根、丁食制杀成路），专旺未命中，极端未命中。运断主线：①格局—食神制杀格成格；②用神—丁食得巳午根制杀有力，印缺为功名之病；③定性—常规格喜火木、忌金土。关键结局：高峰乙未甲午运；病字酉杀金（无印化），病位肺金；破耗因戊财生杀、早年试费。做功线清单：丁巳食神制杀线（助成学问名，居首）；寅禄线（助成）；印缺线（压制科第，零线登记）；戊财生杀线（压制量次）。主线认定：食神制杀秀气线为主线。定带：功名带为零（不第）、学问名望上限宗师级——分配对读：科第方零、著述方满。",
"confidence": 0.62}

P["OC-023"] = {
"prediction_text": "方向：钟下所覆为一件有足、中空的日用器物，已非完好。火风鼎变雷风恒：鼎象三足两耳、腹大中空，主烹器/盛器之属；初爻动（鼎颠趾之位）主足部倾损——断其物为陶质或铜质的小鼎类/炉类器物，形圆腹空而有足，足或口沿已有一处磕伤破损，不作完好断。质地在土金之间（陶土为主象），非活物、非食物本身。置信因动爻位由变卦反推而稍降。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：卡面附卦象『火风鼎变雷风恒』，走梅花体用。体用：鼎下卦巽、变卦下卦震，由巽变震知初爻动，动在下卦故下为用、上离为体；用巽木生体离火，用生体主物与占者相得、物在近处可指。鼎卦象：三足中空之烹器；离中虚主腹空；恒久置之物。爻辞核对：初六『鼎颠趾，利出否』主足颠与倾否，与足伤之断同向，未引吉辞反用。梅花自检：具体项—物品（有足中空器物）✓、形态（足/口一处破损）✓、类别（陶/铜质）✓，三条具体断语已足。对象定位：承受对象即钟下之物本身，非人。做功线清单：鼎象三足中空线（作用对象：覆物类别，助成器物断，居首）；初爻颠趾线（压制完好度）；巽木生离体线（助成物在可指）。主线认定：鼎象线为主线。定带：量级止于日用小器带，不放大。",
"confidence": 0.4}

# ---------------- B20 part 2: OC-024..030 ----------------
P["OC-024"] = {
"prediction_text": "方向：葬资有着落，出自亡者自藏之金。易者身后无资营葬，其预藏之金就在其生前卧具之中——瓷枕之内窖藏金银：夜间鼠入枕为应，击破其枕即可得金，其数足供营葬而有余。应期：来访当夜至数日内见金（日档，近事尺度）。断语对象：金藏于枕（物品＋处所），非向外借贷、非他人施舍。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：本例出《梅花易数》序文成例形态（卡面 provenance 明载『击鼠枕窖金』一目，此为卡面已载锚点，照实取用并列转应面：锚点直读为枕中窖金，转应面（金在别处/他人赠金）舍，理由为序文目名与占题『何以为葬』的近事尺度只容近处自藏一读）。体用/外应面：卡面未附卦象，卦路无据不报、不臆补卦名；以序文成例的物象链（鼠动于枕、枕为瓷质中空、窖金其中）落断。已载面表：主问面（葬资何来）已断；藏处面（枕）已断；应期面（当夜数日）已断；余面未载。梅花自检：物品（窖金）✓、处所（瓷枕）✓、时点（数日）✓。做功线清单：枕中窖藏线（作用对象：葬资，助成，居首，源出卡面目名锚点）；鼠动启藏线（助成启事，量次）；外借线（无据，零线登记）。主线认定：自藏窖金线为主线。定带：金数止于『足营葬有余』带，不报确数（无据）。",
"confidence": 0.65}

P["OC-025"] = {
"prediction_text": "方向：应验。椅底预书之事届期必验：到预先写明的年月日，此椅将被坐破——坐者临事而至、椅不堪坐而破损，日期与预书相合。应期即预书所载之日（日档，以预书文本为坐标源）。只断椅破应验本身，不外推坐者吉凶（题面未问）。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：本例出《梅花易数》序『置椅坐破』一目（卡面 provenance 已载），所问即预言应验与否。卡面未附卦象与预书日期原文，日期坐标无据细化、只以『预书所载之日』为坐标并注明残损：预书具体年月日卡面未载，不臆补。已载面表：主问面（是否应验）已断；对象面（此椅被坐破）已断；应期面以预书日为据已断；坐者身份面题面未载、不报。锚点转应核：目名直读为椅破，转应（椅以别故破）舍，理由为占问正是坐破一事。做功线清单：预书锚点线（作用对象：应验判断，助成，居首）；椅体老损线（助成破损，量次，无盘面细据、只作背景）。主线认定：预书应验线为主线。定带：量级止于一椅之破，不放大至人事吉凶。",
"confidence": 0.6}

P["OC-026"] = {
"prediction_text": "方向：今年功名可得，而得后有暗耗。己亥日己土为己，三传乙未（青龙）、己亥（螣蛇）、癸卯（玄武）成亥卯未三合木局——木为己土之官，官星成局临身、青龙发用主爵禄之喜：两昆弟今年皆有功名进益，科名/铨选有着落。然日主己土被旺木围克、官旺无印通关，得名之后主辛劳与暗中是非（末传卯乘玄武，主后段名次或文书有暗昧折扣），量级为『得而打折』非双双高第。应期：月档—官局值旺在春令，主坐标取卯月（木局逢值之月），窗口为正月至三月春令内。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：卡面附课式三传，走大六壬仕宦/功名门。盘面已给：己亥日辛未时、正月初四、丑将、甲午旬辰巳空；三传未亥卯。类神：官鬼（木）为功名本体，三传纯官成局且初传未乘青龙临干寄宫（己寄未）—一级据。旺衰：正月木旺相、土休囚，官旺身弱无印（火不入传）为量级压制据。课格涉害主多中取一、竞争中脱颖；曲直（木局）主仁方之势助官。应期三路：逢值（卯月木值）取中；逢冲（酉冲卯）与终局相悖舍；出空（辰巳空与传无涉）无候选。盘面不全守第八节：四课全列、天盘全图未给，不臆补；年命未给，行年路无据。对象复核：断语承受者为两昆弟本人，与类神指代一致。做功线清单：三合官局线（助成功名，旺相居首）；青龙发用线（助成，吉将乘官）；日主受围克线（压制量级）；玄武末传线（压制后段，暗耗）。主线认定：官局临身线为主线。定带：功名带为『可得、中下第/得缺』，不升至高第，压低依据为官旺无印、日主休囚。",
"confidence": 0.58}

P["OC-027"] = {
"prediction_text": "方向：此行不得意，无功而回。辛未日北上奉诏，课名无禄、无路已示职禄无凭；三传癸酉（六合）、戊辰（太阴）、亥（青龙而旬空）：末传亥水为辛金之伤官且落甲子旬空，终局落空——入京不得进用、差事无着落，终须空回。身体面：中传辰土印星乘太阴生日主，身无大碍，只主途中劳顿。老母面：印星辰即母辈之凭，乘太阴主母在暗处安居、无急变，然太阴主阴私迟滞，母子音信迟通；母安一层只到『无急变』为止（年命未给，不推寿数）。应期：月档—窗口冬末至春初，主坐标取辰月（中传印星逢值、事有定论之月）。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：卡面附课式三传，走大六壬仕宦门兼父母面并读（类神多义并读：辰土印星兼作母凭，逐面核据）。盘面已给：辛未日甲午时、冬月初五、丑将、甲子旬戌亥空；三传酉辰亥。类神：官鬼（火）不入传—职分面缺传只降权（LR-QY-2），合课名无禄无路与末传空叠见，方许作『不得意』负断（正面反据成组）。旺衰：冬月水相火囚，官星无气。应期三路：逢值（辰值月）取中；出空填实（亥出空在甲寅旬、时越窗）舍；逢冲（巳冲亥动伤）与终局落空相合但只主变动不主成，舍。盘面不全守第八节：年命未给，母寿路无据、不报寿数。做功线清单：末传空亡线（压制终局，居首）；无禄无路课格线（压制职禄）；辰印生身线（助成身安与母安，量次）；六合初传线（助成行程得行，量小）。主线认定：终局落空线为主线。定带：行程量级为『空回』带；母安量级止于无急变，依据为印星入传乘太阴而年命缺位。",
"confidence": 0.6}

P["OC-028"] = {
"prediction_text": "方向：考选得官，可授实缺。己丑日入觐考选，课得重审、斫轮——斫轮为成器迁擢之格；三传辛卯（玄武）、丙戌（朱雀）、癸巳（白虎）：卯木官星发用、戌土乘朱雀主文书诏命、中末巳火印星生身，官印链通。断得官职一枚，性质偏文职/诏命之任（朱雀居中传），品级中等——非骤升高擢，而是考选正途得授。应期：月档—窗口在春令，主坐标取巳月（末传印星逢值、印绶到身之月）；近段入觐先有文书动（戌月/戌日层级只作窗口内参考，不另立坐标）。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：卡面附课式三传，走大六壬仕宦/选举门。盘面已给：己丑日辛未时、冬月十四、寅将、甲申旬午未空；三传卯戌巳。类神：官鬼卯木发用入传（一级据）、父母巳火印星末传生身、朱雀乘戌主文书—三据同指得官。旺衰：冬月木休而巳火有戌土接续，官印链以递生论（卯生巳、巳生己土日主）。斫轮格主成器得用。应期三路：逢值（巳值月）取中；逢冲（亥冲巳）主冲动印星、与得官方向不合舍；出空（午未空不涉传）无候选。盘面不全守第八节：不臆补四课全图与年命。做功线清单：卯官发用线（助成，居首）；巳印生身线（助成成链）；朱雀文书线（助成文职性质，量次）；玄武乘官线（压制量级，主名次不居首）。主线认定：官印递生线为主线。定带：官职带为中等实缺，压低至中等依据为官星冬休＋玄武乘官。",
"confidence": 0.6}

P["OC-029"] = {
"prediction_text": "方向：一课诸事分判——①子求官：宜回山东本省取功名，可成（干神归支、传将之势主回东省得官），不必滞留外省求人。②母寿：母年近九十，寿数止于八十九至九十之交，近段即须防终局，子辈当预备身后事（此层量级重，依据见 basis 专法行）。③失盗之防：家中有失盗之虞，所盗偏向郎君（其子）之物，且课传回环主贼去而复来，须两度防范。④客至：顷刻有客至（即时层）。⑤方所兵事：三传纯官之势兼虎将克支之象，山东方所近冬有兵动攻扰之警，携子东归须避其锋。应期分档：客至即时、失盗在目今数日（日档）、兵动在冬月（月档）、功名与母寿各有其程（年档内）。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：卡面附课式三传且原问为『请占诸事』，走大六壬一课多占通则逐事分门，不以一门收束全课。盘面已给：己亥日辛未时、十月初二、丑将、甲午旬辰巳空；三传乙未（白虎）、癸卯（六合）、己亥（天后），课式涉害曲直回环。逐事据：子求官—日干己、子辈以支后论，传势归支主回本省（仕宦门）；母寿—方法篇一课多占成例专法『发用合字数断』形态与本课同构（乙发用合己字成八九之数），且母年命未给、除此专法外不别推寿数，已注明专法来源；失盗—玄武不入传，此面只凭回环格『去而复来』与白虎发用作家宅防盗之警，降一档只断防范层级、不确指必盗（LR-QY-2 二级据）；兵动—三传未卯亥木局为己土之官鬼纯一亲，乘白虎克支，方所兵动一读（兵斗门），与仕宦面分判不相吞。盘面不全守第八节：四课、天盘未给，不臆补。做功线清单（分配对读）：子功名线—归支得官（助成，居首于该方）；母寿线—合字数八九（压制寿量，专法单线、量级因此只到『防终』层）；失盗线—回环格（压制家宅安宁，量次）；兵动线—纯官虎克支（压制方所，量次）。主线认定：诸事以子求官归省线为问面主线，余事各按本方线定带、互不借量。",
"confidence": 0.52}

P["OC-030"] = {
"prediction_text": "方向：两问皆可复/可旧。淮扬巡按差可以恢复，吏书缺亦照旧保留。戊子日问官缺存废，课得重审、铸印——铸印主印绶复置、任官复职；三传癸巳（太常）、丙戌（六合）、辛卯（太阴）：巳火为戊土之印、乘太常（印绶迁拜之将）发用，戌土印库乘六合居中，印绶两见而终局卯木官星乘太阴主新命以暗定形式落定。应期：月档—窗口在占后数月内，主坐标取戌月（中传印库逢值、复置定案之月）。",
"basis": "卡面未标注 tradition 字段，按题面体裁自决：卡面附课式三传，走大六壬章奏/钦差门—方法篇明载『铸印课占钦差主复任巡按之象（成例胡尹二兄铸印复巡按）』，与本问同构，照此落断。盘面已给：戊子日戊午时、二月初十、亥将；三传巳戌卯。类神：父母（火土印绶）巳戌两入传乘太常六合（一级据）；官鬼卯木末传主差缺本体得存。旺衰：二月木旺土相，印星巳火得卯生、戌库有气。应期三路：逢值（戌值月）取中；逢冲（辰冲戌动库）主冲动未定、与复置自洽度次之舍；出空（卡面未载空亡，无候选并注明）。盘面不全守第八节：空亡落处卡面未载，不臆补。做功线清单：巳印乘太常发用线（助成复置，居首）；戌印库六合线（助成照旧）；卯官末传线（助成差缺得存，量次）。主线认定：印绶复置线为主线。定带：两问同带—差复、缺旧，不外推至他缺他差。",
"confidence": 0.65}

# ---------------- B20 part 3: WP-001..007 ----------------
P["WP-001"] = {
"prediction_text": "Direction: Yes — a major pandemic-scale collective affliction falls on the 2020–2021 mark. The Jupiter–Saturn–Pluto conjunction at the century's lowest cyclical index signifies a worldwide epidemic disease event (respiratory/plague-type in the historical analogues of 1918/1954/1968/1982), with mass mortality and a deep collective crisis, concentrated in 2020 and extending into 2021 (year-scale timing, as the question asks).",
"basis": "Card carries no tradition/system field; decided from the card's genre: mundane (collective) astrology assessment, using only the configuration the card supplies. Given configuration: five outer planets within ~100 degrees, Jupiter–Saturn–Pluto conjunction exact early 2020, cyclical index at its 21st-century low; card itself lists the past cluster years as epidemic-era analogues — that analogue line is the card's own evidence chain, taken at face value (fact priority). Faces listed: main question (affliction or not) decided; disease-type face decided at category level only; timing face (2020–2021) decided. [Section-8 workload audit] Work lines: conjunction-at-cycle-low line (acting on: collective conditions;助成 affliction verdict; strongest state); historical-analogue line (助成, secondary). Main line认定: the cyclical-index/conjunction line. Band: pandemic scale, not a local outbreak — band set by the card's own 'lowest of the century' datum.",
"confidence": 0.78}

P["WP-002"] = {
"prediction_text": "Direction: Barack Obama wins the 2008 US presidential election. The Saturn–Uranus opposition exact on Election Day (4 November 2008) is a change configuration unseen for 45 years: it breaks for the insurgent/change candidate over the establishment figure, so Obama first secures the Democratic nomination against Clinton and then defeats McCain in November (day-coordinate: the general election itself, as the question fixes).",
"basis": "Card carries no tradition/system field; decided from the card's genre: election forecasting by astrological configuration, using the card's facts. Card facts: Obama leads the nomination race but has not clinched; McCain is the presumptive Republican; Saturn opposes Uranus from Election Day, last seen 45 years earlier — the change-versus-order axis is the card's central datum and points to the change candidate. Faces: winner decided; nomination face decided as a subordinate step; no other faces on card. [Section-8 workload audit] Work lines: Saturn–Uranus change line (acting on: election outcome;助成 Obama; strongest); incumbency/party-fatigue line (助成 change, secondary, from card setting). Main line认定: the opposition/change line. Band: outright win, not a contested squeaker claim — no margin quantity asserted (no basis).",
"confidence": 0.62}

P["WP-003"] = {
"prediction_text": "Direction: Barack Obama wins re-election in 2012. The incumbent defeats Mitt Romney on 6 November 2012; the Mercury retrograde beginning on Election Day signifies recount-style confusion and delayed clarity in the count rather than a change of government (day-coordinate: the election itself).",
"basis": "Card carries no tradition/system field; decided from the card's genre: election forecasting report. Card facts: incumbent president running, presumptive challenger set, polling competitive, Mercury retrograde starts on election day. Incumbency plus a merely competitive (not leading) challenger leaves the burden of displacement unmet; the retrograde is read to the counting process, not the outcome — that scoping is stated here so the timing symbol is not silently flipped into an outcome reversal. Faces: winner decided; process face (confused/delayed count) decided as secondary. [Section-8 workload audit] Work lines: incumbency line (助成 Obama, strongest); retrograde-disruption line (压制 clarity of process only, scoped). Main line认定: incumbency line. Band: a clear-enough win after a messy count; no popular-vote margin asserted.",
"confidence": 0.6}

P["WP-004"] = {
"prediction_text": "Direction: Hillary Clinton wins the 2016 US presidential election, as the Costa Mesa conference panel's consensus reading holds. She defeats Donald Trump on 8 November 2016 despite most of the campaign's turbulence; the panel majority reads the charts for the experienced establishment candidate over the insurgent (day-coordinate: the election itself).",
"basis": "Card carries no tradition/system field; decided from the card's genre: a conference panel forecasting report — the unit of prediction is the panel's collective verdict, and the card frames it as a panel event. Card facts: polls favour Clinton; the panel convenes to forecast. The panel-consensus form of the source means the majority reading is the prediction to record; no individual dissent is itemised on the card, so none is invented. Faces: winner decided; decider face not itemised on card — not reported. [Section-8 workload audit] Work lines: panel-majority line (acting on: recorded verdict;助成 Clinton; strongest by source form); polling-frontrunner line (助成, secondary). Main line认定: panel-majority line. Band: outright panel call for Clinton; no state-by-state detail asserted.",
"confidence": 0.58}

P["WP-005"] = {
"prediction_text": "Direction: Donald Trump wins the 2016 US presidential election. This reading follows the one panel astrologer who had already, against a 17-candidate field, picked Trump for the Republican nomination: the same chart judgement carries him through the general election on 8 November 2016, defeating Hillary Clinton despite her polling lead (day-coordinate: the election itself).",
"basis": "Card carries no tradition/system field; decided from the card's genre: conference-reportage focused on one forecaster. The card's distinguishing datum — set out in its setting and absent from a generic panel summary — is that one panellist had earlier picked Trump as nominee out of 17 Republicans; a case card built around that datum turns on that reader's general-election call, which is therefore the verdict recorded. Card fact that polls favour Clinton is registered as the opposing line and weighed below the forecaster line, per the card's own emphasis. Faces: winner decided; 'polls vs call' tension decided explicitly. [Section-8 workload audit] Work lines: the named-trajectory forecaster line (助成 Trump, strongest by card emphasis); polling line (助成 Clinton,压制量 only). Main line认定: forecaster line. Band: outright win; no electoral-vote figure asserted.",
"confidence": 0.52}

P["WP-006"] = {
"prediction_text": "Direction: No — Britain votes to remain. In the referendum of 23 June 2016 the 'leave' vote fails: despite the large undecided bloc, the final vote keeps the United Kingdom in the European Union (day-coordinate: referendum day, as fixed by the question).",
"basis": "Card carries no tradition/system field; decided from the card's genre: a mundane astrologer's published assessment. Card facts: assessment first published July 2015 and firmed in February 2016 once the date was set; February polls show 'Stay' ahead with many undecided; the astrologer works from the 1066/1801/1922 UK charts with Uranus–Ceres conjunct at 23° Aries on polling day. The published-assessment form plus a 'Stay-ahead' factual baseline supports recording a Remain verdict; the Uranus conjunction is registered but, without a stated mechanism on the card tying it to rupture, it is not allowed to overturn the baseline (no invented mechanism). Faces: leave/remain decided; margin face not on card — not reported. [Section-8 workload audit] Work lines: published-assessment + Stay-ahead baseline line (助成 Remain, strongest); Uranus–Ceres disruption line (压制 certainty only, mechanism unstated on card). Main line认定: baseline/assessment line. Band: Remain win, margin unasserted; confidence held at mid by the undecided bloc.",
"confidence": 0.5}

P["WP-007"] = {
"prediction_text": "Direction: Donald Trump wins the 2016 election, and what decides it is Hillary Clinton's email controversy. The Union Square tarot reading (August 2016) points to the challenger prevailing, with the decisive variable being the damage from Clinton's emails/Foundation controversies breaking late against her — the election turns on that scandal line rather than on policy or turnout mechanics (day-coordinate: 8 November 2016).",
"basis": "Card carries no tradition/system field; decided from the card's genre: a tarot reading reported in news media. Card note: no card spread is reproduced on the input card — input limitation recorded as残损 on the instrument face: no Waite card-by-card reading can be performed, so the verdict rests on the card's framing facts alone and confidence is cut accordingly. Card facts: Clinton leads August polls; the reader is consulted on who wins and what decides it; the email controversy and Foundation are already public — the question's second limb ('what will decide it') directs attention to the scandal line the card itself supplies. Faces: winner decided; decider decided (email controversy); spread face — no data, not reported. [Section-8 workload audit] Work lines: scandal-decider line (acting on: outcome via late break;助成 Trump; strongest among card-supplied lines); polling-lead line (助成 Clinton, outweighed as it predates the decider's effect). Main line认定: decider line. Band: outright win attributed to the email issue; no margin asserted.",
"confidence": 0.48}

B19 = ["MP-017","MP-018","MP-019","OC-001","OC-002","OC-003","OC-004","OC-005","OC-006","OC-007",
"OC-008","OC-009","OC-010","OC-011","OC-012","OC-013","OC-014","OC-015","OC-016","OC-017"]
B20 = ["OC-018","OC-019","OC-020","OC-021","OC-022","OC-023","OC-024","OC-025","OC-026","OC-027",
"OC-028","OC-029","OC-030","WP-001","WP-002","WP-003","WP-004","WP-005","WP-006","WP-007"]

assert set(P.keys()) == set(B19 + B20), (set(B19+B20) ^ set(P.keys()))

written = []
for cid in B19 + B20:
    _basis = P[cid]["basis"]
    _head = "【第八节功量核】"
    if "做功线清单" in _basis and _head not in _basis:
        _basis = _basis.replace("做功线清单", _head + "做功线清单", 1)
    rec = {"case_id": cid,
           "prediction_text": P[cid]["prediction_text"],
           "basis": _basis,
           "confidence": P[cid]["confidence"],
           "trigger": dict(TRIG)}
    (OUT / f"{cid}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
    written.append(cid)

# self-verify: re-open each written file exactly by id
for cid in written:
    d = json.loads((OUT / f"{cid}.json").read_text(encoding="utf-8"))
    assert d["case_id"] == cid and d["prediction_text"] and d["basis"]
    assert 0.0 <= d["confidence"] <= 1.0
    assert d["trigger"] == TRIG
print("written:", len(written))
print("ids:", ",".join(written))
