#!/usr/bin/env python3
"""holdout4 acceptance judging-packet builder (packet-building role, review side).

Reads gold (after seal-log unsealing entry was appended), our predictions,
and roster/splits tradition+contamination metadata. Emits anonymized
packetA/packetB (54 entries: ours + master per case), host-mapping.json
(host only) and packet-meta.json. Performs NO scoring.

Master prediction_text construction (no key assertion / timing dropped):
- cases with statement_excerpt + key_assertions: excerpt followed by all
  key_assertions joined (key_assertions == reasoning_points verbatim in this
  pool, so reasoning_points are not repeated). master_predictions[*].outcome
  for the horary cases is byte-identical to the gold outcome description,
  i.e. it is the outcome record, NOT a prediction, and is therefore excluded
  from prediction_text.
- cases with verdict only: the verdict text is the master's statement.
Master direction: structured field copied when present, else null.
Master timing: gold has no structured timing field -> null for all masters.
outcome_record: gold outcome.description verbatim (the narrative text field).
"""
import hashlib
import json
import pathlib

BASE = pathlib.Path(__file__).resolve().parents[3]  # benchmark/phase3
ACC = BASE / "holdout4-acceptance"
OUT = ACC / "judging"


def anon_id(case_id: str, source: str) -> str:
    h = hashlib.sha256(f"holdout4-acc:{case_id}:{source}".encode("utf-8")).hexdigest()
    return "H4-" + h[:8]


def master_text(mp: dict) -> str:
    parts = []
    if mp.get("statement_excerpt"):
        parts.append(mp["statement_excerpt"].strip())
    if mp.get("key_assertions"):
        parts.append("；".join(a.strip() for a in mp["key_assertions"]))
    if mp.get("verdict"):
        parts.append(mp["verdict"].strip())
    return " ".join(p for p in parts if p)


SEALED_SHA256 = "4c5c989cb37c774ce78e3ecb8c2c96b6d4a333fdbd99a35c4d0105006219c147"


def main() -> None:
    import hashlib as _h
    raw = open(BASE / "holdout4" / "test_gold.jsonl", "rb").read()
    assert _h.sha256(raw).hexdigest() == SEALED_SHA256, "gold hash != sealed hash"
    gold = {}
    for line in open(BASE / "holdout4" / "test_gold.jsonl", encoding="utf-8"):
        if line.strip():
            r = json.loads(line)
            gold[r["id"]] = r

    roster = {}
    for line in open(BASE / "roster4-additions.jsonl", encoding="utf-8"):
        if line.strip():
            r = json.loads(line)
            roster[r["id"]] = r

    splits = json.loads(open(BASE / "splits4.json", encoding="utf-8").read())
    assert set(splits["holdout4"]) == set(gold), "splits/gold case mismatch"

    preds = {}
    for f in sorted((ACC / "predictions").glob("*.json")):
        p = json.loads(open(f, encoding="utf-8").read())
        preds[p["case_id"]] = p
    assert set(preds) == set(gold), "prediction/gold case mismatch"

    entries, mapping, meta = [], {}, {}
    for cid in sorted(gold):
        g = gold[cid]
        outcome_record = g["outcome"]["description"]
        tradition = roster[cid]["tradition"]
        contamination = roster[cid]["contamination"]
        assert tradition == g["tradition"]

        p = preds[cid]
        ours = {
            "anon_id": anon_id(cid, "ours"),
            "prediction_text": p["prediction_text"],
            "direction": p.get("direction"),
            "timing": p.get("timing"),
            "outcome_record": outcome_record,
        }

        mp = g["master_predictions"][0]
        master = {
            "anon_id": anon_id(cid, "master"),
            "prediction_text": master_text(mp),
            "direction": mp.get("direction"),
            "timing": mp.get("timing"),
            "outcome_record": outcome_record,
        }

        for src, e in (("ours", ours), ("master", master)):
            assert e["prediction_text"], f"empty prediction_text {cid} {src}"
            entries.append(e)
            mapping[e["anon_id"]] = {"case_id": cid, "source": src}
            meta[e["anon_id"]] = {"tradition": tradition, "contamination": contamination}

    entries.sort(key=lambda e: e["anon_id"])
    assert len(entries) == 50 and len({e["anon_id"] for e in entries}) == 50

    OUT.mkdir(parents=True, exist_ok=True)
    json.dump(entries[:25], open(OUT / "packetA.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    json.dump(entries[25:], open(OUT / "packetB.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    json.dump(mapping, open(OUT / "host-mapping.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    json.dump(meta, open(OUT / "packet-meta.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    stats = {"total": len(entries),
             "packetA": len(entries[:25]), "packetB": len(entries[25:]),
             "mapping": len(mapping), "meta": len(meta)}
    for src in ("ours", "master"):
        ids = [a for a, m in mapping.items() if m["source"] == src]
        stats[src] = {
            "n": len(ids),
            "direction_null": sum(1 for e in entries if e["anon_id"] in ids and e["direction"] is None),
            "timing_null": sum(1 for e in entries if e["anon_id"] in ids and e["timing"] is None),
        }
    json.dump(stats, open(OUT / "build" / "build-stats.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(json.dumps(stats, ensure_ascii=False))


if __name__ == "__main__":
    main()
