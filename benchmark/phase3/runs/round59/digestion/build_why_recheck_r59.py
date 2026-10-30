# -*- coding: utf-8 -*-
"""R59 数据/开采席 任务二: WHY partial 面续采复核 (SUPPLY-RECHECK-why-partial-r59).
逐例回原书扫描页 (PDF 渲染读图) 复核; 数据为本席读图实录.
原书: incoming/wanted-books-4/Book/六爻分类占验技法 (王虎应著).pdf (扫描本无文字层)
印刷页->PDF页: PDF k 页 = 印刷 (2k-2, 2k-1) 页, 右半为先行页."""
import json, hashlib, os

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
BOOK = '/home/hatch/workspace/divination/incoming/wanted-books-4/Book/六爻分类占验技法 (王虎应著).pdf'

# (id, 组, 原锚, 原污染, 原资格, 复核锚, 复核资格, 定案, 依据, 原文定位)
C = []
def add(*a): C.append(a)

DEDUP = '维持不入账（去重）'
MIDP = '维持（present·mid 不入账）'
PART = '维持 partial'
# ---- R57 去重 8 例 ----
add('WHY-076','r57-去重','present','low',False,'present',False,DEDUP,
 '本席回原书读图：例题首「戊寅丙辰月丁亥日，某女測夫妻緣分得地山謙變雷火豐卦」与卦盘（兄弟酉金龍／子孫子水世武／父母丑土×虎／兄弟申金蛇／官鬼午火應勾／父母辰土×雀）俱在，与分类版台账三键（本变卦＋占月日＋问事）全合；同案 GSZ-297 已在册（GSZ 席台账），去重不入账维持。台账所记五爻子/亥异文，本席读图为子孫子水，与分类版读法一致。',
 '《分类占验技法》第四章例四，印刷 p91（PDF p46 左半）')
add('WHY-077','r57-去重','present','low',False,'present',False,DEDUP,
 '例题首「丁丑年壬子月壬辰日，某男測妻生孩子，得天澤履變天水訟卦」与卦盘、应验情况（1999 年 3 月同居女子吵翻、堕胎、不欢而散）俱在，三键全合；同案 GSZ-296 已在册，去重维持。',
 '第四章例五，印刷 p92–93（PDF p47）')
add('WHY-094','r57-去重','present','low',False,'present',False,DEDUP,
 '例题首「戊寅年丙辰月癸巳日，一位八十六歲的老婦人測年運得地天泰變水雷屯卦」与卦盘、应验情况（巳月腿部发肿卧床一月）俱在，三键全合；同案 GSZ-008 已用（dev 集），去重维持。分类版应验作「巳月」与 GSZ 版「五月」之异文，台账已登记。',
 '第六章例七，印刷 p127（PDF p64 左半）')
add('WHY-097','r57-去重','present','low',False,'present',False,DEDUP,
 '例题首「亥月丙寅日，某女測住房風水得風澤中孚變巽為風卦」与卦盘俱在，三键全合；同案 GSZ-152 已在册，去重维持。',
 '第八章例一，印刷 p167（PDF p84 左半）')
add('WHY-101','r57-去重','present','low',False,'present',False,DEDUP,
 '例题首「亥月辛酉日，某男測叔叔家風水得水地比變坤為地卦」与卦盘俱在，其应验尾段（月经不调、回娘家）见次页，三键全合；同案 GSZ-149 已在册，去重维持。',
 '第八章例五，印刷 p171–172（PDF p86 左半、p87 右半）')
add('WHY-105','r57-去重','present','low',False,'present',False,DEDUP,
 '例题首「子月癸巳日，某男測店風水得澤山咸變天山遯卦」与卦盘、应验情况（书店改饭店、拓宽马路拆去一半）俱在，三键全合；同案 GSZ-153 已在册，去重维持。',
 '第八章例八，印刷 p174（PDF p88 右半）')
add('WHY-113','r57-去重','present','low',False,'present',False,DEDUP,
 '例题首「庚辰年甲申月丁酉日剛交節令十幾分鐘後，我被請到醫院，陽曲縣一老婦測病得澤天夬變澤火革卦」与卦盘、应验情况（2001 年搬五层、整修、儿子病愈）俱在，三键全合；同案 GSZ-189 已在册，去重维持。',
 '第十章例五，印刷 p196（PDF p99 右半）')
