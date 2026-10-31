#!/usr/bin/env python3
# R87 数据席落盘脚本：case-annotations-r87.json（全量承接 r86 238 件 + 本轮新定案 62 件）
# 旗标逐件回原卡/结局核读结论均已由本席逐件核定后写死于下表；本脚本只负责落盘与断言。
import json, collections
from collections import Counter

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
r86 = json.load(open(f"{BASE}/data/case-annotations-r86.json"))
anns86 = r86["annotations"]
assert len(anns86) == 238, len(anns86)
assert Counter(a["disposition"] for a in anns86) == {"成立": 14, "部分成立": 187, "不成立": 35, "未核": 2}
man87 = json.load(open(f"{BASE}/runs/round87/judging/outcome-manifest.json"))
cases87 = man87["cases"]
hm87 = json.load(open(f"{BASE}/runs/round87/judging/host-mapping.json"))
inv87 = {v: k for k, v in hm87.items()}
hma = json.load(open(f"{BASE}/runs/round87/acceptance/judging/host-mapping.json"))
inva = {v: k for k, v in hma["ours"].items()}
gold = {}
for line in open(f"{BASE}/holdout30/test_gold.jsonl"):
    g = json.loads(line)
    gold[g["id"]] = g

def outcome(cid):
    return cases87[cid]

# _r86 层落实断言：45 件平台面、文本与 r86 annotations 部分成立条 suggestion 逐件捕获验合
layer86 = man87["_r86_carryover_notes_addendum"]
assert len(layer86) == 45, len(layer86)
sugg86 = {}
for a in anns86:
    if a["registered_round"] == 86 and a["disposition"] == "部分成立":
        sugg86[a["case_id"]] = a["manifest_carry_suggestion"]
assert set(layer86) == {c for c in sugg86 if c in cases87}, (set(layer86) ^ {c for c in sugg86 if c in cases87})
for cid, txt in layer86.items():
    assert sugg86[cid].endswith(txt) or txt in sugg86[cid], cid
acc5 = sorted(c for c in sugg86 if c not in cases87)
assert acc5 == ["CYJ-001", "CYJ-002", "CYJ-004", "CYJ-005", "ZW-015"], acc5
print("r86 layer assert OK (45 platform + 5 acceptance registered)")

# _r82 层结案登记断言：3 件在册、不再滚动对勘
assert sorted(man87["_r82_carryover_notes_addendum"].keys()) == ["LY-406", "LY-446", "LY-524"]
print("r82 closed layer assert OK (3)")

# 指令性字样基线六处断言（评审包以 host-mapping 对位 LR2-016 定位 packetB.json）
for cid, kw in [("BZ-036", "盲测比对须注"), ("BZ-042", "盲测比对时以格局大富一项为主"),
                ("BZ-105", "使用时须分开统计"), ("LY-204", "勿以此斷")]:
    assert kw in cases87[cid], cid
assert "甲戌日巳时" in man87["_r56_lr2016_split"]["editor_note"]
packetB = json.load(open(f"{BASE}/runs/round87/judging/packetB.json"))
lr16 = [p for p in packetB if hm87.get(p.get("anon_id")) == "LR2-016"]
assert lr16 and "editor_note" in lr16[0] and "甲戌日巳时" in json.dumps(lr16[0], ensure_ascii=False)
print("instruction-baseline assert OK (6)")

# MP/WP 无盘面组卡面断言：context 无 attachments
for cid in ["MP-001","MP-002","MP-003","MP-004","MP-005","MP-007","MP-008","MP-009","MP-012",
            "WP-008","WP-009","WP-010","WP-011","WP-012","WP-013"]:
    card = json.load(open(f"{BASE}/inputs-dev12/{cid}.json"))
    assert not card["context"].get("attachments"), cid
print("MP/WP no-attachments assert OK (15 sampled incl. MP-012 precedent)")

# CYJ 验收金标结局逐字在场断言
for cid in ["CYJ-006","CYJ-007","CYJ-008","CYJ-009","CYJ-010"]:
    assert gold[cid]["outcome_record"], cid
    assert "课式头四要素 present" in gold[cid]["grade_note"], cid
print("CYJ gold assert OK (5)")

NEW = []

def P(cid, disp, flag, finding, carry, relation="新登记（R87，平台 basis 留痕定案）"):
    NEW.append((cid, disp, flag, finding, carry, relation, "platform"))

def A(cid, disp, flag, finding, carry, relation="新登记（R87，验收侧旗标定案）"):
    NEW.append((cid, disp, flag, finding, carry, relation, "acceptance"))

