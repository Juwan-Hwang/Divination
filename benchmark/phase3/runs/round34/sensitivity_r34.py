#!/usr/bin/env python3
"""R34 sensitivity annex (analysis role only): impact bound for the
judgeX-block1 isolation self-disclosure (see ADDENDUM-isolation-disclosures).

The seat reported seeing, before scoring: (1) the first items of
judging/packet-diag.json (outcome texts only, prediction fields null),
(2) the first 5 rows of judging/judgeDX-diag.jsonl (another view's scores
for diagnostic predictions of the same underlying cases),
(3) head lines of its own packetA (its assigned material).
Exposure with any score content is confined to (2); outcome texts in (1)
duplicate what the platform packets themselves carry for those cases.

Sensitivity: recompute platform (a) and the (b) liuren-dev8 guardrail
after excluding, in turn: (S1) the cases behind the first-5 diag score
rows that fall inside block1's assignment; (S2) conservatively, all
block1 items that are among the 30 diagnostic cases; (S3) all 30
diagnostic cases from (a). Lines: (a) >= -1.371; (b) liuren8 >= -2.593.
"""
import json
from pathlib import Path

P3 = Path('benchmark/phase3')
R34 = P3 / 'runs/round34'
JD = R34 / 'judging'

ours = json.load(open(R34 / 'final-scores.json'))['ours_axis2']
master = json.load(open(P3 / 'data/master-baseline-dev9.json'))
master8 = json.load(open(P3 / 'data/master-baseline-dev8.json'))
meta = json.load(open(JD / 'host-meta.json'))
hmap = json.load(open(JD / 'host-mapping.json'))
packet1 = json.load(open(JD / 'packet1.json'))
block1_cases = {hmap[e['anon_id']] for e in packet1}

diag_head_rows = []
with open(JD / 'judgeDX-diag.jsonl', encoding='utf-8') as fh:
    for i, line in enumerate(fh):
        if i >= 5:
            break
        diag_head_rows.append(json.loads(line)['anon_id'])
dmap = json.load(open(JD / 'host-diag-mapping.json'))
diag_cases_seen = {dmap[a]['case_id'] for a in diag_head_rows}
diag_packet_head = {dmap[e['anon_id']]['case_id']
                    for e in json.load(open(JD / 'packet-diag.json'))[:5]}
diag30 = {ref['case_id'] for ref in dmap.values()}

liuren8 = sorted(c for c in ours if c in master8
                 and meta[c]['tradition'] in ('liuren', '六壬'))


def pair_mean(ids):
    ids = sorted(ids)
    return round(sum(ours[c] - master[c]['total'] for c in ids) / len(ids), 3), len(ids)


print('block1 size:', len(block1_cases))
print('diag score rows seen (first 5):', sorted(diag_cases_seen))
print('diag packet head cases (first 5):', sorted(diag_packet_head))
s1 = (diag_cases_seen | diag_packet_head) & block1_cases
print('S1 exposed-in-block1:', sorted(s1), '-> (a) excl:', pair_mean(set(ours) - s1))
s2 = diag30 & block1_cases
print('S2 block1 n diag30:', sorted(s2), '-> (a) excl:', pair_mean(set(ours) - s2),
      '| liuren8 excl:', pair_mean(set(liuren8) - s2))
print('S3 (a) excl all diag30:', pair_mean(set(ours) - diag30))
print('baselines: (a) full', pair_mean(set(ours)), '| liuren8 full', pair_mean(set(liuren8)))
print('lines: (a) >= -1.371; (b) liuren dev8 >= -2.593')
