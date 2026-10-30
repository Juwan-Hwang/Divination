import json, pathlib, sys
base = pathlib.Path(__file__).resolve().parent
packet_path = base / "judging" / "packet-ours.json"
judge_path = base / "judging" / "judgeO2.jsonl"
packet = json.loads(packet_path.read_text(encoding="utf-8"))
packet_ids = [r["anon_id"] for r in packet]
lines = judge_path.read_text(encoding="utf-8").splitlines()
errors = []
rows = []
for i, line in enumerate(lines, 1):
    if not line.strip():
        errors.append(f"line {i}: blank")
        continue
    try:
        r = json.loads(line)
    except Exception as e:
        errors.append(f"line {i}: bad json {e}")
        continue
    rows.append(r)
    for k in ("direction", "claims", "timing"):
        v = r.get(k)
        if v is None or v < 0 or v > 2 or (v * 2) != int(v * 2):
            errors.append(f"line {i}: {k}={v} not in 0-2 step0.5")
    if abs(r.get("total", -999) - (r["direction"] + r["claims"] + r["timing"])) > 1e-9:
        errors.append(f"line {i}: total mismatch")
    if r.get("pass") != (r.get("total", 0) >= 4):
        errors.append(f"line {i}: pass mismatch")
    if not r.get("reason"):
        errors.append(f"line {i}: empty reason")
    # timing=1 rows used for the no-verifiable-time-point convention must carry the phrase,
    # except rows where reason gives a substantive partial-hit timing basis
    if r.get("timing") == 1 and "结局无可核时点" not in r.get("reason", ""):
        # flag for manual check, not auto-fail: print warning
        print(f"WARN line {i} {r.get('anon_id')}: timing=1 without phrase")
ids = [r["anon_id"] for r in rows]
if len(rows) != 40:
    errors.append(f"row count {len(rows)} != 40")
if len(set(ids)) != len(ids):
    errors.append("duplicate anon_id")
if set(ids) != set(packet_ids):
    errors.append(f"anon_id set mismatch: missing={set(packet_ids)-set(ids)} extra={set(ids)-set(packet_ids)}")
passes = sum(1 for r in rows if r["pass"])
print(f"rows={len(rows)} passes={passes} packet={len(packet_ids)}")
if errors:
    print("FAIL")
    for e in errors:
        print(e)
    sys.exit(1)
print("OK: all rows valid json, scores in range/step, total=sum, pass=total>=4, anon_id set equal")
