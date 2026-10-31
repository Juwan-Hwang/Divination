# -*- coding: utf-8 -*-
"""R83 数据席落盘脚本：承接 r82 annotations 134 件 + 本轮新定案 13 件 = 147 件，
编制 manifest-carryover-r83-addendum.md。只写两件产出，不改任何分数/结局/金标。
引文逐字断言：任一断言不过即中止。"""
import json, hashlib, collections

B = "/home/hatch/workspace/divination/benchmark/phase3"
def load(p):
    with open(p, encoding="utf-8") as f: return json.load(f)
def text(p):
    with open(p, encoding="utf-8") as f: return f.read()
def assert_in(needle, hay, label):
    assert needle in hay, f"引文断言失败 [{label}]: {needle[:60]}"

# ---------- 底本与承接 ----------
r82 = load(f"{B}/data/case-annotations-r82.json")
base_anns = r82["annotations"]
assert len(base_anns) == 134
assert collections.Counter(a["disposition"] for a in base_anns) == {"成立":12,"部分成立":114,"不成立":6,"未核":2}
base_cases = {a["case_id"] for a in base_anns}

# ---------- 本轮来源 ----------
man = load(f"{B}/runs/round83/judging/outcome-manifest.json")
man_raw = text(f"{B}/runs/round83/judging/outcome-manifest.json")
hm = load(f"{B}/runs/round83/judging/host-mapping.json"); rev = {v:k for k,v in hm.items()}
jx = load(f"{B}/runs/round83/judging/judgeX-merged.json")
jy = load(f"{B}/runs/round83/judging/judgeY-merged.json")
freeze = text(f"{B}/runs/round83/FREEZE-r83.md")
diag = text(f"{B}/runs/round83/acceptance/DIAG-H27.md")
ahm = load(f"{B}/runs/round83/acceptance/judging/host-mapping.json")
aours = {v:k for k,v in ahm["ours"].items()}; amaster = {v:k for k,v in ahm["master"].items()}
def acc_reason(fname, anon):
    with open(f"{B}/runs/round83/acceptance/judging/{fname}", encoding="utf-8") as f:
        for ln in f:
            o = json.loads(ln)
            if o["anon_id"] == anon: return o["reason"]
    raise KeyError(anon)
gold = {}
with open(f"{B}/holdout27/test_gold.jsonl", encoding="utf-8") as f:
    for ln in f:
        o = json.loads(ln); gold[o["id"]] = o
def inp(cid):
    return load(f"{B}/holdout27/inputs/{cid}.json")
seal27 = text(f"{B}/data/holdout27-seal-log.md")

# ---------- 工序一：_r82 层 3 件对勘 ----------
layer = man["_r82_carryover_notes_addendum"]
assert list(layer.keys()) == ["LY-406","LY-446","LY-524"]
r82_by_case = {a["case_id"]: a for a in base_anns}
for cid in ["LY-406","LY-446","LY-524"]:
    assert layer[cid] == r82_by_case[cid]["manifest_carry_suggestion"], cid
    assert "结局逗号收尾疑截断" in layer[cid]
# 评审包传递面：packet 逐件断言 [R82-addendum] 段在场（packet1/2/3 与 packetA/B）
packets = {}
for pn in ["packet1.json","packet2.json","packet3.json","packet4.json","packetA.json","packetB.json"]:
    packets[pn] = load(f"{B}/runs/round83/judging/{pn}")
def packet_entry(anon):
    hits = []
    for pn, items in packets.items():
        for it in items:
            if it.get("anon_id") == anon: hits.append((pn, it))
    return hits
for cid in ["LY-406","LY-446","LY-524"]:
    hits = packet_entry(rev[cid])
    assert hits and all("[R82-addendum]" in it["carry_note"] for _, it in hits), cid
# 双视 reason 逐字据
R = {}
for cid in ["LY-406","LY-446","LY-524"]:
    a = rev[cid]; R[cid] = (jx[a]["reason"], jy[a]["reason"])
assert_in("甲戌出空即愈合", R["LY-406"][0], "LY-406 X")
assert_in("迟险一节未分载", R["LY-406"][1], "LY-406 Y")
assert_in("结局酉日天变戌日而雨", R["LY-446"][0], "LY-446 X")
assert_in("酉日天变戌日而雨差一日", R["LY-446"][1], "LY-446 Y")
assert_in("附子对应未明字", R["LY-524"][0], "LY-524 X")
assert_in("附子与结局所用药对应未明字", R["LY-524"][1], "LY-524 Y")
for cid in ["LY-406","LY-446","LY-524"]:
    for r in R[cid]:
        assert "逗号" not in r and "截断" not in r and "尾逗" not in r, cid  # 逗号要点未见于 reason
# 结局原文逐字
assert man["cases"]["LY-406"] == "果於甲戌出空卽愈﹐"
assert man["cases"]["LY-446"] == "果於酉日天變﹐戌日而雨﹐"
assert_in("次日曰愈﹐", man["cases"]["LY-524"], "LY-524 结局")

# ---------- FREEZE 三件 ----------
assert_in("AS-307 成立（形式旗标）", freeze, "FREEZE AS-307")
assert_in("卡面载 tradition＝astrology，预测 basis 首行却称「卡面未标注 tradition 字段，按题面体裁自决」", freeze, "FREEZE AS-307 basis")
assert_in("LY-001 不成立", freeze, "FREEZE LY-001")
assert_in("卡面仅载 system＝liuyao、无 tradition 字段；首行逐字照录「system＝liuyao」并注明卡面无 tradition 字段，合规，系检查器关键词误报", freeze, "FREEZE LY-001 裁定")
assert_in("ZY-001 不成立", freeze, "FREEZE ZY-001")
assert_in("卡面仅载 system＝yijing、无 tradition 字段；首行如实注未标注 tradition 并同行载明 system＝yijing，合规，系检查器关键词误报", freeze, "FREEZE ZY-001 裁定")
assert "LY-001" not in base_cases and "ZY-001" not in base_cases
assert_in("果於巳年承襲長房世職", man["cases"]["LY-001"], "LY-001 结局")
assert_in("敬仲子孫田氏終代齊有國", man["cases"]["ZY-001"], "ZY-001 结局")
assert rev["LY-001"] == "P3-5d21f235" and rev["ZY-001"] == "P3-8a775d85"
assert rev["AS-307"] == "P3-37942194"

# ---------- 逗号收尾全集扫描（R83 manifest，cases 与 R82 深度一致口径下复扫） ----------
comma_cases = sorted([cid for cid, t in man["cases"].items() if isinstance(t, str) and t.rstrip().endswith(("﹐", "，", ","))])  # LY-540／LY-623 为全角逗号「，」收尾，其余为小逗号「﹐」
expected_comma = sorted(["LY-406","LY-446","LY-524","LY-408","LY-411","LY-416","LY-418","LY-423","LY-425","LY-428","LY-434","LY-437","LY-440","LY-452","LY-514","LY-523","LY-525","LY-528","LY-540","LY-623"])
assert comma_cases == expected_comma, comma_cases
assert all(c in base_cases for c in comma_cases)

# ---------- 基线六处 ----------
assert_in("盲测比对须注", man["cases"]["BZ-036"], "BZ-036")
assert_in("（盲测比对时以格局大富一项为主）", man["cases"]["BZ-042"], "BZ-042")
assert_in("使用时须分开统计", man["cases"]["BZ-105"], "BZ-105")
assert_in("勿以此斷", man["cases"]["LY-204"], "LY-204")
assert [cid for cid,t in man["cases"].items() if "勿以此" in t] == ["LY-204"]
split_note = man["_r56_lr2016_split"]["editor_note"]
assert split_note == "原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。"
assert man_raw.count("原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。") >= 1
lr2_hits = packet_entry(rev["LR2-016"])
assert lr2_hits and all(it.get("editor_note") == split_note for _, it in lr2_hits), "LR2-016 packet editor_note"
ly204_hits = packet_entry(rev["LY-204"])
assert ly204_hits and all("勿以此斷" in it["outcome_record"] for _, it in ly204_hits)
for a in (jx[rev["LY-204"]]["reason"], jy[rev["LY-204"]]["reason"]):
    assert "勿以此" not in a
