#!/usr/bin/env python3
# R81 数据席落盘脚本：case-annotations-r81.json + manifest-carryover-r81-addendum.md
# 纪律：逐件回读原卡/结局原文；引文逐字断言；文本按数据处理。
import json, pathlib, hashlib
from collections import Counter

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")

def load(rel):
    return json.loads((BASE / rel).read_text(encoding="utf-8"))

def text_of(rel):
    return (BASE / rel).read_text(encoding="utf-8")

r80 = load("data/case-annotations-r80.json")
man81 = load("runs/round81/judging/outcome-manifest.json")
man80 = load("runs/round80/judging/outcome-manifest.json")
hm81 = load("runs/round81/judging/host-mapping.json")
freeze81 = text_of("runs/round81/FREEZE-r81.md")
diag24 = text_of("runs/round80/acceptance/DIAG-H24.md")

cases81 = man81["cases"]; cases80 = man80["cases"]
assert cases81 == cases80, "R81 cases 载荷须与 R80 逐字全等"

def outcome(cid):
    v = cases81[cid]
    return v if isinstance(v, str) else (v.get("outcome_record") or "")

def card(cid):
    return load(f"inputs-dev12/{cid}.json")

def pred81(cid):
    return load(f"runs/round81/predictions/{cid}.json")

def q(s, src, label):
    assert s in src, f"引文断言失败 {label}: {s!r}"

# ---------- (a) AS-307 对勘：R80 附则 1 件已于 R81 manifest 落实 ----------
r80_by = {a["case_id"]: a for a in r80["annotations"]}
layer = man81["_r80_carryover_notes_addendum"]
assert set(layer.keys()) == {"AS-307"}, layer.keys()
assert layer["AS-307"] == r80_by["AS-307"]["manifest_carry_suggestion"]
sha81 = hashlib.sha256((BASE / "runs/round81/judging/outcome-manifest.json").read_bytes()).hexdigest()
assert sha81 == "3bdc59dcb6ab001ce8cb3572d063147add96c2c9d9992f4d569f7aea48e4b8be"

# AS-307 R81 再裁复核（FREEZE-r81 §一.2）
q("AS-307（B02）——部分成立，不作废不重测", freeze81, "freeze81 AS-307")
q("卡面未标注 tradition 字段，按题面体裁自决", pred81("AS-307")["basis"], "AS-307 basis首行")
q("astrology（选举占星，自决采用）", pred81("AS-307")["basis"], "AS-307 systems_used")
assert card("AS-307").get("tradition") == "astrology" or "astrology" in json.dumps(card("AS-307"), ensure_ascii=False)
AS307_R82_TEXT = "平台旗标定案：自 R82 起承接本 R81 标注（与 R80 同例同型再裁）：按「卡面 tradition＝astrology、basis 首行误读作未标注，实际所用方法为 astrology 与卡面实质一致、断语方向不受影响，部分成立，不作废不重测」登记；结局原文照录不改。"

# ---------- (c) 平台评审新旗标 68 anon ----------
ANONS_C = """P3-1499cf20 P3-21506fe6 P3-28d75889 P3-1a1f7027 P3-1f679bf7 P3-0a409c2f P3-0595ce12 P3-0c27ec61 P3-3bfd8053 P3-42ff87ac P3-45144e9e P3-4e056282 P3-5018cb02 P3-625dba94 P3-59fe1ed3 P3-537270e5 P3-4ce7a1e7 P3-5bc9cee5 P3-526f4fee P3-724aefd3 P3-7e45115a P3-823658d3 P3-8eb4037e P3-a0630750 P3-bdb967d4 P3-cecce81f P3-e0d2190f P3-ecaab305 P3-c3590da9 P3-c3605fbe P3-c87d846a P3-cba81779 P3-d5ce4675 P3-e3904274 P3-e8f61214 P3-efd50a1e P3-f0667883 P3-c4c7aa95 P3-dee5df91 P3-02db1867 P3-03f97d4c P3-087f07de P3-0e0b7e54 P3-110d0622 P3-11436859 P3-136a219c P3-1d4703cb P3-1d7324db P3-29e3d244 P3-2c1df9f0 P3-313b1a58 P3-387ac185 P3-0c6952ea P3-63c7c255 P3-78a426f8 P3-7b173069 P3-7e570081 P3-8b95d50d P3-8bdc8df3 P3-8f31fa86 P3-9b8881fe P3-a1fb0e49 P3-995ab3bd P3-e3d04aba P3-f47ed890 P3-c88f318a P3-f608247e P3-eb5e86a2""".split()
assert len(ANONS_C) == 68 and len(set(ANONS_C)) == 68
c_cases = []
for an in ANONS_C:
    cid = hm81[an]  # anon 逐件对位复核（KeyError 即失败，不凭序号推断）
    c_cases.append((an, cid))
    assert (BASE / f"inputs-dev12/{cid}.json").exists()
    assert outcome(cid) != ""
assert len({cid for _, cid in c_cases}) == 68, "去重键 case_id 合并后须 68 件"
existing_ids = set(r80_by.keys())
new_c = [(an, cid) for an, cid in c_cases if cid not in existing_ids]
cont_c = [(an, cid) for an, cid in c_cases if cid in existing_ids]
assert len(new_c) == 13 and len(cont_c) == 55, (len(new_c), len(cont_c))
assert {cid for _, cid in cont_c if r80_by[cid]["disposition"] == "未核"} == {"LY-537"}

