#!/usr/bin/env python3
import json

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
with open(BASE + "/data/case-annotations-r77.json", encoding="utf-8") as f:
    ann = json.load(f)
for i in (10, 11, 12, 13):
    print(f"=== SC[{i}] ===")
    print(json.dumps(ann["special_checks"][i], ensure_ascii=False, indent=1))

with open(BASE + "/runs/round78/judging/outcome-manifest.json", encoding="utf-8") as f:
    man = json.load(f)
cases = man["cases"]
for cid, needle in [("BZ-036", "盲测比对须注"), ("BZ-042", "（盲测比对时以格局大富一项为主）"),
                    ("BZ-105", "使用时须分开统计"), ("LY-204", "勿以此斷")]:
    v = cases.get(cid)
    print(f"case {cid}: type={type(v).__name__} needle_present={needle in v if isinstance(v, str) else 'nonstr'}")
    if isinstance(v, str):
        idx = v.find(needle)
        print("  context:", v[max(0, idx-40):idx+len(needle)+25])

split = man.get("_r56_lr2016_split")
print("=== _r56_lr2016_split ===")
print(json.dumps(split, ensure_ascii=False, indent=1)[:2000])
raw = json.dumps(man, ensure_ascii=False)
print("editor sentence count in MAN78:", raw.count("原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。"))
print("LR2-016 in cases:", "LR2-016" in cases)
