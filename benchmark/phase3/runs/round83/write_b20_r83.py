#!/usr/bin/env python3
"""R83 B20 prediction writer. Only writes this batch's prediction files."""
import json
import pathlib

OUT = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round83/predictions")
OUT.mkdir(parents=True, exist_ok=True)

TRIG_OFF = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}

P = {}

P["OC-018"] = {
    "case_id": "OC-018",
    "prediction_text": "方向：贵显至全国级报业领袖而晚运陡转危殆。庚金生子月，伤官当令，丙火七杀透干、己土印绶透干，杀印与伤官并见：以文章名世、执掌大报、声望与权位居报界之首，地位足级（全国性人物，非一省一报之限）。行运前段金水木地尚可扶身任杀，中晚年转入火旺杀强之运，身弱难任七杀，晚年有兵刃横祸、暴亡之险，不得以高寿善终收局——晚段翻凶的触发为运入南方火地、杀旺攻身而印星受困。应期以运档为单位：危厄集中在五十岁后入火杀运之段内，尤防杀旺流年（丙丁巳午年）。置信：中高。",
    "basis": "卡面未标注 tradition 字段；卡面载四柱「己卯 丙子 庚寅 辛巳」、男命、问一生地位与晚年行运，按子平法自决。systems_used=[八字]。格局：子月伤官，丙杀己印并透，庚坐寅绝、时逢辛巳，赖己印辛劫扶身，定为伤官佩印兼杀印相生之贵局，主线为印化杀生身（第八节功量清单：助成线＝己印化丙杀、辛劫帮身、寅巳藏丙戊余气；压制线＝子水伤官泄气、庚坐绝地；主线取印化杀，等级带定全国级，与卡面「报业巨头」事实同级，不降格）。第十节反向限定扫查：断项「晚年横祸」→限定信号＝火杀运段方成立（阶段界），已按界改写为五十岁后火运段内，不表述为全程皆凶；断项「报界之首」→无限定信号，未动作。应期合通则(k)年/运档：先定运段再指年类，不落具体日。",
    "confidence": 0.62,
    "trigger": dict(TRIG_OFF),
}

P["OC-019"] = {
    "case_id": "OC-019",
    "prediction_text": "方向：中年前程亨通至学术机构总干事级，然四十岁前后有一大险关，防横祸暴亡。壬水生辰月，坐申长生，癸劫帮身，丙火偏财透干，卯木伤官泄秀生财：财旺身强能任，主以才学干才显达、位至研究院总干事一类清贵实职。行运木火之乡（甲寅等运）食伤生财最顺；转入水旺比劫之运则劫财夺财、财星受损，且申辰拱水助劫，险年在四十岁上下逢水旺火衰之年（癸壬亥子年、或酉申金水流年冲克财星之时），有遭害、暴卒之虞，寿数难逾四十余。置信：中。",
    "basis": "卡面未标注 tradition 字段；卡面载四柱「癸巳 丙辰 壬申 癸卯」并自注另书所载全异、本例以徐乐吾书为准，照卡面四柱作断，此为输入版本限定、非残损。systems_used=[八字]。格局：壬坐申长生、辰为水库、癸透帮身，身强；丙财透、卯伤官生财，财格带伤官泄秀。第八节功量清单：助成线＝申长生根、癸劫帮身、卯木泄秀生丙财；压制线＝辰土七杀藏而不透、巳火财根受申合绊；主线取伤官生财，等级带定清贵显达（总干事级），与卡面设定同级。第十节反向限定扫查：断项「横祸」→限定信号＝水旺劫财运年方成立（阶段界＋条件界），已收束为四十岁前后水旺之年，不作全程凶断；「显达」一项无限定信号。应期以年档表达，先定运段（水运）再指年类。",
    "confidence": 0.55,
    "trigger": dict(TRIG_OFF),
}

