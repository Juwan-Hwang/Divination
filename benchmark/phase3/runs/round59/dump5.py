import json,sys
base="/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12/"
ids=[]
b=json.load(open("/home/hatch/workspace/divination/benchmark/phase3/runs/round59/batches.json"))
for k in ["B13","B14","B15"]: ids+=b[k]
for cid in ids:
    d=json.load(open(base+cid+".json"))
    c=d.get("context",{})
    print("===",cid,"| trad:",d.get("tradition"),"| Q:",c.get("question"),"| at:",c.get("asked_at"),"| setting:",c.get("setting"))
    a=c.get("attachments",{})
    for k,v in a.items():
        print(" ",k,":",v)
    # extra fields
    for k,v in d.items():
        if k not in ("context","id","tradition","provenance","language","subject"):
            print(" ",k,":",v)
    print(" subj:",d.get("subject"))
