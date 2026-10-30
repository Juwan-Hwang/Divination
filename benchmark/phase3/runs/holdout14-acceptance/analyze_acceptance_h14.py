#!/usr/bin/env python3
"""holdout14 acceptance analysis (analysis role only). Mirror of the
holdout13 analyzer with the R36 PREREG s.3 layered reporting for the
two high-contamination exceptions (PU-003/PU-008):

- Main caliber = low-contamination 38 cases (PU pair excluded); the
  three acceptance criteria are judged on the main caliber and also
  reported on the full 40 alongside.
- PU-003/PU-008 reported as a separate annex segment only.

Merge rule (standing): per side (ours / master), final = mean of the two
judge views; |v1.total - v2.total| >= 3 cases are replaced by the
arbitration score. Missing arbitration with pending disputes exits 2.

Criteria per runs/round36/PREREG.md s.3:
(i) ours mean > master mean; (ii) paired wins > losses;
(iii) paired diff > 0 and diff/SE >= 1.
Outputs: judging/final-scores.json + stdout.
"""
import json
import math
import sys
from pathlib import Path

ACC = Path(__file__).resolve().parent
JD = ACC / "judging"
N = 40
EXCEPTIONS = {"PU-003", "PU-008"}


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
        return None, disputes
    assert set(arb) == set(disputes), (label, sorted(arb), disputes)
    final = {}
    for a, cid in mapping_side.items():
        if a in arb:
            final[cid] = float(arb[a]["total"])
        else:
            final[cid] = (v1[a]["total"] + v2[a]["total"]) / 2
    return final, disputes


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
    ours, d_o = merge_side("ours", "judgeO1.jsonl", "judgeO2.jsonl",
                           "arbitration-ours.jsonl", mapping["ours"])
    master, d_m = merge_side("master", "judgeM1.jsonl", "judgeM2.jsonl",
                             "arbitration-master.jsonl", mapping["master"])
    if ours is None or master is None:
        return 2
    ids = sorted(ours)
    assert ids == sorted(master) and len(ids) == N
    main_ids = [c for c in ids if c not in EXCEPTIONS]
    assert len(main_ids) == 38
    head_m, crit_m, pass_m = criteria(main_ids, ours, master)
    head_f, crit_f, pass_f = criteria(ids, ours, master)
    groups = {
        "liuren-DA": [c for c in ids if c.startswith("DA-")],
        "liuren-BY": [c for c in ids if c.startswith("BY-")],
        "liuren-CY": [c for c in ids if c.startswith("CY-")],
        "liuren-all16": [c for c in ids if c.split("-")[0] in ("DA", "BY", "CY")],
        "liuyao-BQ": [c for c in ids if c.startswith("BQ-")],
        "cezi-CZ": [c for c in ids if c.startswith("CZ-")],
        "bazi-PU-exceptions": [c for c in ids if c in EXCEPTIONS],
    }
    segments = {k: seg(v, ours, master) for k, v in groups.items() if v}
    out = {"ours": ours, "master": master,
           "main_caliber_low38": {**head_m, "criteria": crit_m, "PASS": pass_m},
           "full40": {**head_f, "criteria": crit_f, "PASS": pass_f},
           "segments": segments,
           "disputes_ours": [mapping["ours"][a] for a in d_o],
           "disputes_master": [mapping["master"][a] for a in d_m],
           "per_case": {c: {"ours": ours[c], "master": master[c],
                            "diff": round(ours[c] - master[c], 3)} for c in ids}}
    with open(JD / "final-scores.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print("== main caliber (low 38) ==")
    print(f"ours mean {head_m['ours_mean']} | master mean {head_m['master_mean']}")
    print(f"pair diff {head_m['pair_diff']:+.3f} (SE {head_m['SE']:.3f}) | W/T/L {head_m['W/T/L']}")
    for k, v in crit_m.items():
        print(k, "->", v)
    print("ACCEPTANCE PASS (main caliber):", pass_m)
    print("== full 40 (alongside) ==")
    print(f"ours mean {head_f['ours_mean']} | master mean {head_f['master_mean']} | pair diff {head_f['pair_diff']:+.3f} (SE {head_f['SE']:.3f}) | W/T/L {head_f['W/T/L']} | PASS:", pass_f)
    print("segments:", json.dumps(segments, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
