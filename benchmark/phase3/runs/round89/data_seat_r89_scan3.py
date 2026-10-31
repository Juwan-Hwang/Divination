import json, re
base="/home/hatch/workspace/divination/benchmark/phase3"
hm=json.load(open(f"{base}/runs/round89/judging/host-mapping.json",encoding="utf-8"))
jx=json.load(open(f"{base}/runs/round89/judging/judgeX-merged.json",encoding="utf-8"))
jy=json.load(open(f"{base}/runs/round89/judging/judgeY-merged.json",encoding="utf-8"))
patterns={
 "主问未载/仅载他事": r"主问.*未载|主问.*未記|仅载问者|僅載問者|结局仅载|結局僅載|结局仅记|結局僅記|仅记.*自述|所问.*未载|所問.*未載|问目.*未",
 "字形/文本残损": r"残损|殘損|乱码|亂碼|字形|讹字|訛字|衍字|错字|錯字|占位符|�",
 "合载/混入/转引": r"合载|合載|混入|转引|轉引|旁载|旁載|另载他|编者|編者|编辑|編輯",
 "指令性字样": r"指令|须注|須注|勿以|分开统计|分開統計|评分时|評分時",
 "卡面/盘面缺陷": r"卡面|盤面殘|盘面残|輸入卡|输入卡",
 "结局矛盾/含混": r"自相矛盾|前后矛盾|前後矛盾|句意残缺|句意殘缺|语义未明|語義未明|指代未明|未明字|归属未明|歸屬未明",
 "结局与问面错位": r"错位|錯位|对象为|對象為|记载对象|記載對象|非所问|非所問|答非所问",
}
seen={}
for seat,d in [("X",jx),("Y",jy)]:
    for anon,rec in d.items():
        r=rec.get("reason","")
        hits=[k for k,p in patterns.items() if re.search(p,r)]
        if hits:
            cid=hm.get(anon,"?")
            seen.setdefault(cid,[]).append((seat,anon,hits,r))
for cid in sorted(seen):
    print("=====",cid)
    for seat,anon,hits,r in seen[cid]:
        print(f" [{seat} {anon} {hits}] {r}")
print("TOTAL",len(seen))
