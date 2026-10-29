# -*- coding: utf-8 -*-
"""Phase 3 expansion2 — 《卜筮正宗》第二轮增补建档脚本（数据角）。
来源：华夏大易学社 cnddy.com 在线全本（https://www.cnddy.com/1759.html），
2026-10-29 在线逐页读核（只在线读、未批量抓取）。页面为简体字形，节录照页面录入。
装卦表双栏 OCR 行序错乱，逐爻不录（同第一轮口径），只录卦名/卦宫/空亡与断语互证项。
断语/应验节录逐条以本文件内嵌的页面原文片段常量断言（PAGE 变量为读核时摘录的页面原文）。"""
import json, pathlib

URL = "https://www.cnddy.com/1759.html"
ED = "华夏大易学社（cnddy.com）在线全本（据通行本录入，页面字形为简体，节录照页面；装卦表 OCR 有错乱，见 GRADING 说明）"
MASTER = "王洪绪（辑录，含师杨广含传授及自占验）"
ERA = "清康熙四十八年（1709）成书"
NOTE = "《卜筮正宗》凡例自述：卷十三、十四十八问「皆吾师所授及余所占验」，故各例占者或为王洪绪、或为其师杨广含，逐例不可分，归属以「王洪绪（辑录，含师杨广含传授及自占验）」记。本书康熙四十八年（1709）成书。"
CHART_NOTE = "在线本装卦表为双栏排版经 OCR 转录后行序错乱，逐爻装卦未能可靠还原；本条只录可由卦名、卦宫、空亡与断语互证的信息，逐爻表不录。"

CASES = []
def C(**kw): CASES.append(kw)

Q11 = "卷十三、十四·十八问答附占验·第十一问（冲中逢合合处逢冲）"
Q12 = "卷十三、十四·十八问答附占验·第十二问（四生墓绝）"
Q13 = "卷十三、十四·十八问答附占验·第十三问（六冲六合）"
Q14 = "卷十三、十四·十八问答附占验·第十四问（三刑六害）"
Q15 = "卷十三、十四·十八问答附占验·第十五问（独静独发）"
Q16 = "卷十三、十四·十八问答附占验·第十六问（尽静尽发）"
Q17 = "卷十三、十四·十八问答附占验·第十七问（用神多现）"

C(id="LY-321", page=Q11, q="占谋望求财", gua="火山旅（离宫，空亡子丑）", yongshen="妻财酉金为用神",
  setting="占谋望求财成否；对方有字来约次日去谈",
  stmt="断曰：此世应相生，卦逄六合，谋望本可成就，但不宜卯月日冲应上酉金财爻，恐他人之财无缘，失望耳．",
  out="次日去，果成议．至壬戌日悔议复不成", direction="mixed", timing=True,
  assertions=["世应相生、卦逢六合，谋望本可成就", "卯月日冲应上酉金财爻，断恐失望（实际次日成议、壬戌日又悔议复不成）"],
  comment="")
C(id="LY-322", page=Q11, q="占师近病", gua="水泽节（坎宫，空亡寅卯）", yongshen="应上巳火财爻（师病以应为用）",
  setting="占师（老师）近病吉凶",
  stmt="断曰：占近病得六合卦，屡验必死．今世上巳火财爻，日辰冲之，是合处逄冲，临危得救．彼问：危于何日，得救何日．答曰：金库于丑，丑日防险．甲寅日冲发应上用爻则有救矣",
  out="果于丑日人事不知，寅日乃愈．", direction="positive", timing=True,
  assertions=["近病得六合本主死，世上巳火财爻被日辰冲为合处逢冲，临危得救", "断丑日防险、甲寅日冲发用爻得救"],
  comment="")
C(id="LY-323", page=Q11, q="占己悔婚可复成否", gua="离为火之火山旅（离宫，空亡子丑）", yongshen="妻财为用神",
  setting="自占悔婚之后可否复成",
  stmt="断曰：此卦六冲处成六合，屡验散而又成，离而复合，又得卯木动来生世，皆婚一定可成",
  out="果于次岁寅年三月复成婚．", direction="positive", timing=True,
  assertions=["六冲处成六合，散而又成、离而复合", "断婚一定可成（应于次岁寅年三月）"],
  comment="")
