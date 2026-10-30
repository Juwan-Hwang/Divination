# R39 六壬 W 监测复算脚本（唯一名；显式文件清单，无通配扫描）
# 复算：六壬 30 例集、配对负例 24 例集、合并/分源配对差与 SE、负例子集均差
import json, pathlib, math, statistics
base = pathlib.Path.home() / "workspace/divination/benchmark/phase3"
r39 = base / "runs/round39"
hm = json.loads((r39 / "judging/host-meta.json").read_text())
lr = sorted(k for k, v in hm.items() if isinstance(v, dict) and v.get("tradition") in ("liuren", "六壬"))
assert len(lr) == 30, lr
fs = json.loads((r39 / "final-scores.json").read_text())["ours_axis2"]
mb = json.loads((base / "data/master-baseline-dev9.json").read_text())
rows = [(c, fs[c], mb[c]["total"], round(fs[c] - mb[c]["total"], 4)) for c in lr]
neg = [r for r in rows if r[3] < 0]
expected_neg = ["LR2-013","LR2-014","LR2-015","LR2-016","LR2-017","LR2-018","LR2-019","LR2-021","LR2-022","LR2-023","LR2-024","OC-026","OC-027","OC-029","OC-030","LR3-002","LR3-004","LR3-006","LR3-008","LR3-101","LR3-107","LR3-110","LR3-112","LR3-116"]
assert sorted(r[0] for r in neg) == sorted(expected_neg), [r[0] for r in neg]
def stats(sub):
    ds = [r[3] for r in sub]; n = len(ds)
    se = statistics.stdev(ds) / math.sqrt(n) if n > 1 else 0.0
    return n, round(sum(ds)/n, 3), round(se, 3)
print("all30", stats(rows))
print("dev8-18", stats([r for r in rows if not r[0].startswith("LR3-")]))
print("LR3-12", stats([r for r in rows if r[0].startswith("LR3-")]))
print("neg24 mean diff", round(sum(r[3] for r in neg)/len(neg), 3))
for r in rows: print(r)
print("NEG SET MATCHES HOST LIST: OK, n =", len(neg))
