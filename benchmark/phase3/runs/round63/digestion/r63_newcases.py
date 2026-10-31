import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
def load(p):
    with open(p, encoding="utf-8") as f: return json.load(f)
om=load(base/"runs/round63/judging/outcome-manifest.json")
for cid in ["LY-523","LY-030","LY-408","LY-452","LY-514","AS-207","LY-434","LY-538"]:
    card=load(base/f"inputs-dev12/{cid}.json")
    pred=load(base/f"runs/round63/predictions/{cid}.json")
    print("="*90)
    print(cid, "| subject:", json.dumps(card.get("subject"),ensure_ascii=False)[:200])
    ctx=card.get("context",{})
    for k in ["question","setting","asked_at"]:
        if k in ctx: print(" ", k, ":", str(ctx[k])[:300])
    if card.get("context") is None: print("  full card:", json.dumps(card,ensure_ascii=False)[:800])
    print("  PRED:", pred["prediction_text"][:600])
    print("  OUTCOME:", om["cases"].get(cid))
    st=om.get("stripped_tail",{}).get(cid)
    if st: print("  STRIPPED_TAIL:", json.dumps(st,ensure_ascii=False)[:500])
# r49 LY-538 raw
r49=load(base/"data/case-annotations-r49.json")
for a in r49["annotations"]:
    if a["case_id"]=="LY-538": print("\nR49 LY-538 raw:", json.dumps(a,ensure_ascii=False,indent=1))
# LY-025 / LY-216 r63 predictions check
for cid in ["LY-025","LY-216"]:
    pred=load(base/f"runs/round63/predictions/{cid}.json")
    print(f"\n{cid} R63 prediction_text:", pred["prediction_text"][:700])
# same-story search for LY-030: outcomes containing 鳴之於官 or 分文不復 or 盜盡
for cid,txt in om["cases"].items():
    if isinstance(txt,str) and ("分文不復" in txt or "分文不复" in txt or "鳴之於官" in txt):
        print("\nSAME-STORY?", cid, txt[:400])
# directive scan over all outcomes
keys=["盲测比对","比對","须注","須注","不得","必须","必須","请勿","請勿","ignore","Ignore","评分","評分","量表"]
for cid,txt in om["cases"].items():
    if isinstance(txt,str):
        for k in keys:
            if k in txt:
                print("\nDIRECTIVE?", cid, "key:", k, "|", txt[:350]); break
print("\nLR2016 split:", json.dumps(om.get("_r56_lr2016_split"),ensure_ascii=False)[:900])
