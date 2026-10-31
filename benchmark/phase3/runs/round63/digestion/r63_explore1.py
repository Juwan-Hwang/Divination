import json, pathlib, collections
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
def load(p):
    with open(p, encoding="utf-8") as f: return json.load(f)

r62 = load(base/"data/case-annotations-r62.json")
print("R62 top keys:", list(r62.keys()))
for k,v in r62.items():
    if isinstance(v, list): print(k, "list len", len(v))
    elif isinstance(v, dict): print(k, "dict keys", list(v.keys()))
    else: print(k, repr(v)[:500])
print("\ncounts:", json.dumps(r62.get("counts"), ensure_ascii=False, indent=1)[:3000])
print("\n_provenance:", json.dumps(r62.get("_provenance"), ensure_ascii=False, indent=1)[:4000])
print("\nflags field sample:", json.dumps(r62.get("flags"), ensure_ascii=False)[:2000])
print("\nspecial_checks:", json.dumps(r62.get("special_checks"), ensure_ascii=False, indent=1)[:6000])
ann = r62["annotations"]
print("\nannotation keys union:", sorted({k for a in ann for k in a.keys()}))
for a in ann[:2]:
    print("\nANN sample:", json.dumps(a, ensure_ascii=False, indent=1)[:4000])
# verdict recompute
c = collections.Counter(a["disposition"] for a in ann)
print("\nrecomputed verdicts:", dict(c), "total", len(ann))
print("counts.verdicts:", r62["counts"].get("verdicts"))
partial = [a for a in ann if a["disposition"]=="部分成立"]
print("partial count", len(partial), "all carry non-empty?", all((a.get("manifest_carry_suggestion") or "").strip() for a in partial))
print("partial ids:", [a["case_id"] for a in partial])
for disp in ["成立","不成立","未核"]:
    print(disp, [a["case_id"] for a in ann if a["disposition"]==disp])

om = load(base/"runs/round63/judging/outcome-manifest.json")
print("\n\nOUTCOME top keys:", list(om.keys()))
for k,v in om.items():
    if isinstance(v, dict): print(k, "dict len", len(v), "sample keys", list(v.keys())[:10])
    elif isinstance(v, list): print(k, "list len", len(v))
    else: print(k, repr(v)[:300])
add = om.get("_r63_carryover_notes_addendum")
print("\naddendum type", type(add))
if isinstance(add, dict):
    print("addendum len", len(add))
    for i,(k,v) in enumerate(add.items()):
        print(k, "=>", repr(v)[:400])
        if i>=4: break
cases = om.get("cases")
if isinstance(cases, dict):
    print("\ncases len", len(cases), "sample key", list(cases.keys())[:5])
    sk = list(cases.keys())[0]
    print("case payload type", type(cases[sk]), json.dumps(cases[sk], ensure_ascii=False)[:2000] if not isinstance(cases[sk], str) else cases[sk][:1000])
elif isinstance(cases, list):
    print("\ncases list len", len(cases), json.dumps(cases[0], ensure_ascii=False)[:2000])
