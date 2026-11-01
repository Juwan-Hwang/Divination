# R95 数据席落盘脚本（只标注与承接登记；不改分数／卡面／金标）
import json, copy, re
from collections import Counter

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
r94 = json.load(open(f'{BASE}/data/case-annotations-r94.json'))
add94 = open(f'{BASE}/data/manifest-carryover-r94-addendum.md', encoding='utf-8').read()
man95 = json.load(open(f'{BASE}/runs/round95/judging/outcome-manifest.json'))
man94 = json.load(open(f'{BASE}/runs/round94/judging/outcome-manifest.json'))
plat_map = json.load(open(f'{BASE}/runs/round95/judging/host-mapping.json'))
flags_md = open(f'{BASE}/runs/round95/judging/judge-flags-r95.md', encoding='utf-8').read()

# ---- 底本断言 ----
ann94 = r94['annotations']
assert len(ann94) == 535, len(ann94)
assert Counter(a['disposition'] for a in ann94) == {'成立': 14, '部分成立': 445, '不成立': 73, '未核': 3}

# ---- 承接对勘：_r94 层 7 件与 r94 附则 §三逐字对勘 ----
lay = man95['_r94_carryover_notes_addendum']
assert list(lay.keys()) == ['AS-210', 'BY-049', 'WHY-115', 'SECTION8-MONITORING-R94',
                            'HOLDOUT34-OPENED', 'W57', 'SUPPLY-RECOUNT-R94'], list(lay.keys())
for cid in ('AS-210', 'BY-049', 'WHY-115'):
    bar = [a for a in ann94 if a['case_id'] == cid and a.get('registered_round') == 94]
    assert len(bar) == 1, cid
    assert lay[cid] == bar[0]['manifest_carry_suggestion'], cid
    assert lay[cid] in add94, cid
for k in ('SECTION8-MONITORING-R94', 'HOLDOUT34-OPENED', 'W57', 'SUPPLY-RECOUNT-R94'):
    assert lay[k] in add94, k
# 落实数：7／出入 0

# ---- 旗标 anon 对位（形近串号逐件复核：期望映射写死） ----
bullets = [ln.strip() for ln in flags_md.splitlines() if ln.strip().startswith('- P3-')]
assert len(bullets) == 70, len(bullets)
flag_anons = [re.search(r'P3-[0-9a-f]{8}', ln).group(0) for ln in bullets]
assert len(set(flag_anons)) == 70
EXPECTED = {
 'P3-00a8fa53': 'LY-231', 'P3-01e35d48': 'LY-433', 'P3-025aa811': 'LY-104',
 'P3-035e26fb': 'AS-014', 'P3-0e44d904': 'LY-504', 'P3-106acbd1': 'LY-426',
 'P3-2fe53899': 'LY-011', 'P3-19286a3a': 'LY-320', 'P3-2f191354': 'BZ-016',
 'P3-34349d2d': 'BZ-105', 'P3-3470ddb2': 'BQ-025', 'P3-1f61397e': 'BQ-021',
 'P3-289b3627': 'YY-022', 'P3-28119a8b': 'LY-441', 'P3-3dbc55d8': 'LY-513',
 'P3-146d2c82': 'YM-059', 'P3-11b28378': 'LY-255', 'P3-14c6414b': 'BZ-104',
 'P3-191578e0': 'YY2-004', 'P3-1cf7f09b': 'LY-216', 'P3-1d488a4d': 'LR3-006',
 'P3-1f07d096': 'LR2-022', 'P3-1fd60dbe': 'LY-103', 'P3-320a3c86': 'LY-627',
 'P3-3a535406': 'BZ-019', 'P3-3c82433a': 'BZ-037', 'P3-40150039': 'YY-023',
 'P3-4b26ba32': 'LY-528', 'P3-46fef5c0': 'YM-068', 'P3-457ed5ba': 'LY-623',
 'P3-54af3aef': 'LY-510', 'P3-583a38e3': 'LY-425', 'P3-58b5d858': 'YM-030',
 'P3-5a29793a': 'LY-533', 'P3-5b543baa': 'LY-329', 'P3-5d3944b8': 'LY-023',
 'P3-6089bfea': 'LY-508', 'P3-6225d3d7': 'LY-220', 'P3-650d181f': 'OC-029',
 'P3-66bc8c22': 'LR3-101', 'P3-6af24548': 'YM-070', 'P3-6c5acf4c': 'LR2-016',
 'P3-76d46c61': 'LR2-023', 'P3-86103de5': 'LR3-112', 'P3-9c89678c': 'LY-436',
 'P3-a07cdd52': 'LY-437', 'P3-8ec32bcf': 'BQ-001', 'P3-90f80c39': 'LY-629',
 'P3-9a54d7d9': 'LY-222', 'P3-834377ae': 'LY-458', 'P3-a69298b5': 'LY-531',
 'P3-81849382': 'AS-015', 'P3-8d79d3b3': 'LY-205', 'P3-a2ac77fd': 'AS-004',
 'P3-8d5dfa7c': 'LR2-024', 'P3-a87ddcc9': 'LY-028', 'P3-ad4aa496': 'LY-105',
 'P3-a2cc07d4': 'LY-245', 'P3-8080af8d': 'AS-209', 'P3-ba2b9f13': 'LY-506',
 'P3-c317783a': 'LY-452', 'P3-dfe1667e': 'LY-036', 'P3-e135266b': 'LY-434',
 'P3-e455feea': 'LR3-002', 'P3-e8b49dac': 'LY-430', 'P3-eac7ffbe': 'LY-212',
 'P3-eb6d6f80': 'LY-206', 'P3-ec21f701': 'LY-614', 'P3-f82f8a91': 'MH-010',
 'P3-c04b6ab5': 'LY-524',
}
assert set(EXPECTED) == set(flag_anons), set(EXPECTED) ^ set(flag_anons)
for anon, cid in EXPECTED.items():
    assert plat_map[anon] == cid, (anon, plat_map.get(anon), cid)

