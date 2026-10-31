#!/usr/bin/env python3
# R89 数据席落盘脚本：case-annotations-r89.json（承 r88 全量 309 件原样 + 本轮新定案 12 条）
# 引文逐字断言内置；不改分数、不改结局原文。
import json, hashlib, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
R89 = f"{BASE}/runs/round89"

def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)

def txt(p):
    with open(p, encoding="utf-8") as f:
        return f.read()

r88 = load(f"{BASE}/data/case-annotations-r88.json")
base_anns = r88["annotations"]
assert len(base_anns) == 309, len(base_anns)
from collections import Counter
assert Counter(a["disposition"] for a in base_anns) == {"成立": 14, "部分成立": 238, "不成立": 55, "未核": 2}

man = load(f"{R89}/judging/outcome-manifest.json")
cases = man["cases"]
hm = load(f"{R89}/judging/host-mapping.json")
jx = load(f"{R89}/judging/judgeX-merged.json")
jy = load(f"{R89}/judging/judgeY-merged.json")

# ---- _r88 层 0 件断言 ----
assert man["_r88_carryover_notes_addendum"] == {}, man["_r88_carryover_notes_addendum"]
assert len(man["_r82_carryover_notes_addendum"]) == 3
assert len(man["_r87_carryover_notes_addendum"]) == 43

# ---- 基线六处逐字断言 ----
assert "盲测比对须注" in cases["BZ-036"]
assert "（盲测比对时以格局大富一项为主）" in cases["BZ-042"]
assert "使用时须分开统计" in cases["BZ-105"]
assert "勿以此斷" in cases["LY-204"]
assert man["_r56_lr2016_split"]["editor_note"] == "原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。"
lr2_anon = [k for k, v in hm.items() if v == "LR2-016"][0]
assert lr2_anon == "P3-b82b05c7"
pkt_found = False
for fn in ["packetB.json", "packet3.json"]:
    d = load(f"{R89}/judging/{fn}")
    for it in d:
        if it.get("anon_id") == lr2_anon and it.get("editor_note") == man["_r56_lr2016_split"]["editor_note"]:
            pkt_found = True
assert pkt_found

# ---- 逐件引文逐字断言 ----
def card(cid):
    return load(f"{BASE}/inputs-dev12/{cid}.json")

def pred(cid):
    return load(f"{R89}/predictions/{cid}.json")

# LY-013
assert cases["LY-013"] == "果於次日大愈"
assert "结局时点字形残损" in jy["P3-a2fd9650"]["reason"]
# LR3-008
assert cases["LR3-008"] == "次年冬，推补兵部车驾司。"
assert "辛巳年" in card("LR3-008")["context"]["asked_at"]
assert "干支年未明" in jy["P3-27e0ad9b"]["reason"]
# LY-237
assert cases["LY-237"].startswith("果於出空之日見官")
assert "干支未明" in jy["P3-12faf09a"]["reason"]
# LR3-114
assert "半夜闻鸦鸣，此鸣主何吉凶" in card("LR3-114")["context"]["question"]
assert cases["LR3-114"].startswith("其时亥时右邻木客已被劫")
assert "对象错位" in jy["P3-ac8bd20e"]["reason"]
# BZ-021
c = card("BZ-021")
assert "tradition" not in c and "system" not in c
assert pred("BZ-021")["basis"].startswith("卡面未标注 tradition 字段")
# OC-019
c = card("OC-019")
assert "tradition" not in c and "system" not in c
assert pred("OC-019")["basis"].startswith("卡面未标注 tradition 字段")
assert "检查器误报" in txt(f"{R89}/FREEZE-r89.md") and "OC-019" in txt(f"{R89}/FREEZE-r89.md")
# LY-537 (d)
assert cases["LY-537"] == "果于申予日归"
assert hm["P3-b97286e0"] == "LY-537"
assert "申日" in jx["P3-b97286e0"]["reason"] and "申日" in jy["P3-b97286e0"]["reason"]
# LY-525
assert "月建記載不全" in card("LY-525")["context"]["asked_at"]
assert "月建记载不全" in pred("LY-525")["basis"]
assert cases["LY-525"] == "服之便醒﹐"
# LY-527
assert len(card("LY-527")["context"]["attachments"]["chart_lines_top_to_bottom"]) == 12
assert "一例两占" in pred("LY-527")["prediction_text"] or "一例並錄兩占" in pred("LY-527")["basis"] or "一例并录两占" in pred("LY-527")["basis"]
# LY-532
assert "六神栏缺载" in pred("LY-532")["basis"] or "六神欄缺載" in pred("LY-532")["basis"] or "卡面未载六神" in pred("LY-532")["basis"]
assert cases["LY-532"].startswith("后果死于戌月丁亥日")
# LY-538
assert "兌宮" in json.dumps(card("LY-538"), ensure_ascii=False)
assert "宫位括注" in pred("LY-538")["basis"] or "宮位括注" in pred("LY-538")["basis"]
# LY-529 / LY-530
for cid in ["LY-529", "LY-530"]:
    assert "OCR 轉錄後行序錯亂" in card(cid)["context"]["attachments"]["chart_note"]
