import json, pathlib
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
acc = base/'runs/round91/acceptance'
hm = json.load(open(acc/'judging/host-mapping.json'))
fs = json.load(open(acc/'judging/final-scores-h33.json'))
gold = {json.loads(l)['id']: json.loads(l) for l in open(base/'holdout33/test_gold.jsonl')}
def load_j(name, side):
    m = hm[side]
    out={}
    for l in open(acc/'judging'/name):
        d=json.loads(l); out[m[d['anon_id']]]=d
    return out
O1=load_j('judgeO1.jsonl','ours'); O2=load_j('judgeO2.jsonl','ours')
M1=load_j('judgeM1.jsonl','master'); M2=load_j('judgeM2.jsonl','master')
ids = sorted(fs['per_case'].keys(), key=lambda x:(x.split('-')[0], x))
lines=[]
for cid in ids:
    p=json.load(open(acc/'predictions'/f'{cid}.json'))
    inp=json.load(open(base/'holdout33/inputs'/f'{cid}.json'))
    g=gold[cid]
    lines.append(f"\n===== {cid} ours={fs['per_case'][cid]['ours']} master={fs['per_case'][cid]['master']} diff={fs['per_case'][cid]['diff']}")
    lines.append(f"PRED: {p.get('prediction_text','')}")
    lines.append(f"BASIS: {p.get('basis','')}")
    lines.append(f"TRIGGER: {json.dumps(p.get('trigger',{}), ensure_ascii=False)}")
    for nm,J in (('O1',O1),('O2',O2)):
        d=J[cid]; lines.append(f"{nm}: dir={d['direction']} claims={d['claims']} timing={d['timing']} total={d['total']} gap={d.get('gap_note','')}")
    for nm,J in (('M1',M1),('M2',M2)):
        d=J[cid]; lines.append(f"{nm}: dir={d['direction']} claims={d['claims']} timing={d['timing']} total={d['total']} gap={d.get('gap_note','')}")
    lines.append(f"GOLD_MASTER: {g['master_prediction']}")
    lines.append(f"GOLD_OUTCOME: {g['outcome_record']}")
    lines.append(f"INPUT_Q: {inp.get('question','')} | subject={inp.get('subject','')} | anchors={json.dumps(inp.get('anchors',{}), ensure_ascii=False)}")
    # verify judge means vs final
    om=(O1[cid]['total']+O2[cid]['total'])/2; mm=(M1[cid]['total']+M2[cid]['total'])/2
    assert abs(om-fs['per_case'][cid]['ours'])<0.26, (cid,om)
    assert abs(mm-fs['per_case'][cid]['master'])<0.26, (cid,mm)
out = pathlib.Path(__file__).parent/'diag_compact_h33_r91.txt'
out.write_text('\n'.join(lines))
print('cases', len(ids), 'written', out)
# aggregates: systems_used, trigger, eighth-section mentions
import re
from collections import Counter
syscnt=Counter(); trig=Counter(); eighth=[]
for cid in ids:
    p=json.load(open(acc/'predictions'/f'{cid}.json'))
    b=p.get('basis','')
    m=re.search(r'systems_used[:：]\s*([^。；\n]+)', b) or re.search(r'systems_used[:：]\s*([^。；\n]+)', p.get('prediction_text',''))
    syscnt[m.group(1).strip() if m else 'NO systems_used in basis']+=1
    t=p.get('trigger',{})
    trig[(t.get('changed_main'),t.get('reserve_used'),t.get('disputed'))]+=1
    e8 = ('第八节' in b) or ('R80' in b) or ('做功主线' in b) or ('功量' in b)
    eighth.append((cid, '第八节' in b, 'R80' in b, '做功主线' in b, '功量' in b, '功量清单' in b, '功量核' in b, '功量核算' in b))
print('systems:', syscnt)
print('trigger combos:', trig)
print('eighth (id, 第八节,R80,做功主线,功量,功量清单,功量核,功量核算):')
for e in eighth: print(e)
