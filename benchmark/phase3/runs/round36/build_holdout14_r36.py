#!/usr/bin/env python3
"""R36 data-corner: build holdout14 (gold + input cards).

Composition is fixed by the host's ruling (mechanical execution):
  C = all remaining CZ (file order)                       = 13
  Y = qualified liuyao from task 1 (BQ-026..034)          = 9
  B = PU-003, PU-008 (the only two contamination exceptions,
      A-low on the grade axis per CENSUS-BZ regrade; high
      contamination noted per-case in SEALED for stratified
      acceptance reporting)                               = 2
  L = floor((2/3) * (C+Y+B)) liuren                       = 16
  T = C+Y+B+L                                             = 40
Liuren split (holdout13 ratio DA8/BY5/CY3 @ L16):
  DA = ceil(L/2) = 8, BY = 5, CY = 3 (CY <= 0.2*T = 8).
Each source takes cases in its file's existing order, skipping the
exclusion set: dev9 (inputs-dev11 filenames) + holdout3..holdout13 gold
ids + expansion12/POOL-IDS.txt. Zero intersection is asserted.

Gold rows are the source rows verbatim, EXCEPT the PREREG §6(1)(2)
predicate-hygiene rule: an outcome tail that is an extractor-written
verdict / meta note (OC-023 type) is moved out of outcome.description
into a new top-level field `extractor_verdict_tail`, verbatim, and each
such case is registered in facts + BUILD-LOG. Affected: CZ-018, CZ-020,
CZ-022, CZ-023, CZ-027, CZ-028, PU-003, PU-008 (8 cases). Reviewed and
kept verbatim (event paraphrase glosses, no verdict/coverage content):
CZ-019, CZ-026, CZ-030, CZ-031, CZ-032, CZ-033.

Input cards follow holdout12/13 formats per source; DA charts verbatim
from liuren-duanan/scratch-archive/cases_raw.json; BY charts are the
data corner's visual transcription of the typeset PDF pages (literals
below with page cites); CY cards are ganzhi-level; BQ cards follow the
expansion7 inputs format; PU cards follow the QL card format.

Outputs: benchmark/phase3/holdout14/test_gold.jsonl,
benchmark/phase3/holdout14-inputs/<id>.json, facts JSON next to this
script. No git operations. No prediction, no scoring.
"""
import hashlib
import json
import math
import re
from pathlib import Path

R36 = Path(__file__).resolve().parent
P3 = R36.parents[1]
EXP = P3 / "expansion12"


def load_jsonl(p):
    return [json.loads(l) for l in Path(p).read_text(encoding="utf-8").splitlines() if l.strip()]


# ---------- reserves (all sources, file order) ----------
da_all = load_jsonl(EXP / "liuren-duanan/cases-a.jsonl") + load_jsonl(EXP / "liuren-duanan/cases-b.jsonl")
da_elig = [r for r in da_all if r["holdout_eligible"]]
by_rev = load_jsonl(EXP / "liuren-bianyi-yuce/cases-reviewed.jsonl")
by_seal = [r for r in by_rev if r["review"]["verdict"] == "seal"]
cy_all = load_jsonl(EXP / "liuren-cuiyan/cases-munong.jsonl") + load_jsonl(EXP / "liuren-cuiyan/cases-juan5.jsonl")
cy_elig = [r for r in cy_all if r["holdout_eligible"]]
cz_all = load_jsonl(EXP / "online-routes/cases.jsonl")
bq_all = load_jsonl(EXP / "bushi-quanshu-beixuan/cases.jsonl")
nb2_rev = load_jsonl(EXP / "natal-batch2/cases-reviewed.jsonl")
pu_rows = {r["id"]: r for r in nb2_rev if r["id"] in ("PU-003", "PU-008")}
assert len(bq_all) == 9 and set(pu_rows) == {"PU-003", "PU-008"}

# ---------- exclusions ----------
dev_ids = {p.stem for p in (P3 / "inputs-dev11").glob("*.json")}
assert len(dev_ids) == 487
prior_holdout_ids = set()
for n in range(3, 14):
    prior_holdout_ids |= {r["id"] for r in load_jsonl(P3 / f"holdout{n}/test_gold.jsonl")}
