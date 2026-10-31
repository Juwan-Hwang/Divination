import json
base="/home/hatch/workspace/divination/benchmark/phase3"
ids=["BY-017","BY-018","BY-020","BY-021","CYJ-006","CYJ-007","CYJ-008","CYJ-009","CYJ-010","DA-038","DA-041","DA-042","DA-044","DA-046","GSZ-101","GSZ-103","GSZ-104","GSZ-105","WHY-025","WHY-026","WHY-027","WHY-028","WHY-031","WHY-032","WHY-033","WHY-034","WHY-035","WHY-036"]
lr=[i for i in ids if i.split("-")[0] in ("BY","CYJ","DA")]
ly=[i for i in ids if i.split("-")[0] in ("GSZ","WHY")]
def has(s,*keys): return all(k in s for k in keys)
cnt={}
def inc(k,seg="all"):
    cnt.setdefault(k,0); cnt[k]+=1
tr={"changed_main":0,"reserve_used":0,"disputed":0}
for id_ in ids:
    with open(f"{base}/runs/round87/acceptance/predictions/{id_}.json",encoding="utf-8") as f: p=json.load(f)
    b=p.get("basis",""); t=p.get("trigger",{})
    for k in tr:
        if t.get(k): tr[k]+=1
    seg="lr" if id_ in lr else "ly"
    if "R80-REV1" in b or "第八节" in b: inc("cal8_"+seg); inc("cal8_all")
    if id_ in lr:
        if "应期三路" in b: inc("lr_3lu")
        if "chart_complete=false" in b or "仅干支" in b or "残损" in b: inc("lr_cyj_resid")
        if id_.split("-")[0] in ("BY","DA"): inc("lr_full")
    if id_ in ly:
        if "候选枚举" in b or "候选" in b: inc("ly_cand")
        if "四路合参" in b: inc("ly_4lu")
        if "应期三步" in b: inc("ly_3bu")
        if "对象对齐" in b or "对象复述" in b or "应验对象" in b: inc("ly_obj")
        if "终局反转扫查" in b or "终局反转" in b: inc("ly_rev")
        if "门类对表" in b: inc("ly_men")
print(cnt); print("trigger",tr); print("lr",len(lr),"ly",len(ly))
# inputs IN check
for id_ in ids:
    with open(f"{base}/holdout30/inputs/{id_}.json",encoding="utf-8") as f: inp=json.load(f)
    a=inp.get("anchors",{})
    print(id_, "anchor_keys=", list(a.keys()), "chart_complete=", a.get("chart_complete"), "asked_at=", str(a.get("asked_at"))[:40])
