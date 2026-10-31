import json, pathlib
base=pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
ann=json.load(open(base/'data/case-annotations-r87.json'))
for a in ann['annotations']:
    if a['case_id'] in ('CYJ-006','LY-537','YM-070') :
        print(a['case_id'], json.dumps(a, ensure_ascii=False)[:1200]); print()
man=json.load(open(base/'runs/round88/judging/outcome-manifest.json'))
for cid in ['CYJ-006','CYJ-007','CYJ-008','CYJ-009','CYJ-010']:
    print(cid, 'in layer?', cid in man['_r87_carryover_notes_addendum'], 'in cases?', cid in man['cases'])
# baseline
for cid, needle in [('BZ-036','盲测比对须注'),('BZ-042','（盲测比对时以格局大富一项为主）'),('BZ-105','使用时须分开统计'),('LY-204','勿以此斷')]:
    txt=man['cases'].get(cid,'')
    print('BASE', cid, needle, 'present?', needle in txt, 'ctx:', txt[max(0,txt.find(needle)-40):txt.find(needle)+len(needle)+40] if needle in txt else txt[:200])
print('LR2 split:', json.dumps(man['_r56_lr2016_split'], ensure_ascii=False)[:1500])
# packets search LR2-016 editor_note
import glob
hm=json.load(open(base/'runs/round88/judging/host-mapping.json'))
print('host-mapping type', type(hm), str(hm)[:600])
# find anon for LR2-016
def find(obj, target, path=''):
    if isinstance(obj, dict):
        for k,v in obj.items():
            if v==target or k==target: print('found', path, k, str(v)[:200])
            find(v, target, path+'/'+str(k))
    elif isinstance(obj, list):
        for i,v in enumerate(obj): find(v, target, path+f'[{i}]')
find(hm,'LR2-016')
for pf in sorted((base/'runs/round88/judging').glob('packet*.json')):
    data=open(pf, encoding='utf-8').read()
    if 'LR2-016' in data or 'editor_note' in data:
        print(pf.name, 'has LR2-016?', 'LR2-016' in data, 'editor_note count', data.count('editor_note'))
