#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R83 封存席语义通读转储：按显式 id 清单逐件精确打开盘上 holdout28 输入卡，
渲染为纯文本转储件 runs/round83/dump-cards-holdout28-r83.txt 供逐卡通读。"""
import json, os

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
R83 = os.path.join(BASE, 'runs/round83')
IDS = ['DS-050', 'DS-051', 'DS-052', 'DS-053', 'DS-054', 'DS-055', 'DS-056',
       'DS-057', 'DS-058', 'DS-059', 'DS-060', 'DS-061', 'DS-062',
       'QM-210', 'QM-211', 'QM-010',
       'GSZ-091', 'GSZ-092', 'GSZ-093', 'GSZ-098', 'GSZ-099', 'GSZ-100',
       'WHY-012', 'WHY-016', 'WHY-022', 'WHY-023', 'WHY-024']
lines = []
for cid in IDS:
    card = json.load(open(os.path.join(BASE, f'holdout28/inputs/{cid}.json'),
                          encoding='utf-8'))
    lines.append(f"===== {cid} [{card['tradition']}] =====")
    for k in ('subject', 'context', 'question', 'setting', 'provenance'):
        lines.append(f"{k}: {card[k]}")
    lines.append('anchors: ' + json.dumps(card['anchors'], ensure_ascii=False))
    lines.append('')
out = os.path.join(R83, 'dump-cards-holdout28-r83.txt')
with open(out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print(out, os.path.getsize(out))
