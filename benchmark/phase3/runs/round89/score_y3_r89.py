import json, sys, pathlib
P3=pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
out=P3/'runs/round89/judging/judgeY-block3-scores.jsonl'
def append(rows):
    with out.open('a',encoding='utf-8') as f:
        for r in rows:
            assert abs(r['total']-(r['direction']+r['claims']+r['timing']))<1e-9
            assert r['pass']==(r['total']>=4)
            for k in ('direction','claims','timing'):
                assert r[k]>=0 and r[k]<=2 and (r[k]*2)==int(r[k]*2)
            f.write(json.dumps(r,ensure_ascii=False)+'\n')
    lines=out.read_text(encoding='utf-8').strip().splitlines() if out.stat().st_size else []
    print('total lines now', len(lines))
if __name__=='__main__':
    rows=json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8')) if len(sys.argv)>1 else []
    append(rows)
