import json, pathlib, collections, sys
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
def load(p):
    with open(p, encoding="utf-8") as f: return json.load(f)
def wload(rel): return load(base/rel)

# ============ TASK 1: addendum from R62 annotations ============
r62 = wload("data/case-annotations-r62.json")
ann62 = r62["annotations"]
recomp = collections.Counter(a["disposition"] for a in ann62)
assert dict(recomp) == {"成立":14,"部分成立":65,"不成立":2,"未核":1} or set(recomp.items())==set(r62["counts"]["verdicts"].items()), (recomp, r62["counts"])
assert r62["counts"]["verdicts"] == {"成立":14,"部分成立":65,"不成立":2,"未核":1}
assert len(ann62)==82
partial62 = [a for a in ann62 if a["disposition"]=="部分成立"]
assert len(partial62)==65
assert all((a.get("manifest_carry_suggestion") or "").strip() for a in partial62)

om63 = wload("runs/round63/judging/outcome-manifest.json")
add63 = om63["_r63_carryover_notes_addendum"]
assert isinstance(add63, dict) and len(add63)==65
assert set(add63.keys()) == {a["case_id"] for a in partial62}
mismatch = [a["case_id"] for a in partial62 if add63[a["case_id"]] != a["manifest_carry_suggestion"]]
assert mismatch == [], mismatch
assert all(a["case_id"] in om63["cases"] for a in partial62)
print("TASK1 assertions OK: 65/65 identical")

lines = []
lines.append("# Manifest 承接册附则（R63）——R62 定案承接建议汇编")
lines.append("")
lines.append("## 卷首说明")
lines.append("")
lines.append("- 本附则为 Phase 3 Round 63（R63）数据席（任务一：承接附则编制；与本轮盲测／评审／诊断席互不兼任）产出；汇编来源为 `benchmark/phase3/data/case-annotations-r62.json`（R62 定案正本：annotations 82 件，定案分布成立 14／部分成立 65／不成立 2／未核 1）。")
lines.append("- counts 断言结果：通过。本席以原档 `counts.verdicts` 与 `annotations[].disposition` 双路复算，均为成立 14／部分成立 65／不成立 2／未核 1、总 82，与 R62 公布分布逐项一致；部分成立 65 件每件 `manifest_carry_suggestion` 非空断言亦通过。")
lines.append("- 对勘结果：65/65 全等（详见「对勘记录」）。对勘对象为 `benchmark/phase3/runs/round63/judging/outcome-manifest.json` 的 `_r63_carryover_notes_addendum` 层（本席只读该层与 `cases` 键名集），逐件以全文字符串相等比对本附则转录的 `manifest_carry_suggestion`；不一致者登记于对勘记录，不静默改任一侧（本轮不一致 0 件）。")
lines.append("- **本附则自 R64 manifest 起落实**；本轮（R63）manifest 不据本附则改动。")
lines.append("- **本件只汇编与对勘，不改任何分数与结局原文。**")
lines.append("- 汇编范围：R62 定案中部分成立 65 件，逐件全列于第一节（顺序照原档 `annotations` 排列）；每件的承接注记建议文本照 `case-annotations-r62.json` 该件 `manifest_carry_suggestion` 字段原文录入，不改写（其中「自 R63 起」等表述为原档原文，落实轮次按卷首上一条读作自 R64 起，不回溯改动 R63）。每件定案要旨照原档 `finding` 字段、原旗标要旨照原档 `flag` 字段、与既有承接册／附则条目的关系照原档 `relation` 字段录入。")
lines.append("- 成立 14／不成立 2／未核 1 共 17 件不入正文逐件节，只在文末列 case_id 清单。")
lines.append("- 承接只标注、不改任何既往或本轮分数、不改结局原文、不改原卡。")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 一、部分成立件承接汇编（定案档位：部分成立，65 件，逐件全列）")
lines.append("")
for i, a in enumerate(partial62, 1):
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
lines.append("## 对勘记录")
lines.append("")
lines.append("- 对勘对象：本汇编第一节 65 件承接注记建议文本（源：`case-annotations-r62.json` 各件 `manifest_carry_suggestion`）与 `benchmark/phase3/runs/round63/judging/outcome-manifest.json` 的 `_r63_carryover_notes_addendum` 对应条目，逐件逐字（全文字符串相等）对勘。")
detail = "、".join(f"{a['case_id']}＝一致" for a in partial62)
lines.append(f"- 对勘结果：65 件逐字一致，差异 0 件（对勘明细：{detail}）。")
lines.append("- 键集合差异：无（manifest 层 65 键与部分成立 65 件 case_id 集合全等）。")
lines.append("- 不一致登记：无。两侧均未作任何静默改动；本附则建议文本照源档原文录入，manifest 侧文本照其盘上原文对勘。勘误结论：无须勘误；本附则结论自 R64 manifest 起落实。")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 自验")
lines.append("")
lines.append("- 原档（case-annotations-r62.json）条目数：82；档位分布成立 14／部分成立 65／不成立 2／未核 1，本席以 `annotations[].disposition` 与原档 `counts.verdicts` 双路复算一致。")
lines.append("- 本附则正文条目数：65（第一节部分成立 65 件），与原档部分成立件数对齐；文末不入附则清单 17 件（成立 14＋不成立 2＋未核 1），65＋17＝82 与原档总数对齐。")
lines.append("- 承接注记建议文本：65 件均自原档 JSON 的 `manifest_carry_suggestion` 字段结构化直读录入，未手抄改写；且经上节对勘与 R63 manifest `_r63_carryover_notes_addendum` 逐件逐字一致（65／65）。")
lines.append("- 纪律自报：本席只汇编与对勘，未改任何分数、未改 manifest、未改 annotations、未改原卡；outcome-manifest 只读 `_r63_carryover_notes_addendum` 层与 `cases` 键名集。")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 文末清单：不入附则 17 件（成立 14＋不成立 2＋未核 1，仅列 case_id）")
lines.append("")
for disp in ["成立","不成立","未核"]:
    ids = [a["case_id"] for a in ann62 if a["disposition"]==disp]
    lines.append(f"### {disp} {len(ids)} 件")
    lines.append("")
    for cid in ids: lines.append(f"- {cid}")
    lines.append("")
