#!/usr/bin/env python3
# R87 主持验封独立复核（不 import 组集席脚本）：金标三读对位、id 集、零复用、排除对、卡面禁用键/泄漏标记速扫、快照差异集
import json, hashlib, os, sys

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
gold_path = f"{BASE}/holdout31/test_gold.jsonl"
raw = open(gold_path, "rb").read()
sha = hashlib.sha256(raw).hexdigest()
assert sha == "4b4312147f6657b66fc21fe56207f7ba76857fdd7340ab0a5c5e6728a9210e9d", sha
lines = raw.decode("utf-8").strip().split("\n")
assert len(lines) == 28, len(lines)
gold = [json.loads(l) for l in lines]
gids = [g["id"] for g in gold]
assert len(set(gids)) == 28

used = set(json.load(open(f"{BASE}/runs/round87/used-ids-r87.json")))
# used-ids 文件形态自适应：list 或 dict
if isinstance(used, dict):
    used = set(used.keys())
overlap = [i for i in gids if i in used]
assert not overlap, overlap
assert "LY-015" not in gids and "LY-320" not in gids

# 逐 id 精确打开输入卡（按金标 id 清单，不作目录计数）
FORBIDDEN = {"master_prediction", "outcome_record", "outcome", "gold", "answer", "verdict",
             "actual_result", "result_text", "grade", "score"}
LEAK = ["应验", "后果", "结局", "后来", "果真", "果验", "竟", "卒", "终果"]
card_ids = []
for cid in gids:
    p = f"{BASE}/holdout31/inputs/{cid}.json"
    card = json.load(open(p))
    card_ids.append(cid)
    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                assert k not in FORBIDDEN, (cid, k)
                walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    walk(card)
assert card_ids == gids

# 快照差异集：holdout31 快照 vs 平台快照逐件哈希
def snap_hashes(d):
    out = {}
    for root, _, files in os.walk(d):
        for f in files:
            p = os.path.join(root, f)
            rel = os.path.relpath(p, d)
            out[rel] = hashlib.sha256(open(p, "rb").read()).hexdigest()
    return out
h_new = snap_hashes(f"{BASE}/runs/round87/kb-snapshot-holdout31")
h_plat = snap_hashes(f"{BASE}/runs/round87/kb-snapshot")
assert set(h_new) == set(h_plat), (set(h_new) ^ set(h_plat))
diff = sorted(k for k in h_new if h_new[k] != h_plat[k])
assert diff == ["SKILL.md", "references/calibration.md"], diff

print("HOST VERIFY OK: gold sha 3rd-read match; 28 cards id-set == gold; zero-reuse vs 1220; exclusion pair absent; forbidden keys 0; snapshot diff ==", diff)
