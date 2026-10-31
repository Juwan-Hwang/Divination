import json, pathlib, collections
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
def load(p):
    with open(p, encoding="utf-8") as f: return json.load(f)
# --- verify task2 ---
d = load(base/"data/case-annotations-r63.json")
assert list(d.keys())==["_provenance","round","flags","annotations","special_checks","counts"], list(d.keys())
assert d["round"]==63 and len(d["annotations"])==87 and len(d["flags"])==87
vc = collections.Counter(a["disposition"] for a in d["annotations"])
assert vc==collections.Counter(d["counts"]["verdicts"]), (vc, d["counts"])
assert d["counts"]=={"selfreport_anons_total":87,"cases_total":87,"continuation_cases":77,"same_case_new_gist_cases":3,"new_flag_cases":7,"verdicts":{"成立":12,"部分成立":72,"不成立":2,"未核":1}}, d["counts"]
for a,f in zip(d["annotations"], d["flags"]):
    assert a["registered_round"]==63 and f["registered_round"]==63
    assert f["basis"]==a["finding"] and f["flag"]==a["flag"] and f["manifest_carry_suggestion"]==a["manifest_carry_suggestion"]==f["carry_suggestion"]
    assert f["verdict"]==a["disposition"] and f["relation"]==a["relation"]
    assert set(a.keys())=={"anon_id","case_id","disposition","finding","flag","manifest_carry_suggestion","relation","registered_round","sources_checked","source_seats"}
    if a["disposition"]=="部分成立": assert a["manifest_carry_suggestion"].strip()
    assert a["sources_checked"] and a["source_seats"]
rel = collections.Counter(a["relation"].split("（")[0] for a in d["annotations"])
print("relations:", dict(rel))
for cid in ["LY-254","YM-070","YM-068","LY-540","BZ-019","LY-025","AS-207"]:
    a=[x for x in d["annotations"] if x["case_id"]==cid][0]
    print(cid, a["disposition"], "|", a["relation"], "| carry:", a["manifest_carry_suggestion"][:120])
print("special_checks items:", [s["item"] for s in d["special_checks"]])
# --- verify task1 ---
r62 = load(base/"data/case-annotations-r62.json")
om = load(base/"runs/round63/judging/outcome-manifest.json")
txt = (base/"data/manifest-carryover-r63-addendum.md").read_text(encoding="utf-8")
secs = txt.split("### A")[1:]
assert len(secs)==65, len(secs)
partial=[a for a in r62["annotations"] if a["disposition"]=="部分成立"]
for a in partial:
    assert f"「{a['manifest_carry_suggestion']}」" in txt, a["case_id"]
    assert om["_r63_carryover_notes_addendum"][a["case_id"]]==a["manifest_carry_suggestion"]
tail = txt.split("## 文末清单")[1]
for disp,n in [("成立",14),("不成立",2),("未核",1)]:
    ids=[a["case_id"] for a in r62["annotations"] if a["disposition"]==disp]
    assert f"### {disp} {n} 件" in tail
    for cid in ids: assert f"- {cid}" in tail
print("addendum A-sections: 65; all carries verbatim in text; tail lists OK")
import os
for p in ["data/manifest-carryover-r63-addendum.md","data/case-annotations-r63.json"]:
    fp=base/p; print(p, fp.stat().st_size, "bytes")
print("ALL VERIFY OK")
