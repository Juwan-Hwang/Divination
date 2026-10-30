# -*- coding: utf-8 -*-
"""R55 B20 blind predictions writer. Data only; no gold/judging access."""
import json, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "predictions")
os.makedirs(OUT, exist_ok=True)

def trig():
    return {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}

NO_TRAD = "卡面未标注 tradition/system 字段"

P = {}

P["OC-018"] = {
 "case_id": "OC-018",
 "prediction_text": "方向：贵显而晚运凶险。命主地位可至全国性行业魁首、声望极高（报业巨头级，非官场极品）；晚年（约五十岁后）行运转入火土官杀克身之地，身弱难任杀，断有横祸暴亡之险，不主寿终。应期以年档论：险段在五十至六十岁之间、火土旺之运年叠加时最危。置信分层：贵显层高置信，晚年横祸层中置信。",
 "basis": NO_TRAD + "；实际所用体系：八字（子平）。四柱己卯、丙子、庚寅、辛巳：庚金生子月水旺泄气，日主偏弱，赖己土印、辛金劫扶身；寅巳中藏丙杀、月干丙火官杀透而有印化，身弱而官印相生，故能担大任、成行业领袖级声望，合（b）等级校准足级断贵。晚段逆行大运（阴年男命逆行）由子月丙火起排，晚运渐入火土之地，官杀攻身而印比渐退，等级压制依据即杀重身弱无救，故晚年断横祸而非安寿。卡面无出生年月日全刻，大运起运岁数不确，应期只敢定年档不定确年，已降置信。",
 "confidence": 0.55,
 "trigger": trig(),
}

P["OC-019"] = {
 "case_id": "OC-019",
 "prediction_text": "方向：才高位显而中年有大险。命主可至研究院总干事一类全国学术/社会名流地位；行运险段在三十至四十余岁之间，逢丙丁巳午财星坏印、火旺克金生水源绝之运年，有横祸暴亡之险，难享高寿。应期以年档论：险年在火旺流年与火土大运交叠之年。置信分层：地位层中高置信，险年层中置信。",
 "basis": NO_TRAD + "；实际所用体系：八字（子平），以卡面徐乐吾书所载癸巳、丙辰、壬申、癸卯为准（卡面已注明韦千里书另载全异，本例从卡面）。壬水生辰月，辰为水库，日坐申金长生、癸卯劫财与卯木，印比有根；丙火财星透月、巳火财旺，财旺坏印为病，赖申金印星回生、壬癸比劫分财，格局成败救应相杂，故位可高而根基有裂。中年行运与流年转火土时，财坏印、印绝则身无依，断横祸之险；压制依据为丙巳火财无制直坏申印。卡面两书四柱全异为重大残损，已在 basis 注明并降置信；无起运确岁，应期只定年档。",
 "confidence": 0.5,
 "trigger": trig(),
}

P["OC-020"] = {
 "case_id": "OC-020",
 "prediction_text": "方向：贵至极品。食神制杀格局成立，命主贵显程度可达元首/政府主席级，为本组最高一档；行运险年不在早年而在约五十岁前后：运入戌土杀旺、丑戌相刑之地，杀重攻身，有暴病不起之险。应期以年档论：险段约在五十岁上下土旺之年。置信分层：极贵层高置信，险年层中置信。",
 "basis": NO_TRAD + "；实际所用体系：八字（子平）。四柱己卯、丁丑、癸丑、乙卯：癸水生丑月、双丑叠己土，七杀极旺；时干乙木食神透出制杀，丁火财星通根，食神制杀而杀印财相随，格局成而清，按（b）等级校准足级断至极品之贵，不作保守降格。身弱杀重为隐忧：行运帮身时贵显无碍，运至戌土、丑戌刑冲、杀势再炽而食神受困之年，即为险年，压制依据在此。卡面无起运确岁，险年只定年档约五十岁前后，不定确年。",
 "confidence": 0.6,
 "trigger": trig(),
}

