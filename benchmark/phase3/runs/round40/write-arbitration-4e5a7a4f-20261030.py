import json, pathlib
out = pathlib.Path.home() / "workspace/divination/benchmark/phase3/runs/round40/judging/arbitration-scores.jsonl"
row = {
    "anon_id": "P3-4e5a7a4f",
    "direction": 2.0,
    "claims": 1.0,
    "timing": 1.0,
    "total": 4.0,
    "reason": "终局方向正向吻合：预测贵可成，后果甲午榜中式，终局为成。claims逐条核验prediction_text全文：贵可成、官化父母主功名文凭落实两断为中式所印证；可入仕得贵仅由中式间接支持、结局未载实际入仕，等级中上非极贵与文书有耗量级压制均未被结局记载，故不得满分，记1.0。timing：预测有应期，主坐标卯月（窗口寅卯月内，月档）；结局仅记辛卯年失利与甲午年中式的年份，无月份可与卯月坐标对核，结局无可核时点，依特殊口径记1。"
}
assert row["total"] == row["direction"] + row["claims"] + row["timing"]
out.write_text(json.dumps(row, ensure_ascii=False) + "\n", encoding="utf-8")
print(out.read_text(encoding="utf-8"))