P["OC-020"] = {
    "case_id": "OC-020",
    "prediction_text": "方向：贵至极品（政府主席级），为本批贵显之最；然五十岁前后有寿关。癸水生丑月，两丑夹身，己土七杀当令而重，丁火财星透干，乙木食神透于时干制杀：食神制杀格成，杀重得制反主大贵，位极人臣。行运早年水木之地助食制杀最利，位望隆盛；行至戌运，戌冲两丑、杀库与印库齐动，食神根气受摇，且丑戌刑并起，五十岁前后（戌运内、尤逢戌年辰戌丑未刑冲齐集之年）有病亡之险，寿约止于五十一二。置信：中高。",
    "basis": "卡面未标注 tradition 字段；卡面载四柱「己卯 丁丑 癸丑 乙卯」、男命、问贵显程度与行运险年，按子平法自决。systems_used=[八字]。格局：丑月七杀两见，乙食透时制杀，丁财透，食神制杀格。第八节功量清单：助成线＝乙卯食神两根制丑中己杀、卯木食禄成势；压制线＝两丑杀重、癸坐丑无强根、丁财生杀；主线取食神制杀，制杀得力故等级带定极品（主席级），与卡面「主席级政要」同级，不因杀重降格——降格依据不足。第十节反向限定扫查：断项「寿关」→限定信号＝戌运冲丑库方触发（阶段界），已按界收束于戌运及戌年；「贵至极品」无限定信号。应期运档/年档，先运后年。",
    "confidence": 0.63,
    "trigger": dict(TRIG_OFF),
}

P["OC-021"] = {
    "case_id": "OC-021",
    "prediction_text": "方向：武贵显达至督军、巡阅使级封疆，然根基带冲，晚景失势退隐。乙木生酉月，辛金七杀透干当令，乙坐卯禄自强，丙火伤官透时制杀，戊土偏财透年：杀旺有制、刃禄帮身，主以武功起家、统兵一方，贵显足级至封疆大吏。惟日支卯与月令酉冲，禄刃逢冲，根基不静：一生权位起落大，中晚年运转金水则杀无制、刃被冲，权柄易失，最终以退隐收场，不得在位善终全盛而退。应期以运档计：得意在木火运（伤官制杀得力之段），失意在金水运段。置信：中高。",
    "basis": "卡面未标注 tradition 字段；卡面载四柱「戊午 辛酉 乙卯 丙戌」、男命、问格局高低与一生贵显，按子平法自决。systems_used=[八字]。格局：酉月七杀，丙伤官制杀，乙坐卯禄，卯酉冲。第八节功量清单：助成线＝丙火伤官制辛杀、卯禄为根、午戌藏火土续制生财；压制线＝卯酉冲动禄根、辛杀当令旺强；主线取伤官制杀，等级带定封疆级武贵，与卡面「军阀首领」同级。第十节反向限定扫查：断项「晚年失势」→限定信号＝金水运段杀无制时方成立（阶段界），已按界改写；断项「武贵」→卯酉冲只限定其根基稳定性（条件界：权位带起落），核心落点不变。应期以运档表达，不落日月。",
    "confidence": 0.6,
    "trigger": dict(TRIG_OFF),
}

P["OC-022"] = {
    "case_id": "OC-022",
    "prediction_text": "方向：科第无缘、功名不第，一生转以学问技艺（命理医卜之术）立身成名。乙木生酉月，丁火食神透干制辛杀，戊土正财透时，乙坐巳、时逢寅：食神制杀本可主贵，奈何乙木无卯禄强根，巳酉半合金局助杀，食神制杀力薄而杀势成党，功名之路屡试屡蹉。所喜丁食泄秀、寅巳藏印藏食，文章技艺之才真切：不第之后以术数著述立业，反成一代名家，衣食丰足、名重士林——即「舍官就食」之局。行运木火之段（乙未、甲午运）才名最盛，立身之路在中年后定型。置信：中高。",
    "basis": "卡面未标注 tradition 字段；卡面载四柱「辛巳 丁酉 乙巳 戊寅」并注安命甲午、大运丙申起，卡面设定「屡试功名不第」，按子平法自决。systems_used=[八字]。格局：酉月七杀，丁食制杀，然巳酉半合助杀、乙无禄根，制杀不足，格成而科名之用受压。第八节功量清单：助成（技艺线）＝丁食泄秀透干、寅藏丙食甲劫、巳藏戊丙；压制（功名线）＝辛杀当令、巳酉半合金局、乙坐巳无根；主线分两面核：功名断项主线为杀党压制，等级带定「不第」；立身断项主线为食神泄秀，等级带定「以术成名、衣食丰足」，两带各按其清单取值，不互相挪用。第十节反向限定扫查：断项「以命理立身」→卡面仅言命学世家出身，断项对象界收束为「学问技艺之业」并以命理为首指，不扩及其他行业细节。应期以运档表达：中年木火运定型。",
    "confidence": 0.6,
    "trigger": dict(TRIG_OFF),
}

