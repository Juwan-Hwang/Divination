#!/usr/bin/env python3
"""R39 outcome manifest: verbatim carry-over of the R38 manifest (R39
PREREG s.0: same outcome baseline as R38, no new overlay rulings).
Verifies 487-key set against inputs-dev12 filenames and overlay 16/16
verbatim presence, then writes the R39 manifest as a byte-identical
copy of the cases payload plus carry-over provenance.
Host tooling, build-only; no scoring."""
import json, sys
from pathlib import Path

R39 = Path(__file__).resolve().parent
P3 = R39.parents[1]
SRC = P3 / 'runs/round38/judging/outcome-manifest.json'
OVERLAY = P3 / 'data/outcome-errata-overlay.json'
INPUTS = P3 / 'inputs-dev12'

def main():
    src = json.loads(SRC.read_text(encoding='utf-8'))
    cases = src['cases'] if 'cases' in src else src
    ids = {p.stem for p in INPUTS.glob('*.json')}
    if set(cases) != ids or len(cases) != 487:
        print(f'FATAL: manifest keys {len(cases)} vs inputs-dev12 {len(ids)}'); return 1
    overlay_raw = json.loads(OVERLAY.read_text(encoding='utf-8'))
    overlay = {k: (v['corrected_outcome'] if isinstance(v, dict) else v)
               for k, v in overlay_raw.items() if k != '_comment'}
    ok = sum(1 for cid, corr in overlay.items() if cases.get(cid) == corr)
    if len(overlay) != 16 or ok != 16:
        print(f'FATAL: overlay verbatim {ok}/{len(overlay)}'); return 1
    out = dict(src) if 'cases' in src else {'cases': cases}
    out['_r39_carryover'] = ('Verbatim carry-over of runs/round38/judging/outcome-manifest.json '
                             'per R39 PREREG s.0; cases payload unmodified; overlay 16/16 verified.')
    (R39 / 'judging/outcome-manifest.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'manifest carried: {len(cases)} cases; overlay 16/16 verbatim; keys == inputs-dev12 set')
    return 0

if __name__ == '__main__':
    sys.exit(main())
