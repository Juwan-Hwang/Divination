import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
man = json.loads((base/"runs/round79/judging/outcome-manifest.json").read_text(encoding="utf-8"))
cases = man["cases"]
print("cases type sample:")
for cid in ["LY-506","LR2-016","BZ-036","AS-001"]:
    v = cases.get(cid)
    print(cid, type(v).__name__, json.dumps(v, ensure_ascii=False)[:700])
print("\ntop-level layer keys and types:")
for k,v in man.items():
    if k=="cases": continue
    print(k, type(v).__name__, (len(v) if hasattr(v,'__len__') else ''))
# find layers mentioning LR2-016
print("\nLR2-016 in layers:")
for k,v in man.items():
    if isinstance(v, dict) and "LR2-016" in v:
        print(k, json.dumps(v["LR2-016"], ensure_ascii=False)[:600])
    if isinstance(v, str) and "LR2-016" in v:
        print(k, "str mentions")
# check a case entry for carry_note fields anywhere
import collections
types = collections.Counter(type(v).__name__ for v in cases.values())
print("case value types:", types)
dictcases = [c for c,v in cases.items() if isinstance(v, dict)]
print("dict cases:", dictcases[:20])
if dictcases:
    print(json.dumps(cases[dictcases[0]], ensure_ascii=False)[:800])
