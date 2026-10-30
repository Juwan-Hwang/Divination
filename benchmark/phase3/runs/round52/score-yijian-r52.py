import re, json
entries=json.load(open("/home/hatch/workspace/divination/benchmark/phase3/runs/round52/entries-r52.json",encoding="utf-8"))
# known examined titles (substring match) - from R47 dream titles handled separately, R48/49/50/51
known = ["邵南神术","倪辉方技","王浪仙","张彦泽","红象卦影","俞翁相人","惠吉异术","范子珉","史言命术","沈先生","汤史二相","田道人","狄偁卦影","张文规","王铁面","王文卿相","宜黄人相船","王俊明","方典薄命","叶议秀才","江致平","和州毛人","大散关老人","李弼违","牛鬼","全师秽迹","谢眼妖术","玉女喜神术","叶德孚","李知命","九圣奇鬼","袁州狱","司命真君","黄法师","路当可","杨望才","杨抽马","何文缜","林孝雍","沈持要","黄荐可","相国寺","包大常","僧如胜","吴信叟","黄元道","夏仅","黄山人","周元特","王垂"]
def is_known(t):
    return any(k in t or t in k for k in known)
div_words=["善相","能相","相人","卖卜","卜者","日者","术士","术者","相者","筮","推命","问命","禄命","方技","神术","异术","谈祸福","休咎","占","卦","课","命术","相术","风水","堪舆","择日","遁甲","六壬","拆字","测字","扶乩","降笔","签","梦"]
title_kw=["相","卜","筮","卦","命","术","占","签","风水","日者","方技","神","巫","道士","僧"]
for e in entries:
    b=e["body"]; t=e["title"]
    s=0; hits=[]
    for w in div_words:
        if w in b: s+=2; hits.append(w)
        if w in t: s+=3; hits.append("T:"+w)
    # dialogue density
    s+= min(b.count("曰"),6)
    # verification phrases
    for w in ["无不验","无不中","屡验","奇中","神验","果然","果验","后皆验","皆验","如言","应验"]:
        if w in b: s+=2; hits.append(w)
    # fortune content
    for w in ["当迁","擢第","登科","及第","禄尽","寿","死期","拜相","得官","中选"]:
        if w in b: s+=1
    s+= min(len(b)//800, 3)
    e["score"]=s; e["hits"]=hits; e["known"]=is_known(t); e["dream"]=("梦" in t)
# candidates: not known, not dream title, score>=8
cands=[e for e in entries if not e["known"] and not e["dream"] and e["score"]>=8]
cands.sort(key=lambda x:-x["score"])
print(f"total {len(entries)} known {sum(1 for e in entries if e['known'])} dreamtitle {sum(1 for e in entries if e['dream'])} cands {len(cands)}")
for e in cands:
    print(e["score"], e["fl_title"], e["vol"], e["title"], "blen",e["blen"], ",".join(e["hits"][:10]))
