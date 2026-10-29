#!/usr/bin/env python3
"""Build dev9 pool + seal holdout10 (host tooling, 2026-10-30).

Declared composition (STAGE-SUMMARY-10 continuation list, fixed before build):
- dev9 = dev8 (412) + expansion8 YM dev share (56) + expansion8 DT 7 (medium,
  declared) + expansion9 LR3 dev share (A-low remainder after holdout pick).
- holdout10 = 29 fresh A-grade low cases, sealed before any use:
  YM systematic 14 (sorted by id, every 5th of 70) + LR3 systematic 12
  (evenly spaced over sorted A-low ids) + DS 3 (all).
Selection is by fixed positional rule only; no outcome/score information used.
"""
import json, os, hashlib, shutil, datetime, glob

P3 = 'benchmark/phase3'

def jl(p):
    return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]

def outcome_text(r):
    o = r.get('outcome')
    return o.get('description', '') if isinstance(o, dict) else str(o or '')

splits8 = json.load(open(f'{P3}/splits8.json', encoding='utf-8'))
dev8_ids = splits8['dev8']
assert len(dev8_ids) == 412

# --- expansion8 sources ---
ym = jl(f'{P3}/expansion8/yimao/cases.jsonl')
assert len(ym) == 70 and all(r['outcome_grade'] == 'A' and r['contamination'] == 'low' for r in ym)
ym.sort(key=lambda r: r['id'])
ym_hold = [ym[i] for i in range(0, 70, 5)]
assert len(ym_hold) == 14
ym_hold_ids = {r['id'] for r in ym_hold}
ym_dev = [r for r in ym if r['id'] not in ym_hold_ids]
assert len(ym_dev) == 56

dt = jl(f'{P3}/expansion8/duanyi-tianji/cases.jsonl')
assert len(dt) == 7 and all(r['outcome_grade'] == 'A' and r['contamination'] == 'medium' for r in dt)

ds = jl(f'{P3}/expansion8/ditian-sui/cases.jsonl')
assert len(ds) == 3 and all(r['outcome_grade'] == 'A' and r['contamination'] == 'low' for r in ds)

# --- expansion9 liuren remainder ---
lr = []
for sub in ('liuren-chen1', 'liuren-chen2'):
    for r in jl(f'{P3}/expansion9/{sub}/cases.jsonl'):
        r['_sub'] = sub
        lr.append(r)
# Host adjudication (expansion9/HOST-ADJUDICATION.md): LR3-106/108 downgraded B
# (excluded); LR3-103 medium already out; LR3-010 A/low but dev-only.
EXCLUDE = {'LR3-106', 'LR3-108'}
DEV_ONLY = {'LR3-010'}
lr_all = [r for r in lr if r.get('outcome_grade') == 'A' and r.get('contamination') == 'low'
          and r.get('holdout_eligible') is True and r['id'] not in EXCLUDE]
lr_a = [r for r in lr_all if r['id'] not in DEV_ONLY]
assert len(lr_a) >= 16, f'LR3 A-low holdout-eligible only {len(lr_a)}; host decision needed'
lr_a.sort(key=lambda r: r['id'])
n_lr = len(lr_a)
pick_idx = sorted({round(i * (n_lr - 1) / 11) for i in range(12)})
assert len(pick_idx) == 12, pick_idx
lr_hold = [lr_a[i] for i in pick_idx]
lr_hold_ids = {r['id'] for r in lr_hold}
lr_dev = [r for r in lr_all if r['id'] not in lr_hold_ids]

hold = ym_hold + lr_hold + ds
hold_ids = [r['id'] for r in hold]
assert len(hold_ids) == 29 and len(set(hold_ids)) == 29, hold_ids
dev_adds = ym_dev + dt + lr_dev

# no id may collide with dev8 or holdout9-used ids
used = set(dev8_ids) | set(splits8['holdout9'])
assert not (set(hold_ids) & used), set(hold_ids) & used
assert not ({r['id'] for r in dev_adds} & used)

# --- holdout10 gold + seal ---
os.makedirs(f'{P3}/holdout10', exist_ok=True)
with open(f'{P3}/holdout10/test_gold.jsonl', 'w', encoding='utf-8') as f:
    for r in hold:
        rr = {k: v for k, v in r.items() if not k.startswith('_')}
        f.write(json.dumps(rr, ensure_ascii=False) + '\n')
sha = hashlib.sha256(open(f'{P3}/holdout10/test_gold.jsonl', 'rb').read()).hexdigest()
now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat()
with open(f'{P3}/holdout10-seal-log.md', 'w', encoding='utf-8') as f:
    f.write(f'# holdout10 封存日志\n\n- {now} 封存：29 例（全新 A 级、全 low 污染：易冒六爻 14＋六壬指南续抽 {len(lr_hold)}＋滴天髓八字 3），金标 SHA-256 {sha}，状态未开封。选择规则见 SEALED.md 与 build_dev9.py。\n')
