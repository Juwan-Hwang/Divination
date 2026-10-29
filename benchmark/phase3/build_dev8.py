#!/usr/bin/env python3
"""Build dev8 pool + seal holdout9 (host tooling, 2026-10-29).
dev8 = dev7 (334) + holdout8-used (28) + expansion7 dev-adds (50).
holdout9 = 28 fresh low-contamination A cases from expansion7
(liuren 12 + yiyin 8 + bushi-quanshu 8), sealed before any use.
"""
import json, os, hashlib, shutil, datetime

P3 = 'benchmark/phase3'
def jl(p):
    return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]

exp7 = []
for sub in ('yiyin', 'yiyin2', 'liuren', 'bushi-quanshu'):
    for r in jl(f'{P3}/expansion7/{sub}/cases.jsonl'):
        r['_sub'] = sub
        exp7.append(r)
assert len(exp7) == 78, len(exp7)

TR = {'六壬': 'liuren', '筮占': 'liuyao'}
def outcome_text(r):
    o = r.get('outcome')
    return o.get('description', '') if isinstance(o, dict) else str(o or '')

def pick(sub, n):
    rows = [r for r in exp7 if r['_sub'] == sub and r['contamination'] == 'low' and r.get('outcome_grade') == 'A']
    rows.sort(key=lambda r: r['id'])
    assert len(rows) >= n, (sub, len(rows))
    return rows[:n]

hold = pick('liuren', 12) + pick('yiyin', 8) + pick('bushi-quanshu', 8)
hold_ids = [r['id'] for r in hold]
assert len(hold_ids) == 28 and len(set(hold_ids)) == 28
dev_adds = [r for r in exp7 if r['id'] not in hold_ids]
assert len(dev_adds) == 50

gold8 = jl(f'{P3}/holdout8/test_gold.jsonl')
assert len(gold8) == 28

# holdout9 gold + seal
os.makedirs(f'{P3}/holdout9', exist_ok=True)
with open(f'{P3}/holdout9/test_gold.jsonl', 'w', encoding='utf-8') as f:
    for r in hold:
        rr = {k: v for k, v in r.items() if not k.startswith('_')}
        f.write(json.dumps(rr, ensure_ascii=False) + '\n')
sha = hashlib.sha256(open(f'{P3}/holdout9/test_gold.jsonl', 'rb').read()).hexdigest()
now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat()
with open(f'{P3}/holdout9-seal-log.md', 'w', encoding='utf-8') as f:
    f.write(f'# holdout9 封存日志\n\n- {now} 封存：28 例（expansion7 全新 A 级、全 low 污染：六壬 12＋易隐 8＋卜筮全书 8），金标 SHA-256 {sha}，状态未开封。选择规则见 SEALED.md 与 build_dev8.py。\n')
with open(f'{P3}/holdout9/SEALED.md', 'w', encoding='utf-8') as f:
    f.write('# holdout9 封存说明\n\n- 来源：expansion7（易隐/六壬指南续抽/卜筮全书），全部 A 级、low 污染、从未入任何 dev 池。\n- 构成：六壬 dated 课案 12、易隐六爻 8、卜筮全书六爻 8。\n- 开封条件：dev8 上平台成立后按预注册开封；开封前验金标 SHA 与 seal-log 一致。\n')

# roster8 additions: holdout8-used 28 + expansion7 dev-adds 50
roster = []
for g in gold8:
    roster.append({'id': g['id'], 'outcome_record': outcome_text(g),
                   'tradition': g.get('tradition', ''), 'contamination': g.get('contamination', ''),
                   'source_tier': 'holdout8-used'})
for r in dev_adds:
    roster.append({'id': r['id'], 'outcome_record': outcome_text(r),
                   'tradition': TR.get(r.get('tradition', ''), r.get('tradition', '')),
                   'contamination': r.get('contamination', ''), 'source_tier': f"expansion7-{r['_sub']}"})
with open(f'{P3}/roster8-additions.jsonl', 'w', encoding='utf-8') as f:
    for r in roster:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')

# inputs8: dev7 334 + holdout8 inputs + expansion7 dev-add inputs
os.makedirs(f'{P3}/inputs8', exist_ok=True)
n_copy = 0
for f in os.listdir(f'{P3}/inputs7'):
    shutil.copy(f'{P3}/inputs7/{f}', f'{P3}/inputs8/{f}'); n_copy += 1
def find_input(cid):
    import glob
    for pat in (f'{P3}/expansion6/*/inputs/{cid}.json', f'{P3}/expansion7/*/inputs/{cid}.json'):
        g = glob.glob(pat)
        if g: return g[0]
    raise FileNotFoundError(cid)
for r in roster:
    shutil.copy(find_input(r['id']), f"{P3}/inputs8/{r['id']}.json"); n_copy += 1

dev7_ids = json.load(open(f'{P3}/splits7.json'))['dev7']
dev8_ids = sorted(dev7_ids + [r['id'] for r in roster])
splits = {'dev8': dev8_ids, 'holdout9': sorted(hold_ids),
          'counts': {'dev8': len(dev8_ids), 'holdout9': len(hold_ids), 'inputs8_files': n_copy},
          'holdout9_gold_sha256': sha}
json.dump(splits, open(f'{P3}/splits8.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('dev8:', len(dev8_ids), 'holdout9:', len(hold_ids), 'inputs8:', n_copy, 'sha:', sha)
print('holdout9 ids:', sorted(hold_ids))
