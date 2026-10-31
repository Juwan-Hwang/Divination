import json, pathlib
base=pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round63')
rows=[json.loads(l) for l in open(base/'judging/judgeX-block1.jsonl')]
m=json.load(open(base/'judging/host-mapping.json'))
for r in rows:
    cid=m[r['anon_id']]
    p=json.load(open(base/'predictions'/f'{cid}.json'))
    print(f"=== {r['anon_id']} {cid} ===")
    print("OUTCOME:", r['outcome_record'])
    if 'carry_note' in r: print("CARRY:", r['carry_note'][:200])
    if 'editor_note' in r: print("EDITOR:", r['editor_note'])
    print("PREDICTION_TEXT:")
    print(p.get('prediction_text',''))
    print()
