#!/usr/bin/env python3
"""R57 data-seat flag extraction (unique to round57). Read-only."""
import json, os, sys

BASE = os.path.expanduser('~/workspace/divination/benchmark/phase3')
ANONS = """P3-0c4112be P3-24bc7fb0 P3-29acaf48 P3-40b934ae P3-284962cb P3-13a8ed4e P3-251b6438 P3-3c3266db P3-4a1ce118 P3-4a565aa1 P3-572c80ef P3-546203e4 P3-5c9a00a0 P3-624d2180 P3-6335cdc5 P3-6356cc2d P3-66da1746 P3-703abe8b P3-71cd6647 P3-762a8d1e P3-821d42db P3-98119193 P3-9fa099fe P3-a1020cd3 P3-a21eaf55 P3-a64679ac P3-a939aad9 P3-b43819a5 P3-b91d5e9c P3-b51ec63c P3-a5d34504 P3-aa30993e P3-8244fed7 P3-8cd7f974 P3-aaff364d P3-b8659dcd P3-d6036548 P3-ec87a723 P3-c4a96f29 P3-dde16c85 P3-2328ed60 P3-2e086cb9 P3-3570415a P3-1643d583 P3-2f456743 P3-ce4d2108 P3-cfb64d3e P3-d85bfd87 P3-ef48f4ce""".split()

hm = json.load(open(f'{BASE}/runs/round57/judging/host-mapping.json'))
mf = json.load(open(f'{BASE}/runs/round57/judging/outcome-manifest.json'))

# judge scoring rows: exact filenames only
rows = {}
for side in ('X', 'Y'):
    for b in range(1, 9):
        p = f'{BASE}/runs/round57/judging/judge{side}-block{b}.jsonl'
        if not os.path.exists(p):
            continue
        for line in open(p, encoding='utf-8'):
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except Exception:
                continue
            aid = r.get('anon_id') or r.get('id') or r.get('anon')
            if aid in ANONS:
                rows.setdefault(aid, []).append({'file': os.path.basename(p), 'row': r})

# prior annotation files
prior = {}
for rn in (49, 50, 51, 53, 54, 55, 56):
    p = f'{BASE}/data/case-annotations-r{rn}.json'
    if not os.path.exists(p):
        continue
    d = json.load(open(p))
    for sec in ('flags', 'annotations', 'same_gist_carry_note'):
        for e in d.get(sec, []) or []:
            prior.setdefault(e.get('case_id'), []).append(
                {'round': rn, 'section': sec, 'anon_id': e.get('anon_id'),
                 'verdict': e.get('verdict') or e.get('disposition') or e.get('classification'),
                 'flag': e.get('flag'), 'basis': (e.get('basis') or e.get('finding') or e.get('note') or '')[:400]})

out = []
for aid in ANONS:
    cid = hm.get(aid)
    rec = {'anon_id': aid, 'case_id': cid, 'judge_rows': rows.get(aid, [])}
    if cid:
        rec['manifest_case'] = mf['cases'].get(cid)
        rec['stripped_tail'] = mf.get('stripped_tail', {}).get(cid)
        rec['carry_r56'] = mf.get('_r56_carryover_notes', {}).get(cid)
        rec['carry_r57'] = mf.get('_r57_carryover_notes_addendum', {}).get(cid)
        cardp = f'{BASE}/inputs-dev12/{cid}.json'
        if os.path.exists(cardp):
            c = json.load(open(cardp))
            rec['card'] = {'system': c.get('system'), 'master': c.get('master'),
                           'context': c.get('context'), 'provenance': c.get('provenance'),
                           'notes': c.get('notes'), 'subject': c.get('subject')}
        rec['prior'] = prior.get(cid, [])
    out.append(rec)

json.dump(out, open('/tmp/r57work.json', 'w'), ensure_ascii=False, indent=1)
print('anons', len(ANONS), 'mapped', sum(1 for o in out if o['case_id']),
      'with_judge_rows', sum(1 for o in out if o['judge_rows']),
      'with_prior', sum(1 for o in out if o.get('prior')))
for o in out:
    print(o['anon_id'], o['case_id'], 'rows:', len(o['judge_rows']), 'prior:', len(o.get('prior') or []),
          'carry56:', bool(o.get('carry_r56')), 'carry57:', bool(o.get('carry_r57')))
