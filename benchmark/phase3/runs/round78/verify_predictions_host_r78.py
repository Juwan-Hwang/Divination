import json, os, re, collections
BASE="/home/hatch/workspace/divination/benchmark/phase3"
b=json.load(open(f"{BASE}/runs/round78/batches.json"))
want=[]
for k,v in b.items(): want+=v
assert len(want)==487 and len(set(want))==487
P=f"{BASE}/runs/round78/predictions"
files=set(fn[:-5] for fn in os.listdir(P) if fn.endswith(".json"))
missing=[c for c in want if c not in files]
extra=[c for c in files if c not in set(want)]
bad=[]
trig={"changed_main":0,"reserve_used":0,"disputed":0}
for c in want:
    try:
        d=json.load(open(f"{P}/{c}.json"))
        assert d["case_id"]==c, "case_id mismatch"
        for f in ("prediction_text","basis","confidence","trigger"):
            assert f in d and d[f] not in (None,""), f"missing {f}"
        assert isinstance(d["confidence"],(int,float)) and 0<=d["confidence"]<=1
        t=d["trigger"]
        for f in ("changed_main","reserve_used","disputed","reason"):
            assert f in t, f"trigger missing {f}"
        for f in ("changed_main","reserve_used","disputed"):
            assert isinstance(t[f],bool)
            if t[f]: trig[f]+=1
    except Exception as e:
        bad.append((c,str(e)))
print("want",len(want),"files",len(files),"missing",missing,"extra",extra,"bad",bad)
print("trigger recount:",trig)
assert not missing and not extra and not bad

# ---- tradition first-line host check (三口径：卡面值照录／未标注如实／变体列单） ----
UNMARKED=re.compile(r"未[标標][注註]|無 tradition|无 tradition|not (stated|marked)|no tradition", re.I)
CLAIM=re.compile(r"(tradition|system)\s*[:：]\s*([^\s，。；\n]+)", re.I)
flags=[]; variants=collections.Counter(); n_card=0; n_nocard=0
for c in want:
    card=json.load(open(f"{BASE}/inputs-dev12/{c}.json"))
    cv=None; cf=None
    for f in ("tradition","system"):
        if card.get(f): cv=str(card[f]); cf=f; break
    d=json.load(open(f"{P}/{c}.json"))
    first=d["basis"].split("\n")[0].strip()
    variants[first[:40]]+=0  # placeholder, real inventory below
    if cv:
        n_card+=1
        if cv not in first and UNMARKED.search(first):
            flags.append((c,"card-has-value-but-declares-unmarked",cv,first[:80]))
        elif cv not in first:
            m=CLAIM.search(first)
            if not m:
                flags.append((c,"card-value-not-in-firstline-noclaim",cv,first[:80]))
            elif m.group(2).strip("`'\"")!=cv:
                flags.append((c,"claimed-value-differs",cv,first[:80]))
    else:
        n_nocard+=1
        m=CLAIM.search(first)
        if not UNMARKED.search(first):
            if m and m.group(2).lower() not in ("未标注","未標註"):
                flags.append((c,"card-lacks-but-claims-value",m.group(2),first[:80]))
            elif not m:
                flags.append((c,"card-lacks-no-unmarked-declaration",None,first[:80]))
print("cards with tradition/system:",n_card," without:",n_nocard)
print("tradition flags:",len(flags))
for f in flags: print(" FLAG",f)
# first-line template inventory (top patterns after masking case-specific values)
tmpl=collections.Counter()
for c in want:
    d=json.load(open(f"{P}/{c}.json"))
    first=d["basis"].split("\n")[0].strip()
    t=re.sub(r"(tradition|system)\s*[:：]\s*\S+","\\1: <v>",first)
    t=re.sub(r"[A-Z]{2,3}2?-?\d+","<id>",t)
    tmpl[t[:60]]+=1
print("distinct first-line templates:",len(tmpl))
for t,n in tmpl.most_common(12): print("  ",n,t)
print("HOST VERIFY OK 487/487 + tradition check done")
