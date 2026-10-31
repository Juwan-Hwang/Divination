import json, pathlib
out = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round89/judging/arb-as303-scores.jsonl")
row = {
    "anon_id": "P3-2b8c6727",
    "direction": 0,
    "claims": 0,
    "timing": 0,
    "total": 0,
    "pass": False,
    "reason": "断语主报2024年6月18日前后三战爆发、由地缘突发触发并升级多国卷入，备位窗口6月下旬至8月；结局明载6月18日、7月26/28日、8月4/5日均无三战且至2026年10月亦未发生，终局方向完全相反、具体断语无一被印证、应期坐标全数落空，故三项均为0。"
}
out.write_text(json.dumps(row, ensure_ascii=False) + "\n", encoding="utf-8")
print(out.stat().st_size)