# ---- 结局跨轮全等（70 件旗标所涉行，R95 与 R94 manifest 逐字一致） ----
cases95, cases94 = man95['cases'], man94['cases']
for cid in set(EXPECTED.values()):
    assert cases95[cid] == cases94[cid], cid

# ---- 同旨续接 67 件：在册条或承接层在案断言 ----
NEW_FLAG_CASES = {'BZ-016', 'LY-245', 'LR3-006'}
carry_cases = [cid for cid in EXPECTED.values() if cid not in NEW_FLAG_CASES]
assert len(carry_cases) == 67, len(carry_cases)
layer_case_ids = set()
for k, v in man95.items():
    if isinstance(v, dict):
        layer_case_ids |= set(v.keys())
for cid in carry_cases:
    assert any(a['case_id'] == cid for a in ann94) or cid in layer_case_ids, cid
ym070 = [a for a in ann94 if a['case_id'] == 'YM-070']
assert len(ym070) == 1 and ym070[0]['disposition'] == '未核'
for cid in NEW_FLAG_CASES:
    assert not any(a['case_id'] == cid for a in ann94), cid
    assert cid not in [k for k in man95 if k.startswith('_r') and isinstance(man95[k], dict) and cid in man95[k] and 'carryover' in k], cid

# ---- 新定案逐字断言（原卡＋结局原文） ----
inp = lambda cid: json.load(open(f'{BASE}/inputs-dev12/{cid}.json'))
assert '何命之女有子' in inp('LY-245')['context']['question']
assert '連生二子' in cases95['LY-245'] and '卯' not in cases95['LY-245']
assert inp('BZ-016')['context']['attachments']['pillars'] == inp('BZ-019')['context']['attachments']['pillars'] == '辛卯 丁酉 庚午 丙子'
assert inp('BZ-016')['source_id'] == 'ren-016' and inp('BZ-019')['source_id'] == 'xu-003'
assert '乾隆帝' in cases95['BZ-016'] and '史实同 ren-016' in cases95['BZ-019']
assert cases95['LR3-006'] == '月内升天津巡抚，后以标官劫皇销事发，请告回里。'
assert '均载原文应验段' in man95['stripped_tail']['LR3-006']
assert '仕途吉凶' in inp('LR3-006')['context']['question']
# tradition 三件（FREEZE-r95 §2）
for cid in ('LY-251', 'LY-311', 'LY-515'):
    assert inp(cid).get('tradition') == 'liuyao', cid
    pred = json.load(open(f'{BASE}/runs/round95/predictions/{cid}.json'))
    assert pred['basis'].splitlines()[0].startswith('卡面 tradition＝liuyao（逐字照錄）'), cid