pool_ids = set((EXP / "POOL-IDS.txt").read_text(encoding="utf-8").split())
excluded = dev_ids | prior_holdout_ids | pool_ids

# ---------- composition (host formula, mechanical) ----------
def take(rows, k, label):
    if k is None:
        picked = [r for r in rows if r["id"] not in excluded]
    else:
        picked = [r for r in rows if r["id"] not in excluded][:k]
        assert len(picked) == k, (label, [r["id"] for r in picked])
    return picked

cz_pick = take(cz_all, None, "CZ")
C = len(cz_pick)
assert C == 13, [r["id"] for r in cz_pick]
bq_pick = take(bq_all, None, "BQ")
Y = len(bq_pick)
assert Y == 9, [r["id"] for r in bq_pick]
pu_pick = [pu_rows["PU-003"], pu_rows["PU-008"]]
assert not ({r["id"] for r in pu_pick} & prior_holdout_ids)
assert not ({r["id"] for r in pu_pick} & dev_ids)
# PU ids ARE in POOL-IDS by construction of the natal pool bookkeeping?
# (checked explicitly in facts; the host ruling admits exactly these two,
#  their eligibility flows from CENSUS-BZ + host ruling, not POOL-IDS.)
B = len(pu_pick)
L = (2 * (C + Y + B)) // 3
assert L == 16, (C, Y, B, L)
n_da = math.ceil(L / 2)
n_cy = 3
n_by = L - n_da - n_cy
assert (n_da, n_by, n_cy) == (8, 5, 3)
T = C + Y + B + L
assert T == 40 and n_cy <= 0.2 * T

picks = []  # (source_label, row)
for r in take(da_elig, n_da, "DA"):
    picks.append(("DA", r))
for r in take(by_seal, n_by, "BY"):
    picks.append(("BY", r))
for r in take(cy_elig, n_cy, "CY"):
    picks.append(("CY", r))
for r in bq_pick:
    picks.append(("BQ", r))
for r in pu_pick:
    picks.append(("PU", r))
for r in cz_pick:
    picks.append(("CZ", r))
assert len(picks) == T
pick_ids = [r["id"] for _, r in picks]
assert len(set(pick_ids)) == T
assert not (set(pick_ids) & (dev_ids | prior_holdout_ids)), set(pick_ids) & (dev_ids | prior_holdout_ids)
pool_hits = sorted(set(pick_ids) & pool_ids)

# ---------- four-item verification + grade/contamination basis ----------
checks = {}
for label, r in picks:
    cid = r["id"]
    issues = []
    if label == "BY":
        grade = r["review"]["grade_final"]; contam = r["review"]["contamination_final"]
    elif label == "PU":
        grade = "A-low(CENSUS-BZ改判,分级轴)"; contam = r["review"]["contamination_final"]
    else:
        grade = r["outcome_grade"]; contam = r["contamination"]
    if label == "PU":
        if contam != "high":
            issues.append(f"PU exception expects high, got {contam}")
    else:
        if not str(grade).startswith("A"):
            issues.append(f"grade={grade}")
        if contam != "low":
            issues.append(f"contamination={contam}")
    preds = r.get("master_predictions") or []
    if not preds or not str(preds[0].get("statement_excerpt", "")).strip():
        issues.append("no prediction excerpt")
    outc = r.get("outcome") or {}
    desc = outc.get("description", "") if isinstance(outc, dict) else str(outc)
    if not str(desc).strip():
        issues.append("no outcome description")
    checks[cid] = {"source": label, "grade_basis": grade, "contamination": contam, "issues": issues}
    assert not issues, (cid, issues)

# ---------- triple keys: within picks, vs holdout12 + holdout13 ----------
def triple(row):
    if "context" in row and isinstance(row.get("subject"), dict):
        c = row["context"]
        return (row["subject"].get("name_or_desc", ""), c.get("asked_at", ""), c.get("question", ""))
    if row["id"].startswith("BQ-"):
        return (str(row.get("subject", "")), str(row.get("asked_at", "")),
                str(row.get("question", "")) + "|" + row["hexagram"]["original_name"])
    return (str(row.get("subject", "")), str(row.get("asked_at", "")), str(row.get("question_or_topic", "")))

def norm(s):
    return re.sub(r"\s+", "", str(s))

