# R96 数据席落盘脚本（只标注与承接登记；不改分数／卡面／金标）
import json, copy, re
from collections import Counter

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
r95 = json.load(open(f'{BASE}/data/case-annotations-r95.json'))
add95 = open(f'{BASE}/data/manifest-carryover-r95-addendum.md', encoding='utf-8').read()
man96 = json.load(open(f'{BASE}/runs/round96/judging/outcome-manifest.json'))
man95 = json.load(open(f'{BASE}/runs/round95/judging/outcome-manifest.json'))
plat_map = json.load(open(f'{BASE}/runs/round96/judging/host-mapping.json'))
flags_md = open(f'{BASE}/runs/round96/judging/judge-flags-r96.md', encoding='utf-8').read()
freeze96 = open(f'{BASE}/runs/round96/FREEZE-r96.md', encoding='utf-8').read()

# ---- 底本断言（承接断言以盘上 r95 件实测为准） ----
ann95 = r95['annotations']
assert len(ann95) == 541, len(ann95)
assert Counter(a['disposition'] for a in ann95) == {'成立': 15, '部分成立': 446, '不成立': 77, '未核': 3}
assert len(r95['special_checks']) == 104

# ---- 承接对勘：_r95 层 8 件与 r95 附则 §三逐字对勘 ----
lay = man96['_r95_carryover_notes_addendum']
assert list(lay.keys()) == ['LY-245', 'SECTION8-MONITORING-R95', 'PLATFORM-STAND-R95',
                            'JUDGE-VOID-RESEAT-R95', 'SUPPLY-RECOUNT-R95', 'HOLDOUT35-DEFERRED-R95',
                            'W58', 'REVISION-B-R95'], list(lay.keys())
bar = [a for a in ann95 if a['case_id'] == 'LY-245' and a.get('registered_round') == 95]
assert len(bar) == 1
assert lay['LY-245'] == bar[0]['manifest_carry_suggestion']
assert lay['LY-245'] in add95
for k in ('SECTION8-MONITORING-R95', 'PLATFORM-STAND-R95', 'JUDGE-VOID-RESEAT-R95',
          'SUPPLY-RECOUNT-R95', 'HOLDOUT35-DEFERRED-R95', 'W58', 'REVISION-B-R95'):
    assert lay[k] in add95, k
# 落实数：8／出入 0

# ---- 旗标 anon 对位（形近串号逐件复核：期望映射写死） ----
bullets = [ln.strip() for ln in flags_md.splitlines() if ln.strip().startswith('- P3-')]
assert len(bullets) == 49, len(bullets)
flag_anons = [re.search(r'P3-[0-9a-f]{8}', ln).group(0) for ln in bullets]
assert len(set(flag_anons)) == 49
EXPECTED = {
 'P3-12130b08': 'OC-012', 'P3-122d0580': 'LY-615', 'P3-1af73688': 'LY-537',
 'P3-25dfd904': 'MH-010', 'P3-2896edfd': 'LY-437', 'P3-2ea1af12': 'LY-222',
 'P3-3615aec2': 'LY-441', 'P3-00e0004a': 'AS-210', 'P3-26b68939': 'LR3-101',
 'P3-0da62314': 'LY-623', 'P3-2cece8e8': 'LY-517', 'P3-3c2dba04': 'LY-614',
 'P3-48f68998': 'YM-053', 'P3-5cf9fc33': 'LY-628', 'P3-6206e2db': 'LY-023',
 'P3-678a447b': 'LY-216', 'P3-60c362fb': 'LR3-116', 'P3-77df89d8': 'OC-023',
 'P3-7ae6e4d6': 'LY-104', 'P3-80ca3565': 'LY-513', 'P3-7d21b6da': 'LY-508',
 'P3-3f7db683': 'YY-022', 'P3-514a9e11': 'LY-528', 'P3-5672fa6a': 'LY-240',
 'P3-6f1b6289': 'LR2-023', 'P3-78bb1992': 'LY-430', 'P3-7bf8912f': 'YY-023',
 'P3-4653a2df': 'OC-025', 'P3-8334df99': 'LY-458', 'P3-91ecd560': 'BQ-001',
 'P3-9be85a73': 'LR3-112', 'P3-a57964aa': 'LY-506', 'P3-b03608f7': 'LY-220',
 'P3-b40b0394': 'AS-015', 'P3-bf13fdd0': 'LY-212', 'P3-bfbd72ef': 'YM-070',
 'P3-c0b71020': 'LY-413', 'P3-d52f914a': 'OC-029', 'P3-db4bc72e': 'LY-425',
 'P3-ddfd5708': 'LY-011', 'P3-d76cfecf': 'LY-627', 'P3-e47b0d03': 'LY-342',
 'P3-e51a9fcf': 'YM-068', 'P3-ee2ad080': 'LY-436', 'P3-f36d54df': 'LR2-022',
 'P3-f6c5f877': 'LY-426', 'P3-fb198f9e': 'LY-533', 'P3-f559a676': 'LY-007',
 'P3-ff69b2df': 'YM-030',
}
assert set(EXPECTED) == set(flag_anons), set(EXPECTED) ^ set(flag_anons)
for anon, cid in EXPECTED.items():
    assert plat_map[anon] == cid, (anon, plat_map.get(anon), cid)
# 另加件 anon 反查（FREEZE §2 OC-019 与 §4 B25 三件）
assert plat_map['P3-b44ecfd1'] == 'OC-019'
assert plat_map['P3-fd22ccdf'] == 'YY2-003'
assert plat_map['P3-de871bf3'] == 'YY2-004'
assert plat_map['P3-bfa2c1b9'] == 'YY2-005'

# ---- 结局跨轮全等（53 件所涉行，R96 与 R95 manifest 逐字一致） ----
cases96, cases95 = man96['cases'], man95['cases']
INVOLVED = set(EXPECTED.values()) | {'OC-019', 'YY2-003', 'YY2-004', 'YY2-005'}
assert len(INVOLVED) == 53, len(INVOLVED)
for cid in INVOLVED:
    assert cases96[cid] == cases95[cid], cid

# ---- 同旨续接 39 件：在册条或承接层在案断言 ----
NEW_FLAG_CASES = {'LY-615', 'MH-010', 'LY-342', 'OC-012', 'LY-104', 'LR3-116',
                  'LY-627', 'LY-007', 'OC-025', 'LY-517'}
