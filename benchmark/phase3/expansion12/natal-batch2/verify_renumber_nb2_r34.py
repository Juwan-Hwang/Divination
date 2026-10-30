#!/usr/bin/env python3
"""R34 §6.② 重编独立复验（只读，不改任何文件）。

1) 两文件记录数、id 唯一性、新 id 集合与映射表一致、无 QM-/MP- 残留；
2) 除 id 外零变化证明：将当前文件逐行行首 id 按反向映射换回旧号后，
   SHA-256 须与 RENUMBER-MAP.json 记录的改前哈希逐字相等——反向替换
   只触行首 id 区间，能逐字还原改前文件即证明差异仅在 id；
3) QL-001…008 对齐：只读 holdout12/test_gold.jsonl 的 QL 行 source_id，
   逐条须满足 映射[source_id] == 该行 id；并核金标哈希仍为封存值。
"""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]  # ~/workspace/divination
HOLDOUT_GOLD = ROOT / "benchmark/phase3/holdout12/test_gold.jsonl"
HOLDOUT_SEALED_SHA = "490679552b5bcbff08df369046f977750900f7396857714a51aa438e16b30c90"
LINE_RE = re.compile(r'^\{"id": "((?:QL|PU)-\d{3})", ')

failures = []


def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")
    if not ok:
        failures.append(name)


def main() -> int:
    rmap = json.loads((HERE / "RENUMBER-MAP.json").read_text(encoding="utf-8"))
    fwd = {**rmap["mapping_QM_to_QL"], **rmap["mapping_MP_to_PU"]}
    rev = {v: k for k, v in fwd.items()}
    check("映射表条数", len(fwd) == 92 and len(rev) == 92, f"fwd={len(fwd)}")

    for fn in ["cases.jsonl", "cases-reviewed.jsonl"]:
        raw = (HERE / fn).read_bytes()
        meta = rmap["files"][fn]
        check(f"{fn} 改后哈希与映射记录一致",
              hashlib.sha256(raw).hexdigest() == meta["sha256_after"])
        text = raw.decode("utf-8")
        lines = [l for l in text.split("\n") if l.strip()]
        recs = [json.loads(l) for l in lines]
        ids = [r["id"] for r in recs]
        check(f"{fn} 记录数", len(recs) == 92 == meta["records"], f"n={len(recs)}")
        check(f"{fn} id 全唯一", len(set(ids)) == 92)
        check(f"{fn} id 集合==映射新号集合", set(ids) == set(rev))
        check(f"{fn} 无 QM-/MP- id 残留",
              not any(i.startswith(("QM-", "MP-")) for i in ids))
        restored = []
        for line in text.split("\n"):
            if not line.strip():
                restored.append(line)
                continue
            m = LINE_RE.match(line)
            assert m, f"{fn}: 行首 id 模式不符"
            restored.append(LINE_RE.sub('{"id": "' + rev[m.group(1)] + '", ', line, count=1))
        restored_raw = "\n".join(restored).encode("utf-8")
        check(f"{fn} 反向映射回算哈希==改前哈希（除 id 外零变化）",
              hashlib.sha256(restored_raw).hexdigest() == meta["sha256_before"])

    gold_raw = HOLDOUT_GOLD.read_bytes()
    check("holdout12 金标哈希仍为封存值（未被触碰）",
          hashlib.sha256(gold_raw).hexdigest() == HOLDOUT_SEALED_SHA)
    gold = [json.loads(l) for l in gold_raw.decode("utf-8").split("\n") if l.strip()]
    ql_rows = [r for r in gold if str(r.get("id", "")).startswith("QL-")]
    check("holdout12 QL 行数", len(ql_rows) == 8, f"n={len(ql_rows)}")
    for r in sorted(ql_rows, key=lambda x: x["id"]):
        check(f"对齐 {r['id']}: source_id={r.get('source_id')} 经映射→{fwd.get(r.get('source_id'))}",
              fwd.get(r.get("source_id")) == r["id"])

    print("RESULT:", "ALL PASS" if not failures else f"FAILURES: {failures}")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
