import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
def load(p):
    with open(p, encoding="utf-8") as f: return json.load(f)
hm = load(base/"runs/round63/judging/host-mapping.json")
# sample input + prediction
for cid in ["LY-623","BZ-105","YM-070"]:
    card = load(base/f"inputs-dev12/{cid}.json")
    print(f"\n=== CARD {cid} keys:", list(card.keys()))
    print(json.dumps(card, ensure_ascii=False, indent=1)[:2500])
    pred = load(base/f"runs/round63/predictions/{cid}.json")
    print(f"--- PRED {cid} keys:", list(pred.keys()))
    print(json.dumps(pred, ensure_ascii=False, indent=1)[:1500])
# r62 annotations structure for flags list vs annotations: check flags entries fields
r62 = load(base/"data/case-annotations-r62.json")
print("\n\nr62 flags[0] keys:", list(r62["flags"][0].keys()))
print("r62 flags len", len(r62["flags"]), "annotations len", len(r62["annotations"]))
# do flags and annotations correspond 1:1 by anon?
fa={f["anon_id"] for f in r62["flags"]}; an={a["anon_id"] for a in r62["annotations"]}
print("same anon set?", fa==an)
# check BZ-029/040/LY-537 anons in r63 mapping?
inv={v:k for k,v in hm.items()}
for cid in ["BZ-029","BZ-040","LY-537","YM-070"]:
    print(cid, "r63 anon:", inv.get(cid))