# ---------- 新登记 13 件（平台）逐件引文断言与定案 ----------
NEW_C = {
 "LY-528": ("果一一無錯", "结局仅「果一一無錯﹐」总承、无具体内容分载：总承肯定一层属实，逐项断面无从分核；但结局并非全缺、总承方向可读。故部分成立。"),
 "BZ-042": ("其晚年败落细节本数据集所据来源未备", "结局自注晚年败落细节来源未备、仅格局大富一项可核：自注属实，晚年面无从核验；但大富主面明载且与断语对位。故部分成立。"),
 "LY-416": ("後應申月所請準﹐酉歲迎靈而歸﹐", "结局逗号收尾疑截断：尾逗一层属实；但所请获准、酉岁迎灵而归之主结局明载完整。故部分成立。"),
 "LY-105": ("正在恢复（论坛帖内反馈，二手）", "结局系论坛二手反馈、未经一手核实：来源成色一层属实；但反馈内容（胃癌初期、手术效果不错、正在恢复）与所问母病面直接对应。故部分成立。"),
 "LY-332": ("果中探花．", "卡面用神官鬼午火与逐爻表官鬼巳火并见不合、prediction 已自注存疑：卡面内部不合一层属实；但不合已自注、结局「果中探花」明载、主断可核。故部分成立。"),
 "LY-624": ("後果全無。", "题面两占合断、输入卡只载一卦（再占暌之損不在本条范围、卡面注记明载）、互证面残损：残损一层属实；但本卦结局「後果全無」明载、主占可核。故部分成立。"),
 "LY-423": ("果於次日退災﹐不藥而愈﹐", "结局逗号收尾疑截断：尾逗一层属实；但次日退灾、不药而愈之主结局明载完整。故部分成立。"),
 "BZ-105": ("使用时须分开统计", "回溯断验例、结局系求测者当场自述自证已知往事（结局自注「此为回溯断验」、须分开统计）：成色一层属实；但自注明示在盘、prediction 亦自标回溯例，非隐匿瑕疵。故部分成立。"),
 "LR3-116": ("是牛黄二块", "卡面残损（三传后二传天干与旬空未载）、prediction 自注盘面残损置信低：残损一层属实；但残损已自注、结局物象明载可核。故部分成立。"),
 "YM-069": ("而不知相遇于岳家。", "结局为残句 fragment、仅落点（相遇于岳家）可读：残句一层属实；但相遇落点与寻人终局方向可读。故部分成立。"),
 "LY-602": ("果於寅日早見木日得財。", "结局「早見木日」措辞含混（carry 已登记）：含混一层属实；但寅日得财之终局主载可读。故部分成立。"),
 "OC-009": ("顾维钧外交生涯长达数十年", "四柱未实际给出、prediction 为残损降格断（自明四柱缺载、不能作盘面定断、不报应期）：残损一层属实；但降格已自明、结局事历明载。故部分成立。"),
 "LR2-024": ("已而果然。七月死期为本课结局。", "结局「已而果然」总承与「七月死期为本课结局」并载含混：并载含混一层属实，总承所指未分载；但死期终局明载可读。故部分成立。"),
}
assert set(NEW_C.keys()) == {cid for _, cid in new_c}
for cid, (quote, _) in NEW_C.items():
    q(quote, outcome(cid), f"{cid} outcome")
q("官鬼午火为用神", json.dumps(card("LY-332"), ensure_ascii=False), "LY-332 yongshen")
q("官鬼巳火", json.dumps(card("LY-332"), ensure_ascii=False), "LY-332 chart")
q("同例再占暌之損不在本條範圍", json.dumps(card("LY-624"), ensure_ascii=False), "LY-624 card note")
q("三传天干未载", pred81("LR3-116")["prediction_text"] + pred81("LR3-116").get("basis", ""), "LR3-116 pred")
q("四柱缺载", pred81("OC-009")["prediction_text"], "OC-009 pred")
q("（盲测比对时以格局大富一项为主）", outcome("BZ-042"), "BZ-042 baseline quote")

def carry_text(cid, gist):
    return f"新登记：自 R82 起承接本 R81 标注：按「{gist}」登记；结局原文照录不改。"

GIST_C = {
 "LY-528": "结局仅总承无分载、逐项无从分核，部分成立",
 "BZ-042": "结局自注晚年败落细节来源未备、仅格局大富可核，部分成立",
 "LY-416": "结局逗号收尾疑截断、主结局明载，部分成立",
 "LY-105": "结局系论坛二手反馈未经一手核实、内容与母病面对应，部分成立",
 "LY-332": "卡面用神与逐爻表不合已自注、主断可核，部分成立",
 "LY-624": "两占合断只载一卦互证面残损、主占可核，部分成立",
 "LY-423": "结局逗号收尾疑截断、主结局明载，部分成立",
 "BZ-105": "回溯断验例结局系当场自证、自注须分开统计，部分成立",
 "LR3-116": "卡面残损三传后二传天干与旬空未载已自注，部分成立",
 "YM-069": "结局为残句仅落点可读，部分成立",
 "LY-602": "结局『早見木日』措辞含混、得财终局可读，部分成立",
 "OC-009": "四柱未给 prediction 残损降格已自明，部分成立",
 "LR2-024": "结局总承与死期并载含混、死期明载，部分成立",
}
new_entries = []
anon_of = {cid: an for an, cid in c_cases}
for an, cid in new_c:
    new_entries.append({
        "anon_id": an, "case_id": cid, "disposition": "部分成立",
        "finding": "新旗标（R81 新立）：回原卡与 R81 manifest 结局原文逐字核——" + NEW_C[cid][1],
        "flag": "R81评审席：" + NEW_C[cid][1].split("：")[0] if False else "R81评审席新旗标（回传要旨经本席逐件回读核对）",
        "manifest_carry_suggestion": carry_text(cid, GIST_C[cid]),
        "relation": "新登记（R81）",
        "registered_round": 81,
        "sources_checked": [f"divination/benchmark/phase3/inputs-dev12/{cid}.json",
                            "divination/benchmark/phase3/runs/round81/judging/outcome-manifest.json cases[" + cid + "]",
                            f"divination/benchmark/phase3/runs/round81/predictions/{cid}.json",
                            "divination/benchmark/phase3/runs/round81/judging/host-mapping.json"],
        "source_seats": ["R81评审席"],
    })

