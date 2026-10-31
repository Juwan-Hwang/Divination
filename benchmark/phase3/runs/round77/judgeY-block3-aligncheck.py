import json, re, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round77")
mapping=json.loads((base/"judging/host-mapping.json").read_text())
rows=[json.loads(l) for l in (base/"judging/judgeY-block3.jsonl").read_text().splitlines() if l.strip()]
rows.sort(key=lambda r:r["anon_id"])
txt=(base/"judgeY-block3-scorebuild.py").read_text()
entries=re.findall(r'\("P3-[0-9a-f]+",([\d.]+),([\d.]+),([\d.]+),"([^"]*)"\)',txt)
print("entries",len(entries),"rows",len(rows))
for i,(r,e) in enumerate(zip(rows,entries)):
    cid=mapping[r["anon_id"]]
    print(i, r["anon_id"], cid, "| score:", e[0],e[1],e[2], "| reason:", e[3][:40], "| outcome:", str(r.get("outcome_record",""))[:40])
