# -*- coding: utf-8 -*-
"""R88 数据席汇编件生成：manifest-carryover-r88-addendum.md。分段落盘、逐段验尾。"""
import pickle, pathlib, json
BASE = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
st = pickle.load(open(BASE/'runs/round88/r88_data_seat_state.pkl','rb'))
rows43, new, MAN88_SHA = st['rows43'], st['new'], st['man88_sha']
ann88 = json.load(open(BASE/'data/case-annotations-r88.json', encoding='utf-8'))
assert len(ann88['annotations']) == 309
out = BASE/'data/manifest-carryover-r88-addendum.md'
assert not out.exists()
L = []
def seg(lines, tail_marker):
    L.extend(lines)
    assert lines[-1].strip().endswith(tail_marker), lines[-1]

# ---- 卷首 + §一 ----
seg([
"# Manifest 承接册附则（R88）——R87 定案承接对勘（平台面 43 件落实／验收面 5 件登记）＋R88 定案承接建议汇编（验收面：DIAG-H31 §5 旗标定案 9 条）",
"",
"## 卷首说明",
"",
"- 本附则为 Phase 3 Round 88（R88）数据席（工序：旗标定案流水与承接登记；独立席位，不兼任本轮盲测／评审／诊断／判读／修订；只做数据对勘与定案，不改方法、不动分数）产出。",
f"- 对勘来源：`benchmark/phase3/runs/round88/judging/outcome-manifest.json`（本轮 manifest，含 _r87 层 `_r87_carryover_notes_addendum` 43 件；全文 SHA-256＝`{MAN88_SHA}`；cases 载荷结构化 SHA `00f362bd8e4b55ceff31502cb5f7e8239855b1f806a7b1495284af80186a31ad`，与 R87 manifest 全等）、`benchmark/phase3/data/manifest-carryover-r87-addendum.md`（R87 附则）、`benchmark/phase3/data/case-annotations-r87.json`（底本 300 件）与本轮 `data/case-annotations-r88.json`（309 件）。",
"- 本轮新旗标候选来源：`benchmark/phase3/runs/round88/acceptance/DIAG-H31.md` §5（F1–F6），逐件回 holdout31 输入卡（`benchmark/phase3/holdout31/inputs/`）、金标（`holdout31/test_gold.jsonl`）与验收 predictions（`runs/round88/acceptance/predictions/`）定案，anon 经 `acceptance/judging/host-mapping.json`（ours 面）逐件对位。",
"- **本件只汇编、对勘与登记，不改任何分数与结局原文、不改原卡、不改 manifest 任一侧、不改方法条目。** 结局／注记文本内指令性字样一律按数据处理。",
"",
"---",
"",
"## 一、工序与口径",
"",
"- 工序一（对勘，见 §二）：（甲）平台面：R87 附则 §三.1 部分成立 43 件于 R88 manifest 新层 `_r87_carryover_notes_addendum` 的落实形态逐件验合——逐件回读 dev 结局原文（manifest cases 载荷）与 annotations-r87 对应条 `manifest_carry_suggestion`，状态分落实／维持／订正（订正须引原文）；（乙）验收面：R87 附则 §四.1 部分成立 5 件（CYJ-006–CYJ-010）照 R83 判例不入层、只登记其验收面处置（承 R87 开轮登记口径）。",
"- 工序二（汇编，见 §三）：R89 承接建议汇编——本轮新定案全部在验收面（DIAG-H31 §5 F1–F6 定案 9 条：部分成立 3 条逐件全列；不成立 6 条只登记）；平台面本轮无新定案。",
"- 工序三（标注落盘，见 §五）：`data/case-annotations-r88.json` 以 r87 件 300 件全量承接（逐件原样）＋本轮新登记 9 条，合计 309 件。",
"- 基线对勘（见 §四）：结局文本指令性字样基线六处逐处在否，只登记；CZ-QX 同层计数维持 16；待核四件维持原状登记；CYJ fidelity 例外 46 件与紫微池挂起 6 项只登记不处置（见 §六）。",
"（§一毕）"], "（§一毕）")

