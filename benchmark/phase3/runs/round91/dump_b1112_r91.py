import json, os
base="/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12"
b11=["LY-312","LY-314","LY-315","LY-318","LY-319","LY-320","LY-322","LY-323","LY-324","LY-325","LY-328","LY-329","LY-330","LY-331","LY-332","LY-333","LY-335","LY-336","LY-338","LY-339"]
b12=["LY-340","LY-342","LY-344","LY-402","LY-403","LY-404","LY-405","LY-406","LY-407","LY-408","LY-411","LY-413","LY-415","LY-416","LY-417","LY-418","LY-421","LY-423","LY-424","LY-425"]
out=[]
for cid in b11+b12:
    d=json.load(open(os.path.join(base,cid+".json"),encoding="utf-8"))
    c=d.get("context",{}); a=c.get("attachments",{})
    out.append("=== "+cid+" | tradition="+str(d.get("tradition")))
    out.append("Q: "+str(c.get("question"))+" | setting: "+str(c.get("setting"))+" | asked_at: "+str(c.get("asked_at")))
    out.append("hex: "+str(a.get("hexagram"))+" | date: "+str(a.get("date_ganzhi"))+" | kong: "+str(a.get("空亡")))
    out.append("yongshen: "+str(a.get("yongshen")))
    out.append("moving: "+str(a.get("moving_lines")))
    out.append("hidden: "+str(a.get("hidden_lines")))
    out.append("note: "+str(a.get("chart_note")))
    lines=a.get("chart_lines_top_to_bottom") or []
    for i,l in enumerate(lines):
        out.append("  L%d: %s"%(6-i,l))
    n=d.get("notes") or {}
    cg=n.get("completion_grade") or {}
    fl=cg.get("fields") or {}
    flags=[]
    for k,v in fl.items():
        if isinstance(v,dict) and v.get("grade") not in ("直载","直載",None):
            flags.append(k+"="+str(v.get("grade")))
    if flags: out.append("FLAGS(非直载): "+", ".join(flags))
    out.append("")
open("/home/hatch/workspace/divination/benchmark/phase3/runs/round91/summary_b1112_r91.txt","w",encoding="utf-8").write("\n".join(out))
print("done", len(b11)+len(b12))
