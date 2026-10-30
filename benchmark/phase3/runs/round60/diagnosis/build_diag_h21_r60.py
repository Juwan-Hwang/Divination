import json, math, os
B='/home/hatch/workspace/divination/benchmark/phase3'
D=B+'/runs/round60/diagnosis'
fs=json.load(open(B+'/runs/round60/acceptance/judging/final-scores.json'))
hm=json.load(open(B+'/runs/round60/acceptance/judging/host-mapping.json'))
rev_o={v:k for k,v in hm['ours'].items()}; rev_m={v:k for k,v in hm['master'].items()}
def load(fn):
    return {json.loads(l)['anon_id']:json.loads(l) for l in open(B+'/runs/round60/acceptance/judging/'+fn,encoding='utf-8')}
O1,O2,M1,M2=load('judgeO1.jsonl'),load('judgeO2.jsonl'),load('judgeM1.jsonl'),load('judgeM2.jsonl')
sub={}
for cid in fs['per_case']:
    o1,o2,m1,m2=O1[rev_o[cid]],O2[rev_o[cid]],M1[rev_m[cid]],M2[rev_m[cid]]
    so={k:(o1[k]+o2[k])/2 for k in ('direction','claims','timing')}
    sm={k:(m1[k]+m2[k])/2 for k in ('direction','claims','timing')}
    assert abs(sum(so.values())-fs['ours'][cid])<1e-9,(cid,'ours')
    assert abs(sum(sm.values())-fs['master'][cid])<1e-9,(cid,'master')
    sub[cid]={'ours':so,'master':sm}