add('WHY-116','r57-去重','present','low',False,'present',False,DEDUP,
 '例题首「己卯年丁卯月甲子日，化二建的張某求測自己的病搖得澤天夬變雷天大壯卦」与卦盘、应验情况（庚辰年邻居告知张某已于己卯年死）俱在，三键全合；同案 GSZ-192 已在册，去重维持。',
 '第十章例四，印刷 p200–201（PDF p101）')
# ---- R57 其余 2 例 ----
add('WHY-102','r57-锚点','partial','low',False,'partial',False,PART,
 '本席回原书读图坐实：例六篇题「某男測店中風水得火天大有變離為火卦」无占时行（年月日全缺），卦盘与判断、应验段（酉月一店员因交通事故受伤，一九九七年因经营不景气搬迁）俱在；判断中「月建」仅抽象提及、无具体月建日辰可录，不得以推定补锚。锚点 partial 系原书结构性缺占时，维持。',
 '第八章例六，印刷 p172–173（PDF p87）')
add('WHY-117','r57-滤二','present','low',False,'present',False,'维持不入账（滤二未过）',
 '本席回原书读图坐实：该例应验情况全文仅「以上推斷果然應驗。」一语，无任何具体事实复述，结局不合「独立成文具体」滤；锚点 present（卦盘全列）维持，资格维持不入账。',
 '第十章例五，印刷 p202–203（PDF p102）')
# ---- R56 天气 partial 3 例 ----
add('WHY-001','r56-天气','partial','low',False,'partial',False,PART,
 '本席回原书读图：例一本卦六爻（父母子水／妻财戌土／兄弟申金×／兄弟酉金／子孙亥水／妻财丑土，世应俱标）可辨，变卦列为黑色斑驳带覆盖未全辨，与台账「扫描斑驳」登记合；按全列口径维持 partial。',
 '第一章例一，印刷 p9–10（PDF p5 左半、p6 右半）')
add('WHY-002','r56-天气','partial','low',False,'partial',False,'维持 partial（缺项收窄）',
 '本席读图：本卦六爻全列＋六神＋动爻标记（子孙申金×）＋世应在原扫描下俱可辨；唯变卦（泽地萃）六爻列斑驳未全辨。缺项较台账原记收窄，然变卦全列未达，维持 partial。',
 '第一章例二，印刷 p10–11（PDF p6 左半）')
add('WHY-029','r56-神秘','partial','low',False,'partial',False,'维持 partial（缺项收窄＋台账变卦出处待核）',
 '本席读图补录本卦全列：离为火——兄弟巳火世白虎／子孙未土螣蛇／妻财酉金勾陈／官鬼亥水应朱雀／子孙丑土青龙／父母卯木玄武，六神世应俱在；应验情况「預測是正確的，蛇沒有出現。」在场。惟该例页段（印刷 p55–57）正文仅作「得離為火卦」，判断亦未及动爻与变卦，卦盘无动爻标记可辨；台账原录变卦「火山旅」之出处未在该页段检得，不得以推定补锚，维持 partial 并登记台账变卦出处待核。',
 '第三章笔仙例，印刷 p55–57（PDF p28 左半、p29）')
# ---- R56 地震 present+mid 6 例 ----
EQ = '卦盘全列（六爻＋六神＋世应＋动爻）经本席读图抽验在场，判断与应验情况俱独立成文；污染 mid 系作者自占自验之公开流传面（作者自占、事后见报/受访流传），非页读可裁，维持原判；入账门槛 low 未过，维持不入账。'
for i, loc in [('WHY-013','第二章例一，印刷 p28–31（PDF p15–16）'),
               ('WHY-014','第二章例二，印刷 p31–32（PDF p16–17）'),
               ('WHY-017','第二章例五，印刷 p35–36（PDF p18–19）'),
               ('WHY-018','第二章例六，印刷 p36–38（PDF p19–20；台账原记 p37–38，例题首实在 p36）'),
               ('WHY-019','第二章例七，印刷 p37–38（PDF p19–20）'),
               ('WHY-020','第二章例八，印刷 p38–40（PDF p20–21）')]:
    add(i,'r56-地震','present','mid',False,'present',False,MIDP,EQ,loc)
