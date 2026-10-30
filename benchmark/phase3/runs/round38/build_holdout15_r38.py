#!/usr/bin/env python3
"""Round 38 host tooling: build holdout15 (40 cases) per PREREG §4 and host
rulings (YXS-015 disqualified for cross-case outcome misattribution found by
the enrichment seat; YXS-016 substitutes; YXS-014 asked_at and BYZ-008
subject corrected to the original books, each registered in BUILD-LOG).

Sources (all verified A-low by round38 data seats):
- cezi: zichu-cases-r38.jsonl holdout_eligible, first 20 by id
- liuren bianyi: bianyi-stock-r38.jsonl seal_eligible, host-selected 12
- liuren yuce: yuce-stock-r38.jsonl seal_eligible, host-selected 8 (015 out)
Enrichment (master_predictions / chart_full / question) from
liuren-enrich-r38.jsonl for all 20 liuren cases.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # benchmark/phase3
R38 = Path(__file__).resolve().parent
DV = R38 / "data-verify"

BYZ_SEL = ["BYZ-001", "BYZ-002", "BYZ-004", "BYZ-005", "BYZ-006", "BYZ-007",
           "BYZ-008", "BYZ-009", "BYZ-011", "BYZ-012", "BYZ-013", "BYZ-014"]
YXS_SEL = ["YXS-008", "YXS-009", "YXS-010", "YXS-011", "YXS-012", "YXS-013",
           "YXS-014", "YXS-016"]  # YXS-015 disqualified (host ruling), 016 in

BANNED_CARD_KEYS = {"grade_note", "contamination", "contamination_reason",
                    "contamination_rationale", "outcome", "outcome_grade",
                    "master", "master_predictions", "seal_eligible",
                    "seal_fail_reasons", "holdout_eligible", "review",
                    "method_hint", "disposition", "notes", "extractor_verdict_tail"}


def load_jsonl(path):
    return [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]


def banned_scan(obj, path=""):
    hits = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in BANNED_CARD_KEYS:
                hits.append(f"{path}/{k}")
            hits += banned_scan(v, f"{path}/{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            hits += banned_scan(v, f"{path}[{i}]")
    return hits


def main():
    zichu = load_jsonl(DV / "zichu-cases-r38.jsonl")
    bianyi = {r["id"]: r for r in load_jsonl(DV / "bianyi-stock-r38.jsonl")}
    yuce = {r["id"]: r for r in load_jsonl(DV / "yuce-stock-r38.jsonl")}
    enrich = {r["id"]: r for r in load_jsonl(DV / "liuren-enrich-r38.jsonl")}
    extra = DV / "liuren-enrich-yxs016.jsonl"
    if extra.exists():
        for r in load_jsonl(extra):
            enrich[r["id"]] = r

    zc_sel = sorted([r for r in zichu if r.get("holdout_eligible")],
                    key=lambda r: r["id"])[:20]
    assert len(zc_sel) == 20

    # exclusion sets: dev11 input filenames, holdout3-14 gold ids, POOL-IDS
    dev_ids = {p.stem for p in (ROOT.parent.parent / "benchmark" / "phase3").glob("*")}  # placeholder
    inputs_dir = ROOT / "inputs-dev11"
    if not inputs_dir.exists():
        # locate inputs-dev11 under benchmark/
        cands = list((ROOT.parent).rglob("inputs-dev11"))
        assert cands, "inputs-dev11 not found"
        inputs_dir = cands[0]
    dev_ids = {p.stem for p in inputs_dir.glob("*.json")}
    gold_ids = set()
    for n in range(3, 15):
        gf = ROOT / f"holdout{n}" / "test_gold.jsonl"
        if gf.exists():
            for r in load_jsonl(gf):
                gold_ids.add(r["id"])
    pool_ids = set()
    for cand in (ROOT.parent).rglob("POOL-IDS.txt"):
        pool_ids = {l.strip() for l in open(cand, encoding="utf-8") if l.strip()}
        break

    gold_rows, cards = [], []

    # ---------- cezi ----------
    for r in zc_sel:
        assert r["contamination"] == "low", r["id"]
        assert r["outcome_grade"].startswith("A"), r["id"]
        mp = r["master_predictions"]
        gold_rows.append({
            "id": r["id"], "tradition": "测字",
            "master": mp[0].get("master"),
            "source_work": r["provenance"]["book"],
            "subject": r["subject"]["name_or_desc"],
            "question_or_topic": r["context"]["question"],
            "asked_at": r["context"]["asked_at"],
            "context_at_prediction": r["context"].get("setting", ""),
            "master_predictions": mp,
            "outcome": r["outcome"],
            "outcome_grade": "A-low",
            "contamination": "low",
            "contamination_rationale": r.get("contamination_reason", ""),
            "grade_note": r.get("grade_note", ""),
            "provenance": {"work": r["provenance"]["book"],
                           "edition": r["provenance"]["edition"],
                           "page": r["provenance"]["page"]},
            "transcription": r["provenance"].get("transcription", "visual"),
            "license_status": r.get("license_status", ""),
            "redistributable": r.get("redistributable", False),
        })
        cards.append({
            "id": r["id"], "tradition": "测字",
            "subject": {"name_or_desc": r["subject"]["name_or_desc"]},
            "context": {
                "question": r["context"]["question"],
                "asked_at": r["context"]["asked_at"],
                "setting": r["context"].get("setting", ""),
                "attachments": {
                    "character_written": r["context"]["attachments"].get("character_written", ""),
                },
            },
            "provenance": {"book": r["provenance"]["book"],
                           "edition": r["provenance"]["edition"],
                           "page": r["provenance"]["page"]},
            "language": r.get("language", "zh-Hant"),
        })

    # ---------- liuren ----------
    corrections = []
    for cid in BYZ_SEL + YXS_SEL:
        led = bianyi.get(cid) or yuce.get(cid)
        enr = enrich[cid]
        assert led is not None and enr is not None, cid
        assert led["contamination"] == "low", cid
        assert led["outcome_grade"].startswith("A"), cid
        subject = led["subject"]
        asked_at = led["asked_at"]
        host_notes = []
        if cid == "BYZ-008":
            subject = subject.replace("离襄阳", "寓襄阳", 1)
            corrections.append("BYZ-008 subject 首字：台账「离襄阳」→原书标题「寓襄阳」，建卡/金标按原书。")
            host_notes.append("subject 首字据原书标题改「寓」（台账作「离」），见 ENRICH-NOTES。")
        if cid == "YXS-014":
            asked_at = asked_at.replace("抽酉时", "抽卯时") + "（月将卯）"
            corrections.append("YXS-014 asked_at：台账「昼占抽酉时」→原书例题「昼占抽卯时，月将卯」，建卡/金标按原书；补录课式图与抽卯时自洽。")
            host_notes.append("asked_at 据原书例题改「抽卯时，月将卯」（台账作抽酉时），见 ENRICH-NOTES。")
        if cid == "BYZ-005":
            corrections.append("BYZ-005 outcome 内人名：台账「唐枭台」vs 原书案验「唐皋台」——事件实质相符，金标 outcome 照台账原文保留、差异在此登记备核（不改金标事件文本）。")
            host_notes.append("outcome 人名台账作「唐枭台」、原书作「唐皋台」，事件相符，差异登记备核。")
        gold_rows.append({
            "id": cid, "tradition": "六壬",
            "master": enr["master_predictions"][0].get("master"),
            "source_work": led["source_work"],
            "subject": subject,
            "question_or_topic": enr["question_or_topic"],
            "asked_at": asked_at,
            "context_at_prediction": "",
            "master_predictions": enr["master_predictions"],
            "outcome": led["outcome"],
            "outcome_grade": "A-low",
            "contamination": "low",
            "contamination_rationale": "",
            "grade_note": (led.get("grade_note") or "") + (" " + " ".join(host_notes) if host_notes else ""),
            "provenance": {"work": led["source_work"],
                           "edition": led["provenance"]["edition"],
                           "page": led["provenance"]["page"],
                           "source_ref": led.get("source_ref", "")},
            "transcription": "visual",
            "redistributable": False,
            "chart_full": enr["chart_full"],
            "chart_complete": enr["chart_complete_revised"],
        })
        cards.append({
            "id": cid, "tradition": "六壬",
            "subject": {"name_or_desc": subject},
            "context": {
                "question": enr["question_or_topic"],
                "asked_at": asked_at,
                "setting": "",
                "attachments": {
                    "课式原文": enr["chart_full"],
                    "chart_complete": enr["chart_complete_revised"],
                },
            },
            "provenance": {"book": led["source_work"],
                           "edition": led["provenance"]["edition"],
                           "page": led["provenance"]["page"]},
            "language": "zh-Hans",
        })

    assert len(gold_rows) == 40 and len(cards) == 40
    ids = [r["id"] for r in gold_rows]
    assert len(set(ids)) == 40
    # exclusion assertions
    for cid in ids:
        assert cid not in dev_ids, f"{cid} in dev inputs"
        assert cid not in gold_ids, f"{cid} in earlier holdout gold"
        assert cid not in pool_ids, f"{cid} in POOL-IDS"
    # three-key pairwise distinct
    keys = [(r["subject"], r["asked_at"], r["question_or_topic"]) for r in gold_rows]
    assert len(set(keys)) == 40, "three-key collision"
    # banned key scan on cards
    for c in cards:
        hits = banned_scan(c)
        assert not hits, f"{c['id']} banned keys in card: {hits}"
    # composition assertions
    from collections import Counter
    trad = Counter(r["tradition"] for r in gold_rows)
    src = Counter(r["source_work"] for r in gold_rows)
    assert trad["测字"] == 20 and trad["六壬"] == 20, trad
    assert max(src.values()) <= 20, src
    assert all(r["contamination"] == "low" for r in gold_rows)

    # ---------- write ----------
    out_inputs = ROOT / "holdout15-inputs"
    out_dir = ROOT / "holdout15"
    out_inputs.mkdir(exist_ok=True)
    out_dir.mkdir(exist_ok=True)
    for c in cards:
        (out_inputs / f"{c['id']}.json").write_text(
            json.dumps(c, ensure_ascii=False, indent=1), encoding="utf-8")
    gold_path = out_dir / "test_gold.jsonl"
    with open(gold_path, "w", encoding="utf-8") as fh:
        for r in gold_rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    sha = hashlib.sha256(gold_path.read_bytes()).hexdigest()
    print("cases:", len(gold_rows))
    print("traditions:", dict(trad))
    print("sources:", dict(src))
    print("gold SHA-256:", sha)
    print("corrections:", len(corrections))
    for c in corrections:
        print(" -", c)
    # liuren DA-shizhi-face candidates (subject references another person/kin)
    kw = ("占友", "占同寓", "占观察", "占县", "卜先生", "卜太太", "占开钱店", "占往", "占流年", "自占", "占动静", "占会试", "占病", "占贼", "占年将", "占耕田", "占进京", "占被掳")
    lr = [r for r in gold_rows if r["tradition"] == "六壬"]
    for r in lr:
        print("LR", r["id"], "|", r["subject"], "|", r["question_or_topic"])


if __name__ == "__main__":
    main()
