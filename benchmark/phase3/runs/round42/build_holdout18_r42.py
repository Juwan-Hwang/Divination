#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R42 数据席 D3：holdout18 建卡与封存（构成门校验版）。

口径：runs/round42/PREREG.md §4.2/§4.3/§5、§1.2 转录规格 v1；
供给定案：runs/round42/data-verify/ZC-RECHECK-R42.md、HOST-RULING-ZC164.md、
SUPPLY-R42.md；体例承 runs/round41/build_holdout17_r41.py（显式路径、禁通配遍历）。

本脚本先行三项实核，任一门不过即只登记、不组集（PREREG §4.3「不够数即只登记」）：
  门一 例级零复用：已用并集＝holdout3–17 金标 id（逐文件显式打开）＋dev9 487 id
       （runs/round42/batches.json），逐 id 实核；
  门二 测字新鲜可用数：选例池逐源扣账——留库存 12 与「R41 新核未选 12」经实核
       为同一集合（zc-candidates-r41.jsonl 29 行扣 holdout17 已入选 17 行＝12 行，
       与 holdout17 封存日志 §五留库存清单逐 id 全等），不得重复计数；
       加本轮新增 3（zc-candidates-r42.jsonl），新鲜可用实数＝15；
  门三 构成门：PREREG §4.2 第一档要求 C＝20，新鲜可用 15＜20 → 门不过。
