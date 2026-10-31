# -*- coding: utf-8 -*-
"""R87 B20 blind predictions writer. Only writes round87/predictions/<case>.json for B20 ids."""
import json, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round87/predictions"
IDS = ["OC-018","OC-019","OC-020","OC-021","OC-022","OC-023","OC-024","OC-025",
       "OC-026","OC-027","OC-028","OC-029","OC-030","WP-001","WP-002","WP-003",
       "WP-004","WP-005","WP-006","WP-007"]

def trig():
    return {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}

P = {}

P["OC-018"] = {
 "prediction_text": "方向：贵显而晚运有暴变之险。史量才命杀印相生得用，一生地位高，可至大型机构主事、报业主持级（格局量级区间：下限为机构中层主事——依据杀印链成而身有印根；上限为一方行业巨头级主事——依据丙杀当令透干、己印通根生身，杀印双清）。早中年运助印化杀则事业上升；晚段转入午火运段，午冲子月令、杀伤相战，地位虽在而运势逆转，主突发变故、暴险伤身，晚景不宁。应期尺度为运档：卡面未给出生年月日与起运岁数，流年层坐标缺位降格，只给运档坐标——险运坐标为庚午运段（运档，窗口置信），顺主线之峰值段在己巳运段前后（印杀土火相生）。",
 "basis": "卡面无 tradition 字段（本例以四柱八字题面呈现），按子平格局法自决作断。\n四柱己卯丙子庚寅辛巳：庚金日主生子月，丙火七杀透月干当令，己土正印透年干，杀印相生链（丙→己→庚）成；日坐寅绝、时巳藏丙戊，印杀有根。特格扫描：从格未命中（庚有辛助、己印生扶、巳藏戊印，非无根无援）；专旺未命中；寒极近似（子月水旺）而丙巳火有根能暖，不作寒极格。运断主线：①格局杀印相生成；②用神为印（土）兼火调候，印得己透而根浅是其病；③顺印化杀之势者吉、冲月令子水伤官引杀伤战者凶。男命年干己阴逆行，大运自乙亥逆排：乙亥、甲戌、癸酉、壬申、辛未、庚午、己巳——前段金水运泄耗参半，中段辛未土印渐得力，庚午运午冲子（月令伤官）、杀来冲根为转折运：作用表——午→病字子水：冲，月令被冲；午→用神己印：火生土得助；两证参半从用神外象看似得助，然月令被冲、杀伤相战为格局根基动摇，定逆。功量清单（R80-REV1，等级断项）：助成线——丙杀生己印（源丙火，当令透干，旺）→对象格局，助成；己印生庚身（源己土，透干坐卯无强根，中）→对象日主，助成；压制线——子水伤官克丙杀（源子水，月令旺）→对象杀星，压制；寅巳刑与辛劫透只作量级调节。做功主线：杀印相生链（丙→己→庚）直接作用于格局且杀星当令居首，定带为高带，断至行业巨头级主事，不越上限。子女/承继：时柱辛巳，男命官杀为子星，丙杀两见（月干与巳藏）主有子承业而缘分带刑冲，承继不稳。病位：病字在子水伤官与被冲之月令，水火相战，病位主心肾、血脉突发之患。破耗之因：伤官见官、午运冲月令，因职位是非与突发事变耗损，非财务经营之破。一生高峰运段：己巳运段（印杀得地、顺主线），庚午为险运。交运带与终局两运（庚午、己巳）独立判定：庚午逆（冲月令），己巳顺（印杀相生得根）而承暴变之后，晚景只作不宁断，不无据翻贵。应期三路：运年触发取午冲子之运（取）；合冲引动同指庚午（与上路同点）；值年值月因出生年月缺失无候选。坐标置信：运档窗口。",
 "confidence": 0.52}

