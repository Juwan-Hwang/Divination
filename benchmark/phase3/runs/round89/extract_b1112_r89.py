import json, pathlib
P3 = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
ids = ["LY-312","LY-314","LY-315","LY-318","LY-319","LY-320","LY-322","LY-323","LY-324","LY-325","LY-328","LY-329","LY-330","LY-331","LY-332","LY-333","LY-335","LY-336","LY-338","LY-339","LY-340","LY-342","LY-344","LY-402","LY-403","LY-404","LY-405","LY-406","LY-407","LY-408","LY-411","LY-413","LY-415","LY-416","LY-417","LY-418","LY-421","LY-423","LY-424","LY-425"]
out=[]
for cid in ids:
    d=json.load(open(P3/"inputs-dev12"/f"{cid}.json"))
    c=d.get("context",{})
    a=c.get("attachments",{}) or {}
    out.append({
        "id":cid,"tradition":d.get("tradition"),
        "question":c.get("question"),"asked_at":c.get("asked_at"),"setting":c.get("setting"),
        "hexagram":a.get("hexagram"),"yongshen":a.get("yongshen"),"casting":a.get("casting_method"),
        "lines":a.get("chart_lines_top_to_bottom"),"moving":a.get("moving_lines"),
        "date":a.get("date_ganzhi"),"kongwang":a.get("空亡") or a.get("kongwang"),
        "hidden":a.get("hidden_lines"),"chart_note":a.get("chart_note"),
        "extra":{k:v for k,v in a.items() if k not in ("hexagram","yongshen","casting_method","chart_lines_top_to_bottom","moving_lines","date_ganzhi","空亡","hidden_lines","chart_note")},
        "subject":d.get("subject"),
    })
pathlib.Path(__file__).with_name("summary_b1112_r89.json").write_text(json.dumps(out,ensure_ascii=False,indent=1))
print(len(out))
for o in out:
    print("===",o["id"],o["tradition"],"|",o["question"],"|",o["date"],"| KW:",o["kongwang"])
    print(" HEX:",o["hexagram"],"| YS:",o["yongshen"],"| MOV:",o["moving"],"| HID:",o["hidden"])
    for L in (o["lines"] or []): print("  ",L)
    if o["extra"]: print(" EXTRA:",json.dumps(o["extra"],ensure_ascii=False)[:600])
