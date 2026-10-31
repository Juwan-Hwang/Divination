# -*- coding: utf-8 -*-
"""R88 数据席落盘脚本：_r87 层 43 件对勘 + DIAG-H31 §5 F1-F6 定案 +
case-annotations-r88.json + manifest-carryover-r88-addendum.md。
只读底本，产出仅两件（data/ 下）。逐件断言，任一不过即中止不落盘。"""
import json, hashlib, pathlib, collections, copy

BASE = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
def load(p): return json.load(open(p, encoding='utf-8'))
def sha_file(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
def cases_sha(cases): return hashlib.sha256(json.dumps(cases, ensure_ascii=False, sort_keys=True).encode()).hexdigest()

ann87 = load(BASE/'data/case-annotations-r87.json')
man88 = load(BASE/'runs/round88/judging/outcome-manifest.json')
man87 = load(BASE/'runs/round87/judging/outcome-manifest.json')
assert ann87['round'] == 87 and len(ann87['annotations']) == 300
assert collections.Counter(a['disposition'] for a in ann87['annotations']) == {'成立':14,'部分成立':235,'不成立':49,'未核':2}
MAN88_SHA = sha_file(BASE/'runs/round88/judging/outcome-manifest.json')
assert cases_sha(man88['cases']) == cases_sha(man87['cases']) == '00f362bd8e4b55ceff31502cb5f7e8239855b1f806a7b1495284af80186a31ad'
assert len(man88['cases']) == 487

# ---------- 工序一甲：_r87 层 43 件逐件对勘 ----------
ids43 = ann87['counts']['r87_layer_partial_upheld_platform']
assert len(ids43) == 43
layer = man88['_r87_carryover_notes_addendum']
assert set(layer.keys()) == set(ids43) and len(layer) == 43
by87 = {}
for a in ann87['annotations']:
    if a.get('registered_round') == 87 and a['disposition'] == '部分成立':
        by87.setdefault(a['case_id'], []).append(a)
rows43 = []
for cid in ids43:
    ent = by87[cid]; assert len(ent) == 1, cid
    e = ent[0]
    assert layer[cid] == e['manifest_carry_suggestion'], cid  # 层文本逐字落实
    out = man88['cases'].get(cid)
    assert isinstance(out, str) and len(out) > 0, cid        # dev 结局原文在场
    rows43.append((cid, e['anon_id'], out))
assert len(rows43) == 43  # 落实 43/43，维持 0，订正 0

# ---------- 工序一乙：验收面 5 件（CYJ-006..010）不入层登记 ----------
cyj5 = ['CYJ-006','CYJ-007','CYJ-008','CYJ-009','CYJ-010']
for cid in cyj5:
    assert cid not in layer and cid not in man88['cases'], cid
    ent = [a for a in ann87['annotations'] if a['case_id']==cid and a.get('registered_round')==87]
    assert len(ent)==1 and ent[0]['disposition']=='部分成立', cid
assert 'CYJ-006, CYJ-007, CYJ-008, CYJ-009, CYJ-010' in man88['_r88_manifest_note']
assert 'does not enter the dev manifest layer' in man88['_r88_manifest_note']
# _r82 层 3 件结案续记
assert list(man88['_r82_carryover_notes_addendum'].keys()) == ['LY-406','LY-446','LY-524'] or set(man88['_r82_carryover_notes_addendum'].keys())=={'LY-406','LY-446','LY-524'}

# ---------- 基线六处（R88 盘上逐处回读） ----------
for cid, needle in [('BZ-036','盲测比对须注'),('BZ-042','（盲测比对时以格局大富一项为主）'),
                    ('BZ-105','使用时须分开统计'),('LY-204','勿以此斷')]:
    assert needle in man88['cases'][cid], cid
split_note = man88['_r56_lr2016_split']['editor_note']
assert man88['_r56_lr2016_split']['case_id'] == 'LR2-016'
assert split_note == '原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。'
hm88 = load(BASE/'runs/round88/judging/host-mapping.json')
lr_anon = [k for k,v in hm88.items() if v=='LR2-016'][0]
assert lr_anon == 'P3-678389ac'
packet_hits = []
for pn in ['packet1.json','packet2.json','packet3.json','packet4.json','packetA.json','packetB.json']:
    pkt = load(BASE/'runs/round88/judging'/pn)
    for it in pkt:
        if isinstance(it, dict) and it.get('anon_id')==lr_anon and 'editor_note' in it:
            assert it['editor_note'] == split_note, pn
            packet_hits.append(pn)
assert packet_hits == ['packet2.json','packetA.json'], packet_hits

# ---------- 工序二：DIAG-H31 §5 F1-F6 逐件回读定案 ----------
gold = {}
for line in open(BASE/'holdout31/test_gold.jsonl', encoding='utf-8'):
    if line.strip():
        o = json.loads(line); gold[o['id']] = o
hmacc = load(BASE/'runs/round88/acceptance/judging/host-mapping.json')
ours_inv = {v:k for k,v in hmacc['ours'].items()}
def card(cid): return load(BASE/f'holdout31/inputs/{cid}.json')
def pred(cid): return load(BASE/'runs/round88/acceptance/predictions'/f'{cid}.json')

# F1 WHY-043
c = card('WHY-043'); p = pred('WHY-043'); g = gold['WHY-043']
assert 'hidden' not in json.dumps(c['anchors']) and '伏' not in json.dumps(c['anchors'])
assert '子孙' not in ''.join(c['anchors']['chart_lines_top_to_bottom'])
assert '用神子孙不上卦，震宫首卦震为雷四爻子孙午火，同位伏四爻财丑下' in p['basis']
assert '子孫子水伏在飛神父母亥水下，飛來生伏是吉兆，是懷孕的信息' in g['master_prediction']
assert '到医院检查发现怀孕' in g['outcome_record'] and '做了流产手术' in g['outcome_record']
# F2 DA-051
c = card('DA-051'); p = pred('DA-051'); g = gold['DA-051']
assert '案051' in c['setting'] and '案051' in c['provenance']
assert 'DA-M13载案051同式卯六、辰五、巳四三支连加得十五' in p['basis']
assert '卯' in c['anchors']['四课'] and '辰' in c['anchors']['三传'] and '巳' in c['anchors']['三传']
assert '一气十五年' in g['master_prediction']
# F3 DA-048/051/055
for cid in ['DA-048','DA-051','DA-055']:
    cc = card(cid); pp = pred(cid)
    assert cc['anchors']['课名'] == '底本未载', cid
    assert cc['anchors']['天盘'] and cc['anchors']['四课'] and cc['anchors']['三传'], cid
    assert '课名底本未载' in pp['basis'], cid
    assert gold[cid]['outcome_record'], cid
assert '课名底本未载（卡面如实记未载，不臆补）' in pred('DA-048')['basis']
# F4 WHY-068/069
assert card('WHY-068')['anchors']['asked_at'] == '卯月甲申日'
assert card('WHY-069')['anchors']['asked_at'] == '辰月庚戌日'
assert '子宫瘤' in gold['WHY-068']['outcome_record']
assert '鼻癌' in gold['WHY-069']['outcome_record']
# F5 GSZ-107
g = gold['GSZ-107']
assert '午时云取定可到手' in g['master_prediction'] and '原文录入讹字' in g['grade_note']
assert '重新修改后取走' in g['outcome_record']
# F6 BY-030
c = card('BY-030'); p = pred('BY-030')
assert '原式天将行末另标「关」字' in c['anchors']['四课']
assert '四课原式天将行末另标关字，卡面已注，只作课名关隔背景，不另作断' in p['basis']
assert '次年酉贼破省，黄陂失守' in gold['BY-030']['outcome_record']

SRC = lambda cid: [f"divination/benchmark/phase3/holdout31/inputs/{cid}.json",
                    f"divination/benchmark/phase3/holdout31/test_gold.jsonl [{cid}]",
                    f"divination/benchmark/phase3/runs/round88/acceptance/predictions/{cid}.json",
                    "divination/benchmark/phase3/runs/round88/acceptance/DIAG-H31.md §5",
                    "divination/benchmark/phase3/runs/round88/acceptance/judging/host-mapping.json"]
SEATS = ["DIAG-H31 席（§5 旗标候选）", "R88 数据席回读原卡／金标"]
def entry(cid, disp, flag, finding, sugg):
    return {"anon_id": ours_inv[cid], "case_id": cid, "disposition": disp,
            "finding": finding, "flag": flag, "manifest_carry_suggestion": sugg,
            "registered_round": 88, "relation": "新登记（R88，验收侧旗标定案）",
            "source_seats": SEATS, "sources_checked": SRC(cid)}
def sugg_partial(cid, ftag, gist):
    return (f"验收侧新登记：自 R89 起承接本 R88 标注（DIAG-H31 {ftag}）：按「{gist}，部分成立」登记；金标原文照录不改。")
def sugg_rej(cid, ftag):
    return "只登记不入层：自 R89 起承接本 R88 标注（不成立，验收侧不入 dev 承接层）；金标原文照录不改。"

new = []
new.append(entry('WHY-043','部分成立','DIAG-H31 §5 F1：伏神取用两路候选（卡面不合／取用类）',
  "回原卡与金标逐字核——holdout31 输入卡 anchors 仅载 asked_at／本卦（地风升）／变卦（雷天大壮）／动爻／六爻爻面五项，无 hidden／伏神字段，子孙一亲确不上卦（爻面六亲仅官鬼、父母、妻财），伏神须推算复原，卡面层缺载一层属实（成立面，承 LY-603／LY-246 判例）；两路复原并存属实——我方 basis 逐字载「用神子孙不上卦，震宫首卦震为雷四爻子孙午火，同位伏四爻财丑下」，金标大师断语逐字载「子孫子水伏在飛神父母亥水下，飛來生伏是吉兆，是懷孕的信息」，所取伏神不同（午火／子水）。但断据锚点（本卦／变卦／爻面／月建日辰）全在场、不计 IN，金标 outcome_record 逐字载「到医院检查发现怀孕，二人没有打算马上结婚，于是做了流产手术」，终局明载可核（不成立面）。本席只登记两路并存与卡面缺载，不裁取用方法。故部分成立。",
  sugg_partial('WHY-043','F1','卡面未载伏神字段、子孙不上卦须推算复原，复原两路并存（我方午火伏四爻财丑下／大师子水伏父母亥水下）；锚点全在场、终局明载')))
new.append(entry('DA-051','部分成立','DIAG-H31 §5 F2：方法条目以本案为同式先例候选（自引类）',
  "回原卡、basis 与金标逐字核——holdout31 输入卡 setting／provenance 逐字载本例为《大六壬断案》案051；我方 basis 逐字载「支数：DA-M13载案051同式卯六、辰五、巳四三支连加得十五，本例四课卯、三传辰巳俱在盘面实载，取十五为前程年数之限」——所引方法先例与本案为同一案，先例独立性一层不成立属实（成立面）。但三支实载可核（四课含卯、三传含辰与巳，逐字在卡），金标大师断语逐字载「一气十五年，合作监司之职」，十五之数与大师原断同值、非席位凭空造数，金标 outcome_record 逐年载升迁至司农少卿，终局明载（不成立面）。本席不改方法条目、不改分数，只登记自引形态。故部分成立。",
  sugg_partial('DA-051','F2','方法条目 DA-M13 所引案051同式先例与本案为同一案、先例独立性一层不成立；三支盘面实载、十五之数与大师原断同值、终局明载')))
for cid in ['DA-048','DA-051','DA-055']:
    new.append(entry(cid,'不成立','DIAG-H31 §5 F3：课名底本未载通例候选（残损类）',
      "回原卡逐字核——holdout31 输入卡 anchors 课名逐字作「底本未载」，我方 basis 逐字载课名底本未载、如实记未载不臆补（DA-048 语逐字作「课名底本未载（卡面如实记未载，不臆补）」，余例同旨）；盘体天盘／四课／三传俱全载，课名未载属原书载录形态、不构成断锚点缺口、不计 IN（DIAG-H31 §0 同口径）。金标 outcome_record 终局明载。故旗标不成立，只登记。承 WHY-027／GSZ-105（R87）同型判例。",
      sugg_rej(cid,'F3')))
for cid, asked, outc in [('WHY-068','卯月甲申日','子宫瘤，后服中药而愈'),('WHY-069','辰月庚戌日','鼻癌，手术后正在维持中')]:
    new.append(entry(cid,'不成立','DIAG-H31 §5 F4：asked_at 未载年柱候选（残损类）',
      f"回原卡逐字核——holdout31 输入卡 asked_at 逐字作「{asked}」，月建与日辰俱载在场；年柱未载属原书载录形态、不构成断锚点缺口、不计 IN（DIAG-H31 §0 同口径）。我方 basis 未注此项、仍按月日行断无缺口；金标 outcome_record 逐字载{outc}，终局明载。故旗标不成立，只登记。承 WHY-027（R87）同型判例。",
      sugg_rej(cid,'F4')))
new.append(entry('GSZ-107','部分成立','DIAG-H31 §5 F5：金标断语录入讹字候选（录入类）',
  "回金标逐字核——holdout31 金标 master_prediction 逐字作「父母子水伏而空亡，午时冲出冲实，午时云取定可到手」，金标 grade_note 逐字自载「断语『午时云取』为原文录入讹字，照录登记」，录入讹字一层属实（成立面，承 GSZ-069（R82）判例）。但金标 grade_note 明载建卡口径五要素（卦名／动爻／世应／六亲纳支／月建日辰）复核全在场、不计 IN，金标 outcome_record 逐字载午时取衣、因不合身争执、重新修改后取走，终局明载可核（不成立面）。故部分成立，金标原文照录不改。",
  sugg_partial('GSZ-107','F5','金标断语「午时云取」为原文录入讹字、金标 grade_note 已自载照录登记；五要素全在场、终局明载')))
new.append(entry('BY-030','不成立','DIAG-H31 §5 F6：四课原式附标字候选（卡面不合类）',
  "回原卡与 basis 逐字核——holdout31 输入卡四课注逐字载「原式天将行末另标『关』字」，卡面已自注；我方 basis 逐字载「四课原式天将行末另标关字，卡面已注，只作课名关隔背景，不另作断」，席位已自标且处置与卡面注记一致，不构成数据瑕疵。金标 outcome_record 逐字载「案验：次年酉贼破省，黄陂失守」，终局明载。故旗标不成立，只登记。承 BY-017（R87）同型判例。",
  sugg_rej('BY-030','F6')))
assert len(new) == 9
assert collections.Counter(a['disposition'] for a in new) == {'部分成立':3,'不成立':6}

# ---------- 工序三：annotations-r88 落盘 ----------
out_ann = copy.deepcopy(ann87)
out_ann['round'] = 88
out_ann['_provenance'] = ("R88 数据席（旗标定案流水与承接登记，独立席位，不兼任本轮盲测／评审／诊断／判读／修订，不改方法、不动分数）："
  "以 data/case-annotations-r87.json 为底承接全量 300 件（成立 14／部分成立 235／不成立 49／未核 2），前 300 件逐件原样、无删改；"
  "承接对勘：R87 附则平台侧部分成立 43 件已于 R88 manifest 以 _r87_carryover_notes_addendum 落实（脚本断言：层 id 集与 r87 部分成立∧registered_round＝87∧平台侧集全等、层注记与各条 manifest_carry_suggestion 逐字全等、43 件 dev 结局原文在 cases 载荷逐件回读在场；cases 载荷结构化 SHA 与 R87 manifest 全等）；"
  "验收侧 5 件（CYJ-006／CYJ-007／CYJ-008／CYJ-009／CYJ-010）不在 dev cases、不入层，照 R83 判例只在汇编件登记其验收面处置，_r88_manifest_note 已同口径明载；_r82 层 3 件已经 R85 主持裁定结案，只作在册登记；"
  "本轮新定案 9 条（验收侧，来源＝DIAG-H31 §5 旗标候选 F1–F6，逐件回 holdout31 原卡／金标／验收 predictions 定案）：部分成立 3（WHY-043／DA-051／GSZ-107）、不成立 6（DA-048／DA-051／DA-055／WHY-068／WHY-069／BY-030；DA-051 以 F2 部分成立条与 F3 不成立条两旨并行登记、不合并）；"
  "合计 309 件（成立 14／部分成立 238／不成立 55／未核 2）。基线六处 R88 盘上复核在册、形态未变；CZ-QX 维持 16；待核四件维持；CYJ fidelity 例外 46 件与紫微池挂起 6 项只登记不处置；AS-307 双条并行保留、不合并。")
out_ann['annotations'] = ann87['annotations'] + new
sc = copy.deepcopy(ann87['special_checks'])
sc.append({"item":"（R88）特别核查64：R87 承接对勘与 _r82 层结案登记续记",
  "conclusion":"R87 附则平台侧部分成立 43 件已于 R88 manifest 以 _r87_carryover_notes_addendum 落实（层 id 集与附则 §三.1 清单逐件全等、层注记与 annotations-r87 各条 manifest_carry_suggestion 逐字全等 43/43、dev 结局原文逐件回读在场，落实 43／维持 0／订正 0）；验收侧 5 件（CYJ-006／CYJ-007／CYJ-008／CYJ-009／CYJ-010）不在 dev cases、未入层，照 R83 判例只登记验收面处置（_r88_manifest_note 同口径明载）。_r82 层 3 件（LY-406／LY-446／LY-524）已经 R85 主持裁定结案，注记保留只作在册登记，不再滚动对勘。",
  "evidence":"runs/round88/judging/outcome-manifest.json _r87_carryover_notes_addendum 43 件与 _r88_manifest_note（落盘脚本结构化直读断言）；manifest 全文 SHA-256 "+MAN88_SHA+"、cases 载荷结构化 SHA 00f362bd8e4b55ceff31502cb5f7e8239855b1f806a7b1495284af80186a31ad（与 R87 manifest 全等）。",
  "scope_note":"对勘只登记，不改 manifest 任一侧。"})
sc.append({"item":"（R88）特别核查65：验收侧旗标定案总登记（DIAG-H31 §5，holdout31）",
  "conclusion":"DIAG-H31 §5 旗标候选 F1–F6 逐件回 holdout31 输入卡、金标与验收 predictions 定案：新定案 9 条——部分成立 3（F1 WHY-043 伏神两路并存＋卡面未载伏神字段；F2 DA-051 方法先例自引本案；F5 GSZ-107 金标断语录入讹字），不成立 6（F3 DA-048／DA-051／DA-055 课名底本未载为原书载录形态；F4 WHY-068／WHY-069 asked_at 未载年柱为原书载录形态；F6 BY-030 附标「关」字卡面已注、席位已自标）。DA-051 两旨（F2／F3）并行登记、不合并。本集 IN 实测 0／28 与定案口径一致，无待核新件（F1–F6 全部定案、无维持待核件）。",
  "evidence":"runs/round88/acceptance/DIAG-H31.md §5；holdout31/inputs 与 test_gold.jsonl、runs/round88/acceptance/predictions 逐件回读（落盘脚本逐件逐字断言全过）。",
  "scope_note":"验收侧定案只及标注与承接建议，不改验收分数、不改方法条目。"})
sc.append({"item":"（R88）特别核查66：指令性字样特别核查基线六处复核",
  "conclusion":"基线六处经 R88 盘上逐处回读在册、形态未变，出入 0 处：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）＋LR2-016 manifest editor_note 一处（_r56_lr2016_split 分列层、原文逐字全等）＋LR2-016 评审包 editor_note 层一处（以 host-mapping 对位 anon P3-678389ac 定位 packet2.json 与 packetA.json、独立字段逐字在场、与分列层全等）。本轮新增同型件：无。各席一律按数据处理。",
  "evidence":"runs/round88/judging/outcome-manifest.json 与 packet2.json／packetA.json（落盘脚本逐处逐字断言全过）。",
  "scope_note":"只登记、不改任何文本。"})
sc.append({"item":"（R88）特别核查67：待核四件维持与 CZ-QX 维持登记",
  "conclusion":"BZ-029／BZ-040／LY-537／YM-070 四件无新证据、维持待核原登记（LY-537 以未核条目在册、YM-070 以未核条目在册；BZ-029／BZ-040 不入 annotations）；CZ-QX 维持 16（holdout31 无测字例、DIAG-H31 记不适用／不增；平台侧无测字段新结算），只登记不另行结算。",
  "evidence":"data/case-annotations-r87.json 待核条目承接；runs/round88/PREREG.md 与 runs/round88/acceptance/DIAG-H31.md（CZ-QX 不适用／不增）。",
  "scope_note":"无盘外独立史源不裁。"})
sc.append({"item":"（R88）特别核查68：供给续记——CYJ fidelity 例外与紫微池挂起只登记；AS-307 双条并行续行",
  "conclusion":"CYJ fidelity 例外 46 件照 PREREG-r88 在册口径只登记、不入常规组集、本席不处置；紫微池挂起 6 项照在册口径只登记、无增减、无核查动作。AS-307 双条并行例外形态续行：R80 部分成立条与 R85 不成立条并行保留、不合并（annotations-r88 中 AS-307 仍恰 2 条、逐件原样承接），本轮无新旗标涉 AS-307、不另立第三条。",
  "evidence":"runs/round88/PREREG.md（fidelity 例外 46 不入常规；紫微池挂起 6 项只登记）；data/case-annotations-r87.json AS-307 两条承接（落盘脚本计数断言）。",
  "scope_note":"只登记，不处置。"})
out_ann['special_checks'] = sc
out_ann['counts'] = {
  "base_file":"data/case-annotations-r87.json","base_cases_total":300,
  "base_verdicts":{"成立":14,"部分成立":235,"不成立":49,"未核":2},
  "carryover_check_r87_addendum":{"platform_layer":"_r87_carryover_notes_addendum","platform_items":43,
    "platform_ids":ids43,"platform_result":{"落实":43,"维持":0,"订正":0},
    "acceptance_items":5,"acceptance_ids":cyj5,
    "acceptance_status":"不在 dev cases、不入层，照 R83 判例只在汇编件登记验收面处置；_r88_manifest_note 同口径明载"},
  "carryover_check_r82_closed":{"layer":"_r82_carryover_notes_addendum","items":3,
    "status":"已经 R85 主持裁定结案，R88 只作在册登记、不再滚动对勘"},
  "new_registrations_r88":9,
  "new_cases_r88":{"部分成立_acceptance":["WHY-043","DA-051","GSZ-107"],
                   "不成立_acceptance":["DA-048","DA-051","DA-055","WHY-068","WHY-069","BY-030"],
                   "da051_dual_gist":"DA-051 以 F2（部分成立）与 F3（不成立）两旨并行立条、不合并"},
  "r88_partial_upheld_acceptance":["WHY-043","DA-051","GSZ-107"],
  "baseline_instructional_strings":{"items":6,"result":"R88 盘上逐处在册、形态未变，出入 0 处"},
  "czqx_same_tier_count":16,
  "as307_double_entry":"R80 部分成立条与 R85 不成立条并行保留、不合并；R88 不另立第三条",
  "cases_total":309,"verdicts":{"成立":14,"部分成立":238,"不成立":55,"未核":2}}
assert len(out_ann['annotations']) == 309
assert out_ann['annotations'][:300] == ann87['annotations']
assert sum(1 for a in out_ann['annotations'] if a['case_id']=='AS-307') == 2
assert collections.Counter(a['disposition'] for a in out_ann['annotations']) == {'成立':14,'部分成立':238,'不成立':55,'未核':2}
p_out = BASE/'data/case-annotations-r88.json'
assert not p_out.exists()
with open(p_out,'w',encoding='utf-8') as f: json.dump(out_ann, f, ensure_ascii=False, indent=1)
print('WROTE', p_out)
print('counts ok 309 = 14/238/55/2 ; new 9 = 3 partial + 6 rejected')
# 保存中间量供汇编脚本段使用
import pickle
with open(BASE/'runs/round88/r88_data_seat_state.pkl','wb') as f:
    pickle.dump({'rows43':rows43,'man88_sha':MAN88_SHA,'new':new,'packet_hits':packet_hits,'lr_anon':lr_anon}, f)
print('state saved')
