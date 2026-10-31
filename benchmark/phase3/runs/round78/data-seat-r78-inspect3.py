#!/usr/bin/env python3
import json, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
J = BASE + "/runs/round78/judging"

# named-path opens only (no listing): host-mapping + packets by R77 naming precedent
hm_path = J + "/host-mapping.json"
print("host-mapping exists:", os.path.isfile(hm_path))
anon = None
if os.path.isfile(hm_path):
    with open(hm_path, encoding="utf-8") as f:
        hm = json.load(f)
    print("host-mapping type:", type(hm).__name__)
    s = json.dumps(hm, ensure_ascii=False)
    # find LR2-016 mapping in common shapes
    if isinstance(hm, dict):
        for k, v in hm.items():
            if v == "LR2-016" or k == "LR2-016":
                print("mapping pair:", k, "->", v)
                anon = k if v == "LR2-016" else v
    print("LR2-016 in hm text:", "LR2-016" in s)

with open(BASE + "/runs/round78/judging/outcome-manifest.json", encoding="utf-8") as f:
    man = json.load(f)
lr = man["cases"].get("LR2-016")

for pname in ("packet1.json", "packetA.json"):
    p = J + "/" + pname
    print(pname, "exists:", os.path.isfile(p))
    if not os.path.isfile(p):
        continue
    with open(p, encoding="utf-8") as f:
        pk = json.load(f)
    entries = pk if isinstance(pk, list) else pk.get("cases") or pk.get("entries") or []
    if isinstance(pk, dict) and not entries:
        print("  packet dict keys:", list(pk.keys())[:10])
    for e in entries:
        if isinstance(e, dict) and (e.get("anon_id") == anon or e.get("case_id") == "LR2-016"):
            print("  entry anon:", e.get("anon_id"), "keys:", list(e.keys()))
            print("  editor_note:", json.dumps(e.get("editor_note"), ensure_ascii=False))
            print("  outcome == manifest cases[LR2-016]:", e.get("outcome_record") == lr)
