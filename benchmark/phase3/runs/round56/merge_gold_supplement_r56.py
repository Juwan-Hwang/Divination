#!/usr/bin/env python3
"""R56 并入数据席：把 SUPPLY-GOLD-SUPPLEMENT-r56 的 17 例断语逐字并入 holdout20 金标。

只改 17 例的 master_prediction（null -> 补录逐字）与 grade_note（末尾追加补录登记句；
WHY-030 另注「求求懷」首字置信约 0.8）。其余 8 例与全部其他字段一字不动。
本脚本不作断、不评分、不做 git 操作。
"""
import hashlib
import json
from pathlib import Path

SUPPLEMENT = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round56/digestion/SUPPLY-GOLD-SUPPLEMENT-r56.json")
GOLD = Path("/home/hatch/workspace/divination/benchmark/phase3/holdout20/test_gold.jsonl")

TARGET_IDS = [
    "QW-001", "QW-002", "QW-003", "QW-004", "QW-005", "QW-006",
    "QW-007", "QW-008", "QW-009", "QW-010", "QW-011", "QW-012",
    "WHY-003", "WHY-015", "WHY-021", "WHY-030", "WHY-067",
]


def outcome_hashes(rows):
    return {
        r["id"]: hashlib.sha256((r.get("outcome_record") or "").encode("utf-8")).hexdigest()
        for r in rows
    }


def main():
    supplement = json.loads(SUPPLEMENT.read_text(encoding="utf-8"))
    entries = {e["case_id"]: e for e in supplement["entries"]}
    assert set(entries.keys()) == set(TARGET_IDS), "补录件 id 集与目标 17 例不一致"
    assert len(entries) == 17, "补录件例数不为 17"

    raw_lines = GOLD.read_text(encoding="utf-8").splitlines()
    assert len(raw_lines) == 25, f"金标行数不为 25: {len(raw_lines)}"
    before = [json.loads(line) for line in raw_lines if line.strip()]
    assert len(before) == 25, "金标解析行数不为 25"
    before_ids = [r["id"] for r in before]
    assert len(set(before_ids)) == 25, "金标 id 有重复"
    before_outcome = outcome_hashes(before)
    before_by_id = {r["id"]: r for r in before}

    # 断言：改前 17 例 master_prediction 全为 null
    for cid in TARGET_IDS:
        assert cid in before_by_id, f"金标缺 {cid}"
        assert before_by_id[cid]["master_prediction"] is None, f"改前 {cid} master_prediction 非 null"

    after = []
    for row in before:
        new_row = dict(row)
        cid = row["id"]
        if cid in TARGET_IDS:
            e = entries[cid]
            mp = e["master_prediction"]
            assert isinstance(mp, str) and mp.strip(), f"补录件 {cid} master_prediction 为空"
            new_row["master_prediction"] = mp
            suffix = (
                f"断语经 R56 补录席自原书补录（transcription={e['transcription']}、"
                f"confidence={e['confidence']}），见 digestion/SUPPLY-GOLD-SUPPLEMENT-r56.md"
            )
            new_row["grade_note"] = row["grade_note"] + suffix
            if cid == "WHY-030":
                new_row["grade_note"] += "「求求懷」首字置信约 0.8。"
        after.append(new_row)

    # 断言：行数 25、id 集不变
    assert len(after) == 25, "改后行数不为 25"
    assert [r["id"] for r in after] == before_ids, "改后 id 顺序/集合变化"
    assert set(r["id"] for r in after) == set(before_ids), "改后 id 集变化"

    # 断言：改后 25 例全非空
    for r in after:
        assert isinstance(r["master_prediction"], str) and r["master_prediction"].strip(), \
            f"改后 {r['id']} master_prediction 为空"

    # 断言：outcome_record 逐行与改前哈希一致
    after_outcome = outcome_hashes(after)
    assert after_outcome == before_outcome, "outcome_record 哈希与改前不一致"

    # 断言：其余 8 例整行不变；17 例除 master_prediction/grade_note 外字段不变
    for b, a in zip(before, after):
        if b["id"] not in TARGET_IDS:
            assert a == b, f"非目标例 {b['id']} 被改动"
        else:
            for k in b.keys():
                if k not in ("master_prediction", "grade_note"):
                    assert a[k] == b[k], f"目标例 {b['id']} 字段 {k} 被改动"

    out_text = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in after)
    GOLD.write_text(out_text, encoding="utf-8")

    new_sha = hashlib.sha256(GOLD.read_bytes()).hexdigest()
    print(f"assertions: all passed (before 17 null, after 25 non-empty, lines=25, ids unchanged, outcome_record hashes unchanged)")
    print(f"new_sha256: {new_sha}")


if __name__ == "__main__":
    main()
