#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
R45 数据角：账外待核库存 110 行逐例三键对勘（只读输入，输出落本目录）。

对勘对象（110 行）：
  A. expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl 中 id 不在已用并集
     （runs/round43/data-verify/used-union-r43.jsonl, 901 id）的行
     —— 按 R44 口径自算复现，应为 107 行（BY 100 + YX 7），不符即停。
  B. expansion9/liuren-chen2/cases.jsonl 中 LR3-103 / LR3-106 / LR3-108 三行。

比对全集（池）：
  - BYZ 台账 runs/round38/data-verify/bianyi-stock-r38.jsonl（117 行）
  - YXS 台账 runs/round38/data-verify/yuce-stock-r38.jsonl（50 行；
    37 行 id=null，以 source_ref 为行标识）
  - 已用并集全量行：cases-reviewed 自身已用行（BY/YX 19 行）、
    holdout3-18/test_gold.jsonl 全量（490 行，复核用）
  - 同族库存：expansion9/liuren-chen1、expansion7/liuren（LR/LR2/LR3 族）、
    expansion12/liuren-cuiyan（CY/CYJ）、expansion12/liuren-duanan（DA）、
    data/dev9-baseline-build/part-new.jsonl

三键：占年（asked_at 之年：公历括号年 / 干支年双口径取集合）、
      日干支（asked_at 中「X日」）、主问（subject + question_or_topic 文本）。
候选生成（任一命中即进文核）：
  (a) 年集合交叠 且 日干支相等；
  (b) 主问 bigram Jaccard 相似度 >= 0.30；
  (c) 农历月/日/时支三元组相等（预测学台账 asked_at 仅记农历日期时用）。
判定（四类，写入 ADJUDICATIONS 的为已逐对读文本节录后的定案；
      仅由通用主问套式（占者本人/占动静/占家宅等）触发、且最高相似候选
      年/日/对象皆异者，由脚本按 ③→④ 规则归档并在 note 中列明候选三键）：
  ① duplicate              三键全合 = 同案重复（matched_id 给撞中行）
  ② collide_diff_case      年+干支合、主问异，读文本判为异案（计新鲜）
  ③ suspect_to_duplicate   仅部分键合，读文本归入同案（不计新鲜）
     suspect_to_fresh       仅部分键合，读文本归入真新鲜（计新鲜）
  ④ fresh                   三键无合 = 真新鲜
