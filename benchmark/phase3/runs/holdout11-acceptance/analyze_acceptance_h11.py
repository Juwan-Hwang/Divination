#!/usr/bin/env python3
"""holdout11 acceptance analysis (analysis role only).

Merge rule (standing): per side (ours / master), final = mean of the two
judge views; |v1.total - v2.total| >= 3 cases are replaced by the arbitration
score. If disputes exist but the side's arbitration file is missing, the
script prints the dispute set and exits 2 (host dispatches arbitration,
then reruns).

Criteria per runs/round32/PREREG.md s.4 (all on the 25-case set; the
low-contamination subset equals the full set):
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


def main():
    mapping = json.loads((JD / "host-mapping.json").read_text(encoding="utf-8"))
    ours, d_o = merge_side("ours", "judgeO1.jsonl", "judgeO2.jsonl",
                           "arbitration-ours.jsonl", mapping["ours"])
    master, d_m = merge_side("master", "judgeM1.jsonl", "judgeM2.jsonl",
                             "arbitration-master.jsonl", mapping["master"])
    if ours is None or master is None:
        return 2
    ids = sorted(ours)
    assert ids == sorted(master) and len(ids) == 25
    om = sum(ours[c] for c in ids) / 25
    mm = sum(master[c] for c in ids) / 25
    diffs = [ours[c] - master[c] for c in ids]
    dmean = sum(diffs) / 25
    se = math.sqrt(sum((x - dmean) ** 2 for x in diffs) / 24) / math.sqrt(25)
    w = sum(1 for x in diffs if x > 0)
    t = sum(1 for x in diffs if x == 0)
    l = 25 - w - t
    crit = {
        "(i) ours_mean > master_mean": om > mm,
        "(ii) paired W > L": w > l,
        "(iii) diff > 0 and diff/SE >= 1": dmean > 0 and (dmean / se if se > 0 else float("inf")) >= 1,
    }
    out = {"ours": ours, "master": master,
           "ours_mean": round(om, 3), "master_mean": round(mm, 3),
           "pair_diff": round(dmean, 3), "pair_SE": round(se, 3),
           "diff_over_SE": round(dmean / se, 3) if se > 0 else None,
           "W/T/L": f"{w}/{t}/{l}", "criteria": crit,
           "PASS": all(crit.values()),
           "disputes_ours": [mapping["ours"][a] for a in d_o],
           "disputes_master": [mapping["master"][a] for a in d_m],
           "per_case": {c: {"ours": ours[c], "master": master[c],
                            "diff": round(ours[c] - master[c], 3)} for c in ids}}
    with open(JD / "final-scores.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print(f"ours mean {om:.3f} | master mean {mm:.3f}")
    print(f"pair diff {dmean:+.3f} (SE {se:.3f}, diff/SE {dmean / se:.3f}) | W/T/L {w}/{t}/{l}")
    for k, v in crit.items():
        print(k, "->", v)
    print("ACCEPTANCE PASS:", all(crit.values()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