CARRY_P = "新登记：自 R88 起承接本 R87 标注：按「{g}，部分成立」登记；结局原文照录不改。"
CARRY_N = "只登记不入层：自 R88 起承接本 R87 标注（不成立，不入 _r87_carryover_notes_addendum 承接层）；结局原文照录不改。"
SYN = "同例新旨（R87，与在册旧旨并行）"

# ---------- 平台侧：FREEZE 裁定件 ----------
P("BZ-021", "部分成立",
  "FREEZE-r87 主持裁定：tradition 措辞不实——卡面无 tradition/system 字段，basis 首行虚称卡面载有该字段并逐字照录",
  "回原卡——inputs-dev12/BZ-021.json 顶层无 tradition/system 字段，basis 首行逐字作「tradition＝bazi（卡面 tradition 字段逐字照录——本卡载有 tradition 字段，值即 bazi）」，虚称一层属实；惟标示值 bazi 与本例体裁及分段口径全等、实际作断体系为八字子平、断语不受影响，无回传自相矛盾要件，照 R67 同例判例与 R80 operative 口径主持裁定部分成立、不作废不重测。R87 manifest 结局载蒋介石丙午运权位鼎盛、1975 年卒，终局明载可核。故部分成立。",
  CARRY_P.format(g="basis 首行虚称卡面载有 tradition 字段（卡面实无此字段）、标示值与体裁全等、断语不受影响"))
# ---------- 平台侧：basis 筛检部分成立 ----------
P("AS-003", "部分成立",
  "R87 平台 basis 留痕：卡面 OCR 残损——上升星座/度数原文乱码（残损类）",
  "回原卡——卡面 attachments note 逐字载「The ascending sign/degree is garbled in the 1647 OCR」，残损一层属实，席位据此未据上升度数作断；R87 manifest 结局逐字载 4 月 25 日成交、5 月 17 日付 530 镑，成交终局明载可核。故部分成立。",
  CARRY_P.format(g="上升星座/度数原文乱码已自注、未据以断；成交终局明载"))
P("AS-012", "部分成立",
  "R87 平台 basis 留痕：卡面 OCR 残损——个别行星字形 garbled（残损类）",
  "回原卡——卡面 attachments note 逐字载「Some planet glyphs are garbled in the 1647 OCR」，残损一层属实，席位据七项负面证言文字明确面作断；R87 manifest 结局载一封信件 dashed 其希望、终未得圣职，终局明载可核。故部分成立。",
  CARRY_P.format(g="个别行星字形 OCR 残损已自注、七项证言文字明确；终局明载"))
P("AS-206", "部分成立",
  "R87 平台 basis 留痕：输入残损——问日 OCR 不可读、男方显著星具体行星未明载（残损类）",
  "回原卡——卡面 asked_at 逐字作「the day is not legible in the OCR」，残损一层属实，席位据此降置信；R87 manifest 结局逐字载其人最终促成婚姻、双方满意，婚姻终局明载可核。故部分成立。",
  CARRY_P.format(g="问日 OCR 不可读、男方显著星未明载已自注；婚姻终局明载"))
P("BZ-031", "部分成立",
  "R87 平台 basis 留痕：卡面时柱两说并存——命主初报辛未、韦氏改定庚午（卡面不合类）",
  "回原卡与 basis——卡面载时柱系初报辛未、改定庚午，basis 逐字注「以改定庚午时作断，时柱存疑已降置信」，两说并存一层属实；R87 manifest 结局载邵邨人与弟创立邵氏影业王国，终局明载可核。故部分成立。",
  CARRY_P.format(g="卡面时柱初报/改定两说并存已自注、以改定作断；终局明载"))
P("DT-004", "部分成立",
  "R87 平台 basis 留痕：卡面动爻组原文飞伏交错、读法有歧（卡面不合类）",
  "回原卡——卡面 attachments.moving_lines 逐字载「原文飞伏交错叙述，动爻组读法有歧，图解本整理为同人之兑，此处照原文三处并记」，分歧一层属实，席位据原文三处并记作断并降置信；R87 manifest 结局逐字载「其子果死」，终局明载可核。故部分成立。",
  CARRY_P.format(g="动爻组原文飞伏交错、读法有歧已自注，按原文作断；终局明载"))
P("DT-006", "部分成立",
  "R87 平台 basis 留痕：卡面动爻飞伏语叙述、与图解本整理读法含混（卡面不合类）",
  "回原卡——卡面 attachments.moving_lines 逐字载「原文飞伏语，图解本整理为蛊之鼎，此处以原文为准」，含混一层属实，席位按原文飞神发动作断并降置信；R87 manifest 结局逐字载「果然无事（子病无事）」，终局明载可核。故部分成立。",
  CARRY_P.format(g="动爻飞伏语与图解本整理含混已自注，按原文作断；终局明载"))
