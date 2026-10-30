#!/usr/bin/env python3
"""R37 CENSUS-SUPPLY-15 普查脚本（数据角，元数据/成色层清点 only）。

- 排除集 = inputs-dev11 文件名集 (dev9 487) ∪ holdout3..holdout14 test_gold.jsonl 的 id 字段
  ∪ expansion12/POOL-IDS.txt。
- 对 holdout 金标只取 id 字段，不取任何结局文本作挑选依据。
- 对候选 cases 文件只读元数据字段：id/tradition/source_work/outcome_grade/contamination/
  holdout_eligible/review(verdict,grade_final,contamination_final)/question_or_topic，
  以及 ④ 双全的布尔在场检查（master_predictions 首条 statement_excerpt 非空、outcome.description 非空），
  不输出、不依据结局文本内容做任何挑选。
- 输出：census-supply15-r37.json（同目录）。
"""
import json, os, re
from collections import Counter, defaultdict

BASE = os.path.expanduser("~/workspace/divination/benchmark/phase3")
OUT = os.path.join(BASE, "runs/round37/data-verify/census-supply15-r37.json")

def load_ids_from_gold(path):
    ids = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            ids.append(d.get("id"))
    return ids

# ---------- 排除集 ----------
dev9 = sorted(fn[:-5] for fn in os.listdir(os.path.join(BASE, "inputs-dev11")) if fn.endswith(".json"))
holdout_used = {}
for n in range(3, 15):
    p = os.path.join(BASE, f"holdout{n}", "test_gold.jsonl")
    holdout_used[f"holdout{n}"] = load_ids_from_gold(p)
pool_ids = []
with open(os.path.join(BASE, "expansion12/POOL-IDS.txt")) as f:
    for line in f:
        line = line.strip()
        if line:
            pool_ids.append(line)
excluded = set(dev9) | {i for v in holdout_used.values() for i in v} | set(pool_ids)

result = {
    "exclusion": {
        "dev9_inputs_dev11_count": len(dev9),
        "holdout_counts": {k: len(v) for k, v in holdout_used.items()},
        "holdout_total_rows": sum(len(v) for v in holdout_used.values()),
        "pool_ids_lines": len(pool_ids),
        "pool_ids_unique": len(set(pool_ids)),
        "excluded_union_unique": len(excluded),
    }
}

def has_dual(d):
    """④ 双全布尔在场检查（不读内容作挑选）。"""
    mp = d.get("master_predictions") or []
    stmt_ok = False
    if mp and isinstance(mp, list) and isinstance(mp[0], dict):
        stmt_ok = bool(str(mp[0].get("statement_excerpt") or "").strip())
    oc = d.get("outcome") or {}
    desc_ok = bool(str(oc.get("description") or "").strip()) if isinstance(oc, dict) else bool(oc)
    return stmt_ok and desc_ok

TOPIC_RULES = [  # 按优先级序命中（题材关键词近似分层，口径见 CENSUS-SUPPLY-15 §方法注记）
    ("射覆", ["射覆", "请射"]),
    ("天时岁候/农事", ["晴", "雨", "雪", "天时", "岁候", "应候", "日有大晕", "田蚕", "蚕", "禾"]),
    ("兵事/城池地方安危", ["兵", "城池", "城守", "攻扬", "攻城", "援兵", "贼何日退", "地方安否", "地方安危", "城安危", "城中", "闻警", "开城", "安否（袁州城", "地方安否（西乡县"]),
    ("孕产子息", ["六甲", "孕", "胎", "产妇", "生产", "子息", "过房"]),
    ("疾病", ["病", "疾", "医药", "求医", "臂偶肿"]),
    ("婚姻", ["婚", "嫁娶", "续娶"]),
    ("公讼/劾案", ["讼", "狱", "劾", "逮问", "因案", "官司", "控告", "诬告", "投书"]),
    ("盗贼捕亡/失物逃亡", ["盗", "捕亡", "捕盗", "失物", "失书籍", "失马", "失羊", "失狗", "失钱", "失婢", "失金", "失度", "失银", "失麦", "逃亡", "逃何方", "寻觅", "被掳", "追之", "携子而逃"]),
    ("求财/借贷经商", ["财", "财产", "店业", "营生", "养息", "交易", "买卖", "竞标", "银", "借贷", "借银", "讨银", "贸易", "经商", "行商", "合伙运货", "买皮纸", "卖卜"]),
    ("仕宦功名/考试/前程运程", ["仕", "官", "功名", "前程", "终身", "平生", "身位", "试", "升", "任", "缺", "馆", "入相", "封印", "状元", "谋事", "谋动", "年运", "年将", "运程", "向后如何", "一年事", "年内事", "得第", "中式", "引见", "上任", "到任", "差事", "差遣", "设砚", "受聘", "京信", "升迁消息"]),
    ("行人/出行行止/音信", ["行人", "行程", "行止", "进退", "去就", "去留", "归程", "音信", "寄信", "寄寓", "家报", "何日有信", "信可到", "信能通", "来否", "到否", "可到", "访人", "访友", "得见否", "所候", "来人", "候之人", "搭船", "有船", "水道", "登舟", "出门", "往兴安", "往株树潭", "往下埠", "往芦溪", "游江南", "回省", "尚可居否", "行踪"]),
    ("宅墓/迁居营建", ["宅", "墓", "葬地", "择地", "迁居", "起房", "起屋", "建房", "住否", "可久住", "堤工", "淤沙", "疏浚"]),
    ("杂占其他", []),
]
def topic_bucket(q):
    q = q or ""
    for name, kws in TOPIC_RULES[:-1]:
        for kw in kws:
            if kw in q:
                return name
    return "射覆/杂占其他"

