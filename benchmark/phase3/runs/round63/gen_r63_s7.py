# -*- coding: utf-8 -*-
"""R63 S7 blind predictions: B19+B20+B21 (60 cases). Writes predictions/<id>.json with assertions."""
import json, pathlib

ROOT = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round63")
OUT = ROOT / "predictions"
OUT.mkdir(parents=True, exist_ok=True)

def T(cm=False, ru=False, di=False, reason=""):
    return {"changed_main": cm, "reserve_used": ru, "disputed": di, "reason": reason}

P = {}

# ---------------- MP (no tradition field; genre = HK xuanxue/current-affairs forecast, no chart given) ----------------
P["MP-017"] = dict(
 prediction_text="方向：女性出任——下届香港特首将由女性（林郑月娥）出任。应期：2017年3月26日选举委员会投票日见分晓（事件日坐标）。置信：中低（无盘面，仅据题面动向）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——香港玄学界时事受访预测，无卦盘/命盘数据附卡。\nsystems_used：时事占断（事实优先序 (e)：题面已载唯一女性人选林郑月娥由「不参选」改口「重新考虑参选」，为全卡最强动向信号；男性人选曾俊华仅属已辞职备选、无同等转折信号）。\n已载面：主问面=下届特首性别；关系面=两名人选动向；余面题面未载。本题面无文字/数字锚点，转应核不适用。\n残损：无任何盘面（卦/相/命）数据，事件级以上推不出，依 (c)(g) 口径降置信。\n无应期推算路径（非盘面占断），R61-REV1-2/-3 不适用（应期为题面已给事件日）；无具体断项可作粒度核，R61-REV1-4 不适用。",
 confidence=0.55, trigger=T())

P["MP-018"] = dict(
 prediction_text="方向：不能当选（negative）——曾俊华民望虽为候选人中最高，仍将落败，行政长官由获北京支持的林郑月娥当选。应期：2017年3月26日投票日定局。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——《睇相王》面相/命理时事分析，无命盘四柱附卡（仅给出生日期，未给时辰，不足以排八字盘，不臆补）。\nsystems_used：时事占断（事实优先序 (e)：题面明载「传媒普遍指林郑月娥获北京支持、选情占优，曾俊华被视为陪跑」——1194人选举委员会结构下，建制支持为决定面，民望非决定面）。\n已载面：主问面=曾俊华能否当选（断：不能）；关系面=对手获中央支持；应期面=2017年选举。余面题面未载；无文字/数字锚点，转应核不适用。\n残损：无盘面数据，断语只据题面事实链，置信按事实强度给中高。\nR61-REV1-2/-3 不适用（应期为题面事件日）；断项「林郑当选」指代链回题面关系面、触发为题面支持结构，粒度保留，R61-REV1-4 已核。",
 confidence=0.7, trigger=T())

P["MP-019"] = dict(
 prediction_text="方向：林郑月娥当选2017年香港行政长官（曾俊华、胡国兴落败）。应期：2017年3月26日选举委员会投票当日揭晓。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——风水杂志《新玄机》选举预测，仅给三人出生年（生肖），无八字全盘/面相数据附卡。\nsystems_used：时事占断（事实优先序 (e) 为主）：三人中林郑月娥题面载为前政务司司长，行政历练与建制位置最完整；生肖一路为参：2017丁酉年，林郑、胡国兴同为酉年（值年），曾俊华卯年冲酉（卯酉冲），三人皆带年冲值，生肖路无决定性分野，故不以生肖定主断、只作背景。\n已载面：主问面=选举花落谁家（断：林郑月娥）；关系面=三候选人资历；应期面=3月26日投票。余面题面未载；锚点（出生年）转应面已列：酉年值年可读冲犯、亦可读本命得令，两读并陈后以事实面取舍，取事实面。\n残损：无盘面，置信中。\nR61-REV1-2/-3 不适用（应期为题面事件日）；主断指代链回题面候选人面，R61-REV1-4 已核保留。",
 confidence=0.6, trigger=T())

# ---------------- OC bazi (no tradition field; pillars given) ----------------
P["OC-001"] = dict(
 prediction_text="方向：贵显而晚年落拓。戊土身旺，食神生财（申金生壬子水财）格成，一生事业至一方统帅级（格局量级区间：下限—军政要员，上限—封疆督军级，依据：身旺任财、食伤生财成链）；中年壬申、癸酉运财食得地为一生峰值，军政权位与资财俱盛；晚年入甲戌、乙亥运，官杀克身、戌冲辰库，权位尽失、困顿收场，晚景孤贫向。应期：峰值在壬申运段（运档坐标，窗口标注：卡未给起运岁数，流年层无据不报）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《千里命稿》应运篇论造，四柱齐备）。\nsystems_used：八字子平（立春换年等默认；调候先行、格局定体、旺衰定量合参）。四柱甲戌 戊辰 戊申 壬子：戊土得辰戌根、两戊帮身，身旺；财星壬子得申金食神生，食神生财成链，无强印破财。特格扫描：从格未命中（日主有根有帮）、专旺未命中（财食官并见）、寒燥极端未命中——常规格。运断主线：①格局成（食神生财）；②用神财水得申根而有力；③顺食伤生财之势，忌官杀克身破局之运。大运（男、甲阳年顺行，自月柱戊辰）：己巳、庚午、辛未、壬申、癸酉、甲戌、乙亥。峰值运三核对：壬申运 ①财用申中得生、通根（申为壬水长生）满足；②运干壬即用神财透出，满足；③否决三条核查：壬申 ①运干合绊用神之干：未命中（局无丁）；②运支冲克用神之根：未命中（申即财根）；③运干透忌神且通根：未命中（壬为用神）。满足3项，定壬申为峰值，癸酉次峰。转折运甲戌：运支戌冲月令辰（财库/身根）→病字被冲动、官杀甲克身，方向逆，定低谷，双向对决低谷栏证据直指用神根与日主，胜出。关键结局清单：子女—时柱壬子财星临子嗣宫、食伤申在月，子息有而缘分随运起伏；病位—病字为辰戌冲之土与受克之身，病在脾胃/筋骨之属（由病字落处推）；破财之因—晚运官杀克身、冲库，财随权失而耗；高峰运段—壬申运。格局量级区间已先陈（见 prediction 括注），断语落区间内。应期三步（八字）：尺度运/年档；三路—运年触发（壬申癸酉财食到位）、合冲引动（甲戌冲辰为逆应）、值年（水值年参），取运年触发一路定峰值运档，余两路舍：合冲路主逆向低谷不应峰值、值年路无具体年份锚（起运岁数未给）。BZ-YN 标注：运档坐标（窗口）——卡未给出生日期与起运岁数，流年层缺位降格、不报假年份。R61-REV1-2：主坐标为运档非日月点坐标，复推以合冲路核之同指壬申癸酉段为盛、甲戌转逆，二路同段；R61-REV1-4：等级断项「督军级」支撑指针≥2（身旺+财链）保留。",
 confidence=0.6, trigger=T())

P["OC-002"] = dict(
 prediction_text="方向：贵显且富厚，一生顺遂居多。庚金有申禄、己印，乙木财星合身，亥水食神生财——食神生财、财来就我格，仕途以财政立名，贵至部级（财政部长/央行总裁级，格局量级区间：下限—司局级，上限—部级，依据：财星合身、印禄护身而官星不显，贵以财名胜官名）；中年己卯、庚辰运为峰值（财星得地、印禄相扶）；晚年运平顺，善终向。应期：峰值在己卯运段（运档坐标，窗口标注：起运岁数未给）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《千里命稿》应运篇；四柱甲午 乙亥 庚申 己卯，原书取庚申日，异说庚辰未取，basis 按卡主造）。\nsystems_used：八字子平。庚金坐申禄、得己印生，身有根有助；乙庚合财、亥卯半合财局之势，食神亥水生财。特格扫描三类均未命中，常规格。运断主线：①食神生财格成；②用神财木得亥卯根气；③顺食伤生财势，忌比劫夺财与枭印夺食之重运。大运（男、甲阳顺，自乙亥）：丙子、丁丑、戊寅、己卯、庚辰、辛巳、壬午。峰值三核对：己卯运 ①财用卯得地通根满足；②运干己为印（护身之喜，非忌）呼应格局满足；③否决三条：己卯 ①合绊用神干：未命中；②冲克用神根：未命中（卯即财根）；③透忌神通根：未命中。定己卯峰值。关键结局：子女—时柱己卯印财，子息成器向；病位—病字为亥水寒湿（庚金生于亥月、金寒水冷），病在肺肾/寒湿之属；破财因—比劫运（庚辰参半）防同辈分财，量级小；高峰—己卯运。应期三步：尺度运档；三路取运年触发（财星临运得地），合冲路（无大冲破用）、值年路（无年份锚）舍。BZ-YN：运档坐标（窗口，起运岁数未给，流年缺位降格）。R61-REV1-2 复推：合冲路核己卯无冲破、同段，保留；R61-REV1-4 等级断项指针≥2 保留。",
 confidence=0.6, trigger=T())

P["OC-003"] = dict(
 prediction_text="方向：以商立名、名位显赫而官贵有限。庚金生午月三火围克、身弱无根，所幸丙丁火生时柱己土印星、印再生身，杀印相生链成——一生靠印信、声誉与贵人平台立业，商界领袖级（格局量级区间：下限—富商，上限—商界领袖/社会名流级，依据：杀印链通而印无根、身无禄，贵在名不在官）；早年火土克泄交加较艰，中晚年行辛丑、庚子等金水运身得帮扶、食伤生财，为声名与事业峰值；晚景退而名存。应期：峰值在庚子运段（运档坐标，窗口标注）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《千里命稿》应运篇，四柱丁卯 丙午 庚午 己卯）。\nsystems_used：八字子平。庚金午月死地、丙丁午火官杀成势，身弱；己土印星得火生而生金，杀印相生为救应主线；卯木财星生杀为病助。特格扫描：从杀未命中（有印化杀生身之路、从格判据②不具）、燥极：火旺而有己土泄火生金、未至三条，不作极端格——常规杀印格。运断主线：①杀印格成而印弱；②用神印土有源（火）无根（不透根于支藏本气弱）；③顺杀印链，忌财星坏印之运。大运（男、丁阴年逆，自丙午）：乙巳、甲辰、癸卯、壬寅、辛丑、庚子、己亥。峰值三核对：庚子运 ①用神印土于子无根——不满足；②运干庚比肩帮身呼应「身弱得帮」满足；③否决：庚子 ①合绊用神干：未命中；②冲克用神根：子冲午（冲杀非印根）未命中于印；③透忌神通根：未命中。满足2项（②③）为全程最高，定庚子峰值（辛丑次之：丑印得地）。关键结局：子女—时己印临子嗣宫，子息得力向；病位—病字火炎克金，病在肺/心血之属；破财因—财星卯木在癸卯壬寅运生杀坏印，防因财惹压；高峰—庚子运。应期三步取运年触发路；BZ-YN 运档坐标（窗口）。R61-REV1-2 复推以帮身路核同段保留；R61-REV1-4 已核。",
 confidence=0.58, trigger=T())

P["OC-004"] = dict(
 prediction_text="方向：清贵仕途，位至公使级而非权要。乙木得卯月令、癸丙印伤并透，身旺有文名；惜全局无金，官星不现，仕进只能以才学、资历与印信进身——外交文职清贵（格局量级区间：下限—参赞级，上限—公使/次长级，依据：印伤成象而官星缺位，等级上限受官缺位压制，此为写明依据的定格非无据降格）；中年庚子运官印两见（庚官透、子印得地）为峰值，主任使升阶；晚年戊戌、丁酉运财官参半，平退安老。应期：峰值在庚子运段（运档坐标，窗口标注）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《千里命稿》应运篇，四柱丁丑 癸卯 乙巳 丙子）。\nsystems_used：八字子平。乙木卯月当令、癸水印透、丙火伤官透，身旺；丑土财为用之实，官星全缺为格局上限之据。特格三类未命中。运断主线：①印伤格成、官缺；②用神财土丑中得根而弱；③运来官印则清贵得阶，运来财旺则伤官生财转实务。大运（男、丁阴逆，自癸卯）：壬寅、辛丑、庚子、己亥、戊戌、丁酉。峰值三核对：庚子运 ①财用丑不在子——不满足；②运干庚（官）+运支子（印）补格局所缺之官印，呼应主线满足；③否决：庚子 ①合绊用神干未命中；②子冲无午可冲、未克财根丑未命中；③透忌神通根未命中（庚为所缺之官非忌）。满足2项定峰值。关键结局：子女—时丙子伤官印并，子息文名向；病位—病字子卯刑、巳子水火交，病在肝肾/目之属；破财因—身旺无比劫重运，破耗小，主因俸禄清减；高峰—庚子运。应期三步取运年触发；BZ-YN 运档（窗口）。R61-REV1-2/-4 已核（复推合冲路：庚子无冲破用神，同段保留）。",
 confidence=0.57, trigger=T())

P["OC-005"] = dict(
 prediction_text="方向：贵显于法学/司法一途。乙木卯月当令、亥印未财，身旺；丁火食神透月泄秀生财，食神生财而身旺任之——以学问才名进身，位至法院院长级（格局量级区间：下限—法学教授/法官级，上限—最高法院院长级，依据：食神得令透干、财印两全而官星藏亥不显，贵以专业声望为峰）；中年甲子、癸亥运印星得地，学术与司法声望为一生峰值；晚年辛酉、庚申运官杀得地，仍居职衔而渐退。应期：峰值在甲子运段（运档坐标，窗口标注）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《千里命稿》应运篇，四柱己亥 丁卯 乙未 己卯）。\nsystems_used：八字子平。乙木旺，丁食神透，己财两透，未为财库，卯未半合助身。特格三类未命中。运断主线：①食神生财格成；②用神食神丁火得卯木生、坐月透干有力；③顺食伤生财，印运助名。大运（男、己阴逆，自丁卯）：丙寅、乙丑、甲子、癸亥、壬戌、辛酉、庚申。峰值三核对：甲子运 ①食神用丁于子无地——不满足；②运支子印得地、运干甲劫帮身，印助食神之源（木生火）呼应满足；③否决：甲子 ①合绊用神干未命中；②冲克用神根（丁根在卯/未，子不冲）未命中；③透忌通根未命中。满足2项，与癸亥同级，以先到甲子为峰值（同分并列从先，癸亥称次峰）。关键结局：子女—时己卯财临子嗣宫，子息富厚向；病位—病字木旺火泄，病在肝目/心神之属；破财因—比劫乙丑运防分财，小量级；高峰—甲子运。应期三步取运年触发；BZ-YN 运档（窗口）。R61-REV1-2 复推：值年路无锚，合冲路无破用，同段保留；R61-REV1-4 已核。",
 confidence=0.57, trigger=T())

