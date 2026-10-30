# -*- coding: utf-8 -*-
"""R47 supply ledger writer. Assertions inline; run from repo root."""
import json, pathlib
OUT = pathlib.Path('benchmark/phase3/runs/round47/digestion/supply-ledger-r47.jsonl')
rows = []
def row(**kw): rows.append(kw)

# carried from R46
row(case_key='LK-058', source='类考(leikao)', system='mengzhan', round_banked='R46',
    verdict='counted', cumulative_after=1,
    note='R46 入账承前；R47 席 C 对勘：逸旨卷六印刷 59-60 同载此案（梦者名作伯鄰），两书同载只计一例、不重复计产、不撤销入账。')
# YZ-C019
row(case_key='YZ-C019', source='梦占逸旨 卷六篇十三(寿命篇)', system='mengzhan', round_banked='R47',
    verdict='counted', cumulative_after=2,
    note='回源逐字复核过：占者索紞（visual 高置信两见）；断语逐字「棺者，職也，當有京師貴人舉君。二棺者，□□。」（到货本作職，非 R46 转述之官）；结局纲目级「再遷」为编集者明载之具体结果、与断语可分离，与 yw-mo「後果然」判 A 附保留先例同口径。限度二项逐字登记：断语尾二字栏末漫漶未读定（挂起不臆补）；结局仅纲目级。页位印刷 55＝PDF 60。与 YZ-C020 异人异事对勘维持。')
# near-pool re-review
row(case_key='LK-046', source='类考(leikao)', system='mengzhan', round_banked='R47',
    verdict='counted', cumulative_after=3,
    note='近池复议入账：标志短语精确检索零命中＋传主无任何条目＋无类书著录，冷门性新证据落盘（NEARPOOL-review-r47.md），污染 mid→low 主持核定；判级 A 成立维持。')
row(case_key='LK-054', source='类考(leikao)', system='mengzhan', round_banked='R47',
    verdict='counted', cumulative_after=4,
    note='近池复议入账：污染降 low 主持接受；判级 A 成立——自解在登科之前属真预测，与 LK-062 事后自悟有别（NEARPOOL-review-r47.md）。')
row(case_key='LK-085', source='类考(leikao)', system='mengzhan', round_banked=None,
    verdict='not_counted',
    note='不入账：系梦中告语直告型（「君年逾四十当贵」无解码文本），依 PREREG §1⑦ 直告型不入池；污染降档复议就此作罢。席位所提传主裴叔名全未定之限度并记。')
for k, why in [('LK-024','维持 mid：源书《稽神录》有太平广记采入 220 余事之宽通道、本条在列未证，冷门性证据不足。'),
               ('LK-062','维持：徐元杰《宋史》卷 424 有传＋百科专条＋文集存世，反证强；且其自悟在事后，判级面亦不利。'),
               ('LK-009','维持：陈奇《太平御览》卷 972 引《十六国春秋·前凉录》著录＋百科专条，反证强。附带：维基转述作解者索紞/断字未字/结局停舉孝廉，与类考 R46 读法（索统/木字/斌果停）不同，疑 R46 读误二字——只登记，入 R48 回类考原页复核。'),
               ('LK-039','维持：陈奇《北史》本传，名案面未除。'),
               ('LK-073','维持：梁武帝/萧绎帝王级，污染 high 面未除。')]:
    row(case_key=k, source='类考(leikao)', system='mengzhan', round_banked=None,
        verdict='not_counted', note=why)
# gaoyu typing
for k in ['LK-093','LK-043','LK-057','LK-083']:
    row(case_key=k, source='类考(leikao)', system='mengzhan', round_banked=None,
        verdict='not_counted',
        note='告语型归型＝直告型（GAOYU-typing-r47.md，主持核定接受）：依 PREREG §1⑦ 不入池，只登记。')
# yijian mining
for k, src in [('YJ-001','夷坚志(在线实取 hugbear 全文)'), ('YJ-004','夷坚志(在线实取 hugbear 全文)'), ('YJ-006','夷坚志(在线实取 hugbear 全文)')]:
    row(case_key=k, source=src, system='mengzhan', round_banked='R47', verdict='counted',
        cumulative_after={'YJ-001':5,'YJ-004':6,'YJ-006':7}[k],
        note='主持逐卡核查过：A 级＋污染 low＋三键去重无撞＋输入/金标可分离（MINING-yijian-r47.md＋cards-mining-yijian/）。')
row(case_key='YJ-002', source='夷坚志(在线实取)', system='mengzhan', round_banked=None, verdict='registered_only',
    note='A 级但污染 high，只登记。')
row(case_key='YJ-007', source='夷坚志(在线实取)', system='mengzhan', round_banked=None, verdict='registered_only',
    note='A 级但污染 high，只登记。')
row(case_key='YJ-003', source='夷坚志(在线实取)', system='mengzhan', round_banked=None, verdict='not_counted',
    note='B 级：问辞含「人言梦棺得官」民俗语、可分离性存疑，不入账。')
row(case_key='YJ-005', source='夷坚志(在线实取)', system='mengzhan', round_banked=None, verdict='not_counted',
    note='B 级＋污染 mid，不入账。')
