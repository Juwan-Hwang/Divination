# -*- coding: utf-8 -*-
"""DA 底本 cases_raw 逐案转储（R87 组集席）：按案号精确提取 raw 全文。"""
import json
BASE = '/home/hatch/workspace/divination/benchmark/phase3'
d = json.load(open(f'{BASE}/expansion12/liuren-duanan/scratch-archive/cases_raw.json', encoding='utf-8'))
byn = {e['n']: e for e in d}
out = []
for n in (47, 48, 50, 51, 54, 55, 57, 59, 60, 61, 62, 63):
    e = byn[n]
    out.append(f"===== 案{n} title={e['title']} =====\n{e['raw']}\n")
p = f'{BASE}/runs/round87/dump-da-raw-h31-r87.txt'
open(p, 'w', encoding='utf-8').write('\n'.join(out))
import os
print(p, os.path.getsize(p))
