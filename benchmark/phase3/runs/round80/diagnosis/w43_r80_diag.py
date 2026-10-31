#!/usr/bin/env python3
"""W43 (R80) diagnostic recomputation. Reads only the permitted inputs:
lr-negatives-dev80.json, final-scores.json (round80), DIAG-LR-weight-dev79.json
(prior-round label/book source). Prints recomputed aggregates as JSON.
No gold-standard material is opened.
"""
import json, math, statistics, sys
from pathlib import Path

BASE = Path("/home/hatch/workspace/divination/benchmark/phase3/runs")
neg = json.loads((BASE / "round80/diagnosis/lr-negatives-dev80.json").read_text())
fs = json.loads((BASE / "round80/final-scores.json").read_text())
prev = json.loads((BASE / "round79/diagnosis/DIAG-LR-weight-dev79.json").read_text())

out = {}

# --- final-scores structure probe (keys only + liuren segments) ---
def walk(obj, path=""):
    hits = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = f"{path}/{k}"
            if isinstance(v, dict) and ("pair_diff" in v or "ours_mean" in v or "master_mean" in v):
                hits.append((p, {kk: v[kk] for kk in ("n", "neg", "pair_diff", "SE", "ours_mean", "master_mean") if kk in v}))
            hits.extend(walk(v, p))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            hits.extend(walk(v, f"{path}[{i}]"))
    return hits

out["final_scores_top_keys"] = list(fs.keys())
out["final_scores_segment_like"] = walk(fs)

# --- negatives self-consistency and segment stats ---
negs = neg["negatives"]
out["n_liuren_total"] = neg["n_liuren_total"]
out["n_negative"] = len(negs)
out["self_consistent"] = sum(1 for r in negs if abs((r["ours"] - r["master"]) - r["pair_diff"]) < 1e-9)

def seg_stats(rows):
    diffs = [r["pair_diff"] for r in rows]
    return {"n": len(rows), "sum": round(sum(diffs), 4),
            "mean": round(statistics.fmean(diffs), 4) if diffs else None,
            "median": statistics.median(diffs) if diffs else None}

dev8 = [r for r in negs if r["in_dev8"]]
lr3 = [r for r in negs if not r["in_dev8"]]
out["negative_subset"] = {"dev8": seg_stats(dev8), "LR3": seg_stats(lr3), "ALL": seg_stats(negs)}
out["seg_ids"] = {"dev8": [r["case_id"] for r in dev8], "LR3": [r["case_id"] for r in lr3]}

# --- cross-check ours against final-scores per-case dicts (axis2 value and sub.total) ---
ax = fs.get("ours_axis2", {})
sub = fs.get("ours_sub", {})
chk_n = chk_ax = chk_sub = 0
mismatch = []
for r in negs:
    cid = r["case_id"]
    if cid in ax or cid in sub:
        chk_n += 1
    if cid in ax and abs(ax[cid] - r["ours"]) < 1e-9:
        chk_ax += 1
    elif cid in ax:
        mismatch.append((cid, "ours_axis2", ax[cid], r["ours"]))
    st = (sub.get(cid) or {}).get("total")
    if st is not None and abs(st - r["ours"]) < 1e-9:
        chk_sub += 1
    elif st is not None:
        mismatch.append((cid, "ours_sub.total", st, r["ours"]))
out["final_scores_percase_check"] = {"found": chk_n, "ours_vs_axis2_equal": chk_ax,
                                     "ours_vs_sub_total_equal": chk_sub, "mismatch": mismatch}

