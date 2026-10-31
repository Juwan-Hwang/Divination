p="/home/hatch/workspace/divination/benchmark/phase3/runs/round91/write_b1112_r91.py"
lines=open(p,encoding="utf-8").read().split("\n")
# lines list is 0-indexed; file lines 8..27 (1-indexed) need indentation
indent={8:4,11:4,12:4,13:8,14:8,15:8,16:8,17:8,18:8,19:8,20:12,21:4,22:4,23:8,24:8,25:8,26:8,27:4}
for ln,sp in indent.items():
    i=ln-1
    if lines[i] and not lines[i].startswith(" "):
        lines[i]=" "*sp+lines[i]
# fix __main__ block at end if present
for i,l in enumerate(lines):
    if l.startswith('write_batch("B11"'):
        lines[i]="    "+l
open(p,"w",encoding="utf-8").write("\n".join(lines))
print("patched")
