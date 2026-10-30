#!/usr/bin/env python3
# R40 data-corner supply verification. Explicit paths only; no glob/rglob/listdir.
# Gold files: only the "id" field of each line is read (id-list use, gold content not read).
import json, re, sys
BASE = "/home/hatch/workspace/divination/benchmark/phase3/"

def load_jsonl(rel):
    rows = []
    with open(BASE + rel, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows

def gold_ids(rel):
    ids = []
    with open(BASE + rel, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                ids.append(json.loads(line)["id"])
    return ids

GOLD_FILES = {
    "holdout3": "holdout3/test_gold.jsonl",
    "holdout4": "holdout4/test_gold.jsonl",
    "holdout5": "holdout5/test_gold.jsonl",
    "holdout6": "holdout6/test_gold.jsonl",
    "holdout7": "holdout7/test_gold.jsonl",
    "holdout8": "holdout8/test_gold.jsonl",
    "holdout9": "holdout9/test_gold.jsonl",
    "holdout10": "holdout10/test_gold.jsonl",
    "holdout11": "holdout11/test_gold.jsonl",
    "holdout12": "holdout12/test_gold.jsonl",
    "holdout13": "holdout13/test_gold.jsonl",
    "holdout14": "holdout14/test_gold.jsonl",
    "holdout15": "holdout15/test_gold.jsonl",
}
used = {}
for k, v in GOLD_FILES.items():
    used[k] = gold_ids(v)
used_all = set()
for v in used.values():
    used_all.update(v)
used_12_15 = set()
for k in ("holdout12", "holdout13", "holdout14", "holdout15"):
    used_12_15.update(used[k])

out = {}
out["used_counts"] = {k: len(v) for k, v in used.items()}
out["used_all_unique"] = len(used_all)

# ---------- 1. Zichu ----------
zc38 = load_jsonl("runs/round38/data-verify/zichu-cases-r38.jsonl")
zc39 = load_jsonl("runs/round39/data-verify/zichu-j3-cases-r39.jsonl")
def dist(rows, field):
    d = {}
    for r in rows:
        d[str(r.get(field))] = d.get(str(r.get(field)), 0) + 1
    return d
zc_all = zc38 + zc39
zc_eligible = [r for r in zc_all if r.get("holdout_eligible") is True]
zc_alow_strict = [r for r in zc_all if r.get("outcome_grade") == "A" and r.get("contamination") == "low" and r.get("holdout_eligible") is True]
zc_used_in_12_15 = sorted([r["id"] for r in zc_eligible if r["id"] in used_12_15])
zc_avail = sorted([r["id"] for r in zc_eligible if r["id"] not in used_12_15])
zc122 = [r for r in zc39 if r["id"] == "ZC-122"]
out["zichu"] = {
    "r38_rows": len(zc38), "r39_rows": len(zc39),
    "grade_dist_all": dist(zc_all, "outcome_grade"),
    "contam_dist_all": dist(zc_all, "contamination"),
    "eligible_true": len(zc_eligible),
    "eligible_ids": sorted(r["id"] for r in zc_eligible),
    "alow_strict_count": len(zc_alow_strict),
    "eligible_but_not_alow_strict": sorted(r["id"] for r in zc_eligible if r not in zc_alow_strict),
    "eligible_used_in_h12_15": zc_used_in_12_15,
    "eligible_unused_h12_15": zc_avail,
    "avail_excl_ZC122": [i for i in zc_avail if i != "ZC-122"],
    "avail_overlap_h3_15": sorted([i for i in zc_avail if i in used_all]),
    "zc122_row": [{k: zc122[0].get(k) for k in ("id", "outcome_grade", "contamination", "holdout_eligible", "grade_note")} if zc122 else {}],
}

# ---------- 2. Bianyi ----------
by = load_jsonl("runs/round38/data-verify/bianyi-stock-r38.jsonl")
by_seal = [r for r in by if r.get("seal_eligible") is True]
by_seal_ids = sorted(r["id"] for r in by_seal if r.get("id"))
by_used15 = sorted([i for i in by_seal_ids if i in set(used["holdout15"])])
by_avail = sorted([i for i in by_seal_ids if i not in set(used["holdout15"])])
out["bianyi"] = {
    "rows": len(by),
    "id_null_rows": sum(1 for r in by if not r.get("id")),
    "seal_true": len(by_seal),
    "grade_dist": dist(by, "outcome_grade"), "contam_dist": dist(by, "contamination"),
    "seal_grade_dist": dist(by_seal, "outcome_grade"), "seal_contam_dist": dist(by_seal, "contamination"),
    "used_in_h15": by_used15, "avail_after_h15": len(by_avail), "avail_ids": by_avail,
    "avail_overlap_h3_14": sorted([i for i in by_avail if i in used_all and i not in set(used["holdout15"])]),
}

# ---------- 3. Yuce ----------
yu = load_jsonl("runs/round38/data-verify/yuce-stock-r38.jsonl")
err = load_jsonl("runs/round39/data-verify/yuce-stock-errata-r39.jsonl")
yu_withid = [r for r in yu if r.get("id")]
yu_seal = [r for r in yu if r.get("seal_eligible") is True]
err_ids = sorted(r["applies_to_row_id"] for r in err)
yu_seal_ids = sorted(r["id"] for r in yu_seal)
yu_used15 = sorted([i for i in yu_seal_ids if i in set(used["holdout15"])])
yu_compliant = sorted([i for i in yu_seal_ids if i not in set(used["holdout15"]) and i not in err_ids])
yu_detail = {}
for i in ("YXS-015", "YXS-017", "YXS-018", "YXS-019"):
    row = [r for r in yu if r.get("id") == i]
    if row:
        r = row[0]
        yu_detail[i] = {k: r.get(k) for k in ("id", "outcome_grade", "contamination", "seal_eligible", "chart_complete", "disposition", "source_ref", "subject")}
out["yuce"] = {
    "rows_total": len(yu), "rows_with_id": len(yu_withid), "rows_id_null": len(yu) - len(yu_withid),
    "null_id_dispositions": dist([r for r in yu if not r.get("id")], "disposition"),
    "null_id_seal": dist([r for r in yu if not r.get("id")], "seal_eligible"),
    "seal_true": len(yu_seal), "seal_ids": yu_seal_ids,
    "errata_rows": len(err), "errata_ids": err_ids,
    "errata_corrected_seal": [r["correction"]["corrected_seal_eligible"] for r in err],
    "used_in_h15_among_seal": yu_used15,
    "compliant_unused": yu_compliant,
    "detail": yu_detail,
    "seal_grade_dist": dist(yu_seal, "outcome_grade"), "seal_contam_dist": dist(yu_seal, "contamination"),
}

# ---------- 4. Duanan ----------
da_a = load_jsonl("expansion12/liuren-duanan/cases-a.jsonl")
da_b = load_jsonl("expansion12/liuren-duanan/cases-b.jsonl")
da = da_a + da_b
da_ids = [r["id"] for r in da]
da_elig = [r for r in da if r.get("holdout_eligible") is True]
da_alow_low = [r for r in da if r.get("outcome_grade") == "A-low" and r.get("contamination") == "low"]
da_overlap = {}
for k, v in used.items():
    ov = sorted(set(da_ids) & set(v))
    if ov:
        da_overlap[k] = ov
da_overlap_all = sorted(set(da_ids) & used_all)
da_avail_ids = sorted([i for i in da_ids if i not in used_all])
da_elig_avail = sorted([r["id"] for r in da_elig if r["id"] not in used_all])
# identity check: overlapping gold rows vs stock rows (full dict compare)
stock_by_id = {r["id"]: r for r in da}
identical, differ = [], []
for k in ("holdout12", "holdout13", "holdout14"):
    for line_id in used[k]:
        if line_id in stock_by_id:
            pass
# full compare needs gold rows; re-read only overlapping rows fully for identity check (data-corner stock identity, not scoring)
def gold_rows(rel):
    return load_jsonl(rel)
ident_count = 0; diff_ids = []
for k in ("holdout12", "holdout13", "holdout14", "holdout15"):
    for r in gold_rows(GOLD_FILES[k]):
        if r["id"] in stock_by_id:
            if json.dumps(r, sort_keys=True, ensure_ascii=False) == json.dumps(stock_by_id[r["id"]], sort_keys=True, ensure_ascii=False):
                ident_count += 1
            else:
                diff_ids.append(r["id"])
# POOL-IDS
with open(BASE + "expansion12/POOL-IDS.txt", encoding="utf-8") as f:
    pool_ids = [l.strip() for l in f if l.strip()]
pool_set = set(pool_ids)
# cases_raw / meta chart completeness
with open(BASE + "expansion12/liuren-duanan/scratch-archive/cases_raw.json", encoding="utf-8") as f:
    raw = json.load(f)
with open(BASE + "expansion12/liuren-duanan/scratch-archive/meta.json", encoding="utf-8") as f:
    meta = json.load(f)
raw_by_n = {e["n"]: e["raw"] for e in raw}
meta_by_n = {e["n"]: e for e in meta}
TJ = "贵蛇雀合勾龙空虎常玄阴后"
def chart_class(text):
    t = re.sub(r"\s+", "", text)
    kin = re.findall(r"(?:父|母|兄|弟|子|孙|财|官|鬼|妻)[\u4e00-\u9fff]{2}[贵蛇雀合勾龙空虎常玄阴后]", t)
    footer = ("后阴玄常" in t) or ("朱蛇贵后" in t) or ("后陰玄常" in t)
    grid = sum(1 for c in set(TJ) if c in t)
    if footer and len(kin) >= 3:
        return "complete"
    if footer or len(kin) >= 1:
        return "partial"
    return "none"
chart_counts = {}
for r in da:
    n = int(r["id"].split("-")[1])
    c = chart_class(raw_by_n.get(n, ""))
    chart_counts[c] = chart_counts.get(c, 0) + 1
# triple uniqueness within DA
triples = {}
dup_triples = []
for r in da:
    key = (str(r.get("subject")).strip(), str(r.get("asked_at")).strip(), str(r.get("question_or_topic")).strip())
    if key in triples:
        dup_triples.append((triples[key], r["id"]))
    triples[key] = r["id"]
# sample 10: deterministic spaced indices
sample_idx_a = [0, 18, 36, 54, 72]
sample_idx_b = [0, 15, 30, 45, 60]
sample = [da_a[i] for i in sample_idx_a] + [da_b[i] for i in sample_idx_b]
sample_detail = []
for r in sample:
    n = int(r["id"].split("-")[1])
    rawt = raw_by_n.get(n, "")
    metat = meta_by_n.get(n, {})
    subj_core = str(r.get("subject")).split("（")[0].split("(")[0]
    sample_detail.append({
        "id": r["id"], "subject": r.get("subject"), "asked_at": r.get("asked_at"),
        "question": r.get("question_or_topic"),
        "grade": r.get("outcome_grade"), "contamination": r.get("contamination"),
        "eligible": r.get("holdout_eligible"),
        "stock_row_has_chart_field": any(k for k in r.keys() if "chart" in k.lower()),
        "raw_chart_class": chart_class(rawt),
        "meta_title": metat.get("title"),
        "subject_core_in_raw_or_meta": (subj_core in rawt) or (subj_core in str(metat.get("title", ""))),
        "asked_head_in_raw": str(r.get("asked_at"))[:6] in re.sub(r"\s+", "", rawt) or str(r.get("asked_at"))[:6] in str(metat.get("asked_raw", "")),
        "used_in_holdout": r["id"] in used_all,
    })
out["duanan"] = {
    "a_rows": len(da_a), "b_rows": len(da_b), "total": len(da),
    "id_unique": len(set(da_ids)), "id_dupes": len(da_ids) - len(set(da_ids)),
    "grade_dist": dist(da, "outcome_grade"), "contam_dist": dist(da, "contamination"),
    "eligible_dist": dist(da, "holdout_eligible"),
    "a_grade_dist": dist(da_a, "outcome_grade"), "a_contam_dist": dist(da_a, "contamination"), "a_elig": dist(da_a, "holdout_eligible"),
    "b_grade_dist": dist(da_b, "outcome_grade"), "b_contam_dist": dist(da_b, "contamination"), "b_elig": dist(da_b, "holdout_eligible"),
    "alow_low_count": len(da_alow_low),
    "eligible_true_count": len(da_elig),
    "ineligible_ids": sorted(r["id"] for r in da if r.get("holdout_eligible") is not True),
    "overlap_by_holdout": da_overlap, "overlap_all_ids": da_overlap_all, "overlap_all_count": len(da_overlap_all),
    "unused_ids": da_avail_ids, "unused_count": len(da_avail_ids),
    "eligible_and_unused_ids": da_elig_avail, "eligible_and_unused_count": len(da_elig_avail),
    "gold_row_identical_to_stock": ident_count, "gold_row_differ_ids": diff_ids,
    "pool_total": len(pool_ids), "pool_unique": len(pool_set),
    "pool_contains_da": sorted([i for i in da_ids if i in pool_set]),
    "pool_contains_any_da_prefix": sum(1 for i in pool_ids if i.startswith("DA-")),
    "raw_entries": len(raw), "meta_entries": len(meta),
    "chart_class_all_da": chart_counts,
    "dup_triples_within_da": dup_triples,
    "sample10": sample_detail,
}

# ---------- 5. Cuiyan ----------
cy_m = load_jsonl("expansion12/liuren-cuiyan/cases-munong.jsonl")
cy_j = load_jsonl("expansion12/liuren-cuiyan/cases-juan5.jsonl")
def cy_block(rows, name):
    ids = [r["id"] for r in rows]
    return {
        "file": name, "rows": len(rows), "id_unique": len(set(ids)),
        "grade_dist": dist(rows, "outcome_grade"), "contam_dist": dist(rows, "contamination"),
        "eligible_dist": dist(rows, "holdout_eligible"),
        "eligible_ids": sorted(r["id"] for r in rows if r.get("holdout_eligible") is True),
        "ineligible_ids": sorted(r["id"] for r in rows if r.get("holdout_eligible") is not True),
        "overlap_h3_15": sorted(set(ids) & used_all),
        "eligible_unused_ids": sorted(r["id"] for r in rows if r.get("holdout_eligible") is True and r["id"] not in used_all),
    }
out["cuiyan"] = {"munong": cy_block(cy_m, "cases-munong.jsonl"), "juan5": cy_block(cy_j, "cases-juan5.jsonl")}

print(json.dumps(out, ensure_ascii=False, indent=1))
