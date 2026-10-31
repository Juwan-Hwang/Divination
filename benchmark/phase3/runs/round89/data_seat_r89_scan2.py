import json, re
base="/home/hatch/workspace/divination/benchmark/phase3"
hm=json.load(open(f"{base}/runs/round89/judging/host-mapping.json",encoding="utf-8"))
jx=json.load(open(f"{base}/runs/round89/judging/judgeX-merged.json",encoding="utf-8"))
jy=json.load(open(f"{base}/runs/round89/judging/judgeY-merged.json",encoding="utf-8"))
# keywords for data-face clues (strong)
kw=["tradition","虛稱","虚称","未标注","未標注","卡面","残损","殘損","缺载","缺載","未载","未載","讹","訛","衍字","乱码","亂碼","错配","錯配","错位","錯位","混入","合载","合載","两占","兩占","再占","转引","轉引","他例","无关","無關","他事","对象未","對象未","无对应","無對應","不对应","不對應","未记所问","未記所問","主问","主問","问目","問目","结局仅","結局僅","结局未","結局未","结局无","結局無","结局不","結局不","自相矛盾","矛盾","指令","须注","須注","勿以","分开统计","分開統計","占位","?","？"]
seen={}
for seat,d in [("X",jx),("Y",jy)]:
    for anon,rec in d.items():
        r=rec.get("reason","")
        hits=[k for k in kw if k in r]
        if hits:
            cid=hm.get(anon,"?")
            seen.setdefault(cid,[]).append((seat,anon,rec.get("total"),hits,r))
for cid in sorted(seen):
    print("=====",cid)
    for seat,anon,total,hits,r in seen[cid]:
        print(f" [{seat} {anon} total={total} hits={hits}] {r}")
print("TOTAL cases with hits:",len(seen))
