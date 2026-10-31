import json, pathlib, sys
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round65")
block=base/"judging/judgeY-block3.jsonl"
mp=json.loads((base/"judging/host-mapping.json").read_text(encoding="utf-8"))
rows=[json.loads(l) for l in block.read_text(encoding="utf-8").splitlines() if l.strip()]
start=int(sys.argv[1]); end=int(sys.argv[2])
for idx,row in enumerate(rows[start:end], start=start):
    anon=row["anon_id"]; cid=mp[anon]
    pred=json.loads((base/f"predictions/{cid}.json").read_text(encoding="utf-8"))
    # find prediction_text field
    pt=pred.get("prediction_text")
    if pt is None:
        # print keys
        print(f"### {idx} {anon} {cid} KEYS={list(pred.keys())}")
        print(json.dumps(pred, ensure_ascii=False)[:3000])
    else:
        print(f"### {idx} {anon} {cid}")
        print("OUTCOME:", row.get("outcome_record"))
        if row.get("carry_note"): print("CARRY:", row["carry_note"])
        if row.get("editor_note"): print("EDITOR:", row["editor_note"])
        print("PRED:", pt)
    print()
