# -*- coding: utf-8 -*-
"""R61 S7 seat: batches B19/B20/B21 predictions. Usage: python3 gen_r61_s7.py B19"""
import json, os, sys

OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round61/predictions"
os.makedirs(OUT, exist_ok=True)

def T():
    return {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}

PRED = {}

# ---------------- B19 ----------------
PRED["MP-017"] = {
 "prediction_text": "断：下届香港行政长官由女性出任。2017年3月26日选举委员会投票，胜出者为女性候选人。置信中上：题面时点（2016年12月）女性一方林郑月娥已改口表示重新考虑参选，其出身政务司司长、为现任体制内最顺位之人；男性一方曾俊华虽已辞职备选，然特首人选须中央信任，女性候选人得此之势更顺。应期定点：以月为单位，2017年3月投票日见分晓（依据：题面已给选举日期，应期不出题面尺度）。",
 "basis": "tradition=现代事件占断（据题面体裁自决：新闻受访即断，无卦盘、无生庚，归事件吉凶占）\nsystems_used: 梅花事实优先序（通则e）＋局势取象\n题面已载面：主问面＝下届特首性别；事件面＝梁振英不连任、曾俊华辞职备选、林郑改口考虑参选；关系面＝特首须获中央信任（体制事实）。无起卦数据、无生辰，不臆造盘面；以题面事实收束：女性候选人顺位与得势皆占先。锚点核：题面无文字/数字锚点可作取象，转应核不适用。",
 "confidence": 0.6, "trigger": T()}

PRED["MP-018"] = {
 "prediction_text": "断：曾俊华不能当选2017年香港行政长官，终局落败。方向：败选（单一终局，不取两可）。其民望虽为候选人中最高，然选举由1,194人选举委员会投票、北京支持所在决定成败，题面已明传媒普遍指林郑月娥获北京支持而占优、曾氏被视为陪跑——民望不能抵选委会结构之势。应期定点：月尺度，2017年3月26日投票日落败见分晓（依据：题面选举日期）。等级：非险败惜败，而是结构性落后，票数差距料明显。",
 "basis": "tradition=现代事件占断（据题面体裁自决：杂志面相分析类选题，卡内无面相材料、无生辰全息，仅以所问事件占断）\nsystems_used: 事件占断·事实优先序（通则e）\n题面已载面：主问面＝曾俊华能否当选；事实面＝民望最高、林郑获北京支持占优、曾被视为陪跑。卡内未给面相/掌纹任何材料，面相一路无据不报（有面无据不报）；仅以事件面收束，民望与选委会结构两面相较，结构面为决定面。锚点核：无文字/数字锚点，转应核不适用。",
 "confidence": 0.75, "trigger": T()}

PRED["MP-019"] = {
 "prediction_text": "断：2017年香港行政长官选举由林郑月娥胜出当选。方向单一终局：林郑月娥得票过半当选，曾俊华居次、胡国兴居末。依据之势：三人中唯林郑获北京支持且为现任政务司司长顺位，选委会结构下其票源最实；曾俊华民望高而票源虚，胡国兴更无票源基础。应期定点：月尺度，2017年3月26日投票当日见分晓（题面已给投票日）。生肖辅象：林郑与胡同为酉年，酉金值2017丁酉流年之旺，然胡无票源之实，金旺之象归于有实势之林郑（1957年酉年生一方），不归胡。",
 "basis": "tradition=现代事件占断（据题面体裁自决：风水杂志选举预测，无卦盘，归事件占断兼生肖取象）\nsystems_used: 事件占断·事实优先序（通则e）＋生肖流年取象（辅）\n题面已载面：主问面＝选举花落谁家；人物面＝林郑（酉年）、曾俊华（卯年）、胡国兴（酉年）三人年庚已载；事实面＝提名辩论已毕、3月26日投票。取舍：生肖象只作辅证，主断由票源结构面定；胡国兴同为酉年而无票源，锚点（酉）之转应面已列——取直读归林郑，理由为票源实势在林郑一方。无卦盘可起，不臆造盘面。",
 "confidence": 0.7, "trigger": T()}

PRED["OC-001"] = {
 "prediction_text": "断：戊土日主生辰月当令，申子水财成势、年干甲杀透出，身旺任财杀——一生掌兵权、据方面之贵格，然杀虚财盛，贵在权势而不在久位。事业：早年甲戌、乙亥运官杀之地崭露于军旅；中年壬申、癸酉运（约四十至六十岁段）食伤生财、财旺任之，为一生高峰运段，位至方面军总司令、主政华北之级。晚年：下野之后运入乙亥、丙子之交，水财愈旺而杀印无力扶持，名位不保、寓居终老，终局为落拓善终之局，非刑夭，寿约六旬中段（六十五岁前后，运档坐标，定值档：终局在乙亥运内）。破耗之因：财旺生杀而杀无根，权位随财势聚散，兵败下野即财去权空。子女：时柱壬子财旺，子女宫坐财，子女有出息而缘分聚少离多。",
 "basis": "tradition=八字（子平，四柱已给：甲戌 戊辰 戊申 壬子）\nsystems_used: 八字（调候先行、格局定体、旺衰定量；特格扫描：从格未命中——戊土辰月得令有根，不从；专旺未命中——财杀透干；寒燥极端未命中）\n主线：戊土辰月建旺、申子半合水局财成势，甲杀透而无寅卯强根；格局量级区间：下限方面军级将领（依据：身旺任财杀、财局成势）—上限主政一方之军政首脑（依据：杀透年干、财旺生杀，然杀无根不至极品）。病药链：病＝甲杀虚浮无根（年干七杀，病型为用神无力非破格）；药＝壬子财势与申金食神之流通（食神生财、财生杀成链，得力）；扶抑取向＝身旺不扶，顺财杀流通之势。峰值运三核对：壬申运①申为财源食神得地②壬财透干呼应③否决三条逐项核查：(i)合绊用神之干未命中(ii)冲克用神之根未命中(iii)透忌神且通根未命中，满足3项为峰值；癸酉运同理满足2项为次峰。应期三步：尺度定运/年档（一生之问）；运年触发路取壬申癸酉，合冲引动路无更强候选（戌运冲辰为动荡非高峰），值年路从略并注明舍弃：值年只定年内触发、不定运段高峰。",
 "confidence": 0.6, "trigger": T()}

PRED["OC-002"] = {
 "prediction_text": "断：庚金日主坐申强根，亥月伤官当令，乙木正财透月与日干相合，己印透时——伤官生财、财印并见之清贵格。一生贵显量级：财政金融之最高长官级（财政部长至行政院长级，格局依据：伤官生财成链、印透护身、财官有源）。行运：少年丙子、丁丑运学业仕进；中年戊寅、己卯运（约三十五至五十五岁段）印财相济、寅亥合木财旺，为一生高峰运段，执掌全国财政；晚年庚辰、辛巳运金扶身根，退居而名望财力不衰，移居海外终老，寿高至七旬末（运档坐标，窗口档：终局在辛巳运前后）。破耗之因：乙庚合财、财印时有相战，中年有因财政去职之起伏而无伤根本。婚姻：乙财为妻星合身，妻贤内助；子女：时己印，子女宫平，子息有成。",
 "basis": "tradition=八字（子平，四柱已给：甲午 乙亥 庚申 己卯）\nsystems_used: 八字（格局：伤官生财；特格扫描三类均未命中，走常规旺衰调候；亥月金水寒，午火调候为辅）\n主线：庚金得申禄根、己印生身，身可任财；乙财透而合身、亥伤生财成链，格成。格局量级区间：下限财政要津长官（依据：财印两透、身有禄根）—上限行政院长级（依据：伤官生财成链有源有流，官星藏午不透，上限止于财权之极而非君权）。病药链：病＝己印坐卯受财克、财印轻战（月时之间，病型壅塞，病而有制——申金为庚根不伤）；药＝申禄根与亥水流通（财伤相生不滞）；扶抑取向＝身中和偏强，不重扶抑，顺伤官生财之链。峰值运三核对：戊寅运①寅中丙火调候、亥合财旺（用神财得地）②戊印透干扶身护格③否决三条：(i)未命中(ii)寅申冲日支禄根——命中(ii)之虞，然冲禄同时合亥生财，作用表两读：冲根为逆、合财为顺，以财链完整度胜出定峰但降一档置信；己卯运满足2项为次峰。应期：运/年档，高峰坐标戊寅己卯运（定值），终局坐标辛巳运前后（窗口，理由：起运岁数卡内未给，流年层不定）。",
 "confidence": 0.62, "trigger": T()}

PRED["OC-003"] = {
 "prediction_text": "断：庚金日主生午月，丙丁官杀两透、两午杀旺，己印坐卯无根——杀重身轻、无根之金受火炼，原局为先难之格，贵气全看运来扶身化杀。一生走势先抑后扬：早年乙巳、甲辰运财杀交攻，艰辛谋生；约四十岁后入辛丑运（金库印地，身得扶、杀印相生）事业奠基发迹；庚子运比劫助身、子冲午杀解其攻身，名位与财富俱进，为一生高峰运段（约五十至七十岁段），成上海商界领袖而兼政界名望（格局依据：杀印相生得运扶成格，上限商界领袖＋政府委员级名望，非实权极品）。晚年己亥运印透，亥卯半合财来，守成终老，寿近八旬（运档坐标，窗口档）。破耗之因：早年财杀攻身之运破耗于合伙与时局，中年后无大破。子女：时己印坐卯，子息缘平、晚年有靠。",
 "basis": "tradition=八字（子平，四柱已给：丁卯 丙午 庚午 己卯）\nsystems_used: 八字（格局：杀旺身弱待印化；特格扫描：从官杀格未命中——己印虽弱仍透、庚金有午中丁炼而日主坐午无根细核：判据②外③流通之护弱，印存一线不作从格，定正格身弱；燥热极未命中——巳午未夏令不全、无火局）\n主线：官杀两透两午当权，印星己土坐卯被财克、无根，格破待救，救在运。格局量级区间：下限殷实商人（依据：财星两卯有源）—上限商界领袖兼政名（依据：杀印相生须运扶方成，原局无根故上限不至实权高位）。病药链：病＝丙丁午火官杀太过（月干丙、时？年干丁、两午，病型太过，党众火旺）；药＝己印化杀（时干己土，虚浮无根、药无力，原局内药弱）＋运来金土扶身为外药；扶抑取向＝扶身化杀为先，财运在身扶之前只作耗克论（BZ-FY-2.3 承载门槛：原局判不任）。峰值运三核对：庚子运①庚比透、子为庚沐浴非禄根，用神印在丑运已过，庚子以助身解冲论满足2项②庚干助身呼应③否决三条：(i)未命中(ii)子午冲为冲杀非冲用神之根，未命中(iii)未命中——定峰值；辛丑运满足2项（印得丑库、身入库地）为次峰兼奠基运。应期：运/年档，高峰庚子运（定值），终局己亥运前后（窗口，起运岁数未给）。",
 "confidence": 0.58, "trigger": T()}

PRED["OC-004"] = {
 "prediction_text": "断：乙木日主生卯月建禄，癸印两见（月干癸、时支子），丙伤官透时泄秀——禄印旺而官星全缺之格。仕途形态：以才学文章立身、外交使节见长，官运须待运来官星方显。行运：壬寅、辛丑运（约二十至四十岁）印比扶身、学业仕进；庚子运（约四十至五十岁段）庚正官透、子印相随，官印相生，为一生高峰运段，位至外交总长、一度组阁之级（格局依据：原局无官，上限由运补官印相生而定，止于使节内阁级，不至久掌大权）；己亥运财印相见，渐退；戊戌运财旺克印耗身，晚景转平；丁酉、丙申运（七十岁后）金旺克禄，老身难任，终局在此运内，寿约七十三岁前后（运档坐标，窗口档）。破耗之因：财运克印，因家产文书之事耗损而无大破。婚姻：妻宫巳火伤官，妻能干而夫妇偶有意气之争；子女：时丙伤，子息聪慧。",
 "basis": "tradition=八字（子平，四柱已给：丁丑 癸卯 乙巳 丙子）\nsystems_used: 八字（格局：建禄配印、伤官泄秀；特格扫描：专旺曲直未命中——子水印透、巳火泄气不纯；从格未命中，身禄旺自立）\n主线：禄印两旺身强，官星全无为格之缺，丙伤泄秀为用之出路。格局量级区间：下限清贵文职（依据：印禄旺、伤官秀气）—上限外交总长级（依据：须运补官星方成官印相生，原局无官故不至极品久位）。病药链：病＝无官星之缺与巳子水火相见之轻战（病型为缺位，病轻）；药＝运来庚官（外药），原局癸子印为化杀生身之备（得力）；扶抑取向＝身旺喜泄喜官，不喜再扶。峰值运三核对：庚子运①庚官得？子印得地（相神印通根子水）②庚干正官透出呼应官印相生③否决三条：(i)庚与乙日干相合——本身之合（B1-53④日干合用神为我合之，不作合去），未命中(ii)子水不冲用神之根，未命中(iii)未命中，满足3项定峰值；辛丑运满足2项次峰。应期：运/年档，高峰庚子运（定值），终局丁酉丙申运间（窗口）。",
 "confidence": 0.6, "trigger": T()}

PRED["OC-005"] = {
 "prediction_text": "断：乙木日主生卯月得禄，年时两卯、未土归库，身旺极；丁食神透月泄秀，己偏财两透——食神生财、秀气发越之格，官星全无，贵在名望学问而不以权位称。一生：丙寅、乙丑运（约十至三十岁）比印之地，学业大成、留洋成名；甲子、癸亥运（约三十至五十岁段）印旺水生，身旺任事，司法与学界声望达高峰（曾任法院院长级），为一生峰值运段；壬戌运戌未刑动，职务迁转、驻外使节；晚年辛酉、庚申运官杀金至，身旺能任杀，酉冲卯禄主迁动而不伤根本，退而不休、清望终老，寿高至八旬末（运档坐标，窗口档：终局庚申运内）。破耗之因：比劫两卯旺，财星己土受克，中年有合伙分财之耗，量级有限。婚姻：妻宫未土正财，妻贤而聚少离多（卯未合）；子女：时己财坐卯，子女宫财旺，子息有成而各一方。",
 "basis": "tradition=八字（子平，四柱已给：己亥 丁卯 乙未 己卯）\nsystems_used: 八字（格局：食神生财；特格扫描：曲直专旺未命中——丁食透泄、己财两透，气不纯专；从格未命中）\n主线：身旺禄重，丁食泄秀生己财，格成而清；无官为形态之限（贵在名望）。格局量级区间：下限学界名宿（依据：食神秀气、印亥护身）—上限司法首长级名望（依据：无官星透干，权位上限不及部院实权之极）。病药链：病＝比劫两卯争财之壅（病型太过之轻症，卯禄党众）；药＝丁食神泄比生财成流通链（月干丁火，得卯木生，得力）；扶抑取向＝顺食伤生财之链，不扶身。峰值运三核对：癸亥运①亥印得地生身、亥卯未三合木局身势成②癸印透干呼应③否决三条逐项：(i)未命中(ii)未命中(iii)未命中，满足3项峰值；甲子运满足2项次峰。应期：运/年档，峰值癸亥运（定值），终局庚申运内（窗口，起运未给不落流年）。",
 "confidence": 0.6, "trigger": T()}

