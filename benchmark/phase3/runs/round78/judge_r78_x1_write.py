import json, pathlib, sys
base=pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round78')
out=base/'judging/judgeX-block1-scores.jsonl'
rows=json.loads(pathlib.Path(sys.argv[1]).read_text()) if False else None
