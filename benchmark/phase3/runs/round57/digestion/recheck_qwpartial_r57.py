#!/usr/bin/env python3
# R57 QW partial 17 例开采复核席脚本（唯一名，仅 round57 内）
# 只核查：回 TXT 原文逐例核对 partial 17 例是否实载出生年月日时原文而一轮漏录。
# 不作断、不评分；不打开任何 runs/ 下 predictions/judging/final-scores。
# 行号口径：TXT 为 CRLF/CR 混杂行尾，归一化（\r\n、\r -> \n）后共 5439 行，与 R56 台账行号同口径。
import hashlib
import json
import pathlib
import re

BASE = pathlib.Path("/home/hatch/workspace/divination")
TXT_PATH = BASE / "incoming/wanted-books-4/Book/详批命例精解 (曲炜著).txt"
R56_PATH = BASE / "benchmark/phase3/runs/round56/digestion/SUPPLY-MINING-quwei-r56.json"
OUT_JSON = BASE / "benchmark/phase3/runs/round57/digestion/SUPPLY-RECHECK-qwpartial-r57.json"
OUT_MD = BASE / "benchmark/phase3/runs/round57/digestion/SUPPLY-RECHECK-qwpartial-r57.md"

# 篇界（归一化行号，end 为下一篇起始行、不含）：以正文篇题行实测为准
# 面六（4517）/摘一（5159）/摘四（5275）/摘五（5301）为一轮剔除篇，界线据其篇题行截断相邻 partial 篇。
SEGMENTS = {
    "QW-018": (4003, 4121),   # 面测命例一（次篇面二 4121）
    "QW-019": (4121, 4173),   # 面测命例二
    "QW-020": (4173, 4263),   # 面测命例三
    "QW-021": (4263, 4379),   # 面测命例四
    "QW-022": (4379, 4517),   # 面测命例五（次篇面六 4517，一轮剔除篇）
    "QW-023": (4585, 4657),   # 面测命例七
    "QW-024": (4657, 4773),   # 面测命例八
    "QW-025": (4773, 4825),   # 面测命例九
    "QW-026": (4825, 4981),   # 面测命例十
    "QW-027": (4981, 5073),   # 面测命例十一
    "QW-028": (5073, 5151),   # 面测命例十二（次为第三部分/摘选引言 5147/5151）
    "QW-029": (5185, 5229),   # 摘选命例二
    "QW-030": (5229, 5275),   # 摘选命例三（次篇摘四 5275，一轮剔除篇）
    "QW-031": (5333, 5369),   # 摘选命例六
    "QW-032": (5369, 5397),   # 摘选命例七（正文篇题误作「面测命例七」）
    "QW-033": (5397, 5421),   # 摘选命例八·兄造（本造引言行 5421 起归 QW-034）
    "QW-034": (5421, 5439),   # 摘选命例八·本人造（篇末）
}

