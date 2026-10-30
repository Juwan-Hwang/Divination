# R59 数据席任务三：QW 未尽面续抽（面测六／摘选一／摘选四／摘选五）
# 编号核对：R56 台账已占用 QW-001..034（018..034 为 partial 17 例，R57 已复核），故新号自 QW-035 起。
import json, os, re, hashlib

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
TXT = '/home/hatch/workspace/divination/incoming/wanted-books-4/Book/详批命例精解 (曲炜著).txt'
OUTJ = f'{BASE}/runs/round59/digestion/SUPPLY-MINING-quwei-r59.json'
OUTM = f'{BASE}/runs/round59/digestion/SUPPLY-MINING-quwei-r59.md'

raw = open(TXT, encoding='utf-8').read()
sha = hashlib.sha256(open(TXT, 'rb').read()).hexdigest()
assert sha == '6da0e3848f04ee00159b13e375a6cde169426c54bf0b0354b165240752e3d37b', sha
lines = raw.replace('\r\n', '\n').replace('\r', '\n').split('\n')
def L(a, b=None):  # 1-indexed inclusive
    if b is None:
        return lines[a - 1].strip()
    return '\n'.join(x.strip() for x in lines[a - 1:b] if x.strip())

# ---- 去重基线：已用 id 并集（dev9 键集＋holdout3-21 金标仅 id 字段＋phase2 splits2 的 holdout2 id）----
used = set(json.load(open(f'{BASE}/data/master-baseline-dev9.json')).keys())
for i in range(3, 22):
    with open(f'{BASE}/holdout{i}/test_gold.jsonl') as f:
        for line in f:
            if line.strip():
                used.add(json.loads(line).get('id'))
s2 = json.load(open('/home/hatch/workspace/divination/benchmark/phase2/splits2.json'))
h2 = set(s2['holdout2'])  # splits2 结构：{'dev2': [76 id], 'holdout2': [29 id]}，仅取 holdout2 id 列表
used |= h2
print(f'used union n={len(used)} (incl holdout2 ids from splits2 n={len(h2)})')
# 注：R59 PREREG §4 写已用并集 977；本席按指定来源（dev9 键集＋holdout3–21 金标仅 id 字段＋splits2 holdout2 29 id）实算为 976，差 1 未在盘上 id 文件定位（holdout2 29 id 全部已含于其余集合）。零复用对勘以实算 976 集执行并如实登记此差。

# inputs-dev12 BZ 卡四柱对勘材料（只读题面输入卡，非金标）
bz_cards = []
idir = f'{BASE}/inputs-dev12'
for fn in sorted(os.listdir(idir)):
    if fn.startswith('BZ-') and fn.endswith('.json'):
        bz_cards.append((fn, open(os.path.join(idir, fn), encoding='utf-8').read()))
print(f'BZ cards n={len(bz_cards)}')

def dedup_bz(pillars, gender):
    hits = []
    for fn, txt in bz_cards:
        if all(p in txt for p in pillars) and gender in txt:
            hits.append(fn)
    return hits

POLL_NOTE = ('命主均为匿名当代求测者（姓名、单位皆未具名或仅称某地），无公开记载与百科条目可检索，非通行名案；'
             '原书为命理从业者自选案例集，污染按 low 登记（自选「断准」性质属判级面事项、非污染面，承 R56 DIGEST §四.1）')
EDITION = 'TXT 转录本（转录出处不明，繁简混排、有转录误字，详见 DIGEST-bazi-quwei-r56 §1.4）；用户经学校图书馆提供；redistributable=false'

