import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round94")
block = base/"judging/judgeX-block1.jsonl"
mapping = json.loads((base/"judging/host-mapping.json").read_text(encoding="utf-8"))
# mapping structure unknown: print type in separate check - handle dict variants
rows=[]
for line in block.read_text(encoding="utf-8").splitlines():
    if not line.strip(): continue
    r=json.loads(line)
    rows.append(r)

def resolve(anon):
    if isinstance(mapping, dict):
        v=mapping.get(anon)
        if v is None:
            # maybe values are case->anon or nested
            for k,val in mapping.items():
                if val==anon:
                    return k
                if isinstance(val, dict) and val.get("anon_id")==anon:
                    return val.get("case_id", k)
            return None
        if isinstance(v, dict):
            return v.get("case_id") or v.get("case") or str(v)
        return v
    return None

out=[]
missing=[]
for r in rows:
    anon=r["anon_id"]
    cid=resolve(anon)
    ptext=None
    if cid:
        p=base/"predictions"/f"{cid}.json"
        if p.exists():
            d=json.loads(p.read_text(encoding="utf-8"))
            ptext=d.get("prediction_text")
        else:
            missing.append((anon,cid,"file_missing"))
    else:
        missing.append((anon,None,"no_mapping"))
    out.append({"anon_id":anon,"case_id":cid,"outcome_record":r.get("outcome_record"),"carry_note":r.get("carry_note"),"prediction_text":ptext})

(base/"judgex1_combined.json").write_text(json.dumps(out,ensure_ascii=False,indent=1),encoding="utf-8")
print(f"total {len(out)} missing {missing[:10]}")
print("mapping_type", type(mapping), str(mapping)[:500])
for o in out[:3]:
    print(o["anon_id"], o["case_id"], (o["prediction_text"] or "")[:200])
