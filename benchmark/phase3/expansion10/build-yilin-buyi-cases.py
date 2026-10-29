# -*- coding: utf-8 -*-
"""
易林补遗批建档脚本（expansion10 唯一脚本名）：读 yilin-najia-gen-yb 生成盘面，
组装 cases.jsonl 与 inputs/YB-*.json，并执行三键去重与泄漏自检，结果打印待验盘。
转录来源：校正全本主本扫描页图 200dpi 逐字复核（书页 22/48/54/58/84/85/86/124/125）。
"""
import json, os, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from importlib import import_module
gen = import_module("yilin-najia-gen-yb")

BOOK = "易林补遗"
EDITION = "华龄出版社《四库存目纳甲汇刊（三）》校正全本（（明）张世宝撰，郑同校；用户经学校图书馆提供之扫描本）"
LICENSE = "用户经学校图书馆提供，内部研究使用（redistributable=false）"

def build(cid, subject, gender, question, asked_at, setting, hex_full, moving,
          changed_full, chapter_page, excerpt, direction, assertions, timing,
          outcome_desc, grade_note, completeness, comment, tags):
    d = gen.describe(hex_full, moving=moving, changed_full=changed_full)
    base = d["base"]
    hex_label = f"{base['palace']}宫：{hex_full}（{base['palace_label']}）"
    if d["changed_name"]:
        hex_label += f" 之 {d['changed_name']}"
    prov_page = f"校正全本《易林补遗》{chapter_page}（主本 PDF 页 {int(chapter_page.split('书页')[1].split('）')[0].split('、')[0]) + 18}）" if False else chapter_page
    case = {
        "id": cid,
        "tradition": "liuyao",
        "subject": {"name_or_desc": subject, "gender": gender},
        "context": {
            "question": question,
            "asked_at": asked_at,
            "setting": setting,
            "attachments": {
                "casting_method": "liuyao",
                "hexagram": hex_label,
                "moving_lines": d["moving_lines_text"],
                "chart_lines_top_to_bottom": d["chart_lines_top_to_bottom"],
            },
        },
        "provenance": {"book": BOOK, "edition": EDITION, "license_note": LICENSE, "page": chapter_page},
        "language": "zh-Hant",
        "master_predictions": [{
            "master": "张世宝",
            "tradition": "liuyao",
            "date": asked_at,
            "statement_excerpt": excerpt,
            "source": f"《易林补遗》{chapter_page}",
            "direction": direction,
            "key_assertions": assertions,
            "timing_claim": timing,
        }],
        "outcome": {"description": outcome_desc, "verified_by": "原书自载应验（张世宝自记）"},
        "license_status": "internal-research-only",
        "redistributable": False,
        "outcome_grade": "A",
        "grade_note": grade_note,
        "contamination": "low",
        "contamination_reason": "明代民间占例，求测者皆未具名，结局为冷门局部事实，无著名人物与事件，无从常识先验得知",
        "month_day_complete": True,
        "chart_complete": True,
        "completeness_basis": completeness,
        "holdout_eligible": True,
        "notes": {"tags": tags, "comment": comment, "cross_ref": ""},
    }
    return case

SETTING = "明代民间卖卜占验实录（张世宝自记占例，散文体附断语与应验）"
GN = "断验分离成立：断语（含应期断言）在前、原书另载应验在后，结局为冷门局部事实"

CASES = []
CASES.append(build(
    "YB-001", "病子（父为之占，未具名）", "男", "父占子病，问子病吉凶",
    "八月丁巳日", SETTING, "火地晋", None, None,
    "卷一总断章第一，书页22",
    "此卦六爻无子，兼看亲宫子水伏于初爻土下，又值空亡，日月二爻更无主象。必须互出水山蹇，取外卦坎水配为本宫子孙方为有救，又取内卦艮土配作晋卦父母，子被父伤",
    "negative",
    ["子孙（亲宫子水）伏于初爻土下又值空亡、日月无主象，无救", "子被父伤，主子死"],
    "无明确应期（断后果死）",
    "后果死也。",
    GN + "；原文以「且如」引例而附明确后果（死），非纯规则譬喻",
    "原文只记卦名（晋卦安静）与占日；逐爻装卦按通行纳甲法则推算复原。原文自叙「亲宫子水伏于初爻土下，又值空亡」与复原盘面（子孙甲子水伏初爻父母乙未土下；丁巳日在甲寅旬，空子丑，伏神子正值空亡）全合，可互证",
    "晋卦互卦水山蹇，原文断法取互体配六亲；本例为总断章末二例之一（本批普查自书页22起，此二例在第22页内）",
    ["疾病", "父占子病", "伏神", "互卦取用"]))