print('subscore recompute vs final-scores: all 25 OK')
# coding: cid -> (segment, primary, e4, evidence)
CODING={
 'GSZ-003':('六爻·GSZ','E5-TIM','NA-列','曾合已散与法院离婚方向合（O 双视），差集中于 timing −0.75：我方主坐标午月未中、实于子月经法院离婚；大师「下月经法院离婚」应期基本命中。'),
 'GSZ-005':('六爻·GSZ','无失分主因','NA-列','我方胜（＋2.00）：离原岗办退休手续合退离方向（O 双视）；大师断下岗而实为高高兴兴办退休、仅得 1.50。我方「竞争顶替」子断未验，附记登记、不占主码。'),
 'GSZ-009':('六爻·GSZ','E3','SEAT','射覆主导面为金标的色泽／形态面（黑里透黄褐色、物带点尖），列面记录只取金属质地一面断钥匙串、色泽与尖形两面从未入列，direction／claims 双视均 0；卦盘锚点逐字在场、basis 无缺路登记。'),
 'GSZ-015':('六爻·GSZ','无失分主因','NA-列','我方小胜（＋0.25）：父病难愈、无望方向与大师同分（direction 2.00 同），claims 以癌症一断胜出在我方未断癌名；我方病位旁注肝胆而实肺癌，附记登记、不占主码。'),
 'GSZ-016':('六爻·GSZ','E5-DIR','NA-列','终局方向断反：我方断录取坐实，大师以父母亥水空断名单无名，结局分数第一却因代码写错成绩作废、未被录取（O 双视同指终局方向反）；官空「假空活用」定性与结局相反，属方向层，非应期或次面问题。'),
 'GSZ-017':('六爻·GSZ','无失分主因','NA-列','平局（0.00）：追而不得、终没成双方同断（direction 2.00 同）；我方 claims 损耗在「另有男子牵连」一子断未被结局记载、大师单断 claims 满分，属平局内细节损耗附记、不占主码。'),
 'WHY-072':('六爻·WHY','E5-DIR','NA-列','终局方向全反：我方断相亲能成、对方有意，结局明言相亲不成（O 双视 direction 记 0）；金标主导面世化空破、本人不想去已在同一妻财未土取用内，我方读回头生作反向定性，属方向层。'),
 'WHY-073':('六爻·WHY','E5-TIM','NA-列','终局（未婚同居终散、现独身）双方同断，差全在 timing −1.50：我方断占后一月内散，大师逐年断 1994 年遇离婚带孩女性同居、年份精确命中；对方带孩一面我方未入列，记 A 涉附记。'),
 'WHY-074':('六爻·WHY','E5-DIR','NA-列','终局方向全反：我方断妻辰日归至，结局为同居女携款逃走不归（O 双视）；金标「不会回来」主断面与身份面（未领证同居）并存，我方两面皆反／未入列——主码按终局方向取 DIR，身份面记 A 涉附记。'),
 'WHY-075':('六爻·WHY','E3','SEAT','金标断语仅录身份一面（所问之男并非其夫、乃未婚同居），此即本例主导面，我方列面记录从未入列、径按「丈夫迟归」立断（归断亦与贩毒外逃不归结局相反，见含混登记）；卦盘锚点在场、无缺路登记。'),
 'WHY-078':('六爻·WHY','无失分主因','NA-列','我方胜（＋4.50）：对象藏而不露、同居不成婚终分手合主线（O 双视）。成色注记：本例金标 master_prediction 仅作用神要旨、无具体断语，大师侧两视同判 0 分（承验收 REPORT §一，H21M-b1ad2c79 即本例）——照实登记于成色层，不预占主码。'),
 'WHY-079':('六爻·WHY','E5-OMIT','NA-列','差仅 −0.50 且分项均匀小差（dir −0.25／claims 0／tim −0.25）：我方三角面已入列且未追成合，大师另断「1995 年有男友、今年又出现一个男友」的更替／新出现面，我方未断此面；终局「婚姻不成」与 1999 年另婚（对象不明）之间另有方向边界，见含混登记。'),
 'QW-013':('八字·QW','E3','SEAT','结局可核四项中手足面占其二（兄弟姐妹 6 人、死一、异腹一；弟犯法判刑），我方列面记录无兄弟姐妹一面、整体未入列；学历实为初中、与「事业中上」量级亦不合（O2）。四柱锚点在场、无缺路登记。主导面取舍边界见含混登记。'),
 'QW-014':('八字·QW','无失分主因','NA-列','平局（0.00），分项三项逐项同分：28 岁转房地产、自营成老板、官司破大财与项目巨损双方皆合（O／M 双视）；婚、子女、健康等未验项双方同受此限，不占主码。'),
 'QW-015':('八字·QW','E5-OMIT','NA-列','主断婚姻波折已入列且结婚、生子剖腹部分合（O2），差出自已载事件漏断：丧父花费、兄摊官司坐牢两面未入列（大师逐年断中对应命中），记 OMIT 并同记 A 涉；事业量级与峰值运未被结局印证，双方同受此限。'),
 'QW-016':('八字·QW','E5-CLAIM','NA-列','断项被结局直接推翻：我方断婚姻「聚散波折可守」，结局为添设备之年离婚（O2 明指）；发大财（15 万、100 万）双方同合。子女病残／妻流产一面未入列，记 A 涉附记。'),
 'QW-017':('八字·QW','E5-CLAIM','NA-列','破耗因断项断反：我方断破耗主因在长辈／房产／文书压资金，结局为帮朋友打架致人重伤、官司花两万平息、次年再被告而躲避（O2 明指因由不合）；官非一面仅以伤官见官泛合。丧父一面未入列，记 A 涉附记；结局成色薄（封存日志 §三）另注记。'),
 'QM-001':('奇门·QM','E5-CLAIM','NA-列','处所断项错位：找回与抽屉两点合（O 双视），但我方断居所西南柜屉，实为书店办公桌抽屉——所在场所断项被结局推翻；应期我方 0.25 反高于大师 0（大师断语无应期），非失分项。'),
 'QM-002':('奇门·QM','E5-CLAIM','NA-列','差仅 −0.25、全在 claims：有雨与应期双方满分同断，我方雨量级断「中雨、间歇性」并断非大雨，大师断「雨不会太小」与结局雨势合，我方量级一档偏低；量级小差，形态登记于此。'),
 'QM-003':('奇门·QM','E5-CLAIM','NA-列','天象断项被推翻：无雨、有风、仪式顺利双方同合，我方断晴热骄阳薄云，实况为阴天无阳光、凉风（O 双视同指）；大师断明日阴天全合。'),
 'QM-004':('奇门·QM','无失分主因','NA-列','我方胜（＋0.75）：巳时停电、申时（16:33）复电逐项全合且 claims／timing 反高于大师（大师括注时段与标准申时不合被扣）。成色注记：原书节题结局信息已经主持裁处自输入侧剔除（封存日志 §五 QM-004 裁处），本席编码时卡内无节题。'),
 'QM-005':('奇门·QM','无失分主因','NA-列','平局（0.00），双方满分：西北大阀门坏、当晚 19:20（戌时内）复水，原因、方向、时段逐项同合（O／M 双视）。'),
 'QM-006':('奇门·QM','E5-TIM','NA-列','差集中于 timing −1.25：病重不治、消化系癌方向双方同断（O：食道癌属消化系合），我方转危主坐标子月未中、实于酉月丁未日病逝，大师「酉月或戌月未日」精确命中。'),
 'QM-007':('奇门·QM','E5-TIM','NA-列','差集中于 timing −1.00：伤可愈、出院双方同断；大师断最晚 5 月 20 日出院精确命中，我方出院主坐标取巳日——结局实出院日 5 月 20 日经大师断语对勘为丁巳日、与我方巳日同支，但结局文本本身无干支记载，评审以无从核对扣分（O 双视），定稿 timing 差照录、本席只登记此形态。'),
 'QM-008':('奇门·QM','E5-TIM','NA-列','差全在 timing −1.25：病重性命危方向双方同断，我方主坐标丙午日未中、实于癸亥日（5 月 26 日）去世，大师以值使临干断该日精确命中；病位（脑溢血）结局未载，双方同受此限。'),
}
A_MAIN=['GSZ-009','WHY-075','QW-013']
A_SUB={'WHY-073':'对方离婚带孩一面','WHY-074':'身份面（未领证同居之女）','WHY-079':'男友更替／新出现一面','QW-015':'丧父、兄官司坐牢两面','QW-016':'子女病残、妻流产一面','QW-017':'丧父一面'}
A_INV=A_MAIN+list(A_SUB)
AMB=['WHY-075','QW-013','WHY-079']
def se(p,n): return round(math.sqrt(p*(1-p)/n)*100,1)
from collections import Counter, OrderedDict
prim={c:CODING[c][1] for c in CODING}
def base(p): return '无失分主因' if p=='无失分主因' else ('E3' if p=='E3' else 'E5')
segs=OrderedDict([('全集',list(CODING)),('六爻·GSZ',[c for c in CODING if c.startswith('GSZ')]),('六爻·WHY',[c for c in CODING if c.startswith('WHY')]),('六爻全',[c for c in CODING if c.startswith(('GSZ','WHY'))]),('八字·QW',[c for c in CODING if c.startswith('QW')]),('奇门·QM',[c for c in CODING if c.startswith('QM')]),('非六爻',[c for c in CODING if c.startswith(('QW','QM'))])])
rows=[]
for name,cs in segs.items():
    cnt=Counter(base(prim[c]) for c in cs)
    rows.append((name,len(cs),cnt.get('E3',0),cnt.get('E5',0),cnt.get('无失分主因',0)))
