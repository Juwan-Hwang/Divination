#!/usr/bin/env python3
# R96 holdout35 封存修复席脚本：9 卡 anchors「四化锚点」泄露改写（h34 式盘面事实转述）
# 纪律：不换例、不改构成、不动金标、不动其余 19 卡；改后重跑泄露扫描（LCS<12 对 MP 与 outcome）
import json, hashlib, pathlib, sys

BASE = pathlib.Path.home() / "workspace/divination/benchmark/phase3"
H35 = BASE / "holdout35"
IDS28 = ["DA-082","DA-083","DA-085","DA-086","DA-087","DA-088","DA-090",
         "BY-054","BY-055","BY-056","BY-057","BY-058","BY-060","BY-061",
         "ZW-024","ZW-025","ZW-026","ZW-027","ZW-033","ZW-034","ZW-035",
         "ZW-036","ZW-037","ZW-038","ZW-039","ZW-044","ZW-045","ZW-046"]
FIX = {
 "ZW-025": "交友宫在乙亥、宫干乙；乙干四化：天机禄飞夫妻，天梁权飞夫妻，紫微科飞兄弟，太阴忌飞迁移，迁移与命宫相对；28岁流年（D5-29-21）",
 "ZW-026": "夫妻宫干甲、地支辰；甲干廉贞得禄、落父母位，破军得权、落交友位；本命夫妻三化（禄、权、科）飞入12–21大限三合方（D5-30-08）",
 "ZW-033": "命宫干乙，天梁以权飞迁，论自化权；12–21运内见自化忌，20岁流年命宫叠未宫",
 "ZW-034": "迁移位巨门带生年忌、重叠；疾厄为来因宫、同见巨门忌；22–31运，大命与大迁两宫干合化太阳忌；命宫忌飞冲疾厄",
 "ZW-035": "13–22大运命宫落午（本命疾厄位，紫微坐守）；命宫亥位己干，太阴同铃星坐守",
 "ZW-037": "命宫格干癸；癸干太阴科落子女位；太阴所坐宫干庚，庚干亦使太阴成科（自化）；至第三大限，子女位改作大限疾厄",
 "ZW-038": "生年干癸：破军在交友位，得禄且自化禄；太阴科落财帛位；福德位宫干庚，庚干科亦飞财帛，癸、庚两干之科同会太阴",
 "ZW-039": "生年干辛；田宅位太阳坐守、自化权；田宅对宫即子女位",
 "ZW-046": "财帛位见生年禄；生年忌同宫自化禄；行运逆行，大限命宫叠本命财帛位、坐生年禄，禄归大限命宫，成反格（万象归一元，ZZ-M135）",
}
assert set(FIX) <= set(IDS28) and len(FIX) == 9

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def lcs_len(a, b):
    best = 0; prev = [0]*(len(b)+1)
    for i in range(1, len(a)+1):
        cur = [0]*(len(b)+1)
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                cur[j] = prev[j-1]+1
                if cur[j] > best: best = cur[j]
        prev = cur
    return best

gold_path = H35 / "test_gold.jsonl"
gold_sha_before = sha(gold_path)
gold = {}
for line in gold_path.read_text(encoding="utf-8").splitlines():
    g = json.loads(line); gold[g["id"]] = g
assert list(gold) == IDS28, "金标 id 集/序与定版构成不符"

before = {cid: sha(H35/"inputs"/f"{cid}.json") for cid in IDS28}
old_anchor = {}
for cid, new in FIX.items():
    p = H35/"inputs"/f"{cid}.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    assert list(d.keys()) == ["id","tradition","subject","context","question","setting",
        "provenance","redistributable","license_status","anchors"], cid
    old_anchor[cid] = d["anchors"]["四化锚点"]
    d["anchors"]["四化锚点"] = new
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

after = {cid: sha(H35/"inputs"/f"{cid}.json") for cid in IDS28}
changed = [c for c in IDS28 if before[c] != after[c]]
assert changed == [c for c in IDS28 if c in FIX], f"改动集不符: {changed}"
assert sha(gold_path) == gold_sha_before, "金标被改动"

# 重跑泄露扫描：28 卡全文 vs 金标 MP 与 outcome，LCS 须 <12
report = []
worst = 0
for cid in IDS28:
    card = (H35/"inputs"/f"{cid}.json").read_text(encoding="utf-8")
    lmp = lcs_len(card, gold[cid]["master_prediction"])
    lout = lcs_len(card, gold[cid]["outcome_record"])
    worst = max(worst, lmp, lout)
    report.append((cid, lmp, lout))
    assert lmp < 12 and lout < 12, f"{cid} 仍泄露: MP={lmp} OUT={lout}"
print("gold_sha256:", gold_sha_before)
print("changed:", changed)
for cid, lmp, lout in report:
    if cid in FIX: print(f"{cid}: LCS MP={lmp} OUT={lout} (原锚点: {old_anchor[cid]})")
print("worst LCS all28:", worst)
print("OK")
