# DIAG-H24 编码表与计数复算（编码为本席逐例判读结果，本脚本只做计数复核）
# main: (code, subclass, tim_grade) ; sec: list of (code, subclass, tim_grade)
C = {
 "DS-019": (("E4",None,None), [("E5","CLAIM",None)]),
 "DS-020": (("E4",None,None), [("E5","CLAIM",None)]),
 "DS-021": (("E5","DIR",None), [("E4",None,None)]),
 "DS-022": (("E4",None,None), []),
 "DS-023": (("E5","DIR",None), [("E3","A",None)]),
 "DS-024": (("E5","DIR",None), [("E3","A",None)]),
 "GSZ-034": (("E5","TIM","实质"), []),
 "GSZ-038": (("E5","TIM","实质"), []),
 "GSZ-041": (("E5","TIM","实质"), []),
 "GSZ-042": (("E5","CLAIM",None), [("E5","TIM","实质")]),
 "GSZ-043": (("E5","CLAIM",None), []),
 "GSZ-046": (("E5","DIR",None), [("E4",None,None)]),
 "GSZ-047": (("E5","DIR",None), [("E5","OMIT",None),("E5","TIM","实质")]),
 "QM-021": (("E5","TIM","实质"), []),
 "QM-022": (("E5","CLAIM",None), [("E3","A",None)]),
 "QM-023": (("E5","DIR",None), [("E5","OMIT",None)]),
 "QM-024": (("E5","DIR",None), [("E4",None,None)]),
 "QM-025": (("E5","DIR",None), [("E5","TIM","实质")]),
 "QM-206": (("E5","TIM","实质"), [("E5","CLAIM",None)]),
 "QM-207": (("E5","DIR",None), [("E5","TIM","实质")]),
 "QM-307": (("E5","TIM","实质"), []),
 "QM-308": (("E5","CLAIM",None), [("E5","TIM","轻级")]),
 "QM-309": (("E5","DIR",None), [("E5","TIM","实质")]),
 "ZCB-012": (("E5","TIM","实质"), []),
 "ZCB-013": (("E5","TIM","实质"), []),
 "ZCB-014": (("E5","TIM","轻级"), []),
 "ZCB-015": (("E5","TIM","轻级"), []),
}
from collections import Counter
assert len(C)==27
main=Counter(); sub=Counter(); timg=Counter(); sec=Counter(); e3a=0
seg={}
for cid,(m,ss) in C.items():
    s=cid.split("-")[0]
    main[m[0]]+=1; seg.setdefault(s,Counter())[m[0]]+=1
    if m[0]=="E5": sub[m[1]]+=1
    if m[1]=="TIM": timg[m[2]]+=1
    for x in ss:
        sec[x[0] if x[0]!="E5" else "E5-"+str(x[1])]+=1
        if x[0]=="E5" and x[1]=="TIM": sec["TIM次-"+str(x[2])]+=1
    if m[0]=="E3" or any(x[0]=="E3" and x[1]=="A" for x in ss): e3a+=1
    if m[0]=="E3" and m[1]=="A": pass
print("主码:",dict(main))
print("E5主码子类:",dict(sub))
print("TIM主码分级:",dict(timg))
print("次码:",dict(sec))
print("分段主码:",{k:dict(v) for k,v in sorted(seg.items())})
print("E3A涉 (主或次):",e3a)
tim_claim_nom = sub["TIM"]+sub["CLAIM"]
tim_sub = timg["实质"]+sub["CLAIM"]
print(f"DIR率 {sub['DIR']}/27 = {sub['DIR']/27:.3f}")
print(f"TIM+CLAIM 名义 {tim_claim_nom}/27 = {tim_claim_nom/27:.3f}")
print(f"TIM+CLAIM 实质 {tim_sub}/27 = {tim_sub/27:.3f}")
print(f"OMIT率 {sub['OMIT']}/27 = {sub['OMIT']/27:.3f}")
print(f"E3A涉率 {e3a}/27 = {e3a/27:.3f}")
