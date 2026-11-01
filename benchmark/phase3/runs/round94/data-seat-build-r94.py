# R94 数据席落盘脚本（只标注与承接登记；不改分数／卡面／金标）
import json, copy
from collections import Counter

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
r93 = json.load(open(f'{BASE}/data/case-annotations-r93.json'))
add93 = open(f'{BASE}/data/manifest-carryover-r93-addendum.md', encoding='utf-8').read()
man94 = json.load(open(f'{BASE}/runs/round94/judging/outcome-manifest.json'))
plat_map = json.load(open(f'{BASE}/runs/round94/judging/host-mapping.json'))
acc_map = json.load(open(f'{BASE}/runs/round94/acceptance/judging/host-mapping.json'))
po = json.load(open(f'{BASE}/runs/round94/acceptance/judging/packet-ours.json'))

# ---- 底本断言 ----
ann93 = r93['annotations']
assert len(ann93) == 532, len(ann93)
assert Counter(a['disposition'] for a in ann93) == {'成立': 14, '部分成立': 442, '不成立': 73, '未核': 3}

# ---- 映射断言 ----
exp_plat = {'P3-5f187440': 'LY-240', 'P3-3d26bec0': 'BQ-001', 'P3-a29f78f7': 'LY-023',
            'P3-a84f7062': 'LY-413', 'P3-a93e27cd': 'YY-022', 'P3-f51872c0': 'LR3-112',
            'P3-d83810d5': 'AS-015', 'P3-d94b9a1b': 'AS-210'}
for k, v in exp_plat.items():
    assert plat_map[k] == v, (k, plat_map.get(k))
assert acc_map['ours']['H34O-c4293bf5'] == 'BY-049'
assert acc_map['ours']['H34O-8b344ed4'] == 'WHY-115'

# ---- outcome 原文断言（只限旗标 10 件所涉行） ----
cases = man94['cases']
assert cases['LY-240'] == '果於辰日。'
assert cases['BQ-001'] == '求卜者当场自述：父卧疾三年，昨日鸡鸣时气尽、举家大哭，父忽惊寤自言「我死，有三尺人来迎，欲升天，闻哭声，遂坠地」。'
assert '果如言' in man94['stripped_tail']['BQ-001']
assert cases['LY-023'] == '果於八月其子驚風（其後復占子病，見 LY-024）'
assert cases['LY-413'] == '果然如是。'
assert cases['YY-022'] == '后果然。'
assert '病断（甲戌年不保）原文未载后续结局' in cases['LR3-112'] and '陈忠' in cases['LR3-112']
assert 'she died the eighth of October' in cases['AS-015']
assert 'his Friend was false' in cases['AS-210'] and 'office' not in cases['AS-210'].lower()
po_map = {r['anon_id']: r['outcome_record'] for r in po}
assert po_map['H34O-c4293bf5'] == '县考攻落，学院作主书考，名数、年分亦准。'
assert '所断皆验' in po_map['H34O-8b344ed4'] and '对话核实' in po_map['H34O-8b344ed4']

# ---- 同旨续接 7 件：在册条存在且档位如登记 ----
carry7 = {'LY-240': '部分成立', 'BQ-001': '部分成立', 'LY-023': '成立', 'LY-413': '部分成立',
          'YY-022': '部分成立', 'LR3-112': '部分成立', 'AS-015': '部分成立'}
for cid, disp in carry7.items():
    assert any(a['case_id'] == cid and a['disposition'] == disp for a in ann93), cid
for cid in ('AS-210', 'BY-049', 'WHY-115'):
    assert not any(a['case_id'] == cid for a in ann93), cid

# ---- _r93 层对勘：5 件与 r93 附则承接建议逐字全等 ----
lay = man94['_r93_carryover_notes_addendum']
assert list(lay.keys()) == ['WHY-112', 'HOLDOUT34-SEAL', 'ZIWEI-SUPPLY-BATCH3', 'SECTION8-MONITORING-R93', 'W56'], list(lay.keys())
for k, v in lay.items():
    assert v in add93, k
why = [a for a in ann93 if a['case_id'] == 'WHY-112'][0]
assert lay['WHY-112'] == why['manifest_carry_suggestion']