addendum_text = "\n".join(lines)
out1 = base/"data/manifest-carryover-r63-addendum.md"
out1.write_text(addendum_text, encoding="utf-8")
print("TASK1 written:", out1, len(addendum_text.encode("utf-8")), "bytes")

# ============ TASK 2: R63 annotations ============
hm = wload("runs/round63/judging/host-mapping.json")
flag_lines = (base/"runs/round63/judging/FLAGS-selfreported-r63.md").read_text(encoding="utf-8").splitlines()
def seat_label(h):
    for tok in ["X1","X2","X3","X4","Y1","Y2","Y3","Y4"]:
        if tok in h: return tok
    return None
seat=None; raw_flags=[]
for l in flag_lines:
    if l.startswith("# "):
        s = seat_label(l[2:].strip())
        if s: seat = s
        continue
    if l.startswith("- P3-"):
        anon, txt = l[2:].split("：",1)
        raw_flags.append((anon.strip(), seat, txt))
assert len(raw_flags)==161, len(raw_flags)
byanon = collections.OrderedDict()
for anon, s, t in raw_flags: byanon.setdefault(anon, []).append((s,t))
assert len(byanon)==87
assert all(a in hm for a in byanon)
om62 = wload("runs/round62/judging/outcome-manifest.json")

prior_files=[49,50,51,53,54,55,56,57,58,59,60,61,62]
prior={}
for r in prior_files:
    d = wload(f"data/case-annotations-r{r}.json")
    for a in d["annotations"]:
        prior.setdefault(a["case_id"],[]).append((r,a))

NEW_GIST = {"LY-025","LY-216","LY-538"}
NEW_FLAG = {"LY-523","LY-030","LY-408","LY-452","LY-514","AS-207","LY-434"}
assert not (NEW_GIST & NEW_FLAG)
for cid in NEW_FLAG: assert cid not in prior, cid
for cid in NEW_GIST: assert cid in prior, cid