e5sub=Counter(p for p in prim.values() if p.startswith('E5-'))
e5cases={}
for p in prim.values():
    if p.startswith('E5-'): e5cases.setdefault(p,[]).append([c for c in prim if prim[c]==p][0] if False else None)
e5cases={k:sorted([c for c in prim if prim[c]==k]) for k in e5sub}
assert sum(e5sub.values())==15 and len(A_INV)==9
rates={'OMIT':(e5sub['E5-OMIT'],e5sub['E5-OMIT']/25,0.200),'A_involved':(len(A_INV),len(A_INV)/25,0.44),'CLAIM':(e5sub['E5-CLAIM'],e5sub['E5-CLAIM']/25,0.280),'TIM':(e5sub['E5-TIM'],e5sub['E5-TIM']/25,0.120)}
L=[]
L.append('# DIAG-H21-fresh-r60 · holdout21 验收后诊断（R60 独立诊断席）\n')
L.append('- 角色与产出限（写死）：holdout21 验收后独立诊断角，未兼任本轮平台盲测／评审、验收盲测／评审、W 诊断与数据席。**只诊断、不改方法、不提修订方案**；诊断观察只登记事实形态，不写改法指令。')
L.append('- 对象：holdout21 全集 25 例（已开封、已用）。证据件：`runs/round60/acceptance/REPORT.md`、`runs/round60/acceptance/judging/final-scores.json`（per_case／segments／per_tradition）、同目录 `host-mapping.json` 与 judgeO1/O2/judgeM1/judgeM2.jsonl（reason 全文，只对勘定稿、未据其改分）、`runs/round60/acceptance/predictions/`（25 例 prediction_text＋basis）、`benchmark/phase3/holdout21/test_gold.jsonl`（已开封）、`holdout21/inputs/`、`data/holdout21-seal-log.md` §四–§六及 §五 QM-004/QM-007 裁处、对照基线 DIAG-H20 §2 汇总读数。')
L.append('- 验收定稿读数（承 REPORT，不重判）：我方 3.340 vs 大师 4.350，配对差 −1.010（SE 0.356），W/T/L 4/3/18，三判据全不立；双视无分歧、无仲裁。本席自分项（direction／claims／timing 双视均值）复算 25 例双方 total，与 final-scores 逐值一致（构建脚本断言全过）。\n')
L.append('---\n\n## §0 编码读法（照 DIAG-H20 §0 定本执行于本集，注明本集情形）\n')
L.append('1. **列面记录**＝prediction 的 prediction_text 与 basis 合并；**主导面**＝金标大师断语中与结局逐项对应、且决定该例胜负的断面，以结局实际转折所系者为准（承 h19/h20）。')
L.append('2. **E3（A 主标／A 涉，h19 原口径）**：A 主标＝主导面从未进入列面记录（含取象选择错误）；A 涉例＝A 主标例＋另有一次面（与所问同属一断面族、在金标断语中独立成句）经复核确认未入列之例（一例多面只计 1）。主导面本体已入列、义面／计数／应期未并读者不计 A，记附记并入 E5。')
L.append('3. **E4（二字段格）**：甲＝主导面锚点输入侧在场状态，乙＝席位侧处理状态；格：在场×未列且未登记→SEAT；不在场×已登记缺路→IN；已列为候选→NA-列；余格 MIX／UND。本集建集口径为锚点全在场，甲字段仍逐例按输入卡实读、不预设。')
L.append('4. **E5 主成因码（优先序写定）**：A 主标→E3；格 IN→E4；主导面已入列而失分→E5 细分 DIR（方向断反或相左）／CLAIM（具体断项被结局直接推翻）／TIM（应期主坐标错位）／OMIT（次面漏断：主导面已入列、已载事件之次面未断）；胜／平例记「无失分主因」。')
L.append('5. 含混例以注记登记不强判；金标断语成色事实照实登记于成色注记层、不预占主码。本集调整：无口径调整；分段改按本集构成（六爻 GSZ／WHY、八字 QW、奇门 QM）计。主导面识别以金标定稿为给定前提，本席未重定大师分数、未重评任何一例。\n')
L.append('---\n\n## §1 逐例归因表（25 例）\n')
L.append('分项记法：dir／claims／timing 为双视均值，格式 我方→大师。\n')
L.append('| 例 | 段 | diff | 分项 我方→大师 | 主成因码 | E4 格 | 一句话证据 |')
L.append('|---|---|---|---|---|---|---|')
order=['GSZ-003','GSZ-005','GSZ-009','GSZ-015','GSZ-016','GSZ-017','WHY-072','WHY-073','WHY-074','WHY-075','WHY-078','WHY-079','QW-013','QW-014','QW-015','QW-016','QW-017','QM-001','QM-002','QM-003','QM-004','QM-005','QM-006','QM-007','QM-008']
for cid in order:
    s=sub[cid]; pc=fs['per_case'][cid]
    f=lambda d:'%.2f→%.2f'%(d['direction'],0) # placeholder
    sub_s='%.2f→%.2f／%.2f→%.2f／%.2f→%.2f'%(s['ours']['direction'],s['master']['direction'],s['ours']['claims'],s['master']['claims'],s['ours']['timing'],s['master']['timing'])
    seg,pr,e4,ev=CODING[cid]
    prd = pr if pr=='无失分主因' else ('**E3 A 主标**' if pr=='E3' else pr)
    if cid in A_SUB and pr!='E3': prd+='（A 涉）'
    L.append(f'| {cid} | {seg} | {pc["diff"]:+.2f} | {sub_s} | {prd} | {e4} | {ev} |')