assert "OCR转录行序曾乱" in pred("LY-529")["basis"] or "OCR轉錄行序" in pred("LY-529")["basis"]

SRC = "divination/benchmark/phase3/"
def sc(cid, *extra):
    out = [f"{SRC}inputs-dev12/{cid}.json",
           f"{SRC}runs/round89/judging/outcome-manifest.json cases[{cid}]",
           f"{SRC}runs/round89/predictions/{cid}.json"]
    out.extend(extra)
    return out

JUDGE = [f"{SRC}runs/round89/judging/judgeX-merged.json", f"{SRC}runs/round89/judging/judgeY-merged.json",
         f"{SRC}runs/round89/judging/host-mapping.json", f"{SRC}runs/round89/final-scores.json"]

new = [
 {
  "anon_id": "P3-a2fd9650", "case_id": "LY-013", "disposition": "不成立",
  "flag": "judgeY：结局时点字形残损，结局无可核时点（X 席同例 reason 仅及断语戌日坐标无从核、未及字形）",
  "finding": "回原卡与结局原文逐字核——R89 manifest 结局逐字作「果於次日大愈」，全文无残损字形、无替换字符，时点以「次日」相对载述（原书载录形态）；卡面 asked_at「申月戊辰日」在场，终局（夫病大愈）明载可核。旗标所称「字形残损」于结局原文无据；「无可核干支时点」属原文相对载述、非文本残损。故旗标不成立，只登记。来源席数 1（judgeY）。",
  "manifest_carry_suggestion": "只登记不入层：自 R90 起承接本 R89 标注（不成立＝结局无字形残损、「次日」为原文相对载述，不入 _r89_carryover_notes_addendum 承接层）；结局原文照录不改。",
  "relation": "新立（R89 平台评审旗标定案）",
  "registered_round": 89,
  "sources_checked": sc("LY-013", *JUDGE),
  "source_seats": ["judgeY"]
 },
 {
  "anon_id": "P3-27e0ad9b", "case_id": "LR3-008", "disposition": "不成立",
  "flag": "judgeY：结局仅载次年冬、干支年未明，巳年无从核",
  "finding": "回原卡与结局原文逐字核——R89 manifest 结局逐字作「次年冬，推补兵部车驾司。」，终局（次年冬推补兵部车驾司）明载；「次年」为相对纪年，卡面 asked_at 逐字载「辛巳年（1641）十月己未日癸酉时」，相对纪年可由卡面年柱锚定，非干支缺载。属原书载录形态、不构成断锚点缺口（承 WHY-068／WHY-069 年柱未载 R88 不成立判例）。故旗标不成立，只登记。来源席数 1（judgeY）。",
  "manifest_carry_suggestion": "只登记不入层：自 R90 起承接本 R89 标注（不成立＝相对纪年可由卡面年柱锚定、终局明载，不入 _r89_carryover_notes_addendum 承接层）；结局原文照录不改。",
  "relation": "新立（R89 平台评审旗标定案）",
  "registered_round": 89,
  "sources_checked": sc("LR3-008", *JUDGE),
  "source_seats": ["judgeY"]
 },
 {
  "anon_id": "P3-12faf09a", "case_id": "LY-237", "disposition": "不成立",
  "flag": "judgeY：结局仅载出空之日、干支未明，结局无可核时点",
  "finding": "回原卡与结局原文逐字核——R89 manifest 结局逐字载「果於出空之日見官﹐財利得意﹐……」，终局（见官、财利得意）明载可核，其后「月建財爻生世之故耳……」为原书断后释理并载、非结局缺位；「出空之日」未具名干支属原书载录形态，卡面 asked_at「申月丁卯日」与卦面旬空在场，出空可据盘面推步、非数据缺损。故旗标不成立，只登记。来源席数 1（judgeY）。",
  "manifest_carry_suggestion": "只登记不入层：自 R90 起承接本 R89 标注（不成立＝「出空之日」为原文载述、终局明载，不入 _r89_carryover_notes_addendum 承接层）；结局原文照录不改。",
  "relation": "新立（R89 平台评审旗标定案）",
  "registered_round": 89,
  "sources_checked": sc("LY-237", *JUDGE),
  "source_seats": ["judgeY"]
 },
 {
  "anon_id": "P3-ac8bd20e", "case_id": "LR3-114", "disposition": "不成立",
  "flag": "judgeY：断对象为庵中防失物、实为邻人及北关门外，对象错位",
  "finding": "回原卡与结局原文逐字核——原卡所问逐字作「半夜闻鸦鸣，此鸣主何吉凶？」，问面为鸦鸣吉凶通问、未限定庵中失物；R89 manifest 结局逐字载「其时亥时右邻木客已被劫（邻人被劫一节当场证实）；果次日北关门外行劫，遂获二名。」——邻人被劫与次日行劫获犯即鸦鸣凶应之应验记载，结局对象与问面对应、无错位；「庵中防失物」系我方 prediction 断面取舍，属评分面、非数据瑕疵。故旗标不成立，只登记。来源席数 1（judgeY）。",
  "manifest_carry_suggestion": "只登记不入层：自 R90 起承接本 R89 标注（不成立＝结局应验对象与鸦鸣吉凶问面对应、错位系断面取舍属评分面，不入 _r89_carryover_notes_addendum 承接层）；结局原文照录不改。",
  "relation": "新立（R89 平台评审旗标定案）",
  "registered_round": 89,
  "sources_checked": sc("LR3-114", *JUDGE),
  "source_seats": ["judgeY"]
 },
 {
  "anon_id": "P3-8bf37a5f", "case_id": "BZ-021", "disposition": "不成立",
  "flag": "主持检查器 tradition 旗标（R89）：卡面 tradition 虚称候选——承主持回读裁定登记",
  "finding": "主持裁定件（本席只承接登记、不重裁）：主持已回读裁定不成立——卡面确无 tradition/system 字段、R89 prediction 首行如实写未标注。本席盘上复核：inputs-dev12/BZ-021.json 顶层键仅 id／source_id／subject／context／provenance／language，无 tradition/system 字段；R89 prediction basis 首行逐字作「卡面未标注 tradition 字段，按题面体裁自决（八字）」，如实写明未标注、无虚称；实际作断体系为八字、与题面体裁一致。故旗标不成立。与在册 R87 条（R87 轮 prediction 首行虚称、部分成立）为各轮独立事件、并行不悖，本条不改 R87 定案。",
  "manifest_carry_suggestion": "只登记不入层：自 R90 起承接本 R89 标注（不成立＝R89 首行如实写未标注、无虚称，不入 _r89_carryover_notes_addendum 承接层）；结局原文照录不改。",
  "relation": "新立（R89 主持裁定件，与 R87 部分成立条并行）",
  "registered_round": 89,
  "sources_checked": sc("BZ-021", f"{SRC}runs/round89/FREEZE-r89.md（主持复核体例承接）"),
  "source_seats": ["主持检查器／主持回读裁定（R89）"]
 },
 {
  "anon_id": "P3-06a0a7bf", "case_id": "OC-019", "disposition": "不成立",
  "flag": "主持检查器 tradition 旗标候选（FREEZE-r89）：kind=card_no_field_but_first_line_claims_card_value",
  "finding": "主持裁定件（FREEZE-r89 已裁定、本席只承接登记、不重裁）：裁定逐字要旨——「输入卡无 tradition/system 字段，basis 首行明写『卡面未标注 tradition 字段，本例据卡面四柱以八字自决』，检查器命中之『卡面所载』字面系指卡面所载四柱（癸巳丙辰壬申癸卯），非 tradition 值声称。裁定：检查器误报，旗标不成立，不作废、不重测」（承 R74/R78 检查器误报判例）。本席盘上复核：inputs-dev12/OC-019.json 无 tradition/system 字段，R89 prediction basis 首行与裁定所载合。故不成立。与在册 R84 条（同例同型检查器误报、不成立）并行。",
  "manifest_carry_suggestion": "只登记不入层：自 R90 起承接本 R89 标注（不成立＝检查器误报，不入 _r89_carryover_notes_addendum 承接层）；结局原文照录不改。",
  "relation": "新立（R89 主持裁定件，与 R84 不成立条并行）",
  "registered_round": 89,
  "sources_checked": sc("OC-019", f"{SRC}runs/round89/FREEZE-r89.md"),
  "source_seats": ["主持检查器（FREEZE-r89）"]
 },
 {
  "anon_id": "P3-4c27573a", "case_id": "LY-525", "disposition": "部分成立",
  "flag": "B15+B16 席 basis 自报：卡面残损——月建缺载（asked_at 作「亥日辛酉日（原文如此，月建記載不全）」），旺衰只据日辰立论、置信下调",
  "finding": "逐件回读原卡核实——卡面 asked_at 逐字作「亥日辛酉日（原文如此，月建記載不全）」，月建缺载属实；R89 prediction basis 逐字载残损注明、只据日辰与卦内生克立论、不臆补月建，处置与卡面自注一致。R89 manifest 结局逐字载「服之便醒﹐」，服丸见醒之终局明载可核（逗号收尾一层属在册 R79 条旧旨、不重裁）。故部分成立。与在册 R87 条（同旨：卡面月建记载不全）同旨并行，本条为 R89 轮 basis 再留痕之独立登记。",
  "manifest_carry_suggestion": "新登记：自 R90 起承接本 R89 标注：按「卡面月建记载不全（asked_at 原文自注）、旺衰缺月建一维已自注、只据日辰立论；终局明载，部分成立」登记；结局原文照录不改。",
  "relation": "同旨并行（R87 同旨条并行，R89 basis 再留痕）",
  "registered_round": 89,
  "sources_checked": sc("LY-525"),
  "source_seats": ["B15+B16 平台盲测席 basis 留痕", "R89 数据席回读原卡"]
 },
 {
  "anon_id": "P3-d0401c48", "case_id": "LY-527", "disposition": "部分成立",
  "flag": "B15+B16 席 basis 自报：卡面一例两占——初占火天大有之乾为天、再占雷泽归妹之雷地豫，moving_lines 栏跨两卦并记，置信下调",
  "finding": "逐件回读原卡核实——卡面 hexagram 逐字并载初占与再占两卦，chart_lines_top_to_bottom 十二行两占并载、moving_lines 三动分属两占，一例两占与动爻栏跨卦并记属实；R89 prediction basis 逐字注明并按逐爻表分卦还原作断。R89 manifest 结局载照壁大树宅形一面与「果中經魁」功名一面，分占终局明载可核。故部分成立。与在册 R86 条（同旨：两占合卡、盘面十二行混列）同旨并行，本条为 R89 轮 basis 再留痕之独立登记。",
  "manifest_carry_suggestion": "新登记：自 R90 起承接本 R89 标注：按「一例两占、动爻栏跨两卦并记已注明并按逐爻表分卦还原；分占终局明载，部分成立」登记；结局原文照录不改。",
  "relation": "同旨并行（R86 同旨条并行，R89 basis 再留痕）",
  "registered_round": 89,
  "sources_checked": sc("LY-527"),
  "source_seats": ["B15+B16 平台盲测席 basis 留痕", "R89 数据席回读原卡"]
 },
 {
  "anon_id": "P3-225bde06", "case_id": "LY-532", "disposition": "部分成立",
  "flag": "B15+B16 席 basis 自报：卡面残损——六神栏缺载，病位六神路只据日干推得一类不确、记缺路并降置信",
  "finding": "逐件回读原卡核实——卡面 chart_lines_top_to_bottom 逐爻仅载六亲、地支五行、爻象与世应，无六神栏，六神缺载属实；R89 prediction basis 病位复核逐字载「卡面未载六神（残损：六神栏缺载……不以六神定病位、记缺路并降置信）」，处置如实。但逐爻六亲／地支／世应／动爻俱载，R89 manifest 结局逐字载「后果死于戌月丁亥日，应戌月者世入墓之月也，亥日者，克冲之日也」，终局明载可核。故部分成立。本例历轮无条目、新立。",
  "manifest_carry_suggestion": "新登记：自 R90 起承接本 R89 标注：按「卡面六神栏缺载已自注、病位六神路记缺路；逐爻锚点俱载、终局明载，部分成立」登记；结局原文照录不改。",
  "relation": "新立（R89 平台 basis 留痕定案）",
  "registered_round": 89,
  "sources_checked": sc("LY-532"),
  "source_seats": ["B15+B16 平台盲测席 basis 留痕", "R89 数据席回读原卡"]
 },
 {
  "anon_id": "P3-4bdffa4c", "case_id": "LY-538", "disposition": "部分成立",
  "flag": "B15+B16 席 basis 自报：卡面宫位括注出入——卦名括注（兑宫）与世应不合、原书按震宫五世装，逐爻六亲与世应照卡面直载立论",
  "finding": "逐件回读原卡核实——卡面 hexagram 逐字作「水風井之風澤中孚（兌宮，空亡戌亥）」，卡面 notes「palace字段出入」逐字载 inputs8 卦名括注作「兌宮」、与原书装卦表世应（世在五爻、应在二爻，震宫五世）不合，括注出入属实；R89 prediction basis 逐字注明出入、按逐爻六亲与世应直载立论、不据宫名。R89 manifest 结局与在册 R79 条所核文本一致、仕途终局可读（结局层旧旨不重裁）。故部分成立。与在册 R86 条（同旨：宫位标注出入）同旨并行，本条为 R89 轮 basis 再留痕之独立登记。",
  "manifest_carry_suggestion": "新登记：自 R90 起承接本 R89 标注：按「宫位括注出入（兑宫括注与震宫五世不合）卡面已自注、按世应原样作断；仕途终局可读，部分成立」登记；结局原文照录不改。",
  "relation": "同旨并行（R86 同旨条并行，R89 basis 再留痕；与 R79 结局层条各旨独立）",
  "registered_round": 89,
  "sources_checked": sc("LY-538"),
  "source_seats": ["B15+B16 平台盲测席 basis 留痕", "R89 数据席回读原卡"]
 },
 {
  "anon_id": "P3-17ae815b", "case_id": "LY-529", "disposition": "部分成立",
  "flag": "B15+B16 席 basis 自报：卡面 chart_note 自注逐爻表经 OCR 转录行序曾乱、本条以卦名宫位互证为准，残损轻、已注明",
  "finding": "逐件回读原卡核实——卡面 chart_note 逐字作「在線本裝卦表為雙欄排版經 OCR 轉錄後行序錯亂，逐爻裝卦未能可靠還原；本條只錄可由卦名、卦宮、空亡與斷語互證的信息，逐爻表不錄。」，OCR 行序自注属实；卡面 notes.completion_grade 载逐爻表已经原书装卦表直载补录（书页199／PDF页214）、互证可还原，R89 prediction basis 逐字载明此节并据补录逐爻表立论。R89 manifest 结局逐字载「一一皆是，葬后未出三年，二子皆发科甲．」，终局明载可核。故部分成立。与在册 R75 条（结局总承张力旨）各旨独立、并行不悖。",
  "manifest_carry_suggestion": "新登记：自 R90 起承接本 R89 标注：按「卡面自注 OCR 转录行序曾乱、逐爻表已经原书直载补录互证；终局明载，部分成立」登记；结局原文照录不改。",
  "relation": "同例新旨（R75 结局层旧旨并行）",
  "registered_round": 89,
  "sources_checked": sc("LY-529"),
  "source_seats": ["B15+B16 平台盲测席 basis 留痕", "R89 数据席回读原卡"]
 },
 {
  "anon_id": "P3-9f674377", "case_id": "LY-530", "disposition": "部分成立",
  "flag": "B15+B16 席自报关联件：卡面 chart_note 自注逐爻表经 OCR 转录行序错乱（与 LY-529 同源同形态）",
  "finding": "逐件回读原卡核实——卡面 chart_note 逐字作「在線本裝卦表為雙欄排版經 OCR 轉錄後行序錯亂，逐爻裝卦未能可靠還原；本條只錄可由卦名、卦宮、空亡與斷語互證的信息，逐爻表不錄。」，OCR 行序自注属实，与 LY-529 同出《卜筮正宗》在线本同形态；卡面 notes.completion_grade 载逐爻表已经原书装卦表直载补录（书页199／PDF页214）、互证可还原，R89 prediction 据补录逐爻表立论（basis 载卡面注坤宫、逐爻六亲照卡面直载）。R89 manifest 结局逐字载「后至午月火旺克世，助土克财，财逄月破，一家数口回禄俱死．」，终局明载可核。故部分成立。本例历轮无条目、新立。",
  "manifest_carry_suggestion": "新登记：自 R90 起承接本 R89 标注：按「卡面自注 OCR 转录行序错乱、逐爻表已经原书直载补录互证；终局明载，部分成立」登记；结局原文照录不改。",
  "relation": "新立（R89 平台 basis／卡面自注定案）",
  "registered_round": 89,
  "sources_checked": sc("LY-530"),
  "source_seats": ["B15+B16 平台盲测席（同批同源件）", "R89 数据席回读原卡"]
 },
]