P["OC-006"] = dict(
 prediction_text="方向：后势不振、难复旧观（negative）。戊土申月泄气，申酉金食伤成势生癸水财，本是大商之局；但当前（约1935年）所行乙卯运，乙木官合庚、卯酉冲伤官——官杀克弱身、又冲断食伤生财之源，企业危机非短期可解；再行甲寅运七杀得禄、寅午半合火印虽有化杀之机，然杀势已成、元气已伤，只能守成收缩，家业渐衰，终局不振。应期：低谷在乙卯运段、延续至甲寅运前段（运档坐标，窗口标注：起运岁数未给，运界年份为约数）。置信：中。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《千里命稿》应运篇，四柱癸酉 庚申 戊午 甲寅；问1935年受挫后走势）。\nsystems_used：八字子平。戊土得午印坐根，申酉食伤旺生财，甲杀透时得寅根——原局成败：食伤生财成链为成，杀重（甲寅）身轻（土休）为病，午火印为药。特格三类未命中。运断主线：①食伤生财格；②用神财水得金源；③病在官杀克身无印运通关则挫。大运（男、癸阴逆，自庚申）：己未、戊午、丁巳、丙辰、乙卯、甲寅、癸丑。转折运乙卯双向对决：高峰栏—乙官透可名位进，证据单薄；低谷栏—乙木官星克戊身（直指病字官杀）、卯冲酉金伤官（直指用神之源食伤），干支两路俱全且直指病用，低谷栏胜出，定乙卯为低谷。甲寅运：寅午合火印化杀为顺的一证、甲杀得禄克身为逆的一证，参半从用神定：食伤源已被冲损、财源不继，定守成低平。关键结局：子女—时甲寅杀临子嗣宫，子息承压向；病位—病字官杀克土，病在脾胃/肝胆之属；破财因—乙卯运冲伤官断财源+官杀压身，企业系统性收缩（因已落具体字）；高峰运段—在已过之丙辰、丁巳运（印得地化杀生身、食伤未冲），非未来运。应期三步：尺度运档（问往后走势）；三路取合冲引动路（卯冲酉为坐标锚），运年触发路主已过之峰不取、值年路无锚舍。BZ-YN：运档坐标（窗口）。R61-REV1-2 复推：逢值路核乙卯同运同段，二路同段保留；R61-REV1-4：低谷断项指针≥2（冲+克）保留原粒度。",
 confidence=0.55, trigger=T())

P["OC-007"] = dict(
 prediction_text="方向：依势而行、无自立之基，寿数不永。甲木生申月，两申冲寅、庚杀当头，全局无水印——日主无根无生扶、官杀成势，从杀格成立：一生才情依附父势权门，性情放浪不羁（从杀之主多随势浮沉），文名大于实业；行运以顺杀为吉，乙酉、丙戌财杀运尚可周旋；一入丁亥运，丁火伤官逆杀、亥水印星扶身破从，两逆并至为寿限低谷，寿止四十余岁。应期：低谷在丁亥运段（运档坐标，窗口标注）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《千里命稿》应运篇，四柱庚寅 甲申 甲申 甲戌；1931年命主新逝后持年庚来验）。注：命主为袁寒云（袁克文），与袁世凯本人有别，依卡面自决对象。\nsystems_used：八字子平。特格扫描—从杀格四判据：①日主无根（寅根被两申冲、无水木之根续）具；②无印比成势生扶（无水、比肩甲坐绝虚浮）具；③官杀成势（庚透、两申、戌中辛）具；④无旺食伤逆杀（戌中丁微）具——从杀格锁定，喜忌以顺杀为准（格局定性双向对决：正格身弱读法须印比救应而全局无印，正格读法依据不成立，从杀读法四据俱全，取从杀并锁定）。运断主线：顺财杀之势，忌印比扶身与食伤逆杀。大运（男、庚阳顺，自甲申）：乙酉、丙戌、丁亥、戊子、己丑。转折运丁亥双向对决：低谷栏—丁伤官透逆杀（直指所从之势）、亥印扶身破从+亥冲？（亥与申害、与寅合木扶身）两路直指格局根本，胜出；高峰栏无据。定丁亥为寿限低谷。关键结局：子女—时甲戌比财，子息平常；病位—病字金旺木绝、申寅冲，病在肝胆筋骨/肺之属；破财因—从格忌比劫，乙酉运后财随势散；高峰—丙戌运（财生杀、顺势得意之段）。应期三步取合冲引动（丁亥逆势）；BZ-YN 运档（窗口）。R61-REV1-2 复推：运年触发路同指丁亥段逆，保留；R61-REV1-4 已核。",
 confidence=0.6, trigger=T())

P["OC-008"] = dict(
 prediction_text="方向：权位可观而进退劳神。乙木酉月杀旺，幸坐未、时归卯禄，日主有根；子水印星化杀，戊己财星生杀——杀重身轻有根有印之局，军政可至省主席级（格局量级区间：下限—厅局级，上限—省主席级，依据：杀临月令旺、身有禄根、印星在年距远化力打折）；中年甲子运印得地化杀生身为峰值，权位最进；晚年丙寅、丁卯运食伤帮身泄秀，退居安老向。应期：峰值在甲子运段（运档坐标，窗口标注）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《千里命稿》应运篇，四柱戊子 辛酉 乙未 己卯；原书取己卯时，异说丙子时斥为传闻未取，按卡主造）。\nsystems_used：八字子平。乙木得卯禄、子印，身弱有根；辛杀当令、财生杀为病，子印为药。特格三类未命中。运断主线：①杀格有印救、破中有成；②用神印水子支得地而单薄；③印运为顺、财杀运为逆。大运（男、戊阳顺，自辛酉）：壬戌、癸亥、甲子、乙丑、丙寅、丁卯。峰值三核对：甲子运 ①印用子得地满足；②运干甲劫帮身呼应满足；③否决：甲子 ①合绊用神干未命中；②子冲无午、未克印根未命中；③透忌通根未命中（甲非忌）。满足3项定峰值。关键结局：子女—时己卯财禄临子嗣宫，子息得力；病位—病字金旺克木，病在肝胆/筋骨之属；破财因—财星生杀之运（戊己本局+财运段）因权位开销与同僚牵连耗财；高峰—甲子运。应期三步取运年触发；BZ-YN 运档（窗口）。R61-REV1-2 复推合冲路：子卯刑为小疵不改段，保留；R61-REV1-4 已核。",
 confidence=0.58, trigger=T())

P["OC-009"] = dict(
 prediction_text="方向：无据不报——本卡未给四柱干支（仅注「四柱以原书为准，转录本个别字待校」），无盘可排，格局、用神、大运、应期一概无据，不作任何具体断语。仅登记题面已载层级：命主为顶尖外交官、已历任驻外使节与内阁职务（此为题面事实、非占断）。置信：极低。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《千里命稿》应运篇下论造）。\nsystems_used：八字子平（拟用而无盘）。\n输入残损（照实注明）：subject.birth 仅有说明文字、无 pillars 字段，四柱干支全缺；按方法纪律「没排盘不说盘」，不以命主公开生平反推四柱、不臆补。已载面表：主问面（财富/仕途/婚姻行运）—有面无据不报（无四柱、无大运，盘面无可指认判断路径）；关系面（婚姻）—有面无据不报；余面题面未载。本题面无锚点，转应核不适用。\n断项过闸：全部具体子断因指代链与盘面触发俱无，悉数删去，只保留「无据不报」明言。应期：无应期、R61-REV1-2/-3 不适用；无具体断项、R61-REV1-4 不适用。置信按残损降至0.15。",
 confidence=0.15, trigger=T())

P["OC-010"] = dict(
 prediction_text="方向：名位至尊而实权虚悬、一生随势浮沉。壬水生寅月，三午两丙财星成局、庚印虚浮坐绝，日主无根无助——从财格成立：少时承虚名极位，中段行壬辰、癸巳运比劫印星逆从，失位迁徙、动荡最甚；中晚年甲午、乙未运食伤生财顺势，境遇渐安、退居善终向；寿数可至六十岁上下。应期：动荡低谷在壬辰、癸巳运段，安定期在乙未运段（运档坐标，窗口标注）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《千里命稿》应运篇下，四柱丙午 庚寅 壬午 丙午；原书未附大运表，大运按默认规则自排并注明）。\nsystems_used：八字子平。特格扫描—从财格四判据：①壬水无根（无亥子申辰水根）具；②印庚坐寅绝虚浮、无比劫帮身具；③财成势（三午、两丙、寅午半合火局）具；④无比劫逆势具——从财格锁定（双向对决：正格读法身弱无救、依据弱于从财四据，取从财）。运断主线：顺财食之势，忌印比逆从。大运（男、丙阳顺，自庚寅）：辛卯、壬辰、癸巳、甲午、乙未、丙申、丁酉。转折运壬辰双向对决：低谷栏—壬比肩扶身逆从（直指从格根本）、辰为水库引身自立逆势，胜出；癸巳运癸劫+巳财参半、从逆定低平。关键结局：子女—时丙午财临子嗣宫，从财之命子息缘随势；病位—病字火炎水绝，病在心肾/眼目之属；破财因—逆从之运（壬辰癸巳）财随位失而散；高峰—乙未运（食神生财、顺势安居段，非权位峰而为际遇峰，已注明口径）。应期三步取合冲引动；BZ-YN 运档（窗口）。R61-REV1-2 复推运年触发同段保留；R61-REV1-4 已核。",
 confidence=0.55, trigger=T())

P["OC-011"] = dict(
 prediction_text="方向：才名早著而寿数不永、结局悲剧向（negative）。己土巳月印旺身强，辛金食神泄秀主演艺之才；然两亥财星冲巳、乙木七杀透时无根，情缘与名分纠缠为病——青年戊寅运，寅木杀得根、寅巳相刑、寅亥合财，杀攻身而刑印，情事与声名之压并至，为寿限低谷，二十五岁前后有自伤/横夭之厄，一生结局以悲剧收场。应期：低谷在戊寅运段、尤以寅木流年引动之年为甚（运档坐标，窗口标注：流年层据运内引动给方向、具体年份置信降格）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《千里命稿》应运篇下，四柱庚戌 辛巳 己亥 乙亥；1935年命主新逝后友人嘱推，问性情与一生结局）。\nsystems_used：八字子平。己土得巳印、戌根身旺；辛食神透月泄秀；亥财两见冲巳印；乙杀透时坐亥（亥中甲微根）。特格三类未命中。运断主线：①食神泄秀格成于才名；②用神食神辛金得巳中庚根而弱；③病在杀透无制、财冲印，运至杀根之地则病发。大运（女、庚阳年逆，自辛巳）：庚辰、己卯、戊寅、丁丑、丙子。转折运戊寅双向对决：低谷栏—寅为乙杀之根（杀得根克身，直指病字）、寅巳刑印（伤救应）、寅亥合财动情缘，三路成链胜出；高峰栏仅戊食神制杀一证孤悬，不胜。定戊寅低谷。关键结局：子女—时乙亥杀财，子息缘薄向；病位—病字水火冲刑，病在心神/肾水之属（情志之病由病字落处推）；破财因—财冲印因情耗财；高峰—庚辰运（食神得辰根、少年成名段）。应期三步：尺度运档为主、流年寅年为运内引动（BZ-YN-2.4 格局面④成立故标流年层方向，年份数字不硬报）；BZ-YN 运档（定值）+流年方向（降格）。R61-REV1-2 复推：合冲路（寅亥合、寅巳刑）与触发路同指戊寅段，二路同段保留；R61-REV1-4：寿限断项指针≥2（杀根+刑印）保留，量级表述为「之厄」倾向级。",
 confidence=0.6, trigger=T())

P["OC-012"] = dict(
 prediction_text="方向：少年成名、中年沉沦、晚年稍安。丁火辰月，戊土伤官两透泄火生申金财，伤官生财格而身弱无印——早运己巳、庚午火来帮身，伤官得用，十五六岁泳坛成名为一生峰值；入辛未运土重泄身渐衰；壬申、癸酉运金水财杀交加，弱火受克，婚姻多变、际遇沉沦为低谷；晚行甲戌运甲印透、戌为火库，稍得安顿。应期：峰值在庚午运（约十五至二十五岁段）、低谷在壬申癸酉运段（运档坐标；大运表由卡面给出，五岁起运，坐标为定值级）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《千里命稿》评断篇，四柱己未 戊辰 丁未 戊申；卡面附大运：五岁起运己巳、庚午、辛未、壬申、癸酉、甲戌，照卡采用）。\nsystems_used：八字子平。丁火休囚、土重泄气、无木印，全局以伤官生财为势，身弱为病、无药（印缺）——特格从儿扫描：日主无根？丁在未辰中无火根（未中丁为余气，不作禄刃根）、无印比生扶、食伤成势、生财成链、无印克食伤——四据近全，然未中藏丁一气未绝，从儿作「假从/倾向」登记，格局定性双向对决后取「伤官生财身弱」正格为主、从儿为参（锁定正格：因余气根在，判据①严格不具），运断以正格行（喜火帮身、印运）。运断主线：①伤官生财格；②用神伤官戊土旺而身不受；③火运顺（帮身任伤）、金水运逆。大运照卡。峰值三核对：庚午运 ①伤官用戊于午为火生土得气满足；②运支午为丁火帝旺帮身、运干庚财呼应生财链满足；③否决：庚午 ①合绊用神干未命中；②午冲无子、未克伤官根未命中；③透忌通根：庚为财（身弱财亦忌半）——庚坐午无根，不构成「透忌且通根」，未命中。满足3项定庚午峰值。转折运壬申双向对决：低谷栏—壬官合丁（合绊日主）、申金财旺生杀克弱身，直指日主与病字，胜出。关键结局：子女—时戊申伤官财，子息缘平；婚姻—身弱财杀旺，夫星（官杀水）运至而身不受，婚姻多变（由壬癸运作用表推）；病位—病字土重火弱，病在脾胃/心血之属；破财因—财旺身弱不任财，中年因财与婚变耗损；高峰—庚午运。应期三步取运年触发；BZ-YN：运档坐标（定值，大运表卡面已给）。R61-REV1-2 复推合冲路（壬合丁）同指低谷段保留；R61-REV1-4 已核。",
 confidence=0.62, trigger=T())

P["OC-013"] = dict(
 prediction_text="方向：以艺成名、一生名望为宗。辛金丑月得酉禄，身旺；丁火七杀透月、甲木财星两透生杀，杀势有源——身旺任杀、以技艺承压成名之格，梨园大家级（格局量级区间：下限—名角，上限—行业宗师级，依据：禄旺任杀、财杀有源，贵在技艺声名不在官位）；中年庚辰、辛巳运帮身任杀、名盛为峰值；晚年乙酉运归禄，退而名存、寿数较高向。应期：峰值在庚辰运段（运档坐标，窗口标注：卡仅注八岁起运、无大运表，序列自排）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《千里命稿》评断篇，四柱甲午 丁丑 辛酉 甲午；八岁起运）。\nsystems_used：八字子平。辛金坐酉禄、丑印，身旺；丁杀、甲财。特格：专旺未命中（杀财并透不纯）、余皆未命中。运断主线：①财生杀、身任杀格成；②用神杀丁得甲生而午根在年时；③帮身运顺、食伤制杀运平。大运（男、甲阳顺，自丁丑）：戊寅、己卯、庚辰、辛巳、壬午、癸未、甲申、乙酉。峰值三核对：庚辰运 ①杀用丁于辰无根不满足；②运干庚劫帮身任杀、运支辰印生身呼应满足；③否决：庚辰 ①合绊用神干未命中；②辰冲无戌未命中；③透忌通根未命中。满足2项为最高定峰值（辛巳次峰：比肩+杀得地）。关键结局：子女—时甲午财杀，子息承名向；病位—病字火金交战，病在肺/喉之属（梨园人以金火推喉肺，由病字落处）；破财因—财星两透防因财养杀之耗，量级中；高峰—庚辰运。应期三步取运年触发；BZ-YN 运档（窗口）。R61-REV1-2 复推值年路无锚、合冲路无破，同段保留；R61-REV1-4 已核。",
 confidence=0.57, trigger=T())

P["OC-014"] = dict(
 prediction_text="方向：仕途以财税见长、清稳有成。壬水卯月，寅卯伤官成势，庚辛印星两透制伤护身——伤官配印格：以文才、算学进身财政，位至财政厅长级（格局量级区间：下限—科局级，上限—厅长级，依据：伤官配印成格而印根浅、官星藏辰丑不透）；中年甲申运申金印得地、伤官得制，为峰值；晚年丙戌运财官并至而戌冲辰印根，退平。应期：峰值在甲申运段（运档坐标，窗口标注）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《千里命稿》应运篇下，四柱庚辰 己卯 壬寅 辛丑）。\nsystems_used：八字子平。壬水休、木泄、土克，有庚辛两印为救，伤官配印。特格三类未命中。运断主线：①伤官配印成格；②用神印金庚辛透而根在辰丑藏辛庚弱；③印得地之运顺、财破印之运逆。大运（男、庚阳顺，自己卯）：庚辰、辛巳、壬午、癸未、甲申、乙酉、丙戌。峰值三核对：甲申运 ①印用申得地满足；②运干甲伤官透而得申印制——呼应「配印」满足；③否决：甲申 ①合绊用神干未命中；②申冲寅（冲伤官非印根）未命中；③透忌通根：甲为伤官（本格之忌半）坐申绝地不通根，未命中。满足3项定峰值。关键结局：子女—时辛丑印官，子息文名向；病位—病字木旺水弱，病在肝肾之属；破财因—丙戌运财破印因财失位之耗；高峰—甲申运。应期三步取运年触发；BZ-YN 运档（窗口）。R61-REV1-2/-4 已核保留。",
 confidence=0.55, trigger=T())

