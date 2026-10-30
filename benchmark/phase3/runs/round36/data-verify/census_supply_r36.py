#!/usr/bin/env python3
"""R36 data-verify census script (unique name, round36/data-verify only).

Discipline:
- Reads ONLY explicitly listed files (no rglob / full-tree scans).
- Holdout allocation is checked by id field ONLY (test_gold.jsonl id values;
  dev9 membership by inputs-dev11 filename stems). No outcome content is
  used for any judgement in Part B; Part A reads its own source case files
  (cases.jsonl / cases-reviewed.jsonl) which are extraction archives, not
  holdout gold.
- Writes supply-bz-r36.json and census-ly-r36.json next to this script.
"""
import json
import collections
import pathlib

ROOT = pathlib.Path.home() / "workspace/divination"
P3 = ROOT / "benchmark/phase3"
OUT = P3 / "runs/round36/data-verify"


def read_jsonl(path):
    return [json.loads(l) for l in path.read_text().splitlines() if l.strip()]


def ids_of_gold(holdout_name):
    p = P3 / holdout_name / "test_gold.jsonl"
    if not p.exists():
        return set()
    return {json.loads(l)["id"] for l in p.read_text().splitlines() if l.strip()}


HOLDOUT_IDS = {}
for n in range(3, 14):
    HOLDOUT_IDS[f"holdout{n}"] = ids_of_gold(f"holdout{n}")
ALL_HOLDOUT_USED = set().union(*HOLDOUT_IDS.values()) if HOLDOUT_IDS else set()
DEV9_IDS = {p.stem for p in (P3 / "inputs-dev11").glob("*.json")}
POOL_IDS = {l.strip() for l in (P3 / "expansion12/POOL-IDS.txt").read_text().splitlines() if l.strip()}

# ---------------------------------------------------------------- Part A (BZ)
nb2 = P3 / "expansion12/natal-batch2"
rev = read_jsonl(nb2 / "cases-reviewed.jsonl")
orig = {r["id"]: r for r in read_jsonl(nb2 / "cases.jsonl")}
assert len(rev) == 92 and set(orig) == {r["id"] for r in rev}

seal = [r for r in rev if r["review"]["verdict"] == "seal"]
nonseal = [r for r in rev if r["review"]["verdict"] != "seal"]
verdict_counts = collections.Counter(r["review"]["verdict"] for r in rev)
cross = collections.Counter(
    (r["review"]["grade_final"], r["review"]["contamination_final"]) for r in nonseal
)

