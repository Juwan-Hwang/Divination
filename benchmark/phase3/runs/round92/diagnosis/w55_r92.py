import json, math, pathlib, statistics
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
neg = json.loads((base/"runs/round92/diagnosis/lr-negatives-dev92.json").read_text())
neg91 = json.loads((base/"runs/round91/diagnosis/lr-negatives-dev91.json").read_text())
ids = [n["case_id"] for n in neg["negatives"]]
assert len(ids) == neg["n_negative"] == 24 and neg["n_liuren_total"] == 30
for n in neg["negatives"]:
    assert abs((n["ours"]-n["master"]) - n["pair_diff"]) < 1e-9, n["case_id"]
    assert n["pair_diff"] < 0

# 本席新鲜编码（主标, W子形态, 硬核?, 含混*?, D次标?, 应期形态附记?)
COD = {
 "LR2-013": ("E", None, False, False, False, True),
 "LR2-014": ("D", None, False, False, False, False),
 "LR2-015": ("W", "面", True,  False, False, False),
 "LR2-016": ("D", None, False, False, False, False),
 "LR2-017": ("W", "面", True,  False, False, False),
 "LR2-018": ("W", "面", False, True,  False, False),
 "LR2-019": ("E", None, False, False, False, True),
 "LR2-020": ("E", None, False, False, False, False),
 "LR2-021": ("A", None, False, True,  True,  False),
 "LR2-022": ("W", "面", False, True,  False, False),
 "LR2-023": ("C", None, False, True,  False, False),
 "LR2-024": ("C", None, False, True,  False, False),
 "OC-026":  ("E", None, False, False, True,  False),
 "OC-027":  ("C", None, False, True,  False, False),
 "OC-029":  ("E", None, False, False, False, False),
 "OC-030":  ("A", None, False, False, False, True),
 "LR3-002": ("W", "面", True,  False, False, False),
 "LR3-006": ("E", None, False, False, True,  False),
 "LR3-008": ("D", None, False, False, False, False),
 "LR3-101": ("W", "面", False, True,  False, False),
 "LR3-107": ("A", None, False, False, False, False),
 "LR3-110": ("D", None, False, False, False, False),
 "LR3-112": ("H", None, False, False, False, False),
 "LR3-116": ("A", None, False, False, False, False),
}
assert set(COD) == set(ids)
seg = {n["case_id"]: n["in_dev8"] for n in neg["negatives"]}
diff = {n["case_id"]: n["pair_diff"] for n in neg["negatives"]}

def se(p, n): return math.sqrt(p*(1-p)/n)*100 if n else 0.0
def share(k, n): return f"{k}/{n}={100*k/n:.1f}% (SE {se(k/n, n):.1f}pp)"

from collections import Counter
cnt = Counter(v[0] for v in COD.values())
print("主标分布(合并 n=24):", dict(cnt), "sum", sum(cnt.values()))
for sname, sids in [("dev8", [i for i in ids if seg[i]]), ("LR3", [i for i in ids if not seg[i]])]:
    c = Counter(COD[i][0] for i in sids)
    w = [i for i in sids if COD[i][0] == "W"]; wh = [i for i in w if COD[i][2]]
    print(sname, "n=", len(sids), dict(c), "| W接口", share(len(w), len(sids)), "| W硬核", share(len(wh), len(sids)),
          "| diffsum", sum(diff[i] for i in sids), "mean", sum(diff[i] for i in sids)/len(sids),
          "median", statistics.median(diff[i] for i in sids))
w = [i for i in ids if COD[i][0] == "W"]; wh = [i for i in w if COD[i][2]]
print("合并 W接口", share(len(w), 24), "| /总例30:", share(len(w), 30))
print("合并 W硬核", share(len(wh), 24), "| /总例30:", share(len(wh), 30))
print("W子形态:", Counter(COD[i][1] for i in w))
print("含混* 例:", [i for i in ids if COD[i][3]], len([i for i in ids if COD[i][3]]))
print("D主标:", [i for i in ids if COD[i][0] == "D"])
print("D次标:", [i for i in ids if COD[i][4]])
print("应期形态附记:", [i for i in ids if COD[i][5]])
all_d = [diff[i] for i in ids]
print("合并 diff sum/mean/median:", sum(all_d), sum(all_d)/24, statistics.median(all_d))
ids91 = [n["case_id"] for n in neg91["negatives"]]
print("R91 n=", len(ids91), "进入:", sorted(set(ids)-set(ids91)), "离开:", sorted(set(ids91)-set(ids)))
print("LR3-010 in R92 list:", "LR3-010" in ids, "| in R91 list:", "LR3-010" in ids91)
