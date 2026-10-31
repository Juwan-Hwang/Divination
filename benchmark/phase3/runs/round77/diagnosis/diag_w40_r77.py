#!/usr/bin/env python3
"""R77 W-monitoring round 40 diagnostic seat script (unique to this seat).
Reads only: lr-negatives-dev77.json in this dir + per-case inputs-dev12/<id>.json
Coding transcribed from DIAG-LR-fresh-h16 s2.1 via DIAG-LR-weight-dev76.md s2.
No directory listing/counting of any runs/ dir."""
import json, math, pathlib

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
NEG = BASE / "runs/round77/diagnosis/lr-negatives-dev77.json"
INP = BASE / "inputs-dev12"

# case_id -> (main_label, note)  * = interface/ambiguous ; UNC = no prior coding
CODING = {
 "LR2-013": ("D", "—"),
 "LR2-014": ("W*", "W-face, interface; W<->C interface"),
 "LR2-015": ("E", "same-sign exclusion; W note only"),
 "LR2-016": ("D", "W<->magnitude interface note only"),
 "LR2-017": ("E", "—"),
 "LR2-018": ("D", "—"),
 "LR2-019": ("E", "—"),
 "LR2-021": ("A*", "MW/SEAT; A<->B interface"),
 "LR2-022": ("W*", "W-face, interface; W<->A interface"),
 "LR2-023": ("W*", "W-face, interface; W<->D/E interface"),
 "LR2-024": ("C*", "—"),
 "LR3-002": ("E", "A secondary candidate GZ/SEAT"),
 "LR3-006": ("C*", "—"),
 "LR3-008": ("D", "—"),
 "LR3-010": ("UNC", "no prior coding in h16 s2.1; not coded this round"),
 "LR3-101": ("W*", "W-face, interface; W<->A/C interface"),
 "LR3-107": ("A", "SF/SEAT"),
 "LR3-112": ("H", "W not measurable"),
 "LR3-116": ("A", "QX/SEAT"),
 "OC-026": ("E", "same-sign exclusion note"),
 "OC-027": ("W*", "W-name, interface; W<->C interface"),
 "OC-029": ("E", "A secondary candidate MW/MIX"),
 "OC-030": ("A", "SF/SEAT"),
}

def se(p, n):
    return math.sqrt(p*(1-p)/n)*100 if n else 0.0

def main():
    data = json.loads(NEG.read_text(encoding="utf-8"))
    negs = data["negatives"]
    print(f"round={data['round']} n_liuren_total={data['n_liuren_total']} n_negative={data['n_negative']} listed={len(negs)}")
    rows = []
    for e in negs:
        cid = e["case_id"]
        assert abs((e["ours"]-e["master"]) - e["pair_diff"]) < 1e-9, cid
        p = INP / f"{cid}.json"
        obj = json.loads(p.read_text(encoding="utf-8"))
        book = obj.get("provenance", {}).get("book", "")
        fam = "guide" if "大六壬占验指南" in book else ("pending" if not book else "non-guide")
        seg = "dev8" if e["in_dev8"] else "LR3"
        label, note = CODING[cid]
        rows.append({**e, "book": book, "family": fam, "seg": seg, "label": label, "note": note})
        print(f"{cid} seg={seg} diff={e['pair_diff']:+.2f} label={label} fam={fam} book={book} | {note}")
    for segname, subset in [("dev8", [r for r in rows if r["seg"]=="dev8"]),
                            ("LR3", [r for r in rows if r["seg"]=="LR3"]),
                            ("merged", rows)]:
        n = len(subset)
        s = sum(r["pair_diff"] for r in subset)
        print(f"\n[{segname}] n={n} pair_diff_sum={s:+.2f}")
        from collections import Counter
        c = Counter(r["label"].rstrip("*") for r in subset)
        print(" main-label counts:", dict(sorted(c.items())))
        famc = Counter(r["family"] for r in subset)
        print(" family counts:", dict(sorted(famc.items())))
        coded = [r for r in subset if r["label"] != "UNC"]
        w_int = sum(1 for r in subset if r["label"].rstrip("*") == "W")
        w_hard = 0  # all W in this subset carry * in CODING (verified below)
        w_star = sum(1 for r in subset if r["label"] == "W*")
        print(f" W interface={w_int} (all starred={w_star}) hardcore={w_hard}")
        for denom, dn in [("neg-n", n), ("coded-n", len(coded))]:
            p = w_int/dn if dn else 0
            print(f"  W interface share /{denom}({dn}) = {w_int}/{dn} = {p*100:.1f}% SE {se(p,dn):.1f}pp ; hardcore 0/{dn} = 0.0%")
        wface = sum(1 for r in subset if r["label"]=="W*" and "W-face" in r["note"])
        wname = sum(1 for r in subset if r["label"]=="W*" and "W-name" in r["note"])
        print(f" W subforms: face={wface} name={wname}")
        dmain = [r["case_id"] for r in subset if r["label"]=="D"]
        print(f" D main cases: {dmain}")
    unc = [r["case_id"] for r in rows if r["label"]=="UNC"]
    print(f"\nUNC cases: {unc}")
    print("pair_diff identity ours-master: OK for all listed")

if __name__ == "__main__":
    main()
