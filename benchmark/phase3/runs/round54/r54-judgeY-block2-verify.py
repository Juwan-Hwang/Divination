import json, pathlib, re
root = pathlib.Path(__file__).parent
rows = [json.loads(l) for l in (root/"judging"/"judgeY-block2.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
dump = (root/"r54-judgeY-block2-dump.txt").read_text(encoding="utf-8")
orig_anons = re.findall(r"=== \d+ (P3-[0-9a-f]+) ->", dump)
assert len(rows) == 122, len(rows)
assert [r["anon_id"] for r in rows] == orig_anons, "anon order/set mismatch"
for r in rows:
    assert set(r.keys()) == {"anon_id","direction","claims","timing","total","pass","reason"}, r
    for k in ("direction","claims","timing"):
        assert r[k] in (0,0.5,1,1.5,2), r
    assert abs(r["total"] - (r["direction"]+r["claims"]+r["timing"])) < 1e-9, r
    assert r["pass"] == (r["total"] >= 4), r
    assert isinstance(r["reason"], str) and r["reason"]
print("OK rows=122 pass=", sum(1 for r in rows if r["pass"]), "anon_set_unchanged=True fields_ok=True totals_ok=True")