PRED["OC-006"] = {
 "prediction_text": "断：问约1935年事业受挫、往后走势——终局不利，难复旧观，且须防运内终局之变。戊土日主生申月，庚食神透、癸财透年，食神生财本为富格；然当前所行甲寅大运（约六十二至七十二岁段）：甲七杀透干坐寅禄，杀旺攻身，寅申冲去月提食神——财源之食神被冲、杀来无制，事业受挫正应此运。往后数年：寅运之内收缩守成可保残局，然杀势逐年加深，至戊寅年（1938）寅杀伏吟运支、再冲申提，为全运最险之年，事业与健康同见终局关口；即便挨过，亦只余癸丑运（七十二岁后）财库守成，无力重整旧业。应期：年尺度（问近段走势），窗口为甲寅运余段，主坐标1938戊寅年（定值档：寅运伏吟流年、冲提纲，三路中合冲引动一路独强）。破耗之因：杀运攻身、食神被冲，因时局与债务压力耗尽企业元气。",
 "basis": "tradition=八字（子平，四柱已给：癸酉 庚申 戊午 甲寅；问时约1935年乙亥）\nsystems_used: 八字（格局：食神生财；当前运转折判定＋双向对决；特格扫描未命中）\n主线：申月食神当令生癸财，午印护身，身可自立，格成于食神生财；病在时柱甲寅杀坐禄（潜在），运逢即发。病药链：病＝甲寅七杀（时柱，病型太过之潜伏，寅为杀禄、党于运年）；药＝庚申食神制杀生财（月柱，得力，然运支寅冲申则药伤）；扶抑取向＝制杀护食为要。转折运甲寅双向对决：高峰栏——甲寅运干甲杀无财生、寅中丙印可化杀一线（弱）；低谷栏——运干甲杀透攻身（直指病字成势）、运支寅冲月支申（药被冲伤，结果食神失位），证据链完整且直指病药，低谷栏胜出定逆向。应期三步：尺度年档（问当前受挫后走势，阶段之事）；三路：运年触发路甲寅运已定方向，合冲引动路取1938戊寅年（伏吟＋冲提），值年路无喜用值年可取（癸财值年只主财耗）舍弃并注明。终局两运：甲寅运逆主线已定，癸丑运独立判定为平（丑为财库湿土，守成），不翻贵（承定性：富格而非贵格，晚景守成上限）。",
 "confidence": 0.55, "trigger": T()}

PRED["OC-007"] = {
 "prediction_text": "断：据造验性情、际遇与寿数。甲木日主生申月七杀当令，庚杀透年、三甲比肩并透、年支寅禄被申冲——杀旺比众之造。性情：比肩三透主自负不羁、意气凌人，杀旺压之则郁而狂放，申中壬印暗生主文才敏捷——狂士才子之性，诗酒风流、不受绳墨。际遇：出身显宦（年柱杀印之势、父位显赫），然寅申冲禄、比劫争财（财星仅戌中丁火微藏），一生于权位之外放浪，财来财去、挥霍散尽，名高而实职无成；中年丁亥运（约三十二至四十二岁段）丁伤官直克庚杀，伤官见杀、心志与时局交困，亥水印来本可化杀，惜运末辛未年（1931）未土培杀之根、伤官气衰——寿数止于此运之末，四十二岁前后终局（运档＋流年两层坐标，定值档：丁亥运末、辛未年）。子女：时甲戌，比肩坐子女宫，子息缘薄。",
 "basis": "tradition=八字（子平，四柱已给：庚寅 甲申 甲申 甲戌；占时1931年命主新逝，属验推回溯）\nsystems_used: 八字（格局：杀旺比帮；性情断法B1-51以四柱配合断；回溯应期先运后年，合通则a回溯序）\n主线：申月杀令、两申党杀，寅禄一根被两申冲，根动而不拔；比肩三透为抗杀之党，格成杀比相峙、无财印通关成局。格局量级区间：下限名士（依据：印藏申中、甲木秀气）—上限止于家世之荫与文名（依据：财弱官杀无制成格，不至自致高位）。病药链：病＝庚申七杀太过（年干庚、两申，病型太过，党众）；药＝戌中丁火伤官（藏而微弱、药无力）与申中壬印（暗藏，得力有限）；扶抑取向＝比帮抗杀为势所必然，主放浪不羁。终局定位：丁亥运伤官见杀为转折运——作用表：运干丁→病字庚杀：克（伤官制杀，过甚则心志耗）；运支亥→申杀：害而藏壬印生身（半救）；辛未流年未土生杀培根、丁火入墓，药绝，定终局年。应期：回溯先定丁亥运、再定运末辛未年，两层坐标齐，置信定值。",
 "confidence": 0.6, "trigger": T()}

PRED["OC-008"] = {
 "prediction_text": "断：乙木日主生酉月七杀当令，辛杀透月，然时支卯禄、坐下未土藏乙——杀旺而身有禄根，卯酉冲为禄杀相战之局，子水印星居年可化杀。格局主军政权位：将星当令、禄根抗杀，主握兵符、任方面。行运：壬戌、癸亥运（约十至三十岁）印运化杀生身，军旅崭露；甲子、乙丑运（约四十至六十岁段）甲乙比劫扶身任杀、子印化杀，仕途达高峰，位至省主席、军区司令级（格局依据：杀印相生＋禄根任杀，上限方面军政长官）；丙寅、丁卯运食伤泄秀、卯禄归位，晚年退居而禄根不伤，安享高寿，终局在丁卯运后段，寿约九旬（运档坐标，窗口档）。破耗之因：卯酉冲贯穿一生，权位屡有迁动、部属离合之耗，而无倾覆之破。婚姻：妻宫未土正财，妻贤内助，卯未半合夫妇和；子女：时己财坐卯，子女宫财禄相见，子息有成。",
 "basis": "tradition=八字（子平，四柱已给：戊子 辛酉 乙未 己卯；异说丙子时原书斥误、未取，已注明）\nsystems_used: 八字（格局：杀印相生兼禄根任杀；特格扫描：从官杀未命中——卯禄强根、子印化杀，自立之路通）\n主线：酉月辛杀当权，子印化杀、卯禄为根，格成于杀印禄三全，病在卯酉冲。格局量级区间：下限军职将校（依据：杀旺有制化）—上限省主席/方面司令（依据：杀印相生得禄根任之，不至中枢极品）。病药链：病＝卯酉冲（禄杀相战，病型为冲战，落月时之间）；药＝子水印星化杀生身（年支，得酉金生，源头有力）；扶抑取向＝扶身任杀、护印化杀。峰值运三核对：乙丑运①乙比透扶身、丑为印库湿土生金化杀（用神印得库）②乙干比肩呼应扶身③否决三条：(i)未命中(ii)丑未冲妻宫非用神之根，未命中(iii)未命中，满足3项峰值；甲子运子印值运满足2项次峰。应期：运/年档，峰值乙丑运（定值），终局丁卯运后段（窗口，起运未给）。",
 "confidence": 0.58, "trigger": T()}

PRED["OC-009"] = {
 "prediction_text": "断（残损降格）：本题四柱在输入卡中未实际给出（卡面仅注『原书应运篇下论造，四柱以原书为准，转录本个别字待校』），无盘可排，格局、旺衰、大运、应期一概无据，不断具体运程与等级数值。仅据题面已载事实作最低限度之断：命主为顶尖外交官、已历任驻外使节与内阁职务——以此事实面收束，倾向判断为：仕途贵显已成定局，后半生以清望与使节顾问之任延续，晚景平稳；财富随俸禄名望而厚，非商贾巨富一路；婚姻一面题面列为所问而盘面无据，明写无据不报。置信低（0.20），俟四柱补齐后须整例重断，本断不得作准据引用。",
 "basis": "tradition=八字（子平；输入残损——四柱缺失，据实注明）\nsystems_used: 八字（无盘，仅题面事实收束）\n残损说明：输入卡 birth.pillars 字段无实际干支，仅存说明文字，无法装盘、无法定格局与大运；按规矩不臆补四柱（命主生年虽或可考，亦不以外部知识拼盘）。已载面处置：主问面（财富/仕途/婚姻行运）——仕途面据题面事实（顶尖外交官、历任使节内阁）给方向级断语；财富面给形态级断语；婚姻面有面无据不报。锚点核：题面无可推演锚点，转应核不适用。confidence 因残损降至 0.20。",
 "confidence": 0.2, "trigger": T()}

PRED["OC-010"] = {
 "prediction_text": "断：壬水日主生寅月，三午丙火财星满盘、两丙透干，庚印独透而无根，日主无亥子申辰之根——财多身弱、印虚无力之造。命格形态：富贵之名极盛而自立之实全无，帝位虚拥、一生为人作嫁。际遇三起三落：幼年辛卯、壬辰运（壬辰运辰为水库、身稍得托）登大位而速退，退居尚可自保；癸巳、甲午运（约二十至四十岁段）巳午财势冲天，身弱不任，再被拥立为傀儡之君（甲午运1934年前后应期，运档＋流年坐标），乙未运未为财库、午未合财，败亡系狱之局成于此运（1945乙酉年败亡，流年坐标）；后半生丙申、丁酉运申酉金印得地扶身，归于平民安度，然丙丁财仍透，晚景仅得平顺。寿数：终局在丁酉运末至戊戌运初，约六十一岁（1967年前后，窗口档）。破耗之因：财即是祸——凡财势最旺之运皆为失位之运，财多身弱以财为病，全例应验。子女：时丙午财坐子女宫，子女缘聚散无常、晚景不赖子力。",
 "basis": "tradition=八字（子平，四柱已给：丙午 庚寅 壬午 丙午；原书未附大运表，运序按丙年男顺行自推并注明）\nsystems_used: 八字（格局：财多身弱，BZ-FY-2.2 财为病判别；特格扫描：从财格四判据核——①日主无根命中②庚印虚浮无根、扶身路断命中③财成势命中④无比劫旺动命中，从财格形式四条同具；惟从财喜官泄财护局，此造无官，从财而不见其用，定性为『从财虚势』：名从财而实无所成，运断以财势顺逆与印运扶身两路合参，此取舍已在格局定性对决中并列：正格身弱读与从财读方向同归于『财旺之运凶、印金之运平』，故锁定不碍终局）\n主线：财势独旺、日主无根、印虚，贵名与实势背离。格局量级区间：下限平民（依据：身无根、印无力）—上限虚位至尊之名（依据：财局成势拱出名位，然非实权，不以实权极品论）。病药链：病＝丙午财太过（三午两丙，病型太过，党众满盘，依 BZ-FY-2.2 命中：财当势、日主失根、财耗身无回护）；药＝庚印（年干，虚浮无根、药无力）待运申酉金地为外药；扶抑取向＝不任财，财运皆作耗克论。转折运乙未：作用表——运干乙伤官生财助病（逆）；运支未午合财、未为财库填实病字（逆），双向对决低谷栏胜出。应期：运/年档，傀儡再立取甲午运1934年（运年触发＋值年午财两路同指，定值），败亡取乙未运1945年（合冲引动：未填财库、运末势极，定值），终局窗口丁酉末—戊戌初（起运岁数未给，流年不定，窗口档）。",
 "confidence": 0.55, "trigger": T()}

PRED["OC-011"] = {
 "prediction_text": "断：据造验性情与结局。己土日主生巳月火旺土相，庚辛伤官两透，亥水正财两见，时透乙七杀。性情：伤官双透泄秀，聪明敏慧、才艺天成（演艺之资），然伤官性烈、心思敏感多虑，重情而易为情所困；巳亥冲、两亥自刑之象，主内心纠结、郁结难解。际遇：名高而谤随——伤官旺克官（官星乙木无根浮于时干），主名誉受言论所伤、婚姻情感为一生之结：乙杀为夫星无根坐亥，夫缘飘忽、情事多折且牵连名声。结局：寿数短促。行运逆行：约十五岁后入己卯运，卯亥半合、乙杀得地，杀来攻身而伤官与之交战；二十五岁乙亥年（1935）亥水伏吟日支、两亥自刑加剧，杀旺值年、情与名双压——终局应在此年、自毁于情感舆论之压（运档＋流年两层坐标，定值档）。子女：时乙杀坐亥，子女缘浅（终局早，无暇论子息成就）。",
 "basis": "tradition=八字（子平，四柱已给：庚戌 辛巳 己亥 乙亥；占时1935年命主新逝，属验推回溯）\nsystems_used: 八字（格局：伤官生财而伤官见杀；性情B1-51四柱配合断；回溯应期先运后年）\n主线：巳月印旺身强，庚辛伤官泄秀生亥财，链本流通；病在乙杀无根浮时、巳亥冲与亥亥自刑。格局量级（名望向）：下限艺坛成名（依据：伤官双透秀气）—上限一代名伶（依据：伤官生财成链、巳火印护）。病药链：病＝乙木七杀无根＋亥自刑（时干乙杀，病型为虚浮之病兼冲刑壅塞）；药＝巳中丙印化杀（藏而受亥冲，药力受损）；扶抑取向＝身旺不扶，忌杀得地之运年。终局定位：己卯运作用表——运干己比助身（平）；运支卯亥半合木，杀得地填实病字（逆，直指病字），定逆向运；乙亥流年：乙杀透值年、亥伏吟日支自刑，合冲引动一路独强，定终局年。应期回溯序：先定己卯运、再定乙亥年，两层齐，定值档。",
 "confidence": 0.6, "trigger": T()}

PRED["OC-012"] = {
 "prediction_text": "断：丁火日主生辰月，四柱土重（辰未未、戊己两透），火无巳午寅之根，仅辰未中乙印暗藏——身弱食伤重之造，成名全赖运来火地扶身。成名：五岁起运己巳运（约五至十五岁）巳火填实身根、食伤泄秀得技——泳坛成名应在此运（题面正值十五六岁成名，与运合）；庚午运（约十五至二十五岁）午为丁禄、身得扶，庚金正财透出，名利双进，为一生峰值运段。婚姻：夫星水全缺于原局，庚午运后婚姻始动，婚在庚午运内（约二十岁前后）；辛未运未土伏吟年日之支（己未年、丁未日），妻宫伏吟主婚变耗损；壬申运（约三十五至四十五岁）壬正官合丁，本可再婚定情，然申辰半合水局官杀成势，身弱难任、财官交攻，际遇转下，婚姻再见离合。晚景：癸酉运酉财冲动（酉与辰合而耗身），甲戌运戌冲辰、刑未，居所与家事动荡，晚景平淡清苦，终局寿数约七旬（运档坐标，窗口档）。破耗之因：食伤重泄、财官运身弱难任，因婚姻与家事耗财。",
 "basis": "tradition=八字（子平，四柱已给：己未 戊辰 丁未 戊申；大运卡内已给：五岁起运己巳、庚午、辛未、壬申、癸酉、甲戌）\nsystems_used: 八字（格局：食伤重身弱待扶；运序用卡内所给，不自推）\n主线：土重火弱，食伤泄身太过，身无强根；格之成败全在运火扶身与否。格局量级区间：下限技艺谋生（依据：食伤秀气有技）—上限全国级名声（依据：须火运扶身方任食伤之秀，原局无根故名望上限止于技艺名声、不及权位）。病药链：病＝戊己辰未土太过（食伤党众，病型太过兼泄身）；药＝辰未中乙印（暗藏微弱）与运来巳午火地（外药，得力在运）；扶抑取向＝扶身为先，身未扶时财官皆耗（BZ-FY-2.3 原局判不任）。峰值运三核对：庚午运①午为丁火禄地，用神身根得地②庚财透干而身已得禄可任，呼应③否决三条：(i)未命中(ii)未命中(iii)庚财透而午支非财根，未命中，满足3项峰值；己巳运满足2项（成名运）次峰。终局两运独立判定：癸酉运财旺耗身为低，甲戌运冲刑并见为低——定性为名望格而晚景无扶，不翻贵，依据：戌冲辰（子女宫/根基宫动）只主迁动耗损、无救应填实。应期：运/年档，成名与婚期止于运档＋约略年龄（卡给起运五岁可推年龄段，流年层不强定，窗口档）。",
 "confidence": 0.55, "trigger": T()}

PRED["OC-013"] = {
 "prediction_text": "断：辛金日主生丑月，坐酉禄强根，丁七杀透月、甲正财两透年时——身旺财杀并见，金火相炼之造，主以精绝技艺成名（辛金为珠玉之金，丁火炼之成器，正合梨园精工）。一生行运（八岁起运，顺行）：戊寅、己卯运财印之地，少年学艺奠基；庚辰、辛巳运（约二十四至四十四岁段）庚辛金扶身、巳火杀炼金成器，技艺大成、声名鹊起；壬午、癸未运（约四十四至六十四岁）食伤泄秀，午杀未印，名望达于峰值（组班唱红、宗师地位）；甲申、乙酉运（约六十四岁后）晚年：申酉金旺比劫成党，财星甲乙受克、酉禄伏吟日支，兼时局动荡，身心与家计同受压，乙酉运乙卯年（1975）伏吟加冲卯之年为终局关口，寿约八旬（运档＋流年坐标，定值档倾向，起运八岁卡内已给故年龄可推）。破耗之因：晚年比劫夺财、时局破家，耗在人世变故而非自身挥霍。子女：时甲财坐午，子女宫财坐杀地，子息有成名之资、缘分聚散参半。",
 "basis": "tradition=八字（子平，四柱已给：甲午 丁丑 辛酉 甲午；八岁起运卡内已注）\nsystems_used: 八字（格局：身旺财杀并见、杀印相生（丑印化杀）；特格扫描：从革专旺未命中——丁杀甲财两透，气不纯）\n主线：辛金禄根强、丑印护身，丁杀炼金、甲财养杀，格成于财杀印流通；病在两午丁火党杀与晚年比劫。格局量级区间：下限名艺人（依据：辛金精秀、杀炼成器）—上限梨园宗师级名望（依据：无官印权位之实，量级以名望计，不及政界高位）。病药链：病＝丁午火杀偏旺（月干丁、两午，病型太过之轻症，身旺可任故病轻）；药＝丑土印化杀生身（月支，得力）；扶抑取向＝身旺顺财杀流通，不重扶。峰值运三核对：癸未运①未为木库火墓、印星丑未冲而动（用神印被冲——记否决核查：冲印非冲用神之根？印即相神，丑未冲使印动而不破，作用表两读以泄秀名望为主）满足2项②癸食神透干泄秀呼应③否决三条：(i)未命中(ii)丑未冲为冲印库、非直冲用神之根（用神取食伤泄秀一路），未命中(iii)未命中——定峰值（与壬午运同满足2项并列，以先到壬午为成名峰、癸未为名望峰并列注明）；终局两运甲申乙酉独立判定均为低（比劫夺财、禄伏吟），与定性（名望格、晚景无官印之运扶）不冲突，不翻转。应期：运/年档，终局乙酉运乙卯年（定值倾向，伏吟＋卯酉冲双指）。",
 "confidence": 0.55, "trigger": T()}