# ---- 指令性字样基线（manifest 侧）本轮在盘复核 ----
assert '盲测比对须注' in cases['BZ-036']
assert '（盲测比对时以格局大富一项为主）' in cases['BZ-042']
assert '使用时须分开统计' in cases['BZ-105']
assert '勿以此斷' in json.dumps(man94, ensure_ascii=False)  # LY-204 旧注层在 manifest 内
lr_note = json.dumps(man94.get('_r56_lr2016_split'), ensure_ascii=False)
assert '评分时该细项请按未完全复核处理' in lr_note

# ---- 本轮新登记 3 条 ----
new_entries = [
 {
  'anon_id': 'P3-d94b9a1b', 'case_id': 'AS-210', 'disposition': '部分成立',
  'finding': '新登记（该例首条）：回原卡——所问「If he should obtain the office or place he looked after」，setting 载求测者托一 solar man 友人谋职；逐字核 R94 manifest 结局，通篇仅载三周内揭露其友为假（面有疤痕、发色黑深，与所托之貌不合），得官成否无一字记载——主问面缺位属实；但朋友真伪一线系本问从属断面（友为谋职所托之人、其形貌与真伪在本断之内），结局所载即该断面之印证，非全然他事。故部分成立（与在册 AS-015 兼断面、LY-504 防刑狱断面口径同型；与 LY-513 主问全然无对应之成立口径有别）。',
  'flag': '评审席（R94 平台面）：outcome 仅证实「朋友为假」一线，主断（得官）未载',
  'manifest_carry_suggestion': '平台侧新登记：自 R95 起承接本 R94 标注：按「主问得官成否未载、结局仅印证所托朋友为假一线（本问从属断面），部分成立」登记；结局原文照录不改。',
  'relation': '新登记（该例首条）', 'registered_round': 94,
  'sources_checked': ['divination/benchmark/phase3/inputs-dev12/AS-210.json',
                      'divination/benchmark/phase3/runs/round94/judging/outcome-manifest.json cases[AS-210]',
                      'divination/benchmark/phase3/runs/round94/judging/host-mapping.json（anon 解析：P3-d94b9a1b＝AS-210）'],
  'source_seats': ['R94 评审席旗标', 'R94 数据席回读原卡'],
 },
 {
  'anon_id': 'H34O-c4293bf5', 'case_id': 'BY-049', 'disposition': '部分成立',
  'finding': '新登记（该例首条，验收面）：回原卡——杨姓占收考（《六壬辨疑·毕法案录》课例五十八）；逐字核验收 packet-ours 结局仅「县考攻落，学院作主书考，名数、年分亦准。」——收考终局本身明载（县考落、院考作主书考），主问面非缺位；但各细项仅以「名数、年分亦准」总括带过、未逐项分载，收考细节未全载一层属实。故部分成立。',
  'flag': '评审席（R94 验收面）：outcome 残缺（收考细节未全载）',
  'manifest_carry_suggestion': '验收面新登记：自 R95 起承接本 R94 标注：按「收考终局明载（县考攻落、院考作主书考）、细项仅总括未逐项分载，部分成立」登记；结局原文照录不改。',
  'relation': '新登记（该例首条；holdout34 验收面）', 'registered_round': 94,
  'sources_checked': ['divination/benchmark/phase3/holdout34/inputs/BY-049.json',
                      'divination/benchmark/phase3/runs/round94/acceptance/judging/packet-ours.json（H34O-c4293bf5 行 outcome_record）',
                      'divination/benchmark/phase3/runs/round94/acceptance/judging/host-mapping.json（H34O-c4293bf5＝BY-049）'],
  'source_seats': ['R94 验收评审席旗标', 'R94 数据席回读原卡'],
 },
 {
  'anon_id': 'H34O-8b344ed4', 'case_id': 'WHY-115', 'disposition': '部分成立',
  'finding': '新登记（该例首条，验收面）：回原卡——六爻讲座课上五十多岁女学员问事（综合断病，原书第九章综合例三）；逐字核验收 packet-ours 结局，为对话核实记录混合体：问答摘句（已经退休／已经于一九八九年去世）、「所断皆验」总评、本人症状自述（头晕、高血压、心慌、腿上有风窜来窜去）与括注内其母 1992–1996 逐年断语并载——混合形态与断语层嵌载俱属实；但核实内容本身在场可读，非无结局可核。故部分成立（与在册 LY-216 结果嵌于转述、LR3-101 编者说明并载口径同型）。',
  'flag': '评审席（R94 验收面）：outcome 为混合对话记录（含他人断语）',
  'manifest_carry_suggestion': '验收面新登记：自 R95 起承接本 R94 标注：按「结局为对话核实混合记录、含断语层嵌载，核实内容在场可读，部分成立」登记；结局原文照录不改。',
  'relation': '新登记（该例首条；holdout34 验收面）', 'registered_round': 94,
  'sources_checked': ['divination/benchmark/phase3/holdout34/inputs/WHY-115.json',
                      'divination/benchmark/phase3/runs/round94/acceptance/judging/packet-ours.json（H34O-8b344ed4 行 outcome_record）',
                      'divination/benchmark/phase3/runs/round94/acceptance/judging/host-mapping.json（H34O-8b344ed4＝WHY-115）'],
  'source_seats': ['R94 验收评审席旗标', 'R94 数据席回读原卡'],
 },
]

