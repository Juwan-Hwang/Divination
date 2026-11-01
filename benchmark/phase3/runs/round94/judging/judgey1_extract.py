import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round94")
block=base/"judging/judgeY-block1.jsonl"
mapping=json.loads((base/"judging/host-mapping.json").read_text())
rows=[json.loads(l) for l in block.read_text().splitlines() if l.strip()]
print(f"rows {len(rows)} mapping type {type(mapping)}")
if isinstance(mapping, dict):
    # show sample keys
    print(list(mapping.items())[:3])
else:
    print(mapping[:2])
out=[]
missing=[]
for r in rows:
    anon=r.get("anon_id")
    case=mapping.get(anon) if isinstance(mapping, dict) else None
    # mapping value may be dict?
    if isinstance(case, dict):
        case=case.get("case_id") or case.get("id")
    pred_text=None
    if case:
        p=base/"predictions"/f"{case}.json"
        if p.exists():
            d=json.loads(p.read_text())
            pred_text=d.get("prediction_text")
        else:
            missing.append((anon,case,"no file"))
    else:
        missing.append((anon,case,"no mapping"))
    out.append({"anon_id":anon,"case_id":case,"prediction_text":pred_text,"outcome_record":r.get("outcome_record"),"carry_note":r.get("carry_note")})
print("missing",missing[:10])
path=base/"judging/judgey1_work.json"
path.write_text(json.dumps(out,ensure_ascii=False,indent=1))
print("written",path)
# print first 2
for o in out[:2]:
    print(json.dumps(o,ensure_ascii=False)[:2000])