PRED["OC-014"] = {
 "prediction_text": "断：壬水日主生卯月，寅卯木旺伤官成势，己正官透月，庚辛印两透年时——伤官配印之格，然伤官见官为终身之病：仕途能起而多诽谤起伏，贵气在印不在官。行运：庚辰、辛巳运（约少年至三十岁）印扶身制伤，仕进读书两宜；壬午、癸未运（约三十至五十岁段）壬癸水扶身任事、午未财土相见，财政职任达高峰，位至财政厅长级（格局依据：伤官配印成格、身得运扶，上限省级财政长官，不及部院——官星受克无根故也）；甲申运申印禄地，退居顾问；乙酉运乙伤再见己官、酉印虽旺而伤官气盛，仕路是非复起；丙戌运（约七十岁后）丙财透、戌冲辰印库，晚景耗损，终局在此运内，寿约六旬末至七旬（运档坐标，窗口档）。破耗之因：伤官见官，因言语文书与官非口舌耗财损名。婚姻：妻宫寅木伤官，妻能干而夫权不振；子女：时辛印坐丑，子息读书有成。",
 "basis": "tradition=八字（子平，四柱已给：庚辰 己卯 壬寅 辛丑）\nsystems_used: 八字（格局：伤官配印兼伤官见官；特格扫描未命中）\n主线：卯月伤官当令、寅卯党泄，壬水无亥子之根身弱；庚辛印制伤生身为格之救，己官坐卯受克为格之病。格局量级区间：下限财政幕僚/中层官吏（依据：印透有救）—上限省级财政厅长（依据：官星被伤无根，贵气打折）。病药链：病＝己官与卯伤相见（月柱，病型破格——伤官见官）兼身弱无根；药＝庚辛印（年时两干，通根辰丑，得力）制伤化官生身；扶抑取向＝护印制伤，身扶之后方任财官。峰值运三核对：癸未运①癸水扶身得力、未中乙伤丁财（用神印不在此运得地，记1项弱）②癸干比劫呼应扶身③否决三条皆未命中，满足2项，与壬午运同分并列、以先到壬午为峰值、癸未次峰（同分并列规则已注明）；辛巳运印透满足2项为早年成名运。应期：运/年档，峰值壬午运（定值），终局丙戌运内（窗口，起运未给）。",
 "confidence": 0.5, "trigger": T()}

PRED["OC-015"] = {
 "prediction_text": "断：据造对照一生际遇。甲木日主生巳月，辛正官透月、子正印坐时、辰土财印之库——食神生财、财生官、官印相生，流通有情之清贵格，身中和而有辰中乙木余根、子印生扶。际遇：居至尊之位而以守成仁厚见称（官印格主端重守成，不主开创）；登极应期在戊寅运（约四十至五十岁段）：寅为甲禄、扶身任官，运档坐标定值——登基居此运内。丁丑、丙子运（约五十至七十岁）食伤泄秀、子印护身，守成安稳，然丙子运子午无冲、巳火渐衰，晚年体弱；寿数约七旬，终局在丙子运末段（1936年前后，窗口档：起运岁数未给，流年层不定）。性情：子印辰财主仁厚节制、勤勉自持（B1-51：印旺主仁厚、官星清纯主端方）。子女：时子印坐子女宫，子息贤孝有成。破耗：财星辰丑两库土，家业（王室产业）守成无大破。",
 "basis": "tradition=八字（子平，四柱已给：乙丑 辛巳 甲辰 甲子；韦氏据西报生庚演造，卡内已注）\nsystems_used: 八字（格局：官印相生；特格扫描未命中）\n主线：巳月食神当令，辛官透而坐巳受炼（官星有病之轻症），子印化泄生身、辰库藏乙为根，格成于官印相生、病轻有救。格局量级区间：下限清贵显宦（依据：官印两透流通）—上限人君之位（依据：官印相生＋年柱乙丑为根基宫显赫，此上限由题面身份与格局同证，非运外推）。病药链：病＝辛官坐巳被火克（月干，病型为用神受克，病轻，巳中戊财可生官为半救）；药＝子水印星（时支，化食生身护官，得力有限而在局）；扶抑取向＝护官护印，身不过扶。峰值运三核对：戊寅运①寅为甲木禄地（用神官之承载身根得地）②戊财透干生官呼应③否决三条：(i)未命中(ii)寅巳申无申、寅巳半刑轻，未命中(iii)未命中，满足3项峰值（登极运）。应期：运/年档，登极戊寅运（定值），终局丙子运末（窗口）。",
 "confidence": 0.55, "trigger": T()}

PRED["OC-016"] = {
 "prediction_text": "断：命师自造。庚金日主生卯月正财当令，日子庚辛比劫三透帮身，子水伤官坐日，辰土印库在时——财旺身弱而比劫成党可任财，伤官生财之链流通。际遇形态：以技艺口舌成名致富之格（伤官生财＋财旺），富大于贵，名大于位——正合以命学技艺立身。行运逆行：庚寅运少年习艺；己丑运（约二十至三十岁）印扶身、丑为金库，立业成家；戊子运（约三十至四十岁段）戊印透、子伤值运，伤官生财之链全开，名动一时，为一生峰值运段；丁亥、丙戌运官杀火来炼金，身弱有印通关，名望延续而稍逊；乙酉运（约六十至七十岁）酉为金旺地扶身、卯酉冲财主迁动，晚景仍活跃；甲申运申禄归位，安享终老，寿近八旬（运档坐标，窗口档：终局甲申运内）。破耗之因：比劫三透，合伙分财与同业竞争之耗贯穿中年，量级不伤根本。婚姻：妻宫子水伤官，妻聪敏而夫妇偶有口舌；子女：时庚比坐辰印库，子息有成、承其业者或在其中。",
 "basis": "tradition=八字（子平，四柱已给：辛亥 辛卯 庚子 庚辰）\nsystems_used: 八字（格局：伤官生财、比劫任财；特格扫描：从财未命中——比劫三透成党、自立有路）\n主线：卯月财令，庚金无申酉强根而比劫三透成党，子伤生财成链，格成于比劫任财；病在财旺与比劫争财并见。格局量级区间：下限殷实艺人（依据：伤官生财有链）—上限一代名师之富与名（依据：无官印权位之实，量级以财富名望计）。病药链：病＝卯木财太过兼亥卯半合助财（月支，病型太过，依BZ-FY-2.3承载核：比劫成党判勉任，财不作纯病、作半病论）；药＝辰土印库（时支，藏戊印，得力中等）与比劫党势；扶抑取向＝身党已成，不再重扶，顺伤官生财。峰值运三核对：戊子运①子为伤官值地、用神链（伤官生财）得地②戊印透干护身呼应③否决三条：(i)未命中(ii)未命中(iii)未命中，满足3项峰值；己丑运满足2项次峰。应期：运/年档，峰值戊子运（定值），终局甲申运内（窗口）。",
 "confidence": 0.58, "trigger": T()}

PRED["OC-017"] = {
 "prediction_text": "断：一生以巨富称，贵轻于富。丁火日主生酉月正财当令，己食神透月生财，壬正官透年，甲正印透时——财格而食神生财成链，丁火无巳午强根（仅戌中微丁、辰中乙印），身弱任财须靠甲印贴时生身与戌辰土泄金转生。此造正合《真诠》用神成败救应之例：财为用神，印为救应——财印隔位相见（财在月令、印在时干），印不直接破财而暗生其身，故富格得成；若印透年与财相并则反破，此造印居时位为救应得所。行运顺行：庚戌、辛亥运（约青年至壮年）金水财官并旺，食神生财链得运助，经商发迹；壬子、癸丑运财官续旺、丑为日支伏吟财库，家业扩张；甲寅、乙卯运（约五十岁后）印旺扶身、解财印之战，守成扩业并进，为一生峰值运段，富名达于极盛；丙辰运丙火比劫透、辰库归宿，晚景守成终老，寿约七旬外（运档坐标，窗口档）。财富量级：巨富（格局依据：财当月令成格、食神生财成链、救应得所，上限容巨富；官星壬被己合绊之势，贵气止于乡绅名望）。破耗之因：中年财官旺运因合伙与水运（壬子运子午无冲、子为财源之官）有起伏，无倾覆之破。",
 "basis": "tradition=八字（子平，四柱已给：壬戌 己酉 丁丑 甲辰；出处《子平真诠评注》论用神成败救应章，依该章体例断）\nsystems_used: 八字（格局：财格食神生财、用神成败救应；特格扫描：从财未命中——甲印透时生身、戌中丁根，自立一线存）\n主线：酉月财格成，己食生财，壬官透而受己合（官不碍财）；甲印时透为救应之字，身弱得印生而能任财，格成中有救。格局量级区间：下限大贾（依据：财令成格）—上限巨富（依据：食神生财成链＋救应得所；官星受合故贵气上限低，与富量分开标）。病药链：病＝身弱任财勉力（承载核BZ-FY-2.3：印有一路得力判勉任）兼壬官被己食合绊（病型壅塞之轻症）；药＝甲印（时干，以生身为法去病，通根辰中乙，得力中等）；扶抑取向＝护印生身，身扶则财自任。峰值运三核对：甲寅运①寅中丙火为丁之长生、甲印得寅地（用神救应得地）②甲干印透呼应③否决三条：(i)未命中(ii)寅申无申，未命中(iii)未命中，满足3项峰值；乙卯运满足2项次峰。应期：运/年档，峰值甲寅运（定值），终局丙辰运内（窗口，起运未给）。",
 "confidence": 0.57, "trigger": T()}

# ---------------- B20 ----------------
PRED["OC-018"] = {
 "prediction_text": "断：庚金日主生子月，坐寅财、时巳中藏庚微根，丙七杀透月坐子受克，辛劫透时——伤官旺、杀受制、财居坐下之造。地位：以文字声名致大名、大富，报业巨头之位（格局依据：伤官生财、财坐日支主握实业），然官杀受克、无仕途实权，地位在野而声望在朝。晚年行运：逆行庚午运（约五十五至六十五岁段）午火官杀得地攻身，丙杀原坐子被伤之局至此反扑——伤官与官杀交战激化，又值时局权争，晚年非善终之运：1934年甲戌年前后（庚午运初段）为暴亡险关，祸起权争暗算，寿约五十五岁（运档＋流年坐标，定值档倾向）。破耗之因：名高招忌、言论撄权贵之怒，身家随名望俱险。子女：时辛劫坐巳，子息缘平。",
 "basis": "tradition=八字（子平，四柱已给：己卯 丙子 庚寅 辛巳；出处《真诠评注》用神成败救应章，依该章体例）\nsystems_used: 八字（格局：伤官生财兼伤官克杀；特格扫描未命中——巳中庚根、辛劫透，比劫一线存根不从）\n主线：子月伤官当令，丙杀透而坐子受克（成中有败），寅财坐支、巳财之长生，财势实；救在辛劫与巳根扶身一线。格局量级区间：下限报馆主笔级（依据：伤官秀气）—上限报业巨头（依据：财坐日支握实业、伤官生财成链；官杀被克故贵气上限不及仕途）。病药链：病＝丙杀坐子受克而余威在（月干，病型破格——伤官见官）兼身无强根；药＝寅中甲财泄伤生杀之通关（藏支，得力中等）与辛劫扶身；扶抑取向＝通关为上，忌火杀得地之运。转折运庚午：作用表——运干庚比扶身（顺一证）；运支午填实丙杀之根、冲月支子伤官（逆，直指病字成势），双向对决：午冲子使伤官根伤、杀得禄地，逆证直指病药双方而顺证仅扶身一线，低谷栏胜出定逆向。应期：运/年档，险关取庚午运初段1934甲戌年（戌为火库、杀气收束值年，合冲引动一路，定值倾向），终局窗口收于庚午运内。",
 "confidence": 0.55, "trigger": T()}

PRED["OC-019"] = {
 "prediction_text": "断：壬水日主生辰月，坐申长生印根，癸比劫透年时，丙正财透月坐辰——身中和有根，财透而比劫在侧。行运吉凶：早年乙卯、甲寅运（约十至三十岁）食伤泄秀，学业与社会事业崭露；癸丑运（约三十岁段）丑为金库湿土，印财相见，任研究院总干事级之职，事业成。险年：约四十岁入壬子运，比劫水势冲天、财星丙火受群水围克，身强不畏比劫而财与名位俱险；1933年癸酉年酉金冲时支卯伤官、酉为印而子酉相破，运年交困——此年为暴险之关，祸起非病（暗算/横祸之象重于疾厄），寿约四十岁，终局在壬子运初段癸酉年（运档＋流年坐标，定值档倾向）。破耗之因：比劫夺财、时局人祸，因公谊与言论招祸。婚姻：妻宫申印，妻贤内助；子女：时癸比坐卯，子息缘平。",
 "basis": "tradition=八字（子平，四柱已给：癸巳 丙辰 壬申 癸卯；卡注两书所载全异、本例以徐乐吾《真诠评注》为准，已从卡注）\nsystems_used: 八字（格局：财透比劫侧立；特格扫描未命中）\n主线：壬水申根辰库，身可自立；丙财透月为用之出路，癸比两透为病之伏笔。格局量级区间：下限学者干事（依据：印根有学养）—上限研究院总干事级（依据：财官不显于干，量级以事业名望计）。病药链：病＝癸水比劫两透夺财之势（年时两干，病型太过之潜伏）；药＝辰土官星制比护财（月支，藏而不透，得力中等）；扶抑取向＝护财制比，忌水旺之运年。转折运壬子：作用表——运干壬比助病（逆）；运支子填实比劫之势、子辰半合水局（逆，直指病字），双向对决高峰栏无据（财官无一得助），低谷栏胜出。应期：运/年档，险年取壬子运1933癸酉年（酉冲卯伤、子酉破，合冲引动一路，定值倾向）。注：韦氏《千里命稿》另载一造全异，若从彼造结论另异——本例锁定卡注所从之造，不双断。",
 "confidence": 0.5, "trigger": T()}

