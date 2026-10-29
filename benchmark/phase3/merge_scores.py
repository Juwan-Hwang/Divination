#!/usr/bin/env python3
"""Phase 3 score merger + paired stats (host tooling).
Usage: python3 merge_scores.py <round_dir>
Expects judging/judgeA-part1.jsonl, judgeA-part2.jsonl, judgeB-part1.jsonl,
judgeB-part2.jsonl and (if exists) judging/arbitration.jsonl.
Writes judging/disputes.json (list of anon_ids needing arbitration) on first
pass; after arbitration file exists, writes final-scores.json + stats.
"""
import json, sys, os
from collections import defaultdict

def load_jsonl(p):
    d = {}
    if os.path.exists(p):
        for l in open(p, encoding='utf-8'):
            if l.strip():
                r = json.loads(l); d[r['anon_id']] = r
    return d

def main():
    rd = sys.argv[1]
    jd = os.path.join(rd, 'judging')
    mapping = json.load(open(os.path.join(jd, 'host-mapping.json')))
    meta = json.load(open(os.path.join(jd, 'host-meta.json')))
    A = {}; B = {}
    for part in ('part1', 'part2'):
        A.update(load_jsonl(os.path.join(jd, f'judgeA-{part}.jsonl')))
        B.update(load_jsonl(os.path.join(jd, f'judgeB-{part}.jsonl')))
    ARB = load_jsonl(os.path.join(jd, 'arbitration.jsonl'))
    disputes, final = [], {}
    for anon, cid in mapping.items():
        if anon not in A or anon not in B:
            print('MISSING judge score', anon, cid); continue
        a, b = A[anon], B[anon]
        need = abs((a['claims'] + a['timing']) - (b['claims'] + b['timing'])) >= 2 or a['pass'] != b['pass']
        if need and anon not in ARB:
            disputes.append(anon); continue
        if anon in ARB:
            r = ARB[anon]
            final[cid] = {k: float(r[k]) for k in ('direction', 'claims', 'timing', 'total')}
        else:
            final[cid] = {k: (a[k] + b[k]) / 2 for k in ('direction', 'claims', 'timing', 'total')}
    if disputes:
        json.dump(disputes, open(os.path.join(jd, 'disputes.json'), 'w'))
        print('DISPUTES needing arbitration:', len(disputes)); return
    master = json.load(open(sys.argv[2] if len(sys.argv) > 2 else 'benchmark/phase3/data/master-baseline-dev3.json'))
    def agg(ids):
        n = len(ids)
        if not n: return None
        ours = [final[c]['total'] for c in ids]
        mst = [master[c]['total'] for c in ids if c in master]
        pair = [final[c]['total'] - master[c]['total'] for c in ids if c in master]
        w = sum(1 for x in pair if x > 0); t = sum(1 for x in pair if x == 0); l = sum(1 for x in pair if x < 0)
        return {'n': n, 'ours_mean': round(sum(ours) / n, 3), 'ours_pct': round(sum(ours) / n / 6 * 100, 1),
                'ours_pass': sum(1 for v in final.values() if False) if False else sum(1 for c in ids if final[c]['total'] >= 4),
                'master_mean': round(sum(mst) / len(mst), 3) if mst else None,
                'pair_diff': round(sum(pair) / len(pair), 3) if pair else None,
                'W/T/L': f'{w}/{t}/{l}',
                'timing_ours': round(sum(final[c]['timing'] for c in ids) / n, 3),
                'dir_ours': round(sum(final[c]['direction'] for c in ids) / n, 3),
                'claims_ours': round(sum(final[c]['claims'] for c in ids) / n, 3)}
    allids = list(final.keys())
    by_trad = defaultdict(list); by_cont = defaultdict(list)
    for c in allids:
        by_trad[meta[c]['tradition']].append(c)
        by_cont[meta[c]['contamination']].append(c)
    stats = {'ALL': agg(allids),
             'by_tradition': {k: agg(v) for k, v in sorted(by_trad.items())},
             'by_contamination': {k: agg(v) for k, v in sorted(by_cont.items())}}
    json.dump({'ours_axis2': {c: final[c]['total'] for c in allids},
               'ours_sub': final, 'stats': stats},
              open(os.path.join(rd, 'final-scores.json'), 'w'), ensure_ascii=False, indent=1)
    print(json.dumps(stats, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