P["OC-023"] = {
    "case_id": "OC-023",
    "prediction_text": "方向：钟下所覆为一件经火烹煮、可食之物（熟食之属），物形完整、未破损。火风鼎变雷风恒：鼎者烹饪之器，中虚而有物在焉；上离为火、为熟，下巽为木、为蔬果鸡禽之类，互见乾兑金石之象收束于外——所覆非生冷金玉，乃鼎中烹熟之食类，色带黄赤、味香而熟。变恒主其物久置不变、完好如故，无残缺破碎。置信：低（射覆凭象，动爻未载于卡面，体用分判只能就上下卦变通取之）。",
    "basis": "卡面未标注 tradition 字段；卡面载卦象「火风鼎 变 雷风恒」，问钟下所覆何物、完好与否，按梅花取象自决。systems_used=[梅花易数]。残损注明：卡面未载动爻与起卦法，体用只能据上卦离变震（动在上卦）取用在上、体在下巽一途分判，置信因此下调，不臆补动爻。取象：鼎为烹器、中虚容物，离火主熟、巽木主蔬果禽类，合断为烹熟食类；变恒主完好久置。第十节反向限定扫查：断项「熟食之属」→限定信号＝离火与鼎象只支持「经火处理之食类」这一类别界，不支持指认具体某一种食物，已按界收束至类别层级，不虚指单品；「完好」一项据变恒无限定信号。第八节：本例无量级类断项，R80-REV1 不适用（射覆类别断非等级/数量/分配）。",
    "confidence": 0.35,
    "trigger": dict(TRIG_OFF),
}

P["OC-024"] = {
    "case_id": "OC-024",
    "prediction_text": "方向：葬事有着落——资财不出自借贷变产，而出自易者宅中先人窖藏之金。遗书预言可托之人届时果至，其家无资之困将因一桩意外小事解开：宅中鼠患扰动、击鼠而破枕（器物），窖藏之金由此显露，得金之数足敷营葬有余，葬事遂可体面办成。应期以日档计：即来访后数日内、因击鼠破物而见金，不拖过葬期。置信：中。",
    "basis": "卡面未标注 tradition 字段；题面为易者遗书预言与身后葬资之问，卡面出处自题「击鼠枕窖金」，按梅花外应与情理（通则(e)事实优先：先人窖藏为本题给定的解困路径）自决。systems_used=[梅花易数（外应取象）]。残损注明：卡面未载卦象与起卦记录，本例只能据题面外应（鼠、枕、窖）与序文体裁作断，无卦可复核，置信下调。第十节反向限定扫查：断项「得金足敷营葬」→限定信号＝金出窖藏这一来源界，已收束为「宅中先人窖藏」，不表述为外来横财或他人资助；断项「击鼠破枕见金」→出处题名与外应物象互指，无反向限定，未动作。第八节数量断项「足敷营葬有余」功量核：做功线仅窖金一条（来源单一、量以葬费为度），等级带定「足用有余」，不拔高为巨富。",
    "confidence": 0.5,
    "trigger": dict(TRIG_OFF),
}

P["OC-025"] = {
    "case_id": "OC-025",
    "prediction_text": "方向：应验。椅底预书所记年月日届期之时，果有来客（或家人）坐于此椅、椅被坐破，预言如字应验，分毫不爽。应期即预书所定的那个年月日当日（以日为单位，预书自带坐标，非另推）。置信：中高——此类自设期约的预书，验与不验只在届期一事，象与事直指一物一椅，无旁出对象。",
    "basis": "卡面未标注 tradition 字段；题面为预书届期验否之问，卡面出处自题「置椅坐破」，按梅花预言应验体裁自决。systems_used=[梅花易数]。残损注明：卡面未载预书原文年月日与所坐之人姓名，本例只断「届期椅破、预言应验」之终局，不臆补具体日期与坐破者身份，置信因此不至高位。应验对象复核（通则(f)）：承受对象为邵雍自家之椅，应验对象同为此椅，同一性成立；断语不回收到坐者人身吉凶。第十节反向限定扫查：断项「椅被坐破」→对象界限定于此一椅、阶段界限定于预书届期当日，已在原文按界表述；无其他非量级断项。第八节：无量级类断项，不适用。",
    "confidence": 0.6,
    "trigger": dict(TRIG_OFF),
}