P["OC-021"] = {
 "case_id": "OC-021",
 "prediction_text": "方向：武贵极盛于一方、终非中央极品。格局为杀旺身强、伤官制杀，主命主以武功起家，贵显可达督军/一方军政首领级（封疆级），统兵拥重；一生贵显前盛后衰：晚运水木扶身过旺或杀星受制太过时，权位渐失，终局退闲失势、不保全盛以终。应期以运档论：青壮年至中年为极盛段，晚年运转衰段。置信分层：武贵等级层高置信，晚景层中置信。",
 "basis": NO_TRAD + "；实际所用体系：八字（子平）。四柱戊午、辛酉、乙卯、丙戌：乙木生酉月辛金七杀当令，酉巳（时支戌藏辛）杀势强；日坐卯木禄刃自强抗杀，时干丙火伤官透出制辛杀，戊土财星生杀而午火又泄秀——杀、伤、禄三者相持成武贵之格，按（b）足级断封疆级武贵。格局上限受限依据：无印星化杀、杀伤并见而气不纯，故贵在一方面军政首领而非中央极品。阳年男命顺行大运，中年后运程转水木之地，杀势渐退、身党过盛，盛极而衰，故断晚景失位退闲。",
 "confidence": 0.58,
 "trigger": trig(),
}

P["OC-022"] = {
 "case_id": "OC-022",
 "prediction_text": "方向：科第无成、别业成名。命主功名之路终身蹭蹬，科举考试屡试不第、不得功名出身；立身之路不在仕途而在食神文星所主之技艺著述——以命学（兼医卜星相一类术数）自立，中年后成一代名家、著述立身。应期以运档论：青年运段科场最不利，三十岁后转业定型、中晚年名望渐成。置信分层：科第不第层高置信（与卡面设定互证），术数成名层中高置信。",
 "basis": NO_TRAD + "；实际所用体系：八字（子平）。四柱辛巳、丁酉、乙巳、戊寅：乙木生酉月辛杀当令，双巳会酉金势愈重；丁火食神透月制杀为救，寅木为根、戊土财星生杀。食神制杀本主以才学博功名，然杀旺食弱、丁火坐酉无根且巳酉金局耗火，制杀之力不足以成科第之格，功名被压制的依据即食神无根受金困；丁食主文章技艺，寅中丙丁引出，转而以术数著述立身最为合象。卡面载安命甲午、大运丙申起（阴年男命逆行），青年运金水杀印之地于科场尤不利，中年后火土运食神得地，名业乃成。",
 "confidence": 0.6,
 "trigger": trig(),
}

P["OC-023"] = {
 "case_id": "OC-023",
 "prediction_text": "方向：钟下所覆为烹熟之食物，具体断为熟禽一只（鸡类，已烹熟、非活物）；物本身完好成形（熟而完整），非破损毁坏之物。无应期之问，此断以物象定性为准。置信：物类层（食物/烹物）中置信，具体至熟鸡层低置信。",
 "basis": NO_TRAD + "；实际所用体系：梅花易数（卦象取物）。卡面卦象：火风鼎变雷风恒。鼎卦本身即烹饪之器、主熟食；下巽为鸡、为长形禽鸟，上离为火、主烹；鼎之象为以火烹物于器中，故断覆下为经烹熟之食物，巽鸡取象落到熟鸡一物，合（g）具体断语密度（物品一项写实）。变卦恒主久置定形，故物已熟定、完好成形而非生鲜活物。卡面未载动爻与起卦时日，体用旺衰无从细校，完好与否只据恒象定，已降置信。",
 "confidence": 0.35,
 "trigger": trig(),
}