# fresh findings for new-gist / new-flag
FRESH = {
"LY-025": ("同例新旨（R61／R62 旧旨旗标部分成立、本轮新旨另立）",
  "同例新旨（R61／R62 旧旨为『prediction 终局单判 negative 与何日晴时点问错位』、定案部分成立，本轮新旨与之各旨独立、并行不悖）：回原卡——所问「何日晴」；逐字核 R63 prediction 全文，prediction_text 仅作『终局：连日之雪可望放晴』并载子日应期，并无『终局单判：negative』表述——carry 注记所称单判与本轮 prediction_text 口径不合属实，该注记系旧轮 prediction 文本面之登记、至本轮已过时；但 R63 结局『果於次日卯時，雲開日出』时点明载、无结局数据缺口。故部分成立。",
  "同例新旨：自 R64 起承接本 R63 标注（与 R61／R62 旧旨部分成立定案并行、各旨独立）：按「carry 注记所称 prediction 终局单判 negative 与 R63 prediction_text 晴向终局口径不合、结局时点明载」登记；结局原文照录不改。",
  "carry 注记与本轮 prediction_text 口径冲突（终局单判面）", "部分成立"),
"LY-216": ("同例新旨（R61／R62 旧旨旗标部分成立、本轮新旨另立）",
  "同例新旨（R61／R62 旧旨为『prediction 终局单判 positive 与仆人为祸否问目对应含混』、定案部分成立，本轮新旨与之各旨独立、并行不悖）：回原卡——所问「占僕人為禍否」；逐字核 R63 prediction 全文，prediction_text 终局作『仆人会为祸——变心之祸已成势，宜早处置』，并无『终局单判：positive』表述——carry 注记所称单判与本轮 prediction_text 口径不合属实，该注记系旧轮 prediction 文本面之登记、至本轮已过时；但 R63 结局载二人原欲害主而逃、不能相害之结果，非整例无据。故部分成立。",
  "同例新旨：自 R64 起承接本 R63 标注（与 R61／R62 旧旨部分成立定案并行、各旨独立）：按「carry 注记所称 prediction 终局单判 positive 与 R63 prediction_text 仆人为祸负向终局口径不合」登记；结局原文照录不改。",
  "carry 注记与本轮 prediction_text 口径冲突（终局单判面）", "部分成立"),
"LY-538": ("同例新旨（R49 改断面例（弱）登记、本轮新旨另立）",
  "同例新旨（R49 登记为改断面例（弱）、basis 记『參劾問改斷離任，结局应離任（§4.18）』，本轮含混旨与之各旨独立、并行不悖）：回原卡——所问「占防恭劾」；R63 manifest 结局「后因裁他处缺上台，题留他处官顶此公位将，此将公赴京另补」——文句主语交错、语序含混，参劾过程与终局性质未以明字分载，所指一层属实；但他官顶位、本人赴京另补之离任终局可读，与 R49 登记『结局应離任』一致，非整例无结局；本轮 prediction 断参劾可防、不以丢官定终局与结局之出入属评分面。故部分成立。",
  "同例新旨：自 R64 起承接本 R63 标注（与 R49 改断面例（弱）登记并行、各旨独立）：按「结局文句含混（他官顶位、本人赴京另补），参劾过程未明载、离任另补终局可读」登记；结局原文照录不改。",
  "结局文句含混（参劾过程与终局性质未明载）", "部分成立"),
"LY-523": ("新旗标（R63 新立）",
  "新旗标（R63 新立）：回原卡——所问「占兄病」，R63 prediction 断兄病不治；R63 manifest 结局「果於子時退災，次日起牀，」以逗号收尾——疑似截断之表面属实；但退灾、次日起床之主结局已明载（与 prediction 方向相反属评分面），盘内无据裁定尚有缺失后文。故部分成立（同 LY-416／LY-540 逗号收尾口径）。",
  "同旨新立：自 R64 起承接本 R63 标注：按「结局以逗号收尾、疑似截断，主结局（子时退灾、次日起床）明载」登记；结局原文照录不改、不补字。",
  "结局疑似截断（逗号收尾、主结局明载）", "部分成立"),
"LY-030": ("新旗标（R63 新立）",
  "新旗标（R63 新立）：回原卡——所问「占開店」；R63 manifest 结局「果至六月病，至八月店中財物被夥計盜盡，鳴之於官」止于鸣官、无收束标点与后续，截断属实；同条全文另载于 LY-612 结局（『果於六月疾至，八月夥計盜盡。鳴之於官，分文不復。』），本例缺『分文不復』落点一层属实。但六月病、八月店中财物被盗尽、鸣之于官诸节均明载，开店凶象主线可核，非整例无结局。故部分成立。",
  "同旨新立：自 R64 起承接本 R63 标注：按「结局止于『鳴之於官』、相对同条全文（LY-612）缺『分文不復』落点，病与盗尽诸节明载」登记；结局原文照录不改、不补字。",
  "结局疑似截断（同条全文另载落点）", "部分成立"),
"LY-408": ("新旗标（R63 新立）",
  "新旗标（R63 新立）：回原卡——所问「占妻母病」；R63 manifest 结局仅「果卒於甲戌日，」以逗号收尾——疑似截断之表面属实；但妻母卒于甲戌日之主结局已明载，盘内无据裁定尚有缺失后文。故部分成立（同 LY-416／LY-540 逗号收尾口径）。",
  "同旨新立：自 R64 起承接本 R63 标注：按「结局以逗号收尾、疑似截断，主结局（卒于甲戌日）明载」登记；结局原文照录不改、不补字。",
  "结局疑似截断（逗号收尾、主结局明载）", "部分成立"),
"LY-452": ("新旗标（R63 新立）",
  "新旗标（R63 新立）：回原卡——所问「占通鄉避亂（往何方避）」；R63 manifest 结局「後果從北來，放火燒村而去，房屋稻穀盡成灰燼，」以逗号收尾、疑似截断之表面属实，且占者本人是否避往及其安否确未载，此层属实；但北来焚村之祸实况明载、与所断北凶断面对应，结局非他事。故部分成立。",
  "同旨新立：自 R64 起承接本 R63 标注：按「结局以逗号收尾、疑似截断，北来焚村实况明载，本人是否避往及安否未载」登记；结局原文照录不改、不补字。",
  "结局疑似截断＋本人安否未明载（趋避例）", "部分成立"),
"LY-514": ("新旗标（R63 新立）",
  "新旗标（R63 新立）：回原卡——所问「占防流兵」；R63 manifest 结局「後此人屢次遇兵變，或避之，或有驚無險，」以逗号收尾——疑似截断之表面属实；但屡次遇兵变、或避之或有惊无险之主结局已明载。故部分成立（同 LY-416／LY-540 逗号收尾口径）。",
  "同旨新立：自 R64 起承接本 R63 标注：按「结局以逗号收尾、疑似截断，主结局（或避之、或有惊无险）明载」登记；结局原文照录不改、不补字。",
  "结局疑似截断（逗号收尾、主结局明载）", "部分成立"),
"AS-207": ("新旗标（R63 新立）",
  "新旗标（R63 新立）：回原卡——所问『What manner of death should Canterbury die?』；R63 prediction 断斩首／刀兵之死、问后数月内；R63 manifest 结局『He was beheaded about the tenth of January following.』对所问死法（斩首）与时点（次年一月十日）均明载、与断项逐项对应。旗标所指行刑前过程与身份细节未载一节，非所问、非断项，属源结局记录形态，不构成缺载或成色问题（同 YM-068 口径）；旗标自身亦注『不影响本例终局核验』。故不成立。",
  "不入附则：本 R63 新立定案不成立（结局对所问死法与时点均明载、过程与身份细节非所问非断项），不加承接注记；结局原文照录不改。",
  "结局记录形态（问面已明载、细节非断项）", "不成立"),
"LY-434": ("新旗标（R63 新立）",
  "新旗标（R63 新立）：回原卡——所问占流年、实问援例成否；R63 manifest 结局「果於申日文書實收俱到，」以逗号收尾——疑似截断之表面属实，且援例成否未以明字直断、靠文书实收一节推定，此层属实；但申日文书实收俱到之落点已明载，非整例无结局。故部分成立。",
  "同旨新立：自 R64 起承接本 R63 标注：按「结局以逗号收尾、疑似截断，文书实收俱到有载、援例成否未明字直断」登记；结局原文照录不改、不补字。",
  "结局疑似截断＋成否未明字（文书实收有载）", "部分成立"),
}
# verification asserts for fresh cases
p25 = wload("runs/round63/predictions/LY-025.json")["prediction_text"]
assert "终局单判" not in p25 and "negative" not in p25 and "放晴" in p25
p216 = wload("runs/round63/predictions/LY-216.json")["prediction_text"]
assert "终局单判" not in p216 and "positive" not in p216 and "会为祸" in p216
assert "分文不復" in om63["cases"]["LY-612"]
assert om63["cases"]["LY-030"].endswith("鳴之於官")
assert "beheaded about the tenth of January" in om63["cases"]["AS-207"]