# 逐例人工核查结论（本席逐篇读篇首命头＋全篇扫描后定性；扫描命中原文由脚本机械附证）
FINDINGS = {
    "QW-018": {
        "checked": "篇首命头（4003–4021）逐行读；全篇（4003–4120）关键词扫（出生/生人/生于/农历/阴历/阳历/时辰）＋年月日模式扫＋年·月簇扫",
        "found": "篇首仅记求测日「2002年5月25日」并称求测者「报上出生时辰」（4007），但其所报出生年月日时之值全篇未转录；命头只有干造＋四柱＋大运（1 岁起、62 起运）。全篇年月日模式唯一命中即 4007 的求测日；4109「阴历三月/五月」为 2002 年投资月份，非出生信息。大运可推生年约 1961 年，原文未直载，按写死口径不采。",
        "verdict": "maintain_partial",
    },
    "QW-019": {
        "checked": "篇首命头（4121–4137）逐行读；全篇（4121–4172）三路扫描",
        "found": "命头只有坤造＋四柱＋大运（5 岁起、78 起运）；全篇关键词扫与年月日模式扫均零命中，原文只有四柱、大运与断语/反馈。出生年月日时未载。",
        "verdict": "maintain_partial",
    },
    "QW-020": {
        "checked": "篇首命头（4173–4189）逐行读；全篇（4173–4262）三路扫描",
        "found": "命头只有坤造＋四柱＋大运（1 岁起、72 起运）；全篇关键词扫与年月日模式扫均零命中。出生年月日时未载。",
        "verdict": "maintain_partial",
    },
    "QW-021": {
        "checked": "篇首命头（4263–4277）逐行读；全篇（4263–4378）三路扫描",
        "found": "命头只有干造＋四柱＋大运（3 岁起、70 起运）；关键词唯一命中 4337「流年干乙木有生日主丁火」为生克术语，非出生信息；年月日模式零命中。出生年月日时未载。",
        "verdict": "maintain_partial",
    },
    "QW-022": {
        "checked": "篇首命头（4379–4393）逐行读；全篇（4379–4516）三路扫描",
        "found": "命头只有坤造＋四柱＋大运（0 岁起、80 起运）；关键词命中 4411「我还没出生呢」（叙述其兄去世时命主未出生，无日期）与 4513「阴历八月」（当年换工作的月份反馈），均非出生信息；年月日模式零命中。出生年月日时未载。",
        "verdict": "maintain_partial",
    },
    "QW-023": {
        "checked": "篇首命头（4585–4599）逐行读；全篇（4585–4656）三路扫描",
        "found": "命头只有干造＋四柱＋大运（1 岁起、70 起运）；正文仅另记命主 2001 年来求测（4607），为求测时点非出生信息；关键词扫与年月日模式扫均零命中。出生年月日时未载。",
        "verdict": "maintain_partial",
    },
    "QW-024": {
        "checked": "篇首命头（4657–4671）逐行读；时辰专节（4675–4709）逐行读；全篇（4657–4772）三路扫描",
        "found": "命头只有坤造＋四柱（按寅时排）＋大运（10 岁起、67 起运）。原文实载的是时辰不确定性：命主自述「时辰不太准，可能是寅时也可能是卯时」（4675），作者以 92/93 年事验推定「那您就是寅时出生」（4695）——此仅涉时辰一端且系推定，四柱本已按寅排；出生年月日全篇未载（年月日模式零命中；4761/4769「阴历六月」为当年升职月份）。present 定义须出生年月日与时辰原文俱载，年月日缺载即不合，维持 partial。",
        "verdict": "maintain_partial",
    },
    "QW-025": {
        "checked": "篇首命头（4773–4787）逐行读；全篇（4773–4824）三路扫描",
        "found": "命头只有坤造＋四柱＋大运（4 岁起、64 起运）；全篇关键词扫与年月日模式扫均零命中。出生年月日时未载。",
        "verdict": "maintain_partial",
    },
    "QW-026": {
        "checked": "篇首命头（4825–4839）逐行读；全篇（4825–4980）三路扫描",
        "found": "命头只有坤造＋四柱＋大运（6 岁起、67 起运）；全篇关键词扫与年月日模式扫均零命中。出生年月日时未载。",
        "verdict": "maintain_partial",
    },
    "QW-027": {
        "checked": "篇首命头（4981–4995）逐行读；全篇（4981–5072）三路扫描",
        "found": "命头只有坤造＋四柱＋大运（1 岁起、72 起运）；全篇关键词扫与年月日模式扫均零命中。出生年月日时未载。",
        "verdict": "maintain_partial",
    },
    "QW-028": {
        "checked": "篇首命头（5073–5087）逐行读；全篇（5073–5150）三路扫描",
        "found": "命头只有坤造＋四柱＋大运（1 岁起、78 起运）；正文仅另记 2002 年命主来求测（5099）。关键词唯一命中 5107「童年时居家出生地情况」为断出生地、无日期；年月日模式唯一命中 5141「2003年四月结婚」为婚期，均非出生信息。出生年月日时未载。",
        "verdict": "maintain_partial",
    },
    "QW-029": {
        "checked": "篇首命头（5185–5193）逐行读；全篇（5185–5228）三路扫描",
        "found": "命头只有坤造＋四柱（无大运）；原文唯一日期 5195「99年己卯冬月十五，来中心求测」为求测日，非出生日期；关键词扫零命中。出生年月日时未载。",
        "verdict": "maintain_partial",
    },
    "QW-030": {
        "checked": "篇首命头（5229–5245）逐行读；全篇（5229–5274）三路扫描",
        "found": "命头只有坤造＋四柱＋大运（9 岁起、80 起运）；正文仅另记「此造2001年来求测」（5247），为求测时点；关键词扫与年月日模式扫均零命中。出生年月日时未载。",
        "verdict": "maintain_partial",
    },
    "QW-031": {
        "checked": "篇首命头（5333–5343）逐行读；全篇（5333–5368）三路扫描",
        "found": "命头只有干造＋四柱（无大运）；正文仅另记命主 2002 年夏求测（5345），为求测时点；关键词扫与年月日模式扫均零命中。出生年月日时未载。",
        "verdict": "maintain_partial",
    },
    "QW-032": {
        "checked": "篇首命头（5369–5379）逐行读；全篇（5369–5396）三路扫描",
        "found": "命头只有干造＋四柱＋大运（9 岁起、73 起运）；正文仅另记「命主今年五月来求测」（5381），为求测时点；关键词扫与年月日模式扫均零命中。大运可推生年区间，原文未直载，按写死口径不采。出生年月日时未载。",
        "verdict": "maintain_partial",
    },
    "QW-033": {
        "checked": "篇首命头（5397–5413）逐行读；全篇（5397–5420）三路扫描",
        "found": "命头只有干（造）＋四柱＋大运（7 岁起、80 起运）；求测者代报其兄四柱（5419 反馈「此造是其哥哥四柱」），所报仅四柱；关键词扫与年月日模式扫均零命中。出生年月日时未载。",
        "verdict": "maintain_partial",
    },
    "QW-034": {
        "checked": "本造命头（5421–5435）逐行读；全篇（5421–5438）三路扫描",
        "found": "5421「看完此造求测者又报出一四柱要我预测」，所报只有干＋四柱＋大运（6 岁起、80 起运）；关键词扫与年月日模式扫均零命中。出生年月日时未载。",
        "verdict": "maintain_partial",
    },
}

