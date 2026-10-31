import json, pathlib, collections
# §1 编码表（主码, 次码列表）——与 DIAG-H26.md §1 逐例一致，TIM 次/主带级别后缀
CODE = {
 "DS-031": ("E5-CLAIM", ["E5-TIM-LIGHT"]),
 "DS-032": ("E5-CLAIM", ["E5-TIM-LIGHT"]),
 "DS-033": ("E5-DIR", ["E4"]),
 "DS-034": ("E4", ["E5-CLAIM", "E5-TIM-LIGHT"]),
 "DS-035": ("E5-DIR", ["E4"]),
 "DS-036": ("E5-DIR", ["E4", "E5-TIM-SUB"]),
 "DS-037": ("E5-CLAIM", ["E5-TIM-LIGHT"]),
 "DS-038": ("E5-CLAIM", ["E5-TIM-LIGHT"]),
 "DS-039": ("E4", ["E5-CLAIM"]),
 "GSZ-069": ("E5-OMIT", ["E5-TIM-LIGHT"]),
 "GSZ-074": ("E5-CLAIM", ["E5-TIM-SUB"]),
 "GSZ-075": ("E5-CLAIM", ["E5-TIM-LIGHT"]),
 "GSZ-077": ("E5-TIM-SUB", []),
 "GSZ-078": ("E5-CLAIM", ["E5-TIM-LIGHT"]),
 "QM-034": ("E5-CLAIM", []),
 "QM-035": ("E5-CLAIM", []),
 "QM-036": ("E5-DIR", ["E5-TIM-SUB"]),
 "QM-037": ("E5-TIM-SUB", ["E5-CLAIM"]),
 "QM-038": ("E5-TIM-SUB", ["E5-CLAIM"]),
 "QM-039": ("E5-DIR", ["E5-TIM-SUB"]),
 "QM-040": ("E5-TIM-SUB", ["E5-CLAIM"]),
 "QM-042": ("E5-DIR", ["E5-TIM-SUB"]),
 "QM-043": ("E5-DIR", ["E5-TIM-LIGHT"]),
 "WHY-004": ("E5-OMIT", []),
 "WHY-005": ("E5-DIR", ["E4"]),
 "WHY-006": ("E5-CLAIM", ["E5-TIM-SUB"]),
 "WHY-007": ("E5-CLAIM", ["E5-TIM-LIGHT"]),
}
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
final = json.loads((base/"runs/round82/acceptance/judging/final-scores-h26.json").read_text())
assert set(CODE) == set(final["per_case"]), "id set mismatch"
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
# section-9 execution-form recount from basis texts
chg=trig=restore=0
for cid in CODE:
    pred=json.loads((base/f"runs/round82/acceptance/predictions/{cid}.json").read_text())
    b=pred["basis"]
    assert ("方向未变更" in b) or ("变更事件：无" in b), cid
print("SEC9 recount: changed=0 triggered=0 restored=0 (27/27 basis carry no-change marks)")
print("QM direction<1.75:", final["qimen_direction_attached_read"]["count_direction_mean_below_1p75"], "/", final["qimen_direction_attached_read"]["n_qimen"])
print("TOTAL pair diff:", final["main_caliber_low27"]["pair_diff"])
