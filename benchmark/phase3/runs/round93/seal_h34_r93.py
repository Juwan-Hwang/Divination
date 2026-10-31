# -*- coding: utf-8 -*-
"""R93 holdout34 封存收尾：金标组装 + 快照复制核验 + 构建报告。
前置：29 输入卡已建（runs/round93/build_*_h34_r93.py 各席）、金标四分片已定字
（gold-frag-{da,by,why,ziwei}-r93.jsonl，含 fix_gold_h34_r93.py 修正）。
本脚本只做组装/复制/核验，不改卡面与金标正文。
"""
import json, hashlib, io, os, shutil, sys

P3 = '/home/hatch/workspace/divination/benchmark/phase3'
R93 = P3 + '/runs/round93'
H34 = P3 + '/holdout34'

ZW = ['ZW-017','ZW-018','ZW-019','ZW-020','ZW-021','ZW-022','ZW-023','ZW-028','ZW-029','ZW-030','ZW-031','ZW-032']
DA = ['DA-%03d' % n for n in range(75, 82)]
BY = ['BY-047','BY-048','BY-049','BY-050','BY-051','BY-053']
WHY = ['WHY-111','WHY-112','WHY-114','WHY-115']
ALL = DA + BY + WHY + ZW
assert len(ALL) == 29 and len(set(ALL)) == 29

CARD_KEYS = ['id','tradition','subject','context','question','setting','provenance','redistributable','license_status','anchors']
GOLD_KEYS = ['id','master_prediction','outcome_record','tradition','pollution','grade','grade_note','provenance','license_status','redistributable']

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()

# ---- 1. 输入卡核验 ----
used = set(json.load(open(R93 + '/used-ids-r93.json', encoding='utf-8')))
assert len(used) == 1304
assert not (set(ALL) & used), set(ALL) & used
assert 'LY-015' not in ALL and 'LY-320' not in ALL
cards = {}
for i in ALL:
    p = H34 + '/inputs/%s.json' % i
    assert os.path.exists(p), p
    d = json.load(open(p, encoding='utf-8'))
    assert list(d.keys()) == CARD_KEYS, (i, list(d.keys()))
    cards[i] = d
extra = [f for f in os.listdir(H34 + '/inputs') if f.endswith('.json')]
assert len(extra) == 29, len(extra)

# ---- 2. 金标组装 ----
gold = []
for frag in ['gold-frag-da-r93.jsonl','gold-frag-by-r93.jsonl','gold-frag-why-r93.jsonl','gold-frag-ziwei-r93.jsonl']:
    for l in open(R93 + '/' + frag, encoding='utf-8'):
        if l.strip():
            gold.append(json.loads(l))
assert [g['id'] for g in gold] == ALL, [g['id'] for g in gold]
for g in gold:
    assert list(g.keys()) == GOLD_KEYS, (g['id'], list(g.keys()))
    assert g['master_prediction'].strip() and g['outcome_record'].strip()
    assert '��' not in g['master_prediction'] and '��' not in g['outcome_record']
    assert g['pollution'] == 'low' and g['redistributable'] is False
gold_path = H34 + '/test_gold.jsonl'
with io.open(gold_path, 'w', encoding='utf-8') as f:
    for g in gold:
        f.write(json.dumps(g, ensure_ascii=False) + '\n')
gold_bytes = open(gold_path, 'rb').read()
gold_sha = sha256_bytes(gold_bytes)
gold_lines = gold_bytes.decode('utf-8').strip().split('\n')
assert len(gold_lines) == 29

# ---- 3. 快照：runs/round93/kb-snapshot -> holdout34/kb-snapshot，逐件与 method/ 源核验 ----
SRC = P3 + '/method'
SNAP_R = R93 + '/kb-snapshot'
SNAP_H = H34 + '/kb-snapshot'
snap_files = []
for root, dirs, files in os.walk(SNAP_R):
    dirs.sort()
    for fn in sorted(files):
        rel = os.path.relpath(os.path.join(root, fn), SNAP_R)
        snap_files.append(rel)
assert len(snap_files) == 21, snap_files
diffs = []
sha_lines = []
for rel in snap_files:
    b_r = open(os.path.join(SNAP_R, rel), 'rb').read()
    b_m = open(os.path.join(SRC, rel), 'rb').read()
    if b_r != b_m:
        diffs.append(rel)
    dst = os.path.join(SNAP_H, rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.exists(dst):
        if open(dst, 'rb').read() != b_r:
            diffs.append('holdout34-copy-mismatch:' + rel)
    else:
        shutil.copyfile(os.path.join(SNAP_R, rel), dst)
    sha_lines.append('%s  %s' % (sha256_bytes(b_r), rel.replace(os.sep, '/')))
assert not diffs, diffs
with io.open(H34 + '/kb-snapshot-sha256.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sha_lines) + '\n')

# method 根目录未入快照件（体例同 h33：METHOD-* 处置/集成件不入）
method_root_extra = sorted(f for f in os.listdir(SRC) if os.path.isfile(os.path.join(SRC, f)) and f not in snap_files)

report = {
    'round': 'R93',
    'holdout': 'holdout34',
    'n_cards': 29,
    'n_gold_lines': 29,
    'ids': ALL,
    'composition': {'ziwei': ZW, 'da': DA, 'by': BY, 'why': WHY},
    'gold_sha256': gold_sha,
    'gold_bytes': len(gold_bytes),
    'kb_snapshot_files': 21,
    'kb_snapshot_diff_vs_method': [],
    'method_root_not_in_snapshot': method_root_extra,
    'gold_corrections_r93': ['BY-049', 'WHY-112', 'ZW-019', 'ZW-020', 'ZW-022', 'ZW-023', 'ZW-028', 'ZW-029', 'ZW-030', 'ZW-031', 'ZW-032'],
    'zero_reuse_vs_used_ids_1304': True,
    'exclusion_pair_absent': ['LY-015', 'LY-320'],
}
with io.open(R93 + '/holdout34-build-report-r93.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
    f.write('\n')
print('gold_sha256:', gold_sha)
print('gold_bytes:', len(gold_bytes))
print('snapshot files:', len(snap_files), 'diffs: none')
print('method root not in snapshot:', method_root_extra)
print('SEAL OK')