P["OC-026"] = {
    "case_id": "OC-026",
    "prediction_text": "方向：今年功名有成——昆弟之中至少一人登第，喜信在今年春夏之交见分晓。己亥日占，涉害、曲直为课，三传乙未（青龙）、己亥（螣蛇）、癸卯（玄武）恰成亥卯未三合木局；己土以木为官，官星成局而旺，初传未土乘青龙主文书喜庆临门，功名之象成。惟中传亥水乘螣蛇，主榜前榜后有一番虚惊疑虑、消息反复；末传卯木乘玄武，名次或不居前列、防同名冒籍之扰。应期以月档计：主坐标取卯月至未月之间（木局逢值逢合之月），喜信最迟不逾未月。置信：中。",
    "basis": "卡面未标注 tradition 字段；卡面载课式「涉害、曲直」、三传「乙未（青龙）、己亥（螣蛇）、癸卯（玄武）」、月将丑将、甲午旬辰巳空，问今年功名，按大六壬自决。systems_used=[大六壬]。盘面不全（无天盘全图、四课全列、年命），守快照六壬篇第八节：只据干支、三传链、天将乘传、课格、空亡作断，不臆补四课细节。断据：三传亥卯未三合木局即曲直格，木为己土之官鬼类神，官局成而初传乘青龙，主功名喜信；螣蛇中传只调量级为「过程有虚惊」，玄武末传主名次不居前。应期三路：逢值（卯未月）取之；逢冲（酉月冲卯）与终局方向不合舍之；出空填实（辰巳空与三传无涉）无候选。第十节扫查：断项「一人登第」→三传只见官局一线，对象界收束为「昆弟中至少一人」，不虚指必为兄或弟；「名次不前」无限定信号。",
    "confidence": 0.55,
    "trigger": dict(TRIG_OFF),
}

P["OC-027"] = {
    "case_id": "OC-027",
    "prediction_text": "方向：此行不得意——北上难邀实惠，多半无功而返或中途滞留；本人身体有疾厄之忧，老母在家则惊多于险、大体无恙。辛未日甲午时占，课式无禄、无路，禄路皆无，主奉诏而行却无禄可就、无路可通；三传癸酉（六合）、戊辰（太阴）、亥（青龙）而亥落甲子旬空，末传空亡，终局落空：行至终点无着落。辰土中传乘太阴，本人防暗疾缠绵、行途水土不服之病；北方兵事方紧（题面事实），行程更主迟滞。老母安否：传中不见年命受克之凶象直指母身，断为在家有惊忧牵挂、无大厄。应期以月档计：滞留在行后一二月内见定局（辰月前后事明）。置信：中。",
    "basis": "卡面未标注 tradition 字段；卡面载课式「无禄、无路」、三传「癸酉（合）、戊辰（阴）、亥（青，空）」、月将丑将、甲子旬戌亥空，问北行得意否与母安否，按大六壬自决。systems_used=[大六壬]。盘面不全，守六壬篇第八节，只据所给课式、三传、天将、空亡作断。断据：无禄无路为凶格主向（仕宦/出行门皆忌），末传亥空乘青龙，喜而落空，主终局无成；太阴乘辰主暗疾。应验对象复核：本人断语对回日干辛（行人本人），母之断语只就「传中无直克母象」作有限判断，不把本人疾厄回收到母身。第十节扫查：断项「老母无大厄」→限定信号＝盘面未给母年命（甲子年仅注于卡面），对象界收束为「就所见传课无凶直指」，已按界表述并降置信；断项「无功而返」→无禄无路与末空双指，无反向限定。第八节：等级断项「难邀实惠」功量核——做功线：无禄无路课格（压制）、末传空（压制）、六合初传（微助成，仅主行程有人接应），主线为压制，等级带定「不得意」低位，与断语同向。",
    "confidence": 0.5,
    "trigger": dict(TRIG_OFF),
}

