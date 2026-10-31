# W53 (R90) 六壬 W 监测复算脚本：结构化解析负例清单、自洽复算、逐例材料抽取、聚合计数。
# 只读输入：lr-negatives-dev90.json、runs/round90/predictions/<id>.json、
#           benchmark/phase3/inputs-dev12/<id>.json、runs/round90/final-scores.json 的 ours_sub 行。
import json, math, os

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
NEG = json.load(open(f'{BASE}/runs/round90/diagnosis/lr-negatives-dev90.json'))
FS = json.load(open(f'{BASE}/runs/round90/final-scores.json'))

negs = NEG['negatives']
assert NEG['n_negative'] == len(negs) == 24, len(negs)
assert NEG['n_liuren_total'] == 30
for n in negs:
    assert abs((n['ours'] - n['master']) - n['pair_diff']) < 1e-9, n['case_id']
print('self-consistency: pair_diff == ours - master for 24/24')

dev8 = [n for n in negs if n['in_dev8']]
lr3 = [n for n in negs if not n['in_dev8']]
for name, seg in [('dev8', dev8), ('LR3', lr3), ('merged', negs)]:
    diffs = sorted(n['pair_diff'] for n in seg)
    s = sum(diffs)
    med = diffs[len(diffs)//2] if len(diffs) % 2 else (diffs[len(diffs)//2-1] + diffs[len(diffs)//2]) / 2
    print(f'{name}: n={len(seg)} sum={s:.2f} mean={s/len(seg):.3f} median={med:.3f}')

# ---- extract per-case materials to a working file (unique name, inside round90/diagnosis) ----
out = []
for n in negs:
    cid = n['case_id']
    pred = json.load(open(f'{BASE}/runs/round90/predictions/{cid}.json'))
    card = json.load(open(f'{BASE}/inputs-dev12/{cid}.json'))
    ctx = card.get('context', {})
    out.append({
        'case_id': cid, 'in_dev8': n['in_dev8'], 'pair_diff': n['pair_diff'],
        'ours': n['ours'], 'master': n['master'],
        'ours_sub': FS['ours_sub'].get(cid),
        'question': ctx.get('question'), 'setting': ctx.get('setting'),
        'attachments': ctx.get('attachments'),
        'provenance': card.get('provenance'),
        'prediction_text': pred.get('prediction_text'),
        'basis': pred.get('basis'),
        'confidence': pred.get('confidence'),
    })
with open(f'{BASE}/runs/round90/diagnosis/w53_r90_extract.json', 'w') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print('extract written: w53_r90_extract.json,', len(out), 'cases')
for o in out:
    print(o['case_id'], 'sub=', o['ours_sub'])

# ---- W53 fresh codings (per W-CHARTER §1.2 priority H->C->B->A->W->D/E) ----
# code: main label; hard: W hard-core flag (explicit weight language in basis/prediction_text)
CODING = {
 'LR2-013': ('D', False), 'LR2-014': ('D', False), 'LR2-015': ('W', True),
 'LR2-016': ('D', False), 'LR2-017': ('W', True), 'LR2-019': ('D', False),
 'LR2-021': ('不可判定', False), 'LR2-022': ('D', False), 'LR2-023': ('C*', False),
 'LR2-024': ('C*', False),
 'LR3-002': ('W', True), 'LR3-006': ('C*', False), 'LR3-008': ('D', False),
 'LR3-010': ('UNC', False), 'LR3-101': ('不可判定', False), 'LR3-104': ('不可判定', False),
 'LR3-107': ('不可判定', False), 'LR3-110': ('D', False), 'LR3-114': ('不可判定', False),
 'LR3-116': ('不可判定', False),
 'OC-026': ('D', False), 'OC-027': ('C*', False), 'OC-029': ('不可判定', False),
 'OC-030': ('D', False),
}
assert set(CODING) == {n['case_id'] for n in negs}
from collections import Counter
def agg(seg):
    c = Counter(CODING[n['case_id']][0] for n in seg)
    w = sum(1 for n in seg if CODING[n['case_id']][0] == 'W')
    hard = sum(1 for n in seg if CODING[n['case_id']][1])
    coded = sum(1 for n in seg if CODING[n['case_id']][0] not in ('不可判定', 'UNC'))
    return c, w, hard, coded
def se(p, n):
    return math.sqrt(p * (1 - p) / n) * 100 if n else float('nan')
for name, seg in [('dev8', dev8), ('LR3', lr3), ('merged', negs)]:
    c, w, hard, coded = agg(seg)
    print(f'[{name}] n={len(seg)} coded={coded} counts={dict(c)} W={w} hard={hard}')
    print(f'   W/negatives {w}/{len(seg)} = {w/len(seg)*100:.1f}% (SE {se(w/len(seg), len(seg)):.1f}pp); '
          f'W/coded {w}/{coded} = {w/coded*100:.1f}% (SE {se(w/coded, coded):.1f}pp)')
c, w, hard, coded = agg(negs)
print(f'[merged /30] W {w}/30 = {w/30*100:.1f}% (SE {se(w/30, 30):.1f}pp); hard {hard}/30 = {hard/30*100:.1f}%')
uncodable = [n['case_id'] for n in negs if CODING[n['case_id']][0] in ('不可判定', 'UNC')]
print('uncodable (incl UNC):', len(uncodable), uncodable)
print('D cases:', [n['case_id'] for n in negs if CODING[n['case_id']][0] == 'D'])
