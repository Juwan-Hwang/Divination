import json, math
base="/home/hatch/workspace/divination/benchmark/phase3"
neg=json.load(open(f"{base}/runs/round94/diagnosis/lr-negatives-dev94.json"))
negs=neg["negatives"]
assert neg["n_negative"]==26 and len(negs)==26 and neg["n_liuren_total"]==30
for x in negs: assert abs((x["ours"]-x["master"])-x["pair_diff"])<1e-9 and x["pair_diff"]<0
def seg_stats(xs):
    ds=sorted(x["pair_diff"] for x in xs); n=len(xs)
    med=ds[n//2] if n%2 else (ds[n//2-1]+ds[n//2])/2
    return n, round(sum(ds),2), round(sum(ds)/n,3), med
for name,f in [("dev8",lambda x:x["in_dev8"]),("LR3",lambda x:not x["in_dev8"]),("all",lambda x:True)]:
    print(name, seg_stats([x for x in negs if f(x)]))
# 承登记编码 (源: dev93 DIAG §2 20例 + §1/§4 LR2-018 W*)
coded={"LR2-013":"E","LR2-014":"D","LR2-015":"W-hard","LR2-016":"D","LR2-017":"W-hard","LR2-019":"E",
"LR2-021":"A*","LR2-022":"W*","LR2-023":"C*","LR2-024":"C*","OC-026":"E","OC-027":"C*","OC-030":"A",
"LR3-002":"W-hard","LR3-006":"E","LR3-101":"W*","LR3-107":"A","LR3-110":"D","LR3-112":"H","LR3-116":"A",
"LR2-018":"W*"}
unc=["LR-001","LR3-004","LR3-008","LR3-104","OC-029"]
ids={x["case_id"] for x in negs}
assert set(coded)|set(unc)==ids and not set(coded)&set(unc), (set(coded)|set(unc))^ids
import collections
print("coded n",len(coded), collections.Counter(coded.values()))
def se(p,n): return round(100*math.sqrt(p*(1-p)/n),1)
def share(k,n): 
    p=k/n; return f"{k}/{n}={100*p:.1f}% (SE {se(p,n)}pp)"
W=sum(1 for v in coded.values() if v.startswith("W")); Wh=3
print("coded denom:", share(W,len(coded)), share(Wh,len(coded)))
print("list denom:", share(W,26), share(Wh,26))
print("total denom:", share(W,30), share(Wh,30))
dev8c={k:v for k,v in coded.items() if [x["in_dev8"] for x in negs if x["case_id"]==k][0]}
lr3c={k:v for k,v in coded.items() if k not in dev8c}
for nm,d,ln in [("dev8 coded",dev8c,16),("LR3 coded",lr3c,10)]:
    w=sum(1 for v in d.values() if v.startswith("W")); h=sum(1 for v in d.values() if v=="W-hard")
    print(nm, len(d), collections.Counter(d.values()), "coded:",share(w,len(d)),share(h,len(d)), "list:",share(w,ln),share(h,ln))
print("confounded 7/21:", share(7,21))
print("LR3-010 in list:", "LR3-010" in ids, "| LR3-114 in list:", "LR3-114" in ids)
print("ALL ASSERTIONS PASS")
