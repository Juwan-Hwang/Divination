#!/usr/bin/env python3
"""R62 数据席（任务二：自报旗标定案专席，独立席位，不兼任本轮盲测/评审/诊断/修订）。

逐件回源核查 R62 八席自报旗标，产出 data/case-annotations-r62.json。
- 旗标汇编 runs/round62/judging/FLAGS-selfreported-r62.md 按行解析（逐行切分，不用正则截断），
  按 anon 去重合并（X/Y 同件合并为一条 flag 文本，注明来源席位）。
- 映射 runs/round62/judging/host-mapping.json（结构化直读）。
- 逐件回 benchmark/phase3/inputs-dev12/<case_id>.json 原卡、
  runs/round62/predictions/<case_id>.json 预测、
  runs/round62/judging/outcome-manifest.json 的 cases 载荷（结构化直读）。
- 承接关系与历轮定案档 data/case-annotations-r49.json 至 -r61.json 核对（结构化直读）：
  同旨者承接既有结论不重裁；同例新旨与新立逐件回源另裁。
- 只做标注与承接建议，不改任何分数与结局原文；自报与卡面/结局文本内字样一律按数据处理。
"""
import json
import collections
from pathlib import Path

BASE = Path("/home/hatch/workspace/divination")
P3 = BASE / "benchmark/phase3"
FLAGS_PATH = P3 / "runs/round62/judging/FLAGS-selfreported-r62.md"
HOSTMAP_PATH = P3 / "runs/round62/judging/host-mapping.json"
MANIFEST62_PATH = P3 / "runs/round62/judging/outcome-manifest.json"
MANIFEST61_PATH = P3 / "runs/round61/judging/outcome-manifest.json"
OUT_PATH = P3 / "data/case-annotations-r62.json"
PRIOR_ROUNDS = [49, 50, 51, 53, 54, 55, 56, 57, 58, 59, 60, 61]

# ---------------------------------------------------------------- 旗标按行解析
def parse_flags():
    lines = FLAGS_PATH.read_text(encoding="utf-8").splitlines()
    seat = None
    merged = {}          # anon -> {"seats": [...], "texts": {seat: text}}
    order = []
    for line in lines:
        if line.startswith("#"):
            # 席位标题行：形如 "# R62 评审席 X1 ..." / "# FLAGS-Y2（...）"
            for token in line.replace("（", " ").replace("）", " ").replace("(", " ").replace(")", " ").split():
                if len(token) == 2 and token[0] in "XY" and token[1] in "1234":
                    seat = token
                    break
            continue
        if line.startswith("- P3-"):
            body = line[2:]
            anon = body[:11]
            assert body[11] in "：:", f"旗标行分隔符异常: {line[:40]}"
            text = body[12:].strip()
            assert anon.startswith("P3-") and len(anon) == 11, anon
            if anon not in merged:
                merged[anon] = {"seats": [], "texts": {}}
                order.append(anon)
            assert seat is not None and seat not in merged[anon]["texts"], (anon, seat)
            merged[anon]["seats"].append(seat)
            merged[anon]["texts"][seat] = text
    return merged, order

