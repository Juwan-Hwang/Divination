import re, sys
from pathlib import Path
P3 = Path('/home/hatch/workspace/divination/benchmark/phase3')
jobs = [
 ('verify_predictions_host_r93.py','verify_predictions_host_r94.py'),
 ('count_section8_r93.py','count_section8_r94.py'),
]
for src_name, dst_name in jobs:
    src = P3/'runs/round93'/src_name
    dst = P3/'runs/round94'/dst_name
    t = src.read_text(encoding='utf-8')
    counts = {}
    for a,b in [('round93','round94'), ('R93','R94'), ('_r93','_r94'), ('-r93','-r94'), ('r93.py','r94.py'), ('dev93','dev94')]:
        counts[a] = t.count(a); t = t.replace(a,b)
    dst.write_text(t, encoding='utf-8')
    print(dst_name, counts)
