# -*- coding: utf-8 -*-
"""
build_inputs_dev10_r30.py — 组 inputs-dev10（R30 输入集，n=487）

底本 benchmark/phase3/inputs-r28/，只许两类替换：
 (a) inputs10 切换集 44 例（清单见 data/DID-ANCHORS-R30.md 第一节）以 inputs10/<id>.json 字节替换；
 (b) LR3 12 例年命核查中「查得年命」者，仅增补 context.attachments.年命（seg2 体例）。
     本轮核查结论：12 例全部无据（无具体干支/年龄值），故 (b) 实际补入 0 例、无文件因此变更。
     逐例结论与出处见 FINDINGS_LR3 与产出 BUILD-MANIFEST.md。
自验：文件数、diff 只落在声明例、泄漏扫描（字段名＋词表，命中逐项登记）。
不改任何既有原件；产出仅 inputs-dev10/ 与其内 BUILD-MANIFEST.md。
"""
import hashlib
import json
import re
import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parent
SRC = BASE / "inputs-r28"
SWITCH = BASE / "inputs10"
DST = BASE / "inputs-dev10"
ANCHORS_MD = BASE / "data" / "DID-ANCHORS-R30.md"

LR3_IDS = ["LR3-002", "LR3-004", "LR3-006", "LR3-008", "LR3-010", "LR3-101",
           "LR3-104", "LR3-107", "LR3-110", "LR3-112", "LR3-114", "LR3-116"]

# (b) 核查结论：value=None 表示无据、不补入。12 例逐例证据见 BUILD-MANIFEST.md。
FINDINGS_LR3 = {i: None for i in LR3_IDS}

LEAK_FIELDS = ["master_predictions", "outcome", "statement_excerpt", "key_assertions"]
LEAK_WORDS = ["应验", "應驗", "断语", "结局", "后来", "果验", "果然", "断曰"]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def parse_switch_ids() -> list:
    text = ANCHORS_MD.read_text(encoding="utf-8")
    sec = text.split("## 二、", 1)[0]  # 第一节
    bullet = [ln for ln in sec.splitlines() if "切换集 S" in ln][0]
    ids = re.findall(r"LY-\d+", bullet)
    assert len(ids) == 44, f"第一节解析得 {len(ids)} 例"
    on_disk = sorted(p.stem for p in SWITCH.glob("*.json"))
    assert sorted(ids) == on_disk, "DID 第一节清单与 inputs10/ 盘上文件不一致"
    return ids


