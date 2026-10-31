import json, pathlib, collections
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
def load(p):
    with open(p, encoding="utf-8") as f: return json.load(f)

# Task1 full comparison
r62 = load(base/"data/case-annotations-r62.json")
om = load(base/"runs/round63/judging/outcome-manifest.json")
add = om["_r63_carryover_notes_addendum"]
partial = [a for a in r62["annotations"] if a["disposition"]=="部分成立"]
pids = [a["case_id"] for a in partial]
print("partial ids == add keys set?", set(pids)==set(add.keys()), len(pids), len(add))
mismatch=[]
for a in partial:
    cid=a["case_id"]
    if add.get(cid)!=a["manifest_carry_suggestion"]:
        mismatch.append((cid, a["manifest_carry_suggestion"], add.get(cid)))
print("text mismatches:", len(mismatch))
for m in mismatch: print(m)
print("cases keys contain all partial?", all(c in om["cases"] for c in pids))

# FLAGS file line parse exploration
fp = base/"runs/round63/judging/FLAGS-selfreported-r63.md"
text = fp.read_text(encoding="utf-8")
lines = text.splitlines()
print("\nFLAGS total lines:", len(lines))
for i,l in enumerate(lines[:60]):
    print(i, repr(l)[:600])
print("...")
# count lines containing P3- ?
import re
# exploration only (not final extraction) - count occurrences
cnt = sum(1 for l in lines if "P3-" in l)
print("lines with P3-:", cnt)

hm = load(base/"runs/round63/judging/host-mapping.json")
print("\nhost-mapping type", type(hm))
if isinstance(hm, dict):
    print("keys", list(hm.keys())[:20])
    for k,v in list(hm.items())[:5]:
        print(k, "=>", json.dumps(v, ensure_ascii=False)[:800])
elif isinstance(hm, list):
    print("len", len(hm), json.dumps(hm[0], ensure_ascii=False)[:1000])