# Authored re-review decisions (data seat, R36): each B-grade case was checked
# against cases.jsonl original record (statement_excerpt = source transcription,
# provenance page in the original book). A-low axis follows expansion12 PREREG
# A definition + NL REGRADE-REVIEW precedent (book-internal separable specific
# event suffices; no external corroboration requirement; retrospective
# life-explanation does NOT qualify).
REGRADE = {
    "PU-003": {"decision": "regrade_A-low_grade_only", "sealable": False,
               "reason": "REVIEW-H 以附加的『独立客观史实』要件降 B，与 expansion12 预注册 A 定义（原文明确记载与断语可分离的具体事件记录即可）及 NL REGRADE 先例相悖；本例略历载二十六岁拜江州令、三诏不就、六十三岁炼丹等具体事件，与谨按断语分载可分离，分级轴改判 A-low（传说性质照原 grade_note 注记）。contamination=high 不变，仍不可封存。"},
    "PU-008": {"decision": "regrade_A-low_grade_only", "sealable": False,
               "reason": "同 PU-003：略历载两举进士不第、遇钟离权授道等具体事件，与断语分载可分离，分级轴改判 A-low（实存性属传说系统，照原注记）。contamination=high 不变，仍不可封存。"},
    "QL-009": {"decision": "keep_B", "category": "回顾性地位总评",
               "reason": "钱翁生平（出身豪富、晚年耗顿、寄食侄门）先行叙述，断语为对已知生平的回解，结局与断语同段交织、无断后应验另载。"},
    "QL-010": {"decision": "keep_B", "category": "回顾性叙事",
               "reason": "为娼、被黜、伶人断交等皆生平回顾，与断语同段交织，无事前求测与断后应验结构。"},
    "QL-011": {"decision": "keep_B", "category": "回顾性叙事",
               "reason": "庸役三代为生平前提；『三十年积蓄二千余金』以『据云』嵌于断语同段，非独立应验记载。"},
    "QL-012": {"decision": "keep_B", "category": "幼年事实回顾（转述）",
               "reason": "可分离事实仅三岁丧亲、七岁入寺等幼年回顾（孙福堂转述）；断后生涯（甲子乙丑运）为前瞻，书内无应验。"},
    "QL-015": {"decision": "keep_B", "category": "事件嵌运释同段回顾",
               "reason": "夫病几危、自身遇盗嵌于戊戌运释同段叙述，无独立应验句，断验难分（同易林补遗 B 级型）。"},
    "QL-016": {"decision": "keep_B", "category": "求测在生平之后（前提型）",
               "reason": "造访求测时家道中落已成事实、为求测前提；韦断所释为已然时段，前瞻部分（辛运、未运）书内无应验记载。"},
    "QL-017": {"decision": "keep_B", "category": "结局即断语前瞻复述",
               "reason": "『获贵客垂青、纳为拥抱』在断语内以『当有』前瞻出之，outcome 系其复述，无另载应验。"},
    "QL-020": {"decision": "keep_B", "category": "结局仅求测时状态",
               "reason": "结局仅『年逾四十未嫁』之求测时状态（前提）；癸水、甲运发扬皆前瞻，书内无应验。"},
    "QL-022": {"decision": "keep_B", "category": "结局仅迄今状态总评",
               "reason": "结局仅徒众逾千、逍遥法外之现状总评；子运难逃为前瞻，无应验记载。"},
    "QL-024": {"decision": "keep_B", "category": "转述地位总评",
               "reason": "『已积资成富』为平翁转述的地位总评，与断语同段，无独立应验事件另载。"},
    "QL-033": {"decision": "keep_B", "category": "回顾定位总评",
               "reason": "跑马获利、香槟头奖为回顾定位，与断语同段交织，无断后应验另载。"},
    "QL-019": {"decision": "keep_B", "category": "仅地位总评＋高污染",
               "reason": "结局仅『金融界巨擘、陶朱盛名』地位总评，无具体事件分述；且 contamination=high，纵改判亦不可封。"},
    "QL-034": {"decision": "keep_B", "category": "回顾总评＋造式两说歧义＋高污染",
               "reason": "结局为屡起屡仆回顾总评、无具体事件分述；四柱有己酉丁卯／戊申壬子两说并存歧义；且 contamination=high。"},
}
b_cases = []
for r in nonseal:
    if r["review"]["grade_final"] == "B":
        d = REGRADE[r["id"]]
        o = orig[r["id"]]
        b_cases.append({
            "id": r["id"], "subject": r["subject"], "source_work": r["source_work"],
            "grade_final_reviewH": r["review"]["grade_final"],
            "contamination_final": r["review"]["contamination_final"],
            "provenance_page": o.get("provenance", {}).get("page"),
            **d,
        })
assert len(b_cases) == 15, len(b_cases)

seal_ids = sorted(r["id"] for r in seal)
seal_used = {h: sorted(set(seal_ids) & s) for h, s in HOLDOUT_IDS.items() if set(seal_ids) & s}
seal_unused = sorted(set(seal_ids) - ALL_HOLDOUT_USED)

