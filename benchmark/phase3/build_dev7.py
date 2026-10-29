#!/usr/bin/env python3
"""Phase 3 dev7 pool builder (host tooling, expansion6 integration).

Steps:
1. Load expansion6 stream cases (modern-cn / modern-west / classical-other),
   keep outcome_grade == 'A' only for pool use (B listed in report only).
2. Dedup: id must not exist anywhere in existing corpus inputs/rosters;
   (master, subject) fuzzy dup check reported, not auto-dropped.
3. Holdout8 selection: from NEW A cases only, stratified by stream and
   contamination (prefer low), deterministic sha256 ordering, N target 28.
   Writes phase3/holdout8/test_gold.jsonl + SEALED.md + phase3/holdout8-seal-log.md.
4. Remaining new A cases -> dev-add. Legacy 29 (expansion6/legacy-devadd)
   -> dev-add (tier registered separately).
5. inputs7/: dev6 inputs6 copies (split key stripped) + holdout6-used inputs
   + dev-add inputs (expansion6 stream inputs + legacy inputs).
6. roster7-additions.jsonl for all dev-add ids (outcome_record from cases).
7. splits7.json: dev7 id list + holdout8 id list + tiers.
Run from repo root: python3 benchmark/phase3/build_dev7.py
"""
import json, glob, os, hashlib, sys

P3 = 'benchmark/phase3'
STREAMS = ['modern-cn', 'modern-west', 'classical-other']
HOLDOUT_N = 28

def load_jsonl(p):
    return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]

def existing_ids():
    ids = set()
    for d in ('inputs', 'inputs6'):
        for f in glob.glob(f'{P3}/{d}/*.json'):
            ids.add(os.path.basename(f)[:-5])
    for f in glob.glob(f'{P3}/holdout*/test_gold.jsonl'):
        for r in load_jsonl(f):
            ids.add(r['id'])
    for f in glob.glob('benchmark/phase2/data/roster.jsonl'):
        for r in load_jsonl(f):
            ids.add(r['id'])
    return ids