# --- labels carried from prior round (dev79 rows) ---
labelmap = {r["case_id"]: r for r in prev["rows"]}
rows = []
unlabelled = []
from collections import Counter, OrderedDict
dist = {"dev8": Counter(), "LR3": Counter(), "ALL": Counter()}
for r in negs:
    seg = "dev8" if r["in_dev8"] else "LR3"
    lab = labelmap.get(r["case_id"])
    if lab is None:
        unlabelled.append(r["case_id"])
        rows.append({"case_id": r["case_id"], "seg": seg, "pair_diff": r["pair_diff"],
                     "ours": r["ours"], "master": r["master"], "label": "UNC",
                     "note": "no prior coding in h16 s2.1 or prior-round (dev79) table; not coded this round",
                     "book": None, "family": "pending"})
        dist[seg]["UNC"] += 1; dist["ALL"]["UNC"] += 1
    else:
        rows.append({"case_id": r["case_id"], "seg": seg, "pair_diff": r["pair_diff"],
                     "ours": r["ours"], "master": r["master"], "label": lab["label"],
                     "note": lab["note"], "book": lab["book"], "family": "guide"})
        dist[seg][lab["label"].rstrip("*")] += 1; dist["ALL"][lab["label"].rstrip("*")] += 1
out["rows"] = rows
out["unlabelled"] = unlabelled
out["label_distribution"] = {k: dict(v) for k, v in dist.items()}

# composition difference vs dev79
prev_ids = set(labelmap)
cur_ids = {r["case_id"] for r in negs}
out["entered_vs_r79"] = sorted(cur_ids - prev_ids)
out["left_vs_r79"] = sorted(prev_ids - cur_ids)

# --- W double report (SE per h16 s0.4) ---
def se(p, n):
    return round(math.sqrt(p * (1 - p) / n) * 100, 1) if n else None

def w_report(seg_rows, seg_key):
    n_neg = len(seg_rows)
    labelled = [r for r in seg_rows if r["label"] != "UNC"]
    n_lab = len(labelled)
    w = [r for r in labelled if r["label"].rstrip("*") == "W"]
    res = {}
    for denom_name, denom in (("negative_n", n_neg), ("labelled_n", n_lab)):
        p = len(w) / denom if denom else 0
        res[denom_name] = {"denom": denom, "W_interface_count": len(w),
                           "W_interface_pct": round(p * 100, 1), "SE_pp": se(p, denom),
                           "hardcore_count": 0, "hardcore_pct": 0.0}
    res["W_ids"] = [r["case_id"] for r in w]
    res["W_all_interface_starred"] = all(r["label"].endswith("*") for r in w)
    return res

out["W_double_report"] = {
    "dev8": w_report([r for r in rows if r["seg"] == "dev8"], "dev8"),
    "LR3": w_report([r for r in rows if r["seg"] == "LR3"], "LR3"),
    "ALL": w_report(rows, "ALL"),
}
out["W_subforms_merged"] = {
    "W-face": [r["case_id"] for r in rows if r["label"].rstrip("*") == "W" and "W-face" in r["note"]],
    "W-name": [r["case_id"] for r in rows if r["label"].rstrip("*") == "W" and "W-name" in r["note"]],
}
out["D_main_labels"] = {
    "dev8": [r["case_id"] for r in rows if r["seg"] == "dev8" and r["label"].rstrip("*") == "D"],
    "LR3": [r["case_id"] for r in rows if r["seg"] == "LR3" and r["label"].rstrip("*") == "D"],
}
fam = {"dev8": Counter(), "LR3": Counter(), "ALL": Counter()}
for r in rows:
    fam[r["seg"]][r["family"]] += 1; fam["ALL"][r["family"]] += 1
out["family_counts"] = {k: dict(v) for k, v in fam.items()}

# T2 quantities (merged, negative denominator)
allc = dist["ALL"]
out["T2_merged"] = {"W_interface_pct_negdenom": out["W_double_report"]["ALL"]["negative_n"]["W_interface_pct"],
                    "E_count": allc.get("E", 0), "E_pct": round(allc.get("E", 0) / len(rows) * 100, 1),
                    "AplusC_count": allc.get("A", 0) + allc.get("C", 0),
                    "AplusC_pct": round((allc.get("A", 0) + allc.get("C", 0)) / len(rows) * 100, 1)}

print(json.dumps(out, ensure_ascii=False, indent=1))
