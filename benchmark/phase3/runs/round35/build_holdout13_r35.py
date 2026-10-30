#!/usr/bin/env python3
"""R35 data-corner: build holdout13 (gold + input cards) per PREREG §6.2.

Selection rule (anti-cherry-picking, per tasking): within each source, take
cases in the source file's existing order, skipping holdout12-used ids,
until the source quota is met. Quotas: DA 8, BY 5, CY(munong) 3, QL 10
(all remaining seal), NL 2 (all remaining sealable), CZ 12, HZ 0 (census).
Total 40. No outcome/score-based choice anywhere.

Gold rows are the source rows verbatim (BY/QL from cases-reviewed.jsonl,
incl. review field; NL verbatim from cases.jsonl whose B grade is superseded
by GRADE-ADDENDUM for sealing purposes, exactly as holdout12 did).

Input cards follow holdout12-inputs/ format per source. DA charts are
extracted verbatim from liuren-duanan/scratch-archive/cases_raw.json;
BY charts are the data-corner visual transcription of the typeset PDF
pages (entered below as literals with page cites, cf. BUILD-LOG);
CY cards are ganzhi-level as in holdout12; QL-030's card subject/question
drop the post-hoc descriptor "中储蓄会头奖者" (card only, gold verbatim),
mirroring holdout12's QL-006 hygiene edit.

Outputs: benchmark/phase3/holdout13/test_gold.jsonl,
benchmark/phase3/holdout13-inputs/<id>.json, and a facts JSON next to
this script for SEALED.md / BUILD-LOG.md authoring. No git operations.
"""
import hashlib
import json
import re
from pathlib import Path

R35 = Path(__file__).resolve().parent
P3 = R35.parents[1]
EXP = P3 / "expansion12"


def load_jsonl(p):
    return [json.loads(l) for l in Path(p).read_text(encoding="utf-8").splitlines() if l.strip()]


# ---------- reserves ----------
da_all = load_jsonl(EXP / "liuren-duanan/cases-a.jsonl") + load_jsonl(EXP / "liuren-duanan/cases-b.jsonl")
da_elig = [r for r in da_all if r["holdout_eligible"]]
by_rev = load_jsonl(EXP / "liuren-bianyi-yuce/cases-reviewed.jsonl")
by_seal = [r for r in by_rev if r["review"]["verdict"] == "seal"]
cy_all = load_jsonl(EXP / "liuren-cuiyan/cases-munong.jsonl") + load_jsonl(EXP / "liuren-cuiyan/cases-juan5.jsonl")
cy_elig = [r for r in cy_all if r["holdout_eligible"]]
ql_rev = load_jsonl(EXP / "natal-batch2/cases-reviewed.jsonl")
ql_seal = [r for r in ql_rev if r["review"]["verdict"] == "seal"]
nl_all = load_jsonl(EXP / "natal-leftovers/cases.jsonl")
addendum = json.loads((EXP / "natal-leftovers/GRADE-ADDENDUM.json").read_text(encoding="utf-8"))
nl_sealable_ids = list(addendum["regraded_to_A_low"]) + ["NL-049"]
nl_sealable = [r for r in nl_all if r["id"] in nl_sealable_ids]
cz_all = load_jsonl(EXP / "online-routes/cases.jsonl")
hz_all = load_jsonl(EXP / "huangjince-huozhulin/cases.jsonl")

reserves = {
    "DA_eligible": len(da_elig), "DA_total": len(da_all),
    "BY_seal": len(by_seal), "BY_total": len(by_rev),
    "CY_eligible": len(cy_elig), "CY_total": len(cy_all),
    "QL_seal": len(ql_seal),
    "NL_sealable": len(nl_sealable),
    "CZ_total": len(cz_all), "HZ_total": len(hz_all),
}
assert reserves["DA_eligible"] == 162, reserves
assert reserves["BY_seal"] == 111, reserves
assert reserves["CY_eligible"] == 119, reserves
assert reserves["QL_seal"] == 18, reserves
assert reserves["NL_sealable"] == 7, reserves
assert reserves["CZ_total"] == 33 and reserves["HZ_total"] == 1, reserves

