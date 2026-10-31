#!/usr/bin/env python3
"""R88 开轮已用并集复算（照 R85/R86/R87 开轮五源口径，holdout 范围扩至 3–31）：
dev inputs-dev12 + phase2 splits2 holdout2 + holdout3-31 金标 id + holdout inputs 卡 id + 顶层 inputs6-10 卡 id。
只读 id 集，不打开金标正文内容作判定（仅取 id 字段）。预期并集 1248（R87 封存后登记）。"""
import json, glob, os

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
os.chdir(BASE)

def card_ids(pattern):
    return {os.path.basename(p)[:-5] for p in glob.glob(pattern)}

def gold_ids(path):
    out = set()
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                out.add(json.loads(line)['id'])
    return out

sources = {}
sources['dev'] = card_ids('inputs-dev12/*.json')
with open('../phase2/splits2.json') as f:
    h2 = set(json.load(f)['holdout2'])
sources['holdout2'] = h2
g = set(); inp = set()
for n in range(3, 32):
    d = f'holdout{n}'
    if os.path.exists(f'{d}/test_gold.jsonl'):
        g |= gold_ids(f'{d}/test_gold.jsonl')
    inp |= card_ids(f'{d}/inputs/*.json')
    inp |= card_ids(f'{d}-inputs/*.json')
sources['holdout3-31-gold'] = g
sources['holdout-inputs'] = inp
top = set()
for n in range(6, 11):
    top |= card_ids(f'inputs{n}/*.json')
sources['inputs6-10'] = top

union = set()
for k, v in sources.items():
    print(k, len(v))
    union |= v
print('UNION', len(union))
assert len(union) == 1248, len(union)
with open('runs/round88/used-ids-r88.json', 'w') as f:
    json.dump(sorted(union), f, ensure_ascii=False, indent=0)
print('written runs/round88/used-ids-r88.json')