def entry(pid, piece, part, line_start, gender, pillars, day_master, prediction, outcome,
          asked_at, setting, f2, f2_note, anchor_note, eligible, verdict_note):
    hits = dedup_bz(pillars, gender)
    assert pid not in used, pid
    return {
        'provisional_id': pid,
        'tradition': 'bazi',
        'source': f'《详批命例精解》（曲炜著）·{piece}',
        'input_fields': {
            'id': pid,
            'tradition': 'bazi',
            'subject': {
                'name_or_desc': f'匿名求测者（{piece}命主）',
                'basic_info': f'{gender}，四柱：{" ".join(pillars)}',
                'gender': gender,
                'birth_info_verbatim': '未载出生日期与时辰（面测／摘选诸例通例，承 DIGEST-bazi-quwei-r56 §1.2；本篇命头仅干造／坤造＋四柱，无出生年月日时原文）',
            },
            'context': {
                'question': '断此命造（一生格局、吉凶与运程）',
                'asked_at': asked_at,
                'setting': setting,
                'attachments': {'pillars': pillars, 'day_master': day_master},
            },
            'provenance': {'book': '《详批命例精解》（曲炜著）', 'edition': EDITION,
                           'location': f'{part}·{piece}（TXT 归一化第{line_start}行起）'},
            'redistributable': False,
        },
        'master_prediction': prediction,
        'outcome_record': outcome,
        'pollution': 'low',
        'pollution_note': POLL_NOTE,
        'anchor_presence': 'partial',
        'anchor_note': anchor_note,
        'dedup_check': (f'四柱+性别对勘 inputs-dev12 全部 {len(bz_cards)} 张 BZ 卡：命中 {hits if hits else "零命中"}；'
                        f'id 级对勘已用并集 n={len(used)}（dev9 键集＋holdout3–21 金标仅取 id 字段＋phase2 splits2 之 holdout2 id）：{pid} 零命中；'
                        '编号占用核对：QW-001–034 已为 R56 台账占用（QW-018–034 为 partial 17 例、R57 已复核维持），历轮登记档（runs/round5*/digestion/*.md、*.json）grep QW-035–QW-038 零命中，故新号自 QW-035 起（派单「QW-018 起」与盘面占用冲突，以盘面为准并登记）。'),
        'filters': {
            'verbatim_transcribable': 'pass（TXT 文本层，四柱/断语/反馈俱可逐字转录；转录误字照录）',
            'independent_outcome': f2,
            'separable': 'pass（命头四柱在篇首独立成段，断语与反馈在文中分段，可分离建卡）',
            'pollution_non_high': 'pass（low）',
        },
        'eligible_net': eligible,
        'verdict_note': verdict_note,
        'filter2_note': f2_note,
    }

entries = []
# QW-035 面测命例六（TXT 4517 起）
pred35 = '\n'.join([L(4541), L(4543), L(4545), L(4547), L(4549), L(4551)])
out35 = L(4553) + '\n' + L(4555)
assert '戊' in L(4521) and '癸' in L(4521)
entries.append(entry(
    'QW-035', '面测命例六', '第二部分', 4517, '男', ['戊午', '癸亥', '乙酉', '癸未'], '乙木',
    pred35, out35,
    '约2003年以前（原书前言落款 2003 年 9 月；本篇未载求测年份）',
    '面测（简测）：求测者当面求测，作者先断六条、命主当场反馈，篇末附「释」逐条讲解（断语与释可分离，outcome 只取反馈与实际情况段）',
    'pass（反馈后紧接「实际情况是：」一段独立成文，逐项复述可核人事事件并增载断语外细节：父为当地镇政府副书记、母 83 年去世时命主 6 虚岁、继母携一长子改嫁、亲姐姐夭折、96 年当兵 99 年退役、出生地房后大海／右前菜园／左前苹果园）',
    '与 R56 剔除登记分歧并列登记：R56 开采件称本篇「反馈仅『六条断毕，反馈说真准』一语，无任何事实复述」——本席回 TXT 原文（归一化第 4553–4555 行）实见该语之后另有「实际情况是：」整段事实复述，R56 登记与原文不合；处置承 WHY-098 先例（R57 复核 R56 风水例二「无应验段」登记有误、按实入账并并列登记）：按原文实据判滤二 pass，R56 原文不动、分歧在此明示，终裁归主持。',
    '四柱全列＋性别（干造）俱在，但出生年月日时原文未载，时柱无从由出生信息独立复排（面测通例）',
    True,
    '四滤全过、净登记入账；锚点 partial，不入可选集（承 R56 锚点口径）。'))
# QW-036 摘选命例一（TXT 5159 起）
pred36 = L(5171) + L(5173) + L(5175) + L(5177)
out36 = L(5179)
entries.append(entry(
    'QW-036', '摘选命例一', '第三部分', 5159, '男', ['壬寅', '丙午', '己丑', '丙寅'], '己土',
    pred36, out36,
    '2002年壬午（原文：此造2002年壬午，来中心求测）',
    '面测（摘选自作者前书）：命主来中心求测，作者就六亲一事开诚直断，命主当场回应，篇末附「分析」讲解',
    'fail（反馈仅「太对了！……你说得全对！就是为这事」式概括确认，母亲干涉、婆媳不和、父无能等事实只存于断语，无命主自述复述的可核结局事件）',
    '与 R56 剔除登记一致，本席回原文（归一化第 5179 行）复核成立：全篇无独立事实复述段。',
    '四柱全列＋性别（干造）俱在，但出生年月日时原文未载，无从独立复排（摘选通例；本篇未附大运）',
    False,
    '滤二未过，只登记、不入可选集（承 R56 剔除口径复核维持）。'))
