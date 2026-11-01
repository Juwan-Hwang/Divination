import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round94")
block=base/"judging/judgeX-block4.jsonl"
mapping=json.loads((base/"judging/host-mapping.json").read_text())
# mapping format check keys
print(type(mapping), list(mapping.items())[:2] if isinstance(mapping,dict) else mapping[:2])
rows=[json.loads(l) for l in block.read_text().splitlines() if l.strip()]
out=[]
for r in rows:
    anon=r["anon_id"]
    case=mapping.get(anon) if isinstance(mapping,dict) else None
    out.append((anon,case,r.get("outcome_record"),r.get("carry_note")))
print("rows",len(rows),"mapped",sum(1 for x in out if x[1]))
for a,c,o,n in out[:5]:
    print(a,c,o)
# save mapping list
(base/"judging/judgex4_map.json").write_text(json.dumps(out,ensure_ascii=False,indent=1))
