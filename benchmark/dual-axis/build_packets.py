#!/usr/bin/env python3
"""主持角组包脚本：把三组存档预测 + A 级结局记录组装成匿名评审包。
匿名化：抹去轮次/案例 id/轴一分数/版本信息，随机打乱顺序；映射仅主持角留存。
用法：python3 build_packets.py（须在 grading/outcome-availability.jsonl 落盘后运行）
"""
import json, os, random, sys

ROOT = os.path.expanduser('~/workspace/divination')
GROUPS = [
    ('round17_dev', 'benchmark/runs/round17/predictions'),
    ('round18_test', 'benchmark/runs/round18/predictions'),
    ('round1_dev', 'benchmark/runs/round1/predictions'),
]

grading = {}
with open(f'{ROOT}/benchmark/dual-axis/grading/outcome-availability.jsonl') as f:
    for line in f:
        r = json.loads(line)
        grading[r['id']] = r
assert len(grading) == 135, f'分级表应为 135 行，实得 {len(grading)}'

a_ids = {cid for cid, r in grading.items() if r['grade'] == 'A'}
print(f'A 级案例 {len(a_ids)} / 135')

instances = []
for group, rel in GROUPS:
    d = os.path.join(ROOT, rel)
    for fn in sorted(os.listdir(d)):
        if not fn.endswith('.json'):
            continue
        cid = fn[:-5]
        if cid not in a_ids:
            continue
        pred = json.load(open(os.path.join(d, fn)))
        instances.append({
            'group': group, 'case_id': cid,
            'prediction': {
                'direction': pred.get('direction'),
                'assertions': pred.get('assertions'),
                'summary': pred.get('summary'),
            },
            'outcome_record': grading[cid]['outcome_record'],
        })

random.seed(20261029)
random.shuffle(instances)
packet, mapping = [], {}
for i, inst in enumerate(instances, 1):
    anon = f'DA-{i:03d}'
    packet.append({'anon_id': anon, 'prediction': inst['prediction'],
                   'outcome_record': inst['outcome_record']})
    mapping[anon] = {'group': inst['group'], 'case_id': inst['case_id']}

out_dir = f'{ROOT}/benchmark/dual-axis'
with open(f'{out_dir}/packets/judge-packet.json', 'w') as f:
    json.dump(packet, f, ensure_ascii=False, indent=1)
with open(f'{out_dir}/host-mapping.json', 'w') as f:
    json.dump(mapping, f, ensure_ascii=False, indent=1)

from collections import Counter
print('包内实例数（按组）:', dict(Counter(v['group'] for v in mapping.values())))
print('包内总数:', len(packet))
