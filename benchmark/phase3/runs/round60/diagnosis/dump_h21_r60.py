import json, sys, os
B='/home/hatch/workspace/divination/benchmark/phase3'
hm=json.load(open(B+'/runs/round60/acceptance/judging/host-mapping.json'))
rev_o={v:k for k,v in hm['ours'].items()}; rev_m={v:k for k,v in hm['master'].items()}
def load(fn):
    d={}
    for l in open(B+'/runs/round60/acceptance/judging/'+fn,encoding='utf-8'):
        r=json.loads(l); d[r['anon_id']]=r
    return d
O1,O2,M1,M2=load('judgeO1.jsonl'),load('judgeO2.jsonl'),load('judgeM1.jsonl'),load('judgeM2.jsonl')
gold={json.loads(l)['id']:json.loads(l) for l in open(B+'/holdout21/test_gold.jsonl',encoding='utf-8')}
for cid in sys.argv[1:]:
    p=json.load(open(B+f'/runs/round60/acceptance/predictions/{cid}.json',encoding='utf-8'))
    inp=json.load(open(B+f'/holdout21/inputs/{cid}.json',encoding='utf-8'))
    o1,o2,m1,m2=O1[rev_o[cid]],O2[rev_o[cid]],M1[rev_m[cid]],M2[rev_m[cid]]
    def avg(a,b,k): return (a[k]+b[k])/2
    print('='*20, cid, inp.get('tradition'), 'Q:', inp.get('question'))
    print('SUB ours dir %.2f claims %.2f tim %.2f | master dir %.2f claims %.2f tim %.2f'%(
      avg(o1,o2,'direction'),avg(o1,o2,'claims'),avg(o1,o2,'timing'),avg(m1,m2,'direction'),avg(m1,m2,'claims'),avg(m1,m2,'timing')))
    print('--PRED--', json.dumps(p,ensure_ascii=False)[:6000])
    print('--GOLD MASTER--', gold[cid]['master_prediction'][:3500])
    print('--OUTCOME--', gold[cid]['outcome_record'][:2000])
    print('--O1--', o1['reason'][:1500]); print('--O2--', o2['reason'][:1500])
    print('--M1--', m1['reason'][:1200]); print('--M2--', m2['reason'][:1200])
    print('--ANCHORS--', json.dumps(inp.get('anchors'),ensure_ascii=False)[:1500])