anns = base_anns + new
assert len(anns) == 321
verdicts = Counter(a["disposition"] for a in anns)
assert verdicts == {"成立": 14, "部分成立": 244, "不成立": 61, "未核": 2}, verdicts
# 前 309 件逐件原样断言
assert anns[:309] == base_anns
# AS-307 双条断言
assert sum(1 for a in anns if a["case_id"] == "AS-307") == 2

special = list(r88["special_checks"])
assert len(special) == 68
special += [
 {"item": "（R89）特别核查69：R88 附则承接对勘——_r88 层 0 件与验收面 3 件",
  "conclusion": "R89 manifest _r88_carryover_notes_addendum 为空集（0 件），与 R88 附则 §三「平台面本轮无新定案」逐件回读验合（断言：层在册且为空集）；R88 部分成立验收面 3 件（WHY-043／DA-051／GSZ-107）不在 dev cases、照 R83 判例不入 dev 层、只登记，DA-051 双旨并行形态照 annotations 体例续行不合并；_r82 层 3 件已经 R85 主持裁定结案，本轮不再滚动对勘、只作在册登记（R89 manifest 层实载 3 件）。",
  "evidence": "runs/round89/judging/outcome-manifest.json（_r88 层空集断言、_r82 层 3 件断言、_r89_manifest_note 同口径明载）；data/manifest-carryover-r88-addendum.md §三。",
  "scope_note": "对勘只登记、不改任一侧。"},
 {"item": "（R89）特别核查70：平台评审旗标定案总登记与筛检口径",
  "conclusion": "平台评审旗标来源＝judgeX/judgeY 双视 scores 之 reason 数据面线索（final-scores.json 只取 direction/claims/timing/total 对位）：经严格筛检（数据面专属词面：主问未载／字形残损／干支未明／对象错位／指令性字样等）得候选 33 例，逐件回原卡/结局定案——新立不成立 4 件（LY-013／LR3-008／LY-237／LR3-114）；其余候选或属既有定案同旨复触（AS-015／BQ-001／LR3-101／LY-203／LY-205／LY-206／LY-436／LY-437／LY-458／LY-504／LY-508／LY-513／LY-614／OC-026／YM-030／YM-068 等，照在册条承接、不重复立条）、或属评分面坐标/方向核验语（LR3-006／LY-234／LY-340／LY-502／LY-611／BZ-105／LY-505／MP-013 等，结局终局明载、非数据瑕疵，不立旗）、或属待核/基线在册件触及（YM-070／LR2-016，分见核查73／72）。双视 reason 中例行「某细节未载／结局无可核时点」为评分依据语、非旗标，不取。",
  "evidence": "runs/round89/judging/judgeX-merged.json 与 judgeY-merged.json 全量 reason 扫描件 runs/round89/data_seat_r89_scan3.py 及其输出；逐件回读 inputs-dev12 原卡与 outcome-manifest 结局原文（落盘脚本逐字断言）。",
  "scope_note": "筛检口径只及本轮；不改任何分数。"},
 {"item": "（R89）特别核查71：主持裁定件登记（BZ-021／OC-019）",
  "conclusion": "BZ-021 tradition 虚称旗标经主持回读裁定不成立（卡面确无 tradition/system 字段、R89 首行如实写未标注），OC-019 检查器旗标经 FREEZE-r89 裁定检查器误报、不成立；两件均已逐件入本档 annotations（不成立各 1 条），与在册 R87 BZ-021 部分成立条、R84 OC-019 不成立条各轮独立并行、不合并、不改旧条。",
  "evidence": "runs/round89/FREEZE-r89.md（OC-019 裁定原文）；inputs-dev12/BZ-021.json 与 OC-019.json 顶层字段回读；runs/round89/predictions/BZ-021.json 与 OC-019.json basis 首行逐字断言。",
  "scope_note": "主持裁定只承接登记、不重裁。"},
 {"item": "（R89）特别核查72：指令性字样特别核查基线六处复核",
  "conclusion": "基线六处经 R89 盘上逐处回读在册、形态未变，出入 0 处：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）＋LR2-016 manifest editor_note 一处（_r56_lr2016_split 分列层、原文逐字全等）＋LR2-016 评审包 editor_note 层一处（以 host-mapping 对位 anon P3-b82b05c7 定位 packetB.json 与 packet3.json、独立 editor_note 字段逐字在场、与分列层全等）。本轮 judgeY 同例 reason 明载「编者注中评分指令性字样已按数据处理不承接」，与基线处置一致、不另立新条。本轮新增同型件：无。各席一律按数据处理。",
  "evidence": "runs/round89/judging/outcome-manifest.json 与 packetB.json／packet3.json（落盘脚本逐处逐字断言全过）。",
  "scope_note": "只登记、不改任何文本。"},
 {"item": "（R89）特别核查73：待核四件维持、LY-537「申予日」对勘（X3 旗标）与 CZ-QX 维持登记",
  "conclusion": "待核四件维持原状：BZ-029／BZ-040 本轮无新证据、不入 annotations；YM-070 以未核条目在册、本轮 judgeX reason 触及（『同行都下』语义未明、与在册未核旨同旨）只登记关联；LY-537 对勘结论——judgeX block3（X3）旗标 anon P3-b97286e0 经 host-mapping 映射即 LY-537 本例，与待核件同例：R89 manifest 结局逐字作「果于申予日归」，双视 reason 均读作申日归（X『酉日与申日差一位』、Y『实申日归』），与「申予日」衍字疑同面并记于在册未核条；无盘外独立史源不裁、维持未核、不另立新条、不改其状态。CZ-QX 维持 16（本轮无测字段新结算），只登记不另行结算。",
  "evidence": "runs/round89/judging/host-mapping.json（P3-b97286e0→LY-537 断言）；outcome-manifest cases[LY-537] 逐字断言；judgeX/judgeY-merged.json 同例 reason 逐字断言。",
  "scope_note": "无盘外独立史源不裁；待核维持件只登记触及、不入裁断。"},
 {"item": "（R89）特别核查74：供给续记——紫微池挂起 6 项附估、CYJ fidelity 例外与 AS-307 双条并行续行",
  "conclusion": "紫微池挂起 6 项（ZIWEI-POOL-r84.md §四）已逐项附可行性与工序量估计，汇编于 data/manifest-carryover-r89-addendum.md §六（甲）：六项源 PDF 均在盘（incoming/wanted-books-6/Book，页数经 pdfinfo 实测），增面工序为定点复核／定点视觉转录／续 OCR 三档，例数无依据者照实记不可估。CYJ fidelity 例外 46 件照在册口径只登记、不作出路计数。AS-307 双条并行例外形态续行：R80 部分成立条与 R85 不成立条并行保留、不合并（本档 AS-307 仍恰 2 条）；本轮评审 reason 无 AS-307 数据面新旗标、不另立第三条。出路（乙）新书供给与（丙）组集限度复审各只登记一行、不展开。",
  "evidence": "runs/round84/supply/ZIWEI-POOL-r84.md §四；incoming/wanted-books-6/Book 六件 PDF 在盘与 pdfinfo 页数实测；data/case-annotations-r88.json AS-307 两条承接（落盘脚本计数断言）。",
  "scope_note": "只登记与附估，不预支、不立项。"},
]

