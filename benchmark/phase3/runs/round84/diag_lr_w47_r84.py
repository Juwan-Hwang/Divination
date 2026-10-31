#!/usr/bin/env python3
"""W47 R84 liuren weight diagnosis recomputation. Only reads listed files, per-id exact opens."""
import json, math, statistics
from pathlib import Path
BASE = Path("/home/hatch/workspace/divination/benchmark/phase3")
NEG = BASE/"runs/round84/diagnosis/lr-negatives-dev84.json"
FIN = BASE/"runs/round84/final-scores.json"
OUT = BASE/"runs/round84/diagnosis/w47_r84_diag_out.txt"
neg = json.loads(NEG.read_text())
fin = json.loads(FIN.read_text())
ana = fin["analysis_r84"]["families"]
rows = neg["negatives"]
lines = []
def p(s=""):
    lines.append(str(s))
p(f"n_liuren_total={neg['n_liuren_total']} n_negative={neg['n_negative']} rows={len(rows)}")
for k in ("liuren_dev8","liuren_lr3_new","liuren_merged"):
    v = ana[k]
    p(f"SEG {k}: n={v['n']} diff={v['pair_diff']} SE={v['SE']} ours={v['ours_mean']} master={v['master_mean']} WTL={v['W/T/L']}")
# self-consistency
bad_diff = [r["case_id"] for r in rows if abs((r["ours"]-r["master"])-r["pair_diff"])>1e-9]
bad_axis = [r["case_id"] for r in rows if fin["ours_axis2"].get(r["case_id"]) != r["ours"]]
bad_sub = [r["case_id"] for r in rows if fin["ours_sub"].get(r["case_id"],{}).get("total") != r["ours"]]
p(f"pair_diff_selfconsistent: {len(rows)-len(bad_diff)}/{len(rows)} bad={bad_diff}")
p(f"ours_vs_axis2: {len(rows)-len(bad_axis)}/{len(rows)} bad={bad_axis}")
p(f"ours_vs_subtotal: {len(rows)-len(bad_sub)}/{len(rows)} bad={bad_sub}")
CODING = {
 "LR-001":("UNC","no prior coding in h16 s2.1; not coded this round"),
 "LR2-013":("D",""), "LR2-014":("W*","W-face, interface; W<->C interface"),
 "LR2-015":("E","same-sign exclusion; W note only"), "LR2-016":("D","W<->magnitude interface note only"),
 "LR2-017":("E",""), "LR2-019":("E",""),
 "LR2-021":("A*","MW/SEAT; A<->B interface"), "LR2-022":("W*","W-face, interface; W<->A interface"),
 "LR2-023":("W*","W-face, interface; W<->D/E interface"), "LR2-024":("C*",""),
 "LR3-002":("E","A secondary candidate GZ/SEAT"), "LR3-004":("W","W-face, hard-core"),
 "LR3-006":("C*",""), "LR3-008":("D",""), "LR3-010":("UNC","no prior coding in h16 s2.1; not coded this round"),
 "LR3-101":("W*","W-face, interface; W<->A/C interface"), "LR3-107":("A","SF/SEAT"),
 "LR3-112":("H","W not measurable"), "LR3-114":("C*",""), "LR3-116":("A","QX/SEAT"),
 "OC-026":("E","same-sign exclusion note"), "OC-027":("W*","W-name, interface; W<->C interface"),
 "OC-029":("E","A secondary candidate MW/MIX"), "OC-030":("A","SF/SEAT"),
}
def seg(r): return "dev8" if r["in_dev8"] else "LR3"
for s in ("dev8","LR3","merged"):
    sub = rows if s=="merged" else [r for r in rows if seg(r)==s]
    diffs=[r["pair_diff"] for r in sub]
    p(f"NEGSUB {s}: n={len(sub)} sum={sum(diffs):.2f} mean={statistics.mean(diffs):.3f} median={statistics.median(diffs):.2f}")
    from collections import Counter
    p(f"  main_labels={dict(Counter(CODING[r['case_id']][0] for r in sub))}")
    coded=[r for r in sub if CODING[r['case_id']][0]!="UNC"]
    p(f"  coded_n={len(coded)} unc={[r['case_id'] for r in sub if CODING[r['case_id']][0]=='UNC']}")
    w_int=sum(1 for r in sub if CODING[r['case_id']][0] in ("W","W*"))
    w_hard=sum(1 for r in sub if CODING[r['case_id']][0]=="W")
    for denom,label in ((len(sub),"neg"),(len(coded),"coded")):
        if denom:
            for cnt,name in ((w_int,"W_interface"),(w_hard,"W_hard")):
                pr=cnt/denom; se=math.sqrt(pr*(1-pr)/denom)*100 if denom else 0
                p(f"  {name} {label}_denom: {cnt}/{denom}={pr*100:.1f}% SE={se:.1f}pp")
    p(f"  W_face={sum(1 for r in sub if 'W-face' in CODING[r['case_id']][1] or CODING[r['case_id']][0]=='W')} W_name={sum(1 for r in sub if 'W-name' in CODING[r['case_id']][1])}")
# book provenance per-id exact open
from collections import Counter
books={}
for r in rows:
    cid=r["case_id"]
    card=json.loads((BASE/f"inputs-dev12/{cid}.json").read_text())
    prov=card.get("provenance") or {}
    book=prov.get("book") if isinstance(prov,dict) else None
    books[cid]=book
    p(f"BOOK {cid} | {seg(r)} | diff={r['pair_diff']} | label={CODING[cid][0]} | {CODING[cid][1]} | {book}")
def fam(b):
    if b is None: return "pending"
    return "guide" if "大六壬占验指南" in b else "non-guide"
for s in ("dev8","LR3","merged"):
    sub = rows if s=="merged" else [r for r in rows if seg(r)==s]
    p(f"FAMILY {s}: {dict(Counter(fam(books[r['case_id']]) for r in sub))}")
OUT.write_text("\n".join(lines)+"\n")
print("\n".join(lines))
print("OUT", OUT)