EXTRA_CLAUSE = {
"BZ-019": " 本轮 X3 兼报『结局以「史实同 ren-016」转引他例』一层经核属实（R63 结局文本确以『史实同 ren-016』转引同一命造史实），属结局成色同域、与既有称谓出入定案并行登记，不改既有 disposition。",
"LY-624": " 本轮 X3 兼及结局『後果全無』无时点一层，与总承式短结局同域、并行登记，不改既有 disposition。",
}

def transform_carry(prior_a, latest_round):
    c = prior_a["manifest_carry_suggestion"]
    disp = prior_a["disposition"]
    if prior_a["case_id"]=="YM-070":
        return ("挂起维持（注记合并）：自 R64 起承接 R51＋R55＋R56＋R57＋R58＋R59＋R60＋R61＋R62＋本 R63 登记："
                "按「结局措辞待核（『都下』语义未明）」与卡面 asked_at「甲寅旬」出处待核两项合并登记、并列承接；结局原文照录不改、不补字；无盘外独立史源前不另裁。")
    if disp=="不成立":
        return f"不入附则：承既有定案（R{latest_round} 不成立）口径，自 R64 起承接本 R63 标注，不加承接注记；结局原文照录不改。"
    if c.startswith("同旨续接：自 R63 起承接 "):
        mid = c[len("同旨续接：自 R63 起承接 "):].split("＋本 R62 标注")[0]
        return f"同旨续接：自 R64 起承接 {mid}／R62＋本 R63 标注；结局原文照录不改。"
    if c.startswith("同旨续接：自 R62 起承接 "):  # LY-254 latest is R61 file
        mid = c[len("同旨续接：自 R62 起承接 "):].split("＋本 R61 标注")[0]
        return f"同旨续接：自 R64 起承接 {mid}／R61＋本 R63 标注；结局原文照录不改。"
    if c.startswith("同旨新立：") or c.startswith("同例新旨："):
        return "同旨续接：自 R64 起承接 R62＋本 R63 标注；结局原文照录不改。"
    raise ValueError((prior_a["case_id"], c))