P["OC-015"] = dict(
 prediction_text="方向：位至至尊而权受节制、晚年退养。甲木巳月休，辛金官星透月、子水印星在时，官印相生之链虽弱（辛金巳月受克、甲木无强根）却成象——君主之命以位尊为体、以实权有限为用；早中年庚辰运庚金七杀透、辰土培印，为在位权柄最盛之段；晚年丙子、乙亥运印星得地，主退养安老，寿数七十上下。应期：峰值在庚辰运段（运档坐标，窗口标注：四柱据西报传略译生庚演造，盘面可信度注记降格）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《千里命稿》应运篇下，四柱乙丑 辛巳 甲辰 甲子；卡注「韦氏据西报传略译生庚演造」——出生数据为转译推得，盘面置信先降一档并注明）。\nsystems_used：八字子平。甲木弱、辛官、子印、辰湿土藏乙微根。特格三类未命中。运断主线：①官印相生格成而官弱；②用神官辛无根受巳克；③官杀得地之运权盛、印旺之运退养。大运（男、乙阴年逆行，自辛巳）：庚辰、己卯、戊寅、丁丑、丙子、乙亥、甲戌。峰值三核对：庚辰运 ①官用辛于辰为养地半满足；②运干庚杀透、运支辰为印星之根（辰藏乙癸、湿土生金）呼应官印链满足；③否决：庚辰 ①合绊用神干未命中；②辰冲无戌未命中；③透忌通根未命中（庚在此为官杀之助、非本格忌神）。满足2项定庚辰为峰值。关键结局：子女—时甲子比印，子息承绪向；病位—病字火旺木弱金受克，病在肝肺之属；破财因—君主命以国事耗损论不深断；高峰—庚辰运。应期三步取运年触发；BZ-YN 运档（窗口）。R61-REV1-2 复推：合冲路核庚辰无冲破官印，同段保留；R61-REV1-4：等级断项「至尊位」据题面已载事实（命主为英国君主）非占断拔高，保留。",
 confidence=0.5, trigger=T())

P["OC-016"] = dict(
 prediction_text="方向：以命学立身、名利中平而寿安。庚金卯月囚，子水伤官、亥水食神泄秀生卯木财，辰土印星为根——身弱食伤旺之局，正是以术数、文章技艺谋生的命式（格局量级：以术业名家为上限、不入官贵，依据：官星全缺、印弱财食当道）；中年丙申运申金禄地身转旺、任财任名，为一生峰值；晚年戊戌印运安养，丁酉运劫财防同业相争，整体晚景安适。应期：峰值在丙申运段（运档坐标，窗口标注）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《千里命稿》应运篇自论，四柱辛亥 辛卯 庚子 庚辰，命师本人自造）。\nsystems_used：八字子平。庚金弱、无禄、辰印；食伤两透支、财卯当令。官星全缺为仕途上限之据（写明依据的定格）。特格三类未命中。运断主线：①食伤生财格；②用神食伤水得亥子势而身弱须印比运扶；③禄印运顺、财旺身不受运平。大运（男、辛阴年逆，自辛卯）：庚寅、己丑、戊子、丁亥、丙申、乙未、甲午。峰值三核对：丙申运 ①食伤用水于申为长生得地满足；②运支申为庚金禄地（扶身任用）呼应满足；③否决：丙申 ①合绊用神干未命中；②申冲无寅（局寅不在）未命中；③透忌通根：丙为七杀（身弱之忌）坐申有根——命中(iii)？丙火在申为病地、庚金克火，杀不得势，严格按条文「运干透忌神且得运支通根」：丙在申不通火根（申藏壬庚戊），未命中。满足3项定丙申峰值。关键结局：子女—时庚辰比印，子息平；病位—病字金弱水旺，病在肺肾之属；破财因—丁酉运劫财同业分利；高峰—丙申运。应期三步取运年触发；BZ-YN 运档（窗口）。R61-REV1-2/-4 已核保留。",
 confidence=0.57, trigger=T())

P["OC-017"] = dict(
 prediction_text="方向：一生大富。丁火酉月，财星金临月令而旺，己土食神生财，壬水官星合身，甲木印星透时为救——财格成而身弱有印救应，富格量级至巨富（格局量级区间：下限—富商，上限—巨富级，依据：《子平真诠评注》用神成败救应章引例格：财旺、食生、印救三件俱全）；早年庚戌、辛亥运财官压身、担财艰苦；中年甲寅、乙卯运印星得地扶身任财，为发迹峰值；晚年丙辰运火印并至，守成安富。应期：峰值在甲寅运段（运档坐标，窗口标注）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《子平真诠评注》论用神成败救应章引例，四柱壬戌 己酉 丁丑 甲辰；命主南浔丝商）。\nsystems_used：八字子平（真诠格局法为主）：月令酉金财格，食神己土生财为成，丁火弱赖甲印生扶为救应——成中有救。特格扫描：从财未命中（甲印透时、戌中丁根，判据①②不具），余未命中。运断主线：①财格成；②用神财金当令旺；③印运扶身则任财发富、财官重运身不受则艰。大运（男、壬阳顺，自己酉）：庚戌、辛亥、壬子、癸丑、甲寅、乙卯、丙辰。峰值三核对：甲寅运 ①财用金于寅绝地不满足；②运干甲印透、运支寅印禄地扶身任财，呼应主线满足；③否决：甲寅 ①合绊用神干：甲不合财干未命中；②寅冲无申、未克财根酉未命中；③透忌通根未命中（甲为救应非忌）。满足2项定峰值（乙卯次之）。关键结局：子女—时甲辰印临子嗣宫，子息成器；病位—病字火弱金旺，病在肺/心之属；破财因—早运财官压身之耗、晚运守成无大破；高峰—甲寅运。应期三步取运年触发；BZ-YN 运档（窗口）。R61-REV1-2 复推合冲路无破用同段保留；R61-REV1-4 已核。",
 confidence=0.6, trigger=T())

P["OC-018"] = dict(
 prediction_text="方向：中年鼎盛、晚年有横祸之危（negative for晚年）。庚金子月，食神子水当令，寅卯财星、丙火杀星并透——以文（食伤）生财、以财成名之报业格；中年壬申运申金禄地身旺任事，报业全盛为一生峰值；后行庚午运，午火七杀得地攻弱金、庚金比肩无根，杀攻身而无印化，晚年防横祸伤身、寿限受威胁，终局以险收。应期：峰值在壬申运段、危厄在庚午运段（运档坐标，窗口标注）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《子平真诠评注》用神成败救应章引例，四柱己卯 丙子 庚寅 辛巳；命主报业巨头，问地位与晚年行运）。\nsystems_used：八字子平。庚金休、坐绝、巳中微根；食伤旺、财杀并透，印全缺为病（杀无化）。特格三类未命中。运断主线：①食伤生财格成于名；②用神食神子水当令；③病在杀透无印，杀得地之运为厄。大运（男、己阴逆，自丙子）：乙亥、甲戌、癸酉、壬申、辛未、庚午、己巳。峰值三核对：壬申运 ①食伤用水申为长生满足；②运支申为庚禄、运干壬食神呼应满足；③否决：壬申 ①合绊用神干未命中；②申冲寅（冲财非用根）未命中；③透忌通根未命中。满足3项定峰值。转折运庚午双向对决：低谷栏—午火杀得地克庚身（直指病字）、午冲子水用神（直指用神），两路俱全胜出，定庚午大凶低谷。关键结局：子女—时辛巳劫杀，子息承压；病位/横祸—病字杀火克金，祸在血光/金器之属（由病字五行推，不另造细节）；破财因—杀运事业被夺之耗；高峰—壬申运。应期三步取合冲引动（午冲子）；BZ-YN 运档（窗口）。R61-REV1-2 复推运年触发同指两段保留；R61-REV1-4：横祸断项指针≥2（杀得地+冲用）保留为「之危」倾向级。",
 confidence=0.58, trigger=T())

P["OC-019"] = dict(
 prediction_text="方向：贵显于学界政界而中年有险。壬水辰月，坐下申金印源、癸水劫助，身有根有助；丙火财透、卯木伤官泄秀——印旺身强、伤官生财之局，位至研究院总干事级（格局量级区间：下限—局所级，上限—院署级，依据：印身两旺而官星辰土不透，贵以学术行政为峰）；险年在壬子运：子水羊刃帮身过旺、子卯相刑、子辰半合引动，中年防横祸与官非之厄；庚戌运戌冲辰土官库，职位动荡次之。应期：峰值在癸丑、壬子前段，险厄集中壬子运段（运档坐标，窗口标注；两书四柱全异，本断以卡面指定徐乐吾书为准，置信降格）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《子平真诠评注》引例，四柱癸巳 丙辰 壬申 癸卯）。卡注：韦千里《千里命稿》另载全异四柱，本例以徐乐吾书为准——basis 照卡取舍并因版本分歧降置信（冲突并列登记口径：取舍已写明）。\nsystems_used：八字子平。壬水得申源、癸助；丙财、卯伤、辰官藏。特格三类未命中。运断主线：①印身格成；②用神印申得地；③刃旺刑伤之运为险、官库冲动之运为荡。大运（男、癸阴逆，自丙辰）：乙卯、甲寅、癸丑、壬子、辛亥、庚戌、己酉。转折运壬子双向对决：险栏—壬比+子刃扶身过旺（逆「中和」主线）、子卯刑伤官、子冲无午而刑在，两证成链；顺栏—印源得助一证。险栏直指刑伤与过旺，定壬子为险运（方向逆）。关键结局：子女—时癸卯劫伤，子息文名向；病位—病字水旺刑木，病在肾/肝之属，横祸之虞由刃刑推（倾向级）；破财因—刃旺防因同侪与官非耗财；高峰—癸丑运（劫印+官库得地、学术行政并进段）。应期三步取合冲引动；BZ-YN 运档（窗口）。R61-REV1-2/-4 已核（版本分歧已降置信）。",
 confidence=0.52, trigger=T())

P["OC-020"] = dict(
 prediction_text="方向：贵至极点而寿数受限。癸水丑月，两丑官星重叠、丁财乙食并见，全局无金印——官重身轻无化之局：名位可至政府主席级（格局量级区间：下限—省部级，上限—政府主席级，依据：官星重而当令、食神生财辅官，然身弱无印，贵位与寿数同受压制，此上限/下限均有盘面依据）；中年壬申运申金印得地、官印相生，为一生峰值；五十岁前后入辛未运，未冲丑官库、丁火财动，寿限关口在此运。应期：峰值在壬申运段、寿关在辛未运段（运档坐标，窗口标注）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《子平真诠评注》引例，四柱己卯 丁丑 癸丑 乙卯；命主国民政府主席级政要，问贵显与险年）。\nsystems_used：八字子平。癸水囚、无根无印；丑官两坐、卯食两透生丁财。特格：从官扫描——日主丑中癸有微根、食神两透逆官之气在，从官判据不全，未命中，作正格身弱官重。运断主线：①官格重而身轻；②用神官土当令旺；③印运化官为唯一救路，印运即峰、冲官库运即关。大运（男、己阴逆，自丁丑）：丙子、乙亥、甲戌、癸酉、壬申、辛未。峰值三核对：壬申运 ①官用土于申无地不满足；②运支申印得地化官生身、运干壬劫帮身，呼应救路满足；③否决：壬申 ①合绊用神干未命中；②申与巳无涉、未冲官根丑未命中；③透忌通根未命中。满足2项定峰值。转折运辛未双向对决：低谷栏—未冲丑（冲官库/日主坐支，直指用神与日主）、辛印坐未无根救力薄，胜出，定寿关运。关键结局：子女—时乙卯食神，子息文名；病位—病字土重克水，病在脾胃/肾之属；破财因—官重之命耗于政务交际；高峰—壬申运。应期三步取合冲引动（未冲丑）；BZ-YN 运档（窗口）。R61-REV1-2/-4 已核保留。",
 confidence=0.57, trigger=T())

P["OC-021"] = dict(
 prediction_text="方向：一生武贵、位至一方军阀首领。乙木酉月辛金七杀当令，幸乙坐卯禄有根，丙火伤官透时得午戌火根制杀——伤官制杀格成：以武功、决断立业，权位至督军/巡阅使级（格局量级区间：下限—师旅长级，上限—一方军阀首领级，依据：杀禄两旺、制杀之火有根成势）；中年丙寅运伤官得禄、寅午戌火局制杀成势，为一生峰值；晚年戊辰运财星引杀、辰冲戌，权势渐退。应期：峰值在丙寅运段（运档坐标，窗口标注）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《子平真诠评注》论用神格局高低章引例，四柱戊午 辛酉 乙卯 丙戌；命主旧桂系军阀首领，问格局高低）。\nsystems_used：八字子平。乙木禄根、辛杀当令、丙伤制杀、戊财生杀。特格三类未命中（专旺：杀财并见不纯）。运断主线：①伤官制杀格成；②用神伤官丙火得午戌根；③火运制杀顺、财运生杀逆、金水运参半。大运（男、戊阳顺，自辛酉）：壬戌、癸亥、甲子、乙丑、丙寅、丁卯、戊辰。峰值三核对：丙寅运 ①伤官用丙寅为长生得地满足；②运干丙即用神透出、寅午戌三合火局呼应满足；③否决：丙寅 ①合绊用神干未命中；②寅冲无申未命中；③透忌通根未命中。满足3项定峰值。关键结局：子女—时丙戌伤官，子息承武名向；病位—病字金木交战，病在肝胆/筋骨之属；破财因—戊辰运财生杀耗于军费部属；高峰—丙寅运。应期三步取运年触发；BZ-YN 运档（窗口）。R61-REV1-2 复推合冲路：寅运无冲破用神，同段保留；R61-REV1-4 已核。",
 confidence=0.58, trigger=T())

P["OC-022"] = dict(
 prediction_text="方向：科第无缘、以命学著述立身。乙木酉月，辛杀丁食戊财并见，全局无水——印星全缺为科名之绝：功名试卷以印为凭，无印则虽有食神文才，科第屡试不第（此为写明依据的定格）；一生转以食神生财、著述授徒立业，术数名家级；行运迟至癸巳、壬辰运印星始透得地，著述声名在晚运方成峰值。应期：峰值在壬辰运段（运档坐标；大运丙申起为卡面所给，序列照卡）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——八字（《命理探原》卷七自造自批，四柱辛巳 丁酉 乙巳 戊寅；卡注安命甲午、大运丙申起，照卡采用）。\nsystems_used：八字子平。乙木得寅根、弱；丁食、戊财、辛杀；印（水）全缺——格局定性：食神生财格，科名面以印缺为决定面（类神多面并读：印主文书功名，缺位在此只降权不作「无学」断——命主文才以食神见长，断的是科第之凭缺、非学问缺，此界已分清）。特格三类未命中。运断主线：①食伤生财格；②用神食神丁火得巳午根；③印运迟来为著述之机、财杀运为谋生之劳。大运照卡丙申起（阴年男逆行序）：丙申、乙未、甲午、癸巳、壬辰、辛卯、庚寅。峰值三核对：壬辰运 ①食神用丁于辰无地不满足；②运干壬印透、运支辰为水库印得地，补全局所缺之印、呼应著述主线满足；③否决：壬辰 ①壬合丁（合绊用神食神之干）——命中(i)？按峰值否决条：运干合绊用神之干者伪峰。壬合丁确合食神干——命中，壬辰按伪峰处置、资格取消，峰值顺延：癸巳运核对—①丁于巳得地满足；②运干癸印透呼应满足；③否决：癸巳 ①合绊用神干未命中（癸不合丁）；②巳与局巳伏吟非冲克用根未命中；③透忌通根未命中。满足3项，定癸巳为峰值（壬辰标注伪峰、不参与排序）。关键结局：子女—时戊寅财根，子息务实；病位—病字金火交战水缺，病在肺/心血之属；破财因—财星戊透防以财惹杀之耗；高峰—癸巳运。应期三步取运年触发；BZ-YN 运档（窗口）。R61-REV1-2 复推：值年路核癸巳印食并得地同段保留；R61-REV1-4 已核（含伪峰顺延留痕）。",
 confidence=0.6, trigger=T())

