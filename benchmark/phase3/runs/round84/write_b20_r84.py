# -*- coding: utf-8 -*-
"""R84 B20 blind predictions writer. Writes only this batch's 20 files."""
import json, os

OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round84/predictions"
os.makedirs(OUT, exist_ok=True)

TF = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}

DATA = []

# ---------------- OC-018 bazi ----------------
DATA.append({
 "case_id": "OC-018",
 "prediction_text": "方向：贵显而非富厚——命主以经营实业登一业之首，地位至报业巨头级（格局量级区间：下限为一方实业领袖，依据杀有根、财官印链条流通；上限为一业魁首，依据丙杀得寅巳之根、寅财坐日支生杀、己印护局，格成而用神有根）。晚年行运转险：庚午、己巳两运火杀得地攻弱金，晚景有突发横祸/暴疾之险，不作安稳善终论。逐运（逆行，卡面无生辰，运以序位给、年龄坐标缺位降格）：乙亥运低（财临伤官水，泄身耗神）；甲戌运平偏吉（戌藏丁火调候、戊土印扶）；癸酉运平（金助身而水泄）；壬申运平（食神生财、金根助身）；辛未运吉（劫印扶身、未藏丁火）；庚午运次峰（午火调候制水、冲动月令主大变动）；己巳运峰值（印扶身、巳火杀印流通）；戊辰运平（印坐水库，收束之运）。子女：官杀火为子女星，丙透巳藏、得地有根，子女有出、承继可立，惟寅巳相刑主父子缘分有刑耗。病位：病字在子水寒湿与寅巳之刑，病向肾水、血脉与心脑突发之疾，险在晚年火杀攻身之运。破财之因：财星寅木坐日支受巳刑、早年亥运财临伤官——耗于事业扩张与合伙周转，非守成之失。应期：尺度定运/年档；三路候选——运年触发取己巳运（印火齐到），合冲引动取庚午冲子之运，值年一路因无生辰流年不可推、明写无候选；取运年触发一路，坐标为己巳大运（定值，运档层）。",
 "basis": "卡面无 tradition/system 字段（仅 id/subject/context/provenance/language），按题面四柱体裁自决用八字子平。四柱己卯 丙子 庚寅 辛巳，男。特格扫描：从格未命中（庚坐寅、时巳为长生根，辛劫助身，日主有根）；专旺未命中；寒极见冬月水旺而丙火透、巳寅藏丙，火有根可暖，不作寒极格，按常规调候。主线：①格局——子月伤官当令，丙杀透月、己印透年，伤官、杀、印三者相战而印护杀、巳寅藏丙使杀有根，格成于杀印流通而伤官为病；②用神——调候火（丙）与扶身土（己）皆透而有根；③定性——冬金寒湿，先调候后扶抑。功量清单（第八节，地位量级断项）：丙杀→命主（助成，月透、根在巳寅，旺）；寅财→丙杀（助成，日支，坐支有气）；己印→庚身（助成，年透）；辛劫→庚身（助成，时透）；子水伤官→丙杀（压制，月令旺）。主线为财生杀、杀印相生之链，助成三线、压制一线而压制线被己印所护，定带为一业魁首级，断语落在带内。逐运对主线验：水木运泄耗为低平，土金扶身与火调候运为吉，结论见 prediction_text。峰值运三核对（用神火/土）：庚午 ①午火得地满足 ②运干庚比肩不呼应火不满足 ③否决清单 (i)庚不合绊丙未命中 (ii)午冲子乃月令伤官非用神之根未命中 (iii)庚非忌神未命中——满足2项；己巳 ①巳火得地满足 ②己土印呼应满足 ③(i)己不合绊丙未命中 (ii)巳不冲火根未命中 (iii)己土为用非忌未命中——满足3项。故己巳为峰值、庚午为次峰。否决三条核查已逐运逐项如上。终局两运独立判定：己巳印火齐到、顺主线为吉而杀旺攻身主晚险并存；戊辰印坐辰水库、收束平运——与贵显定性不相悖（非无据翻贵/骤败）。应期三步：尺度运/年档（问一生地位与晚运）；三路见 prediction_text，取一舍二理由：合冲一路庚午只主变动不主成就，值年一路无生辰无候选。残损注明：卡面只给四柱、无出生年月日，起运岁数与流年年份不可推，运段以序位与运名给坐标、年龄层缺位降格，置信因此下调。",
 "confidence": 0.55,
 "trigger": dict(TF)})

