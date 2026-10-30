import json, pathlib
OUT = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round57/predictions")
ids = ["LY-517","LY-518","LY-519","LY-520","LY-521","LY-522","LY-523","LY-524","LY-525","LY-526","LY-527","LY-528","LY-529","LY-530","LY-531","LY-532","LY-533","LY-534","LY-535","LY-536","LY-537","LY-538","LY-539","LY-540","LY-541","LY-542","LY-543","LY-601","LY-602","LY-603","LY-604","LY-605","LY-606","LY-607","LY-608","LY-609","LY-610","LY-611","LY-612","LY-613"]
assert len(ids) == 40
cm = ru = di = 0
for cid in ids:
    p = OUT / f"{cid}.json"
    assert p.exists(), f"missing {cid}"
    d = json.loads(p.read_text(encoding="utf-8"))
    assert d["case_id"] == cid, cid
    assert set(d.keys()) == {"case_id","prediction_text","basis","confidence","trigger"}, (cid, d.keys())
    assert isinstance(d["confidence"], float) and 0 <= d["confidence"] <= 1, cid
    assert d["basis"].splitlines()[0].startswith("tradition"), cid
    assert "动化方向" in d["basis"] and "反转条件" in d["basis"] and "四路" in d["basis"], cid
    t = d["trigger"]
    assert set(t.keys()) == {"changed_main","reserve_used","disputed","reason"}, cid
    cm += t["changed_main"]; ru += t["reserve_used"]; di += t["disputed"]
    assert len(d["prediction_text"]) > 50 and len(d["basis"]) > 300, cid
print("ALL OK: files=40, id set exact")
print(f"trigger counts: changed_main={cm} reserve_used={ru} disputed={di}")