def main():
    exist = existing_ids()
    new_cases = []
    for s in STREAMS:
        p = f'{P3}/expansion6/{s}/cases.jsonl'
        if not os.path.exists(p):
            print('MISSING stream file', p); sys.exit(1)
        for r in load_jsonl(p):
            r['_stream'] = s
            new_cases.append(r)
    a_cases = [r for r in new_cases if r.get('outcome_grade') == 'A']
    print(f'new cases total={len(new_cases)} A={len(a_cases)}')
    clash = [r['id'] for r in a_cases if r['id'] in exist]
    if clash:
        print('ID CLASH with existing corpus:', clash); sys.exit(1)
    # holdout selection: deterministic, stratified by stream then contamination
    def key(r):
        return hashlib.sha256(f"phase3-expansion6-holdout8:{r['id']}".encode()).hexdigest()
    # Selection rule (registered): ALL low-contamination new A cases go to
    # holdout (they carry the primary acceptance criteria); remaining slots
    # filled with high-contamination cases stratified across streams,
    # deterministic sha ordering within stream.
    lows = [r for r in a_cases if r.get('contamination') == 'low']
    highs = [r for r in a_cases if r.get('contamination') != 'low']
    holdout = list(lows)
    by_stream = {}
    for r in highs:
        by_stream.setdefault(r['_stream'], []).append(r)
    remaining = max(0, HOLDOUT_N - len(holdout))
    for s, rows in by_stream.items():
        rows_sorted = sorted(rows, key=key)
        share = max(1, round(remaining * len(rows) / max(1, len(highs))))
        holdout += rows_sorted[:share]
    holdout = sorted(holdout, key=key)
    if len(holdout) > HOLDOUT_N and len(lows) < HOLDOUT_N:
        # trim high-overflow deterministically, keep all lows
        high_part = sorted((r for r in holdout if r.get('contamination') != 'low'), key=key)
        holdout = lows + high_part[:HOLDOUT_N - len(lows)]
    hold_ids = {r['id'] for r in holdout}
    print('holdout8 size:', len(holdout), 'streams:', {s: sum(1 for r in holdout if r['_stream'] == s) for s in STREAMS},
          'low:', sum(1 for r in holdout if r.get('contamination') == 'low'))
    dev_add_new = [r for r in a_cases if r['id'] not in hold_ids]
    # --- write holdout8 gold (answers side only) ---
    os.makedirs(f'{P3}/holdout8', exist_ok=True)
    gold = []
    for r in sorted(holdout, key=lambda r: r['id']):
        gold.append({'id': r['id'], 'tradition': r.get('tradition', ''), 'master': r.get('master', ''),
                     'master_predictions': r.get('master_predictions', []),
                     'outcome': r.get('outcome', {}), 'outcome_grade': 'A',
                     'contamination': r.get('contamination', ''), 'stream': r['_stream'],
                     'provenance': r.get('provenance', {})})
    with open(f'{P3}/holdout8/test_gold.jsonl', 'w', encoding='utf-8') as f:
        for g in gold:
            f.write(json.dumps(g, ensure_ascii=False) + '\n')
    sha = hashlib.sha256(open(f'{P3}/holdout8/test_gold.jsonl', 'rb').read()).hexdigest()
    print('holdout8 gold sha256:', sha)
    # --- inputs7 ---
    os.makedirs(f'{P3}/inputs7', exist_ok=True)
    n_copy = 0
    for src_dir in ('inputs6',):
        for f in glob.glob(f'{P3}/{src_dir}/*.json'):
            r = json.load(open(f, encoding='utf-8')); r.pop('split', None)
            json.dump(r, open(f"{P3}/inputs7/{os.path.basename(f)}", 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
            n_copy += 1
    # holdout6 used inputs (from expansion4 inputs, ids LY-601..629 minus dev-add ones are in inputs6 already;
    # holdout6 ids are those in holdout6/test_gold not in inputs6)
    h6 = {r['id'] for r in load_jsonl(f'{P3}/holdout6/test_gold.jsonl')}
    added_h6 = 0
    for cid in sorted(h6):
        dst = f'{P3}/inputs7/{cid}.json'
        if not os.path.exists(dst):
            for cand in glob.glob(f'{P3}/expansion4/inputs/{cid}.json') + glob.glob(f'{P3}/expansion*/inputs/{cid}.json'):
                r = json.load(open(cand, encoding='utf-8')); r.pop('split', None)
                json.dump(r, open(dst, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
                added_h6 += 1
                break
            else:
                print('WARN no input found for holdout6 id', cid)
    # dev-add inputs: expansion6 streams + legacy
    roster_rows = []
    for r in dev_add_new:
        src = f"{P3}/expansion6/{r['_stream']}/inputs/{r['id']}.json"
        if not os.path.exists(src):
            print('WARN missing stream input', src); continue
        d = json.load(open(src, encoding='utf-8')); d.pop('split', None)
        json.dump(d, open(f"{P3}/inputs7/{r['id']}.json", 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        oc = r.get('outcome', {})
        roster_rows.append({'id': r['id'], 'outcome_record': oc.get('description', ''),
                            'tradition': r.get('tradition', ''), 'contamination': r.get('contamination', ''),
                            'source_tier': 'expansion6-new'})
    legacy_roster = load_jsonl(f'{P3}/expansion6/legacy-devadd/roster-legacy.jsonl')
    for r in legacy_roster:
        src = f"{P3}/expansion6/legacy-devadd/inputs/{r['id']}.json"
        d = json.load(open(src, encoding='utf-8')); d.pop('split', None)
        json.dump(d, open(f"{P3}/inputs7/{r['id']}.json", 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        roster_rows.append(r)
    with open(f'{P3}/roster7-additions.jsonl', 'w', encoding='utf-8') as f:
        for r in roster_rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    dev7_ids = sorted(os.path.basename(f)[:-5] for f in glob.glob(f'{P3}/inputs7/*.json'))
    splits = {'dev7': dev7_ids, 'holdout8': sorted(hold_ids),
              'counts': {'dev6_copied': n_copy, 'holdout6_added': added_h6,
                         'dev_add_new': len(dev_add_new), 'dev_add_legacy': len(legacy_roster),
                         'dev7_total': len(dev7_ids), 'holdout8_total': len(hold_ids)},
              'holdout8_gold_sha256': sha}
    json.dump(splits, open(f'{P3}/splits7.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('dev7 total:', len(dev7_ids), splits['counts'])

if __name__ == '__main__':
    main()