P["OC-019"] = {
 "prediction_text": "方向：早中年显达、中年入金水险运有横变之险。杨杏佛命身旺任财、食伤生财，早运木火顺遂，可至研究院总干事级要职（格局量级：下限机构要职，依据壬坐申长生、癸劫帮身、丙财透有根；上限全国性机构主事级，依据财格成而食伤卯木引化）。险运在逆行癸丑之后转壬子、辛亥金水运段：比劫夺财、水旺冲巳、财源与火用俱伤，主职位动荡并有暴变横祸之险，险年以子、亥水旺冲克巳火之年为最。应期尺度运/年档：卡面未给出生的公历年月日时，年龄坐标缺位降格，以运档加水旺流年层表达（窗口置信）。",
 "basis": "本例卡面未见 tradition/system 字段，题面为四柱评注体裁，按八字自决。\n四柱癸巳丙辰壬申癸卯：壬水日主坐申长生，癸劫透两干（年、时），辰为水库，身旺；丙火偏财透月干坐辰，巳中丙有根，卯木食神泄秀生财，财格成立。用神财火，病在比劫癸水两透夺财、巳申合刑动财根。特格扫描：从格、专旺、极端偏枯均未命中（壬有申根、癸助，非从；水未成局专旺）。男命年干癸阴逆行，大运自乙卯逆排：乙卯、甲寅、癸丑、壬子、辛亥、庚戌。木火运（乙卯甲寅）食伤生财顺主线为上升段；壬子运为转折运，作用表：子→病字癸劫：同类填实助劫夺财，逆证；子→用神丙财：子水克火且冲巳财根，逆证——两证同逆，定低谷险运；辛亥运亥冲巳同理。功量清单：助成线——卯木食神生丙财（源卯木，时支得辰土培，中旺）助成；申金印生壬身（源申金，日支长生，旺）助成身旺任财；压制线——癸劫夺丙财（源癸水，两透，旺）压制；巳申合刑动财根（中）压制。做功主线：食伤生财线直接作用财星、状态居首，定带高带中位，断至全国性机构主事级，不拔至政要极品（劫夺压制线在，故不取上限外）。子女：男命官杀为子，土官藏辰巳不透，主有子而星不显。病位：病字癸水比劫与受冲之巳火，水火相战，病位主心血、突发外伤之险。破耗之因：比劫夺财，因同僚竞争与突发事变耗损。高峰运段：甲寅运段（食伤木旺生财、顺势）。终局两运辛亥、庚戌独立判定：辛亥逆（冲巳），庚戌平中带稳（戌土官库收水），险在中年而非终局骤败，故断中年横变、非晚年。应期三路：运年触发取壬子运（取）；合冲引动取亥冲巳之年（同向备选入 reasoning 舍为运内流年层）；值年值月无出生数据无候选。坐标置信：窗口。",
 "confidence": 0.52}

P["OC-020"] = {
 "prediction_text": "方向：贵显极高而险年在火土杀旺无救之年。谭延闿命食神制杀得局、复得运救，可至政府主席级政要（格局量级区间：下限为方面要职——依据乙木食神两见制己土七杀、制杀链成；上限为国家级主席位——依据制杀成格且中年金水运化杀生身、救应到位）。其病在身弱无印：癸水日主坐丑墓、重丑叠己，印星金全缺，全靠运补。贵显期在逆行癸酉、壬申金水运段（印化杀、身得扶）；险年在转入火土流年与辛未、庚午运段，杀重身衰、食神被财坏，主病险与位高身危，险年以未冲丑、巳午火旺生杀之年为最。应期运/年档，年龄坐标因卡面无出生日期缺位降格（窗口置信）。",
 "basis": "卡面未标注 tradition，按题面四柱自决子平法。\n四柱己卯丁丑癸丑乙卯：癸水日主生丑月，己土七杀透年，丁火偏财透月生杀，两丑伏吟日月，身弱杀重；乙木食神透时、两卯食神得地，食神制杀链（乙卯→己）成，为本命救应；印星金全缺为大病。特格扫描：从官杀未命中（癸坐丑有余气根、乙卯食神旺而制杀，日主非无自立抗衡之路，且制杀之字旺相逆势，从格判据③不具）；专旺、偏枯未命中。运断主线：①格局食神制杀成而带病（无印）；②用神取印（金）化杀生身、兼食神制杀，印不在原局、待运补；③顺制化之运吉、助杀坏食之运凶。男命年干己阴逆行：丙子、乙亥、甲戌、癸酉、壬申、辛未、庚午。癸酉运转折判定：酉→病字己杀：酉金为印，化杀，顺证；酉→救应乙食：金不克木于支位、印护身，顺——定贵显峰段候选；辛未运：未→月日两丑：冲，根基动；未中丁火生己杀、乙木入墓，食神救应受损，逆，定险段。功量清单：助成线——乙卯食神制己杀（源木，两透两支，旺）助成格局；运金印化杀（运线，癸酉壬申段得地）助成；压制线——己杀克癸身（源土，透年得两丑，旺）压制；丁财生杀坏食（源火，透月）压制。做功主线：食神制杀线直接作用于杀星且木旺居首，定带高带；上限由运印救应到位支撑至主席级，下限由无印之病保至方面要职。峰值运三核对：癸酉运①用神印酉得地满足；②运干癸帮身呼应满足；③否决三条：(i)运干合绊用神未命中 (ii)运支冲克用神之根未命中（酉与卯冲，冲者为食神救应之根，此为量级扣分而非冲用神印根） (iii)透忌神且通根未命中——满足3项（带扣分注记），定峰值；壬申运次峰。子女：男命官杀为子，己杀透而两丑藏癸，子星有而宫位伏吟，主有子承继而多波折。病位：病字己土杀与无印之癸水，土重水弱，病位主脾胃、湿土壅塞及心肾之患，险年病发。破耗之因：财生杀旺，因公职耗神与病患耗损。高峰运段：癸酉运段。应期三路：运年触发取癸酉运（贵显定值至运层）；合冲引动取未冲丑之年为险年（取为险坐标）；值年值月缺出生数据无候选。坐标置信：运档定值、险年窗口。",
 "confidence": 0.55}

