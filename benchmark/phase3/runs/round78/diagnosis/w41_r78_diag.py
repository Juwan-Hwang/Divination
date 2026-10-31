#!/usr/bin/env python3
"""W41 R78 diagnostic recomputation. Reads only permitted inputs."""
import json, math, statistics, pathlib

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
neg = json.loads((BASE/"runs/round78/diagnosis/lr-negatives-dev78.json").read_text())
fs = json.loads((BASE/"runs/round78/final-scores.json").read_text())
mb9 = json.loads((BASE/"data/master-baseline-dev9.json").read_text())
mb8 = json.loads((BASE/"data/master-baseline-dev8.json").read_text())

print("final-scores top keys:", list(fs.keys()))
for k in fs:
    if "analysis" in k or "r78" in k or "segment" in k.lower():
        print("KEY", k, json.dumps(fs[k], ensure_ascii=False)[:4000])
print("mb9 type", type(mb9), list(mb9.keys())[:20] if isinstance(mb9, dict) else len(mb9))
print("mb8 type", type(mb8), list(mb8.keys())[:20] if isinstance(mb8, dict) else len(mb8))
# dump small structures
def peek(d, name):
    print(name, "n_keys=", len(d), "sample=", {k: d[k] for k in list(d)[:2]})
peek(mb9, "mb9")
peek(mb8, "mb8")

negs = neg["negatives"]
print("n_liuren_total", neg["n_liuren_total"], "n_negative", neg["n_negative"], "listed", len(negs))
ok=0
for e in negs:
    if abs((e["ours"]-e["master"])-e["pair_diff"])<1e-9: ok+=1
    else: print("pair mismatch", e)
print("pair_diff self-consistent", ok, "/", len(negs))

# ours vs final-scores ours_axis2 / ours_sub
oa = fs.get("ours_axis2", {}); osub = fs.get("ours_sub", {})
ok2=ok3=0
for e in negs:
    cid=e["case_id"]
    if cid in oa and abs(oa[cid]-e["ours"])<1e-9: ok2+=1
    else: print("ours_axis2 mismatch/missing", cid, oa.get(cid), e["ours"])
    if cid in osub and abs(osub[cid]["total"]-e["ours"])<1e-9: ok3+=1
    else: print("ours_sub mismatch/missing", cid)
print("ours vs ours_axis2", ok2, "vs ours_sub.total", ok3)

# master baseline lookup: try to find per-case totals
def find_master(mb, cid):
    # search recursively for dict containing cid with numeric or total
    hits=[]
    def rec(o, path):
        if isinstance(o, dict):
            if cid in o:
                hits.append((path, o[cid]))
            for k,v in o.items(): rec(v, path+"/"+str(k))
        elif isinstance(o, list):
            for i,v in enumerate(o): rec(v, path+f"[{i}]")
    rec(mb, "")
    return hits
for cid in [negs[0]["case_id"], "LR3-010", "OC-027"]:
    print("master9", cid, mb9.get(cid))
    print("master8", cid, mb8.get(cid))
# verify all negatives master vs mb9 total, and dev8 subset vs mb8
ok9=sum(1 for e in negs if abs(mb9[e["case_id"]]["total"]-e["master"])<1e-9)
print("neg master vs mb9.total", ok9, "/", len(negs))
diff8=[e["case_id"] for e in negs if e["case_id"] in mb8 and abs(mb8[e["case_id"]]["total"]-e["master"])>1e-9]
print("neg master vs mb8 differing ids (where present):", diff8)
print("negs present in mb8:", sum(1 for e in negs if e["case_id"] in mb8), "absent:", [e["case_id"] for e in negs if e["case_id"] not in mb8])

for seg_name, filt in [("dev8", lambda e: e["in_dev8"]), ("LR3", lambda e: not e["in_dev8"]), ("combined", lambda e: True)]:
    sub=[e for e in negs if filt(e)]
    diffs=sorted(e["pair_diff"] for e in sub)
    print(seg_name, "n_neg=", len(sub), "sum=", round(sum(diffs),4), "mean_neg=", round(statistics.mean(diffs),4), "median_neg=", statistics.median(diffs), "diffs=", diffs)
    print("  ids=", [e["case_id"] for e in sub])

CODING = {
 "LR2-013":("D",""), "LR2-014":("W*","W-face, interface; W<->C interface"),
 "LR2-015":("E","same-sign exclusion; W note only"), "LR2-016":("D","W<->magnitude interface note only"),
 "LR2-019":("E",""), "LR2-021":("A*","MW/SEAT; A<->B interface"),
 "LR2-022":("W*","W-face, interface; W<->A interface"), "LR2-023":("W*","W-face, interface; W<->D/E interface"),
 "LR2-024":("C*",""),
 "LR3-002":("E","A secondary candidate GZ/SEAT"), "LR3-006":("C*",""), "LR3-008":("D",""),
 "LR3-010":("UNC","no prior coding in h16 s2.1; not coded this round"),
 "LR3-101":("W*","W-face, interface; W<->A/C interface"), "LR3-104":("E",""),
 "LR3-107":("A","SF/SEAT"), "LR3-112":("H","W not measurable"), "LR3-114":("C*",""), "LR3-116":("A","QX/SEAT"),
 "OC-026":("E","same-sign exclusion note"), "OC-027":("W*","W-name, interface; W<->C interface"),
 "OC-029":("E","A secondary candidate MW/MIX"), "OC-030":("A","SF/SEAT"),
}
from collections import Counter
for seg_name, filt in [("dev8", lambda e: e["in_dev8"]), ("LR3", lambda e: not e["in_dev8"]), ("combined", lambda e: True)]:
    sub=[e for e in negs if filt(e)]
    c=Counter(CODING[e["case_id"]][0].rstrip("*") for e in sub)
    n=len(sub); coded=n-c.get("UNC",0)
    w=c.get("W",0)
    def se(p,nn): return round(100*math.sqrt(p*(1-p)/nn),1) if nn and 0<p<1 else 0.0
    print(seg_name, "dist=", dict(sorted(c.items())), "n=", n, "coded=", coded,
          "W_negdenom=", f"{w}/{n}={100*w/n:.1f}% SE {se(w/n,n)}pp",
          "W_codeddenom=", f"{w}/{coded}={100*w/coded:.1f}% SE {se(w/coded,coded)}pp",
          "hardcore=0")
# full liuren segment means using final-scores ours + mb9 if discoverable later in script output
