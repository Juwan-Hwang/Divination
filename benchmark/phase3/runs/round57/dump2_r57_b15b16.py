import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12")
ids = ["LY-540","LY-541","LY-542","LY-543","LY-601","LY-602","LY-603","LY-604","LY-605","LY-606","LY-607","LY-608","LY-609","LY-610","LY-611","LY-612","LY-613"]
for cid in ids:
    d = json.loads((base/f"{cid}.json").read_text(encoding="utf-8"))
    c = d["context"]; a = c.get("attachments",{})
    print(f"== {cid} | Q:{c.get('question')} | asked:{c.get('asked_at')} | date:{a.get('date_ganzhi','-')} | kong:{a.get('kongwang') or a.get('空亡','-')} | hex:{a.get('hexagram')} | mov:{a.get('moving_lines')} | yong:{a.get('yongshen','-')} | hid:{a.get('hidden_lines','-')} | setting:{c.get('setting')}")
    for ln in a.get("chart_lines_top_to_bottom",[]):
        print("   ", ln)
