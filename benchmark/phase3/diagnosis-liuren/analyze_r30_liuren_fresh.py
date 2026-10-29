#!/usr/bin/env python3
"""R30 六壬新鲜例诊断：三批 36 例分数重构（只读既有定稿，不打分）。
批次: holdout9 LR2-001..012 / holdout10 LR3 12例 / round29 dev LR3 12例。
输出: R30-fresh-cases.jsonl（逐例 totals+分项差+门类+systems_used+文本指针）
用法: python3 analyze_r30_liuren_fresh.py
"""
import json, math, os, statistics

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # phase3/
OUT = os.path.join(BASE, "diagnosis-liuren", "R30-fresh-cases.jsonl")

def load(p):
    with open(os.path.join(BASE, p), encoding="utf-8") as f:
        return json.load(f)

def load_jsonl(p):
    with open(os.path.join(BASE, p), encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]

def mean_sub(rows):
    keys = ["direction", "claims", "timing"]
    return {k: round(sum(r[k] for r in rows) / len(rows), 4) for k in keys}

def merge_judges(judge_files, arb_file, disputes):
    """双席均值 + 分歧仲裁覆盖，返回 anon_id -> sub dict。"""
    per = {}
    for jf in judge_files:
        for r in load_jsonl(jf):
            per.setdefault(r["anon_id"], []).append(r)
    out = {}
    for anon, rows in per.items():
        m = mean_sub(rows)
        m["total"] = round(m["direction"] + m["claims"] + m["timing"], 4)
        out[anon] = m
    if arb_file:
        for r in load_jsonl(arb_file):
            if r["anon_id"] in disputes:
                out[r["anon_id"]] = {"direction": r["direction"], "claims": r["claims"],
                                     "timing": r["timing"], "total": r["total"]}
    return out

def se(vals):
    if len(vals) < 2:
        return None
    return round(statistics.stdev(vals) / math.sqrt(len(vals)), 3)

cases = []

# ---------- holdout9: final-scores 已含合并分项 ----------
fs9 = load("holdout9-acceptance/judging/final-scores.json")
hk9 = load("holdout9-acceptance/judging/host-key.json")
gold9 = {r["id"]: r for r in load_jsonl("holdout9/test_gold.jsonl")}
by_case9 = {}
for anon, info in hk9.items():
    by_case9.setdefault(info["case_id"], {})[info["source"]] = fs9["final"][anon]
pair9 = {p["case_id"]: p for p in fs9["pairs"]}
H9_IDS = [f"LR2-{i:03d}" for i in range(1, 13)]
for cid in H9_IDS:
    o, m = by_case9[cid]["ours"], by_case9[cid]["master"]
    assert abs(o["total"] - pair9[cid]["ours"]) < 1e-6 and abs(m["total"] - pair9[cid]["master"]) < 1e-6, cid
    pred = load(f"holdout9-acceptance/predictions/{cid}.json")
    g = gold9[cid]
    cases.append({
        "id": cid, "batch": "holdout9", "source_prefix": "LR2",
        "ours": o["total"], "master": m["total"],
        "diff": round(o["total"] - m["total"], 4),
        "ours_sub": {k: o[k] for k in ("direction", "claims", "timing")},
        "master_sub": {k: m[k] for k in ("direction", "claims", "timing")},
        "d_dir": round(o["direction"] - m["direction"], 4),
        "d_claims": round(o["claims"] - m["claims"], 4),
        "d_timing": round(o["timing"] - m["timing"], 4),
        "category": g.get("question_or_topic", ""),
        "source_work": g.get("source_work", ""),
        "systems_used": pred.get("systems_used"),
        "prediction_text": pred.get("prediction_text", ""),
        "basis": pred.get("basis", ""),
        "master_excerpt": (g.get("master_predictions") or [{}])[0].get("statement_excerpt", ""),
        "master_key_assertions": (g.get("master_predictions") or [{}])[0].get("key_assertions", []),
        "outcome": (g.get("outcome") or {}).get("description", ""),
    })

# ---------- holdout10: judgeA/B 均值 + 仲裁 ----------
disp10 = set(load("holdout10-acceptance/judging/disputes.json") if False else
             json.loads(open(os.path.join(BASE, "holdout10-acceptance/judging/disputes.json"), encoding="utf-8").read())
             ) if False else ["H10-011", "H10-014", "H10-036", "H10-052"]
merged10 = merge_judges(
    ["holdout10-acceptance/judging/judgeA-part1.jsonl", "holdout10-acceptance/judging/judgeA-part2.jsonl",
     "holdout10-acceptance/judging/judgeB-part1.jsonl", "holdout10-acceptance/judging/judgeB-part2.jsonl"],
    "holdout10-acceptance/judging/arbitration.jsonl", set(disp10))
