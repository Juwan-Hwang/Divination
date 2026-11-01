import json, os
base = "/home/hatch/workspace/divination/benchmark/phase3/runs/round94"
with open(os.path.join(base, "judging/host-mapping.json")) as f:
    mapping = json.load(f)
rows = []
with open(os.path.join(base, "judging/judgeY-block3.jsonl")) as f:
    for line in f:
        line = line.strip()
        if line:
            rows.append(json.loads(line))
out = []
missing = []
for i, r in enumerate(rows):
    anon = r["anon_id"]
    cid = mapping.get(anon)
    ptext = None
    if cid:
        ppath = os.path.join(base, "predictions", cid + ".json")
        if os.path.exists(ppath):
            with open(ppath) as f:
                pdata = json.load(f)
            ptext = pdata.get("prediction_text")
        else:
            missing.append((anon, "file_missing:" + str(cid)))
    else:
        missing.append((anon, "no_mapping"))
    if not ptext:
        missing.append((anon, "empty_prediction"))
    out.append({"idx": i, "anon_id": anon, "case_id": cid,
                "prediction_text": ptext, "outcome_record": r.get("outcome_record")})
with open(os.path.join(base, "judging/judgey3-review.jsonl"), "w") as f:
    for o in out:
        f.write(json.dumps(o, ensure_ascii=False) + "\n")
print("rows", len(out))
print("missing", missing)
lens = [len(o["prediction_text"] or "") for o in out]
print("pred_len min/max", min(lens), max(lens))
olens = [len(o["outcome_record"] or "") for o in out]
print("outcome_len min/max", min(olens), max(olens))