pred515 = json.load(open(f'{BASE}/runs/round95/predictions/LY-515.json'))
assert '性別卡面未載' in pred515['basis']
pred251 = json.load(open(f'{BASE}/runs/round95/predictions/LY-251.json'))
assert '支名殘缺' in pred251['basis']
assert cases95['LY-251'] == '果在出空之日而愈﹐辰年占卦至午年出花而死。'
assert cases95['LY-311'] == '此人未到家，一人報曰：令郎申時去世矣'
assert '後竟生離' in cases95['LY-515']

# ---- 指令性字样基线（manifest 侧五处） ----
assert '盲测比对须注' in cases95['BZ-036']
assert '（盲测比对时以格局大富一项为主）' in cases95['BZ-042']
assert '使用时须分开统计' in cases95['BZ-105']
assert '勿以此斷' in json.dumps(man95, ensure_ascii=False)
assert '评分时该细项请按未完全复核处理' in json.dumps(man95.get('_r56_lr2016_split'), ensure_ascii=False)

# ---- 本轮新登记 6 条 ----
HM_SRC = 'divination/benchmark/phase3/runs/round95/judging/host-mapping.json'
MAN_SRC = 'divination/benchmark/phase3/runs/round95/judging/outcome-manifest.json'
FLAG_SRC = 'divination/benchmark/phase3/runs/round95/judging/judge-flags-r95.md'
new_entries = [
 {
  'anon_id': 'P3-a2cc07d4', 'case_id': 'LY-245', 'disposition': '部分成立',
  'finding': '新登记（该例首条）：回原卡——所问「占何命者有子（因有妾多，問何命之女有子）」，R95 prediction 断卯命之女可有子（指向特定命属）；逐字核 R95 manifest 结局，载积德后「連生二子」与临终嘱子，有子终局明载；但二子是否卯命女所生，结局无一字记载——特定对象断语无从核验一层属实；主线有子面非缺位。故部分成立。',
  'flag': '评审席（R95 平台面）：结局载积德后连生二子，未载是否卯命女所生，特定对象断语无从核验',
  'manifest_carry_suggestion': '平台侧新登记：自 R96 起承接本 R95 标注：按「连生二子有载、是否卯命女所生未载，特定对象断语无从核验，部分成立」登记；结局原文照录不改。',
  'relation': '新登记（该例首条）', 'registered_round': 95,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/LY-245.json',
                      f'{MAN_SRC} cases[LY-245]',
                      f'{HM_SRC}（anon 解析：P3-a2cc07d4＝LY-245）',
                      FLAG_SRC],
  'source_seats': ['R95 评审席旗标', 'R95 数据席回读原卡'],
 },
 {
  'anon_id': 'P3-2f191354', 'case_id': 'BZ-016', 'disposition': '成立',
  'finding': '新登记（该例首条）：重点核——BZ-016（source_id ren-016，《滴天髓》任铁樵批）与 BZ-019（source_id xu-003，《子平真诠评注》）逐卡对勘：同为乾隆帝弘历命造、四柱逐字全等（辛卯 丁酉 庚午 丙子）、生辰全同，仅来源书与注家不同；R95 manifest 两例结局同为乾隆帝史实（BZ-019 结局且自载「史实同 ren-016」）——同一命例分见两书、重复入池，旗标成立。去重只建议不执行：建议主持裁定保留其一为正例、另一例标注同例重复待后续轮次处置（同 LY-015／LY-320 例口径），本席不删卡、不改分。BZ-019 侧同旨已由其在册 R75 条并行登记（结局转引 ren-016 一层），本轮照在册条承接、不重复立条。',
  'flag': '评审席（R95 平台面）：与 BZ-019 结局同为乾隆帝史实，疑同一命例重复入池',
  'manifest_carry_suggestion': '只登记不入层：自 R96 起承接本 R95 标注（成立＝同例跨书重复入集，去重处置待主持裁定，不入 _r95_carryover_notes_addendum 承接层）；结局原文照录不改。',
  'relation': '新登记（该例首条；与 BZ-019 同命造重复对位）', 'registered_round': 95,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/BZ-016.json',
                      'divination/benchmark/phase3/inputs-dev12/BZ-019.json',
                      f'{MAN_SRC} cases[BZ-016]／cases[BZ-019]',
                      f'{HM_SRC}（anon 解析：P3-2f191354＝BZ-016）',
                      FLAG_SRC],
  'source_seats': ['R95 评审席旗标', 'R95 数据席全卡对勘'],
 },
 {
  'anon_id': 'P3-1d488a4d', 'case_id': 'LR3-006', 'disposition': '不成立',
  'finding': '新登记（该例首条）：回原卡——所问「仕途吉凶若何？」；逐字核 R95 manifest 结局「月内升天津巡抚，后以标官劫皇销事发，请告回里。」，升任与请告回里两段俱载，stripped_tail 亦明载荣转之职与退位之由均在原文应验段——所问仕途终局完整明载、无缺位无含混。旗标所指「与 prediction 单向凶断只部分对位」系本轮 prediction 与结局的对位程度，属评分面，不构成结局数据缺损。故不成立。',
  'flag': '评审席（R95 平台面）：结局升巡抚后请告回里两段并存，与 prediction 单向凶断只部分对位',
  'manifest_carry_suggestion': '只登记不入层：自 R96 起承接本 R95 标注（不成立＝结局两段俱载完整、所指系 prediction 对位程度属评分面，不入 _r95_carryover_notes_addendum 承接层）；结局原文照录不改。',
  'relation': '新登记（该例首条）', 'registered_round': 95,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/LR3-006.json',
                      f'{MAN_SRC} cases[LR3-006]／stripped_tail[LR3-006]',
                      f'{HM_SRC}（anon 解析：P3-1d488a4d＝LR3-006）',
                      FLAG_SRC],
  'source_seats': ['R95 评审席旗标', 'R95 数据席回读原卡'],
 },
 {
  'anon_id': 'P3-c03c903a', 'case_id': 'LY-251', 'disposition': '不成立',
  'finding': '主持裁定不成立（FREEZE-r95 §2 tradition 旗标裁定，本席逐件回读复核）：回原卡——卡面逐字载 tradition＝liuyao 在场；R95 prediction basis 首行逐字作「卡面 tradition＝liuyao（逐字照錄）」，照录无误；检查器命中系首行后段残损注记用字（妻財□土支名殘缺等盘面残损语境），非 tradition 未照录，系检查器模式误报。照历轮检查器误报判例口径：不成立、不作废、不重测。R95 manifest 结局逐字载「果在出空之日而愈﹐辰年占卦至午年出花而死。」，终局明载可核。本条只裁 tradition 面；该例本轮首入 annotations。',
  'flag': '主持裁定（FREEZE-r95 §2）：tradition 旗标候选——首行已照录，检查器命中系首行后段残损注记用字',
  'manifest_carry_suggestion': '只登记不入层：自 R96 起承接本 R95 标注（不成立＝检查器模式误报，不入 _r95_carryover_notes_addendum 承接层）；结局原文照录不改。',
  'relation': '新登记（该例首条；tradition 面）', 'registered_round': 95,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/LY-251.json',
                      'divination/benchmark/phase3/runs/round95/predictions/LY-251.json',
                      f'{MAN_SRC} cases[LY-251]',
                      f'{HM_SRC}（anon 解析：P3-c03c903a＝LY-251）',
                      'divination/benchmark/phase3/runs/round95/FREEZE-r95.md §2'],
  'source_seats': ['主持检查器＋FREEZE-r95 裁定', 'R95 数据席回读原卡'],
 },
 {
  'anon_id': 'P3-9d15657d', 'case_id': 'LY-311', 'disposition': '不成立',
  'finding': '主持裁定不成立（FREEZE-r95 §2 tradition 旗标裁定，本席逐件回读复核）：回原卡——卡面逐字载 tradition＝liuyao 在场；R95 prediction basis 首行逐字作「卡面 tradition＝liuyao（逐字照錄）」，照录无误，系检查器模式误报。照历轮检查器误报判例口径：不成立、不作废、不重测。R95 manifest 结局逐字载「此人未到家，一人報曰：令郎申時去世矣」，终局明载可核。该例残损面已在册 R91 条（部分成立），本条只裁 tradition 面、与之各旨独立、并行不悖。',
  'flag': '主持裁定（FREEZE-r95 §2）：tradition 旗标候选——首行已照录，检查器误报',
  'manifest_carry_suggestion': '只登记不入层：自 R96 起承接本 R95 标注（不成立＝检查器模式误报，不入 _r95_carryover_notes_addendum 承接层）；结局原文照录不改。',
  'relation': '同例新旨并行（在册 R91 条残损面部分成立，各旨独立、互不覆盖）', 'registered_round': 95,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/LY-311.json',
                      'divination/benchmark/phase3/runs/round95/predictions/LY-311.json',
                      f'{MAN_SRC} cases[LY-311]',
                      f'{HM_SRC}（anon 解析：P3-9d15657d＝LY-311）',
                      'divination/benchmark/phase3/runs/round95/FREEZE-r95.md §2'],
  'source_seats': ['主持检查器＋FREEZE-r95 裁定', 'R95 数据席回读原卡'],
 },
 {
  'anon_id': 'P3-693b7290', 'case_id': 'LY-515', 'disposition': '不成立',
  'finding': '主持裁定不成立（FREEZE-r95 §2 tradition 旗标裁定，本席逐件回读复核）：回原卡——卡面逐字载 tradition＝liuyao 在场；R95 prediction basis 首行逐字作「卡面 tradition＝liuyao（逐字照錄）」，照录无误；检查器命中字样「性別卡面未載」系 basis 内性别字段注记、指性别未载，非 tradition 字样，系检查器模式误报。照历轮检查器误报判例口径：不成立、不作废、不重测。R95 manifest 结局逐字载「後竟生離。……」，终局有载可核。该例 tradition 面已在册 R84 条（不成立＝检查器句式误报），本轮命中字面与 R84 不同（性别字段用字）、同属检查器误报，本条同旨并行登记、互不覆盖。',
  'flag': '主持裁定（FREEZE-r95 §2）：tradition 旗标候选——首行已照录，命中字样「性別卡面未載」指性别字段、非 tradition',
  'manifest_carry_suggestion': '只登记不入层：自 R96 起承接本 R95 标注（不成立＝检查器模式误报，不入 _r95_carryover_notes_addendum 承接层）；结局原文照录不改。',
  'relation': '同例同旨并行（在册 R84 条 tradition 面不成立，命中字面不同、互不覆盖）', 'registered_round': 95,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/LY-515.json',
                      'divination/benchmark/phase3/runs/round95/predictions/LY-515.json',
                      f'{MAN_SRC} cases[LY-515]',
                      f'{HM_SRC}（anon 解析：P3-693b7290＝LY-515）',
                      'divination/benchmark/phase3/runs/round95/FREEZE-r95.md §2'],
  'source_seats': ['主持检查器＋FREEZE-r95 裁定', 'R95 数据席回读原卡'],
 },
]

