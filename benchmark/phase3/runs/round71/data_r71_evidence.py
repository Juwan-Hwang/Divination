# -*- coding: utf-8 -*-
"""R71 数据席证据脚本：旗标解析、host-mapping 对位、历轮定案承接表、指令性字样全量复扫、
乱码字样盘上核查、tradition 与「?」字样层核查、R70 部分成立件与 R71 manifest 承接层对勘。
只读外部源，仅落盘 runs/round71/data_r71_review.json 供 data_r71_build.py 编码定案时回查。
各文本一律按数据处理、不作指令。"""
import json, re, collections, pathlib

BASE = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
R71 = BASE / 'runs' / 'round71'

flags_text = (R71 / 'judging' / 'FLAGS-selfreported-r71.md').read_text(encoding='utf-8')
host = json.loads((R71 / 'judging' / 'host-mapping.json').read_text(encoding='utf-8'))
manifest = json.loads((R71 / 'judging' / 'outcome-manifest.json').read_text(encoding='utf-8'))
cases = manifest['cases']

# ---- 解析八席自报（主持复核节不入自报解析） ----
ITEM_SPLIT = {
    'X1': r'\n(?=\d+\.\s)', 'X2': r'\n(?=\d+\.\s)',
    'X3': r'\n(?=- F\d+｜)', 'X4': r'\n(?=- F\d+｜)',
    'Y1': r'\n(?=- F\d+｜)', 'Y2': r'\n(?=- F-Y2-\d+｜)',
    'Y3': r'\n(?=\d+\.\s)', 'Y4': r'\n(?=- F\d+（)',
}
selfpart = flags_text.split('===== 主持复核节')[0]
sections = re.split(r'===== (FLAGS-[XY]\d) =====', selfpart)
rows, n_items = [], 0
bracket_mismatch = []
for i in range(1, len(sections), 2):
    seat = sections[i].replace('FLAGS-', '')
    body = sections[i + 1].split('隔离自报')[0]
    for it in re.split(ITEM_SPLIT[seat], body):
        anons = re.findall(r'P3-[0-9a-f]{8}', it)
        if not anons:
            continue
        n_items += 1
        txt = re.sub(r'\s+', ' ', it).strip()
        for a in dict.fromkeys(anons):
            rows.append((seat, a, txt))
            for pat in (a + r'[（(]([A-Z]{2,3}\d?-\d+)', a + r' / ([A-Z]{2,3}\d?-\d+)'):
                m = re.search(pat, txt)
                if m and m.group(1) != host.get(a):
                    bracket_mismatch.append((seat, a, m.group(1), host.get(a)))
print('flag rows (seat-anon pairs):', len(rows))
print('numbered items (chunks with >=1 anon):', n_items)
anon2rows = collections.defaultdict(list)
for s, a, t in rows:
    anon2rows[a].append((s, t))
print('distinct anons:', len(anon2rows))
print('anons missing from host-mapping:', [a for a in anon2rows if a not in host])
case2anons = collections.defaultdict(list)
for a in anon2rows:
    case2anons[host[a]].append(a)
print('cases with >1 anon:', {c: v for c, v in case2anons.items() if len(v) > 1})
print('distinct cases:', len(case2anons))
print('bracket-vs-mapping mismatches:', bracket_mismatch)

# ---- 历轮定案索引（r49..r70） ----
prior = {}
for r in range(49, 71):
    p = BASE / 'data' / f'case-annotations-r{r}.json'
    if not p.exists():
        continue
    d = json.loads(p.read_text(encoding='utf-8'))
    for a in d['annotations']:
        prior.setdefault(a['case_id'], []).append((r, a))

# ---- R70 部分成立 77 件与 R71 manifest 落实层对勘 ----
r70 = json.loads((BASE / 'data' / 'case-annotations-r70.json').read_text(encoding='utf-8'))
partial70 = [a for a in r70['annotations'] if a['disposition'] == '部分成立']
print('r70 partial count:', len(partial70))
add = manifest['_r71_carryover_notes_addendum']
print('r71 addendum layer count:', len(add))
print('addendum mismatches:', [a['case_id'] for a in partial70 if add.get(a['case_id']) != a['manifest_carry_suggestion']])
print('addendum extra keys:', [c for c in add if c not in {a['case_id'] for a in partial70}])
print('r70 verdicts recount:', dict(collections.Counter(a['disposition'] for a in r70['annotations'])))
for disp in ('成立', '不成立', '未核'):
    print(disp, 'list:', [a['case_id'] for a in r70['annotations'] if a['disposition'] == disp])