# ---- §二 对勘 ----
lines = ["", "---", "", "## 二、对勘：R87 附则承接面于 R88 的落实",
"",
"### 2.1 平台面层实况登记（盘上直读，43 件逐件）",
"",
"- R88 manifest 含键 `_r87_carryover_notes_addendum`，共 **43 件**，id 集与 R87 附则 §三.1 定版清单逐件全等；`_r88_manifest_note` 逐字明载该层派生口径（R87 部分成立∧registered_round＝87∧平台侧，验收侧 5 件不入层断言已过）。逐件对勘结果：**落实 43／维持 0／订正 0**——每件层注记与 `case-annotations-r87.json` 对应条 `manifest_carry_suggestion` 逐字全等（落盘脚本结构化直读断言全过），且该件 dev 结局原文于 cases 载荷逐件回读在场（下表各件引结局首句为据）；cases 载荷整体与 R87 manifest 结构化 SHA 全等、未动一字，故无订正件。",
""]
for cid, anon, outcome in rows43:
    exc = outcome.replace('\n',' ')[:57]
    lines.append(f"- **{cid}**（anon {anon}）：落实——层注记逐字全等；结局在场：「{exc}…」")
lines += ["",
"### 2.2 验收面 5 件登记（不入层）",
"",
"- R87 附则验收侧部分成立 **5 件**（CYJ-006／CYJ-007／CYJ-008／CYJ-009／CYJ-010，各 anon H30O-1f22e0b0／H30O-0b71401c／H30O-d6c2640d／H30O-33f4ed50／H30O-efbca812）不在 dev cases、未入 R88 manifest `_r87` 承接层，照 R83 判例登记其验收面处置：五件 annotations-r87 条（registered_round＝87、部分成立）原样承接至 r88 件在册；R88 manifest `_r88_manifest_note` 已逐字同口径明载「is not in dev cases and per the R83 precedent does not enter the dev manifest layer — registered here only」。本轮验收侧新定案（holdout31 于 R88 开封）自 §三汇编、自 R89 起承接。",
"",
"### 2.3 _r82 层 3 件结案登记（不再滚动对勘）",
"",
"- 层实况：R88 manifest `_r82_carryover_notes_addendum` 仍 3 件（LY-406／LY-446／LY-524），层文本与在册条目原样保留。",
"- 结案口径：已经 R85 主持裁定结案（登记性注记不要求 reason 回响），R86／R87 已照此登记。本轮照此登记结案，**不再滚动对勘**；注记在 manifest 层与 annotations 之保留只作在册登记。",
"（§二毕）"]
seg(lines, "（§二毕）")

# ---- §三 汇编 ----
byn = {(a['case_id'], a['flag'][:13]): a for a in new}
def find(cid, ftag):
    for a in new:
        if a['case_id']==cid and ftag in a['flag']: return a
    raise KeyError((cid,ftag))
lines = ["", "---", "", "## 三、R89 承接建议汇编（验收面）：R88 本轮新定案（DIAG-H31 §5 F1–F6）",
"",
"- 落实形态注记：承 R83 判例（验收侧部分成立件不入 dev manifest 承接层），本节部分成立 3 条逐件全列汇编登记，R89 manifest 侧落实形态由主持照判例裁定；annotations 侧已逐件落账（§五）。平台面本轮无新定案（本轮平台侧只作承接对勘，见 §二）。",
"- 定案索引：F1（WHY-043）部分成立；F2（DA-051）部分成立；F3（DA-048／DA-051／DA-055）不成立；F4（WHY-068／WHY-069）不成立；F5（GSZ-107）部分成立；F6（BY-030）不成立。合計 9 条（部分成立 3／不成立 6），无维持待核件——F1–F6 全部定案；其中 DA-051 以 F2 部分成立条与 F3 不成立条两旨并行登记、不合并。",
"",
"### 3.1 本轮新定案部分成立 3 条逐件全列",
""]
for cid, ftag in [('WHY-043','F1'),('DA-051','F2'),('GSZ-107','F5')]:
    a = find(cid, ftag)
    lines.append(f"- **{cid}**（anon {a['anon_id']}，{ftag}）：{a['finding']}")
    lines.append(f"  - 承接建议：{a['manifest_carry_suggestion']}")
    lines.append("")