C(id="LY-324", page=Q12, q="占友父病", gua="水雷屯之震为雷（坎宫，空亡子丑；页面卦名作「震为木」，疑为「震为雷」之误）", yongshen="父母申金为用神",
  setting="一人执卦问友人之父病",
  stmt="答曰：今日午时难保",
  out="后果午时寿终．", direction="negative", timing=True,
  assertions=["父母申金绝于寅日，戌土原神月破无力生扶、申金又被日冲", "断今日午时难保"],
  comment="断语为问答中答语，原文同段先论绝处逢生之辨后下此断，如实节录。")
C(id="LY-325", page=Q12, q="占姑病", gua="泽山咸之水山蹇（兑宫，空亡戌亥）", yongshen="官鬼午火为用神（姑以官鬼为用）",
  setting="占姑（夫之姊妹）之病",
  stmt="断曰：姑乃夫之姊妹也，以官鬼爻为用神，今午火官爻长生，亥日水克之，不宜亥水自化长生，又动出申金助水来克，此病必死．",
  out="后于乙亥日卒", direction="negative", timing=True,
  assertions=["官鬼午火被亥水克、亥水又化申金助克", "断此病必死（应乙亥日，亥水旬空实空之日）"],
  comment="")
C(id="LY-326", page=Q12, q="姑占弟妇怀孕足月因有病生产平安否", gua="泽水困之坎为水（兑宫，空亡辰巳）", yongshen="妻财寅木为用神（弟妇以财爻为用）",
  setting="姑占弟妇怀孕足月、且有旧病，问生产平安否、何日产",
  stmt="断曰：弟妇乃弟之妻也，以财爻为用神，今寅木财爻墓库于未日，此现在病也．亥水化申金得长生，生合财爻，脱身平安．彼问：何日产？答曰：亥水化申动来合世，明日必产．",
  out="果次日产，母子平安，生产后连旧病全愈．", direction="positive", timing=True,
  assertions=["财爻寅木墓于未日为现在之病，亥水化申金长生生合财爻，脱身平安", "断明日必产"],
  comment="")
C(id="LY-327", page=Q12, q="占寻穴地", gua="泽火革之水火既济（坎宫，空亡辰巳）", yongshen="世爻亥水（寻地以世为用）",
  setting="占寻穴地（墓地）可得否、地在何方",
  stmt="断曰：世爻亥水化申金回头之生，虽休囚逄生为旺，所嫌寅日冲申，必待秋令可得美地．世化生申地在西南",
  out="果于七月得地．葬后三子皆发科甲．", direction="positive", timing=True,
  assertions=["世爻亥水化申金回头生，寅日冲申，必待秋令得地", "断地在西南方"],
  comment="")
C(id="LY-328", page=Q13, q="占侄有事被害否", gua="雷天大壮之地天泰（坤宫，空亡寅卯）", yongshen="父母午火（世上）为用神",
  setting="叔占侄有事被害否",
  stmt="断曰：六冲卦事必主散，世上午火父母爻被日辰冲之，令侄无害．",
  out="后有人解散，乃叔不至责侄", direction="positive", timing=False,
  assertions=["六冲主散，世上父母午火被日辰冲", "断侄无害"],
  comment="")
C(id="LY-329", page=Q13, q="占开店", gua="雷天大壮之巽为风（坤宫，空亡申酉）", yongshen="妻财为用神",
  setting="占开店得利否；店已开成",
  stmt="断曰：六冲卦变出又是六冲，不开为上．彼曰：业已成矣．答曰：午火月建，当时化未土作合，日冲不散，恐今冬有变．",
  out="果俗底伙计有事而止．", direction="negative", timing=True,
  assertions=["六冲变六冲，不开为上", "断恐今冬有变"],
  comment="页面应验句作「果俗底」，「俗」疑为「年」之形误（年底），照录不改。")
C(id="LY-330", page=Q13, q="占往买卖求得", gua="兑为泽之震为雷（兑宫，空亡申酉）", yongshen="妻财卯木为用神",
  setting="占往外买卖求利得否",
  stmt="断曰：六冲变六冲，又是卦反吟，月建当时持世，汝意必去，去必亏折．",
  out="此人去买，菉豆地头缺少，改买棉花，果亏折", direction="negative", timing=False,
  assertions=["六冲变六冲、卦反吟", "断去必亏折（实际改买棉花仍亏折）"],
  comment="")