assert_in("编者注甲戌日巳时细项未复核", jx[rev["LR2-016"]]["reason"], "LR2-016 X 编者注")
assert_in("编者注『甲戌日巳时』细项未复核不计", jy[rev["LR2-016"]]["reason"], "LR2-016 Y 编者注")

# ---------- 待核四件本轮触及 ----------
assert man["cases"]["LY-537"].find("申予日") >= 0 if isinstance(man["cases"]["LY-537"], str) else True
assert_in("结局申予日字样含混", jx[rev["LY-537"]]["reason"], "LY-537 X 触及")
assert_in("果于申予日归", jy[rev["LY-537"]]["reason"], "LY-537 Y 触及")
assert_in("同行都下", jx[rev["YM-070"]]["reason"], "YM-070 X")
assert_in("语义未明", jy[rev["YM-070"]]["reason"], "YM-070 Y")

# ---------- CZ-QX 维持 16 ----------
fs = load(f"{B}/runs/round83/final-scores.json")
assert fs["analysis_r83"]["families"]["liuyao_zh"]["n"] == 16
assert_in("本集无测字段", diag, "H27 无测字")

# ---------- DIAG-H27 F1–F8 证据断言 ----------
for ftag in ["F1（DS-040", "F2（QM-052", "F3（QM-058", "F4（GSZ-079/088", "F5（GSZ-088", "F6（WHY-008/009/010", "F7（DS-048", "F8（GSZ-081/084"]:
    assert_in(ftag, diag, f"DIAG {ftag}")
# F1 + 残片（DS-040）
assert_in("命主未具名（仅称曾任国家财政部长），按 low 登记；主持如按职位可识别性从严，可复核升档。", gold["DS-040"]["grade_note"], "DS-040 grade_note")
assert_in("表示一个管理财的权力机构；而日支之卯木所生巳火合申，申被巳制，意思是由我来控制那个管理财的权力机构，表示他本人掌握更大的权力。", gold["DS-040"]["master_prediction"], "DS-040 断语")
assert gold["DS-040"]["outcome_record"] == "事实上，命主曾任国家财政部长。"
m1_040 = acc_reason("judgeM1.jsonl", "H27M-c032fdad"); m2_040 = acc_reason("judgeM2.jsonl", "H27M-c032fdad")
assert_in("断语为解释性残句", m1_040, "M1 残片"); assert_in("断语为残片式分析、具体对应含糊", m2_040, "M2 残片")
assert amaster["DS-040"] == "H27M-c032fdad" and aours["DS-040"] == "H27O-51d22c8f"
# F7（DS-048）
o1_048 = acc_reason("judgeO1.jsonl", "H27O-0fccb311"); o2_048 = acc_reason("judgeO2.jsonl", "H27O-0fccb311")
assert_in("结局未明示火灾年份", o1_048, "O1 DS-048"); assert_in("2008火灾烧毁货物厂房、损失二千万", o2_048, "O2 DS-048")
assert_in("是的，是的，那是一场火灾，烧完了所有货物，厂房最后倒了！损失2000多万……", gold["DS-048"]["outcome_record"], "DS-048 结局")
assert_in("是庚辰年，肯定是2000年破大财！", gold["DS-048"]["master_prediction"], "DS-048 大师断语")
# F2（QM-052）
assert_in("stems以第二局为校验代表，第三局干集未另列字段", gold["QM-052"]["grade_note"], "QM-052 grade_note")
assert_in("stems 以第二局为校验代表、第三局干集未另列字段", seal27, "QM-052 封存日志")
assert_in("第三局干集 stem_check 双 ok（第二局干集卡面未单列校验，逐字据 board_verbatim）", diag, "QM-052 basis（DIAG 引）")
_in52 = inp("QM-052"); assert_in("第三局：1999年6月6日晚7点40分来电问", _in52["anchors"]["board_verbatim"], "QM-052 两局盘面")
assert _in52["anchors"]["stem_check"]["tianpan_ok"] and _in52["anchors"]["stem_check"]["dipan_ok"]
# F3（QM-058）
assert_in("盘面巽4/离9两宫神名原印同作「天」，疑排印误，照录", gold["QM-058"]["grade_note"], "QM-058 grade_note")
_in58 = inp("QM-058"); assert_in("巽4｜天", _in58["anchors"]["board_verbatim"], "QM-058 巽4"); assert_in("离9｜天", _in58["anchors"]["board_verbatim"], "QM-058 离9")
# F4（GSZ-079/088）
assert inp("GSZ-079")["anchors"]["asked_at"] == "已卯年戊辰月丙午日（原文「已卯」）"
assert inp("GSZ-088")["anchors"]["asked_at"] == "已卯年已巳月庚辰日（原文「已卯年已巳月」）"
# F5（GSZ-088）
assert_in("第十四章「例三」重号之第一例（见GSZ-089登记）", gold["GSZ-088"]["grade_note"], "GSZ-088 重号")
# F8（GSZ-081/084 同盘异问：结构全同、六神随日而异）
i81, i84 = inp("GSZ-081"), inp("GSZ-084")
for ii in (i81, i84):
    assert ii["anchors"]["ben_gua"] == "雷天大壮" and ii["anchors"]["bian_gua"] == "火天大有"
    joined = " ".join(ii["anchors"]["chart_lines_top_to_bottom"])
    assert_in("兄弟戌土", joined, "动爻"); assert_in("父母午火", joined, "世"); assert_in("妻财子水", joined, "应")
assert i81["anchors"]["asked_at"] != i84["anchors"]["asked_at"] and i81["question"] != i84["question"]
assert i81["anchors"]["chart_lines_top_to_bottom"] != i84["anchors"]["chart_lines_top_to_bottom"]  # 六神排列相异
# F6（WHY-008/009/010 化神六亲未单列）
for cid in ["WHY-008","WHY-009","WHY-010"]:
    assert_in("锚点在场（卦名、变卦、动爻、世应、六亲纳支、月建日辰全列）", gold[cid]["grade_note"], f"{cid} grade_note")
w8 = " ".join(inp("WHY-008")["anchors"]["chart_lines_top_to_bottom"]); assert_in("兄弟卯木○ 应", w8, "WHY-008 动爻行")
w10 = " ".join(inp("WHY-010")["anchors"]["chart_lines_top_to_bottom"]); assert_in("妻财丑土×", w10, "WHY-010 动爻行")
assert_in("只核地支层：丑土动化变卦初爻子水之支", diag, "WHY-010 basis（DIAG 引）")
for cid in ["DS-040","DS-048","QM-052","QM-058","GSZ-079","GSZ-088","GSZ-081","GSZ-084","WHY-008","WHY-009","WHY-010"]:
    assert cid not in base_cases, cid

