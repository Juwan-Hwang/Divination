import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round91")
mapping = json.loads((base/"judging/host-mapping.json").read_text())
rows=[]
with open(base/"judging/judgeX-block2.jsonl") as f:
    for line in f:
        line=line.strip()
        if line: rows.append(json.loads(line))
print(f"total {len(rows)}")
for idx, r in enumerate(rows):
    anon=r["anon_id"]; case=mapping.get(anon,"?")
    pred=json.loads((base/"predictions"/f"{case}.json").read_text())
    ptext=pred.get("prediction_text","")
    out=r.get("outcome_record","")
    carry=(r.get("carry_note") or "")[:900]
    editor=(r.get("editor_note") or "")
    chunk=idx//31
    with open(base/f"judgeX2-view-{chunk}.txt","a") as o:
        o.write(f"\n===== #{idx+1} {anon} case={case} =====\nPRED: {ptext}\nOUTCOME: {out}\n")
        if carry: o.write(f"CARRY(first900): {carry}\n")
        if editor: o.write(f"EDITOR: {editor}\n")
print("done")
