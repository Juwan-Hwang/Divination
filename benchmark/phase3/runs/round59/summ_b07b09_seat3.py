import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12")
ids=["LY-009","LY-01","LY-010","LY-011","LY-012","LY-013","LY-014","LY-015","LY-016","LY-017","LY-018","LY-019","LY-021","LY-022","LY-023","LY-024","LY-025","LY-026","LY-027","LY-028","LY-029","LY-030","LY-031","LY-032","LY-033","LY-034","LY-035","LY-036","LY-102","LY-103","LY-104","LY-105","LY-202","LY-203","LY-204","LY-205","LY-206","LY-207","LY-208","LY-210","LY-211","LY-212","LY-215","LY-216","LY-217","LY-218","LY-219","LY-220","LY-221","LY-222","LY-227","LY-228","LY-230","LY-231","LY-232","LY-234","LY-235","LY-237","LY-240","LY-241"]
for cid in ids:
    d=json.loads((base/f"{cid}.json").read_text())
    ctx=d.get("context",{})
    att=ctx.get("attachments",{})
    trad=d.get("tradition") or d.get("system") or "?"
    print(f"{cid} | trad={trad} | Q={ctx.get('question')} | at={ctx.get('asked_at')} | set={ctx.get('setting','')}")
    print(f"  hex={att.get('hexagram','')} | mov={att.get('moving_lines','')}")
    lines=att.get('chart_lines_top_to_bottom') or att.get('lines_top_to_bottom') or []
    for L in lines: print("   ",L)
    for k in ("hidden_lines","空亡","date_ganzhi"):
        if k in att: print(f"  {k}={att[k]}")
    if d.get("notes",{}).get("completion_grade"): print("  [has completion notes]")
