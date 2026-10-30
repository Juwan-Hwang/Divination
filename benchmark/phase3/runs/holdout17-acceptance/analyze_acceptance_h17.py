#!/usr/bin/env python3
"""holdout17 acceptance analysis (analysis role only). Adapted from the
holdout16 analyzer (analyze_acceptance_h16.py) for R41 PREREG s.3/s.7.

Low-pollution caliber is read per-case from the gold file
(benchmark/phase3/holdout17/test_gold.jsonl, field `contamination`):
holdout17 is all-low (40/40, host-verified at seal), so the main caliber
IS the full 40; both are still reported separately, following the h15/h16
layout.

Merge rule (standing): per side (ours / master), final = mean of the two
judge views; |v1.total - v2.total| >= 3 cases are replaced by the
arbitration score. If disputes exist and no arbitration file covers
exactly those cases, this script exits 2 (unresolved-dispute error).

Criteria per runs/round41/PREREG.md s.7 (照既例):
(i) ours mean > master mean; (ii) paired wins > losses;
(iii) paired diff > 0 and diff/SE >= 1.

CZ-QX guardrail per runs/round41/PREREG.md s.3 (written lines, carried
unchanged from R39):
cezi (ZC, n=20) pair diff < -1.963 -> falsified (CZ-QX 判证伪, rollback);
>= -1.613 -> no deterioration seen (未见恶化, register only);
in between -> undecided band (未定带, register only).
The guardrail verdict is registered separately and never substitutes
for the acceptance criteria.

Outputs: judging/final-scores.json + stdout.
"""
import json
import math
import sys
from collections import Counter
from pathlib import Path

ACC = Path(__file__).resolve().parent
JD = ACC / "judging"
GOLD = ACC.parent.parent / "holdout17" / "test_gold.jsonl"
N = 40
CZQX_FALSIFY_BELOW = -1.963   # R41 PREREG s.3: diff < this -> 证伪
CZQX_NO_WORSE_FROM = -1.613   # R41 PREREG s.3: diff >= this -> 未见恶化


def load_jsonl(name):
    out = {}
    p = JD / name
    if not p.exists():
        return out
    for line in open(p, encoding="utf-8"):
        line = line.strip()
        if line:
            r = json.loads(line)
            out[r["anon_id"]] = r
    return out


def merge_side(label, v1name, v2name, arbname, mapping_side):
    v1, v2 = load_jsonl(v1name), load_jsonl(v2name)
    assert set(v1) == set(mapping_side) == set(v2), (
        label, len(v1), len(v2), len(mapping_side))
    disputes = sorted(a for a in v1 if abs(v1[a]["total"] - v2[a]["total"]) >= 3)
    arb = load_jsonl(arbname)
    if disputes and not arb:
        print(f"{label}: DISPUTES pending arbitration: "
              f"{[mapping_side[a] for a in disputes]}")
        return None, disputes, 0.0
    assert set(arb) == set(disputes), (label, sorted(arb), disputes)
    max_diff = max(abs(v1[a]["total"] - v2[a]["total"]) for a in v1)
    final = {}
    for a, cid in mapping_side.items():
        if a in arb:
            final[cid] = float(arb[a]["total"])
        else:
            final[cid] = (v1[a]["total"] + v2[a]["total"]) / 2
    return final, disputes, max_diff


def seg(ids, ours, master):
    diffs = [ours[c] - master[c] for c in ids]
    n = len(diffs)
    m = sum(diffs) / n
    se = (math.sqrt(sum((x - m) ** 2 for x in diffs) / (n - 1)) / math.sqrt(n)) if n > 1 else 0.0
    return {"n": n, "ours_mean": round(sum(ours[c] for c in ids) / n, 3),
            "master_mean": round(sum(master[c] for c in ids) / n, 3),
            "pair_diff": round(m, 3), "SE": round(se, 3),
            "W/T/L": f"{sum(1 for x in diffs if x > 0)}/{sum(1 for x in diffs if x == 0)}/{sum(1 for x in diffs if x < 0)}"}


def criteria(ids, ours, master):
    s = seg(ids, ours, master)
    diffs = [ours[c] - master[c] for c in ids]
    w = sum(1 for x in diffs if x > 0)
    l = sum(1 for x in diffs if x < 0)
    crit = {
        "(i) ours_mean > master_mean": s["ours_mean"] > s["master_mean"],
        "(ii) paired W > L": w > l,
        "(iii) diff > 0 and diff/SE >= 1": s["pair_diff"] > 0 and s["SE"] > 0 and s["pair_diff"] / s["SE"] >= 1,
    }
    return s, crit, all(crit.values())