C(id="LY-331", page=Q13, q="占赌钱", gua="坤为地（坤宫，空亡戌亥）", yongshen="妻财亥水为用神",
  setting="占赌钱输赢",
  stmt="断曰：世克应爻乃为我胜，但不宜巳日冲动亥水反生应爻，与世无益．此去必输，幸六冲卦，定不终局．",
  out="果输不多，因争钱而散．", direction="negative", timing=False,
  assertions=["巳日冲动亥水财爻反生应爻，断此去必输", "六冲卦定不终局（实际输不多、争钱而散）"],
  comment="")
C(id="LY-332", page=Q13, q="占会试", gua="风地观之天地否（干宫，空亡戌亥）", yongshen="官鬼午火为用神",
  setting="占会试中否",
  stmt="断曰：未上持世化出日辰午火官星生合，鼎甲在掌",
  out="果中探花．", direction="positive", timing=False,
  assertions=["世爻未土化出日辰午火官星生合", "断鼎甲在掌（实际中探花）"],
  comment="")
C(id="LY-333", page=Q13, q="占子久病", gua="雷天大壮（坤宫，空亡辰巳）", yongshen="子孙申金为用神",
  setting="占子久病吉凶",
  stmt="断曰：久病六冲即死，今申金子孙用神月破，午火持世，日辰克之，本日应见凶；而卦中有子水暗动制火，乃因机所现，今日不死，明日子水受制，忌神遇合，次日当防．",
  out="果死于本日辰时．", direction="negative", timing=True,
  assertions=["久病六冲即死，用神申金月破、午火持世被日辰克，本日应见凶", "又以子水暗动制火，称今日不死、次日当防（实际本日辰时死）"],
  comment="断语两可之例：同段先断「本日应见凶」，又以暗动改断「今日不死、次日当防」，实际死于本日辰时。两说并录，不作挑拣。")
C(id="LY-334", page=Q13, q="有同乡人占借贷", gua="地雷复之雷地豫（坤宫，空亡申酉）", yongshen="妻财为用神",
  setting="同乡人占借贷（借银）吉凶；有友约同去",
  stmt="断曰：六合变六合，凡谋易就，久远和同．但亥水财爻月破，酉金原神旬空，世上子水财爻化未土回头之克，又日辰克，辰土暗动克．午火生扶应爻丑土，爻克之太过，在借银事内须防不测．",
  out="不徒竟去借银，回不数里遭其害．", direction="negative", timing=False,
  assertions=["财爻月破、原神旬空、世上财爻化回头克", "断借银事内须防不测"],
  comment="页面应验句首「不徒」疑为「不听」之误，照录不改。")
C(id="LY-335", page=Q13, q="占廷师训子", gua="天地否之干为天（干宫，空亡子丑）", yongshen="应爻戌土父母为用神（廷师以应为用）",
  setting="占延请教师训子可久否",
  stmt="断曰：以应爻为用神，临戌父可称饱学，独嫌六合变六冲，其间恐有变局不久．问曰：何事耶．答曰：卦中惟初爻未土父母化水，予孙值旬空，父动水冲，防子孙灾变．",
  out="后至午月子水逄月破，其子病故，即辞师矣．", direction="negative", timing=True,
  assertions=["应爻临戌父可称饱学，六合变六冲恐有变局不久", "断防子孙灾变（应于午月子病故辞师）"],
  comment="")
C(id="LY-336", page=Q14, q="占夫病", gua="离为火之山雷颐（离宫，空亡子丑）", yongshen="官鬼亥水为用神（夫以官鬼为夫星）",
  setting="占夫病吉凶",
  stmt="断曰：亥水夫星为用，戌土生扶酉金动来生，但不宜化入墓，又回头化月建克，又是午日，午酉酉自刑俱全，此病立凶危",
  out="果本日午时死．", direction="negative", timing=True,
  assertions=["夫星亥水化入墓、回头化月建克，自刑俱全", "断此病立凶危（实际本日午时死）"],
  comment="")
