import json, pathlib
base=pathlib.Path.home()/'workspace/divination/benchmark/phase3/runs/round35'
packet=json.loads((base/'judging/packet3.json').read_text())
mapping=json.loads((base/'judging/host-mapping.json').read_text())
out=[]
for i, item in enumerate(packet):
    anon=item['anon_id']
    cid=mapping[anon]
    pred=json.loads((base/'predictions'/f'{cid}.json').read_text())
    # find prediction_text field
    pt = pred.get('prediction_text') or pred.get('prediction') or ''
    if isinstance(pt, dict):
        pt=json.dumps(pt, ensure_ascii=False)
    out.append({'idx':i,'anon_id':anon,'case_id':cid,'prediction_text':pt,'outcome_record':item['outcome_record'],'pred_keys':list(pred.keys())})
    if i==0:
        print(json.dumps(pred, ensure_ascii=False)[:3000])
(base/'judging'/'yb3_dump.json').write_text(json.dumps(out, ensure_ascii=False, indent=1))
print('written', len(out))
# stats lengths
for o in out[:5]:
    print(o['anon_id'], o['case_id'], len(o['prediction_text']), o['prediction_text'][:200])