# ---------- exclusions ----------
used12 = [r["id"] for r in load_jsonl(P3 / "holdout12/test_gold.jsonl")]
used12_set = set(used12)
dev_ids = {p.stem for p in (P3 / "inputs-dev11").glob("*.json")}
assert len(dev_ids) == 487
prior_holdout_ids = set()
for gold in sorted(P3.glob("holdout*/test_gold.jsonl")):
    if "holdout13" in str(gold):
        continue
    prior_holdout_ids |= {r["id"] for r in load_jsonl(gold)}
pool_ids = set((EXP / "POOL-IDS.txt").read_text(encoding="utf-8").split())
excluded = used12_set | dev_ids | prior_holdout_ids | pool_ids

# ---------- selection (file order, skip excluded) ----------
def take(rows, k, label):
    picked = [r for r in rows if r["id"] not in excluded][:k]
    assert len(picked) == k, (label, [r["id"] for r in picked])
    return picked

picks = []  # (source_label, row)
for r in take(da_elig, 8, "DA"):
    picks.append(("DA", r))
for r in take(by_seal, 5, "BY"):
    picks.append(("BY", r))
for r in take(cy_elig, 3, "CY"):
    picks.append(("CY", r))
for r in take(ql_seal, 10, "QL"):
    picks.append(("QL", r))
for r in take(nl_sealable, 2, "NL"):
    picks.append(("NL", r))
for r in take(cz_all, 12, "CZ"):
    picks.append(("CZ", r))
assert len(picks) == 40
pick_ids = [r["id"] for _, r in picks]
assert len(set(pick_ids)) == 40
assert not (set(pick_ids) & excluded)

# ---------- four-item verification ----------
def triple(row):
    if "context" in row and isinstance(row.get("subject"), dict):
        c = row["context"]
        return (row["subject"].get("name_or_desc", ""), c.get("asked_at", ""), c.get("question", ""))
    return (str(row.get("subject", "")), str(row.get("asked_at", "")), str(row.get("question_or_topic", "")))

def norm(s):
    return re.sub(r"\s+", "", str(s))

checks = {}
for label, r in picks:
    cid = r["id"]
    issues = []
    # grade: A / A-low by governing record
    if label == "BY":
        grade = r["review"]["grade_final"]; contam = r["review"]["contamination_final"]
        if r["review"]["verdict"] != "seal":
            issues.append("verdict!=seal")
    elif label == "QL":
        grade = r["review"]["grade_final"]; contam = r["review"]["contamination_final"]
        if r["review"]["verdict"] != "seal":
            issues.append("verdict!=seal")
    elif label == "NL":
        grade = "A-low(addendum)" if cid in addendum["regraded_to_A_low"] else r["outcome_grade"]
        contam = r["contamination"]
    else:
        grade = r["outcome_grade"]; contam = r["contamination"]
    if not (grade.startswith("A")):
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
    checks[cid] = {"source": label, "grade_final": grade, "contamination_final": contam,
                   "issues": issues}
    assert not issues, (cid, issues)

# triple-key collisions: within picks, and vs holdout12 triples
triples = {r["id"]: tuple(norm(x) for x in triple(r)) for _, r in picks}
seen = {}
for cid, t in triples.items():
    assert t not in seen, (cid, seen.get(t))
    seen[t] = cid
h12_rows = load_jsonl(P3 / "holdout12/test_gold.jsonl")
h12_triples = {tuple(norm(x) for x in triple(r)) for r in h12_rows}
assert not (set(triples.values()) & h12_triples)

