import json, pathlib, sys
ids=['YM-019','YM-020','YM-022','YM-023','YM-024','YM-025','YM-027','YM-028','YM-029','YM-030','YM-032','YM-033','YM-034','YM-035','YM-037','YM-038','YM-039','YM-040','YM-042','YM-043','YM-044','YM-045','YM-047','YM-048','YM-049','YM-050','YM-052','YM-053','YM-054','YM-055','YM-057','YM-058','YM-059','YM-060','YM-062','YM-063','YM-064','YM-065','YM-067','YM-068','YM-069','YM-070','YY-006','YY-010','YY-011','YY-012','YY-013','YY-014','YY-015','YY-016','YY-017','YY-018','YY-019','YY-020','YY-021','YY-022','YY-023','YY-024','YY2-001','YY2-002']
base=pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12')
start=int(sys.argv[1]); end=int(sys.argv[2])
for cid in ids[start:end]:
    d=json.loads((base/(cid+'.json')).read_text())
    c=d.get('context',{}); a=c.get('attachments',{})
    print(f"### {cid} trad={d.get('tradition')} subj={d.get('subject')}")
    print(f"Q={c.get('question')} AT={c.get('asked_at')} SET={c.get('setting')}")
    for k,v in a.items():
        print(f"{k}={v}")
    # any extra context keys
    for k,v in c.items():
        if k not in ('question','asked_at','setting','attachments'):
            print(f"ctx.{k}={v}")