KEYS = ["出生", "生人", "生于", "农历", "農曆", "阴历", "陰曆", "阳历", "陽曆", "时辰", "時辰", "生日"]
DATEPAT = re.compile(r".{0,4}年.{0,6}月.{0,6}日")


def main():
    raw = TXT_PATH.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    r56 = json.loads(R56_PATH.read_text(encoding="utf-8"))
    assert sha == r56["source_sha256"], f"TXT SHA 与一轮台账不符: {sha}"

    text = raw.decode("utf-8")
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    assert len(lines) == 5439, f"归一化行数异常: {len(lines)}"

    partials = [e for e in r56["entries"] if e["anchor_presence"] == "partial"]
    assert len(partials) == 17, f"一轮 partial 应为 17 例，实得 {len(partials)}"
    assert [e["provisional_id"] for e in partials] == [f"QW-{i:03d}" for i in range(18, 35)]

    entries = []
    for e in partials:
        qid = e["provisional_id"]
        a, b = SEGMENTS[qid]
        key_hits, date_hits = [], []
        for i in range(a, b):
            line = lines[i - 1]
            if any(k in line for k in KEYS):
                key_hits.append({"line": i, "text": line.strip()[:200]})
            for m in DATEPAT.finditer(line):
                date_hits.append({"line": i, "match": m.group(0), "text": line.strip()[:200]})
        f = FINDINGS[qid]
        upgraded = f["verdict"] == "upgrade_present"
        entries.append({
            "provisional_id": qid,
            "source": e["source"],
            "tradition": e["tradition"],
            "gender": e["input_fields"]["subject"]["gender"],
            "pillars": e["input_fields"]["context"]["attachments"]["pillars"],
            "r56_birth_info_verbatim": e["input_fields"]["subject"]["birth_info_verbatim"],
            "r56_anchor_presence": "partial",
            "txt_segment_normalized_lines": [a, b - 1],
            "checked": f["checked"],
            "scan_evidence": {"keyword_hits": key_hits, "date_pattern_hits": date_hits},
            "finding": f["found"],
            "verdict": f["verdict"],
            "anchor_presence_after": "present" if upgraded else "partial",
            "birth_info_verbatim_supplement": None,
            "supplement_basis": None,
        })

    upgraded_n = sum(1 for x in entries if x["verdict"] == "upgrade_present")
    doc = {
        "batch": "Phase3 Round57 开采复核席·QW partial 17 例复核（只核查，不作断不评分）",
        "prereg_basis": "runs/round57/PREREG.md §4「QW partial 17 复核」：只核 TXT 原文是否实载出生年月日时而一轮漏录——实载者补录升 present 并登记依据；确未载者维持 partial，不许以大运反推补锚（承 DIGEST-bazi-quwei-r56 §四.3）",
        "source_file": str(TXT_PATH),
        "source_sha256": sha,
        "source_sha256_matches_r56_ledger": True,
        "line_numbering": "TXT 原始为 CRLF/CR 混杂行尾；归一化（\\r\\n、\\r -> \\n）后共 5439 行，本件行号与 R56 台账行号同口径",
        "r56_ledger": str(R56_PATH),
        "checked_count": len(entries),
        "upgraded_present_count": upgraded_n,
        "maintained_partial_count": len(entries) - upgraded_n,
        "optional_pool_recalc": {
            "basis_r56": "R56 定版：QW 入账 34＝present 17＋partial 17（SUPPLY-MINING-quwei-r56.md）；全局可选集 8→65（runs/round56/REPORT.md），holdout20 已自可选集封存 25 例",
            "qw_present_before": 17,
            "qw_present_after": 17 + upgraded_n,
            "qw_partial_after": 17 - upgraded_n,
            "optional_pool_increment_from_this_recheck": upgraded_n,
            "optional_pool_total_after": 65 + upgraded_n,
            "optional_pool_unused_after_holdout20": 65 + upgraded_n - 25,
            "note": "本轮只复算登记、不组集不封存（PREREG §4）；本复核不改变任何既往入账与封存",
        },
        "entries": entries,
    }
    OUT_JSON.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")

    # ---- MD 摘要 ----
    md = []
    md.append("# SUPPLY-RECHECK-qwpartial-r57 —— 曲炜《详批命例精解》QW partial 17 例复核摘要（R57 开采复核席）")
    md.append("")
    md.append("- 底本：`incoming/wanted-books-4/Book/详批命例精解 (曲炜著).txt`，SHA-256 `6da0e3848f04ee00159b13e375a6cde169426c54bf0b0354b165240752e3d37b`（本席实测，与 R56 台账登记一致）。")
    md.append("- 一轮台账：`runs/round56/digestion/SUPPLY-MINING-quwei-r56.json`，partial 17 例＝QW-018–QW-034（面测一至五、七至十二＋摘选二、三、六、七、八两造）；限度登记见 DIGEST-bazi-quwei-r56 §四.3。")
    md.append("- 口径（PREREG §4 写死）：present＝四柱全列＋性别＋出生年月日时原文俱载可复排；只核原文是否实载而一轮漏录，实载者逐字补录升 present，确未载者维持 partial；**不许以大运起运年等反推补锚**。")
    md.append("- 方法：TXT 行尾归一化后 5439 行（与 R56 行号同口径）；逐例三路核查——①篇首命头逐行读；②全篇关键词扫（出生/生人/生于/农历/阴历/阳历/时辰/生日等）；③年月日模式扫与年·月簇扫，命中逐处定性（求测日/流年月份/婚期等非出生信息逐例注明）。篇界按下一篇篇题行截断，面六/摘一/摘四/摘五等一轮剔除篇不混入相邻 partial 篇。")
    md.append("- 本席纪律：只核查、不作断、不评分；未打开任何 runs/ 下 predictions/judging/final-scores；未做 git 操作。")
    md.append("")
    md.append("## 结论")
    md.append("")
    md.append("**升 present 0 例；维持 partial 17 例。** 一轮登记无漏录：面测/摘选诸例原文确实均未载出生年月日时（QW-024 仅时辰寅/卯二选一经推定、年月日全缺；QW-018 仅称求测者「报上出生时辰」而未转录其值），与 DIGEST-bazi-quwei-r56 §1.2/§四.3 的体例登记一致。")
    md.append("")
    md.append("## 逐例结论表")
    md.append("")
    md.append("| 例 | 篇目 | 四柱（性别） | 核查结论 | 复核后锚点 |")
    md.append("|---|---|---|---|---|")
    short = {
        "QW-018": "仅记求测日 2002年5月25日＋「报上出生时辰」一语（4007），所报之值未转录；唯一年月日命中即求测日",
        "QW-019": "命头仅坤造＋四柱＋大运；全篇关键词/年月日扫零命中",
        "QW-020": "命头仅坤造＋四柱＋大运；全篇两扫零命中",
        "QW-021": "命头仅干造＋四柱＋大运；唯一「生」命中为生克术语（4337），年月日扫零命中",
        "QW-022": "命头仅坤造＋四柱＋大运；命中为「还没出生呢」叙述与当年阴历八月反馈，均无日期",
        "QW-023": "命头仅干造＋四柱＋大运；仅另记 2001 年来求测（4607）",
        "QW-024": "时辰寅/卯未定、作者推定寅时（4675/4695），仅涉时辰一端；出生年月日全缺",
        "QW-025": "命头仅坤造＋四柱＋大运；全篇两扫零命中",
        "QW-026": "命头仅坤造＋四柱＋大运；全篇两扫零命中",
        "QW-027": "命头仅坤造＋四柱＋大运；全篇两扫零命中",
        "QW-028": "命头仅坤造＋四柱＋大运；命中为「出生地」断语（5107）与 2003年四月婚期（5141）",
        "QW-029": "命头仅坤造＋四柱；唯一日期 99年己卯冬月十五为求测日（5195）",
        "QW-030": "命头仅坤造＋四柱＋大运；仅另记 2001 年来求测（5247）",
        "QW-031": "命头仅干造＋四柱；仅另记 2002 年夏求测（5345）",
        "QW-032": "命头仅干造＋四柱＋大运；仅另记今年五月来求测（5381）；大运可推生年不采",
        "QW-033": "命头仅干＋四柱＋大运；代报其兄者所报仅四柱；全篇两扫零命中",
        "QW-034": "命头仅干＋四柱＋大运；求测者自报仅四柱；全篇两扫零命中",
    }
    for x in entries:
        pillars = " ".join(x["pillars"])
        md.append(f"| {x['provisional_id']} | {x['source'].split('·')[-1]} | {pillars}（{x['gender']}） | {short[x['provisional_id']]} | partial（维持） |")
    md.append("")
    md.append("逐例完整核查记录（查过何处、扫描命中原文、定性）见同名 JSON `entries[].checked / scan_evidence / finding`。")
    md.append("")
    md.append("## 特别登记（易误读两例）")
    md.append("")
    md.append("- **QW-018（面一）**：「报上出生时辰」（TXT 4007）只证明求测者曾口头报过，书中未录其值；同行「2002年5月25日」为求测日。大运 1 岁起、62 起运可推生年约 1961 年——按写死口径不以推断补锚。")
    md.append("- **QW-024（面八）**：原文对时辰有专节讨论，但内容是「不准、二选一、靠事验推定寅时」，且出生年月日全然未载；即便时辰一端可视为已定，年月日缺载仍不合 present 定义。此例亦是一轮登记中唯一连时柱本身都带不确定性的 partial，维持 partial 且维持一轮注记。")
    md.append("")
    md.append("## 可选集增量复算")
    md.append("")
    md.append("- R56 定版基数：QW 入账 34＝present 17（QW-001–QW-017）＋partial 17；全局可选集 65（R56 REPORT：8→65），holdout20 已自可选集封存 25 例，未用可选库存 40。")
    md.append("- 本复核：升 present **0** 例 → QW present 维持 17、partial 维持 17。")
    md.append("- 复算：可选集增量 **+0**，全局可选集维持 **65**，未用可选库存维持 **40**（65−25）。本轮只复算登记、不组集不封存（PREREG §4）。")
    md.append("")
    md.append("## 限度")
    md.append("")
    md.append("- 本复核只及该 TXT 转录本：若原书纸本另有转录本未收的出生信息页，本席无从检出，结论只对在盘 TXT 成立。")
    md.append("- 扫描以关键词＋日期模式为网、篇首命头逐行为主核；叙述文字中的年龄/事验年份（如各例流年反馈）均按非出生信息定性，未逐条列入表中，完整命中清单在 JSON 附证。")
    md.append("")
    OUT_MD.write_text("\n".join(md), encoding="utf-8")
    print(f"OK checked={len(entries)} upgraded={upgraded_n} maintained={len(entries)-upgraded_n}")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