# ---------- (b) DIAG-H24 旗标候选 F1–F4 ----------
gold24 = {}
for line in text_of("holdout24/test_gold.jsonl").splitlines():
    d = json.loads(line); gold24[d["id"]] = d
acc_hm = load("runs/round80/acceptance/judging/host-mapping.json")["ours"]
acc_inv = {v: k for k, v in acc_hm.items()}
q("此为普通农村老妇人，一生并无大作为", gold24["DS-020"]["master_prediction"], "F1 master")
q("个个富过百万", gold24["DS-020"]["outcome_record"], "F1 outcome")
q("1999年6月4日11点", json.dumps(load("holdout24/inputs/QM-307.json"), ensure_ascii=False), "F2 card")
q("6月13日我妻子平安地生下一个又白又胖的男孩", gold24["QM-307"]["outcome_record"], "F2 outcome")
q("应期6月13日生在三日窗口内近主坐标第2日", diag24, "F2 diag quote")
q("巳亥月", json.dumps(load("holdout24/inputs/GSZ-047.json"), ensure_ascii=False), "F3 card")
q("恥[?]一目", gold24["ZCB-014"]["outcome_record"], "F4 outcome")
q("仙[?]", json.dumps(load("holdout24/inputs/ZCB-014.json"), ensure_ascii=False), "F4 card")
F_CASES = [
 ("DS-020", "F1", "大师断语「一生并无大作为」与结局「五子三女，个个富过百万……寿至九旬」之间张力属实（成立面）；但大师断语主语为命主本人行状，结局主载在子辈量级与寿程、非同一断面全反（不成立面）。故部分成立。"),
 ("QM-307", "F2", "评审 reason「三日窗口内」表述与输入卡占日（1999年6月4日）至生产日（6月13日）相距 9 日出入属实（成立面）；但金标大师断语与结局逐字合（正断 6月13日）、输入/结局数据本身无缺，DIAG-H24 本例 TIM 编码亦自明以日距为准不据该 reason（不成立面）。故部分成立。"),
 ("GSZ-047", "F3", "输入卡月柱原文作「巳亥月」字面含混属实（成立面）；但卡面已自注原文形态、金标 grade_note 载锚点五要素全在场，不计 IN（不成立面）。故部分成立。"),
 ("ZCB-014", "F4", "结局与输入卡原文含 [?] 转录存疑标记各一处属实（成立面）；但存疑标记明示在盘、主结局（裴公中会元、余皆落第）完整可读（不成立面）。故部分成立。"),
]
for cid, fno, finding in F_CASES:
    new_entries.append({
        "anon_id": acc_inv[cid], "case_id": cid, "disposition": "部分成立",
        "finding": f"DIAG-H24 旗标候选 {fno}（R81 定案）：回原卡与金标结局原文逐字核——" + finding,
        "flag": f"DIAG-H24 §6 旗标候选 {fno}",
        "manifest_carry_suggestion": f"验收侧新登记：自 R82 起承接本 R81 标注（DIAG-H24 {fno}）：按「{finding.split('。')[0]}，部分成立」登记；金标原文照录不改。",
        "relation": "新登记（R81，验收侧 DIAG-H24）",
        "registered_round": 81,
        "sources_checked": [f"divination/benchmark/phase3/holdout24/inputs/{cid}.json",
                            f"divination/benchmark/phase3/holdout24/test_gold.jsonl {cid} 条",
                            "divination/benchmark/phase3/runs/round80/acceptance/DIAG-H24.md §6",
                            "divination/benchmark/phase3/runs/round80/acceptance/judging/host-mapping.json"],
        "source_seats": ["DIAG-H24"],
    })

# ---------- (d) QM-031 ----------
gold25 = {}
for line in text_of("holdout25/test_gold.jsonl").splitlines():
    d = json.loads(line); gold25[d["id"]] = d
q("按投资三万元或一万三千元来断", gold25["QM-031"]["master_prediction"], "QM-031 master amounts")
q("原书复盘改按三万元或十三万元", gold25["QM-031"]["master_prediction"], "QM-031 editor note")
q("十三万元左右的商位", gold25["QM-031"]["outcome_record"], "QM-031 outcome")
hm81acc = load("runs/round81/acceptance/judging/host-mapping.json")["ours"]
inv81acc = {v: k for k, v in hm81acc.items()}
QM031_FINDING = "大师断语（金标 master_prediction）内嵌原书复盘编辑注、投资金额口径含混（一万三/三万元与修订后十三万元并存）属实（成立面）；但编辑注明示在盘且自载修订口径、结局「认购了一个十三万元左右的商位」与修订口径对应可核（不成立面）。故部分成立。"
new_entries.append({
    "anon_id": inv81acc["QM-031"], "case_id": "QM-031", "disposition": "部分成立",
    "finding": "验收侧旗标（R81 定案）：回金标原文逐字核——" + QM031_FINDING,
    "flag": "验收侧：金标 master_prediction 内嵌原书复盘编辑注、投资金额口径含混",
    "manifest_carry_suggestion": "验收侧新登记：自 R82 起承接本 R81 标注：按「金标断语内嵌复盘编辑注、金额口径含混而修订口径明示、结局与修订口径对应，部分成立」登记；金标原文照录不改。",
    "relation": "新登记（R81，验收侧）",
    "registered_round": 81,
    "sources_checked": ["divination/benchmark/phase3/holdout25/test_gold.jsonl QM-031 条",
                        "divination/benchmark/phase3/runs/round81/acceptance/judging/host-mapping.json"],
    "source_seats": ["验收侧（R81）"],
})