def summarize(rows, eligible_fn, grade_fn, contam_fn):
    tot = len(rows)
    elig = [r for r in rows if eligible_fn(r)]
    fresh = [r for r in elig if r["id"] not in excluded]
    dual_fail = [r["id"] for r in fresh if not has_dual(r)]
    sealable = [r for r in fresh if has_dual(r)]
    return {
        "file_rows": tot,
        "eligible_total": len(elig),
        "eligible_minus_excluded": len(fresh),
        "excluded_among_eligible": sorted(r["id"] for r in elig if r["id"] in excluded),
        "dual_fail_ids": dual_fail,
        "sealable": len(sealable),
        "sealable_ids": [r["id"] for r in sealable],
        "sealable_grade_dist": dict(Counter(grade_fn(r) for r in sealable)),
        "sealable_contam_dist": dict(Counter(contam_fn(r) for r in sealable)),
        "sealable_topic_dist": dict(Counter(topic_bucket(r.get("question_or_topic") or r.get("question") or "") for r in sealable)),
    }

def read_jsonl(rel):
    rows = []
    with open(os.path.join(BASE, rel)) as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows

sources = {}

# DA 断案
da_rows = read_jsonl("expansion12/liuren-duanan/cases-a.jsonl") + read_jsonl("expansion12/liuren-duanan/cases-b.jsonl")
sources["DA_liuren_duanan"] = summarize(
    da_rows,
    lambda r: r.get("holdout_eligible") is True,
    lambda r: r.get("outcome_grade"), lambda r: r.get("contamination"))
sources["DA_liuren_duanan"]["grade_dist_all"] = dict(Counter(r.get("outcome_grade") for r in da_rows))
sources["DA_liuren_duanan"]["eligible_false_count"] = sum(1 for r in da_rows if r.get("holdout_eligible") is not True)

# BY/YX 辨疑+预测学（以 review 为准）
by_rows = read_jsonl("expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl")
def by_elig(r):
    rv = r.get("review") or {}
    return rv.get("verdict") == "seal"
def by_grade(r):
    return (r.get("review") or {}).get("grade_final")
def by_contam(r):
    return (r.get("review") or {}).get("contamination_final")
for prefix in ("BY", "YX"):
    sub = [r for r in by_rows if str(r.get("id", "")).startswith(prefix + "-")]
    sources[f"{prefix}_bianyi_yuce"] = summarize(sub, by_elig, by_grade, by_contam)
sources["BY_YX_review_dist"] = dict(Counter((r.get("review") or {}).get("verdict") for r in by_rows))

# CY 粹言慕农 + CYJ 卷五
for key, rel in [("CY_cuiyan_munong", "expansion12/liuren-cuiyan/cases-munong.jsonl"),
                 ("CYJ_cuiyan_juan5", "expansion12/liuren-cuiyan/cases-juan5.jsonl")]:
    rows = read_jsonl(rel)
    sources[key] = summarize(rows, lambda r: r.get("holdout_eligible") is True,
                             lambda r: r.get("outcome_grade"), lambda r: r.get("contamination"))

# CZ 测字秘牒（资格据 HOST-RULINGS-3：33 例全合格；源文件 holdout_eligible=false 为抽例时点状态）
cz_rows = read_jsonl("expansion12/online-routes/cases.jsonl")
sources["CZ_cezi_mibitie"] = summarize(
    cz_rows,
    lambda r: str(r.get("outcome_grade", "")).startswith("A") and r.get("contamination") == "low",
    lambda r: r.get("outcome_grade"), lambda r: r.get("contamination"))

# BQ 备选建档 + BQ 原批
bq_new = read_jsonl("expansion12/bushi-quanshu-beixuan/cases.jsonl")
sources["BQ_beixuan"] = summarize(bq_new, lambda r: r.get("holdout_eligible") is True,
                                  lambda r: r.get("outcome_grade"), lambda r: r.get("contamination"))
