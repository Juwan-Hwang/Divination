import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
man=json.loads((base/"runs/round77/judging/outcome-manifest.json").read_text(encoding="utf-8"))
for cid in ["BZ-036","BZ-042","BZ-105","LY-204","LR2-016"]:
    print("==CASE",cid,"==")
    print(json.dumps(man["cases"].get(cid), ensure_ascii=False)[:3000])
    print("stripped_tail:", json.dumps(man.get("stripped_tail",{}).get(cid), ensure_ascii=False)[:1000])
print("==LR2 split==")
print(json.dumps(man.get("_r56_lr2016_split"), ensure_ascii=False, indent=1))
print("==_r77 note tail==")
print(man.get("_r77_manifest_note"))
# host mapping
hm=json.loads((base/"runs/round77/judging/host-mapping.json").read_text(encoding="utf-8"))
print("\nhost-mapping type", type(hm))
if isinstance(hm, dict):
    print("keys sample", list(hm.keys())[:20])
    # find LR2-016
    for k,v in hm.items():
        if "LR2-016" in json.dumps(v, ensure_ascii=False) or k=="LR2-016":
            print("HM",k, json.dumps(v, ensure_ascii=False)[:2000])
    # also dump structure of one value
    first=list(hm.items())[0]
    print("first entry", first[0], json.dumps(first[1], ensure_ascii=False)[:1000])
elif isinstance(hm, list):
    for e in hm:
        if "LR2-016" in json.dumps(e, ensure_ascii=False):
            print("HM entry", json.dumps(e, ensure_ascii=False)[:2000])
# predictions LY-537, YM-070, BZ-029, BZ-040
for cid in ["LY-537","YM-070","BZ-029","BZ-040"]:
    p=base/f"runs/round77/predictions/{cid}.json"
    d=json.loads(p.read_text(encoding="utf-8"))
    print(f"\n==PRED {cid} keys {list(d.keys())}")
    print(json.dumps(d, ensure_ascii=False)[:2500])
# r76 annotations for LY-537, YM-070
r76=json.loads((base/"data/case-annotations-r76.json").read_text(encoding="utf-8"))
for a in r76["annotations"]:
    if a["case_id"] in ("LY-537","YM-070"):
        print("\n==R76 ANN",a["case_id"], json.dumps(a, ensure_ascii=False)[:2500])