special_new = [
 {'item': '（R94）特别核查99：评审席旗标十件定案汇总（平台 8＋验收 2）',
  'conclusion': '逐件回读 outcome 原文定案：同旨续接 7 件不重复立条——LY-240（P3-5f187440，承 R75 条部分成立，总承式「果於辰日」）、BQ-001（P3-3d26bec0，承 R75 条部分成立，cases 本体仅当场自述、后断总承在 stripped_tail）、LY-023（P3-a29f78f7，双席同标，承 R75 条成立，母病未载、仅其子惊风）、LY-413（P3-a84f7062，承 R79 条部分成立，总承式「果然如是」）、YY-022（P3-a93e27cd，承 R75 条部分成立，总承式「后果然」）、LR3-112（P3-f51872c0，承 R75 条部分成立，病面结局缺位、原文自注）、AS-015（P3-d83810d5，承 R75 条部分成立，结局仅载问者本人十月八日亡、夫面未载）；新登记 3 件均部分成立——AS-210（P3-d94b9a1b，该例首条）、BY-049（H34O-c4293bf5，该例首条）、WHY-115（H34O-8b344ed4，该例首条）。本轮不成立 0 件。',
  'evidence': 'runs/round94/judging/host-mapping.json；runs/round94/judging/outcome-manifest.json cases（上列 8 例）；runs/round94/acceptance/judging/host-mapping.json；runs/round94/acceptance/judging/packet-ours.json（H34O-c4293bf5／H34O-8b344ed4 两行 outcome_record）；data/case-annotations-r93.json 在册 7 例条。',
  'scope_note': '只标注、不改任何分数与金标；续接件照在册条承接、原文不改；outcome_record 只读旗标所涉行，未读 predictions basis。'},
 {'item': '（R94）特别核查100：第八节执行面监测计数与 holdout34 开封事实转录',
  'conclusion': '第八节监测（只转录、不判读）：平台面（FREEZE-r94 §3）全集 487 件节名明引 460（94.5%）、功量核标目段 473（97.1%）、主线认定行 450（92.4%）；六爻 325 件节名明引 305、功量核标目 325／325（100%）、主线认定行 305；六壬 30 件明引 30、标目 25、主线 30；其余 132 件明引 125、标目 123、主线 115。验收面（FREEZE-h34 §2）29 件节名明引 29／29、功量核标目 29／29、主线认定行 29／29（h33 验收面明引 3.6%→100%）。holdout34 开封（FREEZE-h34 §0：R94 平台三项全立、全立计 39→40、当轮开封成立；金标 SHA-256 三读一致 530ab1250dfd…）：验收定稿（DIAG-H34）我方 3.603 vs 大师 5.397、配对差 −1.793、SE 0.314、W/T/L 2/4/23、三判据全不成立、未达标；分段：紫微 −1.083（n＝12）、DA −3.643（n＝7）、BY −1.250（n＝6）、六壬全段 −2.538（n＝13）、WHY −1.500（n＝4）。',
  'evidence': 'runs/round94/FREEZE-r94.md §3；runs/round94/acceptance/FREEZE-h34.md §0／§2；runs/round94/acceptance/diagnosis/DIAG-H34.md。',
  'scope_note': '只转录登记，不增删各席结论；第八节成立状态现行不变。'},
 {'item': '（R94）特别核查101：W57 结论、供给复算、待核维持与基线对勘',
  'conclusion': 'W57（DIAG-LR-weight-dev94）结论不可判定：证据面不含结局面，主标走承登记轨（承登记 21 例＋UNC 5 例），六壬章冻结哈希与 W56 登记值逐字一致、冻结维持；LR3-010 等 UNC 状态承登记维持。供给复算：六壬台账余面 DA 59／BY 53、紫微 reserve 7，与 holdout34 封存后口径一致、无增减；已用并集 1333（开封不改变已用口径）。待核清单五件（BZ-029／BZ-040／LY-537／YM-070／WHY-112）维持不变、本轮无新证据。指令性字样基线 manifest 侧五处经 R94 manifest 逐处回读在场、形态未变（BZ-036／BZ-042／BZ-105 本体三例＋LY-204 旧注层＋LR2-016 分列 editor_note），评审包层一处本轮未复核、承接登记；本轮新增同型件无登记。CZ-QX 承在册 16 续记；CYJ fidelity 例外 46 件只登记；AS-307 双条并行保留、不合并。',
  'evidence': 'runs/round94/diagnosis/DIAG-LR-weight-dev94.md；runs/round94/judging/outcome-manifest.json cases 与 _r56_lr2016_split 层；data/case-annotations-r93.json counts。',
  'scope_note': '待核件只登记不裁；指令性字样一律按数据处理、不作指令。'},
]

