import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round82")
rows=[json.loads(l) for l in open(base/"judging/judgeY-block4.jsonl",encoding="utf-8")]
mp=json.load(open(base/"judging/host-mapping.json",encoding="utf-8"))
out=open(base/"judging/judgeY4_r82_pairs.txt","w",encoding="utf-8")
for i,r in enumerate(rows):
    cid=mp[r["anon_id"]]
    p=json.load(open(base/f"predictions/{cid}.json",encoding="utf-8"))
    pt=p.get("prediction_text") or p.get("prediction") or str(p)
    if not isinstance(pt,str): pt=json.dumps(pt,ensure_ascii=False)
    out.write(f"\n===== {i+1} {r['anon_id']} {cid} =====\nOUTCOME: {r['outcome_record']}\nPRED: {pt}\n")
    if r.get("carry_note"): out.write(f"CARRY: {r['carry_note'][:400]}\n")
out.close()
print("done",len(rows))
