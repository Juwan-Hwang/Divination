import json, pathlib
base=pathlib.Path(__file__).parent
inp=base/"judgeY-block4.jsonl"
mp=json.loads((base/"host-mapping.json").read_text())
out=base/"dump-judgeY-block4-r41-a1.txt"
lines=[]
for line in inp.read_text().splitlines():
    if not line.strip(): continue
    o=json.loads(line); anon=o["anon_id"]; cid=mp[anon]
    p=json.loads((base.parent/"predictions"/f"{cid}.json").read_text())
    lines.append(f"=== {anon} | {cid} ===\nOUTCOME: {o['outcome_record']}\nPREDICTION_TEXT:\n{p.get('prediction_text','')}\n")
out.write_text("\n".join(lines))
print(len(lines))
