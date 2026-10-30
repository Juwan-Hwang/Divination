import json, pathlib
base = pathlib.Path.home() / "workspace/divination/benchmark/phase3/runs/round54"
target = base / "judging/judgeX-block4.jsonl"
rows=[]
with open(target, encoding="utf-8") as f:
    for i,line in enumerate(f,1):
        line=line.strip()
        assert line, f"empty line {i}"
        r=json.loads(line)
        assert set(r.keys())=={"anon_id","direction","claims","timing","total","pass","reason"}, (i, r.keys())
        assert abs(r["total"]-(r["direction"]+r["claims"]+r["timing"]))<1e-9, i
        assert r["pass"]==(r["total"]>=4), i
        for k in ("direction","claims","timing"):
            assert r[k] in (0,0.5,1,1.5,2), (i,k,r[k])
        rows.append(r)
print("lines",len(rows))
print("unique anon",len(set(r["anon_id"] for r in rows)))
print("pass count",sum(1 for r in rows if r["pass"]))
print("first",rows[0]["anon_id"],"last",rows[-1]["anon_id"])
