import json, pathlib, collections
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
def load(p):
    with open(p, encoding="utf-8") as f: return json.load(f)

fp = base/"runs/round63/judging/FLAGS-selfreported-r63.md"
lines = fp.read_text(encoding="utf-8").splitlines()
for i,l in enumerate(lines):
    print(i, repr(l)[:700])
