import json, os, sys
base = os.path.expanduser("~/workspace/divination/benchmark/phase3/runs/round44")
batches = json.load(open(os.path.join(base, "batches.json"), encoding="utf-8"))
pred_dir = os.path.join(base, "predictions")
on_disk = set(f[:-5] for f in os.listdir(pred_dir) if f.endswith(".json"))
expected = {}
for bname, ids in batches.items():
    for cid in ids:
        expected[cid] = bname
missing = {cid: b for cid, b in expected.items() if cid not in on_disk}
extra = sorted(c for c in on_disk if c not in expected)
print("expected", len(expected), "on_disk", len(on_disk))
print("missing", len(missing))
from collections import Counter
print(Counter(missing.values()))
for cid, b in sorted(missing.items()):
    print("MISSING", b, cid)
for c in extra:
    print("EXTRA", c)
# field / case_id checks for present files
bad = []
trig_counts = {"changed_main": 0, "reserve_used": 0, "disputed": 0}
trig_n = 0
for cid in sorted(on_disk & set(expected)):
    p = os.path.join(pred_dir, cid + ".json")
    try:
        d = json.load(open(p, encoding="utf-8"))
    except Exception as e:
        bad.append((cid, "json:" + str(e))); continue
    if d.get("case_id") != cid:
        bad.append((cid, "case_id mismatch: " + str(d.get("case_id"))))
    for k in ("prediction_text", "basis", "confidence", "trigger"):
        if k not in d:
            bad.append((cid, "missing field " + k))
    t = d.get("trigger")
    if isinstance(t, dict):
        trig_n += 1
        for k in trig_counts:
            if t.get(k) is True:
                trig_counts[k] += 1
print("bad", len(bad))
for cid, why in bad:
    print("BAD", cid, why)
print("trigger files", trig_n, trig_counts)