CASES.append(build(
    "YB-002", "病妻（夫为之占，未具名）", "女", "夫占妻病，问妻病吉凶",
    "六月丙午日", SETTING, "火泽睽", None, None,
    "卷一总断章第一，书页22",
    "此卦六位无财，亲宫子水伏在未土之下，伏被飞伤又无用处，况日月之中皆无财象，本无救也。再看互出既济，取外卦坎水配为艮内妻财，纵有月建忌神，不能伤克，至戊申日，财遇长生",
    "positive",
    ["六爻无妻财、本无救，赖互出既济取外卦坎水配为妻财", "至戊申日财遇长生，病可愈"],
    "戊申日（财遇长生之日）病愈",
    "至戊申日，病果愈也。",
    GN,
    "原文只记卦名（睽卦安静）与占日；逐爻装卦按通行纳甲法则推算复原。原文自叙「亲宫子水伏在未土之下」与复原盘面（妻财丙子水伏五爻兄弟己未土下）全合，可互证",
    "睽卦互卦水火既济；原文「子水」指伏神地支子水（丙子），其六亲为妻财",
    ["疾病", "夫占妻病", "伏神", "互卦取用"]))
CASES.append(build(
    "YB-003", "问何年得子者（未具名）", "男", "问何年得子",
    "甲申年二月子日", SETTING, "地水师", None, None,
    "后嗣有无章第十三，书页54",
    "此卦子居旺地也，主早生。盖为子孙属木，木胎在酉，木养在戌",
    "positive",
    ["子孙居旺地，主早生", "乙酉年怀胎、丙戌年得子"],
    "木胎在酉、木养在戌：乙酉年怀胎，丙戌年得子",
    "果应乙酉年怀胎，丙戌年得子。",
    GN + "；应验跨年（甲申占、乙酉怀胎、丙戌得子），事实明确可分离",
    "原文只记卦名（师卦，未言动静）与占时；无之卦、无动爻记载，按静卦以通行纳甲法则推算复原。师卦子孙戊寅木居初爻，二月木旺，与原文「子居旺地」合",
    "同章前后二例（辛丑年鼎卦、己亥年大畜卦）断验难分，定B级未入本表，见BUILD-REPORT",
    ["后嗣", "何年得子", "胎养应期"]))
CASES.append(build(
    "YB-004", "孕妇（占腹中胎儿性别，未具名）", "女", "占腹中胎儿男女若何",
    "五月丙午日", SETTING, "火水未济", None, None,
    "六甲生产章第十七，书页58",
    "此卦有内外二子皆临相地，况得日月生扶，该怀双孕，内卦阴包阳是男，外卦阳包阴是女。此卦阳在先而阴在后",
    "positive",
    ["内外二子临相、日月生扶，该怀双孕（双胎）", "内卦阴包阳是男、外卦阳包阴是女，阳先阴后：先生男而后女"],
    "无具体日期（产时见分晓）",
    "果得双胎。先生男而后女也。",
    GN,
    "原文记卦名（未济卦安静）与占日；逐爻装卦按通行纳甲法则推算复原。未济子孙在内卦三爻戊辰土、外卦五爻己未土，与原文「内外二子」合",
    "双胎且性别与出生序皆中，为本批断验最具体之例",
    ["生产", "双胎", "占男女", "阴包阳阳包阴"]))
CASES.append(build(
    "YB-005", "孕妇（占腹中胎儿性别，未具名）", "女", "问腹中胎儿男女",
    "四月辛未日", SETTING, "雷泽归妹", None, None,
    "六甲生产章第十七，书页58",
    "此卦阴阳既不相包，六爻内又无子象，伏出兑家亥水更值旬空。难分男女。岂知互成既济，止取互卦，外宫坎水正配兑家子孙，坎曰中男",
    "positive",
    ["本卦无子象、伏神旬空，本难分男女", "取互卦既济之外卦坎水配为子孙，坎为中男，主生男"],
    "无具体日期（产时见分晓）",
    "果得男子也。",
    GN,
    "原文记卦名（归妹卦，未言动静）与占日；无之卦记载，按静卦以通行纳甲法则推算复原。归妹六爻无子孙，伏神子孙丁亥水伏四爻官鬼庚午火下；辛未日在甲子旬，空戌亥，与原文「伏出兑家亥水更值旬空」全合",
    "与YB-014同卦（归妹安静）而占时、所问、结局皆异，非重复例",
    ["生产", "占男女", "伏神", "互卦取用"]))