hk10 = load("holdout10-acceptance/judging/host-key.json")
fs10 = load("holdout10-acceptance/judging/final-scores.json")
gold10 = {r["id"]: r for r in load_jsonl("holdout10/test_gold.jsonl")}
by_case10 = {}
for anon, info in hk10.items():
    by_case10.setdefault(info["case_id"], {})[info["source"]] = merged10[anon]
H10_IDS = ["LR3-001", "LR3-003", "LR3-005", "LR3-007", "LR3-009", "LR3-102",
           "LR3-105", "LR3-109", "LR3-111", "LR3-113", "LR3-115", "LR3-117"]
for cid in H10_IDS:
    o, m = by_case10[cid]["ours"], by_case10[cid]["master"]
    assert abs(o["total"] - fs10["pairs"][cid]["ours"]) < 0.01 and abs(m["total"] - fs10["pairs"][cid]["master"]) < 0.01, (cid, o, m, fs10["pairs"][cid])
    pred = load(f"holdout10-acceptance/predictions/{cid}.json")
    g = gold10[cid]
    ctx = g.get("context") if isinstance(g.get("context"), str) else (g.get("context_at_prediction") or "")
    cases.append({
        "id": cid, "batch": "holdout10", "source_prefix": "LR3",
        "ours": o["total"], "master": m["total"],
        "diff": round(o["total"] - m["total"], 4),
        "ours_sub": {k: o[k] for k in ("direction", "claims", "timing")},
        "master_sub": {k: m[k] for k in ("direction", "claims", "timing")},
        "d_dir": round(o["direction"] - m["direction"], 4),
        "d_claims": round(o["claims"] - m["claims"], 4),
        "d_timing": round(o["timing"] - m["timing"], 4),
        "category": g.get("question_or_topic") or ctx,
        "source_work": g.get("source_work", ""),
        "chart_complete": g.get("chart_complete"), "month_day_complete": g.get("month_day_complete"),
        "systems_used": pred.get("systems_used"),
        "prediction_text": pred.get("prediction_text", ""),
        "basis": pred.get("basis", ""),
        "master_excerpt": (g.get("master_predictions") or [{}])[0].get("statement_excerpt", ""),
        "master_key_assertions": (g.get("master_predictions") or [{}])[0].get("key_assertions", []),
        "outcome": (g.get("outcome") or {}).get("description", "") if isinstance(g.get("outcome"), dict) else str(g.get("outcome", "")),
    })

# ---------- round29 dev LR3: ours_sub + dev9-baseline-build 大师分项 ----------
fs29 = load("runs/round29/final-scores.json")
mb29 = load("data/master-baseline-dev9.json")
disp_d9 = set(json.loads(open(os.path.join(BASE, "data/dev9-baseline-build/disputes.json"), encoding="utf-8").read())["disputes"]) \
    if isinstance(json.loads(open(os.path.join(BASE, "data/dev9-baseline-build/disputes.json"), encoding="utf-8").read()), dict) \
    else set(json.loads(open(os.path.join(BASE, "data/dev9-baseline-build/disputes.json"), encoding="utf-8").read()))
merged_d9 = merge_judges(
    ["data/dev9-baseline-build/judgeA-part1.jsonl", "data/dev9-baseline-build/judgeA-part2.jsonl",
     "data/dev9-baseline-build/judgeB-part1.jsonl", "data/dev9-baseline-build/judgeB-part2.jsonl"],
    "data/dev9-baseline-build/arbitration.jsonl", disp_d9)
hk_d9 = load("data/dev9-baseline-build/host-key.json")  # anon -> case_id (master only)
master_sub29 = {}
for anon, cid in hk_d9.items():
    if cid.startswith("LR3") and anon in merged_d9:
        master_sub29[cid] = merged_d9[anon]
exp9 = {}
for part in ("liuren-chen1", "liuren-chen2"):
    for r in load_jsonl(f"expansion9/{part}/cases.jsonl"):
        exp9[r["id"]] = r
DEV_IDS = ["LR3-002", "LR3-004", "LR3-006", "LR3-008", "LR3-010", "LR3-101",
           "LR3-104", "LR3-107", "LR3-110", "LR3-112", "LR3-114", "LR3-116"]