def main():
    mapping = json.loads((JD / "host-mapping.json").read_text(encoding="utf-8"))
    ours, d_o, max_o = merge_side("ours", "judgeO1.jsonl", "judgeO2.jsonl",
                                  "arbitration-ours.jsonl", mapping["ours"])
    master, d_m, max_m = merge_side("master", "judgeM1.jsonl", "judgeM2.jsonl",
                                    "arbitration-master.jsonl", mapping["master"])
    if ours is None or master is None:
        return 2
    ids = sorted(ours)
    assert ids == sorted(master) and len(ids) == N

    # Low-pollution caliber from the gold rows themselves (per-case read).
    gold_rows = [json.loads(line) for line in open(GOLD, encoding="utf-8")
                 if line.strip()]
    assert len(gold_rows) == N, len(gold_rows)
    assert sorted(r["id"] for r in gold_rows) == ids
    contam = Counter(r["contamination"] for r in gold_rows)
    grades = Counter(r["outcome_grade"] for r in gold_rows)
    low_ids = sorted(r["id"] for r in gold_rows if r["contamination"] == "low")
    non_low = [c for c in ids if c not in set(low_ids)]
    low_info = {
        "gold_file": "benchmark/phase3/holdout17/test_gold.jsonl",
        "contamination_counts": dict(contam),
        "outcome_grade_counts": dict(grades),
        "low_n": len(low_ids),
        "non_low_ids": non_low,
        "low_subset_equals_full_set": low_ids == ids,
    }

    main_ids = low_ids
    head_m, crit_m, pass_m = criteria(main_ids, ours, master)
    head_f, crit_f, pass_f = criteria(ids, ours, master)
    groups = {
        "cezi-ZC": [c for c in ids if c.startswith("ZC-")],
        "liuren-BYZ": [c for c in ids if c.startswith("BYZ-")],
        "liuren-CY": [c for c in ids if c.startswith("CY-")],
        "liuren-DA": [c for c in ids if c.startswith("DA-")],
        "liuren-all20": [c for c in ids if c.split("-")[0] in ("BYZ", "CY", "DA")],
    }
    # Segment sizes per R41 PREREG s.4.2 composition; assert, do not assume.
    assert len(groups["cezi-ZC"]) == 20, len(groups["cezi-ZC"])
    assert len(groups["liuren-all20"]) == 20, len(groups["liuren-all20"])
    assert len(groups["liuren-BYZ"]) == 7, len(groups["liuren-BYZ"])
    assert len(groups["liuren-CY"]) == 6, len(groups["liuren-CY"])
    assert len(groups["liuren-DA"]) == 7, len(groups["liuren-DA"])
    segments = {k: seg(v, ours, master) for k, v in groups.items() if v}

    # CZ-QX guardrail settlement (R41 PREREG s.3), on the cezi segment.
    zc_diff = segments["cezi-ZC"]["pair_diff"]
    if zc_diff < CZQX_FALSIFY_BELOW:
        czqx_tier, czqx_action = "证伪", "回滚 R39 CZ-QX 并入提交（须回滚）"
    elif zc_diff >= CZQX_NO_WORSE_FROM:
        czqx_tier, czqx_action = "未见恶化", "只登记，不作增益宣称"
    else:
        czqx_tier, czqx_action = "未定带", "只登记读数，不处置"
    czqx = {"segment": "cezi-ZC", "n": segments["cezi-ZC"]["n"],
            "pair_diff": zc_diff, "SE": segments["cezi-ZC"]["SE"],
            "falsify_below": CZQX_FALSIFY_BELOW,
            "no_worse_from": CZQX_NO_WORSE_FROM,
            "tier": czqx_tier, "action": czqx_action}

    out = {"ours": ours, "master": master,
           "main_caliber_low40": {**head_m, "criteria": crit_m, "PASS": pass_m},
           "full40": {**head_f, "criteria": crit_f, "PASS": pass_f},
           "segments": segments,
           "cz_qx_guardrail": czqx,
           "low_pollution": low_info,
           "max_abs_view_diff": {"ours": max_o, "master": max_m},
           "disputes_ours": [mapping["ours"][a] for a in d_o],
           "disputes_master": [mapping["master"][a] for a in d_m],
           "per_case": {c: {"ours": ours[c], "master": master[c],
                            "diff": round(ours[c] - master[c], 3)} for c in ids}}
    with open(JD / "final-scores.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print("== main caliber (low 40; low subset == full set: "
          f"{low_info['low_subset_equals_full_set']}) ==")
    print(f"contamination counts: {dict(contam)} | outcome_grade: {dict(grades)}")
    print(f"ours mean {head_m['ours_mean']} | master mean {head_m['master_mean']}")
    print(f"pair diff {head_m['pair_diff']:+.3f} (SE {head_m['SE']:.3f}) | W/T/L {head_m['W/T/L']}")
    for k, v in crit_m.items():
        print(k, "->", v)
    print("ACCEPTANCE PASS (main caliber):", pass_m)
    print("== full 40 (alongside) ==")
    print(f"ours mean {head_f['ours_mean']} | master mean {head_f['master_mean']} | pair diff {head_f['pair_diff']:+.3f} (SE {head_f['SE']:.3f}) | W/T/L {head_f['W/T/L']} | PASS:", pass_f)
    print("segments:", json.dumps(segments, ensure_ascii=False))
    print(f"CZ-QX guardrail: cezi pair diff {zc_diff:+.3f} -> tier 「{czqx_tier}」 ({czqx_action})")
    print(f"max |view diff|: ours {max_o} | master {max_m} | disputes ours {out['disputes_ours']} master {out['disputes_master']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
