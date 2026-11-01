import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round94/judging")
data=json.loads((base/"judgey1_work.json").read_text())
for idx,o in enumerate(data):
    print(f"=== {idx+1} {o['anon_id']} {o['case_id']} ===")
    print("PRED:", o['prediction_text'])
    print("OUTCOME:", o['outcome_record'])
    print()
