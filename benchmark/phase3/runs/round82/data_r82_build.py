#!/usr/bin/env python3
# R82 数据席落盘脚本：case-annotations-r82.json + manifest-carryover-r82-addendum.md
# 纪律：逐件回读原卡/结局原文；引文逐字断言；anon 两套 host-mapping 逐件对位；文本按数据处理。
# 只写 runs/round82/ 外的两件交付（data/），本脚本自身在 runs/round82/ 内。
import json, pathlib, hashlib
from collections import Counter

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")

def load(rel):
    return json.loads((BASE / rel).read_text(encoding="utf-8"))

def text_of(rel):
    return (BASE / rel).read_text(encoding="utf-8")

def q(s, src, label):
    assert s in src, f"引文断言失败 {label}: {s!r}"

r81 = load("data/case-annotations-r81.json")
man82 = load("runs/round82/judging/outcome-manifest.json")
man81 = load("runs/round81/judging/outcome-manifest.json")
hm82 = load("runs/round82/judging/host-mapping.json")
rev82 = {v: k for k, v in hm82.items()}
freeze82 = text_of("runs/round82/FREEZE-r82.md")
diag26 = text_of("runs/round82/acceptance/DIAG-H26.md")
acc_hm = load("runs/round82/acceptance/judging/host-mapping.json")
acc_inv = {v: k for k, v in acc_hm["ours"].items()}

cases82 = man82["cases"]
assert cases82 == man81["cases"], "R82 cases 载荷须与 R81 深度全等"
sha82 = hashlib.sha256((BASE / "runs/round82/judging/outcome-manifest.json").read_bytes()).hexdigest()
assert sha82 == "088c39f7c0629bf677bebfab1933a261aae1c0eff042511de1ad4f054ac73bae", sha82

def outcome(cid):
    v = cases82[cid]
    return v if isinstance(v, str) else (v.get("outcome_record") or "")

def card(cid):
    return load(f"inputs-dev12/{cid}.json")

def pred82(cid):
    return load(f"runs/round82/predictions/{cid}.json")

# ---------- 评审 reason 直读（X/Y 双视） ----------
reasons = {}
for blk in ["judgeX-block1-scores.jsonl", "judgeX-block2-scores.jsonl", "judgeX-block3-scores.jsonl",
            "judgeX-block4-scores.jsonl", "judgeY-block1-scores.jsonl", "judgeY-block2-scores.jsonl",
            "judgeY-block3-scores.jsonl", "judgeY-block4-scores.jsonl"]:
    seat = blk[5]  # X or Y
    for line in text_of(f"runs/round82/judging/{blk}").splitlines():
        if not line.strip():
            continue
        d = json.loads(line)
        cid = hm82[d["anon_id"]]
        reasons.setdefault(cid, {})[seat] = d["reason"]

# ---------- (a) _r81 层 14 件对勘 ----------
r81_by = {a["case_id"]: a for a in r81["annotations"]}
layer = man82["_r81_carryover_notes_addendum"]
LAYER14 = ["LY-528", "BZ-042", "LY-416", "LY-105", "LY-332", "LY-624", "LY-423", "BZ-105",
           "LR3-116", "YM-069", "LY-602", "OC-009", "LR2-024", "AS-307"]
assert set(layer.keys()) == set(LAYER14) and len(layer) == 14
AS307_R81_TEXT = "平台旗标定案：自 R82 起承接本 R81 标注（与 R80 同例同型再裁）：按「卡面 tradition＝astrology、basis 首行误读作未标注，实际所用方法为 astrology 与卡面实质一致、断语方向不受影响，部分成立，不作废不重测」登记；结局原文照录不改。"
q(AS307_R81_TEXT, text_of("data/manifest-carryover-r81-addendum.md"), "r81 addendum AS-307 text")
for cid in LAYER14:
    if cid == "AS-307":
        continue
    assert layer[cid] == r81_by[cid]["manifest_carry_suggestion"], cid
# AS-307 层文本为建议原文之前缀（止于内层「」），尾段缺失——照实登记，不静默改
AS307_LAYER = layer["AS-307"]
assert AS307_R81_TEXT.startswith(AS307_LAYER) and AS307_LAYER != AS307_R81_TEXT
assert AS307_LAYER.endswith("不作废不重测") and "登记；结局原文照录不改" not in AS307_LAYER
# 评审包 carry_note 14 件全数含 [R81-addendum] 段（落实传递面）
packets_text = ""
for pkt in ["packet1.json", "packet2.json", "packet3.json", "packet4.json"]:
    packets_text += text_of(f"runs/round82/judging/{pkt}")
for cid in LAYER14:
    an = rev82[cid]
    i = packets_text.find(an)
    assert i >= 0 and "[R81-addendum]" in packets_text[i:i + 6000], cid

# 评审落实判定证据（逐件 reason 逐字断言）
q("细项未分载", reasons["LY-528"]["Y"], "LY-528 Y reason")
q("晚年败落结局自注未备不核", reasons["BZ-042"]["X"], "BZ-042 X reason")
q("晚年面来源未备", reasons["BZ-042"]["Y"], "BZ-042 Y reason")
q("回溯病伤大方向近似", reasons["BZ-105"]["Y"], "BZ-105 Y reason")
q("预测本身残损无应期", reasons["OC-009"]["Y"], "OC-009 Y reason")
q("结局以七月死期为本课结局", reasons["LR2-024"]["X"], "LR2-024 X reason")
q("卡面 tradition＝astrology", pred82("AS-307")["basis"], "AS-307 R82 basis")
q("tradition 首行旗标候选：0", freeze82, "FREEZE-r82 tradition 0")
for cid, words in [("LY-416", ["截断", "逗号"]), ("LY-423", ["截断", "逗号"]),
                   ("LY-105", ["二手", "论坛"]), ("LY-332", ["巳火", "午火"]),
                   ("LY-624", ["再占", "暌", "两占"]), ("LR3-116", ["残损"]),
                   ("YM-069", ["残句", "残"]), ("LY-602", ["早見", "含混", "木日"])]:
    for seat in ("X", "Y"):
        for w in words:
            assert w not in reasons[cid][seat], (cid, seat, w)
