import json, pathlib
base = pathlib.Path.home()/"workspace/divination/benchmark/phase3"
negs = json.load(open(base/"runs/round43/diagnosis/lr-negatives-dev43.json"))["negatives"]
fs = json.load(open(base/"runs/round43/final-scores.json"))
out=[]
for n in negs:
    cid=n["case_id"]
    pred=json.load(open(base/f"runs/round43/predictions/{cid}.json"))
    inp=json.load(open(base/f"inputs-dev12/{cid}.json"))
    sub=fs["ours_sub"].get(cid)
    ax=fs["ours_axis2"].get(cid)
    out.append({"neg":n,"pred":pred,"input":inp,"ours_sub":sub,"ours_axis2":ax})
print(json.dumps(out, ensure_ascii=False, indent=1))
