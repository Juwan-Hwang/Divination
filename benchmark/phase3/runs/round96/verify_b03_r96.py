# -*- coding: utf-8 -*-
import json, os
ids = ["BQ-017","BQ-018","BQ-019","BQ-020","BQ-021","BQ-022","BQ-023","BQ-024","BQ-025","BZ-016","BZ-019","BZ-020","BZ-021","BZ-022","BZ-023","BZ-024","BZ-025","BZ-026","BZ-027","BZ-028"]
BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round96/predictions"
total = 0; ok = 0; cm = ru = di = 0; problems = []
for cid in ids:
    p = os.path.join(BASE, cid + ".json")
    try:
        raw = open(p, "rb").read(); total += len(raw)
        d = json.loads(raw.decode("utf-8"))
        assert d["case_id"] == cid, "case_id mismatch"
        for k in ["prediction_text","basis","confidence","trigger"]:
            assert k in d, "missing "+k
        assert isinstance(d["confidence"], (int,float)) and 0 <= d["confidence"] <= 1
        t = d["trigger"]
        for k in ["changed_main","reserve_used","disputed","reason"]:
            assert k in t, "trigger missing "+k
        assert "第八节" in d["basis"] and "功量核" in d["basis"], "no sec8"
        assert "主线认定：" in d["basis"], "no mainline"
        assert "systems_used:" in d["basis"], "no systems_used"
        if cid.startswith("BQ-"):
            assert t["reason"] != "", "liuyao reason empty"
            cm += bool(t["changed_main"]); ru += bool(t["reserve_used"]); di += bool(t["disputed"])
        else:
            assert t["changed_main"] is False and t["reserve_used"] is False and t["disputed"] is False and t["reason"] == "", "bazi trigger shape"
        ok += 1
    except Exception as e:
        problems.append(cid + ": " + str(e))
print("ok", ok, "total_bytes", total, "liuyao_trigger_counts", cm, ru, di)
print("problems", problems)
