#!/usr/bin/env python3
import pathlib, re, json
base=pathlib.Path(__file__).parent/"yuewei-raw-r53"
out=[]
keywords=["占","卜","籤","签","夢","梦","相人","相術","相术","命","風水","风水","形家","乩","讖","谶","預知","预知","兆","算","推命","課","课","卦","壬","爻","星命","祿命","禄命","擇日","择日","堪輿","堪舆","術士","术士","瞽","拆字","測字","测字","圓夢","圆梦","解夢","扶鸞","降筆","籤詩","求籤","神數","數術","陰陽家","阴阳家","望氣","相面","骨相","痣","先兆","預言","预言","斷","断曰","曰：此","必","後果","后果","果如","驗","验"]
# broader single chars for flagging, will manually review
flagchars="占卜夢兆讖乩卦課籤算相命"
for n in range(17130,17185):
    txt=(base/f"bookv_{n}.txt").read_text(encoding="utf-8")
    lines=txt.splitlines()
    title=lines[0].replace("TITLE: ","") if lines else ""
    vol=re.search(r"閱微草堂筆記·(.*?)_全文",title)
    vol=vol.group(1) if vol else title
    body=txt.split("\n\n",1)[1] if "\n\n" in txt else txt
    # cut footer
    body=body.split("上一章回目錄")[0]
    paras=[p.strip() for p in body.split("\n\n") if p.strip()]
    # first para contains header navigation merged: remove prefix up to 作者：紀昀
    if paras:
        p0=paras[0]
        if "作者：紀昀" in p0:
            paras[0]=p0.split("作者：紀昀",1)[1].strip()
            if not paras[0]:
                paras=paras[1:]
    entries=[]
    for i,p in enumerate(paras,1):
        flag=any(k in p for k in keywords) or any(c in p for c in ["占","卜","夢","讖","乩","卦"])
        entries.append({"idx":i,"len":len(p),"flag":bool(flag),"head":p[:60],"text":p})
    out.append({"page":n,"vol":vol,"count":len(paras),"entries":entries})
    print(n, vol, len(paras), "flagged", sum(1 for e in entries if e["flag"]))
pathlib.Path(__file__).parent.joinpath("yuewei-parsed-r53.json").write_text(json.dumps(out,ensure_ascii=False,indent=1),encoding="utf-8")
print("total entries", sum(o["count"] for o in out))
print("total flagged", sum(sum(1 for e in o["entries"] if e["flag"]) for o in out))
