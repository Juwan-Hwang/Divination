import json, math, pathlib, statistics
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
neg = json.loads((base/"runs/round93/diagnosis/lr-negatives-dev93.json").read_text())
neg92 = json.loads((base/"runs/round92/diagnosis/lr-negatives-dev92.json").read_text())
ids = [n["case_id"] for n in neg["negatives"]]
assert len(ids) == neg["n_negative"] == 23 and neg["n_liuren_total"] == 30
for n in neg["negatives"]:
    assert abs((n["ours"]-n["master"]) - n["pair_diff"]) < 1e-9, n["case_id"]
    assert n["pair_diff"] < 0

# 编码来源登记（双轨）：
# 轨一 承 W55（R92 DIAG §2）主标登记的本轮在册例 20 例——本席本轮无逐例许可，
#   只承登记、不作新鲜编码；硬核操作限定照 W55 卷首（套式行不单独构成硬核据）。
# 轨二 LR3-004／LR3-104／LR3-114 三例本轮新进入、无任何既往标定且本轮不可编码，
#   登记 UNC（未标定），不入已编码分母、不以相邻轮材料补位。
# 字段：(主标, W子形态, 硬核?, 含混*?, D次标?, 应期形态附记?)
CARRY = {
 "LR2-013": ("E", None, False, False, False, True),
 "LR2-014": ("D", None, False, False, False, False),
 "LR2-015": ("W", "面", True,  False, False, False),
 "LR2-016": ("D", None, False, False, False, False),
 "LR2-017": ("W", "面", True,  False, False, False),
 "LR2-019": ("E", None, False, False, False, True),
 "LR2-021": ("A", None, False, True,  True,  False),
 "LR2-022": ("W", "面", False, True,  False, False),
 "LR2-023": ("C", None, False, True,  False, False),
 "LR2-024": ("C", None, False, True,  False, False),
 "OC-026":  ("E", None, False, False, True,  False),
 "OC-027":  ("C", None, False, True,  False, False),
 "OC-030":  ("A", None, False, False, False, True),
 "LR3-002": ("W", "面", True,  False, False, False),
 "LR3-006": ("E", None, False, False, True,  False),
 "LR3-101": ("W", "面", False, True,  False, False),
 "LR3-107": ("A", None, False, False, False, False),
 "LR3-110": ("D", None, False, False, False, False),
 "LR3-112": ("H", None, False, False, False, False),
 "LR3-116": ("A", None, False, False, False, False),
}
UNC = {"LR3-004", "LR3-104", "LR3-114"}
assert set(CARRY) | UNC == set(ids) and not (set(CARRY) & UNC)
coded = [i for i in ids if i in CARRY]
seg = {n["case_id"]: n["in_dev8"] for n in neg["negatives"]}
diff = {n["case_id"]: n["pair_diff"] for n in neg["negatives"]}

def se(p, n): return math.sqrt(p*(1-p)/n)*100 if n else 0.0
def share(k, n): return f"{k}/{n}={100*k/n:.1f}% (SE {se(k/n, n):.1f}pp)"

from collections import Counter
cnt = Counter(v[0] for v in CARRY.values())
print("承登记主标分布(已编码 n=20):", dict(cnt), "sum", sum(cnt.values()))
for sname, sids_all in [("dev8", [i for i in ids if seg[i]]), ("LR3", [i for i in ids if not seg[i]])]:
    sids = [i for i in sids_all if i in CARRY]
    c = Counter(CARRY[i][0] for i in sids)
    w = [i for i in sids if CARRY[i][0] == "W"]; wh = [i for i in w if CARRY[i][2]]
    print(sname, "清单n=", len(sids_all), "已编码n=", len(sids), dict(c),
          "| W接口(已编码分母)", share(len(w), len(sids)), "| W硬核", share(len(wh), len(sids)),
          "| W接口(清单分母)", share(len(w), len(sids_all)))
    d_all = [diff[i] for i in sids_all]
    print("   ", sname, "清单负例子集 diff sum/mean/median:", sum(d_all), round(sum(d_all)/len(d_all), 3), statistics.median(d_all))
w = [i for i in coded if CARRY[i][0] == "W"]; wh = [i for i in w if CARRY[i][2]]
print("合并 W接口 已编码分母:", share(len(w), 20), "| 清单分母23:", share(len(w), 23), "| 总例30:", share(len(w), 30))
print("合并 W硬核 已编码分母:", share(len(wh), 20), "| 清单分母23:", share(len(wh), 23), "| 总例30:", share(len(wh), 30))
print("W子形态:", Counter(CARRY[i][1] for i in w))
amb = [i for i in coded if CARRY[i][3]]
print("含混* 例(承登记):", amb, share(len(amb), 20))
print("D主标:", [i for i in coded if CARRY[i][0] == "D"])
print("D次标:", [i for i in coded if CARRY[i][4]])
print("应期形态附记:", [i for i in coded if CARRY[i][5]])
all_d = [diff[i] for i in ids]
print("合并清单(23) diff sum/mean/median:", sum(all_d), round(sum(all_d)/23, 3), statistics.median(all_d))
ids92 = [n["case_id"] for n in neg92["negatives"]]
print("R92 n=", len(ids92), "进入:", sorted(set(ids)-set(ids92)), "离开:", sorted(set(ids92)-set(ids)))
print("LR3-010 in R93 list:", "LR3-010" in ids, "| in R92 list:", "LR3-010" in ids92)
print("UNC 三例 pair_diff:", {i: diff[i] for i in sorted(UNC)})
print("非负例(总例30-负例23):", 30-23)