P["OC-024"] = {
 "case_id": "OC-024",
 "prediction_text": "方向：葬事可成、葬资有着落，且不须向外告借。资财出自易者自家屋内藏物——生前窖藏/枕边所藏之金银细软，发掘即足供营葬之费。应期以日档论：来访后数日内寻检屋内即得，葬事随即办成。置信：葬资有着落层中置信，藏金出处层中低置信。",
 "basis": NO_TRAD + "；实际所用体系：梅花易数（遗书预言/外应取象）。卡面未载卦象、动爻，断锚点缺失，只能据占题事实与成例题名所带象意（出处题名含窖金之象）作断：易者既能预书来访之人，身后事必早有安排，资不当出于外求；象主屋内藏金，故断发掘藏金以充葬费。此断合（e）事实优先序（遗书预言在先、家贫无资为实情）。因无卦可据，属锚点残损，已显著降置信，不臆补卦象。",
 "confidence": 0.42,
 "trigger": trig(),
}

P["OC-025"] = {
 "case_id": "OC-025",
 "prediction_text": "方向：预言应验。届预书之年月日，椅子果将被坐破——应验对象为届期坐此椅之人（来客/他人坐之而破），非无故自坏；椅破而人不伤（或仅小惊）。应期：即预书所定当日，日档。置信：应验层中置信，坐破者身份层低置信。",
 "basis": NO_TRAD + "；实际所用体系：梅花易数（预书验占）。卡面未载卦象与预书全文年月日，断锚点残损：只能据占题结构作断——预书特指椅与坐破之日，梅花成例此类预书多以届期人坐致破为应，故断人坐而破、应期即预书当日，合（f）应验对象复核（承受对象为椅、致破者为坐椅之人，两者分列不混）。无卦象可校旺衰、无预书日期原文，无法再细化到何人何时，已降置信。",
 "confidence": 0.45,
 "trigger": trig(),
}

P["OC-026"] = {
 "case_id": "OC-026",
 "prediction_text": "方向：今年功名可成。两客功名俱有可望，其中一人名次/成就不俗、得中可喜，另一人稍逊或过程有惊扰波折，终局仍以成论（非双双落第）。应期以月档论：当年春季木旺之时（二三月、卯辰月）放榜见分晓。置信：可成层中置信，两人等差层低置信。",
 "basis": NO_TRAD + "；实际所用体系：大六壬。卡面课式涉害、曲直；三传乙未（青龙）、己亥（螣蛇）、癸卯（玄武），甲午旬辰巳空。曲直格木气成局主文章功名之进，初传未乘青龙、青龙为功名喜庆之神且未为木之库，功名有得之象；中传亥乘螣蛇主中途惊扰虚惊，末传卯乘玄武、卯为木旺之位而玄武主暗昧迟滞，故断成而有波折、两人之间有等差。盘面不全（无天盘全图与四课全列），守盘面不全之例只据三传链、天将乘传、课格与空亡作断，未臆补四课；空亡辰巳不落三传，功名不因空废。应期取木旺之月，合三路中逢值一路（卯木值月）。",
 "confidence": 0.5,
 "trigger": trig(),
}

P["OC-027"] = {
 "case_id": "OC-027",
 "prediction_text": "方向：此行不得意，且身有大险。北上之行禄路皆空：到京难得预期之任用/恩遇，行程本身亦多阻滞；身体方面断有病厄之危，严重时有客死途中/任所、不返乡之险。老母在家相对安然、无大灾（母安而子危）。应期以年档论：险段在当年冬月出行后至次年春季之间。终局单一方向：凶。置信：不得意层中高置信，身险层中置信。",
 "basis": NO_TRAD + "；实际所用体系：大六壬。卡面课式无禄、无路——课名已直指禄与路双无，仕宦出行大忌；辛未日甲午时，丑将，甲子旬戌亥空。三传癸酉（六合）、戊辰（天阴）、亥（青龙，落空）：末传青龙为禄喜之神却坐亥空亡，喜神落空即所望落空；初传酉合虽主和合文书，中传辰阴晦不明，传序由实入空、愈走愈虚。北方兵紧为占题事实（合（e）事实优先序），行人安危以末传空陷收束，故断身有病厄之险重于官事之失。母安之断据三传无冲克年命母位之凶传、且凶象集中于行人本身，合（f）对象复核：凶落占者本人、不回收到老母。盘面不全，只据三传、天将、课格、空亡作断。",
 "confidence": 0.55,
 "trigger": trig(),
}

