import json, re
entries=json.load(open("/home/hatch/workspace/divination/benchmark/phase3/runs/round52/entries-r52.json",encoding="utf-8"))
known_titles=["邵南","倪辉","王浪仙","张彦泽","红象","俞翁","惠吉","范子珉","史言","沈先生","汤史","田道人","狄偁","张文规","王铁面","王文卿","相船","王俊明","方典","叶议","江致平","毛人","大散关","李弼违","牛鬼","全师","谢眼","玉女","叶德孚","李知命","九圣奇鬼","袁州狱","司命真君","黄法师","路当可","杨望才","何文缜","何丞相","林孝雍","沈持要","黄荐可","相国寺术者","僧如胜","吴信叟","夏仅","黄山人","上竺观音","秦昌时","乐清二士","僧法恩","三士问相"]
def known(t): return any(k in t for k in known_titles)
pat=re.compile(r"(问命|卖卜|卜者|日者|相者|术者|术士|占者|筮人|推命|禄命|善相|能相|工相|相人|轨革|卦影|布课|扶乩|降乩|拆字|测字|相墓|风水先生|堪舆)")
for e in entries:
    if known(e["title"]) or "梦" in e["title"]: continue
    if e["fl_title"]<137: continue
    m=pat.findall(e["body"])
    if m:
        print(e["fl_title"], e["title"], "hits", len(m), set(m), "|", e["body"][:90])
