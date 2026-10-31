import json, os
base="/home/hatch/workspace/divination/benchmark/phase3"
ids=["BY-017","BY-018","BY-020","BY-021","CYJ-006","CYJ-007","CYJ-008","CYJ-009","CYJ-010","DA-038","DA-041","DA-042","DA-044","DA-046","GSZ-101","GSZ-103","GSZ-104","GSZ-105","WHY-025","WHY-026","WHY-027","WHY-028","WHY-031","WHY-032","WHY-033","WHY-034","WHY-035","WHY-036"]
with open(f"{base}/runs/round87/acceptance/judging/final-scores-h30.json",encoding="utf-8") as f: final=json.load(f)
gold={}
with open(f"{base}/holdout30/test_gold.jsonl",encoding="utf-8") as f:
    for line in f:
        if line.strip():
            o=json.loads(line); gold[o.get("id")]=o
assert set(gold)==set(ids)
with open(f"{base}/runs/round87/acceptance/judging/host-mapping.json",encoding="utf-8") as f: hm=json.load(f)
invO={v:k for k,v in hm["ours"].items()}; invM={v:k for k,v in hm["master"].items()}
def load(p):
    d={}
    with open(p,encoding="utf-8") as f:
        for line in f:
            if line.strip():
                o=json.loads(line); d[o["anon_id"]]=o
    return d
jO1=load(f"{base}/runs/round87/acceptance/judging/judgeO1.jsonl"); jO2=load(f"{base}/runs/round87/acceptance/judging/judgeO2.jsonl")
jM1=load(f"{base}/runs/round87/acceptance/judging/judgeM1.jsonl"); jM2=load(f"{base}/runs/round87/acceptance/judging/judgeM2.jsonl")
out=[]
work=[]
for id_ in ids:
    with open(f"{base}/runs/round87/acceptance/predictions/{id_}.json",encoding="utf-8") as f: pred=json.load(f)
    with open(f"{base}/holdout30/inputs/{id_}.json",encoding="utf-8") as f: inp=json.load(f)
    g=gold[id_]
    out.append(f"\n{'='*80}\nCASE {id_}  ours={final['per_case'][id_]['ours']} master={final['per_case'][id_]['master']} diff={final['per_case'][id_]['diff']}")
    out.append("--- PREDICTION (full json) ---"); out.append(json.dumps(pred,ensure_ascii=False,indent=1))
    out.append("--- GOLD (full) ---"); out.append(json.dumps(g,ensure_ascii=False,indent=1))
    out.append("--- INPUT (full) ---"); out.append(json.dumps(inp,ensure_ascii=False,indent=1))
    # work summary compact
    def jtxt(j,inv):
        o=j.get(inv[id_],{})
        return f"d={o.get('direction')} c={o.get('claims')} t={o.get('timing')} tot={o.get('total')} :: {o.get('reason','')}"
    w={"id":id_,"ours":final['per_case'][id_]['ours'],"master":final['per_case'][id_]['master'],"diff":final['per_case'][id_]['diff'],
       "pred_keys":list(pred.keys()),"gold_keys":list(g.keys()),"input_keys":list(inp.keys()),
       "O1":jtxt(jO1,invO),"O2":jtxt(jO2,invO),"M1":jtxt(jM1,invM),"M2":jtxt(jM2,invM)}
    work.append(w)
with open(f"{base}/runs/round87/acceptance/diagnosis/diag_compact_h30_r87.txt","w",encoding="utf-8") as f:
    f.write("DIAG-H30 编码底稿（R87）：holdout30 28 件 predictions＋金标＋输入卡全文并置；id 集与 final-scores-h30 per_case 全等（28/28，脚本断言）。\n")
    f.write("\n".join(out))
with open(f"{base}/runs/round87/diag_work_h30_r87.json","w",encoding="utf-8") as f: json.dump(work,f,ensure_ascii=False,indent=1)
for w in work: print(w["id"], w["pred_keys"], "|", w["gold_keys"], "|", w["input_keys"])
print("compact bytes", os.path.getsize(f"{base}/runs/round87/acceptance/diagnosis/diag_compact_h30_r87.txt"))