annotations=[]; flags=[]
for anon, es in byanon.items():
    cid = hm[anon]
    seats = [s for s,_ in es]
    flag_text = "；".join(f"{s}：{t}" for s,t in es)
    views = sorted({s[0] for s in seats})
    # outcome equality assertion (continuation basis)
    assert om63["cases"].get(cid) == om62["cases"].get(cid), cid
    base_sources = [f"benchmark/phase3/inputs-dev12/{cid}.json",
                    "benchmark/phase3/runs/round63/judging/FLAGS-selfreported-r63.md",
                    f"benchmark/phase3/runs/round63/judging/outcome-manifest.json cases[{cid}]",
                    f"benchmark/phase3/runs/round63/predictions/{cid}.json"]
    hist = prior.get(cid, [])
    if cid in FRESH:
        relation, finding, carry, category, disp = FRESH[cid]
        sources = base_sources + [f"benchmark/phase3/data/case-annotations-r{r}.json {cid} 条" for r,_ in hist]
        if cid=="LY-030":
            sources.append("benchmark/phase3/runs/round63/judging/outcome-manifest.json cases[LY-612]（同条全文对勘）")
    else:
        assert hist, cid
        latest_round, pa = max(hist, key=lambda x: x[0])
        disp = pa["disposition"]; assert disp, cid
        finding = pa["finding"] + f" 本轮（R63）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。"
        if cid in EXTRA_CLAUSE: finding += EXTRA_CLAUSE[cid]
        relation = f"同旨续接（R{latest_round}）"
        carry = transform_carry(pa, latest_round)
        category = "同旨续接（详见核查事实）"
        sources = base_sources + [f"benchmark/phase3/data/case-annotations-r{r}.json {cid} 条" for r,_ in hist]
    ann = {"anon_id":anon,"case_id":cid,"disposition":disp,"finding":finding,"flag":flag_text,
           "manifest_carry_suggestion":carry,"relation":relation,"registered_round":63,
           "sources_checked":sources,"source_seats":seats}
    annotations.append(ann)
    flags.append({"anon_id":anon,"case_id":cid,"verdict":disp,"disposition":disp,"basis":finding,
                  "carry_suggestion":carry,"manifest_carry_suggestion":carry,"flag":flag_text,
                  "category":category,"views":views,"dual_view":len(views)>1,"relation":relation,
                  "registered_round":63,"sources_checked":sources})

