import json, pathlib, collections, copy
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
SUG = "主持裁定续接：自 R77 起承接本 R76 标注：按「卡面无 tradition/system 字段、basis 首行虚称『卡面 tradition＝bazi』（R69 型）、方法实质八字、不作废不重测」登记；结局原文照录不改。"
SIX = ["BZ-032","BZ-035","BZ-036","BZ-037","BZ-038","BZ-041"]
ANON76 = {"BZ-032":"P3-96c4fc89","BZ-035":"P3-868d8506","BZ-036":"P3-a0772b1c","BZ-037":"P3-414208c8","BZ-038":"P3-5237f97b","BZ-041":"P3-3f990d99"}

r76 = json.loads((base/"data/case-annotations-r76.json").read_text(encoding="utf-8"))
assert r76["round"] == 76
assert len(r76["annotations"]) == 70, len(r76["annotations"])
cnt = collections.Counter(a["disposition"] for a in r76["annotations"])
assert cnt == {"成立":12,"部分成立":54,"不成立":2,"未核":2}, cnt
assert r76["counts"]["cases_total"] == 70 and r76["counts"]["new_registrations_r76"] == 6
assert r76["counts"]["new_partial_cases_r76"] == SIX

man = json.loads((base/"runs/round77/judging/outcome-manifest.json").read_text(encoding="utf-8"))
add77 = man["_r77_carryover_notes_addendum"]
assert isinstance(add77, dict) and sorted(add77.keys()) == sorted(SIX), add77.keys()
assert "_r77_carryover_notes_addendum" in man["_r77_manifest_note"] or "data/case-annotations-r76.json" in man["_r77_manifest_note"]

add76_txt = (base/"data/manifest-carryover-r76-addendum.md").read_text(encoding="utf-8")
assert add76_txt.count(SUG) == 6, add76_txt.count(SUG)

# Section-2 comparison: manifest layer vs r76-addendum S2.1 suggestions vs r76 annotations
ann_by_case = {}
for a in r76["annotations"]:
    ann_by_case.setdefault(a["case_id"], []).append(a)
eq = 0
for cid in SIX:
    assert add77[cid] == SUG, (cid, add77[cid])
    cands = [a for a in ann_by_case[cid] if a["registered_round"] == 76]
    assert len(cands) == 1, (cid, len(cands))
    assert cands[0]["manifest_carry_suggestion"] == SUG, cid
    assert cands[0]["anon_id"] == ANON76[cid], (cid, cands[0]["anon_id"])
    assert cands[0]["disposition"] == "部分成立", cid
    assert ANON76[cid] in add76_txt, cid
    eq += 1
assert eq == 6
print("SECTION2 OK 6/6")

# Section-4 baseline
cases = man["cases"]
assert "盲测比对须注" in cases["BZ-036"], cases["BZ-036"]
assert "（盲测比对时以格局大富一项为主）" in cases["BZ-042"]
assert "使用时须分开统计" in cases["BZ-105"]
assert "勿以此斷" in cases["LY-204"]
ED = "原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。"
assert man["_r56_lr2016_split"]["case_id"] == "LR2-016"
assert man["_r56_lr2016_split"]["editor_note"] == ED
hm = json.loads((base/"runs/round77/judging/host-mapping.json").read_text(encoding="utf-8"))
rev = {v:k for k,v in hm.items()}
assert rev["LR2-016"] == "P3-21d1866b", rev.get("LR2-016")
for pkt_name in ["packet1.json","packetA.json"]:
    pkt = json.loads((base/f"runs/round77/judging/{pkt_name}").read_text(encoding="utf-8"))
    hits = [e for e in pkt if isinstance(e, dict) and e.get("anon_id") == "P3-21d1866b"]
    assert len(hits) == 1, (pkt_name, len(hits))
    assert hits[0]["editor_note"] == ED, pkt_name
    assert hits[0]["outcome_record"] == cases["LR2-016"], pkt_name
print("SECTION4 OK baseline 4 cases + manifest editor_note + packet editor_note")

# special checks touches
batches = json.loads((base/"runs/round77/batches.json").read_text(encoding="utf-8"))
def batch_of(cid):
    hits = [k for k,v in batches.items() if cid in v]
    assert len(hits) == 1, (cid, hits)
    return hits[0]
