#!/usr/bin/env python3
# DIAG-H31 bottom-sheet builder (R88 diagnosis seat). Read-only on inputs; writes one compact txt in round88/.
import json, os, re

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
IDS = ["BY-022","BY-023","BY-024","BY-025","BY-027","BY-028","BY-030",
       "DA-047","DA-048","DA-050","DA-051","DA-054","DA-055","DA-057",
       "GSZ-107","GSZ-108","GSZ-109","GSZ-110",
       "WHY-037","WHY-038","WHY-039","WHY-040","WHY-041","WHY-042","WHY-043","WHY-044","WHY-068","WHY-069"]

final = json.load(open(f"{BASE}/runs/round88/acceptance/judging/final-scores-h31.json"))
hm = json.load(open(f"{BASE}/runs/round88/acceptance/judging/host-mapping.json"))
inv_o = {v: k for k, v in hm["ours"].items()}
inv_m = {v: k for k, v in hm["master"].items()}

def load_jsonl(p):
    return [json.loads(l) for l in open(p) if l.strip()]

judges = {}
for name in ["judgeO1","judgeO2","judgeM1","judgeM2"]:
    judges[name] = {r["anon_id"]: r for r in load_jsonl(f"{BASE}/runs/round88/acceptance/judging/{name}.jsonl")}

gold = {}
for r in load_jsonl(f"{BASE}/holdout31/test_gold.jsonl"):
    gold[r.get("case_id") or r.get("id")] = r

out = []
scan = {}
for cid in IDS:
    pred = json.load(open(f"{BASE}/runs/round88/acceptance/predictions/{cid}.json"))
    inp = json.load(open(f"{BASE}/holdout31/inputs/{cid}.json"))
    g = gold.get(cid, {})
    assert pred.get("case_id") == cid, cid
    o1 = judges["judgeO1"][inv_o[cid]]; o2 = judges["judgeO2"][inv_o[cid]]
    m1 = judges["judgeM1"][inv_m[cid]]; m2 = judges["judgeM2"][inv_m[cid]]
    # sanity: judge totals vs final scores (mean of two views)
    om = round((o1["total"] + o2["total"]) / 2, 4); mm = round((m1["total"] + m2["total"]) / 2, 4)
    assert abs(om - final["ours"][cid]) < 0.26, (cid, om, final["ours"][cid])
    assert abs(mm - final["master"][cid]) < 0.26, (cid, mm, final["master"][cid])
    trig = pred.get("trigger", {})
    basis = pred.get("basis", "") or ""
    ptext = pred.get("prediction_text", "") or ""
    s = {}
    s["trigger"] = trig
    s["chart_complete"] = inp.get("chart_complete")
    s["sec8_mention"] = ("R80-REV1" in basis) or ("第八节" in basis)
    s["sec12_mention"] = ("R87-REV1" in basis) or ("第十二节" in basis)
    s["cand_table"] = ("候选坐标" in basis)
    s["band"] = any(k in basis for k in ["定带", "等级带", "量级带", "功量核算"])
    s["liuren_3roads"] = ("应期三路" in basis) or all(k in basis for k in ["逢值", "逢冲"]) 
    s["enum"] = ("候选枚举" in basis) or ("用神候选" in basis)
    s["four_roads"] = ("四路合参" in basis)
    s["timing3"] = ("应期三步" in basis)
    s["category_table"] = ("门类对表" in basis) or ("门类应期对表" in basis)
    s["obj_align"] = ("对象对齐" in basis)
    scan[cid] = s
    out.append(f"\n{'='*100}\n### {cid}  ours={final['ours'][cid]} master={final['master'][cid]} diff={final['per_case'][cid]['diff']}")
    out.append(f"--SCAN-- {json.dumps(s, ensure_ascii=False)}")
    out.append(f"--JUDGE-O-- O1 d{o1['direction']} c{o1['claims']} t{o1['timing']} tot{o1['total']}: {o1['reason']}")
    out.append(f"           O2 d{o2['direction']} c{o2['claims']} t{o2['timing']} tot{o2['total']}: {o2['reason']}")
    out.append(f"--JUDGE-M-- M1 d{m1['direction']} c{m1['claims']} t{m1['timing']} tot{m1['total']}: {m1['reason']}")
    out.append(f"           M2 d{m2['direction']} c{m2['claims']} t{m2['timing']} tot{m2['total']}: {m2['reason']}")
    out.append(f"--INPUT-- {json.dumps(inp, ensure_ascii=False)}")
    out.append(f"--PRED-- {ptext}")
    out.append(f"--BASIS-- {basis}")
    out.append(f"--GOLD-- {json.dumps(g, ensure_ascii=False)}")

dst = f"{BASE}/runs/round88/acceptance/diagnosis/diag_compact_h31_r88.txt"
os.makedirs(os.path.dirname(dst), exist_ok=True)
with open(dst, "w") as f:
    f.write("\n".join(out))
print("wrote", dst, os.path.getsize(dst))
print(json.dumps(scan, ensure_ascii=False, indent=1))