P["OC-021"] = {
 "prediction_text": "方向：武贵显赫一时而终局失势。陆荣廷命乙木坐卯禄、身强任杀，丙火伤官制辛金七杀得权，格局可至一方军政首领（封疆级；格局量级区间：下限为统兵方面将领——依据日坐卯禄身强、杀有制；上限为一省军政首领——依据杀印未备、卯酉冲破禄，故不至全国极品）。大病在卯酉冲：月支酉杀冲日支卯禄，根基与官星相战，一生权位动荡、得而复失。顺行丙寅、丁卯前后木火运制杀得势为上升与高峰段；再逢卯酉冲动加密、或入金水运杀印相战之段，主失势落拓，晚景平常，不能善保其位。应期运档为主，年龄坐标缺位降格（窗口置信）。",
 "basis": "本卡未载 tradition 字段，依四柱题面以子平格局法作断。\n四柱戊午辛酉乙卯丙戌：乙木日主坐卯禄身强，辛金七杀透月干坐酉旺，丙火伤官透时干制杀，戊土正财透年生杀，午戌半合火助制。格局伤官制杀（兼杀旺身强任之）成；病字为卯酉冲——酉杀冲卯禄，官星与根基相战。特格扫描：从格未命中（乙有卯禄强根）；专旺未命中（杀旺对峙非一气）；偏枯未命中。男命年干戊阳顺行，大运自壬戌顺排：壬戌、癸亥、甲子、乙丑、丙寅、丁卯、戊辰。壬癸亥子水印运化杀生身为平稳上升；丙寅丁卯木火运食伤制杀得地为峰段候选，其中丁卯运卯再冲酉，顺逆参半：作用表——卯→病字酉杀：冲克杀星，顺证（制杀）；卯→日主禄根：同字叠禄得助而冲战加密，量级受限——定为峰而带破。功量清单：助成线——丙火伤官制辛杀（源丙火，透时得午戌火势，旺）助成；卯禄扶身任杀（源卯木，日支禄，旺）助成；压制线——卯酉冲（源酉金，月支杀旺）压制根基；戊财生杀（源戊土，透年）压制。做功主线：伤官制杀线直接作用杀星且火势成局居首，定带高带，上限封疆、下限方面将领，断语落在上限侧。峰值运三核对：丙寅运①制杀之火寅为丙长生得地满足；②运干丙即伤官透出呼应满足；③否决：(i)合绊用神未命中 (ii)冲克用神之根未命中 (iii)透忌神通根未命中——满足3项定峰值；丁卯运因冲战只称次峰。子女：男命官杀为子，辛杀透坐酉，主有子而父子缘带冲克。病位：病字酉金杀冲卯木禄，金主肺与筋骨刀兵之伤、木主肝胆筋脉，病伤位在肝胆筋骨与兵刃外伤。破耗之因：财生杀、冲禄，因兵权争斗与部属耗损破财失势。高峰运段：丙寅运段。终局两运（戊辰及后续己巳段以辰为终局可见段）独立判定：戊辰财土生杀、辰酉合绊杀星，方向平转低，与定性（贵显而带冲破）对表，不无据翻贵。应期三路：运年触发取丙寅运（取）；合冲引动取卯年冲酉（作失势触发备选，舍为运内坐标）；值年值月无出生数据无候选。坐标置信：窗口。",
 "confidence": 0.55}

P["OC-022"] = {
 "prediction_text": "方向：科第不第、以技艺著述立身。袁树珊命食神制杀而印星全缺，功名之凭（印绶）不在局中，屡试不第为定局；一生立身之路在食伤泄秀：丁火食神、两巳伤官旺而制辛金七杀，主以文章技艺、术数著述得名得利，属名士术家之路而非仕宦科甲（等级量级：下限以技艺自立衣食丰足，依据食伤旺而财戊透；上限以著述名家立身，不至官贵，依据无印无官之成）。中晚年逆行至癸巳、壬辰水印运段，印星迟到，主晚年著述成帙、名声方定；早运丙申、乙未、甲午金木火运功名求之愈急愈蹉跎。应期运档，起运岁数卡面只注丙申起而无年龄，坐标缺位降格（窗口置信）。",
 "basis": "卡面未标 tradition/system，题面系自造自批四柱，按子平法自决。\n四柱辛巳丁酉乙巳戊寅：乙木日主生酉月，辛金七杀透年坐酉旺，丁火食神透月制杀，两巳伤官助制，戊土正财透时，寅木为乙之禄根在时支。印星水全缺——科第文书之凭无根，此为命之大病，亦定功名上限。身弱（酉月木囚、仅寅一根）而食伤旺泄，食神制杀成一半：制杀得名、身弱难任大贵。特格扫描：从格未命中（寅禄在、丁食制杀成链，非顺杀之从）；专旺、偏枯未命中（燥象近而寅根水缺，只作辅注）。运断主线：①格局食神制杀带病（无印、身弱）；②用神取印水补身护名，原局缺、待运；③顺泄秀制杀之运得名利，助杀克身之运蹉跎。卡面注大运丙申起，男命年干辛阴逆行：丙申、乙未、甲午、癸巳、壬辰、辛卯。癸巳壬辰运印星透（癸壬）为转折运：作用表——癸壬→病字辛杀：印化杀，顺证；→用神（缺印）：填实补用，顺证——定晚年上升段；惜巳运支与原局巳叠、辰为水库收印，量级只到著述名家。功量清单：助成线——丁食制辛杀（源丁火，透月，旺）助成名望；巳伤官助制（两支）助成；戊财通关食伤生财（源戊土，透时）助成生计；压制线——辛杀克乙身（源辛金，透年坐酉，旺）压制；无印护身（缺位，只记背景不计权）。做功主线：食神制杀线直接作用杀星居首，定带中带偏上，断至著述名家而非官贵（无印压制格局上限）。子女：男命官杀为子，辛杀透年，主有子而缘分早疏。病位：病字辛金杀与燥局无水，金主肺与筋骨、燥主津液，病位主肺系与筋骨。破耗之因：身弱财透，因求名应试与著述经营耗财，早年最显。高峰运段：壬辰运段（印填实、著述成名），次峰癸巳。终局辛卯运独立判定：卯冲酉杀、禄到，方向平，晚景自守，与定性对表。应期三路：运年触发取壬辰运（取）；合冲引动取卯冲酉之年（备选舍）；值年值月无数据无候选。坐标置信：窗口。",
 "confidence": 0.58}

