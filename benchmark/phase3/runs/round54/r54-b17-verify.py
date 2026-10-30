import json, pathlib
base = pathlib.Path(__file__).parent / "predictions"
ids = ["LY-614","LY-615","LY-616","LY-617","LY-618","LY-619","LY-620","LY-621","LY-622","LY-623","LY-624","LY-625","LY-626","LY-627","LY-628","LY-629","MH-001","MH-002","MH-003","MH-006"]
cm=ru=di=0; ok=0; problems=[]
for cid in ids:
    p = base / f"{cid}.json"
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        problems.append(f"{cid}: parse/read fail {e}"); continue
    for f in ["case_id","prediction_text","basis","confidence","trigger"]:
        if f not in d: problems.append(f"{cid}: missing {f}")
    if d.get("case_id")!=cid: problems.append(f"{cid}: case_id mismatch {d.get('case_id')}")
    if not (isinstance(d.get("confidence"),(int,float)) and 0<=d["confidence"]<=1): problems.append(f"{cid}: confidence bad")
    t=d.get("trigger",{})
    for k in ["changed_main","reserve_used","disputed"]:
        if not isinstance(t.get(k),bool): problems.append(f"{cid}: trigger.{k} not bool")
    if not isinstance(t.get("reason"),str): problems.append(f"{cid}: reason not str")
    if cid.startswith("LY"):
        if t.get("changed_main"): cm+=1
        if t.get("reserve_used"): ru+=1
        if t.get("disputed"): di+=1
    else:
        if any([t.get("changed_main"),t.get("reserve_used"),t.get("disputed")]) or t.get("reason")!="":
            problems.append(f"{cid}: non-liuyao trigger not all-false/empty")
    if d.get("basis","").splitlines() and ("tradition" in d["basis"].splitlines()[0] or "system" in d["basis"].splitlines()[0]):
        pass
    else:
        problems.append(f"{cid}: basis first line lacks tradition/system")
    ok+=1
print(f"checked={len(ids)} parsed_ok={ok}")
print(f"liuyao trigger counts: changed_main={cm} reserve_used={ru} disputed={di}")
print("problems:", problems if problems else "none")