# ---------- (e) DIAG-H25 旗标候选 F1–F6（落盘时点 §5 已在盘，一并定案） ----------
diag25 = text_of("runs/round81/acceptance/DIAG-H25.md")
assert "## 5. 旗标候选" in diag25
q("门也被撬得稀巴烂", gold25["GSZ-052"]["outcome_record"], "H25F1 outcome")
q("后未找到失物", gold25["GSZ-052"]["grade_note"], "H25F1 grade_note")
assert "后未找到失物" not in gold25["GSZ-052"]["outcome_record"]
q("戊寅年甲子月未日（原文日柱仅记「未日」）", json.dumps(load("holdout25/inputs/GSZ-060.json"), ensure_ascii=False), "H25F2 card")
q("占时日柱干支不全照录登记", gold25["GSZ-060"]["grade_note"], "H25F2 grade_note a")
q("锚点五要素经本席回原书文字层复核全在场", gold25["GSZ-060"]["grade_note"], "H25F2 grade_note b")
q("丙子年已亥月辛酉日（原文「已亥」）", json.dumps(load("holdout25/inputs/GSZ-049.json"), ensure_ascii=False), "H25F3 card")
q("丙子年已亥月丙寅日（原文「已亥」）", json.dumps(load("holdout25/inputs/GSZ-053.json"), ensure_ascii=False), "H25F4 card")
q("戊寅年已未月庚辰日（原文「已未」）", json.dumps(load("holdout25/inputs/GSZ-058.json"), ensure_ascii=False), "H25F5 card")
assert load("holdout25/inputs/GSZ-061.json")["question"] == "问病"
H25_CASES = [
 ("GSZ-052", "F1", "金标 outcome_record 与 grade_note 载录不一致属实：grade_note 称结局段末「后未找到失物」逐字见原文，而 outcome_record 全文止于「门也被撬得稀巴烂」、未载该句（成立面）；但 outcome_record 主体结局明载、grade_note 所指为原书原文口径（不成立面）。故部分成立。"),
 ("GSZ-060", "F2", "输入卡日柱仅记「未日」、日干缺载、旬空无从判定，且 grade_note 一面载「占时日柱干支不全照录登记」、一面称「锚点五要素……全在场」，两处口径自相矛盾属实（成立面）；但缺载已在卡面自注原文形态、结局与大师断语本身明载可核（不成立面）。故部分成立。"),
 ("GSZ-049", "F3", "输入卡月建原文作「已亥月」、月建天干字面「已」非天干字属实（成立面）；但卡面已自注原文形态、月支与余锚点要素在场、不计 IN（不成立面；承 DIAG-H24 GSZ-047 例）。故部分成立。"),
 ("GSZ-053", "F4", "输入卡月建原文作「已亥月」字面含混属实，与 F3 同型（成立面）；但卡面已自注原文形态、余锚点要素在场、不计 IN（不成立面）。故部分成立。"),
 ("GSZ-058", "F5", "输入卡月建原文作「已未月」字面含混属实，与 F3 同型（成立面）；但卡面已自注原文形态、余锚点要素在场、不计 IN（不成立面）。故部分成立。"),
 ("GSZ-061", "F6", "输入卡 question 仅「问病」、subject 未具名，所问何人未载于卡面属实（成立面）；但锚点五要素在场、大师断语病位与结局（头部血栓）对应可核（不成立面）。故部分成立。"),
]
for cid, fno, finding in H25_CASES:
    new_entries.append({
        "anon_id": inv81acc[cid], "case_id": cid, "disposition": "部分成立",
        "finding": f"DIAG-H25 旗标候选 {fno}（R81 定案）：回原卡与金标原文逐字核——" + finding,
        "flag": f"DIAG-H25 §5 旗标候选 {fno}",
        "manifest_carry_suggestion": f"验收侧新登记：自 R82 起承接本 R81 标注（DIAG-H25 {fno}）：按「{finding.split('。')[0]}，部分成立」登记；金标原文照录不改。",
        "relation": "新登记（R81，验收侧 DIAG-H25）",
        "registered_round": 81,
        "sources_checked": [f"divination/benchmark/phase3/holdout25/inputs/{cid}.json",
                            f"divination/benchmark/phase3/holdout25/test_gold.jsonl {cid} 条",
                            "divination/benchmark/phase3/runs/round81/acceptance/DIAG-H25.md §5",
                            "divination/benchmark/phase3/runs/round81/acceptance/judging/host-mapping.json"],
        "source_seats": ["DIAG-H25"],
    })

# ---------- 指令性字样基线六处复核（R81 manifest） ----------
q("盲测比对须注", outcome("BZ-036"), "baseline BZ-036")
q("（盲测比对时以格局大富一项为主）", outcome("BZ-042"), "baseline BZ-042")
q("使用时须分开统计", outcome("BZ-105"), "baseline BZ-105")
q("勿以此斷", outcome("LY-204"), "baseline LY-204")
EDITOR = "原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。"
man81_text = text_of("runs/round81/judging/outcome-manifest.json")
assert man81_text.count(EDITOR) == 1
for pkt in ["packet3.json", "packetB.json"]:
    pp = BASE / f"runs/round81/judging/{pkt}"
    if pp.exists():
        q(EDITOR, pp.read_text(encoding="utf-8"), f"baseline packet {pkt}")

# ---------- 组装 annotations ----------
assert len(new_entries) == 24 and all(e["disposition"] == "部分成立" for e in new_entries)
annotations = r80["annotations"] + new_entries
assert len(annotations) == 121
assert annotations[:97] == r80["annotations"], "前 97 件全量承接逐件原样"
dist = Counter(a["disposition"] for a in annotations)
assert dist == {"成立": 12, "部分成立": 101, "不成立": 6, "未核": 2}, dist
assert len({a["case_id"] for a in annotations}) == 121

