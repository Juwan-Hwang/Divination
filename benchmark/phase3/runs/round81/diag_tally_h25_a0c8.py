import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
final=json.loads((base/"runs/round81/acceptance/judging/final-scores-h25.json").read_text())
# coding: case -> (main, [secondaries]) ; TIM main grades noted in main string
coding={
 "DS-025":("E5-CLAIM",["E5-TIM-LIGHT"]),
 "DS-026":("E5-DIR",["E4"]),
 "DS-027":("E5-DIR",["E4"]),
 "DS-028":("E5-CLAIM",["E5-TIM-LIGHT"]),
 "DS-029":("E4",["E5-CLAIM"]),
 "DS-030":("E4",["E5-CLAIM"]),
 "GSZ-049":("E5-OMIT",["E5-CLAIM","E5-TIM-SUB"]),
 "GSZ-050":("E5-DIR",["E5-TIM-SUB"]),
 "GSZ-052":("E5-CLAIM",["E5-TIM-LIGHT"]),
 "GSZ-053":("E5-CLAIM",["E5-OMIT"]),
 "GSZ-054":("E5-DIR",["E5-TIM-SUB"]),
 "GSZ-055":("E5-CLAIM",["E5-OMIT","E5-TIM-SUB"]),
 "GSZ-058":("E5-DIR",["E5-OMIT"]),
 "GSZ-059":("E5-CLAIM",["E5-OMIT"]),
 "GSZ-060":("E3-A",["E5-DIR"]),
 "GSZ-061":("E5-OMIT",["E5-CLAIM"]),
 "GSZ-068":("E5-DIR",["E5-CLAIM"]),
 "QM-027":("E5-DIR",["E5-TIM-SUB"]),
 "QM-028":("E5-TIM-ZERO",[]),
 "QM-029":("E5-OMIT",["E5-CLAIM"]),
 "QM-030":("E5-CLAIM",["E5-TIM-LIGHT"]),
 "QM-031":("E5-DIR",["E5-TIM-SUB"]),
 "QM-032":("E5-CLAIM",["E5-TIM-LIGHT"]),
 "QM-208":("E5-DIR",["E5-TIM-SUB"]),
 "QM-209":("E5-DIR",["E5-TIM-SUB"]),
 "QM-310":("E5-CLAIM",["E5-TIM-LIGHT"]),
 "QM-311":("E5-TIM-LIGHT",[]),
}
assert len(coding)==27 and set(coding)==set(final["per_case"])
from collections import Counter
main=Counter(v[0] for v in coding.values())
print("MAIN",dict(main),"sum",sum(main.values()))
e5={k:sum(1 for v in coding.values() if v[0]==f"E5-{k}" or v[0].startswith(f"E5-{k}-")) for k in ["DIR","TIM","CLAIM","OMIT"]}
print("E5 subclasses",e5,"E5total",sum(e5.values()))
tim_grades=Counter(v[0].split("-")[-1] for v in coding.values() if v[0].startswith("E5-TIM"))
print("TIM grades",dict(tim_grades))
sec=Counter(s for v in coding.values() for s in v[1])
print("SEC",dict(sec))
for seg,prefix,n in [("DS","DS-",6),("QM","QM-",10),("GSZ","GSZ-",11)]:
    c=Counter(v[0] for k,v in coding.items() if k.startswith(prefix))
    print(seg,dict(c), "diff", final["segments"][{'DS':'bazi_DS','QM':'qimen_QM','GSZ':'liuyao_GSZ'}[seg]]["pair_diff"])
e4ds=sum(1 for k,v in coding.items() if k.startswith("DS-") and v[0]=="E4")
print("E4 DS",e4ds,"/6")
e3a_involved=sum(1 for v in coding.values() if v[0]=="E3-A" or "E3-A" in v[1])
print("E3-A involved",e3a_involved)
qm_dir=final["qimen_direction_attached_read"]
print("QM dir<1.75",qm_dir["count_direction_mean_below_1p75"],"/",qm_dir["n_qimen"], qm_dir["per_case_direction_mean"])
print("overall",final["main_caliber_low27"])