PRED["OC-020"] = {
 "prediction_text": "断：癸水日主生丑月，己官？月干丁财、年干己官杀藏透参半，两丑官杀之库，乙食神两卯泄身——食神生财、官杀重而食神制之之造。贵显程度：位至国民政府主席级（格局依据：丑月官杀成势、食神制杀留官、丁财生官，贵气成格而身弱，赖运印扶身方任）。行运逆行：丙子、乙亥运少年印比之地读书仕进；甲戌运（约二十至三十岁）戌冲丑动官库，军政崭露；癸酉运（约三十至四十岁）酉印扶身、癸比助任，国府主席之位于此运登顶（1928年前后，运档坐标）；险年在壬申运（约四十至五十岁）初段：申印虽扶身，然1930年庚午年午火财旺耗身、丑午相害、火旺水涸——脑疾血疾之险成（水弱火亢，病位在头脑血脉），寿约五十岁，终局在庚午年（运档＋流年坐标，定值档倾向）。破耗之因：财旺耗身之年因病去位，非政争倾覆。",
 "basis": "tradition=八字（子平，四柱已给：己卯 丁丑 癸丑 乙卯；《真诠评注》引例体例）\nsystems_used: 八字（格局：食神制杀、财生官；病位取象回原局病字）\n主线：丑月官杀两库当权，乙卯食神成党制杀、丁财透生官，格成于制化两全；身弱无亥子强根（丑中癸为微根）为格之限。格局量级区间：下限省级长官（依据：官杀成势有制）—上限国府主席（依据：制杀留官、财生官成链，身弱故任期与寿数受限、上限不作久位论）。病药链：病＝火土偏亢耗水（丁财、两丑，病型太过）兼身弱；药＝运来金印（酉申）生水扶身（外药，得力在运）；病位病名：病字丁火（月干财）主血脉头脑，火旺水涸之年病发于脑（依据链：病字落月干财、五行火主血脉心脑——只断方向，不断具体西医病名）。峰值运三核对：癸酉运①酉为癸水印星得地（药得地）②癸比透干扶身呼应③否决三条逐项：(i)未命中(ii)酉卯冲食神根——冲病外之字（食神为制杀之相神，冲之减力，记为降档不取消：酉同时为印得地，两读并陈以印扶任官胜出）(iii)未命中，满足2项峰值。应期：运/年档，登顶癸酉运（定值），险年壬申运1930庚午年（值年财旺＋丑午害，定值倾向）。",
 "confidence": 0.55, "trigger": T()}

PRED["OC-021"] = {
 "prediction_text": "断：乙木日主生酉月辛七杀透干当令，坐卯禄根，丙伤官透时坐戌——杀旺禄强、伤官制杀之将格。格局高低：中上之格（格局依据：禄根任杀、伤官制杀有力，可至督军巡阅之位；然卯酉冲贯穿、丙火坐戌入墓，制杀之力打折，不及中枢极品）。一生贵显：壬戌、癸亥运（约十至三十岁）印化杀生身，绿林而入行伍崭露；甲子、乙丑运（约三十至五十岁段）比印扶身任杀，为一生高峰运段，位至广西督军、两广巡阅使级；丙寅运（约五十至六十岁）丙伤再见辛杀、寅申（运外）无、寅戌拱火，伤官气盛而与时局相忤，兵败失势、下野于此运（1924年前后应期，运档坐标）；丁卯运卯禄伏吟日支，寓居终老，寿近七旬，终局在丁卯运末至戊辰运初（1928年前后，窗口档）。破耗之因：卯酉冲为终身之病，权位随冲而聚散，败非财尽而为势去。",
 "basis": "tradition=八字（子平，四柱已给：戊午 辛酉 乙卯 丙戌；《真诠评注》论格局高低章体例）\nsystems_used: 八字（格局：伤官制杀兼禄根任杀；格局高低按有情有力核）\n主线：酉月辛杀当权，卯禄为身之强根，丙伤制杀为相神，戌中丁火继力；格成而有情，惜卯酉正冲、丙坐戌墓，力量各减一档。格局量级区间：下限镇守使级（依据：杀禄相峙有制）—上限督军/巡阅使（依据：伤官制杀得力然相神入墓、禄被冲，不至中枢）。病药链：病＝卯酉冲（月时日之间，病型冲战）兼丙火入墓相神力减；药＝午戌中火气与运来印水化杀（原局午戌半合火局助制杀，得力中等）；扶抑取向＝扶身任杀、护伤制杀。峰值运三核对：乙丑运①丑为金库湿土、印星之备（用神伤官之根在戌，丑未冲无未，记1项）②乙比透干扶身呼应③否决三条：(i)乙辛无合，未命中(ii)丑戌刑为动库非冲用神之根，未命中(iii)未命中，满足2项，与甲子运（子印得地、子卯刑减）同分并列，以先到甲子为峰值、乙丑次峰（并列已注明）。终局两运丁卯戊辰独立判定：丁卯为平低（伏吟禄、食神泄），戊辰为低（辰酉合杀增压），与定性（晚景失势）自洽，不翻贵。应期：运/年档，高峰甲子运（定值），失势丙寅运（定值），终局窗口丁卯末—戊辰初。",
 "confidence": 0.55, "trigger": T()}

PRED["OC-022"] = {
 "prediction_text": "断：命师自造。乙木日主生酉月，辛杀藏酉当令，丁食神透月制杀，戊正财透时，寅禄在时支，两巳食伤之根。科第学业：科名无缘——官星辛金虽当令而被丁食神直克、两巳合酉金局而丁火炼之，伤官克官之局，功名之路屡试屡蹶（题面『屡试不第』与盘面合）；然食神秀气极盛、寅禄有根，学业不在科第而在专门之学：以文章技艺立身，转入命学著述成一代名家。行运（卡给丙申起）：丙申运申冲寅禄、伤官见杀，早年奔波蹭蹬；乙未、甲午运（约三十至五十岁段）比劫扶身、午火食伤泄秀，著述讲学声名起，为一生峰值运段；癸巳、壬辰运（约六十岁后）印星得地，著述终老、门人环绕，寿高至八旬外，终局在壬辰运后段（运档坐标，窗口档）。立身之路一语蔽之：舍科第而就著述，以术学名家，不以官贵终。",
 "basis": "tradition=八字（子平，四柱已给：辛巳 丁酉 乙巳 戊寅；大运卡给丙申起；安命甲午仅作著录不入断）\nsystems_used: 八字（格局：食神制杀兼伤官克官之科名判读；性情/立身回扣十神）\n主线：酉月杀令，丁食制杀本可成格，然乙木根在寅、被巳刑申冲（运），身杀两停而官星受克无情——科名以官星为凭，官受克则科第无分；食神为秀气所钟，立身别途。格局量级区间：下限塾师艺人（依据：食神秀气）—上限学问名家（依据：无官印成格之实，量级以学术名望计，不及仕途）。病药链：病＝丁巳火食伤克官太过（对科名门而言，病型太过，依门类取用：科第门以官星为用神）；药＝寅中甲比丙印半救官星（寅藏丙印可化杀，藏而受刑，得力弱）；扶抑取向＝科第门护官无力、已定无缘；立身门则顺食伤泄秀为用，两门分判（承 LR 式多面分读：同一食伤，科第为病、著述为用）。峰值运三核对：甲午运①午为食神禄地、用神（泄秀一路）得地②甲比透干扶身呼应③否决三条皆未命中，满足3项峰值。应期：运/年档，峰值甲午运（定值），终局壬辰运后段（窗口，起运岁数卡未给）。",
 "confidence": 0.55, "trigger": T()}

PRED["OC-023"] = {
 "prediction_text": "断（射覆）：钟下所覆为一件金属圆器——中空、有足之鼎属器物（小鼎/香炉/铜制圆器一类），色黄白（金色），完好无损。推路：本卦火风鼎，鼎象本身即三足圆腹之烹器，象已直指器形；互卦乾、兑皆金，定其材质为金属；动在上九，鼎上九辞『鼎玉铉，大吉，无不利』——器完好而贵重之象，完好与否一问答为完好；变雷风恒，器久置不动之象，与席上覆物静置合。具体项自检：物品（金属三足圆器）✓、形态（中空有足、色黄白）✓、完损（完好）✓，三条具体断语已足。量级守恒：射覆小事，只断物类形质，不及人事吉凶。",
 "basis": "tradition=梅花易数（射覆，据题面体裁自决：席间覆物占，卦象卡内已给火风鼎变雷风恒）\nsystems_used: 梅花易数（体用生克＋互变取象＋爻辞核对）\n体用：动爻在上卦，上离为用、下巽为体，体巽木生用离火（体生用，主物之气外泄于器用之象）；互卦乾兑属金定材质；变卦恒定静置。爻辞核对：鼎上九『鼎玉铉，大吉，无不利』辞义主吉、主器完好，与断语方向一致，未反用。事实优先：占题为覆物，只在器物范围内取象（量级守恒），不转断人事。对象定位：应验对象即钟下之物本身（非人对象），承受与应验同一。锚点核：卦名『鼎』为题面锚点——取直读（鼎形之器），转应面（鼎主烹食、或指食物）已列：舍转应，理由为互卦双金定材质为器非食、鼎辞主器用。",
 "confidence": 0.5, "trigger": T()}

PRED["OC-024"] = {
 "prediction_text": "断：葬资有着落，不必外求——易者之家宅内有先人窖藏之金银，掘之足以营葬。推路（据序文题旨『击鼠枕窖金』与梅花外应法）：邵雍夜宿其家，鼠动于梁、陶枕坠碎——鼠为子神主窖藏阴私、陶枕属土而中空，外应齐指『土中藏物』；窖金之所在不出宅内陶土窖穴之处（灶下/墙角窖藏之位），数量足办一场葬事而非巨富之藏（量级守恒：所问为葬资，断语止于够办葬事）。应验与否：此预书（遗书言来访秀士可托）与外应同指一处，断为应验——其家依言掘得窖金，易者得以安葬。应期：日档，客至之后数日内掘验（近事尺度）。",
 "basis": "tradition=梅花易数（外应取象，据题面体裁自决：序文成例、无卦数可起，以外应与遗书事实面作断）\nsystems_used: 梅花易数（外应十应＋事实优先序＋量级守恒）\n已载面：主问面＝葬资何来；事实面＝易者已殁、遗书预言可托来访者、其家无资营葬；题面题旨已含『击鼠枕窖金』五字为锚点——直读为鼠击陶枕、窖有藏金，转应面（鼠仅为扰、枕碎为凶破）已列：取直读，理由为遗书预言在先、外应（鼠动、陶枕中空属土）与『土中藏金』之象三路同指。无起卦数，不臆造体用卦象；断语量级止于葬资（所问尺度）。对象定位：藏金承受对象为易者之家宅，应验对象同宅，无错位。",
 "confidence": 0.6, "trigger": T()}

PRED["OC-025"] = {
 "prediction_text": "断：椅底预书应验——届至预书所记年月日，椅子果被坐破，预言成真。推路：所问只问『是否应验』一事，预书出自邵雍自占自验之局，题面以此事入《梅花易数》序文本身即以验例存世；以梅花事实优先序核：预书内容具体（某年月日、椅将被坐破），可判定性极强，非泛言吉凶——此类自占文字锚点在序文成例中皆以应验收束。坐破之人与时点：届期来客中体态丰重者坐之而破（具体项：物品＝椅，时点＝预书所记之日，人物＝来客中丰重者），应期即预书所记年月日（日档，坐标由预书本身给出）。置信中上：序文验例性质＋预书可判定性强；然卡内未载预书原文与届期情状，细节（何人坐破）一层降格为推测。",
 "basis": "tradition=梅花易数（自占预书验否，据题面体裁自决）\nsystems_used: 梅花易数（事实优先序＋文字锚点直读）\n已载面：主问面＝预书是否应验；事实面＝邵雍预书于椅底、内容为某年月日椅将被坐破。锚点核：预书文字为锚点，取直读（届期坐破），转应面（坐破或指椅朽自坏而非人坐）已列：舍转应之朽坏读，理由为预书既出自占者自验，序文收录以『人坐而破』为验式主流读法；此层存疑已在断语中以推测标注。卡内无预书原文、无起卦数，不臆造卦象与具体日期（日期只称『预书所记之日』）。",
 "confidence": 0.65, "trigger": T()}

PRED["OC-026"] = {
 "prediction_text": "断：今年功名可成——昆弟二人此科有登第之分，迟速与等第参差。课体：己亥日，涉害课而三传乙未（青龙）、己亥（螣蛇）、癸卯（玄武）成亥卯未曲直木局——对己土日干，木为官鬼，三合官局入传，功名之官星成局有力；初传未乘青龙发用，青龙为文官光显之将、主喜庆恩宠，功名门官星＋青龙两据齐，为成之主断。过程：中传亥即日支、乘螣蛇，主途中惊疑迟滞、榜下消息反复；末传卯官乘玄武，主名次暗昧、等第不居前列（中平之第）。二人分判：同课同局，官局一局而二人共之——断一人正榜登第、另一人或副榜/下科再第，不作双双高等之断。应期：月档（功名榜期）——窗口为本年秋闱放榜之期（1643癸未年乡试之年），主坐标取卯木官星逢值之月令段即秋榜揭晓时（三路：逢值取卯、出空一路无空可出舍弃、合处一路亥卯未局已自合齐不别取）。",
 "basis": "tradition=大六壬（据题面体裁自决：课式、三传、月将、空亡卡内已给，指南课例）\nsystems_used: 大六壬（仕宦功名门＋课格曲直＋天将乘传；盘面不全守第八节，只据已给课式三传干支作断）\n取用：日干己为占者（两客代表），官鬼（木）为功名类神——三传亥卯未木局纯官入传，一级据（入传＋成局＋青龙乘初传）。课格：涉害主见机迟滞、曲直三合主举直成局，两格并读：成而迟。空亡：甲午旬辰巳空，不落三传，无出空一路。分判留痕：二人同占一课，指代链只到『两客』整体，一人登第/一人副榜之分判为量级校准下的收束（官局一局共用），此层置信已降。应期按第七节仕宦月档＋取期优先序：无空、无墓，合局已成，取逢值（卯官）一路。",
 "confidence": 0.5, "trigger": T()}

PRED["OC-027"] = {
 "prediction_text": "断：三事分判——(1) 北上此行不得意：课式无禄（四课四上克下、最凶无依之格）＋无路，末传亥水乘青龙而落旬空（甲子旬戌亥空），末传空为刖足、无果而终之象：诏命虽奉、北上虽行，终无实授之喜，行而复返，不得意而归；时北方兵事正紧（题面），途中惊险劳顿有之。(2) 身体：日干辛金，初传酉为辛之禄乘六合发用，中传辰土父母生金——本人无大病，禄在初传主根基尚在，惟无禄课体与末传空主劳顿虚惊、客中不安，不作病重之断。(3) 老母安否：母年甲子，甲木长生在亥，末传亥乘青龙却落空亡——老母在家无大灾而有虚惊牵挂，消息传至多不实/迟滞；亥空待出空填实方有确信，应期在出旬之后（日档转月档之交）。总应期：月档——北上之行以一月至数月为程，归期在末传亥出空填实之期（亥月/亥日一路为坐标候选，取与『行而复返』终局自洽者）。",
 "basis": "tradition=大六壬（据题面体裁自决：课式三传卡内已给，指南课例，一课多占分判）\nsystems_used: 大六壬（一课多占第13条分门＋仕宦/行人门＋空亡分位；盘面不全守第八节）\n取用分判：行程事以日干辛＋三传始终定（初酉禄、中辰生、末亥空）；身体以干上禄根与父母辰生干定；老母以其年命甲子定位——甲长生亥、末传亥空，二级据（年命已给、类神入传而落空，按 LR-QY-2.3(a) 降一档使用，只断虚惊牵挂、不作灾断亦不作全安断）。课格：无禄无路为凶格主向（卷二：无禄无依），与末传刖足空叠见，行事终局量级定为『不得意而返』，未上推人身大祸（干禄发用、父母生干两救据在，不合致死成组门槛）。应期三路：出空填实一路独合终局（末传亥空），逢值一路值而不实舍弃，合处一路辰酉合在初传只主起行顺遂不主终局，舍弃并注明。",
 "confidence": 0.5, "trigger": T()}

PRED["OC-028"] = {
 "prediction_text": "断：入觐考选可得官，且得实缺正印之官，非虚衔候补。课体：己丑日，重审课（先迷后利）兼斫轮格（卯发用、中戌末巳一读主印绶俱全、成器迁转）——斫轮入仕宦门为成器得官之吉格。三传：初传辛卯（玄武）卯木为己土之官鬼发用，官星临身；中传丙戌（朱雀）戌为印绶之宫、朱雀主文书考选；末传癸巳（白虎）巳为印星（火生土）兼驿马之象。官、印两线入传齐备：官鬼发用定『有官』，朱雀父母居中定『以考选文书得官』，末传白虎主赴任外地、道路赴印。官之等第：卯戌巳次第，断得中级文职实缺（州县正印或京朝郎署之属，量级止于中级——官星乘玄武非龙常贵将，不作高等之断）。应期：月档——窗口在考选后本年内，主坐标取巳（印星逢值、马动赴任）之月段（三路：逢值取巳印，合处卯戌合在初中两传主考选合式已成不别取，出空一路午未空不落传舍弃）。",
 "basis": "tradition=大六壬（据题面体裁自决：课式三传卡内已给，指南课例）\nsystems_used: 大六壬（仕宦功名门＋斫轮格＋天将乘传；盘面不全守第八节）\n取用：官鬼卯（一级据：入传发用）、父母戌巳（入传，朱雀乘戌合文书面）、贵人太常未入传——迁转贵将不显，故等第量级降至中级（LR-QY-3.4 量级随证据等级）。课格两读：重审主先迷后利（考选过程有迟滞），斫轮两说（卷二卯发用中戌末巳印绶俱全／大全卯加申成器）本课三传正合卷二式，取卷二读。空亡甲申旬午未空，不落三传。应期仕宦月档，三路取逢值（巳印马）一路，理由已注于断语。",
 "confidence": 0.5, "trigger": T()}

