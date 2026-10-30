import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
batches=json.loads((base/"runs/round59/batches.json").read_text())
ids=[]
for b in ["B16","B17","B18"]: ids+=batches[b]
ok=0; problems=[]
cm=ru=di=0; cm_ids=[]; ru_ids=[]; di_ids=[]
for cid in ids:
    p=base/f"runs/round59/predictions/{cid}.json"
    if not p.exists(): problems.append(f"{cid}: missing"); continue
    d=json.loads(p.read_text())
    if d.get("case_id")!=cid: problems.append(f"{cid}: case_id mismatch {d.get('case_id')}")
    for f in ("case_id","prediction_text","basis","confidence","trigger"):
        if f not in d: problems.append(f"{cid}: missing field {f}")
    t=d.get("trigger",{})
    for f in ("changed_main","reserve_used","disputed","reason"):
        if f not in t: problems.append(f"{cid}: trigger missing {f}")
    if not (0<=d.get("confidence",-1)<=1): problems.append(f"{cid}: confidence out of range")
    if not d.get("prediction_text"): problems.append(f"{cid}: empty prediction_text")
    if not d.get("basis","").startswith("tradition"): problems.append(f"{cid}: basis first line not tradition")
    if t.get("changed_main"): cm+=1; cm_ids.append(cid)
    if t.get("reserve_used"): ru+=1; ru_ids.append(cid)
    if t.get("disputed"): di+=1; di_ids.append(cid)
    ok+=1
print("expected", len(ids), "read_ok", ok)
print("problems", problems)
print("changed_main", cm, cm_ids)
print("reserve_used", ru, ru_ids)
print("disputed", di, di_ids)
