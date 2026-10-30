# Host clerical normalization: H16-LR seat wrote semantically identical
# trigger values (all false, empty reason) under placeholder key names
# (first/second/third). Rewrite keys to the frozen template names;
# values unchanged.
import json, os
acc = os.path.dirname(os.path.abspath(__file__))
batches = json.load(open(os.path.join(acc, 'batches.json')))
std = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}
n = 0
for cid in batches['H16-LR']:
    p = os.path.join(acc, 'predictions', cid + '.json')
    d = json.load(open(p))
    t = d.get('trigger') or {}
    vals = [v for k, v in t.items() if k != 'reason']
    assert all(v is False for v in vals) and t.get('reason', '') == '', (cid, t)
    d['trigger'] = dict(std)
    json.dump(d, open(p, 'w'), ensure_ascii=False, indent=1)
    n += 1
print('normalized', n)
