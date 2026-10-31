# -*- coding: utf-8 -*-
"""R84 judgeX-block2 评分写盘脚本（X2 席）。

评审依据（本席逐条读完 judgeX-block2.jsonl 全 122 条后定）：
本包内每条 prediction 的 direction/assertions/timing/summary 四字段
全为 null，且包内无题面、无预测文本。在主持纪律下不得回读
host-mapping / predictions 原件，故无方向、无具体断语、无应期可核：
direction=0, claims=0；按冻结评审提示特殊口径「预测断语本身无应期
→ timing 记 0 并注明」，timing=0。total=0，pass=false。
每条 reason 均带异常旗标说明，供主持复核数据包问题。
"""
import json
import os

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round84"
SRC = os.path.join(BASE, "judging", "judgeX-block2.jsonl")
OUT = os.path.join(BASE, "judging", "judgeX-block2-scores.jsonl")

REASON = (
    "异常旗标：本包prediction四字段(direction/assertions/timing/summary)"
    "全为null且无题面与预测文本，无方向、断语、应期可核，direction与claims记0；"
    "预测断语本身无应期，timing记0"
)

SEGMENT_SIZES = [25, 25, 25, 25, 22]


def main():
    with open(SRC, encoding="utf-8") as f:
        rows = [json.loads(line) for line in f if line.strip()]
    assert len(rows) == 122, f"input count {len(rows)} != 122"
    ids = [r["anon_id"] for r in rows]
    assert len(set(ids)) == 122, "anon_id not unique"
    for r in rows:
        pred = r["prediction"]
        assert all(v is None for v in pred.values()), (
            f"non-null prediction found, uniform ruling invalid: {r['anon_id']}"
        )
    assert sum(SEGMENT_SIZES) == 122

    # 无覆写：输出必须不存在
    assert not os.path.exists(OUT), "output already exists, refuse to overwrite"
    with open(OUT, "x", encoding="utf-8"):
        pass

    written = 0
    pos = 0
    for seg_no, size in enumerate(SEGMENT_SIZES, start=1):
        seg_ids = ids[pos:pos + size]
        assert len(seg_ids) == size
        with open(OUT, "a", encoding="utf-8") as f:
            for anon_id in seg_ids:
                rec = {
                    "anon_id": anon_id,
                    "direction": 0,
                    "claims": 0,
                    "timing": 0,
                    "total": 0,
                    "pass": False,
                    "reason": REASON,
                }
                assert rec["total"] == rec["direction"] + rec["claims"] + rec["timing"]
                assert rec["pass"] == (rec["total"] >= 4)
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        pos += size
        written += size
        # 逐段断言：回读核对累计条数与本段末尾 id
        with open(OUT, encoding="utf-8") as f:
            out_lines = [line for line in f if line.strip()]
        assert len(out_lines) == written, (
            f"segment {seg_no}: on-disk {len(out_lines)} != written {written}"
        )
        last = json.loads(out_lines[-1])
        assert last["anon_id"] == seg_ids[-1], f"segment {seg_no} tail id mismatch"
        print(f"segment {seg_no}: +{size} cumulative={written} tail={seg_ids[-1]}")

    assert written == 122 and pos == 122
    print("DONE written=122")


if __name__ == "__main__":
    main()
