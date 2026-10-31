import json, pathlib, collections
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
def load(p): return json.loads((base/p).read_text(encoding="utf-8"))
r78 = load("data/case-annotations-r78.json")
r75 = load("data/case-annotations-r75.json")
r74 = load("data/case-annotations-r74.json")
by78={a["case_id"]:a for a in r78["annotations"]}
mapping = load("runs/round79/judging/host-mapping.json")
import re
text=(base/"runs/round79/judge-flags-r79-host-compiled.md").read_text(encoding="utf-8")
anons=sorted(set(re.findall(r"P3-[0-9a-f]{8}", text)))
flag_cases=[mapping[a] for a in anons]
print("flag cases unique", len(set(flag_cases)))
overlap=[c for c in flag_cases if c in by78]
new=[c for c in flag_cases if c not in by78]
print("overlap n", len(overlap), sorted(overlap))
print("new n", len(new), sorted(new))
for c in sorted(overlap):
    a=by78[c]
    print(f"OVERLAP {c} anon78={a['anon_id']} disp={a['disposition']} reg={a['registered_round']} flag_anons={[an for an in anons if mapping[an]==c]}")
for c in sorted(new):
    print(f"NEW {c} flag_anons={[an for an in anons if mapping[an]==c]}")
# check anon identity: for overlap cases, is flag anon same as anon78?
print("\nanon match check:")
for c in sorted(overlap):
    print(c, by78[c]["anon_id"], "flag:", [an for an in anons if mapping[an]==c], "same?", by78[c]["anon_id"] in [an for an in anons if mapping[an]==c])
# r74->r75 transformation for a touched case
by75={a["case_id"]:a for a in r75["annotations"]}
by74={a["case_id"]:a for a in r74["annotations"]}
print("\nr75 counts", r75["counts"])
print("r74 counts", r74["counts"])
# find cases in r75 not in r74
print("in r75 not r74:", [c for c in by75 if c not in by74])
# find cases whose entry changed r74->r75
changed=[c for c in by75 if c in by74 and by75[c]!=by74[c]]
print("changed n", len(changed), changed[:10])
if changed:
    c=changed[0]
    print("EXAMPLE CHANGED", c)
    for k in by74[c]:
        if by74[c][k]!=by75[c][k]:
            print(" FIELD", k)
            print("  OLD:", json.dumps(by74[c][k], ensure_ascii=False)[:600])
            print("  NEW:", json.dumps(by75[c][k], ensure_ascii=False)[:900])