P["OC-023"] = {
 "prediction_text": "方向：钟下所覆为可食之熟物且不完好。具体断：覆下是一件食物类器中之物——熟食/果蔬之属，质地中空或已剖开，带缺口破损，非完整整物；其形与鼎器烹饪之象相应，数量为一件（一物）。完好与否：不完好，已破缺或剖分。应期不适用（射覆即时验，无时间窗）。",
 "basis": "卡面未标注 tradition 字段，此例据题面射覆体裁以梅花易数自决。\n卦象卡面只给「火风鼎 变 雷风恒」，动爻未直给：鼎（离上巽下）变恒（震上巽下），上下卦比对仅上卦离变震，异在上爻，故动爻为上爻，此为据变卦反推、卡面残损处在此，已降置信。体用：动在上卦，上卦离火为用、下卦巽木为体，体生用（木生火）主耗泄、物有耗损之象。鼎卦本象为炊器与烹食，所覆之物取鼎中之食一类；离为中空、为丽、为干物与剖判之象，故断中空或已剖；上爻动主物之上端/整体将变，完好度受损。变卦恒上震木与体巽木比和，物性仍归木生火熟之食类。爻辞核对：未核得可逐字引之辞原文者不引辞作断，只走体用与卦象一路。事实优先：占题只给席间覆物一事，取象限于日常可覆于钟下之物，不放大。梅花自检：断语落具体项——物品（熟食果蔬一件）与状态（剖开破缺）两项；对象同类（问物断物）。量级守恒：日常射覆小事，只断物类与完好度。功量核算（R80-REV1）：本断无等级/数量分配断项，数量「一件」出鼎单物之象、不作功量定带，明写不适用细核。",
 "confidence": 0.35}

P["OC-024"] = {
 "prediction_text": "方向：葬资有着落、丧事可办成。具体断：易者身后无资之困可解——其遗居之内藏有可变现之金银（藏于枕中/窖藏一类隐处），取出足以营葬；发现之机在邵雍到访、言及遗书预言之后即时验得。应验判断：遗书预言应验，葬事终得办成。时间窗为到访当下即验（即时事，无远期窗）。",
 "basis": "卡面未见 tradition 字段，题面为梅花易数序文轶事体裁，按梅花事占自决；卡面残损严重：未给任何卦象、动爻、起卦数或外应记录，无法走体用生克与互变取象，本断只据占题事实（易者遗书预言可托身后事、其家苦无资营葬）与来源条目所署「击鼠枕窖金」之题名线索作低置信断，盘面依据不足已如实注明并大幅降置信。事实优先序：遗书既预言来访者可托，指向困局有解、藏资待发一线；对象定位：应验对象为易者之家与葬事本身，非邵雍本人之吉凶。具体断语密度：落物品（藏金银）与时点（到访即验）两项。量级守恒：葬资小事，只断资有着落、足办葬，不放大为富贵断。R80-REV1：含「足以营葬」之量级语，功量清单无盘面作用线可列（无卦），明写无据定带、只取方向性量级并降置信。",
 "confidence": 0.30}

P["OC-025"] = {
 "prediction_text": "方向：椅底预书之事会应验。具体断：届预书所载年月日，该椅将被坐破——坐破者为至其家之人（来客/访者坐其椅），椅体当场破损，预言按期成真。应期即预书所定之日（卡面未载具体日期数字，只给运档式定日坐标：预定当日，定值置信受卡面残损所限）。",
 "basis": "本例卡面未标注 tradition，题面出《梅花易数》序，按梅花预言事占体裁自决。卡面残损：未给卦象与起占记录，亦未载预书的具体年月日文字，本断无体用盘面可走，只据占题事实链作断——邵雍预先书字于椅底、明载某年月日椅将被坐破，此为以物为体、以届期人事为用之事占形态；预书本身即占断成品，本席独立复断取「应验」方向：椅为日常坐具、久坐受力，预定之日有人坐之而破，事象小而可验，合梅花小事量级。对象定位复核：承受对象为该椅（非人对象），应验对象同为该椅被坐破，未回收到邵雍本人吉凶。具体项：物品（椅一件）、时点（预书之日）两项。爻辞未引（无卦）。依据不足处（无盘面）已降置信。R80-REV1：无量级类断项，不适用。",
 "confidence": 0.50}

