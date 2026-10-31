# -*- coding: utf-8 -*-
import importlib.util, json, pathlib
P = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
spec = importlib.util.spec_from_file_location("wb", P/'runs/round89/write_b0910_r89.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)  # __name__ != __main__, main block skipped; all add() executed in order
DATA, IDS, OUT = m.DATA, m.IDS, m.OUT
assert [r[0] for r in DATA] == IDS, ([r[0] for r in DATA], IDS)
rows = DATA[20:]
assert [r[0] for r in rows] == IDS[20:]
m.emit(rows, IDS[20:])
for cid in IDS:
    rec = json.loads((OUT/f"{cid}.json").read_text(encoding="utf-8"))
    assert rec["case_id"] == cid and rec["basis"].splitlines()[0] == "liuyao"
    assert set(rec.keys()) == {"case_id","prediction_text","basis","confidence","trigger"}
    assert set(rec["trigger"].keys()) == {"changed_main","reserve_used","disputed","reason"}
def cnt(k):
    return sum(1 for cid in IDS if json.loads((OUT/f"{cid}.json").read_text(encoding="utf-8"))["trigger"][k])
print("FULLSET OK 40; trigger counts changed_main=%d reserve_used=%d disputed=%d" % (cnt("changed_main"), cnt("reserve_used"), cnt("disputed")))