CARRY67 = ['LY-231', 'LY-433', 'LY-104', 'AS-014', 'LY-504', 'LY-426', 'LY-011', 'LY-320',
           'BZ-105', 'BQ-025', 'BQ-021', 'YY-022', 'LY-441', 'LY-513', 'YM-059', 'LY-255',
           'BZ-104', 'YY2-004', 'LY-216', 'LR2-022', 'LY-103', 'LY-627', 'BZ-019', 'BZ-037',
           'YY-023', 'LY-528', 'YM-068', 'LY-623', 'LY-510', 'LY-425', 'YM-030', 'LY-533',
           'LY-329', 'LY-023', 'LY-508', 'LY-220', 'OC-029', 'LR3-101', 'YM-070', 'LR2-016',
           'LR2-023', 'LR3-112', 'LY-436', 'LY-437', 'BQ-001', 'LY-629', 'LY-222', 'LY-458',
           'LY-531', 'AS-015', 'LY-205', 'AS-004', 'LR2-024', 'LY-028', 'LY-105', 'AS-209',
           'LY-506', 'LY-452', 'LY-036', 'LY-434', 'LR3-002', 'LY-430', 'LY-212', 'LY-206',
           'LY-614', 'MH-010', 'LY-524']
assert sorted(CARRY67) == sorted(carry_cases), (sorted(set(CARRY67) ^ set(carry_cases)))

