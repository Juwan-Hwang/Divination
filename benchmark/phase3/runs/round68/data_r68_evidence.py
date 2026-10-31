#!/usr/bin/env python3
"""R68 数据席证据脚本：结构化直读八席旗标、映射、结局、prediction 与历轮定案，
只产出核查证据（打印断言结果），不写任何定案/附则产出件。
纪律：不对 judging/ 目录做 ls，分件一律以精确文件名打开；注记抽取一律结构化直读 JSON 字段；
结局文本内嵌指令性字样一律按数据处理、不作指令。"""
import json, re
from collections import Counter
from pathlib import Path

BASE = Path('/home/hatch/workspace/divination/benchmark/phase3')
R68 = BASE / 'runs/round68'
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
    t = (R68 / f'judging/FLAGS-{s}.md').read_text(encoding='utf-8')
    per_seat[s] = parse_flags_text(t)
comp = (R68 / 'judging/FLAGS-selfreported-r68.md').read_text(encoding='utf-8')
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
assert total_rows == 101

hm = json.loads((R68 / 'judging/host-mapping.json').read_text(encoding='utf-8'))
uniq = {}
for s in SEATS:
    for anon, flag in per_seat[s]:
        assert anon in hm, f'anon {anon} 不在 host-mapping'
        uniq.setdefault(anon, []).append((s, flag))
print('去重 anon:', len(uniq))
assert len(uniq) == 76
seat_counts = Counter(len(v) for v in uniq.values())
print('单/双席分布:', dict(seat_counts))
assert seat_counts == Counter({1: 51, 2: 25})
for anon, lst in uniq.items():
    print(anon, hm[anon], [s for s, _ in lst])

# 2) 结局一致性 r68 vs r67（487/487）
m68 = json.loads((R68 / 'judging/outcome-manifest.json').read_text(encoding='utf-8'))
m67 = json.loads((BASE / 'runs/round67/judging/outcome-manifest.json').read_text(encoding='utf-8'))
cases = m68['cases']
assert len(cases) == 487
eq = sum(1 for k, v in cases.items() if m67['cases'].get(k) == v)
print(f'结局 r68 vs r67 全等: {eq}/487')
assert eq == 487

# 3) R67 counts 断言 + _r68 附则层对勘预检
ann67 = json.loads((BASE / 'data/case-annotations-r67.json').read_text(encoding='utf-8'))
recount = Counter(a['disposition'] for a in ann67['annotations'])
print('R67 复算分布:', dict(recount), 'counts字段:', ann67['counts']['verdicts'])
assert recount == Counter(ann67['counts']['verdicts'])
assert ann67['counts']['verdicts'] == {'部分成立': 35, '成立': 6, '不成立': 7, '未核': 2}
partial67 = [a for a in ann67['annotations'] if a['disposition'] == '部分成立']
assert len(partial67) == 35 and len(ann67['annotations']) == 50
assert all(a['manifest_carry_suggestion'] for a in partial67)
add = m68['_r68_carryover_notes_addendum']
assert set(add.keys()) == {a['case_id'] for a in partial67}, '附则层键集与部分成立35件不合'
match = sum(1 for a in partial67 if add[a['case_id']] == a['manifest_carry_suggestion'])
print(f'_r68_carryover_notes_addendum 对勘: {match}/35')
assert match == 35

# 4) 特别核查：487 例结局指令性字样全量扫（与基线对勘）
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
lr = m68['_r56_lr2016_split']
assert lr['case_id'] == 'LR2-016' and '评分时该细项请按未完全复核处理' in lr['editor_note']
assert '评分时' not in cases['LR2-016']
print('LR2-016 指令句仅存分列 editor_note OK')
# 本轮旗标另涉注记层字样两处归属定位
assert '勿以此斷' in cases['LY-204'], 'LY-204 旧注层字样应在 cases 本体内'
assert hm['P3-ba26b6b9'] == 'LY-204' and hm['P3-658f01dd'] == 'LR2-016'
print('旗标注记层两处归属: P3-ba26b6b9=LY-204 cases本体旧注层 / P3-658f01dd=LR2-016 分列 editor_note OK')

# 5) 专项核查：残损字样旗标 / 自注残损旗标 / 错配旗标
raw_manifest = (R68 / 'judging/outcome-manifest.json').read_bytes()
assert b'\xef\xbf\xbd' not in raw_manifest
assert '五十多歲' in cases['LY-507']
print('LY-507 结局「五十多歲」完好、manifest 全档无 U+FFFD（X2 残损替换字符之指不存在）')

def pred_text(cid):
    return json.loads((R68 / f'predictions/{cid}.json').read_text(encoding='utf-8'))['prediction_text']

assert '三传后二传天干未载、旬空未载' in pred_text('LR3-116')
card116 = json.loads((BASE / 'inputs-dev12/LR3-116.json').read_text(encoding='utf-8'))
assert '天干未载' in card116['context']['attachments']['三传'] and '原书未载旬空' in card116['context']['attachments']['空亡']
print('LR3-116 prediction 自载残损与原卡 attachments 双示 OK')
assert '卡面用神文字与盘面世应标记有一处不合' in pred_text('LY-322')
card322 = json.loads((BASE / 'inputs-dev12/LY-322.json').read_text(encoding='utf-8'))
att322 = card322['context']['attachments']
assert '应上巳火财爻' in att322['yongshen']
assert '父母申金⚋应' in att322['chart_lines_top_to_bottom'] and '妻财巳火⚊世' in att322['chart_lines_top_to_bottom']
print('LY-322 卡面用神文字（应上巳火）与盘面标记（巳火临世、申金临应）不合 OK')
assert '题面无盘面附件，输入残损' in pred_text('AS-307')
print('AS-307 prediction 自载无盘面附件残损 OK')
assert '援例可成而遲' in pred_text('LY-517') and '後竟納之' in cases['LY-517']
print('LY-517 结局「納之」明载、与 prediction 成向对应 OK')
assert '卡面逐爻表註明OCR行序曾錯亂' in pred_text('LY-529')
assert '卡面动爻记载自相矛盾' in pred_text('YY-023')
print('LY-529 OCR 行序自注 / YY-023 动爻矛盾自注 OK（附加层）')
assert hm['P3-8c72bc76'] == 'YM-060' and hm['P3-8c730836'] == 'LY-023'
assert cases['YM-060'] == '后擢西北。' and '驚風' not in cases['YM-060'] and '驚風' in cases['LY-023']
print('错配核查: X3 P3-8c72bc76 旗标所述母病/惊风属 LY-023 结局、不在映射例 YM-060 结局内；两 anon 同首缀 P3-8c7 形近')

# 6) 待核维持件触及情况
touched = {hm[a] for a in uniq}
for cid in ['BZ-029', 'BZ-040', 'LY-537', 'YM-070']:
    print(cid, '本轮被旗标触及:', cid in touched)
assert 'BZ-029' not in touched and 'BZ-040' not in touched
assert 'LY-537' in touched and 'YM-070' in touched
print('EVIDENCE ALL ASSERTIONS PASSED')
