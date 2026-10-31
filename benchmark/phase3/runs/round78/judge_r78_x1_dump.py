import json, sys, pathlib
base=pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round78')
lines=(base/'judging/judgeX-block1.jsonl').read_text().splitlines()
mp=json.loads((base/'judging/host-mapping.json').read_text())
lo=int(sys.argv[1]); hi=int(sys.argv[2])
for i,l in enumerate(lines[lo:hi], start=lo):
    r=json.loads(l)
    aid=r['anon_id']; cid=mp.get(aid)
    pred=json.loads((base/'predictions'/f'{cid}.json').read_text())
    print(f"=== {i} {aid} {cid}")
    print("OUT:", r.get('outcome_record'))
    cn=r.get('carry_note') or r.get('editor_note')
    if cn:
        # print only first 300 chars to detect type
        print("NOTE:", cn[:350].replace('\n',' '))
    print("PRED:", pred.get('prediction_text'))
    print()