bq_old = read_jsonl("expansion7/bushi-quanshu/cases.jsonl")
sources["BQ_bushi_quanshu_orig"] = summarize(
    bq_old,
    lambda r: str(r.get("outcome_grade", "")).startswith("A") and r.get("contamination") == "low",
    lambda r: r.get("outcome_grade"), lambda r: r.get("contamination"))

# HZ 火珠林
hz_rows = read_jsonl("expansion12/huangjince-huozhulin/cases.jsonl")
sources["HZ_huozhulin"] = summarize(hz_rows, lambda r: r.get("holdout_eligible") is True,
                                    lambda r: r.get("outcome_grade"), lambda r: r.get("contamination"))

# NL + natal-batch2
nl_rows = read_jsonl("expansion12/natal-leftovers/cases.jsonl")
with open(os.path.join(BASE, "expansion12/natal-leftovers/GRADE-ADDENDUM.json")) as f:
    addendum = json.load(f)
sources["NL_raw_grade_dist"] = dict(Counter(r.get("outcome_grade") for r in nl_rows))
sources["NL_addendum_type"] = type(addendum).__name__
sources["NL_addendum_preview_keys"] = (list(addendum.keys())[:20] if isinstance(addendum, dict) else [str(x)[:80] for x in addendum[:5]] if isinstance(addendum, list) else str(addendum)[:200])
nb2_rows = read_jsonl("expansion12/natal-batch2/cases-reviewed.jsonl")
def nb2_elig(r):
    return (r.get("review") or {}).get("verdict") == "seal"
sources["NB2_qianli_yuanshi"] = summarize(nb2_rows, nb2_elig,
                                         lambda r: (r.get("review") or {}).get("grade_final"),
                                         lambda r: (r.get("review") or {}).get("contamination_final"))
# NB2 A 级 high 储备（不可封存，仅登记）
a_high = [r for r in nb2_rows if str((r.get("review") or {}).get("grade_final", "")).startswith("A")
          and (r.get("review") or {}).get("contamination_final") == "high" and r["id"] not in excluded]
sources["NB2_A_high_not_sealable_count"] = len(a_high)
sources["NB2_A_high_not_sealable_ids"] = [r["id"] for r in a_high]

result["sources"] = sources

# ---------- 全 expansions 扫描：任何 A/A-low + low + 未入排除集的残余（不限 expansion12） ----------
scan_files = []
for root, dirs, files in os.walk(BASE):
    rel_root = os.path.relpath(root, BASE)
    parts = rel_root.split(os.sep)
    if not parts[0].startswith("expansion"):
        continue
    if rel_root.startswith("expansion12"):
        continue  # 已逐源计入上表，避免双计
    for fn in files:
        if fn.endswith(".jsonl") and ("cases" in fn or "answers" in fn):
            scan_files.append(os.path.join(rel_root, fn))
scan_hits = []
scan_file_stats = {}
for rel in sorted(scan_files):
    try:
        rows = read_jsonl(rel)
    except Exception as e:
        scan_file_stats[rel] = f"ERR {e}"
        continue
    n_a_low_fresh = 0
    for r in rows:
        rid = r.get("id")
        if not rid:
            continue
        grade = r.get("outcome_grade") or (r.get("review") or {}).get("grade_final") or ""
        contam = r.get("contamination") or (r.get("review") or {}).get("contamination_final") or ""
        if str(grade).startswith("A") and contam == "low" and rid not in excluded:
            n_a_low_fresh += 1
            scan_hits.append({"file": rel, "id": rid, "tradition": r.get("tradition"),
                              "grade": grade, "contamination": contam,
                              "holdout_eligible": r.get("holdout_eligible")})
    scan_file_stats[rel] = {"rows": len(rows), "A_low_fresh_hits": n_a_low_fresh}
result["expansion_scan_outside_exp12"] = {"files": scan_file_stats, "hits": scan_hits}

with open(OUT, "w") as f:
    json.dump(result, f, ensure_ascii=False, indent=1)
print(json.dumps(result["exclusion"], ensure_ascii=False))
for k, v in sources.items():
    if isinstance(v, dict) and "sealable" in v:
        print(k, "rows", v["file_rows"], "elig", v["eligible_total"], "fresh", v["eligible_minus_excluded"],
              "sealable", v["sealable"], "dual_fail", v["dual_fail_ids"],
              "grades", v["sealable_grade_dist"], "contam", v["sealable_contam_dist"])
    else:
        print(k, "=", v)
print("scan hits outside exp12:", len(scan_hits))
for h in scan_hits:
    print(" HIT", h)
