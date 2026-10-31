#!/usr/bin/env python3
"""R90 data seat: build data/case-annotations-r90.json from r89 (321) + 41 new.
Platform 11 (partial 7 / not-upheld 4), acceptance 30 (partial 24 / not-upheld 6).
All findings verified per-case against cards / R90 predictions / holdout32 gold.
No scores, outcomes, cards or method files touched."""
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "data/case-annotations-r89.json"
OUT = P3 / "data/case-annotations-r90.json"

ann89 = json.loads(SRC.read_text(encoding="utf-8"))
assert len(ann89["annotations"]) == 321
base = ann89["annotations"]

PM = "divination/benchmark/phase3/runs/round90/judging/host-mapping.json"
AM = "divination/benchmark/phase3/runs/round90/acceptance/judging/host-mapping.json"
GOLD = "divination/benchmark/phase3/holdout32/test_gold.jsonl"

def plat(cid, extra=None):
    s = [f"divination/benchmark/phase3/inputs-dev12/{cid}.json",
         f"divination/benchmark/phase3/runs/round90/predictions/{cid}.json", PM,
         "divination/benchmark/phase3/runs/round90/judging/outcome-manifest.json cases[" + cid + "]"]
    return (extra or []) + s

def acc(cid, extra=None):
    s = [f"divination/benchmark/phase3/holdout32/inputs/{cid}.json",
         f"{GOLD} [{cid}]",
         f"divination/benchmark/phase3/runs/round90/acceptance/predictions/{cid}.json", AM]
    return (extra or []) + s

E = []
def add(anon, cid, disp, flag, finding, sugg, relation, sources, seats):
    E.append({"anon_id": anon, "case_id": cid, "disposition": disp, "finding": finding,
              "flag": flag, "manifest_carry_suggestion": sugg, "relation": relation,
              "registered_round": 90, "sources_checked": sources, "source_seats": seats})

NL = "只登记不入层：自 R91 起承接本 R90 标注（不成立，不入承接层）；结局原文照录不改。"
NA = "只登记不入层：自 R91 起承接本 R90 标注（不成立，验收侧不入 dev 承接层）；金标原文照录不改。"

# ---------------- platform ----------------
add("P3-bb516e65", "AS-009", "部分成立",
    "主持检查器＋FREEZE-r90 裁定：卡面实载 tradition='horary'，R90 prediction basis 首行误称「卡面未标注 tradition 字段」",
    "主持裁定部分成立（FREEZE-r90 tradition 旗标裁定，本席逐件回读复核）：回原卡——卡面顶层逐字载 tradition＝'horary'（键集 uid／tradition／subject／context／provenance）；R90 prediction basis 首行逐字作「卡面未标注 tradition 字段，按题面体裁自决」，与卡面实载不符、措辞不实一层成立。但该例实际作断体系为 horary（basis 内 systems_used 明载 horary astrology、断法与卡面 tradition 一致），无体系误标、无虚构卡面值，不作废不重测。故部分成立。与在册 R85 条（R85 轮主持裁定不成立＋措辞不精确附注）及 R86 条（OCR 残损旨）各轮／各旨独立、并行不悖。",
    "平台侧新登记：自 R91 起承接本 R90 标注：按「卡面实载 tradition＝horary、R90 首行误称未标注属措辞不实，注记须以卡面实载值 horary 为准回写；实际作断体系与卡面一致、无体系误标，部分成立」登记；结局原文照录不改。",
    "同例新轮新旨（R90 主持裁定；与 R85／R86 在册条并行）",
    plat("AS-009", ["divination/benchmark/phase3/runs/round90/FREEZE-r90.md tradition 旗标裁定节"]), ["主持检查器", "FREEZE-r90 主持裁定"])

add("P3-843f2c9d", "BZ-032", "不成立",
    "axis2 评审 X3 席：称 R90 prediction basis 首行虚称 tradition=bazi",
    "回原卡与 R90 prediction 首行逐字核——原卡顶层无 tradition/system 字段（键集 id／source_id／subject／context／provenance／language）；R90 prediction basis 首行逐字作「卡面未标注 tradition 字段，按题面体裁自决｜本例四柱癸未 辛酉 乙酉 丁亥、日主乙木，男。」——如实自承未标注、未称卡面载有 tradition 值，与 axis2 另两席回读一致。X3 席旗标所称首行虚称 tradition＝bazi 于本轮首行无据。故不成立。与在册 R76 条（R76 轮首行确曾虚称、主持裁定部分成立）各轮独立、不改旧条（承 BZ-021 R89 登记同型）。",
    NL, "新登记（R90，axis2 旗标定案；与 R76 在册条各轮独立）", plat("BZ-032"), ["X3（axis2 评审）"])

