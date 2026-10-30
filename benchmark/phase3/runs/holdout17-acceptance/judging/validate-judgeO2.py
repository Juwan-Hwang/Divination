import json, pathlib
base = pathlib.Path(__file__).parent
packet = json.loads((base / "packet-ours.json").read_text(encoding="utf-8"))
lines = (base / "judgeO2.jsonl").read_text(encoding="utf-8").strip().splitlines()
rows = [json.loads(l) for l in lines]
pids = {p["anon_id"] for p in packet}
rids = [r["anon_id"] for r in rows]
assert len(rows) == 40, len(rows)
assert set(rids) == pids and len(set(rids)) == 40, "anon set mismatch"
for r in rows:
    assert set(r) == {"anon_id","direction","claims","timing","total","pass","reason"}, r
    for k in ("direction","claims","timing"):
        assert r[k] in (0,0.5,1,1.5,2), r
    assert abs(r["total"] - (r["direction"]+r["claims"]+r["timing"])) < 1e-9, r
    assert r["pass"] == (r["total"] >= 4), r
print("lines:", len(rows))
print("pass:", sum(r["pass"] for r in rows))
print("mean total:", sum(r["total"] for r in rows)/len(rows))
print("ALL CHECKS OK")