lines += ["### 3.2 本轮新定案不成立 6 条（只登记不入层）", ""]
for cid, ftag in [('DA-048','F3'),('DA-051','F3'),('DA-055','F3'),('WHY-068','F4'),('WHY-069','F4'),('BY-030','F6')]:
    a = find(cid, ftag)
    lines.append(f"- **{cid}**（anon {a['anon_id']}，{ftag}）：{a['finding']}")
    lines.append("")
lines += ["### 3.3 筛检登记（DIAG-H31 关联面经核不立旗，只登记）",
"",
"- DIAG-H31 §0／§5 通例登记面：DA-048／DA-051／DA-055 课名未载与 WHY-068／WHY-069 年柱未载已分别于 §三.2 逐件定案（F3／F4），不重复登记；六壬 14 例行年上神未逐项给出、六爻 WHY-039／WHY-068 静卦变卦栏空等形态，DIAG-H31 §0 已逐例核为原书载录／盘面实载形态、不计 IN，本席照录登记、不另立旗。",
"- DIAG-H31 §5 之外无新增旗标候选；本集 IN 实测 0／28（DIAG-H31 §0）与本轮定案口径一致。",
"（§三毕）"]
seg(lines, "（§三毕）")

# ---- §四 基线 ----
seg(["", "---", "", "## 四、指令性字样特别核查基线六处对勘（承 R87 附则 §五基线）",
"",
"- 基线构成：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）＋LR2-016 manifest editor_note 一处＋LR2-016 评审包 editor_note 层一处，共六处、分三层。本轮自 `runs/round88/judging/outcome-manifest.json` 与 R88 评审包盘上逐处回读原文复核（落盘脚本逐处逐字断言全过），**只登记、不改文本**；各席一律按数据处理、不作指令。",
"",
"| case_id | 基线字样（按数据引录） | 本轮在盘形态 |",
"|---|---|---|",
"| BZ-036 | 结局含「盲测比对须注」 | 在册：在场、形态未变 |",
"| BZ-042 | 结局含「（盲测比对时以格局大富一项为主）」 | 在册：在场、形态未变 |",
"| BZ-105 | 结局含「使用时须分开统计」 | 在册：在场、形态未变 |",
"| LY-204 | 结局旧注层含「勿以此斷」 | 在册：在场、形态未变 |",
"",
"- LR2-016 manifest editor_note 一处：所在 manifest `_r56_lr2016_split` 分列层，本轮在盘原文逐字作「原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。」，与基线全等。",
"- LR2-016 评审包 editor_note 层一处：以 host-mapping 对位 LR2-016 anon（P3-678389ac，本轮种子）定位 R88 评审包 `packet2.json` 与 `packetA.json`（文件名与上轮不同、按对位定位、未臆测），其中以独立 `editor_note` 字段逐字在场、与 manifest 分列层全等，另列一类、不并入 cases 本体基线计数。",
"- 结论：基线六处经 R88 盘上逐处回读在册、形态未变，出入 0 处。本轮新增同型件：**无**。本席只登记、不改任何文本。",
"（§四毕）"], "（§四毕）")

