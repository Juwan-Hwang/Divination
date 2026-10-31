#!/usr/bin/env python3
"""R87 host verification of platform blind predictions (freeze gate).

Checks (host-run only, after all blind seats report):
- completeness: predictions dir id set == batches.json union (487);
- per-file: JSON parses, required fields present, confidence in [0,1],
  trigger subfields present with bool types;
- trigger recount over liuyao-flagged predictions (trigger dict present);
- tradition first-line checker (PREREG-r87 s.7 keyword set: simplified/
  traditional variants + English variants + 未见/未载 variants +
  「没有」 variant from R81 per ADDENDUM-r80 s.2), producing
  CANDIDATE flags only -- adjudication is by host reading originals;
- basis CLAIM declaration-group scan: multiple tradition declarations
  with mutually exclusive values are flagged for host adjudication.
Output: runs/round87/verify-predictions-host-r87.json + stdout summary.
"""
import json
import re
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
R87 = P3 / "runs/round87"
PRED = R87 / "predictions"
INPUTS = P3 / "inputs-dev12"

UNMARKED_PATTERNS = [
    "未标注", "未標註", "未注明", "未載", "未载", "未见", "未見",
    "没有 tradition", "没有tradition", "沒有 tradition", "沒有tradition",
    "无 tradition", "無 tradition", "no tradition", "not specified",
    "not stated", "no system field", "未提供", "缺載", "缺载",
]
CARD_VALUE_CLAIM_PATTERNS = [
    "卡面 tradition", "卡面tradition", "卡片 tradition",
    "與卡面一致", "与卡面一致", "卡面所載", "卡面所载",
]


def first_line(basis):
    for line in (basis or "").splitlines():
        if line.strip():
            return line.strip()
    return ""


def main():
    batches = json.loads((R87 / "batches.json").read_text(encoding="utf-8"))
    want = [cid for ids in batches.values() for cid in ids]
    want_set = set(want)
    assert len(want) == 487 and len(want_set) == 487

    files = {p.stem for p in PRED.glob("*.json")}
    missing = sorted(want_set - files)
    extra = sorted(files - want_set)

    bad = []
    trig_counts = {"changed_main": 0, "reserve_used": 0, "disputed": 0}
    trig_reasons = 0
    flags = []
    claim_groups_flag = []
    first_lines = {}

    for cid in sorted(want_set & files):
        try:
            pred = json.loads((PRED / f"{cid}.json").read_text(encoding="utf-8"))
        except Exception as e:
            bad.append((cid, f"json parse: {e}"))
            continue
        for f in ("case_id", "prediction_text", "basis", "confidence", "trigger"):
            if f not in pred:
                bad.append((cid, f"missing field {f}"))
        if pred.get("case_id") != cid:
            bad.append((cid, "case_id mismatch"))
        conf = pred.get("confidence")
        if not isinstance(conf, (int, float)) or not (0 <= conf <= 1):
            bad.append((cid, f"confidence out of range: {conf!r}"))
        tr = pred.get("trigger") or {}
        for k in ("changed_main", "reserve_used", "disputed"):
            if not isinstance(tr.get(k), bool):
                bad.append((cid, f"trigger.{k} not bool"))
            elif tr.get(k):
                trig_counts[k] += 1
        if tr.get("reason"):
            trig_reasons += 1

        # tradition first-line check
        fl = first_line(pred.get("basis", ""))
        first_lines[cid] = fl
        card_path = INPUTS / f"{cid}.json"
        card = json.loads(card_path.read_text(encoding="utf-8")) if card_path.is_file() else {}
        card_trad = card.get("tradition")
        card_sys = card.get("system")
        fl_low = fl.lower()
        has_unmarked = any(p.lower() in fl_low for p in UNMARKED_PATTERNS)
        has_claim = any(p in fl for p in CARD_VALUE_CLAIM_PATTERNS)
        if (card_trad or card_sys) and has_unmarked:
            flags.append({
                "case_id": cid, "kind": "card_has_field_but_first_line_unmarked",
                "card_tradition": card_trad, "card_system": card_sys,
                "first_line": fl,
            })
        if not (card_trad or card_sys) and has_claim:
            flags.append({
                "case_id": cid, "kind": "card_no_field_but_first_line_claims_card_value",
                "card_tradition": card_trad, "card_system": card_sys,
                "first_line": fl,
            })
        if card_trad and card_trad not in fl and not has_unmarked:
            flags.append({
                "case_id": cid, "kind": "card_tradition_not_in_first_line",
                "card_tradition": card_trad, "card_system": card_sys,
                "first_line": fl,
            })

        # CLAIM declaration groups: look for multiple 'tradition' value claims
        basis = pred.get("basis", "")
        claims = re.findall(r"tradition\s*[=＝:：]\s*([A-Za-z_\-]+|[一-鿿]{2,8})", basis)
        claims_set = {c for c in claims}
        if len(claims_set) > 1:
            claim_groups_flag.append({"case_id": cid, "claims": sorted(claims_set)})

    out = {
        "want": len(want_set), "files": len(files),
        "missing": missing, "extra": extra,
        "bad": bad, "trigger_counts": trig_counts,
        "trigger_reasons_nonempty": trig_reasons,
        "tradition_flag_candidates": flags,
        "claim_group_candidates": claim_groups_flag,
    }
    (R87 / "verify-predictions-host-r87.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"want {len(want_set)} files {len(files)} missing {len(missing)} extra {len(extra)} bad {len(bad)}")
    print("trigger", trig_counts, "reasons_nonempty", trig_reasons)
    print("tradition flag candidates", len(flags))
    for f in flags:
        print(" FLAG", f["case_id"], f["kind"], "| card:", f["card_tradition"], f["card_system"], "| line:", f["first_line"][:80])
    print("claim group candidates", len(claim_groups_flag))
    for f in claim_groups_flag:
        print(" CLAIM", f["case_id"], f["claims"])
    if bad:
        for b in bad[:20]:
            print(" BAD", b)


if __name__ == "__main__":
    main()
