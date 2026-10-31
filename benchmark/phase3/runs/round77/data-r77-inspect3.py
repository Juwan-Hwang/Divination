import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
for name in ["packet1.json","packet2.json","packet3.json","packet4.json","packetA.json","packetB.json"]:
    p=base/f"runs/round77/judging/{name}"
    try:
        d=json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        print(name, "ERR", e); continue
    s=json.dumps(d, ensure_ascii=False)
    print(name, "type", type(d).__name__, "len", len(d) if hasattr(d,'__len__') else '-', "has LR2 anon P3-21d1866b:", "P3-21d1866b" in s, "has editor_note str:", "editor_note" in s, "has phrase:", "评分时该细项请按未完全复核处理" in s)
    if "P3-21d1866b" in s:
        # find entries
        def walk(o, path=""):
            if isinstance(o, dict):
                if o.get("anon_id")=="P3-21d1866b" or o.get("id")=="P3-21d1866b":
                    print("  ENTRY", path, json.dumps(o, ensure_ascii=False)[:4000])
                for k,v in o.items():
                    walk(v, path+"/"+str(k))
            elif isinstance(o, list):
                for i,v in enumerate(o):
                    walk(v, path+f"[{i}]")
        walk(d)
    if "评分时该细项请按未完全复核处理" in s:
        idx=s.find("评分时该细项请按未完全复核处理")
        print("  phrase ctx:", s[max(0,idx-500):idx+200])
# batches check for LY-537, YM-070 seat mapping via batches.json structure
b=json.loads((base/"runs/round77/batches.json").read_text(encoding="utf-8"))
print("\nbatches type", type(b).__name__)
print(json.dumps(b, ensure_ascii=False)[:2000])
# judge merged: check for flag fields
for name in ["judgeX-merged.json","judgeY-merged.json"]:
    d=json.loads((base/f"runs/round77/judging/{name}").read_text(encoding="utf-8"))
    s=json.dumps(d, ensure_ascii=False)
    print(name, "type", type(d).__name__, "len", len(d) if hasattr(d,'__len__') else '-', "contains flag:", '"flag"' in s, "FLAGS:", "FLAGS" in s)
    if isinstance(d, list) and d:
        print("  first keys", list(d[0].keys()) if isinstance(d[0], dict) else type(d[0]))
    if isinstance(d, dict):
        print("  keys", list(d.keys())[:20])
