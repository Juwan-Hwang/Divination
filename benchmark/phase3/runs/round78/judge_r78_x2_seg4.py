import json

BASE = '/home/hatch/workspace/divination/benchmark/phase3/runs/round78'
rows = [json.loads(l) for l in open(f'{BASE}/judging/judgeX-block2.jsonl')]
seg = rows[90:122]
expected = [r['anon_id'] for r in seg]

S = [
 ("P3-6cdacee0",2,2,2,"仆向西略南去金斯顿近泰晤士，周五自归，向西近水与数日内归皆精确应验"),
 ("P3-6d85603d",2,1.5,1.5,"历任法院院长、法学院院长，司法领袖向应验，1986年卒享年八十七合八十余寿数；国际名望一节未分载"),
 ("P3-6e611562",2,2,0.5,"果生女、产母平安，女胎与平安双验；壬申日与亥月产期坐标不合"),
 ("P3-6efde2f3",2,1.5,2,"其后午月方获，得会与午月主坐标精确应验"),
 ("P3-704fd208",0,0.5,0,"断关差不成，卽于壬寅日得差反；次年死于中途非断语所载；亥日不合"),
 ("P3-70c5038c",2,2,2,"蒋介石1936年12月25日获释飞离、未受人身伤害，有惊无险与12月下旬坐标精确应验"),
 ("P3-70d42aa1",2,2,1,"陈诚官至副总统、行政院长，副元首级僚佐定位精确应验；运段应期结局无可核时点"),
 ("P3-7181c2b4",0,0,0,"断功名不成，果中经魁、胞弟又发，全反"),
 ("P3-73c3c3fe",2,1.5,1,"父果于申时到，归向应验；子日主坐标未明字载"),
 ("P3-7410f1bb",2,1.5,2,"申新经整顿存续、荣宗敬本人1938年卒而事业未再大振，近远两段与1938坐标应验；分持细节未载"),
 ("P3-75893327",1.5,1.5,0.5,"子果于卯年得意而归，在世与归期遥远应验；归期超一年窗口，酉月音信未载"),
 ("P3-75a3a893",1.5,1,1,"吴佩孚1927年后下野寓居北平、1939年卒，统帅级后失势向应验；清贫与病因细节结局未载"),
 ("P3-76eeaee8",2,2,2,"韩国瑜2019年4月表态、7月赢初选成候选人，参选与年中定案坐标精确应验"),
 ("P3-76fbc73f",2,1.5,0,"果于巳年得县缺，有官应验；寅年主坐标不合"),
 ("P3-77820b60",2,2,1.5,"雷丁以投降和约交付、围城数周，方式与迟滞应验；交付日较自限晚三日"),
 ("P3-789e9353",2,1.5,2,"蔡英文以817万票史上最高票连任、民进党保立院过半；先低后高过程结局未分载；2020年1月坐标合"),
 ("P3-799cb580",2,1.5,1,"往粤东买货归俱得大利，得利应验；结局无可核时点"),
 ("P3-79af7240",1,1,1.5,"本日巳时先还一半与今日不还半反，乙酉日还清应验酉日转机坐标"),
 ("P3-7a63442a",2,1.5,0,"久病果卒于申日，凶向应验；亥月主坐标不合"),
 ("P3-7a67cc12",2,1.5,0.5,"弟兄次日乃至，可到应验；卯日辰时时点混载与酉日主坐标不合"),
 ("P3-7aada01e",2,2,2,"仆果向东逃，周五得信、周日被捕，向东与短期内被获精确应验"),
 ("P3-7be00a3c",0.5,0.5,1,"后知来客为荆州知府进士，非显达贵客一断反，阴柔不实诸象无载；结局无可核时点"),
 ("P3-7c66cf57",2,1.5,0.5,"在狱者果蒙赦出狱、后历仕途显要，脱狱应验且超预期；壬戌日赦与亥月坐标邻近未精确合"),
 ("P3-7c70edac",2,1.5,0.5,"果于卯日过关并无阻滞，过关成向应验；申日主坐标不合"),
 ("P3-7cc2ca58",2,2,2,"莫迪领导人民党得303席、联盟组阁连任，胜选与计票揭晓坐标应验"),
 ("P3-7dedd4b6",2,1.5,1,"后果取超等补廪，岁考成向应验；结局无可核时点"),
 ("P3-80fd7c9e",2,2,2,"郭台铭未获征召、独立参选后退选，赖清德2024年1月13日当选，全项精确应验"),
 ("P3-8330b9f4",2,2,2,"英国2016年6月23日公投脱欧派以51.9%胜出，胜负与结果时点精确应验"),
 ("P3-8361e0c1",2,2,2,"谭延闿1930年9月22日以国民政府主席任内因脑溢血逝世，位级、死因与1930年坐标精确应验"),
 ("P3-83a583f9",0,0,0,"射覆断巾帕织物一件，开帨实为牛黄二块，类属与件数全错；预测断语本身无应期"),
 ("P3-83a8b790",1.5,1,0,"官职果于孟春迁级，可得一层应验；午月主坐标不合"),
 ("P3-8468ae34",2,1.5,1,"果于次日用针而愈，愈向应验；申日主坐标未明载"),
]
assert [s[0] for s in S] == expected, 'anon_id set/order mismatch seg4'
out = []
for anon, d, c, t, reason in S:
    total = d + c + t
    out.append(json.dumps({"anon_id": anon, "direction": d, "claims": c, "timing": t,
                           "total": total, "pass": total >= 4, "reason": reason}, ensure_ascii=False))
with open(f'{BASE}/judging/judgeX-block2-scores.jsonl', 'a') as f:
    f.write('\n'.join(out) + '\n')
print('seg4 written', len(out), 'pass', sum(1 for s in S if s[1]+s[2]+s[3] >= 4))

# final assertions: total lines and anon_id set equality against this packet only
pkg_ids = [r['anon_id'] for r in rows]
scored = [json.loads(l) for l in open(f'{BASE}/judging/judgeX-block2-scores.jsonl')]
assert len(scored) == len(pkg_ids) == 122, 'final line count mismatch'
assert [s['anon_id'] for s in scored] == pkg_ids, 'final anon_id set/order mismatch'
for s in scored:
    assert abs(s['total'] - (s['direction'] + s['claims'] + s['timing'])) < 1e-9
    assert s['pass'] == (s['total'] >= 4)
    for k in ('direction', 'claims', 'timing'):
        assert 0 <= s[k] <= 2 and (s[k] * 2) == int(s[k] * 2)
print('FINAL OK lines', len(scored), 'pass_total', sum(1 for s in scored if s['pass']))
flag1 = [s['anon_id'] for s in scored if s['direction'] <= 0.5 and s['total'] >= 4]
print('flag1 direction<=0.5 & total>=4:', flag1)