# ---------- 本轮新定案条目 ----------
SRC_ACC = lambda cid, extra: [
    f"divination/benchmark/phase3/holdout27/inputs/{cid}.json",
    f"divination/benchmark/phase3/holdout27/test_gold.jsonl {cid} 条",
    "divination/benchmark/phase3/runs/round83/acceptance/DIAG-H27.md §5",
    "divination/benchmark/phase3/runs/round83/acceptance/judging/host-mapping.json",
] + extra
new = []
new.append({
 "anon_id": rev["LY-001"], "case_id": "LY-001", "disposition": "不成立",
 "finding": "平台旗标定案（FREEZE-r83，本席只承接登记、不重裁）：裁定逐字引录——「卡面仅载 system＝liuyao、无 tradition 字段；首行逐字照录「system＝liuyao」并注明卡面无 tradition 字段，合规，系检查器关键词误报。」本席盘上复核：R83 manifest cases[LY-001] 结局「果於巳年承襲長房世職」在盘；卡面与 basis 首行形态照主持裁定登记（本轮授权输入未含 predictions，basis 原文以 FREEZE-r83 逐字引录为据）。定案不成立（检查器误报，承 R80 LR3-004／LR3-104 同型判例）。",
 "flag": "主持检查器（FREEZE-r83）：tradition 首行核查旗标候选——卡面无 tradition 字段、首行照录 system＝liuyao 并注明无 tradition 字段",
 "manifest_carry_suggestion": "只登记不入层：自 R84 起承接本 R83 标注（不成立＝检查器误报，不入 _r83_carryover_notes_addendum 承接层）；结局原文照录不改。",
 "relation": "新立（R83 平台旗标定案）", "registered_round": 83,
 "sources_checked": ["divination/benchmark/phase3/runs/round83/FREEZE-r83.md",
   "divination/benchmark/phase3/runs/round83/judging/host-mapping.json（anon 解析：P3-5d21f235＝LY-001）",
   "divination/benchmark/phase3/runs/round83/judging/outcome-manifest.json cases[LY-001]"],
 "source_seats": ["主持检查器（FREEZE-r83）"]})
new.append({
 "anon_id": rev["ZY-001"], "case_id": "ZY-001", "disposition": "不成立",
 "finding": "平台旗标定案（FREEZE-r83，本席只承接登记、不重裁）：裁定逐字引录——「卡面仅载 system＝yijing、无 tradition 字段；首行如实注未标注 tradition 并同行载明 system＝yijing，合规，系检查器关键词误报。」本席盘上复核：R83 manifest cases[ZY-001] 结局含「敬仲子孫田氏終代齊有國」在盘；卡面与 basis 首行形态照主持裁定登记（本轮授权输入未含 predictions，basis 原文以 FREEZE-r83 逐字引录为据）。定案不成立（检查器误报，承 R80 LR3-004／LR3-104 同型判例）。",
 "flag": "主持检查器（FREEZE-r83）：tradition 首行核查旗标候选——卡面无 tradition 字段、首行如实注未标注并载明 system＝yijing",
 "manifest_carry_suggestion": "只登记不入层：自 R84 起承接本 R83 标注（不成立＝检查器误报，不入 _r83_carryover_notes_addendum 承接层）；结局原文照录不改。",
 "relation": "新立（R83 平台旗标定案）", "registered_round": 83,
 "sources_checked": ["divination/benchmark/phase3/runs/round83/FREEZE-r83.md",
   "divination/benchmark/phase3/runs/round83/judging/host-mapping.json（anon 解析：P3-8a775d85＝ZY-001）",
   "divination/benchmark/phase3/runs/round83/judging/outcome-manifest.json cases[ZY-001]"],
 "source_seats": ["主持检查器（FREEZE-r83）"]})
def acc_entry(cid, finding, flag, seats, extra_src):
    return {"anon_id": aours[cid], "case_id": cid, "disposition": "部分成立", "finding": finding,
      "flag": flag,
      "manifest_carry_suggestion": f"验收侧新登记：自 R84 起承接本 R83 标注（{flag}）：按「{finding}」登记；金标原文照录不改。",
      "relation": "新登记（R83，验收侧 DIAG-H27）", "registered_round": 83,
      "sources_checked": SRC_ACC(cid, extra_src), "source_seats": seats}
new.append(acc_entry("DS-040",
  "DIAG-H27 旗标候选 F1＋验收评审旗标（大师断语残片，H27M-c032fdad）合并定案（R83）：回 holdout27 输入卡与金标原文逐字核——F1：金标 grade_note 自载污染口径复核留位属实：「命主未具名（仅称曾任国家财政部长），按 low 登记；主持如按职位可识别性从严，可复核升档。」（成立面）；但命主确未具名、无姓名与任期可对位，按 low 登记合封存口径，金标与输入数据本身无误载（不成立面；本席不改判级，复核归主持）。残片旨：金标大师断语逐字以「表示一个管理财的权力机构；而日支之卯木所生巳火合申……」起笔、为解释性残句属实，评审 M1 reason 明载「断语为解释性残句」、M2 reason 明载「断语为残片式分析、具体对应含糊」（成立面）；但断语大意（本人掌握管理财的权力机构）与结局「事实上，命主曾任国家财政部长。」大体相合、终局可核（不成立面）。两旨合并一例登记。故部分成立。",
  "DIAG-H27 §5 旗标候选 F1＋验收评审 M1／M2 旗标（H27M-c032fdad）", ["DIAG-H27","M1","M2"],
  ["divination/benchmark/phase3/runs/round83/acceptance/judging/judgeM1.jsonl H27M-c032fdad 条",
   "divination/benchmark/phase3/runs/round83/acceptance/judging/judgeM2.jsonl H27M-c032fdad 条"]))
new.append(acc_entry("DS-048",
  "DIAG-H27 旗标候选 F7（R83 定案）：回 holdout27 金标与验收评审 reason 原文逐字核——双视 reason 对同一结局字段年份载录口径互歧属实：O1 reason 逐字称「结局未明示火灾年份」，O2 reason 逐字称「2008火灾烧毁货物厂房、损失二千万与低置信火险推测及该年大动象合」（成立面）；但金标结局逐字仅载「是的，是的，那是一场火灾，烧完了所有货物，厂房最后倒了！损失2000多万……」、本身无误载，年份坐实靠大师断语「是庚辰年，肯定是2000年破大财！」一线，互歧属评审表述层（不成立面）。故部分成立。",
  "DIAG-H27 §5 旗标候选 F7", ["DIAG-H27"],
  ["divination/benchmark/phase3/runs/round83/acceptance/judging/judgeO1.jsonl H27O-0fccb311 条",
   "divination/benchmark/phase3/runs/round83/acceptance/judging/judgeO2.jsonl H27O-0fccb311 条"]))
new.append(acc_entry("QM-052",
  "DIAG-H27 旗标候选 F2（R83 定案）：回 holdout27 输入卡、金标与封存日志原文逐字核——干集校验代表局口径相左属实：金标 grade_note 与封存日志台账注记均载「stems以第二局为校验代表，第三局干集未另列字段」，我方 basis 逐字载「第三局干集 stem_check 双 ok（第二局干集卡面未单列校验，逐字据 board_verbatim）」，两处对何局干集经 stem_check 校验的表述相左（成立面）；但第二、三局盘面逐字全载于输入卡 board_verbatim、stem_check 天地盘双 ok 全合、锚点 present、不计 IN（不成立面）。故部分成立。",
  "DIAG-H27 §5 旗标候选 F2", ["DIAG-H27"],
  ["divination/benchmark/phase3/data/holdout27-seal-log.md §二"]))
new.append(acc_entry("QM-058",
  "DIAG-H27 旗标候选 F3（R83 定案）：回 holdout27 输入卡与金标原文逐字核——输入卡盘面神名原印形态属实：金标 grade_note 逐字载「盘面巽4/离9两宫神名原印同作「天」，疑排印误，照录」，输入卡 board_verbatim 巽4／离9 两宫神名同作「天」（成立面）；但卡面与金标均已照录登记、stem_check 全合、不计 IN（不成立面）。故部分成立。",
  "DIAG-H27 §5 旗标候选 F3", ["DIAG-H27"], []))
new.append(acc_entry("GSZ-079",
  "DIAG-H27 旗标候选 F4（R83 定案）：回 holdout27 输入卡与金标原文逐字核——输入卡 asked_at 原文作「已卯年戊辰月丙午日（原文「已卯」）」、干字面「已」非天干字属实（成立面；承 DIAG-H26 F7–F9 例）；但卡面已自注原文形态、锚点五要素全在场、不计 IN（不成立面）。故部分成立。",
  "DIAG-H27 §5 旗标候选 F4", ["DIAG-H27"], []))
