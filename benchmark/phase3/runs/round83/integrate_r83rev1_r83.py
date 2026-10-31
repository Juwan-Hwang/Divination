#!/usr/bin/env python3
# R83-REV1 integration script (integration seat only). Absolute paths only. No /tmp. No runs/ listing.
import pathlib, hashlib, re, sys

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
PROP = BASE / "runs/round83/revision/PROPOSAL-R83-REV1.md"
DECISION = BASE / "runs/round83/revision/DECISION-qimen-r83.md"
GATE = BASE / "runs/round83/revision/GATE-qimen-r83.md"
CAL = BASE / "method/references/calibration.md"
SKILL = BASE / "method/SKILL.md"
INTEG = BASE / "method/METHOD-INTEGRATION-r83.md"

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def extract_section(text: str, start_marker: str, end_marker: str | None) -> str:
    i = text.index(start_marker)
    body_start = text.index("\n", i) + 1
    if end_marker is None:
        body = text[body_start:]
    else:
        j = text.index(end_marker, body_start)
        body = text[body_start:j]
    return body.strip("\n")

def main():
    prop_text = PROP.read_text(encoding="utf-8")
    # sanity: decision and gate exist and contain key phrases
    dec_text = DECISION.read_text(encoding="utf-8")
    gate_text = GATE.read_text(encoding="utf-8")
    assert "设" in dec_text and "R83-REV1" in dec_text
    assert "五项全过" in gate_text or "全过" in gate_text

    sec1 = extract_section(prop_text, "## 一、适用面", "## 二、干预对象")
    sec2 = extract_section(prop_text, "## 二、干预对象", "## 三、条文全文")
    sec3 = extract_section(prop_text, "## 三、条文全文", "## 四、与现行节的并行分工")
    sec4 = extract_section(prop_text, "## 四、与现行节的并行分工", "## 五、判读口径")
    sec5 = extract_section(prop_text, "## 五、判读口径", "## 六、证伪回滚条款")
    sec6 = extract_section(prop_text, "## 六、证伪回滚条款", None)

    # Verify sec3 has exactly 8 clauses
    ids_prop = re.findall(r"\*\*(R83-REV1-\d+)", sec3)
    assert ids_prop == [f"R83-REV1-{k}" for k in range(1, 9)], ids_prop

    cal_bytes_before = CAL.read_bytes()
    cal_text_before = cal_bytes_before.decode("utf-8")
    skill_bytes_before = SKILL.read_bytes()
    skill_text_before = skill_bytes_before.decode("utf-8")
    cal_sha_before, skill_sha_before = sha(cal_bytes_before), sha(skill_bytes_before)
    cal_lines_before = cal_text_before.count("\n")  # file ends with newline; lines == newline count
    assert "## 十一、" not in cal_text_before, "section 11 already present"
    assert "(s)" not in skill_text_before

    # ---- Build section 11 (style follows section 10 head: ## heading + parenthetical registration line) ----
    header = "## 十一、奇门用神落宫定性复核与应期取径明示核（R83 干预 R83-REV1，奇门段别机制，现行）"
    reg = ("（集成登记：提案 runs/round83/revision/PROPOSAL-R83-REV1.md；裁决 runs/round83/revision/DECISION-qimen-r83.md；"
           "闸门 runs/round83/revision/GATE-qimen-r83.md 五项全过；自集成之次轮起算效力，照 R59／R61／R78／R80／R81／R82 先例。"
           "判读口径全文见本节「判读口径」部分，照提案 §五写死，本节不另改写。）")
    section11_parts = [
        header,
        "",
        reg,
        "",
        "**适用面（提案 §一）**",
        sec1,
        "",
        "**干预对象（提案 §二）**",
        sec2,
        "",
        sec3,
        "",
        "**与现行节的并行分工（提案 §四，同例不重复处置）**",
        sec4,
        "",
        "**判读口径（提案 §五全文，写死）**",
        sec5,
        "",
        "**证伪回滚条款与归因分离条款（提案 §六全文）**",
        sec6,
        "",
    ]
    section11 = "\n".join(section11_parts)
    # section11 ends with single newline via last ""? join gives trailing \n from last empty? Actually last element "" gives trailing separator; ensure exactly one trailing newline
    if not section11.endswith("\n"):
        section11 += "\n"
    section11_lines = section11.count("\n")

    new_cal_text = cal_text_before + "\n" + section11
    CAL.write_text(new_cal_text, encoding="utf-8")

    # ---- SKILL pointer (s) after (r) ----
    r_line = "- (r) 断项范围限定：非量级类具体断项初稿写成后、终局合成前，先扫盘面反向限定信号，有限定者按其对象界／阶段界／条件界收束主张范围，无限定者不动作（正本见 references/calibration.md 第十节，R82-REV1，自集成之次轮起算效力）"
    assert r_line in skill_text_before, "r line not found verbatim"
    s_line = "- (s) 奇门用神落宫定性复核与应期取径明示：奇门段作断先列用神清单，方向须过横看落宫生克与竖看旺衰空墓复核并满足两条同向定性指针门槛，应期须明示取径且一例一径、无据不换径（正本见 references/calibration.md 第十一节，R83-REV1，自集成之次轮起算效力）"
    new_skill_text = skill_text_before.replace(r_line + "\n", r_line + "\n" + s_line + "\n", 1)
    assert new_skill_text != skill_text_before
    SKILL.write_text(new_skill_text, encoding="utf-8")

    # ---- Strip-back verification ----
    cal_text_after = CAL.read_text(encoding="utf-8")
    skill_text_after = SKILL.read_text(encoding="utf-8")
    checks = []

    # 1) calibration is pure suffix append: original is prefix
    prefix_ok = cal_text_after.startswith(cal_text_before)
    checks.append(f"calibration 纯后缀追加（原文件为新文件前缀，第五/六/七/九节失效存档标记与第八/十节原文随前缀逐字未动）：{'通过' if prefix_ok else '失败'}")
    assert prefix_ok
    # strip-back: remove added suffix recovers original exactly
    stripped_cal = cal_text_after[:len(cal_text_before)]
    checks.append(f"calibration strip-back 删去新增第十一节后与集成前原文逐字全等：{'通过' if stripped_cal == cal_text_before else '失败'}")
    assert stripped_cal == cal_text_before

    # 2) Clause-by-clause comparison: extract clause segment from section 11
    sec11_text = cal_text_after[len(cal_text_before):]
    # clause segment = from first **R83-REV1-1 to just before the parallel-division heading
    c_start = sec11_text.index("**R83-REV1-1")
    c_end = sec11_text.index("**与现行节的并行分工")
    clause_segment = sec11_text[c_start:c_end].strip("\n")
    clause_equal = (clause_segment == sec3)
    checks.append(f"条文段逐字对勘（第十一节条文段 == 提案件 §三全文）：{'通过' if clause_equal else '失败'}")
    assert clause_equal

    ids_cal = re.findall(r"\*\*(R83-REV1-\d+)", clause_segment)
    checks.append(f"条数与编号：提案件 8 条（R83-REV1-1 至 8），第十一节实测 {len(ids_cal)} 条，编号序列 {'、'.join(ids_cal)}，一致：{'通过' if ids_cal == ids_prop else '失败'}")
    assert ids_cal == ids_prop

    # 3) Key thresholds per clause / judgement, checked in both proposal sec3/sec5 and calibration sec11
    key_checks = [
        ("R83-REV1-4 两条定性指针门槛", "至少两条"),
        ("R83-REV1-4 指针属 (a)-(d)", "值符、值使落宫"),
        ("R83-REV1-5 一例一径/换径一次", "许换径一次"),
        ("R83-REV1-5 第二次换径不许", "第二次换径不许"),
        ("R83-REV1-7 留痕四行", "须留四行"),
        ("判读集 holdout28", "holdout28"),
        ("主指标 DIR ≤1", "DIR 主码计数 **≤1**"),
        ("副指标 TIM ≤1", "TIM 主码计数 **≤1**"),
        ("护栏甲 OMIT ≤1", "OMIT 主码计数 ≤1"),
        ("护栏乙 CLAIM ≤1", "CLAIM 主码计数 ≤1"),
        ("护栏丙 全集 ≥−1.722", "≥−1.722"),
        ("护栏丁 留痕 3/3", "3/3"),
        ("段均分只作附读", "只作附读"),
        ("证伪线 DIR＝3", "DIR 主码计数 ＝3"),
        ("证伪线全集 ≤−1.870", "≤−1.870"),
        ("归因分离禁借 holdout27", "不得以 holdout27 为判读集"),
    ]
    all_key_ok = True
    for label, needle in key_checks:
        in_prop = (needle in sec3) or (needle in sec5) or (needle in sec6) or (needle in sec1) or (needle in sec4)
        in_cal = needle in sec11_text
        ok = in_prop and in_cal
        all_key_ok = all_key_ok and ok
        checks.append(f"关键阈值/门槛「{label}」（{needle}）：提案件有={in_prop}、第十一节有={in_cal}，{'通过' if ok else '失败'}")
    assert all_key_ok

    # 4) Other mandated inclusions in sec11
    for label, needle in [("适用面（§一）全文逐字", sec1), ("并行分工（§四）全文逐字", sec4),
                          ("判读口径（§五）全文逐字", sec5), ("证伪回滚与归因分离（§六）全文逐字", sec6)]:
        ok = needle in sec11_text
        checks.append(f"{label}已载入第十一节：{'通过' if ok else '失败'}")
        assert ok
    # parallel division mentions section 8 and 10
    assert "与第八节" in sec11_text and "与第十节" in sec11_text
    checks.append("并行分工含与第八节、与第十节两项：通过")

    # 5) SKILL strip-back
    stripped_skill = skill_text_after.replace(s_line + "\n", "", 1)
    skill_strip_ok = (stripped_skill == skill_text_before)
    checks.append(f"SKILL strip-back 删去 (s) 指针一行后与集成前原文逐字全等，且 (s) 紧接 (r) 之后一行：{'通过' if skill_strip_ok else '失败'}")
    assert skill_strip_ok
    assert (r_line + "\n" + s_line + "\n") in skill_text_after
    checks.append("SKILL 指针序列：(r) 后按序新增 (s) 一行，无其他改动：通过")

    cal_bytes_after = CAL.read_bytes(); skill_bytes_after = SKILL.read_bytes()
    cal_sha_after, skill_sha_after = sha(cal_bytes_after), sha(skill_bytes_after)
    cal_lines_after = cal_text_after.count("\n")

    # ---- Write METHOD-INTEGRATION-r83.md ----
    checks_block = "\n".join(f"- {c}" for c in checks)
    content = f"""# METHOD-INTEGRATION-r83 · R83-REV1 集成记录（集成席执行）

- 立项依据：裁决件 `runs/round83/revision/DECISION-qimen-r83.md`（裁决「设」，理由 1–8）设立奇门段别干预 R83-REV1「奇门用神落宫定性复核与应期取径明示核」；提案件 `runs/round83/revision/PROPOSAL-R83-REV1.md`（条文 R83-REV1-1 至 8、判读口径、证伪回滚，以此为集成源）；集成席只做集成与验合，不作裁决、不作预测/评审、不看金标。
- 闸门五项结论（`runs/round83/revision/GATE-qimen-r83.md`，五项全过，准予集成）：① 只据聚合——裁决理由 1–8 全部落聚合件轨迹、E5 构成与 direction 附读计数，无单例引用，通过；② 干预对象具体可执行——只限奇门段，对象为方向形成与应期取径，条文八条含留痕四行与不处置面明文，通过；③ 判读口径写死——判读集 holdout28，主 DIR 计数 ≤1、副 TIM 计数 ≤1，护栏甲–丁，n＝3 功效正面处理，通过；④ 证伪回滚齐备——证伪三线、失效存档与 SKILL 指针删除回滚、未达未证伪处置、判读一次性，通过；⑤ 不冲突／不复活／归因分离——与第八节、第十节辖域不相交、不复活第五/六/七/九节、禁借 holdout27 计数，通过。附验：提案引用的奇门章条目编号主持逐一 grep 盘上实存。
- 集成对象（只动三件）：
  1. `references/calibration.md`：在现行第十节（R82-REV1）之后新增第十一节「{header[3:]}」（含集成登记行、适用面 §一、干预对象 §二、条文 R83-REV1-1 至 8 §三、与第八/第十节并行分工 §四、判读口径全文 §五、证伪回滚与归因分离 §六），新增节共 {section11_lines} 行（另与第十节之间空行 1 行分隔）；文件为纯后缀追加，集成前 {cal_lines_before} 行 → 集成后 {cal_lines_after} 行。第五、六、七、九节失效存档标记一字未动，第八、十节原文一字未动（纯前缀追加实测，见 strip-back）。
  2. `SKILL.md`：指针序列在 (r) 行之后按序新增 (s) 一行，原文为：「{s_line}」
  3. 本件 `METHOD-INTEGRATION-r83.md`（新建登记件）。method 其余文件一字未动。
- 集成 diff 摘要：calibration.md {len(cal_bytes_before)} 字节 → {len(cal_bytes_after)} 字节（+{len(cal_bytes_after)-len(cal_bytes_before)}）；SKILL.md {len(skill_bytes_before)} 字节 → {len(skill_bytes_after)} 字节（+{len(skill_bytes_after)-len(skill_bytes_before)}，恰为 (s) 指针一行含换行）。
- 哈希（盘上实测全文 SHA-256）：calibration 改前 {cal_sha_before} → 改后 {cal_sha_after}；SKILL 改前 {skill_sha_before} → 改后 {skill_sha_after}。
- 效力起算：自集成之次轮起算，照 R59／R61／R78／R80／R81／R82 先例。判读集 holdout28 为本提案集成后首个新鲜封存集，其封存快照锚定本轮集成后时点（照提案件 §五写明）；即 holdout28 的封存发生在本次集成之后、快照含第十一节，本提案判读只用该集验收诊断的聚合计数，基线只用提案件所引 holdout26 及以前已定稿聚合。
- 判读口径写死全文转记（提案件 §五）：判读集 holdout28。n＝3 功效处理：holdout28 奇门段 n＝3，段均分与段配对差在该集只作附读登记、不设判读线、不构成成败或证伪条件；主／副判读改用段内主码计数，全部计数线为 ≤ 口径、恰压线计达标。主指标：holdout28 奇门段 DIR 主码计数 ≤1（基线：h25 4/10、h26 4/9）。副指标：holdout28 奇门段 TIM 主码计数 ≤1（基线：h25 2/10、h26 3/9 且实质 3）。护栏甲（防失分换位至 OMIT）：奇门段 OMIT 主码计数 ≤1（基线：h25 1/10、h26 0/9）。护栏乙（防失分换位至 CLAIM）：奇门段 CLAIM 主码计数 ≤1（基线：h25 3/10、h26 2/9）。护栏丙（全集不恶化）：holdout28 全集总配对差 ≥−1.722。护栏丁（执行面）：奇门段 3 例 reasoning 留痕四行齐备为 3/3；缺痕例不豁免，其 DIR／TIM 主码照常计入主／副指标。附读（不设线）：奇门段配对差与段均分、段 direction＜1.75 附读计数、E5 子类全构成，逐项登记入判读件备查。成立条件：主指标与副指标同达、且护栏甲至丁全守，判读成立，本节转现行。未达：主／副任一未达或护栏任一破线、而未触证伪线者，判读未达未证伪，处置照提案件 §六第 2 款（标失效存档、SKILL 指针处置照历轮未达体例由主持集成件登记）。证伪线（任一触发即证伪）：① 奇门段 DIR 主码计数 ＝3；② 奇门段 DIR＋TIM 主码计数 ＝3 且其中 DIR ≥2；③ holdout28 全集总配对差 ≤−1.870；触线即标失效存档、SKILL 指向本节的指针删除回滚（照第七节证伪处置先例）。归因分离（写死）：本提案判读与第十节判读互不构成对方成败条件；本提案不得以 holdout27 为判读集，不得借用 holdout27 的任何计数作基线或判读来源；第十节在 holdout27 的判读结论不改变本提案在 holdout28 的判读口径与计数线，反之亦然；本节不使第八节或第十节复活或失效。判读一次性：只对 holdout28 执行一次，不设顺延判读集、不以 expansion 池未定产出预支后续判读。
- strip-back 验合结果（集成脚本 runs/round83/integrate_r83rev1_r83.py 断言全过后落笔；条文段自 calibration.md 第十一节剥离、与提案件 §三逐条对勘）：
{checks_block}
- 集成脚本：`runs/round83/integrate_r83rev1_r83.py`（唯一脚本，条文与各节文本由脚本自提案件按 §一至§六抽取逐字写入，非手抄）。
- 异常/自报：无。未打开任何单例预测／金标／结局材料；未对任何 runs/ 目录执行列表/计数操作；未用 /tmp；改动只限上述三件。
"""
    INTEG.write_text(content, encoding="utf-8")
    print("CAL_BEFORE", len(cal_bytes_before), cal_sha_before)
    print("CAL_AFTER", len(cal_bytes_after), cal_sha_after, "lines_before", cal_lines_before, "lines_after", cal_lines_after, "section11_lines", section11_lines)
    print("SKILL_BEFORE", len(skill_bytes_before), skill_sha_before)
    print("SKILL_AFTER", len(skill_bytes_after), skill_sha_after)
    print("S_LINE", s_line)
    print("INTEG_BYTES", len(INTEG.read_bytes()))
    print("ALL CHECKS PASSED")
    for c in checks:
        print("CHECK:", c)

if __name__ == "__main__":
    main()
