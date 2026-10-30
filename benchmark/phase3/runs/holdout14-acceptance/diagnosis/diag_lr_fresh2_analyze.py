#!/usr/bin/env python3
"""DIAG-LR-fresh2 aggregation: LR cases of holdout12/13/14 acceptances.
Scores: per side, mean of two judge views per component and total
(all three sets report zero disputes, so no arbitration replacement
triggers; verified against final-scores.json per case).
Attribution primary/secondary codes for h13+h14 losses were coded by
the diagnosis role from predictions+judge reasons+master packet
(earliest-divergence = primary). h12 attribution is NOT recoded here;
only its published DIAG-LR-fresh primary counts are used at family level.
Codes: A=取用误判 B=类神多义未并读 C=缺传误判 D=应期层误 E=断语具体度不足
F=方向反断 G=输入成色所致 H=其他
"""
import json, math, pathlib, collections
BASE = pathlib.Path.home()/"workspace/divination/benchmark/phase3/runs"
SETS = {"h12":"holdout12-acceptance","h13":"holdout13-acceptance","h14":"holdout14-acceptance"}
PRIMARY = {  # losses only, coded by diagnosis role
 "h13": {"BY-002":"B","BY-003":"D","BY-004":"A","BY-006":"A","CY-002":"E","CY-003":"A",
         "CY-004":"A","DA-002":"A","DA-004":"D","DA-005":"D","DA-008":"B","DA-010":"E",
         "DA-011":"A","DA-012":"A","DA-013":"C"},
 "h14": {"BY-007":"A","BY-008":"D","BY-009":"A","BY-010":"A","BY-011":"A","CY-005":"D",
         "CY-006":"D","CY-008":"H","DA-015":"B","DA-016":"B","DA-017":"D","DA-019":"A",
         "DA-020":"A","DA-021":"E","DA-022":"B","DA-023":"E"},
}
SECONDARY = {
 "h13": {"BY-002":["E","D"],"BY-003":["E"],"BY-004":["F"],"BY-006":["E"],"CY-002":["G"],
         "CY-003":["G","F"],"CY-004":["F"],"DA-002":["D","E"],"DA-004":["E"],"DA-005":[],
         "DA-008":["F","E","D"],"DA-010":["D"],"DA-011":["D","E"],"DA-012":["D","E"],
         "DA-013":["F","A"]},
 "h14": {"BY-007":["F","D"],"BY-008":["E"],"BY-009":["D"],"BY-010":["D"],"BY-011":["F","D"],
         "CY-005":["G"],"CY-006":["G"],"CY-008":["G"],"DA-015":["F","D","E"],
         "DA-016":["E","D"],"DA-017":["E"],"DA-019":["B","E","D"],"DA-020":["C","E","D"],
         "DA-021":[],"DA-022":["F","A"],"DA-023":["D"]},
}
def load_jsonl(p):
    d={}
    for line in open(p, encoding="utf-8"):
        if line.strip():
            r=json.loads(line); d[r["anon_id"]]=r
    return d
def src(cid): return "CY" if cid.startswith("CY") else cid.split("-")[0]
def se_of(vals):
    n=len(vals)
    if n<2: return None
    m=sum(vals)/n
    return math.sqrt(sum((x-m)**2 for x in vals)/(n-1))/math.sqrt(n)
rows=[]
for sk,dn in SETS.items():
    jd=BASE/dn/"judging"
    mapping=json.loads((jd/"host-mapping.json").read_text(encoding="utf-8"))
    final=json.loads((jd/"final-scores.json").read_text(encoding="utf-8"))
    assert final.get("disputes_ours")==[] and final.get("disputes_master")==[]
    rev_o={v:k for k,v in mapping["ours"].items()}; rev_m={v:k for k,v in mapping["master"].items()}
    O=[load_jsonl(jd/f"judgeO{i}.jsonl") for i in (1,2)]; M=[load_jsonl(jd/f"judgeM{i}.jsonl") for i in (1,2)]
    for cid,pc in sorted(final["per_case"].items()):
        if src(cid) not in ("DA","BY","CY"): continue
        ao,am=rev_o[cid],rev_m[cid]
        comp={}
        for k in ("direction","claims","timing","total"):
            comp[k]=(sum(j[ao][k] for j in O)/2, sum(j[am][k] for j in M)/2)
        assert abs(comp["total"][0]-pc["ours"])<0.01 and abs(comp["total"][1]-pc["master"])<0.01
        rows.append({"set":sk,"id":cid,"src":src(cid),"diff":pc["diff"],
                     **{k:comp[k][0]-comp[k][1] for k in ("direction","claims","timing")},
                     "o_dir":comp["direction"][0],"m_dir":comp["direction"][1]})
def agg(rs,label):
    if not rs: return
    d=[r["diff"] for r in rs]
    cd={k:sum(r[k] for r in rs)/len(rs) for k in ("direction","claims","timing")}
    tot=sum(abs(cd[k]) for k in cd)
    print(f"{label}: n={len(rs)} diff={sum(d)/len(d):+.3f} SE={se_of(d):.3f} W/T/L="
          f"{sum(1 for x in d if x>0)}/{sum(1 for x in d if x==0)}/{sum(1 for x in d if x<0)} | "
          f"comp mean diffs dir={cd['direction']:+.3f} claims={cd['claims']:+.3f} timing={cd['timing']:+.3f} | "
          f"shares dir={abs(cd['direction'])/tot:.1%} claims={abs(cd['claims'])/tot:.1%} timing={abs(cd['timing'])/tot:.1%}")
print("== score layer ==")
for sk in SETS:
    for s in ("DA","BY","CY"):
        agg([r for r in rows if r["set"]==sk and r["src"]==s], f"{sk}-{s}")
    agg([r for r in rows if r["set"]==sk], f"{sk}-LRall")
for s in ("DA","BY","CY"):
    agg([r for r in rows if r["src"]==s], f"POOLED-{s}")
agg(rows,"POOLED-LRall")
print("\n== primary attribution h13+h14 (new coding) ==")
for sk in ("h13","h14"):
    for s in ("DA","BY","CY","ALL"):
        sub={c:v for c,v in PRIMARY[sk].items() if s=="ALL" or src(c)==s}
        if sub: print(sk,s,dict(collections.Counter(sub.values())),"n_loss=",len(sub))
sub={**PRIMARY["h13"],**PRIMARY["h14"]}
for s in ("DA","BY","CY","ALL"):
    ss={c:v for c,v in sub.items() if s=="ALL" or src(c)==s}
    print("POOLED-new",s,dict(collections.Counter(ss.values())),"n_loss=",len(ss))
fam=lambda v: v in "ABC"
for sk in ("h13","h14"):
    v=list(PRIMARY[sk].values()); print(sk,"取用family primary:",sum(fam(x) for x in v),"/",len(v))
v=list(sub.values()); print("POOLED-new 取用family:",sum(fam(x) for x in v),"/",len(v),
      " (+h12 DIAG 13/24 -> three-set family:",13+sum(fam(x) for x in v),"/",24+len(v),")")
print("\n== secondary (multi-label) counts h13+h14 ==")
sec=collections.Counter()
for sk in SECONDARY:
    for c,tags in SECONDARY[sk].items(): sec.update(tags)
print(dict(sec))
