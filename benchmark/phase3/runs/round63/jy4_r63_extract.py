import json, pathlib
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round63')
rows = [json.loads(l) for l in open(base/'judging/judgeY-block4.jsonl', encoding='utf-8') if l.strip()]
mapping = json.load(open(base/'judging/host-mapping.json', encoding='utf-8'))
out = open(base/'jy4_r63_work.txt', 'w', encoding='utf-8')
print('count', len(rows))
missing = []
for r in rows:
    anon = r['anon_id']
    cid = mapping.get(anon)
    if not cid:
        missing.append((anon, 'no-mapping')); continue
    p = base/'predictions'/f'{cid}.json'
    if not p.exists():
        missing.append((anon, cid)); continue
    data = json.load(open(p, encoding='utf-8'))
    pt = data.get('prediction_text') if isinstance(data, dict) else None
    out.write(f"\n===== {anon} | {cid} =====\n")
    out.write(f"OUTCOME: {r.get('outcome_record')}\n")
    if 'carry_note' in r: out.write("HAS_CARRY_NOTE\n")
    if 'editor_note' in r: out.write("HAS_EDITOR_NOTE\n")
    out.write("PREDICTION_TEXT:\n")
    out.write((pt if pt is not None else json.dumps(data, ensure_ascii=False)) + "\n")
out.close()
print('missing', missing)