for anon, cid, spec in [
    ("P3-41f19f6c", "LY-017", "题为占升遷，澤地萃之天地否，酉月乙巳日"),
    ("P3-435a41cc", "LY-034", "题为占嬸病，離為火之地火明夷，丑月戊午日（本条只裁 tradition 首行旨；卡面 chart_note OCR 自注属另一旨、不在本旗标内）"),
    ("P3-7220235a", "LY-019", "题为占小舟過關恐盤阻，水地比之澤山咸，辰月戊子日"),
]:
    add(anon, cid, "不成立",
        "作废轮（整体分）X2 席据 carry_note 旧注立旗标：疑本例 tradition 首行标示有虚称",
        f"逐件回读本轮（R90）prediction basis 首行，逐字作「卡面未標註 tradition/system 字段，按題面體裁自決用六爻；{spec}。systems_used：六爻納甲（主法）。」——如实自承卡面未标注，与本轮 axis2 各席回读一致；回原卡，卡面顶层确无 tradition/system 字段。旗标所据为 carry_note 旧注、非本轮首行实况。故不成立，只登记。",
        NL, "新登记（R90，作废轮 X2 旗标定案）", plat(cid), ["X2（作废轮整体分）", "axis2 各席回读"])

add("P3-2ad9ea89", "AS-304", "部分成立",
    "作废轮 X1 席：断语归属疑似虚称——prediction_text 称发布者公开落点在特朗普一方，而卡面原文断语已剥离、无从核其归属",
    "逐件回原卡与 R90 prediction 核——卡面 provenance 逐字载标题含断语已剥离、链接略，卡面未载作者姓名、盘面或推论；R90 prediction basis 逐字自承此残损并载「仅据问时与问题作方向断语并显著降置信，不臆补作者星盘」，prediction_text 尾段亦明载方向「据发布时点与其账号一贯立场推定，已降置信」——推定性质如实披露（不成立面）；但 prediction_text 断语段径作「发布者于2024年9月9日公开落点在特朗普一方」以事实语气归属断语，与卡面断语已剥离、无从核对一层不合（成立面）。故部分成立。",
    "平台侧新登记：自 R91 起承接本 R90 标注：按「断语归属为据立场推定、已在 basis 与断语尾段如实披露并降置信；断语段归属语气与卡面断语已剥离之实况一层不合，部分成立」登记；结局原文照录不改。",
    "新登记（R90，X1 旗标定案；与在册 R79／R86 条各旨并行）", plat("AS-304"), ["X1（作废轮）"])

add("P3-3c62af76", "AS-306", "部分成立",
    "作废轮 X1 席：行运依据疑似虚称——prediction_text 以吠陀行运（dasha/过运）权衡为终局依据，而卡面无任何盘面／dasha 数据",
    "逐件回原卡与 R90 prediction 核——卡面 tradition＝vedic-astrology 在载，但 context 仅 question／asked_at／setting，未载任何吠陀盘面、dasha 或过运数据；R90 prediction basis 逐字登记「卡面未载任何吠陀盘面、dasha或过运数据（盘面缺载）」、明载仅据问时与问题自带更替问项作断并降置信——缺载如实披露（不成立面）；但 prediction_text 断语径作「吠陀行运（dasha/过运）权衡终局仍在特朗普一方」，以无盘面数据支撑之行运权衡为终局依据之表述一层属实（成立面）。故部分成立。与在册 R86 条（盘面缺载残损旨）同例并行、本条只裁行运依据表述旨。",
    "平台侧新登记：自 R91 起承接本 R90 标注：按「行运权衡表述无盘面数据支撑一层属实；盘面缺载已在 basis 如实披露并降置信，部分成立」登记；结局原文照录不改。",
    "新登记（R90，X1 旗标定案；与在册 R86 条并行）", plat("AS-306"), ["X1（作废轮）"])

add("P3-58febb21", "LY-518", "部分成立",
    "平台盲测席自报：与 LY-534 同盘异问——卦名、逐爻、动爻、月日全同而问事与来源书不同",
    "逐件回两卡核——本卡（《增删卜易》卷三·面圣上书章）问占上書，申月戊辰日，風澤中孚之山澤損，五爻父母巳火○動，逐爻六行与 LY-534（《卜筮正宗》十八问答第二问，占具題）逐字全同，月日同为申月戊辰日；LY-534 本轮 basis 明载「盘面与 LY-518 上书占同卦同日而问事不同，照本例问事独立作断」。同盘异问一层属实（成立面）；但两例问事（上书／具题）与来源书各自明载，R90 manifest 结局分载「後此人上書﹐不準。」与「后题而果不准行．」，各自终局明载可核、非一卡误植两问（不成立面）。故部分成立，两例并行登记、不删卡、不合并。",
    "平台侧新登记：自 R91 起承接本 R90 标注：按「与 LY-534 同卦同日同爻异问（上书／具题）、两源分载、结局各明载，部分成立」登记；结局原文照录不改。",
    "新登记（R90，同盘异问对偶条，与 LY-534 条互引并行）", plat("LY-518"), ["平台盲测席"])

add("P3-b9cc879f", "LY-534", "部分成立",
    "平台盲测席自报（本例 basis 明载）：与 LY-518 同盘异问——盘面与 LY-518 上书占同卦同日而问事不同",
    "逐件回两卡核——本卡（《卜筮正宗》卷十三、十四·十八问答第二问）问占具題，date_ganzhi 申月戊辰日，風澤中孚之山澤損（艮宮，空亡戌亥），五爻父母巳火○動，逐爻六行与 LY-518（《增删卜易》卷三·面圣上书章，占上書，申月戊辰日）逐字全同；R90 本例 basis 逐字载「盘面与 LY-518 上书占同卦同日而问事不同，照本例问事独立作断」。同盘异问一层属实（成立面）；但两例问事与来源书各自明载，R90 manifest 结局分载「后题而果不准行．」与「後此人上書﹐不準。」，各自终局明载可核、非一卡误植两问（不成立面）。故部分成立，两例并行登记、不删卡、不合并。",
    "平台侧新登记：自 R91 起承接本 R90 标注：按「与 LY-518 同卦同日同爻异问（具题／上书）、两源分载、结局各明载，部分成立」登记；结局原文照录不改。",
    "新登记（R90，同盘异问对偶条，与 LY-518 条互引并行）", plat("LY-534"), ["平台盲测席"])

