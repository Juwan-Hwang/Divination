#!/usr/bin/env python3
"""Build master-baseline judging packet for new dev9 cases (host tooling).
Mirrors data/dev8-baseline-build: anonymized D9B-### items pairing the master
prediction text with the outcome record; split part1/part2; host-key kept apart.
"""
import json, os, glob

P3 = 'benchmark/phase3'
OUT = f'{P3}/data/dev9-baseline-build'
os.makedirs(OUT, exist_ok=True)

cases = {}
for pat in (f'{P3}/expansion8/*/cases.jsonl', f'{P3}/expansion9/*/cases.jsonl'):
    for p in glob.glob(pat):
        for l in open(p, encoding='utf-8'):
            if l.strip():
                r = json.loads(l)
                cases[r['id']] = r

roster = [json.loads(l) for l in open(f'{P3}/roster9-additions.jsonl', encoding='utf-8') if l.strip()]
items, key = [], {}
for i, r in enumerate(sorted(roster, key=lambda x: x['id']), 1):
    anon = f'D9B-{i:03d}'
    key[anon] = r['id']
    c = cases[r['id']]
    texts = []
    for mp in c.get('master_predictions', []):
        t = mp.get('statement_excerpt', '')
        ka = mp.get('key_assertions')
        if ka:
            t += '【逐项断言】' + '；'.join(ka)
        texts.append(t)
    items.append({'anon_id': anon, 'prediction': '\n'.join(texts),
                  'outcome_record': r['outcome_record']})
half = (len(items) + 1) // 2
json.dump(items, open(f'{OUT}/packet.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(items[:half], open(f'{OUT}/packet-part1.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(items[half:], open(f'{OUT}/packet-part2.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(key, open(f'{OUT}/host-key.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('baseline packet items:', len(items), 'parts:', half, '+', len(items) - half)