P["OC-028"] = {
    "case_id": "OC-028",
    "prediction_text": "方向：考选可成，将得实官——得一中等品级的外任实缺（州县正印或同级之职），非虚衔候补。己丑日辛未时占，重审、斫轮为课，三传辛卯（玄武）、丙戌（朱雀）、癸巳（白虎）：卯木为己土之官，官星居初传主事之开端，虽乘玄武主先有暗中阻滞、打点耗费；中传戌土乘朱雀，文书、考选文字见长，考选以文取胜；末传巳火为印绶乘白虎，印绶归身主实授落地，白虎主其职带刑名钱谷之任、到任有威。应期以月档计：主坐标取巳月（印绶逢值、实授见信），戌月为次候（文书定期）已舍（尺度同级而巳更切印星逢值）。置信：中。",
    "basis": "卡面未标注 tradition 字段；卡面载课式「重审、斫轮」、三传「辛卯（玄武）、丙戌（朱雀）、癸巳（白虎）」、月将寅将、甲申旬午未空，问入觐考选得何官，按大六壬自决。systems_used=[大六壬]。盘面不全，守六壬篇第八节只据所给作断，不臆补四课与年命。断据：仕宦门类神取官鬼，卯官居初传、巳印居末传乘白虎主实授，官印链完整；朱雀中传主考选文书得意。第八节功量清单：助成线＝卯官入传、巳印末传归身、朱雀利考选；压制线＝玄武乘官（暗阻耗费）、官星只一位不旺；主线取官印相生，等级带定「中等实缺」，不拔高至方面大员、不降为虚衔。第十节扫查：断项「外任实缺」→限定信号＝末传白虎主刑名钱谷之任，处所界只收到「实缺」层级，未给地名，不虚指具体州县；「考选以文取胜」无限定信号。应期三路：逢值（巳月）取之，逢合（戌与卯合，故戌月为文书候选）次而舍，冲空（午未空与传无涉）无候选。",
    "confidence": 0.55,
    "trigger": dict(TRIG_OFF),
}

P["OC-029"] = {
    "case_id": "OC-029",
    "prediction_text": "方向：分项断——（一）携子求官：子事可成而迟，往返周折后得之；（二）本人此行：劳碌奔波、所访之人可托，事有转圜；（三）老母：年近九十、白虎乘初传未土临传，寿事须防，主一二年内有重病之厄，寿终之期不远，宜早备后事之心。己亥日辛未时占，涉害、曲直、回环为课，三传乙未（白虎）、癸卯（六合）、己亥（天后）：亥卯未三合木局，官星成局，六合居中传主和合可托，故求官终成；回环课主来回反复，故成而迟。末传亥为日支自临乘天后，事终归家门。应期：求官以月档计，主坐标未月（官局逢值）；母事以年档计，防未年、戌年。置信：中。",
    "basis": "卡面未标注 tradition 字段；卡面载课式「涉害、曲直、回环」、三传「乙未（白虎）、癸卯（合）、己亥（天后）」、月将丑将、甲午旬辰巳空，并注其子丑命、母年近九十，按大六壬自决。systems_used=[大六壬]。盘面不全，守六壬篇第八节只据所给作断。断据：三合木局官星成局＋六合中传，求官主成；回环课定其迟与反复；初传未乘白虎，未为木库、亦为年命外长辈之位，白虎主丧病，故母事另断有厄。应验对象复核：求官断语对回其子（丑命，子为求官主体，卡面明载携子求官），母事断语对回其母，二者不相回收。第十节扫查：断项「母有重病之厄」→阶段界限定于一二年内（未戌年），不表述为即时；断项「子事可成」→回环课限定其过程界为「周折后得」，已按界改写。第八节：无明确量级断项（迟速为过程断），功量核仅登记求官助成线（官局、六合）多于压制线（回环反复），成事等级带定「可成而费力」。",
    "confidence": 0.5,
    "trigger": dict(TRIG_OFF),
}

