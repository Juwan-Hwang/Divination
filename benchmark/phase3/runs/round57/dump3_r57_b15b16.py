import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12")
ids = ["LY-604","LY-605","LY-606","LY-607","LY-608","LY-609","LY-610","LY-611","LY-612","LY-613"]
for cid in ids:
    d = json.loads((base/f"{cid}.json").read_text(encoding="utf-8"))
    c = d["context"]; h = c.get("hexagram",{})
    print(f"== {cid} | subj:{d.get('subject')} | Q:{c.get('question')} | cat:{c.get('category')} | rel:{c.get('caster_or_relation')} | date:{h.get('date_ganzhi')} | orig:{h.get('original_name')}->{h.get('changed_name')} palace:{h.get('palace')} kong:{h.get('kongwang')} mov:{h.get('moving_lines')}")
    for ln in h.get("chart_lines",[]):
        print("   ", ln)
    # extra keys
    for k in c:
        if k not in ("question","category","caster_or_relation","asked_at","casting_method","hexagram"):
            print("   EXTRA", k, c[k])