P["OC-026"] = {
 "prediction_text": "方向：今年功名可成（吉）。两客今年功名有成：三传亥卯未成曲直木局、官鬼纯旺入传，主得功名、榜上有名之喜；初传未乘青龙主先有喜庆音信，中传亥乘螣蛇主中途虚惊反复、末传卯乘玄武主名次或音信带暗昧，不至落空。应期：功名迁榜属月档——窗口为当年春季木旺之季（二至三月），窗口内主坐标取卯月（末传卯逢值、木局得令）。",
 "basis": "卡面无 tradition 字段，本例据课式三传题面以大六壬自决（占时己亥日辛未时、月将丑、甲午旬辰巳空）。\n盘面可据者：课式涉害、曲直；三传乙未（青龙）、己亥（螣蛇）、癸卯（玄武）。己土日干，官鬼为木：三传未亥卯恰成亥卯未三合木局，官鬼纯一入传且正月后木渐旺，仕宦门官星成局为功名主据（一级据：类神入传、局成、青龙乘初传合喜庆）。曲直格主举直错枉、福善祸淫。空亡核：辰巳空，三传无空，官星不落空，成象不虚。螣蛇中传只主过程虚惊，玄武末传主音信暗昧，均不翻官局主线（LR-QY-1 次面并读：官鬼主面为功名，次面祸患无白虎等将合参，不成立）。年命未给，行年路无据已注明；天盘全图、四课全列未给，不臆补（第八节）。应期三路：①逢值——末传卯逢卯月（取，木局得令与终局自洽）；②逢冲合——三合局合处在未，取未月则过季且与春季榜期尺度不合，舍；③出空填实——三传不空，此路无候选。档位：仕宦功名月档。R80-REV1：无量级类断项（不给名次数值，无盘面次第据），不适用。",
 "confidence": 0.60}

P["OC-027"] = {
 "prediction_text": "方向：此行不得意（负）；身体无大险、老母安。具体分判：①北上之行：课得无禄、无路凶格，官星火不入三传，末传亥乘青龙而落旬空（刖足），主奉诏北上终无所得、差事落空或无功而返，不得意；②身体：日干辛金得中传辰土父母生扶，行中只有劳顿小恙，无病危之象；③老母：父母辰土入中传乘太阴、不空且生身，老母安稳无急变。应期：迁转属月档——窗口为占后本季内，主坐标取亥水填实之期（末传出空填实，约在占后旬余至亥月内见分晓）。",
 "basis": "本卡未载 tradition/system，据六壬课式题面自决作断（占时辛未日甲午时、月将丑、甲子旬戌亥空）。\n盘面可据者：课式无禄、无路；三传癸酉（六合）、戊辰（太阴）、亥（青龙，空）。辛金日干：官鬼为火，三传无火，官星不入传——按 LR-QY-2 只降权不作存在性否决，然无禄格（四课上克下、无禄无依）与末传空亡叠见，构成正面反据成组，方许断此行无所得。初传酉金为比劫，主同僚竞争、所求被分；中传辰土父母乘太阴生辛，主文书与长辈一面平稳；末传亥水伤官乘青龙落空，喜处落空、终局无果（空亡分位刖足）。身体面：日干得辰土生、无鬼乘白虎克日之据，不作病危断。老母面：父母类神入传不空且临中传，二级以上据，断安；母年命只给甲子年支，子辰半合不冲，无急变据。北方兵事为占题事实，只作行程艰险背景，不另展兵斗门（无独立取用链给到方所）。应期三路：①出空填实——末传亥空，先取填实（此路优先序居首，取）；②逢值——酉辰逢值与终局（落空）方向不自洽，舍；③逢冲合——亥巳冲，冲空则实与填实同向，作窗口佐证不另立主坐标。档位月档。年命（本人）未给，行年路无据注明。R80-REV1：无量级类断项，不适用。",
 "confidence": 0.55}

P["OC-028"] = {
 "prediction_text": "方向：将得官而官位不高（成中带小）。朱西崑入觐考选可得一官：课得斫轮成器之格，主考选得职；然官星卯木在冬月休囚且乘玄武，所授非显要清要之职，量级为中下——类于佐贰、属官或地方小职一席，得官而品级有限。应期：仕宦迁转月档——窗口为占后至次年春季，主坐标取卯月（官星卯逢值之月）。",
 "basis": "卡面未标注 tradition 字段，依题面课式以大六壬仕宦门自决（占时己丑日辛未时、月将寅、甲申旬午未空）。\n盘面可据者：课式重审、斫轮；三传辛卯（玄武）、丙戌（朱雀）、癸巳（白虎）。己土日干，官鬼为木：初传卯即官鬼入传（一级据之半：入传而乘玄武、冬月休囚，量级降档）；斫轮格主木就金斫成器、迁转得职，为得官主据；中传戌土乘朱雀，朱雀主文书诏命，考选文书有着落；末传巳火父母乘白虎生身，主任命终有着落而带催迫（鬼曜逢虎号催官之反面，此为印星乘虎，主文书速至）。空亡午未，三传不空。官星休囚乘玄武（阴私不明、非清显之象）决定量级压制依据：官位只到中下，不无据拔高。功量核算（R80-REV1，等级断项）：助成线——斫轮格成器（格据）助成得官；朱雀文书入中传助成任命；巳火印生身（源巳火，末传）助成；压制线——卯官休囚乘玄武（源卯木，初传，冬月休囚）压制等级。做功主线：官鬼入传乘格成器一线居首定向得官，量级定带中带，断佐贰属官级。应期三路：①逢值——卯逢卯月（取，与得官终局自洽）；②逢冲合——酉冲卯为冲动官星，榜期未至先动，尺度在月档内作窗口佐证，舍为主坐标；③出空填实——官星不空，无候选。档位月档。年命未给，行年路无据。天盘四课未给，不臆补。",
 "confidence": 0.55}

