import json, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round58"
with open(f"{BASE}/judging/host-mapping.json", encoding="utf-8") as f:
    mapping = json.load(f)

rows = []
with open(f"{BASE}/judging/judgeY-block4.jsonl", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            rows.append(json.loads(line))

out = []
missing = []
for r in rows:
    anon = r["anon_id"]
    case = mapping.get(anon)
    if case is None:
        missing.append((anon, "no-mapping"))
        continue
    ppath = f"{BASE}/predictions/{case}.json"
    if not os.path.exists(ppath):
        missing.append((anon, case))
        continue
    with open(ppath, encoding="utf-8") as f:
        pj = json.load(f)
    out.append({
        "anon_id": anon,
        "case_id": case,
        "prediction_text": pj.get("prediction_text"),
        "outcome_record": r.get("outcome_record"),
        "carry_note": r.get("carry_note"),
        "editor_note": r.get("editor_note"),
    })

with open(f"{BASE}/judgeY-block4-merged.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("merged:", len(out), "missing:", missing)
