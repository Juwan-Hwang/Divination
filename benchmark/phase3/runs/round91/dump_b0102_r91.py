import json, pathlib
base=pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12')
batches=json.loads(open('/home/hatch/workspace/divination/benchmark/phase3/runs/round91/batches.json').read())
for batch in ['B01','B02']:
    print(f"##### {batch}")
    for cid in batches[batch]:
        d=json.loads((base/f'{cid}.json').read_text())
        print(f"--- {cid} keys={list(d.keys())} tradition={d.get('tradition')} system={d.get('system')}")
        subj=d.get('subject',{})
        print(" subj:", json.dumps(subj, ensure_ascii=False)[:600])
        ctx=d.get('context',{})
        print(" q:", ctx.get('question'))
        print(" asked:", ctx.get('asked_at'))
        print(" setting:", str(ctx.get('setting'))[:500])
        att=ctx.get('attachments') or d.get('attachments') or {}
        print(" att:", json.dumps(att, ensure_ascii=False)[:1800])
        # other top fields
        for k,v in d.items():
            if k not in ('subject','context','provenance','language','id','uid','tradition'):
                print(f" {k}:", json.dumps(v, ensure_ascii=False)[:800])