# ---------------- OC meihua ----------------
P["OC-023"] = dict(
 prediction_text="方向：钟下所覆为有足之烹饪器物（鼎属器皿），且不完好——足已折损。火风鼎变雷风恒，四爻发动，鼎九四爻辞「鼎折足，覆公餗」正应其象：覆物为三足/有足之器，中虚可盛物，折足破损在身。具体断项：①物品—鼎属有足器皿（对象）；②状态—折足不完好（状态类别）；③体用—巽木体生离火用，耗泄主物有损耗。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——梅花易数（《梅花易数》卷三·钟覆物占，卡附卦象火风鼎变雷风恒）。\nsystems_used：梅花易数（托名邵雍、明以降通行本，著录存疑照实标注）。起卦数据卡已给卦象：鼎下巽上离；变恒下巽上震——上下卦比对，下卦不变、上卦离变震，动在四爻（离初爻阳变阴）。体用：动爻在上卦，上卦离火为用、下卦巽木为体，体生用（木生火）主耗损；互变：变卦震木与体比和。\n爻辞取象核对 (d)：四爻为九四，鼎九四「鼎折足，覆公餗，其形渥，凶」——辞自带凶与折足事象，断语方向（器损不完好）与辞义一致，未翻转。事实优先序 (e)：所占为席间射覆、对象为器物，断项只落器物不回收到人。应验对象复核 (f)：承受对象=钟下器物，应验对象=同一器物，同一。\n梅花自检表：断项落对象（鼎属器皿）+状态（折足）两项，具体断语≥1条主断（射覆单问以一物为核，不凑三条——按自检表第4项口径：余路取象（互卦艮兑未给全象）不足，注明）。量级守恒：日常射覆小事，只断物类与完损、不放大。\n断项粒度核 R61-REV1-4：「鼎属有足器皿」支撑指针2条（鼎卦象本身象鼎器+九四辞折足）保留原粒度；「折足」指针2条（爻辞+体生用耗损）保留。无应期断语（射覆问物态非问时），R61-REV1-2/-3 不适用。",
 confidence=0.55, trigger=T())

P["OC-024"] = dict(
 prediction_text="方向：葬资有着落（positive）——易者之家无资营葬之困将解：其宅中藏有窖藏金银，掘地（击鼠穿枕之机）得之，足以办妥葬事。具体断项：①物品—地下窖藏金银（对象/物品）；②事件—意外掘得、非借贷非赙赠；③承受对象为易者之家，葬事得办。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——梅花易数序例（《梅花易数》序·击鼠枕窖金一节，邵雍携遗书访易者之家问葬资）。\nsystems_used：梅花易数（托名文本，著录口径同前）。\n输入残损（照实注明）：卡未附卦象/起卦数，无体用可排——断语只据题面已载面与序例体裁：题面载「遗书预言来访秀士可托身后事」「其家正苦于无资营葬」，序节名自带「窖金」面（题面锚点：节名文字）。列面：主问面=葬资何来（断：宅中窖藏掘得）；对象面=金银窖藏（物品）；关系面=易者之家承受。锚点转应面已列：「窖金」直读为地下藏金，转应面（借贷/赙赠）已列并舍——序例体裁主意外自得，取直读，理由为节名锚点与遗书预言面合指。\n断项过闸：掘金断项指代链回题面对象面、触发为节名锚点+预言面，指针仅1类（文字锚点），按 R61-REV1-4 粒度降一档：处所由「宅中某处」降为「其宅内地下」区域表述（已在断语中如此落）。无盘面应期可推：应期无据不报、R61-REV1-2/-3 不适用。置信因无卦盘降格。",
 confidence=0.55, trigger=T())

P["OC-025"] = dict(
 prediction_text="方向：应验（positive）——邵雍预书于椅底之事届期应验：至预书所载年月日，椅子将被坐破，如字而验。具体断项：①物品—其家椅子（对象）；②事件—届期被坐破；③时点—预书所载之日（卡未载具体日期，只断届期必验）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——梅花易数序例（《梅花易数》序·置椅坐破，预言验证类）。\nsystems_used：梅花易数（托名文本，著录口径同前）。\n输入残损（照实注明）：卡未附卦象、未载预书具体年月日与届期情境细节，无体用/爻辞可核——断语只据题面已载面：主问面=预书之事是否应验；对象面=椅子；应期面=预书所载年月日（题面已载有此日期、数值未给）。序例体裁：此节在序中正为「预言必验」之例，体裁面与主问面合指应验。锚点转应面：预书文字直读（椅破）与转应（他物代应）并列，取直读——序例无转应记载面，舍转应理由如上。\n断项粒度核 R61-REV1-4：「椅子被坐破」指针为题面体裁面1类，量级守恒下只断事态本身、不增人物/缘由细节（不臆补何人坐破）。应期主坐标无数值可推（预书日期未给），R61-REV1-2/-3 不适用并注明。置信因无盘降格。",
 confidence=0.55, trigger=T())

# ---------------- OC liuren ----------------
P["OC-026"] = dict(
 prediction_text="方向：功名可得（positive）——两客今年功名有成，其中一人功名更显。三传乙未青龙、己亥螣蛇、癸卯玄武：未为木之墓、青龙乘之主喜庆文书之始，中传亥水螣蛇主虚惊迟滞，末传卯木玄武归于功名之本体（曲直课木势成行、卯为日干乙之禄位方向）——先难后成，榜名在末。应期：月档——功名以科考放榜之期为应，窗口为今年秋试放榜之月，主坐标取卯月/放榜月（类神卯木逢值之月，定值标注）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——大六壬（《大六壬占验指南》第57课，卡附课式涉害/曲直、三传天将、月将与空亡）。\nsystems_used：大六壬（指南系）。盘面：1643年正月初四己亥日辛未时，丑将，甲午旬辰巳空。守第八节：只有课式、三传天将、干支占时与空亡可据，不臆补天盘全图/四课全列/年命（两客年命未给，年命路无据注明）。\n取用（仕宦功名门+考试门）：官鬼/父母文书为类神——三传未、亥、卯皆木土水：乙未（木墓于未、青龙）父母面（未中藏丁己乙、青龙主文书喜庆），末传癸卯木为功名进取之体（卯木旺于春、正月木气始盛）。类神多义并读 LR-QY-1：未青龙—文书/喜庆面有据（入传+乘吉将）；亥螣蛇—迟滞虚惊面有据（入传乘蛇）；卯玄武—末传归体、玄武主暗昧，名位得而带不明之疵，降为次级面。LR-QY-2：类神入传一级据可定主线。\n三传链：未→亥→卯，墓→生→禄，递进向身（日干乙木：亥水生乙、卯木同类助），终局向成。课格：曲直主木势进取、涉害主过程有争难——先难后成与课格合。两段式 (i)：近段涉害螣蛇主阻（已由中传指认触发），远段末传卯木归禄主成，触发为末传支本身。应期（第七节+通则）：先定月档（考试榜期月档）；三路—逢值（卯月）取、逢冲合（酉冲卯为破不取、亥卯合为成期备选舍：合路主近段胶着）、出空填实（三传不空、辰巳空不涉类神，此路无候选已明写）；窗口=今年放榜之月，主坐标=卯木逢值之放榜月。R61-REV1-2 复推：换合处机制复推得亥卯合期，与逢值同指春榜季，粒度保留月档；R61-REV1-4：功名断项指针≥2（末传归禄+青龙文书）保留。",
 confidence=0.6, trigger=T())

P["OC-027"] = dict(
 prediction_text="方向：此行不得意（negative）——奉诏北上难遂其愿：课式无禄、无路，三传癸酉（六合）、戊辰（天阴）、亥（青龙、空亡），末传落空、功名之凭虚悬；行至中途多阻，进京纵至亦无显擢，老母安否一面：母年甲子、年命上神未给，此面无据不报（只断：行期之内家中无急变之据亦不足，不作安断）。身体一面：日干辛金、三传酉金同类而辰土生金，身无大碍、唯行役劳顿。应期：月档——窗口为冬月出行后一至两月，主坐标取末传亥水出空填实之期（亥月已过、取次年亥月过远，改取亥日填实于本旬后首个亥日所属之月内节点，坐标降格为月内亥日，窗口标注）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——大六壬（《大六壬占验指南》第58课，卡附课式无禄/无路、三传、月将丑、甲子旬戌亥空）。\nsystems_used：大六壬。盘面：1642年冬月初五辛未日甲午时。守第八节：无天盘全图、其母年命上神未给（仅知母生甲子年），母安一面按 LR-QY-2.4 明写无据不报，不以缺位反推凶安。\n取用（仕宦门+出行门）：官鬼/禄马为类神——课名「无禄、无路」为课格主向（第三节：无禄主职禄无凭、无路主行无通路）；三传酉（金、六合）、辰（土、天阴）、亥（水、青龙、旬空）：末传青龙乘亥而落空——青龙为迁转之将，吉将落空「吉不中不吉」（第四节总论），迁擢之凭虚悬，一级据定主线为不得意。类神并读：辰土天阴生酉金（父母面：文书诏命已下、行有凭据，此面有据保留——诏命本身真、只是行不得意，两面分判不相吞）。三传链：酉→辰→亥，泄→生→空，势往空里去，终局虚。两段式：近段酉合主启程可成行（触发：初传六合），远段末传空主至而不遂（触发：末传亥空），分段各有触发。应期：先定月档（仕宦迁转月档）；三路—出空填实（亥填实）取、逢值（亥值同支而在空期不用，舍：值而不实）、逢冲（巳冲亥为冲空则实备选，与填实同指亥位之实，作复推）；窗口=出行后两月内，主坐标=亥日填实（月内日坐标，承档位表仕宦月档内取日为节点，标注窗口）。R61-REV1-2 复推：冲空机制（巳日冲亥）与填实异日——按取期优先序落空者先取出空填实，填实占优保留亥日，巳日入舍弃留痕；R61-REV1-4：母安面已按无据删断、未以粒度降档冒充覆盖。",
 confidence=0.62, trigger=T())

P["OC-028"] = dict(
 prediction_text="方向：可得官而位在武/外任一途、非清要之缺（positive with qualification）——三传辛卯玄武、丙戌朱雀、癸巳白虎：初传卯木玄武主暗中运作，中传戌土朱雀主文书考选之凭，末传巳火白虎主武职、刑杀之任；课式重审、斫轮（斫轮主车轮之任、运转之官）——断得官为与车马、兵刑或外任相关之职，进身可成而清贵不足。应期：月档——窗口为入觐考选后数月内，主坐标取末传巳火逢值之月（巳月，定值标注）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——大六壬（《大六壬占验指南》第59课，卡附课式重审/斫轮、三传、寅将、甲申旬午未空）。\nsystems_used：大六壬。盘面：1630年冬月十四己丑日辛未时。守第八节：年命未给，该路无据注明；四课全列未给不臆补。\n取用（仕宦门）：官鬼为官职本体——日干己土，克己者木：初传卯木即官鬼入传且居初（事之始），一级据。太常/青龙迁转将未入传——按 LR-QY-2 缺传只降权：迁擢之「清要」量级降一档，不作无官断（正面据：官鬼入传+朱雀文书入传）。类神并读：卯玄武—官面下带暗昧运作面（入传乘玄武，四据有据，作次级面：得官须经暗中经营）；戌朱雀—文书考选面（朱雀主文书、戌为印库方向）；巳白虎—末传定任所性质（白虎主兵刑道路、巳火为土之印）。课格：斫轮主轮转之任（车马/运转），与末传白虎同指武/外任。两段式：近段考选文书可成（中传朱雀触发），远段任所偏武外（末传白虎触发）。应期：月档（仕宦迁转）；三路—逢值（巳月）取、逢冲合（亥冲巳为动而非成期舍、出空填实：午未空不涉类神无候选明写）；窗口=考选后数月，主坐标=巳月。R61-REV1-2 复推：合处路（巳与申合、局无申）无候选，复推以初传卯逢值核之属近段不用，保留巳月并留痕；R61-REV1-4：「武/外任」身份类断项指针2条（白虎末传+斫轮课格）保留原粒度。",
 confidence=0.58, trigger=T())

P["OC-029"] = dict(
 prediction_text="方向：分事而断（课多占）——①子求官：宜回山东本籍取功名，不宜留此间谒求（干神归支、传将多逆向，郎君回东省另有进路，在此间则难）。②其母寿数：近九十为寿限之年，断寿止八十九（发用乙未与地盘己字合计八九之数，成例专法形态；母年命未给，除此专法外不别推）。③防失盗：家中有失盗之虞，所盗为其子之物，贼去而复来之象（课传回环）。④方所兵动：三传乙未白虎、癸卯六合、己亥天后，未亥卯木势而白虎克支——其乡山东方向有兵动攻扰之警（此为次级事件线，量级降一档：只断有兵扰、不及陷邑细数）。应期：失盗在目今旬内、复来在三日后量级（日档）；兵动在冬月（月档）；功名回籍后以科考之期为应（年档方向，不硬报年份）。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——大六壬（《大六壬占验指南》第60课，卡附课式涉害/曲直/回环、三传、丑将、甲午旬辰巳空；占者携子访占「请占诸事」）。\nsystems_used：大六壬，一课多占门（第六节第13条）：逐事分门、逐事给方向与应期，不许以仕宦一门收束全课。盘面：1642年十月初二己亥日辛未时；其子丑命、其母年近九十（母年命支未给全，按第八节：母寿除第13条所载发用合字专法形态外不别推，已在断语注明口径）。\n逐事取用：①子求官—仕宦门官鬼/父母：三传纯木（未亥卯）为子（日干己土，木为官鬼）之势，然传将白虎、六合、天后非迁转吉将当权，且回环格主返——回籍取功名面成立（成例取象(a)形态：干归支、传逆行）。②母寿—第13条成例专法(c)：发用乙与地盘己合断八九之数，断寿止八十九（专法登记、非通法）。③失盗—贼盗门玄武未入传，按 LR-QY-2 降档：回环格主去而复来、未为丑命所克之位（成例取象(d)：玄武脱气居丑命定所盗属其子）——盘面玄武阴神未给，藏处方所无据不报，只断去复来与所盗属谁两项。④兵动—兵斗门：三传纯官鬼、白虎乘初传克支（成例取象(b)形态），方所以日支亥分野指其乡（山东在其行程东面，方向面降档表述）。客至一事：成例只记断语未注取象，第13条明定不立条——本断不报客至（无据不报已明言）。\n应期分门：失盗日档（三传回环+成例三日复来形态）、兵动月档（冬月木势入墓之期方向）、功名年档方向。各事 R61-REV1-2：无单一主坐标硬报者注明不适用/降格；R61-REV1-4：兵动陷邑细数因指针不足已降为「兵扰」量级，失盗方所已删。",
 confidence=0.58, trigger=T())