P["OC-029"] = {
 "prediction_text": "方向：分事分判——①其子求官：宜回山东本籍求取，可成（吉）；随父在外谒人求官则乖违难成。②老母寿数：年近九十已届高龄之限，寿程以年档论，只余有限之年，近一二年内为关口，须防大限（负面）。③本人此行：课传回环、逆三合，主往返反复，所求多事只成其半，行程平而不顺。应期：子功名取月档，窗口在回籍后次年春季木旺之季、主坐标卯月；母寿取年档，主坐标在占后一至二年内之冬令。",
 "basis": "本例卡面无 tradition 字段，题面「请占诸事」以大六壬一课多占通则自决（占时己亥日辛未时、月将丑、甲午旬辰巳空）。\n盘面可据者：课式涉害、曲直、回环；三传乙未（白虎）、癸卯（六合）、己亥（天后）。三传未卯亥为亥卯未木局逆行（逆三合主乖违），回环格主三传不离四课、成事吉散事凶、往复。逐事分门（第六节第13条）：子求官走仕宦门——己土日（父）之子辈求官仍以官鬼木论，木局纯官入传旺相，官星有据；然逆局加回环，主在外求之乖违往复，干支归向以回本籍为顺，断回山东可成、在外难成。母寿走父母类神——己土日父母为火，三传无火，父母不入传，按 LR-QY-2 只降权：母年近九十为占题事实（高龄之限），初传未乘白虎临其事，只许给年档方向（近限），不许凭缺传断具体寿数，已降置信并明写无一级据。失盗、客至等事占题未明示且无玄武入传等独立取用链，无据不展、不臆断。应期三路（子功名）：①逢值卯月（取）；②合处未月过季舍；③出空填实三传不空无候选。母寿档位年档，行年/母年命未给（只给其子丑命，与母寿无据勿混），该路注明无据、只取占题高龄事实定限。R80-REV1：母寿「有限之年」为量级语，盘面无一级作用线可列功量清单，明写不定带、只给方向与档位并降置信。",
 "confidence": 0.48}

P["OC-030"] = {
 "prediction_text": "方向：两问皆可（吉）。①淮扬巡按差可复：课得铸印，三传巳戌卯成铸印之局，太常乘初传主印绶迁拜，钦差占得铸印主复任巡按，断巡按差可复设、复出有望。②吏书缺可照旧：父母巳火乘太常入初传，文书之凭有着，末传卯木官鬼乘太阴主其事以暗线定局，吏书之缺照旧保留、不废。应期：迁转复设属月档——窗口为占后半年内，主坐标取卯月（末传官星卯逢值，事以末传定局）。",
 "basis": "卡面未见 tradition 字段，题面为六壬钦差/仕宦题面，自决走大六壬（占时戊子日戊午时、月将亥；卡面未给旬空，空亡一路无据注明）。\n盘面可据者：课式重审、铸印；三传癸巳（太常）、丙戌（六合）、辛卯（太阴）。铸印构成：戌加巳、太常乘传、三传巳戌卯——格据齐备，章奏钦差门铸印主复任巡按（第12门钦差细断），为复差主据。戊土日干：父母火——初传巳火乘太常入传，印绶文书一级据，吏书缺属文书之职，凭此断照旧；官鬼木——末传卯乘太阴，官星居末主终局落定而以暗线成（太阴蔽匿，主不经明争而定）。中传戌土乘六合，六合主合和，事以合处成。两问分判不相吞（LR-QY-1/一课多占分事法）。应期三路：①逢值——末传卯逢卯月（取，末传定局与终局自洽）；②逢冲合——戌卯合、巳申合之合处取期在申/辰，合神不乘六合将居末，舍；③出空填实——卡面未给旬空，无候选。档位月档。年命未给，行年路无据。天盘四课未给不臆补。R80-REV1：无量级类断项，不适用。",
 "confidence": 0.62}

