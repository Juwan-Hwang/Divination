import json, pathlib
base=pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round82')
mp=json.load(open(base/'judging/host-mapping.json'))
inp=[json.loads(l) for l in open(base/'judging/judgeX-block4.jsonl')]
out=[]
for i,r in enumerate(inp):
    cid=mp[r['anon_id']]
    p=json.load(open(base/'predictions'/f'{cid}.json'))
    out.append(f"### {i+1} {r['anon_id']} {cid}\nPRED: {p['prediction_text']}\nOUTCOME: {r['outcome_record']}\n")
open(base/'judging/judgeX4_r82_pairs.txt','w').write("\n".join(out))
print(len(out))
