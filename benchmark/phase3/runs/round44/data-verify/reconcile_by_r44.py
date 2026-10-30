import json
def load(p): return [json.loads(l) for l in open(p)]
rev = load('expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl')
stock = load('runs/round38/data-verify/bianyi-stock-r38.jsonl')
yuce = load('runs/round38/data-verify/yuce-stock-r38.jsonl')
print('stock rows:', len(stock), 'keys:', sorted(stock[0].keys())[:12])
print('yuce rows:', len(yuce), 'first id:', yuce[0].get('id'))
def key3(r):
    return (r.get('subject',''), r.get('question_or_topic',''), r.get('asked_at',''))
def key2(r):
    return (r.get('subject',''), r.get('asked_at',''))
smap = {}
for r in stock: smap.setdefault(key3(r), []).append(r.get('id'))
ymap = {}
for r in yuce: ymap.setdefault(key3(r), []).append(r.get('id'))
used=set()
for l in open('runs/round43/data-verify/used-union-r43.jsonl'):
    d=json.loads(l); used.add(d.get('id') or d.get('case_id'))
by_rows=[r for r in rev if r['id'].startswith('BY-')]
yx_rows=[r for r in rev if r['id'].startswith('YX-')]
hit3=hit2=miss=0; matched_ids=[]
for r in by_rows:
    if key3(r) in smap: hit3+=1; matched_ids += smap[key3(r)]
    elif key2(r) in {key2(s) for s in stock}: hit2+=1
    else: miss+=1
print(f'BY rows {len(by_rows)}: stock 3-key match {hit3}, 2-key only {hit2}, no match {miss}')
print('matched stock ids sample:', matched_ids[:10], '... total', len(matched_ids))
print('matched stock ids in used union:', sum(1 for i in matched_ids if i in used))
# YX vs yuce stock
yhit=0
for r in yx_rows:
    if key3(r) in ymap: yhit+=1
print(f'YX rows {len(yx_rows)}: yuce-stock 3-key match {yhit}')
# unmatched BY rows detail
stockk={key3(s) for s in stock}
unm=[r['id'] for r in by_rows if key3(r) not in stockk]
print('unmatched BY ids:', unm[:20], 'count', len(unm))
