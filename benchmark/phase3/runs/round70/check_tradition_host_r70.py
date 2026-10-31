import json, os
BASE="/home/hatch/workspace/divination/benchmark/phase3"
b=json.load(open(f"{BASE}/runs/round70/batches.json"))
want=[c for v in b.values() for c in v]
dirs=[d for d in os.listdir(BASE) if d.startswith('inputs')]
def locate(c):
    for d in dirs:
        p=f"{BASE}/{d}/{c}.json"
        if os.path.exists(p): return p
KW={'liuyao':['六爻'],'六爻':['六爻'],'bazi':['八字'],'horary':['卜卦','horary','Horary'],
'meihua':['梅花'],'astrology':['占星'],'fengshui':['风水','堪舆'],'yijing':['筮','易'],
'vedic-astrology':['吠陀','vedic','Vedic','印度占星'],'筮占':['筮'],'liuren':['六壬'],
'ziwei':['紫微'],'qimen':['奇门','遁甲'],'dream':['梦'],'mengzhan':['梦']}
direct=0; nonelabel=0; flags=[]
for c in want:
    card=json.load(open(locate(c)))
    trad=card.get('tradition') or card.get('system')
    pred=json.load(open(f"{BASE}/runs/round70/predictions/{c}.json"))
    b1=pred['basis'].split('\n')[0]
    if trad:
        kws=KW.get(trad,[trad])
        if trad in b1 or any(k in b1 for k in kws): direct+=1
        else: flags.append((c,trad,b1[:100]))
    else:
        if ('未标注' in b1) or ('无tradition' in b1) or ('无 tradition' in b1) or ('未标' in b1): nonelabel+=1
        else: flags.append((c,'NONE',b1[:100]))
print('direct',direct,'none-labelled',nonelabel,'flags',len(flags))
for f in flags: print(f)

# ---- R67 addition (STAGE-SUMMARY-51 item 5), carried through R68/R69 into R70:
# basis tradition declaration group-consistency scan. A basis may repeat a
# heading-style declaration block; two blocks with DIFFERENT values are a
# mislabel (R66 BZ-303/304 pattern). Same-value repeats are registered
# only, not conflicts.
import re
DECL = re.compile(r'(?m)^\s*tradition\s*[=:：]\s*([^\s（(；;，,、]+)')
groups = {}
for c in want:
    pred = json.load(open(f"{BASE}/runs/round70/predictions/{c}.json"))
    vals = [v.strip() for v in DECL.findall(pred['basis'])]
    if len(vals) > 1:
        groups[c] = vals
conflicts = {c: v for c, v in groups.items() if len(set(v)) > 1}
print('declaration-group files:', len(groups), '| CONFLICT groups:', len(conflicts))
for c, v in conflicts.items():
    print('CONFLICT', c, v)
