import json, pathlib
out = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round69/judging/arbitration-scores.jsonl")
rows = [
 {"anon_id":"P3-1d457bb1","direction":1.0,"claims":0.5,"timing":1.0,"total":2.5,"pass":False,
  "reason":"结局仅以it came to passe总承、未明名得职，方向部分吻合；得职仅总承未明名、有权者扶持未被印证且结局载友人虚伪，断语逐条核验只部分成立；预测数月内、结局三周内有载，月份量级偏迟但同在数月窗口内，timing部分命中。"},
 {"anon_id":"P3-2d03cae1","direction":1.0,"claims":0.5,"timing":0.0,"total":1.5,"pass":False,
  "reason":"结局载钱归还，回收方向部分吻合，但预测断至多一部分与结局程度未载不得判满；归还本身被印证，然窃者为年轻/文书经手人未被结局具体记载、追索受阻与钱已散动与三日归还相悖，claims仅部分；预测以月计拖延、结局三日后归还，应期明确错位，timing记0。"},
]
allowed = {0,0.5,1,1.5,2}
assert {r["anon_id"] for r in rows} == {"P3-1d457bb1","P3-2d03cae1"}
for r in rows:
    for k in ("direction","claims","timing"):
        assert r[k] in allowed, (r["anon_id"], k, r[k])
    assert r["total"] == r["direction"]+r["claims"]+r["timing"]
    assert r["pass"] == (r["total"] >= 4)
out.write_text("".join(json.dumps(r, ensure_ascii=False)+"\n" for r in rows), encoding="utf-8")
print(out, out.stat().st_size)
for r in rows: print(r["anon_id"], r["direction"], r["claims"], r["timing"], r["total"], r["pass"])