special_new = [
 {'item': '（R95）特别核查102：评审席旗标七十件与 tradition 旗标三件定案汇总',
  'conclusion': '平台评审旗标 70 件（唯一 anon 70，block1 26／block2 17／block3 16／block4 11）逐件经 host-mapping 对位 case_id、回原卡与 R95 manifest 结局原文（与 R94 manifest 逐字全等 70/70）定案：同旨续接 67 件不重复立条（照在册条或承接层既有登记承接、档位不变；其中 YM-070 照在册未核条待核维持、AS-014 追回程度未载旨与 MH-010 爻辞应验面旨与 BZ-037 未执政偏差旨与 LY-103 书内自述旨均在旧册／承接层在案）；新登记 3 件——BZ-016 成立（该例首条，同例跨书重复入集，只登记不入层）、LY-245 部分成立（该例首条，入 _r95 承接层候选）、LR3-006 不成立（该例首条，结局完整、所指属评分面，只入册不入层）。另 FREEZE-r95 §2 tradition 旗标 3 件（LY-251／LY-311／LY-515）主持裁定检查器误报不成立，按 r93 体例新登记 3 条入册、只登记不入层（LY-311 与在册 R91 残损面条并行、LY-515 与在册 R84 tradition 条同旨并行）。本轮新登记合计 6 条。',
  'evidence': 'runs/round95/judging/judge-flags-r95.md；runs/round95/judging/host-mapping.json；runs/round95/judging/outcome-manifest.json cases（70 例）；runs/round94/judging/outcome-manifest.json cases（跨轮全等对勘）；runs/round95/FREEZE-r95.md §2；data/case-annotations-r94.json 在册条与 R95 manifest 承接层。',
  'scope_note': '只标注、不改任何分数与金标；续接件照在册条承接、原文不改；不成立件只入 annotations 册、不入 manifest 承接层。'},
 {'item': '（R95）特别核查103：平台三项全立与第八节执行面监测计数转录',
  'conclusion': '平台定稿（analyze-output）：(a) 全集配对差 −1.107 ≥ −1.371 立、(b) 四护栏全过、(c) 六爻 dev8 单轮 −1.795 ≥ −1.93 立、熔断未触发——三项全立，全立计 40→41。第八节监测（FREEZE-r95 §3，只转录、不判读）：平台面全集 487 件节名明引 387（79.5%）、功量核标目 443（91.0%）、主线认定行 420（86.2%）；六爻 325 件明引 264（81.2%）、功量核标目 324（99.7%）、主线认定行 265（81.5%）；六壬 30 件三项均 30（100%）；其余 132 件明引 93（70.5%）、标目 89（67.4%）、主线 125（94.7%）。对照：明引率 R93 98.6%→R94 94.5%→R95 79.5%，功量核标目 R94 97.1%→R95 91.0%，形态只登记、不作因果断言。评审首派作废事故：首派 8 席因主持派单附加条收窄定本回读路径（R76 型）全批作废、移存 judging/voided-nullpacket-r95/，重派 8 席定稿，平台定稿以重派分数为准。',
  'evidence': 'runs/round95/analyze-output.txt；runs/round95/FREEZE-r95.md §3；runs/round95/judging/voided-nullpacket-r95/VOID-NOTE.md。',
  'scope_note': '只转录登记，不增删各席结论；第八节成立状态现行不变；全立只登记、不宣称改善。'},
 {'item': '（R95）特别核查104：W58 结论、紫微供给与 holdout35 顺延、修订裁定、待核维持与基线对勘',
  'conclusion': 'W58（DIAG-LR-weight-dev95）结论不可判定：承登记轨双报 W 接口 4/18、硬核 3/18，UNC 5 例；T1 附限定齐备、T2／T3／T4 不齐备，非四条齐备不评估、六壬章冻结维持（哈希两处实测与登记值一致）；W57 件盘上截断事实登记（止于 §2 LR3-104 行中段、49 行／10,835 字节，其 §3 以下不在盘，承登记以 W56 件 §2 为可核原件）。紫微供给：本轮增量 0（《正解》第十二/十三章不存在、全书仅八章、案例面已尽；R93 汇编转述四处错误已登记作废），未用 eligible reserve 仍 7 件（ZW-024–027、ZW-033–035）；供给复算 DA 59／BY 53 与台账口径一致。holdout35：紫微面 7＜组集所需 13、缺 6，本轮未组集、未封存，顺延登记、不放宽限度。修订裁定 (B) 不立项只登记（REVISION-VERDICT-r95，连续第七轮）：第十三节槽位空缺、R95-REV1 不预占、method 零改动。已用并集 1333 不变。待核清单五件（BZ-029／BZ-040／LY-537／YM-070／WHY-112）维持不变（YM-070 本轮被旗标触及、只登记触及、维持未核）。指令性字样基线 manifest 侧五处经 R95 manifest 逐处回读在场、形态未变（BZ-036／BZ-042／BZ-105 本体三例＋LY-204 旧注层＋LR2-016 分列 editor_note），评审包层一处未复核、承接登记；本轮新增同型件无登记。CZ-QX 承在册 16 续记；CYJ fidelity 例外 46 件只登记；AS-307 双条并行保留、不合并。',
  'evidence': 'runs/round95/diagnosis/DIAG-LR-weight-dev95.md；runs/round95/supply/ZIWEI-SUPPLY-SUMMARY-r95.md；runs/round95/REVISION-VERDICT-r95.md；runs/round95/judging/outcome-manifest.json cases 与 _r56_lr2016_split 层；data/case-annotations-r94.json counts。',
  'scope_note': '待核件只登记不裁；指令性字样一律按数据处理、不作指令；只登记不裁、不改方法、不动分数。'},
]