out = {
 "_provenance": "R89 数据席（旗标定案流水与承接登记，独立席位，不兼任本轮盲测／评审／诊断／组集／修订，不改方法、不动分数）：以 data/case-annotations-r88.json 为底承接全量 309 件（成立 14／部分成立 238／不成立 55／未核 2），前 309 件逐件原样、无删改（落盘脚本全等断言验过）；承接对勘：R89 manifest 新层 _r88_carryover_notes_addendum 为 0 件（R88 平台面无新定案、与 R88 附则 §三验合），R88 部分成立验收面 3 件（WHY-043／DA-051／GSZ-107）照 R83 判例不入 dev 层只登记、DA-051 双旨并行不合并；_r82 层 3 件已经 R85 主持裁定结案、不再滚动对勘、只作在册登记；本轮新定案 12 条（平台面）：部分成立 6（LY-525／LY-527／LY-532／LY-538／LY-529／LY-530，来源＝B15+B16 席 basis 卡面残损自报，逐件回原卡核实）、不成立 6（LY-013／LR3-008／LY-237／LR3-114，来源＝平台评审双视 reason 数据面旗标线索；BZ-021／OC-019，来源＝主持检查器旗标与主持裁定）；合计 321 件（成立 14／部分成立 244／不成立 61／未核 2）。本轮平台未全立（final-scores analysis_r89：全集配对差 -1.406 破 (a) 线 -1.371、六爻 (c) -2.124 未立），holdout32 未开封，验收面本轮无新定案。基线六处 R89 盘上复核在册、形态未变；CZ-QX 维持 16；待核四件维持（LY-537 经 X3 旗标对勘同例并记、维持未核）；CYJ fidelity 例外 46 件与紫微池挂起 6 项只登记（挂起 6 项附估见附则 §六）；AS-307 双条并行保留、不合并。",
 "round": 89,
 "annotations": anns,
 "special_checks": special,
 "counts": {
  "base_file": "data/case-annotations-r88.json",
  "base_cases_total": 309,
  "base_verdicts": {"成立": 14, "部分成立": 238, "不成立": 55, "未核": 2},
  "carryover_check_r88_addendum": {
   "platform_layer": "_r88_carryover_notes_addendum",
   "platform_items": 0,
   "platform_result": "层在册且为空集，与 R88 附则 §三「平台面本轮无新定案」验合",
   "acceptance_items": 3,
   "acceptance_ids": ["WHY-043", "DA-051", "GSZ-107"],
   "acceptance_status": "不在 dev cases、不入层，照 R83 判例只在汇编件登记验收面处置；DA-051 双旨并行不合并"
  },
  "carryover_check_r82_closed": {
   "layer": "_r82_carryover_notes_addendum",
   "items": 3,
   "status": "已经 R85 主持裁定结案，R89 只作在册登记、不再滚动对勘"
  },
  "new_registrations_r89": 12,
  "new_cases_r89": {
   "部分成立_platform": ["LY-525", "LY-527", "LY-532", "LY-538", "LY-529", "LY-530"],
   "不成立_platform_judge": ["LY-013", "LR3-008", "LY-237", "LR3-114"],
   "不成立_platform_host": ["BZ-021", "OC-019"]
  },
  "r89_partial_upheld_platform": ["LY-525", "LY-527", "LY-532", "LY-538", "LY-529", "LY-530"],
  "acceptance_side_r89": "本轮平台未全立、holdout32 未开封，验收面无新定案",
  "baseline_instructional_strings": {"items": 6, "result": "R89 盘上逐处在册、形态未变，出入 0 处"},
  "czqx_same_tier_count": 16,
  "as307_double_entry": "R80 部分成立条与 R85 不成立条并行保留、不合并；R89 无新旗标涉 AS-307、不另立第三条",
  "pending_four": "BZ-029／BZ-040／LY-537／YM-070 维持原状；LY-537 经 (d) 对勘：X3 旗标 P3-b97286e0 即 LY-537 同例、并记于在册未核条，维持未核",
  "cases_total": 321,
  "verdicts": {"成立": 14, "部分成立": 244, "不成立": 61, "未核": 2}
 }
}

dest = f"{BASE}/data/case-annotations-r89.json"
with open(dest, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
# 回读断言
back = load(dest)
assert len(back["annotations"]) == 321 and back["annotations"][:309] == base_anns
assert Counter(a["disposition"] for a in back["annotations"]) == verdicts
print("OK", dest, os.path.getsize(dest), hashlib.sha256(open(dest, "rb").read()).hexdigest())