carry_cases = [cid for cid in EXPECTED.values() if cid not in NEW_FLAG_CASES]
assert len(carry_cases) == 39, len(carry_cases)
layer_case_ids = set()
for k, v in man96.items():
    if isinstance(v, dict):
        layer_case_ids |= set(v.keys())
for cid in carry_cases:
    assert any(a['case_id'] == cid for a in ann95) or cid in layer_case_ids, cid
for cid in ('LY-537', 'YM-070'):
    bb = [a for a in ann95 if a['case_id'] == cid]
    assert len(bb) == 1 and bb[0]['disposition'] == '未核', cid
CARRY39 = ['LY-537', 'YM-070', 'LY-437', 'LY-222', 'LY-441', 'AS-210', 'LR3-101',
           'LY-623', 'LY-614', 'YM-053', 'LY-628', 'LY-023', 'LY-216', 'OC-023',
           'LY-513', 'LY-508', 'YY-022', 'LY-528', 'LY-240', 'LR2-023', 'LY-430',
           'YY-023', 'LY-458', 'BQ-001', 'LR3-112', 'LY-506', 'LY-220', 'AS-015',
           'LY-212', 'LY-413', 'OC-029', 'LY-425', 'LY-011', 'YM-068', 'LY-436',
           'LR2-022', 'LY-426', 'LY-533', 'YM-030']
assert sorted(CARRY39) == sorted(carry_cases), sorted(set(CARRY39) ^ set(carry_cases))
for cid in NEW_FLAG_CASES:
    assert cid not in layer_case_ids or True  # 新旨与旧层并行不悖，此处不断言无旧层

# ---- 新定案逐字断言（原卡＋结局原文＋当轮 prediction） ----
inp = lambda cid: json.load(open(f'{BASE}/inputs-dev12/{cid}.json'))
pred = lambda cid: json.load(open(f'{BASE}/runs/round96/predictions/{cid}.json'))
# LY-615 部分成立
assert inp('LY-615')['context']['question'] == '占出門'
assert cases96['LY-615'] == '後因病重，此人未去，女死辰日，夫應不去者，世動而逢合也，女死辰日者，卯木子孫變辰土之故也。'
assert '平安到达' in pred('LY-615')['prediction_text'] and '占者本人' in pred('LY-615')['prediction_text']
assert '女死' not in pred('LY-615')['prediction_text']
# MH-010 部分成立
assert cases96['MH-010'] == '果十日，伐樹起公榭，而匠者適字「元夫」（應九四爻辭）'
assert '遇元夫' in json.dumps(inp('MH-010'), ensure_ascii=False)
assert '相遇相合' in pred('MH-010')['prediction_text']
# LY-342 部分成立
assert inp('LY-342')['context']['question'] == '占今日有人还银否'
assert cases96['LY-342'] == '果于本日巳时还一半，乙酉日巳时还清一半者．'
assert '行序错乱' in json.dumps(inp('LY-342'), ensure_ascii=False)
# OC-012 不成立（串例误植）
assert cases96['OC-012'] == '杨秀琼1930年代为全国泳坛冠军；1937年（丁丑）与陶伯龄结婚；后移居香港、北美，晚景飘零，1982年卒于温哥华。'
assert '女死辰日' not in cases96['OC-012'] and '此人未去' not in cases96['OC-012']
assert '女死辰日' in cases96['LY-615']
# LY-104 不成立
assert '胸部有肿瘤' in cases96['LY-104']
assert '腰腹肠腑' in pred('LY-104')['prediction_text']
# LR3-116 不成立
assert cases96['LR3-116'] == '范大服，开帨视之，是牛黄二块，每块约重四分七八厘。'
assert '玉石' in pred('LR3-116')['prediction_text']
# LY-627 不成立
assert inp('LY-627')['context']['question'] == '占父近病'
assert cases96['LY-627'] == '果至其日而死，此應出旬又被沖克也．'
assert '父近病可愈' in pred('LY-627')['prediction_text']
# LY-007 不成立
assert cases96['LY-007'] == '果得遇於未日'
assert '迎之不遇' in pred('LY-007')['prediction_text'] or '不能相遇' in pred('LY-007')['prediction_text']
# OC-025 不成立
assert cases96['OC-025'] == '届期果有道者来访，坐破其椅。'
assert '预言如期而验' in pred('OC-025')['prediction_text']
# LY-517 不成立
assert cases96['LY-517'] == '後竟納之﹐名敗身喪。'
assert inp('LY-517')['context']['question'] == '占援例'
# OC-019 tradition 误报（FREEZE-r96 §2）
assert 'tradition' not in inp('OC-019') and 'system' not in inp('OC-019')
assert pred('OC-019')['basis'].splitlines()[0].startswith('tradition：卡面没有 tradition 字段')
assert 'OC-019' in freeze96 and '不成立（误报）' in freeze96
assert cases96['OC-019'] == '杨杏佛于1933年6月18日在上海中央研究院门前遇刺身亡。'
# B25 三件（FREEZE-r96 §4）
for cid in ('YY2-003', 'YY2-004', 'YY2-005'):
    assert inp(cid).get('tradition') == 'liuyao', cid
    voided = json.load(open(f'{BASE}/runs/round96/predictions/voided-b25-yy2-r96/{cid}.json'))
    assert voided['trigger'] == {'changed_main': False, 'reserve_used': False, 'disputed': False, 'reason': ''} or \
        (voided['trigger']['changed_main'] is False and voided['trigger']['reserve_used'] is False and voided['trigger']['disputed'] is False), cid
assert pred('YY2-003')['trigger']['disputed'] is True
assert pred('YY2-004')['trigger']['disputed'] is True
assert pred('YY2-005')['trigger']['changed_main'] is True
assert 'B25 派单批注事故' in freeze96

# ---- 指令性字样基线（manifest 侧五处） ----
assert '盲测比对须注' in cases96['BZ-036']
assert '（盲测比对时以格局大富一项为主）' in cases96['BZ-042']
assert '使用时须分开统计' in cases96['BZ-105']
assert '勿以此斷' in json.dumps(man96, ensure_ascii=False)
assert '评分时该细项请按未完全复核处理' in json.dumps(man96.get('_r56_lr2016_split'), ensure_ascii=False)

