import json, pathlib
base=pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
ann=json.load(open(base/'data/case-annotations-r87.json'))
for a in ann['annotations']:
    if a['case_id']=='GSZ-069':
        print('GSZ-069:', json.dumps(a, ensure_ascii=False)[:2000])
for k in ['循环','本案即','同一案','污染','取用分歧','两路','宫首卦','本宫']:
    hits=[a for a in ann['annotations'] if k in (a.get('finding','')+a.get('flag',''))]
    print(f"== {k}: {len(hits)}")
    for a in hits[:5]:
        print(' ', a['case_id'], a['disposition'], 'R'+str(a.get('registered_round')), '|', a.get('flag','')[:120])
card=json.load(open(base/'holdout31/inputs/WHY-043.json'))
print('WHY-043 card full:', json.dumps(card, ensure_ascii=False))
print('WHY-043 anchors keys:', list(card.get('anchors',{}).keys()))
# check other WHY cards for hidden_lines field presence convention
import glob
for p in sorted(glob.glob(str(base/'holdout31/inputs/*.json'))):
    c=json.load(open(p))
    ak=list(c.get('anchors',{}).keys())
    if 'hidden_lines' in ak or 'hidden' in str(ak):
        print('hidden field in', p)
print('sample WHY-037 anchors keys:', list(json.load(open(base/'holdout31/inputs/WHY-037.json')).get('anchors',{}).keys()))