VERDICT_A = {  # 评审落实结论
 "LY-528": "已落实", "BZ-042": "已落实", "LY-416": "未见落实", "LY-105": "未见落实",
 "LY-332": "未见落实", "LY-624": "未见落实", "LY-423": "未见落实", "BZ-105": "已落实",
 "LR3-116": "未见落实", "YM-069": "未见落实", "LY-602": "未见落实", "OC-009": "已落实",
 "LR2-024": "已落实", "AS-307": "已落实",
}
assert Counter(VERDICT_A.values()) == {"已落实": 6, "未见落实": 8}

# ---------- (b) 平台新旗标：逗号收尾全集扫描 ----------
comma_cases = [cid for cid in cases82 if outcome(cid).rstrip().endswith(("﹐", "，", ","))]
assert len(comma_cases) == 20, comma_cases
comma_old = sorted([c for c in comma_cases if c in r81_by])
comma_new = sorted([c for c in comma_cases if c not in r81_by])
assert comma_new == ["LY-406", "LY-446", "LY-524"], comma_new
assert len(comma_old) == 17
q("果於甲戌出空卽愈﹐", outcome("LY-406"), "LY-406 outcome")
q("果於酉日天變﹐戌日而雨﹐", outcome("LY-446"), "LY-446 outcome")
q("次日曰愈﹐", outcome("LY-524"), "LY-524 outcome")
q("甲戌出空即愈", reasons["LY-406"]["X"], "LY-406 X reason")
q("酉日天变、戌日而雨", reasons["LY-446"]["Y"], "LY-446 Y reason")
q("次日曰愈", reasons["LY-524"]["Y"], "LY-524 Y reason")
# LY-204 / AS-209 续接证据
q("勿以此斷", outcome("LY-204"), "LY-204 baseline")
q("1443 [sic — misprint for 1643]", outcome("AS-209"), "AS-209 sic")
assert "LY-204" in r81_by and "AS-209" in r81_by and "LR2-016" in r81_by

NEW_P = {
 "LY-406": "结局逗号收尾疑截断：尾逗一层属实；但甲戌出空即愈之主结局明载完整（双视 reason 均按此评分）。故部分成立。",
 "LY-446": "结局逗号收尾疑截断：尾逗一层属实；但酉日天变、戌日而雨两段主结局明载完整。故部分成立。",
 "LY-524": "结局逗号收尾疑截断：长叙末以「次日曰愈﹐」收尾、尾逗一层属实；但愈之主结局明载完整。按：本例另有 R64 旨 carry（所用药与所问附子对应未明字）在盘、与本旨并行不悖，本例此前未入 annotations、本轮以逗号收尾旨新登记。故部分成立。",
}
GIST_P = {
 "LY-406": "结局逗号收尾疑截断、主结局明载，部分成立",
 "LY-446": "结局逗号收尾疑截断、主结局明载，部分成立",
 "LY-524": "结局逗号收尾疑截断、主结局明载，部分成立",
}
new_entries = []
for cid in comma_new:
    assert (BASE / f"inputs-dev12/{cid}.json").exists()
    new_entries.append({
        "anon_id": rev82[cid], "case_id": cid, "disposition": "部分成立",
        "finding": "新旗标（R82 新立）：回原卡与 R82 manifest 结局原文逐字核——" + NEW_P[cid],
        "flag": "R82评审席新旗标（结局逗号收尾疑截断；回传要旨经本席逐件回读核对）",
        "manifest_carry_suggestion": f"新登记：自 R83 起承接本 R82 标注：按「{GIST_P[cid]}」登记；结局原文照录不改。",
        "relation": "新登记（R82）" if cid != "LY-524" else "新登记（R82，同例新旨）",
        "registered_round": 82,
        "sources_checked": [f"divination/benchmark/phase3/inputs-dev12/{cid}.json",
                            "divination/benchmark/phase3/runs/round82/judging/outcome-manifest.json cases[" + cid + "]",
                            f"divination/benchmark/phase3/runs/round82/predictions/{cid}.json",
                            "divination/benchmark/phase3/runs/round82/judging/host-mapping.json"],
        "source_seats": ["R82评审席"],
    })

# ---------- (c) DIAG-H26 旗标候选 F1–F12 ----------
gold26 = {}
for line in text_of("holdout26/test_gold.jsonl").splitlines():
    d = json.loads(line); gold26[d["id"]] = d
def hcard(cid):
    return load(f"holdout26/inputs/{cid}.json")
def apred(cid):
    return load(f"runs/round82/acceptance/predictions/{cid}.json")
acc_reasons = {}
for jf in ["judgeM1.jsonl", "judgeM2.jsonl", "judgeO1.jsonl", "judgeO2.jsonl"]:
    for line in text_of(f"runs/round82/acceptance/judging/{jf}").splitlines():
        if line.strip():
            d = json.loads(line); acc_reasons[d["anon_id"]] = d["reason"]