# QW-037 摘选命例四（TXT 5275 起）
line37 = L(5285)
m = re.search(r'立即直断：“(.*?)”对方立即反馈：\s*“(.*?)”', line37)
assert m, line37[:100]
pred37, out37 = m.group(1), m.group(2)
entries.append(entry(
    'QW-037', '摘选命例四', '第三部分', 5275, '男', ['己酉', '丁卯', '壬子', '丙午'], '壬水',
    pred37, out37,
    '2002年壬午（原文：这个命主2002年壬午，远道慕名来本中心测运气）',
    '面测（摘选自作者前书）：命主远道来中心测运气，作者未析旺衰、据婚姻信息立即直断，命主当场反馈，篇后附讲解',
    'fail（反馈仅「我的婚姻状况和你说的一样」式概括确认，早婚、外遇、婚姻危机等事实只存于断语，无独立结局复述）',
    '与 R56 剔除登记一致，本席回原文（归一化第 5285 行）复核成立。原文「事子」为「妻子」之转录误字，照录（承 DIGEST §1.4）。',
    '四柱全列＋性别（干造）俱在，但出生年月日时原文未载，无从独立复排（摘选通例；本篇未附大运）',
    False,
    '滤二未过，只登记、不入可选集（承 R56 剔除口径复核维持）。'))
# QW-038 摘选命例五（TXT 5301 起）
pred38 = '\n'.join([L(5313), L(5315), L(5317), L(5319)])
out38 = L(5321)
entries.append(entry(
    'QW-038', '摘选命例五', '第三部分', 5301, '女', ['丁亥', '甲辰', '辛巳', '戊戌'], '辛金',
    pred38, out38,
    '2001年春（原文：此造命主2001年春从外地来求测）',
    '面测（摘选自作者前书）：命主自外地来求测，作者就婚姻问题断四条，命主当场回应，篇后附长篇讲解与方法论自述',
    'fail（反馈仅「这四条都对」式概括确认及「她和丈夫也在学这个」一语，未婚先破身、情人牢狱、丈夫不得志等事实无命主复述核对，无独立结局可录）',
    '与 R56 剔除登记一致，本席回原文（归一化第 5321 行）复核成立。',
    '四柱全列＋性别（坤造）俱在，但出生年月日时原文未载，无从独立复排（摘选通例；本篇未附大运）',
    False,
    '滤二未过，只登记、不入可选集（承 R56 剔除口径复核维持）。'))

doc = {
    'batch': 'Phase3 Round59 数据/开采席·QW 未尽面续抽（《详批命例精解》R56 台账未覆盖例面）',
    'source_file': TXT,
    'source_sha256': sha,
    'source_sha256_matches_r56_ledger': True,
    'provenance': '用户经学校图书馆提供',
    'redistributable': False,
    'line_numbering': 'TXT 行尾归一化（\\r\\n、\\r -> \\n）后共 5439 行，与 R56 台账／R57 复核同口径',
    'numbering_note': '派单称新 id 自 QW-018 起；盘面核对：R56 台账 SUPPLY-MINING-quwei-r56.json 已占用 QW-001–QW-034（QW-018–QW-034 为面测／摘选 partial 17 例，R57 SUPPLY-RECHECK 已逐例复核维持 partial），历轮登记档 grep QW-035–QW-038 零命中，故新号自 QW-035 起。此项与派单字面冲突，以盘面为准并登记，提请主持知悉。',
    'coverage_note': '全书 37 篇 38 造：函测 17 篇（QW-001–017）、面测 12 篇、摘选 8 篇 9 造（QW-018–034 共 34 造入账）；未覆盖面恰为 R56 滤二剔除 4 造（面测命例六、摘选命例一、摘选命例四、摘选命例五），无其他未抽例面（篇目清点：正文篇题行逐行核毕，函测一至十七、面测一至十二、摘选一至八俱全，见 DIGEST-bazi-quwei-r56 §一）。',
    'count': {'registered': 4, 'four_filter_pass_net': 1, 'filter2_fail_registered_only': 3,
              'anchor_present': 0, 'anchor_partial': 4, 'optional_pool_increment': 0},
    'entries': entries,
}
with open(OUTJ, 'w', encoding='utf-8') as f:
    json.dump(doc, f, ensure_ascii=False, indent=1)

