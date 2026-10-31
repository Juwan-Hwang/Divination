import json, pathlib
P3 = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
block = P3/'runs/round89/judging/judgeX-block4.jsonl'
mapping = json.loads((P3/'runs/round89/judging/host-mapping.json').read_text())
rows = [json.loads(l) for l in block.read_text().splitlines() if l.strip()]
print('block rows:', len(rows))
out = []
missing = []
for r in rows:
    anon = r['anon_id']
    cid = mapping.get(anon)
    if cid is None:
        missing.append((anon, 'no mapping'))
        continue
    pf = P3/f'runs/round89/predictions/{cid}.json'
    if not pf.exists():
        missing.append((anon, f'no file {cid}'))
        continue
    pj = json.loads(pf.read_text())
    pt = pj.get('prediction_text')
    out.append({'anon_id': anon, 'case_id': cid, 'outcome': r['outcome_record'], 'prediction_text': pt, 'pred_keys': sorted(pj.keys())})
print('resolved:', len(out), 'missing:', missing)
with open(P3/'runs/round89/x4_dump.jsonl', 'w') as f:
    for o in out:
        f.write(json.dumps(o, ensure_ascii=False) + '\n')
for o in out:
    print(o['anon_id'], o['case_id'], 'pt_len=', len(o['prediction_text']) if o['prediction_text'] else None)