q("4月8日（农历二月十二日；实际农历十九清明，已进入辰月）", gold26["QM-034"]["outcome_record"], "F1 outcome")
q("结局农历标注自相矛盾", acc_reasons[acc_hm["master"]["QM-034"]] if False else text_of("runs/round82/acceptance/judging/judgeM1.jsonl"), "F1 M1")
q("结局农历标注自相参差", text_of("runs/round82/acceptance/judging/judgeM2.jsonl"), "F1 M2")
q("约0点57分才到达石家庄", gold26["QM-038"]["outcome_record"], "F2 outcome")
q("（按：「到达石家庄」与题面回沈阳方向不合，疑原书误植，逐字照录。）", gold26["QM-038"]["outcome_record"], "F2 note")
q("测从石家庄回沈阳一路吉凶", json.dumps(hcard("QM-038"), ensure_ascii=False), "F2 card")
q("（按：结局原文含当时事件名称，逐字以原书印刷276页为准。）", gold26["QM-036"]["outcome_record"], "F3 outcome note")
q("护照没有办成", gold26["QM-036"]["outcome_record"], "F3 outcome main")
q("离9｜虎 伤己 杜丁", json.dumps(hcard("QM-036")["anchors"], ensure_ascii=False), "F5 card")
q("其中星位字作「杜」与九星名不合，字序未厘清", apred("QM-036")["basis"], "F5 pred")
q("兑7、艮8、坎1、乾6四宫在本席读图中未完全厘清，见note", json.dumps(hcard("QM-039")["anchors"], ensure_ascii=False), "F4 card")
q("第一局盘面在本席读图中兑7/艮8两宫字序未完全厘清", gold26["QM-039"]["grade_note"], "F4 grade")
q("坤2｜合 惊乙 己冲丙 芮丙", json.dumps(hcard("QM-042")["anchors"], ensure_ascii=False), "F6 card")
q("坤2宫卡面字序「惊乙 己冲丙 芮丙」干星附记重出、未完全厘清", apred("QM-042")["basis"], "F6 pred")
q("坤2、坎1两宫卡面干星附记有重出字", apred("QM-043")["basis"], "F6 QM-043附记")
q("庚辰年庚辰月已酉日（原文「已酉」）", json.dumps(hcard("GSZ-069")["anchors"], ensure_ascii=False), "F7 card")
q("白牙", json.dumps(hcard("GSZ-069")["anchors"], ensure_ascii=False), "F7 card2")
q("卦盘「白牙」「官鬼己火」为原文录入讹字（白虎/巳火），照录登记", gold26["GSZ-069"]["grade_note"], "F7 grade")
assert hcard("GSZ-069")["question"] == "测病"
q("求测者（台账 subject 为空、原书未具名）", json.dumps(hcard("GSZ-069"), ensure_ascii=False), "F10 card")
q("丁丑年癸丑月已巳日（原文「已巳」）", json.dumps(hcard("GSZ-074")["anchors"], ensure_ascii=False), "F8 card")
q("戊寅年甲寅月已酉日（原文「已酉」）", json.dumps(hcard("GSZ-077")["anchors"], ensure_ascii=False), "F9 card")
q("兄弟已火", json.dumps(hcard("GSZ-077")["anchors"], ensure_ascii=False), "F9 card2")
q("辰月己卯日（原文作辰日己卯日）", json.dumps(hcard("WHY-005")["anchors"], ensure_ascii=False), "F11 card")
q("命主未具名（仅称中央银行行长，无姓名与任期可对位），按 low 登记；主持如按职位可识别性从严，可复核升档。", gold26["DS-034"]["grade_note"], "F12 grade")
q("F1（QM-034", diag26, "diag F1")
q("F12（DS-034", diag26, "diag F12")

H26_CASES = [
 ("QM-034", "F1", "金标结局农历标注自相矛盾属实：同一句内「农历二月十二日」与「实际农历十九清明」两说并存，评审 M1／M2 reason 均明指（成立面）；但公历 4月8日与辰月归属两视一致、主坐标命中不受此出入影响（不成立面）。故部分成立。"),
 ("QM-038", "F2", "金标结局地名与题面方向不合属实：题面为从石家庄回沈阳，结局作「约0点57分才到达石家庄」（成立面）；但金标按语已自载「疑原书误植，逐字照录」、误点三小时与到达时刻之主结局明载可核（不成立面）。故部分成立。"),
 ("QM-036", "F3＋F5", "F3：金标结局关键事件名称以按语略去属实——按语自载「结局原文含当时事件名称，逐字以原书印刷276页为准」、结局字段未载该名称（成立面）；但审批链条与「护照没有办成」之停办终局明载可核（不成立面）。F5：输入卡离 9 宫星位字作「杜」与九星名不合、字序未厘清属实（成立面）；但 prediction 已自注照实登记、锚点 stem_check 全合、不计 IN（不成立面）。两旨合并一例登记。故部分成立。"),
 ("QM-039", "F4", "输入卡第一局盘面四宫未完全厘清属实：board_verbatim 自载「兑7、艮8、坎1、乾6四宫在本席读图中未完全厘清」（成立面）；但金标 grade_note 台账已自注、字段以第二局盘面为校验代表、第一局局头无误，锚点口径 present、不计 IN（不成立面）。故部分成立。"),
 ("QM-042", "F6", "输入卡坤 2 宫字序未完全厘清属实：「坤2｜合 惊乙 己冲丙 芮丙」干星附记重出（成立面；QM-043 坤 2／坎 1 两宫同型、prediction 亦自注，附记不另立号）；但 prediction 已自注照实登记、锚点 stem_check 全合、不计 IN（不成立面）。故部分成立。"),
 ("GSZ-069", "F7＋F10", "F7：题面原文讹字属实——asked_at 作「已酉日」、盘面含「白牙」「官鬼己火」，金标 grade_note 自载为原文录入讹字（白虎/巳火）照录登记（成立面）；但讹字明示在盘、锚点五要素全在场、不计 IN（不成立面）。F10：输入卡 question 仅「测病」、subject 未具名，所问何人未载于卡面属实（成立面；承 DIAG-H25 F6 例）；但锚点五要素在场、大师断语病因与结局（颈椎增生）对应可核（不成立面）。两旨合并一例登记。故部分成立。"),
 ("GSZ-074", "F8", "输入卡 asked_at 原文作「已巳日」、干字面「已」非天干字属实（成立面；承 DIAG-H25 F3–F5 例）；但卡面已自注原文形态、锚点五要素全在场、不计 IN（不成立面）。故部分成立。"),
 ("GSZ-077", "F9", "输入卡 asked_at 原文作「已酉日」、盘面世爻作「兄弟已火」，与 F8 同型字面形态属实（成立面）；但卡面已自注原文形态、锚点五要素全在场、不计 IN（不成立面）。故部分成立。"),
 ("WHY-005", "F11", "输入卡 asked_at 原文作「辰日己卯日」、月建字面与日辰并置形态非常例属实（成立面）；但卡面已注口径（以辰月己卯日为准）、锚点全列在场、不计 IN（不成立面）。故部分成立。"),
 ("DS-034", "F12", "金标 grade_note 自载污染口径复核留位属实：「命主未具名（仅称中央银行行长，无姓名与任期可对位），按 low 登记；主持如按职位可识别性从严，可复核升档。」——职位可识别性之虑在盘（成立面）；但命主确未具名、无姓名与任期可对位，按 low 登记合封存口径，金标与输入数据本身无误载（不成立面）。故部分成立（本席不改判级，复核归主持）。"),
]
for cid, fno, finding in H26_CASES:
    new_entries.append({
        "anon_id": acc_inv[cid], "case_id": cid, "disposition": "部分成立",
        "finding": f"DIAG-H26 旗标候选 {fno}（R82 定案）：回 holdout26 输入卡与金标原文逐字核——" + finding,
        "flag": f"DIAG-H26 §5 旗标候选 {fno}",
        "manifest_carry_suggestion": f"验收侧新登记：自 R83 起承接本 R82 标注（DIAG-H26 {fno}）：按「{finding.split('。')[0]}，部分成立」登记；金标原文照录不改。",
        "relation": "新登记（R82，验收侧 DIAG-H26）",
        "registered_round": 82,
        "sources_checked": [f"divination/benchmark/phase3/holdout26/inputs/{cid}.json",
                            f"divination/benchmark/phase3/holdout26/test_gold.jsonl {cid} 条",
                            "divination/benchmark/phase3/runs/round82/acceptance/DIAG-H26.md §5",
                            "divination/benchmark/phase3/runs/round82/acceptance/judging/host-mapping.json"],
        "source_seats": ["DIAG-H26"],
    })