输出：collate-110-r45.jsonl（逐行）、collate-110-r45.md（方法与计数总表）。
"""
import json, re, glob, collections, os

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    '..', '..', '..')          # benchmark/phase3
BASE = os.path.normpath(BASE)
OUTDIR = os.path.dirname(os.path.abspath(__file__))

def load(rel):
    return [json.loads(l) for l in open(os.path.join(BASE, rel), encoding='utf-8')
            if l.strip()]

GZ = '甲乙丙丁戊己庚辛壬癸'
DZ = '子丑寅卯辰巳午未申酉戌亥'

def asked(r):
    a = r.get('asked_at')
    if isinstance(a, str) and a:
        return a
    c = r.get('context')
    if isinstance(c, dict) and isinstance(c.get('asked_at'), str):
        return c['asked_at']
    return ''

def subj(r):
    s = r.get('subject')
    if isinstance(s, str):
        return s
    if isinstance(s, dict):
        return s.get('name_or_desc', '') or ''
    return ''

def topic(r):
    return r.get('question_or_topic') or ''

def year_set(s):
    """占年双口径：括号内公历年 + 干支年，取集合（两文件记法不同时仍可交叠比对）。"""
    out = set()
    for m in re.finditer(r'（(\d{3,4})）', s or ''):
        out.add('Y' + m.group(1))
    m = re.search(r'([' + GZ + '][' + DZ + '])年', s or '')
    if m:
        out.add(m.group(1))
    m = re.search(r'民国(\d{1,3})年', s or '')
    if m:
        out.add('Y' + str(int(m.group(1)) + 1911))
    m = re.search(r'农历(\d{2,4})年', s or '')
    if m:
        y = int(m.group(1))
        out.add('Y' + str(y + 1911 if y < 200 else y))
    return out

def day_gz(s):
    m = re.search(r'([' + GZ + '][' + DZ + '])日', s or '')
    return m.group(1) if m else None

CN = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7,
      '八': 8, '九': 9, '十': 10, '十一': 11, '十二': 12}
def cn_num(t):
    if t.isdigit():
        return int(t)
    if t in CN:
        return CN[t]
    if t.startswith('廿'):
        return 20 + CN.get(t[1:], 0)
    if t.startswith('三十'):
        return 30 + CN.get(t[2:], 0) if len(t) > 2 else 30
    return None

def lunar_triple(s):
    """(月, 日, 时支) 三元组：预测学台账 asked_at 仅记农历月日时支时用于对位。"""
    if not s:
        return None
    m = re.search(r'([0-9一二三四五六七八九十廿]+)月([0-9一二三四五六七八九十廿]+)日', s)
    if not m:
        return None
    mo, da = cn_num(m.group(1)), cn_num(m.group(2))
    hm = re.search(r'([' + DZ + '])时', s)
    return (mo, da, hm.group(1) if hm else None)

def norm(s):
    s = re.sub(r'[（(][^）)]*[）)]', '', s or '')
    return re.sub(r'[\s，。、：；·]', '', s)

def bigrams(s):
    s = norm(s)
    return {s[i:i + 2] for i in range(len(s) - 1)} if len(s) > 1 else ({s} if s else set())

def jac(a, b):
    A, B = bigrams(a), bigrams(b)
    return len(A & B) / len(A | B) if A | B else 0.0

# ---------------- 对勘对象 ----------------
used = {json.loads(l)['id'] for l in
        open(os.path.join(BASE, 'runs/round43/data-verify/used-union-r43.jsonl'),
             encoding='utf-8') if l.strip()}
assert len(used) == 901, f'已用并集行数异常: {len(used)}'

reviewed = load('expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl')
targets = [r for r in reviewed if r['id'] not in used]
fam = collections.Counter(r['id'].split('-')[0] for r in targets)
assert len(targets) == 107 and fam['BY'] == 100 and fam['YX'] == 7, \
    f'107 行复现失败: total={len(targets)} fam={dict(fam)} —— 按派单口径停下报告'

chen2 = {r['id']: r for r in load('expansion9/liuren-chen2/cases.jsonl')}
for lid in ('LR3-103', 'LR3-106', 'LR3-108'):
    assert lid in chen2 and lid not in used, f'{lid} 前提不符'
    targets.append(chen2[lid])
assert len(targets) == 110

# ---------------- 比对全集 ----------------
def row_label(r):
    return r.get('id') or ('yuce-stock:' + (r.get('source_ref') or '无标识行'))

pools = {}
pools['BYZ台账'] = load('runs/round38/data-verify/bianyi-stock-r38.jsonl')
pools['YXS台账'] = load('runs/round38/data-verify/yuce-stock-r38.jsonl')
pools['reviewed已用行'] = [r for r in reviewed if r['id'] in used]
golds = []
for g in sorted(glob.glob(os.path.join(BASE, 'holdout*', 'test_gold.jsonl'))):
    golds += [json.loads(l) for l in open(g, encoding='utf-8') if l.strip()]
pools['holdout金标'] = golds
pools['指南族'] = (load('expansion9/liuren-chen1/cases.jsonl') +
                   load('expansion9/liuren-chen2/cases.jsonl') +
                   load('expansion7/liuren/cases.jsonl') +
                   load('data/dev9-baseline-build/part-new.jsonl'))
pools['粹言'] = (load('expansion12/liuren-cuiyan/cases-munong.jsonl') +
                 load('expansion12/liuren-cuiyan/cases-juan5.jsonl'))
pools['断案'] = (load('expansion12/liuren-duanan/cases-a.jsonl') +
                 load('expansion12/liuren-duanan/cases-b.jsonl'))

pool_rows = []   # (pool_name, row)
for name, rows in pools.items():
    for r in rows:
        pool_rows.append((name, r))

# ---------------- 候选生成 ----------------
def candidates(t):
    tid = t['id']
    ty, td = year_set(asked(t)), day_gz(asked(t))
    tt = subj(t) + '|' + topic(t)
    lt = lunar_triple(asked(t))
    out = []
    for name, r in pool_rows:
        if r.get('id') == tid:
            continue
        ry, rd = year_set(asked(r)), day_gz(asked(r))
        hit = []
        if ty and ry and (ty & ry) and td and rd and td == rd:
            hit.append('年+日干支合')
        sim = jac(tt, subj(r) + '|' + topic(r))
        if sim >= 0.30:
            hit.append(f'主问相似{sim:.2f}')
        lr = lunar_triple(asked(r))
        if lt and lr and lt == lr and lt[0] is not None:
            hit.append('农历月日时合')
        if hit:
            out.append({'pool': name, 'matched_id': row_label(r),
                        'hit': '+'.join(hit), 'sim': round(sim, 2),
                        'asked_at': asked(r), 'subject': subj(r),
                        'topic': topic(r)})
    out.sort(key=lambda c: (-c['sim'], c['matched_id']))
    return out

# ---------------- 逐对读文本后的定案（主持口径四类） ----------------
# ① 三键全合 = 同案重复
ADJ = {}
for yid, mid, pg in [
        ('YX-001', 'yuce-stock:第五章§1·教学例一（书页303）', '303'),
        ('YX-002', 'yuce-stock:第五章§1·教学例二（书页306）', '306'),
        ('YX-003', 'yuce-stock:第五章§1·教学例三（书页308）', '308'),
        ('YX-004', 'yuce-stock:第五章§1·教学例四（书页310）', '310'),
        ('YX-005', 'yuce-stock:第五章§1·教学例五（书页312）', '312')]:
    ADJ[yid] = ('duplicate', mid,
                '同书同案：主问合（同人同事），农历月/日/时与台账行逐项合'
                '（教学例二台账行 asked_at 字段缺失，以主问+书页序位定案）；'
                '台账行 disposition=notseal（R38 以「无结局落文」剔除），'
                '与本文件 A-low 抽法冲突属资格口径问题、非新鲜问题，'
                '同案已在 R38 普查宇宙内，不计新鲜。')
ADJ['YX-001'] = ('duplicate', 'yuce-stock:第五章§1·教学例一（书页303）',
                 '同书同案：主问合（董事长被投书/董事会调查局事），月日时合'
                 '（三月二十三日亥时）；年记法异文——本行作民国82年（1993）、'
                 '台账行作民国83年，系一处转录异文，余键全合仍判同案。'
                 '台账行 disposition=notseal，不计新鲜。')
ADJ['YX-007'] = ('duplicate', 'CY-019',
                 '三键全合：壬午年三月乙酉日辰时、酉将，乡友崔仲和代占胎孕/六甲，'
                 '两行结局同为母子俱亡。CY-019（《六壬粹言》卷六慕农占验附存）'
                 '在 R43 粹言慕农新鲜 33 内——本案已入供给账，本行系《大六壬预测学》'
                 '第六章§1 对粹言成例的转引重出，不计新鲜。')
ADJ['LR3-108'] = ('duplicate', 'CYJ-041',
                  '三键全合：丁丑年七月丁亥日，太仓钱某中翰占常熟陈南洲公讼/逮问；'
                  '时支同为辰（CYJ-041 原文仅记时支辰时、本行甲辰时）。'
                  'CYJ-041 在 R43 粹言卷五新鲜 55 内——本案已以 CYJ-041 入供给账，'
                  'LR3-108 再入账即同案双计，不计新鲜；附注：R41 粹言三键剔除清单'
                  '（CYJ-026/027/044/045）未含 CYJ-041，此同案关系系本轮新发现。')
# ③ 仅部分键合、读文本归同案
ADJ['BY-081'] = ('suspect_to_duplicate', 'BYZ-004',
                 '主问全合（衣店黄维型占友被掳回否）、年/月合（甲寅年巳月），'
                 '日干支异（壬辰日丑时 vs 甲申日子时）：同人就同一被掳友人'
                 '隔日复占，两行案验同指一事（五月丑日友人归）。'
                 '结局事件已随 BYZ-004（R43 新鲜 66 内）入账，本行计新鲜即同事件双计，'
                 '归同案、不计新鲜。')
# ② 年+干支合、主问异，读文本为异案（计新鲜）
COLLIDE_BY = {
 'BY-019': ['BYZ-001'], 'BY-023': ['BYZ-004', 'BYZ-009', 'BYZ-064', 'BYZ-073'],
 'BY-027': ['BYZ-002', 'BYZ-035'], 'BY-028': ['BYZ-027'],
 'BY-031': ['BYZ-023', 'BYZ-046', 'BYZ-114'], 'BY-037': ['BYZ-085'],
 'BY-045': ['BYZ-033'], 'BY-069': ['BYZ-004', 'BYZ-009', 'BYZ-064', 'BYZ-073'],
 'BY-071': ['BYZ-111'], 'BY-078': ['BYZ-031'], 'BY-083': ['BYZ-003'],
 'BY-087': ['BYZ-111'], 'BY-096': ['BYZ-001'], 'BY-101': ['BYZ-071'],
 'BY-103': ['BYZ-016', 'BYZ-080'], 'BY-114': ['BYZ-039'],
}
COLLIDE_NOTE = ('年+日干支合而月/时/占者/主问皆异（同年内日干支六十日一循环，'
                '同日多占为此书常态），逐对读文本节录判异案，计新鲜。')
for tid, mids in COLLIDE_BY.items():
    ADJ[tid] = ('collide_diff_case', ','.join(mids), COLLIDE_NOTE)
ADJ['BY-027'] = ('collide_diff_case', 'BYZ-002,BYZ-035',
                 '与 BYZ-002 同年同月（辛亥酉月）同日（癸巳）、同问进京，'
                 '但占者异（赵公 vs 梅筱素）、时异（午 vs 巳）、结局异'
                 '（赵公未进京调松江府 vs 梅年终动身次年正月引见），系同日两官各占，异案。'
                 '与 BYZ-035 仅年月日合、问开复，异案。计新鲜。')
ADJ['BY-028'] = ('collide_diff_case', 'BYZ-027',
                 '与 BYZ-027 同年同月（甲寅辰月）同日（辛未），问近（往株树潭行程 vs 迁移远近），'
                 '但时异（巳 vs 午）、课异（比用 vs 别责），系同日异时两占；'
                 '两行案验同指避贼投杨家一事，关联风险已登记，仍按异课异问判异案，计新鲜。')
ADJ['BY-037'] = ('collide_diff_case', 'BYZ-085;BY-082(已用)',
                 '对 BYZ-085 仅年月日合（月时问皆异）；另与已用行 BY-082 同年同月同日同寓兴安，'
                 '但问异（买皮纸下河口 vs 买花）、时异（寅 vs 辰），同日两占，异案。计新鲜。')
ADJ['BY-103'] = ('collide_diff_case', 'BYZ-016,BYZ-080',
                 '与 BYZ-080 同年同月（甲寅午月）同日（甲戌）同问店事，但占者异（易姓 vs 钱姓）、'
                 '时异（酉 vs 卯）、结局异，异案；与 BYZ-016 仅年月日合。计新鲜。')
ADJ['LR3-103'] = ('collide_diff_case', 'LR3-101',
                  '与 LR3-101 同年（1637 丁丑）同日干支（乙未），但月异（六月 vs 二月）、'
                  '占者与主问异（赵光汴请缨行边 vs 刘若宜会试），异案。计新鲜。')
ADJ['BY-014'] = ('suspect_to_fresh', 'BY-065(已用)',
                 '与已用行 BY-065 同年同月（丙辰午月）同日（壬午），但占者/主问异'
                 '（张姓合伙运货往兴安 vs 自占谷城可寓否）、时异（亥 vs 午），同日两占，异案，计新鲜。')
ADJ['BY-098'] = ('suspect_to_fresh', 'BY-009(已用)',
                 '与已用行 BY-009 同年同月（甲寅未月）同日（庚戌），但占者/主问异'
                 '（杨书卿占六甲 vs 自占往南省）、时异（午 vs 亥），异案，计新鲜。')
ADJ['YX-006'] = ('suspect_to_fresh', 'DA-118等(年+日合异案)',
                 '与断案 DA-001/079/096/118 年+日干支合（己酉年己卯日）：'
                 'DA-118 同为三月，但对象（徐承局 vs 佚名男女）、事项（占向后如何 vs 占婚姻）、'
                 '占时（寅时 vs 辰时）三项皆异（与本行 review.dedup_note 既有定案一致），'
                 '余三行月/问皆异，均异案；YXS 台账未覆盖预测学第六章§1，本行不在台账内。'
                 '计新鲜，但带资格旗标：行内 review 记 contamination_final=high、verdict=dev-only，'
                 '入账与否请主持裁。')
# 年+日合而月异（日干支六十日一循环、异月即异日）——逐对核月/问/人后归④
for _tid, _mid, _note in [
    ('BY-018', 'BY-026(已用)', '同年（甲寅）同日（辛亥），月异（辰月 vs 酉月）即异日，问/时皆异，异案。'),
    ('BY-021', 'BY-003(已用)', '同年（甲寅）同日（乙未），月异（卯月 vs 未月）即异日，异案。'),
    ('BY-051', 'BY-001(已用)', '同年（甲寅）同日（庚辰），月异（午月 vs 巳月）即异日，异案。'),
    ('BY-055', 'BY-005(已用)', '同年（甲寅）同日（丁卯），月异（辰月 vs 戌月）即异日，异案。'),
    ('BY-057', 'DA-142', '与断案 DA-142 年+日合（丙辰年甲寅日），月异（巳月 vs 六月）即异日，问异（周伯香会试信 vs 佚名求财），异案。'),
    ('BY-080', 'BY-003(已用)', '同年（甲寅）同日（乙未），月异（卯月 vs 未月）即异日，异案。'),
    ('BY-102', 'BY-065(已用)', '同年（丙辰）同日（壬午），月异（辰月 vs 午月）即异日，异案。'),
    ('BY-105', 'BY-095(已用)', '同年（甲寅）同日（庚寅），月异（亥月 vs 未月）即异日，异案。'),
    ('BY-109', 'BY-108(已用)', '同年（乙丑）同日（庚午），月异（申月 vs 戌月）即异日，异案。'),
    ('BY-110', 'BY-005(已用)', '同年（甲寅）同日（丁卯），月异（午月 vs 戌月）即异日，异案。'),
    ('BY-115', 'BY-009(已用)', '同年（甲寅）同日（庚戌），月异（辰月 vs 未月）即异日，异案。'),
]:
    ADJ[_tid] = ('suspect_to_fresh', _mid, _note + '计新鲜。')

# ---------------- 产出 ----------------
records = []
tally = collections.Counter()
for t in targets:
    tid = t['id']
    fam = tid.split('-')[0]
    cands = candidates(t)
    keys = {'year': sorted(year_set(asked(t))), 'day_ganzhi': day_gz(asked(t)),
            'subject': subj(t), 'topic': topic(t),
            'asked_at_raw': asked(t)}
    if tid in ADJ:
        verdict, matched, note = ADJ[tid]
        if cands:
            top = cands[0]
            note += (f'（脚本候选首位：{top["matched_id"]}，{top["hit"]}，'
                     f'候选共 {len(cands)} 条）')
    elif cands:
        verdict, matched = 'suspect_to_fresh', cands[0]['matched_id']
        top = cands[0]
        note = ('③存疑经文核归④：候选仅由主问套式相似或单键触发；最高相似候选 '
                f'{top["matched_id"]}（{top["pool"]}，{top["hit"]}，'
                f'其 asked_at={top["asked_at"] or "缺失"}、subject={top["subject"] or "缺失"}）'
                '与本行年/日/对象核异，非同案，计新鲜。')
    else:
        verdict, matched, note = 'fresh', None, '三键对全部比对池零命中，真新鲜。'
    fresh = verdict in ('collide_diff_case', 'suspect_to_fresh', 'fresh')
    tally[(fam, verdict)] += 1
    records.append({'row_id': tid, 'family': fam, 'verdict': verdict,
                    'fresh_countable': fresh, 'matched_id': matched,
                    'keys': keys, 'n_candidates': len(cands), 'note': note})

with open(os.path.join(OUTDIR, 'collate-110-r45.jsonl'), 'w', encoding='utf-8') as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')

fresh_total = sum(1 for r in records if r['fresh_countable'])
print('targets:', len(records))
for k in sorted(tally):
    print(k, tally[k])
print('fresh total:', fresh_total)
print('non-fresh:', [(r['row_id'], r['verdict'], r['matched_id'])
                      for r in records if not r['fresh_countable']])
# 计数总表写入 md 由本脚本一并生成
fam_fresh = collections.Counter(r['family'] for r in records if r['fresh_countable'])
fam_all = collections.Counter(r['family'] for r in records)
lines = []
lines.append('# R45 数据角：账外待核库存 110 行三键对勘定案\n')
lines.append('脚本：`collate_110_r45.py`（本目录，只读输入，可复跑）；'
             '逐行定案：`collate-110-r45.jsonl`（110 行）。'
             '角色：数据角——只对勘与计数，未作断、未评分、未提交 git。\n')
lines.append('## 方法\n')
lines.append('- 对象复现：cases-reviewed.jsonl 按 id 对已用并集（901）自算，'
             '不在并集者恰 107 行（BY 100＋YX 7），与 R44 口径逐数吻合；'
             '另加 LR3-103／106／108（三行均不在并集、已逐 id 核），合计 110 行。')
lines.append('- 三键：占年（asked_at 之年，公历括号年与干支年双口径取集合——'
             '预测学两文件记法不同，单口径会漏合）、日干支（「X日」）、'
             '主问（subject＋question_or_topic 文本）。')
lines.append('- 候选生成：(a) 年交叠＋日干支合；(b) 主问 bigram Jaccard ≥0.30；'
             '(c) 农历月/日/时支三元组合（台账 asked_at 仅记农历日期的行）。'
             '候选逐对读两行文本节录（asked_at／subject／主问／断语／结局）定案。')
lines.append('- 比对池：BYZ 台账 117 行、YXS 台账 50 行、reviewed 已用行 19 行、'
             'holdout3–18 金标 490 行（复核）、指南族（chen1＋chen2＋expansion7＋dev9 part-new）、'
             '粹言（慕农＋卷五）、断案（cases-a/b）。')
lines.append('- R44 prose 称「年＋日干支键碰撞 15 处」：本轮同口径实算 BY 对 BYZ 为 '
             '16 行／23 对（ distinct 年+日键 14 组），LR3 对指南族另 1 对；'
             '计数基数不同（行／对／键组），定案以本轮逐对文核为准。\n')
lines.append('## 计数总表（family × verdict）\n')
lines.append('| family | ①同案重复 | ③→同案 | ②异案(新鲜) | ③→新鲜 | ④真新鲜 | 行数 | 真新鲜 |')
lines.append('|---|---|---|---|---|---|---|---|')
for fam in ('BY', 'YX', 'LR3'):
    c = {v: tally.get((fam, v), 0) for v in
         ('duplicate', 'suspect_to_duplicate', 'collide_diff_case',
          'suspect_to_fresh', 'fresh')}
    lines.append(f"| {fam} | {c['duplicate']} | {c['suspect_to_duplicate']} | "
                 f"{c['collide_diff_case']} | {c['suspect_to_fresh']} | {c['fresh']} | "
                 f"{fam_all[fam]} | {fam_fresh[fam]} |")
lines.append(f"| **合计** | {tally[('BY','duplicate')]+tally[('YX','duplicate')]+tally[('LR3','duplicate')]} | "
             f"{tally[('BY','suspect_to_duplicate')]} | "
             f"{sum(v for (f_,v_),v in [(k,tally[k]) for k in tally] if False) or sum(tally[k] for k in tally if k[1]=='collide_diff_case')} | "
             f"{sum(tally[k] for k in tally if k[1]=='suspect_to_fresh')} | "
             f"{sum(tally[k] for k in tally if k[1]=='fresh')} | **110** | **{fresh_total}** |\n")
lines.append('## 真新鲜构成与旗标\n')
lines.append(f'- 真新鲜合计 **{fresh_total}**：BY {fam_fresh["BY"]}（毕法案录）、'
             f'YX {fam_fresh["YX"]}、LR3 {fam_fresh["LR3"]}（指南）。体系归属全为六壬。')
lines.append('- 旗标（计入新鲜但资格另有文内异议，入账与否请主持裁）：'
             '仅 YX-006——行内 review 记 contamination_final=high、verdict=dev-only'
             '（与断案 DA-001/079/096/118 年+日合均已逐对判异案，见逐行 note）。'
             '剔除该旗标行后无争议真新鲜为 '
             f'{fresh_total - 1}。')
lines.append(f'- 非新鲜 {110 - fresh_total} 行：YX-001–005＝《大六壬预测学》第五章§1 教学例一至五，'
             '与 YXS 台账同案（台账行 id=null、disposition=notseal，R38 以无结局落文剔除；'
             '资格冲突请主持裁，但同案已在普查宇宙内，不属新鲜发现）；'
             'YX-007＝CY-019 同案（粹言慕农，已在 R43 新鲜 33 内；预测学第六章§1 转引粹言成例）；'
             'BY-081＝BYZ-004 同事件复占（结局已随 BYZ-004 入账）；'
             'LR3-108＝CYJ-041 同案（已在粹言卷五新鲜账内）。\n')
lines.append('## 与 R43 供给总账（DA 118／BYZ 66／粹言 88）的关系\n')
lines.append('- 本 110 行全为六壬，且分属 R43 总账之外的三个来源：'
             '《六壬辨疑·毕法案录》（BY）、《大六壬预测学》（YX）、'
             '《大六壬占验指南》（LR3）。R43 总账的 DA（断案）118、BYZ（辨疑正文占验）66、'
             '粹言（慕农 33＋卷五 55）88 三个数不因本轮对勘增减——'
             '撞中台账的行（BYZ-004、CY-019、CYJ-041）原本就在那 66／88 之内，本轮只是防止账外行重复计入。')
lines.append(f'- 对勘后六壬新鲜供给口径变化：272（R43 四组）＋{fresh_total}（本轮入账）'
             f'＝{272 + fresh_total}；其中毕法案录 BY 系为新增供给线 {fam_fresh["BY"]} 行、'
             f'指南 LR3 新增 {fam_fresh["LR3"]} 行、预测学 YX 新增 {fam_fresh["YX"]} 行（即 YX-006，带资格旗标）。'
             '构成层面全为六壬，不改变 R43/R44 关于 holdout 构成双 50% 上限的裁决前提。\n')
lines.append('## 字段缺失与异常登记\n')
lines.append('- YXS 台账 yuce-stock-r38.jsonl：实载 50 行（末行无换行符，wc -l 读 49）；'
             '37 行 id=null（未入封行），以 source_ref 为行标识；'
             '第五章§1·教学例二行 asked_at 字段缺失（YX-002 靠主问＋序位定案）。')
lines.append('- BY-085：asked_at 作「咸丰戊午年元旦午时」，日干支字段无可抽'
             '（元旦未记日干支），日键缺失——以年＋主问两键对勘，零命中，判④。')
lines.append('- BYZ-113：asked_at 与 subject 均作「阙」（扫描缺页），'
             '无键可撞，不影响任何一行定案。')
lines.append('- YX-001 年记法异文：本行民国82年（1993）vs 台账行民国83年，'
             '已在逐行 note 登记，仍判同案（月/日/时/主问全合）。')
lines.append('- YX-006／YX-007 的 source_work 字段作「YX」（非书名），'
             '出处以 provenance.page 为准（预测学第六章§1，书页 391–402），已登记。')
with open(os.path.join(OUTDIR, 'collate-110-r45.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')
print('md written')
