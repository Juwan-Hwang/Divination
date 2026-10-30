#!/usr/bin/env python3
"""R34 PREREG §6.② 编号重编：natal-batch2 QM->QL、MP->PU。

只改每行行首 id 字段的值（锚定正则 ^\{"id": "..."），其余字节逐字不动。
QM/MP->QL/PU 均为等长替换（前缀 2 字符＋3 位数字），文件总字节数不变。
执行前哈希、映射表、校验结果写入 RENUMBER-MAP.json。
异常在案：预注册与派单写 MP-001…056，盘上实有 MP-001…057 共 57 例
（同属《袁氏命谱》，CENSUS-NOTES.md 记「57 例（MP-001…MP-057）」，
92 例总数＝57＋35 亦合），本脚本按同号对应续编 PU-057，并在映射中登记。
"""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FILES = ["cases.jsonl", "cases-reviewed.jsonl"]
EXEC_DATE = "2026-10-30"

PINNED = {  # holdout12 既用映射（SEALED.md / PREREG §6.②）
    "QM-005": "QL-001",
    "QM-007": "QL-002",
    "QM-010": "QL-003",
    "QM-020": "QL-004",
    "QM-023": "QL-005",
    "QM-027": "QL-006",
    "QM-029": "QL-007",
    "QM-031": "QL-008",
}

LINE_RE = re.compile(r'^\{"id": "((?:QM|MP)-\d{3})", ')


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def build_maps(all_ids):
    qm_ids = sorted(i for i in all_ids if i.startswith("QM-"))
    mp_ids = sorted(i for i in all_ids if i.startswith("MP-"))
    assert len(qm_ids) == 35, qm_ids
    qm_map = dict(PINNED)
    nxt = 9
    for old in qm_ids:  # 原编号升序续编
        if old not in qm_map:
            qm_map[old] = f"QL-{nxt:03d}"
            nxt += 1
    assert nxt == 36 and len(qm_map) == 35
    assert sorted(qm_map.values()) == [f"QL-{i:03d}" for i in range(1, 36)]
    mp_map = {old: f"PU-{old[3:]}" for old in mp_ids}  # 同号对应
    return qm_map, mp_map


def main() -> int:
    originals = {}
    parsed = {}
    for fn in FILES:
        raw = (HERE / fn).read_bytes()
        originals[fn] = raw
        text = raw.decode("utf-8")
        lines = [l for l in text.split("\n") if l.strip()]
        parsed[fn] = [json.loads(l) for l in lines]
    ids0 = [r["id"] for r in parsed[FILES[0]]]
    for fn in FILES:
        assert [r["id"] for r in parsed[fn]] == ids0, f"{fn} id 序列与首文件不一致"
    assert len(ids0) == len(set(ids0)) == 92, (len(ids0), len(set(ids0)))

    qm_map, mp_map = build_maps(set(ids0))
    full_map = {**qm_map, **mp_map}

    files_meta = {}
    for fn in FILES:
        raw = originals[fn]
        text = raw.decode("utf-8")
        out_lines = []
        for line in text.split("\n"):
            if not line.strip():
                out_lines.append(line)
                continue
            m = LINE_RE.match(line)
            assert m, f"{fn}: 行首 id 模式不符: {line[:60]}"
            old = m.group(1)
            new_line = LINE_RE.sub('{"id": "' + full_map[old] + '", ', line, count=1)
            # 字节级核验：差异位必须全部落在 id 值区间内，且长度不变
            assert len(new_line) == len(line)
            lo = line.index('"id": "') + len('"id": "')
            hi = lo + len(old)
            diffs = [i for i, (a, b) in enumerate(zip(line, new_line)) if a != b]
            assert all(lo <= i < hi for i in diffs), (fn, old, diffs[:5])
            out_lines.append(new_line)
        new_raw = "\n".join(out_lines).encode("utf-8")
        assert len(new_raw) == len(raw)
        # JSON 层核验：除 id 外所有字段逐值相等、记录数不变
        new_recs = [json.loads(l) for l in new_raw.decode("utf-8").split("\n") if l.strip()]
        assert len(new_recs) == len(parsed[fn]) == 92
        for before, after in zip(parsed[fn], new_recs):
            assert after["id"] == full_map[before["id"]]
            b2 = {k: v for k, v in before.items() if k != "id"}
            a2 = {k: v for k, v in after.items() if k != "id"}
            assert b2 == a2, (fn, before["id"])
        new_ids = [r["id"] for r in new_recs]
        assert len(set(new_ids)) == 92 and not any(
            i.startswith(("QM-", "MP-")) for i in new_ids
        )
        (HERE / fn).write_bytes(new_raw)
        files_meta[fn] = {
            "sha256_before": sha256(raw),
            "sha256_after": sha256(new_raw),
            "bytes_before": len(raw),
            "bytes_after": len(new_raw),
            "records": len(new_recs),
        }
        print(f"{fn}: {files_meta[fn]}")

    renumber_map = {
        "purpose": "natal-batch2 编号重编：QM（《千里命稿》）→QL、MP（《袁氏命谱》）→PU，消除 MP 与 expansion6/modern-cn 现代案例的撞号，并使《千里命稿》编号与 holdout12 既用 QL 映射同号对齐。",
        "basis": "benchmark/phase3/runs/round34/PREREG.md §6.②；撞号定案见 runs/round34/audit-ids-report.json 与 R33 ADDENDUM-mp-collision（MP 撞号致 9 例错配）。",
        "executed": EXEC_DATE,
        "scope_files": FILES,
        "files": files_meta,
        "mapping_QM_to_QL": {k: qm_map[k] for k in sorted(qm_map)},
        "mapping_MP_to_PU": {k: mp_map[k] for k in sorted(mp_map)},
        "holdout12_alignment": {
            "note": "QL-001…008 为 holdout12 既用映射（holdout12/SEALED.md 第 6 行、金标 test_gold.jsonl 中 QL 行的 source_id 保持原文 QM 号），与本表逐条一致，经本表可解。",
            "pairs": {v: k for k, v in PINNED.items()},
        },
        "anomalies": [
            "预注册 §6.② 与派单写 MP-001…056，盘上两文件实有 MP-001…057 共 57 例（同属《袁氏命谱》；CENSUS-NOTES.md 记『57 例（MP-001…MP-057）』；两文件总记录 92＝57＋35）。本次按同号对应一并重编 MP-057→PU-057，未留旧前缀残号；如主持裁决不同，仅此一例可按本表回退。",
            "cases-reviewed.jsonl 中 QM-008 与 QL-005（原 QM-023）两例的 review.notes 自由文本内各有一处对对方的旧号互引（『与 QM-023 郑君…』『与 QM-008 郑君…』，系同姓不同人辨异注记）。按派单『只改 id 字段、其余字段逐字不动』未改原文，查阅以本映射为准（QM-008→QL-014、QM-023→QL-005）。cases.jsonl 无此类文本互引（旧号出现次数恰等于 id 数）。",
        ],
        "verification": "脚本内自验：记录数不变（两文件各 92）；新 id 全唯一且无 QM-/MP- 残留；逐行字节差异位全部落在 id 值区间内、行长与文件总字节数不变；逐记录 JSON 深比除 id 外全字段相等。独立复验见 verify_renumber_nb2_r34.py（反向映射回算改前哈希）。",
    }
    (HERE / "RENUMBER-MAP.json").write_text(
        json.dumps(renumber_map, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )
    print("RENUMBER-MAP.json written")
    print("QM->QL:", len(qm_map), " MP->PU:", len(mp_map))
    return 0


if __name__ == "__main__":
    sys.exit(main())
