import json

base = "/home/hatch/workspace/divination/benchmark/phase3/runs/holdout18-acceptance/judging"
with open(base + "/packet-ours.json", encoding="utf-8") as f:
    packet = json.load(f)
with open(base + "/judgeO2.jsonl", encoding="utf-8") as f:
    lines = [ln for ln in f.read().splitlines() if ln.strip()]

rows = [json.loads(ln) for ln in lines]
packet_ids = [p["anon_id"] for p in packet]
row_ids = [r["anon_id"] for r in rows]
assert len(lines) == 30, len(lines)
assert len(packet) == 30
assert row_ids == packet_ids, "anon_id order/set mismatch"
for r in rows:
    assert abs(r["total"] - (r["direction"] + r["claims"] + r["timing"])) < 1e-9, r
    assert r["pass"] == (r["total"] >= 4), r
    for k in ("direction", "claims", "timing"):
        assert 0 <= r[k] <= 2 and (r[k] * 2) == int(r[k] * 2), r
totals = [r["total"] for r in rows]
print("lines:", len(lines))
print("ids_match_packet_order: True")
print("sum_and_pass_consistent: True")
print("pass_count:", sum(1 for r in rows if r["pass"]))
print("fail_count:", sum(1 for r in rows if not r["pass"]))
print("total_distribution:", {t: totals.count(t) for t in sorted(set(totals))})
print("mean_total:", sum(totals) / len(totals))
