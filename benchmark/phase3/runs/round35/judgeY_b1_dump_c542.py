import json, pathlib
base = pathlib.Path(__file__).parent
packet = json.loads((base/"judging"/"packet1.json").read_text(encoding="utf-8"))
mapping = json.loads((base/"judging"/"host-mapping.json").read_text(encoding="utf-8"))
anons = [x["anon_id"] for x in packet]
print("packet count:", len(anons), "unique:", len(set(anons)))
missing = [a for a in anons if a not in mapping]
print("missing in mapping:", missing)
print("all in mapping:", len(missing)==0)
out = []
for i, item in enumerate(packet, 1):
    anon = item["anon_id"]
    cid = mapping[anon]
    pred_path = base/"predictions"/f"{cid}.json"
    if not pred_path.exists():
        print(f"MISSING PRED {anon} {cid}")
        ptext = "<MISSING FILE>"
        extra = {}
    else:
        pj = json.loads(pred_path.read_text(encoding="utf-8"))
        ptext = pj.get("prediction_text", "<NO prediction_text KEY: "+",".join(pj.keys())+">")
        extra = {k: pj[k] for k in pj if k!="prediction_text"}
    out.append(f"\n===== #{i} anon={anon} case={cid} =====\nOUTCOME: {item.get('outcome_record')}\nEXTRA_KEYS: {json.dumps(extra, ensure_ascii=False)[:800]}\nPREDICTION_TEXT:\n{ptext}\n")
dest = base/"judgeY_b1_work_c542.txt"
dest.write_text("\n".join(out), encoding="utf-8")
print("wrote", dest, "chars", dest.stat().st_size)