# ---------------------------------------------------------------- 手工定案（新立 6 件 + 同例新旨 1 件，均逐件回源后另裁）
MANUAL = {
    "MH-002": {
        "disposition": "成立",
        "relation": "新旗标（R62 新立）",
        "category": "结局应验机制与断语机制不同（时点与结果则合）",
        "finding": "新旗标（R62 新立）：回原卡——牡丹占，卡面载邵雍与客往司馬公家觀牡丹、客问花亦有数；R62 prediction 断「明日午时将遇狂风摧折、花落殆尽」，致毁机制系于狂风（用乾金克体巽木、风为巽象）；R62 manifest 结局作「次日午時，果有貴官觀牡丹，二馬相齧，群至花間馳驟，花盡為之踐毀」——应验时点（次日午时）与结果（花尽毁）与断语合，但致毁机制为二马相啮、群至花间践踏，非狂风摧折。旗标所言机制不对应、时点与结果则合，逐项属实。故成立。",
        "carry": "同旨新立：自 R63 起承接本 R62 标注：按「结局应验机制与断语机制不同（马践踏 vs 狂风）、时点与结果则合」登记；结局原文照录不改。",
    },
    "LY-312": {
        "disposition": "成立",
        "relation": "新旗标（R62 新立）",
        "category": "量级严重不对应（小祸倾向 vs 子死）",
        "finding": "新旗标（R62 新立）：回原卡——占买宅吉否；R62 prediction 终局作可买、吉多于凶，仅防「宅中一处小祸」，且 basis 明载该小祸断经粒度核降为倾向表述；R62 manifest 结局作「彼竟得此屋，遷入不半月，其子出花而死」——迁入不半月其子出花而死，人命之祸与「一处小祸」倾向表述量级严重不对应，旗标属实。故成立。",
        "carry": "同旨新立：自 R63 起承接本 R62 标注：按「预测仅防一处小祸（倾向表述）、结局为迁入不半月其子出花而死，量级严重不对应」登记；结局原文照录不改。",
    },
    "LY-624": {
        "disposition": "部分成立",
        "relation": "新旗标（R62 新立）",
        "category": "输入残损（两占合断仅载一卦、已双示）",
        "finding": "新旗标（R62 新立）：回原卡——卡面 subject 自载「求財（兩占合斷）」，notes 定位文明载同例再占暌之损不在本条范围，卡内只载家人之贲一卦；R62 prediction 正文自注「题面记两占合断，输入卡只载一卦，本断只据此一卦，两占互证面残损已注明」，trigger 亦同旨留痕——两占合断而互证面残损属实；但残损已在卡面与 prediction 双处明示、非未注明问题（同 YY2-004／OC-009 残损双示口径）。故部分成立。",
        "carry": "同旨新立：自 R63 起承接本 R62 标注：按「题面两占合断、输入卡只载一卦，互证面残损（卡面与 prediction 已双示）」登记；结局原文照录不改。",
    },
    "LY-540": {
        "disposition": "部分成立",
        "relation": "新旗标（R62 新立）",
        "category": "结局疑似截断（逗号收尾）",
        "finding": "新旗标（R62 新立）：回原卡——占随官上任如何；R62 manifest 结局作「后因官府掣签得缺，近于贼营辞而不去，及至官府去后又因他事而去，至七月城破与官府一同被害，」以逗号收尾，其后疑有未录文字，截断之疑属实一层；但主结局（城破与官府一同被害）已明载、终局可核（同 LY-416 逗号收尾口径）。故部分成立。",
        "carry": "同旨新立：自 R63 起承接本 R62 标注：按「结局以逗号收尾、疑似截断，主结局（城破一同被害）明载」登记；结局原文照录不改。",
    },
    "LY-227": {
        "disposition": "部分成立",
        "relation": "新旗标（R62 新立）",
        "category": "结局混入断法通则（个案结局仅一句）",
        "finding": "新旗标（R62 新立）：回原卡——占乡试，前后两占；R62 manifest 结局本体作「果得成名。」其后整段为六冲/六合断法通则（「凡得六沖卦﹐官父世爻俱旺者﹐不必再占﹐竟許必得」以下），非本例个案结局记载，个案可核内容仅成名一句，通则混入属实；但个案结局「果得成名」本身明载、非缺位（同 LY-516 通则混入口径）。故部分成立。",
        "carry": "同旨新立：自 R63 起承接本 R62 标注：按「个案结局仅『果得成名』、后半混入六冲/六合断法通则」登记；结局原文照录不改。",
    },
    "BZ-035": {
        "disposition": "部分成立",
        "relation": "新旗标（R62 新立）",
        "category": "题面年份与史载不合（已自注）",
        "finding": "新旗标（R62 新立）：回原卡——卡面 birth 载「清嘉庆八年（1803年），原书仅存四柱」，命主李鸿章史载生于 1823 年，卡面 1803 年与史载常年不合属实，四柱（癸未 甲寅 乙亥 己卯）与史载之年相合；但 R62 prediction 正文已自注「输入卡载出生年为1803年，与史载常年不合，断语只据四柱不据年数」，basis 亦同旨——出入已自注、仅限年份一层（同 BZ-036／BZ-037 已自注出入口径）。故部分成立。",
        "carry": "同旨新立：自 R63 起承接本 R62 标注：按「题面出生年 1803 与史载常年不合、prediction 已自注、断语只据四柱不据年数」登记；结局原文照录不改。",
    },
    "YM-038": {
        "disposition": "部分成立",
        "relation": "同例新旨（R61 旧旨旗标不成立、本轮新旨另立）",
        "category": "结局兼载异事（溺亡与所占之疾不同事）",
        "finding": "同例新旨（R61 旧旨为『内部矛盾／通用断例』旗标、定案不成立，本轮新旨与之各旨独立、并行不悖）：回原卡——占子病（子病生死）；R62 prediction 断子病可愈、不至死；R62 manifest 结局作「后其疾不死，未半年溺水而亡。」——后半溺水身亡确与所占之疾为不同事、结局兼载异事属实；但前半「其疾不死」已直接对应所占之疾终局，病面核验完整、非缺位。故部分成立。",
        "carry": "同例新旨：自 R63 起承接本 R62 标注（与 R61 旧旨不成立定案并行、各旨独立）：按「结局兼载半年后溺水身亡、与所占之疾为不同事；所占之疾终局『其疾不死』有明载」登记；结局原文照录不改。",
    },
}

