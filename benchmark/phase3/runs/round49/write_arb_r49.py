import json, pathlib

out = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round49/judging/arbitration-scores.jsonl")
row = {
    "anon_id": "P3-2ef6aab6",
    "direction": 0.5,
    "claims": 0.5,
    "timing": 0,
    "total": 1.0,
    "pass": False,
    "reason": "方向：预测断母不能来、此行作罢，结局为次年三月妹至，终局到来与作罢相反，仅本年及窗口内无人到与结局时间线部分相合，故0.5。断语逐条核验：不来作罢被实际到来推翻；纵有来信终以事阻未被结局记载；戌月只得确讯定不来或改期无期亦未被记载且与次年实际到来不合；仅窗口内不是人到一项与次年才到部分相合，故0.5。应期：预测本身有应期，主坐标取戌月且为定不来之期，结局时点为次年三月人到，时点与事件均不命中，故0。",
}
assert row["anon_id"] == "P3-2ef6aab6"
assert abs(row["total"] - (row["direction"] + row["claims"] + row["timing"])) < 1e-9
assert row["pass"] == (row["total"] >= 4)
out.write_text(json.dumps(row, ensure_ascii=False) + "\n", encoding="utf-8")

# 回读自验
lines = out.read_text(encoding="utf-8").strip().splitlines()
assert len(lines) == 1, f"expected 1 line, got {len(lines)}"
back = json.loads(lines[0])
assert back["anon_id"] == "P3-2ef6aab6"
assert abs(back["total"] - (back["direction"] + back["claims"] + back["timing"])) < 1e-9
assert back["pass"] == (back["total"] >= 4)
print("OK: 1 line, self-verified")
