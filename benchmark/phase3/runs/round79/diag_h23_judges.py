import json, pathlib, collections
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round79/acceptance/judging")
def load(n):
    d={}
    with open(base/f"{n}.jsonl") as f:
        for line in f:
            if line.strip():
                o=json.loads(line); d[o["anon_id"]]=o
    return d
for pair in [("judgeO1","judgeO2"),("judgeM1","judgeM2")]:
    a,b=load(pair[0]),load(pair[1])
    print(pair, len(a), len(b))
    # anon prefixes differ? check intersection
    print("common", len(set(a)&set(b)))
    # They likely share suffix? print ids
    for k in list(a)[:2]: print(k, b.get(k))
    # try pairing by order in file
    la=list(a.values()); lb=list(b.values())
    for x,y in zip(la,lb):
        print(f"meanTotal={(x['total']+y['total'])/2} dirMean={(x['direction']+y['direction'])/2} claimsMean={(x['claims']+y['claims'])/2} timMean={(x['timing']+y['timing'])/2}")
        print(" 1:",x['reason'])
        print(" 2:",y['reason'])
    print()