P("LY-018", "部分成立",
  "R87 平台 basis 留痕：残损注明——卡面六亲标注与卦宫推定不完全对齐（卡面不合类）",
  "回原卡与 basis——basis 逐字载「卡面六亲标注与按卦名推定的卦宫五行不能完全对齐（如四爻酉金卡面标子孙），逐爻装卦的宫位坐标存疑——此为输入残损」，不合一层属实，席位只据卡面所标六亲与动变作断；R87 manifest 结局逐字载掘破缸一口、尽是瓦屑泥土无财，终局明载可核。故部分成立。",
  CARRY_P.format(g="卡面六亲标注与卦宫推定不完全对齐、宫位坐标存疑已自注；终局明载"))
P("LY-103", "部分成立",
  "R87 平台 basis 留痕：卡面空亡字段与卡内推算注自相矛盾（卡面不合类）",
  "回原卡——卡面 attachments 空亡逐字作「子丑」，卡内 notes.completion_grade 空亡 basis 逐字载「由已载日干支『丙辰』按旬空规则推得戌亥」，两载自相矛盾一层属实，席位以标准旬空戌亥为准、作误载处理并自报降置信；R87 manifest 结局逐字载「果然应验」当晚雨停，终局明载可核。故部分成立。",
  CARRY_P.format(g="卡面空亡字段与卡内推算注自相矛盾已自报、按标准旬空裁定；终局明载"))
P("LY-301", "部分成立",
  "R87 平台 basis 留痕：卡面残损注明——装卦表 OCR 行序错乱注记与直载注记并存（残损类）",
  "回原卡与 basis——basis 逐字载「在线本装卦表双栏 OCR 转录有行序错乱之记，卡面 notes 又称逐爻为原书直载——两说并存，盘面证据链有瑕，已降置信并标 disputed」，残损一层属实；R87 manifest 结局逐字载「果於三月乃妻去世矣」，终局明载可核。故部分成立。",
  CARRY_P.format(g="装卦表 OCR 行序错乱注记与直载注记并存、证据链有瑕已自注；终局明载"))
P("LY-416", "部分成立",
  "R87 平台 basis 留痕：残损注明——双卦并载、初占卦名原文未直书（残损类＋多卦合卡类）",
  "回原卡与 basis——basis 逐字载「卡面 chart_lines 并载两卦共十二行……初占卦名原文未直书，以再占为主断、初占为参，不臆补初占卦名」，并载与初占卦名缺载两层属实（R86 筛检时本例 basis 无此留痕、本轮 basis 新载，口径以本轮回卡为准）；R87 manifest 结局逐字载「後應申月所請準，酉歲迎靈而歸」，终局明载可核。故部分成立。与在册 R81 条各旨独立。",
  CARRY_P.format(g="双卦并载、初占卦名原文未直书，残损已自注，只据再占主断；终局明载"), SYN)
P("LY-525", "部分成立",
  "R87 平台 basis 留痕：残损注明——卡面月建记载不全（残损类）",
  "回原卡与 basis——basis 逐字载「卡面 asked_at 作『亥日辛酉日（原文如此，月建記載不全）』，月建缺失，旺衰缺月建一层……置信下调」，残损一层属实；R87 manifest 结局逐字载「服之便醒」，终局明载可核。故部分成立。与在册 R79 结局层条各旨独立。",
  CARRY_P.format(g="卡面月建记载不全、旺衰缺一层已自注；终局明载"), SYN)
P("LY-603", "部分成立",
  "R87 平台 basis 留痕：卡面未载 hidden_lines、伏神系推算复原（残损类）",
  "回原卡与 basis——basis 逐字载子孙午火「按震宫首卦同位推得，卡面未载 hidden_lines，此为推算」，复原一层属实，席位两路并参作断；R87 manifest 结局逐字载「果卒於癸卯日」，终局明载可核。故部分成立。",
  CARRY_P.format(g="卡面未载 hidden_lines、伏神推算复原已自注；终局明载"))
P("LY-620", "部分成立",
  "R87 平台 basis 留痕：输入残损注明——原书无逐爻装卦表、盘面推算复原（残损类）",
  "回原卡——卡面 notes 明载盘面系据本变卦名以标准纳甲推算复原、非原表直载，basis 逐字自注并降置信，残损一层属实；R87 manifest 结局逐字载「果於削職後七月而終」，终局明载可核。故部分成立。与在册 R79 不成立条（结局对应面）各旨独立。",
  CARRY_P.format(g="原书无逐爻装卦表、盘面推算复原卡面明载；终局明载"), SYN)
