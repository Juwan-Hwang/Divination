#!/usr/bin/env python3
"""R39 §4.1 inputs-dev12 校验脚本（数据角自写，唯一名）。

三项校验（PREREG §4.1 写死口径）：
(1) inputs-dev12 与 inputs-dev11 的 id 集（文件名集）全等、卡数各 487；
(2) 两目录 JSON 深比对 diff 只出现在 STRIP-LOG 登记的 15 卡 20 字段内
    （期望集在下方 EXPECTED 硬编码，与扫描件清单一致）；
    附带字节级核查：未登记的 472 卡逐字（SHA-256）一致，登记卡必有差异。
(3) 题面字段逐卡哈希不变。题面字段集（按 INPUT-HYGIENE-SCAN.md 口径定义）：
    - 顶层标识键：id / uid / source_id（卡内有者）
    - subject（整棵子树）
    - context.question
    - context.attachments 课式本体：attachments 全部键扣除非课式字段
      {note, chart_note, source, secondhand, chart_excerpt} 后的子集
    哈希方式：上述字段组装为规范 dict 后 json.dumps(sort_keys=True,
    ensure_ascii=False) 的 SHA-256。
BUILD-MANIFEST.md 非卡，不入 (1)(2) 卡口径；其存在单独报告。
"""
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]  # benchmark/phase3/
A = ROOT / "inputs-dev11"
B = ROOT / "inputs-dev12"

EXPECTED = {
    ("AS-304", "provenance.book"), ("AS-304", "provenance.url"),
    ("AS-306", "provenance.book"),
    ("WP-002", "provenance.url"),
    ("WP-003", "provenance.work"), ("WP-003", "provenance.url"),
    ("WP-006", "provenance.work"), ("WP-006", "provenance.url"),
    ("WP-007", "provenance.url"),
    ("WP-008", "provenance.work"), ("WP-008", "provenance.url"),
    ("WP-009", "provenance.url"),
    ("WP-012", "provenance.url"),
    ("WP-013", "provenance.page"),
    ("BZ-301", "context.setting"),
    ("ZY-003", "context.setting"),
    ("LY-506", "context.setting"),
    ("BZ-016", "context.setting"),
    ("AS-015", "context.asked_at"),
    ("AS-015", "context.attachments.note"),
}
EXPECTED_CARDS = {c for c, _ in EXPECTED}
NON_CHART_ATTACHMENT_KEYS = {"note", "chart_note", "source", "secondhand", "chart_excerpt"}


def deep_diff(a, b, path=""):
    out = []
    if type(a) is not type(b):
        return [path]
    if isinstance(a, dict):
        for k in sorted(set(a) | set(b)):
            p = f"{path}.{k}" if path else k
            if k not in a or k not in b:
                out.append(p)
            else:
                out.extend(deep_diff(a[k], b[k], p))
    elif isinstance(a, list):
        if len(a) != len(b):
            out.append(path)
        else:
            for i, (x, y) in enumerate(zip(a, b)):
                out.extend(deep_diff(x, y, f"{path}[{i}]"))
    elif a != b:
        out.append(path)
    return out


def face_hash(data):
    face = {}
    for k in ("id", "uid", "source_id"):
        if k in data:
            face[k] = data[k]
    if "subject" in data:
        face["subject"] = data["subject"]
    ctx = data.get("context") or {}
    if "question" in ctx:
        face["context.question"] = ctx["question"]
    att = ctx.get("attachments")
    if isinstance(att, dict):
        face["context.attachments.chart"] = {
            k: v for k, v in att.items() if k not in NON_CHART_ATTACHMENT_KEYS
        }
    blob = json.dumps(face, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def sha_file(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    ok = True
    a_ids = {p.stem for p in A.glob("*.json")}
    b_ids = {p.stem for p in B.glob("*.json")}
    print(f"(1) dev11 cards={len(a_ids)} dev12 cards={len(b_ids)}")
    print(f"(1) id sets equal: {a_ids == b_ids}; symdiff={sorted(a_ids ^ b_ids)}")
    if not (len(a_ids) == len(b_ids) == 487 and a_ids == b_ids):
        ok = False
    print(f"(1) BUILD-MANIFEST in dev12 exists: {(B / 'BUILD-MANIFEST.md').exists()} (non-card, reported only)")

    all_diffs = set()
    byte_same_unexpected, byte_diff_unexpected = [], []
    face_mismatch = []
    for cid in sorted(a_ids):
        pa, pb = A / f"{cid}.json", B / f"{cid}.json"
        da = json.loads(pa.read_text(encoding="utf-8"))
        db = json.loads(pb.read_text(encoding="utf-8"))
        for p in deep_diff(da, db):
            all_diffs.add((cid, p))
        same_bytes = sha_file(pa) == sha_file(pb)
        if cid in EXPECTED_CARDS and same_bytes:
            byte_same_unexpected.append(cid)
        if cid not in EXPECTED_CARDS and not same_bytes:
            byte_diff_unexpected.append(cid)
        if face_hash(da) != face_hash(db):
            face_mismatch.append(cid)

    print(f"(2) deep-diff (card, field) count={len(all_diffs)}; expected={len(EXPECTED)}")
    print(f"(2) diffs == expected set: {all_diffs == EXPECTED}")
    if all_diffs != EXPECTED:
        ok = False
        print(f"    missing: {sorted(EXPECTED - all_diffs)}")
        print(f"    extra:   {sorted(all_diffs - EXPECTED)}")
    print(f"(2) byte-check: stripped cards byte-identical (bad)={byte_same_unexpected}; "
          f"unstripped cards byte-differ (bad)={byte_diff_unexpected}")
    if byte_same_unexpected or byte_diff_unexpected:
        ok = False

    print(f"(3) face-field hash mismatches: {len(face_mismatch)} {face_mismatch}")
    if face_mismatch:
        ok = False

    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
