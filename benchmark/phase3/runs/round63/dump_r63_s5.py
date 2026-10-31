import json
base='/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12'
b=json.load(open('/home/hatch/workspace/divination/benchmark/phase3/runs/round63/batches.json'))
ids=[]
for k in ['B13','B14','B15']: ids+=b[k]
assert len(ids)==60, len(ids)
out=[]
for cid in ids:
    d=json.load(open(f'{base}/{cid}.json'))
    ctx=d.get('context',{})
    att=ctx.get('attachments',{}) or {}
    lines=[]
    lines.append(f"==={cid} trad={d.get('tradition')} q={ctx.get('question')} at={ctx.get('asked_at')} setting={ctx.get('setting')}")
    for k,v in att.items():
        if k=='chart_lines_top_to_bottom':
            lines.append(' lines(top->bottom):')
            for i,l in enumerate(v): lines.append(f'   L{6-i}: {l}')
        else:
            lines.append(f' {k}={v}')
    # other ctx keys
    for k,v in ctx.items():
        if k not in ('question','asked_at','setting','attachments'):
            lines.append(f' ctx.{k}={v}')
    out.append('\n'.join(lines))
open('/home/hatch/workspace/divination/benchmark/phase3/runs/round63/inputs_r63_s5.txt','w').write('\n'.join(out))
print('ok', len(ids))
