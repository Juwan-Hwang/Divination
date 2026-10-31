#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""delta 收尾登记：封存日志 append delta 节 + 构建报告文本插入 delta 节（原节不动）。"""
import json, hashlib

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
REG = json.load(open(f'{BASE}/runs/round76/delta-holdout22-register-r76-hostseat.json', encoding='utf-8'))
SEAL_LOG = f'{BASE}/data/holdout22-seal-log.md'
REPORT = f'{BASE}/runs/round76/build-holdout22-report-r76.json'

NEW_SHA = REG['gold_delta']['new_sha256_hashlib']
assert NEW_SHA == REG['gold_delta']['new_sha256_sha256sum']
ids = REG['new_selection_ids']
ds = REG['ds011_change']; qm = REG['qm301_change']; v5 = REG['zcb005_verification']
scan5 = REG['zcb005_card_scan']

seal_section = f"""
## 九、主持裁处与 delta 重建（R76 主持裁处 delta 修正席，2026-10-31）

本节为封存后主持裁处之执行登记，以 append 追加，原 §一–§八一字未动。执行脚本 `runs/round76/delta_holdout22_r76_hostseat.py`、登记件 `runs/round76/delta-holdout22-register-r76-hostseat.json`、原书叶面渲染件 `runs/round76/delta-r76-hostseat/`（PDF557/558 页 300dpi 渲染与裁切图）。前置核验：动手前金标 SHA-256 实测 `1e299bdaf10724bf2ba66d1f4933fdcbeee11b5970f978df975872bb7164ae6a`，与主持第三读一致；快照 `kb-snapshot-holdout22` 未动（其 SHA 清单文件哈希改前改后一致）。本席不开封、不作断、不评分、未做 git 操作。

### 九.1 三项裁处执行

1. **ZCB-003 换例（剔除 → ZCB-005）——已执行**。裁处理由：ZCB-003 输入卡锚点原文含结论句「故知丁艱」，属断语/结局事实入卡。处置：精确删除 `holdout22/inputs/ZCB-003.json` 与 `holdout22/test_gold.jsonl` 中 ZCB-003 行（精确路径/精确行操作，非通配删除）；以台账 `runs/round76/digestion/SUPPLY-MINING-zichubu-r76.json` 之 ZCB-005 记录（eligible＝true∧anchor_status＝present∧contamination_pre＝low∧separable＝true，本席复断言通过）按与原测字四例同一规格建卡建标（详见 §九.2）。测字构成仍 4 例：ZCB-001、ZCB-002、ZCB-004、ZCB-005；T 仍 27。
2. **DS-011 卡面中性化——已执行**（逐字对照见 §九.4）。`holdout22/inputs/DS-011.json` 的 setting 与 provenance 各 1 处，删第八章小节题全文「商海沉浮，女强人命运多舛」，定位只留「第八章第一节六」，其余字串一字不动；subject 之「女企业家」为输入侧事实，保留未动。原题全文只留本日志登记（本节对照与 §三标旗①）。金标 DS-011 行除行序重整外一字未动（金标侧 provenance 照原登记）。
3. **QM-301 卡面中性化——已执行**（逐字对照见 §九.4）。`holdout22/inputs/QM-301.json` 中实例题「少收的贷款能找回」全卡共 2 处（setting 1 处、provenance 1 处），逐处删该题名全文、保留下编第七章「钱物丢失预测」实例一之定位部分；全卡其余字段经检索无该题名字串，question「刚才卖货时少收了顾客500元钱，看货款能不能找回来」为输入侧问句原文、非题名字串，一字未动。金标 QM-301 行除行序重整外一字未动。

### 九.2 ZCB-005 建卡与金标断语逐字核验登记

- **建卡规格（同原测字四例）**：字段白名单 {{id, tradition, subject, context, question, setting, provenance, redistributable, license_status, anchors}}，键序同原四例；context 与 anchors.split_process_verbatim ← 台账 input_side 逐字（字形拆分过程为输入侧锚点原文）；anchors.character＝「因」；subject＝「孟瓶庵与榜前同测二友」、question＝「榜前书因字请测（三人同字分测）」为组写（口径在此登记）；setting＝「《字触补》卷二·外部·叶9（《四库未收书辑刊》陆辑第拾捌册，PDF页557下半）」、provenance 同 setting＋「；用户经学校图书馆提供；redistributable=false」；license_status＝「古籍文本（合集扫描本），内部研究用」；setting/provenance 只载卷叶与 PDF 页定位、不载原书条题（同原四例中性化口径）。剥离：title/anchor_*/contamination_*/separable/eligible/cz_qx_*/dedup/transcription/master_assertion/outcome 不入卡。
- **取原书口径**：任务书作《字触补》在 `incoming/wanted-books-3/` 之合集 PDF 内；台账 meta 登记之 container_file 实为 `incoming/wanted-books-5/Book/四库未收书辑刊 陆辑 拾捌册 (四库未收书辑刊编纂委员会编).pdf`（wanted-books-3/Book 下无此 PDF），本席以台账 meta 为准取原书，该文件 SHA-256 实测 `c692398989c29e04a6964b19191c0ac3f0ac69668fdc2d3cff78d2146ead6b5e` 与台账登记一致。ZCB-005 出处照台账 source 字段：卷二·外部·叶9，PDF页557下半（条末续于 PDF558 上半）。
- **金标断语逐字核验（回原书叶面，300dpi 渲染逐句对勘）——逐字核验通过，不补录**。金标 master_prediction＝「（孟）君必為此科解首矣；（友二）君此科恐無分，或後此有恩科亦必中；（友三）其終於一衿乎。」（全文 {v5['master_prediction_chars']} 字），三人三断照原书分列，逐断对勘：
  - 孟瓶庵断「君必為此科解首矣」——原书叶9（PDF557下半）「其人曰此為國中一人之象君必為此科解首矣」，逐字合。
  - 友二断「君此科恐無分，或後此有恩科亦必中」——原书叶9（PDF557下半）「其人曰君此科恐無分或後此有恩科亦必中」（原书无逗号，逗号为转录标点），逐字合。
  - 友三断「其終於一衿乎」——原书叶9续（PDF558上半）「君之扇適加因字正中有困之象其終於一衿乎」，逐字合。
  - 结局「後三君皆如其言」——原书叶9续（PDF558上半）「後三君皆如其言此人惜不傳姓名殆亦高鳳之流亞矣」，台账 outcome 逐字合、照台账。
  - 登记说明：金标中（孟）／（友二）／（友三）标签与分号为三人三断之分列标记（同 DS 例「／」台账摘录分隔符先例），非原书文字；断语本体逐字，故不触发逐字补录，无补录字数。grade_note 照原四例公式组写（锚点 present 依据、污染 low 依据、转录 visual confidence＝0.9、CZ-QX 计数例注记均承台账逐字）。
  - 附注（输入侧）：台账 input_side 作「以徐[?]茶書一因字」，原书叶面该处作「以餘茶書一因字」（餘字清晰）；[?] 为台账未判准标记、非断语字段，输入卡照规格承台账逐字不改，仅此附注。
- **新卡同一套自检（全过）**：字段白名单键序合；禁用键递归扫描零命中；断语片段扫描（标点分句整句≥8字＋去空白12字滑动窗口，对卡全文本逐字子串）零命中；结局片段扫描零命中——无 fragment 需分类登记；内容级一级/二级标记＋字段名黑名单扫描零命中；卡内无「故知…」式结论句（「故知」子串检索零命中）。

### 九.3 新选集与新金标 SHA

- **新选集 id 全表（T＝27，金标行序照 id 序重整后之序）**：{'、'.join(ids)}。构成：八字 DS 9（DS-004–DS-012）、六爻 GSZ 4（GSZ-022、GSZ-023、GSZ-024、GSZ-026）、奇门 QM 10（QM-011–QM-014、QM-201–QM-203、QM-301–QM-303）、测字 ZCB 4（ZCB-001、ZCB-002、ZCB-004、ZCB-005）。其余 24 例之卡与金标内容一字未动（金标仅行序重整与 ZCB 一删一增；未动行经逐行字节无损自检）。
- **改后两卡复扫**：DS-011、QM-301 改后重行断语/结局片段扫描、标记扫描、禁用键扫描、字段白名单核，均零命中/通过。
- **新金标 SHA-256（双读）**：脚本 hashlib 读数 `{NEW_SHA}`；脚本外 `sha256sum` 读数 `{REG['gold_delta']['new_sha256_sha256sum']}`；两读一致，成立。原 SHA `1e299bdaf10724bf2ba66d1f4933fdcbeee11b5970f978df975872bb7164ae6a` 自本节落盘起作废留痕（承 §八口径）。开封条件不变（§八写死口径不改）。

### 九.4 两卡改动逐字对照（改前／改后）

**DS-011（inputs/DS-011.json，setting 与 provenance 各 1 处）**

- setting 改前：「{ds['before']['setting']}」
- setting 改后：「{ds['after']['setting']}」
- provenance 改前：「{ds['before']['provenance']}」
- provenance 改后：「{ds['after']['provenance']}」

**QM-301（inputs/QM-301.json，setting 与 provenance 各 1 处）**

- setting 改前：「{qm['before']['setting']}」
- setting 改后：「{qm['after']['setting']}」
- provenance 改前：「{qm['before']['provenance']}」
- provenance 改后：「{qm['after']['provenance']}」
"""