P["OC-030"] = {
    "case_id": "OC-030",
    "prediction_text": "方向：两问皆可——淮扬巡按差可复设，吏书缺亦可照旧存留。戊子日戊午时占，重审、铸印为课：铸印格主印信官职重新铸成、废而复置，正应「差可复否」之问；三传癸巳（太常）、丙戌（六合）、辛卯（太阴）：六合居中传主和合复旧，巳火为戊土之印居初传乘太常（主朝廷旧典常制），印与合双见，复设与照旧皆有着落。惟末传卯木为官星乘太阴，复设之后人事安排带暗中更易——差可复而未必尽如原议之人选。应期以月档计：主坐标取巳月（印星逢值、铸印成形），戌月（六合定期）为次候已舍。置信：中。",
    "basis": "卡面未标注 tradition 字段；卡面载课式「重审、铸印」、三传「癸巳（太常）、丙戌（六合）、辛卯（太阴）」、月将亥将，代占官缺存废两问，按大六壬自决。systems_used=[大六壬]。盘面不全（未注旬空），守六壬篇第八节只据所给课式、三传、天将作断，空亡一路无据不推。断据：章奏/仕宦门取印绶与官星：铸印格＋巳印初传＋六合中传，三线同向主复置与照旧。第十节扫查：断项「差可复」→限定信号＝末传太阴乘官，条件界收束为「差额可复、人选带暗变」，已按界改写，不表述为全如原议；断项「吏书缺照旧」→六合主合旧，无反向限定，未动作。应期三路：逢值（巳月）取之；逢合（戌月卯戌合）次候舍之，理由为印星逢值更切铸印成形；出空填实一路因卡面未载旬空，明写无候选。",
    "confidence": 0.55,
    "trigger": dict(TRIG_OFF),
}

P["WP-001"] = {
    "case_id": "WP-001",
    "prediction_text": "Direction: Yes — the 2020–2021 window holds a major collective affliction of epidemic kind: a fast-spreading pestilential disease (respiratory/fever class) sweeping many countries, with heavy mortality and social disruption, cresting in 2020 as the Jupiter–Saturn–Pluto conjunction perfects. The configuration — five outer planets compressed within ~100 degrees, the three heaviest planets conjunct, and the cyclical index at its 21st-century low — is of the same family that coincided with the 1918, 1954, 1968 and 1982 clusters; on that precedent the affliction is a pandemic-scale epidemic rather than a merely local outbreak, running from early 2020 through 2021 before it loosens. Timing unit: year (mundane scale), main coordinate early 2020 (conjunction exact) with the affliction's tail through 2021. Confidence: moderate-high.",
    "basis": "Card carries no tradition/system field; the card's own setting supplies the mundane configuration (Jupiter–Saturn–Pluto conjunction exact early 2020, five outer planets within ~100°, cyclical index at century low, past cluster precedents 1918/1954/1968/1982), decided by western mundane astrology per the card's genre. systems_used=[western mundane astrology]. No natal data is given or needed; no chart is fabricated — the reading rests only on the configuration stated on the card. Calibration §8 (quantity check): affliction-scale lines — three-planet conjunction including Saturn–Pluto (classic pestilence pair), extreme cyclical-index low, four historical cluster precedents — main line is the Saturn–Pluto conjunction, scale band set at 'pandemic-scale, multi-country', not downgraded to a local epidemic and not upgraded beyond what precedents support. Calibration §10 scan: claim 'respiratory/fever class' → limiting signal: the card gives no sign/house placements, so the claim is bounded to the epidemic class level only, no organ system or country named; claim 'cresting 2020' → bounded by the conjunction's exact date (stage bound), tail into 2021 stated as loosening, not as a second peak.",
    "confidence": 0.65,
    "trigger": dict(TRIG_OFF),
}

