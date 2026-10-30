import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
batches=json.loads((base/"runs/round57/batches.json").read_text())
ids=batches["B11"]+batches["B12"]
for cid in ids:
    p=base/"inputs-dev12"/f"{cid}.json"
    d=json.loads(p.read_text())
    print("="*80)
    print(cid)
    print(json.dumps(d, ensure_ascii=False, indent=1))