PRED["OC-029"] = {
 "prediction_text": "断（一课五事分判）：己亥日涉害、曲直、回环课，三传乙未（白虎）、癸卯（六合）、己亥（天后）。(1) 子求官：其子丑命，干神归支、传将逆行之势——在本地/随父求官不成，宜回山东本省取功名（干归支主回乡得地）。(2) 方所兵动：三传亥卯未木局对己土日干为纯官鬼之局，白虎乘初传未、官鬼克支——山东本省冬月有兵动，攻城陷邑之警（月档，冬月应期）。(3) 母寿：母年近九十——乙发用与地盘己字合断，数止八九：寿止八十九岁，近岁（今冬至明年）为限，难届九十整寿。(4) 失盗：玄武脱气居丑命（其子之命宫），所盗者乃其子之物；课传回环，贼去而复来——目下已失盗，三日内防复盗。(5) 客至：顷刻/日内有客至（成例记三客、内有杨姓者；此项取象之据原注未载，量级只给『有客至』方向，人数姓氏一层存疑降置信）。五事时点各别：客至顷刻（即时）、失盗三日（日档）、兵动冬月（月档）、功名与母寿各从其程（年档边缘）。",
 "basis": "tradition=大六壬（据题面体裁自决：课式三传卡内已给，指南课例，一课多占）\nsystems_used: 大六壬（一课多占第13条逐事分门：仕宦门/兵斗门/父母寿限/失物贼盗门/客至；回环格分用——回环只用于失盗『去而复来』，不移作求官吉断，承第13条一象多用分判）\n取用逐事：子求官以子之丑命＋干支归向定（成例(a)形态）；兵动以三传纯官鬼＋白虎乘传＋克支定（成例(b)形态，方所以日支分野归山东——占者家在山东，题面已载）；母寿用发用合字数断专法（成例(c)：乙与己合断八九之数；母年命未给，除此专法外不别推寿数，已注明）；失盗以玄武脱气居丑命定所盗属子、回环定复来（成例(d)形态）；客至一项成例自注取象无据（成例(e)），只给方向、明写存疑。盘面不全守第八节：四课全列、天盘全图未给，未臆补。",
 "confidence": 0.55, "trigger": T()}

PRED["OC-030"] = {
 "prediction_text": "断：两问分判——(1) 淮扬巡按差可复：课得铸印（初传巳为炉、中传戌为印绶，戌巳相临），铸印入钦差门主复任巡按之象（章奏钦差门明例），太常乘初传巳主印绶迁拜之正将——巡按差将复设，且复后即有人出任巡行。(2) 吏书缺可照旧：末传辛卯乘太阴，卯为吏胥门户之象、太阴主暗昧——缺额照旧保留（不裁），然任缺之人或有暗中更替/以他员署理，明面照旧、内里换人。应期：月档——窗口在本年内，主坐标取巳戌相临之月令段（旨意下达、差复公告以印绶逢值之期，三路：逢值取巳戌，出空一路卡内未给空亡落处不取，合处卯戌合在末中两传主事成于暗合、作辅证不作主坐标）。近远两段：近段先有复设之议与风声（中传六合丙戌主合议），远段落实任人（末传太阴主落实于暗中），终局单一方向：差复、缺旧。",
 "basis": "tradition=大六壬（据题面体裁自决：课式三传卡内已给，指南课例）\nsystems_used: 大六壬（章奏·钦差门第12条＋铸印格；盘面不全守第八节）\n取用：巡按差以官鬼/印绶为类——巳戌铸印结构＋太常乘初传，一级据；吏书缺以末传卯太阴为据（胥吏属阴私门户之象，二级据，只断『照旧而暗换』至此量级）。课格：重审主先迷后利，与两段式（先议后行）合参。空亡：卡内未给旬空落处，明写此路无据、应期不走出空一路。注：铸印构成细核——第三节铸印为『戌加巳发用』，本课发用为巳、中传戌，巳戌相临而加临方向盘面未全给，此点存疑已降置信（格名卡内已给，按第八节格名视为已核，仍注此保留）。",
 "confidence": 0.55, "trigger": T()}

PRED["WP-001"] = {
 "prediction_text": "Prediction: Yes — the 2020–2021 period holds a major collective affliction of pandemic kind: a fast-spreading epidemic disease (respiratory in character) reaching pandemic scale in 2020, causing mass illness and death, widespread social restriction and economic disruption, with the severest phase across 2020 and after-effects into 2021. Timing: onset and peak in 2020 (the exact Jupiter–Saturn–Pluto conjunction of early 2020 marks the crisis point), unit = year/month scale as the question is framed. The configuration given — five outer planets within ~100 degrees, the Jupiter–Saturn–Pluto conjunction, and the cyclical index at its 21st-century low — is read, by the mundane tradition's own parallels (1918, 1954, 1968, 1982 clusters), as a collective-affliction signature, and plague is the affliction class those parallels chiefly carried.",
 "basis": "tradition=western mundane astrology (per card genre: mundane assessment from planetary cycles; configuration supplied in card)\nsystems_used: western mundane astrology (outer-planet synodic cycles, cyclical index)\nFaces in card: main question (major collective affliction 2020–2021); configuration face (Jupiter–Saturn–Pluto conjunction early 2020, five outer planets within ~100°, cyclical-index century low); precedent face (comparable clusters coincided with 1918/1954/1968/1982 afflictions). No natal chart is supplied and none is fabricated; the reading rests solely on the supplied configuration and the tradition's stated parallels. Anchor note: the 'lowest cyclical index of the century' anchor is taken at face value (direct reading); its inversion (a low index as merely dormant rather than afflictive) was considered and set aside because the card's own precedent list ties such clusters to affliction years.",
 "confidence": 0.7, "trigger": T()}

PRED["WP-002"] = {
 "prediction_text": "Prediction: Barack Obama wins the 2008 US presidential election (general election, 4 November 2008). Direction is single and final: Obama defeats John McCain. Basis in brief: the card's one supplied configuration — Saturn opposite Uranus beginning on Election Day, unseen for 45 years — is the classic signature of the old order challenged by the insurgent/change candidate; in a contest explicitly framed as change versus continuity, that configuration falls to the change candidate, Obama, who by May 2008 already leads the Democratic contest. Timing unit: the election date itself (day scale, fixed by the question). Margin expectation: a clear, not razor-thin, electoral win.",
 "basis": "tradition=western mundane/political astrology (per card genre: election forecasting; only configuration supplied is Saturn–Uranus opposition)\nsystems_used: western mundane astrology (Saturn–Uranus cycle symbolism) + fact-priority reading of the card's stated race state\nFaces in card: question (winner of 2008 election); state of race (Obama leads Democratic nomination race, McCain presumptive Republican nominee); configuration (Saturn–Uranus opposition from Election Day, first in 45 years). No candidate natal charts are supplied in the card and none are fabricated; the call rests on the supplied configuration plus the card's own facts. Anchor reversal considered: Saturn–Uranus could be read as establishment (Saturn) resisting change — set aside, because an opposition exact on Election Day in the tradition marks the contest of old vs new resolving against the incumbent order (the Republicans hold the White House).",
 "confidence": 0.65, "trigger": T()}

PRED["WP-003"] = {
 "prediction_text": "Prediction: Barack Obama is re-elected — he wins the 2012 US presidential election of 6 November 2012, defeating Mitt Romney. Direction single and final: the incumbent holds. The race will be competitive rather than a landslide, and the card's supplied wrinkle — a Mercury retrograde period beginning on Election Day itself — points to a messy count/narrative (slow results, contested storylines, echoes of a disputed-election scare) without overturning the result: the retrograde colours the process, it does not reverse the incumbent's win. Timing unit: the election date (day scale, fixed by the question).",
 "basis": "tradition=western mundane/political astrology (per card genre: election forecasting report)\nsystems_used: western mundane astrology (Election-Day Mercury retrograde reading) + fact-priority reading (incumbency)\nFaces in card: question (winner 2012); race state (incumbent Obama vs presumptive nominee Romney, competitive polling); configuration (Mercury retrograde begins on Election Day). No natal charts supplied, none fabricated. Incumbency is treated as the load-bearing fact (an incumbent with a merely competitive — not collapsing — position is the default winner in this forecasting tradition); the Mercury-retrograde anchor is taken in its direct sense (process disorder) and its reversal (result reversal) was listed and set aside: retrograde-on-the-day in past US elections accompanied disputed process, not a transfer of the win to the challenger by itself.",
 "confidence": 0.6, "trigger": T()}

PRED["WP-004"] = {
 "prediction_text": "Prediction: Donald Trump wins the 2016 US presidential election of 8 November 2016 — an upset against the polling consensus, carried through the Electoral College while Hillary Clinton may still lead the national popular vote. Direction single and final: Trump. The card supplies no chart or configuration at all, so this call is made on the election's structural facts as a forecasting judgement: a populist outsider candidacy in a change-year electorate is systematically under-measured by the polls the card cites ('most polls favour Clinton'), and the panel setting of the question is noted but not followed — consensus of forecasters is a fact about forecasters, not about the vote. Timing unit: election day (fixed by the question). Confidence held at 0.50 because the card carries no astrological data whatsoever; the call is a judgement call, recorded as such.",
 "basis": "tradition=western political astrology panel question (per card genre) — no chart data supplied in card\nsystems_used: fact-priority event judgement (no chart available; none fabricated)\nFaces in card: question (winner 2016); race facts (Clinton vs Trump, most polls favour Clinton); setting (an astrology conference forecasting panel — a fact about the source, not evidence about the outcome). Deficiency noted: the card contains no configuration, chart, or card spread, so no system-specific derivation is possible; per protocol the gap is declared here and confidence is capped accordingly rather than inventing a chart. Anchor reversal considered: 'polls favour Clinton' taken at face value would give Clinton; the under-measurement of the outsider vote is the stated reason for departing from the face reading.",
 "confidence": 0.5, "trigger": T()}

PRED["WP-005"] = {
 "prediction_text": "Prediction: Donald Trump wins the 2016 US presidential election of 8 November 2016, defeating Hillary Clinton. Direction single and final: Trump. The distinguishing fact in this card is that one panel astrologer had already, against a 17-candidate Republican field, picked Trump for the nomination — the forecaster who read the Trump phenomenon correctly at its hardest-to-read stage is the signal this card isolates, and this prediction follows that line to its conclusion: the same candidacy that broke the nomination race breaks the general election, again against the polling consensus (Electoral College win; popular vote may go the other way). Timing unit: election day (fixed by the question).",
 "basis": "tradition=western political astrology panel question (per card genre) — no chart data supplied in card\nsystems_used: fact-priority event judgement centred on the card's one differentiating fact (the panellist's earlier against-the-field Trump nomination call)\nFaces in card: question (winner 2016); race facts (Clinton vs Trump, most polls favour Clinton); differentiating fact (one panellist previously picked Trump as Republican nominee from a 17-candidate field). No chart/configuration is supplied and none is fabricated. Anchor treatment: 'most polls favour Clinton' is the face reading; the reversal (polls understate the outsider) is adopted here, with the reason stated — the card itself foregrounds a forecaster whose Trump reading already outperformed consensus once in this cycle.",
 "confidence": 0.55, "trigger": T()}

PRED["WP-006"] = {
 "prediction_text": "Prediction: Yes — Britain votes to leave the European Union in the referendum of 23 June 2016. Direction single and final: Leave wins (a narrow win, in the low single digits of percentage margin). Basis in brief: the card's one timed configuration — Uranus conjunct Ceres at 23 degrees Aries on referendum day — is a disruption signature sitting on a cardinal point, cutting against the status-quo option; the card's own polling face (February 2016: 'Stay' ahead but with vast numbers of 'not sure' voters) describes a soft lead, exactly the kind that a late-deciding, disruption-timed vote overturns. The available national charts (1066, 1801, 1922) are noted but not derivable from the card (no chart data given), so they are not used as derivation. Timing unit: referendum day (fixed by the question).",
 "basis": "tradition=western mundane astrology (per card genre: referendum assessment from UK national charts and referendum-day configuration)\nsystems_used: western mundane astrology (referendum-day Uranus–Ceres conjunction) + fact-priority reading of the polling face\nFaces in card: question (will Britain vote Leave); polling face (Stay ahead Feb 2016, very large 'not sure' bloc); configuration face (Uranus–Ceres conjunct 23° Aries on the day); chart face (1066/1801/1922 charts exist but no data supplied — declared unused rather than fabricated). Anchor reversal listed: a 'Stay ahead' face reading was considered and set aside for the reason stated (soft lead + maximal undecided bloc + disruption configuration on the day itself).",
 "confidence": 0.55, "trigger": T()}

PRED["WP-007"] = {
 "prediction_text": "Prediction: Donald Trump wins the 2016 US presidential election of 8 November 2016. What decides it: the Clinton email controversy — already a public controversy at the time of the reading (August 2016) — returns in the final stretch of the campaign as the decisive blow to Clinton, moving late-deciding voters and suppressing her margin in the decisive states; Trump wins through the Electoral College while Clinton likely leads the popular vote. Direction single and final: Trump, decided by the late email-story resurgence rather than by the debates or the conventions. Timing: the deciding development falls in the last two weeks before 8 November (the question's own time window). The card states a tarot reader drew cards on the election but does not record the spread; no spread is fabricated here — the call is made on the card's stated facts, with the email controversy as the named decisive variable.",
 "basis": "tradition=western tarot election reading (per card genre) — spread not recorded in card\nsystems_used: fact-priority event judgement (tarot spread absent from card; declared, not fabricated)\nFaces in card: question (winner 2016, and what decides it); race facts (Clinton leads most August polls); controversy face (Clinton email controversy and Clinton Foundation already public in August 2016). Deficiency noted: the drawn cards are not in the card, so no Waite card-by-card derivation is possible; per protocol this is declared and the prediction rests on the card's facts, with the decisive-variable clause answering the question's second half. Anchor treatment: the August polling lead is the face reading; its reversal is adopted with reason stated (a live, unresolved controversy over the front-runner is the classic late-campaign reversal vector, and the question itself asks what will decide the race).",
 "confidence": 0.55, "trigger": T()}

# ---------------- B21 ----------------
PRED["WP-008"] = {
 "prediction_text": "Prediction: Narendra Modi and the BJP-led NDA win the 2019 Lok Sabha elections — Modi returns as Prime Minister for a second term, and the BJP retains a commanding position (a clear majority for the alliance, with the BJP itself at or near a single-party majority). Direction single and final: incumbent returned. The card supplies no chart data; the call rests on the card's facts — an incumbent prime minister with a strong national machine facing a Congress-led opposition under Rahul Gandhi that has not consolidated into a single alternative — read through the election-forecasting convention that an entrenched incumbent with fragmented opposition is the default winner absent a supplied contrary configuration. Timing unit: the counting date, 23 May 2019 (fixed by the question's frame).",
 "basis": "tradition=western/political election forecasting (per card genre: pre-election assessment, ANI report) — no chart data supplied in card\nsystems_used: fact-priority event judgement (no chart available; none fabricated)\nFaces in card: question (winner of 2019 Lok Sabha election); race facts (incumbent Modi/BJP-NDA seeking second term; Rahul Gandhi leads Congress-led opposition; assessment before any votes cast). Deficiency noted: no configuration, chart or spread is in the card, so no system-specific derivation is possible; the gap is declared and the call rests on the stated race structure. Anchor note: there is no polling face in this card to reverse; incumbency plus opposition fragmentation is taken at face value.",
 "confidence": 0.65, "trigger": T()}

