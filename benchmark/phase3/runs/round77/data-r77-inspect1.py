import json, pathlib, collections, re
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
r76=json.loads((base/"data/case-annotations-r76.json").read_text(encoding="utf-8"))
print("r76 top keys:", list(r76.keys()))
for k,v in r76.items():
    if k=="annotations":
        print("annotations len", len(v))
        print("dispositions", collections.Counter(a.get("disposition") for a in v))
        # last 8
        for a in v[-8:]:
            print("ANN", a.get("case_id"), a.get("anon_id"), a.get("disposition"), a.get("registered_round"), repr(a.get("manifest_carry_suggestion"))[:300])
    elif k=="_provenance":
        print("_provenance len", len(v))
    else:
        print(k, json.dumps(v, ensure_ascii=False)[:4000])
print("--- special_checks raw ---")
print(json.dumps(r76.get("special_checks"), ensure_ascii=False, indent=1)[:8000])
print("--- counts raw ---")
print(json.dumps(r76.get("counts"), ensure_ascii=False, indent=1)[:8000])

man=json.loads((base/"runs/round77/judging/outcome-manifest.json").read_text(encoding="utf-8"))
print("\nMANIFEST top keys:", list(man.keys()))
for k,v in man.items():
    if isinstance(v, dict):
        print(k, "dict len", len(v), "sample keys", list(v.keys())[:10])
    elif isinstance(v, list):
        print(k, "list len", len(v))
    else:
        print(k, repr(v)[:500])
add=man.get("_r77_carryover_notes_addendum")
print("\n_r77 type", type(add))
print(json.dumps(add, ensure_ascii=False, indent=1)[:8000])
