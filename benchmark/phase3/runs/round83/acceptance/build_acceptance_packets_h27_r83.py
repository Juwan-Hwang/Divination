#!/usr/bin/env python3
"""holdout27 acceptance packet builder (R83) (host tooling, build-only; no scoring).

Gold is OPENED only when the platform fully stands (R82 platform
all-stand; data/holdout27-seal-log.md s.10). This script is run by the
host only after the opening is declared; see
runs/round83/acceptance/OPENING.md.
- packet-ours.json: our blind predictions (predictions/<case_id>.json ->
  prediction_text) vs gold outcome text.
- packet-master.json: masters' recorded predictions, taken verbatim from
  the gold master_prediction string field, vs the same gold outcome text.
Case id set is the holdout27 acceptance composition written into
CASE_IDS below (27 ids, per seal log; asserted equal to the gold id
set). Anon ids: H27O-/H27M-<8 hex>,
random.Random(20261095), sorted case order, redraw on collision. Mappings
in judging/host-mapping.json (host-only).
Outcome/master texts come ONLY from holdout27/test_gold.jsonl itself.
Gold integrity gate: the SHA-256 of holdout27/test_gold.jsonl is asserted
equal to the sealed value before any packet is built; a mismatch aborts.
Built-in assertions: both packets 27 items; anon id sets unique and
disjoint; host-mapping covers 54 entries; every outcome_record verbatim
equal to the gold outcome text; packet-ours prediction_text verbatim equal
to the predictions file prediction_text; packet-master prediction_text
verbatim equal to the composed gold master text.
"""
import hashlib
import json
import random
from pathlib import Path

ACC = Path(__file__).resolve().parent
P3 = ACC.parents[2]
GOLD = P3 / "holdout27" / "test_gold.jsonl"
GOLD_SHA256 = "81b1d7c4df8428cb014f6054ac113f24c288f7257fc6437f934ca8ba35ac1295"
CASE_IDS = [
    "DS-040", "DS-041", "DS-042", "DS-043", "DS-044", "DS-045",
    "DS-046", "DS-048", "DS-049",
    "QM-044", "QM-045", "QM-046", "QM-047", "QM-048", "QM-049",
    "QM-052", "QM-055", "QM-058",
    "GSZ-079", "GSZ-081", "GSZ-084", "GSZ-086", "GSZ-088",
    "WHY-008", "WHY-009", "WHY-010", "WHY-011",
]
SEED = 20261095


def outcome_text(rec):
    o = rec.get("outcome_record")
    if isinstance(o, str) and o.strip():
        return o
    raise ValueError(f"no outcome text for {rec.get('id')}")


def master_text(rec):
    m = rec.get("master_prediction")
    if isinstance(m, str) and m.strip():
        return m
    raise ValueError(f"no master text for {rec.get('id')}")


def main():
    digest = hashlib.sha256(GOLD.read_bytes()).hexdigest()
    assert digest == GOLD_SHA256, digest
    print(f"gold SHA-256 assertion passed: {digest}")

    gold = {}
    for line in open(GOLD, encoding="utf-8"):
        line = line.strip()
        if line:
            r = json.loads(line)
            gold[r["id"]] = r
    batch_ids = list(CASE_IDS)
    assert len(batch_ids) == 27 and len(set(batch_ids)) == 27, len(batch_ids)
    assert set(batch_ids) == set(gold), (
        sorted(set(batch_ids) - set(gold)), sorted(set(gold) - set(batch_ids)))
    ids = sorted(batch_ids)
    assert len(ids) == 27, len(ids)

    preds = {}
    for cid in ids:
        p = json.loads((ACC / "predictions" / f"{cid}.json").read_text(encoding="utf-8"))
        preds[cid] = p["prediction_text"]

    rng = random.Random(SEED)
    used = set()

    def new_anon(prefix):
        while True:
            a = prefix + "-%08x" % rng.getrandbits(32)
            if a not in used:
                used.add(a)
                return a

    ours_items, master_items = [], []
    mapping = {"ours": {}, "master": {}}
    for cid in ids:
        oc = outcome_text(gold[cid])
        a1 = new_anon("H27O")
        ours_items.append({"anon_id": a1, "prediction_text": preds[cid],
                           "outcome_record": oc})
        mapping["ours"][a1] = cid
        a2 = new_anon("H27M")
        master_items.append({"anon_id": a2, "prediction_text": master_text(gold[cid]),
                             "outcome_record": oc})
        mapping["master"][a2] = cid
    ours_items.sort(key=lambda x: x["anon_id"])
    master_items.sort(key=lambda x: x["anon_id"])

    assert len(ours_items) == 27, len(ours_items)
    assert len(master_items) == 27, len(master_items)
    anon_ours = [e["anon_id"] for e in ours_items]
    anon_master = [e["anon_id"] for e in master_items]
    assert len(set(anon_ours)) == 27, len(set(anon_ours))
    assert len(set(anon_master)) == 27, len(set(anon_master))
    assert not (set(anon_ours) & set(anon_master))
    assert len(mapping["ours"]) + len(mapping["master"]) == 54
    assert set(mapping["ours"]) == set(anon_ours)
    assert set(mapping["master"]) == set(anon_master)
    assert set(mapping["ours"].values()) == set(ids)
    assert set(mapping["master"].values()) == set(ids)
    for e in ours_items:
        cid = mapping["ours"][e["anon_id"]]
        assert e["outcome_record"] == outcome_text(gold[cid]), cid
        assert e["prediction_text"] == preds[cid], cid
    for e in master_items:
        cid = mapping["master"][e["anon_id"]]
        assert e["outcome_record"] == outcome_text(gold[cid]), cid
        assert e["prediction_text"] == master_text(gold[cid]), cid
    print("assertions passed: packets 27+27; anon sets unique (27+27) and disjoint; "
          "host-mapping covers 54")
    print("assertions passed: every outcome_record verbatim vs gold outcome; "
          "ours prediction_text verbatim vs predictions files; "
          "master prediction_text verbatim vs gold master text")

    JD = ACC / "judging"
    JD.mkdir(parents=True, exist_ok=True)
    for name, obj in (("packet-ours.json", ours_items),
                      ("packet-master.json", master_items),
                      ("host-mapping.json", mapping)):
        with open(JD / name, "w", encoding="utf-8") as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=1)
    (JD / "anon-seed.txt").write_text(
        f"anon seed: {SEED}; H27O- ours, H27M- master; random.Random(SEED), "
        "sorted case order, redraw on collision.\n", encoding="utf-8")
    print(f"gold: {len(ids)}; packet-ours: {len(ours_items)}; packet-master: {len(master_items)}")
    print("outcome non-empty:", sum(1 for e in ours_items if e["outcome_record"].strip()))
    print("master text non-empty:", sum(1 for e in master_items if e["prediction_text"].strip()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
