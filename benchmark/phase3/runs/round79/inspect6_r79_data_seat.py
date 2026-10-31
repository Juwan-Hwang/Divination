import json, pathlib, re
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
man = json.loads((base/"runs/round79/judging/outcome-manifest.json").read_text(encoding="utf-8"))
# search string across cases
for cid, txt in man["cases"].items():
    if "还一半" in txt or "還一半" in txt: print("还一半 in case:", cid, txt[:200])
for layer, v in man.items():
    if isinstance(v, dict):
        for cid, txt in v.items():
            if isinstance(txt, str) and ("还一半" in txt or "還一半" in txt): print("还一半 in layer:", layer, cid, txt[:200])
# YM-015 card full
card = json.loads((base/"inputs-dev12/YM-015.json").read_text(encoding="utf-8"))
print("\nYM-015 card:", json.dumps(card, ensure_ascii=False)[:1500])
pred = json.loads((base/"runs/round79/predictions/YM-015.json").read_text(encoding="utf-8"))
print("\nYM-015 pred:", json.dumps(pred, ensure_ascii=False)[:800])
# LR2-023 prediction check
pred2 = json.loads((base/"runs/round79/predictions/LR2-023.json").read_text(encoding="utf-8"))
t2 = json.dumps(pred2, ensure_ascii=False)
print("\nLR2-023 pred has 儿妇:", "兒婦" in t2 or "儿妇" in t2, "| 妊:", "妊" in t2, "| 性别:", "性别" in t2 or "性別" in t2)
print("LR2-023 pred:", t2[:700])
# BZ-304 prediction check
pred3 = json.loads((base/"runs/round79/predictions/BZ-304.json").read_text(encoding="utf-8"))
t3 = json.dumps(pred3, ensure_ascii=False)
print("\nBZ-304 pred has 恢复正常:", "恢复正常" in t3, "| pred:", t3[:500])
# LY-613 prediction ? check
pred4 = json.loads((base/"runs/round79/predictions/LY-613.json").read_text(encoding="utf-8"))
t4 = json.dumps(pred4, ensure_ascii=False)
print("\nLY-613 pred '?' count:", t4.count("?"), " '？' count:", t4.count("？"))
# LY-322 substantive layers
print("\nLY-322 all layers:")
for layer, v in man.items():
    if isinstance(v, dict) and "LY-322" in v: print(" ", layer, str(v["LY-322"])[:300])
print("\nLY-322 card notes/context:")
c322 = json.loads((base/"inputs-dev12/LY-322.json").read_text(encoding="utf-8"))
print(json.dumps(c322, ensure_ascii=False)[:1500])
# history of 24 new cases in earlier annotation files
new_cases = ['AS-209','AS-215','AS-304','BQ-021','BZ-104','LR2-016','LR3-002','LY-011','LY-255','LY-322','LY-329','LY-408','LY-411','LY-413','LY-428','LY-434','LY-440','LY-514','LY-523','LY-525','LY-538','LY-620','LY-623','YM-015']
hist = {}
for r in range(49,79):
    p = base/f"data/case-annotations-r{r}.json"
    if not p.exists(): continue
    d = json.loads(p.read_text(encoding="utf-8"))
    for a in d["annotations"]:
        if a["case_id"] in new_cases:
            hist.setdefault(a["case_id"], []).append((r, a.get("disposition"), str(a.get("flag",""))[:80]))
for c in new_cases:
    h = hist.get(c, [])
    print(f"\nHIST {c}: rounds {[x[0] for x in h]}")
    if h: print("  last:", h[-1][0], h[-1][1], "| flag:", h[-1][2])
