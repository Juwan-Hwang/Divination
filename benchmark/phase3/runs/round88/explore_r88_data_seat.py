import json, collections, hashlib, pathlib
base=pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
ann=json.load(open(base/'data/case-annotations-r87.json'))
print('_provenance:', ann['_provenance'][:600])
print('counts:', json.dumps(ann['counts'], ensure_ascii=False))
print('special_checks len', len(ann['special_checks']))
for sc in ann['special_checks'][-6:]:
    print('SC:', json.dumps(sc, ensure_ascii=False)[:800])
# R87 new entries
new=[a for a in ann['annotations'] if a.get('registered_round')==87]
print('new87 count', len(new), collections.Counter(a['disposition'] for a in new))
for a in new[:3]:
    print('NEW sample:', json.dumps(a, ensure_ascii=False)[:1500])
# the 43 platform ids from r87 addendum 3.1
ids43=["BZ-021","AS-003","AS-012","AS-206","BZ-031","DT-004","DT-006","LY-018","LY-103","LY-301","LY-416","LY-525","LY-603","LY-620","LY-621","OC-024","OC-025","YM-002","YM-032","YY-019","ZY-003","MP-001","MP-002","MP-003","MP-004","MP-005","MP-006","MP-007","MP-008","MP-009","MP-010","MP-011","MP-013","MP-014","MP-017","MP-018","MP-019","WP-008","WP-009","WP-010","WP-011","WP-012","WP-013"]
byid={}
for a in ann['annotations']:
    byid.setdefault(a['case_id'], []).append(a)
for cid in ids43:
    lst=[a for a in byid.get(cid,[]) if a.get('registered_round')==87]
    print(cid, 'r87entries', len(lst), lst[0]['disposition'] if lst else None, 'anon', lst[0].get('anon_id') if lst else None)
for cid in ["CYJ-006","CYJ-007","CYJ-008","CYJ-009","CYJ-010"]:
    lst=[a for a in byid.get(cid,[]) if a.get('registered_round')==87]
    print(cid, 'r87entries', len(lst), lst[0]['disposition'] if lst else None)
# AS-307
print('AS-307 entries', len(byid.get('AS-307',[])), [(a['disposition'], a.get('registered_round')) for a in byid.get('AS-307',[])])
print('total disp', collections.Counter(a['disposition'] for a in ann['annotations']))
# manifest r88
man=json.load(open(base/'runs/round88/judging/outcome-manifest.json'))
layer=man['_r87_carryover_notes_addendum']
print('layer43 len', len(layer), 'keys==ids43 set?', set(layer.keys())==set(ids43))
mismatch=[]
for cid in ids43:
    sug=[a for a in byid.get(cid,[]) if a.get('registered_round')==87][0]['manifest_carry_suggestion']
    if layer[cid]!=sug:
        mismatch.append(cid)
print('layer vs suggestion mismatch', mismatch)
print('_r87_manifest_note:', man['_r87_manifest_note'][:800])
print('_r88_manifest_note:', man['_r88_manifest_note'][:800])
# cases payload sample
for cid in ['BZ-021','AS-003']:
    print(cid, 'case payload:', json.dumps(man['cases'][cid], ensure_ascii=False)[:1000])
# sha of file and cases
raw=open(base/'runs/round88/judging/outcome-manifest.json','rb').read()
print('manifest sha256', hashlib.sha256(raw).hexdigest())
cases_json=json.dumps(man['cases'], ensure_ascii=False, sort_keys=True)
print('cases structured sha?', hashlib.sha256(cases_json.encode()).hexdigest())