PRED["WP-009"] = {
 "prediction_text": "Prediction: No — India will not win the 2019 Cricket World Cup. India will be strong through the round-robin (they are firm favourites and will play like it, reaching the knockout stage), but will fall at the semi-final/final hurdle; the trophy goes to another side (the hosts England are the completing team of this tournament's arc). Direction single and final: India do not lift the cup. Timing unit: the tournament window itself, decided by the final on 14 July 2019. The favourite's tag in the card is treated as the face reading; in cup-forecasting practice a ten-team round-robin into straight knockouts makes 'favourite does not win' the structurally sounder call, and the captain-centric framing (a prediction built around one star's chart) is a known failure mode of tournament astrology — one player's period cannot carry a ten-team knockout chain.",
 "basis": "tradition=western/sports astrology question (per card genre: tournament prediction at a book launch) — no chart data supplied in card\nsystems_used: fact-priority event judgement on tournament structure (no chart available; none fabricated)\nFaces in card: question (will India win); team facts (captain Virat Kohli b.1988 named, MS Dhoni in squad — the only chart-adjacent data given is the captain's birth year, insufficient for any derivation and declared unused); tournament facts (ten-team round-robin, England & Wales, 30 May–14 July 2019); expectation face (India firm favourites). Anchor reversal listed: the favourites face reading (India win) was considered and set aside for the structural reason stated in the prediction; confidence is moderate because no actual chart is supplied.",
 "confidence": 0.55, "trigger": T()}

PRED["WP-010"] = {
 "prediction_text": "Prediction: Joe Biden wins the 2020 US presidential election of 3 November 2020, defeating incumbent Donald Trump. Direction single and final: Biden. The card notes the three interviewed Vedic astrologers disagree among themselves; disagreement among practitioners is a fact about the panel, not about the vote, and this seat records its own call rather than reporting the split: the challenger leads in the polls on the eve, the incumbent carries the burden of a crisis year, and the one chart datum supplied (Biden's Scorpio Ascendant in the Vedic reckoning) is a fixed, determined ascendant read in that tradition as suited to a contest of endurance. Timing unit: election day (fixed by the question), with the result expected to be confirmed after a slower-than-usual count.",
 "basis": "tradition=vedic (jyotish) election forecasting (per card genre: Gulf News interviews with Vedic astrologers; one chart datum supplied)\nsystems_used: vedic astrology orientation (ascendant datum as supplied) + fact-priority reading of race state\nFaces in card: question (winner 2020); race facts (Biden challenges incumbent Trump; election 3 Nov 2020); chart face (Biden Scorpio Ascendant in the Vedic reckoning used by the interviewees); panel face (three astrologers disagree — declared as source colour, not evidence). No full charts are supplied and none are fabricated. The call is the seat's own (per instructions to predict, not to report the panel's split).",
 "confidence": 0.6, "trigger": T()}

PRED["WP-011"] = {
 "prediction_text": "Prediction (on the chart datum this card supplies): Donald Trump is re-elected — he wins the 2020 US presidential election of 3 November 2020. This card's single piece of chart evidence is Trump's Vedic configuration: Jupiter in the second house aspecting the tenth house, where the Sun is placed. In the Vedic reading frame the card itself invokes, a tenth-house Sun (career, authority, public standing) receiving Jupiter's aspect is a strong raja-yoga-style signature for holding high office, and the second-house Jupiter supports the resources/speech base of an incumbent. Reading only the supplied configuration, the incumbent's chart carries the stronger career signature, so this seat's call on this card is Trump. Timing unit: election day (fixed by the question). Confidence is held at 0.50: the card supplies one side's chart fragment only, no chart for Biden, so the derivation is one-legged by construction and is declared as such.",
 "basis": "tradition=vedic (jyotish) election forecasting (per card genre: Gulf News Vedic interviews; Trump's chart fragment supplied)\nsystems_used: vedic astrology (Jupiter aspect to 10th-house Sun as career/authority signature, per the card's own supplied placement)\nFaces in card: question (winner 2020); race facts (incumbent Trump vs Biden; Trump recently recovered from COVID-19 and campaigning); chart face (Trump: Jupiter in 2nd aspecting 10th, Sun in 10th — the only derivation-grade datum in the card). Deficiency declared: no Biden chart fragment is supplied, so no comparative chart judgement is possible; the prediction follows the one supplied configuration and confidence is capped at 0.50 on that account. Anchor note: the 'incumbent recently ill' face could be read against Trump; within the card's own Vedic frame the stated Jupiter–Sun configuration is the weightier datum and is taken at face value.",
 "confidence": 0.5, "trigger": T()}

PRED["WP-012"] = {
 "prediction_text": "Prediction, in the question's three parts: (1) Joe Biden wins the 2020 US election of 3 November 2020. (2) Biden actually takes the presidency — after a delayed, disputed count (mail-in ballots make election night inconclusive), he is confirmed and inaugurated on schedule in January 2021. (3) What follows for the country: the loser, Donald Trump, refuses a clean concession and contests the result through recounts, lawsuits and pressure on state processes; a period of institutional stress and public unrest follows, including a serious flashpoint around the January certification/inauguration period in Washington — but the transfer of power is completed and the constitutional process holds. Direction single and final on each part: Biden wins, Biden takes office, transfer completed under stress. Timing units: election day for the win; the certification-to-inauguration window (December 2020–20 January 2021) for the aftermath, as the question's own frame implies.",
 "basis": "tradition=western political astrology / election aftermath assessment (per card genre: eve-of-election news report) — no chart data supplied in card\nsystems_used: fact-priority event judgement across the question's three stated faces (no chart available; none fabricated)\nFaces in card: three-part question (winner / who actually takes the presidency / what follows); race facts (Biden leads most polls on the eve); process facts (mail-in voting disputes; warnings the loser may not accept the result — both supplied in the card and used as the derivation base for parts 2 and 3). The aftermath reading is anchored strictly on those two supplied process facts rather than on any invented configuration: a pre-announced non-acceptance posture plus a slow mail-in count yields a contested-but-completed transfer as the centred outcome. Confidence split reflected in the single figure: high on the winner, moderate on the severity of the flashpoint.",
 "confidence": 0.65, "trigger": T()}

PRED["WP-013"] = {
 "prediction_text": "Prediction: Labour under Keir Starmer wins the UK general election of 4 July 2024 — a large Labour victory and majority, with the governing Conservatives under Rishi Sunak reduced to a heavy defeat. Direction single and final: Labour. The card's polling face (Labour ahead by roughly twenty points) is in this case taken at face value: a lead of that size, sustained to within a fortnight of polling day in a snap election the incumbent side itself called from weakness, is not the soft-lead pattern that reverses; the supplied colour (Sunak's D-Day early-departure criticism) points the same way — a campaign compounding incumbent damage. The election falling in Cancer is noted as the card's only astrological datum; it is colour, not derivation, and is not dressed up as one. Timing unit: election day (fixed by the question).",
 "basis": "tradition=western mundane/political astrology (per card genre: Jessica Adams election post) — minimal chart data supplied\nsystems_used: fact-priority event judgement; the single supplied astrological datum (election in Sun-sign Cancer) recorded but not used as derivation\nFaces in card: question (winner, UK general election 4 July 2024); polling face (Labour lead ~20 points); campaign face (snap election called 22 May; Sunak criticised over D-Day departure); astro face (election in Cancer — declared colour only). Anchor treatment: unlike the soft-lead cases, this lead is wide and late; the face reading is adopted, with the reason for not reversing stated in the prediction. No charts are supplied and none are fabricated.",
 "confidence": 0.75, "trigger": T()}

PRED["YM-002"] = {
 "prediction_text": "断：兄弟之病可愈，终局向愈（单一终局），但病程缠绵、愈后防一反复。盘面：天火同人之火山旅，初爻父母卯木动化辰土、五爻妻财申金动化未土。用神兄弟午火居四爻：未月得相、与月建午未相合而暂绊，忌神官鬼亥水居世爻而临甲子旬空（戌亥空）、休囚无力——近段（本旬内）忌神落空，病势不进、平稳向愈，此为近段结论。远段：原神父母卯木发动生用，却被日辰申金所克、又被五爻申金动来克伤（仇神临日而动），生源受损；待亥水出空填实之期（出旬后亥日一带），忌神得值，防病势一反复——远段触发为五爻申金动化未土、仇势不解与亥水出空两项。两段合成终局：愈（愈期在解法之日）。病位：病之官鬼亥水居三爻，爻位主腰腹下焦、五行水主肾与膀胱下焦，两路同指下焦水道之疾（六神朱雀临之，只作旁注）。应期（日档，近病尺度）：窗口为本旬内至出旬之初，主坐标取寅日——寅冲五爻申金（冲去克原神之仇神，为解法日），原神得解则病向愈落定；亥日为忌神填实之反复点，只作远段警示不作愈期。",
 "basis": "tradition=liuyao（卡内 tradition 字段已给 liuyao；盘面全给：未建甲子旬壬申日，同人变旅）\nsystems_used: 六爻纳甲（用神兄弟午火；病占原神存续判别、病位取象复核、应期三步＋疾病门类对表）\n动化方向：卯木化辰土——化神辰土→用神午火为被生（泄用），非回头生克；申金化未土——未土生申金为回头生，仇神得生增力。方向定性：无四类吉向动化直指用神，定性以四路合参为准。反转条件：源绝子链核——原神卯木休囚、临未月入墓、无日月生扶、被申金动克三征近齐，但子链第①项须原神化退且化绝，卯化辰非化绝，子链不全成立，只降格不翻转。\n四路：本气＋（午火未月相、月合有气）／元忌仇0（原神动生用而受仇克、忌神空而暂解）／动化−（仇神回头生、原神化泄，只调量级）／世应不计（代占看用神）；合参方向：成／愈向。对象对齐：所问对象＝占者之兄弟；用神＝四爻兄弟午火；应验对象＝兄弟本人，同一。病占复述：愈否、病势、病位三断主语逐条对回『兄弟』，无错位。应期对表：疾病门首选对位（动空/化空冲空实空）本盘用神静而不空，无点；次选『冲去克神之日』对位近之——克原神之申金被寅冲，取寅日，已在断语注明查表路径。原神存续：源减未绝（有根三征仅根蒂一线、源绝三征因化绝一项缺失不作源绝论）。",
 "confidence": 0.5, "trigger": {"changed_main": False, "reserve_used": False, "disputed": False, "reason": "主用神兄弟午火为现卦唯一兄弟爻、取用无两现无争议（disputed=false）；用神未改定、终局未翻转（changed_main=false）；未取伏神、未保留应验位候选（reserve_used=false）。"}}

PRED["YM-003"] = {
 "prediction_text": "断：占官不得，升迁无望，终局向败（单一终局）。盘面：山地剥之风山渐，戌建甲辰旬庚戌日。用神官鬼巳火居二爻（应）：戌月休囚、戌为火墓，官星入月墓，又生月日戌土而泄气，本气无根。原神妻财卯木居三爻发动，然甲辰旬卯空（寅卯空）、卯戌相合绊住，更化申金——申为木之绝地、且回头克卯木：原神动而化绝自伤，生官之源已绝。五爻子孙子水（世）发动本为忌神，却化出官鬼巳火（忌化用）：曾有一线近官之象（名义/暂代之机），只作降格余地，不成终局之成。两路权重以旺衰日月为最高：用神休囚入墓、原神化绝无根无回头生，源绝判据链四项全成立，终局按源绝改定为败。应期（月档，官职迁转尺度）：窗口为戌月至亥月，主坐标取亥月——亥冲巳火用神，官星被冲散、不得之应落定（败局取败应一路，与终局自洽）。",
 "basis": "tradition=liuyao（卡内 tradition 字段已给；戌建甲辰旬庚戌日，剥变渐）\nsystems_used: 六爻纳甲（用神官鬼巳火；用神候选枚举、动化定性裁决表、终局反转扫查源绝子链、应期三步）\n用神候选枚举：现卦官鬼巳火（二爻）定主；变爻官鬼巳火（子水所化）与主用同支同亲，保留应验位（见 trigger）；日月戌土非官鬼之亲，不入。动化方向：卯木化申金——化神申金克本爻卯木为回头克，且申为木绝，属化绝；子水化巳火——化神巳火被本爻子水克，属忌化用。方向定性：忌化用本为吉向（裁决表第2步④），静态表象只调量级。反转条件：源绝子链逐项——①原神化退且化绝（卯化申绝）✓②无回头生（申金克木不生）✓③原神无根无气（旬空、戌月休囚、卯戌合绊）✓④用神无自救（巳火休囚入月墓）✓，四项全成立，复核后按扫查口径翻转终局为败，忌化用只留『曾近官』之降格。\n四路：本气−／元忌仇−（原神化绝、忌神动）／动化＋（忌化用，已被反转条件压过并注明）／世应不计（自占仕途，世非用神）；合参方向：败。应期对表：功名门类对表仅『发案挂榜』以父母为用神，与本题官职迁转门类不合，明写对表无此门类，按三步＋D项定亥月。对象对齐：所问＝占者本人仕途，用神官鬼，应验落占者本人，同一。",
 "confidence": 0.58, "trigger": {"changed_main": False, "reserve_used": True, "disputed": False, "reason": "主用神仍为现卦二爻官鬼巳火、未改定（changed_main=false）；取用按现卦优先次序明确、无两读争议（disputed=false）；变爻官鬼巳火（子水化出）与主用同亲同支，按候选枚举第3步保留应验位，故 reserve_used=true。终局之翻转出自反转扫查源绝子链，非主用神变更。"}}

PRED["YM-004"] = {
 "prediction_text": "断：子病可愈而迟，终局向愈（单一终局），愈在伏神出伏之期。盘面：火地晋之山地剥，甲辰旬戊申日（原书未记月建，旺衰月一层无从判，已注明）。用神子孙不上卦，变爻无子孙、日支申金非子孙之亲——按次序取伏神：乾宫首卦初爻子孙甲子水，伏于本卦初爻父母未土之下（飞神未土克水为飞来克伏之形）。然伏神得日辰申金之生（申为水之长生、日生伏）、又得四爻兄弟酉金（世）发动生水：伏有力一面成立；飞神未土未空未破、遮压未开：飞开一面未成——两条件只具其一，断伏神待出、半出待应。近段：子孙伏藏，病势缠绵未解、药力未达；远段：待冲开飞神之丑日，伏神出则病见转机，触发为日辰冲飞（丑冲未）一路。病位：动化克用之戌土（世爻酉金化出）居四爻、五行土主脾胃，爻位四爻胸腹脾胃区，两路同指脾胃/胸腹之疾。应期（日档，近病尺度）：窗口为本旬（甲辰旬）内，主坐标取丑日——冲飞神未土，飞开伏出、病愈之应（走合流D项冲起日首选一路）。",
 "basis": "tradition=liuyao（卡内 tradition 字段已给；甲辰旬戊申日，晋变剥；月建卡内明注未记，月一层旺衰无从枚举，已降置信）\nsystems_used: 六爻纳甲（用神取伏神子孙子水；飞伏有用无用清单、伏神待出四项判别、病占两段式、病位取象复核）\n伏神待出四项：①伏得生扶/临值✓（日申生伏）②飞神空破墓绝✗（未土无空破据，月建缺失不臆断）③动爻生伏✓（世酉金动生）④冲飞之路✗（盘中无冲未之爻，待应期丑日）——满足2项、根基项①在，定『待出』档，不直断已出成事。动化方向：酉金化戌土——戌土生酉金为回头生（原神自救之象），化神戌土→伏神子水为克（土克水），记为远段之压、只调量级。反转条件：源绝三征——原神酉金得日申同气之扶、动化回头生，有根有源，源绝不成立。\n四路：本气＋（伏神得日生、以日与动爻论，月层缺失已注）／元忌仇0（飞神克伏而伏得双生）／动化＋（原神回头生）／世应不计（代占看用神，世为原神另计于路2）；合参方向：愈向（迟）。对象对齐：所问对象＝占者之子；用神＝伏神子孙子水；应验对象＝其子本人，同一。病占复述：愈否、病势、病位主语逐条对回『子』，无错位。应期对表：疾病门首选对位为动空/化空之冲空实空，本盘用神伏藏非空，对表无伏藏对位，明写后回三步＋D项取冲飞之丑日。",
 "confidence": 0.48, "trigger": {"changed_main": False, "reserve_used": True, "disputed": False, "reason": "主用神一经取定未改（changed_main=false）；取用次序（变爻无→日月非亲→伏神）明确无争议（disputed=false）；用神子孙不上卦，按飞伏次序取伏神甲子水为用神，属启用伏神一路，故 reserve_used=true。"}}