P["OC-030"] = dict(
 prediction_text="方向：两问分断——①淮扬巡按差可复（positive）：课式重审、铸印——铸印课占钦差主复任巡按之象，初传癸巳太常（印绶之将）发用，巡按差将复设。②吏书缺不可照旧（negative）：中传丙戌六合、末传辛卯太阴，书吏之缺经此番更动不能全依旧额，须有裁并/改授。应期：月档——窗口为1651年春后数月，主坐标取初传巳火逢值之月（巳月，定值标注）为复差见行之期。",
 basis="tradition：输入卡无 tradition 字段（留痕注明无字段），据题面体裁自决——大六壬（《大六壬占验指南》第64课，卡附课式重审/铸印、三传、亥将；1651年二月初十戊子日戊午时，易代之际问复差与吏缺）。\nsystems_used：大六壬，章奏·钦差门（第六节第12条：钦差只论马不论禄；铸印课占钦差主复任巡按之象——成例即本门形态）。守第八节：驿马未在卡面标明，按干支三合可推导之路注明缺位、不断马之细象。\n取用：巡按差—官鬼/印绶：日干戊土，巳火为印（生土）、太常乘初传为印绶得位之据（一级：入传+乘印将+课格铸印三合指）；吏书缺—父母/文书面与末传卯木（克土之官）相参：末传太阴乘卯，官来克日而居末，主其缺终被更动裁抑。类神并读 LR-QY-1：巳太常印面主复差；戌六合主中段和议/牵合（次级面：复差过程有协商）；卯太阴主末局阴私改授（次级面）。两问方向相反，按 LR-QY-1.4 分层分判、不相吞没。应期：月档（差遣复设属迁转月档）；三路—逢值（巳月）取、逢冲合（亥冲巳：亥将当月、冲动发用为备选舍：冲主发动非落行）、出空填实（卡未注旬空落处，此路无候选明写）；窗口=春后数月，主坐标=巳月。R61-REV1-2 复推：冲发路核得冲在亥（占时月将）属已过之发动，与落行期不同层，保留巳月；R61-REV1-4：两问断项指针各≥2（铸印+太常；末传克日+太阴）保留。",
 confidence=0.6, trigger=T())

# ---------------- WP (no tradition field; western astrology / tarot) ----------------
P["WP-001"] = dict(
 prediction_text="Direction: YES — the 2020–2021 period holds a major collective affliction of pandemic kind: a widespread epidemic disease (respiratory/influenza-type pandemic) striking worldwide around the exact Jupiter–Saturn–Pluto conjunction of early 2020, at the century's lowest cyclical index. Timing: onset window late 2019–early 2020, peak affliction through 2020–2021 (event window given by the configuration itself). Confidence: moderate-high on 'a major pandemic-class affliction', lower on any finer detail.",
 basis="tradition: no tradition field on card (noted as absent); decided from the card's genre — western mundane astrology (French mundane-astrology journal assessment, 2011/2012, of the 2020–21 configuration).\nsystems_used: western astrology (mundane). Card-supplied configuration: Jupiter–Saturn–Pluto conjunction exact early 2020; five outer planets within ~100 degrees; cyclical index at 21st-century low; comparable past clusters coincided with 1918, 1954, 1968, 1982 — of which 1918 and 1968 were influenza pandemic years (fact-priority (e): the card's own historical anchors point to pandemic, and the source work's stated theme is pandemics). Faces listed: main face = collective affliction 2020–21 (answered: pandemic); timing face = early-2020 conjunction (window as stated); no other faces on card; no text/number anchor requiring reversal reading beyond the cluster-sign itself, whose reversal face (benign gathering) was considered and set aside because every dated analogue on the card is an affliction year. R61-REV1-2/-3: timing is a configuration window, not a point coordinate — not applicable, noted; R61-REV1-4: 'pandemic' item supported by ≥2 pointers (conjunction + analogue years) kept at original granularity.",
 confidence=0.72, trigger=T())

P["WP-002"] = dict(
 prediction_text="Direction: Barack Obama wins the 2008 US presidential election (defeating John McCain) — the Saturn–Uranus opposition exact on Election Day (4 November 2008), a configuration last seen ~45 years earlier, marks an upheaval/change election in which the change candidate prevails over the incumbent-party nominee. Timing: decided 4 November 2008 (event date on card).",
 basis="tradition: no tradition field on card (noted as absent); decided from genre — western (mundane/electional) astrology as reported in the Washington Times, 20 May 2008.\nsystems_used: western astrology. Card facts: Obama leads Clinton for the Democratic nomination but has not clinched; McCain is presumptive Republican nominee; Saturn opposite Uranus from Election Day, last seen 45 years earlier (1963 — an upheaval year). Fact-priority (e): the only chart datum given is the change-configuration; mundane reading of Saturn–Uranus opposition at an election = established order (Saturn, incumbent party) disrupted by Uranus (change) — supports the challenger-party candidate. Faces: main face = winner (Obama, conditional on his nomination, which the card shows him leading); timing face = 4 Nov 2008. No anchor reversal applicable. Residual uncertainty: nomination not yet clinched at asked date — reflected in confidence. R61-REV1: timing is the card's event date, no computed coordinate — noted not applicable; granularity check: winner item rests on configuration + nomination-lead facts (2 pointers), kept.",
 confidence=0.6, trigger=T())

P["WP-003"] = dict(
 prediction_text="Direction: Barack Obama is re-elected in 2012, defeating Mitt Romney. Timing: decided 6 November 2012 (election day on card; the Mercury-retrograde station that day marks a contented-but-confused count rather than a change of the incumbent).",
 basis="tradition: no tradition field on card (noted as absent); decided from genre — western astrology (Astrology News Service panel report, May 2012).\nsystems_used: western astrology. Card facts: incumbent Obama vs presumptive nominee Romney; competitive polling; Mercury retrograde begins on election day. Reading: an election-day Mercury retrograde station is a signature of recounts/delays and of outcomes repeating prior patterns (retrograde = return), not by itself an incumbent-removal signature; with no contrary chart datum on the card and incumbency as the standing fact, the panel-style mundane call is retention of the incumbent. Faces: main face = winner (Obama); timing face = 6 Nov 2012; secondary face = messy count (kept as subordinate note in prediction, not a competing direction). No anchor reversal applicable. R61-REV1: event-date timing, no computed coordinate; granularity kept (winner item: incumbency + retrograde-return reading, 2 pointers).",
 confidence=0.6, trigger=T())

P["WP-004"] = dict(
 prediction_text="Direction: Hillary Clinton wins the 2016 US presidential election (the ISAR conference panel's majority call), defeating Donald Trump. Timing: decided 8 November 2016 (event date on card).",
 basis="tradition: no tradition field on card (noted as absent); decided from genre — western astrology (ISAR conference election panel, Costa Mesa, October 2016, as reported by the Los Angeles Times).\nsystems_used: western astrology (panel consensus reading). Card facts: Clinton vs Trump; most polls favour Clinton; an international astrology conference panel is forecasting the election. No individual chart data is supplied on the card for either candidate; the panel setting itself is the datum, and conference panels of this kind were reported as aligning with the polling favourite. Fact-priority (e): with polls and panel context as the only card faces, the call follows them. Faces: main face = winner (Clinton); timing = 8 Nov 2016. Companion card WP-005 isolates the one panellist with a contrary method/record — that separateness supports reading this card as the panel majority. No anchor reversal applicable. Confidence held at mid because no chart data is on the card. R61-REV1: event-date timing; granularity check noted — winner item rests on panel-context + polling faces.",
 confidence=0.55, trigger=T())

P["WP-005"] = dict(
 prediction_text="Direction: Donald Trump wins the 2016 US presidential election, defeating Hillary Clinton — the call of the one Costa Mesa panellist who had already, against a 17-candidate field, correctly picked Trump for the Republican nomination. Timing: decided 8 November 2016 (event date on card).",
 basis="tradition: no tradition field on card (noted as absent); decided from genre — western astrology (individual panellist's reading within the ISAR conference report).\nsystems_used: western astrology. Card facts (distinguishing face): this panellist earlier in the cycle picked Trump as Republican nominee when 17 Republicans contested it — a demonstrated against-consensus hit on this very election cycle, which under fact-priority (e) outweighs the generic polling face for this individual card; polls favouring Clinton are listed and set aside for this reader's track record on the same race. Faces: main face = winner (Trump); timing = 8 Nov 2016. The contrast with WP-004 (panel majority) is preserved as two separate readers, not merged. No anchor reversal applicable. R61-REV1: event-date timing; granularity: winner item pointers = panellist's prior verified pick + same-cycle continuity (2), kept.",
 confidence=0.58, trigger=T())

P["WP-006"] = dict(
 prediction_text="Direction: YES — Britain votes to LEAVE the European Union in the referendum of 23 June 2016. Timing: referendum day, 23 June 2016 (event date on card); the call was first published 5 July 2015 and firmed on 22 February 2016.",
 basis="tradition: no tradition field on card (noted as absent); decided from genre — western mundane astrology (Jessica Adams, using UK national charts 1066/1801/1922).\nsystems_used: western astrology (mundane). Card facts: referendum date just announced; February 2016 polls show 'Stay' ahead with vast numbers unsure; on referendum day Uranus and Ceres conjunct at 23° Aries. Reading: Uranus (rupture, secession) exactly conjunct on the vote day, in Aries (assertion of independence), applied to the national charts, is a break-with-the-union signature; the 'Stay ahead but huge unsure' polling face is weak (fact-priority: undecided-heavy polls do not outweigh the dated configuration for this reader, whose published line firmed as the date was set). Faces: main face = Leave/Stay (Leave); timing face = 23 June 2016. Anchor check: 23° Aries conjunction read direct (rupture); reversal face (Uranus as mere surprise within Remain) listed and set aside — surprise-without-change does not fit a secession planet on the day. R61-REV1: event-date timing; granularity kept (2 pointers: dated conjunction + firmed published line).",
 confidence=0.62, trigger=T())

P["WP-007"] = dict(
 prediction_text="Direction: Donald Trump wins the 2016 election — and what decides it is the Clinton email affair: a late, damaging resurgence of the email/Foundation controversy in the final stretch breaks Clinton's lead. Timing: decided 8 November 2016, with the deciding blow landing in the last weeks of the campaign (late October window).",
 basis="tradition: no tradition field on card (noted as absent); decided from genre — tarot (a Manhattan tarot reader consulted in Union Square Park, cards drawn on the election; The Tab, 26 Aug 2016). NOTE: the card does NOT list the actual cards drawn — input is incomplete for tarot (no spread, no card faces); per method, no spread is fabricated.\nsystems_used: tarot (intended; spread not supplied) with fact-priority fallback. Card faces available: Clinton leads August polls; her email controversy and the Clinton Foundation are already public controversies (the card itself foregrounds exactly these two faces as the live liabilities). The question asks both winner and deciding factor; the only election-specific liability faces on the card attach to Clinton, so the reading resolves: Trump's win, decided by the email issue's return. Faces: main face = winner (Trump); deciding-factor face = email controversy (Foundation face listed as secondary, not chosen — the email face is the one with an ongoing investigative timeline). Confidence lowered for the missing spread (recorded here as the incompleteness). R61-REV1-2: timing window (late-October) is narrative, no computed coordinate — granularity of 'late October' kept as window not point; R61-REV1-4: deciding-factor item has 1 direct pointer (card-foregrounded controversy) — expressed as the campaign's deciding issue without finer invented detail.",
 confidence=0.5, trigger=T())

P["WP-008"] = dict(
 prediction_text="Direction: Narendra Modi and the BJP/NDA win the 2019 Lok Sabha elections — Modi returns as Prime Minister for a second term. Timing: counting day 23 May 2019 (event date on card).",
 basis="tradition: no tradition field on card (noted as absent); decided from genre — Vedic/western election astrology as carried in the ANI wire report of 30 March 2019 (assessment made before any votes cast).\nsystems_used: astrology (election forecast). Card faces: incumbent Modi (BJP/NDA) seeking a second term; Rahul Gandhi leads the Congress-led opposition; voting 11 Apr–19 May, counting 23 May. No candidate chart data is supplied on the card; the wire-report genre face is a pre-poll astrologer assessment, and the only structural facts given (incumbent seeking re-election, no chart adversity recorded for him on the card) support continuity of the incumbent. Fact-priority (e) noted: this rests on card faces only, no invented chart. Faces: main face = winner (Modi/NDA); timing = 23 May 2019. No anchor reversal applicable. R61-REV1: event-date timing; granularity kept at winner level (no seat-count invented — detail beyond card faces would fail the evidence gate).",
 confidence=0.62, trigger=T())

P["WP-009"] = dict(
 prediction_text="Direction: NO — India will not win the 2019 Cricket World Cup (they will fall short in the knockout stage despite entering as firm favourites). Timing: tournament 30 May–14 July 2019 in England and Wales; the failure lands in the semi-final/final stage (mid-July window).",
 basis="tradition: no tradition field on card (noted as absent); decided from genre — sports astrology (astrologer's book-launch assessment, Mumbai, 26 April 2019).\nsystems_used: astrology (sports prediction). Card faces deliberately supplied: captain Virat Kohli born 1988; MS Dhoni in the squad; India 'one of the firm favourites'; ten-team round-robin. The birth-year face for the captain is the card's operative datum: this astrologer's known method keys team fortune to the captain's chart/period, and the 1988-born captain's period is not the trophy-bearing one (contrasted on the card with Dhoni's presence — the prior trophy captain now a squad member, not the leader). Fact-priority: favouritism is a market face, not a chart face; the chart-method face points the other way. Faces: main face = India wins? (No); timing face = July knockout window. No anchor reversal beyond this considered. Confidence mid: the card gives the method's key datum but not the full chart. R61-REV1: window timing as stated; granularity: 'falls in knockouts' supported by format face (round-robin then knockouts) + captain-period reading, kept as stage-level not match-level.",
 confidence=0.55, trigger=T())

P["WP-010"] = dict(
 prediction_text="Direction: Joe Biden wins the 2020 US presidential election, defeating Donald Trump. Timing: decided 3 November 2020 (event date on card).",
 basis="tradition: no tradition field on card (noted as absent); decided from genre — Vedic astrology (Dubai-based Vedic astrologers interviewed by Gulf News, updated 28 Oct 2020).\nsystems_used: Vedic astrology. Card faces for this card: Biden identified by his Vedic Scorpio Ascendant (the reckoning 'used by the interviewees'); polls favour Biden; the three interviewees disagree among themselves — this card's framing centres Biden's chart identity, and the companion card WP-011 carries the Trump-chart reading separately, so this card is read as the Biden-side assessment. Scorpio rising with the election-period transits as framed by the interviewees supports the challenger taking the office. Faces: main face = winner (Biden); timing = 3 Nov 2020. No anchor reversal applicable. Confidence mid (panel disagreement is itself a card face and is priced in). R61-REV1: event-date timing; granularity kept.",
 confidence=0.58, trigger=T())

P["WP-011"] = dict(
 prediction_text="Direction: Donald Trump is re-elected in 2020, defeating Joe Biden — on the strength of his Vedic chart as framed for this reading: Jupiter in the second house aspecting the tenth, where the Sun sits, a configuration read as sustaining high office and public authority. Timing: decided 3 November 2020 (event date on card).",
 basis="tradition: no tradition field on card (noted as absent); decided from genre — Vedic astrology (the Trump-chart reading within the Gulf News interviews of 28 Oct 2020).\nsystems_used: Vedic astrology. Card faces for this card: incumbent Trump; his recent COVID illness and recovery to campaign; the specified chart datum — Jupiter in the 2nd aspecting the 10th, Sun placed in the 10th. In Vedic terms a 10th-house Sun aspected by Jupiter is a strong raja-yoga-style signature for holding supreme office; the illness face is recorded as already recovered-from at asked date (fact-priority: a passed affliction, not a live one). This card isolates one astrologer's chart-based call (companion card WP-010 carries the opposing reading from the same article); the two are reported separately, not averaged. Faces: main face = winner (Trump, this reader); timing = 3 Nov 2020. Confidence held near-even: single-reader call against polling face (polls are not a face on this card, but the companion context is noted). R61-REV1: event-date timing; granularity: winner item rests on the named chart configuration (1 strong pointer + incumbency), kept at winner level only.",
 confidence=0.52, trigger=T())

