import json, pathlib
base=pathlib.Path.home()/'workspace/divination/benchmark/phase3/inputs-dev12'
ids=['LY-614','LY-615','LY-616','LY-617','LY-618','LY-619','LY-620','LY-621','LY-622','LY-623','LY-624','LY-625','LY-626','LY-627','LY-628','LY-629','MH-001','MH-002','MH-003','MH-006']
for cid in ids:
    d=json.loads((base/f'{cid}.json').read_text())
    ctx=d.get('context',{})
    # strip notes/provenance
    print(f'===== {cid} tradition={d.get("tradition")} subject={d.get("subject")} =====')
    print(json.dumps(ctx, ensure_ascii=False, indent=1))