# ---------- liuyao bounded census ----------
allocated = dev_ids | prior_holdout_ids
liuyao_files = [
    "expansion3/cases.jsonl", "expansion4/cases.jsonl", "expansion5/cases.jsonl",
    "expansion7/bushi-quanshu/cases.jsonl", "expansion7/yiyin/cases.jsonl",
    "expansion7/yiyin2/cases.jsonl", "expansion8/duanyi-tianji/cases.jsonl",
    "expansion8/yimao/cases.jsonl", "expansion10/yilin-buyi/cases.jsonl",
    "expansion10/yilin-buyi-zongduan/cases.jsonl",
    "expansion11/bushi-zhengzong/cases.jsonl",
    "expansion12/huangjince-huozhulin/cases.jsonl",
]
census = {}
for rel in liuyao_files:
    p = P3 / rel
    if not p.exists():
        census[rel] = {"exists": False}
        continue
    rows = load_jsonl(p)
    ly = [r for r in rows if str(r.get("tradition")) in ("liuyao", "六爻", "筮占")]
    fresh = [r["id"] for r in ly
             if str(r.get("outcome_grade", "")).startswith("A")
             and r.get("contamination") == "low" and r["id"] not in allocated]
    census[rel] = {"rows": len(rows), "liuyao_rows": len(ly),
                   "ids": [r["id"] for r in ly], "fresh_A_low_unallocated": fresh}
census_fresh_total = sum(len(v.get("fresh_A_low_unallocated", [])) for v in census.values())

# ---------- gold ----------
gold_rows = [r for _, r in picks]
gold_path = P3 / "holdout13/test_gold.jsonl"
gold_path.parent.mkdir(parents=True, exist_ok=True)
gold_text = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in gold_rows)
gold_path.write_text(gold_text, encoding="utf-8")
gold_sha = hashlib.sha256(gold_path.read_bytes()).hexdigest()

# ---------- input cards ----------
inputs_dir = P3 / "holdout13-inputs"
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
            continue  # commentator continuation lines, not chart
        block.append(s)
    text = "\n".join(block)
    trans = re.findall(
        r"([父母兄子财官鬼孙])\s+([甲乙丙丁戊己庚辛壬癸]?[子丑寅卯辰巳午未申酉戌亥])\s+([" + GEN + r"])[◎⊙]*\s*$",
        text, flags=re.M)
    assert len(trans) == 3, (cid, trans, text)
    return text, "；".join(f"{a}{b}（{c}）" for a, b, c in trans)

