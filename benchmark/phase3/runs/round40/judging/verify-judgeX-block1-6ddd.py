import json, pathlib
base = pathlib.Path.home() / "workspace/divination/benchmark/phase3/runs/round40/judging"
packet = json.loads((base/"packet1.json").read_text(encoding="utf-8"))
want = [r["anon_id"] for r in packet]
lines = (base/"judgeX-block1.jsonl").read_text(encoding="utf-8").strip().split("\n")
rows = [json.loads(x) for x in lines]
errs = []
if len(rows) != len(want): errs.append(f"line count {len(rows)} != {len(want)}")
if [r["anon_id"] for r in rows] != want: errs.append("anon_id order/set mismatch")
if set(r["anon_id"] for r in rows) != set(want): errs.append("anon_id set mismatch")
for r in rows:
    if set(r.keys()) != {"anon_id","direction","claims","timing","total","pass","reason"}: errs.append(f"fields {r['anon_id']}")
    for k in ("direction","claims","timing"):
        v = r[k]
        if not (0 <= v <= 2) or (v*2) != int(v*2): errs.append(f"scale {r['anon_id']} {k}={v}")
    if abs(r["total"] - (r["direction"]+r["claims"]+r["timing"])) > 1e-9: errs.append(f"total {r['anon_id']}")
    if r["pass"] != (r["total"] >= 4): errs.append(f"pass {r['anon_id']}")
    if not r["reason"]: errs.append(f"reason empty {r['anon_id']}")
print("rows", len(rows), "pass", sum(1 for r in rows if r["pass"]), "errors", errs if errs else "none")
print("mean total", round(sum(r["total"] for r in rows)/len(rows), 3))
