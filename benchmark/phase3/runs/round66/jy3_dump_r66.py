import json
base="/home/hatch/workspace/divination/benchmark/phase3/runs/round66"
with open(base+"/judging/host-mapping.json") as f: mapping=json.load(f)
with open(base+"/judging/judgeY-block3.jsonl") as f:
    rows=[json.loads(l) for l in f if l.strip()]
for r in rows:
    anon=r["anon_id"]; cid=mapping[anon]
    with open(f"{base}/predictions/{cid}.json") as f: p=json.load(f)
    txt=p.get("prediction_text","")
    print(f"===== {anon} | {cid} =====")
    print(txt)
    print()