supply_bz = {
    "meta": {
        "seat": "data (R36 census, no prediction/scoring/set-building)",
        "sources": [
            "expansion12/natal-batch2/cases-reviewed.jsonl (92)",
            "expansion12/natal-batch2/cases.jsonl (92, originals)",
            "expansion12/natal-batch2/REVIEW-H.md, CENSUS-NOTES.md, RENUMBER-MAP.json",
            "expansion12/natal-leftovers/cases.jsonl (55), GRADE-ADDENDUM.json, REGRADE-REVIEW.md, CENSUS-NOTES.md",
            "expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl (126), REVIEW-G.md",
            "holdout3..holdout13 test_gold.jsonl (id field only), inputs-dev11 filenames, expansion12/POOL-IDS.txt",
        ],
        "id_note": "IDs are post-R34-renumber: QM->QL (QL-001..008 aligned to holdout12), MP->PU. REVIEW-H/CENSUS old QM/MP numbers map via RENUMBER-MAP.json.",
    },
    "A_a_natal_batch2": {
        "total": len(rev),
        "verdict_counts": dict(verdict_counts),
        "seal_ids": seal_ids,
        "seal_used_by_holdout": seal_used,
        "seal_unused": seal_unused,
        "nonseal_total": len(nonseal),
        "nonseal_cross_grade_x_contamination": {f"{g}/{c}": n for (g, c), n in sorted(cross.items())},
        "nonseal_reason_classes": {
            "A_grade_but_high_contamination_only": 59,
            "B_grade_and_low_contamination": 11,
            "B_grade_and_high_contamination": 4,
            "reject": 0,
        },
        "nonseal_ids_A_high": sorted(r["id"] for r in nonseal
                                     if r["review"]["grade_final"] == "A"
                                     and r["review"]["contamination_final"] == "high"),
        "B_cases_rereviewed": b_cases,
        "rereview_totals": {
            "B_cases_total": len(b_cases),
            "regrade_A_low_grade_only_not_sealable_high_contamination": 2,
            "regrade_to_sealable": 0,
            "keep_B": 13,
        },
        "new_sealable_from_A_a": 0,
    },
}

# --- A(b) natal-leftovers (NL) + 袁氏命谱 book account
nl = read_jsonl(P3 / "expansion12/natal-leftovers/cases.jsonl")
addendum = json.loads((P3 / "expansion12/natal-leftovers/GRADE-ADDENDUM.json").read_text())
regraded_nl = addendum["regraded_to_A_low"]
nl_by_source = collections.Counter(r["source_work"] for r in nl)
nl_grade = collections.Counter(r["outcome_grade"] for r in nl)
nl_cont = collections.Counter(r["contamination"] for r in nl)
nl_sealable_ids = sorted(set(regraded_nl) | {r["id"] for r in nl if r.get("holdout_eligible")})
nl_used = {h: sorted(set(nl_sealable_ids) & s) for h, s in HOLDOUT_IDS.items() if set(nl_sealable_ids) & s}
supply_bz["A_b_natal_leftovers"] = {
    "total": len(nl),
    "by_source_work": dict(nl_by_source),
    "grade_as_written": dict(nl_grade),
    "contamination": dict(nl_cont),
    "addendum_regraded_to_A_low": regraded_nl,
    "sealable_ids_effective": nl_sealable_ids,
    "sealable_used_by_holdout": nl_used,
    "sealable_unused": sorted(set(nl_sealable_ids) - ALL_HOLDOUT_USED),
    "nonsealable_remaining": len(nl) - len(nl_sealable_ids),
}
supply_bz["A_b_yuanshi_mingpu_book"] = {
    "book": "《袁氏命谱》四库存目子平汇刊8重校绘图本 (incoming/wanted-books-2)",
    "book_total_zao_stated_in_preface": 64,
    "extracted_PU": 57,
    "dedup_removed_at_extraction": [
        {"subject": "关羽", "pool_match": "NL-021"},
        {"subject": "明毅宗（崇祯）", "pool_match": "wei-014/BZ-034"},
        {"subject": "乾隆", "pool_match": "xu-003/BZ-016/BZ-019/ren-016"},
        {"subject": "曾国藩", "pool_match": "NL-018"},
        {"subject": "左宗棠", "pool_match": "NL-019"},
        {"subject": "彭玉麟", "pool_match": "NL-020"},
        {"subject": "李鸿章", "pool_match": "wei-015/BZ-035"},
    ],
    "unextracted": 0,
    "account": "64 = 57 extracted + 7 dedup-removed + 0 unextracted (CENSUS-NOTES natal-batch2 §一, full 64 read)",
    "sealable_from_book": 0,
    "note": "All 57 extracted are A-grade but high contamination (famous historical figures); REVIEW-H seal = 0 for this book.",
}