new.append(acc_entry("GSZ-088",
  "DIAG-H27 旗标候选 F4＋F5（R83 定案）：回 holdout27 输入卡与金标原文逐字核——F4：输入卡 asked_at 原文作「已卯年已巳月庚辰日（原文「已卯年已巳月」）」、干字面「已」非天干字属实（成立面）；但卡面已自注原文形态、锚点五要素全在场、不计 IN（不成立面）。F5：金标 grade_note 逐字载「第十四章「例三」重号之第一例（见GSZ-089登记）」——原书例号重号属实（成立面）；但台账已分号登记、本例数据无误载（不成立面）。两旨合并一例登记。故部分成立。",
  "DIAG-H27 §5 旗标候选 F4＋F5", ["DIAG-H27"], []))
new.append(acc_entry("GSZ-081",
  "DIAG-H27 旗标候选 F8（R83 定案）：回 holdout27 输入卡与金标原文逐字核——同盘异问形态属实：本例与 GSZ-084 本卦「雷天大壮」、变卦「火天大有」、动爻兄弟戌土、世父母午火、应妻财子水全同（成立面）；但两例六神排列随日辰而异、非盘面逐字全同，asked_at（戊寅年戊午月甲寅日）与所问（代占子出国考试）与 GSZ-084 各异、锚点各自在场、不计 IN、非数据误载（不成立面；DIAG「盘面逐字全同」表述本席按六神层出入照实分层登记）。故部分成立。",
  "DIAG-H27 §5 旗标候选 F8", ["DIAG-H27"], []))
new.append(acc_entry("GSZ-084",
  "DIAG-H27 旗标候选 F8（R83 定案）：回 holdout27 输入卡与金标原文逐字核——同盘异问形态属实：本例与 GSZ-081 本卦「雷天大壮」、变卦「火天大有」、动爻兄弟戌土、世父母午火、应妻财子水全同（成立面）；但两例六神排列随日辰而异、非盘面逐字全同，asked_at（戊寅年癸亥月戊寅日）与所问（代占母病）与 GSZ-081 各异、锚点各自在场、不计 IN、非数据误载（不成立面；DIAG「盘面逐字全同」表述本席按六神层出入照实分层登记）。故部分成立。",
  "DIAG-H27 §5 旗标候选 F8", ["DIAG-H27"], []))
for cid, dong in [("WHY-008","上爻兄弟卯木、二爻兄弟寅木两动"),("WHY-009","父母丑土、官鬼午火两动"),("WHY-010","初爻妻财丑土独发")]:
    new.append(acc_entry(cid,
      f"DIAG-H27 旗标候选 F6（R83 定案）：回 holdout27 输入卡与金标原文逐字核——输入卡动爻化神六亲未单列属实：本例动爻（{dong}）于卡面 chart_lines 仅载本卦六亲与动标记、化神六亲未单列，三例 predictions basis 均自注此节并降置信（DIAG-H27 §5 引 WHY-010 basis「只核地支层：丑土动化变卦初爻子水之支」）（成立面）；但金标 grade_note 逐字载「锚点在场（卦名、变卦、动爻、世应、六亲纳支、月建日辰全列）」、化神地支可由变卦爻位核得、不计 IN（不成立面）。故部分成立。",
      "DIAG-H27 §5 旗标候选 F6", ["DIAG-H27"], []))
assert len(new) == 13
assert all(a["case_id"] not in base_cases for a in new)
# acc_entry 的 suggestion 以 finding 全文嵌套过长，改写为简式（与 r82 体例一致的短式注记）
short_notes = {
 "DS-040": "验收侧新登记：自 R84 起承接本 R83 标注（DIAG-H27 F1＋M 残片旨）：按「金标 grade_note 自载污染口径复核留位属实（命主未具名、仅称曾任国家财政部长，按 low 登记、主持可复核升档；本席不改判级）＋大师断语为解释性残句属实（M1／M2 双视明指）而大意与结局大体相合可核，部分成立」登记；金标原文照录不改。",
 "DS-048": "验收侧新登记：自 R84 起承接本 R83 标注（DIAG-H27 F7）：按「双视评审 reason 对结局年份载录口径互歧属实（O1 称结局未明示火灾年份、O2 称 2008 火灾）；金标结局本身无误载、年份坐实靠大师断语 2000 年庚辰年一线，互歧属评审表述层，部分成立」登记；金标原文照录不改。",
 "QM-052": "验收侧新登记：自 R84 起承接本 R83 标注（DIAG-H27 F2）：按「干集校验代表局口径相左属实（台账作 stems 以第二局为校验代表、第三局未另列；basis 作第三局 stem_check 双 ok、第二局未单列校验）；两局盘面全载、stem_check 双 ok、锚点 present 不计 IN，部分成立」登记；金标原文照录不改。",
 "QM-058": "验收侧新登记：自 R84 起承接本 R83 标注（DIAG-H27 F3）：按「输入卡盘面巽4／离9 两宫神名原印同作「天」、疑排印误照录属实；卡面与金标均已照录登记、stem_check 全合不计 IN，部分成立」登记；金标原文照录不改。",
 "GSZ-079": "验收侧新登记：自 R84 起承接本 R83 标注（DIAG-H27 F4）：按「输入卡 asked_at 原文作「已卯日」、干字面「已」非天干字属实；卡面已自注原文形态、锚点五要素全在场不计 IN，部分成立」登记；金标原文照录不改。",
 "GSZ-088": "验收侧新登记：自 R84 起承接本 R83 标注（DIAG-H27 F4＋F5）：按「asked_at 原文「已卯年已巳月」同型字面属实＋金标 grade_note 自载原书「例三」重号第一例属实；卡面已自注、台账已分号登记、锚点五要素全在场不计 IN，部分成立」登记；金标原文照录不改。",
 "GSZ-081": "验收侧新登记：自 R84 起承接本 R83 标注（DIAG-H27 F8）：按「与 GSZ-084 同盘异问属实（本卦／变卦／动爻／世应／六亲纳支全同）；六神随日而异非逐字全同、两例 asked_at 与所问各异、锚点各自在场不计 IN，部分成立」登记；金标原文照录不改。",
 "GSZ-084": "验收侧新登记：自 R84 起承接本 R83 标注（DIAG-H27 F8）：按「与 GSZ-081 同盘异问属实（本卦／变卦／动爻／世应／六亲纳支全同）；六神随日而异非逐字全同、两例 asked_at 与所问各异、锚点各自在场不计 IN，部分成立」登记；金标原文照录不改。",
 "WHY-008": "验收侧新登记：自 R84 起承接本 R83 标注（DIAG-H27 F6）：按「输入卡动爻化神六亲未单列属实（basis 已自注降置信）；锚点全列在场、化神地支可由变卦爻位核得、不计 IN，部分成立」登记；金标原文照录不改。",
 "WHY-009": "验收侧新登记：自 R84 起承接本 R83 标注（DIAG-H27 F6）：按「输入卡动爻化神六亲未单列属实（basis 已自注降置信）；锚点全列在场、化神地支可由变卦爻位核得、不计 IN，部分成立」登记；金标原文照录不改。",
 "WHY-010": "验收侧新登记：自 R84 起承接本 R83 标注（DIAG-H27 F6）：按「输入卡动爻化神六亲未单列属实（basis 已自注「只核地支层」）；锚点全列在场、化神地支可由变卦爻位核得、不计 IN，部分成立」登记；金标原文照录不改。",
}
for a in new:
    if a["case_id"] in short_notes: a["manifest_carry_suggestion"] = short_notes[a["case_id"]]