BY_CHARTS = {
    "BY-002": {"课式": "前后引从",
               "三传": "财酉（太阴）、子辰（青龙）、官亥（贵人）",
               "四课": "天将 常蛇阴合／上 未子酉寅／下 子巳寅丁",
               "天地盘": "蛇朱合勾／子丑寅卯／贵亥 辰青／后戌 巳空／酉申未午／阴元常白"},
    "BY-003": {"课式": "首尾相见、旺禄临身、冬蛇掩目、魁度天门",
               "三传": "财戌（太阴）、禄卯（青龙）、子午（朱雀）",
               "四课": "天将 合朱空青／上 巳午寅卯／下 午未卯乙",
               "天地盘": "勾合朱蛇／辰巳午未／青卯 申贵／空寅 酉后／丑子亥戌／白常无阴"},
    "BY-004": {"课式": "六阳数足",
               "三传": "子午（螣蛇）、财辰（六合）、禄寅（青龙）",
               "四课": "天将 蛇后元白／上 午申戌子／下 申戌子甲",
               "天地盘": "勾合朱蛇／卯辰巳午／青寅 未贵／空丑 申后／子亥戌酉／白常元阴"},
    "BY-005": {"课式": "六阴相继、前孤后寡、二贵皆空",
               "三传": "官亥（贵人）、财酉（太阴）、子未（太常）",
               "四课": "天将 贵朱勾空／上 亥丑卯巳／下 丑卯巳丁",
               "天地盘": "勾青空白／卯辰巳午／合寅 未常／朱丑 申元／子亥戌酉／蛇贵后阴"},
    "BY-006": {"课式": "旺禄临身、魁度天门、虎视逢虎",
               "三传": "兄戌（太阴）、父午（天空）、子申（太常）",
               "四课": "天将 白常青空／上 未申巳午／下 申酉午己",
               "天地盘": "勾青空白／辰巳午未／合卯 申常／朱寅 酉元／丑子亥戌／蛇贵后阴"},
}

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
    elif label in ("QL", "NL"):
        if label == "QL":
            pillars, gender = r["chart"]["pillars"], r["chart"].get("gender")
            subj, ques = r["subject"], r["question_or_topic"]
            note = "四柱/性别自源行 chart 字段入 attachments；context 原文为空未填"
            if cid == "QL-030":
                subj = subj.replace("（中储蓄会头奖者，佚名）", "（佚名）")
                ques = ques.replace("某女（中储蓄会头奖者，佚名）", "某女（佚名）")
                note += "；subject/question 中后事身份词「中储蓄会头奖者」已删（照 holdout12 QL-006 卡卫生先例，金标不动）"
        else:
            m = re.search(r"四柱（([^）]+)）", r["question_or_topic"])
            pillars = m.group(1)
            gender = "男" if ("之弟" in r["subject"] or "长孙" in r["subject"]) else None
            subj, ques = r["subject"], r["question_or_topic"]
            note = "四柱自 question_or_topic 括注提取入 attachments；性别据 subject 明示（弟/长孙）记男"
        att = {"四柱": pillars}
        if gender:
            att["性别"] = gender
        card = {"id": cid, "subject": {"name_or_desc": subj},
                "context": {"question": ques, "asked_at": r["asked_at"],
                            "setting": r["context_at_prediction"], "attachments": att},
                "provenance": prov_flat(r), "language": r["provenance"]["language"]}
        card_notes[cid] = note + "；源行 grade_note/review 未入卡"
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
        card_notes[cid] = "课式/三传/四课/天地盘自原书排印本 PDF 页图直录（数据角视觉转录，2026-10-30）；排印本玄武省作「元」、三传天将按全称记、四课与天地盘天将行照原字；grade_note/review 未入卡"
    elif label == "CY":
        card = {"id": cid, "subject": {"name_or_desc": r["subject"]},
                "context": {"question": r["question_or_topic"], "asked_at": r["asked_at"],
                            "setting": r["context_at_prediction"],
                            "attachments": {"干支占时": r["asked_at"],
                                            "note": "原书页图有课盘列（liuren-cuiyan/render/cy-p-153.png），转录底稿 TRANSCRIPTION-NOTES.md 未录盘字、页图盘字漫漶，本卡不臆录，仅录干支/月将/占时"}},
                "provenance": prov_flat(r), "language": r["provenance"]["language"]}
        card_notes[cid] = "仅干支级建卡（原书有课盘列但转录未录盘字，不臆录）；grade_note 未入卡"
    blob = json.dumps(card, ensure_ascii=False)
    for bad in ("grade_note", "master_predictions", "method_hint", '"outcome"', '"review"', "contamination"):
        assert bad not in blob, (cid, bad)
    (inputs_dir / f"{cid}.json").write_text(
        json.dumps(card, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

facts = {
    "reserves": reserves,
    "used12": used12,
    "pick_ids": pick_ids,
    "picks_by_source": {lab: [r["id"] for l2, r in picks if l2 == lab]
                        for lab in ("DA", "BY", "CY", "QL", "NL", "CZ")},
    "checks": checks,
    "triples": {k: list(v) for k, v in triples.items()},
    "liuyao_census": census,
    "liuyao_fresh_total": census_fresh_total,
    "gold_sha256": gold_sha,
    "card_notes": card_notes,
    "prior_holdout_ids_count": len(prior_holdout_ids),
}
(R35 / "build_holdout13_facts_r35.json").write_text(
    json.dumps(facts, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps({"reserves": reserves, "picks": facts["picks_by_source"],
                  "gold_sha256": gold_sha, "liuyao_fresh_total": census_fresh_total},
                 ensure_ascii=False, indent=1))
print("cards written:", len(list(inputs_dir.glob('*.json'))))