L.append('')
L.append('含混登记：含混 3/25——WHY-075（金标断语仅录身份面、主导面取身份面则 A 主标，取归否面则方向全反为 E5-DIR；本席按「金标断语中决定胜负的断面」读法取身份面为主导面、主码 E3，归断相反一节并记于证据句）；QW-013（手足面整体未入列近 A 主标，但本例为一生总断、结局可核项仅四项且分散于学历／手足／婚姻／弟刑四面，主导面权重取舍可议，主码按手足面占可核项之半取 E3）；WHY-079（差仅 −0.50、分项均匀小差，次面漏断 OMIT 与终局方向边界 DIR 两读并存，主码按 claims 持平、男友更替面未断取 OMIT）。含混点均落在主导面权重或分界，无一例锚点在场状态不可判；不可测 0 例。')
L.append('成色注记（不预占主码）：WHY-078 金标断语仅作用神要旨一例（见该例证据句）；QM-004 输入侧节题已经主持裁处剔除、QM-007 输入侧伤情细节按台账注记改写（封存日志 §三／§五），两例主码均按列面与结局实读、与成色无涉；QW 五例承「作者自选断准集」构成（大师侧基线被选集抬高属构成事实，承验收 REPORT §三），QW-017 另有结局成色薄注记（封存日志 §三）。\n')
L.append('---\n\n## §2 汇总计数（主成因码＋E3／E4 两层并报；份额带 n，比例带 SE，SE＝√(p(1−p)/n)）\n')
L.append('### 2.1 主成因码\n')
L.append('| 段 | n | E3 | E4 | E5 | 无失分主因 |')
L.append('|---|---|---|---|---|---|')
for name,n,e3,e5,nn in rows: L.append(f'| {name} | {n} | {e3} | 0 | {e5} | {nn} |')
L.append('')
L.append('- E5 细分（15 例）：DIR＝'+'、'.join(e5cases['E5-DIR'])+f"（{e5sub['E5-DIR']}）；CLAIM＝"+'、'.join(e5cases['E5-CLAIM'])+f"（{e5sub['E5-CLAIM']}）；TIM＝"+'、'.join(e5cases['E5-TIM'])+f"（{e5sub['E5-TIM']}）；OMIT＝"+'、'.join(e5cases['E5-OMIT'])+f"（{e5sub['E5-OMIT']}）；合 15。")
L.append('- 无失分主因 7 例＝胜 4（GSZ-005、GSZ-015、WHY-078、QM-004）＋平 3（GSZ-017、QW-014、QM-005），与定稿 W/T/L 4/3/18 逐例对应；负 18 例主码 E3 3＋E5 15、E4 0。\n')
L.append('### 2.2 E3 层（h19 原口径）\n')
L.append('| 段 | n | A 主标 | A 涉例（主标＋次标例） |')
L.append('|---|---|---|---|')
segA=[('全集',list(CODING)),('六爻·GSZ',segs['六爻·GSZ']),('六爻·WHY',segs['六爻·WHY']),('八字·QW',segs['八字·QW']),('奇门·QM',segs['奇门·QM']),('非六爻',segs['非六爻'])]
for name,cs in segA:
    am=[c for c in cs if c in A_MAIN]; ai=[c for c in cs if c in A_INV]
    L.append(f'| {name} | {len(cs)} | {len(am)}（{len(am)/len(cs)*100:.1f}%，SE {se(len(am)/len(cs),len(cs))}pp） | {len(ai)}（{len(ai)/len(cs)*100:.1f}%，SE {se(len(ai)/len(cs),len(cs))}pp） |')