# ---- 本轮新登记 14 条 ----
HM_SRC = 'divination/benchmark/phase3/runs/round96/judging/host-mapping.json'
MAN_SRC = 'divination/benchmark/phase3/runs/round96/judging/outcome-manifest.json'
FLAG_SRC = 'divination/benchmark/phase3/runs/round96/judging/judge-flags-r96.md'
FRZ_SRC = 'divination/benchmark/phase3/runs/round96/FREEZE-r96.md'
new_entries = [
 {
  'anon_id': 'P3-122d0580', 'case_id': 'LY-615', 'disposition': '部分成立',
  'finding': '新登记（annotations 首条；与 manifest _r66 层解释层注记并行、各旨独立）：回原卡——所问「占出門」，subject 兼出門與嫁女；R96 prediction 以占者本人（世爻）出行平安到达立论、主坐标午日；逐字核 R96 manifest 结局「後因病重，此人未去，女死辰日，夫應不去者，世動而逢合也，女死辰日者，卯木子孫變辰土之故也。」——未去与女死事实明载可核、非缺位；但结局主体指代链（此人／夫）与占题对象未明字分载，prediction 对象立论与结局主体读法错位一层属实；女死大事 prediction 全未触及，事件面不完全对位。故部分成立。',
  'flag': '评审席（R96 平台面）：预测以占者本人出行平安到达立论，结局却载丈夫因病未去、女死辰日，预测主体与结局主体错位（Y1）',
  'manifest_carry_suggestion': '平台侧新登记：自 R97 起承接本 R96 标注：按「未去与女死事实明载、主体指代未明字分载与对象立论错位、女死面 prediction 未触及，部分成立」登记；结局原文照录不改。',
  'relation': '新登记（annotations 首条；与 _r66 层解释层注记各旨独立、并行不悖）', 'registered_round': 96,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/LY-615.json',
                      'divination/benchmark/phase3/runs/round96/predictions/LY-615.json',
                      f'{MAN_SRC} cases[LY-615]',
                      f'{HM_SRC}（anon 解析：P3-122d0580＝LY-615）',
                      FLAG_SRC],
  'source_seats': ['R96 评审席旗标', 'R96 数据席回读原卡'],
 },
 {
  'anon_id': 'P3-25dfd904', 'case_id': 'MH-010', 'disposition': '部分成立',
  'finding': '新登记（annotations 首条；与 manifest _r61 层「爻辞应验面有载、妇人坠跌面未载」旨并行、各旨独立）：回原卡——枯枝坠地占，卡面引九四爻辞「睽孤，遇元夫」；R96 prediction 以爻辞遇合立论（孤身男子与一位女子／妇人相遇相合）；逐字核 R96 manifest 结局「果十日，伐樹起公榭，而匠者適字「元夫」（應九四爻辭）」——「元夫」在结局指匠者题字、非遇合男子，同词所指不同，字面合而事不合一层属实；爻辞字面应验面有载，遇合事件面无对应记载。故部分成立。',
  'flag': '评审席（R96 平台面）：「元夫」在结局指匠者题字、在预测指遇合男子，同词所指不同，字面合而事不合（X1，所指 prediction_text）',
  'manifest_carry_suggestion': '平台侧新登记：自 R97 起承接本 R96 标注：按「『元夫』结局指匠者题字、与 prediction 遇合所指不同，字面合而事不合；爻辞字面应验有载、遇合事件面未载，部分成立」登记；结局原文照录不改。',
  'relation': '新登记（annotations 首条；与 _r61 层旧旨各旨独立、并行不悖）', 'registered_round': 96,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/MH-010.json',
                      'divination/benchmark/phase3/runs/round96/predictions/MH-010.json',
                      f'{MAN_SRC} cases[MH-010]',
                      f'{HM_SRC}（anon 解析：P3-25dfd904＝MH-010）',
                      FLAG_SRC],
  'source_seats': ['R96 评审席旗标', 'R96 数据席回读原卡'],
 },
 {
  'anon_id': 'P3-e47b0d03', 'case_id': 'LY-342', 'disposition': '部分成立',
  'finding': '新登记（同例新旨并行）：回原卡——所问「占今日有人还银否」；逐字核 R96 manifest 结局「果于本日巳时还一半，乙酉日巳时还清一半者．」——本日还一半明载；乙酉日句「还清一半者」表述含混（还清与一半并置），全额与否只能靠上下文推定，含混一层属实；还银终局非全缺。故部分成立。与在册 R91 条（卡面 chart_note 自注 OCR 行序错乱、逐爻表不录，残损面部分成立）各旨独立、并行不悖。',
  'flag': '评审席（R96 平台面）：结局还银表述含混（「乙酉日巳时还清一半者」），全额与否靠上下文推定（X4）',
  'manifest_carry_suggestion': '平台侧新登记：自 R97 起承接本 R96 标注：按「还银本日一半明载、乙酉日『还清一半者』表述含混、全额与否靠上下文推定，部分成立」登记；结局原文照录不改。',
  'relation': '同例新旨并行（在册 R91 条残损面部分成立，各旨独立、互不覆盖）', 'registered_round': 96,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/LY-342.json',
                      f'{MAN_SRC} cases[LY-342]',
                      f'{HM_SRC}（anon 解析：P3-e47b0d03＝LY-342）',
                      FLAG_SRC],
  'source_seats': ['R96 评审席旗标', 'R96 数据席回读原卡'],
 },
 {
  'anon_id': 'P3-12130b08', 'case_id': 'OC-012', 'disposition': '不成立',
  'finding': '新登记（同例新旨并行）：回原卡——所问命主（杨秀琼）成名、婚姻与一生行运；逐字核 R96 manifest 结局为杨秀琼泳坛冠军、结婚、移居与 1982 年卒于温哥华之记载，通篇无「此人未去、女死辰日」一字；旗标所引结局实为 LY-615（P3-122d0580）例结局原文（该例另有同旨旗标在册、本席已对位定案，见 LY-615 条），系评审席串例误植于本 anon——主持注记所问「两 anon 是否同例」经对位核定为不同例。本例结局数据完整、无所指缺位。故不成立。与在册 R87 条（tradition 面不成立）各旨独立、并行不悖。',
  'flag': '评审席（R96 平台面）：结局载「此人未去、女死辰日」，含预测全未触及的女儿死亡大事，事件面严重错位（X1）',
  'manifest_carry_suggestion': '只登记不入层：自 R97 起承接本 R96 标注（不成立＝旗标所引结局系 LY-615 例串例误植、本例结局无所指事实，不入 _r96_carryover_notes_addendum 承接层）；结局原文照录不改。',
  'relation': '同例新旨并行（在册 R87 条 tradition 面不成立，各旨独立、互不覆盖）', 'registered_round': 96,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/OC-012.json',
                      'divination/benchmark/phase3/inputs-dev12/LY-615.json',
                      f'{MAN_SRC} cases[OC-012]／cases[LY-615]',
                      f'{HM_SRC}（anon 解析：P3-12130b08＝OC-012、P3-122d0580＝LY-615）',
                      FLAG_SRC],
  'source_seats': ['R96 评审席旗标', 'R96 数据席全卡对勘'],
 },
 {
  'anon_id': 'P3-7ae6e4d6', 'case_id': 'LY-104', 'disposition': '不成立',
  'finding': '新登记（同例新旨并行）：回原卡——所问「自测病情」；逐字核 R96 manifest 结局「实际：女占者胸部有肿瘤，因有后顾之忧而测，后于戌日接受手术（汇编转录的实际反馈）」——病位（胸部）明载可核；R96 prediction 断病位偏腰腹肠腑一区，与明载病位不合属断语层误差／评分面，非结局数据缺位或含混。故不成立。本条只裁病位错位面；愈否终局未载面已由在册 R75 条（部分成立）登记、本条不重裁。',
  'flag': '评审席（R96 平台面）：实际病位为胸部肿瘤，与预测腰腹肠腑一区指向不合（X2，所指 claims）',
  'manifest_carry_suggestion': '只登记不入层：自 R97 起承接本 R96 标注（不成立＝结局病位明载、错位属断语层，不入 _r96_carryover_notes_addendum 承接层）；结局原文照录不改。',
  'relation': '同例新旨并行（在册 R75 条愈否未载面部分成立，各旨独立、互不覆盖）', 'registered_round': 96,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/LY-104.json',
                      'divination/benchmark/phase3/runs/round96/predictions/LY-104.json',
                      f'{MAN_SRC} cases[LY-104]',
                      f'{HM_SRC}（anon 解析：P3-7ae6e4d6＝LY-104）',
                      FLAG_SRC],
  'source_seats': ['R96 评审席旗标', 'R96 数据席回读原卡'],
 },
 {
  'anon_id': 'P3-60c362fb', 'case_id': 'LR3-116', 'disposition': '不成立',
  'finding': '新登记（同例新旨并行）：回原卡——所问袖帨中包何物（射覆）；逐字核 R96 manifest 结局「范大服，开帨视之，是牛黄二块，每块约重四分七八厘。」——实物与分量明载完整；R96 prediction 断玉石玉件类，与明载实物指向不合属断语层误差／评分面，非结局数据缺位。故不成立（承 R85 OC-023 射覆错位同型判例）。本条只裁实物错位面；卡面残损面已由在册 R81 条（部分成立）登记、本条不重裁。',
  'flag': '评审席（R96 平台面）：射覆实物为牛黄二块，与预测玉石玉件类指向不合（X2，所指 claims）',
  'manifest_carry_suggestion': '只登记不入层：自 R97 起承接本 R96 标注（不成立＝结局实物明载完整、错位属断语层，不入 _r96_carryover_notes_addendum 承接层）；结局原文照录不改。',
  'relation': '同例新旨并行（在册 R81 条残损面部分成立，各旨独立、互不覆盖）', 'registered_round': 96,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/LR3-116.json',
                      'divination/benchmark/phase3/runs/round96/predictions/LR3-116.json',
                      f'{MAN_SRC} cases[LR3-116]',
                      f'{HM_SRC}（anon 解析：P3-60c362fb＝LR3-116）',
                      FLAG_SRC],
  'source_seats': ['R96 评审席旗标', 'R96 数据席回读原卡'],
 },
 {
  'anon_id': 'P3-d76cfecf', 'case_id': 'LY-627', 'disposition': '不成立',
  'finding': '新登记（同例新旨并行）：回原卡——所问「占父近病」；R96 prediction 断父近病可愈、应期主坐标巳日；逐字核 R96 manifest 结局「果至其日而死，此應出旬又被沖克也．」——父病终局（死）与时点（其日）均明载可核；旗标所指「时点重合而事件相反」系 prediction 愈断与结局之对位，属评分面，不构成结局数据缺损。故不成立。本条只裁 timing 对位面；结局尾句应验解释层（在册 R65 新旨条部分成立）与卡面残损面（在册 R91 条部分成立）本条不重裁。',
  'flag': '评审席（R96 平台面）：父于所预测之愈期主坐标日死亡，时点重合而事件相反（X4，所指 timing）',
  'manifest_carry_suggestion': '只登记不入层：自 R97 起承接本 R96 标注（不成立＝结局终局与时点明载、所指系 prediction 对位属评分面，不入 _r96_carryover_notes_addendum 承接层）；结局原文照录不改。',
  'relation': '同例新旨并行（在册 R65 解释层条与 R91 残损面条，各旨独立、互不覆盖）', 'registered_round': 96,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/LY-627.json',
                      'divination/benchmark/phase3/runs/round96/predictions/LY-627.json',
                      f'{MAN_SRC} cases[LY-627]',
                      f'{HM_SRC}（anon 解析：P3-d76cfecf＝LY-627）',
                      FLAG_SRC],
  'source_seats': ['R96 评审席旗标', 'R96 数据席回读原卡'],
 },
 {
  'anon_id': 'P3-f559a676', 'case_id': 'LY-007', 'disposition': '不成立',
  'finding': '新登记（同例新旨并行）：回原卡——所问占父已起程、去迎可能遇否；R96 prediction 断迎之不遇、未日父自归；逐字核 R96 manifest 结局「果得遇於未日」——得遇事实与未日时点均明载可核；旗标所指「未日得遇与未日不遇断时点重合而事件相反」系 prediction 与结局之对位，属评分面，不构成结局数据缺损。故不成立。本条只裁 timing 对位面；tradition 面已由在册 R91 条（部分成立）登记、本条不重裁。',
  'flag': '评审席（R96 平台面）：未日得遇与「未日不遇」断时点重合而事件相反（X4，所指 timing）',
  'manifest_carry_suggestion': '只登记不入层：自 R97 起承接本 R96 标注（不成立＝结局得遇与时点明载、所指系 prediction 对位属评分面，不入 _r96_carryover_notes_addendum 承接层）；结局原文照录不改。',
  'relation': '同例新旨并行（在册 R91 条 tradition 面部分成立，各旨独立、互不覆盖）', 'registered_round': 96,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/LY-007.json',
                      'divination/benchmark/phase3/runs/round96/predictions/LY-007.json',
                      f'{MAN_SRC} cases[LY-007]',
                      f'{HM_SRC}（anon 解析：P3-f559a676＝LY-007）',
                      FLAG_SRC],
  'source_seats': ['R96 评审席旗标', 'R96 数据席回读原卡'],
 },
 {
  'anon_id': 'P3-4653a2df', 'case_id': 'OC-025', 'disposition': '不成立',
  'finding': '新登记（同例新旨并行）：回原卡——所问椅底预书之事是否应验；逐字核 R96 manifest 结局「届期果有道者来访，坐破其椅。」——终局明载完整；旗标所指 prediction_text 本身呈「应验后记述」形态（含「预言如期而验」字样）系 prediction 生成形态与评审计分注记，评审席已自注按文本字面与结局对核计分，非结局数据缺损。故不成立。本条只裁 prediction 形态面；卡面残损面已由在册 R87 条（部分成立）登记、本条不重裁。',
  'flag': '评审席（R96 平台面）：prediction_text 本身呈「应验后记述」形态（含「预言如期而验」字样），已按文本字面与结局对核计分（Y2 附注，所指 prediction_text）',
  'manifest_carry_suggestion': '只登记不入层：自 R97 起承接本 R96 标注（不成立＝结局明载完整、所指系 prediction 形态与计分注记，不入 _r96_carryover_notes_addendum 承接层）；结局原文照录不改。',
  'relation': '同例新旨并行（在册 R87 条残损面部分成立，各旨独立、互不覆盖）', 'registered_round': 96,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/OC-025.json',
                      'divination/benchmark/phase3/runs/round96/predictions/OC-025.json',
                      f'{MAN_SRC} cases[OC-025]',
                      f'{HM_SRC}（anon 解析：P3-4653a2df＝OC-025）',
                      FLAG_SRC],
  'source_seats': ['R96 评审席旗标', 'R96 数据席回读原卡'],
 },
 {
  'anon_id': 'P3-2cece8e8', 'case_id': 'LY-517', 'disposition': '不成立',
  'finding': '新登记（同例新旨并行）：回原卡——所问「占援例」（捐纳）入仕可否；逐字核 R96 manifest 结局「後竟納之，名敗身喪。」——「納之」在占题语境下明指纳捐成面（承在册 R85 条「成面明载、终局名敗身喪并载」定案），指代并非无从读；终局并载面已由 R85 条登记。旗标所指「納之指代不明」与在册定案不合，且结局虽简、成败两面俱载可核。故不成立。本条只裁指代面；R85 成败并存条与 R68 应期面条本条不重裁。',
  'flag': '评审席（R96 平台面）：结局「後竟納之，名敗身喪」中「納之」指代不明，只能按终局量级评分（Y1）',
  'manifest_carry_suggestion': '只登记不入层：自 R97 起承接本 R96 标注（不成立＝「納之」于占题语境明指纳捐成面、承 R85 定案，不入 _r96_carryover_notes_addendum 承接层）；结局原文照录不改。',
  'relation': '同例新旨并行（在册 R85 条成败并存部分成立，各旨独立、互不覆盖）', 'registered_round': 96,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/LY-517.json',
                      f'{MAN_SRC} cases[LY-517]',
                      f'{HM_SRC}（anon 解析：P3-2cece8e8＝LY-517）',
                      FLAG_SRC],
  'source_seats': ['R96 评审席旗标', 'R96 数据席回读原卡'],
 },
 {
  'anon_id': 'P3-b44ecfd1', 'case_id': 'OC-019', 'disposition': '不成立',
  'finding': '主持裁定不成立（FREEZE-r96 §2 tradition 旗标裁定，本席逐件回读复核）：回原卡——卡面键仅 id／subject／context／provenance／language，无 tradition／system 字段；R96 prediction basis 首行逐字作「tradition：卡面没有 tradition 字段，仅见 subject/context/provenance，据命造评注引例体裁自决用子平法；卡面 note 明载两书四柱全异、本例以卡面所载（徐乐吾书）为准」，首行明写没有该字段、与卡面实况相符；检查器命中系「卡面 tradition」字面子串与实情表述相撞，系检查器模式误报。照历轮检查器误报判例口径：不成立、不作废、不重测。R96 manifest 结局逐字载「杨杏佛于1933年6月18日在上海中央研究院门前遇刺身亡。」，终局明载可核。该例 tradition 面已在册 R84／R89／R93 三条（均不成立、命中字面各异），本轮命中字面为「卡面 tradition」子串、本条同旨并行登记、互不覆盖；两书四柱全异面已由在册 R91 条（部分成立）登记、本条不重裁。',
  'flag': '主持裁定（FREEZE-r96 §2）：tradition 旗标候选——卡面无 tradition 字段、首行已明写没有，检查器命中系「卡面 tradition」字面子串与实情表述相撞（误报）',
  'manifest_carry_suggestion': '只登记不入层：自 R97 起承接本 R96 标注（不成立＝检查器模式误报，不入 _r96_carryover_notes_addendum 承接层）；结局原文照录不改。',
  'relation': '同例同旨并行（在册 R84／R89／R93 tradition 面三条不成立，命中字面不同、互不覆盖）', 'registered_round': 96,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/OC-019.json',
                      'divination/benchmark/phase3/runs/round96/predictions/OC-019.json',
                      f'{MAN_SRC} cases[OC-019]',
                      f'{HM_SRC}（anon 解析：P3-b44ecfd1＝OC-019）',
                      f'{FRZ_SRC} §2'],
  'source_seats': ['主持检查器＋FREEZE-r96 裁定', 'R96 数据席回读原卡'],
 },
 {
  'anon_id': 'P3-fd22ccdf', 'case_id': 'YY2-003', 'disposition': '部分成立',
  'finding': 'FREEZE-r96 §4 B25 派单批注事故登记（本席承接登记）：回原卡——卡面 tradition 逐字为 liuyao 在场；原席作断按卡面以六爻法行（正确），仅 trigger 循主持误批注「本批均为非六爻例」全填 false（盘上作废件 trigger 三布尔全 false、本席逐件回读验合），trigger 登记错误一层属实；作断实质不受影响。主持处置：原件复制留痕至 predictions/voided-b25-yy2-r96／、派全新补测席全盲重测并覆盖同名件（重测件 trigger 盘上实测 disputed＝true，已并入 FREEZE §1 全集复算 changed_main＝1／reserve_used＝0／disputed＝2）。照 R76 operative 口径（登记层属实、方法实质正确）定部分成立。本条只裁 B25 事故面；该例结局年份阙如面已由在册 R85 条（部分成立）登记、本条不重裁。',
  'flag': '主持登记（FREEZE-r96 §4）：B25 派单批注事故——卡面 tradition＝liuyao，原件 trigger 循误批注全填 false，作废重测',
  'manifest_carry_suggestion': '只登记不入逐例层：自 R97 起承接本 R96 标注（部分成立＝trigger 误填一层属实、作断按卡面正确；B25 轮级事实另以轮级候选入 _r96_carryover_notes_addendum）；结局原文照录不改。',
  'relation': '同例新旨并行（在册 R85 条年份阙如面部分成立，各旨独立、互不覆盖）', 'registered_round': 96,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/YY2-003.json',
                      'divination/benchmark/phase3/runs/round96/predictions/voided-b25-yy2-r96/YY2-003.json',
                      'divination/benchmark/phase3/runs/round96/predictions/YY2-003.json',
                      f'{MAN_SRC} cases[YY2-003]',
                      f'{HM_SRC}（anon 解析：P3-fd22ccdf＝YY2-003）',
                      f'{FRZ_SRC} §4'],
  'source_seats': ['主持 FREEZE-r96 §4 事故登记', 'R96 数据席回读原卡'],
 },
 {
  'anon_id': 'P3-de871bf3', 'case_id': 'YY2-004', 'disposition': '部分成立',
  'finding': 'FREEZE-r96 §4 B25 派单批注事故登记（本席承接登记）：回原卡——卡面 tradition 逐字为 liuyao 在场；原席作断按卡面以六爻法行（正确），仅 trigger 循主持误批注「本批均为非六爻例」全填 false（盘上作废件 trigger 三布尔全 false、本席逐件回读验合），trigger 登记错误一层属实；作断实质不受影响。主持处置：原件复制留痕至 predictions/voided-b25-yy2-r96／、派全新补测席全盲重测并覆盖同名件（重测件 trigger 盘上实测 disputed＝true，已并入 FREEZE §1 全集复算）。照 R76 operative 口径（登记层属实、方法实质正确）定部分成立。本条只裁 B25 事故面；该例盘面残损面（在册 R75 条部分成立）与 tradition 面（在册 R93 条不成立）本条不重裁。',
  'flag': '主持登记（FREEZE-r96 §4）：B25 派单批注事故——卡面 tradition＝liuyao，原件 trigger 循误批注全填 false，作废重测',
  'manifest_carry_suggestion': '只登记不入逐例层：自 R97 起承接本 R96 标注（部分成立＝trigger 误填一层属实、作断按卡面正确；B25 轮级事实另以轮级候选入 _r96_carryover_notes_addendum）；结局原文照录不改。',
  'relation': '同例新旨并行（在册 R75 条残损面部分成立与 R93 条 tradition 面不成立，各旨独立、互不覆盖）', 'registered_round': 96,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/YY2-004.json',
                      'divination/benchmark/phase3/runs/round96/predictions/voided-b25-yy2-r96/YY2-004.json',
                      'divination/benchmark/phase3/runs/round96/predictions/YY2-004.json',
                      f'{MAN_SRC} cases[YY2-004]',
                      f'{HM_SRC}（anon 解析：P3-de871bf3＝YY2-004）',
                      f'{FRZ_SRC} §4'],
  'source_seats': ['主持 FREEZE-r96 §4 事故登记', 'R96 数据席回读原卡'],
 },
 {
  'anon_id': 'P3-bfa2c1b9', 'case_id': 'YY2-005', 'disposition': '部分成立',
  'finding': 'FREEZE-r96 §4 B25 派单批注事故登记（本席承接登记）：回原卡——卡面 tradition 逐字为 liuyao 在场；原席作断按卡面以六爻法行（正确），仅 trigger 循主持误批注「本批均为非六爻例」全填 false（盘上作废件 trigger 三布尔全 false、本席逐件回读验合），trigger 登记错误一层属实；作断实质不受影响。主持处置：原件复制留痕至 predictions/voided-b25-yy2-r96／、派全新补测席全盲重测并覆盖同名件（重测件 trigger 盘上实测 changed_main＝true，已并入 FREEZE §1 全集复算）。照 R76 operative 口径（登记层属实、方法实质正确）定部分成立。本条只裁 B25 事故面；该例空亡未载面已由在册 R91 条（部分成立）登记、本条不重裁。',
  'flag': '主持登记（FREEZE-r96 §4）：B25 派单批注事故——卡面 tradition＝liuyao，原件 trigger 循误批注全填 false，作废重测',
  'manifest_carry_suggestion': '只登记不入逐例层：自 R97 起承接本 R96 标注（部分成立＝trigger 误填一层属实、作断按卡面正确；B25 轮级事实另以轮级候选入 _r96_carryover_notes_addendum）；结局原文照录不改。',
  'relation': '同例新旨并行（在册 R91 条空亡未载面部分成立，各旨独立、互不覆盖）', 'registered_round': 96,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/YY2-005.json',
                      'divination/benchmark/phase3/runs/round96/predictions/voided-b25-yy2-r96/YY2-005.json',
                      'divination/benchmark/phase3/runs/round96/predictions/YY2-005.json',
                      f'{MAN_SRC} cases[YY2-005]',
                      f'{HM_SRC}（anon 解析：P3-bfa2c1b9＝YY2-005）',
                      f'{FRZ_SRC} §4'],
  'source_seats': ['主持 FREEZE-r96 §4 事故登记', 'R96 数据席回读原卡'],
 },
]