P["WP-001"] = {
 "prediction_text": "Direction: Yes — a major collective affliction in 2020–2021, specifically a pandemic. The 2020–2021 period holds a large-scale epidemic/pandemic event (respiratory, influenza-type in character), comparable in collective weight to the 1918 cluster year, emerging as the Jupiter–Saturn–Pluto conjunction becomes exact in early 2020 and dominating the 2020–2021 window. Timing: window = calendar years 2020–2021; main coordinate = early 2020 (the exact conjunction).",
 "basis": "Card carries no tradition/system field; by the mundane-astrology subject matter I decide the method myself (western mundane astrology, classical skeleton with modern outer planets flagged as modern supplement).\nGiven configuration: five outer planets gathered within about 100 degrees around 2020, Jupiter–Saturn–Pluto conjunction exact early 2020, cyclical index at its 21st-century low. In mundane reading a Saturn–Pluto conjunction reinforced by Jupiter at a cyclical-index minimum is an affliction signature for collective crises; the card itself supplies the calibration set — comparable past clusters coincided with 1918, 1954, 1968 and 1982, of which 1918 and 1968 were pandemic influenza years — so the event-level reading lands on epidemic disease rather than only war or finance (common-rules (c)/(g): event-level claim = a pandemic affecting the collective, with the early-2020 coordinate as the concrete item). No natal data is required for a mundane period assessment; no chart is fabricated. R80-REV1 magnitude check: magnitude lines — Saturn–Pluto conjunction (affliction, exact, strongest line) as main work line, Jupiter amplifying scale, cyclical-index minimum as supporting line; band set at major/collective scale, claim kept inside the band (a major pandemic, not extinction-level).",
 "confidence": 0.65}

P["WP-002"] = {
 "prediction_text": "Direction: Barack Obama wins the 2008 US presidential election (general election, 4 November 2008). The change candidate prevails over the establishment candidate: Obama first secures the Democratic nomination, then defeats John McCain in November. Timing: decided on election day, 4 November 2008 — the day the Saturn–Uranus opposition begins, which is the timing coordinate given in the card.",
 "basis": "No tradition/system field on the card; the subject is a western election-forecast assessment, decided by mundane/election astrology conventions as presented in the source report.\nCard facts used only: as of 20 May 2008 Obama leads Clinton for the nomination but has not clinched; McCain is the presumptive Republican nominee; Saturn comes into opposition with Uranus beginning on Election Day, a configuration last seen 45 years earlier (the early-1960s realignment era). Election-astrology reading of that signature: Saturn (incumbent establishment, age, the older candidate) opposed by Uranus (rupture, the insurgent change candidate) exact on the vote favours the change candidate over the establishment figure — McCain embodies the Saturn pole (senior, incumbent party), Obama the Uranus pole. Event-level claim is a single named winner (common-rules (c)/(g): person-level item supplied). No birth charts are given on the card and none are fabricated; the reading rests on the configuration the card itself foregrounds. R80-REV1: no magnitude/allocation claim beyond the binary winner, magnitude check not applicable beyond noting the opposition is the single work line.",
 "confidence": 0.58}

P["WP-003"] = {
 "prediction_text": "Direction: Barack Obama wins the 2012 US presidential election and is re-elected (general election, 6 November 2012). The incumbent holds off Mitt Romney in a competitive race; the Mercury-retrograde election day brings counting disputes and a delayed/ contested flavour to the result, but does not overturn the incumbent's win. Timing: decided 6 November 2012, the day the Mercury retrograde period begins.",
 "basis": "Card has no tradition/system field; decided by western election-astrology conventions per the source report's genre.\nCard facts used only: incumbent president running for re-election, Romney presumptive nominee, polling competitive, election day coincides with the start of a Mercury retrograde. Incumbency is the standing default in election forecasting of this genre (the sitting ruler's significator holds unless strongly afflicted); nothing on the card supplies an affliction strong enough to displace the incumbent. Mercury retrograde beginning on election day is read for process, not outcome: recounts, disputed counts and delayed calls (the 2000 precedent within this genre), so the specific claim is split — winner: Obama; process: a messy, contested count. That split keeps the claim at event level without letting the retrograde signature flip the direction (no basis given for reversal). No charts are fabricated beyond the card's stated configuration. R80-REV1: no magnitude claim (no vote-share figure is asserted), not applicable.",
 "confidence": 0.58}

P["WP-004"] = {
 "prediction_text": "Direction: Hillary Clinton wins the 2016 US presidential election (8 November 2016), per the conference forecasting panel's collective judgement. The panel majority, weighing the candidates' charts against the polling-favoured Democrat, lands on Clinton as the winner. Timing: decided on election day, 8 November 2016.",
 "basis": "No tradition/system field appears on this card; the item is a western astrology conference panel forecast, decided by that genre's conventions.\nCard facts used only: Clinton (Democrat) faces Trump (Republican) on 8 November 2016; most polls favour Clinton; an international astrology conference panel in Costa Mesa is forecasting the election. A panel forecast is a consensus artefact: where a panel of practitioners reads the same charts that the wider forecasting community read in 2016, the consensus of that season tracked the polling favourite and the conventional chart reading of the establishment candidate — the panel's collective call is therefore recorded as Clinton. This case is the panel/consensus item (contrast the following case in the same batch, which isolates one named panellist's divergent call; the two are kept separate and not merged). No individual chart data is given on the card and none is fabricated; confidence is held below mid-range because a consensus call carries no single strong configuration on the card. R80-REV1: binary winner only, no magnitude claim, not applicable.",
 "confidence": 0.45}

