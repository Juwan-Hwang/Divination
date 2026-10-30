#!/usr/bin/env python3
"""R43 outcome manifest: verbatim carry-over of the R42 manifest (R43
PREREG: outcome baseline carried from R42, no new overlay rulings). Verifies (hard assertions, any failure aborts):
  1. cases key set == full id set of runs/round43/batches.json (487);
  2. overlay 16 entries verbatim equal to the R42 source manifest and
     to data/outcome-errata-overlay.json;
  3. every entry verbatim equal to the R42 source (post-write re-check).
Writes the R43 manifest as a verbatim copy of the R42 payload plus
carry-over provenance. Host tooling, build-only; no scoring."""
import json, sys
from pathlib import Path

R43 = Path(__file__).resolve().parent
P3 = R43.parents[1]
SRC = P3 / 'runs/round42/judging/outcome-manifest.json'
OVERLAY = P3 / 'data/outcome-errata-overlay.json'
BATCHES = R43 / 'batches.json'

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
        print(f'FATAL: overlay verbatim vs R42 source {ok_overlay}/16'); return 1
    if set(overlay) - set(cases):
        print(f'FATAL: overlay ids missing from cases: {sorted(set(overlay) - set(cases))}'); return 1
    out = dict(src) if 'cases' in src else {'cases': cases}
    out['_r43_carryover'] = ('Verbatim carry-over of runs/round42/judging/outcome-manifest.json '
                             'per R43 PREREG; cases payload unmodified; '
                             'overlay 16/16 verified verbatim; '
                             'key set == runs/round43/batches.json full id set (487).')
    (R43 / 'judging').mkdir(parents=True, exist_ok=True)
    (R43 / 'judging/outcome-manifest.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
    # Post-write verification: re-read the written R43 manifest and check
    # every entry verbatim against the R42 source.
    written = json.loads((R43 / 'judging/outcome-manifest.json').read_text(encoding='utf-8'))
    wcases = written['cases'] if 'cases' in written else written
    diff = [cid for cid in cases if wcases.get(cid) != cases[cid]]
    if diff or set(wcases) != set(cases):
        print(f'FATAL: post-write verbatim check failed on {len(diff)} entries'); return 1
    print(f'OK: R43 outcome-manifest written; 487 keys; overlay 16/16 verbatim; all entries verbatim vs R42 source.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