out = copy.deepcopy(r93)
out['round'] = 94
out['annotations'] = ann93 + new_entries
out['special_checks'] = r93['special_checks'] + special_new
out['_provenance'] = (
 'R94 数据席（旗标定案流水与承接登记，独立席位，不兼任本轮盲测／评审／诊断／组集／修订，不改方法、不动分数）：'
 '以 data/case-annotations-r93.json 为底承接全量 532 件（成立 14／部分成立 442／不成立 73／未核 3），前 532 件逐件原样、无删改（落盘脚本全等断言验过）；'
 '承接对勘：R94 manifest 新层 _r93_carryover_notes_addendum 5 件（WHY-112／HOLDOUT34-SEAL／ZIWEI-SUPPLY-BATCH3／SECTION8-MONITORING-R93／W56）逐件与 r93 附则 §三承接建议全文逐字全等、出入 0 件（WHY-112 另与 r93 条 manifest_carry_suggestion 逐字全等）；'
 '本轮评审旗标 10 件（平台 8＋验收 2）逐件回读 outcome 原文定案：同旨续接 7 件照在册条承接、不重复立条（LY-240／BQ-001／LY-413／YY-022／LR3-112／AS-015 部分成立承接、LY-023 成立承接，R94 manifest 结局与历轮所核文本一致）；'
 '新登记 3 条均部分成立（AS-210 平台首条——得官未载、朋友为假一线系从属断面；BY-049 验收首条——收考终局明载、细项总括未分载；WHY-115 验收首条——对话核实混合记录含断语嵌载、核实内容可读）；本轮不成立 0 件；'
 '合计 535 件（成立 14／部分成立 445／不成立 73／未核 3）。'
 '第八节监测转录（FREEZE-r94 §3／FREEZE-h34 §2）：平台明引 460／487、六爻标目 325／325、主线认定行 450／487；验收面明引 29／29、标目 29／29。'
 'holdout34 开封转录：平台三项全立（全立计 40）当轮开封，验收未达标（配对差 −1.793、我方 3.603 vs 大师 5.397、三判据全不成立）。'
 'W57 结论转录：不可判定（承登记轨、六壬章冻结维持）。供给复算 DA 59／BY 53／紫微 reserve 7 与封存后口径一致；已用并集 1333。'
 '待核清单五件维持不变（BZ-029／BZ-040／LY-537／YM-070／WHY-112）。指令性字样基线 manifest 侧五处在场、形态未变；CZ-QX 维持 16；CYJ fidelity 例外 46 件只登记；AS-307 双条并行保留。'
 '体例注明：不成立件处置承 r93 盘上体例——不成立条入 annotations 册、只不入 manifest 承接层（r93 两件 OC-019／YY2-004 即此例）；本轮不成立 0 件、无涉。'
)
out['counts'] = {
 'base_file': 'data/case-annotations-r93.json', 'base_cases_total': 532,
 'base_verdicts': {'成立': 14, '部分成立': 442, '不成立': 73, '未核': 3},
 'carryover_check_r93_addendum': {'platform_layer': '_r93_carryover_notes_addendum', 'platform_items': 5,
   'platform_result': '逐件与 r93 附则 §三承接建议全文逐字全等，落实 5／出入 0（层实在 runs/round94/judging/outcome-manifest.json；WHY-112 另与 r93 条 manifest_carry_suggestion 逐字全等）'},
 'new_registrations_r94': 3,
 'new_cases_r94': {'部分成立_platform': ['AS-210'], '部分成立_acceptance': ['BY-049', 'WHY-115']},
 'r94_judge_flags': {'total': 10, '同旨续接_不重复立条': ['LY-240', 'BQ-001', 'LY-023', 'LY-413', 'YY-022', 'LR3-112', 'AS-015'],
                     '新登记': ['AS-210', 'BY-049', 'WHY-115'], '不成立': []},
 'section8_monitoring_r94': {
   'source': 'FREEZE-r94 §3＋FREEZE-h34 §2（只监测、不判读）',
   'platform': {'n': 487, '节名明引': 460, '节名明引率': '94.5%', '功量核标目段': 473, '主线认定行': 450,
                'liuyao': {'n': 325, '节名明引': 305, '功量核标目段': 325, '主线认定行': 305},
                'liuren': {'n': 30, '节名明引': 30, '功量核标目段': 25, '主线认定行': 30},
                'other': {'n': 132, '节名明引': 125, '功量核标目段': 123, '主线认定行': 115}},
   'acceptance_h34': {'n': 29, '节名明引': 29, '功量核标目段': 29, '主线认定行': 29}},
 'holdout34_acceptance': {'opened': True, 'opening_basis': 'FREEZE-h34 §0：R94 平台三项全立、全立计 39→40',
   'pair_diff': -1.793, 'ours_mean': 3.603, 'master_mean': 5.397, 'SE': 0.314, 'WTL': '2/4/23',
   'verdict': '未达标（三判据全不成立）',
   'segments': {'紫微': -1.083, 'DA': -3.643, 'BY': -1.250, '六壬全段': -2.538, 'WHY': -1.5}},
 'w57_conclusion': '不可判定（证据面不含结局面、主标承登记轨 21 例＋UNC 5 例；六壬章冻结哈希与 W56 登记值一致、冻结维持）',
 'supply_recount_r94': {'DA': 59, 'BY': 53, 'ziwei_reserve': 7},
 'instructional_baseline_six': 'manifest 侧五处（BZ-036／BZ-042／BZ-105 cases 本体＋LY-204 旧注层＋LR2-016 分列 editor_note）逐处在场、形态未变；评审包层一处未复核、承接登记；本轮新增同型件无登记',
 'czqx_same_tier_count': 16,
 'as307_double_entry': 'R80 部分成立条与 R85 不成立条并行保留、不合并；本轮不立第三条',
 'pending_five': 'BZ-029／BZ-040／LY-537／YM-070／WHY-112 五件维持不变、本轮无新证据',
 'used_union': 1333,
 'cases_total': 535,
 'verdicts': {'成立': 14, '部分成立': 445, '不成立': 73, '未核': 3},
}

# ---- 落盘断言 ----
assert out['annotations'][:532] == ann93
assert len(out['annotations']) == 535 == 532 + 3
assert Counter(a['disposition'] for a in out['annotations']) == {'成立': 14, '部分成立': 445, '不成立': 73, '未核': 3}
assert {a['case_id'] for a in out['annotations'][532:]} == {'AS-210', 'BY-049', 'WHY-115'}
assert all(a['registered_round'] == 94 for a in out['annotations'][532:])
assert len(out['special_checks']) == 101
with open(f'{BASE}/data/case-annotations-r94.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
chk = json.load(open(f'{BASE}/data/case-annotations-r94.json'))
assert len(chk['annotations']) == 535 and chk['counts']['cases_total'] == 535
print('OK: annotations-r94 total=535 verdicts=', dict(Counter(a['disposition'] for a in chk['annotations'])), 'special_checks=', len(chk['special_checks']))
