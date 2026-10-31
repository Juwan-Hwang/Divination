import json, pathlib
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round64')
inp = base/'judging/judgeX-block1.jsonl'
mapping = json.loads((base/'judging/host-mapping.json').read_text(encoding='utf-8'))
rows = [json.loads(l) for l in inp.read_text(encoding='utf-8').splitlines() if l.strip()]
out = []
for i, r in enumerate(rows):
    anon = r['anon_id']
    cid = mapping.get(anon)
    pf = base/'predictions'/f'{cid}.json'
    try:
        pj = json.loads(pf.read_text(encoding='utf-8'))
    except Exception as e:
        pj = {'ERROR': str(e)}
    # find prediction_text
    pt = pj.get('prediction_text') if isinstance(pj, dict) else None
    if pt is None:
        pt = json.dumps(pj, ensure_ascii=False)
    out.append(f"=== {i} {anon} -> {cid} ===")
    out.append(f"OUTCOME: {r.get('outcome_record')}")
    if 'carry_note' in r: out.append(f"CARRY: {r['carry_note']}")
    if 'editor_note' in r: out.append(f"EDITOR: {r['editor_note']}")
    out.append(f"PRED: {pt}")
    out.append("")
(base/'jx1-dump.txt').write_text("\n".join(out), encoding='utf-8')
print(len(rows))
print((base/'jx1-dump.txt').stat().st_size)