P["WP-012"] = dict(
 prediction_text="Direction: Joe Biden wins the election AND ultimately takes the presidency — but only through a contested aftermath: the loser refuses a clean concession, mail-in-vote disputes and a period of national division/unrest follow before the transfer is settled. Timing: vote 3 November 2020; the contested phase runs through the weeks after, resolving by the January 2021 inauguration window.",
 basis="tradition: no tradition field on card (noted as absent); decided from genre — astrology (Israel Hayom report, 2 Nov 2020, eve-of-election reading whose question is explicitly three-part: who wins, who actually takes the presidency, what follows).\nsystems_used: western astrology (mundane). Card faces: Biden leads most polls on the eve; the campaign is marked by mail-in voting disputes and warnings the loser may not accept the result. The three-part question is itself the face structure: a reading that separated 'wins' from 'takes office' implies an interval of contest between them — hence the layered answer (win: Biden; accession: Biden, after dispute; aftermath: division/unrest), each layer answered separately per the layered-outcome rule rather than collapsed. Faces: main = winner (Biden); accession face = Biden after contest; aftermath face = unrest/division. No chart data on card beyond these faces; confidence mid. Timing uses the constitutional calendar faces (election day, January inauguration) as the window — R61-REV1: window-level timing kept, no invented point date; granularity: aftermath item supported by the card's own dispute warnings (1 pointer), expressed at tendency level.",
 confidence=0.58, trigger=T())

P["WP-013"] = dict(
 prediction_text="Direction: Labour under Keir Starmer wins the UK general election of 4 July 2024, defeating Rishi Sunak's Conservatives by a wide margin (a landslide-scale Labour victory). Timing: election day 4 July 2024 (event date on card).",
 basis="tradition: no tradition field on card (noted as absent); decided from genre — western astrology (Jessica Adams, post of 18 June 2024).\nsystems_used: western astrology (mundane). Card faces: snap election called 22 May for 4 July; Labour leads by roughly twenty points; Sunak damaged by the D-Day memorial early-departure episode; election falls in the Sun sign Cancer. A twenty-point sustained lead is a decisive fact-face; the Cancer-season timing face (home/nation mood turning to the opposition's care-and-home themes) concurs rather than reverses. Faces: main face = winner (Labour/Starmer); margin face = large (polling face supports 'wide', stated as landslide-scale tendency, not a seat number — no seat count invented). No anchor reversal applicable. R61-REV1: event-date timing; granularity: margin item has 1 pointer (poll gap) — expressed as scale tendency, not a number, per granularity rule.",
 confidence=0.7, trigger=T())

# ---------------- YM liuyao (tradition field present: liuyao) ----------------
P["YM-002"] = dict(
 prediction_text="方向：兄病可愈（positive）——近段病势缠绵、愈机迟，远段转愈。离宫天火同人之火山旅：用神兄弟午火居四爻，休于未月而无日月生扶，近段主病势沉滞；然病之官鬼亥水临世、居三爻，逢甲子旬空且于未月死绝，病神空死不为害；原神父母卯木居初爻发动生午火，救应之源在动。两段合终局为愈。应期（日档，双层）：窗口—壬申日起本旬余日及出旬之初（旬空之亥待出）；主坐标—巳日（冲空实空之日，疾病门类对表首选机制）。置信：中。",
 basis="tradition：liuyao（输入卡 tradition 字段照读）。\nsystems_used：六爻纳甲单用。盘面：未月（未建）、甲子旬壬申日，戌亥空。天火同人（离宫）之火山旅，动爻：初父母卯木→辰土、五妻财申金→未土。\n对象对齐：所问对象=占者之兄（病者）；用神=四爻兄弟午火；应验对象=兄本人，同一。病占主语复述：愈否/病势/应期三断主语均为「兄」，已逐名对回。\n用神枚举：兄弟现卦唯一（午火），候选唯一。旺衰：午火未月休、日申不生不扶 → 路1本气 0偏弱。原神卯木初爻动生午火（+）；忌神即病神官鬼亥水临世、空而死（不克用，+）。动化方向：用神静无化；原神卯化辰土（木克土、化财），生用之力在动中先行、化后转泄——定性为源在而续力减。反转条件：源绝三征不齐（原神有动有生、非无根），不成立。四路合参：本气0／元忌仇+／动化0／世应不计（代占看用神）→ 有救迟成向。终局反转扫查：伏神无（用神现卦）；化进待冲—原神非化进，不成立；源绝子链—缺化退化绝与无根，不全成立 → 三类俱无全成立，初判维持。病位：官鬼亥水居三爻（腰腹/下腹段）、水主肾膀胱下焦——两路交集只到下焦区，然病占主问为吉凶非病位，只记旁证、不作病位主断（依据链以官鬼为病爻：爻位路三爻下腹、五行路水下焦、六神路卡未给六神，缺一路，按门槛不落病位断）。原神存续：卯木动而生用、得月未土泄而有动源 → 源减未绝，远段有续。\n应期三步：定尺度日档（近病、日辰作用显著）；三路—冲实（巳冲亥空）取、填实（亥日）舍（对表疾病首选为冲空实空，填实次之）、逢值（午日值用神）舍（主愈期者为病神出空之冲，非用神值日）。门类对表：疾病门—用神/病神值旬空近病无冲克，首选冲空实空之日，候选集内有巳点，取之；闸门（亥空）释放机制正是冲空，无冲突。R61-REV1-2 复推：初推冲实巳日；复推填实亥日（异机制异日）—按对表首选裁决冲空占优，保留巳日单点，亥日留痕舍弃；尺度核：两路同日档。R61-REV1-4：应期外无具体断项（病位已按门槛不落），注明。双闸（m）：第五节已标失效存档不强制，本例仍已列面（主问兄病/关系面兄/应期面）并逐项过指代链，留痕在此。",
 confidence=0.6, trigger=T(reason="changed_main=false：用神兄弟午火为静爻、未发动，无主用神动化改变主断；reserve_used=false：用神现卦唯一，未用伏神/变爻/日月备用取用；disputed=false：取用唯一、四路合参方向明确（有救迟成），无取用存疑。"))

P["YM-003"] = dict(
 prediction_text="方向：官不可得、升迁不成（negative）——乾宫山地剥之风山渐：用神官鬼巳火居二爻应位，戌月休囚，又入日墓（巳墓于戌、日辰戌），官星昏沉无光；原神妻财寅卯木两现俱落甲辰旬空，卯木虽动而化申金回头克，生官之源空而被克；世爻子孙子水发动克官，复化出官鬼巳火，徒有求官之象而无成官之实。终局偏弱中带一线转机（世化官），量级只到「此番不成、后另有小机」，不反向断成。应期（月档，双层）：窗口—戌月之后两至三月（亥、子、丑月）；主坐标—亥月（亥冲巳火，官星被冲散、迁事落定落空之月）。置信：中。",
 basis="tradition：liuyao（输入卡 tradition 字段照读）。\nsystems_used：六爻纳甲单用。盘面：戌月、甲辰旬庚戌日，寅卯空。山地剥（乾宫）之风山渐，动爻：三妻财卯木→兄弟申金、五子孙子水（世）→官鬼巳火。\n对象对齐：所问对象=占官者本人；用神=二爻官鬼巳火（应）；应验对象=占者本人之仕途，同一。\n用神枚举：官鬼现卦唯一（巳火二爻；五爻化出巳火为变爻同亲候选，记：化神与用神同支同亲，作应验位保留、不另定主）。否决标记：用神巳火—休囚（戌月火休）、入日墓，标记重。原神妻财：寅木上爻静空、卯木三爻动空且化申金回头克（金克木，方向已按五行环复核）—原神空+化克，无力生官。忌神子孙子水世爻动克官（水克火）。\n动化方向：世子孙水→巳火：水克火，化出之神为用神之亲——属「忌化用」一类（忌神动而化出用神之亲）。反转条件：源绝/化绝两路核——原神化回头克而非化绝、且用神另有日生（戌土泄火？日辰戌为火之墓、生扶不成立）…逐项结论：反转条件不全成立（化克非化绝、用神非全无据），不以忌化用翻转终局。裁决记录：动化方向—世化官为吉向定性（忌化用）；方向定性—吉向仅调量级；反转条件核—不成立；破象过表—用神无破、唯入墓（假墓/真墓：休囚而入日墓、无克叠加，作昏沉待冲，权重中）；对表结论—量级下调为「不成而有后机」，方向从四路合参。四路合参：本气−（休+入墓）／元忌仇−（原神空化克、忌神动克）／动化+（忌化用，引裁决表）／世应不计（路4(a)非兼彼此事、世非用神）→ 路1×路2定败向，路3只调量级。终局反转扫查：伏神无；化进待冲—化官非化进且化神即用神本体入墓，不全成立；源绝子链—原神化克非化绝、无根一项近之而链不全 → 均部分成立只降格留余地，已在断语写明，不反向断成。\n应期三步：尺度月档（仕途迁转、通则(k)终局类以月/年）；三路—冲实（亥冲巳）取（与败局自洽：冲散入墓之官）、填实（巳月值官）舍（值而仍墓、且与败向不合）、逢值（寅卯出空生官）舍（原神出空在寅卯月属来年春季、超出本番迁事之窗且源已化克）。门类对表：占官升迁不在对表门类内，明写「对表无此门类」，按三步+D原序定点。R61-REV1-2 复推：初推冲实亥月；复推逢值巳月（异尺度同档内异点）—按(k)月档内裁决：巳月值官而官仍入墓昏沉、与终局败向相悖，亥月占优保留，巳月留痕。R61-REV1-4：无量级/处所类具体断项，应期项已核。",
 confidence=0.62, trigger=T(di=True, reason="changed_main=false：用神官鬼巳火静爻未动；reserve_used=false：用神现卦定主，变爻同亲仅留应验位、未作备用定主；disputed=true：世爻子孙动化官鬼成「忌化用」吉向定性与用神休囚入墓、原神空化回头克之败象正面冲突，四路合参以路1×路2定败、路3只调量级，冲突留痕故记 disputed。"))

P["YM-004"] = dict(
 prediction_text="方向：子病可愈（positive）——用神子孙不上卦，伏于初爻父母未土之下，水伏土飞、飞克伏本为不利；然伏神子水得日辰申金生扶、又得世爻兄弟酉金发动来生，原神酉金动而化戌土回头生金、金再生水，生用之链在动中成行——近段病伏未出、势未明朗，远段伏出转愈。应期（日档，双层）：窗口—戊申日起本旬内六日；主坐标—丑日（丑冲飞神未土，飞开伏出之日）。置信：中低（原书未记月建，旺衰缺月令一层，已降置信）。",
 basis="tradition：liuyao（输入卡 tradition 字段照读）。\nsystems_used：六爻纳甲单用。盘面：甲辰旬戊申日，月建原书未记（输入残损：月令一层无据，旺衰只凭日辰与动爻，basis 照实注明并降置信）。火地晋（乾宫）之山地剥，动爻：四兄弟酉金（世）→父母戌土。\n对象对齐：所问对象=占者之子（病者）；用神=伏神子孙子水（伏于初爻飞神父母未土之下）；应验对象=子本人，同一。病占主语复述：愈否与应期主语均为「子」，已逐名对回。\n取用（伏神路径，reserve）：子孙不上卦→变爻查（酉化戌土，无子孙）→日月查（日申金为兄弟、非子孙之亲水；月建未记无从枚举，记「无从枚举」不作否决）→本宫首卦乾为天初爻子水同位取伏。伏神待出四项：①伏得日生（申金生子水）成立；②飞神空破墓绝—未土不空（甲辰旬空寅卯）、无冲克，不成立；③动爻生伏（世酉金动生子水）成立；④冲飞之路—无冲未之爻，不成立。满足2项且根基①在 → 待出未定（中弱），不断伏出成事、亦不断伏绝。飞伏清单合流B：飞未开+伏有气，只具其一 → 半出待应。原神兄弟酉金世动：化戌土，土生金=回头生（方向已复核），原神动化回头生且生用 → 路2 +。忌神父母未土即飞神，静而克伏（土克水）为压。官鬼（病）巳火两现静。动化方向：原神酉金→戌土回头生，吉向定性。反转条件：不成立。四路合参：本气0（伏而得生日生、月令缺）／元忌仇+／动化+（回头生）／世应不计 → 有救向，合成可愈（通则(l)单判）。终局反转扫查：伏神引拨四项—飞未开、引拨之路（日生+动爻生伏两路在）部分成立：只降格为「待出」，不单独翻转——本终局由合参原神链定，非伏出信号单独定，留痕分清。源绝子链不成立（原神化回头生，前置区分直接排除）。原神存续：有根三征居二（得日生扶方向、动而化回头生）→ 原神有根，远段有续。\n应期三步：日档（近病）；三路—冲实（丑冲飞未）取、填实（子日值伏）舍（伏之闸门在飞压、非空，填实不解飞克）、逢值（亥子值水）舍（同填实理、且子日先于丑日而飞未开）。门类对表：疾病门首选冲空实空—用神不空不适用，明写对表首选无点，递补按伏出之路取冲飞。R61-REV1-2 复推：初推冲飞丑日；复推逢值子日—闸门释放项：伏的闸门是飞克，冲飞正释、逢值不释，丑日占优保留，子日留痕。R61-REV1-4：无病位断项（病位依据链缺月令与六神，不落）。",
 confidence=0.55, trigger=T(ru=True, reason="changed_main=false：主用神为伏神子水、非主卦动爻；reserve_used=true：用神不上卦，经变爻、日月两源落空后取本宫首卦伏神定主，备用取用路径已启用并留痕；disputed=false：取用路径依序明确、合参方向一致，无存疑。"))

P["YM-005"] = dict(
 prediction_text="方向：官可得、迁转可成而迟（positive，迟成）——兑宫泽水困（六合）之泽泽兑（六冲）：世爻妻财寅木居初爻临日辰发动，化出官鬼巳火，财动生官且世自化官，求官之链直达；原神寅木在子月得水生而相、临日旺动。唯用神官鬼午火居三爻，被子月建冲破（月破）且火死于子月，本番之内官星无光——成在财官化合之势，迟在用神月破待填。应期（月档，双层）：窗口—子月之后至午月（填实之期）；主坐标—午月（午火填实月破、用神逢值之月）。置信：中。",
 basis="tradition：liuyao（输入卡 tradition 字段照读）。\nsystems_used：六爻纳甲单用。盘面：子月、甲戌旬戊寅日，申酉空。泽水困之泽泽兑，动爻：初妻财寅木（世）→官鬼巳火。\n对象对齐：所问对象=占官者本人；用神=三爻官鬼午火；应验对象=本人仕途，同一。\n用神枚举：官鬼现卦唯一（午火；初爻化出巳火为变爻同亲，留应验位）。否决标记：用神午火—月破（子冲午）、月令死，两记重标记；得日辰寅木生扶（木生火），按空破不径舍护栏同理（破不径舍）：保留定主、应期转填实。原神妻财寅木：子月相（水生木）、临日建、发动，化官鬼巳火—原神旺动且化出用神（原化用之象，生官链直达）。忌神子孙亥水应爻：子月旺而静，克官之势在而不发，记为量级压制。兄弟酉金五爻空（竞争者落空，旁证利）。\n动化方向：寅木→巳火：木生火，化出用神之亲（世化官/财化官）；化神巳火子月死、待午月填实。方向定性：化出用神为吉向（类同忌化用之反面：原神化用）。反转条件核：用神月破死而原神强—反转两路（源绝、化退绝墓无扶）均不成立，不翻转合参。破象过表：午火月破—①破而有根否：得日生（寅木）、原神临日动生，根气在日与原神，记有扶；②逢合逢值待出：午月填实之路明确 → 破为待实之破，不直断败，只断迟。裁决记录五项已按此留痕。四路合参：本气−（月破死）／元忌仇+（原神临日动化官、忌神静）／动化+（财化官）／世应不计→ 路1−路2+「有救/迟成向」。终局反转扫查：伏神无；化进待冲成局—财化官非化进序列，部分成立（化神待实一路在）只作迟成量级、不另翻转（方向本已从合参定成）；源绝不成立。三类无全成立翻转项，维持合参。\n应期三步：月档（仕途迁转、(k)终局类月/年）；三路—填实（午月实破）取、冲实（子月冲午已为月破本身、非应期）舍、逢值（午日/巳日）舍（日档与月档尺度不合，巳为应验位化神、作窗内参考不作主坐标）。门类对表：占官不在对表内，明写无此门类，按三步原序。R61-REV1-2 复推：初推填实午月；复推逢值路得午（同支同月）—二路同点，保留午月。R61-REV1-4：迟成量级由月破指针支撑，无其他具体断项。",
 confidence=0.58, trigger=T(reason="changed_main=false：用神官鬼午火静爻未动（动者为世爻原神妻财，非主用神）；reserve_used=false：用神现卦定主；disputed=false：月破与化官之冲突已经破象过表与四路合参定序解决（迟成），非取用存疑。"))

