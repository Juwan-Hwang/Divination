import json, pathlib, collections
# §1 编码表（主码, 次码列表）——与 DIAG-H27.md §1 逐例一致，TIM 带级别后缀
CODE = {
 "DS-040": ("E5-DIR", ["E4"]),
 "DS-041": ("E5-CLAIM", ["E5-TIM-LIGHT"]),
 "DS-042": ("E5-CLAIM", ["E5-TIM-LIGHT"]),
 "DS-043": ("E5-CLAIM", ["E5-TIM-LIGHT"]),
 "DS-044": ("E5-DIR", ["E4"]),
 "DS-045": ("E5-CLAIM", ["E5-TIM-LIGHT"]),
 "DS-046": ("E4", ["E5-CLAIM"]),
 "DS-048": ("E5-TIM-SUB", ["E5-CLAIM"]),
 "DS-049": ("E5-OMIT", ["E5-TIM-LIGHT"]),
 "GSZ-079": ("E5-DIR", ["E4", "E5-TIM-LIGHT"]),
 "GSZ-081": ("E5-DIR", ["E4", "E5-TIM-LIGHT"]),
 "GSZ-084": ("E5-OMIT", ["E5-CLAIM", "E5-TIM-LIGHT"]),
 "GSZ-086": ("E5-CLAIM", []),
 "GSZ-088": ("E5-DIR", ["E4"]),
 "QM-044": ("E5-TIM-SUB", ["E5-CLAIM"]),
 "QM-045": ("E5-CLAIM", ["E5-TIM-LIGHT"]),
 "QM-046": ("E5-CLAIM", ["E5-TIM-LIGHT"]),
 "QM-047": ("E5-CLAIM", ["E5-TIM-SUB"]),
 "QM-048": ("E5-CLAIM", ["E5-TIM-SUB"]),
 "QM-049": ("E5-CLAIM", ["E5-TIM-LIGHT"]),
 "QM-052": ("E5-DIR", ["E4", "E5-TIM-SUB"]),
 "QM-055": ("E5-CLAIM", ["E5-TIM-LIGHT"]),
 "QM-058": ("E5-CLAIM", ["E5-TIM-LIGHT"]),
 "WHY-008": ("E5-OMIT", []),
 "WHY-009": ("E4", ["E5-CLAIM"]),
 "WHY-010": ("E5-DIR", ["E4"]),
 "WHY-011": ("E5-CLAIM", ["E4", "E5-TIM-LIGHT"]),
}
# 第十节执行形态（逐例回读 predictions basis 之 R82 段逐项指名断项计数）
# scanned=受扫查指名断项数; bound=其中有限定信号收束项数; unacted=其中无限定信号未动作项数
SEC10 = {
 "DS-040": (2,2,0), "DS-041": (2,2,0), "DS-042": (2,2,0), "DS-043": (2,2,0),
 "DS-044": (2,2,0), "DS-045": (2,2,0), "DS-046": (2,2,0), "DS-048": (2,2,0),
 "DS-049": (2,1,1),
 "GSZ-079": (1,1,0), "GSZ-081": (1,0,1), "GSZ-084": (1,1,0), "GSZ-086": (1,1,0), "GSZ-088": (2,2,0),
 "QM-044": (2,1,1), "QM-045": (2,1,1), "QM-046": (1,1,0), "QM-047": (2,1,1),
 "QM-048": (1,1,0), "QM-049": (1,1,0), "QM-052": (2,1,1), "QM-055": (1,1,0), "QM-058": (2,1,1),
 "WHY-008": (2,1,1), "WHY-009": (1,1,0), "WHY-010": (1,1,0), "WHY-011": (1,1,0),
}
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
final = json.loads((base/"runs/round83/acceptance/judging/final-scores-h27.json").read_text())
assert set(CODE) == set(final["per_case"]) and len(CODE) == 27, "id set mismatch"
assert set(SEC10) == set(CODE), "sec10 id set mismatch"
for cid,(s,b,u) in SEC10.items():
    assert s == b + u, cid
def seg(cid):
    return cid.split("-")[0]
main = collections.Counter(v[0] for v in CODE.values())
print("MAIN:", dict(main), "sum", sum(main.values()))
dir_main = main["E5-DIR"]; claim_main = main["E5-CLAIM"]; omit_main = main["E5-OMIT"]; e4_main = main["E4"]
tim_sub_main = main["E5-TIM-SUB"]; tim_light_main = main.get("E5-TIM-LIGHT",0); tim_zero_main = main.get("E5-TIM-ZERO",0)
print(f"DIR={dir_main} CLAIM={claim_main} OMIT={omit_main} E4={e4_main} TIM_sub_main={tim_sub_main} TIM_light_main={tim_light_main} TIM_zero_main={tim_zero_main}")
print(f"TIM+CLAIM substantive (main) = {tim_sub_main + claim_main}")
sec = collections.Counter(s for v in CODE.values() for s in v[1])
print("SECONDARY:", dict(sec))
for s in ["DS","QM","GSZ","WHY"]:
    ids=[c for c in CODE if seg(c)==s]
    mc=collections.Counter(CODE[c][0] for c in ids)
    segkey={"DS":"bazi_DS","QM":"qimen_QM","GSZ":"liuyao_GSZ","WHY":"liuyao_WHY"}[s]
    print(s, "n=",len(ids), "diff=", final["segments"][segkey]["pair_diff"], dict(mc))
tot_items = sum(v[0] for v in SEC10.values())
bound_cases = sum(1 for v in SEC10.values() if v[1] > 0)
all_unacted_cases = [c for c,v in SEC10.items() if v[1] == 0 and v[2] > 0]
any_unacted_cases = [c for c,v in SEC10.items() if v[2] > 0]
print(f"SEC10: scanned_items={tot_items} bound_cases={bound_cases} all_unacted_cases={all_unacted_cases} any_unacted_cases={len(any_unacted_cases)} {any_unacted_cases}")
print("QM direction<1.75:", final["qimen_direction_attached_read"]["count_direction_mean_below_1p75"], "/", final["qimen_direction_attached_read"]["n_qimen"])
print("TOTAL pair diff:", final["main_caliber_low27"]["pair_diff"])
print("IN: 0/27 (per-card anchor check, see DIAG-H27 §0/§5)")