# ---------- special_checks 承接 + 新增 ----------
sc = list(r82["special_checks"])
assert len(sc) == 39
sc.append({
 "item": "特别核查㊵（R83）：R82 附则承接建议 3 件于 R83 manifest 落实对勘与评审落实事实",
 "conclusion": "层文本对勘：_r82_carryover_notes_addendum 共 3 件（LY-406／LY-446／LY-524），层文本与 case-annotations-r82.json 对应条 manifest_carry_suggestion 逐字全等 3/3。评审传递面：3 件 carry_note 全数以 [R82-addendum] 段入 R83 评审包（落盘脚本逐件断言在场）。评审落实（以双视 reason 为据，照 R82 对 LY-416／LY-423 逗号件同型判例：reason 未载逗号／截断要点、仅按主结局常规评分者登记未见落实）：已落实 0 件、未见落实 3 件——LY-406（X「甲戌出空即愈合」、Y「迟险一节未分载」，均未涉逗号要点）、LY-446（X／Y 均按酉日天变戌日而雨评分、未涉逗号要点）、LY-524（双视均按次日愈评分、未涉逗号要点；双视另明载「附子对应未明字」属 R64 并行旧旨、与本层注记各旨独立）。",
 "evidence": "落盘脚本逐件断言：层键集 3 件、层文本 3/3 全等；评审包 [R82-addendum] 3/3 在场；3 件双视 reason 引文逐字在盘且「逗号／截断／尾逗」字样不在场断言通过。",
 "scope_note": "对勘只登记、不改 manifest 与分数任一侧。"})
sc.append({
 "item": "特别核查㊶（R83）：平台旗标定案总登记（FREEZE 三件＋逗号收尾全集续接＋reason 数据形态注记续接）",
 "conclusion": "FREEZE-r83 tradition 首行旗标候选 3 件照主持裁定落案：AS-307 形式旗标成立——与 R80／R81 同例同型（卡面 tradition＝astrology、basis 首行误述未标注、实际方法与卡面实质一致、断案方向不受影响），照历轮成例只登记不改预测，本册 AS-307 条目已以部分成立在册（registered_round＝80）、同旨续接、条目不动；LY-001／ZY-001 不成立（检查器关键词误报）——两件不在 134 件内，按 R80 LR3-004／LR3-104 判例新立不成立条目入册（只登记不入层）。平台逗号收尾全集经 R83 manifest 复扫仍 20 件、全数已在册，同旨续接只登记。双视 reason 数据形态注记同旨续接（均已在册、条目不动）：LY-452 逗号收尾疑截断（Y reason 明载）、LR2-016 编者注细项未复核（X／Y 明载、属基线六处）、LY-524 附子对应未明字（X／Y 明载、R64 并行旧旨）、LY-441 晴否含混、YM-069 结局残句、YY2-004 残盘降格、LY-508 登记层同旨；Y 席 reason 以「（登记层）」引述既有承接注记者另有 LY-533／LY-436／LY-628／BQ-021／BQ-025／LY-220／LY-011／LY-329／LR3-101／YM-030 十件，均已在册同旨续接。AS-014 一件 Y reason 载「（登记层）」字样、其所指为追回程度未载之评分细项、非数据形态旗标且本册无条，不立件、只登记备查。本轮 R83 judging 目录内无独立 FLAGS 回传文件（按授权精确文件名开读 judgeX／judgeY-merged 与 FREEZE 为据），平台旗标候选以 FREEZE 裁定与双视 reason 明载形态注记为全集口径，照实登记。",
 "evidence": "落盘脚本断言：FREEZE 裁定引文逐字在盘；LY-001／ZY-001 anon 经 host-mapping 对位（P3-5d21f235／P3-8a775d85）；逗号收尾扫描 20 件与 R82 全集全等；续接诸件 reason 引文逐字在盘。",
 "scope_note": "续接件只登记、不重裁、不改条目；新立不成立件只及标注，不改分数。"})
sc.append({
 "item": "特别核查㊷（R83）：DIAG-H27 旗标候选 F1–F8 定案与验收评审旗标（DS-040 大师断语残片）定案",
 "conclusion": "F1–F8 逐件回 holdout27 输入卡／金标／封存日志核后定案：按 case 合并新登记 11 件、全部部分成立（DS-040 合 F1＋M 残片旨、GSZ-088 合 F4＋F5、GSZ-081／GSZ-084 各承 F8、WHY-008／WHY-009／WHY-010 各承 F6）：各件或卡面／金标形态出入属实而自注在盘、锚点在场不计 IN，或口径互歧／相左属实而数据本身无误载；F1 为封存席自标复核留位、本席不改判级；F8 本席另核得两例六神排列随日辰而异、DIAG「盘面逐字全同」表述按六神层出入分层登记。验收评审旗标除 DS-040 残片一件（H27M-c032fdad，M1／M2 双视明指）外，四席 reason 全文关键词复扫无其他数据形态旗标。",
 "evidence": "落盘脚本逐件引文断言：金标 grade_note／master_prediction／outcome_record、输入卡 asked_at／board_verbatim／chart_lines、封存日志 §二台账注记、O1／O2 与 M1／M2 reason 原句均逐字在盘；anon 经 acceptance host-mapping ours／master 侧逐件对位。",
 "scope_note": "验收侧定案只及标注与承接建议，不改金标与任何分数。"})
sc.append({
 "item": "特别核查㊸（R83）：指令性字样特别核查基线六处复核（承 R82 附则 §四基线）",
 "conclusion": "基线六处经 R83 manifest 与 R83 评审包盘上逐处回读在册、形态未变：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）逐字在场；LR2-016 manifest editor_note 一处在 _r56_lr2016_split 分列层、原文逐字与基线全等；LR2-016 评审包 editor_note 层一处在 R83 评审包（packet4／packetB，anon P3-e46de48c）中以独立 editor_note 字段逐字在场。本轮评审实触两处：LR2-016 双视 reason 均明载编者注「甲戌日巳时」细项未复核、按未复核处理；LY-204 评审包 outcome_record 含旧注「勿以此斷」在盘（packet2／packetA）、双视 reason 均按功名实绩评分、未涉旧注字样。本轮新增同型件：无——manifest 全量扫描「勿以此」字样仅 LY-204 一件、与基线第四处同件同旨续接，不另立号。",
 "evidence": "脚本逐字断言：四例字样均在 cases 本体；「勿以此」全量扫描恰 1 件（LY-204）；editor_note 全句在分列层与评审包字段逐字在场；host-mapping 对位 P3-e46de48c＝LR2-016、P3-7e0064c3＝LY-204（R83 种子）。",
 "scope_note": "各席与本席均按数据处理、不作指令；只登记、不改文本。"})
sc.append({
 "item": "特别核查㊹（R83）：待核四件维持登记与本轮触及关联；CZ-QX 维持 16",
 "conclusion": "BZ-029（俞大维卒年待核＋旗标错配线索）／BZ-040（许世英享年待核）／LY-537（「申予日」衍字疑）／YM-070（「甲寅旬」挂起）四件维持原登记，本轮不核查、不关闭。LY-537 本轮被双视 reason 触及（X 明载「结局申予日字样含混」、Y 径作「果于申予日归」评分），只登记关联、不并案、不改其未核状态；YM-070 本轮被双视 reason 触及（X／Y 均载结局『同行都下』语义未明），与其在册未核条目同旨、维持挂起；BZ-029／BZ-040 本轮双视 reason 均按主结局常规评分、无待核事项新触及登记。CZ-QX 维持 16 只登记、无增减（平台定稿 families.liuyao_zh n＝16；holdout27 本集无测字段）。",
 "evidence": "R83 manifest cases[LY-537] 仍载「申予日」字样、cases[YM-070] 结局在盘；LY-537／YM-070 未核条目随 134 件全量承接在册；final-scores.json analysis_r83 families.liuyao_zh n＝16 断言通过；DIAG-H27 §0 明载本集无测字段。",
 "scope_note": "待核件无盘外独立史源不裁。"})