# BZ-105：同旨续接，X4 附加一层经回源属实、与既有档位相容，承接不重裁并注明
EXTRA_NOTE = {
    "BZ-105": " 本轮 X4 附加一层（结局证实的两段皆病伤面、prediction 军职升迁一段未获独立证实）经回原卡／R62 prediction／R62 结局核对属实——prediction 回溯所问过去两段为军职升迁/得职之年与病伤之年，结局仅证实 1972 年患目疾、1982 年患病住院两段病伤，升迁段确无独立证实；该层属回溯成色同一问题域，与既有部分成立档位相容，承接不重裁、档位不变。",
}

YM070_CARRY = ("挂起维持（注记合并）：自 R63 起承接 R51＋R55＋R56＋R57＋R58＋R59＋R60＋R61＋本 R62 登记："
               "按「结局措辞待核（『都下』语义未明）」与卡面 asked_at「甲寅旬」出处待核两项合并登记、并列承接；"
               "结局原文照录不改、不补字；无盘外独立史源前不另裁。")


def main() -> None:
    merged, order = parse_flags()
    hostmap = json.loads(HOSTMAP_PATH.read_text(encoding="utf-8"))
    man62 = json.loads(MANIFEST62_PATH.read_text(encoding="utf-8"))
    man61 = json.loads(MANIFEST61_PATH.read_text(encoding="utf-8"))
    cases62, cases61 = man62["cases"], man61["cases"]

    priors = {}  # case_id -> [(round, ann)]
    for rnd in PRIOR_ROUNDS:
        doc = json.loads((P3 / f"data/case-annotations-r{rnd}.json").read_text(encoding="utf-8"))
        for ann in doc["annotations"]:
            priors.setdefault(ann["case_id"], []).append((rnd, ann))

    assert len(order) == 82, f"去重后 anon 数不符: {len(order)}"

    annotations = []
    for anon in order:
        info = merged[anon]
        assert anon in hostmap, f"host-mapping 缺 {anon}"
        cid = hostmap[anon]
        seats = info["seats"]
        flag_text = "；".join(f"{s}：{info['texts'][s]}" for s in seats)

        # 逐件回源：原卡与本轮预测必须实存且可读（结构化直读）
        card = json.loads((P3 / f"inputs-dev12/{cid}.json").read_text(encoding="utf-8"))
        pred = json.loads((P3 / f"runs/round62/predictions/{cid}.json").read_text(encoding="utf-8"))
        assert card is not None and pred is not None
        # 结局文本与 R61 manifest 逐件全等断言
        assert cid in cases62 and cid in cases61, cid
        assert cases62[cid] == cases61[cid], f"{cid} 结局文本 R62 与 R61 不一致"

        prior_list = priors.get(cid, [])
        prior_sources = [f"benchmark/phase3/data/case-annotations-r{r}.json {cid} 条" for r, _ in prior_list]
        base_sources = [
            f"benchmark/phase3/inputs-dev12/{cid}.json",
            "benchmark/phase3/runs/round62/judging/FLAGS-selfreported-r62.md",
            f"benchmark/phase3/runs/round62/judging/outcome-manifest.json cases[{cid}]",
            f"benchmark/phase3/runs/round62/predictions/{cid}.json",
        ]

        if cid in MANUAL:
            m = MANUAL[cid]
            disposition, finding, relation = m["disposition"], m["finding"], m["relation"]
            carry, category = m["carry"], m["category"]
            sources = base_sources + prior_sources
        else:
            assert prior_list, f"{cid} 无历轮定案且不在手工定案表"
            latest_rnd, latest = prior_list[-1]
            assert latest_rnd >= 55, (cid, latest_rnd)
            disposition = latest["disposition"]
            assert disposition in ("成立", "部分成立", "不成立", "未核"), (cid, disposition)
            finding = (f"承接既有定案不重裁（历轮最近定案 R{latest_rnd} {disposition}）："
                       f"{latest['finding']}"
                       f" 本轮（R62）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。")
            if cid in EXTRA_NOTE:
                finding += EXTRA_NOTE[cid]
            relation = f"同旨续接（R{latest_rnd}）"
            category = "同旨续接（详见核查事实）"
            if cid == "YM-070":
                carry = YM070_CARRY
            elif disposition == "不成立":
                carry = (f"不入附则：承既有定案（R{latest_rnd} 不成立）口径，自 R63 起承接本 R62 标注，"
                         "不加承接注记；结局原文照录不改。")
            elif disposition == "未核":
                raise AssertionError(f"{cid} 未核续接未预设承接文本")
            else:
                rounds_txt = "／".join(f"R{r}" for r, _ in prior_list if r >= 55)
                carry = (f"同旨续接：自 R63 起承接 {rounds_txt}＋本 R62 标注；结局原文照录不改。")
            sources = base_sources + prior_sources

        annotations.append({
            "anon_id": anon,
            "case_id": cid,
            "disposition": disposition,
            "finding": finding,
            "flag": flag_text,
            "manifest_carry_suggestion": carry,
            "relation": relation,
            "registered_round": 62,
            "sources_checked": sources,
            "source_seats": seats,
            "_category": category,
        })

    # ---------------------------------------------------------------- counts 复算
    verdicts = dict(collections.Counter(a["disposition"] for a in annotations))
    n_cont = sum(1 for a in annotations if a["relation"].startswith("同旨续接"))
    n_newgist = sum(1 for a in annotations if a["relation"].startswith("同例新旨"))
    n_new = sum(1 for a in annotations if a["relation"].startswith("新旗标"))
    assert n_cont + n_newgist + n_new == len(annotations) == 82
    for a in annotations:
        if a["disposition"] == "部分成立":
            assert a["manifest_carry_suggestion"], a["case_id"]
        assert a["manifest_carry_suggestion"], a["case_id"]
    counts = {
        "selfreport_anons_total": len(order),
        "cases_total": len(annotations),
        "continuation_cases": n_cont,
        "same_case_new_gist_cases": n_newgist,
        "new_flag_cases": n_new,
        "verdicts": {k: verdicts.get(k, 0) for k in ("成立", "部分成立", "不成立", "未核")},
    }
    assert sum(counts["verdicts"].values()) == 82

    # ---------------------------------------------------------------- 特别核查
    flagged_cases = {a["case_id"] for a in annotations}
    inv = {v: k for k, v in hostmap.items()}
    assert inv["YM-070"] in merged and inv["LY-537"] not in merged
    assert inv["BZ-029"] not in merged and inv["BZ-040"] not in merged
    special_checks = [
        {
            "item": "特别核查①：LY-537 与 YM-070 与『待核／挂起维持』登记的关系",
            "conclusion": "YM-070 出现在本轮旗标中（P3-f46e875e，X4／Y4 同报『都下』语义未明），已照实核、承接既有定案给 disposition 为未核（挂起），与待核维持口径一致、无差异；本定案产出与待核维持登记并行不悖。LY-537 本轮未出现在旗标中，不在本件范围，其待核／挂起维持登记不变。",
            "evidence": "YM-070：R62 manifest 结局「后果同行都下。」中『都下』语义未明（R51–R61 历轮登记、R61 定案未核），另卡面 asked_at『甲寅旬』出处待核为并存挂起项，两项合并登记，本轮自报与之同旨。LY-537：其 R62 anon（P3-9fc56d88）不在本轮 82 件旗标 anon 集内；其『果于申予日归』疑衍字未核登记（R56／R57／R61）照旧。",
            "scope_note": "本核查只登记关系，不改分数、不改 manifest；待核口径照旧。",
        },
        {
            "item": "特别核查②：BZ-029／BZ-040 未入本轮旗标——维持原登记",
            "conclusion": "两件本轮均未出现在旗标中，不在本件范围，维持原登记（R55 定案未核），不另裁。",
            "evidence": "两件 R62 anon（BZ-029＝P3-cf1fc87c、BZ-040＝P3-7ffb5c0a）均不在本轮 82 件旗标 anon 集内。原登记：BZ-029 命主俞大维卒年于本席核查范围内无可裁史源、BZ-040 命主许世英生年口径与卒年享年存疑，均 R55 定案未核、待盘外独立史源。",
            "scope_note": "本核查只登记维持，不改分数、不改 manifest；待核口径照旧。",
        },
        {
            "item": "特别核查③：同例新旨（YM-038）与附加层（BZ-105）登记",
            "conclusion": "YM-038 本轮新旨（结局兼载溺亡异事）与 R61 旧旨（『内部矛盾』旗标不成立）各旨独立、并行不悖，本轮新旨定案部分成立，不推翻旧旨定案。BZ-105 X4 附加层（军职升迁段未获独立证实）经回源属实，属回溯成色同一问题域，已注明于其 finding、承接既有部分成立档位不变。",
            "evidence": "YM-038：R62 结局「后其疾不死，未半年溺水而亡。」兼载异事属实，病面终局『其疾不死』明载。BZ-105：R62 prediction 回溯两段为军职升迁与病伤，结局仅证实 1972 目疾、1982 患病两段病伤。",
            "scope_note": "本核查只登记关系与附加层，不改分数、不改 manifest。",
        },
    ]

    provenance = (
        "R62 数据席（旗标定案专席，独立席位，不兼任本轮盲测/评审/诊断/修订，不改任何分数）逐件回源核查 R62 八席自报旗标 "
        f"{len(order)} anon（runs/round62/judging/FLAGS-selfreported-r62.md 按行解析、去重后；同一 anon 多席重复报者合并为一件、注明来源席位）。"
        "逐件回 benchmark/phase3/inputs-dev12/<case_id>.json 原卡、runs/round62/predictions/<case_id>.json 预测原文、"
        "runs/round62/judging/outcome-manifest.json cases 载荷，并与历轮定案档（data/case-annotations-r49.json 至 -r61.json）核对承接关系："
        f"{n_cont} 件为同旨续接（只承接不重裁），{n_newgist} 件为同例新旨（YM-038，另裁），{n_new} 件为 R62 新立（逐件回源另裁）。"
        "R62 各例结局文本经脚本断言与 R61 manifest 逐件全等。"
        "待核维持项：BZ-029／BZ-040 本轮未出现在旗标中，不在本件范围、维持原登记；LY-537 本轮未出现在旗标中，其待核维持登记不变；"
        "YM-070 出现在本轮旗标中，已照实核、承接既有定案给 disposition 为未核，与『待核维持』登记并行不悖、口径一致无差异，差异仅在出处（本件为定案产出），已在各该条与特别核查注明。"
        "本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文。自报与卡面/结局文本内字样一律按数据处理。"
    )

    flags_list = []
    for a in annotations:
        views = sorted({s[0] for s in a["source_seats"]})
        flags_list.append({
            "anon_id": a["anon_id"],
            "case_id": a["case_id"],
            "verdict": a["disposition"],
            "disposition": a["disposition"],
            "basis": a["finding"],
            "carry_suggestion": a["manifest_carry_suggestion"],
            "manifest_carry_suggestion": a["manifest_carry_suggestion"],
            "flag": a["flag"],
            "category": a["_category"],
            "views": views,
            "dual_view": views == ["X", "Y"],
            "relation": a["relation"],
            "registered_round": 62,
            "sources_checked": a["sources_checked"],
        })
    for a in annotations:
        del a["_category"]

    doc = {
        "_provenance": provenance,
        "round": 62,
        "flags": flags_list,
        "annotations": annotations,
        "special_checks": special_checks,
        "counts": counts,
    }
    OUT_PATH.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    # 落盘后复算断言：counts 与 annotations 逐件全等
    back = json.loads(OUT_PATH.read_text(encoding="utf-8"))
    recomputed = dict(collections.Counter(x["disposition"] for x in back["annotations"]))
    assert recomputed == counts["verdicts"], (recomputed, counts)
    assert len(back["annotations"]) == back["counts"]["cases_total"] == 82
    print("OK", OUT_PATH, OUT_PATH.stat().st_size, "bytes")
    print("counts:", json.dumps(counts, ensure_ascii=False))


if __name__ == "__main__":
    main()