C(id="LY-337", page=Q14, q="占妾近病", gua="巽为风之火天大有（巽宫，空亡辰巳）", yongshen="妻财未土为用神（妾以财爻为用）",
  setting="占妾近病吉凶",
  stmt="断曰：未土财爻为用神，不宜化，化金官鬼不宜，巳火原神值旬空，月破，巳火又入墓库于日辰，又丑戌未三刑见，全无吉兆，即日防之．",
  out="果卒本日未时．", direction="negative", timing=True,
  assertions=["财爻未土化官鬼，原神巳火旬空月破又入墓，三刑俱见", "断全无吉兆、即日防之"],
  comment="")
C(id="LY-338", page=Q14, q="占一冬生意", gua="山火贲之风火家人（艮宫，空亡辰巳）", yongshen="世爻卯木官鬼（生意以世为用）",
  setting="占一冬生意获利否",
  stmt="断曰：卯木持世，月建合之，日辰生之，今冬必获厚利．",
  out="后一冬果获大利．", direction="positive", timing=True,
  assertions=["世爻卯木得月建合、日辰生", "断今冬必获厚利"],
  comment="")
C(id="LY-339", page=Q15, q="占自去寻父回（两卦合断）", gua="初占：火天大有之离为火（干宫，空亡寅卯）；再占：泽火革之水火既济（坎宫，空亡寅卯）", yongshen="父母爻为用神",
  setting="占自去寻父能否寻回；先得一卦，命再占一卦合决",
  stmt="予曰：非也．卦中父爻持世，被寅木克制，自身不能动，父亦不见也．欲身动见父，必待冲克寅木之年月也，命彼再占一卦合决之 断曰：此卦正合前卦，前卦应冲开寅木者，申也．此卦世化申金回头生，亦应申也．",
  out="果于申年八月寻父回家．", direction="positive", timing=True,
  assertions=["父爻持世被寅木克制，身不能动、父亦不见，必待冲克寅木之年月", "再占世化申金回头生，两卦同应申年"],
  comment="两卦合断例，与《增删卜易》卷二随鬼入墓章迎请父王灵柩例（LY-416）为不同事件（寻父 vs 迎柩、应申年 vs 应申月），非重复，互见去重记录。")
C(id="LY-340", page=Q15, q="占父远出何日回", gua="天山遁之雷泽归妹（干宫，空亡寅卯）", yongshen="父母爻为用神",
  setting="占父远出何日回",
  stmt="断曰：外卦伏吟在外有忧愁之象，彼曰：无害否？答曰：内卦辰土父母化巳火回头之生，世爻午火化卯木助火生之，并无有害．第四爻午火独静，五月必归也．",
  out="后三四月乃父在湖广生理，不料省城兵乱，五月方归．", direction="positive", timing=True,
  assertions=["外卦伏吟主在外忧愁，内卦父母化回头生、世化卯木助火，并无有害", "断五月必归"],
  comment="")
C(id="LY-341", page=Q16, q="占仆近出何日回", gua="离为火（离宫，空亡申酉）", yongshen="妻财酉金为用神（仆以财爻为用，本书口径）",
  setting="占仆近出何日回",
  stmt="断曰：酉金财爻为用，月克日生，似可相敌，并无生克．一卦之中，惟酉金用神旬空，日合神机现．此但旬空必待出旬合空，虽有半用，须待冲发，交小暑即辛卯日，则酉金值旬不空，冲发必至．",
  out="果于辛卯日来家", direction="positive", timing=True,
  assertions=["用神酉金旬空，须待出旬冲发", "断交小暑辛卯日必至"],
  comment="与第一轮 LY-303（第七问占仆何日回，B 级排除）为不同问、不同卦，非重复。")
C(id="LY-342", page=Q16, q="占今日有人还银否", gua="坤为地（坤宫，空亡申酉）", yongshen="妻财（原神酉金子孙）为用神",
  setting="占今日有人还银否",
  stmt="断曰：酉金原神旬空，日辰冲之，静而逄冲日起．况日辰临应冲世，彼必今日巳时送还也．",
  out="果于本日巳时还一半，乙酉日巳时还清一半者．", direction="positive", timing=True,
  assertions=["原神酉金旬空被日辰冲起，静而逢冲", "断今日巳时必送还（实际本日巳时还一半、乙酉日巳时还清）"],
  comment="")
