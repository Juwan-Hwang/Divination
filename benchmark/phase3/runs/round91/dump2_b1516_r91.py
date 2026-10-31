import json, pathlib
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
batches = json.loads((base/'runs/round91/batches.json').read_text())
ids = batches['B15'] + batches['B16']
out = []
for cid in ids:
    d = json.loads((base/f'inputs-dev12/{cid}.json').read_text())
    # strip verbose notes but keep grades summary
    notes = d.get('notes')
    grade_info = None
    if isinstance(notes, dict):
        cg = notes.get('completion_grade')
        if isinstance(cg, dict):
            fields = cg.get('fields', {})
            grade_info = {k: (v.get('grade') if isinstance(v, dict) else v) for k, v in fields.items()}
        else:
            grade_info = notes
    elif notes:
        grade_info = notes
    slim = {k: v for k, v in d.items() if k != 'notes'}
    out.append(f"===== {cid} grades={json.dumps(grade_info, ensure_ascii=False)}")
    out.append(json.dumps(slim, ensure_ascii=False))
    out.append('')
pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round91/cards2_b1516_r91.txt').write_text('\n'.join(out))
print('ok')
