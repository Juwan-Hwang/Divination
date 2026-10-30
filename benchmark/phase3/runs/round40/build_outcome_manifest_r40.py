#!/usr/bin/env python3
"""R40 outcome manifest: verbatim carry-over of the R39 manifest (R40
PREREG s.0: same outcome baseline as R39, no new overlay rulings;
build rule s.6). Task-designated provenance sections: R40 PREREG
s.2/s.7. Verifies (hard assertions, any failure aborts):
  1. cases key set == full id set of runs/round40/batches.json (487);
  2. overlay 16 entries verbatim equal to the R39 source manifest and
     to data/outcome-errata-overlay.json;
  3. every non-overlay entry verbatim equal to the R39 source.
Writes the R40 manifest as a verbatim copy of the R39 payload plus
carry-over provenance. Host tooling, build-only; no scoring."""
import json, sys
from pathlib import Path

R40 = Path(__file__).resolve().parent
P3 = R40.parents[1]
SRC = P3 / 'runs/round39/judging/outcome-manifest.json'
OVERLAY = P3 / 'data/outcome-errata-overlay.json'
BATCHES = R40 / 'batches.json'

def main():
    src = json.loads(SRC.read_text(encoding='utf-8'))
    cases = src['cases'] if 'cases' in src else src
    batches = json.loads(BATCHES.read_text(encoding='utf-8'))
    batch_ids = {cid for ids in batches.values() for cid in ids}
    if set(cases) != batch_ids or len(cases) != 487 or len(batch_ids) != 487:
        print(f'FATAL: manifest keys {len(cases)} vs batches.json ids {len(batch_ids)}'); return 1
    overlay_raw = json.loads(OVERLAY.read_text(encoding='utf-8'))
    overlay = {k: (v['corrected_outcome'] if isinstance(v, dict) else v)
               for k, v in overlay_raw.items() if k != '_comment'}
    if len(overlay) != 16:
        print(f'FATAL: overlay entries {len(overlay)} != 16'); return 1
    ok_overlay = sum(1 for cid, corr in overlay.items() if cases.get(cid) == corr)
    if ok_overlay != 16:
        print(f'FATAL: overlay verbatim vs R39 source {ok_overlay}/16'); return 1
    non_overlay = [cid for cid in cases if cid not in overlay]
    # cases here IS the R39 source payload (pre-write), so the R40 output
    # cases are verbatim by construction; assert the split counts and
    # that overlay ids are exactly the overlay file's id set.
    if set(overlay) - set(cases):
        print(f'FATAL: overlay ids missing from cases: {sorted(set(overlay) - set(cases))}'); return 1
    out = dict(src) if 'cases' in src else {'cases': cases}
    out['_r40_carryover'] = ('Verbatim carry-over of runs/round39/judging/outcome-manifest.json '
                             'per R40 PREREG s.2/s.7 (carry-over rule stated in s.0/s.6); '
                             'cases payload unmodified; overlay 16/16 verified verbatim; '
                             'key set == runs/round40/batches.json full id set (487).')
    (R40 / 'judging').mkdir(parents=True, exist_ok=True)
    (R40 / 'judging/outcome-manifest.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
    # Post-write verification: re-read the written R40 manifest and check
    # every entry (overlay and non-overlay) verbatim against the R39 source.
    written = json.loads((R40 / 'judging/outcome-manifest.json').read_text(encoding='utf-8'))
    wcases = written['cases']
    if set(wcases) != batch_ids or len(wcases) != 487:
        print('FATAL: written manifest key set != batches.json id set'); return 1
    ov_ok = sum(1 for cid in overlay if wcases.get(cid) == cases.get(cid) == overlay[cid])
    nov_ok = sum(1 for cid in non_overlay if wcases.get(cid) == cases.get(cid))
    if ov_ok != 16 or nov_ok != len(non_overlay):
        print(f'FATAL: post-write verbatim overlay {ov_ok}/16, non-overlay {nov_ok}/{len(non_overlay)}'); return 1
    if written.get('stripped_tail') != src.get('stripped_tail'):
        print('FATAL: stripped_tail not verbatim'); return 1
    print(f'manifest carried: {len(wcases)} cases; keys == batches.json id set (487)')
    print(f'overlay verbatim (R40 == R39 == overlay file): {ov_ok}/16 -> {sorted(overlay)}')
    print(f'non-overlay verbatim vs R39: {nov_ok}/{len(non_overlay)}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
