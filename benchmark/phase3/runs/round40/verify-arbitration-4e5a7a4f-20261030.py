import json, pathlib
base = pathlib.Path.home() / "workspace/divination/benchmark/phase3/runs/round40"
scores = base / "judging/arbitration-scores.jsonl"
packet = base / "judging/arbitration-packet.json"
mapping = base / "judging/host-mapping.json"
pred = base / "predictions/YM-023.json"

lines = scores.read_text(encoding="utf-8").strip().splitlines()
assert len(lines) == 1, len(lines)
row = json.loads(lines[0])
assert set(row.keys()) == {"anon_id", "direction", "claims", "timing", "total", "reason"}, row.keys()
assert row["anon_id"] == "P3-4e5a7a4f"
for k in ("direction", "claims", "timing"):
    v = row[k]
    assert 0 <= v <= 2 and (v * 2) == int(v * 2), (k, v)
assert row["total"] == row["direction"] + row["claims"] + row["timing"]
assert (row["total"] >= 4) is True  # pass = total>=4
pkt = json.loads(packet.read_text(encoding="utf-8"))
assert len(pkt) == 1 and pkt[0]["anon_id"] == "P3-4e5a7a4f"
assert pkt[0]["outcome_record"] == "后甲午榜中式（辛卯年是岁失利）。"
mp = json.loads(mapping.read_text(encoding="utf-8"))
assert mp["P3-4e5a7a4f"] == "YM-023"
p = json.loads(pred.read_text(encoding="utf-8"))
assert p["case_id"] == "YM-023" and "卯月" in p["prediction_text"] and "等级中上非极贵" in p["prediction_text"]
assert "结局无可核时点" in row["reason"]
print("SELFCHECK OK: 1 line, fields ok, steps ok, total=sum, mapping YM-023 ok, outcome ok")
print(json.dumps(row, ensure_ascii=False))
