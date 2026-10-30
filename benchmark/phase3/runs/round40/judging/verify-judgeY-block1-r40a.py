# self-check for judgeY-block1.jsonl (explicit paths only, no glob)
import json, pathlib
base = pathlib.Path(__file__).resolve().parent
pkt = json.loads((base / "packet1.json").read_text(encoding="utf-8"))
lines = (base / "judgeY-block1.jsonl").read_text(encoding="utf-8").strip().split("\n")
rows = [json.loads(x) for x in lines]
errs = []
if len(rows) != len(pkt):
    errs.append(f"line count {len(rows)} != packet {len(pkt)}")
pkt_ids = [r["anon_id"] for r in pkt]
out_ids = [r["anon_id"] for r in rows]
if set(out_ids) != set(pkt_ids):
    errs.append("anon_id set mismatch")
if len(set(out_ids)) != len(out_ids):
    errs.append("duplicate anon_id in output")
if out_ids != pkt_ids:
    errs.append("order differs from packet (set equal but order differs)")
allowed = {0, 0.5, 1.0, 1.5, 2.0}
for r in rows:
    for k in ("anon_id", "direction", "claims", "timing", "total", "pass", "reason"):
        if k not in r:
            errs.append(f"{r.get('anon_id')} missing field {k}")
    for k in ("direction", "claims", "timing"):
        if r[k] not in allowed:
            errs.append(f"{r['anon_id']} {k}={r[k]} not in 0-2 step0.5")
    if abs(r["total"] - (r["direction"] + r["claims"] + r["timing"])) > 1e-9:
        errs.append(f"{r['anon_id']} total != sum")
    if r["pass"] != (r["total"] >= 4):
        errs.append(f"{r['anon_id']} pass flag wrong")
    if not str(r["reason"]).strip():
        errs.append(f"{r['anon_id']} empty reason")
    # special timing notes
    if r["anon_id"] in ("P3-014beff5", "P3-03996b68", "P3-1fda090a") and "预测本身无应期" not in r["reason"]:
        errs.append(f"{r['anon_id']} missing no-timing note")
print("lines:", len(rows), "pass:", sum(1 for r in rows if r["pass"]),
      "fail:", sum(1 for r in rows if not r["pass"]))
print("errors:", errs if errs else "NONE")