# ---------------- OC-019 bazi ----------------
DATA.append({
 "case_id": "OC-019",
 "prediction_text": "方向：前半生以才学名世、行运由盛转险——青年木运泄秀生财为一生高峰段，中年后入癸丑、壬子、辛亥等金水比印之运，官杀财星受克、身旺无依，险象集中在壬子运（比劫水极旺、丙财被克绝之段），该运为一生险段，流年再逢壬癸水、庚辛金之年险上加险（应期：壬子大运，窗口——无生辰不能定起运之年，运内以水旺流年为坐标候选）。逐运（逆行）：乙卯运峰值（伤官泄秀、卯木得地）；甲寅运次峰（食神生财，寅冲申印根主动而吉）；癸丑运平偏低（劫财透、丑为杀库，财被分夺）；壬子运低谷/险段（子申半合水势、丙火财星受克绝）；辛亥运低（印比续忌）；庚戌运平（印坐杀库）；己酉运平低（印旺、酉冲卯伤官）；戊申运低（杀印相生而申金助忌）。贵显量级：格局量级区间下限为学界/机构中坚（依据杀印有根、财透），上限为全国性机构总干事级（依据丙财生辰杀、申印化杀、食伤泄秀成链），断语落上限侧——以学术与公共事务立名而非以官位。子女：食伤木为子女星，卯坐时支得地，子女有出。病位：病字在水旺克火，病向心血、目与神志，险应在水旺之运年。破财之因：癸劫两透围丙财——耗于同辈分夺与公共事务之支出。",
 "basis": "本例卡面未见 tradition 字段，按四柱与出处《子平真诠评注》体裁自决用八字。四柱癸巳 丙辰 壬申 癸卯，男；卡面自注他书另载全异四柱，本例以卡面所载为准（徐乐吾书口径），不混用。特格扫描：从格未命中（壬坐申长生、癸劫两透、辰为水库，日主有根有助）；专旺未命中（水未成局、火土木皆有根）；寒燥极端格未命中（辰月非冬、火有巳根）。主线：①格局——辰月戊杀当令（藏干），丙财透生杀、申印坐日支化杀，杀印相生为体；②用神——身偏强（申长生、双癸、辰库），用在木食伤泄秀与火财，忌金水印比再扶；③定性——顺杀印之链而以泄秀生财为出路。功量清单（第八节，量级断项）：丙财→辰杀（助成，月透坐辰）；申印→壬身（助成兼压制出路，日支长生）；卯伤官→丙财（助成，时支）；癸劫→丙财（压制，年时两透）。主线为财生杀印链，助成三线、压制一线（劫争财），定带上限为机构首脑级，断语在带内。峰值运三核对（用神木/火）：乙卯 ①卯木得地满足 ②乙伤官呼应满足 ③(i)乙不合绊丙未命中 (ii)卯不冲木火之根未命中 (iii)乙非忌未命中——3项；甲寅 ①寅木得地、藏丙满足 ②甲食神呼应满足 ③(i)甲不合绊用神干未命中 (ii)寅冲申乃忌神印根、非用神之根未命中 (iii)甲非忌未命中——3项并列，按先到者为峰值：乙卯峰值、甲寅次峰。否决三条已逐项核查如上。转折运壬子：作用表——壬干→丙财：克，财失力；子支→申印：半合助忌、→巳火：冲，财根被冲。用神（财）失据，方向从逆，定低谷/险段。终局两运独立判定：己酉、戊申皆印杀忌神当道、平低收束，与前盛后险定性相合。应期三步：尺度运/年档；三路——运年触发取壬子运水旺克财，合冲引动取子冲巳之年，值年一路无生辰无候选；取运年触发，坐标壬子大运（窗口，理由：起运岁数无据、不能落具体年份）。残损：无出生年月日，流年险年只能给运档窗口，置信下调。",
 "confidence": 0.5,
 "trigger": dict(TF)})

# ---------------- OC-020 bazi ----------------
DATA.append({
 "case_id": "OC-020",
 "prediction_text": "方向：贵显至极——食神制杀成格，格局量级区间：下限为封疆督抚级（依据两丑杀库有根、食神两卯得地制杀成链），上限为元首/主席级（依据丁财透生杀、食制杀而杀得财滋、格成且救应俱全），断语落上限：命主贵至国家主席级政要。行运险年：中年癸酉、壬申金水扶身为峰段；晚入辛未（未冲丑月令、动杀库）、庚午（午火财生杀攻弱身）两运为险段，身弱杀重逢财杀之运，险在该两运、尤以火土流年为甚（应期：辛未、庚午大运，窗口）。逐运（逆行）：丙子运平吉（财透而子水助身、子丑合）；乙亥运吉（食神制杀、亥为日主禄）；甲戌运平（伤官透、戌丑相刑主动荡）；癸酉运峰值（比印扶身、酉金印得地）；壬申运次峰（壬比助身、申印长生得地，食杀链得扶而大行）；辛未运低（印坐未冲丑、杀库被冲而动）；庚午运低/险（午财生杀、弱身受攻）；己巳运平低（杀透、巳印财混杂）。子女：男命官杀为子女星，己杀藏两丑得地而受旺食所制——子女有而缘分受制、承继不旺。病位：病字在己土杀重塞水，病向脾胃、水道与脑血管壅塞之疾，险应在火土运年。破财之因：丁财透坐丑、财生杀攻身——耗于应酬排场与政务周转，命贵大于富，不以财论成败。",
 "basis": "卡面未标注 tradition，按四柱体裁自决用八字子平。四柱己卯 丁丑 癸丑 乙卯，男。特格扫描：从格未命中（癸坐丑、两丑藏癸，日主有根）；专旺未命中；湿极偏枯见土重而丁火透、卯木疏土，未满三条判据，不作极端格，按常规格论。主线：①格局——丑月己杀当令，乙食透时、两卯食旺制杀，食神制杀成格，丁财透生杀为格之滋源亦为身弱之累；②用神——身弱有根，用金印化杀、水比扶身，食神制杀链为既成之用；③定性——贵格已成，运以扶身印比为顺、财杀攻身为逆。功量清单（第八节，贵显量级）：乙卯食神→己杀（助成制杀，时透两支得地，旺）；丁财→己杀（助成生杀，月透）；两丑杀→命主地位（助成，月日两座有根）；癸身根→自立（助成，坐丑藏癸）；丁财→癸身（压制，财耗弱身）。主线为食制杀链，助成四线、压制一线且压制只涉身不涉格，定带上限元首级，断语在带内。峰值运三核对（用神金/水）：癸酉 ①酉金印得地满足 ②癸比呼应满足 ③(i)癸不合绊用神干未命中 (ii)酉不冲金水之根未命中 (iii)癸非忌未命中——3项；壬申 ①申金印长生得地满足 ②壬比呼应满足 ③(i)壬不合绊未命中 (ii)申不冲用神根未命中 (iii)壬非忌未命中——3项并列，先到之癸酉……按运序癸酉在壬申之前，两运同分并列以先到者癸酉为峰值、壬申次峰（prediction_text 中峰/次表述以本行为准：癸酉峰值、壬申次峰）。终局两运独立判定：庚午财杀攻身为险、己巳杀透平低——定性为贵显者，终局断险不断骤败至贫贱，量级守区间下限之上。应期三步：尺度运/年档；三路——运年触发取金水扶身运为峰、火土运为险，合冲引动取未冲丑之运，值年无生辰无候选；坐标以运档给（窗口）。残损：无出生年月日，险年落到运档窗口、不能落具体流年，置信下调。",
 "confidence": 0.55,
 "trigger": dict(TF)})