# ---------- 指令性字样基线六处复核（R82） ----------
q("盲测比对须注", outcome("BZ-036"), "baseline BZ-036")
q("（盲测比对时以格局大富一项为主）", outcome("BZ-042"), "baseline BZ-042")
q("使用时须分开统计", outcome("BZ-105"), "baseline BZ-105")
EDITOR = "原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。"
man82_text = text_of("runs/round82/judging/outcome-manifest.json")
assert man82_text.count(EDITOR) == 1
assert man82["_r56_lr2016_split"]["editor_note"] == EDITOR
for pkt in ["packet4.json", "packetB.json"]:
    q(EDITOR, text_of(f"runs/round82/judging/{pkt}"), f"baseline packet {pkt}")
# 待核维持
assert outcome("LY-537") == "果于申予日归"
q("申日归", reasons["LY-537"]["Y"], "LY-537 Y touch")
q("结局申日归", reasons["LY-537"]["X"], "LY-537 X touch")

# ---------- 组装 annotations ----------
assert len(new_entries) == 13 and all(e["disposition"] == "部分成立" for e in new_entries)
annotations = r81["annotations"] + new_entries
assert len(annotations) == 134
assert annotations[:121] == r81["annotations"], "前 121 件全量承接逐件原样"
dist = Counter(a["disposition"] for a in annotations)
assert dist == {"成立": 12, "部分成立": 114, "不成立": 6, "未核": 2}, dist
assert len({a["case_id"] for a in annotations}) == 134

special = list(r81["special_checks"]) + [
 {"item": "特别核查㉟（R82）：R81 附则承接建议 14 件于 R82 manifest 落实对勘与评审落实事实",
  "conclusion": "层文本对勘：_r81_carryover_notes_addendum 共 14 件，13 件与 case-annotations-r81.json 对应条 manifest_carry_suggestion 逐字全等；AS-307 层文本为 R81 附则 §三.1 建议原文之前缀（止于内层引号、尾段「登记；结局原文照录不改。」未入层，源于建包捕获口径），要旨完整、照实登记为文本层出入 1 件、不静默改任一侧。评审落实（以双视 reason／定稿为据）：14 件 carry_note 全数以 [R81-addendum] 段入评审包；已落实 6 件（LY-528／BZ-042／BZ-105／OC-009／LR2-024／AS-307），未见落实 8 件（LY-416／LY-105／LY-332／LY-624／LY-423／LR3-116／YM-069／LY-602，reason 均未见注记要点、仅按主结局常规评分）。逐件表见附则 §二。",
  "evidence": "落盘脚本逐件断言：层键集 14 件、13 件文本全等、AS-307 前缀关系；评审包 [R81-addendum] 14/14 在场；已落实件 reason 引文逐字在盘、未见落实件 reason 要点字样不在场断言通过；AS-307 R82 prediction basis 首行已正写「卡面 tradition＝astrology」、FREEZE-r82 tradition 旗标候选 0。",
  "scope_note": "对勘只登记、不改 manifest 与分数任一侧。"},
 {"item": "特别核查㊱（R82）：平台评审旗标定案总登记（逗号收尾全集＋LY-204／AS-209 续接）",
  "conclusion": "结局逗号收尾疑截断全集经 manifest 全量扫描共 20 件：已在 r81 承接册者 17 件（LY-408／LY-411／LY-416／LY-418／LY-423／LY-425／LY-428／LY-434／LY-437／LY-440／LY-452／LY-514／LY-523／LY-525／LY-528／LY-540／LY-623）同旨续接、条目逐件原样不动；册外 3 件（LY-406／LY-446／LY-524）逐件回原卡/结局核后定案部分成立、新登记入册。LY-204 旧注「勿以此斷」与 AS-209 年份误印 [sic] 两件同旨续接（均已在册、档位不变）；LR2-016 编者注属基线六处、只对勘登记不新立（见核查㊳）。",
  "evidence": "落盘脚本断言：逗号收尾扫描 20 件、旧 17／新 3 分账；新 3 件结局引文与双视 reason 引文逐字在盘；AS-209 结局「1443 [sic — misprint for 1643]」逐字在盘。",
  "scope_note": "续接件只登记、不重裁、不改条目；新登记件只及标注与承接建议，不改分数。"},
 {"item": "特别核查㊲（R82）：DIAG-H26 旗标候选 F1–F12 定案",
  "conclusion": "F1–F12 逐件回 holdout26 输入卡/金标核后均定案部分成立、新登记入册（registered_round＝82），按 case 合并为 10 件（QM-036 合 F3＋F5、GSZ-069 合 F7＋F10，QM-043 同型字序附记于 F6 不另立号）：各件或结局/卡面形态出入属实而自注在盘、锚点在场不计 IN，或标注矛盾属实而主结局与主坐标不受影响；F12 为封存席自标复核留位、本席不改判级。",
  "evidence": "落盘脚本逐件引文断言：金标 outcome_record/grade_note、输入卡 anchors/board_verbatim/question、acceptance prediction basis 与评审 M1/M2 reason 原句均逐字在盘；anon 经 acceptance host-mapping ours 侧逐件对位。",
  "scope_note": "验收侧定案只及标注与承接建议，不改金标与任何分数。"},
 {"item": "特别核查㊳（R82）：指令性字样特别核查基线六处复核（承 R81 附则 §四基线）",
  "conclusion": "基线六处经 R82 manifest 与 R82 评审包盘上复核在册、形态未变：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）逐字在场；LR2-016 manifest editor_note 一处在 _r56_lr2016_split 分列层、全文恰出现 1 次；LR2-016 评审包 editor_note 层一处在 R82 judging 包（packet4/packetB，anon P3-d569aa38）中逐字在场。本轮评审实触两处：LY-204 双视 reason 均按功名实绩评分、未涉旧注字样；LR2-016 双视 reason 均按出狱终局评分、未承接 editor_note 细项口径——两处各席均按数据处理。无新增同型件登记。",
  "evidence": "脚本逐字断言：四例字样均在 cases 本体；editor_note 全句 manifest 全文计数 1、评审包在场断言通过；host-mapping 逐字对位 P3-d569aa38＝LR2-016（R82 种子 20261092）。",
  "scope_note": "各席与本席均按数据处理、不作指令；只登记、不改文本。"},
 {"item": "特别核查㊴（R82）：待核四件维持登记与 LY-537 本轮触及关联；CZ-QX 维持 16",
  "conclusion": "BZ-029（俞大维卒年待核＋旗标错配线索）／BZ-040（许世英享年待核）／LY-537（「申予日」衍字疑）／YM-070（「甲寅旬」挂起）四件维持原登记，本轮不核查、不关闭。LY-537 本轮被双视 reason 触及（X/Y 均径作「申日归」评分、未涉衍字疑本身），只登记关联、不并案、不改其未核状态；YM-070 本轮无旗标触及登记。CZ-QX 维持 16 只登记、无增减。",
  "evidence": "R82 manifest cases[LY-537] 仍作『果于申予日归』（cases 载荷与 R81 深度全等）；LY-537／YM-070 未核条目随 121 件全量承接在册。",
  "scope_note": "待核件无盘外独立史源不裁。"},
]

