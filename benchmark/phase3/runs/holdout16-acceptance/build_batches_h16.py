import json, os
acc = os.path.dirname(os.path.abspath(__file__))
inp = os.path.join(os.path.dirname(os.path.dirname(acc)), 'holdout16', 'inputs')
ids = sorted(f[:-5] for f in os.listdir(inp) if f.endswith('.json'))
assert len(ids) == 40, len(ids)
cezi = [i for i in ids if i.startswith('ZC-')]
liuren = [i for i in ids if not i.startswith('ZC-')]
assert len(cezi) == 20 and len(liuren) == 20, (len(cezi), len(liuren))
batches = {'H16-CZ': cezi, 'H16-LR': liuren}
json.dump(batches, open(os.path.join(acc, 'batches.json'), 'w'), ensure_ascii=False, indent=1)
print('batches:', {k: len(v) for k, v in batches.items()})
