import json, re, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round77")
rows=[json.loads(l) for l in (base/"judging/judgeY-block3.jsonl").read_text().splitlines() if l.strip()]
rows.sort(key=lambda r:r["anon_id"])
txt=(base/"judgeY-block3-scorebuild.py").read_text()
entries=[(float(a),float(b),float(c),d) for a,b,c,d in re.findall(r'\("P3-[0-9a-f]+",([\d.]+),([\d.]+),([\d.]+),"([^"]*)"\)',txt)]
assert len(entries)==120, len(entries)
# insert missing positions 41 (LR3-104) and 42 (LY-104), in sorted order they sit at indices 41,42
entries.insert(41,(2.0,2.0,1.0,"上疏不利获咎验，荐人下狱拟配；结局无可核时点"))
entries.insert(42,(0.0,0.0,0.0,"断自测病可愈非重症，实胸部肿瘤后于戌日手术，全反；午日病退应期错"))
assert len(entries)==122
# LY-242 (index 43): scores corrected to match its reason (婚成、白头、儿女成行全验；次日允婚应期近)
entries[43]=(2.0,2.0,1.0,entries[43][3])
out=base/"judging/judgeY-block3-scores.jsonl"
def num(x): return int(x) if x==int(x) else x
with out.open("w",encoding="utf-8") as f:
    for r,(d,c,t,reason) in zip(rows,entries):
        total=d+c+t
        f.write(json.dumps({"anon_id":r["anon_id"],"direction":num(d),"claims":num(c),"timing":num(t),"total":num(total),"pass":total>=4,"reason":reason},ensure_ascii=False)+"\n")
print(out, out.stat().st_size)
