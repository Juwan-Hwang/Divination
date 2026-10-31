#!/usr/bin/env python3
# R75 数据席构建脚本：议程一（R74 承接附则编制＋R75 manifest 对勘）＋议程二（R75 旗标定案）。
# 独立席位：不改任何分数、结局原文、原卡、prediction。引文逐字断言内置、失败即停。
import json, re, collections, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
DATA = f"{BASE}/data"
R75D = f"{BASE}/runs/round75"

def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)

def fail(msg):
    raise SystemExit(f"ASSERT FAIL: {msg}")

def ain(needle, hay, label):
    if needle not in hay:
        fail(f"{label}: quote not found: {needle!r}")

def anot(needle, hay, label):
    if needle in hay:
        fail(f"{label}: unexpected string present: {needle!r}")

# ================= 议程一：R74 定案复算 + R75 manifest 对勘 + 附则编制 =================
r74 = load(f"{DATA}/case-annotations-r74.json")
anns74 = r74["annotations"]
cnt_disp = collections.Counter(a["disposition"] for a in anns74)
EXPECTED74 = {"成立": 8, "部分成立": 67, "不成立": 6, "未核": 2}
if dict(cnt_disp) != EXPECTED74:
    fail(f"r74 annotations disposition recount {dict(cnt_disp)} != {EXPECTED74}")
if r74["counts"]["verdicts"] != EXPECTED74:
    fail(f"r74 counts.verdicts {r74['counts']['verdicts']} != {EXPECTED74}")
if len(anns74) != 83 or sum(EXPECTED74.values()) != 83:
    fail("r74 total != 83")
partials74 = [a for a in anns74 if a["disposition"] == "部分成立"]
if len(partials74) != 67:
    fail("r74 partial count != 67")
for a in partials74:
    if not a.get("manifest_carry_suggestion"):
        fail(f"r74 partial {a['case_id']} empty manifest_carry_suggestion")

man75 = load(f"{R75D}/judging/outcome-manifest.json")
layer75 = man75["_r75_carryover_notes_addendum"]   # 只读该层
cases75 = man75["cases"]                            # 与 cases 载荷
if set(layer75.keys()) != {a["case_id"] for a in partials74}:
    fail("R75 layer key set != r74 partial set")
endswith_ok, full_equal, marker_cnt, mismatches = 0, 0, 0, []
for a in partials74:
    cid, sug = a["case_id"], a["manifest_carry_suggestion"]
    note = layer75[cid]
    if note.endswith(sug):
        endswith_ok += 1
    else:
        mismatches.append(cid)
    if note == sug:
        full_equal += 1
    if "[R75-addendum]" in note:
        marker_cnt += 1
if mismatches:
    fail(f"carryover endswith mismatches: {mismatches}")
print(f"[agenda1] counts dual-path OK 8/67/6/2=83; endswith {endswith_ok}/67; full-equal {full_equal}/67; marker-present {marker_cnt}/67")

def idlist(disp):
    return [a["case_id"] for a in anns74 if a["disposition"] == disp]

lines = []
lines.append("# Manifest 承接册附则（R75）——R74 定案承接建议汇编")
lines.append("")
lines.append("## 卷首说明")
lines.append("")
lines.append("- 本附则为 Phase 3 Round 75（R75）数据席（议程一：承接附则编制；与本轮盲测／评审／诊断席互不兼任）产出；汇编来源为 `benchmark/phase3/data/case-annotations-r74.json`（R74 定案正本：annotations 83 件，定案分布成立 8／部分成立 67／不成立 6／未核 2）。")
lines.append("- counts 断言结果：通过。本席以原档 `counts.verdicts` 与 `annotations[].disposition` 双路复算，均为成立 8／部分成立 67／不成立 6／未核 2、总 83，与原档 counts 逐项一致；部分成立 67 件每件 `manifest_carry_suggestion` 非空断言亦通过。")
lines.append("- 对勘结果：67/67 尾部全合（详见「对勘记录」）。对勘对象为 `benchmark/phase3/runs/round75/judging/outcome-manifest.json` 的 `_r75_carryover_notes_addendum` 层（本席只按精确文件名打开该文件、只读该层与 `cases` 载荷），逐件核验 manifest 注记以本附则转录的 `manifest_carry_suggestion` 逐字收尾；不一致者登记于对勘记录，不静默改任一侧（本轮尾部不一致 0 件）。")
lines.append("- **本附则已落实于 R75 manifest（`_r75_carryover_notes_addendum` 层）**——与 R74 附则「编成后自下一轮 manifest 起落实」的口径不同：R75 manifest 构建时已嵌入本 67 件注记，本附则为该已嵌入内容的汇编与对勘记录。")
lines.append("- 嵌入形态登记：逐件核得 67 件注记与对应 `manifest_carry_suggestion` 全文逐字相等（67/67 全等，强于尾部收尾要求）；注记中含「[R75-addendum]」分隔字样者 0 件，盘上嵌入形态为建议文本原文直入、无编辑注前缀段。此与任务单所载构造式（编辑注＋分隔字样＋建议文本）不尽一致，差异在此明示登记（详见对勘记录），附则侧与 manifest 侧均未作任何改动。")
lines.append("- **本件只汇编与对勘，不改任何分数与结局原文。**")
lines.append("- 汇编范围：R74 定案中部分成立 67 件，逐件全列于第一节（顺序照原档 `annotations` 排列）；每件的承接注记建议文本照 `case-annotations-r74.json` 该件 `manifest_carry_suggestion` 字段原文录入，不改写。每件定案要旨照原档 `finding` 字段、原旗标要旨照原档 `flag` 字段、与既有承接册／附则条目的关系照原档 `relation` 字段录入。")
lines.append("- 成立 8 件、不成立 6 件、未核 2 件不入正文逐件节，只在文末列 case_id 清单。")
lines.append("- 承接只标注、不改任何既往或本轮分数、不改结局原文、不改原卡。")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 一、部分成立件承接汇编（定案档位：部分成立，67 件，逐件全列）")
lines.append("")
for i, a in enumerate(partials74, 1):
    lines.append(f"### A{i}. {a['case_id']}")
    lines.append("")
    lines.append(f"- case_id：{a['case_id']}")
    lines.append(f"- anon_id：{a['anon_id']}")
    lines.append(f"- 定案（部分成立）：{a['finding']}")
    lines.append(f"- 原旗标要旨（照原档 `flag` 字段）：{a['flag']}")
    lines.append(f"- 承接注记建议文本（照原档 `manifest_carry_suggestion` 原文）：「{a['manifest_carry_suggestion']}」")
    lines.append(f"- 与既有承接册／附则条目的关系（照原档 `relation` 字段）：{a['relation']}")
    lines.append("")