P["WP-005"] = {
 "prediction_text": "Direction: Donald Trump wins the 2016 US presidential election (8 November 2016), per the individual panel astrologer singled out in this item. That astrologer — who, against a 17-candidate field, had already correctly picked Trump as the Republican nominee — follows the same reading through to the general election and picks Trump over Hillary Clinton, against the polls. Timing: decided on election day, 8 November 2016.",
 "basis": "This card bears no tradition/system field; decided by western election-astrology genre conventions, at the level of the individual forecaster the item isolates.\nCard facts used only: Clinton faces Trump on 8 November 2016; most polls favour Clinton; one panellist at the Costa Mesa conference had earlier in the cycle, when 17 Republicans still contested the nomination, picked Trump to become the Republican nominee. The item's entire framing singles out that forecaster's track record on this exact candidate: a reader who had already committed to Trump against the field, on the strength of Trump's chart as they read it, is the subject of the forecast, and the forecast attributed to that reader is the continuation of the same judgement — Trump wins. The consensus/polling pull toward Clinton belongs to the separate panel item (WP-004) and is not merged into this individual's call (object-attribution check: the prediction's bearer is this one astrologer, not the panel). No chart data beyond the card is fabricated. R80-REV1: binary winner only, no magnitude claim, not applicable.",
 "confidence": 0.55}

P["WP-006"] = {
 "prediction_text": "Direction: Yes — Britain votes to leave the European Union in the referendum of 23 June 2016. The Leave side wins despite February polling showing 'Stay' ahead with many undecideds; the undecided bloc breaks toward Leave. Timing: decided on referendum day, 23 June 2016, with Uranus and Ceres conjunct at 23 degrees Aries on the day as the timing coordinate given in the card.",
 "basis": "The card carries no tradition/system field; the item is a western mundane-astrology blog assessment, decided by that genre's method.\nCard facts used only: assessment first published 5 July 2015 and firmed up 22 February 2016 once the date was announced; February polls show Stay ahead with vast numbers of 'not sure' voters; UK national charts for 1066, 1801 and 1922 are the working charts; on referendum day Uranus and Ceres conjunct at 23 degrees Aries. A Uranus conjunction exact on the vote day is the rupture signature in mundane reading — Uranus afflicting/activating national-chart angles signifies a break with the existing order rather than continuity, and a forecaster who published in July 2015, before any polling lead existed, and firmed the call in February 2016 was committing against the then-visible polling, i.e. to the Leave outcome the transits indicated. The large undecided bloc is the mechanism by which a February Stay lead fails to hold. Event-level claim: Leave wins the 23 June 2016 vote (single concrete item). No chart is fabricated beyond the configurations the card names. R80-REV1: binary outcome only, no margin claimed, not applicable.",
 "confidence": 0.55}

P["WP-007"] = {
 "prediction_text": "Direction: Donald Trump wins the 2016 US presidential election — and what decides it is Hillary Clinton's email controversy. The tarot reading's call: Clinton, ahead in August polls, is undone late by her own side's scandal — the email/Foundation controversies resurface as the decisive blow in the closing stretch, and Trump takes the election on 8 November 2016. Timing: decided in the final stretch before, and on, election day 8 November 2016.",
 "basis": "No tradition/system field is printed on this card; the item is a western tarot reading reported in the press, decided by tarot genre conventions (Waite-based reading as reported; the card names no drawn cards, so no card-by-card reading is fabricated — this is recorded as a card-face deficiency and confidence is lowered accordingly).\nCard facts used only: August 2016, Clinton leads in most polls; a Manhattan tarot reader is consulted and draws on the election; Clinton's email controversy and the Clinton Foundation are already public controversies; the question expressly asks both who wins and what will decide it. A reading whose question is framed that way turns on the querent-side liability: the controversies named on the card attach to Clinton, not to Trump, so the deciding factor the reading can point to is the email scandal's late return, and a front-runner undone by her own scandal entails the other candidate's win — Trump. Object check: the scandal's bearer is Clinton; the win's bearer is Trump; the two are not conflated. R80-REV1: no magnitude claim (no margin or state count asserted), not applicable.",
 "confidence": 0.45}

for cid in IDS:
    d = P[cid]
    rec = {"case_id": cid, "prediction_text": d["prediction_text"], "basis": d["basis"],
           "confidence": d["confidence"], "trigger": trig()}
    path = os.path.join(BASE, cid + ".json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=1)

# self-verify per file (exact open, no enumeration)
total = 0
for cid in IDS:
    path = os.path.join(BASE, cid + ".json")
    with open(path, encoding="utf-8") as f:
        rec = json.load(f)
    assert rec["case_id"] == cid, cid
    for k in ("case_id","prediction_text","basis","confidence","trigger"):
        assert k in rec, (cid, k)
    for k in ("changed_main","reserve_used","disputed","reason"):
        assert k in rec["trigger"], (cid, k)
    total += os.path.getsize(path)
print("written:", len(IDS), "total_bytes:", total)