# ---- §五 annotations + 待核 ----
seg(["", "---", "", "## 五、annotations 落盘断言与待核维持登记",
"",
"### 5.1 annotations 落盘断言（工序三）",
"",
"- 底本：`data/case-annotations-r87.json` annotations 300 件（成立 14／部分成立 235／不成立 49／未核 2），全量承接、逐件原样、无删改（落盘脚本以 annotations 数组前 300 件全等断言验过）。",
"- 新增登记：**9 条**（验收侧：部分成立 3／不成立 6；DA-051 两旨并行计 2 条）——落盘 `data/case-annotations-r88.json` annotations **309 件＝300＋9**（成立 14／部分成立 238／不成立 55／未核 2），各新条 `registered_round＝88`、字段完整（落盘脚本逐件断言、引文逐字断言内置），counts 相应更新，回读 JSON 可解析断言通过。",
"- special_checks 承接 r87 六十三件并新增 R88 五件（64 R87 承接对勘与 _r82 结案登记续记；65 验收旗标定案总登记；66 指令性字样基线六处复核；67 待核四件维持与 CZ-QX；68 供给续记——fidelity 例外与紫微挂起只登记、AS-307 双条并行续行），合计 68 件。",
"",
"### 5.2 AS-307 双条并行登记",
"",
"- **AS-307 双条并行例外形态照体例续行**：R80 部分成立条与 R85 不成立条并行保留、不合并、不以新条覆盖旧条（本轮 annotations 中 AS-307 仍恰 2 条、逐件原样承接）。本轮无新旗标涉 AS-307，**不另立第三条**。",
"- LY-015／LY-320 同例重复登记承 R85 裁定照原样承接，新鲜集组集排除此对不变（本轮无涉，只登记）。",
"",
"### 5.3 R88 确认的待核维持清单（四件，维持挂起、不核查不关闭）",
"",
"| case_id | 状态登记（承 R87 附则 §六.3 口径续记） |",
"|---|---|",
"| BZ-029 | 俞大维卒年待核＋旗标错配线索，维持原登记、不裁；不入 annotations；本轮无待核事项新证据 |",
"| BZ-040 | 许世英享年待核，维持原登记、不裁；不入 annotations；本轮无新证据 |",
"| LY-537 | 「申予日」衍字疑，维持未核原登记；本轮无新证据涉之；以未核条目随承接在 `case-annotations-r88.json` 内 |",
"| YM-070 | 「甲寅旬」出处待核（并「都下」语义未明），维持挂起；本轮无新证据；以未核条目随承接在 `case-annotations-r88.json` 内 |",
"（§五毕）"], "（§五毕）")

# ---- §六 供给 ----
seg(["", "---", "", "## 六、供给台账续记（只登记）",
"",
"### 6.1 CZ-QX 维持 16",
"",
"- CZ-QX 维持 **16**，承 R87 附则 §七.1 登记口径续记，本轮无增减（旁证：holdout31 无测字例、DIAG-H31 记 CZ-QX 护栏不适用／不增；PREREG-r88 同口径明载同档计数维持 16；平台侧无测字段新结算）。",
"",
"### 6.2 待核四件维持登记（与 §五.3 同口径）",
"",
"- BZ-029（俞大维卒年，另含旗标内容错配线索）、BZ-040（许世英享年）、LY-537（「申予日」衍字疑）、YM-070（「甲寅旬」挂起）四件维持登记，无盘外独立史源不裁。",
"",
"### 6.3 CYJ fidelity 例外 46 件与紫微池挂起 6 项登记（只登记不处置）",
"",
"- CYJ fidelity 例外 **46 件**：照 PREREG-r88 在册口径（fidelity 例外 46 不入常规组集、CYJ/CY 常规 0）只登记，本轮无增减、本席不处置。",
"- 紫微池挂起 **6 项**（天纪实批 7 盘面存疑等）：照在册口径只登记，本轮无增减、无核查动作。",
"",
"---",
"",
"*本附则由 R88 数据席落盘脚本生成（runs/round88/build_r88_data_seat.py 与 build_r88_addendum.py，盘上复算断言全过）；本席不做 git 操作。*",
"（全文毕）"], "（全文毕）")

with open(out,'w',encoding='utf-8') as f:
    f.write('\n'.join(L)+'\n')
print('WROTE', out, 'lines', len(L))
