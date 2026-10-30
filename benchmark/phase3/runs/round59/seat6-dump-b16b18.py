import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
batches=json.loads((base/"runs/round59/batches.json").read_text())
ids=[]
for b in ["B16","B17","B18"]:
    ids+=batches[b]
for cid in ids:
    d=json.loads((base/f"inputs-dev12/{cid}.json").read_text())
    out={k:d.get(k) for k in ("id","tradition","system","master","era","subject","context","language") if k in d}
    notes=d.get("notes") or {}
    if isinstance(notes,dict):
        keep={k:notes.get(k) for k in ("tags","comment") if notes.get(k)}
        if keep: out["notes_keep"]=keep
    print(json.dumps(out,ensure_ascii=False))
    print("---CASE-END---")
