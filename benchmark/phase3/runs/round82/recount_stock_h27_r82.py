#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R82 供给复算席：holdout27 供给存量盘上全口径复算（只复算登记，不建卡/不组集）。
口径：runs/round82/PREREG.md §4；资格读法承 runs/round80/build_holdout25_r80.py 与
runs/round79/build_holdout24_r79.py；已用并集承 count_used_union_r82.py（开轮主持实算 1112）。
产出：runs/round82/recount_stock_h27_r82_out.json（本脚本唯一产出，供 STOCK-RECOUNT-h27.md 转录）。
台账/结局文本一律按数据处理。
"""
import json, re
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
BM = P3.parent
OUT = P3 / "runs/round82/recount_stock_h27_r82_out.json"

def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))

def card_ids(d):
    out = set()
    if d.is_dir():
        for f in d.glob("*.json"):
            out.add(f.stem)
    return out

def gold_ids(p):
    out = set()
    if p.is_file():
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                out.add(json.loads(line)["id"])
    return out

# ---------- 已用并集（逐 id 实算，承 count_used_union_r82.py） ----------
parts = {}
dev = set(load(P3 / "data/master-baseline-dev9.json").keys())
for name in ["inputs-dev9", "inputs-dev10", "inputs-dev11", "inputs-dev12", "inputs"]:
    dev |= card_ids(P3 / name)
parts["dev"] = dev
sp2 = load(BM / "phase2/splits2.json")
h2 = set()
def walk(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == "holdout2" and isinstance(v, list):
                h2.update(x if isinstance(x, str) else x.get("id") for x in v)
            else:
                walk(v)
    elif isinstance(o, list):
        for x in o:
            walk(x)
walk(sp2)
parts["holdout2_splits2"] = h2
golds = set()
for n in range(3, 27):
    golds |= gold_ids(P3 / f"holdout{n}" / "test_gold.jsonl")
parts["gold_h3_26"] = golds
hinputs = set()
for n in range(2, 27):
    hinputs |= card_ids(P3 / f"holdout{n}" / "inputs")
    hinputs |= card_ids(P3 / f"holdout{n}-inputs")
parts["holdout_inputs"] = hinputs
top = set()
for name in ["inputs6", "inputs7", "inputs8", "inputs9", "inputs10"]:
    top |= card_ids(P3 / name)
parts["top_inputs6_10"] = top
USED = set()
for v in parts.values():
    USED |= v
assert len(USED) == 1112, len(USED)

R = {"used_union": {"total": len(USED), "parts": {k: len(v) for k, v in parts.items()}},
     "ledgers": {}, "old_faces": {}}

def funnel(rows):
    """rows: list of (id, stages) where stages is list of (stage_name, passed_bool).
    Returns per-stage elimination counts in given order (sequential funnel)."""
    stages = [s for s, _ in rows[0][1]] if rows else []
    remaining = list(rows)
    out = []
    for s in stages:
        nxt = [(i, st) for (i, st) in remaining if dict(st)[s]]
        out.append({"stage": s, "eliminated": len(remaining) - len(nxt),
                    "eliminated_ids": [i for (i, st) in remaining if not dict(st)[s]],
                    "remaining": len(nxt)})
        remaining = nxt
    return out, [i for i, _ in remaining]

def nonempty(x):
    return isinstance(x, str) and bool(x.strip())

# ---------- DS 段氏理象学 r76 ----------
ds = load(P3 / "runs/round76/digestion/SUPPLY-MINING-duanshi-r76.json")
rows = []
for r in ds["records"]:
    rows.append((r["case_id"], [
        ("eligible_net=true", r.get("eligible_net") is True),
        ("anchor present", r.get("anchor_status") == "present"),
        ("contamination low", r.get("contamination_pre") == "low"),
        ("四滤全pass", all(str(v).startswith("pass") for v in r["filters"].values())),
        ("断语/结局非空", nonempty(r.get("master_assertion")) and nonempty(r.get("outcome"))),
    ]))
f, qual = funnel(rows)
R["ledgers"]["DS-r76"] = {"path": str(P3 / "runs/round76/digestion/SUPPLY-MINING-duanshi-r76.json"),
    "total": len(rows), "funnel": f, "qualified": qual,
    "qualified_used": [i for i in qual if i in USED],
    "qualified_unused": [i for i in qual if i not in USED],
    "ledger_count_field": ds.get("count")}

# ---------- QM 开悟 r76 ----------
kw = load(P3 / "runs/round76/digestion/SUPPLY-MINING-kaiwu-r76.json")
rows = []
for c in kw["cases"]:
    sc = c.get("stem_check") or {}
    rows.append((c["case_id"], [
        ("anchor present", c.get("anchor_status") == "present"),
        ("contamination low", c.get("contamination_pre") == "low"),
        ("separable=true", c.get("separable") is True),
        ("stem_check天地盘双ok(全合)", bool(sc.get("tianpan_ok")) and bool(sc.get("dipan_ok"))),
        ("断语/结局非空", nonempty(c.get("master_assertion")) and nonempty(c.get("outcome"))),
    ]))
f, qual = funnel(rows)
R["ledgers"]["KW-kaiwu-r76"] = {"path": str(P3 / "runs/round76/digestion/SUPPLY-MINING-kaiwu-r76.json"),
    "total": len(rows), "funnel": f, "qualified": qual,
    "qualified_used": [i for i in qual if i in USED],
    "qualified_unused": [i for i in qual if i not in USED]}

# ---------- QM 启悟 r76 ----------
qw76 = load(P3 / "runs/round76/digestion/SUPPLY-MINING-qiwu-r76.json")
rows = []
for c in qw76["cases"]:
    rows.append((c["case_id"], [
        ("anchor present", c.get("anchor_status") == "present"),
        ("contamination low", c.get("contamination_pre") == "low"),
        ("separable=true", c.get("separable") is True),
        ("断语/结局非空", nonempty(c.get("master_assertion")) and nonempty(c.get("outcome"))),
    ]))
f, qual = funnel(rows)
R["ledgers"]["QW76-qiwu-r76"] = {"path": str(P3 / "runs/round76/digestion/SUPPLY-MINING-qiwu-r76.json"),
    "total": len(rows), "funnel": f, "qualified": qual,
    "qualified_used": [i for i in qual if i in USED],
    "qualified_unused": [i for i in qual if i not in USED]}

# ---------- QM 石建国 r76 ----------
sg = load(P3 / "runs/round76/digestion/SUPPLY-MINING-shijianguo-r76.json")
rows = []
for c in sg["cases"]:
    rows.append((c["case_id"], [
        ("anchor present", c.get("anchor_status") == "present"),
        ("contamination low", c.get("contamination_pre") == "low"),
        ("separable=true", c.get("separable") is True),
        ("断语/结局非空", nonempty(c.get("master_assertion")) and nonempty(c.get("outcome"))),
    ]))
f, qual = funnel(rows)
R["ledgers"]["SG-shijianguo-r76"] = {"path": str(P3 / "runs/round76/digestion/SUPPLY-MINING-shijianguo-r76.json"),
    "total": len(rows), "funnel": f, "qualified": qual,
    "qualified_used": [i for i in qual if i in USED],
    "qualified_unused": [i for i in qual if i not in USED],
    "screened_out_n": len(sg.get("screened_out", []))}

# ---------- ZCB 字触补 r76 ----------
zc = load(P3 / "runs/round76/digestion/SUPPLY-MINING-zichubu-r76.json")
rows = []
for c in zc["cases"]:
    rows.append((c["case_id"], [
        ("eligible=true", c.get("eligible") is True),
        ("anchor present", c.get("anchor_status") == "present"),
        ("contamination low", c.get("contamination_pre") == "low"),
        ("separable=true", c.get("separable") is True),
        ("断语/结局非空", nonempty(c.get("master_assertion")) and nonempty(c.get("outcome"))),
    ]))
f, qual = funnel(rows)
zc_unused_all = [i for i in qual if i not in USED]
R["ledgers"]["ZCB-zichubu-r76"] = {"path": str(P3 / "runs/round76/digestion/SUPPLY-MINING-zichubu-r76.json"),
    "total": len(rows), "funnel": f, "qualified": qual,
    "qualified_used": [i for i in qual if i in USED],
    "qualified_unused_before_ruling": zc_unused_all,
    "zcb003_in_qualified_unused": "ZCB-003" in zc_unused_all,
    "qualified_unused_selectable": [i for i in zc_unused_all if i != "ZCB-003"],
    "meta_counts": zc["meta"].get("counts")}

# ---------- GSZ 卦例说真 r57（含五要素复核，承 build_holdout25_r80.py five_elements） ----------
gsz = load(P3 / "runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json")
gsz_by = {e["provisional_id"]: e for e in gsz["entries"]}
def filt_all_true(fl):
    return all(v is True for v in fl.values())
rows = []
for e in gsz["entries"]:
    rows.append((e["provisional_id"], [
        ("grade A", e.get("grade") == "A"),
        ("pollution low", e.get("pollution") == "low"),
        ("anchor present", e.get("anchor_presence") == "present"),
        ("eligible_net=true", e.get("eligible_net") is True),
        ("四滤全true", filt_all_true(e.get("filters") or {})),
        ("断语/结局非空", nonempty(e.get("master_prediction")) and nonempty(e.get("outcome_record"))),
    ]))
f, qual = funnel(rows)
net_list = gsz["counts"]["net_eligible_A_low_present"]
book_txt = (P3 / "runs/round76/gsz-book-r76.txt").read_text(encoding="utf-8")
LIUQIN = ["兄弟", "子孙", "妻财", "官鬼", "父母"]
GANZHI = list("甲乙丙丁戊己庚辛壬癸子丑寅卯辰巳午未申酉戌亥")
def five_elements(cid):
    e = gsz_by[cid]
    chart = e["input_fields"]["chart"]
    lines = chart["chart_lines_top_to_bottom"]
    joined = "\n".join(lines)
    el = {}
    el["gua_name"] = bool(chart.get("ben_gua"))
    el["moving"] = ("动" in joined) or bool(chart.get("bian_gua"))
    el["shi_ying"] = ("世" in joined) and ("应" in joined)
    el["liuqin_nazhi"] = all(
        any(lq in ln and any(g in ln for g in GANZHI) for ln in lines)
        for lq in [x for x in LIUQIN if any(x in ln for ln in lines)]) and \
        sum(1 for ln in lines if any(lq in ln for lq in LIUQIN)) >= 6
    asked = e["input_fields"]["asked_at"]
    el["yuejian_richen"] = bool(re.search(r"月", asked) and re.search(r"日", asked))
    el["in_book_ben_gua"] = chart["ben_gua"][:2] in book_txt or chart["ben_gua"] in book_txt
    el["in_book_asked"] = asked.split("（")[0][:7] in book_txt.replace(" ", "")
    return el
five = {}
for cid in net_list:
    el = five_elements(cid)
    five[cid] = {"elements": el, "pass": all(el.values())}
qual_unused = [i for i in qual if i not in USED]
R["ledgers"]["GSZ-guaishuo-r57"] = {"path": str(P3 / "runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json"),
    "total": len(rows), "funnel": f, "qualified": qual,
    "qualified_equals_net_list": set(qual) == set(net_list), "net_list_n": len(net_list),
    "qualified_used": [i for i in qual if i in USED],
    "qualified_unused": qual_unused,
    "five_element_on_unused": five and {k: v for k, v in five.items() if k in qual_unused},
    "five_element_fail_unused": [k for k in qual_unused if not five[k]["pass"]],
    "five_element_pass_unused": [k for k in qual_unused if five[k]["pass"]],
    "counts_field": {k: (v if not isinstance(v, list) else f"list[{len(v)}]") for k, v in gsz["counts"].items()}}

# ---------- WHY 一轮 r56 ----------
why1 = load(P3 / "runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json")
net1 = why1["counts"]["net_eligible_A_low_present"]
e1 = {e["provisional_id"]: e for e in why1["entries"]}
# r56 台账 entries 无 grade/filters/eligible_net 字段（逐项实查键集），净入账以 counts 名单为准；
# 名单外条目逐项以 anchor_presence/pollution 登记其不合项。
rows = []
for e in why1["entries"]:
    rows.append((e["provisional_id"], [
        ("anchor present", e.get("anchor_presence") == "present"),
        ("pollution low", e.get("pollution") == "low"),
        ("counts净入账名单成员", e["provisional_id"] in net1),
    ]))
f, qual = funnel(rows)
R["ledgers"]["WHY1-wanghuying-r56"] = {"path": str(P3 / "runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json"),
    "total": len(rows), "funnel": f, "qualified": qual,
    "qualified_equals_net_list": set(qual) == set(net1),
    "entry_keys_union": sorted({k for e in why1["entries"] for k in e.keys()}),
    "qualified_used": [i for i in qual if i in USED],
    "qualified_unused": [i for i in qual if i not in USED],
    "counts_field": {k: (v if not isinstance(v, list) else f"list[{len(v)}]") for k, v in why1["counts"].items()}}

# ---------- WHY 二轮 r57-r2 ----------
why2 = load(P3 / "runs/round57/digestion/SUPPLY-MINING-wanghuying-r57-r2.json")
net2 = why2["counts"]["net_eligible_A_low_present"]
rows = []
for e in why2["entries"]:
    rows.append((e["provisional_id"], [
        ("grade A", e.get("grade") == "A"),
        ("pollution low", e.get("pollution") == "low"),
        ("anchor present", e.get("anchor_presence") == "present"),
        ("eligible_net=true", e.get("eligible_net") is True),
        ("四滤全true", filt_all_true(e.get("filters") or {})),
        ("断语/结局非空", nonempty(e.get("master_prediction")) and nonempty(e.get("outcome_record"))),
    ]))
f, qual = funnel(rows)
R["ledgers"]["WHY2-wanghuying-r57r2"] = {"path": str(P3 / "runs/round57/digestion/SUPPLY-MINING-wanghuying-r57-r2.json"),
    "total": len(rows), "funnel": f, "qualified": qual,
    "qualified_equals_net_list": set(qual) == set(net2), "net_list_n": len(net2),
    "registered_only_ids": [e.get("provisional_id") for e in why2.get("registered_only", [])],
    "qualified_used": [i for i in qual if i in USED],
    "qualified_unused": [i for i in qual if i not in USED]}

# ---------- QW 曲炜 r56 ----------
qw56 = load(P3 / "runs/round56/digestion/SUPPLY-MINING-quwei-r56.json")
def filt_all_pass_str(fl):
    return all(str(v).startswith("pass") for v in (fl or {}).values())
rows = []
for e in qw56["entries"]:
    rows.append((e["provisional_id"], [
        ("anchor present", e.get("anchor_presence") == "present"),
        ("pollution low", e.get("pollution") == "low"),
        ("四滤全pass", filt_all_pass_str(e.get("filters"))),
        ("结局非空", nonempty(e.get("outcome_record"))),
    ]))
f, qual = funnel(rows)
R["ledgers"]["QW-quwei-r56"] = {"path": str(P3 / "runs/round56/digestion/SUPPLY-MINING-quwei-r56.json"),
    "total": len(rows), "funnel": f, "qualified": qual,
    "entry_keys_union": sorted({k for e in qw56["entries"] for k in e.keys()}),
    "qualified_used": [i for i in qual if i in USED],
    "qualified_unused": [i for i in qual if i not in USED]}

# ---------- QW 曲炜续抽 r59 ----------
qw59 = load(P3 / "runs/round59/digestion/SUPPLY-MINING-quwei-r59.json")
rows = []
for e in qw59["entries"]:
    rows.append((e["provisional_id"], [
        ("anchor present", e.get("anchor_presence") == "present"),
        ("pollution low", e.get("pollution") == "low"),
        ("四滤全pass", filt_all_pass_str(e.get("filters"))),
        ("eligible_net=true", e.get("eligible_net") is True),
        ("断语/结局非空", nonempty(e.get("master_prediction")) and nonempty(e.get("outcome_record"))),
    ]))
f, qual = funnel(rows)
R["ledgers"]["QW-quwei-r59"] = {"path": str(P3 / "runs/round59/digestion/SUPPLY-MINING-quwei-r59.json"),
    "total": len(rows), "funnel": f, "qualified": qual,
    "qualified_used": [i for i in qual if i in USED],
    "qualified_unused": [i for i in qual if i not in USED],
    "count_field": qw59.get("count")}

# ---------- QM 奇门 r56（资格承 QM-REVIEW-r58 复核） ----------
qm56 = load(P3 / "runs/round56/digestion/SUPPLY-MINING-qimen-r56.json")
qmr = load(P3 / "runs/round58/digestion/QM-REVIEW-r58.json")
rev = {c["provisional_id"]: c for c in qmr["cases"]}
rows = []
for c in qm56["cases"]:
    cid = c["provisional_id"]
    rv = rev.get(cid, {})
    rows.append((cid, [
        ("anchor present(台账)", c.get("anchor_presence") == "present"),
        ("pollution low(台账)", c.get("pollution") == "low"),
        ("R58复核 eligible_optional=true", rv.get("eligible_optional") is True),
        ("断语/结局非空", nonempty(c.get("master_prediction_verbatim")) and nonempty(c.get("outcome_record"))),
    ]))
f, qual = funnel(rows)
R["ledgers"]["QM-qimen-r56"] = {"path": str(P3 / "runs/round56/digestion/SUPPLY-MINING-qimen-r56.json"),
    "review_path": str(P3 / "runs/round58/digestion/QM-REVIEW-r58.json"),
    "total": len(rows), "funnel": f, "qualified": qual,
    "qualified_used": [i for i in qual if i in USED],
    "qualified_unused": [i for i in qual if i not in USED]}

# ---------- 复核件（升格 0，只登记） ----------
R["rechecks"] = {
    "QW-partial-r57": {"path": str(P3 / "runs/round57/digestion/SUPPLY-RECHECK-qwpartial-r57.json"),
        "checked": load(P3 / "runs/round57/digestion/SUPPLY-RECHECK-qwpartial-r57.json")["checked_count"],
        "upgraded": load(P3 / "runs/round57/digestion/SUPPLY-RECHECK-qwpartial-r57.json")["upgraded_present_count"]},
    "WHY-partial-r59": {"path": str(P3 / "runs/round59/digestion/SUPPLY-RECHECK-why-partial-r59.json"),
        "candidate_n": load(P3 / "runs/round59/digestion/SUPPLY-RECHECK-why-partial-r59.json")["candidate_n"],
        "upgrades": load(P3 / "runs/round59/digestion/SUPPLY-RECHECK-why-partial-r59.json")["summary"]["anchor_upgrades_to_present_n"],
        "pool_increment": load(P3 / "runs/round59/digestion/SUPPLY-RECHECK-why-partial-r59.json")["summary"]["optional_pool_increment_n"]},
    "QWpartial-r57-ids": [e["provisional_id"] for e in load(P3 / "runs/round57/digestion/SUPPLY-RECHECK-qwpartial-r57.json")["entries"]],
}

# ---------- 旧面普查 A：supply-ledger r46–r50 jsonl ----------
led_files = ["runs/round46/digestion/supply-ledger-r46.jsonl",
             "runs/round47/digestion/supply-ledger-r47.jsonl",
             "runs/round48/digestion/supply-ledger-r48.jsonl",
             "runs/round49/digestion/supply-ledger-r49.jsonl",
             "runs/round50/digestion/supply-ledger-r50-rest.jsonl",
             "runs/round50/digestion/supply-ledger-r50-yijian.jsonl"]
old_led = {}
for rel in led_files:
    p = P3 / rel
    raw = [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    ents = []
    for e in raw:
        if "summary" in e:
            continue
        eid = e.get("id") or e.get("case_key")
        if not eid or eid in ("SUMMARY",):
            continue
        if e.get("verdict") in ("summary", "path_summary"):
            continue
        is_counted = (e.get("counted") is True) or (e.get("verdict") == "counted")
        ents.append({"id": eid, "counted": is_counted, "raw": e})
    counted = [e["id"] for e in ents if e["counted"]]
    old_led[rel] = {"total": len(ents), "ids": [e["id"] for e in ents],
        "counted_ids": counted,
        "counted_used": [i for i in counted if i in USED],
        "counted_unused": [i for i in counted if i not in USED],
        "not_counted_n": len(ents) - len(counted),
        "entries_detail": [{"id": e["id"], "counted": e["counted"],
                            "grade": e["raw"].get("grade_host") or e["raw"].get("grade"),
                            "contamination": e["raw"].get("contamination"),
                            "verdict": e["raw"].get("verdict"), "source": e["raw"].get("source"),
                            "tradition": e["raw"].get("tradition") or e["raw"].get("system"),
                            "in_used": e["id"] in USED} for e in ents]}
R["old_faces"]["supply_ledgers_r46_r50"] = old_led

# ---------- 旧面普查 B：cards-mining 目录（r46–r53） ----------
mining = {}
import glob as globmod
for d in sorted(globmod.glob(str(P3 / "runs/round*/digestion/cards-mining*"))):
    dp = Path(d)
    ids = set()
    for fp in dp.rglob("*.json"):
        stem = fp.stem
        for suf in ("-input", "-gold"):
            if stem.endswith(suf):
                stem = stem[: -len(suf)]
        ids.add(stem)
    rel = str(dp.relative_to(P3))
    mining[rel] = {"total_ids": len(ids), "ids": sorted(ids),
                   "used": sorted(i for i in ids if i in USED),
                   "unused": sorted(i for i in ids if i not in USED)}
R["old_faces"]["cards_mining_dirs"] = mining

# yw cards-mining (round46, non cards-mining-* naming)
yw = {}
for fp in sorted((P3 / "runs/round46/digestion/cards-mining").glob("*.json")):
    stem = fp.stem
    for suf in ("-input", "-gold"):
        if stem.endswith(suf):
            stem = stem[: -len(suf)]
    yw.setdefault(stem, 0)
    yw[stem] += 1
R["old_faces"]["cards_mining_r46_yw"] = {"ids": sorted(yw),
    "used": sorted(i for i in yw if i in USED), "unused": sorted(i for i in yw if i not in USED)}

# ---------- 旧面普查 C：expansion–expansion12 池 ----------
exp = {}
for name in ["expansion"] + [f"expansion{i}" for i in range(2, 13)]:
    d = P3 / name
    if not d.is_dir():
        continue
    ids = set()
    files = []
    for fp in d.rglob("*.jsonl"):
        fids = set()
        for line in fp.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except Exception:
                continue
            v = o.get("id") or o.get("case_id") or o.get("provisional_id")
            if v:
                fids.add(v)
        if fids:
            files.append({"file": str(fp.relative_to(P3)), "n_ids": len(fids)})
            ids |= fids
    exp[name] = {"total_ids": len(ids), "used_n": len([i for i in ids if i in USED]),
                 "unused_ids": sorted(i for i in ids if i not in USED), "files": files}
R["old_faces"]["expansion_pools"] = exp

OUT.write_text(json.dumps(R, ensure_ascii=False, indent=1), encoding="utf-8")
print("used union", len(USED), {k: len(v) for k, v in parts.items()})
for k, v in R["ledgers"].items():
    print(k, "total", v["total"], "qualified", len(v["qualified"]),
          "used", len(v["qualified_used"]),
          "unused", len(v.get("qualified_unused", v.get("qualified_unused_selectable", []))))
print("GSZ five pass unused:", R["ledgers"]["GSZ-guaishuo-r57"]["five_element_pass_unused"])
print("GSZ five fail unused:", R["ledgers"]["GSZ-guaishuo-r57"]["five_element_fail_unused"])
print("written", OUT, OUT.stat().st_size)