# xuanjie candidates counted
xj_counted = {
 'XJ47-047':'A/low 主持核定：自占逐字、结局独立详载；与 LK-009/LK-039 之北朝陈奇异代异人、三键不撞。结局「謗」字待核不碍方向与可分离。',
 'XJ47-092':'A/low：自占长文、结局跨年详载，输入/金标可分离。',
 'XJ47-289':'A/low：自占、结局详载且坠梯应于丁忧一节非复述断语。',
 'XJ47-373':'A/low：傅恕断语含转述乡占成分，建卡时须注明；断语具体（第六名）、结局独立。',
 'XJ47-386':'A/low：子为父占、断语逐字、结局独立。',
 'XJ47-442':'A/low：结局含数字独立覆核（欠柴千七百束与官账符），成色最强一类。',
 'XJ47-500':'A/low：自解逐字、结局独立（乙丑状元）。',
 'XJ47-502':'A/low：自占逐字、结局独立；断语与结局落差（祿至而居第二）如实记，金标以结局为准。',
}
cum = 7
for k in ['XJ47-047','XJ47-092','XJ47-289','XJ47-373','XJ47-386','XJ47-442','XJ47-500','XJ47-502']:
    cum += 1
    row(case_key=k, source='梦林玄解 梦征(PDF 1052-1213)', system='mengzhan', round_banked='R47',
        verdict='counted', cumulative_after=cum, note=xj_counted[k])
assert cum == 15, cum
xj_not = {
 'XJ47-036':'B 级（结局仅「果如其言」确认式、无具体内容）＋low-mid，不入账。主持裁定：确认式短语零内容者 (ii) 不立，与 YZ-C019 纲目级载具体结果「再遷」有别。',
 'XJ47-076':'A 级但污染 mid（晋书索统传系本传名段），不入账。',
 'XJ47-081':'A 级但污染 mid（与 076 同源索统传），不入账。',
 'XJ47-222':'B 级＋污染 mid＋处方型断语复合（脩桥延寿），不入账；处方型属性只登记。',
 'XJ47-267':'B 级（结局确认式）＋躒字待核，不入账。',
 'XJ47-338':'A 级但污染 mid（晋书忠义传系），不入账。',
 'XJ47-345':'B 级文本极简，不入账。',
 'XJ47-368':'B 级（结局确认式＋梦者名待核），不入账。',
 'XJ47-371':'A 级但污染 mid（唐人史传系）＋占者名待核，不入账。',
 'XJ47-393':'B 级＋污染 mid＋结局末句残，不入账。',
 'XJ47-428':'B 级＋污染 mid-high：三国志吴书丁固本传名段、梦书高频引例——主持裁定仍触 (iii) 名案预判线，不入账。',
 'XJ47-469':'B 级文本简，不入账。',
 'XJ47-495':'B 级（忧虑式自述断语）＋low-mid＋梦者名待核，不入账。',
}
for k, why in xj_not.items():
    row(case_key=k, source='梦林玄解 梦征(PDF 1052-1213)', system='mengzhan', round_banked=None,
        verdict='not_counted', note=why)
# seat C registrations
row(case_key='REGISTER-yizhi-waipian', source='梦占逸旨 外篇', system='mengzhan', round_banked=None,
    verdict='path_summary',
    note='未登存文 31 页逐页实检：分母 363 条、四滤淘汰 359、同案互见剥离 4 条（李伯邻梦洗马＝LK-058 只计一例）、精读候选 0、新入账 0。瓶颈在体例：有断语者皆名案、非名案者无占者。结构校正：篇十一＝科甲篇、篇十三＝寿命篇（正 R46 存疑）。')
row(case_key='REGISTER-leikao-cont', source='类考(leikao) 续读', system='mengzhan', round_banked=None,
    verdict='path_summary',
    note='本轮实读新页 38 页（PDF 21-29、31-49、51-60；PDF 30 与 R46 重叠已剔除），余约 352 页未读逐段登记不充数——与 PREREG §1⑤ 任务量有缺口，入 R48 议程。分母 163 条、互见剥离 36、新登 127、四滤淘汰 116、精读候选 11 例（LK2-C01…C11）、low 为 0、新入账 0；LK2-C01/C02 为 low-mid，列 R48 近池复议候选。')
row(case_key='REGISTER-xuanjie-mengzheng', source='梦林玄解 梦征五卷', system='mengzhan', round_banked=None,
    verdict='path_summary',
    note='连号 592 扣并入号 1、实条 591；四滤首要淘汰：(i) 299、(iii) 256、全过 21、R46 既登回遇 15（不重复计产）。转录全程 visual（本机无 tesseract，如实标注）。对 R46 采样三处校正：沈瑀（非沈雲）、陈武帝（非梁武帝）、理母思瓜人名异读宋瓊 vs 理/瓌——只涉登记文本、不涉入账例，作 errata 登记。')
row(case_key='SUMMARY', source='-', system='-', round_banked='R47', verdict='summary',
    cumulative_total=15, trigger_line=13, trigger_fired=True,
    note='累计 15/13，数量触发达成。构成可行性另见 PREREG-ADDENDUM-1：总量 15＜25 且 15 例全梦占（单体系 100%＞50%），四限度 (2) 两款均不合，holdout19 本轮不组集（R45 先例口径）。R48 绑定约束＝新鲜合规非梦占非六壬 ≥15 例（算式见 ADDENDUM）。各路径四滤产出率：复核路 3/9（YZ-C019＋近池 2/8）、告语归型 0/4、夷坚 3/（四滤淘汰逐例点名后精读 7）、玄解 8/591（A-low 8/21 候选）、逸旨外篇 0/363、类考续读 0/163（本轮实读面）。')
with OUT.open('w', encoding='utf-8') as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
counted = [r for r in rows if r.get('verdict') == 'counted']
assert len(counted) == 15, len(counted)
assert counted[-1]['cumulative_after'] == 15
print('ledger rows:', len(rows), '| counted:', len(counted), '| cumulative final: 15')