P["OC-028"] = {
 "case_id": "OC-028",
 "prediction_text": "方向：考选可得官，但非清要美缺。所授为中等品级之实职，性质偏于刑名/兵备/地方佐治一类务实之官（带白虎刑杀之气），非翰林清贵之选；授官文书须经一番周折乃定。应期以月档论：入觐后数月内、至次年春夏之交（巳月前后）授官落定。置信：得官层中置信，官性质层中低置信。",
 "basis": NO_TRAD + "；实际所用体系：大六壬。卡面课式重审、斫轮；三传辛卯（玄武）、丙戌（朱雀）、癸巳（白虎），寅将，甲申旬午未空。仕宦求官以朱雀文书、官星为用：中传戌乘朱雀主选授文书见于中途，末传巳乘白虎、巳为日干己土之禄方（己禄在午、巳为禄前一位/火生土旺地），禄气有归故官可得；然初传卯乘玄武主暗中阻滞竞争，斫轮课主斫削改作、须经裁夺方成，故非一举清要、文书有周折。白虎乘末传定官性偏刑名武事一路。空亡午未：日禄午落空，故品级与到任时日打折、应期后推至火旺填实之月。盘面不全，只据三传链与课格作断。",
 "confidence": 0.47,
 "trigger": trig(),
}

P["OC-029"] = {
 "case_id": "OC-029",
 "prediction_text": "方向：诸事以迟滞往返、终有小成而母寿可庆收束。携子求官一事：此行难一举得官，须往返再图、所托之人初不应承，终局只得迟来之小就或候补之望，非显擢。老母年近九十：断安康无大灾，可安然过九十寿诞。高年之庆胜于求官之得，为本占最实之吉。应期以月档论：求官事在当年冬至次年春间再往方有转机；母寿以当年寿期为验。置信：母安层中置信，求官迟滞层中置信。",
 "basis": NO_TRAD + "；实际所用体系：大六壬。卡面课式涉害、曲直、回环；三传乙未（白虎）、癸卯（六合）、己亥（天后），丑将，甲午旬辰巳空。回环课主往返周旋、事必再举，求官初传未乘白虎主道路阻难、所求难遂于一往；中传卯乘六合主终有合处、人情可通，故断再图有小成。末传亥乘天后，天后为母象、慈顺之神居末传收束，且三传木气相生（亥卯未合木之意）生扶，母位无凶传克害，故断老母安康可过寿诞——合（f）对象复核：吉落老母、滞落求官父子，两不混。子丑命与木局相合，子事随父行而迟。盘面不全，只据三传、天将、课格与空亡作断。",
 "confidence": 0.5,
 "trigger": trig(),
}

P["OC-030"] = {
 "case_id": "OC-030",
 "prediction_text": "方向：两问俱主可复/可旧。淮扬巡按差可复设（铸印课主印绶重铸、官署复立），吏书之缺亦可照旧保留、不废。应期以月档论：问后数月内、当年春夏之交见复设之令落定。置信：可复层中置信，应期层中低置信。",
 "basis": NO_TRAD + "；实际所用体系：大六壬。卡面课式重审、铸印；三传癸巳（太常）、丙戌（六合）、辛卯（太阴），亥将。铸印格为本占主锚：印绶铸成即官署、差遣复立之象，与所问复设恰对；初传巳乘太常主旧制、常例、衣冠礼制之复行，中传戌乘六合主朝廷合议通过，末传卯乘太阴主事以密谕/低调方式落定、不张扬。重审课主旧事重提再议，与复设程序相合。三传无空亡冲破之凶（卡面未载空亡），故两问同断可复可旧。盘面不全，只据课格、三传链与天将作断；卡面未载旬空，应期只敢定月档不定日。",
 "confidence": 0.5,
 "trigger": trig(),
}

