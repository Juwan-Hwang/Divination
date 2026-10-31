import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
def load(p):
    with open(p, encoding="utf-8") as f: return json.load(f)
r62 = load(base/"data/case-annotations-r62.json")
f0 = r62["flags"][0]; a0 = [a for a in r62["annotations"] if a["anon_id"]==f0["anon_id"]][0]
print("flags basis == ann finding?", f0["basis"]==a0["finding"])
print("flags flag == ann flag?", f0["flag"]==a0["flag"])
print("flags carry == manifest_carry?", f0["carry_suggestion"]==f0["manifest_carry_suggestion"]==a0["manifest_carry_suggestion"])
print("flags relation == ann relation?", f0["relation"]==a0["relation"])
print("flags views:", f0["views"], "ann source_seats:", a0["source_seats"])
print("flags category:", f0["category"])
# check across all
diff=0
for f in r62["flags"]:
    a=[x for x in r62["annotations"] if x["anon_id"]==f["anon_id"]][0]
    if f["basis"]!=a["finding"] or f["flag"]!=a["flag"] or f["manifest_carry_suggestion"]!=a["manifest_carry_suggestion"] or f["relation"]!=a["relation"] or f["sources_checked"]!=a["sources_checked"]:
        diff+=1; print("DIFF", f["case_id"])
print("diff count", diff)
cats={}
for f in r62["flags"]: cats[f["category"]]=cats.get(f["category"],0)+1
print("categories:", cats)
rels={}
for a in r62["annotations"]: rels[a["relation"].split("（")[0]]=rels.get(a["relation"].split("（")[0],0)+1
print("relation prefixes:", rels)
# how are new vs continuation distinguished in counts? continuation 75, same_case_new 1, new 6 = 82
# print relations full for non-continuation
for a in r62["annotations"]:
    if "续接" not in a["relation"]:
        print(a["case_id"], a["relation"], "| cat:", [f["category"] for f in r62["flags"] if f["anon_id"]==a["anon_id"]])
