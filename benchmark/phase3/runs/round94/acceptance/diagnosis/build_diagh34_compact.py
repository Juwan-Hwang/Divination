import json, os
BASE='/home/hatch/workspace/divination/benchmark/phase3'
scores=json.load(open(f'{BASE}/runs/round94/acceptance/judging/final-scores-h34.json'))
gold={}
for line in open(f'{BASE}/holdout34/test_gold.jsonl'):
    line=line.strip()
    if line:
        g=json.loads(line); gold[g['id']]=g
ids=sorted(scores['per_case'].keys())
out=[]
for cid in ids:
    pred=json.load(open(f'{BASE}/runs/round94/acceptance/predictions/{cid}.json'))
    inp=json.load(open(f'{BASE}/holdout34/inputs/{cid}.json'))
    g=gold[cid]
    sc=scores['per_case'][cid]
    out.append(f"===== {cid} ours={sc['ours']} master={sc['master']} diff={sc['diff']} tradition={inp.get('tradition')} =====")
    out.append(f"[Q] {inp.get('question')} | subject={inp.get('subject')} | setting={inp.get('setting')}")
    out.append(f"[ANCHORS] {json.dumps(inp.get('anchors'),ensure_ascii=False)}")
    out.append(f"[PRED] {pred.get('prediction_text')}")
    out.append(f"[BASIS] {pred.get('basis')}")
    out.append(f"[TRIGGER] {json.dumps(pred.get('trigger'),ensure_ascii=False)} conf={pred.get('confidence')}")
    out.append(f"[MASTER] {g.get('master_prediction')}")
    out.append(f"[OUTCOME] {g.get('outcome_record')}")
    out.append('')
open(f'{BASE}/runs/round94/acceptance/diagnosis/diagh34_compact.txt','w').write('\n'.join(out))
print('cases',len(ids))
print('gold ids match', set(gold)==set(ids))