# --- A(c) G/H inventory
g = read_jsonl(P3 / "expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl")
g_seal = [r for r in g if r["review"]["verdict"] == "seal"]
g_seal_unused = sorted({r["id"] for r in g_seal} - ALL_HOLDOUT_USED)
supply_bz["A_c_G_inventory"] = {
    "file": "expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl",
    "total": len(g),
    "tradition_counts": dict(collections.Counter(r["tradition"] for r in g)),
    "verdict_counts": dict(collections.Counter(r["review"]["verdict"] for r in g)),
    "seal_total": len(g_seal),
    "seal_unused_in_any_holdout3_13": g_seal_unused,
    "seal_unused_count": len(g_seal_unused),
    "bazi_cases_in_G": sum(1 for r in g if r["tradition"] == "八字"),
    "bazi_sealable_in_G": 0,
}
supply_bz["A_c_H_inventory"] = {
    "file": "expansion12/natal-batch2/cases-reviewed.jsonl",
    "total": len(rev),
    "tradition_counts": dict(collections.Counter(r["tradition"] for r in rev)),
    "seal_total": len(seal),
    "seal_unused_in_any_holdout3_13": seal_unused,
    "bazi_sealable_new_in_H": 0,
    "note": "All 18 seal (QL) were consumed: holdout12 x8 + holdout13 x10 (see A_a seal_used_by_holdout).",
}

# --- A(d) 千里命稿 coverage (figures from natal-batch2/CENSUS-NOTES.md §二/§三)
supply_bz["A_d_qianli_minggao_book"] = {
    "book": "《千里命稿》中州古籍重印本, PDF 423 pp; 应运篇 book pp.225-304 read in full; other chapters census by chapter characterisation",
    "note_on_task_wording": "natal-batch2's 92 = 袁氏命谱 57 + 千里命稿 35; the 千里命稿 book itself contributed 35, not 92.",
    "extracted_QM_now_QL": 35,
    "extracted_grade_split": {"A": 22, "B": 13},
    "dedup_removed_at_extraction": 12,
    "discarded_listed_in_census": {
        "identity_or_prospective_only": 19,
        "fact_embedded_in_prediction_flow": 3,
        "incomplete_or_damaged_chart": 6,
        "newborn_or_undecided_prospective": 6,
        "other_listed": 8,
        "total_listed": 42,
    },
    "yingyun_identifiable_items_approx": 35 + 12 + 42,
    "coverage_of_yingyun": "35/89 extracted (39%), 18/89 seal (20%)",
    "unextracted_space": "应运篇已逐页全读，余条均已逐条定性弃置（见上）；理论各篇短式例全类弃、评断篇原则弃（CENSUS 未逐条计数）——按现行入封标准未抽空间可封存实得 0。",
    "sealable_new": 0,
}

supply_bz["totals"] = {
    "native_seal_unused_bazi": len(seal_unused) + len(supply_bz["A_b_natal_leftovers"]["sealable_unused"]),
    "regraded_to_sealable_bazi": 0,
    "regraded_grade_only_not_sealable": 2,
    "new_sealable_bazi_total": 0,
}

(OUT / "supply-bz-r36.json").write_text(json.dumps(supply_bz, ensure_ascii=False, indent=1))

