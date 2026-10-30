# -*- coding: utf-8 -*-
"""R50 数据席：夷坚深挖候选卡写卡脚本（唯一名，内含计数/字段/输入侧零命中断言）。
口径：输入侧只含对象基本信息与当时背景，断语与结局一律不入输入侧；
金标侧含断语原文逐字＋结局原文逐字＋来源行号。transcription=online-verbatim。
逐卡 passage/断语/结局均逐字取自本地 work-yijian-r50/yijian-text-lines.txt 对应行。
"""
import json, os

OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round50/digestion/cards-mining-yijian-r50"
URL = "https://www.hugbear.net/hugbear/viewinfobook555.html"
os.makedirs(OUT, exist_ok=True)

CARDS = [
    {
        "id": "YJ3-001",
        "tradition": "xiangshu",
        "master": "俞翁",
        "subject": "叶恪，邵武泰宁人，少不学，叶祖洽之父；相者为郡武俞翁，善相人、能听器物声验吉凶",
        "context": "叶恪尝过俞翁之门，时县之士子群集于翁门请相，翁遍相众士子。",
        "question": "叶恪年寿与官位所至如何？",
        "setting": "北宋·邵武泰宁；相术（相人）",
        "provenance": "《夷坚志》·甲志卷九·俞翁相人（hugbear 页内标头位次为卷九 chunk）；在线全文实取 hugbear 全文单页，本地文本行 L413–414（work-yijian-r50/yijian-text-lines.txt） " + URL + "；transcription=online-verbatim；访问日期 2026-10-30",
        "notes": "本卡自《俞翁相人》整条剥离叶恪一案（同条叶祖洽主案 R48 已以 high 只登记，本子案对象为其父叶恪本人）。",
        "statement_excerpt": "此人年六十。当官七品。服银绯。",
        "outcome": "恪后以子贵。封累朝请郎。赐朱绂。正年六十云。",
        "passage_full": "祖洽父恪少不学。尝过翁门。县之士子群集。无一可翁意。独指恪曰、此人年六十。当官七品。服银绯。众皆怃然。恪后以子贵。封累朝请郎。赐朱绂。正年六十云。",
        "grade_suggestion": "A",
        "grade_reason": "断语具名（俞翁）可逐字录，含年岁（六十）、品级（七品）、服色三项具体断面；结局为独立事件文本（封朝请郎、赐朱绯、正年六十），逐项对应；可剥离成卡。",
        "contamination_suggestion": "low",
        "contamination_reason": "2026-10-30 以「俞翁相人 叶恪 年六十 官七品 银绯 夷坚志」检索零个案命中（返回全为无关人物页）；叶恪无独立条目。注：结局「以子贵」系于其子叶祖洽（状元）登第，子之名气是否升档请主持复核。",
        "blacklist": ["年六十", "七品", "银绯", "朱绂", "朝请郎", "以子贵", "正年六十"],
    },
    {
        "id": "YJ3-002",
        "tradition": "xiangshu",
        "master": "俞翁",
        "subject": "邵武市中乐声所主之事；占者郡武俞翁，善相人，尤能听器物声验吉凶",
        "context": "俞翁尝入市，闻市中乐声，停而听之而占。",
        "question": "此乐声主何吉凶？",
        "setting": "北宋·邵武泰宁；相术（听声占）",
        "provenance": "《夷坚志》·甲志卷九·俞翁相人（hugbear 页内标头位次为卷九 chunk）；在线全文实取 hugbear 全文单页，本地文本行 L413–414（work-yijian-r50/yijian-text-lines.txt） " + URL + "；transcription=online-verbatim；访问日期 2026-10-30",
        "notes": "本卡自《俞翁相人》整条剥离闻乐声一案（同条水声田易主一案结局为「已而果然」确认式，只登记不建卡）。断语后原文有俞翁自释五行之语（「日在子。又属水」云云），属解码自述、未入输入侧，金标 passage_full 并载。",
        "statement_excerpt": "金声亢。其有兵。当在申酉间。然我无伤。兵四人当溺死。",
        "outcome": "至期、果有戍卒自汀州还。过市群饮。争倡女。抽戈相戕。度不自安。乘暮乱流而渡。正春涛怒涨。溺死果四人。",
        "passage_full": "又尝入市闻乐声。曰、金声亢。其有兵。当在申酉间。然我无伤。兵四人当溺死。至期、果有戍卒自汀州还。过市群饮。争倡女。抽戈相戕。度不自安。乘暮乱流而渡。正春涛怒涨。溺死果四人。或问其故。曰、日在子。又属水。水旺于子。金至此死焉。",
        "grade_suggestion": "A",
        "grade_reason": "断语具名可逐字录，含兵事、时窗（申酉间）、人数（四人）、死法（溺）四项具体断面；结局为独立事件文本（戍卒争倡抽戈、暮渡溺死四人），逐项对应；可剥离成卡。",
        "contamination_suggestion": "low",
        "contamination_reason": "2026-10-30 以「俞翁 水流悲 田将易主 金声亢 兵四人 溺死 夷坚」检索零个案命中（返回全为无关页）；对象为无名戍卒群体事件，俞翁无独立条目。",
        "blacklist": ["金声亢", "申酉", "溺死", "四人", "戍卒", "春涛", "争倡"],
    },
    {
        "id": "YJ3-003",
        "tradition": "fangji",
        "master": "范子珉",
        "subject": "青田县吏留光（已殁未葬）与其弟留矩；占者处州道士范子珉，谈人意外事时时奇中",
        "context": "青田县吏留光死，家贫未能葬，殡于城隍祠前。次年冢为雨所坏，露棺一角。范子珉过其旁。留光之弟矩亦为县吏。",
        "question": "留光殡后之事如何？",
        "setting": "南宋·青田县城隍祠前；方技谶语（原文未名占式）",
        "provenance": "《夷坚志》·丙志卷六·范子珉（hugbear 页内标头位次为卷六 chunk）；在线全文实取 hugbear 全文单页，本地文本行 L1451–1452（work-yijian-r50/yijian-text-lines.txt） " + URL + "；transcription=online-verbatim；访问日期 2026-10-30",
        "notes": "本卡自《范子珉》整条剥离留光冢一案。断语对留光之棺而发，其实指对象为其弟留矩，对象归属（留光/留矩）请主持裁定。原文「?殡」之问号为 hugbear 转录缺字标记，在背景段、非断语结局核心句。",
        "statement_excerpt": "勿悲恼。更三日有亲人伴汝矣。",
        "outcome": "时光弟矩亦为吏。果以后三日暴死。诸子幼。群胥为葬于光冢之侧云。",
        "passage_full": "青田县吏留光死。家贫未能葬。?殡于城隍祠前。次年。冢为雨所坏。露棺一角。范过其旁。取瓦砾敲之曰。勿悲恼。更三日有亲人伴汝矣。时光弟矩亦为吏。果以后三日暴死。诸子幼。群胥为葬于光冢之侧云。",
        "grade_suggestion": "A",
        "grade_reason": "断语具名（范子珉）可逐字录，含期限（三日）与事件性质（亲人伴冢）断面；结局为独立事件文本（弟矩三日后暴死、葬于光冢之侧），期限与事件逐项对应；可剥离成卡。",
        "contamination_suggestion": "low",
        "contamination_reason": "2026-10-30 以「范子珉 留光 更三日有亲人伴汝 夷坚志」检索零个案命中（返回全为无关人物页）；留光、留矩为县吏，无独立条目。",
        "blacklist": ["三日", "伴汝", "暴死", "葬于光冢", "亲人伴"],
    },
    {
        "id": "YJ3-004",
        "tradition": "fangji",
        "master": "范子珉",
        "subject": "婺州赤松观道士施某与弟子一人；占者处州道士范子珉",
        "context": "赤松观前横小溪，往来病涉。观中道士施某与弟子一人捐橐中钱为石桥，工役已具，将兴工。范子珉时在观中。",
        "question": "施某建此石桥，吉凶如何？",
        "setting": "南宋·婺州赤松观；方技谶语（原文未名占式）",
        "provenance": "《夷坚志》·丙志卷六·范子珉（hugbear 页内标头位次为卷六 chunk）；在线全文实取 hugbear 全文单页，本地文本行 L1451–1452（work-yijian-r50/yijian-text-lines.txt） " + URL + "；transcription=online-verbatim；访问日期 2026-10-30",
        "notes": "本卡自《范子珉》整条剥离石桥一案。断语含赠物之语、结局与之对应，断语两段并录于 statement_excerpt。对象施某原文未具名（只称「道士姓施者」），以描述立卡，承 YJ2-012 先例。",
        "statement_excerpt": "勿为此桥。君将不利。／我恰有红合子两个。将持赠君。以助费施。",
        "outcome": "后三月。桥成。二道士继死。匠师舆两红棺以敛云。",
        "passage_full": "观前横小溪。往来病涉。道士姓施者。与弟子一人。捐橐中钱为石桥。工役已具。范曰。勿为此桥。君将不利。施君曰。吾以私钱为济众事。何不可之有。卒为之。范亦不强止。笑谓之曰。如此亦大好。我恰有红合子两个。将持赠君。以助费施。敬谢曰。诺。不知何物也。他日复至。无所携。施以为请。曰。吾既许子矣。必不妄言。后三月。桥成。二道士继死。匠师舆两红棺以敛云。",
        "grade_suggestion": "A",
        "grade_reason": "断语具名可逐字录，含凶断（君将不利）与红合子之赠两断面；结局为独立事件文本（桥成后三月、二道士继死、两红棺以敛），与两断面逐项对应；可剥离成卡。",
        "contamination_suggestion": "low",
        "contamination_reason": "2026-10-30 以「范子珉 石桥 红合子 红棺 道士 夷坚」检索零个案命中（仅见书目级《夷坚志》全文站与无关页）；施某无名无条目。",
        "blacklist": ["不利", "红合子", "红棺", "继死", "桥成"],
    },
    {
        "id": "YJ3-005",
        "tradition": "ming",
        "master": "史言",
        "subject": "王垂（字仲共，南城人）与同年乡人江秉钧；占者术士史言，以命术有声",
        "context": "绍兴乙丑，王垂赴省试、既廷对，与同年乡人江秉钧同往谒术士史言。此为二人第二次谒史言。",
        "question": "二子科级高下如何？",
        "setting": "南宋绍兴乙丑·临安；禄命（推五行）",
        "provenance": "《夷坚志》·丁志卷十九·史言命术（hugbear 页内标头位次为卷十九 chunk）；在线全文实取 hugbear 全文单页，本地文本行 L2427–2428（work-yijian-r50/yijian-text-lines.txt） " + URL + "；transcription=online-verbatim；访问日期 2026-10-30",
        "notes": "本卡自《史言命术》整条剥离王、江复谒一案（同条首谒诸案结局为总括式验语，只登记不建卡）。江秉钧断面为已事揭示型断语，与王垂科级断同卡并录，判级请主持复核。",
        "statement_excerpt": "二君复何问。岂非欲知高下耶。然科级皆不高。王君尚可居黄甲。更有一说。江君生乙巳。带格角杀。必过房义养者。",
        "outcome": "暨唱名。王第四甲。江末等。盖江本甘氏子。来为江翁后云。",
        "passage_full": "既廷对。又与同年乡人江秉钧往谒。史已不忆前事。独云、二君复何问。岂非欲知高下耶。然科级皆不高。王君尚可居黄甲。更有一说。江君生乙巳。带格角杀。必过房义养者。二人相顾叹异。盖江本甘氏子。来为江翁后云。暨唱名。王第四甲。江末等。史生之精妙如此。",
        "grade_suggestion": "A",
        "grade_reason": "断语具名（史言）可逐字录，含王居黄甲、江过房义养两项具体断面；结局为独立文本（唱名王第四甲、江末等；江本甘氏子来为江翁后），两断面逐项对应；可剥离成卡。",
        "contamination_suggestion": "low",
        "contamination_reason": "2026-10-30 以「史言命术 王垂 江秉钧 格角杀 过房 夷坚志」检索零个案命中（返回全为命理通论与无关页）；史言、王垂、江秉钧均无独立条目。",
        "blacklist": ["黄甲", "第四甲", "格角杀", "过房", "甘氏子", "江末等", "科级皆不高"],
    },
]