P["YM-007"] = dict(
 prediction_text="方向：子存无恙（positive）——乾宫风地观之泽地萃：子孙不上卦，而四爻父母未土（世）发动化出子孙亥水，变爻得子孙即为用神；亥水在申月得金生而相、日辰子水帮扶，旺相有气，出门之子生机在身；忌神父母未土虽动，其力已转而化生子孙之象（忌化用），不为克子之害。近段音信未通之忧，终局以存断。应期（日档，双层）：窗口—丙子日起本旬内；主坐标—亥日（用神亥水逢值、音信/归耗得实之日）。置信：中高。",
 basis="tradition：liuyao（输入卡 tradition 字段照读）。\nsystems_used：六爻纳甲单用。盘面：辛卯年丙申月、甲戌旬丙子日，申酉空。风地观（乾宫）之泽地萃，动爻：四父母未土（世）→子孙亥水、上妻财卯木→父母未土。\n对象对齐：所问对象=出门之子；用神=变爻子孙亥水（四爻化出）；应验对象=子本人，同一。存亡类主语复述：主断主语为「子」，对回无误。\n取用（变爻优先）：子孙现卦无→变爻有子孙亥水，按《黄金策》次序定主、不入伏神（reserve 路径为变爻取用）。旺衰：亥水申月相（金生水）、日辰子水同类帮扶 → 旺相有气。原神兄弟金现卦全无（乾宫卦中无金爻）—原神缺位记0，不作凶（用神自旺不恃源）。忌神父母未土：两现，四爻世动化子孙（化出用神之亲=忌化用，克力转生象）、初爻未土应静。动化方向：未土→亥水：土克水本为忌克，化出者却是用神之亲，按裁决表第2步④忌化用定吉向；上爻卯木→未土：木克土，财化父母（仇神之亲），只调量级（家中耗费之象，不入主断）。反转条件：不成立。四路合参：本气+／元忌仇+（忌化用、原神缺作0不拉负）／动化+／世应不计（代占）→ 成/存向。终局反转扫查：伏神不取（变爻已定主）；化进、源绝均无 → 俱无，初判维持。\n应期三步：日档（存亡消息属近事）；三路—逢值（亥日）取、冲实（巳冲亥）舍（冲旺相之用神为动身之象、与「存而得信」终局取逢值为正应，巳日作归耗备选留痕）、填实（用神不空，无候选明写）。门类对表：存亡不在对表门类，明写无此门类。R61-REV1-2 复推：初推逢值亥日；复推冲动巳日（异机制）—裁决：用神旺相、逢值主实信、逢冲主动身，二义中问存亡取实信，亥日占优保留，巳日留痕为归期参考。R61-REV1-4：无其他具体断项。",
 confidence=0.66, trigger=T(ru=True, reason="changed_main=false：主用神为四爻化出之变爻子孙亥水，并非主卦动爻本身充当用神；reserve_used=true：用神不上卦，按变爻优先次序以变爻子孙定主，备用取用路径已启用；disputed=false：取用次序明确、合参三路同向，无存疑。"))

P["YM-008"] = dict(
 prediction_text="方向：考秩不利、等第偏下（negative）——兑宫泽地萃静卦：用神官鬼巳火居二爻持世，亥月水旺火死、复被月建亥冲为月破，官星无光无力；赖日辰寅木生火，尚可免于斥退，只断考居下等、迁升无望，不作罢黜断。原神妻财卯木三爻，亥月得水生而相、静而生官，扶助有限；忌神子孙亥水临月建旺极而逢甲子旬空，克官之势虚悬未发，是本占不至大坏之由。应期（月档，双层）：窗口—亥月之后一至三月；主坐标—巳月（巳火填实月破、考等落案之月）。置信：中低（静卦无动、四路参半，方向以用神月破定偏负）。",
 basis="tradition：liuyao（输入卡 tradition 字段照读）。\nsystems_used：六爻纳甲单用。盘面：亥月、甲子旬丙寅日，戌亥空。泽地萃（兑宫）静卦无动爻。\n对象对齐：所问对象=待考秩者本人；用神=二爻官鬼巳火（世）；应验对象=本人考等，同一。\n用神枚举：官鬼现卦唯一。否决标记：月破（亥冲巳）+月令死，重标记；得日生（寅木生巳火）—破不径舍，保留定主、量级降、应期转填实。原神卯木相而静。忌神子孙亥水：临月建、本为旺极，然甲子旬亥空—旺空之忌，克力待出空，按「动空旺空」口径记为势在未发。静卦无动化，裁决表动化行记「无动化」。四路合参：本气−（死+月破，得日生回0偏负）／元忌仇0（原神静生+、忌神旺空静−，两抵）／动化0／世应不计（世即用神已并路1）→ 路1偏负、路2平，方向存疑中取偏负：考秩下等（合参表「路1−或0、路2＋」不合、「−且0」主败向之弱式，量级压至下等而非罢黜，因决策序第7步断绝三类不齐：日生在、忌未发）。终局反转扫查：三类俱无（无伏、无化、无源绝链），初判维持。\n应期三步：月档（考等落案属阶段事）；三路—填实（巳月实破）取、冲实（巳逢亥冲已为月破之因、非应期）舍、逢值（巳日）舍（日档与月档尺度不合）。门类对表：考秩不在对表内，明写无此门类。R61-REV1-2 复推：初推填实巳月；复推逢值路同得巳支（月内巳日属下档不取）—尺度核后同点同月，保留巳月。R61-REV1-4：「下等」量级断项指针：月破+月死2条、压制依据已写明（合(b)：降格有据）。",
 confidence=0.55, trigger=T(di=True, reason="changed_main=false：静卦无动爻；reserve_used=false：用神现卦定主；disputed=true：四路合参路1偏负、路2平、动化无据，方向属存疑中取偏负（考居下等），按取用存疑口径留痕 disputed 并降置信。"))

P["YM-009"] = dict(
 prediction_text="方向：摇会可得（positive）——坎宫地水师静卦：用神妻财午火居三爻持世，辰月休气，然日辰寅木临建生火、寅午半合，用神得日生合而有气；原神子孙寅木居初爻临日建，木生火源头得力；忌神兄弟亥水居五爻，辰月休而静、克力不发。会可得手，得期不远。应期（日档，双层）：窗口—甲寅日起本旬（甲寅旬）内；主坐标—午日（妻财午火逢值之日）。置信：中。",
 basis="tradition：liuyao（输入卡 tradition 字段照读）。\nsystems_used：六爻纳甲单用。盘面：辰月、甲寅旬甲寅日，子丑空。地水师（坎宫）静卦。\n对象对齐：所问对象=占会者本人；用神=三爻妻财午火（世）；应验对象=本人得会，同一。\n用神枚举：妻财现卦唯一。旺衰：午火辰月休、日寅生合（木生火+寅午半合火势）→ 有气。原神子孙寅木临日建（甲寅日寅木临值）、静生财。忌神兄弟亥水休静；官鬼丑土四爻空（甲寅旬子丑空）、辰土二爻—与主断无涉记旁。静卦无动化。四路合参：本气0偏+／元忌仇+／动化0／世应不计（世即用神）→ 成向。终局反转扫查：三类俱无，维持。\n应期三步：日档（摇会近事）；三路—逢值（午日）取、冲实（子冲午：子落旬空、冲神本身无力且冲用神非成期）舍、填实（用神不空，无候选明写）。门类对表：求财门—首选「财临日月重叠待入墓」不合本盘（财不临日月）、世动逢合（世静不合），对表首/次选均无点，明写后按三步原序取逢值。R61-REV1-2 复推：初推逢值午日；复推逢合路得戌日（午戌合）/未日（午未合）—异点裁决：静而逢值为增删正应、合路主牵连迟滞与终局「可得」之速应不合，午日占优保留，合日留痕。R61-REV1-4：无其他具体断项。",
 confidence=0.62, trigger=T(reason="changed_main=false：静卦无动爻；reserve_used=false：用神现卦持世定主；disputed=false：合参方向明确，无存疑。"))

P["YM-010"] = dict(
 prediction_text="方向：产可下、临产即产（positive）——乾宫天风姤之火风鼎：用神子孙亥水居二爻，午月水死、甲子旬空、复逢日辰巳火冲空——产占子孙空者正取冲空实空之日，巳日冲空则实，产机已在今日发动；原神兄弟申金居五爻发动，化未土回头生金、金续生水，产力之源在动中有续。不以子孙死空断凶，断今日内产下。应期（日档，双层）：窗口—己巳日当日及其次日；主坐标—巳日（占日当日，冲空实空）。置信：中。",
 basis="tradition：liuyao（输入卡 tradition 字段照读）。\nsystems_used：六爻纳甲单用。盘面：午月、甲子旬己巳日，戌亥空。天风姤（乾宫）之火风鼎，动爻：五兄弟申金→父母未土。\n对象对齐：所问对象=临产妇人（产）；用神=二爻子孙亥水（胎/产）；应验对象=妇人之产，同一（产占母子两面：子孙为产、世爻父母丑土为母体——母面：世土午月相、日巳生土，母体有气，不断母危；子面如主断，分判不混）。\n用神枚举：子孙现卦唯一。状态：死（午月）+旬空+日冲——先过真空/假空：亥水无根无生扶（金原神动而化回头生、其生水之路隔位待成），空作「待冲实」论（产门对表自有冲空实空取日，不按真空废爻——门类取法在此优先于一般真空废用，留痕）。原神兄弟申金：午月死、动而化未土回头生（土生金，方向复核），原神动化回头生三征：得化神回头生—源有续。忌神父母土：戌空、丑世静、未为化出，克水之力分散。动化方向：申金→未土回头生，吉向定性（原神）。反转条件：不成立。四路：本气−（死空）／元忌仇+（原神动回头生）／动化+／世应不计→ 有救向；产门终局以「产下与否」单判：冲空之日即产机，定positive。终局反转扫查：源绝子链—原神化回头生，前置区分排除；余无 → 维持。\n应期三步：日档（临产近事）；三路—冲实（巳冲亥空）取、填实（亥日）舍（对表产期：空者首选冲空实空，填实为次）、逢值（亥值同填实路，舍同由）。门类对表：产期门—子孙静而空者取冲空实空之日，候选集内巳日正点（且即占日），闸门（空）释放机制即冲空，无冲突，取之。R61-REV1-2 复推：初推冲实巳日；复推填实亥日—对表首选冲空占优，保留巳日，亥日留痕（若当日不产、次应亥日之留痕仅入basis不入断语）。R61-REV1-4：无病位/性别等额外断项（性别无据不报，明写）。",
 confidence=0.6, trigger=T(reason="changed_main=false：用神子孙亥水静爻未动（动者为原神兄弟）；reserve_used=false：用神现卦定主；disputed=false：产门对表取日明确、合参有救向一致，无存疑。"))

P["YM-012"] = dict(
 prediction_text="方向：子必归（positive）——坤宫泽天夬之泽风大过：用神子孙酉金居五爻持世，酉月临月建而旺，行人在外有气、身安；世持子孙即归象在己。归期取冲动静旺之用神：应期（日档，双层）：窗口—甲子日起本旬内至卯日；主坐标—卯日（卯冲酉金，静而旺之用神逢冲则动身归至）。妻财亥水四爻旬空、子水初爻动而化丑土，途中耗费之象只调量级（归途有小耗），不改归断。置信：中高。",
 basis="tradition：liuyao（输入卡 tradition 字段照读）。\nsystems_used：六爻纳甲单用。盘面：酉月、甲子旬甲子日，戌亥空。泽天夬（坤宫）之泽风大过，动爻：初妻财子水→兄弟丑土。\n对象对齐：所问对象=占者之子（行人）；用神=五爻子孙酉金（世）；应验对象=子本人，同一。行人类主语复述：归否/归期主语均为「子」，已逐名对回。\n用神枚举：子孙现卦唯一（酉金；三爻化出？变爻丑土为兄弟，非子孙）。旺衰：酉金临月建旺、日辰子水泄之（金生水，爻泄于日，量级小疵）。原神妻财水：亥空、子水动化丑土（水入土墓/化兄弟劫财之亲）—归途耗费面。忌神官鬼寅木应爻：酉月绝、静。动化方向：子水→丑土：水入墓化兄弟，非用神动化，只调量级。类别条件读法（行人）：用神静而旺—按行人门静旺逢冲而归读，不涉化退化进。四路：本气+／元忌仇0（原神弱、忌神绝静）／动化0／世应计（a类？代占行人以用神为主、世即用神，应鬼绝不克，作同向佐证不计符）→ 归向。终局反转扫查：三类俱无，维持。\n应期三步：日档（近归，行人门远应月近应日—本题问何日归、日档）；三路—冲实（卯冲酉）取、逢值（酉日）舍（静旺逢冲先动、逢值主仍在位待归，与「归至」终局取冲为动身坐标）、填实（用神不空无候选；亥空为原神非用神，不混）。门类对表：行人门—用神状态对位：静旺者不在表列伏/动/化退三首选内，次选三合冲开/入墓/动空均不合，明写对表无正点，按三步原序取逢冲。R61-REV1-2 复推：初推逢冲卯日；复推逢值酉日—裁决：行人静旺以冲为动身之机（机制占优），保留卯日，酉日留痕。R61-REV1-4：耗费断项指针1条（财化墓）已降为「小耗」倾向表述。",
 confidence=0.64, trigger=T(reason="changed_main=false：用神子孙酉金静爻持世未动；reserve_used=false：用神现卦定主；disputed=false：合参归向明确，无存疑。"))

