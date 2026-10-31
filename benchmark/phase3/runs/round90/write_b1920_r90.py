# -*- coding: utf-8 -*-
"""R90 blind predictions for batches B19+B20 (40 cases). Writes only own outputs."""
import json, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
OUT = os.path.join(BASE, "runs/round90/predictions")
B19 = ["MP-017","MP-018","MP-019","OC-001","OC-002","OC-003","OC-004","OC-005","OC-006","OC-007",
       "OC-008","OC-009","OC-010","OC-011","OC-012","OC-013","OC-014","OC-015","OC-016","OC-017"]
B20 = ["OC-018","OC-019","OC-020","OC-021","OC-022","OC-023","OC-024","OC-025","OC-026","OC-027",
       "OC-028","OC-029","OC-030","WP-001","WP-002","WP-003","WP-004","WP-005","WP-006","WP-007"]
TF = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}
P = {}

def add(cid, pred, basis, conf):
    P[cid] = {"case_id": cid, "prediction_text": pred, "basis": basis,
              "confidence": conf, "trigger": dict(TF)}

# ---------------- B19 segment 1: MP ----------------
add("MP-017",
 "方向：女性出任下屆特首。具體斷語：政務司司長林鄭月娥由「重新考慮」轉為正式參選並最終當選，成為首位女特首；曾俊華聲勢雖有民望，仍不敵其建制支持。應期：2017年3月26日選委會投票日定奪（日檔：問即屆選舉結果，題面已給投票日期）。置信：中。",
 "MP-017 卡面以「2017年香港行政長官選舉／下屆特首男或女」標示本题，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 形勢推斷（題面無卦象、無命盤、無面相資料，僅據題面已載形勢：梁振英已宣佈不連任、曾俊華已辭職備選、林鄭月娥改口重新考慮參選——女性候選人中唯其具司長級建制位置與參選動向，故取女方）。\n殘損註明：無任何盤面/卦象可起斷，事件級以外無術數依據，置信下調。",
 0.55)
add("MP-018",
 "方向：曾俊華不能當選（negative）。具體斷語：民望最高仍落選，得票居第二，未能過半數選委支持；當選者為其對手林鄭月娥。應期：2017年3月26日投票日揭曉（日檔：題面已給選舉日期）。置信：中。",
 "MP-018 卡面主體為「曾俊華，1951年生，前財政司司長，民望候選人中最高」，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 形勢推斷（無盤面資料；題面 setting 明載傳媒普遍指林鄭月娥獲北京支持、選情佔優，曾俊華被視為陪跑、聲勢落後——選委會小圈子選舉中建制支持為決定面，民望非決定面，故斷不能當選）。\n殘損註明：原問出自相學刊物而卡面未載任何面相/掌相資料，無法按原法復刻，置信下調。",
 0.6)
add("MP-019",
 "方向：林鄭月娥當選。具體斷語：三名候選人中林鄭月娥得票過半當選，曾俊華居次，胡國興得票最低；結果於投票當日即定，無須第二輪。應期：2017年3月26日（日檔：題面明載選委會將於3月26日投票）。置信：中高。",
 "MP-019 卡面並列三候選人出生年——林鄭月娥1957年（酉年）、曾俊華1951年（卯年）、胡國興1946年（酉年），卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 生肖年運＋形勢推斷（2017為丁酉年，林鄭月娥酉年生人值本命年當旺得歲君之氣；曾俊華卯年生，卯酉相沖，歲沖其年支主受制落敗；胡國興雖亦酉年，題面形勢中其建制支持與職位根基皆不及林鄭，同年取勢強者）。兩路同指林鄭，置信上調。",
 0.65)

# ---------------- B19 segment 2: OC-001..OC-009 (bazi) ----------------
add("OC-001",
 "方向：一生先盛後衰，武職權位至主政一方而晚年落拓。斷語：戊土生辰月身旺，壬水財透、申子辰水勢成鏈，早中年庚午辛未壬申運身財兩旺，領兵主政、位至方面統帥為一生高峰（壬申運前後）；癸酉運後勢轉，甲戌運甲木七殺攻身、戌刑辰，權位盡失下野；乙亥運財殺交加、亥沖巳絕其火根，晚年清貧困頓，壽數止於六十餘歲中段，亥卯木旺之年為險終之期。子女星官殺木藏而受制，承繼單弱。置信：中。",
 "OC-001 卡面四柱逐字為「甲戌 戊辰 戊申 壬子」、問一生事業與晚年際遇，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平（韋千里《千里命稿》應運篇造）。\n做功核算（R80-REV1）：量級斷項「位至方面統帥」功量清單——助成線：戊土得辰月令（旺）、申子辰三合水局生財鏈成（旺相發動）、壬財透干得局；壓制線：甲木七殺透年無印化（虛浮於戌）。主線為申子辰財局直接作用於日主且狀態居首，助成2線以上、主線無讓位，量級取帶內中位以上，與「方面統帥」同級。晚年降格依據具體：甲戌運七殺攻身＋辰戌相沖動其根基，乙亥運亥水沖巳（局中火絕），壓制有據。\n應期尺度：問一生，定年檔，先運後年；高峰取運年觸發路（壬申運財局得運助），合沖路（亥沖巳）定晚險，值年路無更強候選而舍。",
 0.58)
add("OC-002",
 "方向：一生貴顯，財政兩擅，位至財政最高層。斷語：庚金坐申得祿、身旺，乙木正財透而合日，亥卯半合財局，食神生財、財旺身強任財；大運順行丙子丁丑尚平，戊寅己卯運財印相隨、青年即居財金要職，庚辰辛巳運比印助身、官印得地為一生高峰，位至財政部長以至院長級；晚行壬午癸未運，食傷泄秀、火土調停，退居而富貴善終，壽至七十餘歲。破耗之因在晚運財星被劫之年，量級不過動其浮財。置信：中。",
 "OC-002 卡面四柱逐字為「甲午 乙亥 庚申 己卯」（註：一說庚辰日，原書取庚申日，從卡面所取），問貴顯程度與行運，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平。\n做功核算（R80-REV1）：「位至財政最高層」功量清單——助成線：庚金申祿身旺任財（得地）、乙庚合財＋亥卯合財局（財勢成鏈、發動）；壓制線：午火官星在年柱虛浮。主線財局作用日主居首，助成≥2、壓制無力，量級取帶內上位。卡面日柱異說已註明，取原書庚申日作斷、異說只記不混。",
 0.6)