add("P3-135f80c6", "LY-626", "部分成立",
    "平台盲测席 basis 数据残损登记：卡面三处自相矛盾（asked_at 与补录 date_ganzhi 口径不一；chart_note 称逐爻未能可靠还原而 chart_lines 已实载；moving_lines 作无动爻而 moving_lines_text 称见断语所涉动爻）",
    "回原卡逐处核——卡面 context.asked_at 逐字作「原書未記月日（十八問答體例）」，而 notes 补录 date_ganzhi 为酉月壬辰日，两处口径不一属实；hexagram.chart_note 逐字称逐爻装卦未能可靠还原、逐爻表不录，而 chart_lines 六爻已实载；moving_lines 逐字作「無動爻（靜卦）」，moving_lines_text 又称「見斷語節錄所涉動爻」，三处自相矛盾属实（成立面）。R90 prediction basis 逐字照实登记三处矛盾、明载按补录月日行盘、不臆补动爻并降置信；R90 manifest 结局逐字载「果死於午日午時，此謂伏無提拔也．」，终局明载可核（不成立面）。故部分成立。与在册 R86 条（OCR 行序错乱旨）同例新旨、并行不悖。",
    "平台侧新登记：自 R91 起承接本 R90 标注：按「卡面三处自相矛盾（月日口径／chart_note 与逐爻实载／动爻两载）已照实登记、按补录月日行盘不臆补动爻；终局明载，部分成立」登记；结局原文照录不改。",
    "同例新旨（R90，与在册 R86 条并行）", plat("LY-626"), ["平台盲测席"])

add("P3-efc91c61", "LR3-010", "部分成立",
    "平台盲测席 basis 自报：卡面问仕途而 provenance 门类登记作公讼门，两处登记不一致（UNC）",
    "回原卡——卡面 question 逐字为「此在朝官员仕途吉凶若何？」，provenance 逐字作「《大六壬占验指南》·公讼门·代占一课」，问面与门类登记不一致属实（成立面）；R90 prediction basis 逐字自承此不一致并标 UNC、明载照卡面问面作断并降置信、年命未给不臆补；卡面课式（玄胎、伏吟）、四课、三传俱载，R90 manifest 结局逐字载「后知为四明讳象坤钱相公所占。果因人言请告而去。」，终局明载可核（不成立面）。故部分成立；UNC 标照 PREREG-r90 §6 口径维持、不代编。",
    "平台侧新登记：自 R91 起承接本 R90 标注：按「问面（仕途）与 provenance 门类（公讼门）登记不一致、basis 已自承标 UNC 并照问面作断；课式锚点俱载、终局明载，部分成立；UNC 维持」登记；结局原文照录不改。",
    "新登记（R90，平台 basis 自报定案）", plat("LR3-010"), ["平台盲测席"])

# ---------------- acceptance: (f) outcome granularity ----------------
add("H32O-33b93bd5", "WHY-085", "部分成立",
    "验收评审 O2 席：金标 outcome 以「所断皆验」类概括语宣称全验而未逐项载事实",
    "回 holdout32 金标逐字核——outcome_record 逐字作「此女为某电脑公司的会计，1986年谈恋爱，1988年结婚，现有一女儿，父亲1993年去世。其他断语也皆符合实际情况。」——职业、恋爱、结婚、女儿、父去世五项有事实载述，尾句「其他断语也皆符合实际情况」以概括语宣称其余断语（流产、脾胃、血液循环、头晕诸项）全验而未逐项载事实，粒度缺口一层属实（成立面，照历轮 outcome 粒度类口径）；但已载五项终局事实明载可核、金标 grade_note 明载结局与原书应验情况核对相合（不成立面）。故部分成立（验收面部分成立件照 R83 判例不入 dev 层、只登记）。",
    "验收侧新登记：自 R91 起承接本 R90 标注：按「金标 outcome 五项事实明载、尾句以『其他断语也皆符合实际情况』概括宣称余项全验未逐项载事实，部分成立」登记；金标原文照录不改。",
    "新登记（R90，验收侧旗标定案）", acc("WHY-085"), ["O2（验收评审）"])

add("H32O-66616b38", "WHY-091", "部分成立",
    "验收评审 O2 席：金标 outcome 以「所断皆验」类概括语宣称全验而未逐项载事实",
    "回 holdout32 金标逐字核——outcome_record 逐字作「以上判断全部正确。此人原有官职，后于1989年辞去。财运一直不错。但到了1997年开始，财运走入低谷，到了1999年就连生活也成了困难。2000年也没有什么起色。」——首句「以上判断全部正确」以概括语宣称全验，其后事实载述集中于官职与财运两面，本人安危（年内无灾难）一面未见逐项事实载述，粒度缺口一层属实（成立面，照历轮 outcome 粒度类口径）；但官职、财运终局事实明载可核、金标 grade_note 明载结局与原书应验情况核对相合（不成立面）。故部分成立（验收面不入 dev 层、只登记）。",
    "验收侧新登记：自 R91 起承接本 R90 标注：按「金标 outcome 首句『以上判断全部正确』概括全验、安危一面未逐项载事实，部分成立」登记；金标原文照录不改。",
    "新登记（R90，验收侧旗标定案）", acc("WHY-091"), ["O2（验收评审）"])

