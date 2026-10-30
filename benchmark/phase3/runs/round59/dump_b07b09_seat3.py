import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12")
ids=["LY-009","LY-01","LY-010","LY-011","LY-012","LY-013","LY-014","LY-015","LY-016","LY-017","LY-018","LY-019","LY-021","LY-022","LY-023","LY-024","LY-025","LY-026","LY-027","LY-028","LY-029","LY-030","LY-031","LY-032","LY-033","LY-034","LY-035","LY-036","LY-102","LY-103","LY-104","LY-105","LY-202","LY-203","LY-204","LY-205","LY-206","LY-207","LY-208","LY-210","LY-211","LY-212","LY-215","LY-216","LY-217","LY-218","LY-219","LY-220","LY-221","LY-222","LY-227","LY-228","LY-230","LY-231","LY-232","LY-234","LY-235","LY-237","LY-240","LY-241"]
for cid in ids:
    p=base/f"{cid}.json"
    try:
        d=json.loads(p.read_text())
    except Exception as e:
        print(cid, "ERR", e); continue
    print("="*80)
    print(json.dumps(d, ensure_ascii=False, indent=1))