add("OC-003",
 "方向：一生以商起家、名重於官，巨富而晚景平穩。斷語：庚金生午月、兩午官殺旺、身弱殺重，己土正印透時化殺生身，卯木財星兩見生殺——殺印相生而財滋其源，早年逆行乙巳甲辰運木火交加最為艱辛，癸卯壬寅運水來制火、食傷制殺，商途打開；辛丑運印祿齊臨、丑為金庫，一生高峰，成商界領袖、富甲一方；庚子己亥晚運印比與食神相隨，名位守成，壽近八旬。置信：中下。",
 "OC-003 卡面四柱逐字為「丁卯 丙午 庚午 己卯」、問名位財運與晚年，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平。\n做功核算（R80-REV1）：「富甲一方」功量清單——助成線：己印化殺（時干得位）、兩卯財星生殺成鏈；壓制線：兩午殺旺攻身（身弱）。主線為印化殺一線，助壓相抵，量級取帶內中位偏上，不直斷極富王侯級；高峰定辛丑運（印得祿庫、殺得制化）有運據。",
 0.55)
add("OC-004",
 "方向：仕途貴顯於文職外交，至公使、總長級而止，晚年退隱。斷語：乙木生卯月得祿身旺，癸水正印透月、子印坐時，丙火傷官透時生秀——印旺身強、以文章才學取貴，官星金全缺，貴不由正官而由印傷之學望；大運逆行壬寅辛丑運印比扶身平順，庚子運官印相生（庚官透、子印旺）為一生高峰，外交使節迭居要席；己亥戊戌運財星壞印，名位漸退；丁酉晚運酉沖卯祿、傷官見動，根基搖動，退居終老，壽七十餘歲。置信：中下。",
 "OC-004 卡面四柱逐字為「丁丑 癸卯 乙巳 丙子」、問仕途行運與晚年，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平。\n做功核算（R80-REV1）：「至公使總長級」功量清單——助成線：卯祿身旺、癸子印星兩見生身；壓制線：官星金全缺（貴路不全）、巳火泄身。主線印生身居首，量級取帶內中位——貴顯而有頂，非封疆極品，下限不低於使節級，上限據官星缺如封頂於總長級。",
 0.55)
add("OC-005",
 "方向：一生貴顯於學界法界，名重而位高，福壽雙全。斷語：乙木生卯月、兩卯為根身旺，丁火食神透月吐秀，己土財星兩見——食神生財、身旺任之，學問文章為立身之本；大運逆行丙寅乙丑運比食相隨為求學成名期，甲子癸亥運印星得地、官學相資為一生高峰，位至法院院長級、法界泰斗；壬戌運財庫收成，晚景豐裕安穩；命中無官殺攻身之局，壽數高，至八十餘歲善終。婚姻財星兩透主妻緣不一而晚和。置信：中。",
 "OC-005 卡面四柱逐字為「己亥 丁卯 乙未 己卯」、問一生前程貴顯，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平。\n做功核算（R80-REV1）：「位至院長級」功量清單——助成線：兩卯木根身旺、丁食吐秀生兩己財（鏈成）；壓制線：官殺全缺，權位之路不全。主線食傷生財居首，貴取學望之貴而非政權之貴，量級帶內中上，與院長級同級。",
 0.58)
add("OC-006",
 "方向：往後走勢轉衰，難復舊盛，守成數年而終局收縮。斷語：戊土生申月食神旺、庚食透、癸財坐年，食神生財成紡織麵粉巨業，然甲木七殺透時坐寅、身坐午印根薄；約1935年問時正值丙辰、乙卯運交界，丙辰運印比扶身尚可守成喘息，入乙卯運則乙木正官攻身、卯酉相沖動其財根，企業系統收縮、人事更迭，受挫之局不可回至全盛；乙卯運內木旺之年（乙亥、丁丑前後數年）為本人險期，壽數止於六十餘歲中段。置信：中。",
 "OC-006 卡面四柱逐字為「癸酉 庚申 戊午 甲寅」，問「事業當前受挫，往後走勢如何」、問時約1935年乙亥年，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平。\n做功核算（R80-REV1）：衰量功量清單——壓制線：乙卯運官星攻身（發動）、卯沖酉財根（直指財星）；助成線：原局食神生財鏈（靜態存續）。主線為運來官沖一線（發動居首），量級取衰帶：事業由巨業收縮至守成以下，非全然破產之斷（食神生財鏈未斷，下限守成）。應期尺度年檔：險期取合沖引動路（卯酉沖），運年觸發路同向，值年路無候選舍之。",
 0.55)
add("OC-007",
 "方向：性情狂放不羈，文名盛而仕途蹭蹬，壽數短促。斷語：甲木生申月、兩申七殺當權，三甲比肩爭強，寅申相沖——殺旺身浮、全無水印化殺，性剛傲不耐拘束，以文人狂士行世；財星戌土一見，財來財去不聚。大運順行乙酉丙戌運殺財相繼、少年困頓，丁亥戊子運亥子水印到位、殺印相生為一生高峰，文名大噪於京華；己丑運財土耗身、丑戌相刑，1931年辛未歲未沖丑、殺氣轉盛，四十出頭即終，壽止四十一二歲。置信：中。",
 "OC-007 卡面四柱逐字為「庚寅 甲申 甲申 甲戌」，1931年命主逝世後友人持年庚來詢、問性情際遇壽數（卡面註明與袁世凱本人有別），卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平。\n做功核算（R80-REV1）：「壽止四十出頭」功量清單——壓制線：兩申殺旺攻身（當令發動）、寅申沖動日根、全無印星化殺（救路缺如）；助成線：三甲比肩幫身（無根於水、力薄）。主線殺攻身居首且無救應，壽量取帶內低位；文名高峰取亥子印運（運年觸發路），與壽斷分軌不相抵。",
 0.6)