special_new = [
 {'item': '（R96）特别核查105：评审席旗标四十九件与 tradition 旗标一件、B25 事故三件定案汇总',
  'conclusion': '平台评审旗标 49 件（唯一 anon 49，block1 11／block2 17／block3 7／block4 14）逐件经 host-mapping 对位 case_id、回原卡与 R96 manifest 结局原文（与 R95 manifest 逐字全等 49/49）定案：同旨续接 39 件不重复立条（照在册条或承接层既有登记承接、档位不变；其中 LY-537／YM-070 照在册未核条待核维持）；新登记 10 件——部分成立 3 件（LY-615 主体指代未分载与对象立论错位、MH-010「元夫」所指不同字面合而事不合、LY-342「还清一半者」表述含混，均入 _r96 承接层候选）、不成立 7 件（OC-012 旗标所引结局系 LY-615 例串例误植、LY-104 病位错位属断语层、LR3-116 射覆实物错位属断语层、LY-627 与 LY-007 timing 对位属评分面、OC-025 prediction 形态属计分注记、LY-517「納之」指代承 R85 定案明指成面）。另 FREEZE-r96 §2 tradition 旗标 1 件（OC-019）主持裁定检查器误报不成立、新登记入册（与在册历轮 tradition 三条同旨并行、命中字面不同）；FREEZE-r96 §4 B25 事故 3 件（YY2-003／004／005）照 R76 operative 口径定部分成立、新登记入册（trigger 误填属实、作断按卡面正确，原件留痕作废、全盲重测覆盖）。本轮新登记合计 14 条。',
  'evidence': 'runs/round96/judging/judge-flags-r96.md；runs/round96/judging/host-mapping.json；runs/round96/judging/outcome-manifest.json cases（53 例）；runs/round95/judging/outcome-manifest.json cases（跨轮全等对勘）；runs/round96/FREEZE-r96.md §2／§4；data/case-annotations-r95.json 在册条与 R96 manifest 承接层。',
  'scope_note': '只标注、不改任何分数与金标；续接件照在册条承接、原文不改；不成立件只入 annotations 册、不入 manifest 承接层；B25 逐例条只入册、其轮级事实另以轮级候选入层。'},
 {'item': '（R96）特别核查106：第八节执行面监测计数转录',
  'conclusion': '第八节监测（FREEZE-r96 §3，只转录、不判读）：平台面全集 487 件节名明引 487（100%）、功量核标目 487（100%）、主线认定行 487（100%）；六爻 325 件三项均 325（100%）；六壬 30 件三项均 30（100%）；其余 132 件三项均 132（100%）。对照：节名明引率平台面 R93 98.6%→R94 94.5%→R95 79.5%→R96 100%，功量核标目 R95 91.0%→R96 100%，主线认定行 R95 86.2%→R96 100%；三轮降后本轮三项全满，形态只登记、不作因果断言。验收面附读待 h35 开封轮对照（h34 验收面 100%、h33 3.6%）。',
  'evidence': 'runs/round96/FREEZE-r96.md §3。',
  'scope_note': '只转录登记，不增删主持结论；第八节成立状态现行不变；全满只登记、不宣称改善。'},
 {'item': '（R96）特别核查107：holdout35 组集封存判定转录、待核维持与基线对勘',
  'conclusion': 'holdout35 组集封存判定（主持收束定版、本席只转录）：紫微累计 18（reserve 7＋本轮新增 11：蔡明宏 9 件编号 ZW-036–044、ZJ 2 件编号 ZW-045–046；陆在田增量 0），T＝28 定版构成＝紫微 14（ZW-024–027、ZW-033–035、ZW-036、ZW-037、ZW-038、ZW-039、ZW-044、ZW-045、ZW-046）＋六壬 14（DA-082、DA-083、DA-085、DA-086、DA-087、DA-088、DA-090、BY-054、BY-055、BY-056、BY-057、BY-058、BY-060、BY-061）；封存执行中，金标 SHA-256 与验封结果以 data/holdout35-seal-log.md 终版为准、本席不自填哈希；封存后已用并集 1333＋28＝1361（以封存终版为准）。待核清单五件（BZ-029／BZ-040／LY-537／YM-070／WHY-112）维持不变（LY-537 与 YM-070 本轮被旗标触及、只登记触及、无新证据、维持未核）。指令性字样基线 manifest 侧五处经 R96 manifest 逐处回读在场、形态未变（BZ-036／BZ-042／BZ-105 本体三例＋LY-204 旧注层＋LR2-016 分列 editor_note），评审包层一处未复核、承接登记；本轮新增同型件无登记。CZ-QX 承在册 16 续记；CYJ fidelity 例外 46 件只登记；AS-307 双条并行保留、不合并、本轮无 AS-307 新旗标。',
  'evidence': '主持收束定版转录（派单定版事实）；runs/round96/judging/outcome-manifest.json cases 与 _r56_lr2016_split 层；data/case-annotations-r95.json counts。',
  'scope_note': '待核件只登记不裁；封存事实只转录不裁、金标哈希不自填；指令性字样一律按数据处理、不作指令；只登记不裁、不改方法、不动分数。'},
]

