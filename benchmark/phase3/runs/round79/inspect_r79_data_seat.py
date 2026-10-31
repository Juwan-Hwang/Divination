import json, collections, pathlib, re
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
r78 = json.loads((base/"data/case-annotations-r78.json").read_text(encoding="utf-8"))
print("r78 top keys:", list(r78.keys()))
for k,v in r78.items():
    if k!="annotations":
        print(k, "=", json.dumps(v, ensure_ascii=False)[:2000])
print("annotations n=", len(r78["annotations"]))
print("dispositions:", collections.Counter(a["disposition"] for a in r78["annotations"]))
print("fields sample:", list(r78["annotations"][0].keys()))
cases78 = [a["case_id"] for a in r78["annotations"]]
print("unique cases78:", len(set(cases78)))
print("cases78:", sorted(set(cases78)))
anons78 = [a["anon_id"] for a in r78["annotations"]]
print("anons78 unique:", len(set(anons78)))

mapping = json.loads((base/"runs/round79/judging/host-mapping.json").read_text(encoding="utf-8"))
print("\nmapping type:", type(mapping))
if isinstance(mapping, dict):
    print("mapping keys sample:", list(mapping.keys())[:10])
    # print structure of first values
    for i,(k,v) in enumerate(mapping.items()):
        if i<5: print(k, "->", json.dumps(v, ensure_ascii=False)[:500])
elif isinstance(mapping, list):
    print("mapping len", len(mapping), json.dumps(mapping[:3], ensure_ascii=False)[:1000])

manifest = json.loads((base/"runs/round79/judging/outcome-manifest.json").read_text(encoding="utf-8"))
print("\nmanifest top keys:", list(manifest.keys()))
print("cases n=", len(manifest.get("cases", {})))
for k,v in manifest.items():
    if k!="cases":
        print("KEY", k, "=", json.dumps(v, ensure_ascii=False)[:800])
# sample case structure
sample_id = list(manifest["cases"].keys())[0]
print("sample case", sample_id, json.dumps(manifest["cases"][sample_id], ensure_ascii=False)[:1200])
