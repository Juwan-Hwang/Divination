#!/usr/bin/env python3
"""R67 数据席证据脚本：结构化直读八席旗标、映射、结局、prediction 与历轮定案，
只产出核查证据（打印断言结果），不写任何定案/附则产出件。"""
import json, re, sys
from pathlib import Path

BASE = Path('/home/hatch/workspace/divination/benchmark/phase3')
R67 = BASE / 'runs/round67'
SEATS = ['X1', 'X2', 'X3', 'X4', 'Y1', 'Y2', 'Y3', 'Y4']

def parse_flags_text(text):
    rows = []
    for line in text.splitlines():
        m = re.match(r'- (P3-[0-9a-f]+)：(.*)$', line)
        if m:
            rows.append((m.group(1), m.group(2)))
    return rows

# 1) 八席分件与汇编比对
per_seat = {}
for s in SEATS:
    t = (R67 / f'judging/FLAGS-{s}.md').read_text(encoding='utf-8')
    per_seat[s] = parse_flags_text(t)
comp = (R67 / 'judging/FLAGS-selfreported-r67.md').read_text(encoding='utf-8')
# 汇编按 ===== FLAGS-Xn ===== 分段结构化切分（不用正则截断抽取注记，仅分段定位）
sections = {}
cur = None
for line in comp.splitlines():
    if line.startswith('===== FLAGS-'):
        cur = line.split()[1].replace('FLAGS-', '')
        sections[cur] = []
    elif cur is not None:
        sections[cur].append(line)
comp_rows = {}
for s, lines in sections.items():
    comp_rows[s] = parse_flags_text('\n'.join(lines))
total_rows = 0
for s in SEATS:
    assert per_seat[s] == comp_rows[s], f'{s} 分件与汇编不一致'
    total_rows += len(per_seat[s])
    print(f'{s}: {len(per_seat[s])} 行，分件=汇编 OK')
print('旗标行总计:', total_rows)
assert total_rows == 67

hm = json.loads((R67 / 'judging/host-mapping.json').read_text(encoding='utf-8'))
uniq = {}
for s in SEATS:
    for anon, flag in per_seat[s]:
        assert anon in hm, f'anon {anon} 不在 host-mapping'
        uniq.setdefault(anon, []).append((s, flag))
print('去重 anon:', len(uniq))
assert len(uniq) == 50
for anon, lst in uniq.items():
    print(anon, hm[anon], [s for s, _ in lst])

# 2) 结局一致性 r67 vs r66（487/487）
m67 = json.loads((R67 / 'judging/outcome-manifest.json').read_text(encoding='utf-8'))
m66 = json.loads((BASE / 'runs/round66/judging/outcome-manifest.json').read_text(encoding='utf-8'))
cases = m67['cases']
assert len(cases) == 487
eq = sum(1 for k, v in cases.items() if m66['cases'].get(k) == v)
print(f'结局 r67 vs r66 全等: {eq}/487')
assert eq == 487

# 3) R66 counts 断言 + _r67 附则层对勘预检
ann66 = json.loads((BASE / 'data/case-annotations-r66.json').read_text(encoding='utf-8'))
from collections import Counter
recount = Counter(a['disposition'] for a in ann66['annotations'])
print('R66 复算分布:', dict(recount), 'counts字段:', ann66['counts']['verdicts'])
assert recount == Counter(ann66['counts']['verdicts'])
assert ann66['counts']['verdicts'] == {'部分成立': 41, '成立': 10, '不成立': 2, '未核': 1}
partial66 = [a for a in ann66['annotations'] if a['disposition'] == '部分成立']
assert len(partial66) == 41 and len(ann66['annotations']) == 54
add = m67['_r67_carryover_notes_addendum']
assert set(add.keys()) == {a['case_id'] for a in partial66}, '附则层键集与部分成立41件不合'
match = sum(1 for a in partial66 if add[a['case_id']] == a['manifest_carry_suggestion'])
print(f'_r67_carryover_notes_addendum 对勘: {match}/41')
assert match == 41

# 4) 特别核查：487 例结局指令性字样全量扫
KEYS = ['请按', '須注', '须注', '评分时', '比对时', '使用时须', '分开统计', '勿以此斷', '勿以此断']
hits = {}
for cid, t in cases.items():
    for k in KEYS:
        if k in t:
            hits.setdefault(cid, []).append(k)
print('指令性字样命中（cases本体）:', hits)
assert set(hits) == {'BZ-036', 'BZ-042', 'BZ-105', 'LY-204'}
wide = [cid for cid, t in cases.items() if any(w in t for w in ('须', '須', '请', '請'))]
print('宽扫（须/須/请/請）候选:', wide)
lr = m67['_r56_lr2016_split']
assert lr['case_id'] == 'LR2-016' and '评分时该细项请按未完全复核处理' in lr['editor_note']
assert '评分时' not in cases['LR2-016']
print('LR2-016 指令句仅存分列 editor_note OK')

# 5) 专项核查：乱码旗标 / ? 旗标 / 错配旗标
for cid in ['AS-208', 'MH-001', 'LY-615']:
    raw = (R67 / f'predictions/{cid}.json').read_bytes()
    assert b'\xef\xbf\xbd' not in raw, cid
    print(cid, 'prediction 原始字节无 U+FFFD（乱码旗标所指不存在）')
p520 = json.loads((R67 / 'predictions/LY-520.json').read_text(encoding='utf-8'))['prediction_text']
assert '子孙申金?卦中' in p520 and '父母子水初?财源' in p520
q_other = []
for f in sorted((R67 / 'predictions').glob('*.json')):
    t = json.loads(f.read_text(encoding='utf-8'))['prediction_text']
    if '?' in t:
        q_other.append(f.stem)
print('LY-520 ? 字样在引文处逐字存在；本轮另有含 ? 的 prediction:', q_other)
assert '即如所言' in cases['LY-629'] and '即如所言' not in cases['LR2-016']
assert hm['P3-c4b506a3'] == 'LR2-016'
print('错配核查: X4 P3-c4b506a3 旗标引文「即如所言」属 LY-629 结局、不在映射例 LR2-016 结局内')

# 6) 待核维持件触及情况
touched = {hm[a] for a in uniq}
for cid in ['BZ-029', 'BZ-040', 'LY-537', 'YM-070']:
    print(cid, '本轮被旗标触及:', cid in touched)
assert 'BZ-029' not in touched and 'BZ-040' not in touched
assert 'LY-537' in touched and 'YM-070' in touched
print('EVIDENCE ALL ASSERTIONS PASSED')