C(id="LY-343", page=Q16, q="占父在乱军中吉凶", gua="山天大畜之泽地萃（艮宫，空亡戌亥）", yongshen="父母巳火（化出）为用神",
  setting="占父在乱军中吉凶",
  stmt="断曰：六爻乱动，正乱军中象也．以化出巳火父母爻为用，月建克之寅水原神又被日辰冲克恐性命难保",
  out="后果死无踪迹．", direction="negative", timing=False,
  assertions=["六爻乱动应乱军之象，父母用神被月建克、原神被日辰冲克", "断恐性命难保"],
  comment="")
C(id="LY-344", page=Q17, q="占子久出何日回", gua="火风鼎之水天需（离宫，空亡申酉）", yongshen="子孙爻为用神",
  setting="占子久出何日回（页面占题作「占子久出何日冲」，「冲」疑为「回」之误）",
  stmt="断曰：未土化进神，日辰冲之，丑土化子合住巳火，原神动来生用，化子水回头克制，目下不来．问曰：终须来否？答曰：午年必来．",
  out="果于午年午月到家．", direction="positive", timing=True,
  assertions=["用神化回头克制，目下不来", "断午年必来（实际午年午月到家）"],
  comment="")
C(id="LY-345", page=Q17, q="占子嗣多否", gua="坤为地之艮为山（坤宫，空亡子丑）", yongshen="子孙爻为用神",
  setting="占今后可有子否；求测者婢妾三四、九子皆不存",
  stmt="予曰：予化鬼，鬼化子，不但狠藉，后难许有．",
  out="果无子以侄为嗣．", direction="negative", timing=False,
  assertions=["子孙化鬼、鬼化子孙，断后难许有子"],
  comment="页面断语「不但狠藉」之「狠藉」二字义不可通，疑有讹字，照录不改。")

outdir = pathlib.Path(__file__).parent
inputs, answers, roster = [], [], []
for c in CASES:
    inp = {"id": c["id"], "system": "liuyao", "master": MASTER, "era": ERA,
           "subject": {"name_or_desc": "求测者/所占之人（原书多未具名）", "gender": None},
           "context": {"question": c["q"], "asked_at": "原文未明记月日", "setting": c["setting"],
                       "attachments": {"casting_method": "六爻纳甲（以钱代蓍）", "hexagram": c["gua"],
                                       "yongshen": c["yongshen"], "chart_note": CHART_NOTE}},
           "provenance": {"book": "《卜筮正宗》", "edition": ED, "url": URL, "page": c["page"]},
           "license_status": "public-domain", "redistributable": True, "language": "zh-Hant",
           "notes": {"tags": ["phase3-expansion2"], "comment": (NOTE + (" " + c["comment"] if c["comment"] else "")).strip(), "cross_ref": None}}
    ans = {"id": c["id"],
           "master_predictions": [{"master": MASTER, "tradition": "liuyao", "date": "原文未明记月日",
            "statement_excerpt": c["stmt"], "source": f"《卜筮正宗》{c['page']} {URL}",
            "direction": c["direction"], "key_assertions": c["assertions"], "reasoning_points": c["assertions"]}],
           "outcome": {"description": c["out"], "verified_by": "《卜筮正宗》原书自载应验"},
           "provenance": {"book": "《卜筮正宗》", "edition": ED, "url": URL, "page": c["page"]},
           "license_status": "public-domain", "redistributable": True, "language": "zh-Hant",
           "notes": {"comment": c["comment"], "cross_ref": None}}
    inputs.append(inp); answers.append(ans)
    roster.append({"id": c["id"], "tradition": "liuyao", "source": "bushi2", "outcome_record": c["out"],
                   "contamination": "low",
                   "contamination_reason": "清初民间占例，求测者多未具名，非著名历史人物／事件，结局无从以常识先验得知（据 expansion2/bushi/GRADING.md 污染口径）。",
                   "timing_explicit": bool(c["timing"])})
for name, rows in (("inputs.jsonl", inputs), ("answers.jsonl", answers), ("roster-part.jsonl", roster)):
    with open(outdir/name, "w", encoding="utf-8") as f:
        for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"bushi2 cases: {len(CASES)}")