CASES.append(build(
    "YB-006", "家主（自占阖宅，未具名）", "男", "家主自占，问阖宅一年人口休咎（人宅六事）",
    "寅月甲寅旬辛酉日", SETTING, "天风姤", None, None,
    "人宅六事章第四十四，书页84-85",
    "此卦世在初爻，正临空地，世爻为家主，初爻为小口，其年二月内，家主与次男皆生病疾。又看五爻为父，又逢月破之乡，此年十月内，父患大灾",
    "negative",
    ["世爻（家主）临空：其年二月内家主与次男皆生病疾", "五爻父逢月破：此年十月内父患大灾"],
    "二月内（家主、次男病）、十月内（父灾）",
    "其年二月内，家主与次男皆生病疾；此年十月内，父患大灾。",
    "断验分离成立：断语分载二月、十月两组应期，原书以「应此卦也」收束确认；事件本身（何人、何时、何事）明确可分离。按：本例断语与应验同段叙述，分离度弱于同批他例，主持如从严可复核",
    "原文记卦名与占时（原书卦名作「垢」，系姤之异写，本书疾病章涣之姤例同作「垢」，校正本通例如此，盘面按天风姤复原）；逐爻装卦按通行纳甲法则推算复原。姤世在初爻父母辛丑土，甲寅旬空子丑，与原文「世在初爻，正临空地」合；五爻兄弟壬申金，寅月冲申，与原文「五爻为父，又逢月破」之月破合（原文以人宅分宫以五爻为父）",
    "人宅六事以六爻分宫配家人（初爻小口、五爻父），与通行六亲并行，原文口径照录",
    ["人宅", "一年休咎", "分宫定位", "月破", "旬空"]))
CASES.append(build(
    "YB-007", "某家宅长与宅母（家人代占，未具名）", "未知", "家人代占人宅，问阖宅一年人口休咎（人宅六事）",
    "正月甲子旬壬申日", SETTING, "雷天大壮", None, "火天大有",
    "人宅六事章第四十四，书页85",
    "家人占者，不必取六爻分宫所断。此卦五爻临月破，理应宅长之灾，岂知申日卜之，不为月破，此宅长反主一年康泰。又论第二爻为宅母，被日辰冲破，理合生灾，虽临月建，目下纵是平安",
    "negative",
    ["五爻宅长虽临月破，申日卜之不为月破，宅长反主一年康泰", "二爻宅母被日辰冲破，目下平安，后至七八月染灾殃"],
    "宅母应期在七八月；宅长为一年康泰",
    "后至七八月，宅母果染灾殃，有此验也。",
    GN + "。按：本例双断——宅长康泰（吉）与宅母灾殃（凶）；有独立应验句者为宅母一断（「有此验也」），A级以此为准，direction以此凶断为主轴登记，评分时请注意双向性；宅长「一年康泰」一断原书无独立应验句，仅以本例入录附记",
    "原文记本变卦名（大壮之大有）与占时；动爻由本变卦爻位异同唯一确定为上六爻，逐爻装卦按通行纳甲法则推算复原。五爻子孙庚申金正月（寅月）冲申月破、二爻官鬼甲寅木壬申日冲破，与原文「五爻临月破」「第二爻被日辰冲破」全合（原文以人宅分宫以五爻为宅长、二爻为宅母）",
    "原文「申日卜之，不为月破」谓申日与月破之申同支反得日扶，为本书特有断法口径，照录",
    ["人宅", "代占", "月破", "日冲", "双断"]))