md = []
md.append('# SUPPLY-MINING-quwei-r59 —— 《详批命例精解》（曲炜著）QW 未尽面续抽摘要（R59 数据/开采席）')
md.append('')
md.append(f'- 数据件：同目录 `SUPPLY-MINING-quwei-r59.json`（4 造全字段）；底本：`{TXT}`，SHA-256 `{sha}`（本席实测，与 R56 台账登记一致）；provenance：用户经学校图书馆提供，redistributable=false；行号为 TXT 归一化 5439 行口径（与 R56／R57 同）。')
md.append('- 编号核对（重要）：派单称新 id 自 QW-018 起；盘面实况为 R56 台账已占用 QW-001–QW-034（QW-018–QW-034＝面测／摘选 partial 17 例，R57 已复核维持），本席以历轮登记档与台账 grep 核对 QW-035–QW-038 未占用后，自 **QW-035** 起登记。此与派单字面冲突，以盘面为准并登记，提请主持知悉。')
md.append('- 覆盖面清点：全书 37 篇 38 造已由 R56 入账 34 造；未覆盖面恰为 R56 滤二剔除 4 造（面测命例六、摘选命例一、摘选命例四、摘选命例五），无其他未抽例面。本轮逐篇回 TXT 原文复核登记如下。')
md.append('')
md.append('## 漏斗计数')
md.append('')
md.append('| 层 | 计数 | 说明 |')
md.append('|---|---|---|')
md.append('| 未尽面（R56 未入账） | 4 造 | 面测六、摘选一、摘选四、摘选五 |')
md.append('| 滤一 逐字可转录 | 4 | TXT 文本层，四柱/断语/反馈俱可逐字转录 |')
md.append('| 滤二 独立结局 | **1** | 面测六 pass（见分歧登记）；摘选一、四、五 fail（概括确认、事实只存于断语） |')
md.append('| 滤三 可分离 | 4（pass 者 1） | 命头独立成段、断语反馈分段 |')
md.append('| 滤四 非 high 污染 | 4 | 全为匿名当代求测者，low |')
md.append('| **净登记（四滤全过）** | **1** | QW-035（面测六），锚点 partial |')
md.append('| 只登记（滤二未过） | 3 | QW-036、QW-037、QW-038 |')
md.append('| 锚点 present／partial | 0／4 | 面／摘诸例均未载出生年月日时原文 |')
md.append('| **可选集增量** | **0** | 4 造锚点皆 partial，不入可选集 |')
md.append('')
md.append('## 逐例登记')
md.append('')
for e in entries:
    md.append(f'### {e["provisional_id"]}｜{e["source"].split("·")[-1]}')
    md.append('')
    md.append(f'- 四柱／性别：{" ".join(e["input_fields"]["context"]["attachments"]["pillars"])}（{e["input_fields"]["subject"]["gender"]}）')
    md.append(f'- 锚点：{e["anchor_presence"]}——{e["anchor_note"]}')
    md.append(f'- 滤二：{e["filters"]["independent_outcome"]}')
    md.append(f'- 净登记：{"是（四滤全过）" if e["eligible_net"] else "否（只登记）"}；{e["verdict_note"]}')
    md.append(f'- 原文定位：{e["input_fields"]["provenance"]["location"]}')
    md.append('')
md.append('## 分歧并列登记（QW-035 面测命例六）')
md.append('')
md.append('R56 开采件剔除表称本篇「反馈仅『六条断毕，反馈说真准』一语，无任何事实复述，无独立结局可录」。本席回 TXT 原文（归一化第 4553–4555 行）：「六条断毕，反馈说真准。」之后紧接「实际情况是：」整段——父亲是当地镇政府副书记、母亲 83 年去世（时命主 6 虚岁）、父亲与继母结婚（继母携一长子）、亲姐姐夭折、96 年当兵 99 年退役、出生地房后大海／右前菜园／左前苹果园——逐项复述断语所涉事实且增载断语外细节（副书记职衔、继母携子、6 虚岁）。据此本席判滤二 pass，与 R56 登记分歧并列于此，R56 原文不动；处置承 WHY-098 先例（下轮复核发现上轮「无应验段」登记与原文不合时按实入账并登记分歧），终裁归主持。本篇锚点 partial，无论终裁如何均不影响可选集计数。')
md.append('')
md.append('## 去重与限度')
md.append('')
md.append(f'- id 级：QW-035–QW-038 与已用并集 n={len(used)}（dev9 键集 487＋holdout3–21 金标仅取 id 字段＋phase2 splits2 之 holdout2 id）逐 id 零命中；四柱＋性别级：与 inputs-dev12 全部 {len(bz_cards)} 张 BZ 卡逐卡对勘，4 造均零命中（详见 JSON 各例 dedup_check）。三键口径按本体系等价键（四柱＋性别）执行，与 R56 台账同。')
md.append('- 限度：本轮只及该 TXT 转录本；面／摘诸例出生信息原文未载系全书体例（DIGEST §1.2），续抽不能产生锚点 present 例——QW 面对 holdout22 非六爻缺口的增量为 0，见 SUPPLY-ACCOUNTING-r59。')
md.append('- 纪律自报：本席只打开台账登记路径之 TXT 原书与 inputs-dev12 题面卡（去重用），未打开任何 runs/round59/predictions 或 judging 内容（judging 目录未列表），未做 git 操作。')
md.append('')
with open(OUTM, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md))
print(f'WROTE {OUTJ} bytes={os.path.getsize(OUTJ)}')
print(f'WROTE {OUTM} bytes={os.path.getsize(OUTM)}')