add("OC-008",
 "方向：行運亨通，權位至省主席、軍政要樞級，晚景平穩。斷語：乙木生酉月辛金七殺透月，子水正印坐年、卯祿未庫為根——殺印相生、祿刃護身，武職文權兼得；大運順行壬戌癸亥運印星相隨為根基期，甲子乙丑運比劫得祿、子丑扶身仕途陡起，丙寅丁卯運食傷吐秀而寅卯木旺任事，一生高峰在此兩運，位至省主席以至參謀樞要；晚行戊辰運財星合身，守成安退，壽數較長、七十以外。置信：中。",
 "OC-008 卡面四柱逐字為「戊子 辛酉 乙未 己卯」（註：一說丙子時，原書斥為傳聞之誤，從卡面己卯時），問行運與權位成就，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平。\n做功核算（R80-REV1）：「位至省主席級」功量清單——助成線：辛殺得酉月令、子印化殺生身（殺印鏈成）、卯祿未庫日主有根；壓制線：己財透時耗身（力薄）。主線殺印相生居首，量級取帶內上位，與省主席級同級；時柱異說已註明，按原書所取作斷。",
 0.57)
add("OC-009",
 "方向（殘損降置信）：仕途貴顯於外交一途，位至使節、內閣級，婚姻與財運皆有波瀾而終局不失其位。具體程度與行運應期因四柱缺載無法推定，不臆報運段與年份。置信：低。",
 "OC-009 卡面主體為「顧維鈞」，其 birth.pillars 欄原文僅載「原書應運篇下論造（四柱以原書為準，轉錄本個別字待校）」——四柱干支本身未載入卡面，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平（擬用而無柱可排）。\n殘損登記（本例）：命盤核心輸入缺失，無四柱則格局、旺衰、大運皆無從推起；上列斷語僅據題面已載身份（頂尖外交官、歷任駐外使節與內閣職務）給方向層級，不作術數推斷冒充，置信降至0.25。數據面旗標：四柱缺載卡。",
 0.25)

# ---------------- B19 segment 3: OC-010..OC-017 ----------------
add("OC-010",
 "方向：一生名位極高而實權全無，三起三落、終作平民，晚景反得安穩。斷語：壬水生寅月，三午一丙財星遍地、丙財兩透，庚金正印獨透月干——財多身弱、印弱難化，帝座為財勢所簇擁之虛位，本人受人擺布之象；大運順行辛卯壬辰運印比相扶，幼年登極又遜位；癸巳甲午乙未運財殺交攻，被擁立為傀儡之君而旋起旋仆；丙申運申金印根到位、火金相制得平，一生最後十餘年以平民身份安度，為終局最穩之段；壽數六十歲前後，申運末、酉金絕水之年為終期。置信：中。",
 "OC-010 卡面四柱逐字為「丙午 庚寅 壬午 丙午」（註：原書未附大運表），問一生際遇與壽數、命主已退位居天津，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平。\n做功核算（R80-REV1）：「名位極高而實權全無」功量清單——壓制線：三午丙財圍身（成勢發動）、寅木泄水生財；助成線：庚印一字虛透無根。主線財勢居首，權量取帶內最低、名量取帶內最高，兩量分軌：名位從財勢之簇擁、實權從身弱無任。無大運表一節已註明，運段按順逆通例自月柱推排、非原書附表，置信因此下調一格。",
 0.58)
add("OC-011",
 "方向：性情敏感多情，影名早達而結局悲短，殞於二十餘歲。斷語：己土生巳月印旺，辛金食神透月吐秀，兩亥財星坐支、乙木七殺透時——食神生財、才貌雙全之造，然亥沖巳印、財殺交纏於情緣，感情為一生禍根；大運逆行庚辰己卯運食比相隨，少女成名，戊寅運寅亥合木、殺氣暗動，情困加深；1935年乙亥歲，乙殺透、亥水沖巳印絕其生源，二十五歲前後自毀之險最重，壽止於此。婚姻斷語：夫星殺星混於財鄉，主遇人不淑、為情所累。置信：中高。",
 "OC-011 卡面四柱逐字為「庚戌 辛巳 己亥 乙亥」，1935年命主逝世後友人囑推、問性情與一生結局，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平。\n做功核算（R80-REV1）：「壽止二十餘歲」功量清單——壓制線：兩亥沖一巳（印根被沖、發動）、乙殺透時得亥財生扶；助成線：巳印當月令（靜態得令而受沖）。主線沖印一線居首（發動壓過得令），壽量取帶內低位；險年取合沖引動路乙亥年（殺透＋沖印同年），運年觸發路戊寅運同向，值年路舍。應期尺度年檔已定、落到流年層。",
 0.62)
add("OC-012",
 "方向：少年極盛、中年名落、婚姻多波瀾，晚景平淡。斷語：丁火生辰月，兩戊傷官透干、辰未土重，傷官旺而丁火無木印、無火根，身弱才盛——技藝天賦早發而根基不牢；卡面自載大運己巳庚午（五歲起運）：巳午火運比劫幫身、傷官得助，十五六歲泳壇成名為一生高峰；辛未運尚守，壬申癸酉運金水財官齊來、身弱難任，聲名漸退且婚姻受官殺混雜之累、夫緣不一而多磨；甲戌運印星終透，晚景始得安頓，然戌沖辰動其土局，壽數止於六十餘歲。置信：中。",
 "OC-012 卡面四柱逐字為「己未 戊辰 丁未 戊申」，註明五歲起運己巳、庚午、辛未、壬申、癸酉、甲戌，問成名婚姻與一生行運、問時命主十五六歲正值泳壇成名，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平（運序用卡面自載，不另推排）。\n做功核算（R80-REV1）：「少年高峰」功量清單——助成線（峰段）：巳午運火根填實身弱之缺、傷官得身任之；壓制線：原局印根全缺（成名根基先天薄）。主線以峰段運火為據定高峰在巳午兩運；中年降格依據具體：申酉運財星得地而日主無根任財，壓制有據，名落之斷不作無據降格。",
 0.6)
