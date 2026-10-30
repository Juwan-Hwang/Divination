import json, pathlib
base = pathlib.Path.home() / 'workspace/divination/benchmark/phase3/runs/round35'
packet = json.loads((base/'judging/packet2.json').read_text())
mapping = json.loads((base/'judging/host-mapping.json').read_text())
out = base/'judging/review-yb2-6c173.txt'
with out.open('w') as f:
    for i, p in enumerate(packet):
        cid = mapping[p['anon_id']]
        pred = json.loads((base/f'predictions/{cid}.json').read_text())
        f.write(f"===== [{i+1}/122] anon={p['anon_id']} case={cid} =====\n")
        f.write(f"PREDICTION_TEXT: {pred.get('prediction_text','')}\n")
        f.write(f"OUTCOME: {p['outcome_record']}\n\n")
print('written', out, 'entries', len(packet))