special = list(r80["special_checks"]) + [
 {"item": "特别核查㉘（R81）：R80 附则承接建议 1 件于 R81 manifest 落实对勘",
  "conclusion": "R81 manifest 新层 _r80_carryover_notes_addendum 共 1 件（AS-307），层文本与 case-annotations-r80.json 对应条 manifest_carry_suggestion 逐字全等（且逐字在 R80 附则 §三.1）。1 件全部落实，未落实 0 件。cases 载荷与 R80 件深度全等、manifest 全文 SHA-256＝3bdc59dcb6ab001ce8cb3572d063147add96c2c9d9992f4d569f7aea48e4b8be。",
  "evidence": "落盘脚本逐件断言：层键集＝{AS-307}、文本全等；cases81＝＝cases80 深度断言通过。",
  "scope_note": "对勘只读 R81 manifest 与 R80 附则／标注，不改 manifest 任一侧；逐件表见附则 §二。"},
 {"item": "特别核查㉙（R81）：平台评审新旗标汇编一致性与定案总登记",
  "conclusion": "评审席回传 68 个 anon、经 runs/round81/judging/host-mapping.json 逐件对位为 68 例（去重键 case_id、无重复例、形近串号逐件对位未凭序号推断）。与 r80 承接册 97 件对勘：同例 55 件——同旨续接 54 件（档位承既有定案、条目逐件原样不动）、待核触及 1 件（LY-537，见核查㉞）；97 件外新登记 13 件，全部部分成立（LY-528／BZ-042／LY-416／LY-105／LY-332／LY-624／LY-423／BZ-105／LR3-116／YM-069／LY-602／OC-009／LR2-024）。",
  "evidence": "落盘脚本逐件断言：68 anon 全数于 host-mapping 在册、原卡在盘、R81 结局非空；新登记 13 件逐件结局引文断言通过。",
  "scope_note": "续接件只登记、不重裁、不改条目；新登记件结论只及标注与承接建议，不改分数。"},
 {"item": "特别核查㉚（R81）：同例再裁一件——AS-307 tradition 首行（FREEZE-r81 §一.2）",
  "conclusion": "AS-307 本轮主持再裁部分成立、不作废不重测（与 R80 同例同型）：卡面 tradition＝astrology、R81 basis 首行作「卡面未标注 tradition 字段，按题面体裁自决」属误读误述；实际所用 astrology 与卡面实质一致。本席只承接登记主持裁定、不重裁；r80 既有条目逐件原样不动，新旨承接建议汇编入本轮附则、自 R82 manifest 以新层落实（承 R79 BZ-037 同例新旨例）。",
  "evidence": "FREEZE-r81 §一.2 引文与 R81 prediction basis/systems_used 逐字断言通过；原卡 tradition＝astrology 在盘。",
  "scope_note": "本件不计新登记件数、不改总件数分布；另 32 件 LY tradition 旗标主持裁定不成立（检查器误报）只在 FREEZE-r81 登记、本席不入册（承 R80 LR3-004/104 中『只登记』口径中属主持件者从其例，此处明记）。"},
 {"item": "特别核查㉛（R81）：DIAG-H24 旗标候选 F1–F4 定案",
  "conclusion": "F1（DS-020）／F2（QM-307）／F3（GSZ-047）／F4（ZCB-014）四件逐件回原卡/金标结局核后均定案部分成立、新登记入册（registered_round＝81）：F1 张力属实而断面不全同；F2 reason 表述出入属实而金标数据本身无缺；F3 月柱原文含混属实而自注在盘、锚点全在场；F4 [?] 存疑标记属实而明示在盘、主结局可读。",
  "evidence": "落盘脚本逐件引文断言：F1 大师断语/结局、F2 输入卡 cast_time/结局/DIAG reason 原句、F3 输入卡「巳亥月」、F4 结局与输入卡 [?] 标记均逐字在盘。",
  "scope_note": "验收侧定案只及标注与承接建议，不改金标与任何分数。"},
 {"item": "特别核查㉜（R81）：验收侧旗标 QM-031 与 DIAG-H25 旗标候选 F1–F6 定案登记",
  "conclusion": "QM-031 定案部分成立、新登记入册：金标 master_prediction 内嵌原书复盘编辑注、金额口径（一万三/三万元与修订后十三万元）含混属实；编辑注明示在盘、结局与修订口径对应可核。DIAG-H25 旗标候选 F1–F6（GSZ-052／GSZ-060／GSZ-049／GSZ-053／GSZ-058／GSZ-061）于本席落盘过程中补齐落盘（§5 在盘），逐件回原卡/金标核后均定案部分成立、新登记入册：F1 金标两字段载录不一致属实而主体结局明载；F2 日干缺载与 grade_note 口径自相矛盾属实而缺载自注在盘；F3–F5 月建原文形态含混属实而自注在盘、锚点在场（承 H24 GSZ-047 例）；F6 对象信息缺载属实而锚点在场、断语结局对应可核。",
  "evidence": "QM-031 金标断语/结局逐字断言通过；DIAG-H25 §5 在盘断言通过，F1–F6 逐件引文断言（金标 outcome_record/grade_note、输入卡 asked_at/question）通过。",
  "scope_note": "验收侧定案只及标注与承接建议，不改金标与任何分数。"},
 {"item": "特别核查㉝（R81）：指令性字样特别核查基线六处复核（承 R80 附则 §四基线）",
  "conclusion": "基线六处经 R81 manifest 与 R81 评审包盘上复核在册、形态未变：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）逐字在场（BZ-042／BZ-105 本轮兼为新登记件、基线登记与标注并行不悖）；LR2-016 manifest editor_note 一处在 _r56_lr2016_split 分列层、全文恰出现 1 次；LR2-016 评审包 editor_note 层一处在 R81 judging 包中逐字在场。另 LY-204 本轮结局后段旧注层「勿以此断」字样已按数据处理（(c) 类 P3-c3590da9 定案承接既有部分成立）。无新增同型件登记。",
  "evidence": "脚本逐字断言：四例字样均在 cases 本体；editor_note 全句 manifest 全文计数 1、评审包在场断言通过。",
  "scope_note": "各席与本席均按数据处理、不作指令；只登记、不改文本。"},
 {"item": "特别核查㉞（R81）：待核四件维持登记与 LY-537 本轮触及关联；CZ-QX 维持 16",
  "conclusion": "BZ-029（俞大维卒年待核＋旗标错配线索）／BZ-040（许世英享年待核）／LY-537（「申予日」衍字疑）／YM-070（「甲寅旬」挂起）四件维持原登记，本轮不核查、不关闭。LY-537 本轮被平台评审旗标 P3-387ac185 触及（结局「果于申予日归」日名含讹字、与待核同例同旨），只登记关联、不并案、不改其未核状态；与待核 LY-537 关联之 P3-313b1a58（LY-538）旗标为同旨续接、只登记关联不并案。CZ-QX 维持 16 只登记、无增减。",
  "evidence": "R81 manifest cases[LY-537] 仍作『果于申予日归』（cases 载荷与 R80 逐字全等）；LY-537／YM-070 未核条目随 97 件全量承接在册。",
  "scope_note": "待核件无盘外独立史源不裁。"},
]

