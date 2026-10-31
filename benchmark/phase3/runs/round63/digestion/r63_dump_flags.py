import json, pathlib, collections
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
def load(p):
    with open(p, encoding="utf-8") as f: return json.load(f)
r62 = load(base/"data/case-annotations-r62.json")
# dual view example
for f in r62["flags"]:
    if f["dual_view"]:
        print("dual example:", f["case_id"], f["views"], [a["source_seats"] for a in r62["annotations"] if a["anon_id"]==f["anon_id"]]); break
print("dual count:", sum(1 for f in r62["flags"] if f["dual_view"]))

# --- parse R63 FLAGS by lines (splitlines, prefix '- P3-') ---
hm = load(base/"runs/round63/judging/host-mapping.json")
lines = (base/"runs/round63/judging/FLAGS-selfreported-r63.md").read_text(encoding="utf-8").splitlines()
seat=None; entries=[]
for l in lines:
    if l.startswith("# "):
        seat=l[2:].strip()
        continue
    if l.startswith("- P3-"):
        body=l[2:]
        anon, txt = body.split("：",1)
        entries.append({"anon":anon.strip(),"seat_header":seat,"text":txt})
print("flag lines:", len(entries))
# seat label: derive from header: e.g. 'R63 评审旗标 X1' -> X1 ; 'R63 评审旗标 X2（...）' -> X2; 'R63 评审旗标 Y1（block1）' -> Y1; '# R63 评审旗标（Y4）' -> Y4
def seat_label(h):
    for tok in ["X1","X2","X3","X4","Y1","Y2","Y3","Y4"]:
        if tok in h: return tok
    return h
for e in entries: e["seat"]=seat_label(e["seat_header"])
byanon=collections.OrderedDict()
for e in entries:
    byanon.setdefault(e["anon"],[]).append(e)
print("unique anons:", len(byanon))
missing=[a for a in byanon if a not in hm]
print("anons missing from mapping:", missing)
cases=[hm[a] for a in byanon]
print("unique cases:", len(set(cases)), "dup cases:", [c for c,n in collections.Counter(cases).items() if n>1])

# prior annotations index
prior_files=[49,50,51,53,54,55,56,57,58,59,60,61,62]
prior={}
for r in prior_files:
    d=load(base/f"data/case-annotations-r{r}.json")
    for a in d["annotations"]:
        prior.setdefault(a["case_id"],[]).append((r,a))
flagged_cases=set(cases)
new_cases=[c for c in flagged_cases if c not in prior]
print("\ncases with NO prior annotation:", sorted(new_cases))
cont=[c for c in flagged_cases if c in prior]
print("cases with prior:", len(cont))

# outcome equality r63 vs r62
om63=load(base/"runs/round63/judging/outcome-manifest.json")
om62=load(base/"runs/round62/judging/outcome-manifest.json")
diffs=[c for c in flagged_cases if om63["cases"].get(c)!=om62["cases"].get(c)]
print("\noutcome r63!=r62 among flagged:", diffs)

# write dump file
out=[]
for anon, es in byanon.items():
    cid=hm[anon]
    rec={"anon":anon,"case_id":cid,"seats":[e["seat"] for e in es],"flags_r63":[f"{e['seat']}：{e['text']}" for e in es],
         "outcome_r63":om63["cases"].get(cid),
         "prior":[{ "round":r, "disposition":a["disposition"], "relation":a["relation"], "flag":a["flag"], "finding":a["finding"], "carry":a["manifest_carry_suggestion"]} for r,a in prior.get(cid,[])]}
    out.append(rec)
pathlib.Path(base/"runs/round63/digestion/r63_flagdump.json").write_text(json.dumps(out,ensure_ascii=False,indent=1),encoding="utf-8")
print("dump written, records:", len(out))