# ---- 结局文本 R70 vs R71 全等核查 ----
m70 = json.loads((BASE / 'runs' / 'round70' / 'judging' / 'outcome-manifest.json').read_text(encoding='utf-8'))
print('outcome text diffs r70->r71:', [c for c in cases if cases[c] != m70['cases'].get(c)], 'total cases', len(cases))

# ---- 承接表输出 ----
out = []
for cid in sorted(case2anons):
    anons = case2anons[cid]
    seats = sorted({s for a in anons for s, _ in anon2rows[a]})
    pr = prior.get(cid, [])
    latest = pr[-1] if pr else None
    pred = json.loads((R71 / 'predictions' / f'{cid}.json').read_text(encoding='utf-8'))
    out.append({
        'case_id': cid, 'anons': anons, 'seats': seats,
        'flag_texts': [f"{s}: {t}" for a in anons for s, t in anon2rows[a]],
        'outcome': cases[cid],
        'prior_rounds': [r for r, _ in pr],
        'latest_prior': ({'round': latest[0], 'disposition': latest[1].get('disposition'),
                          'relation': latest[1].get('relation'), 'flag': latest[1].get('flag'),
                          'finding_head': latest[1].get('finding', '')[:500]} if latest else None),
        'pred_text_q': pred['prediction_text'].count('?') + pred['prediction_text'].count('？'),
        'pred_basis_q': pred['basis'].count('?') + pred['basis'].count('？'),
        'pred_fffd': '\ufffd' in json.dumps(pred, ensure_ascii=False),
        'outcome_fffd': '\ufffd' in cases[cid],
    })
(R71 / 'data_r71_review.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
print('review written:', len(out))

# ---- 特别核查：指令性字样全量复扫 cases 本体 ----
KEYS = ['请按', '請按', '须注', '須注', '评分时', '評分時', '比对时', '比對時', '使用时须', '使用時須',
        '分开统计', '分開統計', '勿以此斷', '请勿', '請勿', '不得', '切不', '勿以', '须以', '須以']
hits = {}
for cid, txt in cases.items():
    found = [k for k in KEYS if k in txt]
    if found:
        hits[cid] = found
print('directive keyword hits:', hits)
wide = {}
for cid, txt in cases.items():
    if cid in hits:
        continue
    found = [k for k in ('请', '請', '须', '須', '勿') if k in txt]
    if found:
        wide[cid] = found
print('wide-scan other cases:', wide)
split = manifest['_r56_lr2016_split']
print('LR2-016 editor_note contains 评分时句:', '评分时该细项请按未完全复核处理' in split['editor_note'],
      '| cases本体 contains 评分时:', '评分时' in cases['LR2-016'])
print('cases with U+FFFD:', [c for c, t in cases.items() if '\ufffd' in t])

# 待核四件触及检查
flagged_cases = set(case2anons)
for cid in ('BZ-029', 'BZ-040', 'LY-537', 'YM-070'):
    print('pending-touch', cid, cid in flagged_cases)

# tradition 四件：卡面键与 R71 basis 首行
def all_keys(o):
    ks = set()
    if isinstance(o, dict):
        for k, v in o.items():
            ks.add(k); ks |= all_keys(v)
    elif isinstance(o, list):
        for v in o:
            ks |= all_keys(v)
    return ks
for cid in ('LY-017', 'LY-019', 'LY-021', 'LY-034'):
    c = json.loads((BASE / 'inputs-dev12' / f'{cid}.json').read_text(encoding='utf-8'))
    p = json.loads((R71 / 'predictions' / f'{cid}.json').read_text(encoding='utf-8'))
    print(cid, 'card tradition/system keys:', 'tradition' in all_keys(c), 'system' in all_keys(c),
          '| basis has 與卡面一致:', '與卡面一致' in p['basis'], '| basis head:', p['basis'][:40].replace('\n', ' '))