with open(SEAL_LOG, 'a', encoding='utf-8') as f:
    f.write(seal_section)

# 构建报告：文本插入 delta 节（原节字节不动）
raw = open(REPORT, encoding='utf-8').read()
assert 'delta_r76_host_ruling' not in raw
report_before_sha = hashlib.sha256(raw.encode('utf-8')).hexdigest()
delta_obj = {
    'executor': '主持裁处 delta 修正席（R76）',
    'date': '2026-10-31',
    'script': 'runs/round76/delta_holdout22_r76_hostseat.py',
    'register': 'runs/round76/delta-holdout22-register-r76-hostseat.json',
    'precheck_gold_sha256': REG['precheck']['gold_sha256_before'],
    'changes': {
        '1_zcb003_replaced_by_zcb005': {
            'removed_input_card': 'holdout22/inputs/ZCB-003.json（精确路径删除）',
            'removed_gold_id': 'ZCB-003',
            'reason': '输入卡锚点原文含结论句「故知丁艱」，属断语/结局事实入卡，主持裁定换例',
            'new_card': REG['zcb005_card'],
            'new_gold': REG['zcb005_gold'],
            'eligibility': REG['zcb005_eligibility'],
            'field_mapping': REG['zcb005_field_mapping'],
            'verbatim_verification': REG['zcb005_verification'],
            'card_scan_same_suite': REG['zcb005_card_scan'],
            'cezi_composition_after': ['ZCB-001', 'ZCB-002', 'ZCB-004', 'ZCB-005'],
        },
        '2_ds011_neutralized': ds,
        '3_qm301_neutralized': qm,
    },
    'modified_cards_rescan': REG['modified_cards_rescan'],
    'source_book_check': REG['source_book_check'],
    'gold_delta': REG['gold_delta'],
    'new_selection_ids': ids,
    'final_check': REG['final_check'],
    'kb_snapshot_holdout22_untouched': True,
    'note': '原报告各节一字未动，本节为文本追加；封存日志同步登记于 data/holdout22-seal-log.md §九。'
              '金标 DS-011/QM-301 行除行序外一字未动。',
}
delta_txt = json.dumps(delta_obj, ensure_ascii=False, indent=2)
delta_txt_indented = '\n'.join('  ' + line if line else line for line in delta_txt.splitlines())
stripped = raw.rstrip()
assert stripped.endswith('}')
new_raw = stripped[:-1].rstrip() + ',\n  "delta_r76_host_ruling": ' + delta_txt_indented + '\n}\n'
json.loads(new_raw)  # 合法性校验
with open(REPORT, 'w', encoding='utf-8') as f:
    f.write(new_raw)
print('seal log appended; report delta inserted; report sha before:', report_before_sha)
print('new sha:', NEW_SHA)