verdicts = collections.Counter(a["disposition"] for a in annotations)
n_cont = sum(1 for a in annotations if a["relation"].startswith("同旨续接"))
n_newgist = sum(1 for a in annotations if a["relation"].startswith("同例新旨"))
n_new = sum(1 for a in annotations if a["relation"].startswith("新旗标"))
print("verdicts:", dict(verdicts), "cont/newgist/new:", n_cont, n_newgist, n_new)
assert n_cont+n_newgist+n_new==87
# maintained cases not in flags
inv = {v:k for k,v in hm.items()}
for cid in ["BZ-029","BZ-040","LY-537"]:
    assert inv[cid] not in byanon, cid
assert inv["YM-070"] in byanon

special_checks = [
 {"item":"特别核查①：YM-070 与『待核／挂起维持』登记的关系",
  "conclusion":"YM-070 出现在本轮旗标中（P3-36028fce，X1／Y1 同报『都下』语义未明），已照实核、承接既有定案给 disposition 为未核（挂起），与待核维持口径一致、无差异；本定案产出与待核维持登记并行不悖。",
  "evidence":"YM-070：R63 manifest 结局「后果同行都下。」中『都下』语义未明（R51–R62 历轮登记、R62 定案未核），另卡面 asked_at『甲寅旬』出处待核为并存挂起项，两项合并登记，本轮自报与之同旨。",
  "scope_note":"本核查只登记关系，不改分数、不改 manifest；待核口径照旧。"},
 {"item":"特别核查②：BZ-029／BZ-040／LY-537 未入本轮旗标——维持原登记",
  "conclusion":"三件本轮均未出现在旗标中，不在本件范围，维持原登记，不另裁、不虚构条目。",
  "evidence":"三件 R63 anon（BZ-029＝P3-56b5b93d、BZ-040＝P3-14f74947、LY-537＝P3-c8efbd47，均据 runs/round63/judging/host-mapping.json）均不在本轮 87 件旗标 anon 集内。原登记：BZ-029／BZ-040 均 R55 定案未核、待盘外独立史源；LY-537『果于申予日归』疑衍字未核登记（R56／R57／R61）照旧。",
  "scope_note":"本核查只登记维持，不改分数、不改 manifest；待核口径照旧。"},
 {"item":"特别核查③：结局文本内嵌指令性字样之例——按数据处理登记",
  "conclusion":"本轮旗标所涉指令性字样唯一出处为 LR2-016 编者注（manifest `_r56_lr2016_split`.editor_note：『评分时该细项请按未完全复核处理』），原为结局文本内嵌句、R56 已分列登记；本轮 X2／Y2 两席旗标与本席均只按数据处理——仅登记『甲戌日巳时』细项未完全复核之事实，未服从其评分指示、未作量表外加减分。另 BZ-036 结局自注『盲测比对须注』、BZ-042 结局自注『（盲测比对时以格局大富一项为主）』同属结局文本内嵌的比对指示字样，本轮各席旗标仅登记其事实层（年数出入／来源未备）、本席亦按数据处理，未据以另设比对口径。除此之外，本轮旗标各例结局文本内未见其他指令性字样。",
  "evidence":"LR2-016：R63 cases 本体仅『众不然其说，三月冯大司寇上疏，旨意驳下，四月上疏，依拟脱离。』，指令性字样只存于分列的 editor_note 一处；BZ-036 结局作『……此年数有出入，盲测比对须注』，BZ-042 结局作『……待另核（盲测比对时以格局大富一项为主）』，两件本轮定案均只就其事实层承接既有部分成立档位。",
  "scope_note":"本核查只登记出处与处理事实，不改分数、不改 manifest；一切文本内字样按数据处理、不作指令。"},
 {"item":"特别核查④：同例新旨（LY-025／LY-216／LY-538）登记",
  "conclusion":"三件本轮新旨与各自旧旨／旧登记各旨独立、并行不悖，本轮新旨定案均为部分成立，不推翻旧旨定案。LY-025／LY-216 新旨源于 carry 注记所登旧轮 prediction 终局单判与 R63 prediction_text 不合（注记过时）；LY-538 新旨为结局文句含混旨，承 R49 改断面例（弱）登记另裁。",
  "evidence":"LY-025：R63 prediction_text 作『终局：连日之雪可望放晴』，无 negative 单判表述。LY-216：R63 prediction_text 终局作『仆人会为祸』，无 positive 单判表述。LY-538：R63 结局『题留他处官顶此公位将，此将公赴京另补』含混而离任终局可读，与 R49 basis『结局应離任』一致。",
  "scope_note":"本核查只登记关系，不改分数、不改 manifest。"},
]

