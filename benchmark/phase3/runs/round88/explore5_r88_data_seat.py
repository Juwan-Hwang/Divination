import json, pathlib, re
base=pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
ann=json.load(open(base/'data/case-annotations-r87.json'))
kw=['讹字','同式','先例','自引','伏神','底本未载','未载年','年柱','附标','省字']
for k in kw:
    hits=[a for a in ann['annotations'] if k in (a.get('finding','')+a.get('flag',''))]
    print(f"== {k}: {len(hits)}")
    for a in hits[:6]:
        print(' ', a['case_id'], a['disposition'], 'R'+str(a.get('registered_round')), '|', a.get('flag','')[:110])
# ours anon mapping for the 8 cases
hm=json.load(open(base/'runs/round88/acceptance/judging/host-mapping.json'))
print('hm keys', list(hm.keys()))
ours=hm.get('ours',{})
inv={v:k for k,v in ours.items()}
for cid in ['WHY-043','DA-051','DA-048','DA-055','WHY-068','WHY-069','GSZ-107','BY-030']:
    print(cid, 'ours anon', inv.get(cid))
# CYJ fidelity exception 46 & ziwei 6: search PREREG-r88 and FREEZE-r88
for fn in ['PREREG.md','FREEZE-r88.md','PREREG-ADDENDUM-r88.md']:
    t=open(base/'runs/round88'/fn, encoding='utf-8').read()
    for pat in ['fidelity','46','紫微','挂起','CZ-QX','测字']:
        for m in re.finditer(pat, t):
            s=max(0,m.start()-80); print(fn, pat, ':', t[s:m.end()+80].replace('\n',' '))
            break
