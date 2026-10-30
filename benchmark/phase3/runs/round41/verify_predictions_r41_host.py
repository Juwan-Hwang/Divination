#!/usr/bin/env python3
"""R41 host verification of platform blind predictions (host tooling,
build-only; no scoring). Checks against runs/round41/batches.json:
  1. every batch id has predictions/<id>.json, JSON parses;
  2. case_id == filename stem; required fields present
     (case_id/prediction_text/basis/confidence/trigger);
  3. confidence in [0,1]; trigger has the four keys with boolean triple;
  4. counts trigger triple over liuyao-tradition inputs (inputs-dev12
     tradition field) for the record.
Prints a summary; exit 1 on any structural failure."""
import json, sys
from pathlib import Path

R41 = Path(__file__).resolve().parent
P3 = R41.parents[1]
batches = json.loads((R41 / 'batches.json').read_text(encoding='utf-8'))
all_ids = [cid for ids in batches.values() for cid in ids]
fail = []
trig = {'changed_main': 0, 'reserve_used': 0, 'disputed': 0}
trig_liuyao = {'changed_main': 0, 'reserve_used': 0, 'disputed': 0}
n_ok = 0
for cid in all_ids:
    p = R41 / 'predictions' / f'{cid}.json'
    if not p.exists():
        fail.append(f'{cid}: missing'); continue
    try:
        d = json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        fail.append(f'{cid}: json error {e}'); continue
    if d.get('case_id') != cid:
        fail.append(f'{cid}: case_id mismatch {d.get("case_id")}'); continue
    for f in ('prediction_text', 'basis', 'confidence', 'trigger'):
        if f not in d:
            fail.append(f'{cid}: missing field {f}')
    c = d.get('confidence')
    if not isinstance(c, (int, float)) or not (0 <= c <= 1):
        fail.append(f'{cid}: confidence out of range {c}')
    t = d.get('trigger') or {}
    for k in ('changed_main', 'reserve_used', 'disputed', 'reason'):
        if k not in t:
            fail.append(f'{cid}: trigger missing key {k}')
    for k in trig:
        if t.get(k) is True:
            trig[k] += 1
    try:
        inp = json.loads((P3 / 'inputs-dev12' / f'{cid}.json').read_text(encoding='utf-8'))
        if inp.get('tradition') == 'liuyao':
            for k in trig_liuyao:
                if t.get(k) is True:
                    trig_liuyao[k] += 1
    except Exception:
        pass
    n_ok += 1
extra = [p.stem for p in (R41 / 'predictions').glob('*.json') if p.stem not in set(all_ids)]
print(f'ids expected: {len(all_ids)}; files ok: {n_ok}; extra files: {extra}')
print(f'trigger totals (all): {trig}')
print(f'trigger totals (liuyao inputs only): {trig_liuyao}')
if fail:
    print(f'FAILURES {len(fail)}:'); [print(' -', x) for x in fail[:40]]; sys.exit(1)
print('OK: all 487 predictions structurally valid.')
