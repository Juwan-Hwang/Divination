import json, pathlib
base = pathlib.Path(__file__).parent
packet = json.loads((base / "packet-ours.json").read_text(encoding="utf-8"))
lines = (base / "judgeO1.jsonl").read_text(encoding="utf-8").strip().splitlines()
rows = [json.loads(l) for l in lines]
pids = [p["anon_id"] for p in packet]
rids = [r["anon_id"] for r in rows]
assert len(rows) == 29 == len(packet), len(rows)
assert set(rids) == set(pids) and len(set(rids)) == 29
for r in rows:
    assert set(r) == {"anon_id","direction","claims","timing","total","pass","gap_note"}, r
    assert all(isinstance(r[k], int) and 0 <= r[k] <= 2 for k in ("direction","claims","timing"))
    assert r["total"] == r["direction"] + r["claims"] + r["timing"]
    assert r["pass"] == (r["total"] >= 4)
tot = sum(r["total"] for r in rows)
print("rows", len(rows))
print("sum", tot)
print("mean", f"{tot/len(rows):.3f}")
print("pass", sum(1 for r in rows if r["pass"]))
print("VERIFY_OK")