add("H32O-6cdcd67b", "WHY-083", "部分成立",
    "验收评审 O2 席：金标 outcome 以「所断皆验」类概括语宣称全验而未逐项载事实",
    "回 holdout32 金标逐字核——outcome_record 逐字作「所断皆验，后俩人和好，女的又回到他的身边。」——「所断皆验」以概括语宣称全验，事实载述只有和好、返回一事，大师断语中对方有妻室、情人结过婚又离婚、迷恋、吵架缘由诸项均未逐项载事实，粒度缺口属实（成立面，照历轮 outcome 粒度类口径）；但主问（分手後会否回到身边）终局明载可核、金标 grade_note 明载结局与原书应验情况核对相合（不成立面）。故部分成立（验收面不入 dev 层、只登记）。",
    "验收侧新登记：自 R91 起承接本 R90 标注：按「金标 outcome 以『所断皆验』概括全验、仅和好一事有事实载述，部分成立」登记；金标原文照录不改。",
    "新登记（R90，验收侧旗标定案）", acc("WHY-083"), ["O2（验收评审）"])

add("H32O-fcb3084c", "BY-031", "部分成立",
    "验收评审 O2 席：金标 outcome 以「所断皆验」类概括语宣称全验而未逐项载事实",
    "回 holdout32 金标逐字核——outcome_record 逐字作「此为路费占也。果所约者复有馈赠之助，而挹彼注兹，先阻后遂，其说亦准。但魁罡加临卯酉，津梁阻隔，半途而返。」——馈赠之助、先阻后遂、半途而返有事实载述，「其说亦准」为概括语，大师断语中二财并见、丁驿重逢、远行诸项未逐项载事实，粒度缺口一层属实（成立面，照历轮 outcome 粒度类口径）；但路费主线终局明载可核、金标 grade_note 已明载文尾同段照录处置（不成立面）。故部分成立（验收面不入 dev 层、只登记）。",
    "验收侧新登记：自 R91 起承接本 R90 标注：按「金标 outcome 主线事实明载、『其说亦准』概括语下二财／丁驿诸项未逐项载事实，部分成立」登记；金标原文照录不改。",
    "新登记（R90，验收侧旗标定案）", acc("BY-031"), ["O2（验收评审）"])

# ---------------- acceptance: (g) blind self-reports ----------------
add("H32O-6cdb1eb6", "DA-059", "部分成立",
    "验收盲测席 basis 自报：年命上神卡面未给，该路无据不报",
    "回原卡逐字核——卡面 subject 载「徐学士（戊辰生，四十一岁）」，anchors 载 asked_at／课名／天盘／四课／三传，无年命上神字段，年命一路上神未给属实（成立面）；R90 验收 prediction basis 逐字自承「年命上神卡面未给，该路无据不报」、只据干上与三传立论；金标 outcome_record 逐字载庚戌年及第第三甲、其子中第五甲、徐铨授官病死诸事，终局明载可核（不成立面）。故部分成立。",
    "验收侧新登记：自 R91 起承接本 R90 标注：按「年命上神卡面未给、basis 已自承该路无据不报；盘体锚点俱载、终局明载，部分成立」登记；金标原文照录不改。",
    "新登记（R90，验收侧 basis 自报定案）", acc("DA-059"), ["验收盲测席"])

add("H32O-1bf143d2", "DA-062", "部分成立",
    "验收盲测席 basis 自报：行年上神卡面未给（前程以行年为主，该路无据）",
    "回原卡逐字核——卡面 subject 载「邵二十一公之孙（丁亥生，二十二岁）」，anchors 载 asked_at／课名／天盘／四课／三传，无行年上神字段，行年一路上神未给属实（成立面）；R90 验收 prediction basis 逐字自承「前程以行年为主，卡面未给行年上神，该路明写无据」、只据三传官父链立论；金标 outcome_record 逐字载其孙患遗泄、壬子年十二月亡诸事，终局明载可核（不成立面）。故部分成立。",
    "验收侧新登记：自 R91 起承接本 R90 标注：按「行年上神卡面未给、basis 已自承该路无据；盘体锚点俱载、终局明载，部分成立」登记；金标原文照录不改。",
    "新登记（R90，验收侧 basis 自报定案）", acc("DA-062"), ["验收盲测席"])

add("H32O-ab167668", "DA-064", "部分成立",
    "验收盲测席 basis 自报：年命上神未给，该路无据",
    "回原卡逐字核——卡面 subject 载「陈学谕（辛未生，三十八岁）」，anchors 载 asked_at／课名／天盘／四课／三传，无年命上神字段，年命一路上神未给属实（成立面）；R90 验收 prediction basis 逐字自承「年命上神未给，该路无据」、只据三传立论；金标 outcome_record 逐字载其人得心病九年而卒、妻血病诸事，终局明载可核（不成立面）。故部分成立。",
    "验收侧新登记：自 R91 起承接本 R90 标注：按「年命上神卡面未给、basis 已自承该路无据；盘体锚点俱载、终局明载，部分成立」登记；金标原文照录不改。",
    "新登记（R90，验收侧 basis 自报定案）", acc("DA-064"), ["验收盲测席"])