for cid in DEV_IDS:
    o = fs29["ours_sub"][cid]
    mtot = mb29[cid]["total"]
    m = master_sub29.get(cid)
    if m is not None:
        assert abs(m["total"] - mtot) < 0.26, (cid, m, mtot)  # 容仲裁/取整差
    pred = load(f"runs/round29/predictions/{cid}.json")
    g = exp9.get(cid, {})
    inp = load(f"inputs-dev9/{cid}.json")
    q = ((inp.get("context") or {}).get("question")) or g.get("question_or_topic", "")
    cases.append({
        "id": cid, "batch": "dev9-R29", "source_prefix": "LR3",
        "ours": fs29["ours_axis2"][cid], "master": mtot,
        "diff": round(fs29["ours_axis2"][cid] - mtot, 4),
        "ours_sub": {k: o[k] for k in ("direction", "claims", "timing")},
        "master_sub": ({k: m[k] for k in ("direction", "claims", "timing")} if m else None),
        "d_dir": (round(o["direction"] - m["direction"], 4) if m else None),
        "d_claims": (round(o["claims"] - m["claims"], 4) if m else None),
        "d_timing": (round(o["timing"] - m["timing"], 4) if m else None),
        "category": q,
        "source_work": g.get("source_work", ""),
        "systems_used": pred.get("systems_used"),
        "prediction_text": pred.get("prediction_text", ""),
        "basis": pred.get("basis", ""),
        "master_excerpt": (g.get("master_predictions") or [{}])[0].get("statement_excerpt", ""),
        "master_key_assertions": (g.get("master_predictions") or [{}])[0].get("key_assertions", []),
        "outcome": (g.get("outcome") or {}).get("description", "") if isinstance(g.get("outcome"), dict) else "",
    })

# ---------- 败例归因（诊断角逐例读 basis+大师原断+结局后人工分类，互斥主类） ----------
# A 章内有条未用/用反; B 章内无条目(细断识别层); C 输入决定性字段缺失; D 量级/两段程度错位; E 应期档位/取法
CLASS = {
 "LR2-001": ("A", "§六.6婚姻主断含日辰相合相生一路，basis全程未核干支合/支上生干上，只以蒿矢+退茹+初传克日压财旺定不成", "—"),
 "LR2-002": ("B", "§六.10性别三路无纯阴返阳判男、胎神夹克/子宿冲克断夭年条；我方自创传支皆阴判女、应期压日档产厄", "E"),
 "LR2-003": ("B", "§六.9考试无已试后伏吟必中、双课名次先后次第法；我方只以伏吟迟滞+禄位分判，一中一不中", "C(酉时课天将/四课未给)"),
 "LR2-004": ("B", "暗拱年命定独中只见§六.4.8公讼赦路人助层，考试门无此迁移条；我方以父母不入传+无禄定八人全落", "C(八人年命未给)"),
 "LR2-006": ("B", "§六.9考试无河魁临干发用/贵居命年/朱雀遁乙奇乘长生/盘珠格等干上四课层吉象组；我方以父母朱雀不入传定不中", "C(年命未给)"),
 "LR2-009": ("A", "§六.9取用明列青龙为迁转之将，basis却以午火为兄弟非官禄迳废青龙发用升迁路；且未作升迁+意外之忧两段断", "B(太岁作鬼冲龙断灾细象)"),
 "LR2-010": ("B", "§六.9/§二.4无太岁月建生日定速迁、蒿矢逢金成簇、贵德驿马城吏全逢诸细象；我方以末传天空+遥克总象压初传官乘贵人", "A(末传权重)"),
 "LR2-011": ("E", "方向断语与大师同向，亏损全在timing(-1.75)：大师巳年年档，我方按月档取酉逢值；§七.3仕宦干年支月推的年坐标未走", "—"),
 "LR3-001": ("E", "终局向贵与大师同、dir/claims差均为0，亏损全在timing(-1.0)：我方年档午年，大师明春起官；近程起官点未识别", "B(禄马生龙神起官期)"),
 "LR3-007": ("D", "铸印迁转第一段同向，远段我方断止步、大师难久任后降职，程度差一档；仲裁H10-014同旨", "B(贵临空害断难久任)"),
 "LR3-009": ("C", "大师全断系于兄/蔡二命支分指(亥贵官星临支为兄命、辰为蔡命)，basis自记年命未给，双对象分指在输入层无据", "B(双命分推先后条)"),
 "LR3-105": ("B", "§六.12章奏无天驿二马加临年命/德马夹克/天马恋长生/朱雀空文书不就组合；我方以贵人发用+曲直局生身定允，与大师全反", "C(年命未给)"),
 "LR3-109": ("A", "§六.12钦差细断明载只论马不论禄、basis亦自引，却以末传子水北位定南北，未以马(巳/其长生午)定方；后拈利一段反断对", "B(马长生定方细法)"),
 "LR3-111": ("B", "章内无不言所事的来意推断门(干上神定事类/河魁加命马临行年断相携)；我方迳收贼盗单门断防盗小失", "C(行年未给)"),
 "LR3-113": ("E", "dir/claims不亏，timing-0.5：连茹逢空下大师断尚未起程、九月子丑日到，我方以末传逢值定九日内戌日，迟归档位未识别", "B(连茹逢空断未起程)"),
 "LR3-115": ("B", "游都贼符只列§六.11兵斗取用名目，无夜惊应候以游都贼符定贼至方所之条；我方以白虎临门断伤折", "—"),
 "LR3-117": ("B", "章内无射覆门：东方朔遁甲取传重排、亥主图书、页数断法全缺；我方以§五支类象拼金银钱", "—"),
 "LR3-002": ("B", "§六.11兵斗无回马剥官煞/干败支墓乘火鬼/天魁合犯煞/旅焚细象；我方以炎上+末传生干定偏吉可成，与大师兴师无济全反", "A(干支互乘墓条未用)"),
 "LR3-004": ("B", "§六.9无本命丁马恩星化凶/蛇化为龙化吉组合(恩星条只在§六.4.4公讼)；我方以官乘玄武+八专定暗滞，与大师远大显赫全反", "C(年命未给)"),
 "LR3-006": ("B", "§六.9无四课城吏/二马出现/传将递互相生定荣转细则，官星不入三传时无替代判据；我方以官印不入传定虚望", "C(行年未给)"),
 "LR3-008": ("B", "§六.9/§三无干上贵人乘进气仲冬填实/虎马丁神作岁君生日/四墓覆生已废复兴组合；我方以绝嗣+八专压铸印定有始无终", "A(格权重+四课层未核)"),
 "LR3-101": ("B", "§六.9考试只有兼看帘幕贵一句、无皇恩发用/幕贵/末见长生太阳/朱雀生太岁识别细则(皇恩起例只在§六.4公讼)；我方以蒿矢+父母乘玄武定不中", "A(朱雀须入传为自加条件)"),
 "LR3-107": ("B", "章内无人物占门：临身贵人定科第、姓氏推断、岁破发用断获罪全缺；我方以天将阴私象拼暗昧可疑", "C(课体名残泐存疑)"),
 "LR3-110": ("E", "主坐标与大师同为乙巳填实日，timing仍-0.5：窗口我方本旬内、大师三日内，窗口宽度粒度差；总差仅-0.5，近噪声", "—"),
 "LR3-112": ("B", "§六.5无玄墓发用收魂杀/纯财生官死气克日远年断、病课兼断贼至条；总差仅-0.5且大师远断未见应验记载，轻度", "—"),
 "LR3-114": ("B", "章内无鸣占/应候门以贼盗方所人数细断应事；我方以传水生干+太常断小吉无祸，与大师贼劫邻人全反", "—"),
 "LR3-116": ("B", "章内无射覆门：刚日发用日上神射法/支色双义/天医断药/四八数全缺；我方以支类象拼布帛手帕", "C(三传天干/旬空未载)"),
}
for c in cases:
    if c["diff"] < 0:
        cat, note, sec = CLASS[c["id"]]
        c["primary_category"] = cat
        c["category_note"] = note
        c["secondary"] = sec
    else:
        c["primary_category"] = None
        c["category_note"] = ""
        c["secondary"] = ""

