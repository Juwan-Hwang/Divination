import json, os
base="/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12"
ids=["LY-339","LY-402","LY-416","LY-417","LY-425","LY-418","LY-319"]
out=[]
for cid in ids:
    d=json.load(open(os.path.join(base,cid+".json"),encoding="utf-8"))
    out.append("##### "+cid)
    out.append(json.dumps(d,ensure_ascii=False,indent=1))
    out.append("")
open("/home/hatch/workspace/divination/benchmark/phase3/runs/round91/raw_b1112_r91.txt","w",encoding="utf-8").write("\n".join(out))
print("ok")