out = {
 "_provenance": "R81 数据席（附则承接对勘＋annotations 全量承接与本轮新定案，独立席位，不兼任本轮盲测/评审/诊断/组集/修订/集成，不改任何分数）：以 data/case-annotations-r80.json 为底承接全量 97 件（成立 12／部分成立 77／不成立 6／未核 2），前 97 件逐件原样、无删改（落盘脚本以数组全等断言验过）；承接对勘：R80 附则汇编 1 件（AS-307）已于 R81 manifest 以 _r80_carryover_notes_addendum 落实、逐字全等（1/1）；本轮新定案：平台评审新旗标 68 例去重后同旨续接 54 件＋待核触及 1 件（只登记、条目不动）、新登记 13 件全部部分成立；AS-307 经 FREEZE-r81 §一.2 同例再裁部分成立（只入特别核查与附则汇编、条目不动，承 BZ-037 例）；DIAG-H24 旗标候选 F1–F4 四件定案部分成立新登记；验收侧 QM-031 定案部分成立新登记；DIAG-H25 旗标候选 F1–F6 六件于落盘过程中补齐在盘、一并定案部分成立新登记。承接后总件数 121（成立 12／部分成立 101／不成立 6／未核 2）。指令性字样基线六处经 R81 manifest 与评审包复核在册、形态未变（见特别核查㉝）。待核四件 BZ-029／BZ-040／LY-537／YM-070 维持原登记、不核查不关闭。CZ-QX 维持 16 只登记。本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文；结局/注记文本内指令性字样一律按数据处理。",
 "round": 81,
 "annotations": annotations,
 "special_checks": special,
 "counts": {
   "base_file": "data/case-annotations-r80.json", "base_cases_total": 97,
   "base_verdicts": {"成立": 12, "部分成立": 77, "不成立": 6, "未核": 2},
   "carryover_check_r80_addendum": {"layer": "_r80_carryover_notes_addendum", "items": 1, "implemented": 1, "not_implemented": 0},
   "platform_judge_flags_r81_anons": 68, "platform_judge_flags_r81_cases": 68,
   "continuation_cases_r81": 54, "pending_touch_cases_r81": ["LY-537"],
   "same_case_readjudication_r81": ["AS-307"],
   "new_registrations_r81": 24,
   "new_partial_cases_r81": [e["case_id"] for e in new_entries],
   "diag_h24_flag_candidates": {"F1": "DS-020", "F2": "QM-307", "F3": "GSZ-047", "F4": "ZCB-014"},
   "acceptance_flags_r81": ["QM-031"],
   "diag_h25_flag_candidates": {"F1": "GSZ-052", "F2": "GSZ-060", "F3": "GSZ-049", "F4": "GSZ-053", "F5": "GSZ-058", "F6": "GSZ-061"},
   "cases_total": 121,
   "verdicts": {"成立": 12, "部分成立": 101, "不成立": 6, "未核": 2},
 },
}
p_out = BASE / "data/case-annotations-r81.json"
p_out.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
back = json.loads(p_out.read_text(encoding="utf-8"))
assert len(back["annotations"]) == 121 and Counter(a["disposition"] for a in back["annotations"]) == dist

