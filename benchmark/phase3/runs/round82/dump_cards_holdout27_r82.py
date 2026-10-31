#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R82 封存席语义通读转储：按显式 id 清单逐件打开 holdout27 输入卡，拼纯文本转储
供封存席逐卡通读（只读转储，落 runs/round82/dump-cards-holdout27-r82.txt）。"""
import json, os

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
IDS = ['DS-040', 'DS-041', 'DS-042', 'DS-043', 'DS-044', 'DS-045', 'DS-046',
       'DS-048', 'DS-049',
       'QM-044', 'QM-045', 'QM-046', 'QM-047', 'QM-048', 'QM-049', 'QM-052',
       'QM-055', 'QM-058',
       'GSZ-079', 'GSZ-081', 'GSZ-084', 'GSZ-086', 'GSZ-088',
       'WHY-008', 'WHY-009', 'WHY-010', 'WHY-011']
out = []
for cid in IDS:
    card = json.load(open(os.path.join(BASE, f'holdout27/inputs/{cid}.json'),
                          encoding='utf-8'))
    out.append(f"===== {cid} [{card['tradition']}] =====")
    out.append(f"subject: {card['subject']}")
    out.append(f"context: {card['context']}")
    out.append(f"question: {card['question']}")
    out.append(f"setting: {card['setting']}")
    out.append(f"anchors: {json.dumps(card['anchors'], ensure_ascii=False)}")
    out.append('')
text = '\n'.join(out)
p = os.path.join(BASE, 'runs/round82/dump-cards-holdout27-r82.txt')
with open(p, 'w', encoding='utf-8') as f:
    f.write(text)
print(p, len(text.encode('utf-8')))