# ---------------------------------------------------------------- Part B (LY)
# Explicit case-file list only. For expansion/expansion2 (inputs/answers layout)
# only ids are taken from inputs.jsonl; source attribution from GRADING/SOURCES docs.
ly_files = [
    # (path, kind) kind: cases = full case rows; ids = id-only rows
    (ROOT / "masters-dataset/chinese-divination/inputs.jsonl", "ids_master"),
    (P3 / "expansion/zengshan/inputs.jsonl", "ids"),
    (P3 / "expansion/bushi/inputs.jsonl", "ids"),
    (P3 / "expansion2/zengshan/inputs.jsonl", "ids"),
    (P3 / "expansion2/bushi/inputs.jsonl", "ids"),
    (P3 / "expansion3/cases.jsonl", "cases"),
    (P3 / "expansion4/cases.jsonl", "cases"),
    (P3 / "expansion5/cases.jsonl", "cases"),
    (P3 / "expansion7/bushi-quanshu/cases.jsonl", "cases"),
    (P3 / "expansion7/yiyin/cases.jsonl", "cases"),
    (P3 / "expansion7/yiyin2/cases.jsonl", "cases"),
    (P3 / "expansion8/yimao/cases.jsonl", "cases"),
    (P3 / "expansion8/duanyi-tianji/cases.jsonl", "cases"),
    (P3 / "expansion10/yilin-buyi/cases.jsonl", "cases"),
    (P3 / "expansion10/yilin-buyi-zongduan/cases.jsonl", "cases"),
    (P3 / "expansion11/bushi-zhengzong/cases.jsonl", "cases"),
    (P3 / "expansion12/huangjince-huozhulin/cases.jsonl", "cases"),
]
PREFIX_SOURCE = [
    ("LY-0", "masters-initial (LY-001-036: 增删26/卜筮正宗10; LY-2xx etc. handled by file)"),
]
per_file = []
all_ly_ids = collections.defaultdict(list)  # prefix -> ids
for path, kind in ly_files:
    rows = read_jsonl(path)
    ids = [r["id"] for r in rows]
    entry = {"file": str(path.relative_to(ROOT)), "rows": len(rows), "ids_sample": ids[:3]}
    if kind == "cases":
        entry["source_work_counts"] = dict(collections.Counter(str(r.get("source_work")) for r in rows))
        entry["grade_counts"] = dict(collections.Counter(str(r.get("outcome_grade")) for r in rows))
        entry["contamination_counts"] = dict(collections.Counter(str(r.get("contamination")) for r in rows))
    per_file.append(entry)
    for i in ids:
        all_ly_ids[i.split("-")[0]].append(i)

prefix_summary = {}
for pref, ids in sorted(all_ly_ids.items()):
    ids = sorted(set(ids))
    in_dev = [i for i in ids if i in DEV9_IDS]
    in_hold = [i for i in ids if i in ALL_HOLDOUT_USED]
    neither = [i for i in ids if i not in DEV9_IDS and i not in ALL_HOLDOUT_USED]
    prefix_summary[pref] = {"n": len(ids), "in_dev9": len(in_dev), "in_holdout3_13": len(in_hold),
                            "neither": neither}

ly = {"per_file": per_file, "prefix_summary": prefix_summary,
      "total_unique_ly_ids": sum(v["n"] for v in prefix_summary.values())}
(OUT / "census-ly-r36.json").write_text(json.dumps(ly, ensure_ascii=False, indent=1))

print(json.dumps(supply_bz["totals"], ensure_ascii=False))
print("BZ nonseal cross:", supply_bz["A_a_natal_batch2"]["nonseal_cross_grade_x_contamination"])
print("seal used:", seal_used, "unused:", seal_unused)
print("NL sealable unused:", supply_bz["A_b_natal_leftovers"]["sealable_unused"])
print("G seal unused:", len(g_seal_unused), "G traditions:", supply_bz["A_c_G_inventory"]["tradition_counts"])
print("LY prefixes:", {k: v["n"] for k, v in prefix_summary.items()})
for k, v in prefix_summary.items():
    if v["neither"]:
        print("NEITHER", k, v["neither"])
