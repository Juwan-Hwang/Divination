import json, pathlib
base = pathlib.Path(__file__).resolve().parent
packet = json.loads((base / "judging" / "packet3.json").read_text(encoding="utf-8"))
lines = (base / "judging" / "judgeY-block3.jsonl").read_text(encoding="utf-8").strip().splitlines()
rows = [json.loads(x) for x in lines]
packet_ids = [p["anon_id"] for p in packet]
out_ids = [r["anon_id"] for r in rows]
assert len(rows) == len(packet) == 122, (len(rows), len(packet))
assert out_ids == packet_ids, "order/set mismatch"
assert set(out_ids) == set(packet_ids) and len(set(out_ids)) == 122
allowed = {0, 0.5, 1, 1.5, 2}
for r in rows:
    assert set(r.keys()) == {"anon_id","direction","claims","timing","total","pass","reason"}, r
    assert r["direction"] in allowed and r["claims"] in allowed and r["timing"] in allowed, r
    assert abs(r["total"] - (r["direction"]+r["claims"]+r["timing"])) < 1e-9, r
    assert r["pass"] == (r["total"] >= 4), r
    assert isinstance(r["reason"], str) and len(r["reason"]) > 5, r
print("SELFCHECK OK lines=122 anon_set_equal=True order_equal=True totals_ok=True pass_ok=True")
print("pass_count=", sum(1 for r in rows if r["pass"]))
print("score_sum=", sum(r["total"] for r in rows), "mean=", sum(r["total"] for r in rows)/len(rows))