CASES.append(build(
    "YB-008", "家主一门十一口（家主占一年人口六事，未具名）", "未知", "家主来占一年人口六事（问阖家一年休咎）",
    "癸卯年寅月壬午日", SETTING, "泽山咸", [2, 5], None,
    "人宅六事章第四十四，书页86-87",
    "此卦内三爻太旺，房屋新创整齐者。外三爻是兑，正值休囚。况在甲戌旬占，兑酉又居空亡。五爻为人口，亦值空亡，虽云动不为空，岂知化出申爻亦空也。外卦与五爻皆绝于月建寅中，同败于日辰午内，又被动爻与日辰克制，人口之爻毫无救助",
    "negative",
    ["人口之爻空绝、毫无救助，全家人口有大灾", "此年春季瘟疫，十一口连丧十人"],
    "此年春季正二三月内",
    "其家一十一口，此年春季同染瘟疫之灾，正二三月内，连丧十人，止留一口。",
    GN + "；死亡人数（十一口丧十）为具体数字事实",
    "原文明记动爻（二爻五爻动），动爻从原文；变卦雷风恒由动爻推得，逐爻装卦按通行纳甲法则推算复原。壬午日在甲戌旬（空申酉），五爻兄弟丁酉金值空、动化兄弟庚申金亦空，与原文「五爻亦值空亡，化出申爻亦空」全合",
    "结局惨烈而属无名之家局部事件，污染仍为low（无从先验得知具体丧亡人数）",
    ["人宅", "瘟疫", "一年休咎", "旬空", "化空"]))
CASES.append(build(
    "YB-009", "病父（子为之占，未具名）", "男", "子占父病，问何日见凶",
    "五月甲子日", SETTING, "风地观", None, "风雷益",
    "疾病吉凶章第六十九「占何日病凶云」，书页124",
    "此卦父爻动居旺地，又带青龙贵人，本为吉象；岂知父化月破，后至乙亥日，原神绝而忌神生",
    "negative",
    ["父爻虽旺相带吉神，化爻月破、原神绝而忌神生，父必丧", "应期乙亥日"],
    "乙亥日",
    "后至乙亥日，果然父丧。",
    GN,
    "原文记本变卦名（观之益）与占日；动爻由本变卦爻位异同唯一确定为初爻，逐爻装卦按通行纳甲法则推算复原。初爻父母乙未土动化子孙庚子水，五月（午月）子午冲，与原文「父化月破」全合",
    "「占何日病凶云」子目五例皆问应期，断语应期明确",
    ["疾病", "子占父病", "病凶应期", "化月破"]))
CASES.append(build(
    "YB-010", "病夫（妻为之占，未具名）", "男", "妻占夫病，问何日见凶",
    "三月甲子旬丁卯日", SETTING, "风水涣", None, "天风姤",
    "疾病吉凶章第六十九「占何日病凶云」，书页124",
    "所嫌仇神忌神皆动，独无用爻，又鬼伏仇爻之下，又值旬空，毫无救助。挨至乙亥日用爻透出，鬼受忌神来伤",
    "negative",
    ["仇忌皆动、用爻无救，夫病必死", "挨至乙亥日用爻透出、鬼受忌神伤之时应"],
    "乙亥日",
    "挨至乙亥日，夫果死也。",
    GN,
    "原文记本变卦名（涣之垢卦，「垢」系姤之异写，同YB-006）与占时；动爻由本变卦爻位异同唯一确定为三、四爻，逐爻装卦按通行纳甲法则推算复原。按：原文称「独无用爻，又鬼伏仇爻之下」，而通行装卦涣卦五爻有辛亥水官鬼，原文口径与通行装卦表面不合，原文照录、盘面按通行装卦复原并在此登记，主持可裁",
    "与YB-009同为乙亥日应期，一愈一死无涉（本例为死）",
    ["疾病", "妻占夫病", "病凶应期", "旬空"]))
CASES.append(build(
    "YB-011", "病子（父为之占，未具名）", "男", "父占子病，问何日见凶",
    "五月甲午旬癸卯日", SETTING, "泽地萃", [6], None,
    "疾病吉凶章第六十九「占何日病凶云」，书页124",
    "此卦子孙太弱，父母相而又动，虽受卯日相伤，又逢月建扶起，父又化为进气，能克用爻；虽有原神暗动，又值立时空不能相救。后至丙午日，忌象叨生",
    "negative",
    ["子孙太弱、父母动而化进气克用爻，原神不能救，子必死", "应期丙午日"],
    "丙午日",
    "后至丙午日，此男果死。",
    GN,
    "原文明记动爻（上六爻动），变卦天地否由动爻推得；逐爻装卦按通行纳甲法则推算复原。上六父母丁未土动化父母壬戌土，同属土爻位进（未→戌），与原文「父又化为进气」相应（按：化爻六亲干支照变卦本位，原文「进气」口径照录）",
    "原神（兄弟丁酉金居五爻）为癸卯日冲动（卯酉冲）而暗动，与原文「原神暗动」合",
    ["疾病", "父占子病", "病凶应期", "化进气"]))