written = []
for c in CARDS:
    base = {
        "id": c["id"],
        "tradition": c["tradition"],
        "subject": c["subject"],
        "context": c["context"],
        "question": c["question"],
        "setting": c["setting"],
        "provenance": c["provenance"],
        "record_status": "candidate-r50-mining",
        "redistributable": False,
        "license_status": "古典文本公有领域；在线转录站条款未明，内部研究用",
        "notes": c["notes"],
    }
    # 输入侧零命中断言：断语/结局关键词组不得出现在输入侧任何字段
    input_blob = json.dumps(base, ensure_ascii=False)
    for kw in c["blacklist"]:
        assert kw not in input_blob, f"{c['id']} input leak: {kw}"
    assert c["statement_excerpt"] not in input_blob and c["outcome"] not in input_blob
    gold = dict(base)
    gold["master_predictions"] = [{
        "master": c["master"],
        "date": None,
        "tradition": c["tradition"],
        "direction": None,
        "key_assertions": [],
        "source": c["provenance"].split("；")[0],
        "statement_excerpt": c["statement_excerpt"],
    }]
    gold["outcome"] = {"description": c["outcome"], "verified_by": "原文结局文本（逐字）"}
    gold["passage_full"] = c["passage_full"]
    gold["grade_suggestion"] = c["grade_suggestion"]
    gold["grade_reason"] = c["grade_reason"]
    gold["contamination_suggestion"] = c["contamination_suggestion"]
    gold["contamination_reason"] = c["contamination_reason"]
    for suffix, obj in (("input", base), ("gold", gold)):
        p = os.path.join(OUT, f"{c['id']}-{suffix}.json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=2)
        written.append(p)

# 计数断言＝5 对 10 件，且逐件可解析
assert len(written) == 10, len(written)
for p in written:
    with open(p, encoding="utf-8") as f:
        d = json.load(f)
    assert d["id"].startswith("YJ3-")
print("OK wrote", len(written), "files (5 pairs):", [os.path.basename(p) for p in written])