counts = {
 "base_file": "data/case-annotations-r82.json", "base_cases_total": 134,
 "base_verdicts": {"成立":12,"部分成立":114,"不成立":6,"未核":2},
 "carryover_check_r82_addendum": {"layer": "_r82_carryover_notes_addendum", "items": 3,
   "layer_text_verbatim": 3, "layer_text_prefix_only": [],
   "judging_implemented": [], "judging_not_seen": ["LY-406","LY-446","LY-524"]},
 "freeze_r83_flag_rulings": {"AS-307": "成立（形式旗标；同例同型续接，部分成立条目在册不动）",
   "LY-001": "不成立（新立）", "ZY-001": "不成立（新立）"},
 "platform_comma_cases_r83": 20, "continuation_cases_r83": 20,
 "pending_touch_cases_r83": ["LY-537","YM-070"],
 "new_registrations_r83": 13,
 "new_partial_cases_r83": ["DS-040","DS-048","QM-052","QM-058","GSZ-079","GSZ-088","GSZ-081","GSZ-084","WHY-008","WHY-009","WHY-010"],
 "new_not_upheld_cases_r83": ["LY-001","ZY-001"],
 "diag_h27_flag_candidates": {"F1":"DS-040","F2":"QM-052","F3":"QM-058","F4":"GSZ-079/GSZ-088","F5":"GSZ-088","F6":"WHY-008/WHY-009/WHY-010","F7":"DS-048","F8":"GSZ-081/GSZ-084"},
 "acceptance_judge_flag_extra": {"H27M-c032fdad": "DS-040（大师断语残片，并入 F1 件）"},
 "cases_total": 147, "verdicts": {"成立":12,"部分成立":125,"不成立":8,"未核":2}}

out = {
 "_provenance": "R83 数据席（附则承接对勘＋annotations 全量承接与本轮新定案，独立席位，不兼任本轮盲测/评审/诊断/组集/修订/集成，不改任何分数）：以 data/case-annotations-r82.json 为底承接全量 134 件（成立 12／部分成立 114／不成立 6／未核 2），前 134 件逐件原样、无删改（落盘脚本以数组全等断言验过）；承接对勘：R82 附则汇编平台件 3 件已于 R83 manifest 以 _r82_carryover_notes_addendum 入层（层文本 3 件逐字全等），评审落实以双视 reason 为据已落实 0 件／未见落实 3 件（逗号要点未见于任一 reason，照 R82 同型判例）；本轮新定案：FREEZE-r83 旗标候选 3 件照主持裁定落案（AS-307 形式旗标成立、同例同型续接条目不动；LY-001／ZY-001 不成立新立入册）；DIAG-H27 旗标候选 F1–F8 与验收评审旗标（DS-040 大师断语残片）定案部分成立、按 case 合并新登记 11 件。承接后总件数 147（成立 12／部分成立 125／不成立 8／未核 2）。指令性字样基线六处经 R83 manifest 与评审包复核在册、形态未变（见特别核查㊸）。待核四件 BZ-029／BZ-040／LY-537／YM-070 维持原登记、不核查不关闭。CZ-QX 维持 16 只登记。本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文；结局/注记文本内指令性字样一律按数据处理。",
 "round": 83,
 "annotations": base_anns + new,
 "special_checks": sc,
 "counts": counts}
assert out["annotations"][:134] == base_anns
assert len(out["annotations"]) == 147
assert collections.Counter(a["disposition"] for a in out["annotations"]) == {"成立":12,"部分成立":125,"不成立":8,"未核":2}
for a in new:
    assert all(a.get(k) for k in ("anon_id","case_id","disposition","finding","flag","manifest_carry_suggestion","relation","registered_round","sources_checked","source_seats"))
