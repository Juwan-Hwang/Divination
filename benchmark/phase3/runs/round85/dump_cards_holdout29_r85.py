#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""holdout29 输入卡语义通读转储（组集席自读用）：按写定 id 清单逐件精确
打开盘上卡，整卡转储至 runs/round85/dump-cards-holdout29-r85.txt。"""
import json, os

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
IDS = ['DA-025', 'CYJ-001', 'BY-012', 'DA-033', 'CYJ-002', 'BY-014',
       'DA-034', 'CYJ-004', 'BY-015', 'DA-035', 'CYJ-005', 'BY-016',
       'DA-037', 'ZW-004', 'ZW-005', 'ZW-006', 'ZW-007', 'ZW-008',
       'ZW-009', 'ZW-010', 'ZW-011', 'ZW-012', 'ZW-013', 'ZW-014',
       'ZW-015', 'ZW-016', 'DS-063']
out = os.path.join(BASE, 'runs/round85/dump-cards-holdout29-r85.txt')
with open(out, 'w', encoding='utf-8') as f:
    for cid in IDS:
        card = json.load(open(os.path.join(BASE, 'holdout29/inputs', f'{cid}.json'), encoding='utf-8'))
        f.write(f'===== {cid} =====\n')
        f.write(json.dumps(card, ensure_ascii=False, indent=2))
        f.write('\n')
print(out, os.path.getsize(out))