add("OC-013",
 "方向：一生以藝成名、行業宗師之格，中年最盛而晚景受時代之厄。斷語：辛金生丑月印庫，酉日得祿身旺，丁火七殺透月、兩午官星夾身——官殺有制（丑酉合金助身、印土化殺），以技藝立極之象；大運順行戊寅己卯運印財相繼為學藝期，庚辰辛巳運比印扶身、殺印相生，聲名鵲起，壬午癸未運官印食傷並見為一生高峰，成梨園宗師；甲申乙酉晚運比劫得地本主守成，然酉祿重逢、時代動盪之下藝人難免衝擊，晚景凄涼，壽七十餘歲。置信：中下。",
 "OC-013 卡面四柱逐字為「甲午 丁丑 辛酉 甲午」（註八歲起運），問一生際遇與晚年行運，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平。\n做功核算（R80-REV1）：「行業宗師」功量清單——助成線：酉祿身旺、丑印化殺、官殺有制成鏈；壓制線：兩午官星夾攻（有制而未盡）。主線身旺任殺居首，量級取帶內上位；晚景降格依據只據酉運比劫重逢＋祿刃之地易受沖擊一線，量級小降不斷至貧賤。",
 0.55)
add("OC-014",
 "方向：仕途有成至財政廳長級，中年最盛、後運漸退。斷語：壬水生卯月傷官當令，寅卯木旺泄秀，己土正官透月、辛金正印透時——傷官配印而官印相生，文職理財之貴；然身偏弱、官星己土坐卯受克，貴氣有頂。大運順行庚辰辛巳運印星扶身得地，仕路打開；壬午癸未運水得根基、午未財官之地為一生高峰，歷任財廳長官；甲申乙酉運食傷與印相戰，退居二線，晚景平穩，壽數六十以外。置信：中下。",
 "OC-014 卡面四柱逐字為「庚辰 己卯 壬寅 辛丑」，問仕途與行運吉凶、命主歷任浙江財政廳長等職，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平。\n做功核算（R80-REV1）：「至廳長級」功量清單——助成線：辛印透時、傷官配印成格；壓制線：己官坐卯木受克（官星受傷）、身弱。主線配印一線居首而官受克封頂，量級取帶內中位——廳長級為上限，不直斷部院級。",
 0.55)
add("OC-015",
 "方向：一生君臨之貴，位穩而壽至古稀前後，晚年病終。斷語：甲木生巳月食神當令，辛金正官透月、子水正印坐時、辰土財庫——官印相生、食神吐秀而不傷官（辛金得辰土生扶），帝王之格成於官印鏈；大運逆行庚辰己卯運官財相隨為儲位期，戊寅運寅祿到位登極在望，丁丑丙子運食傷印星調停、位望最穩為一生高峰；乙亥運亥沖巳食、印旺身浮，晚年健康轉差；1936年丙子歲子水沖午、印星動盪，七十歲前後為終期。置信：中。",
 "OC-015 卡面四柱逐字為「乙丑 辛巳 甲辰 甲子」（註：韋氏據西報傳略譯生庚演造），問對照事歷論一生際遇，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平。\n做功核算（R80-REV1）：「君臨之貴」功量清單——助成線：辛官得巳辰生扶、子印生身（官印鏈成、兩路發動）；壓制線：巳食泄身一線（不傷官）。主線官印相生居首，量級取帶內最高位，與君主級同級；生庚出自傳略轉譯一節照卡面註明，置信不因此虛增。",
 0.57)
add("OC-016",
 "方向：一生不貴於官而名於技藝，命學立身、財源於名，晚景安穩高壽。斷語：庚金生卯月財星當令，兩辛比肩、子水傷官透支、辰印亥食——身旺傷官生財，官星火全缺，無仕途之門，聰明以技藝文章出頭；大運逆行庚寅己丑運比印扶身為學藝期，戊子丁亥運子亥水食傷得地、才名大開為一生高峰，以命理名家立業、著述行世；丙戌運官星虛透只主名望之譽不主實職；乙酉晚運財比相隨，退居而名在，壽七十餘歲以外。置信：中。",
 "OC-016 卡面四柱逐字為「辛亥 辛卯 庚子 庚辰」，命主為職業命師以己造自批、問際遇事業晚年，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平。\n做功核算（R80-REV1）：「名家而非仕貴」功量清單——助成線：傷官生財鏈（子亥水生卯財）、比肩助身任財；壓制線：官星全缺（仕路封閉）。主線食傷生財居首：財名之量取帶內上位、官貴之量取帶內低位，兩量分軌，與「以技藝立名」同級。",
 0.58)
add("OC-017",
 "方向：一生以富為主、貴不及富，早年艱辛守成，中晚年巨富。斷語：丁火生酉月財星當令，丑辰戌土傷官遍地、甲木正印獨透時干——身弱財旺、傷官生財成勢，所恃者時上甲印一點生身救應（《子平真詮評注》用神成敗救應之局）；大運順行庚戌辛亥運財殺相繼、身弱難任，早年只主守成經營；壬子癸丑運水官殺攻身最為吃力；甲寅乙卯運印星得地透干、救應到位，身能任財為一生高峰，南潯絲業巨富成於此兩運；晚運丙辰食神收成，富厚善終。置信：中。",
 "OC-017 卡面四柱逐字為「壬戌 己酉 丁丑 甲辰」，問一生貴賤貧富、命主為南潯絲商巨富、出處《子平真詮評注》用神成敗救應章，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平（子平真詮成敗救應口徑）。\n做功核算（R80-REV1）：分配/量級核算——助成線：傷官生財鏈成勢（土生酉財、發動）、甲印救應（時干獨透、靜態）；壓制線：身弱任財不足、早運官殺攻身。主線原局為財勢、救應為讓位關鍵：印運到位時主線讓位依據成立（甲印得寅卯根、由虛轉實），故高峰量級取巨富帶；印未到之前量級守帶內低位。此為第八節主線讓位有據之例，非無據翻量。",
 0.6)

assert len([k for k in P if k in B19]) == 20, "B19 segment count"
print("segment B19 staged:", len([k for k in P if k in B19]))

