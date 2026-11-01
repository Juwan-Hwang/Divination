import json, os
D = "/home/hatch/workspace/divination/benchmark/phase3/runs/round94/predictions"
ids = ["MH-007", "MH-008", "MH-009", "MH-010"] + ["MP-%03d" % i for i in range(1, 17)]
MARK = ""
for c in ids:
p = os.path.join(D, c + ".json")
d = json.load(open(p, encoding="utf-8"))
if MARK not in d["basis"]:
d["basis"] = d["basis"].replace("量级类断项", MARK + "量级类断项", 1)
with open(p, "w", encoding="utf-8") as f:
json.dump(d, f, ensure_ascii=False, indent=1)
print("patched", c)
print("done")
