#!/usr/bin/env python3
"""R36 DIAG-BZ-fresh reproduction/digest script (diagnosis role only).

Reads only opened data: holdout12/13 acceptance predictions+judging+
final-scores, holdout12/13 test_gold, holdout12/13 input cards,
runs/round35/final-scores.json, runs/round35/judging/host-meta.json,
data/master-baseline-dev9.json. Dev two-segment split replicates
runs/round34/analyze_r34.py by_trad verbatim: 'bazi' -> BZ 29,
'八字' -> natal 26 (disjoint).
Outputs: stdout stats + diag_bz_fresh_r36_digest.txt in this dir.
No method files touched; no git operations.
"""
import json, math
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
P3 = HERE.parents[2]  # benchmark/phase3

QL12 = [f"QL-{i:03d}" for i in range(1, 9)]
NL12 = ["NL-001", "NL-002", "NL-005", "NL-031", "NL-043"]
QL13 = ["QL-013", "QL-014", "QL-023", "QL-025", "QL-026", "QL-027",
        "QL-030", "QL-031", "QL-032", "QL-035"]
NL13 = ["NL-006", "NL-049"]
FRESH = ([("h12", c) for c in QL12 + NL12]
         + [("h13", c) for c in QL13 + NL13])


def mean_se(vals):
    n = len(vals)
    m = sum(vals) / n
    se = (math.sqrt(sum((x - m) ** 2 for x in vals) / (n - 1))
          / math.sqrt(n)) if n > 1 else 0.0
    return m, se


def load_jsonl(path):
    out = {}
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if line:
            r = json.loads(line)
            out[r["anon_id"]] = r
    return out


def merged_subscores(acc_dir):
    """Double-judge mean per dimension; disputes must be empty (verified
    against final-scores disputes lists by caller)."""
    jd = P3 / "runs" / acc_dir / "judging"
    hmap = json.loads((jd / "host-mapping.json").read_text(encoding="utf-8"))
    res = {}
    for side, f1, f2 in (("ours", "judgeO1.jsonl", "judgeO2.jsonl"),
                         ("master", "judgeM1.jsonl", "judgeM2.jsonl")):
        v1, v2 = load_jsonl(jd / f1), load_jsonl(jd / f2)
        inv = {cid: anon for anon, cid in hmap[side].items()}
        disputes = [c for c in inv
                    if abs(v1[inv[c]]["total"] - v2[inv[c]]["total"]) >= 3]
        assert not disputes, (acc_dir, side, disputes)
        sub, reasons = {}, {}
        for cid, anon in inv.items():
            a, b = v1[anon], v2[anon]
            sub[cid] = {k: (float(a[k]) + float(b[k])) / 2
                        for k in ("direction", "claims", "timing", "total")}
            reasons[cid] = (a.get("reason", ""), b.get("reason", ""))
        res[side] = sub
        res[side + "_reasons"] = reasons
    return res


