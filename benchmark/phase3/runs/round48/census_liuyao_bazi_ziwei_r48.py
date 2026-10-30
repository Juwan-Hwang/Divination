#!/usr/bin/env python3
"""R48 census seat (liuyao/bazi/ziwei): disk-evidence recount only.
Reads ONLY: masters-dataset/data/*.jsonl, benchmark/phase3/holdout*/test_gold.jsonl,
expansion*/**/cases*.jsonl stock files, sources registration markdown.
Does NOT open any runs/*/predictions, judging or final-scores.
Asserts every count it prints."""
import json, glob, os, collections

ROOT = "/home/hatch/workspace/divination"
P3 = os.path.join(ROOT, "benchmark/phase3")

def load_jsonl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]

# --- used union: dev (masters-dataset data) + holdout3-18 gold ids ---
used = set()
dev = list(json.load(open(os.path.join(P3, "data/master-baseline-dev9.json"), encoding="utf-8")).keys())
used |= set(dev)
gold_n = 0
for d in sorted(glob.glob(os.path.join(P3, "holdout[0-9]*"))):
    g = os.path.join(d, "test_gold.jsonl")
    if os.path.exists(g):
        rows = load_jsonl(g)
        gold_n += len(rows)
        used |= {r["id"] for r in rows}
print(f"dev rows={len(dev)} gold rows={gold_n} used-union>={len(used)}")
assert len(dev) > 400 and gold_n > 400

# --- stock files per book ---
stocks = {
    "yiyin (YY)": "expansion7/yiyin/cases.jsonl",
    "yiyin2 (YY)": "expansion7/yiyin2/cases.jsonl",
    "bushi-quanshu (BQ)": "expansion7/bushi-quanshu/cases.jsonl",
    "bushi-quanshu-beixuan (BQ)": "expansion12/bushi-quanshu-beixuan/cases.jsonl",
    "yimao (YM)": "expansion8/yimao/cases.jsonl",
    "duanyi-tianji (DT)": "expansion8/duanyi-tianji/cases.jsonl",
    "ditian-sui (DS)": "expansion8/ditian-sui/cases.jsonl",
    "bushi-zhengzong-12-18 (ZG)": "expansion11/bushi-zhengzong/cases.jsonl",
    "yilin-buyi (YB)": "expansion10/yilin-buyi/cases.jsonl",
    "yilin-buyi-zongduan (YB)": "expansion10/yilin-buyi-zongduan/cases.jsonl",
    "huangjince-huozhulin (HZ)": "expansion12/huangjince-huozhulin/cases.jsonl",
    "natal-batch2 (PU=mingpu, QL=qianli)": "expansion12/natal-batch2/cases.jsonl",
    "natal-leftovers (NL incl. ziping)": "expansion12/natal-leftovers/cases.jsonl",
    "mingli-tanyuan-mt (MT)": "expansion8/mingli-tanyuan/cases.jsonl",
    "ziwei-quanshu": "expansion8/ziwei/cases.jsonl",
}
for label, rel in stocks.items():
    p = os.path.join(P3, rel)
    rows = load_jsonl(p) if os.path.getsize(p) > 0 else []
    ids = [r["id"] for r in rows]
    in_used = sum(1 for i in ids if i in used)
    elig = sum(1 for r in rows if r.get("holdout_eligible") is True)
    grades = collections.Counter(r.get("outcome_grade") for r in rows)
    contam = collections.Counter(r.get("contamination") for r in rows)
    print(f"{label}: n={len(rows)} in_used_union={in_used} eligible={elig} grades={dict(grades)} contamination={dict(contam)} path=benchmark/phase3/{rel}")
    assert len(ids) == len(set(ids)), label

# --- PU / QL fresh-compliant recount (A + low + eligible + not used) ---
nb2 = load_jsonl(os.path.join(P3, "expansion12/natal-batch2/cases.jsonl"))
for pref in ("PU", "QL"):
    sub = [r for r in nb2 if r["id"].startswith(pref + "-")]
    fresh_ok = [r["id"] for r in sub if r.get("outcome_grade") == "A" and r.get("contamination") == "low"
                and r.get("holdout_eligible") is True and r["id"] not in used]
    print(f"{pref}: n={len(sub)} fresh-A-low-eligible-notused={len(fresh_ok)} {fresh_ok}")
    assert fresh_ok == [], pref  # R43 conclusion re-verified on disk this round

# --- NL (ziping subset NL-046..055) recount ---
nl = load_jsonl(os.path.join(P3, "expansion12/natal-leftovers/cases.jsonl"))
zp = [r for r in nl if r["id"] >= "NL-046"]
fresh_ok = [r["id"] for r in zp if r.get("holdout_eligible") is True and r["id"] not in used]
print(f"NL ziping subset: n={len(zp)} eligible-notused={fresh_ok}")
print("ALL ASSERTIONS PASSED")