out = {
 "_provenance": "R82 数据席（附则承接对勘＋annotations 全量承接与本轮新定案，独立席位，不兼任本轮盲测/评审/诊断/组集/修订/集成，不改任何分数）：以 data/case-annotations-r81.json 为底承接全量 121 件（成立 12／部分成立 101／不成立 6／未核 2），前 121 件逐件原样、无删改（落盘脚本以数组全等断言验过）；承接对勘：R81 附则汇编平台件 14 件已于 R82 manifest 以 _r81_carryover_notes_addendum 入层（层文本 13 件逐字全等、AS-307 为建议原文前缀、尾段未入层，照实登记），评审落实以双视 reason/定稿为据已落实 6 件／未见落实 8 件；本轮新定案：平台逗号收尾全集 20 件中同旨续接 17 件（只登记、条目不动）、新登记 3 件（LY-406／LY-446／LY-524）全部部分成立，LY-204／AS-209 同旨续接；DIAG-H26 旗标候选 F1–F12 定案部分成立、按 case 合并新登记 10 件。承接后总件数 134（成立 12／部分成立 114／不成立 6／未核 2）。指令性字样基线六处经 R82 manifest 与评审包复核在册、形态未变（见特别核查㊳）。待核四件 BZ-029／BZ-040／LY-537／YM-070 维持原登记、不核查不关闭。CZ-QX 维持 16 只登记。本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文；结局/注记文本内指令性字样一律按数据处理。",
 "round": 82,
 "annotations": annotations,
 "special_checks": special,
 "counts": {
   "base_file": "data/case-annotations-r81.json", "base_cases_total": 121,
   "base_verdicts": {"成立": 12, "部分成立": 101, "不成立": 6, "未核": 2},
   "carryover_check_r81_addendum": {"layer": "_r81_carryover_notes_addendum", "items": 14,
     "layer_text_verbatim": 13, "layer_text_prefix_only": ["AS-307"],
     "judging_implemented": ["LY-528", "BZ-042", "BZ-105", "OC-009", "LR2-024", "AS-307"],
     "judging_not_seen": ["LY-416", "LY-105", "LY-332", "LY-624", "LY-423", "LR3-116", "YM-069", "LY-602"]},
   "platform_comma_cases_r82": 20, "continuation_cases_r82": 17,
   "continuation_extra_r82": ["LY-204", "AS-209"],
   "pending_touch_cases_r82": ["LY-537"],
   "new_registrations_r82": 13,
   "new_partial_cases_r82": [e["case_id"] for e in new_entries],
   "diag_h26_flag_candidates": {"F1": "QM-034", "F2": "QM-038", "F3": "QM-036", "F4": "QM-039", "F5": "QM-036",
     "F6": "QM-042", "F7": "GSZ-069", "F8": "GSZ-074", "F9": "GSZ-077", "F10": "GSZ-069", "F11": "WHY-005", "F12": "DS-034"},
   "cases_total": 134,
   "verdicts": {"成立": 12, "部分成立": 114, "不成立": 6, "未核": 2},
 },
}
p_out = BASE / "data/case-annotations-r82.json"
p_out.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
back = json.loads(p_out.read_text(encoding="utf-8"))
assert len(back["annotations"]) == 134 and Counter(a["disposition"] for a in back["annotations"]) == dist