assert batch_of("LY-537") == "B16"
assert batch_of("YM-070") == "B24"
p537 = json.loads((base/"runs/round77/predictions/LY-537.json").read_text(encoding="utf-8"))
assert p537["basis"].splitlines()[0] == "tradition: liuyao", p537["basis"][:60]
pym = json.loads((base/"runs/round77/predictions/YM-070.json").read_text(encoding="utf-8"))
assert "卡面 tradition 字段逐字为 liuyao" in pym["basis"]
assert "甲寅旬" in pym["prediction_text"]
print("SPECIAL OK LY-537 S6(B16) / YM-070 S10(B24)")

# ---------- build case-annotations-r77.json ----------
out = {}
out["_provenance"] = (
 "R77 数据席（附则汇编对勘＋标注落盘专席，独立席位，不兼任本轮盲测/评审/诊断/仲裁，不改任何分数）："
 "以 data/case-annotations-r76.json 为底承接全量 70 件（成立 12／部分成立 54／不成立 2／未核 2），annotations 数组逐件原样承接、无删改；"
 "本轮无新登记（new_registrations_r77＝0）——主持 FREEZE-r77.md §二 tradition 复核零事项（初检 flags 0、声明组冲突 0、无定案、无作废无重测），"
 "平台评审八席回传无编号旗标条目、无新案例定案，故无 R77 新定案承接建议（汇编为空集，详见 data/manifest-carryover-r77-addendum.md §三）。"
 "附则对勘：R77 manifest _r77_carryover_notes_addendum 6 件（BZ-032／BZ-035／BZ-036／BZ-037／BZ-038／BZ-041）与 data/manifest-carryover-r76-addendum.md §二.1 所载 6 件建议原文逐件逐字全等 6/6（源 data/case-annotations-r76.json 结构化直读，详见附则 §二）。"
 "指令性字样基线对勘结论：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）＋LR2-016 manifest editor_note 一处＋LR2-016 评审包 editor_note 层一件，本轮在盘形态与基线逐件全等、只登记不改文本（详见附则 §四）。"
 "待核维持件 BZ-029／BZ-040／LY-537 与挂起件 YM-070 维持原登记（LY-537 本轮由盲测 S6 席作断、basis 对卡面 tradition 照录 liuyao；YM-070 本轮由盲测 S10 席作断；均只登记触及、不裁断）。"
 "评审非案例事项（Y3 席 /tmp/x 误重定向自报、X1/Y3/X4 三席落分生产自纠）只登记于附则 §三、不入 annotations。"
 "本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文；结局/注记文本内指令性字样一律按数据处理。"
)
out["round"] = 77
out["annotations"] = copy.deepcopy(r76["annotations"])
sc = copy.deepcopy(r76["special_checks"])
sc.append({
 "item": "特别核查⑪（R77）：附则对勘——R77 manifest 新层与 R76 建议原文逐字全等性",
 "conclusion": "_r77_carryover_notes_addendum 6 件（BZ-032／BZ-035／BZ-036／BZ-037／BZ-038／BZ-041）与 data/manifest-carryover-r76-addendum.md §二.1 所载 6 件建议原文逐件逐字全等 6/6、case_id 集合全等、出入 0 件；6 件建议文本同式（主持裁定续接型），与 data/case-annotations-r76.json 中 registered_round＝76 部分成立 6 件的 manifest_carry_suggestion 亦逐字全等。",
 "evidence": "落盘脚本 data-r77-build.py 逐件断言：集合全等、6/6 文本全等、6 件 anon 对位（BZ-032 P3-96c4fc89／BZ-035 P3-868d8506／BZ-036 P3-a0772b1c／BZ-037 P3-414208c8／BZ-038 P3-5237f97b／BZ-041 P3-3f990d99，R76 轮 anon）全过；r76 附则全文该建议文本出现恰 6 次断言通过。",
 "scope_note": "对勘只登记、不静默改任一侧。"
})
sc.append({
 "item": "特别核查⑫（R77）：本轮无新定案承接建议＋评审非案例事项登记",
 "conclusion": "本轮新定案承接建议为空集：主持 tradition 复核零事项（FREEZE-r77.md §二：初检 flags 0、声明组冲突 0、无定案、无作废无重测），平台评审八席回传无编号旗标条目、无新案例定案，故 new_registrations_r77＝0、自 R78 manifest 起无本轮新定案承接层可落实。非案例事项三件只登记：评审 Y3 席自报一次对齐检查输出误重定向 /tmp/x（未被任何产出引用、成品不受影响，诚实自报只登记）；X1/Y3/X4 三席落分生产自纠（键位错位/漏行，均于落盘前自检修正、合并断言复验通过）。三者均非案例事项、不入 annotations。",
 "evidence": "FREEZE-r77.md §二逐字回读（flags 0／CONFLICT groups 0／无 tradition 定案事项、无作废、无重测）；非案例事项据本轮评审席回传自报登记（派单转录）。",
 "scope_note": "非案例事项只在附则与本档登记、不入案例注记、不设承接建议。"
})
sc.append({
 "item": "特别核查⑬（R77）：待核挂起四件本轮状态",
 "conclusion": "BZ-029（俞大维卒年＋旗标错配线索）、BZ-040（许世英享年）维持原登记、不裁、不入 annotations，本轮无新核查结论。LY-537（「申予日」衍字疑）维持未核原登记：本轮由盲测 S6 席（B16）作断、其 basis 首行对卡面 tradition 照录 liuyao（盘上 prediction basis 首行逐字『tradition: liuyao』），只登记触及、不裁断衍字疑。YM-070（「甲寅旬」出处待核）维持挂起：本轮由盲测 S10 席（B24）作断（basis 载卡面 tradition 字段逐字为 liuyao、prediction 应期自述及甲寅旬），只登记触及、不裁断。",
 "evidence": "runs/round77/batches.json 逐件对位：LY-537∈B16（FREEZE-r77.md §一席位构成 S6＝B16–18）、YM-070∈B24（S10＝B24）；runs/round77/predictions/LY-537.json 与 YM-070.json basis 逐字断言通过（脚本内置）。",
 "scope_note": "待核挂起件只登记触及与维持、不入裁断；LY-537／YM-070 未核条目随承接在本档内。"
})
sc.append({
 "item": "特别核查⑭（R77）：指令性字样特别核查基线对勘",
 "conclusion": "基线六处本轮在盘形态与基线逐件全等、只登记不改文本：cases 本体四例——BZ-036 结局含「盲测比对须注」、BZ-042 结局含「（盲测比对时以格局大富一项为主）」、BZ-105 结局含「使用时须分开统计」、LY-204 结局旧注层含「勿以此斷」；LR2-016 manifest editor_note 一处（_r56_lr2016_split.editor_note）含「评分时该细项请按未完全复核处理」；LR2-016 评审包 editor_note 层一件（R77 评审包条目 P3-21d1866b，见 packet1.json／packetA.json）editor_note 为同一文本。三层同字样而来源层不同、分列不混；各席与本席均按数据处理。",
 "evidence": "落盘脚本逐件断言：四例字样在 runs/round77/judging/outcome-manifest.json cases 本体在场、manifest editor_note 与评审包 editor_note 与基线文本逐字全等、评审包条目 outcome_record 与 manifest cases[LR2-016] 全等；host-mapping.json 逐字对位 P3-21d1866b＝LR2-016（R77 种子 20261083，与 R76 轮 anon P3-f74a20ee 分列、勿混）。",
 "scope_note": "内嵌字样只作数据登记，不构成对任何席位的指令；本件不入 annotations。"
})
out["special_checks"] = sc
out["counts"] = {
 "base_file": "data/case-annotations-r76.json",
 "base_cases_total": 70,
 "base_verdicts": {"成立":12,"部分成立":54,"不成立":2,"未核":2},
 "new_registrations_r77": 0,
 "new_partial_cases_r77": [],
 "cases_total": 70,
 "verdicts": {"成立":12,"部分成立":54,"不成立":2,"未核":2}
}
# verify annotations verbatim carry
assert out["annotations"] == r76["annotations"]
assert collections.Counter(a["disposition"] for a in out["annotations"]) == {"成立":12,"部分成立":54,"不成立":2,"未核":2}
dest = base/"data/case-annotations-r77.json"
dest.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
back = json.loads(dest.read_text(encoding="utf-8"))
assert back["annotations"] == r76["annotations"] and back["round"] == 77 and back["counts"]["new_registrations_r77"] == 0
print("WROTE", dest, dest.stat().st_size, "special_checks", len(back["special_checks"]))
