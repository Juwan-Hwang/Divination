import json, os, re, math, collections
base="/home/hatch/workspace/divination/benchmark/phase3"
neg=json.load(open(f"{base}/runs/round94/diagnosis/lr-negatives-dev94.json"))
ids=[x["case_id"] for x in neg["negatives"]]
print("n_neg", len(ids), "total", neg["n_liuren_total"])
# segment sums
for seg, filt in [("dev8", lambda x: x["in_dev8"]), ("LR3", lambda x: not x["in_dev8"]), ("all", lambda x: True)]:
    xs=[x for x in neg["negatives"] if filt(x)]
    s=sum(x["pair_diff"] for x in xs)
    diffs=sorted(x["pair_diff"] for x in xs)
    med=diffs[len(diffs)//2] if len(diffs)%2==1 else (diffs[len(diffs)//2-1]+diffs[len(diffs)//2])/2
    print(seg, len(xs), round(s,2), round(s/len(xs),3), med)
    # self-consistency
    bad=[x["case_id"] for x in xs if abs((x["ours"]-x["master"])-x["pair_diff"])>1e-9]
    print("  selfcheck bad:", bad)
for cid in ids:
    inp=json.load(open(f"{base}/inputs-dev12/{cid}.json"))
    pred=json.load(open(f"{base}/runs/round94/predictions/{cid}.json"))
    ctx=inp.get("context",{})
    att=ctx.get("attachments",{}) or {}
    prov=inp.get("provenance",{}) or {}
    pt=pred.get("prediction_text","") or ""
    bs=pred.get("basis","") or ""
    has_sec8 = "第八节" in bs
    has_gong = "功量清单" in bs
    has_mainline = "做功主线认定" in bs or "主线认定" in bs
    weight_words=[w for w in ["权重居首","居首","压过","降为次","降权","主线","压制居首","权重打折","权重"] if w in (pt+bs)]
    keys=list(att.keys())
    print(f"\n== {cid} dev8={ [x['in_dev8'] for x in neg['negatives'] if x['case_id']==cid][0]} diff={[x['pair_diff'] for x in neg['negatives'] if x['case_id']==cid][0]}")
    print("  Q:", ctx.get("question","")[:80])
    print("  book:", prov.get("book","")[:90])
    print("  att_keys:", keys)
    att_s=json.dumps(att, ensure_ascii=False)
    print("  att_len:", len(att_s), "att_head:", att_s[:160].replace("\n"," "))
    print("  sec8:", has_sec8, "gong:", has_gong, "mainline:", has_mainline, "weight_words:", weight_words)
    print("  pred_head:", pt[:220].replace("\n"," "))
