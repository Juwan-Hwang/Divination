# -*- coding: utf-8 -*-
"""Round56 judgeX block1 scoring.
Finding: every source row's `prediction` is {direction, assertions, timing, summary}
all null and there is no prediction_text field. With no assertion to compare
against outcome_record, no item can earn credit -> all scores 0.
Special notes flag rows whose outcome is a bare affirmation / embedded in the
judgment passage, and rows whose carry_note states the outcome covers only a
partial facet."""
import json

SRC = "/home/hatch/workspace/divination/benchmark/phase3/runs/round56/judging/judgeX-block1.jsonl"
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round56/judging/scoresX-block1.jsonl"

BASE_NOTE = "预测各字段均为null、无任何断语可与结局核对，一致性无项可成立。自报：预测侧内容缺失，prediction全字段为null。"

# outcome is only a bare affirmation or is recorded inside the judgment passage itself
EMBEDDED = {
    "P3-005280bd",  # 'Confirmed in the text: I judged that...' judgment quoted as outcome
    "P3-0c1f6b0c",  # 彼曰：果一一無錯 (bare affirmation)
    "P3-0dc01222",  # 后果然 (bare affirmation)
    "P3-10570ec9",  # 'Recorded within the judgment passage itself'
    "P3-2af3591e",  # 'Confirmed in the text' within judgment narrative
    "P3-37679a8a",  # 已而果然 + 七月死期为本课结局
}
EMBEDDED_NOTE = "预测各字段均为null、无任何断语可与结局核对，一致性无项可成立。自报：预测侧内容缺失，且结局为断语式/嵌于断语段落、与预测不可分离。"

# carry_note states outcome covers only a partial facet / asked facet unrecorded
PARTIAL = {
    "P3-0605ecfd", "P3-08496a2f", "P3-0866c552", "P3-23677a67",
    "P3-2ba0d2f3", "P3-31e65266", "P3-368c3ee9",
}
PARTIAL_NOTE = "预测各字段均为null、无任何断语可与结局核对，一致性无项可成立。自报：预测侧内容缺失，且结局仅载部分断面、所问面无独立记载。"

rows = []
with open(SRC, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            rows.append(json.loads(line))

out_lines = []
for r in rows:
    aid = r["anon_id"]
    if aid in EMBEDDED:
        note = EMBEDDED_NOTE
    elif aid in PARTIAL:
        note = PARTIAL_NOTE
    else:
        note = BASE_NOTE
    out_lines.append(json.dumps({"anon_id": aid, "score": 0, "note": note}, ensure_ascii=False))

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines) + "\n")

print(f"wrote {len(out_lines)} lines to {OUT}")