P("LY-621", "部分成立",
  "R87 平台 basis 留痕：输入残损注明——原书无装卦表、盘面推算复原（残损类）",
  "回原卡——卡面 notes 明载盘面据本变卦名标准纳甲推算复原，basis 逐字自注并降置信，残损一层属实；R87 manifest 结局逐字载「果卒於九月丁亥日」，终局明载可核。故部分成立。",
  CARRY_P.format(g="原书无装卦表、盘面推算复原卡面明载；终局明载"))
P("OC-024", "部分成立",
  "R87 平台 basis 留痕：卡面残损严重——未给任何卦象、动爻、起卦数或外应记录（残损类）",
  "回原卡——卡面无卦象盘面附件，残损一层属实，席位据此只据占题事实与题名线索作低置信断、明写盘面依据不足；R87 manifest 结局逐字载其家掘之果得金、葬事得办，终局明载可核。故部分成立。",
  CARRY_P.format(g="卡面未给卦象动爻起卦记录、残损严重已自注；终局明载"))
P("OC-025", "部分成立",
  "R87 平台 basis 留痕：卡面残损——未给卦象与起占记录、未载预书年月日文字（残损类）",
  "回原卡——卡面无体用盘面，残损一层属实，席位据此只据占题事实链作断并降置信；R87 manifest 结局逐字载届期道者来访坐破其椅，终局明载可核。故部分成立。",
  CARRY_P.format(g="卡面未给卦象与起占记录、残损已自注；终局明载"))
P("YM-002", "部分成立",
  "R87 平台 basis 留痕：残损注记——卡面只记未建甲子旬、无占时与六神（残损类）",
  "回原卡与 basis——basis 逐字载「卡面只记『未建甲子旬壬申日』，无占时与六神，六神象意不入断」，残损一层属实；R87 manifest 结局逐字载「后至酉月丁亥日，其病不治」，终局明载可核。故部分成立。",
  CARRY_P.format(g="卡面无占时与六神、残损已自注；终局明载"))
P("YM-032", "部分成立",
  "R87 平台 basis 留痕：残损注——子孙不现且伏位未载，为本例主要残损（残损类）",
  "回原卡与 basis——basis 逐字自注子孙不上卦、伏位未载未取伏神、置信已降，残损一层属实；R87 manifest 结局逐字载「后应生男不育」，终局明载可核。故部分成立。",
  CARRY_P.format(g="子孙不现且伏位未载、主要残损已自注；终局明载"))
P("YY-019", "部分成立",
  "R87 平台 basis 留痕：卡面 chart 一爻文字残损、呈缺字符（残损类）",
  "回原卡与 trigger——trigger reason 逐字载「卡面 chart 一爻文字残损（『��弟辛巳火』应为兄弟辛巳火），disputed=true 并已据六亲序复原注明」，残损一层属实；R87 manifest 结局逐字载「而夫死也」，终局明载可核。故部分成立。",
  CARRY_P.format(g="卡面一爻文字残损呈缺字符、已据六亲序复原注明；终局明载"))
P("ZY-003", "部分成立",
  "R87 平台 basis 留痕：读辞与残损注明——动爻原传未明言（残损类）",
  "回原卡与 basis——basis 逐字载「动爻原传未明言，所据为随卦辞……动爻不明使朱熹一动读爻辞之路不可执行，在此照实注明」，残损一层属实，席位改按变卦卦辞参本卦卦象作断；R87 manifest 结局逐字载穆姜薨于东宫、终未得出，终局明载可核。故部分成立。",
  CARRY_P.format(g="动爻原传未明言、读辞之路不可执行已自注；终局明载"))
