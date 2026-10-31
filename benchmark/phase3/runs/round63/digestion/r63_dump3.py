import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
recs=json.loads((base/"runs/round63/digestion/r63_flagdump.json").read_text(encoding="utf-8"))
start=int(__import__("sys").argv[1]); end=int(__import__("sys").argv[2])
for rec in recs[start:end]:
    print("="*80)
    print(rec["case_id"], rec["anon"], "seats", rec["seats"])
    for f in rec["flags_r63"]: print(" R63旗:", f)
    lp=rec["latest_prior"]
    if lp:
        print(f" 最近定案 R{lp['round']} {lp['disposition']} rel={lp['relation']}")
        print(" 旧旗:", (lp["flag"] or "")[:500])
        print(" 旧finding:", (lp["finding"] or "")[:600])
    else:
        print(" 无历轮定案（新立候选）")
    print(" R63结局:", (rec["outcome_r63"] or "")[:400])