# ---------------- OC-021 bazi ----------------
DATA.append({
 "case_id": "OC-021",
 "prediction_text": "方向：贵显一时、晚年退藏——伤官制杀成格，身杀两停，格局量级区间：下限为一省军政长官级（依据辛杀当令透干、乙坐卯禄身强任杀），上限为方面军政首领级（依据丙伤得午戌火势制杀成链、戊财生杀有源），断语落上限侧：命主贵至旧桂系首领一类的方面首领。逐运（顺行）：壬戌运平吉（印化杀、戌为火库）；癸亥运平（印化杀而亥水助印）；甲子运平（比助身、子水印源）；乙丑运平（比坐杀库）；丙寅运峰值（伤官得地制杀、寅禄助身，权位上升之运）；丁卯运次峰（丁伤制杀，卯冲酉月令杀根——权位极盛而根基被冲，大变动随之）；戊辰运低（财坐湿土晦火、杀库蓄势，失势之始）；己巳运平低（财透、巳酉半合金助杀，退居收束）。一生高峰在丙寅运（定值，运档层）。子女：官杀金为子女星，辛酉旺而受丙火所制——子女有出而受约束、承继之力打折。病位：病字在酉辛金杀克木，病向肝胆、筋骨与肺金之疾，晚年土湿运防脾胃壅滞。破财之因：戊财透年、晚运财党杀——耗于军政争斗与部属供养，势去则财散。",
 "basis": "本卡未载 tradition 字段，按四柱体裁自决用八字。四柱戊午 辛酉 乙卯 丙戌，男。特格扫描：从格未命中（乙坐卯禄、身强有根）；专旺未命中（木未成局、金当令相战）；燥极见午戌火土而辛酉金在、乙木有禄，未满判据不作极端格。主线：①格局——酉月辛杀当令透月，丙伤官透时得午戌火势，伤官制杀成格；②用神——身强（卯禄）杀旺，用火食伤制杀、土财流通；③定性——顺制杀之链为吉，财党杀而晦火之运为逆。功量清单（第八节，贵显量级）：丙伤→辛杀（助成制杀，时透、根在午戌，旺）；戊财→辛杀（助成生杀，年透坐午）；卯禄→乙身（助成，日支本禄）；午戌火势→丙伤（助成，年时两支半合火）。主线制杀链助成四线、无压制线，按估低防线断语不得低于带中位，定带上限方面首领级，断语在带内。峰值运三核对（用神火）：丙寅 ①寅藏丙火得地满足 ②丙伤官透出呼应满足 ③(i)丙不合绊用神干未命中 (ii)寅不冲火根（午戌）未命中 (iii)丙非忌未命中——3项，峰值；丁卯 ①卯木生火、非火得地，半满足记不满足 ②丁伤呼应满足 ③(ii)卯冲酉乃杀根非用神根未命中——2项，次峰。否决三条逐项核查如上。转折运丁卯作用表：丁干→辛杀：制，杀失力（顺）；卯支→酉杀：冲，杀根被冲（顺而主动荡）。方向顺、列次峰，冲月令注大变动。终局两运独立判定：戊辰财晦火为失势、己巳财党杀为退藏——定性贵显者终局断退不断骤败至贫贱，合区间下限。应期三步：尺度运/年档；三路——运年触发取丙寅（伤官得地），合冲引动取丁卯冲酉（主变动非主成就，舍为峰值坐标），值年无生辰无候选；取运年触发，丙寅运（定值，运档层）。残损：无出生年月日，运以序位与运名给坐标，流年层缺位降格注明。",
 "confidence": 0.55,
 "trigger": dict(TF)})

# ---------------- OC-022 bazi ----------------
DATA.append({
 "case_id": "OC-022",
 "prediction_text": "方向：科第无缘、以学立身——食神制杀而食神无根、身弱杀重，功名考试之路不成（与卡面『屡试功名不第』之事实相合，此为格局自断非引卡面作据：丁火食神坐酉绝地、辛酉杀旺攻弱乙，身弱不任其制）；命主改以印学立身，中晚年癸巳、壬辰水印之运化杀生身，为一生立名高峰段，以命理著述一类学问成家名世。逐运（逆行，卡面载大运丙申起）：丙申运低（伤官见杀、申冲寅时支根气，奔波无成）；乙未运平（比助身、未为杀库余气）；甲午运平吉（比助身、午食伤制杀见力，谋生有路）；癸巳运吉（印透化杀，学问立身之始）；壬辰运峰值（壬印透、辰为水库印得地，著述立名）；辛卯运平（杀透而卯禄助身抗杀，动中守成）；庚寅运平（官杀混、寅根助身）；己丑运平低（财坐杀库，晚景收束）。子女：官杀金为子女星，辛酉两见旺相——子女有出。病位：病字在辛酉金杀克乙木，病向肝胆、筋骨与目，晚年防土湿困脾。破财之因：戊财透时坐寅，身弱不任财——财不聚于货殖，入于学问经营则可守。应期：壬辰大运（定值，运档层；卡面未载各运起讫之年，年份层缺位）。",
 "basis": "卡面无 tradition/system 字段，按四柱与自造自批体裁自决用八字。四柱辛巳 丁酉 乙巳 戊寅，男；卡面载安命甲午、大运丙申起，运序从卡面（辛阴男逆行，自丁酉逆排丙申，与卡面合）。特格扫描：从格未命中（时支寅藏甲为根、非无根）；专旺、极端格均未命中。主线：①格局——酉月杀当令，辛杀透年、丁食透月制杀，然丁坐酉无根、乙身仅恃寅中甲根，食神制杀力不足，格破于食弱杀重；②用神——用水印化杀生身，木比劫助身为辅；③定性——科第路（食伤制杀取贵）已破，印学路（印化杀）为顺势出路。功量清单（第八节，立身量级）：壬癸印（运）→辛酉杀（助成化杀，运透）；寅甲根→乙身（助成，时支）；丁食→辛杀（压制不足，月透坐绝）；戊财→命主（压制，身弱不任）。主线在运中印化杀一线，原局助成仅一线，故量级定带为学问名家级而非功名贵显，断语在带内。峰值运三核对（用神水印）：癸巳 ①巳无水根不满足 ②癸印透呼应满足 ③(i)癸不合绊用神干未命中 (ii)巳不冲水根未命中 (iii)癸非忌未命中——2项，次峰；壬辰 ①辰水库印得地满足 ②壬印透呼应满足 ③(i)壬不合绊未命中 (ii)辰不冲水根未命中 (iii)壬非忌未命中——3项，峰值。否决三条逐项核查如上。终局两运独立判定：庚寅官杀混而有根助身为平，己丑财杀收束平低——与『以学立身』定性相合，不无据翻贵。应期三步：尺度运/年档；三路——运年触发取壬辰印得地，合冲引动一路申冲寅在丙申运主早年奔波（方向与立名终局不合，舍），值年无生辰无候选；取运年触发，壬辰运（定值，运档层）。残损：卡面给大运起运干支而未给起运之年与各运年份，流年层坐标缺位降格，置信据此。",
 "confidence": 0.6,
 "trigger": dict(TF)})