for anon, cid, q, subj in [
    ("H32O-6cdb1eb6", "DA-059", "占前程", "徐学士（戊辰生，四十一岁）"),
    ("H32O-daafa169", "DA-060", "占赴省试", "谢省元（乙丑生，四十五岁）"),
    ("H32O-b3238cc5", "DA-061", "占子国子监试（赵公代占）", "赵公之子（己丑生，二十二岁）"),
    ("H32O-1bf143d2", "DA-062", "占孙前程", "邵二十一公之孙（丁亥生，二十二岁）"),
    ("H32O-5f9d5b17", "DA-063", "占赴任", "何知丞（丙寅生，四十三岁）"),
    ("H32O-ab167668", "DA-064", "占前程", "陈学谕（辛未生，三十八岁）"),
]:
    add(anon, cid, "不成立",
        "验收盲测席残损自报：课名底本未载（DA-059–064 同形态逐件之一）",
        f"回原卡逐字核——本例（{subj}，{q}）anchors 课名逐字作「底本未载」，卡面如实记未载；天盘／四课／三传俱全载，课名未载属原书载录形态、不构成断锚点缺口、不计 IN，照 R88 DA-051 F3 同型判例。故不成立，只登记。",
        NA, "新登记（R90，验收侧旗标定案，承 R88 DA-051 F3 同型判例）", acc(cid), ["验收盲测席"])

add("H32O-7358a085", "BY-032", "部分成立",
    "验收盲测席 basis 自报：题面未载孕妇身份与孕程，该面无据、置信已降",
    "回原卡逐字核——卡面 subject 逐字作「徐姓（占家宅）」、question 作「徐姓占家宅（孕产）」，anchors 课名（三传递生）／天盘／四课／三传俱载，但孕妇为何人、孕程均未载，身份面缺载属实（成立面）；R90 验收 prediction basis 逐字自承「题面未载孕妇身份与孕程，该面无据、置信已降」、只就子孙胎面立论；金标 outcome_record 逐字载「果是六月小产复孕未冲丑腹故也。」，终局明载可核（不成立面）。故部分成立。",
    "验收侧新登记：自 R91 起承接本 R90 标注：按「孕妇身份与孕程卡面未载、basis 已自承该面无据并降置信；课盘锚点俱载、终局明载，部分成立」登记；金标原文照录不改。",
    "新登记（R90，验收侧 basis 自报定案）", acc("BY-032"), ["验收盲测席"])

add("H32O-391c6db0", "BY-033", "部分成立",
    "验收盲测席 basis 自报：本命行年卡面未给，年龄坐标无据",
    "回原卡逐字核——卡面 subject 逐字作「梁姓（占终身）」，未载生年与年龄，anchors 课名（三传互克末助初财）／天盘／四课／三传俱载、无本命行年字段，本命行年未给属实（成立面）；R90 验收 prediction basis 逐字自承「本命行年卡面未给，年龄坐标无据，应期只落支年不落岁数，置信已降」；金标 outcome_record 逐字载「幼失父母，多受欺凌，中年丧妻，复娶得一子。」，终局明载可核（不成立面）。故部分成立。",
    "验收侧新登记：自 R91 起承接本 R90 标注：按「本命行年卡面未给、basis 已自承年龄坐标无据并降置信；课盘锚点俱载、终局明载，部分成立」登记；金标原文照录不改。",
    "新登记（R90，验收侧 basis 自报定案）", acc("BY-033"), ["验收盲测席"])

add("H32O-43703c8a", "WHY-071", "部分成立",
    "验收盲测席自报：病名层级限度——金标 outcome 只验癌种、生死终局层级未载",
    "回 holdout32 金标逐字核——outcome_record 逐字作「应验情况：其母果然是食道癌（最后结果如何，因没再见此人面，不得而知）」：病名（癌种）层级有应验载述，母病生死终局层级明载不得而知、未载，限度一层属实（成立面）；但病名层级本身明载可核、金标 grade_note 明载结局与原书应验情况核对相合（不成立面）。故部分成立（验收面不入 dev 层、只登记）。",
    "验收侧新登记：自 R91 起承接本 R90 标注：按「金标 outcome 病名（食道癌）层级明载、生死终局层级明载不得而知未载，部分成立」登记；金标原文照录不改。",
    "新登记（R90，验收侧旗标定案）", acc("WHY-071"), ["验收盲测席"])

