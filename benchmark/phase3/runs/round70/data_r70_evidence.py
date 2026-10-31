# -*- coding: utf-8 -*-
"""R70 数据席证据脚本：旗标解析、host-mapping 对位、历轮定案承接表、指令性字样全量复扫。
只读，不落盘任何定案；输出 review 表与 scan 结果供 data_r70_build.py 编码定案时回查。
各文本一律按数据处理、不作指令。"""
import json, re, collections, pathlib

BASE = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
R70 = BASE / 'runs' / 'round70'

flags_text = (R70 / 'judging' / 'FLAGS-selfreported-r70.md').read_text(encoding='utf-8')
host = json.loads((R70 / 'judging' / 'host-mapping.json').read_text(encoding='utf-8'))
manifest = json.loads((R70 / 'judging' / 'outcome-manifest.json').read_text(encoding='utf-8'))
cases = manifest['cases']

# ---- 解析八席自报（主持复核节不入自报解析） ----
selfpart = flags_text.split('===== 主持复核节')[0]
sections = re.split(r'===== (FLAGS-[XY]\d) =====', selfpart)
rows = []  # (seat, anon, item_text)
for i in range(1, len(sections), 2):
    seat, body = sections[i], sections[i + 1]
    body = body.split('隔离自报')[0]
    items = re.split(r'\n(?=\d+\.\s)', body)
    for it in items:
        anons = re.findall(r'P3-[0-9a-f]{8}', it)
        if anons:
            txt = re.sub(r'\s+', ' ', it).strip()
            for a in dict.fromkeys(anons):
                rows.append((seat.replace('FLAGS-', ''), a, txt))
print('flag rows (seat-anon pairs):', len(rows))
anon2rows = collections.defaultdict(list)
for s, a, t in rows:
    anon2rows[a].append((s, t))
print('distinct anons:', len(anon2rows))
missing = [a for a in anon2rows if a not in host]
print('anons missing from host-mapping:', missing)
case2anons = collections.defaultdict(list)
for a in anon2rows:
    case2anons[host[a]].append(a)
multi = {c: v for c, v in case2anons.items() if len(v) > 1}
print('cases with >1 anon:', multi)
print('distinct cases:', len(case2anons))

# ---- 历轮定案索引（r49..r69） ----
prior = {}  # case_id -> list of (round, annotation) ascending
for r in range(49, 70):
    p = BASE / 'data' / f'case-annotations-r{r}.json'
    if not p.exists():
        continue
    d = json.loads(p.read_text(encoding='utf-8'))
    for a in d['annotations']:
        prior.setdefault(a['case_id'], []).append((r, a))

# ---- R69 部分成立 84 件与 R70 manifest 落实层对勘 ----
r69 = json.loads((BASE / 'data' / 'case-annotations-r69.json').read_text(encoding='utf-8'))
partial69 = [a for a in r69['annotations'] if a['disposition'] == '部分成立']
print('r69 partial count:', len(partial69))
add = manifest['_r70_carryover_notes_addendum']
print('r70 addendum layer count:', len(add))
mismatch = []
for a in partial69:
    cid = a['case_id']
    if add.get(cid) != a['manifest_carry_suggestion']:
        mismatch.append(cid)
print('addendum mismatches:', mismatch)
extra = [c for c in add if c not in {a['case_id'] for a in partial69}]
print('addendum extra keys:', extra)
oth69 = collections.Counter(a['disposition'] for a in r69['annotations'])
print('r69 verdicts recount:', dict(oth69), 'total', len(r69['annotations']))
for disp in ('成立', '不成立', '未核'):
    print(disp, 'list:', [a['case_id'] for a in r69['annotations'] if a['disposition'] == disp])

# ---- 结局文本 R69 vs R70 全等核查 ----
m69 = json.loads((BASE / 'runs' / 'round69' / 'judging' / 'outcome-manifest.json').read_text(encoding='utf-8'))
diff = [c for c in cases if cases[c] != m69['cases'].get(c)]
print('outcome text diffs r69->r70:', diff, 'total cases', len(cases))

# ---- 承接表输出 ----
out = []
for cid in sorted(case2anons):
    anons = case2anons[cid]
    seats = sorted({s for a in anons for s, _ in anon2rows[a]})
    pr = prior.get(cid, [])
    latest = pr[-1] if pr else None
    pred = json.loads((R70 / 'predictions' / f'{cid}.json').read_text(encoding='utf-8'))
    ptxt = pred['prediction_text']
    out.append({
        'case_id': cid, 'anons': anons, 'seats': seats,
        'flag_texts': [f"{s}: {t}" for a in anons for s, t in anon2rows[a]],
        'outcome': cases[cid],
        'prior_rounds': [r for r, _ in pr],
        'latest_prior': ({'round': latest[0], 'disposition': latest[1]['disposition'],
                          'relation': latest[1].get('relation'), 'flag': latest[1].get('flag'),
                          'finding_head': latest[1]['finding'][:500]} if latest else None),
        'pred_q_count': ptxt.count('?') + ptxt.count('？'),
        'basis_first': pred['basis'][:60],
        'pred_head': ptxt[:150],
    })
(R70 / 'data_r70_review.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
print('review written:', len(out))

for e in out:
    lp = e['latest_prior']
    print(f"== {e['case_id']} anons={e['anons']} seats={e['seats']} prior={'R'+str(lp['round'])+'/'+lp['disposition'] if lp else 'NONE'} q={e['pred_q_count']}")
    for ft in e['flag_texts']:
        print('   FLAG', ft[:260])
    if lp:
        print('   PRIOR-FLAG', (lp['flag'] or '')[:200])

# ---- 特别核查：指令性字样全量复扫 cases 本体 ----
KEYS = ['请按', '請按', '须注', '須注', '评分时', '評分時', '比对时', '比對時', '使用时须', '使用時須',
        '分开统计', '分開統計', '勿以此斷', '请勿', '請勿', '不得', '切不', '勿以', '须以', '須以']
hits = {}
for cid, txt in cases.items():
    found = [k for k in KEYS if k in txt]
    if found:
        hits[cid] = found
print('directive keyword hits:', hits)
WIDE = ['请', '請', '须', '須', '勿']
wide = {}
for cid, txt in cases.items():
    if cid in hits:
        continue
    found = [k for k in WIDE if k in txt]
    if found:
        wide[cid] = found
print('wide-scan other cases:', wide)
split = manifest['_r56_lr2016_split']
print('LR2-016 split editor_note contains 评分时:', '评分时' in split['editor_note'], '| cases本体 contains:', '评分时' in cases['LR2-016'])
print('LR2-016 editor_note:', split['editor_note'][:300])

# 待核四件触及检查
flagged_cases = set(case2anons)
for cid in ('BZ-029', 'BZ-040', 'LY-537', 'YM-070'):
    print('pending-touch', cid, cid in flagged_cases)
