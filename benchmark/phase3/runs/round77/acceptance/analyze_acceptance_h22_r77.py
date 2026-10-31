#!/usr/bin/env python3
"""holdout22 acceptance analysis (analysis role only). Adapted from the
holdout21 analyzer (analyze_acceptance_h21_r60.py) for R77 PREREG s.2.

Calibers (R77 PREREG s.2): the set is all-low (27/27, gold field
`pollution`, seal log data/holdout22-seal-log.md) and has NO known
pollution-caliber conflict case, so MAIN caliber == sealed caliber ==
all 27 cases. The three criteria are judged on this single caliber.

Merge rule (standing): per side (ours / master), final = mean of the
two judge views; |v1.total - v2.total| >= 3 cases are replaced by the
arbitration score. If disputes exist and no arbitration file covers
exactly those cases, this script exits 2 (unresolved-dispute error).

Criteria per R77 PREREG s.2 (照 R42 PREREG s.8, literal):
(i) ours mean > master mean; (ii) paired wins > losses on the
low-pollution subset; (iii) paired diff > 0 on the low-pollution
subset. diff/SE reported descriptively; the h17-style diff/SE >= 1
side condition is registered as a side note only, not a gate.

CZ-QX: this set HAS 4 cezi cases (ZCB-001/002/004/005); per R77
PREREG s.2 their segment read is registered as an acceptance segment
only and does NOT settle the CZ-QX same-tier count, which stays 16
(settled at R76 from zicibu mining). Registered only.

Outputs: judging/final-scores.json + stdout.
"""
import json
import math
import sys
from collections import Counter
from pathlib import Path

ACC = Path(__file__).resolve().parent
JD = ACC / "judging"
GOLD = ACC.parents[2] / "holdout22" / "test_gold.jsonl"
N = 27
MID_OVERRIDE = {}  # no conflict case in holdout22 (R77 PREREG s.2)


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
    contam_sealed = Counter(r["pollution"] for r in gold_rows)
    grades = Counter(r["grade"] for r in gold_rows)
    trad_of = {r["id"]: r["tradition"] for r in gold_rows}
    # Main caliber: sealed low minus host-ruled mid override.
    main_low_ids = sorted(r["id"] for r in gold_rows
                          if r["pollution"] == "low"
                          and MID_OVERRIDE.get(r["id"]) != "mid")
    sealed_low_ids = sorted(r["id"] for r in gold_rows
                            if r["pollution"] == "low")
    low_info = {
        "gold_file": "benchmark/phase3/holdout22/test_gold.jsonl",
        "contamination_field": "pollution",
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
        "bazi_DS": [c for c in ids if c.startswith("DS-")],
        "qimen_QM": [c for c in ids if c.startswith("QM-")],
        "cezi_ZCB": [c for c in ids if c.startswith("ZCB-")],
        "liuyao_GSZ": [c for c in ids if c.startswith("GSZ-")],
        "non_liuyao": [c for c in ids if not c.startswith("GSZ-")],
    }
    assert len(groups["bazi_DS"]) == 9, len(groups["bazi_DS"])
    assert len(groups["qimen_QM"]) == 10, len(groups["qimen_QM"])
    assert len(groups["cezi_ZCB"]) == 4, len(groups["cezi_ZCB"])
    assert len(groups["liuyao_GSZ"]) == 4, len(groups["liuyao_GSZ"])
    assert len(groups["non_liuyao"]) == 23, len(groups["non_liuyao"])
    segments = {k: seg(v, ours, master) for k, v in groups.items() if v}
    per_trad = {}
    for tr in sorted(set(trad_of.values())):
        per_trad[tr] = seg([c for c in ids if trad_of[c] == tr], ours, master)

    czqx = {"settled": False,
            "note": "holdout22 contains 4 cezi cases; per R77 PREREG s.2 the cezi segment read is registered as an acceptance segment only, CZ-QX same-tier count stays 16 (settled at R76)."}

    out = {"ours": ours, "master": master,
           "main_caliber_low27": {**head_m, "criteria": crit_m, "PASS": pass_m},
           "sealed_caliber_full27": {**head_f, "criteria": crit_f, "PASS": pass_f},
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
    print("== main caliber (low n=27, no exclusions) ==")
    print(f"sealed contamination counts: {dict(contam_sealed)} | grades: {dict(grades)}")
    print(f"ours mean {head_m['ours_mean']} | master mean {head_m['master_mean']}")
    print(f"pair diff {head_m['pair_diff']:+.3f} (SE {head_m['SE']:.3f}) | W/T/L {head_m['W/T/L']}")
    for k, v in crit_m.items():
        print(k, "->", v)
    print("ACCEPTANCE PASS (main caliber):", pass_m)
    print("== sealed caliber (full n=27, alongside) ==")
    print(f"ours mean {head_f['ours_mean']} | master mean {head_f['master_mean']} | pair diff {head_f['pair_diff']:+.3f} (SE {head_f['SE']:.3f}) | W/T/L {head_f['W/T/L']} | PASS:", pass_f)
    print("segments:", json.dumps(segments, ensure_ascii=False))
    print("per_tradition:", json.dumps(per_trad, ensure_ascii=False))
    print(f"max |view diff|: ours {max_o} | master {max_m} | disputes ours {out['disputes_ours']} master {out['disputes_master']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