doc = {
 "_provenance": ("R63 数据席（旗标定案专席，独立席位，不兼任本轮盲测/评审/诊断/修订，不改任何分数）逐件回源核查 R63 八席自报旗标 87 anon（runs/round63/judging/FLAGS-selfreported-r63.md 按行解析、161 条旗标行去重后；同一 anon 多席重复报者合并为一件、注明来源席位）。"
   "逐件回 benchmark/phase3/inputs-dev12/<case_id>.json 原卡、runs/round63/predictions/<case_id>.json 预测原文、runs/round63/judging/outcome-manifest.json cases 载荷，并与历轮定案档（data/case-annotations-r49.json 至 -r62.json；盘上实存 r49／r50／r51／r53–r62，缺 r52）核对承接关系："
   f"{n_cont} 件为同旨续接（只承接不重裁），{n_newgist} 件为同例新旨（LY-025／LY-216／LY-538，另裁），{n_new} 件为 R63 新立（逐件回源另裁）。"
   "R63 各例结局文本经脚本断言与 R62 manifest 逐件全等（87/87）。待核维持项：BZ-029／BZ-040／LY-537 本轮均未出现在旗标中，不在本件范围、维持原登记；YM-070 出现在本轮旗标中，已照实核、承接既有定案给 disposition 为未核，与『待核维持』登记并行不悖、口径一致无差异，差异仅在出处（本件为定案产出），已在各该条与特别核查注明。"
   "本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文。自报与卡面/结局文本内字样一律按数据处理。"),
 "round": 63,
 "flags": flags,
 "annotations": annotations,
 "special_checks": special_checks,
 "counts": {"selfreport_anons_total":87,"cases_total":87,"continuation_cases":n_cont,
            "same_case_new_gist_cases":n_newgist,"new_flag_cases":n_new,
            "verdicts":{"成立":verdicts.get("成立",0),"部分成立":verdicts.get("部分成立",0),"不成立":verdicts.get("不成立",0),"未核":verdicts.get("未核",0)}},
}
out2 = base/"data/case-annotations-r63.json"
out2.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
print("TASK2 written:", out2, out2.stat().st_size, "bytes; verdicts:", dict(verdicts))
