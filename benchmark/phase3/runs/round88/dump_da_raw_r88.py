# -*- coding: utf-8 -*-
"""DA 底本 cases_raw 逐案转储（R88 组集席）：按案号精确提取 raw 全文。"""
import json, os
BASE = '/home/hatch/workspace/divination/benchmark/phase3'
d = json.load(open(f'{BASE}/expansion12/liuren-duanan/scratch-archive/cases_raw.json', encoding='utf-8'))
byn = {e['n']: e for e in d}
out = []
for n in (59, 60, 61, 62, 63, 64, 65, 66, 67, 68):
    e = byn[n]
    out.append(f"===== 案{n} title={e['title']} =====\n{e['raw']}\n")
p = f'{BASE}/runs/round88/dump-da-raw-h32-r88.txt'
open(p, 'w', encoding='utf-8').write('\n'.join(out))
print(p, os.path.getsize(p))
