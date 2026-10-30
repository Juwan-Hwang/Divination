import json, sys
base = "/home/hatch/workspace/divination/benchmark/phase3/runs/holdout16-acceptance"
with open(base + "/judging/packet-master.json", encoding="utf-8") as f:
    packet = json.load(f)
packet_ids = [row["anon_id"] for row in packet]
rows = []
with open(base + "/judging/judgeM1.jsonl", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        line = line.strip()
        if not line:
            print(f"FAIL line {i}: empty"); sys.exit(1)
        rows.append(json.loads(line))
errors = []
if len(rows) != 40: errors.append(f"row count {len(rows)} != 40")
out_ids = [r["anon_id"] for r in rows]
if set(out_ids) != set(packet_ids): errors.append("anon_id set mismatch")
if len(set(out_ids)) != len(out_ids): errors.append("duplicate anon_id")
allowed = {0, 0.5, 1, 1.5, 2}
for r in rows:
    if set(r.keys()) != {"anon_id","direction","claims","timing","total","pass","reason"}:
        errors.append(f"{r.get('anon_id')}: keys {sorted(r.keys())}")
    for k in ("direction","claims","timing"):
        if r[k] not in allowed: errors.append(f"{r['anon_id']}: {k}={r[k]} not 0-2 step0.5")
    if abs(r["total"] - (r["direction"]+r["claims"]+r["timing"])) > 1e-9:
        errors.append(f"{r['anon_id']}: total mismatch")
    if r["pass"] != (r["total"] >= 4): errors.append(f"{r['anon_id']}: pass mismatch")
    if not isinstance(r["pass"], bool): errors.append(f"{r['anon_id']}: pass not bool")
    if not r["reason"]: errors.append(f"{r['anon_id']}: empty reason")
np = sum(1 for r in rows if r["pass"])
print(f"rows={len(rows)} pass={np} fail={len(rows)-np}")
if errors:
    print("VERIFY FAIL"); [print(" -", e) for e in errors]; sys.exit(1)
print("VERIFY OK: 40 lines, anon_id set equal to packet, fields/steps/total/pass all consistent")
