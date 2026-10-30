#!/usr/bin/env python3
"""R51 arbitration scores (independent arbitrator). Writes arbitration-scores.jsonl."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT = BASE / "judging" / "arbitration-scores.jsonl"
DISPUTES = BASE / "judging" / "disputes.json"

SCORES = [
    {
        "anon_id": "P3-2e6e0cf9",
        "direction": 0,
        "claims": 0.5,
        "timing": 0.5,
        "total": 1.0,
        "pass": False,
        "reason": "结局本日巳时已还一半、乙酉日巳时还清另一半，与预测『今日无人还银、今日不得、非今日』终局方向正相反，direction=0；核心断语今日无人还/今日不得被证伪，仅乙酉日清偿与『须待酉金出空填实之后』的酉条件部分相合，claims=0.5；主时点『非今日』错误，酉日仅对应最后清偿而非预测所报主坐标（且明言不另报远期主坐标、另论），timing=0.5。",
    },
    {
        "anon_id": "P3-62b26d9f",
        "direction": 2,
        "claims": 1.5,
        "timing": 1,
        "total": 4.5,
        "pass": True,
        "reason": "结局『败血三日后复完胎』即出血之惊后胎儿复完好，与预测『胎安、能保、不安为虚惊』终局方向完全吻合，direction=2；胎安能保与惊后消解两条主断语被印证，但巳日之惊的具体时点/形态未被结局记载、亥日落定亦未被印证，未被记载的子断语不给满分，claims=1.5；三日后在本旬窗口内，窗口命中，但主坐标亥日并非三日后之日，主坐标未中，timing=1。",
    },
    {
        "anon_id": "P3-ac60d103",
        "direction": 1,
        "claims": 1,
        "timing": 1,
        "total": 3.0,
        "pass": False,
        "reason": "结局『后擢齐地分野』证实擢升，升的事件成立，但齐地为东方/东北之地，与预测『升往北方』的纯北向仅部分相合，direction=1；断语中擢升被印证、北向仅部分印证，文书随官北行与资费迟备均未被结局记载、不得给满分，claims=1；结局无可核时点（仅言『后』，无月日可核预测的巳月主坐标），timing=1。",
    },
    {
        "anon_id": "P3-b2f5e814",
        "direction": 0,
        "claims": 0,
        "timing": 0,
        "total": 0.0,
        "pass": False,
        "reason": "结局『後照此行，予目其平安一十七載』即照此入宅后亲历十七载平安，与预测『择此日入宅有碍父母、不宜用、入住后易不安/病扰』终局方向正相反，direction=0；有碍父母、不宜用、易不安/病扰诸断语均被十七载平安证伪，claims=0；预测子月内卯日碍象显形在结局十七载平安的时段内从未显形，应期未中，timing=0。",
    },
]

ALLOWED = {0, 0.5, 1, 1.5, 2}

def main():
    disputes = json.loads(DISPUTES.read_text(encoding="utf-8"))
    dispute_anons = {d["anon_id"] for d in disputes}
    assert len(SCORES) == 4, f"row count {len(SCORES)} != 4"
    assert {s["anon_id"] for s in SCORES} == dispute_anons, "anon set mismatch vs disputes.json"
    for s in SCORES:
        for k in ("direction", "claims", "timing"):
            assert s[k] in ALLOWED, f"{s['anon_id']} {k}={s[k]} not in allowed set"
        assert s["total"] == s["direction"] + s["claims"] + s["timing"], f"{s['anon_id']} total mismatch"
        assert s["pass"] == (s["total"] >= 4), f"{s['anon_id']} pass mismatch"
    with OUT.open("w", encoding="utf-8") as f:
        for s in SCORES:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    # re-read self-check
    lines = OUT.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 4
    for line in lines:
        row = json.loads(line)
        assert row["total"] == row["direction"] + row["claims"] + row["timing"]
        assert row["pass"] == (row["total"] >= 4)
    print(f"wrote {OUT} rows={len(lines)}")

if __name__ == "__main__":
    main()