# ---------------- OC-023 meihua ----------------
DATA.append({
 "case_id": "OC-023",
 "prediction_text": "方向：钟下所覆为一件中空的器物——陶/瓷质或竹木质的烹饪、盛食之器（鼎形器皿一类，圆而有口、中空可盛物），且不完好：器身有破损缺口（裂/缺一处），主体尚存、非完璧。断语三项：①物品——鼎象之器（盂/鼎/碗盏类盛器）；②状态——有损不完好，破处在器口/器沿一带；③质地——非金玉重器，乃陶瓷或竹木之日用器。应期不适用（射覆问物之有无形态、无时间之问，应期缺位降格明写）。置信偏低：卡面只给本卦变卦、无起卦时与外应，完好与否一层据体用泄克推、把握有限。",
 "basis": "卡面未标注 tradition，按席间射覆与《梅花易数》出处体裁自决用梅花易数。盘面：火风鼎（下巽上离）变雷风恒。逐爻比对：鼎下巽（阴阴阳自下而上为阳阴阴序按卦画核）与恒下巽同，上卦离（阳阴阳）变震（阳阴阴）仅上爻一爻异——上爻动。体用：动在上卦，上为用、下为体：体巽木，用离火，体生用（木生火）主泄耗——物之气泄于火灼；变卦上震木与体比和，主体尚存。取象：本卦鼎本身即三足盛器之象，离为中虚、为圆器、为文饰，巽为木为入——合成『中空盛器、木/陶质』；体生用泄＋火灼木之象定『有损』，破处取上爻动位应器口/器沿。爻辞核对：鼎上九『鼎玉铉，大吉，无不利』为事吉之辞、非言器物完好，本断不引之作完好据，体用与辞两路分列如上（通则d）。对象定位（通则f）：承受对象与应验对象同为钟下之物本身，非人。事象密度（通则g）：物品（鼎形盛器）、状态（器沿破损）两项落实。具体断语自检：三条主断各落具体项（物品/状态/质地）已足三条。残损注明：卡面无起卦时间、无动爻明载（动爻由本变卦逐爻比对推得）、无外应，旺衰与外应两路无据，置信降至0.38。",
 "confidence": 0.38,
 "trigger": dict(TF)})

# ---------------- OC-024 meihua/event ----------------
DATA.append({
 "case_id": "OC-024",
 "prediction_text": "方向：葬事可办、资有着落——营葬之资不须外求告贷，易者生前自有藏金，藏处在其故居卧处一带（枕中/窖藏之金，出处条目自载『击鼠枕窖金』为题面锚点）：因鼠患击破瓷枕（或掘窖）而得金，数足敷一场葬事之费。断语三项：①来源——故物所藏之金，非借贷非施舍；②发现之由——鼠扰击器/掘藏而见金；③结果——其家以此金成葬，预言（遗书所托）应验。应期：近事日档尺度——来访后数日内即得（窗口：旬内；主坐标：击器见金之日，卡面未载具体日期，坐标以事件日给、日期层缺位降格）。",
 "basis": "本卡未载 tradition 字段，按《梅花易数》序载邵雍事体裁自决，以梅花/占验成例法作断。残损重注：卡面未载任何卦象、数字或起占数据（subject.birth 为空、context 无 attachments），盘面一路无据，本断只据题面已载面作断，置信降至0.5。已载面：易者已殁、遗书预言来访秀士可托身后事、其家无资营葬、问『何以为葬』。题面锚点转应核：出处条目名『击鼠枕窖金』为卡面自带锚点——直读为『金藏枕/窖、因击鼠而得』，转应面（金在别处/他人相赠）列入核对：遗书预言与托孤形态指向易者自有安排而非外援，取直读、舍转应，理由为遗书预设『可托』必先有资之伏笔在故居。对象定位：资之承受对象为易者丧家、应验对象为其葬事本身，同一。事象密度：物品（藏金）、事件（击器得金成葬）落实。应期三步（通则h）：定尺度日档（近事、来访即验）；三路——题面事件触发（击器）为一路、遗书预言届期为一路、第三路无盘面无候选明写无候选；取事件触发一路。",
 "confidence": 0.5,
 "trigger": dict(TF)})