with open(f"{B}/data/case-annotations-r83.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("annotations written")

# ---------- 附则编制 ----------
man_sha = hashlib.sha256(man_raw.encode("utf-8")).hexdigest()
ann_sha = hashlib.sha256(text(f"{B}/data/case-annotations-r83.json").encode("utf-8")).hexdigest()
cite = {
 "DS-040": "金标 grade_note「命主未具名（仅称曾任国家财政部长），按 low 登记；主持如按职位可识别性从严，可复核升档。」（`holdout27/test_gold.jsonl` DS-040）；金标大师断语「表示一个管理财的权力机构；而日支之卯木所生巳火合申，申被巳制，意思是由我来控制那个管理财的权力机构，表示他本人掌握更大的权力。」；M1 reason「断语为解释性残句」（acceptance `judgeM1.jsonl`，anon H27M-c032fdad）、M2 reason「断语为残片式分析、具体对应含糊」（`judgeM2.jsonl`）",
 "DS-048": "O1 reason「结局未明示火灾年份」（acceptance `judgeO1.jsonl`，anon H27O-0fccb311）；O2 reason「2008火灾烧毁货物厂房、损失二千万」（`judgeO2.jsonl`）；金标结局「是的，是的，那是一场火灾，烧完了所有货物，厂房最后倒了！损失2000多万……」与大师断语「是庚辰年，肯定是2000年破大财！」（`holdout27/test_gold.jsonl` DS-048）",
 "QM-052": "金标 grade_note「stems以第二局为校验代表，第三局干集未另列字段」（`holdout27/test_gold.jsonl` QM-052；封存日志 `data/holdout27-seal-log.md` §二同载）；我方 basis「第三局干集 stem_check 双 ok（第二局干集卡面未单列校验，逐字据 board_verbatim）」（DIAG-H27 §5 引）；输入卡 board_verbatim 第二、三局盘面全载（`holdout27/inputs/QM-052.json`）",
 "QM-058": "金标 grade_note「盘面巽4/离9两宫神名原印同作「天」，疑排印误，照录」（`holdout27/test_gold.jsonl` QM-058）；输入卡 board_verbatim「巽4｜天 杜戊 心丙」「离9｜天 景壬 蓬辛」（`holdout27/inputs/QM-058.json`）",
 "GSZ-079": "输入卡 asked_at「已卯年戊辰月丙午日（原文「已卯」）」（`holdout27/inputs/GSZ-079.json` anchors）",
 "GSZ-088": "输入卡 asked_at「已卯年已巳月庚辰日（原文「已卯年已巳月」）」（`holdout27/inputs/GSZ-088.json` anchors）；金标 grade_note「第十四章「例三」重号之第一例（见GSZ-089登记）」（`holdout27/test_gold.jsonl` GSZ-088）",
 "GSZ-081": "输入卡本卦「雷天大壮」／变卦「火天大有」／动爻兄弟戌土／世父母午火／应妻财子水、asked_at「戊寅年戊午月甲寅日」、question「测子出国考试可通过否（某女代占）」（`holdout27/inputs/GSZ-081.json`；与 GSZ-084 卡对勘，六神排列相异）",
 "GSZ-084": "输入卡本卦「雷天大壮」／变卦「火天大有」／动爻兄弟戌土／世父母午火／应妻财子水、asked_at「戊寅年癸亥月戊寅日」、question「测母亲病（某女代占）」（`holdout27/inputs/GSZ-084.json`；与 GSZ-081 卡对勘，六神排列相异）",
 "WHY-008": "输入卡 chart_lines 动爻行「兄弟卯木○ 应」「兄弟寅木×」、化神六亲未单列（`holdout27/inputs/WHY-008.json`）；金标 grade_note「锚点在场（卦名、变卦、动爻、世应、六亲纳支、月建日辰全列）」（`holdout27/test_gold.jsonl` WHY-008）",
 "WHY-009": "三例 predictions basis 自注卡面未载动爻化神六亲（DIAG-H27 §5 F6）；金标 grade_note「锚点在场（卦名、变卦、动爻、世应、六亲纳支、月建日辰全列）」（`holdout27/test_gold.jsonl` WHY-009）",
 "WHY-010": "输入卡 chart_lines 动爻行「妻财丑土×」、化神六亲未单列（`holdout27/inputs/WHY-010.json`）；我方 basis「只核地支层：丑土动化变卦初爻子水之支」（DIAG-H27 §5 引）；金标 grade_note「锚点在场（卦名、变卦、动爻、世应、六亲纳支、月建日辰全列）」",
}
L = []
L.append("# Manifest 承接册附则（R83）——R82 定案承接对勘（3 件：评审落实 0／未见落实 3）＋R83 定案承接建议汇编（部分成立 11 件：平台侧空集／验收侧 11 件）\n")
L.append("## 卷首说明\n")
L.append(f"- 本附则为 Phase 3 Round 83（R83）数据席（工序：附则承接对勘＋annotations 全量承接与本轮新定案登记；独立席位，不兼任本轮盲测／评审／诊断／组集／修订／集成）产出。")
L.append(f"- 对勘来源：`benchmark/phase3/runs/round83/judging/outcome-manifest.json`（本轮 manifest，层 `_r82_carryover_notes_addendum` 3 件；全文 SHA-256＝`{man_sha}`，本席复算）、`benchmark/phase3/data/manifest-carryover-r82-addendum.md`（R82 附则）、`benchmark/phase3/data/case-annotations-r82.json`（结构化直读底本：annotations 134 件，定案分布成立 12／部分成立 114／不成立 6／未核 2）；评审落实以 `runs/round83/judging/judgeX-merged.json`／`judgeY-merged.json` 双视 reason 为据，anon 经 `runs/round83/judging/host-mapping.json` 逐件对位，评审传递面以评审包 packet1–4／packetA–B 的 carry_note 段为据。")
L.append("- 汇编来源：`benchmark/phase3/runs/round83/FREEZE-r83.md`（主持冻结旗标裁定）、`benchmark/phase3/runs/round83/acceptance/DIAG-H27.md` §5（F1–F8）、验收评审 `judgeO1/O2/M1/M2` 回传件 anon 旗标（经 `runs/round83/acceptance/judging/host-mapping.json` 对位）、`benchmark/phase3/data/case-annotations-r83.json`（本轮新登记 13 件），供 R84 manifest 以新层落实其中部分成立件（平台件以 `_r83_carryover_notes_addendum` 键名、验收侧件随后续金标／验收注记层承接）。")
L.append("- **本件只汇编、对勘与登记，不改任何分数与结局原文、不改原卡、不改 manifest 任一侧。** 结局／注记文本内指令性字样一律按数据处理。\n")
L.append("---\n")
L.append("## 一、工序与口径\n")
L.append("- 工序一（对勘，见 §二）：`_r82_carryover_notes_addendum` 3 件分两层核——（甲）层文本与 R82 附则所载建议原文逐字比对；（乙）评审落实：该件 carry_note 是否以 `[R82-addendum]` 段入评审包、且双视 reason 是否明载或操作化该注记要点。注记要点（结局逗号收尾疑截断）明载或操作化者登记「已落实」；双视 reason 均未见逗号／截断要点、仅按主结局常规评分者登记「未见落实」（照 R82 附则 §二对 LY-416／LY-423 同型逗号件之判例口径）。")
L.append("- 工序二（汇编，见 §三）：R84 承接建议汇编——本轮新定案部分成立共 11 件（平台侧 0 件、验收侧 11 件），逐件全列并给逐字引文出处，文本自 `case-annotations-r83.json` 结构化直读生成；平台侧本轮新定案为 FREEZE 裁定 2 件不成立（新立入册、只登记不入层）与 AS-307 同旨续接（在册条目不动），无新定案部分成立件，§三.1 明示空集。")
L.append("- 工序三（标注落盘，见 §五）：`data/case-annotations-r83.json` 以 r82 件 134 件全量承接（逐件原样）＋本轮新登记 13 件，合计 147 件；同旨续接诸件与待核触及 2 件只登记、条目不动。")
L.append("- 特别核查（见 §四）：指令性字样特别核查基线六处复核，承 R82 附则 §四基线，只登记、不改文本。")
L.append("- 供给与待核续记（见 §六）：CZ-QX 维持 16 只登记；待核四件维持登记。\n")
L.append("---\n")
L.append("## 二、对勘：R82 附则 3 件于 R83 manifest 入层与评审落实（已落实 0／未见落实 3）\n")
L.append("### 2.1 层实况登记（盘上直读）\n")
L.append("- R83 manifest 含键 `_r82_carryover_notes_addendum`，共 **3 件**，键集与 R82 附则 §三平台件汇编清单（LY-406／LY-446／LY-524）全等；层文本与 `case-annotations-r82.json` 对应条 `manifest_carry_suggestion`（同文亦载 R82 附则 §三 N1–N3）**逐字全等 3/3**，出入 0 件。")
L.append("- 评审传递面：3 件 carry_note 全数以 `[R82-addendum]` 段入 R83 评审包（packet1／packet2／packet3 及 packetA／packetB 对应件，落盘脚本逐件断言 3/3 在场）。\n")
L.append("### 2.2 逐件评审落实对勘（3 件，以双视 reason 为据）\n")
L.append("| # | case_id | anon_id（R83） | 评审 reason 逐字据（节录） | 结论 |")
L.append("|---|---|---|---|---|")
rows = [
 ("LY-406", f"X：「{R['LY-406'][0]}」；Y：「{R['LY-406'][1]}」——双视均按甲戌出空即愈之主结局评分，未见「截断／逗号」字样", "未见落实"),
 ("LY-446", f"X：「{R['LY-446'][0]}」；Y：「{R['LY-446'][1]}」——双视均按酉日天变、戌日而雨之主结局评分，未见「截断／逗号」字样", "未见落实"),
 ("LY-524", f"X：「{R['LY-524'][0]}」；Y：「{R['LY-524'][1]}」——双视均按次日愈之主结局评分，未见「截断／逗号」字样；双视所载「附子对应未明字」属 R64 并行旧旨、非本层注记要点", "未见落实"),
]
for i,(cid,ev,concl) in enumerate(rows,1):
    L.append(f"| {i} | {cid} | {rev[cid]} | {ev} | {concl} |")
L.append("")
L.append("- 对勘结论：**已落实 0 件**、**未见落实 3 件**（LY-406／LY-446／LY-524）。共同形态与 R82 未见落实 8 件同型：注记已入层、入评审包 carry_note，但双视 reason 只按主结局常规评分、未载注记所限定之逗号收尾疑截断要点；本席只登记事实，不改分数，是否在后续轮次强化评审口径留主持。\n")
L.append("---\n")
L.append("## 三、R84 承接建议汇编：R83 本轮新定案（部分成立 11 件逐件全列）\n")
L.append("- 落实键名写定：自 R84 manifest 起以 `_r83_carryover_notes_addendum` 键名落实本节平台件建议注记原文；验收侧件随后续金标／验收注记层承接、文本照录于本节。\n")
L.append("### 3.1 平台侧\n")
L.append("- **空集**：本轮平台侧无新定案部分成立件。平台侧本轮定案另有着落、不入本汇编：FREEZE-r83 裁定 LY-001／ZY-001 不成立 2 件已新立入册（只登记不入层，见 §五）；AS-307 形式旗标成立照裁定落案——与 R80／R81 同例同型，其部分成立条目已在册（registered_round＝80），本轮同旨续接、条目不动，不重复立件。LY-001／ZY-001 二件经核不在 134 件承接册内，故按不成立新立处理（承 R80 LR3-004／LR3-104 判例），不适用「已在册照原状态承接」一款。\n")
L.append("### 3.2 验收侧（DIAG-H27 F1–F8＋验收评审旗标，11 件）\n")
acc_new = [a for a in new if a["case_id"] in short_notes]
for i, a in enumerate(acc_new, 1):
    L.append(f"#### N{i}. {a['case_id']}\n")
    L.append(f"- case_id：{a['case_id']}")
    L.append(f"- anon_id：{a['anon_id']}（ours 侧；master 侧 {amaster[a['case_id']]})" if a["case_id"]=="DS-040" else f"- anon_id：{a['anon_id']}")
    L.append(f"- 定案类别：部分成立（registered_round＝83；新登记（R83，验收侧 DIAG-H27））")
    L.append(f"- 核对结论：{a['finding']}")
    L.append(f"- 逐字引文出处：{cite[a['case_id']]}")
    L.append(f"- 承接注记建议文本（原文）：「{a['manifest_carry_suggestion']}」\n")
L.append("---\n")
with open(f"{B}/data/manifest-carryover-r83-addendum.md", "w", encoding="utf-8") as f:
    f.write("\n".join(L) + "\n")
print("addendum part 1 written, lines:", len(L))

# ---------- 附则 §四–§六（续写） ----------
L2 = []
L2.append("## 四、指令性字样特别核查基线六处对勘（承 R82 附则 §四基线）\n")
L2.append("- 基线构成：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）＋LR2-016 manifest editor_note 一处＋LR2-016 评审包 editor_note 层一处，共六处、分三层。本轮自 `runs/round83/judging/outcome-manifest.json` 与 R83 评审包盘上逐处回读原文复核，**只登记、不改文本**；各席与本席均按数据处理、不作指令。\n")
L2.append("| case_id | 基线字样（按数据引录） | 本轮在盘形态 |")
L2.append("|---|---|---|")
L2.append("| BZ-036 | 结局含「盲测比对须注」 | 在册：在场、形态未变 |")
L2.append("| BZ-042 | 结局含「（盲测比对时以格局大富一项为主）」 | 在册：在场、形态未变 |")
L2.append("| BZ-105 | 结局含「使用时须分开统计」 | 在册：在场、形态未变 |")
L2.append("| LY-204 | 结局旧注层含「勿以此斷」 | 在册：在场、形态未变（评审包 packet2／packetA outcome_record 同字在盘；本轮双视 reason 均按功名实绩评分、未涉旧注字样，只登记） |")
L2.append("")
L2.append("- LR2-016 manifest editor_note 一处：所在 manifest `_r56_lr2016_split` 分列层，本轮在盘原文逐字与基线全等。")
L2.append("- LR2-016 评审包 editor_note 层一处：R83 评审包（packet4／packetB，anon P3-e46de48c）中以独立 `editor_note` 字段逐字在场、与 manifest 分列层全等，另列一类、不并入 cases 本体基线计数；本轮双视 reason 均明载编者注「甲戌日巳时」细项未复核、按未复核处理——评审实触一处，只登记。")
L2.append("- 结论：基线六处经 R83 盘上逐处回读在册、形态未变，出入 0 处。本轮有评审实触记录者 1 处（LR2-016）。本轮新增同型件：**无**——manifest 全量扫描「勿以此」字样仅 LY-204 一件，与基线第四处同件、同旨续接，不另立号。本席只登记、不改任何文本。\n")
L2.append("---\n")
L2.append("## 五、annotations 落盘断言与同旨续接登记\n")
L2.append("### 5.1 annotations 落盘断言（工序三）\n")
L2.append("- 底本：`data/case-annotations-r82.json` annotations 134 件（成立 12／部分成立 114／不成立 6／未核 2），全量承接、逐件原样、无删改（落盘脚本以 annotations 数组前 134 件全等断言验过）。")
L2.append("- 新增登记：**13 件**（平台 FREEZE 不成立新立 2 件：LY-001／ZY-001；验收侧 DIAG-H27 F1–F8 与评审残片旨按 case 合并 11 件、全部部分成立，见 §三.2）——落盘 `data/case-annotations-r83.json` annotations **147 件＝134＋13**（成立 12／部分成立 125／不成立 8／未核 2），各新件 `registered_round＝83`、字段完整（落盘脚本逐件断言），counts 相应更新，回读 JSON 可解析断言通过。")
L2.append("- 平台旗标定案构成：FREEZE 候选 3 件（AS-307 同旨续接 1 件、条目不动；LY-001／ZY-001 不成立新立 2 件）；逗号收尾全集经 R83 manifest 复扫 20 件、全数已在册同旨续接只登记；双视 reason 数据形态注记同旨续接 8 件（LY-452／LR2-016／LY-524／LY-441／YM-069／YY2-004／LY-508＋LY-204 基线件）与「（登记层）」引述续接 10 件（LY-533／LY-436／LY-628／BQ-021／BQ-025／LY-220／LY-011／LY-329／LR3-101／YM-030），均条目不动；AS-014 引述一件为评分细项、不立件只登记（见特别核查㊶）。待核触及 2 件（LY-537／YM-070，见 §五.2）。本轮 R83 judging 目录内无独立 FLAGS 回传文件，平台候选以 FREEZE 裁定与双视 reason 明载形态注记为全集口径，照实登记。")
L2.append("- special_checks 承接 r82 三十九件并新增 R83 五件（㊵ R82 承接 3 件落实对勘；㊶ 平台旗标总登记；㊷ DIAG-H27 F1–F8 与验收评审旗标定案；㊸ 指令性字样基线六处复核；㊹ 待核四件维持与 CZ-QX），合计 44 件。\n")
L2.append("### 5.2 R83 确认的待核维持清单（四件，维持挂起、不核查不关闭）\n")
L2.append("| case_id | 状态登记（承 R82 附则 §五.2 口径续记） |")
L2.append("|---|---|")
L2.append("| BZ-029 | 俞大维卒年待核＋旗标错配线索，维持原登记、不裁；不入 annotations；本轮双视 reason 按主结局常规评分、无新触及 |")
L2.append("| BZ-040 | 许世英享年待核，维持原登记、不裁；不入 annotations；本轮双视 reason 按主结局常规评分、无新触及 |")
L2.append("| LY-537 | 「申予日」衍字疑，维持未核原登记；本轮被双视 reason 触及（X 明载「结局申予日字样含混」、Y 径作「果于申予日归」评分），只登记关联、不并案、不改待核状态；以未核条目随承接在 `case-annotations-r83.json` 内 |")
L2.append("| YM-070 | 「甲寅旬」出处待核，维持挂起；本轮被双视 reason 触及（X／Y 均载结局『同行都下』语义未明、与在册未核条目同旨），只登记关联、不改待核状态；以未核条目随承接在 `case-annotations-r83.json` 内 |\n")
L2.append("---\n")
L2.append("## 六、供给台账续记（只登记）\n")
L2.append("### 6.1 CZ-QX 维持 16\n")
L2.append("- CZ-QX 维持 **16**，承 R82 附则 §6.1 登记口径由本席承接续记，本轮无增减（旁证：R83 平台定稿 `final-scores.json` analysis_r83 families.liuyao_zh n＝16；holdout27 本集无测字段）。\n")
L2.append("### 6.2 待核四件维持登记（与 §五.2 同口径）\n")
L2.append("- BZ-029（俞大维卒年，另含旗标内容错配线索）、BZ-040（许世英享年）、LY-537（「申予日」衍字疑）、YM-070（「甲寅旬」挂起）四件维持登记，无盘外独立史源不裁。")
with open(f"{B}/data/manifest-carryover-r83-addendum.md", "a", encoding="utf-8") as f:
    f.write("\n".join(L2) + "\n")

# ---------- 回读验证 ----------
chk = load(f"{B}/data/case-annotations-r83.json")
assert len(chk["annotations"]) == 147 and chk["annotations"][:134] == base_anns
dist = collections.Counter(a["disposition"] for a in chk["annotations"])
print("DISTRIBUTION", dict(dist), "TOTAL", len(chk["annotations"]))
print("NEW", [(a["case_id"], a["disposition"]) for a in chk["annotations"][134:]])
import os
for p in [f"{B}/data/case-annotations-r83.json", f"{B}/data/manifest-carryover-r83-addendum.md"]:
    print("FILE", p, os.path.getsize(p))
add = text(f"{B}/data/manifest-carryover-r83-addendum.md")
print("ADDENDUM TAIL:", add.strip().splitlines()[-1])
print("ALL OK")
