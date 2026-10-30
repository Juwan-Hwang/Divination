#!/usr/bin/env python3
import json, pathlib
data=json.loads((pathlib.Path(__file__).parent/"yuewei-parsed-r53.json").read_text(encoding="utf-8"))
outdir=pathlib.Path(__file__).parent/"yuewei-review-r53"
outdir.mkdir(exist_ok=True)
# chunk by 7 pages
for ci in range(0,len(data),7):
    chunk=data[ci:ci+7]
    lines=[]
    for pg in chunk:
        lines.append(f"\n===== bookv_{pg['page']} {pg['vol']} 条目{pg['count']} =====")
        for e in pg["entries"]:
            if e["flag"]:
                lines.append(f"\n--- [{pg['page']}#{e['idx']}] ---\n{e['text']}")
    (outdir/f"chunk-{ci//7+1:02d}.txt").write_text("\n".join(lines),encoding="utf-8")
# also list unflagged heads for verification
lines=[]
for pg in data:
    for e in pg["entries"]:
        if not e["flag"]:
            lines.append(f"{pg['page']}#{e['idx']}: {e['head']}")
(outdir/"unflagged-heads.txt").write_text("\n".join(lines),encoding="utf-8")
print("done")