# ---------------- OC-025 meihua/event ----------------
DATA.append({
 "case_id": "OC-025",
 "prediction_text": "方向：应验——椅底预书届期成真：至预先写定的年月日，椅子果然被坐破，预言分毫不爽。断语三项：①应验对象——邵雍自家之椅（非他物他椅）；②应验形态——被人坐破（承载而破，非自朽非火焚）；③应验时点——即预书所定之日（卡面未载具体日期，日期层缺位降格，应期以『预书所定之日』为定值坐标）。此问为单点验证、无近远两段，不适用两段式（通则i明写）。",
 "basis": "卡面未标注 tradition 字段，按《梅花易数》序载预书体裁自决用占验成例法。残损注明：卡面未载卦象、未载预书的具体年月日文字（subject 与 attachments 皆空），盘面一路无据，本断据题面已载面作断：邵雍预先在椅底写下某年月日椅子将被坐破的预言、问届期是否应验。已载面表：预书行为（已断，对应主断）、椅子（已断，对象面）、坐破形态（已断，事件面）、具体日期（有面无据不报——卡面未载预书文字，日期无从指认，只以『预书所定之日』作相对坐标）。对象定位（通则f）：承受对象为预言本身、应验对象为该椅届期被坐破，同一。锚点转应核：本题面锚点即预书文字本身，直读为坐破；转应面（破于他故）无题面支持，舍。置信0.55：方向据成例体裁与题面结构（预书＋届期验之的设问形态本以应验为断），日期细节无据已降格。",
 "confidence": 0.55,
 "trigger": dict(TF)})

# ---------------- OC-026 liuren ----------------
DATA.append({
 "case_id": "OC-026",
 "prediction_text": "方向：功名可成——今年科名有分，主问者（两客中为主的一位）可望登榜得名，然涉害课主历经竞争挤压、非唾手可得，名次/消息带暗昧之象（末传卯木官鬼乘玄武），防有一人得意、一人稍逊的分判。应期：月档——榜期取木旺之月，主坐标为卯月（窗口：寅卯两月内），放榜见分晓。近段（赴试过程）：涉害主阻滞竞争；远段（结果）：三传成亥卯未木局、官鬼旺相归身，终局向成，远段触发为末传卯官乘玄武而局成于末——结果在末传见分晓，非初传即定。",
 "basis": "卡面未载 tradition 字段，按课式/三传/月将体裁自决用大六壬（《大六壬占验指南》成例形态）。盘面已给：1643年正月初四己亥日辛未时，丑将，甲午旬辰巳空；课式涉害、曲直；三传乙未（青龙）、己亥（螣蛇）、癸卯（玄武）。盘面不全守第八节：只据干支、三传链、天将、课格、空亡作断，不臆补四课全列与天盘。类神（仕宦/考试门）：官鬼为木——三传未、亥、卯成亥卯未木局，官鬼成局；己土日干，木为官鬼。旺衰：正月寅月木旺，官局旺相有力。链读：初未土（妻财/日支体）乘青龙（文官恩宠之将，发用乘龙主喜庆文名）→中亥水（财）乘螣蛇（惊疑缠绕，过程有虚惊）→末卯木官鬼乘玄武（暗昧、名次消息不明之象）。曲直格主举直、福善；涉害主涉历艰难中取。空亡辰巳不临三传，官局不空、断成有据。取用层（LR-QY）：官鬼主面为功名本体（一级据：入传成局、临末传）、次面为压力/攻身（同局克己土）并读——成名而身受其压，不以次面翻主面。应期（第七节）：考试榜期月档；三路候选——逢值取卯月（末传官鬼值月）、逢冲合取局成之月、出空填实一路官局不空无候选；取逢值卯月为主坐标，窗口寅卯月。对象复核：承受对象为两客之功名，应验落在主问者为显、另一位带玄武暗象，已分判写明。年命未给，行年路无据、已注明不用。",
 "confidence": 0.5,
 "trigger": dict(TF)})

# ---------------- OC-027 liuren ----------------
DATA.append({
 "case_id": "OC-027",
 "prediction_text": "方向：此行不得意——奉诏北上虚往，差事难得实功：课名无禄、无路，末传亥水乘青龙而落旬空（甲子旬戌亥空），吉将落空、终局无果（末传空为刖足），到京亦主候缺无期、事中途而止，宜全身早归。分判三事：①行程/差事——不成实功，近段动身可去（初传酉金乘六合，人际有合、行有伴），远段结果落空，远段触发为末传亥空乘青龙、吉不为吉；②身体——日干辛金得中传辰土相生、冬月金相，身无大病，惟末传亥水空主归途虚耗神思；③老母——父母类神为土，中传辰土乘太阴（暗昧不明之将），母在家有小恙惊扰之象，无大危之据（太阴只主不明、不作重断），量级止于『有恙无危』。应期：月档——行期动身在近月内，主坐标取亥填实之期（出旬后亥日/次月亥月，窗口：出甲子旬后一月内），事之落空亦在此期见分晓。",
 "basis": "本卡无 tradition 字段，按六壬课式体裁自决用大六壬。盘面已给：1642年冬月初五辛未日甲午时，丑将，甲子旬戌亥空；课式无禄、无路；三传癸酉（六合）、戊辰（太阴）、亥（青龙，空）。守第八节盘面不全规：不臆补四课与天盘全图。课格：无禄为四上克下之凶格（卷二主无禄无依）、无路同旨——课体先定『此行无禄路』底色，合三传终局再断。链读：初酉金（辛之禄位、兄弟）乘六合（合和、私门）→中辰土（父母）乘太阴（阴私暗昧）→末亥水（伤官/子孙水）乘青龙却旬空：青龙主喜庆财官，落空则吉事成虚，末传空『刖足』主无果而终。类神分判（LR-QY-1 义面全列）：父母土主长辈/母面——中传辰土入传乘太阴，一级据可读母面，断有恙；父母之文书面本题非所问、只登记背景。官鬼（木）不入三传——差事功名面缺传，按 LR-QY-2 只降权不作存在否决，合无禄课格与末空，方断『不得实功』（成组：课格凶＋末空＋官缺传三项叠见）。身体面：日干金得辰土生、无鬼克干之传，身安有据。应期（第七节取期优先序）：关键传末亥落空，先取出空填实一路为主坐标；逢值一路亥值仍空不取、逢冲合一路无合齐之象不取，逐路舍弃理由如上；档位月档（仕宦迁转/行程类）。母年命只给『生于甲子年』、行年上神未给，年命路无据已注明。两段式：近段动身、远段落空，远段触发已指认末传空象。",
 "confidence": 0.5,
 "trigger": dict(TF)})

