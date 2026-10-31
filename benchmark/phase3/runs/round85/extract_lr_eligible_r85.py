#!/usr/bin/env python3
"""R85 主持：自 R84 expansion12a 核查台账提取 eligible 243 例（台账登记序），按来源分组计数。
只读台账行，不打开金标。"""
import re, json
from collections import OrderedDict

path = '/home/hatch/workspace/divination/benchmark/phase3/runs/round84/supply/EXPANSION-AUDIT-expansion12a-r84.md'
rows = []
for line in open(path):
    if line.startswith('|') and ' eligible ' in line:
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        # 列: id | pool | 来源 | 四滤... | 结论 | 定位
        rows.append(cells)
print('total eligible rows:', len(rows))
groups = OrderedDict()
for c in rows:
    src = c[2]
    groups.setdefault(src, []).append(c[0])
for src, ids in groups.items():
    print(src, len(ids))
    print('  first15:', ids[:15])
out = {src: ids for src, ids in groups.items()}
with open('/home/hatch/workspace/divination/benchmark/phase3/runs/round85/lr-eligible-ledger-r85.json', 'w') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print('written lr-eligible-ledger-r85.json')