lines.append("---")
lines.append("")
lines.append("## 二、对勘记录")
lines.append("")
lines.append("- 对勘源：`benchmark/phase3/runs/round75/judging/outcome-manifest.json` 的 `_r75_carryover_notes_addendum` 层，共 67 件。")
lines.append("- 逐件对勘：67 件 case_id 集合与本附则汇编集合全等；每件注记均以 `case-annotations-r74.json` 对应件 `manifest_carry_suggestion` 逐字收尾，67/67；且 67 件注记与建议文本全文逐字相等，67/67。")
lines.append('- 嵌入形态差异登记：任务单所载构造式为「[该例既有 editor_note（若有）] + " [R75-addendum] " + manifest_carry_suggestion」；盘上实际注记无该分隔字样、无编辑注前缀段（计数：含「[R75-addendum]」者 0 件、与建议文本全文相等者 67 件）。尾部收尾核验不受影响（67/67）；此差异只登记，不改任一侧。')
lines.append("- 不一致登记：尾部不一致 0 件；附则侧与 manifest 侧均未作任何改动（不静默改任一侧）。")
lines.append("- 勘误：无。")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 三、不入正文清单（照 R74 定案档位）")
lines.append("")
lines.append(f"- 成立 8 件：{'／'.join(idlist('成立'))}")
lines.append(f"- 不成立 6 件：{'／'.join(idlist('不成立'))}")
lines.append(f"- 未核 2 件：{'／'.join(idlist('未核'))}")
lines.append("")
with open(f"{DATA}/manifest-carryover-r75-addendum.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("[agenda1] addendum written")

# ================= 议程二：R75 旗标普查、去重、定案 =================
SEATS = ["X1", "X2", "X3", "X4", "Y1", "Y2", "Y3", "Y4"]
EXPECTED_ITEMS = {"X1": 10, "X2": 5, "X3": 10, "X4": 11, "Y1": 5, "Y2": 7, "Y3": 9, "Y4": 15}
flags_text, item_counts, anon_mentions = {}, {}, []
ANON_RE = re.compile(r"P3-[0-9a-f]{8}")
for s in SEATS:
    t = open(f"{R75D}/judging/FLAGS-{s}.md", encoding="utf-8").read()
    flags_text[s] = t
    item_counts[s] = len(re.findall(r"(?m)^\d+\.", t))
    if item_counts[s] != EXPECTED_ITEMS[s]:
        fail(f"FLAGS-{s} numbered items {item_counts[s]} != expected {EXPECTED_ITEMS[s]}")
    for a in ANON_RE.findall(t):
        anon_mentions.append((s, a))
if sum(item_counts.values()) != 72:
    fail("numbered items total != 72")
if len(anon_mentions) != 98:
    fail(f"anon mentions {len(anon_mentions)} != 98")
FLAGS_ALL = "\n".join(flags_text[s] for s in SEATS)

hostmap = load(f"{R75D}/judging/host-mapping.json")
revmap = {v: k for k, v in hostmap.items()}
seat_cases = collections.defaultdict(list)   # case_id -> [(seat, anon)]
for s, a in anon_mentions:
    if a not in hostmap:
        fail(f"anon {a} not in host-mapping")
    seat_cases[hostmap[a]].append((s, a))
if len(seat_cases) != 63:
    fail(f"distinct judge-flag cases {len(seat_cases)} != 63")

# 历轮定案档（逐号精确打开；r52 盘上不存在、登记）
missing_rounds = []
prior_files = {}
for r in range(49, 75):
    p = f"{DATA}/case-annotations-r{r}.json"
    if not os.path.exists(p):
        missing_rounds.append(r)
        continue
    prior_files[r] = load(p)
if missing_rounds != [52]:
    fail(f"missing prior rounds {missing_rounds} != [52]")

def prior_entries(cid):
    out = []
    for r in sorted(prior_files):
        for a in prior_files[r].get("annotations") or []:
            if a["case_id"] == cid:
                out.append((r, a))
    return out

def latest_prior(cid):
    es = prior_entries(cid)
    return es[-1] if es else (None, None)

man74 = load(f"{BASE}/runs/round74/judging/outcome-manifest.json")
man73 = load(f"{BASE}/runs/round73/judging/outcome-manifest.json")
MAN_BY_ROUND = {73: man73, 74: man74, 75: man75}

def outcome_of(cid, rnd=75):
    return MAN_BY_ROUND[rnd]["cases"][cid]

def pred_of(cid):
    return load(f"{R75D}/predictions/{cid}.json")

def card_dump(cid):
    return json.dumps(load(f"{BASE}/inputs-dev12/{cid}.json"), ensure_ascii=False)

def quote_src(cid, src):
    if src == "flags":
        return FLAGS_ALL
    if src == "outcome":
        return outcome_of(cid)
    if src == "pred_text":
        return pred_of(cid)["prediction_text"]
    if src == "pred_all":
        p = pred_of(cid)
        return p["prediction_text"] + "\n" + p.get("basis", "")
    if src == "card":
        return card_dump(cid)
    fail(f"unknown quote source {src}")

# ---- 逐件表：(case_id, kind, expected_disposition, flag_text, [(quote, source)...], note_text_or_None, [(note_quote, source)...])
# kind: carry=同旨续接 / newgist=同例新旨 / new=新旗标 / pending=待核维持
CASES = [
 ("AS-008","carry","部分成立","X3：结局自注年份歧（史实 1643 与 OCR 1644）",[("1643（史实）与 OCR 1644","flags")],None,[]),
 ("AS-015","carry","部分成立","X3：结局仅载问者本人死日，夫存亡与归讯未载；Y3：同图兼断例，结局仅载问者本人死日，主断无从印证",[("结局仅载问者本人死日","flags")],None,[]),
 ("BQ-001","carry","部分成立","Y4：结局正文止于父气尽复苏自述，死亡时点须靠 carry 承接的 stripped_tail 后断才可核，正文自身不完整",[("正文自身不完整","flags")],None,[]),
 ("BQ-025","carry","部分成立","X3：结局止于占后半日即时记载，养蜂终局未载",[("养蜂终局未载","flags")],None,[]),
 ("BZ-304","carry","部分成立","Y2：结局末句引述「5-6月恢复正常」不见于本轮 prediction_text 全文（carry 已标注原始出处未载）",[("5-6月恢复正常","flags")],None,[]),
 ("LR2-020","carry","不成立","X1：outcome_record「男女五人被盗而死」与占者一行的对应关系未明载",[("男女五人被盗而死","flags"),("男女五人被盗而死","outcome")],None,[]),
 ("LR2-022","carry","部分成立","Y4：结局终句「果三日死」主语文本未明示，本座位按 carry 注记以本案病弟断面读",[("果三日死","flags"),("果三日死","outcome")],None,[]),
 ("LR2-023","carry","部分成立","X4：outcome_record 混载儿妇妊性别与澹宁壬午春死，与 prediction 所占本人病断面不完全同面；Y4：结局以「后果然」总承本病断面，又载澹宁壬午春死，与本病愈迟断面的时距关系不明",[("澹宁壬午春死","flags")],None,[]),
 ("LR3-101","carry","部分成立","Y1：主问断面在结局中无独立记载——中否仅以补官间接对应",[("中否仅以补官间接对应","flags")],
   "本轮 Y1 旗标所指中否仅以补官间接对应一层，与历轮旧旨（会试中否未明字、仅以补官间接对应）同旨，该旨定案部分成立与 R66 新旨并行承接、档位不变。",
   [("后补刑部主政，恬退不仕。","outcome")]),
 ("LR3-112","carry","部分成立","X2：prediction 只断刘一纯之病可愈，outcome_record 主体载贼入室被获（陈忠）等节，病面结局缺位（结局内已自注病断后续未载）；Y2：outcome_record 主载贼入室被获一节，所占病面结局缺位（原文自注病断后续未载）",[("病面结局缺位","flags")],None,[]),
 ("LY-023","carry","成立","X3：所断母病、结局为其子惊风（断面迁移例，carry_note 已自注）；Y3：大师自标迁移例——结局对应其子惊风，与 prediction 所问面（母病）不对位，所问面结局未载",[("结局为其子惊风","flags")],None,[]),
 ("LY-025","carry","部分成立","Y2：carry_note 历轮旧旨对 prediction 方向/模板的描述与本轮 prediction_text 实际口径不合，carry_note 内部已自注此点",[("与本轮 prediction_text 实际口径不合","flags")],
   "另本轮核明：逐字核 R75 prediction_text 作晴向终局（『終局（主斷）：可放晴』）、全文无 negative 表述，Y2 旗标所指 carry 旧旨口径不合一层与 R63 新旨同旨、并行承接、档位不变。",
   [("終局（主斷）：可放晴","pred_text")]),
 ("LY-036","carry","部分成立","X3：carry_note 内部口径冲突——R71 标注称 prediction「不报方向」，R72 标注又称其与 prediction_text 实含方向断口径不合；Y3：carry_note 内部口径冲突——R72 注称「prediction 不报方向」，但本轮 prediction_text 实含方向断",[("carry_note 内部口径冲突","flags")],
   "另本轮核明：逐字核 R75 prediction_text 明载『傾向可升選（positive 傾向、置信低）』方向断，X3／Y3 所指 carry_note 内部口径冲突一层与 R71 新旨同旨、并行承接、档位不变。",
   [("傾向可升選（positive 傾向、置信低）","pred_text")]),
 ("LY-104","carry","部分成立","X4：carry 注明病灶与手术有载、愈否终局未载；Y4：结局仅载病灶（胸部肿瘤）与戌日手术，愈否终局未载",[("愈否终局未载","flags")],None,[]),
 ("LY-204","carry","部分成立","Y4：一组结局后半混入断法通则或应验解释层之例（P3-c2010fd9），个案事实明载于前半，只按事实层计分、通则层不计",[("通则层不计","flags")],None,[]),
 ("LY-205","carry","部分成立","X4：carry 注明禄面有载、财面未载，prediction 为求财断、结局载午年保举得官，两面错位；Y4：结局禄面有载、财面未载，与预测断面错位",[("禄面有载、财面未载","flags")],None,[]),
 ("LY-206","carry","成立","Y2：outcome_record 仅载死亡断面（巳月生疮、酉月卒），所问终身财福面无对应记录，carry_note 已多轮标注此断面缺位",[("终身财福面无对应记录","flags")],None,[]),
 ("LY-207","carry","部分成立","Y2：carry_note 历轮旧旨对 prediction 方向/模板的描述与本轮 prediction_text 实际口径不合，carry_note 内部已自注此点",[("与本轮 prediction_text 实际口径不合","flags")],
   "另本轮核明：逐字核 R75 prediction_text 仍为功名向主断（『終局（主斷）：可成/得升得補』）、全文无病向表述，Y2 旗标所指 carry 旧旨口径不合一层与 R69 新旨同旨、并行承接、档位不变。",
   [("終局（主斷）：可成/得升得補","pred_text")]),
 ("LY-212","carry","成立","X3：索债本问在原书无结局、结局为所避江难实况；Y3：大师自标趋避例——结局对应所避江难实况，与 prediction 所问面（索债）不对位，所问面结局未载",[("结局为所避江难实况","flags")],None,[]),
 ("LY-216","carry","部分成立","X1：outcome_record 为妇人转述的反问句，结果嵌于问句、无独立终局叙述，carry_note 历轮亦同旨登记",[("结果嵌于问句","flags")],None,[]),
 ("LY-218","carry","部分成立","X1：同一 prediction 文件内含两占且终局相反（主断寿元有根基、次断寿元受损），结局父健母终双面并载；Y1：同一 prediction 内主斷与再占次盤终局方向相反，结局父健、母终于子年分载两面",[("终局相反","flags")],
   "另本轮核明：逐字核 R75 prediction 全文，主断『壽元尚有根基、近期無大厄』与再占次盘『壽元受損、防沖克之期有厄』两占终局方向相反并陈，结局父健母终双面分载——两占并陈与双面分载已在既有双占合载定案内，本轮并行登记、档位不变。",
   [("壽元尚有根基、近期無大厄","pred_text"),("壽元受損、防沖克之期有厄","pred_text")]),
 ("LY-220","carry","部分成立","X3：结局为他人功名记载、和好面未载；Y3：结局只载兄弟功名等事，和好面未载，主断无从印证",[("和好面未载","flags")],None,[]),
 ("LY-222","carry","成立","X2：prediction 断子嗣之望，outcome_record 为父子相逢（失散见归面），断面错位（carry_note 已注大师改断面）",[("大师改断面","flags")],None,[]),
 ("LY-240","carry","部分成立","X3：总承式结局、断面未分载——结局仅「果於辰日」；Y3：总承式结局（「果於辰日」），事件断面未分载，claims 无法逐条满分核验",[("果於辰日","flags"),("果於辰日","outcome")],None,[]),
 ("LY-252","carry","部分成立","X4：合并登记结局尾句为应验解释层或断法通则混入之例（含 LY-252），只取个案事实层计分；Y4：一组结局后半混入断法通则或应验解释层之例（P3-c0796247），个案事实明载于前半",[("LY-252","flags")],None,[]),
 ("LY-418","carry","部分成立","X3：结局疑似截断（以逗号收尾），carry_note 亦有同注",[("LY-418","flags")],None,[]),
 ("LY-425","carry","部分成立","X3：问面与结局名目有别——所问为「得缺」、结局为「沒有中榜」，carry_note 已注结局对应功名总断",[("沒有中榜","flags")],None,[]),
 ("LY-426","carry","成立","X3：开店得利面无记载、结局为旁及官非断面；Y3：结局只载其子赌博送官杖死，与 prediction 所问面（开店贸易利否）完全不对位，所问面结局未载",[("开店得利面无记载","flags")],None,[]),
 ("LY-430","carry","成立","X2：prediction 断掣签到任，outcome_record 为病死断面、到任面无记载（carry_note 已注两占合断＋危灾断面对应）；Y2：outcome_record 对应再占危灾断面（病死），prediction 主断的掣签到任面无记载",[("掣签到任面无记载","flags")],None,[]),
 ("LY-432","carry","不成立","Y1：结局「五月高遷。次日卽愈。」似合载两事（高迁与愈），本例 prediction 仅及功名一面，只按功名面计分",[("次日卽愈","flags"),("五月高遷。 次日卽愈。","outcome")],None,[]),
 ("LY-433","carry","成立","X3：功名面无记载、结局仅载其子未年而死",[("功名面无记载、结局仅载其子未年而死","flags")],None,[]),
 ("LY-436","carry","成立","X3：prediction 为天时晴燥断、结局为午年子月而死的人身寿元断面；Y3：结局只载午年子月有人死，与 prediction 所问面（本月天时晴雨）完全不对位，所问面结局未载",[("人身寿元断面","flags")],None,[]),
 ("LY-437","carry","成立","X3：所问小厮病、结局为占者本人革职（断面迁移例，carry_note 已自注）；Y3：大师自标迁移例——结局对应占者本人革职，与 prediction 所问面（小厮病）不对位，所问面结局未载",[("结局为占者本人革职","flags")],None,[]),
 ("LY-441","carry","部分成立","X2：outcome_record「星辰無光」晴否判定含混（carry_note 已登记）；Y2：outcome_record「果於戌時，星辰無光」晴否判定含混（carry_note 已标注）",[("星辰無光","flags")],None,[]),
 ("LY-445","carry","部分成立","X3：结局仅干支日记录——亥日未载、机理类子断语无从逐条核验（carry_note 已注）",[("亥日未载","flags")],None,[]),
 ("LY-452","carry","部分成立","X3：结局以逗号收尾疑似截断，北来焚村明载，但本人避往方位与安否未载；Y3：结局以逗号收尾疑似截断；北来焚村明载，但本人避往方位与安否未载",[("北来焚村明载","flags")],None,[]),
 ("LY-458","carry","成立","Y3：结局仅载「在外平安」，所问母来否结果未载，归断无从印证",[("母来否结果未载","flags")],None,[]),
 ("LY-504","carry","部分成立","X1：outcome_record 记载对象为将军之侄被拿问，与 prediction 主问（本人升迁）断面错位，升迁结果未直接记载；Y1：结局对应防刑狱断面，主问断面无独立记载",[("将军之侄被拿问","flags")],None,[]),
 ("LY-506","carry","部分成立","X1：两占合载，结局「果死于卯日」的死亡归属未明字（carry_note 历轮同旨）；Y1：结局「果死於卯日」之死亡归属（母／子）在结局原文中未明字（carry_note 历轮同此登记）",[("死亡归属","flags")],None,[]),
 ("LY-508","carry","成立","X4：carry 注明所问终身财福、结局仅载丑年死亡、财福面无独立记载；Y4：所问终身财福，结局仅载丑年死亡，财福面无独立记载（carry 已登记）",[("财福面无独立记载","flags")],None,[]),
 ("LY-510","carry","部分成立","Y1：结局对应再问遍游，主问断面无独立记载（仅侧面／间接对应）",[("结局对应再问遍游","flags")],None,[]),
 ("LY-513","carry","成立","X1：间接验证例——结局仅记病终，prediction 的终身功名断语无对应结局事件可核；Y1：功名断语无对应结局事件，主问断面无独立记载",[("终身功名断语无对应结局事件","flags")],None,[]),
 ("LY-516","carry","部分成立","X4：合并登记结局尾句为应验解释层或断法通则混入之例（含 LY-516），只取个案事实层计分；Y4：一组结局后半混入断法通则或应验解释层之例（P3-db09fb3b），个案事实明载于前半",[("LY-516","flags")],None,[]),
 ("LY-529","carry","部分成立","X2：prediction 单断坟地形势不佳，outcome_record 为「一一皆是」总承＋「二子皆发科甲」——总承与发科甲实绩与「地不佳」单断之间存在张力且断语未分载，本席标为本轮新见张力；Y2：outcome_record 内部张力——「一一皆是」总承与实绩并存，后者与 prediction 的坟地不佳方向相左",[("总承与发科甲实绩","flags")],
   "另本轮核明：X2／Y2 所指总承与发科甲实绩对负向单断之核验张力一层——结局『一一皆是，葬后未出三年，二子皆发科甲．』中发科甲实绩明载已在既有定案登记、总承未分载即既有旨本身，方向落差属评分面，与既有定案同域、并行登记、档位不变。",
   [("一一皆是，葬后未出三年，二子皆发科甲．","outcome")]),
 ("LY-531","carry","部分成立","X1：结局仅侧载「午月中途过害」，仆人归否未明载，prediction 的即归断无从成立；Y1：归否未明载，主问断面无独立记载",[("仆人归否未明载","flags")],None,[]),
 ("LY-533","carry","部分成立","X3：所断房价、结局为覆舟而亡、房价面无验；Y3：卡面自注「占此应彼」——所问索房价，结局对应人身祸福（午月覆舟亡），房价面无验",[("房价面无验","flags")],None,[]),
 ("LY-536","carry","部分成立","Y4：一组结局后半混入断法通则或应验解释层之例（P3-c247b1bf），个案事实明载于前半，只按事实层计分",[("P3-c247b1bf","flags")],None,[]),
 ("LY-540","carry","部分成立","X3：结局疑似截断（以逗号收尾），carry_note 亦有同注",[("LY-540","flags")],None,[]),
 ("LY-613","carry","部分成立","X1：carry_note 指出 prediction 爻位处含「?」占位字样一处（主体断语完整可读），不影响核验",[("占位字样一处","flags")],
   "另本轮核明：逐字核 R75 prediction 全文（prediction_text 与 basis），本轮不在场之字样为半角与全角问号（断言另见脚本），X1 旗标所报为 carry 旧注口径，字样层本轮不在场、注记层一层并行登记、档位不变（同 R71 口径）。",
   []),
 ("LY-614","carry","部分成立","X4：carry 注明兄病终局未载，outcome_record 仅载「戊申日沈屙復起」并以反问收束；Y4：结局以反问语收束，仅载戊申日沉屙复起，兄病最终结局未载（carry 已登记）",[("兄病终局未载","flags"),("戊申日沈屙復起","outcome")],None,[]),
 ("LY-627","carry","部分成立","X3：结局指代不明——「果至其日而死」之「其日」在 outcome_record 内无先行指代",[("其日","flags"),("果至其日而死","outcome")],
   "本轮 X3 旗标所指『其日』指代未明一层，与 R57／R61／R64 旧旨同旨、该旨定案不成立照旧承接；本例现行档位为 R65 新旨（结局尾句应验解释层）部分成立，两旨并行不悖、档位不变。",
   [("果至其日而死","outcome")]),
 ("LY-628","carry","部分成立","X4：carry（R73 新旨）注明结局受杖责主体未明字、胜负方向读法受影响；Y4：结局「果被杖责」受责主体未明字，胜负方向读法受影响（carry R73 新旨已登记）",[("受杖责主体未明字","flags"),("果被杖責","outcome")],None,[]),
 ("LY-629","carry","部分成立","X1：结局为总承式且系「改向之后」应验，原问坟地吉凶未独立分载；Y1：总承式结局且系改向后应验，主问断面无独立记载",[("改向之后","flags")],None,[]),
 ("OC-029","carry","部分成立","X4：carry 注明求官面未载、余诸事面有载；Y4：结局多断面混载，求官面未载（carry 附注已登记），预测主断面无从核验",[("求官面未载","flags")],None,[]),
 ("YM-030","carry","部分成立","X4：carry 注明『复完胎』语义未明、胎终局判定存疑；Y4：结局「败血三日后复完胎」中「复完胎」语义未明，胎终局判定存疑（carry 已登记）",[("复完胎","flags"),("败血三日后复完胎","outcome")],None,[]),
 ("YY-006","carry","部分成立","X4：outcome_record 为总承式收束（「年月日悉符其占」），逐条子断语与逐项时点无分项记载；Y4：结局三事明载，但具体年月日以「悉符其占」总承收束，无逐项可核时点（carry 已登记）",[("悉符其占","flags"),("年月日悉符其占","outcome")],None,[]),
 ("YY-022","carry","部分成立","X3：总承式结局、断面未分载——结局仅「后果然」；Y3：总承式结局（「后果然」），事件断面未分载",[("后果然","flags"),("后果然","outcome")],None,[]),
 ("YY-023","carry","部分成立","X4：outcome_record 为总承式收束（「后果然」），逐条子断语与逐项时点无分项记载；Y4：结局仅「后果然」总承，断面未分载，claims 不得满分",[("后果然","flags"),("后果然","outcome")],None,[]),
 ("YY2-004","carry","部分成立","X1：prediction 为残损登记、明言无据可断、不定方向不报应期——属弃断条目；Y1：prediction 自明盘面残损、本卦名与六爻不可复原，明确不报方向与应期——属弃断登记",[("属弃断","flags")],None,[]),
]

CASES += [
 ("LY-035","new","部分成立","X3：结局措辞内部张力——outcome_record 作「果驗，己亥日到家」，「果驗」字样与本轮 prediction「未歸/短期不至」方向相反并存，究竟所验为何断无从由结局原文判定",
   [("果驗，己亥日到家","flags")],
   "新旗标（R75 新立）：回原卡——所问「占父何日歸」；逐字核 R75 prediction 全文，主断作『未歸/短期不至』、主坐标为寅日；R75 manifest 结局仅『果驗，己亥日到家』——归家终局与己亥日时点均明载，但『果驗』二字所指为何断，结局原文未分载：本轮 prediction 之方向（未归）与时点（寅日）均与结局相反，『果驗』若指原书原断，其断语不在本例结局内，所指含混一层属实；方向与时点落差本身属评分面。故部分成立。",
   [("占父何日歸","card"),("未歸/短期不至","pred_text"),("果驗，己亥日到家","outcome")]),
 ("LY-227","newgist","部分成立","Y4：其一——prediction_text 内主断（可中）与再占次盘（难中）方向相反并陈，以主断为主、次盘相抵扣 claims；其二——一组结局后半混入断法通则或应验解释层之例（P3-fc427e92），个案事实明载于前半；X4：合并登记结局尾句为应验解释层或断法通则混入之例（含 LY-227）",
   [("方向相反并陈","flags"),("LY-227","flags")],
   "同例新旨（R62 旧旨为『结局后半混入断法通则』、定案部分成立，本轮新旨与之各旨独立、并行不悖）：逐字核 R75 prediction 全文——主断作『終局（主斷）：可中/有望入選』、再占次盘作『終局（再占/次盤）：難中/此次落空』，两占终局方向相反并陈属实，核验须分面；但结局『果得成名。』明载、与主断面直接对应，再占面无独立结局分载系两占结构本身、非记录缺位。故部分成立。",
   [("終局（主斷）：可中/有望入選","pred_text"),("終局（再占/次盤）：難中/此次落空","pred_text"),("果得成名。","outcome")]),
 ("BZ-019","newgist","部分成立","盲测席：卡面 setting 含「盲测时不得给身份」指令性字样，触及原卡与结局记录（按数据处理、未服从）",
   [("盲测时不得给身份","card")],
   "同例新旨（R61 旧旨为『prediction 称谓与传主帝王身分出入』、定案部分成立，本轮新旨与之各旨独立、并行不悖）：盲测席旗标指卡面 setting 含指令性字样——逐字回读原卡，setting 明载『盲测时不得给身份』，字样在卡面属实；但该字样系本例盲测设计本身的身份 withheld 指示，R61 定案已明载此节，逐字核 R75 prediction 全文（prediction_text 与 basis）均未见身份字样、无身份被给之实，结局转引口径如旧。各席与本席均按数据处理、未以该字样为指令。故部分成立。",
   [("盲测时不得给身份","card")]),
 ("LY-537","pending","未核","盲测席：卡面逐爻表 OCR 行序错乱、逐爻装卦未能可靠还原，提示行序风险（卡面已自注、逐爻表不录）",
   [("逐爻裝卦未能可靠還原","card")],
   "待核维持（本轮旗标触及、只登记不裁）：盲测席旗标登记卡面逐爻表 OCR 行序错乱风险——逐字回读原卡 chart_note 明载逐爻装卦表经 OCR 转录后行序错乱、『逐爻裝卦未能可靠還原』、本条逐爻表不录，触及属实；逐字回读 R75 结局原文确作『果于申予日归』。本例维持 R68 未核原登记（『申予日』措辞待核、无盘外独立史源不裁，承 R56／R57／R61／R64／R67／R68／R72／R74 链），本轮只登记触及、不入裁断。",
   [("逐爻裝卦未能可靠還原","card"),("行序錯亂","card"),("果于申予日归","outcome")]),
 ("YM-070","pending","未核","X4：carry 注明结局『都下』语义未明，outcome_record「后果同行都下」只能确认「同行」二字，其余语义无法确核；Y4：结局「后果同行都下」中「都下」语义未明（carry 已登记待核），同行方向可读、余义不可核",
   [("后果同行都下","flags")],
   "待核维持（本轮旗标触及、只登记不裁）：X4／Y4 旗标登记结局『都下』语义未明、待核——逐字回读 R75 结局原文确作『后果同行都下。』，触及属实；本例维持 R71 未核原登记（『都下』语义未明＋『甲寅旬』出处待核并列、无盘外独立史源不裁），挂起维持，本轮只登记触及、不入裁断。",
   [("后果同行都下。","outcome")]),
]

SUGGESTIONS = {
 "LY-227": "同例新旨：自 R76 起承接本 R75 标注（与 R62 通则混入旧旨并行）：按「prediction 两占终局方向相反并陈、结局『果得成名』明载对应主断面」登记；结局原文照录不改。",
 "BZ-019": "同例新旨：自 R76 起承接本 R75 标注（与 R61 称谓出入旧旨并行）：按「卡面 setting 含『盲测时不得给身份』字样、系盲测 withheld 设计、prediction 未受身份提示」登记；结局原文照录不改。",
 "LY-035": "同旨新立：自 R76 起承接本 R75 标注：按「结局『果驗』所指未分载、归家终局与己亥日时点明载」登记；结局原文照录不改。",
 "LY-537": "待核维持：自 R76 起维持原登记（『申予日』措辞待核、无盘外独立史源不裁）；结局原文照录不改。",
 "YM-070": "待核维持：自 R76 起维持原登记（『都下』语义未明＋『甲寅旬』出处待核、挂起维持、无盘外独立史源不裁）；结局原文照录不改。",
}
RELATIONS = {
 "LY-227": "同例新旨（R62 旧旨并行）",
 "BZ-019": "同例新旨（R61 旧旨并行）",
 "LY-035": "新旗标（R75 新立）",
 "LY-537": "待核维持（旗标触及、只登记不裁）",
 "YM-070": "待核维持（旗标触及、只登记不裁）",
}

annotations = []
for (cid, kind, disp, flag_text, quotes, note, note_quotes) in CASES:
    # 引文逐字断言（旗标层）
    for (q, src) in quotes:
        ain(q, quote_src(cid, src), f"{cid} flag quote [{src}]")
    for (q, src) in note_quotes:
        ain(q, quote_src(cid, src), f"{cid} note quote [{src}]")
    # 结局跨轮全等断言（承接前提）
    if outcome_of(cid, 75) != outcome_of(cid, 74):
        fail(f"{cid}: R75 outcome != R74 outcome")
    seats = sorted({s for (s, a) in seat_cases.get(cid, [])})
    # X4 第 11 条以 case_id 点名 LY-252／LY-516／LY-227（无 anon），补记来源席
    if cid in ("LY-252", "LY-516", "LY-227"):
        seats = sorted(set(seats) | {"X4"})
    lr, la = latest_prior(cid)
    if kind in ("carry", "newgist"):
        if la is None:
            fail(f"{cid}: expected prior annotation, none found")
        if la["disposition"] != disp:
            fail(f"{cid}: latest prior disposition {la['disposition']} != expected {disp}")
        if outcome_of(cid, 75) != MAN_BY_ROUND[lr]["cases"][cid]:
            fail(f"{cid}: R75 outcome != R{lr} outcome")
        finding = f"承接既有定案不重裁（历轮最近定案 R{lr} {disp}）：" + la["finding"]
        if note:
            finding += " " + note
        finding += " 本轮（R75）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。"
        suggestion = SUGGESTIONS.get(cid, f"同旨续接：自 R76 起承接 R{lr}＋本 R75 标注；结局原文照录不改。")
        relation = RELATIONS.get(cid, f"同旨续接（R{lr}）")
    elif kind == "new":
        if la is not None:
            fail(f"{cid}: marked new but prior annotation exists at R{lr}")
        finding = note
        suggestion = SUGGESTIONS[cid]
        relation = RELATIONS[cid]
    elif kind == "pending":
        finding = note
        suggestion = SUGGESTIONS[cid]
        relation = RELATIONS[cid]
    else:
        fail(f"unknown kind {kind}")
    if disp == "部分成立" and not suggestion:
        fail(f"{cid}: partial without suggestion")
    sources = [f"divination/benchmark/phase3/inputs-dev12/{cid}.json"]
    for s in seats:
        sources.append(f"divination/benchmark/phase3/runs/round75/judging/FLAGS-{s}.md")
    sources.append(f"divination/benchmark/phase3/runs/round75/judging/outcome-manifest.json cases[{cid}]")
    sources.append(f"divination/benchmark/phase3/runs/round75/predictions/{cid}.json")
    for (r, _a) in prior_entries(cid):
        sources.append(f"divination/benchmark/phase3/data/case-annotations-r{r}.json {cid} 条")
    annotations.append({
        "anon_id": revmap[cid],
        "case_id": cid,
        "disposition": disp,
        "finding": finding,
        "flag": flag_text,
        "manifest_carry_suggestion": suggestion,
        "relation": relation,
        "registered_round": 75,
        "sources_checked": sources,
        "source_seats": seats if seats else ["盲测席"],
    })

# LY-613 字样层本轮不在场断言（半角/全角问号）
_p613 = pred_of("LY-613")
anot("?", _p613["prediction_text"] + _p613.get("basis", ""), "LY-613 pred_all")
anot("？", _p613["prediction_text"] + _p613.get("basis", ""), "LY-613 pred_all")
# BZ-019 身份字样未入 prediction 断言
_p19 = pred_of("BZ-019")
anot("乾隆", _p19["prediction_text"] + _p19.get("basis", ""), "BZ-019 pred_all")
anot("弘历", _p19["prediction_text"] + _p19.get("basis", ""), "BZ-019 pred_all")
anot("弘曆", _p19["prediction_text"] + _p19.get("basis", ""), "BZ-019 pred_all")

# BQ-013 锚点核查：X4 第 11 条以其 anon 为序位起点、未对本例提出主张；结局无通则/解释层混入
if outcome_of("BQ-013") != "「雨果不止」——雨果然连绵不止。":
    fail("BQ-013 outcome changed")
annotated_ids = {a["case_id"] for a in annotations}
if "BQ-013" in annotated_ids:
    fail("BQ-013 must not be annotated")
if annotated_ids != (set(seat_cases.keys()) - {"BQ-013"}) | {"BZ-019", "LY-537"}:
    fail(f"annotated set mismatch: extra={annotated_ids - set(seat_cases.keys())} missing={set(seat_cases.keys()) - annotated_ids}")
if len(annotations) != 64 or len(annotated_ids) != 64:
    fail(f"annotations total {len(annotations)} != 64 (dedupe)")

annotations.sort(key=lambda a: a["anon_id"])
verdicts = dict(collections.Counter(a["disposition"] for a in annotations))
EXPECTED75 = {"成立": 12, "部分成立": 48, "不成立": 2, "未核": 2}
if verdicts != EXPECTED75:
    fail(f"R75 verdicts {verdicts} != {EXPECTED75}")
kind_counts = collections.Counter(k for (_c, k, *_r) in CASES)
if dict(kind_counts) != {"carry": 59, "newgist": 2, "new": 1, "pending": 2}:
    fail(f"kind counts {dict(kind_counts)}")
for a in annotations:
    if a["disposition"] == "部分成立" and not a["manifest_carry_suggestion"]:
        fail(f"{a['case_id']}: partial missing suggestion (final sweep)")

counts75 = {
    "judge_flag_numbered_items_total": 72,
    "judge_flag_numbered_items_by_seat": EXPECTED_ITEMS,
    "judge_flag_anon_mentions_total": 98,
    "judge_flag_anons_total": 63,
    "judge_flag_cases_total": 63,
    "judge_flag_cases_annotated": 62,
    "judge_flag_anchor_only_cases": 1,
    "blind_seat_flag_cases": 2,
    "host_tradition_flags_total": 24,
    "host_tradition_in_scope_cases": 0,
    "cases_total": 64,
    "continuation_cases": 59,
    "same_case_new_gist_cases": 2,
    "new_flag_cases": 1,
    "pending_touch_cases": 2,
    "verdicts": verdicts,
}
# 双路复算：counts 与 annotations 逐项对账
if dict(collections.Counter(a["disposition"] for a in annotations)) != counts75["verdicts"]:
    fail("counts dual-path mismatch")
if counts75["continuation_cases"] + counts75["same_case_new_gist_cases"] + counts75["new_flag_cases"] + counts75["pending_touch_cases"] != counts75["cases_total"]:
    fail("classification totals do not reconcile")

provenance75 = (
    "R75 数据席（旗标定案专席，独立席位，不兼任本轮盲测/评审/诊断，不改任何分数）逐件回源核查 R75 八席评审旗标 72 条编号条目"
    "（X1 10／X2 5／X3 10／X4 11／Y1 5／Y2 7／Y3 9／Y4 15，盘上逐号点数与各席回报逐项一致）／98 次 anon 出现、经 host-mapping.json 解析去重为 63 anon／63 例，"
    "另加盲测席触及结局记录与原卡之旗标 2 例（BZ-019／LY-537），合计入案 64 例。其中 X4 第 11 条以 P3-e7317eba（BQ-013）为序位起点合并登记结局通则／解释层混入诸例、未对 BQ-013 本例提出主张，"
    "本席逐字核其结局『「雨果不止」——雨果然连绵不止。』无通则／解释层混入，BQ-013 不入案、只在此登记；该条所举实例 LY-252／LY-516／LY-227 与 Y4 第 15 条所举 LY-204／LY-536 均已各按 anon 入案。"
    "逐件回 benchmark/phase3/inputs-dev12/<case_id>.json 原卡、runs/round75/predictions/<case_id>.json 预测原文、runs/round75/judging/outcome-manifest.json cases 载荷"
    "（落笔前回读本例结局原文，引文逐字断言内置于落盘脚本 data_r75_build.py），并与历轮定案档（data/case-annotations-r49.json 至 -r74.json 逐号精确打开；r52 号文件盘上不存在、已登记）核对承接关系："
    "59 件为同旨续接（只承接不重裁），同例新旨 2 件（LY-227 两占方向相反并陈、BZ-019 卡面指令性字样），1 件为 R75 新立（LY-035『果驗』所指未分载、部分成立），"
    "另待核维持件 LY-537 与挂起件 YM-070 本轮被旗标触及、只登记触及以未核入案（BZ-029／BZ-040 未被触及、不入本件）。R75 各例结局文本经脚本断言与 R74 manifest 逐件全等（64/64），承接件另与各自历轮最近定案轮 manifest 全等。"
    "边界登记：主持 tradition 检查 24 件旗标已于冻结时裁定（runs/round75/FREEZE-r75.md 第二节：24/24 均属检查器关键词覆盖缺口、卡面确无 tradition/system 字段、实效归 none-labelled），不在本标注范围、未入 annotations，仅在此记边界。"
    "指令性字样特别核查：BZ-019 卡面 setting 含『盲测时不得给身份』字样，已按同例新旨定案（字样属实、系盲测 withheld 设计、prediction 未受身份提示）；卡面／结局／prediction 内字样一律按数据处理、本席未服从任何内嵌指令。"
    "本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文。"
)

special75 = [
    {"item": "特别核查①：待核维持件（BZ-029／BZ-040／LY-537）与挂起件（YM-070）状态登记",
     "conclusion": "BZ-029／BZ-040 本轮未被任何旗标触及，不入 annotations、维持各自原登记。LY-537 本轮被盲测席旗标触及（卡面逐爻表 OCR 行序风险），YM-070 被 X4／Y4 旗标触及（『都下』语义未明），均只登记触及、维持未核原登记入案。",
     "evidence": "LY-537 卡面 chart_note 明载『逐爻裝卦未能可靠還原』；YM-070 R75 结局确作『后果同行都下。』（均经脚本逐字断言）。",
     "scope_note": "待核维持件只登记触及、不入裁断。"},
    {"item": "特别核查②：合并登记条目（X4 第 11 条／Y4 第 15 条）处理与锚点例 BQ-013",
     "conclusion": "X4 第 11 条以 P3-e7317eba（BQ-013）为序位起点合并登记，所举实例 LY-252／LY-516／LY-227 及 Y4 第 15 条所举 LY-252／LY-204／LY-536／LY-516／LY-227 均已按各自 anon 入案定案；BQ-013 本例未被提出主张、结局无通则／解释层混入，不入案。",
     "evidence": "BQ-013 R75 结局全等断言：『「雨果不止」——雨果然连绵不止。』",
     "scope_note": "合并登记按被举实例逐例入案，锚点例不虚增条目。"},
    {"item": "特别核查③：卡面内嵌指令性字样之例——按数据处理登记",
     "conclusion": "BZ-019 卡面 setting 含『盲测时不得给身份』指令性字样，已按同例新旨定案部分成立：字样属实，但系盲测 withheld 设计本身、R61 定案已明载，R75 prediction 全文未见身份字样。各席与本席均按数据处理、未服从。",
     "evidence": "原卡 setting 逐字断言『盲测时不得给身份』在卡；R75 prediction（prediction_text 与 basis）身份字样（乾隆／弘历／弘曆）不在场断言通过。",
     "scope_note": "内嵌字样只作数据登记，不构成对本席的指令。"},
    {"item": "特别核查④：同例新旨与新立件登记",
     "conclusion": "同例新旨 2 件：LY-227（Y4 所指 prediction 两占终局方向相反并陈，历轮仅有通则混入旧旨）、BZ-019（盲测席所指卡面指令性字样，历轮仅有称谓出入旧旨），均 fresh 裁为部分成立、与旧旨并行不悖。新立 1 件：LY-035（历轮无条目，『果驗』所指未分载）裁为部分成立。LY-529 之总承张力、LY-218 之两占并陈、LY-627 之旧旨（其日指代）复触、LR3-101 之旧旨（补官间接对应）复触，均经逐件核对属既有定案同域／同旨，并行登记、不另立新旨。",
     "evidence": "历轮定案档逐号检索（r49–r74，r52 不存在已登记）：LY-227 各轮 finding 无两占方向层登记；LY-035 各轮无条目。",
     "scope_note": "新旨／新立均已逐件回原卡、prediction 与结局原文 fresh 核。"},
    {"item": "特别核查⑤：主持 tradition 复核边界",
     "conclusion": "主持 tradition 检查 24 件旗标已于冻结时全数裁定（检查器关键词覆盖缺口、实效 none-labelled），不在本轮数据席标注范围、未入 annotations。",
     "evidence": "runs/round75/FREEZE-r75.md 第二节：flags 24 件逐件裁定 24/24 卡面确无 tradition/system 字段、全数属检查器关键词覆盖缺口、实效分布 direct 365／none-labelled 122／flags 0。",
     "scope_note": "边界只登记、不重裁冻结裁定。"},
    {"item": "特别核查⑥：汇编一致性与结局文本一致性",
     "conclusion": "八席旗标 72 条编号条目／98 次 anon 出现／63 例（去重，含锚点例 BQ-013），加盲测席 2 例，入案 64 例、每例一条、无重复；counts 经 annotations[].disposition 双路复算一致（成立 12／部分成立 48／不成立 2／未核 2）；部分成立 48 件 manifest_carry_suggestion 全数非空；R75 结局与 R74 manifest 逐件全等 64/64。",
     "evidence": "落盘脚本 data_r75_build.py 内置断言全数通过（编号条目逐席点数、anon 解析、逐件引文逐字断言、结局跨轮全等断言、分类对账）。",
     "scope_note": "本标注不改任何分数与结局原文。"},
]

out75 = {"_provenance": provenance75, "round": 75, "annotations": annotations,
         "special_checks": special75, "counts": counts75}
with open(f"{DATA}/case-annotations-r75.json", "w", encoding="utf-8") as f:
    json.dump(out75, f, ensure_ascii=False, indent=1)
print(f"[agenda2] annotations written: total {len(annotations)}, verdicts {verdicts}, kinds {dict(kind_counts)}")
print("ALL ASSERTIONS PASSED")