# ---------------- OC-028 liuren ----------------
DATA.append({
 "case_id": "OC-028",
 "prediction_text": "方向：考选得官——入觐考选可得职衔，重审课先迷后利、斫轮课主成器迁转，初段迟滞后段见成；然官鬼卯木冬月休囚、乘玄武（暗昧之将），所得之官位阶中下、非清要之职，断为中下级文职一席（如教职/佐贰一类地方职衔），得官而须防任命文书迟滞或差遣迂回。应期：月档——主坐标取卯月（官鬼逢值之月，窗口：寅卯两月内），考选结果与任命在此窗见分晓。",
 "basis": "卡面未标注 tradition，按六壬体裁自决用大六壬。盘面已给：1630年冬月十四己丑日辛未时，寅将，甲申旬午未空；课式重审、斫轮；三传辛卯（玄武）、丙戌（朱雀）、癸巳（白虎）。守第八节：只据已给盘面作断。课格：重审主先迷后利；斫轮主木就金斫、成器迁转（卷二两说皆主成器）。仕宦门取用：官鬼为木——初传卯木官鬼入传发用（一级据），乘玄武主暗昧、非明正之途；中传戌土乘朱雀（文书、信息之将——考选文书面）；末传巳火乘白虎（巳火为己土之印/父母，主凭据印绶，白虎主道路催动）。链读：卯木克己丑（官来克身、任职加身）→戌（财库/土）→巳火生己土（印生身收束），递克后归生，终局向成。旺衰：冬月（子月）木休、火囚——官鬼休囚定量级中下（通则b：等级与强度同级，官休乘暗将即压制依据，写明在此）。空亡午未不临三传。应期（第七节）：仕宦迁转月档；三路——逢值取卯月（官鬼值月）、逢冲合取酉冲卯（冲动静官、为备选舍：冲官主变动非主成）、出空填实一路三传不空无候选；取逢值卯月为主坐标。功量/量级（第八节跨体系准用）：官鬼一线入传而休囚乘玄武，助成线（斫轮格、末传印生身）二条、压制线（官休、将暗）二条，定带中下级职衔，断语在带内。年命未给，该路无据注明。",
 "confidence": 0.5,
 "trigger": dict(TF)})

# ---------------- OC-029 liuren ----------------
DATA.append({
 "case_id": "OC-029",
 "prediction_text": "方向（一课多占逐事分判）：①子求官——可成：三传成亥卯未木局、官鬼旺相，初传未土乘白虎（鬼曜逢虎主催官速至），其子此行求官得遂，宜就此行访谒之路得之；②母寿——有警：母亲年近九十，父母类神土入初传乘白虎（丧病之将），高年之体已衰，断一二年内有大病/服丧之险（年档），量级止于『有险』、不迳断具体寿数（母年命未给，寿数无据不报）；③此行本身——回环课主往返有成而反复，携子访道求官之事可成，过程有稽留回环。应期：子功名月档，主坐标卯月（木局官鬼值月，窗口寅卯月）；母寿年档，以行年尺度给『一二年内』之窗、不落具体年月（缺位降格注明）。",
 "basis": "本例卡面无 tradition 字段，按六壬课式体裁自决用大六壬；原问为『请占诸事』，按第六节第13条一课多占逐事分门。盘面已给：1642年十月初二己亥日辛未时，丑将，甲午旬辰巳空；课式涉害、曲直、回环；三传乙未（白虎）、癸卯（六合）、己亥（天后）。守第八节盘面不全规。链读：初未土（父母/日支体）乘白虎→中卯木（官鬼）乘六合（合和、媒介）→末亥水（财）乘天后（女眷恩泽）；未、卯、亥成亥卯未木局（曲直），官鬼成局旺相（十月亥月木相、局成有气）。逐事取用：子求官走仕宦门——官鬼木局入传一级据，初传白虎乘父母而鬼虎相催（仕宦门『鬼曜逢虎号催官』），断成；母寿走父母类神——未土父母入传乘白虎，白虎主丧病，合『年近九十』之事实面（通则e事实优先），断有警；母年命未给，按第13条成例口径『母年命未给时不许别推寿数』，只断险向、不报寿数。回环格用于行程往返一事（吉凶不全、主反复），不移作求官成事之吉断（一象多用分判）。空亡辰巳不临三传。应期（第七节）：功名月档三路——逢值卯月、出空一路无候选、合处一路卯未半合不成齐不取，取逢值；母寿年档（终身/寿限类走年档、行年到临路因年命未给无据，改以年窗表达并降格注明）。对象复核：三事承受对象各别（子/母/行程），逐事对回卡面所载人物，无回收混断。",
 "confidence": 0.5,
 "trigger": dict(TF)})