# ---------- 附则（自 annotations 结构化直读生成，无正则抽取） ----------
lines = []
lines.append("# Manifest 承接册附则（R81）——R80 定案承接对勘（1 件全落实）＋R81 定案承接建议汇编（部分成立 25 件）")
lines.append("")
lines.append("## 卷首说明")
lines.append("")
lines.append("- 本附则为 Phase 3 Round 81（R81）数据席（工序：附则承接对勘＋annotations 全量承接与本轮新定案登记；独立席位，不兼任本轮盲测／评审／诊断／组集／修订／集成）产出。")
lines.append(f"- 对勘来源：`benchmark/phase3/runs/round81/judging/outcome-manifest.json`（本轮 manifest，新层 `_r80_carryover_notes_addendum` 1 件；全文 SHA-256＝`{sha81}`，本席复算）、`benchmark/phase3/data/manifest-carryover-r80-addendum.md`（R80 附则，其 §三汇编为 R80 定案部分成立 1 件）、`benchmark/phase3/data/case-annotations-r80.json`（结构化直读底本：annotations 97 件，定案分布成立 12／部分成立 77／不成立 6／未核 2）。")
lines.append("- 汇编来源：`benchmark/phase3/runs/round81/FREEZE-r81.md` §一.2（AS-307 再裁）、`benchmark/phase3/runs/round80/acceptance/DIAG-H24.md` §6（F1–F4）、`benchmark/phase3/data/case-annotations-r81.json`（本轮新登记 24 件），供 R82 manifest 以新层落实其中部分成立件（平台件以 `_r81_carryover_notes_addendum` 键名、验收侧件随后续金标／验收注记层承接）。")
lines.append("- **DIAG-H25 旗标候选 F1–F6 已一并定案**：`runs/round81/acceptance/DIAG-H25.md` §5 于本席落盘过程中补齐在盘，六件逐件定案部分成立、新登记入册（并见 §五.3）。")
lines.append("- **本件只汇编、对勘与登记，不改任何分数与结局原文、不改原卡、不改 manifest 任一侧。** 结局／注记文本内指令性字样一律按数据处理。")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 一、工序与口径")
lines.append("")
lines.append("- 工序一（对勘，见 §二）：`_r80_carryover_notes_addendum` 1 件核其是否已按 R80 附则所载文本落实于 R81 manifest 对应 case 的 carry 呈现——与 `case-annotations-r80.json` 对应条 `manifest_carry_suggestion` 逐字比对（该文本同时逐字在 R80 附则 §三.1）。")
lines.append("- 工序二（汇编，见 §三）：R82 承接建议汇编——本轮新定案部分成立共 25 件（新登记 24 件＋AS-307 同例再裁 1 件），逐件全列，文本自 `case-annotations-r81.json` 结构化直读生成（AS-307 新层文本照 R80 附则体例拟、见 §三.1 首件）。")
lines.append("- 工序三（标注落盘，见 §五）：`data/case-annotations-r81.json` 以 r80 件 97 件全量承接（逐件原样）＋本轮新登记 24 件，合计 121 件；同旨续接 54 件与待核触及 1 件只登记、条目不动。")
lines.append("- 特别核查（见 §四）：指令性字样特别核查基线六处复核，承 R80 附则 §四基线，只登记、不改文本。")
lines.append("- 供给与待核续记（见 §六）：CZ-QX 维持 16 只登记；待核四件维持登记。")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 二、对勘：R80 附则 1 件已于 R81 manifest 以 `_r80_carryover_notes_addendum` 落实（1/1）")
lines.append("")
lines.append("### 2.1 层实况登记（盘上直读）")
lines.append("")
lines.append("- R81 manifest 含新键 `_r80_carryover_notes_addendum`，共 **1 件**，键集＝{AS-307}，与 R80 附则 §三汇编清单全等；cases 载荷与 R80 manifest 深度全等（落盘脚本断言通过）。")
lines.append("")
lines.append("### 2.2 逐件对勘（1 件）")
lines.append("")
lines.append("| # | case_id | anon_id（R80） | R80 附则所载建议文本（＝落实层文本，逐字） | 结论 |")
lines.append("|---|---|---|---|---|")
lines.append(f"| 1 | AS-307 | P3-c6628422 | {layer['AS-307']} | 落实 |")
lines.append("")
lines.append("- 对勘结论：**1 件全部落实、未落实 0 件**——层文本与 R80 附则所载文本逐字全等（落盘脚本断言），无勘误，不静默改任一侧。")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 三、R82 承接建议汇编：R81 本轮新定案（部分成立 25 件逐件全列）")
lines.append("")
lines.append("- 落实键名写定：自 R82 manifest 起以 `_r81_carryover_notes_addendum` 键名落实本节平台件建议注记原文；验收侧件（DS-020／QM-307／GSZ-047／ZCB-014／QM-031／GSZ-052／GSZ-060／GSZ-049／GSZ-053／GSZ-058／GSZ-061）随后续金标／验收注记层承接、文本照录于本节。")
lines.append("")
lines.append("### 3.1 AS-307（同例再裁，FREEZE-r81 §一.2）")
lines.append("")
lines.append("- case_id：AS-307")
lines.append("- anon_id（R81）：P3-6e72b9e2（经 `runs/round81/judging/host-mapping.json` 对位）")
lines.append("- 裁定要旨：卡面 tradition＝astrology、basis 首行误读作未标注、实际所用 astrology 与卡面实质一致——部分成立，不作废不重测（与 R80 同例同型）。")
lines.append(f"- 承接注记建议文本（供 R82 manifest 落实，原文）：「{AS307_R82_TEXT}」")
lines.append("- 与既有承接册条目的关系：同例再裁（r80 条目逐件原样不动，承 R79 BZ-037 同例新旨例）；本轮汇编入册供 R82 以新层落实。")
lines.append("")
lines.append("### 3.2 新登记部分成立 18 件（自 annotations 结构化直读）")
lines.append("")
for i, e in enumerate(new_entries, 1):
    lines.append(f"#### N{i}. {e['case_id']}")
    lines.append("")
    lines.append(f"- case_id：{e['case_id']}")
    lines.append(f"- anon_id：{e['anon_id']}")
    lines.append(f"- 定案：{e['disposition']}（registered_round＝81；{e['relation']}）")
    lines.append(f"- 核对结论：{e['finding']}")
    lines.append(f"- 承接注记建议文本（原文）：「{e['manifest_carry_suggestion']}」")
    lines.append("")
