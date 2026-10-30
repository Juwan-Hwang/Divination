import json, pathlib
base = pathlib.Path(__file__).parent
block = base/"judging"/"judgeX-block1.jsonl"
mapping = json.loads((base/"judging"/"host-mapping.json").read_text(encoding="utf-8"))
rows=[]
for line in block.read_text(encoding="utf-8").splitlines():
    if line.strip():
        rows.append(json.loads(line))
print(f"COUNT {len(rows)}")
out=[]
for r in rows:
    anon=r["anon_id"]
    cid=mapping.get(anon)
    pfile=base/"predictions"/f"{cid}.json"
    try:
        pdata=json.loads(pfile.read_text(encoding="utf-8"))
        ptext=pdata.get("prediction_text","")
        # also include other keys if prediction_text missing
        extra={k:v for k,v in pdata.items() if k!="prediction_text"}
    except Exception as e:
        ptext=f"<ERR {e}>"
        extra={}
    out.append(f"\n=== {anon} | {cid} ===\nOUTCOME: {r['outcome_record']}\nEXTRA: {json.dumps(extra, ensure_ascii=False)}\nPREDICTION_TEXT:\n{ptext}\n")
(base/"r54-judgeX-block1-dump.txt").write_text("\n".join(out), encoding="utf-8")
print("written")