MPWP = [
 ("MP-001", "无盘面、无出生时辰", "蔡英文以817万票大胜韩国瑜552万票"),
 ("MP-002", "无盘面无时辰", "以817万票史上最高票连任"),
 ("MP-003", "无盘面，只有 subject/context/provenance", "7月赢得国民党初选成为总统候选人"),
 ("MP-004", "无盘面无时辰", "蔡英文以817万票连任当选"),
 ("MP-005", "无盘面", "韩国瑜得552万票败选"),
 ("MP-006", "只有出生年1957、无月日时，八字排盘输入残损不起盘", "同年6月6日再被罢免高雄市长职务"),
 ("MP-007", "无盘面无时辰", "2020年1月总统大选大败"),
 ("MP-008", "无盘面", "成为候选人并以817万票大胜韩国瑜"),
 ("MP-009", "卡面自述卜卦而问、未载任何卦象盘面", "韩国瑜被罢免高雄市长"),
 ("MP-010", "只有出生年1950、无时辰，相法/命盘材料残损", "赖清德当选总统"),
 ("MP-011", "无三人完整生辰，命盘残损不臆造", "赖清德5,586,019票第一"),
 ("MP-013", "只有出生年1959、无时辰，命盘残损", "以3,254票险胜连任"),
 ("MP-014", "只有出生年1946、无时辰", "败于拜登"),
 ("MP-017", "无任何占测盘面与命造数据", "以777票当选第五任香港特首"),
 ("MP-018", "未载命造与面相数据", "曾俊华得365票落选"),
 ("MP-019", "仅载三人生年、无完整命造与盘面", "林郑月娥以777票当选"),
 ("WP-008", "无出生数据、无起卦盘面", "BJP won 303 seats and the NDA formed the government"),
 ("WP-009", "无队长本命盘、无卜卦盘", "India lost the semi-final to New Zealand"),
 ("WP-010", "仅给出拜登吠陀天蝎上升一句、无完整盘面", "Joe Biden defeated Donald Trump"),
 ("WP-011", "仅给出特朗普吠陀盘一处配置、无完整盘面", "Donald Trump lost the 2020 election to Joe Biden"),
 ("WP-012", "无盘面", "Biden won both the popular vote"),
 ("WP-013", "仅注选举时太阳在巨蟹座、无完整盘面", "Labour won the 4 July 2024 general election in a landslide"),
]
for cid, gist, ocfrag in MPWP:
    assert ocfrag in outcome(cid), cid
    P(cid, "部分成立",
      "R87 平台 basis 留痕：输入残损——" + gist + "（残损类）",
      f"回原卡——卡面无盘面附件（或仅题面锚点），{gist}属实，席位据此只按题面事实作断并降置信、不臆补盘面；R87 manifest 结局逐字载「{outcome(cid)}」，终局明载可核。故部分成立。照 MP-012（R86 同型已定案）判例。",
      CARRY_P.format(g="题面无盘面附件、输入残损已自注，终局明载"))
# ---------- 平台侧：不成立（FREEZE 检查器误报＋加扫误检） ----------
for cid, des in [
    ("BZ-022", "卡面 tradition＝bazi、首行逐字照录该值；命中「未载」指起运岁数原书未载"),
    ("BZ-024", "卡面 tradition＝bazi、首行逐字照录该值；命中「未载」指起运岁数未载"),
    ("BZ-026", "卡面 tradition＝bazi、首行逐字照录该值；命中「未载」指起运岁数未载"),
    ("BZ-028", "卡面 tradition＝bazi、首行逐字照录该值；命中「未载」指起运岁数未载"),
    ("BQ-021", "卡面 tradition＝六爻、首行逐字照录该值；命中字面指盘面要素缺载"),
    ("BQ-025", "卡面 tradition＝六爻、首行逐字照录该值；命中字面指盘面要素缺载"),
    ("LY-446", "卡面 tradition＝liuyao、首行逐字照录该值；「未見」出方法引文"),
    ("LR3-110", "卡面无 tradition/system 字段、首行明写「卡面 tradition 未标注」属如实未标注声明，检查器以子串误检"),
    ("OC-012", "卡面未载 tradition/system 字段、首行如实声明未标注，主持加扫误检、放行"),
]:
    rel = SYN if cid in {a["case_id"] for a in anns86} else "新登记（R87，平台 basis 留痕定案）"
    P(cid, "不成立",
      "FREEZE-r87 tradition 初检/加扫候选：检查器误报",
      f"主持逐件回读首行＋输入卡字段裁定（FREEZE-r87 定版）：{des}，非 tradition 虚称或误标。起运岁数未载属八字命例通例形态（承 OC-018 判例）。故旗标不成立，只登记。",
      CARRY_N, rel)
# ---------- 验收侧 ----------
for cid in ["CYJ-006", "CYJ-007", "CYJ-008", "CYJ-009", "CYJ-010"]:
    g = gold[cid]
    A(cid, "部分成立",
      "DIAG-H30 §5 F1＋验收 basis 残损注明：卡面 chart_complete=false、chart_fidelity 明载仅干支，四课、三传、天将、空亡、年命俱未给（残损类）",
      f"回原卡——holdout30 输入卡 anchors 逐字载 chart_complete＝False、chart_fidelity「仅干支（复原不能）：原书课盘列在盘、转录底稿未录盘、页图字迹不足以逐字可靠转录」，盘体缺载一层属实；金标 grade_note 所载「课式头四要素 present（R84 核查台账）」指课式头层、与盘体缺载两口径并列（与 R87 CYJ 锚点专项复核并案：主持裁定按 (乙) 收紧、已用面效力不动）。席位按残损口径只据干支大势作断；金标 outcome_record 逐字载「{g['outcome_record']}」，终局明载可核。故部分成立。承 CYJ-001 等（R86）同型判例。",
      CARRY_P.format(g="课盘 fidelity 降级、盘体缺载（仅干支），课式头 present 口径并列；终局明载"))