PRED["YM-005"] = {
 "prediction_text": "断：占官可成，迁转得遂，终局向成（单一终局），量级为寻常迁转、非显擢骤升。盘面：泽水困（六合）之泽泽兑（六冲），子建甲戌旬戊寅日。用神官鬼午火居三爻：子月临死地，然得日辰寅木之生（日生用神），休囚而有扶。原神妻财寅木即世爻，临日建（寅日）、发动生官，且动化官鬼巳火——原神化出用神本身，原化用之局，生官之源与官星同气。忌神子孙亥水居应爻，子月旺相而静，只作量级之压（在位有同僚水势之阻），不动不克成局。仇神兄弟酉金临甲戌旬空（申酉空）、静而无力。六合变六冲：事以合起、以冲终——迁转可成而任所/后续仍有再调之象，只调量级不翻方向。应期（月档，官职迁转尺度）：窗口为巳月至午月，主坐标取巳月——巳为化神填实之月、兼冲去忌神亥水之解法月（巳亥冲），两路合流同指，先于一般逢值取之；午月（用神逢值）为备选，只入 reasoning。",
 "basis": "tradition=liuyao（卡内 tradition 字段已给；子建甲戌旬戊寅日，困变兑，飞伏章例）\nsystems_used: 六爻纳甲（用神官鬼午火；候选枚举、动化定性裁决表、应期三步＋合流D项）\n用神候选：现卦官鬼午火（三爻）定主；变爻官鬼巳火（世化出）保留应验位（见 trigger）；日月子水、寅木非官亲。动化方向：寅木化巳火——木生火，化神受本爻生、且化出用神之亲，属原化用；化神巳火→世寅木为被生、→用神午火同亲相助。方向定性：原化用为吉向（裁决表第2步同旨），六冲卦象等静态表象只调量级。反转条件：源绝三征不成立（原神临日发动、化用有源）；化退/化绝无生扶一路不成立（世化火非退绝）。\n四路：本气＋（休囚得日生扶，按路1定义记＋）／元忌仇＋（原神临日动生、忌神静、仇神空）／动化＋（原化用）／世应不计（世即原神，已并入路2，不重复计）；合参方向：成。应期对表：迁转门类对表无条（发案挂榜以父为用不合），明写无此门类，按三步＋D项：解法日（巳冲亥）与填实（巳化神）合流取巳月；逢值午月同尺度相距一步不对决、按D项首选序取巳。对象对齐：所问＝占者本人官职，用神官鬼，应验落本人，同一。",
 "confidence": 0.6, "trigger": {"changed_main": False, "reserve_used": True, "disputed": False, "reason": "主用神为现卦三爻官鬼午火、未改定（changed_main=false）；取用无两读争议（disputed=false）；变爻官鬼巳火（世爻化出）按候选枚举保留应验位、且其填实之月被取为应期主坐标，故 reserve_used=true。"}}

PRED["YM-007"] = {
 "prediction_text": "断：出门之子尚存，终局向存（单一终局：人存）。盘面：风地观之泽地萃，辛卯年丙申月甲戌旬丙子日。用神子孙不上卦现爻，变爻有子孙——四爻父母未土（世）动化子孙亥水，按『变爻有用神不取伏神』次序，用神即此化出之亥水：申月金生水为相、日辰子水比助，用神有气有源。忌神父母未土两现（初爻应、四爻世），世爻未土发动克亥水，然未土申月休囚、克力有限；且用神正出自世爻之化——父占子，世化出子孙，主其子由父之卦中显形、生机自世而来。上爻妻财卯木动化未土，卯木申月临绝、化土被本爻克，不碍用神主线。近段：子在外平安无恙；音信一层：亥水用神逢值之日（亥日）可得确信，窗口在本旬内（日档，主坐标亥日，用神逢值一路；冲实、填实两路无空可冲、无空可填，明写无候选）。对象复述（行人类准病占例）：存亡与音信两断主语逐条对回『子』（占者出门之子）本人，非迎候者，无错位。",
 "basis": "tradition=liuyao（卡内 tradition 字段已给；丙申月甲戌旬丙子日，观变萃）\nsystems_used: 六爻纳甲（用神取变爻子孙亥水；候选枚举次序、动化定性裁决表、对象对齐复述）\n用神候选：现卦无子孙；变爻子孙亥水（世化出）按黄金策次序定主，不入伏神；日月申金、子水——子水支以坤？本卦乾宫，子水为子孙之亲，日辰同亲一路与变爻同指亥子水系，作同向佐证并记。动化方向：未土化亥水——化神亥水被本爻未土克（本爻克化神），非回头生克；亥水→世未土为被克。方向定性：变爻出用神、用神得月生日报助，定性以四路为准。反转条件：源绝不成立（原神金即月建申、生源在月）；伏神引拨不适用（用神非伏）。\n四路：本气＋（亥水申月相、日比助）／元忌仇0（忌神未土动而休囚、原神在月建）／动化0（世化出用神，非四吉向亦非退绝）／世应不计（代占看用神）；合参方向：存。应期对表：存亡近行人门，行人首选对位（伏藏/动/化退）本盘用神属变爻化出、无对位点，明写后按三步取逢值亥日。对象对齐：所问对象＝占者之子；用神＝变爻子孙亥水；应验对象＝子本人，同一。",
 "confidence": 0.58, "trigger": {"changed_main": False, "reserve_used": True, "disputed": False, "reason": "主用神一经取定未改（changed_main=false）；取用依变爻优先次序明确、无争议（disputed=false）；用神子孙不现于现卦六爻，按次序取变爻化出之子孙亥水为主用神，属现卦之外取用一路，故 reserve_used=true。"}}

PRED["YM-008"] = {
 "prediction_text": "断：考秩得中平之等，不失其位，终局向成（保位）而量级偏低（单一终局）。盘面：泽地萃静卦，亥建甲子旬丙寅日。用神官鬼巳火居二爻（世）：亥月临绝地，然得日辰寅木之生、寅亥相合（日生合用神），绝处有扶。原神妻财卯木居三爻，亥月得水生为相、日寅比助，静而有气，虽静不发动，生官之源在盘。忌神子孙亥水居四爻临月建而旺，恰临甲子旬空（戌亥空）——旺而逢空为假空待出：本旬之内忌神落空、不克用神，考秩可安然过关；待出空之后（下旬亥水值日一带），忌神填实克官，远段防考语见绌、上司见责之反复，触发为亥水出空填实一线。近远两段合成终局：本轮考秩中平保位。应期（月档，考核迁转尺度）：窗口为亥月内至次年巳月，主坐标取巳月——巳火用神逢值、得生旺之气，考成定等之期落此（逢值一路；冲实一路亥冲巳为忌神值方，与成向相悖舍弃；填实一路无空可填，明写无候选）。",
 "basis": "tradition=liuyao（卡内 tradition 字段已给；亥建甲子旬丙寅日，萃静卦）\nsystems_used: 六爻纳甲（用神官鬼巳火；真空/假空判别、两段式、应期三步）\n动化方向：静卦无动爻、无化出之神，记『无动化』；方向定性：无动化定性，以四路合参定方向。反转条件：三类信号俱无（无伏、无化进、原神卯木静而有气非源绝），初判维持，扫查记录在此。假空判别：忌神亥水——假空判据①旺相有根（临月建）✓②临值月建✓，真空判据不足，判假空待出，只转应期不作废爻。\n四路：本气0（用神月绝而得日生合，旺衰中平）／元忌仇0（原神静有气不生、忌神旺而空暂解）／动化0（静卦）／世应不计（世即用神，并入路1）；路1、路2俱0而路4不计——按合参末则本应记方向存疑，然用神得日生合之扶为路1内已计之生扶、忌神落空为路2内已计之暂解，两扶对两弱，终局以『中平保位』降置信落定（置信0.45即此故），不以六神卦象补定。应期对表：考秩门类对表无条，明写无此门类，按三步取逢值巳月。对象对齐：所问＝占者本人考秩，用神官鬼世爻，应验落本人，同一。",
 "confidence": 0.45, "trigger": {"changed_main": False, "reserve_used": False, "disputed": False, "reason": "静卦、用神官鬼巳火为现卦唯一官爻且持世，取用唯一无争议（disputed=false）；无改定（changed_main=false）；未取变爻/伏神、无应验位保留（reserve_used=false）。"}}

PRED["YM-009"] = {
 "prediction_text": "断：摇会可得，此会标得归己，终局向成（单一终局）。盘面：地水师静卦，辰建甲寅旬甲寅日（日月同支寅，日建临值）。用神妻财午火居三爻（世）：辰月得相气（春末火进），日辰寅木生之、寅午半合火势——用神得日生合，旺相有气。原神子孙寅木居初爻，临日建、与用神半合相生，生财之源贴身有力。忌神兄弟亥水居五爻，辰月休囚、静而不动，克财之力弱；仇神父母酉金居应爻，静而无援。世财居中、原神临日合生、忌神休囚静伏——得会之局。应期（月档，会社按月开标之尺度）：窗口为本月至午月，主坐标取午月——妻财逢值之月，标会落定（逢值一路；冲实一路无空墓可冲、填实一路无空可填，均明写无候选）。量级：得会顺利、中途无兄弟劫标之变（忌神无力故也）。",
 "basis": "tradition=liuyao（卡内 tradition 字段已给；辰建甲寅旬甲寅日，师静卦）\nsystems_used: 六爻纳甲（用神妻财午火；四路合参、求财门应期三步）\n动化方向：静卦无动化，记无动化；反转扫查：三类信号俱无，初判维持。\n四路：本气＋（午火辰月相、得日生合）／元忌仇＋（原神临日合生、忌神休囚静）／动化0（静卦）／世应不计（世即用神并入路1；应父母不生不克世，不另计）；合参方向：成。应期对表：求财门首选对位『财临日月重叠待入墓』本盘财不临日月、无点；次选『世动逢合』世静无点——对表两点俱无，明写后回三步＋D项，D项四路（冲起/出墓/解法/实空）俱无候选，取逢值午月。对象对齐：所问＝占者本会得否，用神妻财世爻，应验落占者本人，同一。",
 "confidence": 0.62, "trigger": {"changed_main": False, "reserve_used": False, "disputed": False, "reason": "静卦、用神妻财午火现卦唯一且持世，取用无争议（disputed=false）；无改定（changed_main=false）；无变爻/伏神取用、无应验位保留（reserve_used=false）。"}}

PRED["YM-010"] = {
 "prediction_text": "断：产在即日，临盆应于占日当日（巳日）之内，母子向安（单一终局：顺产）。盘面：天风姤之火风鼎，午建甲子旬己巳日。用神子孙亥水居二爻：午月临死、又临甲子旬空（戌亥空），然占日巳火正冲亥水——空爻逢日冲，冲空则实：子孙被日辰冲实而发动，正是临产发动之机。原神兄弟申金居五爻发动生水，化未土回头生（土生金），生源在动中续力；酉金原神居三爻静而待援。忌神父母丑土（世）、戌土（上爻，戌亦旬空）克水之力受空与月火牵制。产期对表对位：子孙静者逢值逢冲、空者冲空实空之日——巳日冲空实空，两对位同指占日。应期（日档，临产尺度）：窗口为巳日至亥日数日之内，主坐标取巳日（当日）——冲实一路胜出；亥日（子孙逢值）为对决败者，只入 reasoning。母体一线：世爻父母丑土午月得相、无动克之伤，产母平安之象与子孙冲实同向，分判同安。",
 "basis": "tradition=liuyao（卡内 tradition 字段已给；午建甲子旬己巳日，姤变鼎，产期章例）\nsystems_used: 六爻纳甲（用神子孙亥水；真空/假空判别、产期门类对表、应期对决、对象分判母/子）\n动化方向：申金化未土——未土生申金为回头生，原神得生续力；化神未土→用神亥水为克，然未土先自生其本爻，原神生水之链不断，记量级之压不翻定性。方向定性：原神动而生用神为吉向。反转条件：源绝三征不成立（原神动化回头生、有根在申酉）。假空判别：亥水——假空判据②得生扶（申金动生）✓④逢冲则实（巳日冲亥）✓，判假空待出，冲日即出。\n四路：本气0（子孙月死旬空而逢冲实、得动生，旺衰与状态相抵记0偏＋）／元忌仇＋（原神发动回头生、忌神一空一受制）／动化＋（原神回头生）／世应不计（世为产母，另行分判不入合参）；合参方向：产而安。应期对决：巳日（冲实）与亥日（逢值）同为日尺度、相距逾一步进，触发对决——闸门项：子孙闸门为旬空，巳冲实、亥填实皆为开释机制各记平；天然视野项：临产近事日档，两候选皆合各0；合流项：巳日兼日辰本身冲空（与占日同体，为对表『空者冲空实空之日』正对位）——按裁决序同分回原序，对表对位序中冲空实空先于逢值，取巳日。对象对齐：所问对象＝临产妇人及其胎；用神子孙主胎、世父母主母体，两条线分开断、分开写，应验各落其人，同一性逐条已核。",
 "confidence": 0.6, "trigger": {"changed_main": False, "reserve_used": False, "disputed": False, "reason": "用神子孙亥水为现卦唯一子孙爻，取用无争议（disputed=false）；主用神未改定（changed_main=false）；变爻化出父母未土非用神之亲、未保留应验位，未取伏神（reserve_used=false）。"}}

PRED["YM-012"] = {
 "prediction_text": "断：子将归，归期在卯日，终局向归（单一终局）。盘面：泽天夬之泽风大过，酉建甲子旬甲子日。用神子孙酉金居五爻（世）：临月建（酉月）而旺，日辰子水泄之无大伤，本气旺相。忌神火不上卦，无克用之神；原神兄弟辰未之土静而生金，生源在盘。初爻妻财子水临日发动，化丑土而受回头克（土克水）、兼子丑相合——财爻为行人盘缠消息之象，动而化合绊，主行程已在途中、耗于盘缠牵绊，只调量级（归迟速）不翻归否。行人门类别读法：用神静而旺者，静待冲动——归期取冲动用神之日。应期（日档，近归尺度）：窗口为本旬（甲子旬）内，主坐标取卯日——卯冲酉金，静而旺之用神逢冲则行、则至（冲实一路）；酉日（用神逢值）为对决败者入 reasoning；填实一路无空可填，明写无候选。对象复述：归否与归期两断主语逐条对回『子』（占者之子）本人，非迎候者，无错位。",
 "basis": "tradition=liuyao（卡内 tradition 字段已给；酉建甲子旬甲子日，夬变大过，独发章例而动爻非用神）\nsystems_used: 六爻纳甲（用神子孙酉金；行人门类别读法、应期三步＋行人门类对表＋应期对决）\n动化方向：子水化丑土——化神丑土克本爻子水为回头克，兼子丑合（合绊）；化神→用神酉金为生（土生金），财化土生子孙之原神，记同向佐证。方向定性：用神本身无动化，定性以四路为准；财爻回头克只涉行程量级。反转条件：三类信号俱无，初判维持。\n四路：本气＋（酉金临月建旺相）／元忌仇＋（忌神火不上卦、原神静生）／动化0（用神无动化；旁爻动化不入路3主项）／世应不计（世即用神并入路1）；合参方向：归。应期对表：行人门首选对位（伏藏/动逢合/化退）本盘用神静旺无对位点；次选『用神三合取冲开、入墓取开墓、动空取实空』亦无对位——明写对表无点，回三步＋D项：D项四路无冲起/解法（无飞伏空墓），三路取冲实（卯冲酉，静者待冲）。应期对决：卯日与酉日同尺度相距逾一步进——闸门项用神无闸门状态各0；天然视野项近事日档皆合各0；合流项皆无各0；三项皆同分，回原序（静者待冲在逢值之前）取卯日，留痕在此。对象对齐：所问对象＝占者之子；用神子孙酉金（世）；应验对象＝子本人，同一。",
 "confidence": 0.58, "trigger": {"changed_main": False, "reserve_used": False, "disputed": False, "reason": "用神子孙酉金现卦唯一且持世，取用无争议（disputed=false）；主用神未改定（changed_main=false）；动爻为妻财、非用神候选，未保留应验位，未取伏神（reserve_used=false）。"}}