triples = {r["id"]: tuple(norm(x) for x in triple(r)) for _, r in picks}
seen = {}
for cid, t in triples.items():
    assert t not in seen, (cid, seen.get(t))
    seen[t] = cid
for hn in ("holdout12", "holdout13"):
    h_triples = {tuple(norm(x) for x in triple(r)) for r in load_jsonl(P3 / f"{hn}/test_gold.jsonl")}
    clash = set(triples.values()) & h_triples
    assert not clash, (hn, clash)

# ---------- predicate hygiene: strip extractor verdict tails ----------
TAILS = {
    "CZ-018": "（成婚日期与所断尽合）",
    "CZ-020": "——经营品类、路线、前次亏折、本次合伙均获具体确认。",
    "CZ-022": "（原文作『次以二人同至』，『以』疑为『日』之讹，转录照原文，校记于此）",
    "CZ-023": "（与所断豹尾对应）",
    "CZ-027": "（榜文公布后与所断合）",
    "CZ-028": "——议婚地点（都中、非本郡、远隔五百余里）与对象门第（大贵）获具体确认。成婚结局未载。",
    "PU-003": "（结局为道教传说性质，书内具体可分离）",
    "PU-008": "（结局为传说性质，书内可分离，无确切卒年）",
}
KEPT_REVIEWED = ["CZ-019", "CZ-026", "CZ-030", "CZ-031", "CZ-032", "CZ-033"]
rows_by_id = {r["id"]: r for _, r in picks}
for cid in KEPT_REVIEWED:
    assert cid in rows_by_id
stripped = {}
gold_rows = []
for label, r in picks:
    cid = r["id"]
    if cid in TAILS:
        desc = r["outcome"]["description"]
        tail = TAILS[cid]
        r = json.loads(json.dumps(r))  # copy; source file untouched
        if desc.endswith(tail):
            r["outcome"]["description"] = desc[: -len(tail)]
        elif desc.endswith(tail + "。"):  # parenthetical just before final stop (CZ-023)
            r["outcome"]["description"] = desc[: -(len(tail) + 1)] + "。"
        else:
            raise AssertionError((cid, desc[-60:]))
        assert r["outcome"]["description"].strip()
        r["extractor_verdict_tail"] = tail
        stripped[cid] = tail
    gold_rows.append(r)
assert set(stripped) == set(TAILS)

# ---------- gold ----------
gold_path = P3 / "holdout14/test_gold.jsonl"
gold_path.parent.mkdir(parents=True, exist_ok=True)
gold_text = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in gold_rows)
gold_path.write_text(gold_text, encoding="utf-8")
gold_sha = hashlib.sha256(gold_path.read_bytes()).hexdigest()

# ---------- input cards ----------
inputs_dir = P3 / "holdout14-inputs"
inputs_dir.mkdir(parents=True, exist_ok=True)
raw_da = {c["n"]: c for c in json.loads(
    (EXP / "liuren-duanan/scratch-archive/cases_raw.json").read_text(encoding="utf-8"))}

GEN = "贵蛇雀合勾龙青空虎常玄阴后朱"
def da_chart(cid):
    n = int(cid.split("-")[1])
    lines = [l.rstrip() for l in raw_da[n]["raw"].split("\n")]
    hi = next(i for i, l in enumerate(lines)
              if "日" in l and ("将" in l or "时" in l) and ("旬" in l or "年" in l))
    block = []
    for l in lines[hi + 1:]:
        if "先生曰" in l:
            break
        s = l.strip()
        if not s:
            if block:
                break
            continue
        if any(m in s for m in ("，", "。", "：")):
            continue
        block.append(s)
    text = "\n".join(block)
    trans = re.findall(
        r"([父母兄子财官鬼孙])\s+([甲乙丙丁戊己庚辛壬癸]?[子丑寅卯辰巳午未申酉戌亥])\s+([" + GEN + r"])[◎⊙]*\s*$",
        text, flags=re.M)
    assert len(trans) == 3, (cid, trans, text)
    return text, "；".join(f"{a}{b}（{c}）" for a, b, c in trans)