with open(f'{P3}/holdout10/SEALED.md', 'w', encoding='utf-8') as f:
    f.write('# holdout10 封存说明\n\n'
            '- 来源：expansion8（易冒、滴天髓阐微）＋expansion9（大六壬占验指南续抽），全部 A 级、low 污染、从未入任何 dev 池、从未被任何轮次使用。\n'
            '- 构成：易冒六爻 14（YM 70 例按 id 排序每第 5 例系统抽样）＋六壬 12（LR3 A-low 全集按 id 排序等距抽样）＋滴天髓八字 3（全收）。\n'
            '- 选择只用固定位置规则，未使用任何结局/分数信息。\n'
            '- 开封条件：dev9 上平台成立后按预注册开封；开封前验金标 SHA 与 seal-log 一致。\n')

# --- roster9 additions (dev-bound only; holdout outcomes stay sealed in gold) ---
TR = {'yimao': 'liuyao', 'duanyi-tianji': 'liuyao'}
roster = []
for r in ym_dev:
    roster.append({'id': r['id'], 'outcome_record': outcome_text(r), 'tradition': 'liuyao',
                   'contamination': 'low', 'source_tier': 'expansion8-yimao'})
for r in dt:
    roster.append({'id': r['id'], 'outcome_record': outcome_text(r), 'tradition': 'liuyao',
                   'contamination': 'medium', 'source_tier': 'expansion8-duanyi-tianji'})
for r in lr_dev:
    roster.append({'id': r['id'], 'outcome_record': outcome_text(r), 'tradition': 'liuren',
                   'contamination': 'low', 'source_tier': f"expansion9-{r['_sub']}"})
with open(f'{P3}/roster9-additions.jsonl', 'w', encoding='utf-8') as f:
    for r in roster:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')

# --- inputs-dev9: inputs8 copies + new dev inputs ---
os.makedirs(f'{P3}/inputs-dev9', exist_ok=True)
n_copy = 0
for fn in os.listdir(f'{P3}/inputs8'):
    shutil.copy(f'{P3}/inputs8/{fn}', f'{P3}/inputs-dev9/{fn}'); n_copy += 1

def find_input(cid):
    for pat in (f'{P3}/expansion8/*/inputs/{cid}.json', f'{P3}/expansion9/*/inputs/{cid}.json'):
        g = glob.glob(pat)
        if g: return g[0]
    raise FileNotFoundError(cid)

for r in roster:
    shutil.copy(find_input(r['id']), f"{P3}/inputs-dev9/{r['id']}.json"); n_copy += 1

# --- inputs-r28: dev9 inputs with the 47 C-track cases switched to inputs9 versions ---
SWITCH = sorted(fn[:-5] for fn in os.listdir(f'{P3}/inputs9') if fn.endswith('.json'))
assert len(SWITCH) == 47 and all(i in dev8_ids for i in SWITCH)
os.makedirs(f'{P3}/inputs-r28', exist_ok=True)
for fn in os.listdir(f'{P3}/inputs-dev9'):
    shutil.copy(f'{P3}/inputs-dev9/{fn}', f'{P3}/inputs-r28/{fn}')
for cid in SWITCH:
    shutil.copy(f'{P3}/inputs9/{cid}.json', f'{P3}/inputs-r28/{cid}.json')

dev9_ids = sorted(dev8_ids + [r['id'] for r in roster])
splits = {'dev9': dev9_ids, 'holdout10': sorted(hold_ids),
          'counts': {'dev9': len(dev9_ids), 'holdout10': len(hold_ids),
                     'inputs_dev9_files': n_copy, 'inputs_r28_switched': len(SWITCH)},
          'holdout10_gold_sha256': sha}
json.dump(splits, open(f'{P3}/splits9.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

os.makedirs(f'{P3}/dev9-build', exist_ok=True)
with open(f'{P3}/dev9-build/BUILD.md', 'w', encoding='utf-8') as f:
    f.write('# dev9 组池＋holdout10 封存记录（2026-10-30）\n\n')
    f.write(f'- dev9 n={len(dev9_ids)}＝dev8 412＋YM {len(ym_dev)}＋DT 7（medium，声明在案）＋LR3 {len(lr_dev)}。\n')
    f.write(f'- holdout10 n=29：YM 抽样 {[r["id"] for r in ym_hold]}；LR3 抽样 {[r["id"] for r in lr_hold]}（A-low 全集 {n_lr} 例等距 12）；DS {[r["id"] for r in ds]}。\n')
    f.write(f'- LR3 主持裁决后 A-low 留出合格 {n_lr} 例（裁决见 expansion9/HOST-ADJUDICATION.md：LR3-106/108 降 B 排除、LR3-010 dev-only），入 dev {len(lr_dev)} 例（含 dev-only 1）。\n')
    f.write(f'- inputs-r28 切换子集 47 例（inputs9 补录版）：{SWITCH}。\n')
    f.write(f'- 金标 SHA-256 {sha}。\n')
print('dev9:', len(dev9_ids), 'holdout10:', len(hold_ids), 'inputs-dev9:', n_copy, 'sha:', sha)
print('holdout10 ids:', sorted(hold_ids))
print('dev adds:', len(roster))