P["WP-002"] = {
    "case_id": "WP-002",
    "prediction_text": "Direction: Barack Obama wins the 2008 presidential election. Saturn moves into opposition with Uranus beginning on Election Day itself — the old order (Saturn) challenged by the insurgent force of change (Uranus), a configuration last seen 45 years earlier in another era-breaking period. In mundane terms the aspect favours the candidate who embodies change over the candidate of continuity: Obama, the younger challenger running on 'change', defeats John McCain, the establishment figure of the incumbent party. The victory is decisive enough to be known on election night/the following day (4–5 November 2008), not a prolonged disputed count. Confidence: moderate-high.",
    "basis": "Card carries no tradition/system field; question is a dated mundane election query with one configuration given on the card (Saturn opposite Uranus from Election Day, last seen 45 years earlier), decided by western mundane astrology. systems_used=[western mundane astrology]. No birth charts are supplied on the card, so no natal claims are made; the call rests on the election-day configuration plus the card's facts (Obama leads for the nomination on a change platform; McCain is the incumbent party's presumptive nominee). Calibration §10 scan: claim 'decisive, known election night' → limiting signal: a Saturn–Uranus opposition can also signify a contested, grinding count, so the claim is bounded — result clear within the immediate election window, no claim made about popular-vote margin; claim 'Obama wins' → no limiting signal in the given configuration (Uranus rising against Saturn supports the challenger), unmodified. Calibration §8: no quantity/margin claim is made, so no scale band is set beyond the win itself.",
    "confidence": 0.65,
    "trigger": dict(TRIG_OFF),
}

P["WP-003"] = {
    "case_id": "WP-003",
    "prediction_text": "Direction: Barack Obama is re-elected on 6 November 2012 — but the count is messy. Mercury turns retrograde on election day itself, the classic signature of a confused, glitch-ridden tally: machine failures, long lines, delayed reporting and post-election disputes over the numbers, echoing the 2000 Mercury-retrograde election's chaos. The incumbent nevertheless emerges the winner once the count settles; the retrograde mars the process, not the final outcome. Timing: result direction apparent within days of 6 November, full clarity only as Mercury moves forward again later in November. Confidence: moderate.",
    "basis": "Card carries no tradition/system field; dated mundane election query whose card supplies one operative configuration (Mercury retrograde beginning on election day, 6 Nov 2012) and the fact of a competitive race with an incumbent seeking re-election; decided by western mundane astrology. systems_used=[western mundane astrology]. No candidate charts are given on the card; the outcome call weighs incumbency (card fact) against the retrograde signature, which in the 2000 precedent disrupted the count without ultimately reversing who took office — hence process-chaos is predicted, outcome-reversal is not. Calibration §10 scan: claim 'Obama re-elected' → limiting signal: Mercury retrograde bounds the manner of the win (disputed/glitched count), not its direction — claim rewritten with that condition bound attached; claim 'clarity later in November' → stage-bounded to Mercury's forward motion, no exact day asserted. Calibration §8: no margin/scale claim made.",
    "confidence": 0.55,
    "trigger": dict(TRIG_OFF),
}

P["WP-004"] = {
    "case_id": "WP-004",
    "prediction_text": "Direction: Hillary Clinton wins the 2016 presidential election. The forecasting panel convened at the international astrology conference in Costa Mesa reads the race for the Democrat: Clinton, the experienced establishment figure favoured by most polls (card fact), takes the White House over Donald Trump on 8 November 2016. The panel's collective judgment aligns with the polling picture rather than against it. Confidence: moderate (panel consensus plus polling concurrence, though election panels have missed before).",
    "basis": "Card carries no tradition/system field; the card frames the source as an international astrology conference election forecasting panel (Costa Mesa, Oct 2016) with most polls favouring Clinton; decided by western mundane astrology as practised by such panels (consensus of practitioners reading the candidates' charts and election-day figures). systems_used=[western mundane astrology]. No individual chart data is reproduced on the card, so the prediction follows the panel format itself: the consensus call. Calibration §10 scan: claim 'Clinton wins' → limiting signal: the card notes a competitive, polarised race and gives no chart data, so no margin, map, or state-by-state claims are made — the claim is bounded to the winner only; no other specific claims advanced. Calibration §8: no quantity claim (no electoral-vote or margin figure) is made.",
    "confidence": 0.55,
    "trigger": dict(TRIG_OFF),
}

