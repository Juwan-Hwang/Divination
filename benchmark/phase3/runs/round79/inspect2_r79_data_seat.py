import json, collections, pathlib, re
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
out=[]
def p(*a):
    out.append(" ".join(str(x) for x in a))
mapping = json.loads((base/"runs/round79/judging/host-mapping.json").read_text(encoding="utf-8"))
p("mapping type", type(mapping).__name__)
if isinstance(mapping, dict):
    p("mapping keys", list(mapping.keys())[:20])
    for k in list(mapping.keys())[:3]:
        p(" sample", k, json.dumps(mapping[k], ensure_ascii=False)[:600])
elif isinstance(mapping, list):
    p("len", len(mapping), json.dumps(mapping[:2], ensure_ascii=False)[:800])

r78 = json.loads((base/"data/case-annotations-r78.json").read_text(encoding="utf-8"))
by_case78 = {a["case_id"]: a for a in r78["annotations"]}
by_anon78 = {a["anon_id"]: a for a in r78["annotations"]}

# parse flags md
text = (base/"runs/round79/judge-flags-r79-host-compiled.md").read_text(encoding="utf-8")
# anon ids in order
anons = re.findall(r"P3-[0-9a-f]{8}", text)
p("flag anon occurrences", len(anons), "unique", len(set(anons)))
uniq = sorted(set(anons))
p("unique anons", uniq)
# How mapping looks - try resolve each
def resolve(anon):
    if isinstance(mapping, dict):
        if anon in mapping:
            v=mapping[anon]
            return v
        # maybe values contain anon
        for k,v in mapping.items():
            if isinstance(v, dict) and v.get("anon_id")==anon: return {k:v}
            if isinstance(v, list):
                for e in v:
                    if isinstance(e, dict) and e.get("anon_id")==anon: return e
        return None
    else:
        for e in mapping:
            if isinstance(e, dict) and e.get("anon_id")==anon: return e
        return None

for anon in uniq:
    r = resolve(anon)
    p(anon, "->", json.dumps(r, ensure_ascii=False)[:400] if r else "NOT FOUND")

(pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round79/inspect2_r79_out.txt")).write_text("\n".join(out), encoding="utf-8")
print("\n".join(out[:40]))