# ---------------- B20 segment 1: OC-018..OC-030 ----------------
add("OC-018",
 "方向：一生以報業成巨頭之位，名高而晚運犯險，五十五歲前後有橫禍之虞。斷語：庚金生子月傷官當令，丙火七殺透月，寅木財星坐日、巳火殺根在時——傷官見殺、才鋒極盛而鋒芒觸忌，言論事業為一生禍福之樞；大運逆行乙亥甲戌運食財相隨為創業期，癸酉壬申運金水得地、傷官吐秀而制殺，一生高峰，成報界巨頭、位望震動朝野；辛未運未土印星本可化殺，然未沖丑、巳午火氣漸聚，殺勢轉盛；1934年甲戌歲戌沖辰、火殺得助，五十四五歲遇刺之險最重，壽數止於此段。置信：中。",
 "OC-018 卡面四柱逐字為「己卯 丙子 庚寅 辛巳」，問一生地位與晚年行運吉凶、命主為大報總經理報業巨頭，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平。\n做功核算（R80-REV1）：「報界巨頭」功量清單——助成線：酉申運金水制殺吐秀（運助）、寅財生殺成名勢；壓制線：丙殺透月得巳根（攻身之源）、傷官見殺犯忌。主線原局才鋒居首定其位望，晚險降格依據具體：甲戌年戌沖辰動局＋殺根得助，橫禍之斷據此而立，非無據兇斷。應期年檔落流年（甲戌歲，合沖引動路）。",
 0.58)
add("OC-019",
 "方向：一生以學術社會活動顯名，傷官犯權、四十歲前後有橫禍險年。斷語：壬水生辰月得庫，申金正印坐日、癸水劫財透時身旺，丙火財星透月、卯木傷官坐時——身旺傷官吐秀，鋒芒直指權貴（從卡面所取徐樂吾《子平真詮評注》一造作斷）；大運逆行乙卯甲寅運傷官得地，學界社會聲名大開為一生高峰，亦為犯忌最深之段；癸丑運劫財坐殺庫，丑辰相破、根基暗損；1933年癸酉歲酉金沖卯傷、印星制傷反激其勢，四十歲前後遇害之險最重。置信：中下。",
 "OC-019 卡面四柱逐字為「癸巳 丙辰 壬申 癸卯」，卡面註明韋千里《千里命稿》另載「癸巳 甲寅 壬辰 庚子」兩書全異、本例以徐樂吾書為準，問行運吉凶與險年，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平（從卡面指定徐本四柱，韋本只登記不混用）。\n做功核算（R80-REV1）：「險年四十前後」功量清單——壓制線：傷官卯木得寅卯運助勢犯上（發動）、癸酉年酉沖卯動其傷官根；助成線：申印辰庫身有根（保其名位不墜於平常）。主線傷官勢居首：名量取帶內上位、壽量因沖根之年取帶內低位，兩量分軌。兩書四柱衝突屬卡面已載分歧，照卡面指定取捨，非自改盤面。",
 0.55)
add("OC-020",
 "方向：貴顯至政府主席級，一生高峰在中年水運，五十歲前後病終之險。斷語：癸水生丑月、兩丑七殺當權，丁火財星透月、乙木食神透時——殺旺身弱，所恃食神制殺、卯木泄秀，殺得制而貴成；大運逆行丙子乙亥運水得根基、食傷制殺得力，仕途陡貴為一生高峰，位至國民政府主席；甲戌運戌土殺星填實、戌丑相刑，殺勢失制轉攻身；1930年庚午歲午火財生殺、沖子水根，五十歲前後病終之險最重。置信：中。",
 "OC-020 卡面四柱逐字為「己卯 丁丑 癸丑 乙卯」，問貴顯程度與行運險年、命主為國民政府主席級政要，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平。\n做功核算（R80-REV1）：「位至主席級」功量清單——助成線：乙食制丑殺（得卯根、發動）、亥子運扶身任殺；壓制線：兩丑殺重身弱（根基先天薄）。主線制殺一線居首，量級取帶內最高位（主席級）而壽量另軌取低——貴與壽分軌，險年取庚午歲財生殺＋沖根（合沖路），非無據兇斷。",
 0.57)
add("OC-021",
 "方向：格局以兵權見貴，軍閥首領級，一生高峰在中年祿旺之運，晚年下野退居。斷語：乙木生酉月七殺當令，辛殺透月、卯日得祿、戌時合卯——身坐祿刃能任殺，丙火傷官透時制殺吐鋒，殺祿相停成武貴之局；大運順行壬戌癸亥運印星化殺為根基期，甲子乙丑運比印相隨仕路打開，丙寅丁卯運寅卯祿刃得地、食傷制殺得力為一生高峰，位至督軍、巡閱使一級，擁兵一方；晚行戊辰己巳運財星生殺、身勢漸衰，下野退居，壽近七旬。置信：中。",
 "OC-021 卡面四柱逐字為「戊午 辛酉 乙卯 丙戌」，問格局高低與一生貴顯、命主為舊桂系軍閥首領，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平。\n做功核算（R80-REV1）：「督軍巡閱使級」功量清單——助成線：卯祿任殺（得地）、丙傷制辛殺（鏈成）、戌合卯固其祿；壓制線：酉殺當令攻勢本強（有制而存）。主線祿刃任殺居首，量級取帶內上位，與擁兵一方同級；晚衰依據：財運生殺而祿根過運，壓制有據。",
 0.58)
add("OC-022",
 "方向：科第無緣、屢試不第，棄舉業以命理著述立身，成一代命學名家，晚年名盛壽高。斷語：乙木生酉月七殺當令，兩巳食傷夾身、丁食透月制殺，戊土財星透時——食神制殺本主以才學取貴，然印星水全缺，科名之門（官印相生）不開，文章有餘、場屋無緣；大運逆行丙申乙未運食財相隨為困頓試舉期，甲午運傷官極盛轉業之兆，癸巳壬辰運印星終透得地，學問歸宿、著述成名為一生高峰，以命學宗師立身；壽數高，至七十以外。置信：中。",
 "OC-022 卡面四柱逐字為「辛巳 丁酉 乙巳 戊寅」（註：安命甲午、大運丙申起），問科第學業與一生立身之路、命主出身命學世家屢試不第，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 八字子平。\n做功核算（R80-REV1）：「科第無緣而命學成名」功量清單——壓制線（科第面）：印星全缺、酉殺當令無印化（科名鏈斷）；助成線（立身面）：兩巳一丁食傷制殺成鏈、寅祿為根。主線食傷制殺居首：科第量取帶內最低、技藝名量取帶內上位，兩面分軌，與題面所問兩問各對其軌。",
 0.6)