BY_CHARTS = {
    "BY-007": {"课式": "日禄临支、交车相合、有始无终、闭口卦体、虎临干鬼",
               "三传": "父午（太阴）、官卯（白虎）、财子（勾陈）",
               "四课": "天将 白阴青常／上 卯午丑辰／下 午酉辰己",
               "天地盘": "空白常元／寅卯辰巳／青丑 午阴／勾子 未后／亥戌酉申／合朱蛇贵"},
    "BY-008": {"课式": "避难逃生、日禄归支",
               "三传": "子申（青龙）、财亥（朱雀）、鬼寅（天后）",
               "四课": "天将 青常朱青／上 申巳亥申／下 巳寅申戌",
               "天地盘": "青勾合朱／申酉戌亥／空未 子蛇／白午 丑贵／巳辰卯寅／常元阴后"},
    "BY-009": {"课式": "朽木难雕、初遭夹克、交车相合",
               "三传": "父戌（六合）、官巳（太阴）、子子（青龙）",
               "四课": "天将 青阴合常／上 子巳戌卯／下 巳戌卯庚",
               "天地盘": "青空白常／子丑寅卯／勾亥 辰元／合戌 巳阴／酉申未午／朱蛇贵后"},
    "BY-010": {"课式": "众鬼全彰、传遇三奇",
               "三传": "鬼卯（六合）、官寅（朱雀）、兄丑（螣蛇）",
               "四课": "天将 合勾龙空／上 卯辰巳午／下 辰巳午己",
               "天地盘": "勾青空白／辰巳午未／合卯 申常／朱寅 酉元／丑子亥戌／蛇贵后阴"},
    "BY-011": {"课式": "狐假虎威、三六相合、传财化鬼、辛日逢丁",
               "三传": "父未（白虎）、财卯（天后）、子亥（六合）",
               "四课": "天将 白合贵常／上 未亥寅午／下 亥卯午辛",
               "天地盘": "蛇贵后阴／丑寅卯辰／朱子 巳元／合亥 午常／亥酉申未／勾青空白"},
}
CY_RENDER = {"CY-005": "cy-p-154.png", "CY-006": "cy-p-154.png", "CY-008": "cy-p-154.png"}

card_notes = {}
def prov_flat(r):
    p = r["provenance"]
    return {"book": p["work"], "edition": p["edition"], "page": p["page"]}

