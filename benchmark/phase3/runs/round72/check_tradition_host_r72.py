import json, os
BASE="/home/hatch/workspace/divination/benchmark/phase3"
b=json.load(open(f"{BASE}/runs/round72/batches.json"))
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
NONE_ZH=['未标注','无tradition','无 tradition','未标','未標註','無tradition','無 tradition','未標']
NONE_EN=['no tradition field','bears no tradition','no tradition indicated',
'tradition not stated','tradition not specified','no tradition label',
'no tradition given','tradition field absent','without a tradition field']
direct=0; nonelabel=0; flags=[]
for c in want:
    card=json.load(open(locate(c)))
    trad=card.get('tradition') or card.get('system')
    pred=json.load(open(f"{BASE}/runs/round72/predictions/{c}.json"))
    b1=pred['basis'].split('\n')[0]
    if trad:
        kws=KW.get(trad,[trad])
        if trad in b1 or any(k in b1 for k in kws): direct+=1
        else: flags.append((c,trad,b1[:100]))
    else:
        b1l=b1.lower()
        if any(k in b1 for k in NONE_ZH) or any(k in b1l for k in NONE_EN): nonelabel+=1
        else: flags.append((c,'NONE',b1[:100]))
print('direct',direct,'none-labelled',nonelabel,'flags',len(flags))
for f in flags: print(f)

# ---- R72 change (STAGE-SUMMARY-56 R72 list item 1, per R71 FREEZE s.2):
# the none-labelled keyword set above now also covers English variants
# (NONE_EN, matched case-insensitively): R71's 7 initial flags were all
# English first-line variants (WP-001..007) adjudicated not-upheld by the
# host. Comparability with the R71 initial check is registered in
# FREEZE-r72 s.2.
# ---- R71 carried change: Traditional variants in NONE_ZH (R70's 33
# initial flags were all Simplified-set misses on Traditional first lines).
# ---- R67 addition, carried through R68-R72:
# basis tradition declaration group-consistency scan. A basis may repeat a
# heading-style declaration block; two blocks with DIFFERENT values are a
# mislabel (R66 BZ-303/304 pattern). Same-value repeats are registered
# only, not conflicts.
import re
DECL = re.compile(r'(?m)^\s*tradition\s*[=:：]\s*([^\s（(；;，,、]+)')
groups = {}
for c in want:
    pred = json.load(open(f"{BASE}/runs/round72/predictions/{c}.json"))
    vals = [v.strip() for v in DECL.findall(pred['basis'])]
    if len(vals) > 1:
        groups[c] = vals
conflicts = {c: v for c, v in groups.items() if len(set(v)) > 1}
print('declaration-group files:', len(groups), '| CONFLICT groups:', len(conflicts))
for c, v in conflicts.items():
    print('CONFLICT', c, v)