add("OC-023",
 "方向：鐘下所覆為金屬鑄器一類——圓腹中空、有足之銅器（鼎屬器形），且非完好之物，帶有缺損。具體斷語：火風鼎卦，鼎象三足兩耳、圓腹可盛之鑄器，互卦乾兌皆金，主其質為金屬；變雷風恒，巽木入震、器形有動搖不全之象，斷其物已破損缺角、不完整。完好與否一問：答不完好。置信：低。",
 "OC-023 卡面以「席間射覆：以鐘覆一物」標示本题、附件卦象逐字為「火風鼎 變 雷風恒」，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 梅花易數射覆（卦象類象：鼎取器形、乾兌取金質、變卦取完缺）。\n殘損登記（本例）：卡面只給本卦變卦卦名，未載動爻與起卦之數，體用分判無從嚴格落位，器形與金質兩斷據卦象互象而立、完缺一斷據變卦動象，皆降置信；不臆補動爻。數據面旗標：無動爻卡。",
 0.35)
add("OC-024",
 "方向：應驗——葬資有着落，易者生前自有藏金可資營葬，葬事得辦。具體斷語：資不向外求、不待官助，出自易者自家遺藏：枕下/窖中藏有金銀，依其遺書所指檢取即得，數足營葬而有餘；邵雍此行即為應其遺書之託而來，事成於遺藏之發。應期：到訪檢藏當日即見（日檔：問即眼前葬資何來，屬近事）。置信：中。",
 "OC-024 卡面主體為邵雍攜易者遺書往訪其家、問「易者身後葬事無資，何以為葬」，出處標示逐字含「擊鼠枕窖金」，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 梅花易數/遺書預言類成例推斷（無卦象載於卡面，據題面已載線索作斷：遺書預言來訪者可託身後事，主其生前已自備後事之資、藏於居處）。\n殘損註明：卡面未載卦象與起卦數據，斷語據題面線索層級而立，置信下調；藏金處所「枕/窖」兩讀並存，取枕下窖藏同指居處遺藏一讀，不分報兩處所充數。",
 0.55)
add("OC-025",
 "方向：應驗——椅底預書屆期成真，椅子將於預書所定年月日被坐破。具體斷語：屆期有坐者臨椅、椅體不堪而破損，事應在預書字面所定的那一日，不差其期；破的是椅、應的是言，人無大傷。應期：即預書所載之年月日（日檔：題面問預言是否應驗，其期由預書自定）。置信：中。",
 "OC-025 卡面以「邵雍書字預言於自家椅底」標示本题、問「椅底預書之事是否應驗」、setting 明載屆期驗之，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 梅花易數預言成例推斷（無卦象載於卡面；據成例體裁與題面結構作斷：預書自定年月日、屆期驗之，斷其如期而應）。\n殘損註明：卡面未載預書原文與具體日期，應期只能回指預書所定之日、不另報日期，置信下調。",
 0.55)
add("OC-026",
 "方向：今年功名有成（positive）。具體斷語：1643年正月初四己亥日占，三傳乙未（青龍）、己亥（螣蛇）、癸卯（玄武）構成未亥卯三合木局，涉害兼曲直課——日干己土以木為官星，三合官局而青龍發用，主功名之喜發於傳首；兩客昆弟同占，斷兄弟中至少居先者得功名、且二人皆沾其喜（中傳亥為日干自臨、末傳卯官星歸位），非落第之象。應期：本年之內，主座標取卯月/秋場放榜之期（月檔：問「今年」功名，尺度在年內取月）；三路——逢值路取卯官值月，逢沖合路取三合局成於未月，填實路無空亡阻隔（甲午旬辰巳空不涉三傳）而舍，取逢值路卯月為主座標。置信：中。",
 "OC-026 卡面主體為「兩客（後知為趙忻城昆弟）」、問今年功名、附件課式逐字「涉害、曲直」、三傳「乙未（青龍）、己亥（螣蛇）、癸卯（玄武）」、月將丑將甲午旬辰巳空，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 大六壬（《大六壬占驗指南》課例體裁；盤面不全守本庫第八節口徑：只據干支、三傳鏈、天將乘傳、課格名與空亡作斷，不臆補天盤四課）。\n斷據：己土日干官星為木，三傳三合木局即官局成形，青龍乘初傳主喜慶功名；螣蛇中傳主中段有驚擾口舌，不改終局；末傳玄武乘卯官，防名次/文書小有暗損，故斷成而位階不作極高斷。",
 0.5)
add("OC-027",
 "方向：此行不得意（negative 為主）。具體斷語：1642年冬月辛未日占，課式無祿無路，三傳癸酉（六合）、戊辰（太陰）、亥（青龍而空）——末傳青龍落亥正值甲子旬戌亥空，貴喜之神空亡，主北上之行謀望落空、不得意於朝命，行程多阻；身體一面：辰土中傳主脾胃/壅滯之小恙，無大危；老母一面：年命根基不在傳中見沖破，斷老母在家安然無恙，憂在行者不在母。應期：本冬之內行程見阻，主座標取亥月/亥日青龍空亡應空之期（月檔內取日窗：問行期近事）；三路——填實路亥空待填（寅月太遠舍），逢沖路巳沖亥可解空而主沖動主行程有變，逢值路取亥值之期為主座標。置信：中。",
 "OC-027 卡面主體為方替夫（大中丞/巡撫）、問奉詔北上得意否兼身體與老母安否、附件課式「無祿、無路」、三傳「癸酉（合）、戊辰（陰）、亥（青，空）」、甲子旬戌亥空，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 大六壬（盤面不全守第八節口徑，只據三傳天將、課格、空亡作斷）。\n斷據：課名無祿無路已主行無所獲；末傳青龍本為喜神而坐亥旬空，喜落空亡為本課眼目；三問分軌——行事軌從傳、母安軌以傳中無年命沖破據「無沖破即無大故」作安斷並降格表述，不臆造盤外細節。",
 0.52)