P["YM-013"] = dict(
 prediction_text="方向：妻病重、难愈（negative）——艮宫山天大畜之风天小畜：用神妻财子水两现，取动者五爻子水（应）发动，午月水囚、日辰巳火不生反耗，动而化父母巳火（仇神之亲、临日旺），用神化向生忌之源、自身无力；原神子孙金全卦不现（变爻亦无），医药之源缺位；病之官鬼寅木两现而休。近段病势沉重，远段无源续救——一段终局加重，远段无独立转机可报（原神缺位为据）。危重转折应期（日档，双层）：窗口—己巳日起本旬内；主坐标—午日（午冲子水，弱用神逢冲之日）。置信：中。",
 basis="tradition：liuyao（输入卡 tradition 字段照读）。\nsystems_used：六爻纳甲单用。盘面：午月、甲子旬己巳日，戌亥空。山天大畜（艮宫）之风天小畜，动爻：五妻财子水（应）→父母巳火。\n对象对齐：所问对象=占者之妻（病者）；用神=五爻妻财子水（动）；应验对象=妻本人，同一。病占主语复述：病势/危期主语均为「妻」，逐名对回无误。\n用神枚举：妻财两现（五爻动、初爻静）—两现裁决：取动者为主用神（标记互比：动者优先，承枚举节第4步），初爻子水静者记旁参（同囚于午月）。旺衰：子水午月囚、日巳火（水克火为爻克日、不得日扶）。原神子孙金：现卦无、变爻无、日月非金亲（午/巳火）→ 缺位（按枚举：日月皆非才寻伏，而子孙属「原神」非用神本身，不入伏神取用——原神缺位照实记，不臆补）。忌神兄弟土：戌空、辰静，克力未发（量级缓冲）。官鬼寅木（病）：上爻与二爻世两现，午月休、日巳泄。动化方向：子水→巳火：水克火，化出者为父母（火）—父母于艮宫为生兄弟忌神之仇神，化神临日建旺；定性：用神动化仇神、非吉向四类。反转条件：化退/化绝—子化巳非退非绝，不成立；源绝子链—原神本缺位（非化绝链），不套用，只记「无源」。四路：本气−／元忌仇−（无源、忌虽静而化神生忌）／动化−／世应不计（代占）→ 败向。决策序第7步断死三类核：用神囚无气（近之）、日月克泄无救（月囚日耗、原神缺）、化仇神——三类大半成立而忌神未发、官鬼休，量级止于「重、难愈」，不直断必死（留痕分清）。病位：官鬼寅木居上爻/二爻分指头/腿两处、木主肝胆——两路分指无交集，按病位门槛不落病位，只断病势（明写）。原神存续：缺位，无从判有根，远段无续救之据（通则(i)：远段无据已明言理由，不虚构转折）。\n应期三步：日档（近病危重）；三路—冲实（午冲子）取（与危局自洽：冲弱用神为危期）、填实（子日值用）舍（值日属来旬、且与危向不合）、逢值（巳日化神临日）舍（化神值日主化势成、非危期正点，作旁证）。门类对表：疾病门—旺相者冲去克神为愈期等条以用神旺为前提，本盘用神囚，不合首选各条，明写对表无正点，按三步取与终局自洽之冲。R61-REV1-2 复推：初推逢冲午日；复推填实子日—尺度同日档、方向相反（危/愈），按终局自洽原则午日占优保留，子日留痕。R61-REV1-4：病位断项已删（不适用粒度降档冒充）。",
 confidence=0.6, trigger=T(cm=True, reason="changed_main=true：主用神妻财子水（两现取动者）本身为五爻动爻、动而化父母巳火，主动化参与主断定性；reserve_used=false：用神现卦两现内定主，未用伏神等备用路径；disputed=false：两现取动依枚举节明序、非存疑，合参方向一致。"))

P["YM-014"] = dict(
 prediction_text="方向：有火灾之虞、患在小火惊扰而非焚宅（negative，量级小）——乾宫乾为天（六冲）之风天小畜：火患之神官鬼午火居四爻，临日辰戊午发动、又得未月合（午未合），火神临日月而动，宅中火警之机已动；然官鬼化父母未土，火势泄入宅土、患有所归；宅之用神父母戌土居上爻持世，未月土旺，宅本有气、子孙子水虽空（解神弱）而世旺可支。断：旬内有小火/火警虚惊之应，不至大焚。应期（日档，双层）：窗口—戊午日起三日内；主坐标—午日（占日当日，官鬼临日发动、火机最显之日）。置信：中。",
 basis="tradition：liuyao（输入卡 tradition 字段照读）。\nsystems_used：六爻纳甲单用。盘面：未月、甲寅旬戊午日，子丑空。乾为天（乾宫）之风天小畜，动爻：四官鬼午火→父母未土。\n对象对齐：所问对象=占者家宅；用神双面分判—宅体取父母戌土（世），火患取官鬼午火；应验对象=家宅本身（非人对象，照实落宅不回收到人），同一。家宅门（L1-76 内外分宅人）：四爻属外卦门户之位，火发于外卦近门户/灶位方向，只作方位旁注（指针1条，降为方向表述）。\n旺衰：父母戌土未月旺（世旺宅固）；官鬼午火未月休而临日建、月合（午未六合）—火神得日月之气而动，患机成立。子孙子水（制鬼解患）初爻：未月死+甲寅旬空—真空倾向（死、空、无生扶三项近齐），解神无力，量级上调一档（由虚惊升至小火），然世旺与化土泄火两路压回，不至大焚——压制/缓冲依据均已写明。动化方向：午火→未土：火生土，化出父母（宅体之亲），火势归宅土而泄，定性为患有出路、非化进非化绝。反转条件：不成立。四路（以宅安为终局）：本气+（父母旺）／元忌仇−（官鬼临日动、解神空死）／动化+（火化父母泄）／世应不计→ 合参：患动而宅固，终局按通则(l)单判为「有患（negative）而量级小」。终局反转扫查：三类俱无全成立（无伏、官鬼非用神化进链、源绝不涉），维持。\n应期三步：日档（火患近事）；三路—逢值（午日临日）取、冲实（子冲午：子落旬空，冲神无力）舍、填实（未日化神值）舍（未日主患息之期、非患发坐标，作次应留痕）。门类对表：家宅/火灾不在对表门类，明写无此门类。R61-REV1-2 复推：初推逢值午日；复推化神逢值未日（患息向）—问患发取午、问患息取未，所问为「火灾之虞」即患之有无与发时，午日占优保留，未日留痕为患息参考。R61-REV1-4：方位断项指针1条已降为方向旁注。",
 confidence=0.6, trigger=T(reason="changed_main=false：主用神父母戌土为静爻持世（动者官鬼为患神、非宅体用神本身）；reserve_used=false：用神现卦定主；disputed=false：双面取用依家宅门分判明确，合参已定量级，无存疑。"))

P["YM-015"] = dict(
 prediction_text="方向：功名可成、乡举可中（positive）——乾宫山地剥之火地晋：父母为功名文书之用神，两现取动者四爻戌土，巳月得火生而相、复临日辰甲戌（临日建），文书有力；原神官鬼巳火居二爻应位，临月建而旺，生父母之源鼎盛；父母动而化兄弟酉金（子孙之亲），酉金落甲戌旬空，剥官之化神落空无力，不碍成名，只主名次稍逊/榜尾之量级。应期（月档，双层）：窗口—巳月之后至酉月（秋闱放榜之窗）；主坐标—酉月（化神酉金填实之月、乡试放榜之期）。置信：中高。",
 basis="tradition：liuyao（输入卡 tradition 字段照读）。\nsystems_used：六爻纳甲单用。盘面：壬午年巳月、甲戌旬甲戌日，申酉空。山地剥（乾宫）之火地晋，动爻：四父母戌土→兄弟酉金。\n对象对齐：所问对象=占功名者本人；用神=四爻父母戌土（功名门以父母为用神，承对表功名门）；应验对象=本人功名，同一。\n用神枚举：父母两现（四爻动、初爻未土静）—取动者定主，初爻未土旁参。旺衰：戌土巳月相（火生土）、临日建 → 旺相有气。原神官鬼巳火：临月建旺、生父母。忌神妻财木：寅卯两现，巳月休、静。世爻子孙子水五爻：巳月囚、静（子孙持世—对表次选「子孙持世取值子孙之日」为日档次选，与月档尺度不合，舍并留痕）。动化方向：戌土→酉金：土生金，化出子孙之亲（于乾宫酉金为兄弟？乾宫金：酉金为兄弟——卡面化神标注兄弟酉金，从卡面：化兄弟。兄弟于功名主竞争/劫夺之亲）—化神旬空：化出无力，定性只调量级（竞争者落空反利己）。反转条件：不成立。四路：本气+／元忌仇+／动化0（化空之兄弟不克用、只调量级）／世应不计→ 成向。终局反转扫查：化进待冲—非化进；余无 → 维持。\n应期三步：尺度月档（乡举榜期、(k)以月/年）；三路—填实（酉月实空化神）取、冲实（辰冲戌用神）舍（冲用神主文书动荡、与成局不合）、逢值（戌月值父母）舍（戌月迟于秋闱试期、尺度内次选）。门类对表：功名发案门—父母动者首选「逢值逢合之日」，属日档取法；本问尺度定月档（问乡举之期、年内事），对表日点不入月档主坐标，明写对表首选尺度不合、递补填实路（化神空待实），理由如上。R61-REV1-2 复推：初推填实酉月；复推逢值戌月—异点裁决：试期在秋（酉月为秋闱放榜之天然视野，天然视野项酉胜），且化神待实闸门以填实为释，酉月占优保留，戌月留痕。R61-REV1-4：名次量级已降为「榜尾之量级」倾向表述（指针：化神空1条）。",
 confidence=0.63, trigger=T(cm=True, reason="changed_main=true：主用神父母戌土本身为四爻动爻、动而化兄弟酉金，主动化参与量级定性；reserve_used=false：用神现卦两现内取动定主，未用备用路径；disputed=false：两现取动依明序，合参成向一致，无存疑。"))

P["YM-017"] = dict(
 prediction_text="方向：友可遇（positive）——乾宫天山遁之水泽节（六合）：访友以应爻为友，五爻兄弟申金居应、为五动中之独静一爻（独静定应期）：申金未月得土生而相，友人有着落；独静之应逢值逢冲则遇。余爻五动主行程多扰（父母、官鬼交动，途有迁延），只调迟速不改可遇。应期（日档，双层）：窗口—丙午日起本旬内；主坐标—申日（独静应爻逢值之日）。置信：中。",
 basis="tradition：liuyao（输入卡 tradition 字段照读）。\nsystems_used：六爻纳甲单用。盘面：未月、甲辰旬丙午日，寅卯空。天山遁（乾宫）之水泽节，动爻五：初父母辰土→官鬼巳火、二官鬼午火（世）→妻财卯木（空）、三兄弟申金→父母丑土、四官鬼午火→兄弟申金、上父母戌土→子孙子水；独静：五兄弟申金（应）。\n对象对齐：所问对象=所访之友；用神=五爻兄弟申金（应爻，访友以应为对方）；应验对象=友本人，同一。\n用神枚举：兄弟两现（三爻动、五爻静）—访友取应位之五爻为主用神（对象定位优先于动静互比，留痕），三爻动兄弟作行程旁参。旺衰：申金未月相（土生金）、日午火克之（火克金，日克量级）→ 有气受压。独发独静（L1-15）：独静只定应期、不定吉凶主轴—主轴仍从用神旺衰与世应：世官鬼午火动化卯木财（空），寻访之心动而化空，主途中有虚耗；应静而相，友在可寻。四路：本气0偏+／元忌仇0（原神父母土多动生应+、忌神官鬼火多动克应−，两抵）／动化0（用神静）／世应计（a）—应静世动：我往就人、友待我至，作可遇之佐证（+量级）→ 可遇向。终局反转扫查：乱动卦取用已按对象定位定主；三类信号无全成立者（伏无、化进不涉用神、源绝不涉），维持。\n应期三步：日档（访友近事、问何日遇）；三路—逢值（申日）取、冲实（寅冲申：寅落甲辰旬空，冲神本身旬空、冲而无力且期在值后）舍、填实（用神不空无候选明写）。门类对表：访友不在对表门类，明写无此门类。R61-REV1-2 复推：初推逢值申日；复推逢冲寅日—闸门核：用神无空墓闸门，逢冲之支自落旬空为虚冲，逢值占优保留，寅日留痕。R61-REV1-4：无其他具体断项。",
 confidence=0.6, trigger=T(reason="changed_main=false：主用神兄弟申金（应爻）为独静之静爻，未动；reserve_used=false：用神现卦应位定主；disputed=false：兄弟两现已按对象定位（应位优先）明序取舍，非存疑。"))

P["YM-018"] = dict(
 prediction_text="方向：子将归（positive）——艮宫火泽睽之泽山咸：五爻乱动中四爻子孙酉金持世独静（独静定应期），用神即归人之象；酉金巳月死气、赖日辰丑土生金，弱而有生，人在途有归意；五爻兄弟未土动化子孙酉金、三爻兄弟丑土动化子孙申金，子孙之象两番化出，归信叠见。应期（日档，双层）：窗口—乙丑日起六日内；主坐标—卯日（卯冲酉金，独静之用神逢冲则动身归至之日）。置信：中低（用神月死，量级压至「归而迟速一般」，不作速归断）。",
 basis="tradition：liuyao（输入卡 tradition 字段照读）。\nsystems_used：六爻纳甲单用。盘面：巳月、甲子旬乙丑日，戌亥空。火泽睽（艮宫）之泽山咸，动爻五：初父母巳火（应）→兄弟未土、二官鬼卯木→父母午火、三兄弟丑土→子孙申金、五兄弟未土→子孙酉金、上父母巳火→兄弟未土；独静：四子孙酉金（世）。\n对象对齐：所问对象=占者之子（行人）；用神=四爻子孙酉金（世）；应验对象=子本人，同一。行人类主语复述：归否/归期主语均为「子」，逐名对回。\n用神枚举：子孙现卦以四爻世为定主；变爻同亲两现（申金、酉金化出）记应验位旁参（归信叠见之据）。旺衰：酉金巳月死、日丑土生 → 死而有生，弱。原神妻财水全卦不现（变爻亦无）—源缺，量级压制。忌神父母火：巳火两现动、化兄弟—父母动主音信/阻隔交杂。类别条件读法（行人）：用神独静—静者待冲值而动身；化出子孙两处按行人门作「归象化出」旁证，不作化进定性（用神本身未动）。四路：本气0偏−（死有生）／元忌仇0（源缺−、忌动化兄不直克+）／动化0（用神静）／世应不计→ 方向存疑边缘：以独静待应+归象化出两据合成「将归」弱positive（量级与置信已压）。终局反转扫查：三类俱无全成立，维持弱判。\n应期三步：日档（近归）；三路—冲实（卯冲酉）取、逢值（酉日）舍（独静以冲为动身之机先于逢值，酉日作归至后备留痕）、填实（用神不空无候选明写）。门类对表：行人门—用神静者对表无直列，伏/动/化退首选均不合，明写无正点，按独静通法取逢冲。R61-REV1-2 复推：初推逢冲卯日；复推逢值酉日—裁决：独静闸门为「静」，冲正释静、值不释静，卯日占优保留，酉日留痕。R61-REV1-4：无其他具体断项。",
 confidence=0.57, trigger=T(reason="changed_main=false：主用神子孙酉金为独静静爻，未动（化出子孙为旁爻所化、非用神主动）；reserve_used=false：用神现卦持世定主，变爻同亲仅作应验位旁参；disputed=false：方向虽弱而由独静通法与归象化出两据合成，非取用存疑（弱判已以置信0.57标明）。"))

# ---------------- main ----------------
def main():
    batches = json.loads((ROOT / "batches.json").read_text(encoding="utf-8"))
    want = []
    for k in ("B19", "B20", "B21"):
        want += batches[k]
    assert len(want) == 60, len(want)
    assert set(P.keys()) == set(want), (set(want) ^ set(P.keys()))
    assert len(P) == 60
    sizes = {}
    for cid in want:
        rec = P[cid]
        obj = {"case_id": cid, "prediction_text": rec["prediction_text"], "basis": rec["basis"],
               "confidence": rec["confidence"], "trigger": rec["trigger"]}
        assert 0.0 <= obj["confidence"] <= 1.0
        t = obj["trigger"]
        assert set(t.keys()) == {"changed_main", "reserve_used", "disputed", "reason"}
        txt = json.dumps(obj, ensure_ascii=False, indent=1)
        p = OUT / f"{cid}.json"
        p.write_text(txt + "\n", encoding="utf-8")
        sizes[cid] = p.stat().st_size
    cm = sum(1 for c in want if P[c]["trigger"]["changed_main"])
    ru = sum(1 for c in want if P[c]["trigger"]["reserve_used"])
    di = sum(1 for c in want if P[c]["trigger"]["disputed"])
    print(f"WROTE {len(sizes)} files; trigger true counts: changed_main={cm} reserve_used={ru} disputed={di}")
    for cid in want:
        print(cid, sizes[cid])

if __name__ == "__main__":
    main()