assert len(cases) == 36, len(cases)
with open(OUT, "w", encoding="utf-8") as f:
    for c in cases:
        f.write(json.dumps(c, ensure_ascii=False) + "\n")

for batch in ("holdout9", "holdout10", "dev9-R29", "ALL"):
    sub = [c for c in cases if batch == "ALL" or c["batch"] == batch]
    diffs = [c["diff"] for c in sub]
    print(f"{batch}: n={len(sub)} ours={statistics.mean([c['ours'] for c in sub]):.3f} "
          f"master={statistics.mean([c['master'] for c in sub]):.3f} diff={statistics.mean(diffs):.3f} SE={se(diffs)} "
          f"W/T/L={sum(1 for d in diffs if d>0)}/{sum(1 for d in diffs if d==0)}/{sum(1 for d in diffs if d<0)}")
    for k in ("d_dir", "d_claims", "d_timing"):
        vals = [c[k] for c in sub if c[k] is not None]
        if vals:
            print(f"   {k}: mean={statistics.mean(vals):.3f} sum={sum(vals):.2f} n={len(vals)} SE={se(vals)}")
from collections import Counter, defaultdict
cat_cases = defaultdict(list)
for c in cases:
    if c["primary_category"]:
        cat_cases[c["primary_category"]].append(c)
for cat in "ABCDE":
    sub = cat_cases[cat]
    if not sub:
        continue
    by_batch = Counter(x["batch"] for x in sub)
    print(f"CAT {cat}: n={len(sub)} sumDiff={sum(x['diff'] for x in sub):.2f} "
          f"d_dir={sum(x['d_dir'] for x in sub):.2f} d_claims={sum(x['d_claims'] for x in sub):.2f} "
          f"d_timing={sum(x['d_timing'] for x in sub):.2f} batches={dict(by_batch)} ids={[x['id'] for x in sub]}")
print("written", OUT)
