import json, sys
base="benchmark/phase3/runs/round42"
# paths relative to workspace root? exec workdir is ~, so use ~/workspace/divination/...
import os
root=os.path.expanduser("~/workspace/divination")
judge_path=os.path.join(root, base, "judging/judgeX-block1.jsonl")
map_path=os.path.join(root, base, "judging/host-mapping.json")
rows=[json.loads(l) for l in open(judge_path, encoding="utf-8") if l.strip()]
mapping=json.load(open(map_path, encoding="utf-8"))
# mapping format unknown: print type in first call if needed
start=int(sys.argv[1]) if len(sys.argv)>1 else 0
end=int(sys.argv[2]) if len(sys.argv)>2 else len(rows)
print(f"TOTAL {len(rows)} mapping_type={type(mapping)}")
if isinstance(mapping, dict):
    # show sample keys
    print("MAP_SAMPLE", list(mapping.items())[:2])
for i in range(start, min(end, len(rows))):
    anon=rows[i]["anon_id"]
    outcome=rows[i]["outcome_record"]
    case_id=None
    if isinstance(mapping, dict):
        v=mapping.get(anon)
        if isinstance(v, dict):
            case_id=v.get("case_id") or v.get("case") or str(v)
        else:
            case_id=v
    elif isinstance(mapping, list):
        for e in mapping:
            if e.get("anon_id")==anon:
                case_id=e.get("case_id"); break
    pred_path=os.path.join(root, base, "predictions", f"{case_id}.json")
    try:
        pred=json.load(open(pred_path, encoding="utf-8"))
        ptext=pred.get("prediction_text") or pred.get("prediction") or str(pred)
    except Exception as e:
        ptext=f"<ERR {e} case={case_id}>"
    print(f"\n=== {i} {anon} case={case_id} ===")
    print("OUTCOME:", outcome)
    print("PRED:", ptext)
