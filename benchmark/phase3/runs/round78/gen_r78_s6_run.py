import json, sys, importlib.util, pathlib
spec = importlib.util.spec_from_file_location("w", "/home/hatch/workspace/divination/benchmark/phase3/runs/round78/gen_r78_s6_write.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
batch = sys.argv[1]
ids = m.BATCHES[batch]
written=[]
for cid in ids:
    assert cid in m.DATA, cid
    rec = m.build(cid)
    (m.OUT/f"{cid}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
    written.append(cid)
assert set(written)==set(ids) and len(written)==len(ids)
print(batch, "written", len(written), written)
