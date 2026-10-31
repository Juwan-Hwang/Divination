import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
b=json.loads((base/"runs/round77/batches.json").read_text(encoding="utf-8"))
for cid in ["LY-537","YM-070","BZ-029","BZ-040","BZ-036","BZ-042","BZ-105","LY-204","LR2-016"]:
    hits=[k for k,v in b.items() if cid in v]
    print(cid, hits)
# FREEZE seat mapping: S6 B16-18, S10 B24
# Also check r76 addendum section 2.1 suggestion extraction via text search
txt=(base/"data/manifest-carryover-r76-addendum.md").read_text(encoding="utf-8")
sug="主持裁定续接：自 R77 起承接本 R76 标注：按「卡面无 tradition/system 字段、basis 首行虚称『卡面 tradition＝bazi』（R69 型）、方法实质八字、不作废不重测」登记；结局原文照录不改。"
print("suggestion occurrences in r76 addendum:", txt.count(sug))
# judge merged entry structure for one
jm=json.loads((base/"runs/round77/judging/judgeX-merged.json").read_text(encoding="utf-8"))
k0=list(jm.keys())[0]
print("judgeX entry sample", k0, json.dumps(jm[k0], ensure_ascii=False)[:800])
# check any keys containing flag in merged entries values
flags=[]
for src in ["judgeX-merged.json","judgeY-merged.json"]:
    d=json.loads((base/f"runs/round77/judging/{src}").read_text(encoding="utf-8"))
    keys=set()
    for v in d.values():
        if isinstance(v, dict): keys.update(v.keys())
    print(src, "value keys union", sorted(keys))
