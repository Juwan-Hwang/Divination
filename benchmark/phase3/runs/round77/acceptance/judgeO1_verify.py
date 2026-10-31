import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round77/acceptance")
packet = json.loads((base/"judging/packet-ours.json").read_text(encoding="utf-8"))
mapping = json.loads((base/"judging/host-mapping.json").read_text(encoding="utf-8"))["ours"]
assert len(packet)==27, len(packet)
assert set(mapping.keys())=={r["anon_id"] for r in packet}
for r in packet:
    cid = mapping[r["anon_id"]]
    pred = json.loads((base/f"predictions/{cid}.json").read_text(encoding="utf-8"))
    # find prediction_text field (top-level or nested)
    txt = pred.get("prediction_text")
    if txt is None:
        print(r["anon_id"], cid, "KEYS", list(pred.keys()))
    else:
        assert txt==r["prediction_text"], (r["anon_id"], cid, "MISMATCH")
        print(r["anon_id"], cid, "OK len", len(txt))
print("all verified")