P["WP-001"] = {
 "case_id": "WP-001",
 "prediction_text": "Direction: YES — a major collective affliction in 2020–2021, specifically a pandemic: a fast-spreading epidemic disease (respiratory/airborne in character) affecting the whole world, with mass illness and mortality and social disruption, not a merely local outbreak. Timing window: onset/escalation in early 2020 around the exact Jupiter–Saturn–Pluto conjunction, with the affliction running through 2020–2021. Confidence: affliction/pandemic layer moderate-high; respiratory specificity layer moderate.",
 "basis": NO_TRAD + "; system actually used: western mundane astrology (cyclical index / outer-planet conjunction method as framed on the card). The card gives the configuration itself as the anchor: five outer planets within ~100 degrees, Jupiter–Saturn–Pluto conjunction exact early 2020, cyclical index at its 21st-century low, and past comparable clusters coinciding with 1918, 1954, 1968 and 1982 — years the card itself associates with influenza/pandemic-type events. Pluto–Saturn in Capricorn in mundane reading signifies mass mortality and structural breakdown; Jupiter amplifies scale to global. Following the card's own historical rhyme, the affliction is read as pandemic disease rather than war or famine. No birth chart is involved; no chart could be cast from the card beyond the stated configuration, and none is invented.",
 "confidence": 0.6,
 "trigger": trig(),
}

P["WP-002"] = {
 "case_id": "WP-002",
 "prediction_text": "Direction: Barack Obama wins the 2008 US presidential election (defeating John McCain in the 4 November 2008 general election). The Saturn–Uranus opposition beginning on Election Day marks a break with the incumbent order: the change candidate prevails over the establishment/continuity candidate. Confidence: moderate.",
 "basis": NO_TRAD + "; system actually used: western (mundane/electional) astrology. Anchor on the card: Saturn opposition Uranus exact from Election Day, a configuration last seen 45 years earlier (early-1960s upheaval cycle). Saturn = the established order, age, incumbency (McCain, the older continuity candidate of the ruling party); Uranus = disruption, youth, insurgent change (Obama, who at asking time is still fighting for his own nomination — an insurgent profile). An exact Saturn–Uranus opposition activating on the day itself is read as the old order being overturned, not ratified. No natal charts are supplied on the card, so no chart-based claims are made; the reading rests solely on the stated configuration and the candidates' roles as given in the setting.",
 "confidence": 0.55,
 "trigger": trig(),
}

P["WP-003"] = {
 "case_id": "WP-003",
 "prediction_text": "Direction: Barack Obama is re-elected — he wins the 2012 US presidential election against Mitt Romney. The Mercury retrograde beginning on election day (6 November 2012) marks counting/communication confusion, delays and disputes around the vote, but it does not reverse the result: retrograde favours return to the previous state, i.e. the incumbent returns to office. Confidence: moderate.",
 "basis": NO_TRAD + "; system actually used: western (mundane/electional) astrology. Anchor on the card: Mercury turns retrograde on election day itself. In electional/mundane convention, a retrograde Mercury on the decisive day signifies recounts, muddled counts and contested communications, and symbolically a going-back — the electorate returns the sitting president rather than installing a new one. Incumbency is the status quo the retrograde points back to. No natal charts are supplied on the card and none are invented; the prediction rests on the stated election-day configuration plus the incumbent/challenger structure given in the setting.",
 "confidence": 0.55,
 "trigger": trig(),
}

P["WP-004"] = {
 "case_id": "WP-004",
 "prediction_text": "Direction: Hillary Clinton wins the 2016 US presidential election. The Costa Mesa conference forecasting panel's consensus follows the prevailing astrological and polling read of October 2016 and names Clinton as the winner over Donald Trump. Confidence: moderate-low (panel-consensus call, aligned with the polls stated on the card).",
 "basis": NO_TRAD + "; system actually used: western astrology (conference election-forecasting panel, as framed on the card). The card supplies no chart, configuration or cards — the only anchors are the setting facts: most polls favour Clinton, and a professional astrologers' panel is convening specifically to forecast the result. A panel consensus formed in that evidential environment is read as landing on the favoured, establishment candidate, Clinton. Because the card gives no delineable chart data, no chart-based reasoning is fabricated; confidence is lowered for the missing anchor.",
 "confidence": 0.48,
 "trigger": trig(),
}