L.append('')
L.append('A 主标 3 例：GSZ-009、WHY-075、QW-013。A 涉次标 6 例：'+'；'.join(f'{c}（{v}）' for c,v in A_SUB.items())+'。\n')
L.append('### 2.3 E4 层（二字段格，h19 原口径）\n')
L.append('| 段 | n | IN | SEAT | MIX | UND | NA-列 |')
L.append('|---|---|---|---|---|---|---|')
for name,cs in segA:
    st=[c for c in cs if CODING[c][2]=='SEAT']
    L.append(f'| {name} | {len(cs)} | 0 | {len(st)} | 0 | 0 | {len(cs)-len(st)} |')
L.append('')
L.append('落格 3 例（＝A 主标 3 例，逐例同一）：GSZ-009、WHY-075、QW-013——三例锚点均在场（六爻卦盘全列逐字、八字四柱全列）、主导面未入列且 basis 无缺路登记，故落 SEAT 而非 IN。**IN 在本集为 0，系逐例实读结果**：25 例输入卡锚点逐例在场（六爻卦象全列、八字四柱、奇门局式全载，QM-004 双局并载），无一例主导面锚点不在场。\n')
L.append('---\n\n## §3 REV1 判读读数（本席只给读数、不下 REV1 成立与否的结论；分母 N＝25）\n')
L.append('| 读数 | 本集（holdout21） | n/25 | DIAG-H20 基线 |')
L.append('|---|---|---|---|')
L.append(f"| OMIT 主码率 | {rates['OMIT'][1]:.3f} | {rates['OMIT'][0]}/25 | {rates['OMIT'][2]:.3f} |")
L.append(f"| A 涉率 | {rates['A_involved'][1]*100:.1f}% | {rates['A_involved'][0]}/25 | {rates['A_involved'][2]*100:.1f}% |")
L.append(f"| CLAIM 主码率 | {rates['CLAIM'][1]:.3f} | {rates['CLAIM'][0]}/25 | {rates['CLAIM'][2]:.3f} |")
L.append(f"| TIM 主码率 | {rates['TIM'][1]:.3f} | {rates['TIM'][0]}/25 | {rates['TIM'][2]:.3f} |")
L.append('| 总配对差（并记，非四率之一） | −1.010（SE 0.356） | 25 | −1.080 |')
L.append('')
L.append('四率读数如上，与基线并排供主持照写死线值判读；本席不作达线／破线结论。\n')
L.append('---\n\n## §4 限度\n')
L.append('1. 单编码限度：E3／E4／主成因码全部由本席单一编码者完成；含混 3/25（WHY-075、QW-013、WHY-079），若后续编码者对主导面权重处置不同，E3 主码计数可在含混例范围内摆动（摆动上限：E3 3→1、E5-DIR 3→4、E5-OMIT 2→3 之间）。')
L.append('2. 基数小：全集 25 例，八字段仅 5 例、单段 SE 大；§2 分段份额只作构成登记，不作显著性宣称。QW 大师均分 4.400 含作者自选「断准」集的选择偏倚（封存日志逐例 grade_note），影响外推解释、不改变本集内归因。')
L.append('3. 主导面以金标大师断语＋结局对应为给定前提：主导面定位若经独立复核移位，E3／E4／主码计数随之移位，本件无材料自查此环（与 h19/h20 同限度）。WHY-078 大师侧 0 分系金标断语成色事实（仅用神要旨），其胜例计入 W 与「无失分主因」均承定稿口径、本席照录不改。')
L.append('4. QM-007 的 timing 差含一层核验形态：我方巳日与实出院日丁巳同支，但结局文本无干支记载、评审无从核对——此形态只登记于该例证据句，不改变定稿分项与主码。\n')
L.append('---\n\n## §5 诊断观察（只登记事实形态，不作改法指令）\n')
L.append('1. 本集负例主码形态：E5 占负例 15/18，其中 TIM 与 CLAIM 各 5 例并列最多——TIM 5 例中奇门占 3 例（QM-006/007/008 均为病占死期／出院坐标错位或核验形态）、六爻 2 例；CLAIM 5 例中奇门占 3 例（QM-001 处所、QM-002 雨量级、QM-003 阴晴），八字 2 例（婚姻可守、破耗因由）。')
L.append('2. DIR 3 例全在六爻段（GSZ-016 录取、WHY-072 相亲、WHY-074 行人归否），均为终局方向整体反转，非子断或坐标问题；六爻段另有 E3 2 例（GSZ-009 取象面、WHY-075 身份面），六爻 12 例中方向／取面层失分合计 5 例。')
L.append('3. A 涉次标 6 例构成：六亲／婚育灾面 4（QW-015 丧父兄牢、QW-016 子病残妻流产、QW-017 丧父、WHY-073 带孩面），身份面 1（WHY-074），关系更替面 1（WHY-079）——与 h20 次标以六亲／婚育灾面为主的构成同形态，只作构成登记。')
L.append('4. 奇门段形态：绝对分全集最高（我方 4.781），8 例 direction 双视均值无一例低于 1.75，失分集中于 claims 细节与 timing 坐标两项；八字段失分形态与 h20 同类（可核事件漏断、断项被推翻、量级与结局不合），段配对差 −1.550 为全集最深。')
L.append('5. IN 连续两集为 0（h20、h21 均为锚点全在场建集）：落格例两集同为 SEAT 形态（锚点在场、主导面未入列、无缺路登记），h21 落格 3 例与 h20 同数。')
L.append('\n— 完 —\n')
md='\n'.join(L)
open(D+'/DIAG-H21-fresh-r60.md','w',encoding='utf-8').write(md)
out={'diagnosis':'DIAG-H21-fresh-r60','case_set':'holdout21','n':25,
 'acceptance':{'ours_mean':fs['main_caliber_low25']['ours_mean'],'master_mean':fs['main_caliber_low25']['master_mean'],'pair_diff':fs['main_caliber_low25']['pair_diff'],'SE':fs['main_caliber_low25']['SE'],'WTL':fs['main_caliber_low25']['W/T/L'],'pass':False},
 'subscore_recompute':'all 25 ours/master totals match final-scores',
 'per_case_primary':{c:(prim[c] if prim[c]!='无失分主因' else 'none') for c in order},
 'per_case_subscores':{c:{'ours':sub[c]['ours'],'master':sub[c]['master'],'diff':fs['per_case'][c]['diff']} for c in order},
 'primary_cause_counts':{name:{'n':n,'E3':e3,'E4':0,'E5':e5,'no_loss_cause':nn} for name,n,e3,e5,nn in rows},
 'E5_subtypes':{k:e5cases[k] for k in sorted(e5cases)},
 'E3_layer_h19_caliber':{'A_main':{'count':3,'share':0.12,'SE_pp':se(0.12,25),'cases':A_MAIN},'A_involved':{'count':9,'share':0.36,'SE_pp':se(0.36,25),'cases':A_INV},'A_sub_cases':A_SUB,'ambiguous':AMB},
 'E4_grid_h19_caliber':{'IN':0,'SEAT':3,'SEAT_cases':A_MAIN,'MIX':0,'UND':0,'NA_listed':22},
 'REV1_readings_N25':{'OMIT_primary_rate':{'value':rates['OMIT'][1],'count':rates['OMIT'][0],'baseline_h20':0.2},'A_involved_rate':{'value':rates['A_involved'][1],'count':rates['A_involved'][0],'baseline_h20':0.44},'CLAIM_primary_rate':{'value':rates['CLAIM'][1],'count':rates['CLAIM'][0],'baseline_h20':0.28},'TIM_primary_rate':{'value':rates['TIM'][1],'count':rates['TIM'][0],'baseline_h20':0.12},'pair_diff':{'value':-1.01,'baseline_h20':-1.08},'note':'readings only; no REV1 verdict by this seat'},
 'ambiguous':AMB,'unmeasurable':0,
 'quality_notes':{'WHY-078':'gold master_prediction only yongshen gist, no concrete claim; master scored 0 by both views (REPORT s.1)','QM-004':'section-title outcome info removed from input side by host ruling (seal log s.5)','QM-007':'input context rewritten per ledger note (seal log s.3)','QW-017':'thin outcome (seal log s.3)','QW_segment':'author-selected verified-accurate collection (grade_note)'}}
json.dump(out,open(D+'/DIAG-H21-fresh-r60.json','w',encoding='utf-8'),ensure_ascii=False,indent=1,sort_keys=True)
print('written', os.path.getsize(D+'/DIAG-H21-fresh-r60.md'), os.path.getsize(D+'/DIAG-H21-fresh-r60.json'))
print('rates', rates)
