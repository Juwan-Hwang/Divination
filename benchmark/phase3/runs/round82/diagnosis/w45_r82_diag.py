import json, math, statistics, re, pathlib
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
neg = json.load(open(base/'runs/round82/diagnosis/lr-negatives-dev82.json'))
fs = json.load(open(base/'runs/round82/final-scores.json'))
print('final-scores top keys:', list(fs.keys()))
for k,v in fs.items():
    if isinstance(v, dict) and k not in ('ours_axis2','ours_sub'):
        print(k, json.dumps(v, ensure_ascii=False)[:2000])
negs = neg['negatives']
ok_pd = all(abs((n['ours']-n['master'])-n['pair_diff'])<1e-9 for n in negs)
ok_ax = all(fs['ours_axis2'].get(n['case_id'])==n['ours'] for n in negs)
ok_sub = all(fs['ours_sub'].get(n['case_id'],{}).get('total')==n['ours'] for n in negs)
print('pair_diff self-consistent:', ok_pd, 'ours vs axis2:', ok_ax, 'ours vs sub.total:', ok_sub)
for seg, sel in [('dev8', lambda n: n['in_dev8']), ('LR3', lambda n: not n['in_dev8']), ('merged', lambda n: True)]:
    s=[n for n in negs if sel(n)]
    diffs=[n['pair_diff'] for n in s]
    print(seg, 'n_neg', len(s), 'sum', round(sum(diffs),4), 'mean', round(statistics.mean(diffs),4), 'median', statistics.median(diffs))
# labels: parse W44 (round81) table + h16 s2.1 + dev80 table for OC-029 / LR3-104
def parse_table(path):
    rows={}
    for line in open(path, encoding='utf-8'):
        m = re.match(r'\| ([A-Z0-9\-]+) \| (dev8|LR3) \| (-?[\d.]+) \| ([^|]+) \| ([^|]*) \| ([^|]*) \| ([^|]*) \|', line)
        if m: rows[m.group(1)] = dict(seg=m.group(2), label=m.group(4).strip(), note=m.group(5).strip(), book=m.group(6).strip())
    return rows
w44 = parse_table(base/'runs/round81/diagnosis/DIAG-LR-weight-dev81.md')
w43 = parse_table(base/'runs/round80/diagnosis/DIAG-LR-weight-dev80.md')
print('W44 rows', len(w44), 'W43 rows', len(w43))
for cid in ('OC-029','LR3-104','LR3-010','LR-001','LR2-020'):
    print(cid, 'W44:', w44.get(cid), 'W43:', w43.get(cid))
h16 = (base/'runs/round41/diagnosis/DIAG-LR-fresh-h16.md').read_text(encoding='utf-8')
for cid in ('OC-029','LR3-104'):
    for m in re.finditer(cid, h16):
        s=max(0,m.start()-200); print('h16 ctx', cid, ':', h16[s:m.end()+200].replace('\n',' '))
# inputs-dev12 provenance for the 24
import glob
for n in negs:
    cid=n['case_id']
    p = base/f'inputs-dev12/{cid}.json'
    try:
        card=json.load(open(p))
        prov = card.get('provenance') or {}
        print(cid, '|', prov.get('book'))
    except Exception as e:
        print(cid, 'ERR', e)
# assemble labels for r82 negs: W44 table first, else W43, else UNC-candidate
for n in negs:
    cid=n['case_id']
    src = w44.get(cid) or w43.get(cid)
    print('LABEL', cid, 'dev8' if n['in_dev8'] else 'LR3', n['pair_diff'], src['label'] if src else 'NONE', '|', src['note'] if src else '', '| src', 'W44' if cid in w44 else ('W43' if cid in w43 else 'none'))