WHYQ = [
    ("H32O-e556d890", "WHY-070", "测叔叔病之吉凶"),
    ("H32O-43703c8a", "WHY-071", "某男测母病（断癌种）"),
    ("H32O-5fe6c940", "WHY-080", "一男子求测恋爱结果如何"),
    ("H32O-b0ece1b4", "WHY-081", "一女子打电话问夫妻缘分（作者代摇）"),
    ("H32O-e7bba204", "WHY-082", "某女测夫妻缘分"),
    ("H32O-6cdcd67b", "WHY-083", "某男测与女朋友吵架分手，她还会回到身边吗"),
    ("H32O-90cd7fb3", "WHY-084", "某男（1955年生）测一生运气"),
    ("H32O-33b93bd5", "WHY-085", "某女（1962年生）测一生运气"),
    ("H32O-645e500d", "WHY-086", "某男（1957年生）测一生运气"),
    ("H32O-a7278c48", "WHY-087", "某女（1961年生）测一生运气"),
    ("H32O-f50f2a57", "WHY-088", "某男（1962年生）测一生运气"),
    ("H32O-2f0229c1", "WHY-089", "某女测本年年运"),
    ("H32O-c5665410", "WHY-090", "某出租车司机测年运"),
    ("H32O-66616b38", "WHY-091", "某男测年运"),
]
for anon, cid, q in WHYQ:
    add(anon, cid, "部分成立",
        "验收盲测席残损自报：台账 subject 空缺（卡面自注，WHY 全例同形态逐件之一）",
        f"回原卡逐字核——卡面 subject 逐字作「求测者（台账 subject 为空、原书未具名）」，台账 subject 空缺一层属实（成立面）；但卡面自注已明载此节，question／context 明载所问（本例：{q}），anchors 卦面锚点（asked_at／本卦／变卦／动爻／逐爻）俱载，金标 outcome_record 终局明载可核（不成立面）。故部分成立。本条为 WHY 全例（14 例）同形态逐件登记之一，与本例其余旨（若有）并行不悖。",
        f"验收侧新登记：自 R91 起承接本 R90 标注：按「台账 subject 空缺卡面已自注、所问与卦面锚点俱载、终局明载，部分成立（WHY 全例同形态）」登记；金标原文照录不改。",
        "新登记（R90，验收侧 basis 自报定案，WHY 全例同形态逐件登记）", acc(cid), ["验收盲测席"])

# ---------------- assertions on sources ----------------
def txt(p):
    return (P3 / p).read_text(encoding="utf-8")
assert "tradition': 'horary'" in txt("inputs-dev12/AS-009.json") or '"tradition": "horary"' in txt("inputs-dev12/AS-009.json")
for cid in ["DA-059", "DA-060", "DA-061", "DA-062", "DA-063", "DA-064"]:
    assert "底本未载" in txt(f"holdout32/inputs/{cid}.json"), cid
for _, cid, _ in WHYQ:
    assert "台账 subject 为空" in txt(f"holdout32/inputs/{cid}.json"), cid
gold = txt("holdout32/test_gold.jsonl")
for s in ["其他断语也皆符合实际情况", "以上判断全部正确", "所断皆验，后俩人和好", "其说亦准", "最后结果如何，因没再见此人面，不得而知"]:
    assert s in gold, s

assert len(E) == 41, len(E)
from collections import Counter
c = Counter(e["disposition"] for e in E)
assert c == {"部分成立": 31, "不成立": 10}, c