CASES.append(build(
    "YB-012", "病妻（夫为之占，未具名）", "女", "夫占妻病，问何日见凶",
    "三月甲戌旬庚辰日", SETTING, "地水师", [2, 6], None,
    "疾病吉凶章第六十九「占何日病凶云」，书页124-125",
    "此卦青龙财爻持世，兄弟又不交重，鬼又化出财来，本为佳兆；岂知土官发动，《书》云：「更论土爻临鬼动，多凶少吉祸难逃」，此鬼太刚",
    "negative",
    ["财爻持世、鬼化财本佳兆，然土官发动克财，妻病凶", "五月庚申日官遇长生、月建扶土鬼，应死"],
    "五月庚申日",
    "果应五月庚申日，妻死。",
    GN,
    "原文明记动爻（九二、上六爻动），变卦雷地豫由动爻推得；逐爻装卦按通行纳甲法则推算复原。世在三爻妻财戊午火，与原文「青龙财爻持世」合（六神未建模，青龙为原文自叙）；九二官鬼戊辰土动化妻财乙巳火，与原文「鬼又化出财来」全合；上六父母癸酉金动化子孙丙寅木。按：庚辰日在甲戌旬，空申酉，上六父母正值旬空，原文未及，照实登记",
    "断语引《书》歌诀一句，属断语构成部分，照录",
    ["疾病", "夫占妻病", "病凶应期", "鬼化财"]))
CASES.append(build(
    "YB-013", "病女（父为之占，久远之病，未具名）", "女", "父占女久远病，问吉凶",
    "七月甲寅旬癸亥日", SETTING, "艮为山", None, None,
    "疾病吉凶章第六十九「占何日病凶云」，书页125",
    "此卦用爻临月建，忌神又不兴，似无凶兆；岂知卦犯六冲，《经》云：「初爻遇此当瘳瘥，久病逢之命必伤。」",
    "negative",
    ["用爻临月建、忌神不兴，本似无凶", "然卦犯六冲，久病逢冲命必伤，应在子月戊午日"],
    "子月戊午日（用象死于月建、败于日辰）",
    "果应在子月戊午日，其女死也。",
    GN,
    "原文记卦名（艮卦安静）与占时；逐爻装卦按通行纳甲法则推算复原。用爻子孙丙申金居五爻，七月（申月）临月建，与原文「用爻临月建」全合；艮为山为六冲卦，与原文「卦犯六冲」合",
    "新病逢冲则愈、久病逢冲则死为本书明文口径，本例问者特标「久远病」",
    ["疾病", "父占女病", "久病", "六冲卦"]))
CASES.append(build(
    "YB-014", "病子（母为之占，未具名）", "男", "母占子病，问吉凶",
    "九月甲子旬辛未日", SETTING, "雷泽归妹", None, None,
    "疾病吉凶章第六十九「占何日病凶云」，书页125",
    "此卦六爻无子，虽伏出亥水子孙在四爻之下，又落空亡；世上父母又被日辰冲动，本绝卦也；岂知互出水火既济，取互体坎水配成兑卦，子孙乃无中生有也。惟互出之爻，再不受日月并动爻伤克",
    "positive",
    ["六爻无子、伏神落空、父母被冲，本为绝卦", "赖互出既济取互体坎水配为子孙，无中生有，子病可脱体", "亥月戊子日用值旺乡，病愈"],
    "亥月戊子日",
    "此子果应亥月戊子日，用值旺乡，病全脱体。",
    GN,
    "原文记卦名（归妹卦安静）与占时；逐爻装卦按通行纳甲法则推算复原。归妹六爻无子孙，伏神子孙丁亥水伏四爻官鬼庚午火下；辛未日在甲子旬，空戌亥，与原文「伏出亥水子孙在四爻之下，又落空亡」全合；归妹世在三爻、世爻即父母丁丑土，辛未日未冲丑，与原文「世上父母又被日辰冲动」全合（「世上」谓世位所临之爻）",
    "与YB-005同卦同静（归妹安静）而占时、所问、结局皆异；本例为「占何日病凶云」子目中唯一得生之例（编号于去重剔除后重排）",
    ["疾病", "母占子病", "伏神", "互卦取用", "绝处逢生"]))