# ---- R56 股票 present+mid 6 例 ----
STK_PRE = '维持（present·mid 不入账）'
add('WHY-045','r56-股票','present','mid',False,'present',False,STK_PRE,
 '例题首「戌月丙寅日，測第二天日本股票尼森的價格變化得火澤睽變火水未濟卦」与卦盘全列（六神俱在）经读图在场；污染 mid 维持，不入账。','第九章一日例二，印刷 p145（PDF p73 左半）')
add('WHY-046','r56-股票','present','mid',False,'present',False,STK_PRE,
 '例题首「戌月丁卯日，測第二天日本股票尼森漲跌情況得兌為澤變地澤臨卦」与卦盘全列（六神俱在）经读图在场；污染 mid 维持，不入账。','第九章一日例三，印刷 p146（PDF p74 右半）')
add('WHY-047','r56-股票','present','mid',False,'present',False,STK_PRE,
 '例题首「戌月戊辰日，測第二日尼森股票的變化情況得風天小畜卦」与卦盘全列（六神俱在）经读图在场；污染 mid 维持，不入账。','第九章一日例四，印刷 p146（PDF p74 右半）')
add('WHY-048','r56-股票','present','mid',False,'present',False,STK_PRE,
 '例题首「戌月辛未日，測第二天日本尼森股票的變化情況得雷火豐變雷山小過卦」在场；惟本席放大读图确认：该盘原书未印六神列（其余锚点要素全在场）。原席判 present，与同章判 partial 诸例（WHY-050/051 等同为无六神列）口径不一致——本席维持原判，六神是否属锚点要件之定义分歧另节登记提请主持裁；无论何裁，本例污染 mid、不入账，可选集无影响。','第九章一日例五，印刷 p147（PDF p74 左半，卦盘放大复核）')
add('WHY-049','r56-股票','present','mid',False,'present',False,STK_PRE,
 '例题首「戌月辛未日，森田先生也搖卦測尼森股票第二天的變化情況得兌為澤變乾為天卦」在场；卦盘原书未印六神列（余要素全在场），同 WHY-048 注：维持原判 present，定义分歧另节登记；污染 mid 不入账。','第九章一日例六，印刷 p148（PDF p75 右半）')
add('WHY-052','r56-股票','present','mid',False,'present',False,STK_PRE,
 '例题首「亥月甲戌日，測第二天尼森股票變化情況得火地晉變天水訟卦」在场；卦盘原书未印六神列（余要素全在场），同 WHY-048 注：维持原判 present，定义分歧另节登记；污染 mid 不入账。','第九章一日例九，印刷 p149–150（PDF p75 左半、p76 右半）')
# ---- R56 股票 partial+mid 17 例 ----
STK_PART_BASIS = '本席逐页读图：例题首（占月日＋问事＋本变卦名）、卦盘六爻全列＋动爻＋世应、判断与应验情况（次日尼森股价具体涨跌数值）俱在场；卦盘原书未印六神列（本章一日/一周/买卖诸例版式通例），与台账 partial 所指缺项一致，维持 partial；污染 mid 维持，不入账。'
for i, loc in [('WHY-050','第九章一日例七，印刷 p148–149（PDF p75）'),
               ('WHY-051','第九章一日例八，印刷 p149（PDF p75 左半）'),
               ('WHY-053','第九章一日例十，印刷 p150（PDF p76 右半）'),
               ('WHY-054','第九章一日例十一，印刷 p151（PDF p76 左半）'),
               ('WHY-055','第九章一日例十二，印刷 p151（PDF p76 左半）'),
               ('WHY-056','第九章一日例十三，印刷 p152（PDF p77 右半）'),
               ('WHY-057','第九章一日例十四，印刷 p152（PDF p77 右半）'),
               ('WHY-058','第九章一日例十五，印刷 p153（PDF p77 左半）'),
               ('WHY-059','第九章一周例一，印刷 p154（PDF p78 右半）'),
               ('WHY-060','第九章一周例二，印刷 p155–156（PDF p78 左半、p79 右半）'),
               ('WHY-061','第九章一周例三，印刷 p156（PDF p79 右半）'),
               ('WHY-062','第九章一周例四，印刷 p157–158（PDF p79 左半、p80 右半）'),
               ('WHY-063','第九章买卖例一，印刷 p158（PDF p80 右半）'),
               ('WHY-064','第九章买卖例二，印刷 p159–160（PDF p80 左半、p81 右半）'),
               ('WHY-065','第九章买卖例三，印刷 p160（PDF p81 右半）'),
               ('WHY-066','第九章买卖例四，印刷 p160（PDF p81 右半）')]:
    add(i,'r56-股票','partial','mid',False,'partial',False,PART,STK_PART_BASIS,loc)