PRED["YM-013"] = {
 "prediction_text": "断：妻病危重，终局向凶——恐难痊愈（单一终局）。盘面：山天大畜之风天小畜，午建甲子旬己巳日。用神妻财两现：五爻丙子水（应）发动、初爻甲子水静——两现取动舍静，主用神定五爻子水。子水午月临死、无申酉金原神在卦（原神金全然不上卦，亦无变爻金），休囚无根无源；更动而化巳火——巳为水之绝地，用神动化绝。忌神兄弟辰土（三爻）、戌土（四爻，戌临旬空）土党克水，辰土午月得相、静而有力。病之官鬼寅木居二爻（世）与上爻。近段：用神临死化绝，病势沉重、药石难达（原神不上卦即医药无源之象）；远段：原神无从填实之期可待、忌神土党待午火生助之日更盛，无转机触发可指——两段同凶，合成终局。危期（日档）：窗口为本旬内，主坐标取午日——午为月建值日、火旺生土（生助克神之日，正合疾病对表『休囚者生助克神之日为危期』对位），病危之应落此。病位：官鬼寅木主爻取临世之二爻——爻位二爻主下腹/腿区、五行木主肝胆筋目，两路交于肝胆下腹之区落断（上爻寅木象头目，作旁注）；对象逐条对回『妻』，病位只落妻身。",
 "basis": "tradition=liuyao（卡内 tradition 字段已给；午建甲子旬己巳日，大畜变小畜，独发章例）\nsystems_used: 六爻纳甲（用神妻财子水两现取动；决策序终局三类条件、病占两段式、病位取象复核、疾病门类对表）\n用神候选：妻财两现（五爻动、初爻静），过标记互比——五爻动而无空破、初爻静，舍静用动定主；初爻无空破标记，落选所据为静爻比较项，不保留应验位（见 trigger）。动化方向：子水化巳火——化神巳火被本爻子水克（本爻克化神），然巳为水绝地，属化绝；化神临日建（巳日）有力而与用神相战。方向定性：用神化绝、无回头生。反转条件核：源绝子链须原神化退且化绝——本盘原神根本不上卦、无原神动爻，子链第①项无从成立，记『无此信号』，不以源绝翻转（初判本即凶向，无待翻转）；伏神、化进两信号俱无。三信号俱无，初判维持。\n四路：本气−（子水月死、无根、无日月生扶）／元忌仇−（原神不上卦、忌神土党得月相）／动化−（用神化绝）／世应不计（代占看用神）；合参方向：凶。终局断危之门槛：决策序第7步三类——用神休囚无气✓、无原神生扶且忌神得月生助✓、动化绝✓，三类同具，故敢断危重难愈，不作死字绝对语（留『恐难痊愈』表述）。对象对齐：所问对象＝占者之妻；用神妻财子水；应验对象＝妻本人，同一；病占复述：愈否、病势、病位、危期四断主语逐条对回『妻』，无错位。应期对表：疾病门次选对位『休囚者生助克神之日为危期』正中，取午日（月建值日、火生土），闸门释放无冲突（用神无空墓合闸门）。",
 "confidence": 0.55, "trigger": {"changed_main": False, "reserve_used": False, "disputed": False, "reason": "用神两现按两现章舍静用动定主、无取用争议（disputed=false）；主用神未改定（changed_main=false）；落选之初爻妻财无空破标记、未保留应验位，未取伏神（reserve_used=false）。"}}

PRED["YM-014"] = {
 "prediction_text": "断：家宅不致成火灾，终局向安（单一终局：火患不发生，仅虚惊小扰）。盘面：乾为天（六冲）之风天小畜，未建甲寅旬戊午日。用神父母（家宅）两现：上爻壬戌土（世）、三爻甲辰土（应），取世爻戌土为主——戌土未月比和得相、日辰午火生之，用神旺相有气，宅体无伤。火险之神官鬼午火居四爻，临日建（午日）而动，然动化父母未土：火生土、化出宅神本身——火势一动即泄归宅神，且化神未土与月建同支，火入土而熄之象。六冲卦只主其动、其散：火象动而即散，不成燎原。近段：占日午日火神值日发动，防灶火、电火一类小火光虚惊（当日/近日，具体项：物品为灶火电器之属）；远段：化神未土填实后火势全泄，无后续火患之触发。应期（日档）：窗口为本旬内火旺之日（巳午日），主坐标取午日（占日，火神值日而动化泄尽之日，虚惊应此）。对象核对：应验对象为家宅本身（非人对象），火灾之断只落宅、不回收到家人身上。",
 "basis": "tradition=liuyao（卡内 tradition 字段已给；未建甲寅旬戊午日，乾变小畜，家宅占）\nsystems_used: 六爻纳甲（用神父母戌土（世）；火神官鬼午火动化复核、量级守恒准用——所问为火灾之虞，量级止于宅火）\n用神候选：父母两现（上爻世、三爻应），家宅占以世居之戌土为主用神（占者所居之宅体），三爻辰土为同宅之应位旁参，落选所据为世应主从，不涉空破、不保留应验位（见 trigger）。动化方向：午火化未土——火生土，化神受本爻生；化神未土→用神戌土同土比和、→世为生入宅体。方向定性：火神动化宅神、泄而不克用，为解象。反转条件：三类信号俱无，初判维持。\n四路：本气＋（戌土月比和、日生）／元忌仇＋（火神动而化泄归用、克宅之金申静而不克土）／动化＋（化出用神之亲父母）／世应计（家宅兼宅人两方？本题只问宅之火患，应父母辰土与世同亲同向，记同向佐证不另定方向）；合参方向：安。应期对表：家宅门类不在对表内，明写对表无此门类，按三步日档取火神值日午日。对象对齐：所问对象＝占者家宅；用神父母戌土；应验对象＝家宅本身，同一（非人对象已按通则f落断）。",
 "confidence": 0.6, "trigger": {"changed_main": False, "reserve_used": False, "disputed": False, "reason": "用神父母两现按世应主从取世爻戌土、无争议（disputed=false）；主用神未改定（changed_main=false）；旁参之三爻辰土无空破标记、未保留应验位，未取伏神（reserve_used=false）。"}}

PRED["YM-015"] = {
 "prediction_text": "断：功名可成而不在本年——乡举之期在三年后酉年之科，终局向成（迟成，单一终局）。盘面：山地剥之火地晋，壬午年巳建甲戌旬甲戌日。用神官鬼巳火居二爻（应）：临月建（巳月）而旺，本气极强，功名本体有据。原神妻财卯木（三爻）巳月休、卯戌合绊，生官之力迟滞；忌神子孙子水（世）巳月临绝、静而无力克官。关键在文书：父母戌土居四爻发动，化兄弟酉金——甲戌旬酉空（申酉空），父母动而化空：榜文之神动而落空，主本年（壬午年）乡试名落/报迟，功名之期被化空之神推后。待酉金出空填实、逢值之年，文书得实、官星临旺之局方成——乡试逢酉之年正为下科（乙酉年），两路合流同指。应期（年档，功名远期尺度）：窗口为壬午年至乙酉年，主坐标取乙酉年（化神酉填实值年＋乡试科年，两机制合流；冲开一路卯冲酉，卯年非乡试之年、与功名科期尺度不合，舍弃并注明；逢值一路巳年官旺而文书未实，舍弃并注明）。",
 "basis": "tradition=liuyao（卡内 tradition 字段已给；壬午年巳建甲戌旬甲戌日，剥变晋，独发章例）\nsystems_used: 六爻纳甲（用神官鬼巳火兼父母文书；化空待实、应期三步＋功名门类对表＋对决）\n动化方向：戌土化酉金——土生金，化神受本爻生；化神酉金→用神巳火为被克（火克金）、→忌神子水为生（金生水，量级之压）。化神旬空，按决策序第5步：父母非用神本身，其化空只转应期（待填实），不否定官星旺相之终局方向。方向定性：用神旺相无动化，定性以四路为准。反转条件：化进待冲成局信号核——化出者为父母化空、非用神化进，不适用；源绝不成立（原神卯木休而有合绊、非化绝）；三信号俱无翻转项，初判维持。\n四路：本气＋（巳火临月建旺）／元忌仇0（原神合绊迟滞、忌神绝而静）／动化−（父母化空，只压应期与量级，不翻方向——已按裁决表量级规则处理）／世应不计（自占功名，应为官鬼用神已入路1）；合参方向：成（迟）。应期对表：功名发案挂榜门对位『空与入墓必待冲开、破与旬空须期填实』——父母化空一路正合『须期填实』，取填实之酉；与乡试科年（酉年科）合流后按对决合流项胜出（巳年逢值无第二机制合流），主坐标定乙酉年。对象对齐：所问＝占者本人功名，用神官鬼，应验落本人，同一。",
 "confidence": 0.55, "trigger": {"changed_main": False, "reserve_used": False, "disputed": False, "reason": "主用神官鬼巳火现卦取定、未改（changed_main=false）；取用无争议（disputed=false）；父母化空之填实期被用作应期主坐标，属应期机制而非用神候选之应验位保留，未取伏神，故 reserve_used=false（此界定已在此注明）。"}}

PRED["YM-017"] = {
 "prediction_text": "断：访友可遇，遇期在卯日，终局向遇（单一终局，迟遇）。盘面：天山遁之水泽节（六合），未建甲辰旬丙午日，五爻动而独三爻兄弟申金静——本章独静之例。友之定位：应爻五爻兄弟壬申金亦静？盘列五爻兄弟壬申金为应而不动，三爻兄弟丙申金亦静——卦中五动一静之『独静』落在三爻申金（五爻申金与之同支同亲，并读为友之静位）。独静只定应期：友静待冲待值。世爻官鬼午火居二爻发动，化妻财卯木回头生（木生火）——世动求友、化神回生，主我方诚意有归；然卯木临甲辰旬空（寅卯空），化神落空待实：遇期被推至卯木出空填实之日。用神（友/应申金）未月得土生为相、日午火克之而力有限。应期（日档，近事尺度）：窗口为本旬至出旬（约七日之内），主坐标取卯日——出旬后卯木填实、世化之神得实而遇友（填实一路，兼为闸门开释：世化空之闸门以填实开释）；申日（独静爻逢值）为对决败者，只入 reasoning。动化裁决记录：动化方向——世午火化卯木回头生，定性吉向；反转条件——源绝/化退化绝无生扶两路俱不成立（卯木空而非绝、且回头生世）。",
 "basis": "tradition=liuyao（卡内 tradition 字段已给；未建甲辰旬丙午日，遁变节，独静章例）\nsystems_used: 六爻纳甲（应爻兄弟申金为友；独静定应期、动化定性裁决表留痕、应期对决）\n动化方向：初辰土化巳火（土被火生、化神受生）、二午火化卯木（回头生）、三申金化丑土（回头生）、四午火化申金（化出兄弟友亲，火克金为本爻克化神）、上戌土化子水（化神受克泄）。与主线相关者：世化回头生（吉向）、四爻官化兄弟（友亲化出之佐）。方向定性：世动化回头生定性吉向，静态表象（五动之乱）只调量级（迟）。反转条件：不成立（逐项：化神卯木旬空非化绝、有回头生，源绝子链第①②项即破）。\n四路：本气＋（申金未月相、得土生）／元忌仇0（原神土众静生、忌神火动而化兄弟分流）／动化＋（世化回头生）／世应计（访友为兼彼此之事：应申金不克世、生合谈不上，记0不拖方向）；合参方向：遇（迟）。应期对表：访友门类对表无条，明写无此门类，按三步＋独静法。应期对决：卯日（填实）与申日（逢值）同为日尺度、相距逾一步进——闸门项：世化卯空为闸门，卯填实正好开释＋1、申不释放−1，闸门项卯胜，不待后项，主坐标定卯日，留痕在此。对象对齐：所问对象＝所访之友（应爻兄弟申金）；世为占者本人；遇之应验落于友与占者相会一事，承受/应验同一（相会事件），已核。",
 "confidence": 0.52, "trigger": {"changed_main": False, "reserve_used": False, "disputed": False, "reason": "用神友位（应爻/独静申金）取定明确、无两读争议（disputed=false）；主用神未改定（changed_main=false）；未取伏神、无落选候选保留应验位（reserve_used=false）；申日仅作应期对决败者入 reasoning，非用神应验位。"}}

PRED["YM-018"] = {
 "prediction_text": "断：子将归，归期在卯日，终局向归（单一终局）。盘面：火泽睽之泽山咸，巳建甲子旬乙丑日，五爻动而独四爻子孙酉金（世）静——独静章例，独静之爻即用神本位。用神子孙酉金：巳月临死地，然得日辰丑土之生（日生用神），休囚而有扶；独静定应期：静者待冲——卦中二爻官鬼卯木正发动（卯冲酉之爻已动，冲意已发），归期取卯木逢值之卯日，冲动独静之用神则行则至。三爻兄弟丑土动化子孙申金（土生金、化出子孙，回头生链）、五爻兄弟未土动化子孙酉金（化出用神同支）——子孙两路化出，与用神同气，主子在外平安、归意已成，只作同向佐证。应期（日档，近归尺度）：窗口为本旬（甲子旬）内，主坐标取卯日（冲实一路：卯冲酉，静而逢冲则至）；酉日（用神逢值）为备选入 reasoning（冲意已由动爻卯木先行，逢冲序在逢值之前）。对象复述：归否、归期两断主语逐条对回『子』（占者之子）本人，无错位。",
 "basis": "tradition=liuyao（卡内 tradition 字段已给；巳建甲子旬乙丑日，睽变咸，独静章例）\nsystems_used: 六爻纳甲（用神子孙酉金（世，独静）；独静定应期、行人门类别读法准用、对象复述）\n动化方向：初巳火化辰土（化神受生）、二卯木化午火（化神受生；卯木→用神酉金为克，然卯为冲用之爻，其动主冲起不主克断）、三丑土化申金（土生金、化出子孙）、五未土化酉金（化出用神本身）、上巳火化未土（化神受生）。方向定性：子孙两路化出、用神有出处，定性吉向；世（用神）本身静，动化定性只调量级（平安佐证）。反转条件：三类信号俱无（用神非伏、化出非用神化进待冲之局、原神土动化生非源绝），初判维持。\n四路：本气0（酉金月死而得日生，记0偏＋）／元忌仇＋（原神兄弟土两动化生子孙、忌神火动化土分流不克金成局）／动化＋（子孙化出两路）／世应不计（世即用神并入路1）；合参方向：归。应期对表：行人门对位——用神静者无首选对位，次选精神类推『静而逢值逢冲』，本盘冲用之卯木已动于二爻，冲路先于值路，取卯日；对决核：卯日与酉日相距逾一步进，闸门项用神无空墓闸门各0、合流项卯兼动爻已发之冲（第二机制同指）＋1，卯胜，留痕在此。对象对齐：所问对象＝占者之子；用神子孙酉金（世）；应验对象＝子本人，同一。",
 "confidence": 0.58, "trigger": {"changed_main": False, "reserve_used": False, "disputed": False, "reason": "用神子孙酉金现卦独静之位取定明确、无争议（disputed=false）；主用神未改定（changed_main=false）；化出子孙申金/酉金只作同向佐证、未立应验位，未取伏神（reserve_used=false）。"}}

BATCHES = {"B19": ["MP-017","MP-018","MP-019","OC-001","OC-002","OC-003","OC-004","OC-005","OC-006","OC-007","OC-008","OC-009","OC-010","OC-011","OC-012","OC-013","OC-014","OC-015","OC-016","OC-017"],
"B20": ["OC-018","OC-019","OC-020","OC-021","OC-022","OC-023","OC-024","OC-025","OC-026","OC-027","OC-028","OC-029","OC-030","WP-001","WP-002","WP-003","WP-004","WP-005","WP-006","WP-007"],
"B21": ["WP-008","WP-009","WP-010","WP-011","WP-012","WP-013","YM-002","YM-003","YM-004","YM-005","YM-007","YM-008","YM-009","YM-010","YM-012","YM-013","YM-014","YM-015","YM-017","YM-018"]}

def main():
    batch = sys.argv[1]
    ids = BATCHES[batch]
    written = []
    for cid in ids:
        p = PRED[cid]
        obj = {"case_id": cid, "prediction_text": p["prediction_text"], "basis": p["basis"],
               "confidence": p["confidence"], "trigger": p["trigger"]}
        path = os.path.join(OUT, cid + ".json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=1)
        written.append(path)
    # self-verify exact ids only
    for cid in ids:
        path = os.path.join(OUT, cid + ".json")
        with open(path, encoding="utf-8") as f:
            o = json.load(f)
        assert set(o.keys()) == {"case_id","prediction_text","basis","confidence","trigger"}, cid
        assert o["case_id"] == cid
        tg = o["trigger"]
        assert set(tg.keys()) == {"changed_main","reserve_used","disputed","reason"}, cid
        assert isinstance(tg["changed_main"], bool) and isinstance(tg["reserve_used"], bool) and isinstance(tg["disputed"], bool)
        print(cid, os.path.getsize(path))
    print("OK", batch, len(ids))

if __name__ == "__main__":
    main()
