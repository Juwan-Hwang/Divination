# -*- coding: utf-8 -*-
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_r78_s5_parse import IDS
from gen_r78_s5_predict import predict

OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round78/predictions"

def run(batch):
    ids = IDS[batch]
    written = []
    os.makedirs(OUT, exist_ok=True)
    for cid in ids:
        p = predict(cid)
        path = os.path.join(OUT, f"{cid}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(p, f, ensure_ascii=False, indent=1)
        written.append(cid)
    # self-verify: exact-open each file, id-set assertion
    got = []
    for cid in ids:
        with open(os.path.join(OUT, f"{cid}.json"), encoding="utf-8") as f:
            d = json.load(f)
        assert d["case_id"] == cid, cid
        assert set(d.keys()) == {"case_id", "prediction_text", "basis", "confidence", "trigger"}, (cid, d.keys())
        assert set(d["trigger"].keys()) == {"changed_main", "reserve_used", "disputed", "reason"}
        assert d["basis"].splitlines()[0] == "tradition: liuyao", cid
        got.append(d["case_id"])
    assert set(got) == set(ids) and len(got) == len(ids), (batch, got)
    trig = {"changed_main": 0, "reserve_used": 0, "disputed": 0}
    for cid in ids:
        with open(os.path.join(OUT, f"{cid}.json"), encoding="utf-8") as f:
            d = json.load(f)
        for k in trig: trig[k] += 1 if d["trigger"][k] else 0
    print(f"{batch}: wrote {len(written)}/{len(ids)} verified id-set OK trigger={trig}")

if __name__ == "__main__":
    run(sys.argv[1])