def main():
    import re
    root = os.path.expanduser("~/workspace/divination")
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "yilin-buyi")
    os.makedirs(os.path.join(outdir, "inputs"), exist_ok=True)

    # ---- 三键去重（先于落盘）：全池 cases.jsonl 扫描 ----
    pool = []
    for p in glob.glob(root + "/benchmark/**/cases.jsonl", recursive=True):
        if "expansion10" in p:
            continue
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if line:
                pool.append((p, json.loads(line)))
    print(f"pool cases loaded: {len(pool)}")
    def day_token(s):
        m = re.findall(r"([甲乙丙丁戊己庚辛壬癸][子丑寅卯辰巳午未申酉戌亥]日)", s or "")
        return m[-1] if m else ""
    KIN = ["妻占夫病", "父占子病", "母占子病", "夫占妻病", "子占父病", "父占女", "夫占妻", "子占父"]
    dropped = []
    kept = []
    for c in CASES:
        dt = day_token(c["context"]["asked_at"])
        hexshort = c["context"]["attachments"]["hexagram"].split("：")[1].split("（")[0]
        kin = [k for k in KIN if k in c["context"]["question"]]
        hit = None
        for p, pc in pool:
            pat = pc.get("context", {}).get("asked_at", "")
            phex = pc.get("context", {}).get("attachments", {}).get("hexagram", "")
            pq = pc.get("context", {}).get("question", "")
            if dt and day_token(pat) == dt and hexshort in phex and any(k in pq for k in kin):
                hit = pc["id"]
                break
        if hit:
            dropped.append((c["id"], hit))
            print(f"DEDUP DROP {c['id']} == pool {hit} (day={dt}, hex={hexshort}, kin={kin})")
        else:
            kept.append(c)
    print(f"dedup: kept {len(kept)}, dropped {len(dropped)}")
    # 去重后按书序重编 YB 号
    for i, c in enumerate(kept, 1):
        c["id"] = f"YB-{i:03d}"
    CASES_FINAL = kept

    # 写 cases.jsonl 与 inputs
    with open(os.path.join(outdir, "cases.jsonl"), "w", encoding="utf-8") as f:
        for c in CASES_FINAL:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    for old in glob.glob(os.path.join(outdir, "inputs", "YB-*.json")):
        os.remove(old)
    for c in CASES_FINAL:
        inp = {k: v for k, v in c.items() if k not in ("master_predictions", "outcome")}
        with open(os.path.join(outdir, "inputs", f"{c['id']}.json"), "w", encoding="utf-8") as f:
            json.dump(inp, f, ensure_ascii=False, indent=2)
    print(f"wrote {len(CASES_FINAL)} cases")

    # ---- 泄漏自检 ----
    FORBID_KEYS = {"outcome", "master_predictions", "key_assertions", "direction", "timing_claim"}
    FORBID_TERMS = ["后果死", "病果愈", "果得双胎", "果得男子", "果染灾殃", "连丧十人",
                    "果然父丧", "夫果死", "男果死", "病全脱体", "果应"]
    def walk(o, path=""):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in FORBID_KEYS:
                    yield f"KEY {path}/{k}"
                yield from walk(v, path + "/" + k)
        elif isinstance(o, list):
            for i, v in enumerate(o):
                yield from walk(v, f"{path}[{i}]")
        elif isinstance(o, str):
            for t in FORBID_TERMS:
                if t in o:
                    yield f"TERM {t} at {path}"
    bad = 0
    for c in CASES_FINAL:
        inp = json.load(open(os.path.join(outdir, "inputs", f"{c['id']}.json"), encoding="utf-8"))
        hits = list(walk(inp))
        if hits:
            bad += 1
            print(f"LEAK {c['id']}: {hits}")
    print(f"leak check done, files with hits: {bad}")

if __name__ == "__main__":
    main()