def main():
    gold, pred, inp = {}, {}, {}
    for hset, gold_dir, inp_dir in (
            ("h12", "holdout12", "holdout12-inputs"),
            ("h13", "holdout13", "holdout13-inputs")):
        for line in open(P3 / gold_dir / "test_gold.jsonl", encoding="utf-8"):
            r = json.loads(line)
            gold[(hset, r["id"])] = r
        acc = "holdout12-acceptance" if hset == "h12" else "holdout13-acceptance"
        for _, cid in [x for x in FRESH if x[0] == hset]:
            pred[(hset, cid)] = json.loads(
                (P3 / "runs" / acc / "predictions" / f"{cid}.json")
                .read_text(encoding="utf-8"))
            ipath = P3 / inp_dir / f"{cid}.json"
            inp[(hset, cid)] = (json.loads(ipath.read_text(encoding="utf-8"))
                                if ipath.exists() else None)

    subs, finals = {}, {}
    for hset, acc in (("h12", "holdout12-acceptance"),
                      ("h13", "holdout13-acceptance")):
        subs[hset] = merged_subscores(acc)
        finals[hset] = json.loads(
            (P3 / "runs" / acc / "judging/final-scores.json")
            .read_text(encoding="utf-8"))
        # cross-check merged totals vs final-scores
        for cid in finals[hset]["ours"]:
            assert abs(subs[hset]["ours"][cid]["total"]
                       - finals[hset]["ours"][cid]) < 1e-9, (hset, cid)
            assert abs(subs[hset]["master"][cid]["total"]
                       - finals[hset]["master"][cid]) < 1e-9, (hset, cid)
    print("subscore merge cross-check vs final-scores: OK (49+40 cases)")

    # ---------- fresh stats ----------
    def fresh_rows(keys):
        return [(k, subs[k[0]]["ours"][k[1]], subs[k[0]]["master"][k[1]])
                for k in keys]

    def seg_stats(keys):
        rows = fresh_rows(keys)
        diffs = [o["total"] - m["total"] for _, o, m in rows]
        dm, dse = mean_se(diffs)
        out = {"n": len(rows), "pair_diff": round(dm, 3), "SE": round(dse, 3)}
        for dim in ("direction", "claims", "timing", "total"):
            om, ose = mean_se([o[dim] for _, o, _ in rows])
            mm, mse = mean_se([m[dim] for _, _, m in rows])
            gm, gse = mean_se([o[dim] - m[dim] for _, o, m in rows])
            out[dim] = {"ours": round(om, 3), "ours_SE": round(ose, 3),
                        "master": round(mm, 3), "master_SE": round(mse, 3),
                        "gap": round(gm, 3), "gap_SE": round(gse, 3)}
        return out

    groups = {
        "QL12": [("h12", c) for c in QL12], "NL12": [("h12", c) for c in NL12],
        "QL13": [("h13", c) for c in QL13], "NL13": [("h13", c) for c in NL13],
        "QL_all": [("h12", c) for c in QL12] + [("h13", c) for c in QL13],
        "NL_all": [("h12", c) for c in NL12] + [("h13", c) for c in NL13],
        "fresh25": FRESH,
    }
    print("\n== fresh subscore segments ==")
    for name, keys in groups.items():
        print(name, json.dumps(seg_stats(keys), ensure_ascii=False))

    print("\n== fresh composition ==")
    print("master works:", Counter(gold[k]["source_work"] for k in FRESH))
    print("masters:", Counter(gold[k]["master"] for k in FRESH))
    print("outcome_grade:", Counter(gold[k]["outcome_grade"] for k in FRESH))
    print("contamination:", Counter(gold[k]["contamination"] for k in FRESH))
    print("grade_final:", Counter(
        (gold[k].get("review") or {}).get("grade_final") for k in FRESH))
    mt = [subs[k[0]]["master"][k[1]]["total"] for k in FRESH]
    mm, mse = mean_se(mt)
    print(f"fresh master total mean {mm:.3f} SE {mse:.3f}; "
          f"<=1.25: {sum(1 for x in mt if x <= 1.25)}/25; "
          f"<=3: {sum(1 for x in mt if x <= 3)}/25; "
          f">=5: {sum(1 for x in mt if x >= 5)}/25; "
          f">=5.5: {sum(1 for x in mt if x >= 5.5)}/25")
    ot = [subs[k[0]]["ours"][k[1]]["total"] for k in FRESH]
    om, ose = mean_se(ot)
    print(f"fresh ours total mean {om:.3f} SE {ose:.3f}")
    print("question topics (fresh):")
    for k in FRESH:
        g = gold[k]
        print(" ", k, "|", g["subject"], "|", g["question_or_topic"],
              "| chart:", (g.get("chart") or {}), "| outcome_dir:",
              (g.get("outcome") or {}).get("direction"),
              "| master_dir:", [mp.get("direction")
                                 for mp in g["master_predictions"]])

    # ---------- dev stats (R35) ----------
    r35 = json.loads((P3 / "runs/round35/final-scores.json")
                     .read_text(encoding="utf-8"))
    ours35, sub35 = r35["ours_axis2"], r35["ours_sub"]
    meta = json.loads((P3 / "runs/round35/judging/host-meta.json")
                      .read_text(encoding="utf-8"))
    base = json.loads((P3 / "data/master-baseline-dev9.json")
                      .read_text(encoding="utf-8"))
    all_ids = sorted(ours35)

    def by_trad(tr):  # verbatim from analyze_r34.py
        return [c for c in all_ids if meta[c]["tradition"] == tr]

    bz, natal = by_trad("bazi"), by_trad("八字")
    assert len(bz) == 29 and len(natal) == 26 and not set(bz) & set(natal)
    print("\n== dev segments (R35 reads) ==")
    for name, ids in (("BZ29", bz), ("natal26", natal)):
        diffs = [ours35[c] - base[c]["total"] for c in ids]
        dm, dse = mean_se(diffs)
        bt = [base[c]["total"] for c in ids]
        bm, bse = mean_se(bt)
        ovm, ovse = mean_se([ours35[c] for c in ids])
        print(f"{name}: n={len(ids)} pair {dm:+.3f} SE {dse:.3f} | "
              f"ours {ovm:.3f} SE {ovse:.3f} | master {bm:.3f} SE {bse:.3f} | "
              f"contam {Counter(meta[c]['contamination'] for c in ids)} | "
              f"master<=1.25: {sum(1 for x in bt if x <= 1.25)}/{len(ids)} | "
              f"master<=3: {sum(1 for x in bt if x <= 3)}/{len(ids)} | "
              f"master>=5: {sum(1 for x in bt if x >= 5)}/{len(ids)}")
        for dim in ("direction", "claims", "timing"):
            vm, vse = mean_se([sub35[c][dim] for c in ids])
            print(f"   ours {dim}: {vm:.3f} SE {vse:.3f}")
        # low-contamination layers within each segment
        for cl in ("low", "high"):
            sub_ids = [c for c in ids if meta[c]["contamination"] == cl]
            if sub_ids:
                dd = [ours35[c] - base[c]["total"] for c in sub_ids]
                m2, s2 = mean_se(dd)
                print(f"   contam={cl}: n={len(sub_ids)} pair {m2:+.3f} "
                      f"SE {s2:.3f}")
        print("   ids:", ids)
        print("   master src:", Counter(base[c]["src"] for c in ids))
    low5 = ["MP-003", "MP-015", "MP-002", "MP-018", "OC-006"]
    print("natal low-baseline 5 in R35:",
          {c: {"ours": ours35[c], "master": base[c]["total"],
               "diff": round(ours35[c] - base[c]["total"], 3)} for c in low5})
    natal_nolow = [c for c in natal if c not in low5]
    dd = [ours35[c] - base[c]["total"] for c in natal_nolow]
    m2, s2 = mean_se(dd)
    print(f"natal26 excl low5 (only 3 of the 5 are in-segment): "
          f"n={len(natal_nolow)} pair {m2:+.3f} SE {s2:.3f}")
    in_seg_low = [c for c in natal if base[c]["total"] <= 1.25]
    print("natal26 in-segment master<=1.25:", in_seg_low)
    natal_ex3 = [c for c in natal if c not in in_seg_low]
    dd = [ours35[c] - base[c]["total"] for c in natal_ex3]
    m2, s2 = mean_se(dd)
    print(f"natal26 excl in-segment low3: n={len(natal_ex3)} "
          f"pair {m2:+.3f} SE {s2:.3f}")
    bz_low = [c for c in bz if base[c]["total"] <= 1.25]
    print("BZ29 master<=1.25:", bz_low,
          {c: base[c]["total"] for c in bz_low})
    mixed3 = ["MP-014", "MP-015", "MP-018"]
    ctrl29 = natal + mixed3
    dd = [ours35[c] - base[c]["total"] for c in ctrl29]
    m2, s2 = mean_se(dd)
    bt = [base[c]["total"] for c in ctrl29]
    bm2, bs2 = mean_se(bt)
    print(f"control29 (natal26+mixed3, R35): pair {m2:+.3f} SE {s2:.3f} | "
          f"master {bm2:.3f} SE {bs2:.3f} | master<=1.25: "
          f"{sum(1 for x in bt if x <= 1.25)}/29 | contam "
          f"{Counter(meta[c]['contamination'] for c in ctrl29)}")
    ctrl_ex5 = [c for c in ctrl29 if c not in low5]
    dd = [ours35[c] - base[c]["total"] for c in ctrl_ex5]
    m2, s2 = mean_se(dd)
    print(f"control29 excl low5: n={len(ctrl_ex5)} pair {m2:+.3f} SE {s2:.3f}")
    low6 = [c for c in bz + natal if meta[c]["contamination"] == "low"]
    dd = [ours35[c] - base[c]["total"] for c in low6]
    m2, s2 = mean_se(dd)
    bm2, bs2 = mean_se([base[c]["total"] for c in low6])
    om2, os2 = mean_se([ours35[c] for c in low6])
    print(f"dev low6 (BZ2+natal4): pair {m2:+.3f} SE {s2:.3f} | ours "
          f"{om2:.3f} SE {os2:.3f} | master {bm2:.3f} SE {bs2:.3f} | {low6}")
    for name, ids in (("BZ29", bz), ("natal26", natal)):
        hi = [c for c in ids if meta[c]["contamination"] == "high"]
        om3, os3 = mean_se([ours35[c] for c in hi])
        bm3, bs3 = mean_se([base[c]["total"] for c in hi])
        print(f"{name} high-only: n={len(hi)} ours {om3:.3f} SE {os3:.3f} "
              f"| master {bm3:.3f} SE {bs3:.3f}")
    # pair-gap decomposition dev-segment vs fresh25
    f_ours, f_master = 2.570, 5.300
    for name, ids in (("BZ29", bz), ("natal26", natal),
                      ("control29", ctrl29), ("natal_ex3", natal_ex3)):
        om3, _ = mean_se([ours35[c] for c in ids])
        bm3, _ = mean_se([base[c]["total"] for c in ids])
        gap = (om3 - bm3) - (-2.730)
        print(f"decomp {name}: pair {(om3-bm3):+.3f} vs fresh -2.730 -> "
              f"gap {gap:+.3f} = ours-side {om3-f_ours:+.3f} + "
              f"master-side {f_master-bm3:+.3f}")

    # dev question/topic listing from inputs-dev11 (topic composition)
    print("\n== dev inputs-dev11 questions ==")
    for name, ids in (("BZ29", bz), ("natal26", natal), ("mixed3", mixed3)):
        for c in ids:
            ipath = P3 / "inputs-dev11" / f"{c}.json"
            d = json.loads(ipath.read_text(encoding="utf-8"))
            ctx = d.get("context") or {}
            subj = d.get("subject") or {}
            print(f" {name} {c} | Q: {ctx.get('question')} | subj: "
                  f"{subj.get('name_or_desc')} | contam: "
                  f"{meta[c]['contamination']} | master: {base[c]['total']}")

    # ---------- digest for attribution reading ----------
    lines = []
    for k in FRESH:
        hset, cid = k
        g, p = gold[k], pred[k]
        o, m = subs[hset]["ours"][cid], subs[hset]["master"][cid]
        lines.append(f"\n{'='*100}\n### {hset} {cid} | ours {o} | master {m} "
                     f"| diff {o['total']-m['total']:+.2f}")
        lines.append(f"SUBJECT: {g['subject']} | Q: {g['question_or_topic']}")
        lines.append(f"CHART(gold): {g.get('chart')} | grade: "
                     f"{g['outcome_grade']}/{(g.get('review') or {}).get('grade_final')} "
                     f"| grade_note: {g.get('grade_note')}")
        lines.append(f"INPUT KEYS: {sorted((inp[k] or {}).keys())}")
        lines.append(f"INPUT: {json.dumps(inp[k], ensure_ascii=False)[:1500]}")
        for mp in g["master_predictions"]:
            lines.append(f"MASTER_PRED: dir={mp.get('direction')} "
                         f"timing={mp.get('timing_claim')} "
                         f"assertions={mp.get('key_assertions')}")
            lines.append(f"MASTER_TEXT: {mp.get('statement_excerpt')}")
        lines.append(f"OUTCOME: {json.dumps(g['outcome'], ensure_ascii=False)}")
        lines.append(f"OURS_PRED: {p['prediction_text']}")
        lines.append(f"OURS_BASIS: {p.get('basis')}")
        ro = subs[hset]["ours_reasons"][cid]
        rm = subs[hset]["master_reasons"][cid]
        lines.append(f"JUDGE O1: {ro[0]}\nJUDGE O2: {ro[1]}")
        lines.append(f"JUDGE M1: {rm[0]}\nJUDGE M2: {rm[1]}")
    out = HERE / "diag_bz_fresh_r36_digest.txt"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"\ndigest written: {out} ({len(lines)} blocks)")


if __name__ == "__main__":
    main()
