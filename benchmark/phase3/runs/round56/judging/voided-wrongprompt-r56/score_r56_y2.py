#!/usr/bin/env python3
"""Round56 judgeY block2 scoring.
Finding: every row in judgeY-block2.jsonl has prediction =
{direction: None, assertions: None, timing: None, summary: None}
and no prediction_text field. With no prediction assertions at all,
there is nothing to match against the outcome: direction, specific
claims and timing are all unreported, and unreported items earn no
points per the frozen rubric. Hence score 0 for every row, with a
self-report note on the missing prediction.
"""
import json

SRC = "/home/hatch/workspace/divination/benchmark/phase3/runs/round56/judging/judgeY-block2.jsonl"
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round56/judging/scoresY-block2.jsonl"

NOTE = "无预测断语可核对，方向、具体项与应期均未报，无命中项。自报：prediction四字段全null且无prediction_text，预测缺失、与结局不可分离核对"

SCORES = [
    ("P3-4030e45c", 0),
    ("P3-4083843d", 0),
    ("P3-4183d668", 0),
    ("P3-418a1c12", 0),
    ("P3-41d3c809", 0),
    ("P3-4293712e", 0),
    ("P3-44d20875", 0),
    ("P3-4565da91", 0),
    ("P3-45677bcc", 0),
    ("P3-466185ee", 0),
    ("P3-4bbe44e3", 0),
    ("P3-4caab6d0", 0),
    ("P3-4caf2a95", 0),
    ("P3-4ce93213", 0),
    ("P3-4d26187a", 0),
    ("P3-4e0a50c8", 0),
    ("P3-4e31b653", 0),
    ("P3-4e6b207f", 0),
    ("P3-4f5b66e5", 0),
    ("P3-4fae0a80", 0),
    ("P3-4fe333ba", 0),
    ("P3-5046f8ae", 0),
    ("P3-51121408", 0),
    ("P3-51e36ff0", 0),
    ("P3-5209accf", 0),
    ("P3-52ae805b", 0),
    ("P3-52b0df03", 0),
    ("P3-52ca4119", 0),
    ("P3-539ceaae", 0),
    ("P3-53cf84c4", 0),
    ("P3-542a6189", 0),
    ("P3-548911e7", 0),
    ("P3-56e04887", 0),
    ("P3-56e99751", 0),
    ("P3-579ae347", 0),
    ("P3-57c4cf60", 0),
    ("P3-58a742fe", 0),
    ("P3-58fbf807", 0),
    ("P3-595d3674", 0),
    ("P3-5a727b85", 0),
    ("P3-5a852ae0", 0),
    ("P3-5ab76249", 0),
    ("P3-5ac3602c", 0),
    ("P3-5bd8b550", 0),
    ("P3-5be10ce5", 0),
    ("P3-5c3c7922", 0),
    ("P3-5ce7625e", 0),
    ("P3-5d2a95a6", 0),
    ("P3-5d3a320a", 0),
    ("P3-5dbd7a9a", 0),
    ("P3-5e21f899", 0),
    ("P3-5e5c612d", 0),
    ("P3-5f1ed40e", 0),
    ("P3-60117bfc", 0),
    ("P3-60262913", 0),
    ("P3-6026c2c6", 0),
    ("P3-603f165f", 0),
    ("P3-61462599", 0),
    ("P3-61d345b1", 0),
    ("P3-61df5d3a", 0),
    ("P3-62afddf9", 0),
    ("P3-62fbea30", 0),
    ("P3-62ffc051", 0),
    ("P3-640d3b37", 0),
    ("P3-66d5ea37", 0),
    ("P3-66fe9d26", 0),
    ("P3-6724cf4a", 0),
    ("P3-67306c84", 0),
    ("P3-67a36944", 0),
    ("P3-69081cd9", 0),
    ("P3-698c4342", 0),
    ("P3-6a732a09", 0),
    ("P3-6a9283fd", 0),
    ("P3-6aec6546", 0),
    ("P3-6c824963", 0),
    ("P3-6e1e61f8", 0),
    ("P3-6e9ae18d", 0),
    ("P3-6ebcf231", 0),
    ("P3-6ecb1f08", 0),
    ("P3-6f25137d", 0),
    ("P3-6f895da7", 0),
    ("P3-7012f0da", 0),
    ("P3-7025e52a", 0),
    ("P3-708adf24", 0),
    ("P3-71107de7", 0),
    ("P3-7215a592", 0),
    ("P3-724b78f0", 0),
    ("P3-72ab018b", 0),
    ("P3-72b027b9", 0),
    ("P3-730e1b13", 0),
    ("P3-7313c230", 0),
    ("P3-74db6b68", 0),
    ("P3-75f951b6", 0),
    ("P3-76211cee", 0),
    ("P3-765ccbb2", 0),
    ("P3-7721c2f6", 0),
    ("P3-778135e7", 0),
    ("P3-77e15773", 0),
    ("P3-77f49ae6", 0),
    ("P3-780d7e50", 0),
    ("P3-7829d50e", 0),
    ("P3-7902add6", 0),
    ("P3-797e345e", 0),
    ("P3-7a9127c0", 0),
    ("P3-7b3fe3d9", 0),
    ("P3-7b89bfc2", 0),
    ("P3-7b9ee6bd", 0),
    ("P3-7be9c32e", 0),
    ("P3-7c715db8", 0),
    ("P3-7d992d25", 0),
    ("P3-7e1b304e", 0),
    ("P3-7f049bb1", 0),
    ("P3-7f343a11", 0),
    ("P3-7f6634a2", 0),
    ("P3-7ff47321", 0),
    ("P3-80702b68", 0),
    ("P3-827c12d0", 0),
    ("P3-833061e1", 0),
    ("P3-83cd0e11", 0),
    ("P3-83cf3319", 0),
    ("P3-84d1225b", 0),
    ("P3-84f79ebc", 0),
]

def main():
    with open(SRC, encoding="utf-8") as f:
        src_ids = [json.loads(line)["anon_id"] for line in f if line.strip()]
    score_ids = [a for a, _ in SCORES]
    assert src_ids == score_ids, "anon_id order/list mismatch with source"
    with open(OUT, "w", encoding="utf-8") as f:
        for anon_id, score in SCORES:
            f.write(json.dumps({"anon_id": anon_id, "score": score, "note": NOTE}, ensure_ascii=False) + "\n")
    print(f"wrote {len(SCORES)} rows to {OUT}")

if __name__ == "__main__":
    main()
