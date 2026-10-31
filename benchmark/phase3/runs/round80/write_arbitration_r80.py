import json
from pathlib import Path

out_path = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round80/judging/arbitration-scores.jsonl")

# Arbitration for P3-18b0aba1 (BQ-001), based solely on arbitration packet
# (outcome_record + carry_note) and prediction_text reread via host-mapping.
# Sub-claim enumeration (non-timing claims in prediction_text):
#  (1) 父寿已尽、寿数将终
#  (2) 气绝复苏只是回光返照、此苏非愈
#  (3) 元气已泄、将在极短期内再绝而不起
#  (4) 附断: 兑/乾象链庚辛日金火相战之机理断语与「家人当预备后事」劝告
# Verification: outcome_record alone records the revival incident;
# carry_note states stripped_tail post-claim "更三日，当永去" is wholly
# confirmed by "果如言" -- counted as outcome verification material.
# Hence (1)(2)(3) are verified by the carried "永去" outcome (he did not
# recover and died permanently); (4) has no record in outcome, so claims
# cannot be full marks per frozen rubric. 3/4 verified -> claims 1.5.
# Direction: predicted death/negative matches carried "永去" -> 2.0.
# Timing: prediction has timing (window 3 days, main coordinate day 0/1);
# outcome has a verifiable time point via carry_note "更三日", so neither
# special rule (no verifiable point -> 1, no timing in prediction -> 0)
# applies. Window "三日内" touches the day-3 point, but main coordinate
# 当日/次日 mismatches "更三日" -> partial credit 1.0.

record = {
    "anon_id": "P3-18b0aba1",
    "direction": 2.0,
    "claims": 1.5,
    "timing": 1.0,
    "total": 4.5,
    "pass": True,
    "reason": "子断共4条编号核验:(1)父寿已尽寿数将终 (2)气绝复苏仅回光返照此苏非愈 (3)元气已泄极短期内再绝而不起 (4)兑乾象链庚辛金火相战机理及家人预备后事附断。carry_note载stripped_tail后断『更三日，当永去』以『果如言』总承应验，逐字计入结局核验:该承接证实永去，故(1)(2)(3)得印证、方向完全吻合; (4)结局无记载，依口径不得满分，claims按3/4印证计1.5。timing:预测有应期且承接给出可核时点『更三日』，两项特殊口径均不适用;预测窗口三日内触及三日点，但主坐标当日/次日与更三日不合，计1.0。",
}

# Validate before write
for k in ("direction", "claims", "timing"):
    v = record[k]
    assert 0 <= v <= 2, k
    assert (v * 2) == int(v * 2), f"{k} not 0.5 step"
assert record["total"] == record["direction"] + record["claims"] + record["timing"]
assert record["pass"] == (record["total"] >= 4)

out_path.write_text(json.dumps(record, ensure_ascii=False) + "\n", encoding="utf-8")

# Read back and assert
lines = out_path.read_text(encoding="utf-8").strip().splitlines()
assert len(lines) == 1, f"expected 1 line, got {len(lines)}"
obj = json.loads(lines[0])
for field in ("anon_id", "direction", "claims", "timing", "total", "pass", "reason"):
    assert field in obj, f"missing {field}"
assert obj["anon_id"] == "P3-18b0aba1"
for k in ("direction", "claims", "timing"):
    v = obj[k]
    assert 0 <= v <= 2 and (v * 2) == int(v * 2), k
assert obj["total"] == obj["direction"] + obj["claims"] + obj["timing"], "total mismatch"
assert obj["pass"] == (obj["total"] >= 4), "pass mismatch"
print("OK", json.dumps(obj, ensure_ascii=False))
