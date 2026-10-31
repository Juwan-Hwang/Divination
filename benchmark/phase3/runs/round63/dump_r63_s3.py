import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
batches = json.loads((base/"runs/round63/batches.json").read_text())
ids = batches["B07"]+batches["B08"]+batches["B09"]
assert len(ids)==60, len(ids)
out=[]
for cid in ids:
    p = base/"inputs-dev12"/f"{cid}.json"
    d = json.loads(p.read_text())
    out.append(d)
print(json.dumps(out, ensure_ascii=False, indent=1))
