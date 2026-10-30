#!/usr/bin/env python3
"""R33 host tooling: rebuild the 19 MP packets with the correct outcomes
(modern-cn, cross-verified against roster7/8-additions) after the id
collision documented in ADDENDUM-mp-collision.md. New files only."""
import json
from pathlib import Path

P3 = Path('benchmark/phase3')
JD = P3 / 'runs/round33/judging'
MP_IDS = [f'MP-{i:03d}' for i in range(1, 20)]


def load_jsonl(path):
    out = {}
    for line in open(path, encoding='utf-8'):
        line = line.strip()
        if line:
            r = json.loads(line)
            out[r.get('id') or r.get('case_id')] = r
    return out


def outcome_of(rec):
    v = rec.get('outcome_record')
    if isinstance(v, str) and v.strip():
        return v
    o = rec.get('outcome')
    if isinstance(o, str) and o.strip():
        return o
    if isinstance(o, dict):
        for k in ('description', 'outcome_record', 'text'):
            d = o.get(k)
            if isinstance(d, str) and d.strip():
                return d
    return None


modern = load_jsonl(P3 / 'expansion6/modern-cn/cases.jsonl')
add7 = load_jsonl(P3 / 'roster7-additions.jsonl')
add8 = load_jsonl(P3 / 'roster8-additions.jsonl')
hmap = json.load(open(JD / 'host-mapping.json'))
inv = {v: k for k, v in hmap.items()}

packets = []
for n in (1, 2, 3, 4):
    packets += json.load(open(JD / f'packet{n}.json'))
orig = {e['anon_id']: e for e in packets}

out = []
for cid in MP_IDS:
    oc = outcome_of(modern[cid])
    ref = add7.get(cid) or add8.get(cid)
    assert ref is not None, cid
    assert outcome_of(ref) == oc, f'cross-check mismatch {cid}'
    anon = inv[cid]
    if orig[anon].get('outcome_record') == oc:
        print(cid, anon, 'orig packet already correct, excluded')
        continue
    e = dict(orig[anon])
    e['outcome_record'] = oc
    out.append(e)
    print(cid, anon, 'orig outcome head:', str(orig[anon].get('outcome_record'))[:24],
          '-> fixed head:', oc[:24])

json.dump(out, open(JD / 'packetMP.json', 'w'), ensure_ascii=False, indent=1)
print('packetMP.json written:', len(out))