P["WP-005"] = {
    "case_id": "WP-005",
    "prediction_text": "Direction: Donald Trump wins the 2016 presidential election. The one panel astrologer who, back when seventeen Republicans still contested the nomination, singled out Trump to become the Republican nominee reads the same figure through to November: the outsider who defied the field defies the polls as well, and defeats Hillary Clinton on 8 November 2016 despite most polls favouring her (card fact). A reader already proven right against consensus on this candidate is followed against consensus again. Confidence: moderate.",
    "basis": "Card carries no tradition/system field; the card distinguishes one panel astrologer by a verified prior call (picked Trump as nominee from a 17-candidate field) from the general panel; decided by western mundane astrology, weighting the demonstrated track record on this exact candidate as the operative signal. systems_used=[western mundane astrology]. No chart data is reproduced on the card; the discriminating fact supplied is the astrologer's earlier against-consensus success on Trump, which is treated as the basis for following that reader's line to its conclusion (nominee → president). Calibration §10 scan: claim 'Trump wins' → limiting signal: polls on the card favour Clinton, so the claim is expressly bounded as an against-consensus call resting on one reader's record, with no margin or map claims attached; no limiting signal narrows the winner claim itself. Calibration §8: no quantity claim made.",
    "confidence": 0.55,
    "trigger": dict(TRIG_OFF),
}

P["WP-006"] = {
    "case_id": "WP-006",
    "prediction_text": "Direction: Britain votes to Leave the European Union on 23 June 2016. The assessment first published in July 2015 and firmed up in February 2016 — when newspaper polls still showed 'Stay' ahead amid masses of undecideds (card facts) — reads the UK national charts and the referendum-day figure (Uranus conjunct Ceres at 23° Aries: a disruptive, break-with-the-nurturing-order signature) as a rupture vote: the electorate breaks with the union rather than ratifying the status quo. The undecided mass breaks late toward Leave, overturning the February polling lead. Confidence: moderate.",
    "basis": "Card carries no tradition/system field; mundane referendum query with the UK national charts (1066/1801/1922) and a referendum-day configuration (Uranus–Ceres conjunction at 23° Aries) supplied on the card; decided by western mundane astrology. systems_used=[western mundane astrology]. The astrologer's two-stage publication (Jul 2015, firmed Feb 2016, before the date was set in public expectations and against the polling trend) is treated as a committed against-consensus reading; Uranus on referendum day supports rupture over continuity. Calibration §10 scan: claim 'Leave wins' → limiting signal: February polls favoured Stay with many undecided, so the claim is bounded to a late-breaking, narrow rupture — no landslide or percentage figure is asserted; claim rests on the referendum-day configuration and national-chart reading only, no regional breakdown claimed. Calibration §8: scale band for the margin set at 'narrow' per the polling facts on the card; no numeric margin asserted.",
    "confidence": 0.55,
    "trigger": dict(TRIG_OFF),
}

P["WP-007"] = {
    "case_id": "WP-007",
    "prediction_text": "Direction: Donald Trump wins the 2016 election — and what decides it is Hillary Clinton's email controversy. The Union Square tarot reading (August 2016, Clinton ahead in most polls) turns on the scandal cards around Clinton: the email affair and the Foundation questions (both already public, card facts) are not background noise but the deciding weight; a late resurgence of the email story in the final stretch breaks Clinton's lead, and Trump takes the election on 8 November 2016. Timing: the decisive turn falls in the last two weeks before election day. Confidence: low-moderate (single-reader street reading; the 'what decides it' element is the stronger half of the call).",
    "basis": "Card carries no tradition/system field; the card specifies a tarot reader consulted in Manhattan's Union Square Park who drew cards on the election (Aug 2016) — no card faces are reproduced on the input card, so the spread itself cannot be re-read and no specific Waite card meanings are fabricated. systems_used=[tarot (Waite tradition, per skill default)]. Input limitation stated plainly: the drawn cards are not on the card, so this prediction rests on the question's own structure ('who wins, and what will decide it') and the card's facts (Clinton leading in polls; email controversy and Foundation already public) — the deciding-factor claim is therefore weighted higher than the winner claim, and overall confidence is lowered accordingly rather than padded. Calibration §10 scan: claim 'Trump wins' → limiting signal: absence of the actual spread bounds this to the weaker half of the prediction, stated as such; claim 'email controversy decides it' → bounded to a late-campaign resurgence (stage bound: final two weeks), not asserted as a constant effect across the whole campaign. Calibration §8: no margin/scale claim made.",
    "confidence": 0.4,
    "trigger": dict(TRIG_OFF),
}

written = 0
for cid, obj in P.items():
    (OUT / f"{cid}.json").write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")
    written += 1
print("written:", written)
