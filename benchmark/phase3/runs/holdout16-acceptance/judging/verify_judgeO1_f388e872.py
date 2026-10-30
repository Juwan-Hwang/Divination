import json
from pathlib import Path

base = Path(__file__).resolve().parent
packet_path = base / "packet-ours.json"
judge_path = base / "judgeO1.jsonl"

packet = json.loads(packet_path.read_text(encoding="utf-8"))
packet_ids = [row["anon_id"] for row in packet]

lines = judge_path.read_text(encoding="utf-8").splitlines()
assert len(lines) == 40, f"line count {len(lines)} != 40"
assert len(packet_ids) == 40, f"packet count {len(packet_ids)} != 40"

seen = []
passes = 0
allowed = {i * 0.5 for i in range(5)}
for idx, line in enumerate(lines, 1):
    row = json.loads(line)
    assert set(row.keys()) == {"anon_id", "direction", "claims", "timing", "total", "pass", "reason"}, (idx, row.keys())
    for k in ("direction", "claims", "timing"):
        assert row[k] in allowed, (idx, k, row[k])
    assert row["total"] == row["direction"] + row["claims"] + row["timing"], (idx, row)
    assert row["pass"] == (row["total"] >= 4), (idx, row)
    assert isinstance(row["pass"], bool)
    assert isinstance(row["reason"], str) and row["reason"].strip()
    if row["timing"] == 1 and "结局无可核时点" not in row["reason"]:
        pass  # timing=1 may also be a partial-hit score; not asserted
    seen.append(row["anon_id"])
    passes += 1 if row["pass"] else 0

assert seen == packet_ids, "anon_id order/set mismatch with packet"
assert len(set(seen)) == 40, "duplicate anon_id"
print(f"OK lines={len(lines)} packet={len(packet_ids)} id_set_equal=True pass_count={passes}")
