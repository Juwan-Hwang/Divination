import json, os
BASE="/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12"
IDS=["LY-537","LY-538","LY-539","LY-540","LY-541","LY-542","LY-543","LY-601","LY-602","LY-603","LY-604","LY-605","LY-606","LY-607","LY-608","LY-609","LY-610","LY-611","LY-612","LY-613","LY-614","LY-615","LY-616","LY-617","LY-618","LY-619","LY-620","LY-621","LY-622","LY-623","LY-624","LY-625","LY-626","LY-627","LY-628","LY-629","MH-001","MH-002","MH-003","MH-006","MH-007","MH-008","MH-009","MH-010","MP-001","MP-002","MP-003","MP-004","MP-005","MP-006","MP-007","MP-008","MP-009","MP-010","MP-011","MP-012","MP-013","MP-014","MP-015","MP-016"]
for cid in IDS:
    d=json.load(open(os.path.join(BASE,cid+".json"),encoding="utf-8"))
    ctx=d.get("context",{})
    att=ctx.get("attachments",{}) or {}
    print("###",cid,"trad=",d.get("tradition"))
    print("Q:",ctx.get("question"),"| setting:",ctx.get("setting"),"| asked:",ctx.get("asked_at"))
    # other ctx keys
    for k,v in ctx.items():
        if k not in ("question","setting","asked_at","attachments"):
            print(" ctx."+k+":",json.dumps(v,ensure_ascii=False)[:800])
    for k,v in att.items():
        if k=="chart_note": continue
        print(" att."+k+":",json.dumps(v,ensure_ascii=False)[:1200])
    # subject
    print(" subj:",json.dumps(d.get("subject"),ensure_ascii=False)[:300])
    # any top-level extra
    for k in d:
        if k not in ("id","tradition","subject","context","provenance","language","notes"):
            print(" top."+k+":",json.dumps(d[k],ensure_ascii=False)[:800])