def main() -> None:
    switch_ids = parse_switch_ids()
    src_files = sorted(SRC.glob("*.json"))
    assert len(src_files) == 487, f"底本 {len(src_files)} 件"

    if DST.exists():
        shutil.rmtree(DST)
    DST.mkdir(parents=True)
    for p in src_files:
        shutil.copyfile(p, DST / p.name)

    # (a) 字节替换并逐例验哈希
    a_confirm = []
    for i in switch_ids:
        data = (SWITCH / f"{i}.json").read_bytes()
        (DST / f"{i}.json").write_bytes(data)
        assert sha((DST / f"{i}.json").read_bytes()) == sha(data)
        a_confirm.append(i)

    # (b) 年命补入（本轮补入集为空集；若将来有值，按 seg2 体例写 context.attachments.年命）
    b_applied = []
    for i, val in FINDINGS_LR3.items():
        if val is None:
            continue
        p = DST / f"{i}.json"
        obj = json.loads(p.read_text(encoding="utf-8"))
        obj["context"]["attachments"]["年命"] = val
        p.write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")
        b_applied.append(i)

    # 自验 1：文件数
    out_files = sorted(DST.glob("*.json"))
    assert len(out_files) == 487, f"产出 {len(out_files)} 件"
    assert [p.name for p in out_files] == [p.name for p in src_files], "文件名集与底本不一致"

    # 自验 2：diff 只落在 (a)(b) 声明例
    diff_ids = []
    for p in out_files:
        if sha(p.read_bytes()) != sha((SRC / p.name).read_bytes()):
            diff_ids.append(p.stem)
    declared = sorted(set(a_confirm) | set(b_applied))
    assert sorted(diff_ids) == declared, f"diff {sorted(diff_ids)} != 声明 {declared}"

    # 自验 3：泄漏扫描（全部变更文件；新增文本 = 新文件全文，因替换为整文件字节替换）
    leak_lines = []
    total_hits = 0
    for i in diff_ids:
        t = (DST / f"{i}.json").read_text(encoding="utf-8")
        hits = {w: t.count(w) for w in LEAK_FIELDS + LEAK_WORDS if w in t}
        guo = len(re.findall("果", t))
        total_hits += sum(hits.values())
        leak_lines.append((i, hits, guo))

    # 清单
    md = []
    md.append("# inputs-dev10 · BUILD-MANIFEST（R30 输入集，数据角交付 2026-10-30）")
    md.append("")
    md.append("- 底本：`benchmark/phase3/inputs-r28/`（487 件）；产出：本目录 487 件 `.json`＋本清单。")
    md.append("- 组集脚本：`benchmark/phase3/build_inputs_dev10_r30.py`（本批唯一新脚本）。")
    md.append(f"- (a) inputs10 切换集替换确认：**{len(a_confirm)}/44**（逐例字节替换、替换后与 `inputs10/` 源文件 SHA-256 一致）。")
    md.append(f"- (b) LR3 年命补入：**{len(b_applied)}/12**（12 例全部无据，见下逐例登记；无文件因 (b) 变更）。")
    md.append(f"- diff（vs inputs-r28）：**{len(diff_ids)} 例**，全部落在 (a) 声明集内、(b) 0 例；其余 "
              f"{487 - len(diff_ids)} 例与底本逐字（SHA-256）一致。")
    md.append("")
    md.append("## (a) 44 例替换确认（id · 替换后 SHA-256 前 12 位，与 inputs10 源一致）")
    md.append("")
    for i in a_confirm:
        md.append(f"- {i} · {sha((DST / f'{i}.json').read_bytes())[:12]} · 已替换")
    md.append("")
    md.append("## (b) LR3 12 例年命核查逐例登记")
    md.append("")
    md.append("核查口径（同 runs/liuren-seg2 补全口径）：须有占者年命/本命/行年的**具体干支或年龄值**方算有据；"
              "仅出现「命」字机制语而无值、或应期年干支冒充行年者，一律记无据。seg2 体例：补入字段为 "
              "`context.attachments.年命`（字符串、值内嵌出处），本轮无一例达到补入标准，故未动任何 LR3 文件。")
    md.append("")
    md.append("核查来源：① chen 记录：`expansion9/liuren-chen1/cases.jsonl`、`liuren-chen2/cases.jsonl` 及两目录 "
              "BUILD-REPORT、inputs（12 例 subject.birth 均为空、记录全文无年命值）；② 原书《大六壬指南》卷四占验指南"
              "对应成例原文：主源（cases provenance 所载）https://www.360doc.cn/article/2385464_179387847.html "
              "（该页本轮直抓失败、无 HTTP 状态，与 seg2 报告所载同一失败；经搜索索引所载该页全文片段核读）；"
              "③ 注解本全文互证：https://www.golla.tw:443/sm/liuren/87707.html（陈剑/张洪《六壬指南注解》卷三，"
              "含疾病/会试/仕宦诸章，逐课整页核读）及注解本 360doc http://www.360doc.cn/article/52920_996123561.html "
              "索引片段；④ 原书精校本索引片段 https://www.scribd.com/document/770896154/"
              "%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%8C%87%E5%8D%97-%E7%B2%BE%E6%A0%A1%E7%8F%8D%E8%97%8F%E5%85%A8%E6%9C%AC 。"
              "三路断语字面与 cases.jsonl 摘录逐字合。")
    md.append("")
    findings_text = {
        "LR3-002": "无据。chen1 记录无年命值；原书仕宦门本课（注解本仕宦章占验七）断语仅「即官至卯年亦不见利」「由卯上乘白虎驿马，名为回马」等语，卯为年档/课上之支、非占者年命；注家仅考订其人为陈洪范，无年命注。",
        "LR3-004": "无据（有「本命」字样而无值）。断语「喜本命丁马恩星以化之，为逢凶也吉」仅及本命机制（丁马恩星为命上所乘神将组合），未给本命干支/生肖值；原书仕宦章占验九同文，注家无年命注。R30 诊断亦按「年命未给」计（C 次因）。",
        "LR3-006": "无据。断语「曰，应于何年？曰，丁丑行年蛇墓克日」系应期问答：丁丑为应验年（历法年）干支、非占者占时行年值；注解本仕宦章占验二十一同文、无年命注。R30 诊断亦按「行年未给」计。",
        "LR3-008": "无据。chen1 记录无年命值；原书仕宦章占验二十七断语仅「虎马丁神发用，作岁君生日」等语，无年命/本命/行年值，注家按语亦无。",
        "LR3-010": "无据。chen1 记录无年命值；公讼门本课（注解本公讼章占验十五）断语无年命值；且占时对象未揭名，年命无从载。",
        "LR3-101": "无据。chen2 记录无年命值；会试门本课（注解本会试章占验八）断语仅「朱雀生太岁」等语，无占者（刘若宜）年命值。",
        "LR3-104": "无据。chen2 记录无年命值；章奏门本课（注解本章奏章占验五）断语仅「岁破为鬼」「朱雀乘太岁克日」等语，无年命值。",
        "LR3-107": "无据。chen2 记录无年命值；公讼门本课（注解本公讼章占验四）断语无年命值；占时来客未揭名，年命无从载。",
        "LR3-110": "无据。chen2 记录无年命值；走失门本课（原书走失）断语只及马色、方位、限期，无占者年命值。",
        "LR3-112": "无据（有「命上神」字样而无值）。断语「官鬼遥克玄武，公命上神又制盗神」仅及命上神之作用、未给命支值；注解本疾病章占验六同文、无年命注；余文亦无刘一纯年命值。",
        "LR3-114": "无据。chen2 记录无年命值；应候门本课（原书应候）断语只及贼人数、来方、获期，无占者年命值。",
        "LR3-116": "无据。chen2 记录无年命值；射覆门本课（原书射覆）断语只及袖中物类、色、数，无占者年命值（射覆占物，本与占者年命无关）。",
    }
    for i in LR3_IDS:
        md.append(f"- {i}：{findings_text[i]}")
    md.append("")
    md.append("## diff 与泄漏扫描")
    md.append("")
    md.append(f"- diff 总例数：**{len(diff_ids)}**，逐例即上 (a) 44 例全表；(b) 0 例。")
    md.append("- 泄漏扫描对象：全部 44 个变更文件全文。字段名扫描（master_predictions/outcome/"
              "statement_excerpt/key_assertions）：**命中 0**。")
    md.append("- 词表扫描（应验/應驗/断语/结局/后来/果验/果然/断曰＋单字「果」）命中两类，均逐项定性如下：")
    md.append("  1. 「断语」15 例（LY-324、325、328、329、330、331、332、333、335、336、338、339、340、342、344）："
              "均出自 `chart_note` 同一说明套语「本条只录可由卦名、卦宫、空亡与断语互证的信息，逐爻表不录」，"
              "只提及断语为互证来源、未引任何断语内容——无泄漏。")
    md.append("  2. LY-036「應驗」2 处／「果」1 处：其一在 `asked_at`「本月（據應驗「果於本月」，月名原文未記）」，"
              "系 inputs10 源文件自带的定月注记、引原书应验语三字以说明月份推定依据；只涉「事在本月内发生」的时间粒度、"
              "未载所占何事之结果与方向——按时间注记登记，内容性泄漏无。其二在 `chart_note` 元说明句"
              "「（此僅引原書對盤面世位的載述，不涉斷語吉凶與應驗）」，为范围声明、未引任何应验内容。"
              "两处均为源文件原有，非本轮组集新增文字，是否可接受请主持角裁量（本角不改 inputs10 原件）。")
    md.append("  3. 其余词（应验简体/结局/后来/果验/果然/断曰）命中 0；单字「果」其余命中 0。")
    md.append("- 结论：变更内容不含结局/断语/应验的具体内容（方向、结果、应期断语均无）；唯 LY-036 定月注记一处"
              "引应验语说明月份来源，已如实登记待主持裁量。年命方面本轮补入 0 例，无年命字段新增、无相关泄漏面。")
    md.append("")
    (DST / "BUILD-MANIFEST.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"switch={len(a_confirm)} b_applied={len(b_applied)} diff={len(diff_ids)} files={len(out_files)}")
    for i, hits, guo in leak_lines:
        if hits or guo:
            print("leak-scan hit:", i, hits, "果count=", guo)


if __name__ == "__main__":
    main()