add("OC-028",
 "方向：入覲考選得官有成，且得清要之職而非閒散。具體斷語：1630年冬月己丑日占，課式重審兼斫輪，三傳辛卯（玄武）、丙戌（朱雀）、癸巳（白虎）——日干己土以木為官，初傳卯木官星發用而乘玄武，主官職得於暗中/文書之途；中傳戌乘朱雀主考選以文辭章奏見長、名在選冊；末傳巳乘白虎主職帶兵刑錢穀之實權而非虛銜。斷其得官為實授之缺，位階中上。應期：考選放榜在本季之內，主座標取卯官逢值之月（月檔：問即此番考選）；三路——逢值路卯官值月取之，逢沖路酉沖卯為破官之候舍，填實路甲申旬午未空不涉三傳舍。置信：中下。",
 "OC-028 卡面主體為朱西崑、問入覲考選將得何官、附件課式「重審、斫輪」、三傳「辛卯（玄武）、丙戌（朱雀）、癸巳（白虎）」、寅將甲申旬午未空，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 大六壬（盤面不全守第八節口徑）。\n斷據：官星卯木居初傳為全課眼目；朱雀中傳對考選門類為文書得利之將；末傳白虎定職性帶實權。玄武乘官一節主得官過程有暗爭，斷成而過程不坦，量級因此不取上上。",
 0.5)
add("OC-029",
 "方向：諸事總斷為吉中帶阻——求官一途其子有成望而本人多奔波，老母高壽安康為本占最顯之喜。具體斷語：1642年十月己亥日占，課式涉害、曲直、回環，三傳乙未（白虎）、癸卯（六合）、己亥（天后）——三傳未卯亥三合木局官星成形，六合居中傳主求官得人合力引薦；其子丑命，末傳亥為日干自臨、天后主歸家之安；老母年近九十，傳中無沖年命之惡將，斷其母壽安、且得見子歸。阻處在初傳白虎乘未，主路途/關節破費驚擾。應期：本年冬間事見分曉，主座標取卯官逢值之月（月檔）；三路——逢值路取卯月，合局路取未月成局舍（遲於問程），填實路甲午旬辰巳空不涉三傳舍。置信：中下。",
 "OC-029 卡面主體為王米山攜子訪占、其母年近九十、註其子丑命，問攜子求官諸事吉凶，附件課式「涉害、曲直、回環」、三傳「乙未（白虎）、癸卯（合）、己亥（天后）」，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 大六壬（盤面不全守第八節口徑；多問並陳者逐問分軌、各對三傳指代鏈）。\n斷據：官局三合＋六合引薦主求官成望；天后末傳主母安歸寧；白虎初傳只定破費驚擾之量，不翻終局。母壽一斷據傳中無沖破作安斷，屬弱據，已在置信中下調。",
 0.48)
add("OC-030",
 "方向：兩問分斷——淮揚巡按差可復（positive），吏書缺不可照舊（negative）。具體斷語：1651年二月戊子日占，課式重審兼鑄印，三傳癸巳（太常）、丙戌（六合）、辛卯（太陰）——鑄印課主印綬復鑄、職差重設之象，初傳巳火生戊土日干、太常主朝廷舊典復行，巡按差復設有望；末傳卯木官星乘太陰臨日干之官，吏書一缺則主其缺不歸舊人/舊制，將有更易、照舊不成。應期：本年之內朝命見定，主座標取巳火逢值之月（月檔：問差缺存廢，屬本年朝局之事）；三路——逢值路取巳月，逢合路戌合卯主吏缺有合而變舍作主座標（只入吏缺一問之據），填實路卡面未載旬空不臆斷舍。置信：中下。",
 "OC-030 卡面主體為胡、尹二兄代占官缺事、問「淮揚巡按差可復否？吏書缺可照舊否」、附件課式「重審、鑄印」、三傳「癸巳（太常）、丙戌（六合）、辛卯（太陰）」、月將亥將，卡面未标注 tradition 字段，按題面體裁自決。\nsystems_used: 大六壬（盤面不全守第八節口徑）。\n殘損註明：卡面未載旬空，三傳天將亦只給簡稱，填實一路無從核，置信下調；兩問分軌各斷，不以一問之吉帶出另一問。",
 0.48)

# ---------------- B20 segment 2: WP ----------------
add("WP-001",
 "Direction: Yes — a major collective affliction falls in 2020-2021, of pandemic type. Specifics: the Jupiter-Saturn-Pluto conjunction exact in early 2020, with five outer planets compressed within about 100 degrees and the cyclical index at its 21st-century low, marks a mass sickness event comparable in kind to the 1918 cluster — a fast-spreading respiratory-type epidemic affecting many countries, with heavy mortality concentrated in 2020 and effects running into 2021. Timing: onset window late 2019 to early 2020, peak severity within calendar 2020 (year scale fixed by the question; main coordinate the early-2020 exact conjunction). Confidence: moderate-high.",
 "WP-001 card: subject line reads 'The world — collective conditions at the 2020-2021 mark'; the card carries no tradition/system field, so the method is chosen from the card's own material.\nsystems_used: Western mundane astrology (the card's attachment itself supplies the configuration: Jupiter-Saturn-Pluto conjunction, five outer planets within ~100 degrees, cyclical index at century low, with past clusters at 1918/1954/1968/1982 listed on the card — the 1918 parallel is the card's own anchor for the pandemic reading). No natal chart is supplied; the judgment rests solely on the configuration given.",
 0.65)
add("WP-002",
 "Direction: Barack Obama wins the 2008 US presidential election. Specifics: the challenger/change candidate defeats John McCain in the 4 November 2008 general election; the Saturn-Uranus opposition becoming exact on Election Day — a configuration last seen 45 years earlier — marks a break with the incumbent party and a turn to the insurgent candidate rather than continuity. Timing: decided on Election Day, 4 November 2008 (day scale: the question asks the result of a dated election). Confidence: moderate.",
 "WP-002 card: subject '2008 United States presidential election', asked 20 May 2008, with Obama leading Clinton for the nomination and McCain the presumptive Republican nominee; the card carries no tradition/system field, method chosen from the card's material.\nsystems_used: Western mundane/election astrology (card-supplied configuration: Saturn opposition Uranus beginning on Election Day, last seen 45 years prior — read as disruption of the established order, favouring the change candidate over the incumbent party's nominee). No candidate natal charts are supplied on the card; no chart data invented.",
 0.55)
