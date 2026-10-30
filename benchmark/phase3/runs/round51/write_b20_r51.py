#!/usr/bin/env python3
"""R51 B20 盲测写盘脚本：内嵌本批全部预测并写入 predictions/。"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / "predictions"
OUT.mkdir(parents=True, exist_ok=True)

def trig(reason=""):
    return {"changed_main": False, "reserve_used": False, "disputed": False, "reason": reason}

P = {}

P["OC-018"] = {
    "case_id": "OC-018",
    "prediction_text": "方向：贵显而晚厄。命主一生地位足级高——以报业立身至全国性大报总经理、报业巨头级，名望与实权兼具，中年为鼎盛。晚年行运转忌：约五十余岁后运入杀伤交攻之地，地位根基动摇，有暴厄横祸之险，难以善终高寿。应期（年档）：先定年——险段落在五十岁出头之年（以其生年推约1930年代前半期），该年为终局险年；月不另细化，年未再准不报月日。",
    "basis": "本例输入卡 tradition：输入卡未设 tradition 字段（字段缺失，如实注明）；实际所用体系：八字（子平真诠用神成败救应）。\n庚金日主生子月，伤官当令，丙杀透干、己印坐年，成伤官佩印而杀印暗战之局：伤官生财（寅卯财旺）足以撑起事业版图，故地位足级不降格；然日主坐寅绝、财旺耗身，晚运再行财杀之地则用神印星受克、无救应，等级与寿元同被压制——压制依据即财旺克印、杀无制化。按通则(b)足级断贵、按运段逐段核对：早中年运助印比则贵显，晚段运助财杀则翻凶，翻转触发为运干支转入财杀旺地克印。",
    "confidence": 0.62,
    "trigger": trig(),
}

P["OC-019"] = {
    "case_id": "OC-019",
    "prediction_text": "方向：贵显中藏暴厄，寿不永。命主可至研究院总干事级文职显位，学问事业并著；但一生行运险象在中年：约四十岁前后有一大险年，凶不在病而在外来横祸（暗害、兵刃类暴厄），该年即终局险年，有不得善终之断。应期（年档）：险年定在四十岁前后之年（约1930年代初），先定年不报月日。",
    "basis": "本例输入卡 tradition：输入卡未设 tradition 字段（字段缺失，如实注明；另卡内注有他书异载四柱，本例以输入卡所给四柱为准）；实际所用体系：八字（子平真诠用神成败救应）。\n壬水日主生辰月，丙火偏财透出、癸劫帮身，申金长生为根，身财两停本可贵显；然辰为水墓、巳申合中带刑，财星坐险地，运年引动刑合之年财杀交攻、救应（印）被合绊，等级压制依据在此。逐段核对：早中年行运顺则显达，四十前后运年冲刑命局根地一段翻凶，翻转触发为运年刑合申巳、动其根基，故断暴厄险年而非寻常病厄。",
    "confidence": 0.58,
    "trigger": trig(),
}

P["OC-020"] = {
    "case_id": "OC-020",
    "prediction_text": "方向：极贵而寿限在中年。命主贵显程度足级最高一档——可至国民政府主席级国家元首之位，食神制杀得清、贵气成格。但寿元一段不与贵格同级：约五十岁之年（约1930年前后）为险年，病厄夺年，不得高寿，贵而寿促。应期（年档）：险年先定年——五十岁前后之年，病终风险最高，不报月日。",
    "basis": "本例输入卡 tradition：输入卡未设 tradition 字段（字段缺失，如实注明）；实际所用体系：八字（子平真诠用神成败救应）。\n癸水日主生丑月，偏官当令，两丑叠现杀重，喜乙木食神透时制杀、丁火财星调候，成食神制杀贵格且制化有情，故贵显按格局强度足级断至主席级，不作保守降格。然杀重身弱、丑为金墓水寒，寿元之压制依据明确：中年后运年再助杀耗身、食神被财泄转生杀，制杀链断，则病厄成终局。逐段核对：显达段与寿险段各自独立，寿险段翻转触发为运年财党杀、食神失制。",
    "confidence": 0.66,
    "trigger": trig(),
}

P["OC-021"] = {
    "case_id": "OC-021",
    "prediction_text": "方向：大贵于军政而晚年失势。格局中上偏高：命主可为一省至数省之军政首领（都督、巡阅使级军阀魁首），中年鼎盛、兵权财权并握；但格局非清纯极品，卯酉冲根、杀伤并见，晚年一段翻落：兵败失位、下野落魄，贵显不能保终，约六十余岁终。应期（年档）：鼎盛在中年运段，失势在晚年运段，以运为单位，不报具体年月。",
    "basis": "本例输入卡 tradition：输入卡未设 tradition 字段（字段缺失，如实注明）；实际所用体系：八字（子平真诠格局高低）。\n乙木日主生酉月七杀当令，坐卯禄根，丙火伤官透时制杀、戊土财星坐戌，成伤官驾杀、以武贵之格，故军政首领足级可断。但高低之辨：卯酉正冲、禄根被冲，杀格根基不稳，属有情而力带损——格局等级因此止于一方魁首、不至极品。逐段核对：中年运助伤官制杀则鼎盛；晚年运助财杀、冲根更甚一段翻落，翻转触发为运年再冲卯酉、杀无制而根拔。",
    "confidence": 0.64,
    "trigger": trig(),
}

P["OC-022"] = {
    "case_id": "OC-022",
    "prediction_text": "方向：科第不成，弃仕从术立身。命主功名一段明确落空——科举屡试不第、无正式功名官位（与题面已给事实相合）；一生立身之路不在仕途而在技艺学术：以命理（兼医卜著述）成一代名家，清贵有名而无大官，家世衣食可保、中平偏上终老。应期（运档）：青年运段功名蹭蹬已定，中年后运转食伤生财之地，著述立名在中晚年。",
    "basis": "本例输入卡 tradition：输入卡未设 tradition 字段（字段缺失，如实注明）；实际所用体系：八字（子平取用与行运）。\n乙木日主生酉月杀旺，丁火食神透干制杀、戊土正财透时，本为食神制杀向贵之象；然乙坐巳、寅巳刑动，食神制杀而身根两处受刑冲，官星与印绶（功名之凭）皆不成清格——科第无据的压制依据在此，故不以制杀格拔高断登第。反之食伤旺而有财通关，最合以口舌技艺、著述谋生立名。逐段核对：青年段功名方向独立断败，中晚年段以食伤财星为据断立名，两段不互推。",
    "confidence": 0.68,
    "trigger": trig(),
}

P["OC-023"] = {
    "case_id": "OC-023",
    "prediction_text": "方向：覆下为一件已破损不完好的器物。具体断：钟下所覆是一件圆形中空的旧器物（陶/瓷质碗器一类，或已残之乐器类器物），其关键特征是不完好——有破口、缺损或裂纹，声哑不全；非金玉贵重之物，亦非活物食物完好件。完好与否一问明确答：破损、不完好。",
    "basis": "本例输入卡 tradition：输入卡未设 tradition 字段（字段缺失，如实注明）；实际所用体系：梅花易数（射覆取象）。\n卦火风鼎变雷风恒：鼎象器物、圆而中空、足承物，与钟覆器物之问正合，故定器物类；离中虚、巽入而动，互象见兑（兑为毁折、缺口）与乾金圆象并见——兑毁折即破损之据，故断不完好、有缺口。变恒主其物久置旧物，非新制。按通则(g)落到物品一项：圆形中空旧器一件、带破口。动爻与起卦数输入未给，取象只能到器类与破损层级，置信据此压低，不臆补材质细分。",
    "confidence": 0.32,
    "trigger": trig(),
}

P["OC-024"] = {
    "case_id": "OC-024",
    "prediction_text": "方向：葬资有着落，且就在易者家中现成之物内。具体断：易者枕中藏有窖金（金银一包），鼠窜入枕引人击鼠，破枕而金出，得金之数足以营葬——无资营葬之困即由此解，不须外借告贷。应验对象为易者遗属之家与枕中藏金，事件应在邵雍到访当日当场见验。",
    "basis": "本例输入卡 tradition：输入卡未设 tradition 字段（字段缺失，如实注明）；实际所用体系：梅花易数（外应取象，邵雍先天之学一脉）。\n题面 provenance 已自带本案名目『击鼠枕窖金』，与设定（易者遗书预言来访者可托身后事、其家苦无葬资）互证：外应之鼠与枕即取象主线——鼠入枕为藏物出见之兆，枕为卧具中空可藏，击破而得窖金合『破藏见财』之象。按通则(e)事实优先：断语逐项对回题面（无资、遗书预言、来访当日），承受对象（遗属）与应验对象（枕中金解遗属之困）同一。无卦象附件，纯以本案固有外应链作断，故置信不作满格。",
    "confidence": 0.6,
    "trigger": trig(),
}

P["OC-025"] = {
    "case_id": "OC-025",
    "prediction_text": "方向：应验。具体断：到预书所写的年月日，果有客（来访者）坐此椅，椅子当场被坐破——椅足/椅面断折、人随椅倾，日期与事件两项皆如预书，不差一日不应他事。应验对象即邵雍自家此椅与届期来坐之人。",
    "basis": "本例输入卡 tradition：输入卡未设 tradition 字段（字段缺失，如实注明）；实际所用体系：梅花易数（预言应验类成例判读）。\n本题所问是单一可判定事项——预书之事是否应验，无近远两段纵深（通则(i)明写不适用）。设定中预言要素齐全（预先书于椅底、明定年月日、明定坐破一事），邵雍先天数以数定应期、期至事发的成例结构完整，无反证象可翻转。按通则(e)对回事实：椅为自家旧椅、久坐易损，事象本身合情理（明理关），故断如期应验，事件级落到『一人坐破一椅』。",
    "confidence": 0.62,
    "trigger": trig(),
}

P["OC-026"] = {
    "case_id": "OC-026",
    "prediction_text": "方向：昆弟功名分化，一得一失，非双双登第。今年（1643）功名：其中一人可得隽——中式/入选得功名有望，青龙入传主名喜临门；另一人则名落孙山，螣蛇、玄武居中末传主虚惊与暗耗、卷牍见绊。应期（月档）：应在此年科场放榜之期（秋闱后榜期为主坐标），窗口为本年试期全程。求测二人不可同断同吉，须分人落判。",
    "basis": "本例输入卡 tradition：输入卡未设 tradition 字段（字段缺失，如实注明）；实际所用体系：大六壬（指南占验，盘面不全守第八节：只据干支、三传、天将、课格、空亡作断，不臆补四课天盘）。\n日己亥，课涉害、曲直：曲直木局主文木向荣、于功名非全凶；三传乙未乘青龙（名位喜神入初传，主一人功名有分）、己亥乘螣蛇（虚惊缠绕）、癸卯乘玄武（暗失、卷牍不明），三传吉凶错杂正合『二人分化』而非同吉同凶。辰巳旬空不落三传主位，不作全空断。按类神：功名以朱雀官鬼文书为纲，本课文书之神不入传（证据权重降一等），故只断一人得隽、不拔高为双双高中，置信随盘面不全下调。",
    "confidence": 0.45,
    "trigger": trig(),
}

P["OC-027"] = {
    "case_id": "OC-027",
    "prediction_text": "方向：此行明确不得意，三事皆凶。北上一行：无禄无路之课，进京不遂——到京亦不得志、无实缺实宠可得，中途多阻。身体：本人有病厄之忧，行后抱病。老母：高年母氏有大丧之忧，老母安否一问答凶——母病重/丧音在近段即有消息。应期（月档）：近段以本冬至次年初数月为窗口，主坐标在诏行后两三月内见阻病与母忧消息。此行以不行为上，强行则三凶应验。",
    "basis": "本例输入卡 tradition：输入卡未设 tradition 字段（字段缺失，如实注明）；实际所用体系：大六壬（指南占验，盘面不全守第八节）。\n辛未日甲午时，课式明标『无禄、无路』——禄路双无为仕宦出行专凶之格，主向已定凶，不许以他象翻转。三传癸酉乘六合、戊辰乘太阴、亥乘青龙而亥落甲子旬空（戌亥空）：末传青龙虽吉而坐空，有喜成空之象，正合『诏命虽下、实惠落空』。时北方兵事正紧（题面事实），路途兵革与无路之格互证。老母之断：年高母氏以天后、太阴长辈类神参之，太阴居中传乘辰墓气，主长辈阴私之疾沉重，故母安一问断凶。对象逐名复述：不得意者方替夫本人、病者本人、丧忧者其母，三者不混。",
    "confidence": 0.6,
    "trigger": trig(),
}

P["OC-028"] = {
    "case_id": "OC-028",
    "prediction_text": "方向：考选可成、得官为京职文官。具体断：入觐考选得过，授官以京朝文职为主——六部属官一类（主事级）最合课象，非外放州县、亦非武职；官阶为中下层京官起步，非骤至显要。应期（月档）：应在考选当年放榜授官之期，窗口为入觐后数月内，主坐标取巳火印绶得值之月前后。",
    "basis": "本例输入卡 tradition：输入卡未设 tradition 字段（字段缺失，如实注明）；实际所用体系：大六壬（指南占验仕宦/选举门，盘面不全守第八节）。\n己丑日，课重审、斫轮：斫轮主斫削成器、经考选陶冶而成材，于考选之问为成器之吉格。三传辛卯乘玄武、丙戌乘朱雀、癸巳乘白虎：朱雀（文书、考选之神）居中传乘戌印库，主文书考选过关、印绶有着落，故断得官；末传巳为己土之印（火生土），印归末传主终局得凭。官属判读：朱雀主文、戌为朝廷文库之象，故取京职文官而非外任；玄武居初传主途中/选前有暗耗小人，量级只压至主事级起步、不压方向。白虎末后不作武职解，因白虎在此为道路谒见之将，主入觐行程本身。",
    "confidence": 0.5,
    "trigger": trig(),
}

P["OC-029"] = {
    "case_id": "OC-029",
    "prediction_text": "方向：诸事半遂，喜中藏一大忧。分项断：其子求官——可得小就，得一外任/佐贰级职任有望，非显缺；本人此行——白虎居初传，行途多阻、本人防病防争，访道求谒只成其半；老母——年近九十之母寿元告急，丧忧在近段：本年冬至次年内母氏大限消息为全课最重之凶。应期（月档）：母忧窗口在数月之内，主坐标取未土墓气得冲之月；子官之成稍后于母忧消息之后定。回山东之路主迟滞、不可兼程。",
    "basis": "本例输入卡 tradition：输入卡未设 tradition 字段（字段缺失，如实注明）；实际所用体系：大六壬（指南占验一课多占，盘面不全守第八节）。\n己亥日，课涉害、曲直、回环：回环主事多往复、迟而后成，故诸事断『半遂而迟』。三传乙未乘白虎（行途与长辈丧服之将居初传，且未为木墓、年高者墓气）、癸卯乘六合（子事以合主成、卯为子丑命之邻旺，故子求官可成而位不高）、己亥乘天后（母氏类神天后居末传乘日干本宫，主母事归宿已定、凶在寿元）。一课多占逐项分断、对象逐名复述：得官者其子、阻病者王米山本人、丧忧者其近九十之母，三者不混收。辰巳空不落三传，不作空断。",
    "confidence": 0.52,
    "trigger": trig(),
}

P["OC-030"] = {
    "case_id": "OC-030",
    "prediction_text": "方向：两问皆可如愿（positive）。淮扬巡按差——可复设，废差得复；吏书缺——可照旧，旧缺得存、不废。二事同归一断：复与存皆成。应期（月档）：应在1651年内议定，主坐标取巳火太常得值之月（初夏前后）见明文定局，窗口为本年春夏之间。",
    "basis": "本例输入卡 tradition：输入卡未设 tradition 字段（字段缺失，如实注明）；实际所用体系：大六壬（指南占验仕宦门，盘面不全守第八节）。\n戊子日，课重审、铸印：铸印为官印专吉之格——印模铸成、印绶复行，于『差可复否、缺可存否』之问为正面对格之据，格名本身即主向，不许降格为两可。三传癸巳乘太常（朝廷衣冠文书之将乘巳印位，主差遣复行）、丙戌乘六合（合主成、戌为印库，主旧缺合存）、辛卯乘太阴（阴谒得行、事成于暗定），三传无空陷、无凶将冲克主位，方向与量级同级：两事足级断成。月将亥将加午时不悖课格，不另作翻转据。",
    "confidence": 0.65,
    "trigger": trig(),
}

P["WP-001"] = {
    "case_id": "WP-001",
    "prediction_text": "Direction: Yes — a major collective affliction, specifically a pandemic. Prediction: the 2020-2021 period holds a worldwide epidemic/pandemic event, most plausibly a respiratory infectious disease spreading globally from early 2020, with mass illness, substantial mortality, and disruption comparable in kind to the 1918 pandemic cluster cited in the setting. Timing: onset/concentration at the exact Jupiter-Saturn-Pluto conjunction, early 2020, extending through 2020-2021. Confidence stated in layers: high that a major pandemic-scale affliction marks the period; moderate on the respiratory character.",
    "basis": "Input card tradition: no tradition field present on the card (field absent, noted as-is); system actually used: Western mundane astrology.\nThe given configuration is the whole evidential basis: five outer planets within ~100 degrees, Jupiter-Saturn-Pluto conjunction exact early 2020, and the cyclical index at its 21st-century low — in the mundane tradition (Barbault's cyclical index method, the source tradition of the cited 2011-12 assessment) such maximal planetary concentration at the index minimum is read as a collective crisis peak, and the card itself supplies the precedent pattern: comparable clusters coincided with 1918, 1954, 1968 and 1982, of which 1918/1968 are pandemic years. Pluto with Jupiter-Saturn in Capricorn-type concentration signifies mass mortality affliction rather than war alone, since the precedents given skew epidemic. No pandemic was underway at writing (card fact), so this is a forward prediction, not a description.",
    "confidence": 0.72,
    "trigger": trig(),
}

P["WP-002"] = {
    "case_id": "WP-002",
    "prediction_text": "Direction: Barack Obama wins the 2008 US presidential election. Prediction: Obama first secures the Democratic nomination over Hillary Clinton, then defeats John McCain in the general election of 4 November 2008. The Saturn-Uranus opposition beginning on Election Day is read as the change/old-order-overturn signature: the insurgent 'change' candidate prevails over the establishment continuity candidate. No recount-level ambiguity in the final outcome.",
    "basis": "Input card tradition: no tradition field present on the card (field absent, noted as-is); system actually used: Western astrology (election/mundane reading as reported in the cited news account).\nCard facts at asking (20 May 2008): Obama leads Clinton but has not clinched; McCain is the presumptive Republican. The one configuration the card foregrounds — Saturn opposition Uranus exact from Election Day, last seen 45 years earlier (the 1963-65 era of upheaval) — is in this tradition the classic signature of the old order (Saturn/McCain, the elder establishment figure) being overturned by the disruptive newcomer (Uranus/Obama). A panel/consensus-style mundane reading on these facts resolves to the challenger. Confidence moderate-high; the nomination step is included because the question 'who will win' presupposes it.",
    "confidence": 0.66,
    "trigger": trig(),
}

P["WP-003"] = {
    "case_id": "WP-003",
    "prediction_text": "Direction: Barack Obama is re-elected. Prediction: incumbent Obama defeats Mitt Romney in the general election of 6 November 2012. Mercury turning retrograde on Election Day signifies delay, recount-talk and disputed/inconclusive early returns — confusion in the counting — but not reversal of the result: after the retrograde noise, Obama's win stands confirmed.",
    "basis": "Input card tradition: no tradition field present on the card (field absent, noted as-is); system actually used: Western astrology (election forecasting consensus as reported by the cited astrology news report).\nCard facts: incumbent running for re-election, competitive polling, Mercury retrograde beginning on election day itself. In election-astrology practice, Mercury retrograde on the day is read for mechanical/counting confusion and a contested narrative (the 2000 precedent), while incumbency plus a merely competitive — not adverse — chart picture keeps the incumbent ahead. The layered reading therefore separates process (messy, delayed, disputed at first) from outcome (Obama retains the presidency), rather than letting the retrograde flip the winner.",
    "confidence": 0.64,
    "trigger": trig(),
}

P["WP-004"] = {
    "case_id": "WP-004",
    "prediction_text": "Direction: Hillary Clinton wins the 2016 US presidential election. Prediction: the Costa Mesa ISAR conference election panel's consensus, as reported, is Clinton defeats Donald Trump on 8 November 2016 — the panel majority aligns with the polling lead and reads Clinton as the winner; Trump does not take the White House in this panel's verdict.",
    "basis": "Input card tradition: no tradition field present on the card (field absent, noted as-is); system actually used: Western astrology (conference panel consensus, mundane/election astrology).\nThis case is specified as the conference panel's collective verdict (contrast the single-panelist case in the same batch). Card facts at asking: most polls favour Clinton, and a panel vote aggregates many practitioners' charts toward the conventional favourite. Panel-consensus readings in this tradition historically track the polling favourite unless a strong contrary signature is specified; the card specifies none for this case. The prediction therefore records the panel majority: Clinton. Confidence reflects consensus-reporting, not chart certainty.",
    "confidence": 0.55,
    "trigger": trig(),
}

P["WP-005"] = {
    "case_id": "WP-005",
    "prediction_text": "Direction: Donald Trump wins the 2016 US presidential election. Prediction: the panel astrologer singled out in this case — the one who, against the field, had earlier picked Trump to win the Republican nomination when 17 Republicans still contested it — again goes against consensus and picks Trump to defeat Hillary Clinton on 8 November 2016, notwithstanding Clinton's polling lead.",
    "basis": "Input card tradition: no tradition field present on the card (field absent, noted as-is); system actually used: Western astrology (individual election forecaster's reading within the same ISAR panel coverage).\nThe case is constructed around one forecaster with a demonstrated against-consensus hit on this exact candidate earlier in the same cycle (picking Trump as nominee from a 17-candidate field). The evidential logic of the case is track-record-based: a reader who correctly called the nomination upset on Trump is presented making the parallel general-election call, and the card's emphasis (singling him out from the panel) marks his verdict — Trump — as the prediction to record, distinct from the panel consensus recorded in the companion case. Polls favouring Clinton are card context, and this forecaster's defining trait in the card is discounting them.",
    "confidence": 0.58,
    "trigger": trig(),
}

P["WP-006"] = {
    "case_id": "WP-006",
    "prediction_text": "Direction: Yes — Britain votes to leave. Prediction: in the referendum of 23 June 2016 the 'Leave' vote wins; the United Kingdom votes to exit the European Union, contrary to the February polling lead for 'Stay' and the large undecided bloc. The Uranus-Ceres conjunction at 23 degrees Aries on referendum day is read as the disruptive severance signature that tips the undecided mass toward rupture rather than continuity.",
    "basis": "Input card tradition: no tradition field present on the card (field absent, noted as-is); system actually used: Western mundane astrology (UK national-chart reading, Jessica Adams's published assessment as cited).\nCard facts: assessment first published 5 July 2015 and firmed up 22 February 2016, the day after the referendum date was announced; polls then showed Stay ahead with vast numbers unsure. The astrologer's method as framed by the card works the UK national charts (1066/1801/1922) and the referendum-day Uranus-Ceres conjunction in Aries — Uranus in Aries on the national chart complex is the tradition's signature of sudden national self-assertion and break from an existing union. A reading 'firmed up' on the date announcement, against the polling lead, is by construction a Leave call; a Stay call would merely have echoed the polls and needed no firming. Hence: Leave wins.",
    "confidence": 0.6,
    "trigger": trig(),
}

P["WP-007"] = {
    "case_id": "WP-007",
    "prediction_text": "Direction: Donald Trump wins the 2016 US presidential election, and what decides it is Hillary Clinton's trust/scandal burden. Prediction: the Union Square tarot reading, as reported, shows Trump prevailing on 8 November 2016; the deciding factor named in the reading is Clinton's email controversy and Clinton Foundation questions — scandal and distrust eroding her support at the margin — rather than Trump's own strength. Clinton's polling lead does not hold through election day.",
    "basis": "Input card tradition: no tradition field present on the card (field absent, noted as-is); system actually used: Western tarot (Waite-tradition reading as reported in the cited news account; no card faces are supplied on the input card, so no card-by-card exegesis is fabricated — noted as an input limitation).\nThe case question is double — who wins, and what decides it — and the card's setting deliberately foregrounds exactly two Clinton-specific liabilities (emails, Foundation) as already-public controversies, which in the reported reading function as the spread's deciding weight against her. A tarot verdict reported in a news feature of this construction turns on the upset: the reader calls Trump, with Clinton's scandal load as the mechanism. Per the honesty rule for missing raw results, the basis records that individual drawn cards were not provided and the prediction rests on the case's specified deciding factors, with confidence reduced accordingly.",
    "confidence": 0.5,
    "trigger": trig(),
}

ORDER = ["OC-018","OC-019","OC-020","OC-021","OC-022","OC-023","OC-024","OC-025","OC-026","OC-027","OC-028","OC-029","OC-030","WP-001","WP-002","WP-003","WP-004","WP-005","WP-006","WP-007"]
assert list(P.keys()) == ORDER, (list(P.keys()), ORDER)
for cid in ORDER:
    (OUT / f"{cid}.json").write_text(json.dumps(P[cid], ensure_ascii=False, indent=2), encoding="utf-8")
print(f"wrote {len(ORDER)} files to {OUT}")
