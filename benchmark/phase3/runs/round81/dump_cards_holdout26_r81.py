#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R81 封存席语义通读转储：按显式 id 清单逐件打开 holdout26 输入卡，拼纯文本转储
供封存席逐卡通读（只读转储，落 runs/round81/dump-cards-holdout26-r81.txt）。"""
import json, os

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
IDS = ['DS-031', 'DS-032', 'DS-033', 'DS-034', 'DS-035', 'DS-036', 'DS-037',
       'DS-038', 'DS-039',
       'QM-034', 'QM-035', 'QM-036', 'QM-037', 'QM-038', 'QM-039', 'QM-040',
       'QM-042', 'QM-043',
       'GSZ-069', 'GSZ-074', 'GSZ-075', 'GSZ-077', 'GSZ-078',
       'WHY-004', 'WHY-005', 'WHY-006', 'WHY-007']
out = []
for cid in IDS:
    card = json.load(open(os.path.join(BASE, f'holdout26/inputs/{cid}.json'),
                          encoding='utf-8'))
    out.append(f"===== {cid} [{card['tradition']}] =====")
    out.append(f"subject: {card['subject']}")
    out.append(f"context: {card['context']}")
    out.append(f"question: {card['question']}")
    out.append(f"setting: {card['setting']}")
    out.append(f"anchors: {json.dumps(card['anchors'], ensure_ascii=False)}")
    out.append('')
text = '\n'.join(out)
p = os.path.join(BASE, 'runs/round81/dump-cards-holdout26-r81.txt')
with open(p, 'w', encoding='utf-8') as f:
    f.write(text)
print(p, len(text.encode('utf-8')))
