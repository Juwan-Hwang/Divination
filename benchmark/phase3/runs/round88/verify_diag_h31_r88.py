#!/usr/bin/env python3
# DIAG-H31 verification: execution-face keyword counts + IN per-case check. Read-only.
import json

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
LR = ["BY-022","BY-023","BY-024","BY-025","BY-027","BY-028","BY-030",
      "DA-047","DA-048","DA-050","DA-051","DA-054","DA-055","DA-057"]
LY = ["GSZ-107","GSZ-108","GSZ-109","GSZ-110",
      "WHY-037","WHY-038","WHY-039","WHY-040","WHY-041","WHY-042","WHY-043","WHY-044","WHY-068","WHY-069"]

def basis(cid):
    return json.load(open(f"{BASE}/runs/round88/acceptance/predictions/{cid}.json")).get("basis","")

def cnt(ids, *keys):
    return [c for c in ids if any(k in basis(c) for k in keys)]

print("LR 定带:", cnt(LR, "定带"))
print("LY 定带:", cnt(LY, "定带"))
print("LR 应期三路字样:", cnt(LR, "应期三路"))
print("LR 盘面实载:", len(cnt(LR, "盘面实载")), "残损与缺路:", len(cnt(LR, "残损与缺路")))
print("LR 候选坐标全集:", cnt(LR, "候选坐标全集"))
print("LY 候选坐标表:", cnt(LY, "候选坐标表"))
print("LY 用神候选枚举/枚举:", cnt(LY, "枚举"))
print("LY 四路:", cnt(LY, "四路"))
print("LY 应期三步:", cnt(LY, "应期三步"))
print("LY 对表:", cnt(LY, "对表"))
print("LY 对象对齐:", cnt(LY, "对象对齐"))
print("LY 对象复述:", cnt(LY, "对象复述"))
print("ALL R80:", len(cnt(LR+LY, "R80-REV1")), "R87:", len(cnt(LR+LY, "R87-REV1")))
print("LR 落点处置/落点:", cnt(LR, "落点"))
print("LY 落点处置:", cnt(LY, "落点处置"))

# IN check: liuren anchors completeness; liuyao chart completeness
for cid in LR:
    inp = json.load(open(f"{BASE}/holdout31/inputs/{cid}.json"))
    a = inp.get("anchors", {})
    print(cid, "LR anchors:", {k: bool(a.get(k)) for k in ["asked_at","天盘","四课","三传"]}, "课名:", a.get("课名"))
for cid in LY:
    inp = json.load(open(f"{BASE}/holdout31/inputs/{cid}.json"))
    a = inp.get("anchors", {})
    print(cid, "LY anchors:", {k: bool(a.get(k)) for k in ["asked_at","ben_gua","chart_lines_top_to_bottom"]}, "bian:", a.get("bian_gua"), "moving:", a.get("moving_lines"))