A("BY-017", "不成立",
  "DIAG-H30 §5 F2：三传中传天将转录缺字候选（卡面不合类）",
  "回原卡——holdout30 输入卡三传逐字作「财申（合）、财酉（朱）、子戌（蛇）」，天盘注逐字载「元＝玄武、龙＝青龙，原书省字照录」——「朱」为朱雀省字、属原书省字体例且卡面已明载省字照录口径，非转录缺字；席位已自标降档、主断不依赖该字。金标 outcome_record 逐字载城陷案验，终局明载。故旗标不成立，只登记。",
  CARRY_N)
A("GSZ-105", "不成立",
  "DIAG-H30 §5 F3：asked_at 年柱仅作「寅年」简写候选（残损类）",
  "回原卡与金标——holdout30 输入卡 asked_at 逐字作「寅年甲寅月癸未日（原文年柱仅作『寅年』）」，金标 grade_note 逐字载「锚点：月建（甲寅月）与日辰（癸未日）在场，年柱简写不碍锚点定式，照录登记」，封存口径已定、不计 IN（DIAG-H30 §0 同口径）。属原书通例形态。故旗标不成立，只登记。承 DS-063（R86）同型判例。",
  CARRY_N)
A("WHY-027", "不成立",
  "DIAG-H30 §5 F4：asked_at 未载年柱候选（残损类）",
  "回原卡——holdout30 输入卡 asked_at 逐字作「未月甲午日」，六爻断据面月建与日辰俱载在场；年柱未载属原书载录形态、不构成断锚点缺口，席位按月日行断无缺口。金标 outcome_record 逐字载壬子日家中漏电火灾、发现及时无大损失，终局明载。故旗标不成立，只登记。",
  CARRY_N)
for cid in ["WHY-032", "WHY-033"]:
    A(cid, "不成立",
      "DIAG-H30 §5 F5：回溯应期形态候选——金标应验所据婚史全在占时之前",
      "回原卡与金标——两例所问均为夫妻缘分，金标应验所据婚史在占时之前，属原书应期例以已发生婚史为应验面之体例形态，非输入卡或结局数据瑕疵，与本例核验无涉；金标 outcome_record 逐字明载婚史终局。故旗标不成立，只登记。承 ZW-011（R86）同型判例。",
      CARRY_N)

assert len(NEW) == 62, len(NEW)
print(Counter((f, d) for _, d, _, _, _, _, f in NEW))

new_anns = []
for cid, disp, flag, finding, carry, relation, face in NEW:
    if face == "platform":
        anon = inv87[cid]
        srcs = [f"divination/benchmark/phase3/inputs-dev12/{cid}.json",
                f"divination/benchmark/phase3/runs/round87/predictions/{cid}.json",
                f"divination/benchmark/phase3/runs/round87/judging/outcome-manifest.json cases[{cid}]",
                "divination/benchmark/phase3/runs/round87/judging/host-mapping.json",
                "divination/benchmark/phase3/runs/round87/FREEZE-r87.md"]
        seats = ["R87 平台盲测席 basis 留痕／FREEZE-r87 主持裁定", "R87 数据席回读原卡"]
    else:
        anon = inva[cid]
        srcs = [f"divination/benchmark/phase3/holdout30/inputs/{cid}.json",
                f"divination/benchmark/phase3/holdout30/test_gold.jsonl [{cid}]",
                f"divination/benchmark/phase3/runs/round87/acceptance/predictions/{cid}.json",
                "divination/benchmark/phase3/runs/round87/acceptance/DIAG-H30.md §5",
                "divination/benchmark/phase3/runs/round87/acceptance/judging/host-mapping.json"]
        seats = ["DIAG-H30 席（§5 旗标候选）", "R87 数据席回读原卡／金标"]
    new_anns.append({
        "anon_id": anon, "case_id": cid, "disposition": disp, "finding": finding,
        "flag": flag, "manifest_carry_suggestion": carry, "registered_round": 87,
        "relation": relation, "source_seats": seats, "sources_checked": srcs,
    })

