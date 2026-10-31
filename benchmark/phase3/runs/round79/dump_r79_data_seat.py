import json, pathlib, re
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
man = json.loads((base/"runs/round79/judging/outcome-manifest.json").read_text(encoding="utf-8"))
mapping = json.loads((base/"runs/round79/judging/host-mapping.json").read_text(encoding="utf-8"))
r78 = json.loads((base/"data/case-annotations-r78.json").read_text(encoding="utf-8"))
by78 = {a["case_id"]: a for a in r78["annotations"]}
flagtext = (base/"runs/round79/judge-flags-r79-host-compiled.md").read_text(encoding="utf-8")
anons = sorted(set(re.findall(r"P3-[0-9a-f]{8}", flagtext)))
# flag lines per anon
flaglines = {}
for line in flagtext.splitlines():
    m = re.search(r"P3-[0-9a-f]{8}", line)
    if m: flaglines.setdefault(m.group(0), []).append(line.strip())
# carry layers in chronological order
layer_keys = [k for k in man.keys() if re.match(r"_r\d+_carryover", k)]
def latest_carry(cid):
    hits=[]
    for k in layer_keys:
        v = man[k]
        if isinstance(v, dict) and cid in v: hits.append((k, v[cid]))
    return hits
out=[]
for anon in anons:
    cid = mapping[anon]
    out.append(f"\n{'='*80}\n### {cid}  anon={anon}  in_r78={'YES' if cid in by78 else 'NO'}")
    for fl in flaglines.get(anon, []): out.append("FLAG: "+fl)
    cardp = base/f"inputs-dev12/{cid}.json"
    if cardp.exists():
        card = json.loads(cardp.read_text(encoding="utf-8"))
        for key in ("question","setting","tradition","system"):
            if key in card: out.append(f"CARD {key}: {json.dumps(card[key], ensure_ascii=False)[:400]}")
        out.append("CARD keys: "+",".join(card.keys()))
    else:
        out.append("CARD: NOT in inputs-dev12")
    out.append("OUTCOME: "+man["cases"].get(cid,"<missing>"))
    st = man.get("stripped_tail",{}).get(cid)
    if st: out.append("STRIPPED_TAIL: "+st)
    for k,v in latest_carry(cid)[-2:]:
        out.append(f"CARRY[{k}]: {v[:500]}")
    if cid in by78:
        a=by78[cid]
        out.append(f"R78 disp={a['disposition']} rel={a['relation']}")
        out.append("R78 flag: "+a["flag"][:400])
    predp = base/f"runs/round79/predictions/{cid}.json"
    out.append("PRED exists: "+str(predp.exists()))
(base/"runs/round79/dump_r79_out.txt").write_text("\n".join(out), encoding="utf-8")
print("written", len("\n".join(out)))
