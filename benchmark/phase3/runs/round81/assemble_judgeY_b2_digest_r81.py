import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round81")
rows = [json.loads(l) for l in open(base/"judging/judgeY-block2.jsonl", encoding="utf-8") if l.strip()]
mapping = json.load(open(base/"judging/host-mapping.json", encoding="utf-8"))
print("rows", len(rows))
chunk = 16
for ci in range(0, len(rows), chunk):
    part = rows[ci:ci+chunk]
    out = []
    for i, r in enumerate(part, start=ci+1):
        anon = r["anon_id"]; case = mapping[anon]
        pred = json.load(open(base/"predictions"/f"{case}.json", encoding="utf-8"))
        ptext = pred.get("prediction_text") or pred.get("prediction") or ""
        if not isinstance(ptext, str):
            ptext = json.dumps(ptext, ensure_ascii=False)
        out.append(f"===== #{i} {anon} -> {case} =====\n[预测原文]\n{ptext}\n[结局]\n{r.get('outcome_record','')}\n[carry_note存在: {bool(r.get('carry_note'))} editor_note存在: {bool(r.get('editor_note'))}]\n")
    p = base/f"judgeY_b2_digest_{ci//chunk+1:02d}.txt"
    p.write_text("\n".join(out), encoding="utf-8")
    print(p.name, len(part))
