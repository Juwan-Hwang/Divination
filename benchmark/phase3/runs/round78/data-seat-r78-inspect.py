#!/usr/bin/env python3
# R78 data seat inspection: structured reads only, named paths only.
import json, hashlib, collections

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
ANN77 = BASE + "/data/case-annotations-r77.json"
MAN78 = BASE + "/runs/round78/judging/outcome-manifest.json"
MAN77 = BASE + "/runs/round77/judging/outcome-manifest.json"

with open(ANN77, encoding="utf-8") as f:
    ann = json.load(f)
print("ANN keys:", list(ann.keys()))
print("ANN round:", ann.get("round"))
print("ANN counts:", json.dumps(ann.get("counts"), ensure_ascii=False))
print("ANN n annotations:", len(ann["annotations"]))
print("ANN verdict dist:", collections.Counter(a["disposition"] for a in ann["annotations"]))
ids = [a["case_id"] for a in ann["annotations"]]
print("ANN unique case_ids:", len(set(ids)))
sc = ann.get("special_checks")
print("ANN special_checks type:", type(sc).__name__, "len:", len(sc) if sc else 0)
if isinstance(sc, list):
    for i, item in enumerate(sc):
        s = json.dumps(item, ensure_ascii=False)
        print(f"SC[{i}] len={len(s)} head={s[:160]}")
print("ANN other keys detail:")
for k, v in ann.items():
    if k not in ("annotations", "special_checks", "_provenance", "counts"):
        print(" ", k, "=", json.dumps(v, ensure_ascii=False)[:300])

with open(MAN78, encoding="utf-8") as f:
    man = json.load(f)
print("\nMAN78 top keys:", list(man.keys()))
note = man.get("_r78_manifest_note")
print("MAN78 _r78_manifest_note:", json.dumps(note, ensure_ascii=False))
cases = man["cases"]
print("MAN78 cases type:", type(cases).__name__, "n:", len(cases))

# structured SHA candidates for cases
target = "00f362bd8e4b55ceff31502cb5f7e8239855b1f806a7b1495284af80186a31ad"
cands = {
    "dumps(sort_keys,ensure_ascii=False,sep)": json.dumps(cases, sort_keys=True, ensure_ascii=False, separators=(",", ":")),
    "dumps(sort_keys,ensure_ascii=True,sep)": json.dumps(cases, sort_keys=True, ensure_ascii=True, separators=(",", ":")),
    "dumps(sort_keys,ensure_ascii=False,default)": json.dumps(cases, sort_keys=True, ensure_ascii=False),
    "dumps(ensure_ascii=False,sep,nosort)": json.dumps(cases, ensure_ascii=False, separators=(",", ":")),
}
for name, s in cands.items():
    h = hashlib.sha256(s.encode("utf-8")).hexdigest()
    print(f"SHA cand {name}: {h} match={h==target}")

with open(MAN77, encoding="utf-8") as f:
    man77 = json.load(f)
print("cases equal r77 vs r78:", man77["cases"] == cases)

# six-place check on MAN78
def find_case(cid):
    if isinstance(cases, dict):
        return cases.get(cid)
    for c in cases:
        if c.get("case_id") == cid:
            return c
    return None

for cid, needle in [("BZ-036", "盲测比对须注"), ("BZ-042", "（盲测比对时以格局大富一项为主）"),
                    ("BZ-105", "使用时须分开统计"), ("LY-204", "勿以此斷")]:
    c = find_case(cid)
    s = json.dumps(c, ensure_ascii=False) if c is not None else ""
    print(f"case {cid}: present={needle in s}")
    if c is not None:
        print(f"  case keys: {list(c.keys())}")

# LR2-016 editor_note in manifest layers
raw = json.dumps(man, ensure_ascii=False)
print("editor_note phrase count in MAN78 json:", raw.count("评分时该细项请按未完全复核处理"))
print("full editor sentence count:", raw.count("原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。"))
split = man.get("_r56_lr2016_split")
print("_r56_lr2016_split:", json.dumps(split, ensure_ascii=False)[:800])
# search all top-level keys for LR2-016 editor_note
for k, v in man.items():
    sv = json.dumps(v, ensure_ascii=False)
    if "editor_note" in sv:
        print(f"top key with editor_note: {k}")