assert len(C) == 41, len(C)
entries = []
for (i, g, oa, op, oe, ra, re_, v, b, loc) in C:
    entries.append({
        'case_id': i, 'cohort': g,
        'original': {'anchor_presence': oa, 'pollution': op, 'eligible_net': oe},
        'recheck': {'anchor_presence': ra, 'eligible_net': re_},
        'verdict': v, 'basis': b, 'source_location': loc,
        'source_book': '六爻分类占验技法 (王虎应著).pdf（台账登记路径，扫描本无文字层）',
    })

out = {
 'artifact': 'SUPPLY-RECHECK-why-partial-r59',
 'round': 59, 'seat': '数据/开采席',
 'scope': 'WHY 一轮（R56 台账）与二轮（R57 台账 r2）中 anchor_presence=partial、或 filters 未全过、或 eligible_net≠true 之全部条目',
 'candidate_n': 41,
 'method': '逐例回原书扫描 PDF 按台账登记路径精确打开，pdftoppm 200dpi 渲染后逐页读图复核四滤（断语逐字可录／结局独立成文具体／断语结局可分离／污染非 high）与锚点在场口径；升 present 须原文实据，不以推定补锚。印刷页→PDF 页映射：PDF k 页＝印刷 (2k−2, 2k−1) 页。',
 'summary': {
   'verdicts_all_maintained_n': 41,
   'anchor_upgrades_to_present_n': 0,
   'eligibility_changes_n': 0,
   'optional_pool_increment_n': 0,
   'notes': [
     '缺项收窄 2 例：WHY-002（本卦全列＋六神＋动爻已可辨，唯变卦列斑驳）、WHY-029（本卦全列经读图补录，唯动爻/变卦未见原书明载，台账变卦「火山旅」出处待核）。',
     'WHY-102 partial 系原书结构性缺占时（篇题无占时行），非扫描质量问题，无从升格。',
     'WHY-117 滤二未过经读图坐实：应验情况仅「以上推斷果然應驗。」一语。',
     '去重 8 例（WHY-076/077/094/097/101/105/113/116）三键经原书页逐一复验全合，去重维持。']},
 'definitional_divergence': {
   'issue': '六神列是否属锚点在场要件',
   'evidence': 'R56 台账 rules 括注锚点要件为「卦名、动爻、世应、六亲纳支、月建日辰」（未列六神）；然股票章诸盘原书版式多未印六神列，R56 席对同等版式判罚不一致：WHY-048/049/052 判 present，WHY-050/051/053–066 判 partial（本席逐页读图确认两组卦盘同为无六神列、余要素全在场）。天气/地震等章卦盘则六神俱印。',
   'seat_handling': '本席按原席个案原判逐例维持、不以重新定义升降任何一例，定义分歧登记于此提请主持裁。',
   'impact_either_way': '受影响 20 例（048/049/050/051/052/053–066）污染皆 mid、均不入可选集；裁六神为要件则 048/049/052 降 partial，裁非要件则 050/051/053–066 可升 present——两种裁法对可选库存与 holdout22 构成的影响皆为 0。'},
 'out_of_scope_registered': [
   {'id': 'WHY-R2-REG-01', 'note': 'R57 台账 registered_only：月球例（两书同案且结局口径冲突，挂起待裁），不在 entries 内，本轮未复核、维持挂起。'},
   {'id': 'WHY-R2-REG-02', 'note': 'R57 台账 registered_only：风水例十（亥月辛酉日水山蹇变水地比），不在 entries 内，本轮未复核。'}],
 'dedup_statement': '复核候选 41 例均为既有台账条目，其 id 与三键（本变卦＋占月日＋问事）于 R56/R57 入账时已与已用并集对勘在案；本轮逐例复核未见推翻项，全部维持原处置，不产生新入账，与已用并集（实算 n=976，见 SUPPLY-ACCOUNTING-r59）零复用不受影响。',
 'entries': entries,
}
jp = f'{BASE}/runs/round59/digestion/SUPPLY-RECHECK-why-partial-r59.json'
with open(jp, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
raw = open(jp, 'rb').read()
print('json bytes:', len(raw), 'sha256:', hashlib.sha256(raw).hexdigest())

L = []
L.append('# SUPPLY-RECHECK-why-partial-r59 —— WHY partial 面续采复核（R59 数据/开采席）')
L.append('')
L.append('- 数据件：同目录 `SUPPLY-RECHECK-why-partial-r59.json`（41 例全字段）。原书：`/home/hatch/workspace/divination/incoming/wanted-books-4/Book/六爻分类占验技法 (王虎应著).pdf`（台账登记路径；扫描本、无文字层，71,769,090 字节、104 PDF 页）。印刷页→PDF 页：PDF k 页＝印刷 (2k−2, 2k−1) 页，右半为先行页。')
L.append('- 范围：R57 二轮台账（WHY-072–117）中 eligible_net≠true 10 例＋R56 一轮台账中非净入账 31 例，共 **n=41**；另 R57 registered_only 2 例（月球例、风水例十）不在 entries 内，仅范围外登记、未复核。')
L.append('- 方法：逐例回原书渲染读图，按四滤＋锚点在场口径复核；升 present 须原文实据，不以推定补锚。')
L.append('')
L.append('## 结论总表')
L.append('')
L.append('| 项 | n |')
L.append('|---|---|')
L.append('| 复核候选 | 41 |')
L.append('| 原判维持 | 41 |')
L.append('| 锚点升 present | **0** |')
L.append('| 资格变更（转为可入账） | **0** |')
L.append('| 可选集增量 | **0** |')
L.append('| 缺项收窄（判定不变） | 2（WHY-002、WHY-029） |')
L.append('')
L.append('## 逐例复核')
L.append('')
for e in entries:
    L.append(f"### {e['case_id']}（{e['cohort']}）")
    L.append('')
    L.append(f"- 原判：锚点 {e['original']['anchor_presence']}／污染 {e['original']['pollution']}／eligible_net={str(e['original']['eligible_net']).lower()}")
    L.append(f"- 复核判：锚点 {e['recheck']['anchor_presence']}／eligible_net=false —— **{e['verdict']}**")
    L.append(f"- 依据：{e['basis']}")
    L.append(f"- 原文定位：{e['source_location']}")
    L.append('')
L.append('## 定义分歧登记（提请主持裁）')
L.append('')
L.append('**六神列是否属锚点在场要件。** R56 台账 rules 括注要件为「卦名、动爻、世应、六亲纳支、月建日辰」，未列六神；但股票章诸盘原书版式多未印六神列，R56 席判罚不一致：WHY-048/049/052 判 present、WHY-050/051/053–066 判 partial，本席逐页读图确认两组同为无六神列、余锚点要素全在场。本席逐例维持原判、不以重新定义升降。受影响 n=20，污染皆 mid、均不入可选集，两种裁法对可选库存与 holdout22 构成影响皆为 0。')
L.append('')
L.append('## 去重声明')
L.append('')
L.append('41 例均为既有台账条目，id 与三键于入账时已对勘在案，本轮复核未见推翻项、不产生新入账；与已用并集（实算 n=976，见 SUPPLY-ACCOUNTING-r59）零复用不受影响。去重 8 例另经原书页逐一复验三键全合。')
L.append('')
L.append('## 纪律自报')
L.append('')
L.append('本席只按台账登记路径打开原书 PDF 与两轮台账，未打开任何 runs/round59/predictions 或 judging 内容（judging 目录未列表），未做 git 操作。读图中间件（页图渲染）存于本目录 why-pages/ 子目录，为复核证据 scratch。')
md = '\n'.join(L) + '\n'
mp = f'{BASE}/runs/round59/digestion/SUPPLY-RECHECK-why-partial-r59.md'
with open(mp, 'w', encoding='utf-8') as f:
    f.write(md)
print('md bytes:', len(md.encode('utf-8')))