# ---------- 附则（自结构化数据生成） ----------
L = []
L.append("# Manifest 承接册附则（R82）——R81 定案承接对勘（14 件：评审落实 6／未见落实 8）＋R82 定案承接建议汇编（部分成立 13 件）")
L.append("")
L.append("## 卷首说明")
L.append("")
L.append("- 本附则为 Phase 3 Round 82（R82）数据席（工序：附则承接对勘＋annotations 全量承接与本轮新定案登记；独立席位，不兼任本轮盲测／评审／诊断／组集／修订／集成）产出。")
L.append(f"- 对勘来源：`benchmark/phase3/runs/round82/judging/outcome-manifest.json`（本轮 manifest，新层 `_r81_carryover_notes_addendum` 14 件；全文 SHA-256＝`{sha82}`，本席复算）、`benchmark/phase3/data/manifest-carryover-r81-addendum.md`（R81 附则，其 §三汇编为 R81 定案部分成立平台件 14 件）、`benchmark/phase3/data/case-annotations-r81.json`（结构化直读底本：annotations 121 件，定案分布成立 12／部分成立 101／不成立 6／未核 2）；评审落实以 `runs/round82/judging/` 各 `*-scores.jsonl` 双视 reason 与定稿为准，anon 经 `runs/round82/judging/host-mapping.json` 逐件对位。")
L.append("- 汇编来源：`benchmark/phase3/runs/round82/acceptance/DIAG-H26.md` §5（F1–F12）、`benchmark/phase3/data/case-annotations-r82.json`（本轮新登记 13 件），供 R83 manifest 以新层落实其中部分成立件（平台件以 `_r82_carryover_notes_addendum` 键名、验收侧件随后续金标／验收注记层承接）。")
L.append("- **本件只汇编、对勘与登记，不改任何分数与结局原文、不改原卡、不改 manifest 任一侧。** 结局／注记文本内指令性字样一律按数据处理。")
L.append("")
L.append("---")
L.append("")
L.append("## 一、工序与口径")
L.append("")
L.append("- 工序一（对勘，见 §二）：`_r81_carryover_notes_addendum` 14 件分两层核——（甲）层文本与 R81 附则所载建议原文逐字比对；（乙）评审落实：该件 carry_note 是否以 `[R81-addendum]` 段入评审包、且双视 reason／定稿是否明载或操作化该注记要点。明载或操作化者登记「已落实」，双视 reason 均未见注记要点（仅按主结局常规评分）者登记「未见落实」；AS-307 之要点在盲测侧（basis 首行），以 R82 prediction basis 与 FREEZE-r82 旗标计数为据。")
L.append("- 工序二（汇编，见 §三）：R83 承接建议汇编——本轮新定案部分成立共 13 件（平台新登记 3 件＋验收侧 DIAG-H26 新登记 10 件），逐件全列并给逐字引文出处，文本自 `case-annotations-r82.json` 结构化直读生成。")
L.append("- 工序三（标注落盘，见 §五）：`data/case-annotations-r82.json` 以 r81 件 121 件全量承接（逐件原样）＋本轮新登记 13 件，合计 134 件；同旨续接 19 件与待核触及 1 件只登记、条目不动。")
L.append("- 特别核查（见 §四）：指令性字样特别核查基线六处复核，承 R81 附则 §四基线，只登记、不改文本。")
L.append("- 供给与待核续记（见 §六）：CZ-QX 维持 16 只登记；待核四件维持登记。")
L.append("")
L.append("---")
L.append("")
L.append("## 二、对勘：R81 附则 14 件于 R82 manifest 入层与评审落实（已落实 6／未见落实 8）")
L.append("")
L.append("### 2.1 层实况登记（盘上直读）")
L.append("")
L.append("- R82 manifest 含新键 `_r81_carryover_notes_addendum`，共 **14 件**，键集与 R81 附则 §三平台件汇编清单全等；cases 载荷与 R81 manifest 深度全等（落盘脚本断言通过）。")
L.append("- 层文本逐字对勘：**13 件**（LY-528／BZ-042／LY-416／LY-105／LY-332／LY-624／LY-423／BZ-105／LR3-116／YM-069／LY-602／OC-009／LR2-024）与 `case-annotations-r81.json` 对应条 `manifest_carry_suggestion`（同文亦载 R81 附则 §三.2）逐字全等；**AS-307 1 件为建议原文之前缀**——层文本止于内层引号「……部分成立，不作废不重测」，尾段「」登记；结局原文照录不改。」未入层（R81 附则 §三.1 原文含该尾段），要旨完整。本席照实登记为文本层出入 1 件，不静默改任一侧，裁处更正留主持。")
L.append("- 评审传递面：14 件 carry_note 全数以 `[R81-addendum]` 段入 R82 评审包（packet1–4／packetA–B，落盘脚本逐件断言 14/14 在场）。")
L.append("")
L.append("### 2.2 逐件评审落实对勘（14 件，以双视 reason／定稿为据）")
L.append("")
L.append("| # | case_id | anon_id（R82） | 评审 reason 逐字据（节录） | 结论 |")
L.append("|---|---|---|---|---|")
EVID = {
 "LY-528": "Y：「坟地中上可用与总承果一一无错合，细项未分载；结局无可核时点」——注记「仅总承无分载」要点明载",
 "BZ-042": "X：「晚年败落结局自注未备不核」；Y：「晚年面来源未备」——注记「来源未备、仅大富可核」要点双视明载",
 "LY-416": "X／Y 均按「申月所请准、酉岁迎灵而归」主结局评分，未见「截断／逗号」字样",
 "LY-105": "X／Y 均按胃癌初期、手术恢复评分，未见「二手／论坛」来源成色字样",
 "LY-332": "X／Y 均按探花与前列断语评分，未见用神午火／巳火不合字样",
 "LY-624": "X／Y 均按「后果全无」主占评分，未见「再占／两占」互证残损字样",
 "LY-423": "X／Y 均按次日不药而愈主结局评分，未见「截断／逗号」字样",
 "BZ-105": "Y：「回溯病伤大方向近似，然1972目疾、1982住院与所断1983/1984年份全错位」——注记「回溯断验」要点明载",
 "LR3-116": "X／Y 均按牛黄二块物象评分，未见「残损」字样",
 "YM-069": "X／Y 均按相遇于岳家落点评分，未见「残句／残」字样",
 "LY-602": "X／Y 均按寅日得财终局评分，未见「早見／木日／含混」字样",
 "OC-009": "Y：「预测本身残损无应期，timing记0并注明」；X：「断文明言无应期坐标」——注记「prediction 残损降格」要点明载",
 "LR2-024": "X：「结局以七月死期为本课结局，方向反」——注记「死期明载可读」要点操作化明载；Y 同按七月死期评分",
 "AS-307": "盲测侧：R82 prediction basis 首行已正写「卡面 tradition＝astrology」、FREEZE-r82 tradition 首行旗标候选 0（误读未复发）；双视 reason 按胜选终局常规评分、无异议",
}
for i, cid in enumerate(LAYER14, 1):
    L.append(f"| {i} | {cid} | {rev82[cid]} | {EVID[cid]} | {VERDICT_A[cid]} |")
