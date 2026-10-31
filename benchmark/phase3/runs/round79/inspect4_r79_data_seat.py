import json, pathlib, collections
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
for r in range(49,79):
    p = base/f"data/case-annotations-r{r}.json"
    if not p.exists():
        print(r, "MISSING"); continue
    d=json.loads(p.read_text(encoding="utf-8"))
    ann=d.get("annotations",[])
    print(r, "len", len(ann), "counts.cases_total", d.get("counts",{}).get("cases_total"), "verdicts", collections.Counter(a["disposition"] for a in ann), "counts keys", list(d.get("counts",{}).keys())[:12])