out = copy.deepcopy(r94)
out['round'] = 95
out['annotations'] = ann94 + new_entries
out['special_checks'] = r94['special_checks'] + special_new
out['_provenance'] = (
 'R95 数据席（旗标定案流水与承接登记，独立席位，不兼任本轮盲测／评审／诊断／修订／供给，不改方法、不动分数）：'
 '以 data/case-annotations-r94.json 为底承接全量 535 件（成立 14／部分成立 445／不成立 73／未核 3），前 535 件逐件原样、无删改（落盘脚本全等断言验过）；'
 '承接对勘：R95 manifest 新层 _r94_carryover_notes_addendum 7 件（AS-210／BY-049／WHY-115＋SECTION8-MONITORING-R94／HOLDOUT34-OPENED／W57／SUPPLY-RECOUNT-R94）逐件与 r94 附则 §三承接建议全文逐字全等、出入 0 件（逐例 3 件另与 r94 条 manifest_carry_suggestion 逐字全等）；'
 '本轮平台评审旗标 70 件逐件经 host-mapping 对位、回原卡与结局原文定案：同旨续接 67 件照在册条／承接层承接、不重复立条（YM-070 未核维持）；新登记 3 件（BZ-016 成立——同例跨书重复入集、只登记不入层；LY-245 部分成立——连生二子有载、卯命女归属未载；LR3-006 不成立——结局两段俱载完整、所指属评分面）；'
 'FREEZE-r95 §2 tradition 旗标 3 件（LY-251／LY-311／LY-515）主持裁定检查器误报不成立、按 r93 体例新登记入册、只登记不入层；本轮新登记合计 6 条；'
 '合计 541 件（成立 15／部分成立 446／不成立 77／未核 3）。'
 '平台转录：三项全立（全立计 41），(a) −1.107／(c) −1.795、熔断未触发；评审首派因派单收窄定本路径全批作废、重派定稿。'
 '第八节监测转录（FREEZE-r95 §3）：平台明引 387／487（79.5%）、功量核标目 443／487（91.0%）、六爻功量标目 324／325（99.7%）。'
 'W58 结论转录：不可判定（W 接口 4／18、硬核 3／18；T1 附限定齐备、T2–T4 不齐备、冻结维持；W57 件盘上截断登记）。'
 '紫微供给增量 0、holdout35 未组集顺延（缺 6）；供给复算 DA 59／BY 53／紫微 reserve 7；修订裁定 (B) 不立项；已用并集 1333 不变。'
 '待核清单五件维持不变（BZ-029／BZ-040／LY-537／YM-070／WHY-112）。指令性字样基线 manifest 侧五处在场、形态未变；CZ-QX 维持 16；CYJ fidelity 例外 46 件只登记；AS-307 双条并行保留。'
 '体例注明：不成立件处置承 r93 盘上体例——不成立条入 annotations 册、只不入 manifest 承接层；成立之同例重复件（BZ-016）承 LY-015／LY-320 例只登记不入层。'
)
out['counts'] = {
 'base_file': 'data/case-annotations-r94.json', 'base_cases_total': 535,
 'base_verdicts': {'成立': 14, '部分成立': 445, '不成立': 73, '未核': 3},
 'carryover_check_r94_addendum': {'platform_layer': '_r94_carryover_notes_addendum', 'platform_items': 7,
   'platform_result': '逐件与 r94 附则 §三承接建议全文逐字全等，落实 7／出入 0（层实在 runs/round95/judging/outcome-manifest.json；逐例 3 件另与 r94 条 manifest_carry_suggestion 逐字全等）'},
 'new_registrations_r95': 6,
 'new_cases_r95': {'部分成立_platform': ['LY-245'], '成立_platform': ['BZ-016'],
                   '不成立_platform': ['LR3-006'], '不成立_tradition': ['LY-251', 'LY-311', 'LY-515']},
 'r95_judge_flags': {'total': 70, '同旨续接_不重复立条': CARRY67,
                     '新登记': ['BZ-016', 'LY-245', 'LR3-006'], '新登记不成立': ['LR3-006']},
 'r95_tradition_rulings': {'total': 3, '不成立': ['LY-251', 'LY-311', 'LY-515'],
   'source': 'FREEZE-r95 §2 主持裁定：3 件均首行已照录、检查器误报，不作废不重测；按 r93 体例只入 annotations、不入承接层'},
 'platform_r95': {'a_pair_diff': -1.107, 'b_guardrails': '四护栏全过', 'c_single': -1.795,
   'fuse_triggered': False, 'all_stand': True, 'full_stand_count': 41},
 'judging_void_r95': '首派 8 席因主持派单附加条收窄定本回读路径（R76 型）全批作废、移存 judging/voided-nullpacket-r95/；重派 8 席定稿，平台定稿以重派分数为准',
 'section8_monitoring_r95': {
   'source': 'FREEZE-r95 §3（只监测、不判读）',
   'platform': {'n': 487, '节名明引': 387, '节名明引率': '79.5%', '功量核标目': 443, '功量核标目率': '91.0%', '主线认定行': 420,
                'liuyao': {'n': 325, '节名明引': 264, '功量核标目': 324, '功量核标目率': '99.7%', '主线认定行': 265},
                'liuren': {'n': 30, '节名明引': 30, '功量核标目': 30, '主线认定行': 30},
                'other': {'n': 132, '节名明引': 93, '功量核标目': 89, '主线认定行': 125}}},
 'holdout35': {'sealed': False, 'status': '未组集顺延：紫微面 7＜组集所需 13、缺 6，不放宽限度、不以他面充数'},
 'ziwei_supply_r95': {'increment': 0, 'reserve': 7, 'note': '《正解》第十二/十三章不存在、全书仅八章、案例面已尽'},
 'supply_recount_r95': {'DA': 59, 'BY': 53, 'ziwei_reserve': 7},
 'w58_conclusion': '不可判定（承登记轨：W 接口 4／18、硬核 3／18、UNC 5；T1 附限定齐备、T2／T3／T4 不齐备；六壬章冻结维持；W57 件盘上截断——止于 §2 LR3-104 行中段、49 行／10,835 字节）',
 'revision_verdict_r95': '(B) 不立项只登记（连续第七轮；第十三节槽位空缺、R95-REV1 不预占、method 零改动、第八节维持现行）',
 'instructional_baseline_six': 'manifest 侧五处（BZ-036／BZ-042／BZ-105 cases 本体＋LY-204 旧注层＋LR2-016 分列 editor_note）逐处在场、形态未变；评审包层一处未复核、承接登记；本轮新增同型件无登记',
 'czqx_same_tier_count': 16,
 'as307_double_entry': 'R80 部分成立条与 R85 不成立条并行保留、不合并；本轮无 AS-307 新旗标、不立第三条',
 'pending_five': 'BZ-029／BZ-040／LY-537／YM-070／WHY-112 五件维持不变（YM-070 本轮被旗标触及、只登记触及、无新证据）',
 'used_union': 1333,
 'cases_total': 541,
 'verdicts': {'成立': 15, '部分成立': 446, '不成立': 77, '未核': 3},
}

# ---- 落盘断言 ----
assert out['annotations'][:535] == ann94
assert len(out['annotations']) == 541 == 535 + 6
assert Counter(a['disposition'] for a in out['annotations']) == {'成立': 15, '部分成立': 446, '不成立': 77, '未核': 3}
assert [a['case_id'] for a in out['annotations'][535:]] == ['LY-245', 'BZ-016', 'LR3-006', 'LY-251', 'LY-311', 'LY-515']
assert len(out['special_checks']) == 104 == 101 + 3
with open(f'{BASE}/data/case-annotations-r95.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
back = json.load(open(f'{BASE}/data/case-annotations-r95.json'))
assert back['counts']['cases_total'] == 541 and len(back['annotations']) == 541
print('OK: case-annotations-r95.json written, 541 annotations, special_checks 104')
