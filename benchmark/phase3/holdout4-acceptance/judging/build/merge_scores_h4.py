#!/usr/bin/env python3
"""holdout4 acceptance score merger + paired stats (host tooling).

Usage: python3 merge_scores_h4.py
Expects judging/judgeA.jsonl and judgeB.jsonl (each covering all 50 anon
ids). First pass writes judging/disputes.json (anon ids where
|(claims+timing) A-B| >= 2 or pass differs) and exits; after
judging/arbitration.jsonl exists, writes holdout4-acceptance/final-scores.json
with per-case ours/master scores, paired stats (ALL / LOW / HIGH) and the
three acceptance-criteria booleans.
"""
import json
import os
import pathlib

BASE = pathlib.Path(__file__).resolve().parents[3]  # benchmark/phase3
ACC = BASE / "holdout4-acceptance"
JD = ACC / "judging"


def load_jsonl(p):
    d = {}
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                d[r["anon_id"]] = r
    return d


def agg(rows):
    """rows: list of (ours_sub, master_sub) dicts."""
    n = len(rows)
    if not n:
        return None
    ours = [o["total"] for o, _ in rows]
    mst = [m["total"] for _, m in rows]
    pair = [o - m for o, m in zip(ours, mst)]
    w = sum(1 for x in pair if x > 0)
    t = sum(1 for x in pair if x == 0)
    l = sum(1 for x in pair if x < 0)

    def sub(idx, key):
        return round(sum(r[idx][key] for r in rows) / n, 3)

    return {
        "n": n,
        "ours_mean": round(sum(ours) / n, 3),
        "master_mean": round(sum(mst) / n, 3),
        "pair_diff": round(sum(pair) / n, 3),
        "W/T/L": f"{w}/{t}/{l}",
        "ours_pass": sum(1 for v in ours if v >= 4),
        "master_pass": sum(1 for v in mst if v >= 4),
        "ours_sub": {k: sub(0, k) for k in ("direction", "claims", "timing")},
        "master_sub": {k: sub(1, k) for k in ("direction", "claims", "timing")},
    }


def main():
    mapping = json.load(open(JD / "host-mapping.json", encoding="utf-8"))
    meta = json.load(open(JD / "packet-meta.json", encoding="utf-8"))
    A = load_jsonl(JD / "judgeA.jsonl")
    B = load_jsonl(JD / "judgeB.jsonl")
    ARB = load_jsonl(JD / "arbitration.jsonl")
    assert set(A) == set(mapping), f"judgeA coverage {len(A)} != {len(mapping)}"
    assert set(B) == set(mapping), f"judgeB coverage {len(B)} != {len(mapping)}"

    disputes, final = [], {}
    for anon in mapping:
        a, b = A[anon], B[anon]
        need = abs((a["claims"] + a["timing"]) - (b["claims"] + b["timing"])) >= 2 or a["pass"] != b["pass"]
        if need and anon not in ARB:
            disputes.append(anon)
            continue
        if anon in ARB:
            r = ARB[anon]
            final[anon] = {k: float(r[k]) for k in ("direction", "claims", "timing", "total")}
        else:
            final[anon] = {k: (a[k] + b[k]) / 2 for k in ("direction", "claims", "timing", "total")}
    if disputes:
        json.dump(disputes, open(JD / "disputes.json", "w"))
        print("DISPUTES needing arbitration:", len(disputes))
        return

    per_case = {}
    for anon, m in mapping.items():
        per_case.setdefault(m["case_id"], {})[m["source"]] = final[anon]
    rows_all, rows_by_cont = [], {}
    for cid, d in sorted(per_case.items()):
        rows_all.append((d["ours"], d["master"]))
        cont = meta[next(a for a, m in mapping.items() if m["case_id"] == cid)]["contamination"]
        rows_by_cont.setdefault(cont, []).append((d["ours"], d["master"]))

    stats = {"ALL": agg(rows_all)}
    for cont in ("low", "high"):
        stats[cont.upper()] = agg(rows_by_cont.get(cont, []))
    low = stats["LOW"] or stats["ALL"]
    stats["criteria"] = {
        "i_all_ours_mean_gt_master": stats["ALL"]["ours_mean"] > stats["ALL"]["master_mean"],
        "ii_low_wins_gt_losses": int(low["W/T/L"].split("/")[0]) > int(low["W/T/L"].split("/")[2]),
        "iii_low_pair_diff_positive": low["pair_diff"] > 0,
    }
    stats["criteria"]["PASS_ALL"] = all(stats["criteria"].values())
    json.dump({"per_case": per_case, "stats": stats},
              open(ACC / "final-scores.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(json.dumps(stats, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