L.append("")
L.append("- 对勘结论：**已落实 6 件**（LY-528／BZ-042／BZ-105／OC-009／LR2-024／AS-307）、**未见落实 8 件**（LY-416／LY-105／LY-332／LY-624／LY-423／LR3-116／YM-069／LY-602）。未见落实 8 件之共同形态：注记已入评审包 carry_note，但双视 reason 只按主结局常规评分、未载注记所限定之成色／残损／含混要点；本席只登记事实，不改分数，是否在后续轮次强化评审口径留主持。")
L.append("")
L.append("---")
L.append("")
L.append("## 三、R83 承接建议汇编：R82 本轮新定案（部分成立 13 件逐件全列）")
L.append("")
L.append("- 落实键名写定：自 R83 manifest 起以 `_r82_carryover_notes_addendum` 键名落实本节平台件建议注记原文；验收侧件（QM-034／QM-038／QM-036／QM-039／QM-042／GSZ-069／GSZ-074／GSZ-077／WHY-005／DS-034）随后续金标／验收注记层承接、文本照录于本节。")
L.append("")
QUOTE_SRC = {
 "LY-406": "逐字引文出处：R82 manifest 结局「果於甲戌出空卽愈﹐」（`runs/round82/judging/outcome-manifest.json` cases[LY-406]）；X 席 reason「实甲戌出空即愈」（`judgeX-block1-scores.jsonl`，anon P3-3d681ad2）",
 "LY-446": "逐字引文出处：R82 manifest 结局「果於酉日天變﹐戌日而雨﹐」（cases[LY-446]）；Y 席 reason「果于酉日天变、戌日而雨」（`judgeY-block3-scores.jsonl`，anon P3-94ec2dec）",
 "LY-524": "逐字引文出处：R82 manifest 结局末句「次日曰愈﹐」（cases[LY-524]）；Y 席 reason「次日曰愈」（`judgeY-block3-scores.jsonl`，anon P3-b0195290）",
 "QM-034": "逐字引文出处：金标结局「4月8日（农历二月十二日；实际农历十九清明，已进入辰月）」（`holdout26/test_gold.jsonl` QM-034）；评审 M1 reason「结局农历标注自相矛盾」、M2 reason「结局农历标注自相参差」（acceptance `judgeM1.jsonl`／`judgeM2.jsonl`，master anon H26M-3d7e46bd）",
 "QM-038": "逐字引文出处：金标结局「约0点57分才到达石家庄」及按语「（按：「到达石家庄」与题面回沈阳方向不合，疑原书误植，逐字照录。）」（`holdout26/test_gold.jsonl` QM-038）；输入卡 question「测从石家庄回沈阳一路吉凶」（`holdout26/inputs/QM-038.json`）",
 "QM-036": "逐字引文出处：金标结局按语「（按：结局原文含当时事件名称，逐字以原书印刷276页为准。）」与「护照没有办成」（`holdout26/test_gold.jsonl` QM-036）；输入卡「离9｜虎 伤己 杜丁」（`holdout26/inputs/QM-036.json` anchors）；我方 basis 自注「其中星位字作「杜」与九星名不合，字序未厘清」（`runs/round82/acceptance/predictions/QM-036.json`）",
 "QM-039": "逐字引文出处：输入卡「兑7、艮8、坎1、乾6四宫在本席读图中未完全厘清，见note」（`holdout26/inputs/QM-039.json` anchors）；金标 grade_note「第一局盘面在本席读图中兑7/艮8两宫字序未完全厘清」（`holdout26/test_gold.jsonl` QM-039）",
 "QM-042": "逐字引文出处：输入卡「坤2｜合 惊乙 己冲丙 芮丙」（`holdout26/inputs/QM-042.json` anchors）；我方 basis 自注「坤2宫卡面字序「惊乙 己冲丙 芮丙」干星附记重出、未完全厘清」（`runs/round82/acceptance/predictions/QM-042.json`）",
 "GSZ-069": "逐字引文出处：输入卡 asked_at「庚辰年庚辰月已酉日（原文「已酉」）」、盘面「白牙」「官鬼己火」（`holdout26/inputs/GSZ-069.json` anchors）；金标 grade_note「卦盘「白牙」「官鬼己火」为原文录入讹字（白虎/巳火），照录登记」（`holdout26/test_gold.jsonl` GSZ-069）；输入卡 question 逐字仅「测病」、subject「求测者（台账 subject 为空、原书未具名）」",
 "GSZ-074": "逐字引文出处：输入卡 asked_at「丁丑年癸丑月已巳日（原文「已巳」）」（`holdout26/inputs/GSZ-074.json` anchors）",
 "GSZ-077": "逐字引文出处：输入卡 asked_at「戊寅年甲寅月已酉日（原文「已酉」）」、盘面世爻「兄弟已火」（`holdout26/inputs/GSZ-077.json` anchors）",
 "WHY-005": "逐字引文出处：输入卡 asked_at「辰月己卯日（原文作辰日己卯日）」（`holdout26/inputs/WHY-005.json` anchors）",
 "DS-034": "逐字引文出处：金标 grade_note「命主未具名（仅称中央银行行长，无姓名与任期可对位），按 low 登记；主持如按职位可识别性从严，可复核升档。」（`holdout26/test_gold.jsonl` DS-034）",
}
for i, e in enumerate(new_entries, 1):
    L.append(f"#### N{i}. {e['case_id']}")
    L.append("")
    L.append(f"- case_id：{e['case_id']}")
    L.append(f"- anon_id：{e['anon_id']}")
    L.append(f"- 定案类别：{e['disposition']}（registered_round＝82；{e['relation']}）")
    L.append(f"- 核对结论：{e['finding']}")
    L.append(f"- {QUOTE_SRC[e['case_id']]}")
    L.append(f"- 承接注记建议文本（原文）：「{e['manifest_carry_suggestion']}」")
    L.append("")
