import json, sys
base="/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12/"
for cid in sys.argv[1:]:
    with open(base+cid+".json",encoding="utf-8") as f:
        d=json.load(f)
    out={k:v for k,v in d.items() if k not in ("notes","provenance")}
    print("="*15, cid)
    print(json.dumps(out, ensure_ascii=False))
    n=d.get("notes",{})
    cg=n.get("completion_grade",{}) if isinstance(n,dict) else {}
    if cg:
        print("COMPLETION_FLAGS:", json.dumps({k:v.get("grade") for k,v in cg.get("fields",{}).items()}, ensure_ascii=False))
    if isinstance(n,dict) and n.get("input_flags"):
        print("INPUT_FLAGS:", json.dumps(n["input_flags"], ensure_ascii=False))