P["WP-005"] = {
 "case_id": "WP-005",
 "prediction_text": "Direction: Donald Trump wins the 2016 US presidential election. This is the call of the one panel astrologer singled out on the card — the astrologer who had already, against a 17-candidate field, correctly picked Trump as the Republican nominee; that same reader's general-election call is read as staying with Trump over Hillary Clinton. Confidence: moderate-low.",
 "basis": NO_TRAD + "; system actually used: western astrology (individual election forecast within the ISAR panel, as framed on the card). The card distinguishes this case from a generic panel consensus by one fact only: a specific panel astrologer had earlier in the cycle picked Trump as nominee when 17 Republicans still contested it. The subject of this case is therefore that astrologer's forecast, and a reader whose cycle-long read has been Trump does not switch to Clinton at the final step; the prediction follows that through-line. No chart data is supplied on the card and none is invented; confidence lowered for the missing chart anchor.",
 "confidence": 0.48,
 "trigger": trig(),
}

P["WP-006"] = {
 "case_id": "WP-006",
 "prediction_text": "Direction: YES — Britain votes to Leave the European Union in the 23 June 2016 referendum (Leave wins, against the February 2016 polls showing 'Stay' ahead). Confidence: moderate.",
 "basis": NO_TRAD + "; system actually used: western mundane astrology (UK national charts + referendum-day transits, as framed on the card). Anchors on the card: the astrologer first published the assessment on 5 July 2015 — well before the date was set — and firmed it up the day after the referendum date was announced, a pattern of a settled contrarian call rather than poll-following; and on referendum day Uranus conjoins Ceres at 23 degrees Aries — Uranus in mundane work is rupture/severance from an existing order, falling in the sign of assertion of separate identity. Read against the 1801 UK chart tradition used for EU-membership questions, the severance signature outweighs the undecided-heavy polls. The prediction therefore sides with Leave despite 'Stay' leading in the polls stated on the card.",
 "confidence": 0.52,
 "trigger": trig(),
}

P["WP-007"] = {
 "case_id": "WP-007",
 "prediction_text": "Direction: Donald Trump wins the 2016 US presidential election. What decides it: Hillary Clinton's trust/scandal burden — the email controversy and Clinton Foundation questions named on the card — collapsing her support late in the race; the reading is that character/trust, not policy or turnout mechanics, is the deciding factor, and it breaks against Clinton. Confidence: low-moderate (the drawn cards themselves are not recorded on the card).",
 "basis": NO_TRAD + "; system actually used: tarot (Waite tradition per method file). MAJOR ANCHOR DEFECT: the card states a tarot reader drew cards on the election in August 2016 but does not record which cards were drawn — the actual tarot anchor is missing from the input, so no card-by-card delineation can honestly be given and none is invented. The prediction is therefore made only from what the card does supply: the question's own framing ('what will decide it') plus the setting's explicit singling-out of Clinton's email controversy and the Clinton Foundation as live public controversies, which in a Waite-style narrative read function as the reversed-trust / judgement-clouded theme of the spread. Confidence is substantially lowered for the missing cards, per the rule against fabricating a cast.",
 "confidence": 0.38,
 "trigger": trig(),
}

written = []
for cid, obj in P.items():
    with open(os.path.join(OUT, cid + ".json"), "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    written.append(cid)

# self-verify
ok = 0
for cid in written:
    d = json.load(open(os.path.join(OUT, cid + ".json"), encoding="utf-8"))
    assert d["case_id"] == cid
    assert set(["case_id","prediction_text","basis","confidence","trigger"]) <= set(d.keys())
    assert 0.0 <= d["confidence"] <= 1.0
    t = d["trigger"]
    assert set(["changed_main","reserve_used","disputed","reason"]) <= set(t.keys())
    ok += 1
print("written:", len(written), "verified:", ok)
print(sorted(written))
