#!/usr/bin/env python3
"""Phase 3 judging packet builder (host tooling).
Usage: python3 build_packets.py <round_dir>
Reads <round_dir>/predictions/*.json, attaches outcome_record from rosters,
anonymizes (P3-xxxx), splits into two packets, writes judging/ files.
"""
import json, sys, glob, os, hashlib

def load_roster():
    out = {}
    for p in ('benchmark/phase2/data/roster.jsonl', 'benchmark/phase3/data/roster3.jsonl', 'benchmark/phase3/roster4-additions.jsonl', 'benchmark/phase3/roster5-additions.jsonl', 'benchmark/phase3/roster6-additions.jsonl', 'benchmark/phase3/roster7-additions.jsonl', 'benchmark/phase3/roster8-additions.jsonl', 'benchmark/phase3/roster9-additions.jsonl'):
        if os.path.exists(p):
            for l in open(p, encoding='utf-8'):
                r = json.loads(l)
                out[r['id']] = {'outcome_record': r.get('outcome_record', ''),
                                'tradition': r.get('tradition', ''),
                                'contamination': r.get('contamination', '')}
    return out

def main():
    rd = sys.argv[1]
    roster = load_roster()
    preds = []
    for f in sorted(glob.glob(os.path.join(rd, 'predictions', '*.json'))):
        p = json.load(open(f, encoding='utf-8'))
        cid = p.get('id') or p.get('case_id')
        if cid not in roster:
            print('MISSING outcome for', cid); continue
        preds.append((cid, p))
    items, mapping = [], {}
    for cid, p in preds:
        anon = 'P3-' + hashlib.sha256(('phase3:' + rd + ':' + cid).encode()).hexdigest()[:8]
        mapping[anon] = cid
        items.append({'anon_id': anon,
                      'prediction': {k: p.get(k) for k in ('direction', 'assertions', 'timing', 'summary')},
                      'outcome_record': roster[cid]['outcome_record']})
    items.sort(key=lambda x: x['anon_id'])
    half = (len(items) + 1) // 2
    os.makedirs(os.path.join(rd, 'judging'), exist_ok=True)
    json.dump(items[:half], open(os.path.join(rd, 'judging', 'packetA.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump(items[half:], open(os.path.join(rd, 'judging', 'packetB.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump(mapping, open(os.path.join(rd, 'judging', 'host-mapping.json'), 'w'), ensure_ascii=False, indent=1)
    meta = {cid: {k: roster[cid][k] for k in ('tradition', 'contamination')} for _, cid in
            [(None, c) for c in mapping.values()]}
    json.dump(meta, open(os.path.join(rd, 'judging', 'host-meta.json'), 'w'), ensure_ascii=False, indent=1)
    print('packets:', len(items[:half]), '+', len(items[half:]), '=', len(items))

if __name__ == '__main__':
    main()