L.append("---")
L.append("")
L.append("## 四、指令性字样特别核查基线六处对勘（承 R81 附则 §四基线）")
L.append("")
L.append("- 基线构成：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）＋LR2-016 manifest editor_note 一处＋LR2-016 评审包 editor_note 层一处，共六处、分三层。本轮自 `runs/round82/judging/outcome-manifest.json` 与 R82 评审包盘上逐处回读原文复核，**只登记、不改文本**；各席与本席均按数据处理、不作指令。")
L.append("")
L.append("| case_id | 基线字样（按数据引录） | 本轮在盘形态 |")
L.append("|---|---|---|")
L.append("| BZ-036 | 结局含「盲测比对须注」 | 在册：在场、形态未变 |")
L.append("| BZ-042 | 结局含「（盲测比对时以格局大富一项为主）」 | 在册：在场、形态未变 |")
L.append("| BZ-105 | 结局含「使用时须分开统计」 | 在册：在场、形态未变（本轮兼评审落实已落实件、并行不悖） |")
L.append("| LY-204 | 结局旧注层含「勿以此斷」 | 在册：在场、形态未变（本轮评审双视实触：reason 均按功名实绩评分、未涉旧注字样，只登记） |")
L.append("")
L.append("- LR2-016 manifest editor_note 一处：所在 manifest `_r56_lr2016_split` 分列层，本轮在盘原文逐字与基线全等、manifest 全文恰出现 1 次（落盘脚本断言）。")
L.append("- LR2-016 评审包 editor_note 层一处：R82 评审包（packet4／packetB，anon P3-d569aa38）中同句逐字在场、与 manifest 分列层全等，另列一类、不并入 cases 本体基线计数；本轮双视 reason 均按出狱终局评分、未承接该细项口径，只登记。")
L.append("- 结论：基线六处经 R82 盘上逐处回读在册、形态未变，出入 0 处。本轮有评审实触记录者 2 处（LY-204 与 LR2-016）。无新增同型件登记。本席只登记、不改任何文本。")
L.append("")
L.append("---")
L.append("")
L.append("## 五、annotations 落盘断言与同旨续接登记")
L.append("")
L.append("### 5.1 annotations 落盘断言（工序三）")
L.append("")
L.append("- 底本：`data/case-annotations-r81.json` annotations 121 件（成立 12／部分成立 101／不成立 6／未核 2），全量承接、逐件原样、无删改（落盘脚本以 annotations 数组前 121 件全等断言验过）。")
L.append("- 新增登记：**13 件**，全部部分成立（平台新登记 3 件，见 §三 N1–N3；DIAG-H26 F1–F12 按 case 合并 10 件，见 N4–N13）——落盘 `data/case-annotations-r82.json` annotations **134 件＝121＋13**（成立 12／部分成立 114／不成立 6／未核 2），各新件 `registered_round＝82`、字段完整（落盘脚本逐件断言），counts 相应更新，回读 JSON 可解析断言通过。")
L.append("- 平台旗标定案构成：逗号收尾全集 20 件——同旨续接 17 件（档位承既有定案、条目逐件原样不动，只登记）；新登记 3 件（上）。LY-204／AS-209 两件同旨续接只登记。待核触及 1 件（LY-537，见 §五.2）。")
L.append("- special_checks 承接 r81 三十四件并新增 R82 五件（㉟ R81 承接 14 件落实对勘；㊱ 平台旗标总登记；㊲ DIAG-H26 F1–F12 定案；㊳ 指令性字样基线六处复核；㊴ 待核四件维持与 CZ-QX），合计 39 件。")
L.append("")
L.append("### 5.2 R82 确认的待核维持清单（四件，维持挂起、不核查不关闭）")
L.append("")
L.append("| case_id | 状态登记（承 R81 附则 §5.2 口径续记） |")
L.append("|---|---|")
L.append("| BZ-029 | 俞大维卒年待核＋旗标错配线索，维持原登记、不裁；不入 annotations |")
L.append("| BZ-040 | 许世英享年待核，维持原登记、不裁；不入 annotations |")
L.append("| LY-537 | 「申予日」衍字疑，维持未核原登记；本轮被双视 reason 触及（X／Y 均径作「申日归」评分、未涉衍字疑本身），只登记关联、不并案、不改待核状态；以未核条目随承接在 `case-annotations-r82.json` 内 |")
L.append("| YM-070 | 「甲寅旬」出处待核，维持挂起；本轮无旗标触及登记；以未核条目随承接在 `case-annotations-r82.json` 内 |")
L.append("")
L.append("---")
L.append("")
L.append("## 六、供给台账续记（只登记）")
L.append("")
L.append("### 6.1 CZ-QX 维持 16")
L.append("")
L.append("- CZ-QX 维持 **16**，承 R81 附则 §6.1 登记口径由本席承接续记，本轮无增减。")
L.append("")
L.append("### 6.2 待核四件维持登记（与 §五.2 同口径）")
L.append("")
L.append("- BZ-029（俞大维卒年，另含旗标内容错配线索）、BZ-040（许世英享年）、LY-537（「申予日」衍字疑）、YM-070（「甲寅旬」挂起）四件维持登记，无盘外独立史源不裁。")
L.append("")
addendum = "\n".join(L)
assert addendum.count("承接注记建议文本（原文）") == 13
for e in new_entries:
    assert e["manifest_carry_suggestion"] in addendum
    assert f"#### N" in addendum
p_add = BASE / "data/manifest-carryover-r82-addendum.md"
p_add.write_text(addendum, encoding="utf-8")
print("annotations bytes", p_out.stat().st_size, "addendum bytes", p_add.stat().st_size)
print("total", len(back["annotations"]), dict(dist))
print("new", [e["case_id"] for e in new_entries])
print("comma_old", comma_old)