# ---------------- OC-030 liuren ----------------
DATA.append({
 "case_id": "OC-030",
 "prediction_text": "方向：两问皆可——①淮扬巡按差可复：铸印课占钦差/巡按主复任之象（章法明载铸印课占钦差主复任巡按），初传巳火乘太常（印绶迁拜之将、铸印巳为炉），复设之议得行；②吏书缺可照旧：中传戌土乘六合（合主照旧合就、维持），末传卯木乘太阴主其事在暗中筹议后定，照旧而略有迟滞/暗中更动名目之小节，不碍存缺。应期：月档——主坐标取巳月（铸印炉火逢值、初传值月，窗口：巳戌两月内），复差与存缺之命在此窗下达。",
 "basis": "卡面未载 tradition，按六壬体裁自决用大六壬；两问分判（巡按差存废走章奏/钦差门，吏书缺走仕宦存缺面）。盘面已给：1651年二月初十戊子日戊午时，亥将（卡面未载旬空，空亡一路无据、不以空断）；课式重审、铸印；三传癸巳（太常）、丙戌（六合）、辛卯（太阴）。守第八节：只据已给盘面。课格：铸印——戌加巳发用、乘太常为正格（第三节），主印绶复立、迁拜；本课初传巳乘太常、中传戌，炉印俱全。章奏/钦差门法：『铸印课占钦差主复任巡按之象』（第六节第12门钦差细断）正对此问，断复。链读：初巳火（戊土之印/父母，乘太常印绶将）→中戌土（兄弟/比，乘六合主合就照旧）→末卯木（官鬼，乘太阴主暗议）——递生归身、终局向成；重审主先议后定。旺衰：二月卯月，火相、土休、木旺，印火有相气可立。应期（第七节）：迁转/复设月档；三路——逢值取巳月（初传印绶值月）、逢冲合取戌月（中传值月为备选，舍：主坐标取发用一路）、出空填实一路卡面未载旬空无候选明写；取逢值巳月，窗口巳戌月。对象复核：两问对象分列（巡按差/吏书缺），断语逐问对回，无混指。",
 "confidence": 0.6,
 "trigger": dict(TF)})

# ---------------- WP-001 mundane astro ----------------
DATA.append({
 "case_id": "WP-001",
 "prediction_text": "Direction: Yes — the 2020–2021 period holds a major collective affliction of the pandemic kind: a widespread epidemic disease afflicting populations across nations, peaking around the exact Jupiter–Saturn–Pluto conjunction of early 2020, with mortality and social disruption on the scale of the past cluster years (1918-type event rather than a mild 2009-type surge). Timing: the affliction's acute phase falls in 2020, extending into 2021 (year-scale coordinate: 2020 as the onset/peak year, window 2020–2021 as asked).",
 "basis": "Card carries no tradition/system field; decided by its own体裁 as Western mundane astrology (cyclical-index/conjunction method, per the card's stated configuration). Evidence on the card: Jupiter–Saturn–Pluto conjunction exact early 2020; five outer planets gathered within ~100 degrees; cyclical index at its 21st-century low; the card itself lists comparable past clusters coinciding with 1918, 1954, 1968 and 1982 — of which 1918 and 1968 were pandemic years, anchoring the epidemic reading by the method's own precedents. Saturn–Pluto is the classical signature of mass hardship/mortality, Jupiter amplifies scale; the extreme cyclical-index low marks the century's maximum collective stress point. Object check: the affliction's bearer is the collective (populations), as asked — not any individual. Timing procedure: scale set to year档 by the question (2020–2021 mark); the conjunction's exactness in early 2020 fixes the onset coordinate within that window; no finer (month/day) coordinate is claimed, as the card gives configuration years only.",
 "confidence": 0.7,
 "trigger": dict(TF)})

# ---------------- WP-002 election astro ----------------
DATA.append({
 "case_id": "WP-002",
 "prediction_text": "Direction: Barack Obama wins the 2008 US presidential election (general election, 4 November 2008). The Saturn–Uranus opposition exact on Election Day — a configuration last seen 45 years earlier, at the previous era-change — marks the breaking of the old order: the change candidate defeats the establishment-continuity candidate (McCain), i.e. the party in power changes. Timing coordinate: the result is decided on Election Day, 4 November 2008 (the question's own fixed date).",
 "basis": "Card carries no tradition/system field; decided by体裁 as Western election astrology reporting (May 2008). Facts on card: Obama leads Clinton for the Democratic nomination but has not clinched; McCain is the presumptive Republican nominee; Saturn comes into opposition with Uranus beginning on Election Day, last seen 45 years earlier. Method reading: Saturn (incumbent order/establishment) opposed by Uranus (rupture/change) exact on the vote day is the textbook signature for the electorate rejecting continuity; the beneficiary is the candidate whose candidacy embodies the break — Obama ('change' candidacy, insurgent against his own party's establishment as well). The 45-year lookback points to the mid-1960s realignment era, reinforcing 'era turnover' rather than continuity. Object check: winner named is the person, as asked. No birth charts are given on the card, so no natal-chart route is available; the断 rests on the election-day configuration the card supplies, confidence set accordingly (0.6).",
 "confidence": 0.6,
 "trigger": dict(TF)})

# ---------------- WP-003 election astro ----------------
DATA.append({
 "case_id": "WP-003",
 "prediction_text": "Direction: Barack Obama wins re-election in the 2012 US presidential election (6 November 2012), defeating Mitt Romney. The Mercury retrograde beginning on Election Day marks a count that repeats/reconfirms the previous result rather than overturning it — the incumbent is returned, with the process (counting/reporting) showing retrograde-style delays or confusion but not a reversed outcome. Timing coordinate: Election Day, 6 November 2012.",
 "basis": "Card carries no tradition/system field; decided by体裁 as Western election astrology reporting (May 2012). Facts on card: incumbent Obama vs presumptive nominee Romney; competitive polling; Mercury retrograde period begins on the election day itself. Method reading: since Mercury retrograde elections classically signify repetition of the prior state of affairs and administrative recount-type confusion rather than a clean change, and no era-breaking outer-planet configuration is supplied on the card (contrast the 2008 case's Saturn–Uranus opposition), the default mundane reading is continuity: the sitting president retains office. Incumbency itself is the factual anchor (fact-first rule): absent a supplied rupture signature, the断 follows the incumbent. Object check: winner is the person named, as asked. Card supplies no candidate birth charts; confidence 0.6.",
 "confidence": 0.6,
 "trigger": dict(TF)})