门不过时：不写 holdout18/inputs、不写 test_gold.jsonl、不落封存结论；
仅写构建报告 build-holdout18-report.json（含 §5 扫描第一道结果）并以退出码 2 结束。
构成口径若经主持裁决变更，自本脚本 GATE 节改写后重跑（口径变更只能自主持裁决起）。
内容级断语扫描（PREREG §5 第一道）：取材时先以字段名黑名单拦截断语类字段，
再以 scan_content_markers_r42.py 之标记集扫 input_side 全字段（结果入构建报告）。
只建卡与封存：不作断、不评分、不做 git 操作。
"""
import json, os, sys

BASE = os.path.expanduser('~/workspace/divination/benchmark/phase3')
R42 = os.path.join(BASE, 'runs/round42')
sys.path.insert(0, R42)
from scan_content_markers_r42 import scan_content, scan_field_names  # PREREG §5 标记集

def load_jsonl(p):
    return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]

# ---------------- 已用并集（逐文件显式路径，禁通配） ----------------
HOLDOUT_GOLDS = [os.path.join(BASE, f'holdout{i}/test_gold.jsonl') for i in
                 (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)]
used_gold = set()
for p in HOLDOUT_GOLDS:
    for r in load_jsonl(p):
        used_gold.add(r['id'])
batches = json.load(open(os.path.join(R42, 'batches.json'), encoding='utf-8'))
used_dev = set()
for v in batches.values():
    used_dev.update(v)
used_union = used_gold | used_dev

# ---------------- 测字选例池逐源扣账 ----------------
ZC_INVENTORY_TASK = ['ZC-139', 'ZC-143', 'ZC-144', 'ZC-145', 'ZC-146', 'ZC-149', 'ZC-150',
                     'ZC-154', 'ZC-156', 'ZC-157', 'ZC-158', 'ZC-160']  # 派单列名（承 h17 封存日志 §五）
zc_r41 = load_jsonl(os.path.join(BASE, 'runs/round41/data-verify/zc-candidates-r41.jsonl'))
zc_r41_ids = [r['id'] for r in zc_r41]
h17_zc_sel = [r['id'] for r in load_jsonl(os.path.join(BASE, 'holdout17/test_gold.jsonl'))
              if r['id'].startswith('ZC-')]
zc_r41_unselected = [i for i in zc_r41_ids if i not in h17_zc_sel]
zc_r42 = load_jsonl(os.path.join(R42, 'data-verify/zc-candidates-r42.jsonl'))
zc_r42_ids = [r['id'] for r in zc_r42]
fresh_zc = sorted(set(zc_r41_unselected) | set(zc_r42_ids))
assert all(i not in used_union for i in fresh_zc), '新鲜池与已用并集相交'
pool_accounting = {
    'zc_candidates_r41_total': len(zc_r41_ids),
    'holdout17_zc_selected_from_r41': sorted(set(zc_r41_ids) & set(h17_zc_sel)),
    'r41_unselected_derived': zc_r41_unselected,
    'inventory_list_from_task_and_h17_seal_log': ZC_INVENTORY_TASK,
    'inventory_equals_r41_unselected': sorted(ZC_INVENTORY_TASK) == sorted(zc_r41_unselected),
    'r42_new': zc_r42_ids,
    'fresh_available_union': fresh_zc,
    'fresh_available_count': len(fresh_zc),
    'task_stated_pool_count': 27,
    'pool_count_discrepancy': ('派单「库存12＋R41新核未选12＋新增3＝27」中前两项经实核为同一集合'
                               '（zc-candidates-r41.jsonl 29 行－h17 已入选 17 行＝12 行，'
                               '与 h17 封存日志 §五留库存 12 例逐 id 全等），重复计数 12；'
                               'ZC-RECHECK-R42 的 Z＝35 为累计合规数（32＋3），未扣 holdout17 已用 20 例。'
                               '另 ZC-122 台账为 A-low 但经 R41 普查身份未定旗标排除（ZC-CENSUS-R41 §三），不计入。'),
}

# ---------------- PREREG §5 第一道：候选材料 input_side 制备期扫描 ----------------
FIELD_BLACKLIST_NOTE = '字段名黑名单先行拦截（scan_field_names），再内容级扫描（scan_content）'
stage1 = {}

def stage1_scan(cid, input_obj):
    fn = scan_field_names(input_obj)
    ch = scan_content(input_obj)
    stage1[cid] = {'fieldname_hits': [list(h) for h in fn],
                   'content_hits': [list(h) for h in ch]}

zc_rows = {r['id']: r for r in zc_r41 + zc_r42}
for cid in fresh_zc:
    stage1_scan(cid, zc_rows[cid].get('input_material', {}))

DA_SEL = ['DA-134', 'DA-145', 'DA-152', 'DA-159', 'DA-167', 'DA-185', 'DA-206']
BYZ_CAND = ['BYZ-078', 'BYZ-107', 'BYZ-114']  # 序1–3 有候选行；序4–7（BYZ-018/019/020/025）无候选行，见 material_gaps
CY_CAND = ['CY-034', 'CY-040', 'CY-047', 'CY-061']  # 慕农序1–4 有候选行；序5–6（CY-010/011）无，见 material_gaps
dabyz = {r['id']: r for r in load_jsonl(os.path.join(BASE, 'runs/round41/data-verify/da-byz-candidates-r41.jsonl'))}
for cid in DA_SEL + BYZ_CAND:
    c = dabyz[cid]
    stage1_scan(cid, {'subject': c.get('subject'), 'question': c.get('question_or_topic'),
                      'asked_at': c.get('asked_at'), 'chart': c.get('chart', {})})
yxs = {r['id']: r for r in load_jsonl(os.path.join(BASE, 'runs/round41/data-verify/yxs-candidates-r41.jsonl'))}
for cid in CY_CAND:
    stage1_scan(cid, yxs[cid].get('input_side', {}))
munong = {r['id']: r for r in load_jsonl(os.path.join(BASE, 'expansion12/liuren-cuiyan/cases-munong.jsonl'))}
for cid in ['CY-010', 'CY-011']:
    r = munong[cid]
    stage1_scan(cid, {'subject': r.get('subject'), 'question': r.get('question_or_topic'),
                      'asked_at': r.get('asked_at')})  # 慕农村台账无课式字段，题面三字段先扫；课式须回 render 页图转录后另扫

material_gaps = [
    'BYZ 序4–7（BYZ-018/019/020/025，承 SUPPLY-R42 §二.2 排序外原序）：runs/round41/data-verify/da-byz-candidates-r41.jsonl 无候选行（该文件 BYZ 仅含 R41 候选 10 例），建卡级材料须回原书页图逐例制备（体例同 R41 候选制备），本轮未制备。',
    'CY 序5–6（CY-010/011，承 SUPPLY-R42 §三.1 排序外原序）：runs/round41/data-verify/yxs-candidates-r41.jsonl 无候选行（仅含候选 10 例），expansion12/liuren-cuiyan/cases-munong.jsonl 台账行无课式字段，建卡级材料须回 render 页图逐字转录课盘列（承 h17 裁定二体例），本轮未制备。',
]

# ---------------- GATE：构成门 ----------------
C_REQUIRED = 20  # PREREG §4.2 第一档（Z≥20 → C＝20，L＝20，T＝40）；派单写死 T＝40
gate = {
    'used_union': {'holdout3_17_gold_ids': len(used_gold), 'dev9_ids': len(used_dev),
                   'union': len(used_union), 'overlap': len(used_gold & used_dev)},
    'pool_accounting': pool_accounting,
    'c_required': C_REQUIRED,
    'fresh_zc_available': len(fresh_zc),
    'verdict': 'FAIL' if len(fresh_zc) < C_REQUIRED else 'PASS',
    'shortage': C_REQUIRED - len(fresh_zc),
    'note': ('新鲜可用 15＜20：若强行组集，须复用已用例（违例级零复用）、降级/旗标例'
             '（违全 A-low；ZC-122 旗标排除在案）或他源填数（违 PREREG §4.2 不以他源破上限填数），三路皆禁。'
             'PREREG §4.2 第二档（13≤Z≤19 → C＝Z、L＝Z、T＝2Z）以何 Z 口径适用、ZC-164 在不足数时'
             '是否仍列备选末位，均属主持裁决事项，本席不自改构成。'),
}

report = {'round': 'R42', 'seat': 'D3 build/seal', 'gate': gate,
          'scan_stage1_candidate_prep': {'method': FIELD_BLACKLIST_NOTE, 'per_id': stage1},
          'material_gaps': material_gaps,
          'scan_stage2_card_selfcheck': '未执行：构成门不过、未建卡，无卡可扫（PREREG §5 第二道以建卡为前提）',
          'scan_stage3_host_verify': '主持验封道，非本席执行',
          'remediation': [
              {'ids': CY_CAND, 'stage': '第一道（候选制备期）',
               'finding': 'yxs-candidates-r41.jsonl 四行 input_side.chart.三传.断语线索 子字段：字段名黑名单命中（断语）＋内容 L1 命中（断曰）各 1/例——即 h17 污染事件的同一带入路径，本轮于制备期被拦截。',
               'disposition': '建卡时该子字段整项不入卡（断语只许入金标侧，PREREG §5 制备纪律）；本轮未建卡，拦截事实在此存证，组集重开时按此执行并于建卡自校验（第二道）复扫零命中为准。'},
          ],
          'gold_sha256': None,
          'outputs_written': []}
with open(os.path.join(R42, 'build-holdout18-report.json'), 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
print('used union:', len(used_gold), len(used_dev), len(used_union))
print('fresh ZC:', len(fresh_zc), fresh_zc)
print('inventory == r41 unselected:', pool_accounting['inventory_equals_r41_unselected'])
print('stage1 hits:', {k: (len(v['fieldname_hits']), len(v['content_hits'])) for k, v in stage1.items() if v['fieldname_hits'] or v['content_hits']})
print('GATE:', gate['verdict'], 'shortage:', gate['shortage'])
sys.exit(2 if gate['verdict'] == 'FAIL' else 0)
