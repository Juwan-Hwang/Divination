import json, os
BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round65"
batches = json.load(open(os.path.join(BASE, "batches.json"), encoding="utf-8"))
ids = batches["B10"] + batches["B11"] + batches["B12"]
ok = 0; total = 0; problems = []
trig = {"changed_main": 0, "reserve_used": 0, "disputed": 0}
trad = {}
for cid in ids:
    p = os.path.join(BASE, "predictions", cid + ".json")
    try:
        raw = open(p, "rb").read(); total += len(raw)
        o = json.loads(raw.decode("utf-8"))
    except Exception as e:
        problems.append((cid, str(e))); continue
    assert o["case_id"] == cid
    assert set(o.keys()) == {"case_id", "prediction_text", "basis", "confidence", "trigger"}, o.keys()
    assert isinstance(o["confidence"], (int, float)) and 0 <= o["confidence"] <= 1
    t = o["trigger"]
    assert set(t.keys()) == {"changed_main", "reserve_used", "disputed", "reason"}
    assert all(isinstance(t[k], bool) for k in ("changed_main", "reserve_used", "disputed")) and isinstance(t["reason"], str) and t["reason"]
    lines = o["basis"].split("\n")
    assert lines[0] == "tradition=liuyao", lines[0]
    assert lines[1].startswith("systems_used="), lines[1]
    trad[lines[0]] = trad.get(lines[0], 0) + 1
    pt = o["prediction_text"]
    assert "方向" in pt and "窗口" in pt and "主坐标" in pt, cid
    for k in trig: trig[k] += int(t[k])
    ok += 1
print("ok", ok, "/", len(ids), "bytes", total, "trig", trig, "tradition", trad, "problems", problems)
