import json, os
base = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(base))
batches = json.load(open(os.path.join(base, 'batches.json')))
ids = [i for k in sorted(batches) for i in batches[k]]
assert len(ids) == 487 and len(set(ids)) == 487, (len(ids), len(set(ids)))
req = ['case_id','prediction_text','basis','confidence','trigger']
trig_keys = ['changed_main','reserve_used','disputed','reason']
bad = []
tc = {'changed_main':0,'reserve_used':0,'disputed':0}
for cid in ids:
    p = os.path.join(base, 'predictions', cid + '.json')
    if not os.path.exists(p):
        bad.append((cid, 'missing')); continue
    try:
        d = json.load(open(p))
    except Exception as e:
        bad.append((cid, 'json:' + str(e))); continue
    for f in req:
        if f not in d: bad.append((cid, 'field:' + f))
    if d.get('case_id') != cid: bad.append((cid, 'id-mismatch'))
    t = d.get('trigger') or {}
    for k in trig_keys:
        if k not in t: bad.append((cid, 'trig:' + k))
    for k in tc:
        if t.get(k) is True: tc[k] += 1
    c = d.get('confidence')
    if not isinstance(c, (int, float)) or not (0 <= c <= 1): bad.append((cid, 'conf'))
    if not (d.get('prediction_text') or '').strip(): bad.append((cid, 'empty-text'))
print('checked', len(ids), 'bad', len(bad))
for b in bad[:20]: print(b)
print('trigger counts (all):', tc)
