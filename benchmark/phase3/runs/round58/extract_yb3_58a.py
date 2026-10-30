import json, pathlib
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round58')
rows = [json.loads(l) for l in (base/'judging/judgeY-block3.jsonl').read_text().splitlines() if l.strip()]
mp = json.loads((base/'judging/host-mapping.json').read_text())
out = []
for r in rows:
    cid = mp[r['anon_id']]
    pred = json.loads((base/'predictions'/f'{cid}.json').read_text())
    pt = pred.get('prediction_text') or pred
    out.append({'anon_id': r['anon_id'], 'case_id': cid, 'outcome': r['outcome_record'], 'prediction_text': pt})
(base/'yb3_texts_58a.json').write_text(json.dumps(out, ensure_ascii=False, indent=1))
print(len(out))