out = dict(r86)
out["round"] = 87
out["_provenance"] = (
    "R87 数据席（附则承接对勘＋annotations 全量承接与本轮新定案，独立席位，不兼任本轮盲测/评审/诊断/组集/修订/CYJ 复核，不改任何分数）："
    "以 data/case-annotations-r86.json 为底承接全量 238 件（成立 14／部分成立 187／不成立 35／未核 2），前 238 件逐件原样、无删改；"
    "承接对勘：R86 附则平台侧部分成立 45 件已于 R87 manifest 以 _r86_carryover_notes_addendum 落实（脚本断言：层 id 集与 r86 部分成立∧registered_round＝86∧在 dev cases 集全等、注记文本逐件捕获验合）；验收侧 5 件（CYJ-001／CYJ-002／CYJ-004／CYJ-005／ZW-015）照 R83 判例不入 dev 层、照 r86 附则 §四原样对勘登记；"
    "_r82 层 3 件已经 R85 主持裁定结案，本轮不再滚动对勘、只作在册登记；"
    "本轮新定案 62 件：平台侧 52 件（部分成立 43／不成立 9；来源＝FREEZE-r87 主持裁定 15 件候选＋加扫 1 件，其中 BZ-021 部分成立、误报不成立 9 件立条、BQ 六件 R84 同旨条引据不重复立条＋平台 predictions basis 残损/卡面不合/多卦合卡三类留痕逐件回原卡与 R87 manifest 结局定案 42 件部分成立）＋验收侧 10 件（部分成立 5／不成立 5；来源＝DIAG-H30 §5 F1–F5＋验收 predictions basis 留痕逐件回 holdout30 输入卡与金标定案）；"
    "在册同旨旗标只登记不重复立条（引据清单见附则）；合断体例与命例通例等经核不立旗者只筛检登记；"
    "AS-307 双条并行例外形态照体例续行（R80 部分成立条与 R85 不成立条并行保留、不合并；本轮 AS-307 无新旗标，其 basis 输入残损留痕与 R68 已定案旨同旨、只引据登记，不另立第三条）；"
    "LY-015／LY-320 同例重复登记承 R85 裁定、本轮照原样承接；待核四件维持；CZ-QX 维持 16 只登记。"
)
out["annotations"] = anns86 + new_anns
sc = list(r86["special_checks"])
sc += [
 {"item": "（R87）特别核查59：R86 承接对勘与 _r82 层结案登记",
  "conclusion": "R86 附则平台侧 45 件已于 R87 manifest 以 _r86_carryover_notes_addendum 落实（层 id 集与附则 §三.1 清单逐件全等、注记文本捕获验合 45/45）；验收侧 5 件（CYJ-001／CYJ-002／CYJ-004／CYJ-005／ZW-015）照 R83 判例不入 dev 层、照附则 §四原样对勘。_r82 层 3 件（LY-406／LY-446／LY-524）已经 R85 主持裁定结案，本轮不再滚动对勘，注记在 manifest 层与 annotations 之保留只作在册登记。",
  "evidence": "runs/round87/judging/outcome-manifest.json _r86_carryover_notes_addendum 45 件（落盘脚本结构化直读断言）；manifest 全文 SHA-256 f3329d5c6f6502d36add1f586f669939a644105377b5c6819f42d64b63fd10c3、cases 载荷结构化 SHA 00f362bd8e4b55ceff31502cb5f7e8239855b1f806a7b1495284af80186a31ad（PREREG-r87 §0 登记）。",
  "scope_note": "对勘只登记，不改 manifest 任一侧。"},
 {"item": "（R87）特别核查60：平台旗标定案总登记（FREEZE 裁定＋basis 三类留痕）",
  "conclusion": "FREEZE-r87 tradition 初检候选 15 件主持裁定：14 件检查器误报不成立（其中 BQ-017／BQ-018／BQ-020／BQ-022／BQ-023／BQ-024 六件 R84 同旨不成立条在册、只引据不重复立条；BQ-021／BQ-025／BZ-022／BZ-024／BZ-026／BZ-028／LY-446／LR3-110 八件立不成立新条）、BZ-021 措辞不实部分成立不重测；主持加扫 OC-012 误检放行立不成立条。平台 predictions basis 三类留痕逐件回原卡定案：新定案部分成立 42 件；同旨已定案者入引据清单；Lilly 散文述位设计形态、八字命例通例（起运未载）与合断体例无异常留痕者经核不立旗，只筛检登记。",
  "evidence": "runs/round87/FREEZE-r87.md；runs/round87/predictions 逐件 basis（落盘脚本逐件回卡断言：MP/WP 无盘面组卡面无 attachments、MPWP 结局逐字在场、CYJ 金标逐字在场）。",
  "scope_note": "basis 留痕不凭转述定案，逐件以原卡与结局原文为准。"},
 {"item": "（R87）特别核查61：验收侧旗标定案总登记（holdout30）",
  "conclusion": "DIAG-H30 §5 旗标候选 F1–F5 与验收 predictions basis 留痕逐件回 holdout30 输入卡与金标定案：新定案 10 件（部分成立 5＝CYJ-006／CYJ-007／CYJ-008／CYJ-009／CYJ-010；不成立 5＝BY-017／GSZ-105／WHY-027／WHY-032／WHY-033）。CYJ 五例与 R87 CYJ 锚点专项复核并案（主持裁定按 (乙) 收紧、已用面效力不动），不追改封存与分数；DA/BY 全盘例 basis 明载盘面完整无残损，不立旗。",
  "evidence": "runs/round87/acceptance/DIAG-H30.md §5／§0；holdout30/inputs 与 test_gold.jsonl 逐件回读（落盘脚本金标 outcome 逐字引录）。",
  "scope_note": "验收侧定案只及标注与承接建议，不改验收分数。"},
 {"item": "（R87）特别核查62：指令性字样特别核查基线六处复核",
  "conclusion": "基线六处经 R87 盘上逐处回读在册、形态未变，出入 0 处：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）＋LR2-016 manifest editor_note 一处（_r56_lr2016_split 分列层、原文逐字全等）＋LR2-016 评审包 editor_note 层一处（以 host-mapping 对位 anon P3-f23fb8ad 定位 packetB.json、独立字段在场）。本轮新增同型件：无。各席一律按数据处理。",
  "evidence": "runs/round87/judging/outcome-manifest.json 与 packetB.json（落盘脚本逐处逐字断言全过）。",
  "scope_note": "只登记、不改任何文本。"},
 {"item": "（R87）特别核查63：待核四件维持与 CZ-QX 维持登记",
  "conclusion": "BZ-029／BZ-040／LY-537／YM-070 四件无新证据、维持待核原登记（LY-537 本轮 basis 仍载 OCR 行序同型留痕，只登记关联、不并案）；CZ-QX 维持 16（holdout30 无测字例、平台定稿口径不变），只登记不另行结算；紫微池挂起 6 项只登记。",
  "evidence": "data/case-annotations-r86.json 待核条目承接；runs/round87/acceptance/DIAG-H30.md（CZ-QX 不适用／不增）。",
  "scope_note": "无盘外独立史源不裁。"},
]
out["special_checks"] = sc
cnt = Counter(a["disposition"] for a in out["annotations"])
out["counts"] = {
 "base_file": "data/case-annotations-r86.json", "base_cases_total": 238,
 "base_verdicts": {"成立": 14, "部分成立": 187, "不成立": 35, "未核": 2},
 "carryover_check_r86_addendum": {"platform_layer": "_r86_carryover_notes_addendum", "platform_items": 45,
   "platform_ids": sorted(layer86.keys()), "acceptance_items": 5, "acceptance_ids": acc5},
 "carryover_check_r82_closed": {"layer": "_r82_carryover_notes_addendum", "items": 3,
   "status": "已经 R85 主持裁定结案（登记性注记不要求 reason 回响），R87 不再滚动对勘"},
 "new_registrations_r87": 62,
 "new_cases_r87": {
   "部分成立_platform": sorted(c for c, d, _, _, _, _, f in NEW if f == "platform" and d == "部分成立"),
   "不成立_platform": sorted(c for c, d, _, _, _, _, f in NEW if f == "platform" and d == "不成立"),
   "部分成立_acceptance": sorted(c for c, d, _, _, _, _, f in NEW if f == "acceptance" and d == "部分成立"),
   "不成立_acceptance": sorted(c for c, d, _, _, _, _, f in NEW if f == "acceptance" and d == "不成立")},
 "r87_layer_partial_upheld_platform": sorted(c for c, d, _, _, _, _, f in NEW if f == "platform" and d == "部分成立"),
 "r87_partial_upheld_acceptance": sorted(c for c, d, _, _, _, _, f in NEW if f == "acceptance" and d == "部分成立"),
 "as307_double_entry": "R80 部分成立条与 R85 不成立条并行保留、不合并；R87 不另立第三条（本轮残损留痕与 R68 已定案旨同旨、引据登记）",
 "cases_total": len(out["annotations"]),
 "verdicts": {"成立": cnt["成立"], "部分成立": cnt["部分成立"], "不成立": cnt["不成立"], "未核": cnt["未核"]},
}
assert out["counts"]["cases_total"] == 300
assert out["counts"]["verdicts"] == {"成立": 14, "部分成立": 235, "不成立": 49, "未核": 2}, out["counts"]["verdicts"]
assert out["annotations"][:238] == anns86
with open(f"{BASE}/data/case-annotations-r87.json", "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
print("written annotations:", len(out["annotations"]), out["counts"]["verdicts"], "special_checks:", len(sc))