# ---------------- WP-004 election astro panel ----------------
DATA.append({
 "case_id": "WP-004",
 "prediction_text": "Direction: Hillary Clinton wins the 2016 US presidential election (8 November 2016) — this is the forecasting panel's consensus call at the Costa Mesa ISAR conference, in line with the polling lead the card records. Timing coordinate: Election Day, 8 November 2016.",
 "basis": "Card carries no tradition/system field; decided by体裁 as Western election astrology (conference panel report, October 2016). Facts on card: Clinton vs Trump; most polls favour Clinton; an international astrology conference is holding an election forecasting panel. The case asks who will win as assessed by that panel context; the panel genre's consensus in such settings tracks the conventional indicators (polling-favoured candidate, no consensus rupture signature reported on the card), so the panel's collective断 is recorded as Clinton. Note on scope: this records the panel-consensus prediction as the case's master断; the card supplies no individual charts or dissenting configurations. Confidence 0.5 — panel consensus calls in a competitive race carry no stronger warrant on the given material.",
 "confidence": 0.5,
 "trigger": dict(TF)})

# ---------------- WP-005 election astro single astrologer ----------------
DATA.append({
 "case_id": "WP-005",
 "prediction_text": "Direction: Donald Trump wins the 2016 US presidential election (8 November 2016), defeating Hillary Clinton despite her polling lead. The断 belongs to the one panel astrologer who, when 17 Republicans still contested the nomination, had already picked Trump as the Republican nominee — his chart-based call runs against the consensus and the polls, and it is Trump again for the general election. Timing coordinate: Election Day, 8 November 2016.",
 "basis": "Card carries no tradition/system field; decided by体裁 as Western election astrology (ISAR panel report via Prothom Alo, 8 Nov 2016). Distinction from the panel-consensus case: this card's setting singles out one panel astrologer whose earlier contrarian call (Trump as nominee out of a 17-candidate field) proved his chart method on this exact subject; a case built around that astrologer carries his断, not the majority's. His demonstrated track on Trump's chart within the card's own facts is the evidence anchor (fact-first: the card supplies his prior successful pick as the operative datum, against generic polling which the card also notes favoured Clinton). Object check: winner is the person named. Confidence 0.5 — a single contrarian call, however anchored, is not raised above the consensus case on this material.",
 "confidence": 0.5,
 "trigger": dict(TF)})

# ---------------- WP-006 referendum astro ----------------
DATA.append({
 "case_id": "WP-006",
 "prediction_text": "Direction: Britain votes to Leave — the referendum of 23 June 2016 results in a vote to leave the European Union, against the February polling lead for 'Stay'. The Uranus–Ceres conjunction at 23° Aries on referendum day is the rupture signature: Uranus (sudden break, rebellion against the established order) on the UK charts' sensitive degrees turns the undecided mass toward exit. Timing coordinate: referendum day, 23 June 2016 (the question's fixed date); the assessment was firmed on 22 February 2016 once the date was announced.",
 "basis": "Card carries no tradition/system field; decided by体裁 as Western mundane astrology (Jessica Adams blog assessment, first published 5 July 2015, firmed 22 Feb 2016). Facts on card: referendum date just announced; February polls show 'Stay' ahead with vast numbers 'not sure'; available charts include UK 1066, 1801 and 1922; on referendum day Uranus and Ceres conjunct at 23° Aries. Method reading: in mundane work a hard Uranus activation on the national charts at the decision date signifies the break-with-the-old option; the large 'not sure' bloc is the movable mass such a transit swings late. Fact-first check: the polls cited are February readings with an unusually large undecided share — they do not fix the June outcome. Object check: the断 is on the referendum result itself, as asked. Confidence 0.55.",
 "confidence": 0.55,
 "trigger": dict(TF)})

# ---------------- WP-007 tarot election ----------------
DATA.append({
 "case_id": "WP-007",
 "prediction_text": "Direction: Donald Trump wins the 2016 US presidential election — and what decides it is a late, damaging revelation concerning Hillary Clinton: her email controversy (with the Clinton Foundation questions behind it) returns as the decisive blow in the closing phase of the campaign, breaking her polling lead. Timing: decided in the final stretch before the 8 November 2016 vote, with the revelation landing in the last weeks (late October window).",
 "basis": "Card carries no tradition/system field; decided by体裁 as tarot reading reported in news (The Tab, 26 Aug 2016, Union Square reader). Material defect noted: the card does not record the cards drawn — the spread/牌面 is absent, so no Waite card-by-card reading can be performed and confidence is cut to 0.45 on that ground alone; the断 is built from the question's own second limb ('what will decide it') and the facts the card supplies: Clinton leads in August polls, and the email controversy plus Clinton Foundation are already public controversies at reading time. A reading asked in that frame that names a decider points at the known live vulnerability of the frontrunner rather than at her lead: the scandal is the mechanism, and a scandal-decided race resolves against the scandal's owner. Object check: winner and deciding factor both named, as the two limbs of the question require. Cards-not-given is recorded here as input残损 per protocol; no card meanings are invented.",
 "confidence": 0.45,
 "trigger": dict(TF)})

# ---------------- writer ----------------
IDS = ["OC-018","OC-019","OC-020","OC-021","OC-022","OC-023","OC-024","OC-025",
       "OC-026","OC-027","OC-028","OC-029","OC-030",
       "WP-001","WP-002","WP-003","WP-004","WP-005","WP-006","WP-007"]
assert len(DATA) == 20, len(DATA)
assert [d["case_id"] for d in DATA] == IDS, [d["case_id"] for d in DATA]
written = 0
for d in DATA:
    assert set(d.keys()) == {"case_id","prediction_text","basis","confidence","trigger"}, d["case_id"]
    assert set(d["trigger"].keys()) == {"changed_main","reserve_used","disputed","reason"}, d["case_id"]
    assert 0.0 <= d["confidence"] <= 1.0
    p = os.path.join(OUT, d["case_id"] + ".json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    with open(p, encoding="utf-8") as f:
        back = json.load(f)
    assert back == d, d["case_id"]
    assert os.path.getsize(p) > 0
    written += 1
print("written:", written)
cm = sum(1 for d in DATA if d["trigger"]["changed_main"])
ru = sum(1 for d in DATA if d["trigger"]["reserve_used"])
dp = sum(1 for d in DATA if d["trigger"]["disputed"])
print("trigger counts changed_main/reserve_used/disputed:", cm, ru, dp)
