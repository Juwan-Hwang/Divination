import json, pathlib, collections
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
def load(p):
    with open(p, encoding="utf-8") as f: return json.load(f)
hm = load(base/"runs/round63/judging/host-mapping.json")
lines = (base/"runs/round63/judging/FLAGS-selfreported-r63.md").read_text(encoding="utf-8").splitlines()
def seat_label(h):
    for tok in ["X1","X2","X3","X4","Y1","Y2","Y3","Y4"]:
        if tok in h: return tok
    return h
seat=None; byanon=collections.OrderedDict()
for l in lines:
    if l.startswith("# "): seat=seat_label(l[2:].strip()); continue
    if l.startswith("- P3-"):
        anon, txt = l[2:].split("：",1)
        byanon.setdefault(anon.strip(),[]).append((seat,txt))
prior_files=[49,50,51,53,54,55,56,57,58,59,60,61,62]
prior={}
for r in prior_files:
    d=load(base/f"data/case-annotations-r{r}.json")
    for a in d["annotations"]:
        prior.setdefault(a["case_id"],[]).append((r,a))
om63=load(base/"runs/round63/judging/outcome-manifest.json")
out=[]
for anon, es in byanon.items():
    cid=hm[anon]
    hist=prior.get(cid,[])
    latest=None
    if hist:
        r,a=max(hist,key=lambda x:x[0])
        latest={"round":r,"disposition":a.get("disposition"),"type_label":a.get("type_label"),"relation":a.get("relation"),"flag":a.get("flag"),"finding":a.get("finding") or a.get("basis"),"carry":a.get("manifest_carry_suggestion")}
    out.append({"anon":anon,"case_id":cid,"seats":[s for s,_ in es],"flags_r63":[f"{s}：{t}" for s,t in es],"outcome_r63":om63["cases"].get(cid),"prior_rounds":[r for r,_ in hist],"latest_prior":latest})
pathlib.Path(base/"runs/round63/digestion/r63_flagdump.json").write_text(json.dumps(out,ensure_ascii=False,indent=1),encoding="utf-8")
print("records",len(out))
for rec in out:
    lp=rec["latest_prior"]
    print(rec["case_id"], rec["anon"], "seats", rec["seats"], "| prior rounds", rec["prior_rounds"], "| latest:", (lp["round"],lp["disposition"],lp["relation"]) if lp else None)