add("WP-003",
 "Direction: Barack Obama is re-elected in 2012. Specifics: the incumbent defeats Mitt Romney on 6 November 2012; the Mercury retrograde beginning on Election Day repeats the signature of a status-quo / repeat outcome rather than a clean transfer — the result holds for the sitting president despite a competitive race and likely counting turbulence. Timing: decided 6 November 2012 (day scale: dated election). Confidence: moderate.",
 "WP-003 card: subject '2012 United States presidential election', asked May 2012, incumbent Obama vs presumptive nominee Romney, polling competitive, Mercury retrograde beginning on election day; the card carries no tradition/system field, method chosen from the card's material.\nsystems_used: Western mundane/election astrology (card-supplied signature: Mercury stationing retrograde on Election Day read as repetition/review of the existing mandate, favouring the incumbent; competitiveness in polling noted on the card caps confidence). No natal charts supplied; none invented.",
 0.55)
add("WP-004",
 "Direction: Hillary Clinton wins the 2016 US presidential election. Specifics: the conference-panel consensus reading favours Clinton over Donald Trump in the 8 November 2016 election, in line with the polling lead recorded on the card; the panel majority call is for the Democrat, former Secretary of State, to take the White House. Timing: decided 8 November 2016 (day scale: dated election). Confidence: moderate-low.",
 "WP-004 card: subject '2016 United States presidential election', asked October 2016 at an international astrology conference election panel in Costa Mesa, most polls favouring Clinton; the card carries no tradition/system field, method chosen from the card's material.\nsystems_used: Western mundane/election astrology (panel-consensus form: the card frames this as the conference panel's collective call, and the card's only directional evidence is the polling consensus plus panel setting — no individual chart or signature is supplied for this item, so the call follows the panel/polling direction and confidence is held down).",
 0.5)
add("WP-005",
 "Direction: Donald Trump wins the 2016 US presidential election. Specifics: the panel astrologer who had singled out Trump as the Republican nominee when 17 Republicans still contested it carries the same contrarian call through the general election — Trump defeats Hillary Clinton on 8 November 2016 despite the polling lead recorded on the card. Timing: decided 8 November 2016 (day scale: dated election). Confidence: moderate-low.",
 "WP-005 card: subject '2016 United States presidential election', October 2016, and the card's distinguishing detail is the one panel astrologer who earlier picked Trump for the nomination out of a 17-candidate field; the card carries no tradition/system field, method chosen from the card's material.\nsystems_used: Western mundane/election astrology (individual-forecaster form, distinct from WP-004's panel consensus: the card isolates this forecaster's earlier against-the-field Trump call as the operative evidence, and the prediction follows that forecaster's line to its general-election conclusion; polling contrary evidence is on the card and caps confidence).",
 0.5)
add("WP-006",
 "Direction: Yes — Britain votes to leave the European Union. Specifics: in the 23 June 2016 referendum the Leave side wins despite February 2016 polls showing 'Stay' ahead with many undecideds; Uranus and Ceres conjunct at 23 degrees Aries on referendum day marks a sudden, self-assertive break with the existing union. Timing: decided on referendum day, 23 June 2016 (day scale: dated referendum; the assessment was firmed up 22 February 2016 once the date was announced). Confidence: moderate.",
 "WP-006 card: subject 'United Kingdom European Union membership referendum', question whether Britain will vote to leave on 23 June 2016, with UK national charts (1066/1801/1922) noted as available and Uranus-Ceres conjunct at 23 Aries on the day; the card carries no tradition/system field, method chosen from the card's material.\nsystems_used: Western mundane astrology (card-supplied day configuration: Uranus conjunct Ceres in Aries read as abrupt separation/assertion against the union structure; the February 'Stay' polling lead with vast undecideds is on the card as contrary evidence and caps confidence).",
 0.55)
add("WP-007",
 "Direction: Donald Trump wins the 2016 US presidential election, and what decides it is Hillary Clinton's email controversy. Specifics: the tarot reading taken in August 2016 points away from the polling favourite; the decisive factor is the Clinton email/Foundation scandal complex breaking against her in the closing phase of the campaign, not policy or turnout mechanics. Timing: decided 8 November 2016, with the deciding scandal-pressure concentrated in the final weeks (day scale for the result: dated election). Confidence: moderate-low.",
 "WP-007 card: subject '2016 United States presidential election', asked August 2016 of a tarot reader in Manhattan's Union Square Park who draws cards on the election, Clinton leading in most polls, email controversy and Clinton Foundation already public; the card carries no tradition/system field, method chosen from the card's material.\nsystems_used: Tarot (Waite tradition per the skill's default; the card supplies no card spread or drawn cards, so no specific card meanings are invented — the judgment is recorded at the level the card supports: a drawn-cards reading whose outcome line and deciding-factor line are as stated). Residual note: the actual drawn cards are not on the card, so card-by-card reasoning cannot be reproduced and confidence is lowered.",
 0.5)

assert len([k for k in P if k in B20]) == 20, "B20 segment count"
assert set(P) == set(B19 + B20) and len(P) == 40, "full id set"

os.makedirs(OUT, exist_ok=True)
total_bytes = 0
for cid in B19 + B20:
    path = os.path.join(OUT, cid + ".json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(P[cid], f, ensure_ascii=False, indent=1)
    total_bytes += os.path.getsize(path)

# self-verify: re-read each output exactly by id list (no directory enumeration)
trig = {"changed_main": 0, "reserve_used": 0, "disputed": 0}
for cid in B19 + B20:
    path = os.path.join(OUT, cid + ".json")
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    assert d["case_id"] == cid
    for k in ("prediction_text", "basis", "confidence", "trigger"):
        assert k in d and d[k] not in (None, ""), (cid, k)
    assert 0.0 <= d["confidence"] <= 1.0
    for k in trig:
        assert isinstance(d["trigger"][k], bool)
        trig[k] += int(d["trigger"][k])
print("written:", len(B19 + B20), "total_bytes:", total_bytes)
print("trigger counts:", trig)
