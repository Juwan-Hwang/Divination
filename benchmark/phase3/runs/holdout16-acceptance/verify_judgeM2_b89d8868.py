import json, sys
base = "/home/hatch/workspace/divination/benchmark/phase3/runs/holdout16-acceptance/judging"
with open(base + "/packet-master.json", encoding="utf-8") as f:
    packet = json.load(f)
packet_ids = [r["anon_id"] for r in packet]
rows = []
with open(base + "/judgeM2.jsonl", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        line = line.strip()
        assert line, f"line {i} empty"
        rows.append(json.loads(line))
errors = []
if len(rows) != 40:
    errors.append(f"row count {len(rows)} != 40")
out_ids = [r["anon_id"] for r in rows]
if set(out_ids) != set(packet_ids):
    errors.append(f"id set mismatch missing={set(packet_ids)-set(out_ids)} extra={set(out_ids)-set(packet_ids)}")
if len(out_ids) != len(set(out_ids)):
    errors.append("duplicate anon_id")
allowed = {0, 0.5, 1, 1.5, 2}
for r in rows:
    for k in ("direction", "claims", "timing"):
        if r[k] not in allowed:
            errors.append(f"{r['anon_id']} {k}={r[k]} not in 0-2 step0.5")
    if abs(r["total"] - (r["direction"] + r["claims"] + r["timing"])) > 1e-9:
        errors.append(f"{r['anon_id']} total mismatch")
    if r["pass"] != (r["total"] >= 4):
        errors.append(f"{r['anon_id']} pass mismatch")
    if r["timing"] == 0 and "无应期" not in r["reason"]:
        errors.append(f"{r['anon_id']} timing=0 without note")
    if not r["reason"]:
        errors.append(f"{r['anon_id']} empty reason")
npass = sum(1 for r in rows if r["pass"])
print(f"rows={len(rows)} packet={len(packet_ids)} pass={npass} fail={len(rows)-npass}")
print("ERRORS:", errors if errors else "none")
sys.exit(1 if errors else 0)
