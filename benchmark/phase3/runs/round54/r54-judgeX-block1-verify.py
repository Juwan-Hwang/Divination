import json, pathlib, re
base = pathlib.Path(__file__).parent
rows=[json.loads(l) for l in (base/"judging"/"judgeX-block1.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
dump=(base/"r54-judgeX-block1-dump.txt").read_text(encoding="utf-8")
anons_dump=re.findall(r"=== (P3-[0-9a-f]+) \|", dump)
assert len(rows)==122, len(rows)
assert [r["anon_id"] for r in rows]==anons_dump, "anon order/set mismatch"
for r in rows:
    assert set(r.keys())=={"anon_id","direction","claims","timing","total","pass","reason"}, r
    assert abs(r["direction"]+r["claims"]+r["timing"]-r["total"])<1e-9, r
    assert r["pass"]==(r["total"]>=4), r
    for k in ("direction","claims","timing"):
        v=r[k]; assert 0<=v<=2 and abs(v*2-round(v*2))<1e-9, r
print("OK rows",len(rows),"pass",sum(1 for r in rows if r["pass"]),"fail",sum(1 for r in rows if not r["pass"]))
print("sum totals",sum(r["total"] for r in rows))