specials = ann89["special_checks"] + [
    {"item": "（R90）特别核查75：R89 附则承接对勘——平台面 _r89 层 6 件落实验合与 AS-009 承接注记",
     "conclusion": "runs/round90/judging/outcome-manifest.json 新层 _r89_carryover_notes_addendum 6 件（LY-525／LY-527／LY-529／LY-530／LY-532／LY-538）逐件与 data/case-annotations-r89.json 对应条 manifest_carry_suggestion 全文逐字全等（落盘脚本逐件断言全过）：落实 6／维持 0／订正 0，出入 0 件。注：该层实在 manifest 件、非 kb-snapshot（kb-snapshot 为 method 21 文件快照、无注记层），任务二所指 manifest 层文件以此件为准据登记。AS-009 承接注记：本轮新定案部分成立一条之 manifest_carry_suggestion 已按「卡面实载 tradition＝horary、注记须以实载值回写」形态写定，自 R91 manifest 起落实。",
     "evidence": "runs/round90/build_manifest_r90.py；runs/round90/judging/outcome-manifest.json _r89_carryover_notes_addendum；data/case-annotations-r89.json 六条 manifest_carry_suggestion；runs/round90/FREEZE-r90.md。",
     "scope_note": "只对勘与登记，不改 manifest 任一侧文本。"},
    {"item": "（R90）特别核查76：平台面旗标定案总登记（新定案 11 条）与承接筛检",
     "conclusion": "平台面新定案 11 条：部分成立 7（AS-009 主持裁定／AS-304／AS-306 X1／LY-518／LY-534 同盘异问／LY-626 卡面自相矛盾新旨／LR3-010 UNC）、不成立 4（BZ-032 X3／LY-017／LY-034／LY-019 作废轮 X2，均经本轮 basis 首行逐件回读）。承接筛检（同旨已在册、不重复立条）：AS-301／AS-302／AS-303／AS-305／AS-307 盘面缺载（在册 R86 条）、AS-304／AS-306 盘面缺载面（在册 R86 条，本轮新条只裁归属／行运表述旨）、BQ-001 与 BQ-010–BQ-024 chart_complete=false 及注家同人多卡形态（在册 R86 条逐件在册；BQ-002–009 不在本轮平台集、无本轮 prediction）、BZ-301／BZ-302 无四柱（在册 R86 条）、LY-036 无盘面栏（在册 R75 条同旨）、LY-626 OCR 旨（在册 R86 条）、OC-009 四柱缺载（在册 R81 条）。AS-307 双条并行续行、本轮不立第三条（本轮 basis 首行已逐字照录卡面 tradition＝astrology、无新旗标旨）。",
     "evidence": "runs/round90/FREEZE-r90.md；runs/round90/predictions 逐件 basis；inputs-dev12 逐件原卡；data/case-annotations-r89.json 在册各条。",
     "scope_note": "结论只及标注与承接建议，不改分数。"},
    {"item": "（R90）特别核查77：验收面（holdout32 开封）旗标定案总登记（新定案 30 条）",
     "conclusion": "本轮平台三项全立（final-scores analysis_r90 platform：(a) -0.991 立／(b) 四护栏全立／(c) -1.707 立、all_stand=true），holdout32 已开封验收，验收面新定案 30 条：部分成立 24（O2 outcome 粒度 4：WHY-085／WHY-091／WHY-083／BY-031；年命／行年／身份面自报 6：DA-059／DA-062／DA-064／BY-032／BY-033／WHY-071 病名层级；WHY 全例台账 subject 空缺 14）、不成立 6（DA-059–064 课名底本未载，承 R88 DA-051 F3 判例）。验收面部分成立件照 R83 判例不入 dev 层、只登记。holdout33 封存待开封（本轮不开封）。",
     "evidence": "runs/round90/final-scores.json analysis_r90.platform；holdout32/test_gold.jsonl 逐件 outcome 原文；holdout32/inputs 逐件原卡；runs/round90/acceptance/predictions 逐件 basis；runs/round90/acceptance/judging/host-mapping.json。",
     "scope_note": "结论只及标注与承接建议，不改验收分数与金标原文。"},
    {"item": "（R90）特别核查78：指令性字样基线六处复核",
     "conclusion": "基线六处经 R90 盘上逐处回读在册、形态未变，出入 0 处：cases 本体四例（BZ-036「盲测比对须注」／BZ-042「（盲测比对时以格局大富一项为主）」／BZ-105「使用时须分开统计」／LY-204 旧注层「勿以此斷」）于 runs/round90/judging/outcome-manifest.json 在场；LR2-016 manifest editor_note 一处于 _r56_lr2016_split 分列层逐字在场；评审包 editor_note 层一处于 packetB.json 与 packet3.json 以独立 editor_note 字段逐字在场（anon P3-9d74d730）。本轮新增同型件：无。只登记、不改文本。",
     "evidence": "runs/round90/judging/outcome-manifest.json cases 与 _r56_lr2016_split；runs/round90/judging/packetB.json／packet3.json editor_note 字段；runs/round90/judging/host-mapping.json。",
     "scope_note": "各席一律按数据处理、不作指令。"},
    {"item": "（R90）特别核查79：待核四件维持与 CZ-QX 维持 16",
     "conclusion": "待核四件维持原状、不核查不关闭：BZ-029（俞大维卒年＋旗标错配线索，无新证据）、BZ-040（许世英享年，无新证据）、LY-537（「申予日」衍字疑，以未核条目随承接在册；R89 已并记 X3 旗标 anon 与本例同例事实，本轮无新史源、维持未核）、YM-070（「甲寅旬」出处待核并「都下」语义未明，以未核条目随承接在册）。CZ-QX 维持 16：holdout32 无测字例、同档计数不变，只登记。",
     "evidence": "data/case-annotations-r89.json LY-537／YM-070 未核条承接；data/manifest-carryover-r89-addendum.md §五.3；PREREG-r90 §2（CZ-QX 本集无测字例）。",
     "scope_note": "无盘外独立史源不裁。"},
    {"item": "（R90）特别核查80：紫微供给工序排期承接登记、并集与已用数登记",
     "conclusion": "紫微工序排期照 PREREG-r90 §5 裁定（甲）主路径转录登记（承接于 manifest-carryover-r90-addendum §六）：自 R91 起首批 #1 天纪定点复核＋#2 许铨仁《钦天四化》定点转录（书 p.26–27），次批 #3 徐曾生续 OCR，再次批 #6 陆在田＋#5 许铨仁《命理学正解》，殿后 #4 蔡明宏普查；工序量附估承 manifest-carryover-r89-addendum §六不改估；h34 组集判据＝紫微面实测 eligible≥9。本轮只作排期承接登记、不抢跑。并集与已用数：已用并集 1304（PREREG-r90 开轮主持复算、与 R89 封存 holdout33 后登记逐值相符）；holdout32 已开封、标已用；holdout33 封存待开封（最早 R91 全立轮）。CYJ fidelity 例外 46 件只登记、不充 eligible。",
     "evidence": "runs/round90/PREREG.md §5／§0 开轮登记；data/manifest-carryover-r89-addendum.md §六；data/holdout33-seal-log.md。",
     "scope_note": "只登记排期与台账数，不预支例数、不立项（丙）。"},
]

