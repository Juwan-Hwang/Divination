import json, re
entries=json.load(open("/home/hatch/workspace/divination/benchmark/phase3/runs/round52/entries-r52.json",encoding="utf-8"))
pats=[r"占曰",r"断曰",r"判曰",r"相之曰",r"谓之曰.{0,20}当",r"告之曰.{0,20}(当|必)",r"曰.{0,6}当(迁|擢|登|拜|死|生|得|中|为)"]
seen=set()
for pat in pats:
    for e in entries:
        if e["fl_title"]<137: continue
        for m in re.finditer(pat, e["body"]):
            key=(e["fl_title"],m.start()//60)
            if key in seen: continue
            seen.add(key)
            s=max(0,m.start()-40)
            print(e["fl_title"], e["title"], "|", e["body"][s:m.end()+45])
