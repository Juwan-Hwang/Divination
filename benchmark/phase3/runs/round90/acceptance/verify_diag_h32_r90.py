import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
r90=base/"runs/round90/acceptance"
final=json.loads((r90/"judging/final-scores-h32.json").read_text())
ids=list(final["per_case"].keys())
s8name=s8label=s8full=only_level=s12name=s12dui=0; lists={}
for cid in ids:
    b=json.loads((r90/f"predictions/{cid}.json").read_text())['basis']
    if "第八节" in b or "R80" in b: s8name+=1; lists.setdefault('s8name',[]).append(cid)
    if "功量核算" in b: s8full+=1; lists.setdefault('s8full',[]).append(cid)
    if "功量" in b: s8label+=1; lists.setdefault('s8label',[]).append(cid)
    if "量级" in b and "功量" not in b: only_level+=1; lists.setdefault('only_level',[]).append(cid)
    if "第十二节" in b: lists.setdefault('s12name',[]).append(cid)
    if "R87" in b: lists.setdefault('s12r87',[]).append(cid)
    if "对位" in b: lists.setdefault('s12dui',[]).append(cid)
print("S8 节名/R80:", s8name, "| 功量字样:", s8label, lists.get('s8label'), "| 功量核算全称:", s8full, lists.get('s8full'), "| 仅量级无功量:", only_level, lists.get('only_level'))
print("S12 第十二节字样:", lists.get('s12name'), "| R87:", lists.get('s12r87'), "| 对位:", lists.get('s12dui'))
# judge O2 flags
packet=json.loads((r90/"judging/packet-ours.json").read_text())
preds={cid: json.loads((r90/f"predictions/{cid}.json").read_text()) for cid in ids}
anon2case={e["anon_id"]:cid for e in packet for cid,p in preds.items() if p["prediction_text"]==e["prediction_text"]}
for name in ["judgeO1.jsonl","judgeO2.jsonl","judgeM1.jsonl","judgeM2.jsonl"]:
    for line in (r90/f"judging/{name}").read_text().splitlines():
        j=json.loads(line)
        if j.get("flag"): print(name, anon2case.get(j["anon_id"]), "FLAG:", j["flag"])
# snapshot listing check (names only, for § header)
snap=base/"runs/round88/kb-snapshot-holdout32"
print("snapshot exists:", snap.exists())
