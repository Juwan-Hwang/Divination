import json, pathlib
base=pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round91')
mapping=json.loads((base/'judging/host-mapping.json').read_text())
rows=[json.loads(l) for l in (base/'judging/judgeY-block4.jsonl').read_text().splitlines() if l.strip()]
for i,r in enumerate(rows,1):
    cid=mapping[r['anon_id']]
    p=json.loads((base/'predictions'/f"{cid}.json").read_text())
    txt=p.get('prediction_text','')
    print(f"=== {i} {r['anon_id']} {cid} ===")
    print(txt)
    print()