lines.append("---")
lines.append("")
lines.append("## 四、指令性字样特别核查基线六处对勘（承 R80 附则 §四基线）")
lines.append("")
lines.append("- 基线构成：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）＋LR2-016 manifest editor_note 一处＋LR2-016 评审包 editor_note 层一处，共六处、分三层。本轮自 `runs/round81/judging/outcome-manifest.json` 与 R81 评审包盘上逐处回读原文复核，**只登记、不改文本**；各席与本席均按数据处理、不作指令。")
lines.append("")
lines.append("| case_id | 基线字样（按数据引录） | 本轮在盘形态 |")
lines.append("|---|---|---|")
lines.append("| BZ-036 | 结局含「盲测比对须注」 | 在册：在场、形态未变 |")
lines.append("| BZ-042 | 结局含「（盲测比对时以格局大富一项为主）」 | 在册：在场、形态未变（本轮兼新登记标注、并行不悖） |")
lines.append("| BZ-105 | 结局含「使用时须分开统计」 | 在册：在场、形态未变（本轮兼新登记标注、并行不悖） |")
lines.append("| LY-204 | 结局旧注层含「勿以此斷」 | 在册：在场、形态未变（本轮评审旗标 P3-c3590da9 触及、承接既有定案） |")
lines.append("")
lines.append("- LR2-016 manifest editor_note 一处：所在 manifest `_r56_lr2016_split` 分列层，本轮在盘原文逐字与基线全等、manifest 全文恰出现 1 次（落盘脚本断言）。")
lines.append("- LR2-016 评审包 editor_note 层一处：R81 评审包中同句逐字在场、与 manifest 分列层全等，另列一类、不并入 cases 本体基线计数。")
lines.append("- 结论：基线六处经 R81 盘上逐处回读在册、形态未变，出入 0 处。无新增同型件登记。本席只登记、不改任何文本。")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 五、annotations 落盘断言、同旨续接登记与 DIAG-H25 定案")
lines.append("")
lines.append("### 5.1 annotations 落盘断言（工序三）")
lines.append("")
lines.append("- 底本：`data/case-annotations-r80.json` annotations 97 件（成立 12／部分成立 77／不成立 6／未核 2），全量承接、逐件原样、无删改（落盘脚本以 annotations 数组前 97 件全等断言验过）。")
lines.append("- 新增登记：**24 件**，全部部分成立（平台新登记 13 件，见 §三.2 N1–N13；DIAG-H24 F1–F4 四件，见 N14–N17；验收侧 QM-031 一件，见 N18；DIAG-H25 F1–F6 六件，见 N19–N24）——落盘 `data/case-annotations-r81.json` annotations **121 件＝97＋24**（成立 12／部分成立 101／不成立 6／未核 2），各新件 `registered_round＝81`、字段完整（落盘脚本逐件断言），counts 相应更新，回读 JSON 可解析断言通过。")
lines.append("- 平台评审新旗标 68 例定案构成：新登记 13 件（上）；同旨续接 54 件（档位承既有定案、条目逐件原样不动，只登记）；待核触及 1 件（LY-537，见 §五.2）。AS-307 同例再裁 1 件只入特别核查㉚与 §三.1 汇编、不计新登记。")
lines.append("- special_checks 承接 r80 二十七件并新增 R81 七件（㉘ R80 承接 1 件落实对勘；㉙ 平台旗标 68 例总登记；㉚ AS-307 同例再裁；㉛ DIAG-H24 F1–F4 定案；㉜ QM-031 与 DIAG-H25 F1–F6 定案；㉝ 指令性字样基线六处复核；㉞ 待核四件维持与 CZ-QX），合计 34 件。")
lines.append("")
lines.append("### 5.2 R81 确认的待核维持清单（四件，维持挂起、不核查不关闭）")
lines.append("")
lines.append("| case_id | 状态登记（承 R80 附则 §5.2 口径续记） |")
lines.append("|---|---|")
lines.append("| BZ-029 | 俞大维卒年待核＋旗标错配线索，维持原登记、不裁；不入 annotations |")
lines.append("| BZ-040 | 许世英享年待核，维持原登记、不裁；不入 annotations |")
lines.append("| LY-537 | 「申予日」衍字疑，维持未核原登记；本轮被平台评审旗标 P3-387ac185 触及（同例同旨），只登记关联、不并案、不改待核状态；以未核条目随承接在 `case-annotations-r81.json` 内 |")
lines.append("| YM-070 | 「甲寅旬」出处待核，维持挂起；本轮无新触及登记；以未核条目随承接在 `case-annotations-r81.json` 内 |")
lines.append("")
lines.append("### 5.3 DIAG-H25 定案登记")
lines.append("")
lines.append("- **DIAG-H25 旗标候选 F1–F6 已定案入册**：该件 §5 于本席落盘过程中补齐在盘，六件（GSZ-052／GSZ-060／GSZ-049／GSZ-053／GSZ-058／GSZ-061）逐件回原卡/金标核后均定案部分成立、新登记入册（§三.2 N19–N24、特别核查㉜）。无顺延件。")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 六、供给台账续记（只登记）")
lines.append("")
lines.append("### 6.1 CZ-QX 维持 16")
lines.append("")
lines.append("- CZ-QX 维持 **16**，承 R80 附则 §6.1 登记口径由本席承接续记，本轮无增减。")
lines.append("")
lines.append("### 6.2 待核四件维持登记（与 §五.2 同口径）")
lines.append("")
lines.append("- BZ-029（俞大维卒年，另含旗标内容错配线索）、BZ-040（许世英享年）、LY-537（「申予日」衍字疑）、YM-070（「甲寅旬」挂起）四件维持登记，无盘外独立史源不裁。")
lines.append("")
addendum = "\n".join(lines)
# 逐件闭合验核：19 件建议文本全列、每件标题与文本各恰一次（结构化计数，非正则截断）
assert addendum.count("承接注记建议文本（原文）") == 24
assert addendum.count("承接注记建议文本（供 R82 manifest 落实，原文）") == 1
for e in new_entries:
    assert e["manifest_carry_suggestion"] in addendum
    assert f"#### N" in addendum
assert AS307_R82_TEXT in addendum
p_add = BASE / "data/manifest-carryover-r81-addendum.md"
p_add.write_text(addendum, encoding="utf-8")
print("annotations bytes", p_out.stat().st_size, "addendum bytes", p_add.stat().st_size)
print("total", len(back["annotations"]), dict(dist))
print("new", [e["case_id"] for e in new_entries])
