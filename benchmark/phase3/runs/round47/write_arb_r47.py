import json
from pathlib import Path

base = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round47")
packet_path = base / "judging" / "arbitration-packet.json"
out_path = base / "judging" / "arbitration-scores.jsonl"

packet = json.loads(packet_path.read_text(encoding="utf-8"))
packet_anons = {row["anon_id"] for row in packet}

rows = [
    {
        "anon_id": "P3-7f4dd90e",
        "direction": 1.0,
        "claims": 1.0,
        "timing": 1.0,
        "total": 3.0,
        "pass": False,
        "reason": "方向部分合：官非牵连、近事偏凶与结局以失城逮问合，但结局为荆州知府、甲戌进士，与不是显贵、奔走藏匿不合或未载；claims：官非与偏凶被逮问印证，身份与藏匿等子断语未被结局印证或相悖，不得满分；timing记1，结局无可核时点，未载子日可核时点。",
    },
    {
        "anon_id": "P3-7ffaf8c7",
        "direction": 0.0,
        "claims": 0.0,
        "timing": 0.5,
        "total": 0.5,
        "pass": False,
        "reason": "方向全反：断开铺可开、有利可图而利薄迟，结局为夥計盜盡、分文不復；claims：有利可图、利薄迟及见利落定均未被印证且被盜盡结局否定；timing：主坐标亥月见利未应，八月盜盡仅落在寅至亥宽窗内，故低分。",
    },
]

assert len(rows) == 2, f"row count {len(rows)} != 2"
assert {r["anon_id"] for r in rows} == packet_anons, "anon set mismatch with arbitration-packet.json"
for r in rows:
    assert r["total"] == r["direction"] + r["claims"] + r["timing"], f"total mismatch {r['anon_id']}"
    assert r["pass"] == (r["total"] >= 4), f"pass mismatch {r['anon_id']}"

with out_path.open("w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

# verify written file
lines = [ln for ln in out_path.read_text(encoding="utf-8").splitlines() if ln.strip()]
assert len(lines) == 2
for ln in lines:
    obj = json.loads(ln)
    assert obj["total"] == obj["direction"] + obj["claims"] + obj["timing"]
    assert obj["pass"] == (obj["total"] >= 4)
print("OK", len(lines))
for ln in lines:
    print(ln)
