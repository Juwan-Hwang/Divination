import json, pathlib
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round58')
mapping = json.load(open(base/'judging/host-mapping.json'))
rows = [json.loads(l) for l in open(base/'judging/judgeY-block1.jsonl')]
out = []
for i, r in enumerate(rows, 1):
    cid = mapping[r['anon_id']]
    pred = json.load(open(base/'predictions'/f'{cid}.json'))
    out.append(f"=== {i} {r['anon_id']} {cid} ===")
    out.append("PRED: " + pred.get('prediction_text',''))
    out.append("OUTCOME: " + r.get('outcome_record',''))
    if r.get('carry_note'): out.append("CARRY: " + r['carry_note'])
    if r.get('editor_note'): out.append("EDITOR: " + r['editor_note'])
    out.append("")
open(base/'judgeY-block1-digest-ebd1521b.txt','w').write("\n".join(out))
print(len(rows))
