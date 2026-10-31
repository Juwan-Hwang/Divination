import json
from pathlib import Path

base = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round88")
out = base / "judging" / "arbitration-scores.jsonl"

rows = [
    {
        "case_id": "BQ-001",
        "direction": 0.0,
        "claims": 0.5,
        "timing": 1.0,
        "total": 1.5,
        "pass": False,
        "reason": "结局仅为求卜者当场自述父卧疾三年、昨日气尽后复苏，未记载父辞世这一终局，预测的死亡方向未得印证，direction 0；claims 仅卧疾三年与气尽复苏部分与自述吻合，核心断语数日内辞世、不出本月、庚辛日危期均未被结局记载，仅 0.5；结局无可核时点，timing 按特殊口径记 1。",
    },
    {
        "case_id": "YM-030",
        "direction": 2.0,
        "claims": 1.5,
        "timing": 0.0,
        "total": 3.5,
        "pass": False,
        "reason": "结局败血三日后复完胎，胎儿保全，终局方向与胎安完全吻合，direction 2；claims 中小惊无碍、胎终保全获印证，但胎稳安位的全程状态未被结局完整记载且中途有败血过程，记 1.5；预测应期主坐标为亥月，结局为三日后复完，不命中，timing 0。",
    },
]

lines = [json.dumps(r, ensure_ascii=False) for r in rows]
out.write_text("\n".join(lines) + "\n", encoding="utf-8")

# Post-write assertions
read_back = out.read_text(encoding="utf-8").splitlines()
assert len(read_back) == 2, f"line count {len(read_back)}"
seen = set()
for line in read_back:
    obj = json.loads(line)
    assert set(obj.keys()) == {"case_id", "direction", "claims", "timing", "total", "pass", "reason"}, obj.keys()
    seen.add(obj["case_id"])
    for k in ("direction", "claims", "timing"):
        v = obj[k]
        assert 0 <= v <= 2 and (v * 2) == int(v * 2), (k, v)
    assert obj["total"] == obj["direction"] + obj["claims"] + obj["timing"], obj
    assert obj["pass"] == (obj["total"] >= 4), obj
assert seen == {"BQ-001", "YM-030"}, seen
print(f"OK rows=2 bytes={out.stat().st_size}")
