import json, pathlib
base = pathlib.Path(__file__).parent
packet = json.loads((base / "packet-master.json").read_text(encoding="utf-8"))
rows = [json.loads(l) for l in (base / "judgeM2.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
pids = [p["anon_id"] for p in packet]
rids = [r["anon_id"] for r in rows]
assert len(rows) == 40, len(rows)
assert set(rids) == set(pids) and len(set(rids)) == 40, "anon set mismatch"
for r in rows:
    assert set(r) == {"anon_id", "direction", "claims", "timing", "total", "pass", "reason"}, r
    for k in ("direction", "claims", "timing"):
        assert r[k] in [i * 0.5 for i in range(5)], (r["anon_id"], k, r[k])
    assert abs(r["total"] - (r["direction"] + r["claims"] + r["timing"])) < 1e-9, r["anon_id"]
    assert r["pass"] == (r["total"] >= 4), r["anon_id"]
print("lines:", len(rows))
print("pass:", sum(r["pass"] for r in rows))
print("ALL CHECKS OK")