for label, r in picks:
    cid = r["id"]
    if label == "CZ":
        card = {"id": cid, "subject": r["subject"],
                "context": {"question": r["context"]["question"],
                            "asked_at": r["context"]["asked_at"],
                            "setting": r["context"]["setting"],
                            "attachments": {"所测字": r["context"]["attachments"]["character_written"]}},
                "provenance": r["provenance"], "language": r["language"]}
        card_notes[cid] = "沿原 context 建卡；attachments 剔除 method_hint（断语侧理据）、仅留所测字；源行 grade_note/notes 未入卡"
    elif label == "PU":
        att = {"四柱": r["chart"]["pillars"]}
        if r["chart"].get("gender"):
            att["性别"] = r["chart"]["gender"]
        card = {"id": cid, "subject": {"name_or_desc": r["subject"]},
                "context": {"question": r["question_or_topic"], "asked_at": r["asked_at"],
                            "setting": r["context_at_prediction"], "attachments": att},
                "provenance": prov_flat(r), "language": r["provenance"]["language"]}
        card_notes[cid] = "四柱/性别自源行 chart 字段入 attachments；context 原文为空未填；源行 grade_note/review 未入卡"
    elif label == "BQ":
        card = {"id": cid, "tradition": "六爻",
                "subject": {"name_or_desc": r["subject"], "gender": None},
                "context": {"question": r["question"], "asked_at": r["asked_at"],
                            "setting": r["question"],
                            "attachments": {"casting_method": r["casting_method"],
                                            "hexagram": r["hexagram"]["original_name"] + (
                                                " 之 " + r["hexagram"]["changed_name"] if r["hexagram"]["changed_name"] else ""),
                                            "chart_excerpt": r["hexagram"]["chart_lines"],
                                            "chart_complete": r["chart_complete"],
                                            "completeness_basis": r["completeness_basis"]}},
                "provenance": {"book": r["provenance"]["work"], "edition": r["provenance"]["edition"],
                               "page": r["provenance"]["page"], "claimed_source": r["provenance"]["claimed_source"]},
                "language": "zh-Hans"}
        card_notes[cid] = "照 expansion7 inputs 体例建卡（占问背景＋卦象，无断语/结局）；grade_note/comment 未入卡"
    elif label == "DA":
        chart_text, trans = da_chart(cid)
        mj = re.search(r"([子丑寅卯辰巳午未申酉戌亥])将", r["asked_at"]).group(1) + "将"
        xk = re.search(r"甲[子丑寅卯辰巳午未申酉戌亥]旬，[子丑寅卯辰巳午未申酉戌亥]{2}空", r["asked_at"]).group(0)
        card = {"id": cid, "subject": {"name_or_desc": r["subject"]},
                "context": {"question": r["question_or_topic"], "asked_at": r["asked_at"],
                            "setting": r["context_at_prediction"],
                            "attachments": {"课盘原文": chart_text, "三传": trans, "月将": mj, "旬空": xk}},
                "provenance": prov_flat(r), "language": r["provenance"]["language"]}
        card_notes[cid] = "课盘原文/三传自 scratch-archive/cases_raw.json 原文直录（评注续行已滤除、只留盘列）；grade_note 未入卡"
    elif label == "BY":
        card = {"id": cid, "subject": {"name_or_desc": r["subject"]},
                "context": {"question": r["question_or_topic"], "asked_at": r["asked_at"],
                            "setting": r["context_at_prediction"],
                            "attachments": BY_CHARTS[cid]},
                "provenance": prov_flat(r), "language": r["provenance"]["language"]}
        card_notes[cid] = "课式/三传/四课/天地盘自原书排印本 PDF 页图直录（数据角视觉转录，2026-10-30，200dpi）；排印本玄武省作「元」、三传天将按全称记、四课与天地盘天将行照原字（BY-010 四课天将行第三字原字作「龙」）；grade_note/review 未入卡"
    elif label == "CY":
        card = {"id": cid, "subject": {"name_or_desc": r["subject"]},
                "context": {"question": r["question_or_topic"], "asked_at": r["asked_at"],
                            "setting": r["context_at_prediction"],
                            "attachments": {"干支占时": r["asked_at"],
                                            "note": f"原书页图有课盘列（liuren-cuiyan/render/{CY_RENDER[cid]}），转录底稿 TRANSCRIPTION-NOTES.md 未录盘字、页图盘字漫漶，本卡不臆录，仅录干支/月将/占时"}},
                "provenance": prov_flat(r), "language": r["provenance"]["language"]}
        card_notes[cid] = "仅干支级建卡（原书有课盘列但转录未录盘字，不臆录）；grade_note 未入卡"
    blob = json.dumps(card, ensure_ascii=False)
    for bad in ("grade_note", "master_predictions", "method_hint", '"outcome"', '"review"', "contamination", "extractor_verdict_tail"):
        assert bad not in blob, (cid, bad)
    (inputs_dir / f"{cid}.json").write_text(
        json.dumps(card, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

facts = {
    "composition": {"C_cz": C, "Y_bq": Y, "B_pu": B, "L_liuren": L, "T": T,
                    "DA": n_da, "BY": n_by, "CY": n_cy},
    "pick_ids": pick_ids,
    "picks_by_source": {lab: [r["id"] for l2, r in picks if l2 == lab]
                        for lab in ("DA", "BY", "CY", "BQ", "PU", "CZ")},
    "checks": checks,
    "triples": {k: list(v) for k, v in triples.items()},
    "pool_ids_hits": pool_hits,
    "stripped_verdict_tails": stripped,
    "kept_reviewed_outcomes": KEPT_REVIEWED,
    "gold_sha256": gold_sha,
    "card_notes": card_notes,
    "excluded_counts": {"dev9": len(dev_ids), "prior_holdout_ids": len(prior_holdout_ids),
                        "pool_ids": len(pool_ids)},
}
(R36 / "build_holdout14_facts_r36.json").write_text(
    json.dumps(facts, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps({"composition": facts["composition"], "picks": facts["picks_by_source"],
                  "pool_ids_hits": pool_hits, "gold_sha256": gold_sha,
                  "stripped": list(stripped)}, ensure_ascii=False, indent=1))
print("cards written:", len(list(inputs_dir.glob('*.json'))))
