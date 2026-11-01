# -*- coding: utf-8 -*-
import json, pathlib
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round94')
block = [json.loads(l) for l in open(base/'judging/judgeY-block2.jsonl', encoding='utf-8') if l.strip()]
anons = [r['anon_id'] for r in block]
# items 83-122
S = [
(2,2,2,"无"),
(2,2,1,"位极人臣高寿果应；应期无时点可核（中性记1）"),
(2,2,2,"无"),
(1,1,1,"保位面合而难大升被证伪（月内实授天津巡抚）；应期无具名时点可核（中性记1）"),
(2,2,2,"无"),
(1,1,1,"中否结局未明载、仅以补官间接对应，断语无从证实；应期无时点可核（中性记1）"),
(1,1,1,"父子相逢果应于子嗣面，然系失散子见归、非所断再得子；应期尺度近而坐标未明"),
(2,2,1,"不治而死果应、十二日合旬月尺度；无主坐标可对，记部分对齐"),
(2,2,2,"无"),
(2,2,0,"自病果愈；主坐标旬内戌日与实际卯月愈不对齐"),
(1,1,1,"终局如常面合而过程反：主坐标巳日实为变症疼痛之日、申日才定，记部分对齐"),
(2,1,0,"雨止天开果应而时点偏：实际当日酉时晴、非所断寅日，次日又雨"),
(0,0,1,"所问房价面无验，所载午月覆舟亡与断语无涉；仅午字尺度相邻"),
(2,1,1,"赃鱼部分寻回果应，贼人水上营生一层结局未载；应期无具名时点可核（中性记1）"),
(2,2,1,"在赦内果应脱解；主坐标寅月与实际壬戌日赦无从对齐，记部分对齐"),
(0,0,0,"方向反转：断店可开待利，实际六月病、八月财物盗尽；应期亦不对齐"),
(2,2,1,"仆果至；主坐标酉日与实际甲寅日偏，窗口含而坐标偏"),
(0,0,0,"方向反转：断父病危重、人参不宜，实际次日不药而愈；应期亦不对齐"),
(2,2,1,"败选与罢免通过果应、年内去职合；无确日坐标，记部分对齐"),
(2,2,2,"无"),
(0,0,2,"方向反转：断岳母病愈，实际乙酉日死；时点恰落所断酉日，故应期对齐而方向 claims 皆反"),
(0,0,0,"方向反转：断病可愈，实际卒于丑月；应期亦不对齐"),
(2,2,2,"无"),
(2,1,1,"寻回并遇于岳家合相熟之家一层，西向未证；应期无时点可核（中性记1）"),
(2,2,1,"子病果死本日，危重果应；主坐标午日与实际本日辰时坐标偏、危期即至面合"),
(0,0,0,"所断到任面无验，所载七月渴死与断语相反；应期亦不对齐"),
(2,2,1,"当晚雨停果应；主坐标申时未获单证，窗口数小时合、记部分对齐"),
(2,2,1,"讼终未成果应；应期无时点可核（中性记1）"),
(0,0,1,"方向反转：断财可得中上，实际求之不得；结局无时点可核（中性记1）"),
(2,2,1,"统治山西三十八年果应；应期无时点可核（中性记1）"),
(2,2,1,"财果入手；主坐标亥日与实际次日戊申偏，窗口含而坐标偏"),
(2,2,2,"无"),
(2,2,2,"无"),
(2,2,1,"子果归；主坐标酉日偏，实际当日即归早于所断，窗口含"),
(2,1,1,"得官果应且历转巡抚都御史，量级远超所断五至七品带；应期无时点可核（中性记1）"),
(2,2,0,"子病果死；主坐标酉日与实际午日午时不对齐"),
(2,2,2,"无"),
(1,1,1,"行程遇兵不能进果应，然京授巡抚一层未断；母安稳面仅就近段、寿终在后年"),
(2,1,0,"过考果应而等第反：断中上非最优，实际得上上卷；应期亥月巳日与实际次年孟夏不对齐"),
(2,1,1,"次年冬推补兵部车驾司、得职量级合；主坐标戌年未获证实，记部分对齐"),
]
assert len(S)==40, len(S)
outp = base/'judging/judgeY2-scores.jsonl'
with open(outp,'a',encoding='utf-8') as f:
    for j,(d,c,t,g) in enumerate(S):
        i=82+j; tot=d+c+t
        f.write(json.dumps({"anon_id":anons[i],"direction":d,"claims":c,"timing":t,"total":tot,"pass":tot>=4,"gap_note":g},ensure_ascii=False)+"\n")
print("chunk3 appended")
# self-verify
lines=[l for l in open(outp,encoding='utf-8') if l.strip()]
rows=[json.loads(l) for l in lines]
assert len(rows)==len(block)==122, (len(rows),len(block))
assert [r['anon_id'] for r in rows]==anons, "anon set/order mismatch"
for r in rows:
    assert r['total']==r['direction']+r['claims']+r['timing']
    assert r['pass']==(r['total']>=4)
    assert all(r[k] in (0,1,2) for k in ('direction','claims','timing'))
tot=sum(r['total'] for r in rows); npass=sum(1 for r in rows if r['pass'])
print("rows",len(rows),"mean",round(tot/len(rows),3),"pass",npass,"sum",tot)
