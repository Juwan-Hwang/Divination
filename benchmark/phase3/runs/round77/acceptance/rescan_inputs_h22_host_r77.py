#!/usr/bin/env python3
"""R77 host opening re-scan (holdout22): content-level prediction-phrase scan over
holdout22 input cards (markers verbatim from R42 PREREG s.5, copied from
runs/round56/build_holdout20_r56.py). Input side only; gold not opened
by this script beyond the id list needed for the card set.
"""
import json
import os

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
IN_DIR = os.path.join(BASE, "holdout22", "inputs")

LEVEL1 = ['断语线索', '断曰', '斷語', '正议', '正議', '验语', '驗語',
          '断语：', '斷語：', '占断', '占斷', '大师断', '大師斷']
LEVEL2 = ['果验', '果然', '果應', '后验', '後驗', '结局', '結局', '应验', '應驗']
FIELD_BLACKLIST = ['断语', '斷語', '断曰', '斷曰', '正议', '正議', '验语', '驗語',
                   '占断', '占斷', '线索', '線索']


def scan_content(obj, path=''):
    hits = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            hits += scan_content(v, f'{path}/{k}')
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            hits += scan_content(v, f'{path}[{i}]')
    elif isinstance(obj, str):
        for lvl, markers in (('L1', LEVEL1), ('L2', LEVEL2)):
            for m in markers:
                idx = obj.find(m)
                if idx >= 0:
                    hits.append([path, lvl, m, obj[max(0, idx - 12):idx + len(m) + 12]])
    return hits


def scan_field_names(obj, path=''):
    hits = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            for frag in FIELD_BLACKLIST:
                if frag in k:
                    hits.append([f'{path}/{k}', frag])
                    break
            hits += scan_field_names(v, f'{path}/{k}')
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            hits += scan_field_names(v, f'{path}[{i}]')
    return hits


files = sorted(f for f in os.listdir(IN_DIR) if f.endswith('.json'))
assert len(files) == 27, len(files)
total_hits = {}
for f in files:
    card = json.load(open(os.path.join(IN_DIR, f), encoding='utf-8'))
    h = scan_content(card) + scan_field_names(card)
    if h:
        total_hits[f] = h
print("cards scanned:", len(files))
print("cards with hits:", len(total_hits))
for f, h in total_hits.items():
    print(f, json.dumps(h, ensure_ascii=False))