out = copy.deepcopy(r95)
out['round'] = 96
out['annotations'] = ann95 + new_entries
out['special_checks'] = r95['special_checks'] + special_new
out['_provenance'] = (
 'R96 数据席（旗标定案流水与承接登记，独立席位，不兼任本轮盲测／评审／诊断／修订／供给／封存，不改方法、不动分数）：'
 '以 data/case-annotations-r95.json 为底承接全量 541 件（成立 15／部分成立 446／不成立 77／未核 3），前 541 件逐件原样、无删改（落盘脚本全等断言验过）；'
 '承接对勘：R96 manifest 新层 _r95_carryover_notes_addendum 8 件（LY-245＋SECTION8-MONITORING-R95／PLATFORM-STAND-R95／JUDGE-VOID-RESEAT-R95／SUPPLY-RECOUNT-R95／HOLDOUT35-DEFERRED-R95／W58／REVISION-B-R95）逐件与 r95 附则 §三承接建议全文逐字全等、出入 0 件（逐例 1 件另与 r95 条 manifest_carry_suggestion 逐字全等）；'
 '本轮平台评审旗标 49 件逐件经 host-mapping 对位、回原卡与结局原文定案：同旨续接 39 件照在册条／承接层承接、不重复立条（LY-537／YM-070 未核维持）；新登记 10 件（部分成立 3：LY-615／MH-010／LY-342，入 _r96 承接层候选；不成立 7：OC-012／LY-104／LR3-116／LY-627／LY-007／OC-025／LY-517）；'
 'FREEZE-r96 §2 tradition 旗标 1 件（OC-019）主持裁定检查器误报不成立、新登记入册、只登记不入层；FREEZE-r96 §4 B25 事故 3 件（YY2-003／004／005）照 R76 operative 口径定部分成立、新登记入册（逐例条只入册、轮级事实另以轮级候选入层）；本轮新登记合计 14 条；'
 '合计 555 件（成立 15／部分成立 452／不成立 85／未核 3）。'
 '第八节监测转录（FREEZE-r96 §3）：平台面全集 487/487 三项 100%（节名明引／功量核标目／主线认定行），轨迹 R93 98.6%→R94 94.5%→R95 79.5%→R96 100%。'
 'holdout35 转录（主持收束定版）：紫微累计 18（reserve 7＋新增 11），T＝28 定版构成紫微 14＋六壬 14，封存执行中、金标哈希与验封以 data/holdout35-seal-log.md 终版为准；封存后已用并集 1361。'
 '待核清单五件维持不变（BZ-029／BZ-040／LY-537／YM-070／WHY-112）。指令性字样基线 manifest 侧五处在场、形态未变；CZ-QX 维持 16；CYJ fidelity 例外 46 件只登记；AS-307 双条并行保留。'
 '体例注明：不成立件处置承 r93 盘上体例——不成立条入 annotations 册、只不入 manifest 承接层。'
)
out['counts'] = {
 'base_file': 'data/case-annotations-r95.json', 'base_cases_total': 541,
 'base_verdicts': {'成立': 15, '部分成立': 446, '不成立': 77, '未核': 3},
 'carryover_check_r95_addendum': {'platform_layer': '_r95_carryover_notes_addendum', 'platform_items': 8,
   'platform_result': '逐件与 r95 附则 §三承接建议全文逐字全等，落实 8／出入 0（层实在 runs/round96/judging/outcome-manifest.json；逐例 1 件 LY-245 另与 r95 条 manifest_carry_suggestion 逐字全等）'},
 'new_registrations_r96': 14,
 'new_cases_r96': {'部分成立_platform': ['LY-615', 'MH-010', 'LY-342'],
                   '不成立_platform': ['OC-012', 'LY-104', 'LR3-116', 'LY-627', 'LY-007', 'OC-025', 'LY-517'],
                   '不成立_tradition': ['OC-019'],
                   '部分成立_b25': ['YY2-003', 'YY2-004', 'YY2-005']},
 'r96_judge_flags': {'total': 49, '同旨续接_不重复立条': CARRY39,
                     '新登记': ['LY-615', 'MH-010', 'LY-342', 'OC-012', 'LY-104', 'LR3-116', 'LY-627', 'LY-007', 'OC-025', 'LY-517'],
                     '新登记部分成立': ['LY-615', 'MH-010', 'LY-342'],
                     '新登记不成立': ['OC-012', 'LY-104', 'LR3-116', 'LY-627', 'LY-007', 'OC-025', 'LY-517']},
 'r96_tradition_rulings': {'total': 1, '不成立': ['OC-019'],
   'source': 'FREEZE-r96 §2 主持裁定：卡面无 tradition 字段、首行已明写没有，检查器命中系字面子串相撞误报，不作废不重测；按体例只入 annotations、不入承接层'},
 'r96_b25_accident': {'total': 3, '部分成立': ['YY2-003', 'YY2-004', 'YY2-005'],
   'source': 'FREEZE-r96 §4 主持登记：B25 派单误批注「本批均为非六爻例」，三件卡面 tradition＝liuyao、原席作断正确、仅 trigger 全填 false；原件留痕 predictions/voided-b25-yy2-r96/ 作废、全盲重测覆盖（重测 trigger 复算 changed_main＝1／reserve_used＝0／disputed＝2）；照 R76 operative 口径定部分成立，逐例条只入册、轮级事实另以轮级候选入 _r96 层'},
 'section8_monitoring_r96': {
   'source': 'FREEZE-r96 §3（只监测、不判读）',
   'platform': {'n': 487, '节名明引': 487, '节名明引率': '100%', '功量核标目': 487, '功量核标目率': '100%', '主线认定行': 487, '主线认定行率': '100%',
                'liuyao': {'n': 325, '节名明引': 325, '功量核标目': 325, '主线认定行': 325},
                'liuren': {'n': 30, '节名明引': 30, '功量核标目': 30, '主线认定行': 30},
                'other': {'n': 132, '节名明引': 132, '功量核标目': 132, '主线认定行': 132}},
   'trajectory': '节名明引率 R93 98.6%→R94 94.5%→R95 79.5%→R96 100%'},
 'holdout35': {'sealed': '封存执行中', 'T': 28,
   'composition': '紫微 14（ZW-024–027、ZW-033–035、ZW-036、ZW-037、ZW-038、ZW-039、ZW-044、ZW-045、ZW-046）＋六壬 14（DA-082、DA-083、DA-085、DA-086、DA-087、DA-088、DA-090、BY-054、BY-055、BY-056、BY-057、BY-058、BY-060、BY-061）',
   'ziwei_cumulative': 18, 'ziwei_increment_r96': 11,
   'gold_sha_and_verification': '以 data/holdout35-seal-log.md 终版为准（本席不自填哈希）'},
 'instructional_baseline_six': 'manifest 侧五处（BZ-036／BZ-042／BZ-105 cases 本体＋LY-204 旧注层＋LR2-016 分列 editor_note）逐处在场、形态未变；评审包层一处未复核、承接登记；本轮新增同型件无登记',
 'czqx_same_tier_count': 16,
 'as307_double_entry': 'R80 部分成立条与 R85 不成立条并行保留、不合并；本轮无 AS-307 新旗标、不立第三条',
 'pending_five': 'BZ-029／BZ-040／LY-537／YM-070／WHY-112 五件维持不变（LY-537／YM-070 本轮被旗标触及、只登记触及、无新证据）',
 'used_union': '封存后 1361（1333＋28，以封存终版为准）',
 'cases_total': 555,
 'verdicts': {'成立': 15, '部分成立': 452, '不成立': 85, '未核': 3},
}

# ---- 落盘断言 ----
assert out['annotations'][:541] == ann95
assert len(out['annotations']) == 555 == 541 + 14
assert Counter(a['disposition'] for a in out['annotations']) == {'成立': 15, '部分成立': 452, '不成立': 85, '未核': 3}
assert [a['case_id'] for a in out['annotations'][541:]] == ['LY-615', 'MH-010', 'LY-342', 'OC-012', 'LY-104', 'LR3-116', 'LY-627', 'LY-007', 'OC-025', 'LY-517', 'OC-019', 'YY2-003', 'YY2-004', 'YY2-005']
assert len(out['special_checks']) == 107 == 104 + 3
with open(f'{BASE}/data/case-annotations-r96.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
back = json.load(open(f'{BASE}/data/case-annotations-r96.json'))
assert back['counts']['cases_total'] == 555 and len(back['annotations']) == 555
print('OK: case-annotations-r96.json written, 555 annotations, special_checks 107')
