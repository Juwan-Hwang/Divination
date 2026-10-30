import json, pathlib
base = pathlib.Path(__file__).resolve().parent
packet = json.loads((base/"packet4.json").read_text())
lines = (base/"judgeX-block4.jsonl").read_text(encoding="utf-8").strip().splitlines()
rows = [json.loads(x) for x in lines]
assert len(rows)==len(packet)==121, (len(rows), len(packet))
pids = [e["anon_id"] for e in packet]
rids = [r["anon_id"] for r in rows]
assert set(rids)==set(pids) and len(set(rids))==121
for r in rows:
    assert set(r.keys())=={"anon_id","direction","claims","timing","total","pass","reason"}, r
    for k in ("direction","claims","timing"):
        v=r[k]; assert 0<=v<=2 and (v*2)==int(v*2), r
    assert abs(r["total"]-(r["direction"]+r["claims"]+r["timing"]))<1e-9, r
    assert r["pass"]==(r["total"]>=4), r
    assert r["reason"]
    if r["timing"]==1 and "结局无可核时点" in r["reason"]:
        pass
np = sum(1 for r in rows if r["pass"])
print(f"VERIFY OK lines={len(rows)} anon_set_equal=True totals_ok=True pass_count={np}")