out = {
    "_provenance": "R90 数据席（旗标定案流水与承接登记，独立席位，不兼任本轮盲测／评审／诊断／组集／修订，不改方法、不动分数）：以 data/case-annotations-r89.json 为底承接全量 321 件（成立 14／部分成立 244／不成立 61／未核 2），前 321 件逐件原样、无删改（落盘脚本全等断言验过）；承接对勘：R90 manifest 新层 _r89_carryover_notes_addendum 6 件（LY-525／LY-527／LY-529／LY-530／LY-532／LY-538）逐件与 r89 条 manifest_carry_suggestion 全文逐字全等、出入 0 件；_r82 层 3 件已经 R85 主持裁定结案、不再滚动对勘、只作在册登记。本轮平台三项全立（analysis_r90：(a) -0.991／(c) -1.707、all_stand=true），holdout32 已开封验收。本轮新定案 41 条：平台面 11（部分成立 7：AS-009／AS-304／AS-306／LY-518／LY-534／LY-626／LR3-010；不成立 4：BZ-032／LY-017／LY-034／LY-019），验收面 30（部分成立 24：WHY-085／WHY-091／WHY-083／BY-031／DA-059／DA-062／DA-064／BY-032／BY-033／WHY-071 及 WHY 全例台账 subject 空缺 14 件；不成立 6：DA-059–064 课名底本未载，承 R88 DA-051 F3 判例）；合计 362 件（成立 14／部分成立 275／不成立 71／未核 2）。基线六处 R90 盘上复核在册、形态未变；CZ-QX 维持 16；待核四件维持（LY-537 并记 X3 旗标同例、维持未核）；CYJ fidelity 例外 46 件只登记；AS-307 双条并行保留、不合并、本轮不立第三条；紫微工序排期照 PREREG-r90 §5（甲）转录登记、附估承 r89 附则 §六不改估；已用并集 1304、holdout32 已用、holdout33 封存待开封。",
    "round": 90,
    "annotations": base + E,
    "special_checks": specials,
    "counts": {
        "base_file": "data/case-annotations-r89.json",
        "base_cases_total": 321,
        "base_verdicts": {"成立": 14, "部分成立": 244, "不成立": 61, "未核": 2},
        "carryover_check_r89_addendum": {
            "platform_layer": "_r89_carryover_notes_addendum",
            "platform_items": 6,
            "platform_ids": ["LY-525", "LY-527", "LY-529", "LY-530", "LY-532", "LY-538"],
            "platform_result": "逐件与 r89 条 manifest_carry_suggestion 全文逐字全等，落实 6／出入 0（层实在 runs/round90/judging/outcome-manifest.json；kb-snapshot 为 method 快照、无注记层）",
            "acceptance_items_r89": 0,
            "acceptance_status": "R89 验收面无新定案（h32 未开封），只登记",
        },
        "carryover_check_r82_closed": {"layer": "_r82_carryover_notes_addendum", "items": 3,
            "status": "已经 R85 主持裁定结案，R90 只作在册登记、不再滚动对勘"},
        "new_registrations_r90": 41,
        "new_cases_r90": {
            "部分成立_platform": ["AS-009", "AS-304", "AS-306", "LY-518", "LY-534", "LY-626", "LR3-010"],
            "不成立_platform": ["BZ-032", "LY-017", "LY-034", "LY-019"],
            "部分成立_acceptance": ["WHY-085", "WHY-091", "WHY-083", "BY-031", "DA-059", "DA-062", "DA-064", "BY-032", "BY-033", "WHY-071",
                                     "WHY-070", "WHY-071", "WHY-080", "WHY-081", "WHY-082", "WHY-083", "WHY-084", "WHY-085", "WHY-086", "WHY-087", "WHY-088", "WHY-089", "WHY-090", "WHY-091"],
            "不成立_acceptance": ["DA-059", "DA-060", "DA-061", "DA-062", "DA-063", "DA-064"],
        },
        "r90_partial_upheld_platform": ["AS-009", "AS-304", "AS-306", "LY-518", "LY-534", "LY-626", "LR3-010"],
        "r90_partial_upheld_acceptance": ["WHY-085", "WHY-091", "WHY-083", "BY-031", "DA-059", "DA-062", "DA-064", "BY-032", "BY-033", "WHY-071",
                                           "WHY-070", "WHY-080", "WHY-081", "WHY-082", "WHY-084", "WHY-086", "WHY-087", "WHY-088", "WHY-089", "WHY-090"],
        "acceptance_side_r90": "holdout32 已开封（平台三项全立），验收面新定案 30 条（部分成立 24／不成立 6），部分成立件照 R83 判例不入 dev 层、只登记；holdout33 封存待开封",
        "baseline_instructional_strings": {"items": 6, "result": "R90 盘上逐处在册、形态未变，出入 0 处"},
        "czqx_same_tier_count": 16,
        "as307_double_entry": "R80 部分成立条与 R85 不成立条并行保留、不合并；R90 无 AS-307 新旗标旨、不另立第三条",
        "pending_four": "BZ-029／BZ-040／LY-537／YM-070 维持原状；LY-537 经 R89 对勘：X3 旗标即 LY-537 同例、并记于在册未核条，维持未核",
        "used_union": 1304,
        "cases_total": 362,
        "verdicts": {"成立": 14, "部分成立": 275, "不成立": 71, "未核": 2},
    },
}

OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
back = json.loads(OUT.read_text(encoding="utf-8"))
assert back["annotations"][:321] == base
assert len(back["annotations"]) == 362
assert Counter(a["disposition"] for a in back["annotations"]) == {"成立": 14, "部分成立": 275, "不成立": 71, "未核": 2}
assert len(back["special_checks"]) == 80
for a in back["annotations"][321:]:
    assert a["registered_round"] == 90 and a["finding"] and a["flag"] and a["manifest_carry_suggestion"]
print("written", OUT, OUT.stat().st_size, "bytes; new", len(E), Counter(e["disposition"] for e in E))
