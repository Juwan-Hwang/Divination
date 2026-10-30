#!/usr/bin/env python3
"""holdout19 acceptance analysis (analysis role only). Adapted from the
holdout18 analyzer (analyze_acceptance_h18.py) for R52 PREREG s.3.

Calibers (R52 PREREG s.2/s.3, host ruling carried from R51):
- Sealed caliber: gold `contamination_suggestion` read per-case; the set
  is all-low (25/25, seal log data/holdout19-seal-log.md).
- MAIN caliber: XJ47-047 is ruled MID from strictness (host ruling,
  restated in R52 PREREG s.2 before unsealing), so the main
  low-pollution subset excludes XJ47-047 -> n=24. The three criteria
  are judged on the MAIN caliber; the sealed caliber (n=25) is
  reported alongside; any disagreement resolves to the main caliber.

Merge rule (standing): per side (ours / master), final = mean of the
two judge views; |v1.total - v2.total| >= 3 cases are replaced by the
arbitration score. If disputes exist and no arbitration file covers
exactly those cases, this script exits 2 (unresolved-dispute error).

Criteria per R52 PREREG s.3 (照 R42 PREREG s.8, literal):
(i) ours mean > master mean; (ii) paired wins > losses on the
low-pollution subset; (iii) paired diff > 0 on the low-pollution
subset. diff/SE reported descriptively; the h17-style diff/SE >= 1
side condition is registered as a side note only, not a gate.

CZ-QX: this set has NO cezi case (seal log composition); per R52
PREREG s.3 the guardrail is NOT settled this round and the same-tier
continuation count stays 4. Registered only.

Outputs: judging/final-scores.json + stdout.
"""
import json
import math
import sys
from collections import Counter
from pathlib import Path

ACC = Path(__file__).resolve().parent
JD = ACC / "judging"
GOLD = ACC.parent.parent / "holdout19" / "test_gold.jsonl"
N = 25
MID_OVERRIDE = {"XJ47-047": "mid"}  # host ruling (R51, restated R52 PREREG s.2)


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
        "(iii) diff > 0": s["pair_diff"] > 0,
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

    gold_rows = [json.loads(line) for line in open(GOLD, encoding="utf-8")
                 if line.strip()]
    assert len(gold_rows) == N, len(gold_rows)
    assert sorted(r["id"] for r in gold_rows) == ids
    contam_sealed = Counter(r["contamination_suggestion"] for r in gold_rows)
    grades = Counter(r["grade_suggestion"] for r in gold_rows)
    trad_of = {r["id"]: r["tradition"] for r in gold_rows}
    # Main caliber: sealed low minus host-ruled mid override.
    main_low_ids = sorted(r["id"] for r in gold_rows
                          if r["contamination_suggestion"] == "low"
                          and MID_OVERRIDE.get(r["id"]) != "mid")
    sealed_low_ids = sorted(r["id"] for r in gold_rows
                            if r["contamination_suggestion"] == "low")
    low_info = {
        "gold_file": "benchmark/phase3/holdout19/test_gold.jsonl",
        "contamination_field": "contamination_suggestion",
        "sealed_contamination_counts": dict(contam_sealed),
        "grade_counts": dict(grades),
        "host_mid_override": MID_OVERRIDE,
        "main_low_n": len(main_low_ids),
        "sealed_low_n": len(sealed_low_ids),
        "excluded_from_main": [c for c in sealed_low_ids if c not in set(main_low_ids)],
    }

    head_m, crit_m, pass_m = criteria(main_low_ids, ours, master)
    head_f, crit_f, pass_f = criteria(sealed_low_ids, ours, master)

    groups = {
        "mengzhan_all": [c for c in ids if trad_of[c] == "mengzhan"],
        "mengzhan_xuanjie_XJ47": [c for c in ids if c.startswith("XJ47-")],
        "mengzhan_leikao_LK": [c for c in ids if c.startswith("LK-")],
        "mengzhan_yizhi_YZ": [c for c in ids if c.startswith("YZ-")],
        "non_mengzhan_all": [c for c in ids if trad_of[c] != "mengzhan"],
        "yijian_all": [c for c in ids if c.startswith(("SS-", "YJ2-", "YJ3-"))],
        "yuewei_YW3": [c for c in ids if c.startswith("YW3-")],
    }
    assert len(groups["mengzhan_all"]) == 12, len(groups["mengzhan_all"])
    assert len(groups["non_mengzhan_all"]) == 13, len(groups["non_mengzhan_all"])
    assert len(groups["yijian_all"]) == 12, len(groups["yijian_all"])
    segments = {k: seg(v, ours, master) for k, v in groups.items() if v}
    per_trad = {}
    for tr in sorted(set(trad_of.values())):
        per_trad[tr] = seg([c for c in ids if trad_of[c] == tr], ours, master)

    czqx = {"settled": False,
            "note": "No cezi case in holdout19 (R52 PREREG s.3); guardrail not settled, same-tier continuation count stays 4."}

    out = {"ours": ours, "master": master,
           "main_caliber_low24": {**head_m, "criteria": crit_m, "PASS": pass_m},
           "sealed_caliber_full25": {**head_f, "criteria": crit_f, "PASS": pass_f},
           "side_note_diff_over_SE_main": (round(head_m["pair_diff"] / head_m["SE"], 3) if head_m["SE"] > 0 else None),
           "side_note_h17_style_SE_gate_would_hold": bool(head_m["pair_diff"] > 0 and head_m["SE"] > 0 and head_m["pair_diff"] / head_m["SE"] >= 1),
           "segments": segments,
           "per_tradition": per_trad,
           "cz_qx_guardrail": czqx,
           "low_pollution": low_info,
           "max_abs_view_diff": {"ours": max_o, "master": max_m},
           "disputes_ours": [mapping["ours"][a] for a in d_o],
           "disputes_master": [mapping["master"][a] for a in d_m],
           "per_case": {c: {"ours": ours[c], "master": master[c],
                            "diff": round(ours[c] - master[c], 3)} for c in ids}}
    with open(JD / "final-scores.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print("== main caliber (low n=24, XJ47-047 ruled mid excluded) ==")
    print(f"sealed contamination counts: {dict(contam_sealed)} | grades: {dict(grades)}")
    print(f"ours mean {head_m['ours_mean']} | master mean {head_m['master_mean']}")
    print(f"pair diff {head_m['pair_diff']:+.3f} (SE {head_m['SE']:.3f}) | W/T/L {head_m['W/T/L']}")
    for k, v in crit_m.items():
        print(k, "->", v)
    print("ACCEPTANCE PASS (main caliber):", pass_m)
    print("== sealed caliber (full n=25, alongside) ==")
    print(f"ours mean {head_f['ours_mean']} | master mean {head_f['master_mean']} | pair diff {head_f['pair_diff']:+.3f} (SE {head_f['SE']:.3f}) | W/T/L {head_f['W/T/L']} | PASS:", pass_f)
    print("segments:", json.dumps(segments, ensure_ascii=False))
    print("per_tradition:", json.dumps(per_trad, ensure_ascii=False))
    print(f"max |view diff|: ours {max_o} | master {max_m} | disputes ours {out['disputes_ours']} master {out['disputes_master']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
