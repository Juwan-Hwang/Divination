import json

rows = [
    {"anon_id": "H30M-10fb8b8d", "direction": 2.0, "claims": 2.0, "timing": 0.0, "reason": "重围无隙、门户破败不可保与围久粮空、城陷贼入完全吻合；预测断语本身无应期，timing记0。"},
    {"anon_id": "H30M-1a6cd083", "direction": 2.0, "claims": 1.5, "timing": 2.0, "reason": "1982结婚、1992离婚、妻高而漂亮均验；性感、第三者疑心等子断语结局未载，claims不给满分。"},
    {"anon_id": "H30M-28cf2b76", "direction": 1.5, "claims": 1.0, "timing": 0.0, "reason": "城外难久居、迁袁州、贼逼省垣大体相符；向亥四百里驻足等具体断语未见结局印证；预测断语本身无应期，timing记0。"},
    {"anon_id": "H30M-2fab055b", "direction": 2.0, "claims": 2.0, "timing": 0.0, "reason": "对方肯定答应办事，结局厂长毫无犹豫答应，唯一断语全验；预测断语本身无应期，timing记0。"},
    {"anon_id": "H30M-3159a551", "direction": 2.0, "claims": 1.0, "timing": 1.0, "reason": "争屋四散、住宅拆毁分居已验；腹痛白带、脾泄、少妇掌家等多数子断语结局未载；仅以来年泛指对己卯年，timing部分命中。"},
    {"anon_id": "H30M-3302aa36", "direction": 2.0, "claims": 2.0, "timing": 2.0, "reason": "特大火灾、巳月、卯日逐项吻合，应期精确命中。"},
    {"anon_id": "H30M-52ee71b3", "direction": 2.0, "claims": 1.5, "timing": 1.5, "reason": "火灾发生且规模大，四月十二日入下一旬之日点命中；申酉日与西北方位结局未明载，claims与timing不给满分。"},
    {"anon_id": "H30M-67bf623f", "direction": 2.0, "claims": 2.0, "timing": 2.0, "reason": "六月入相、秋出师均按时应验，全项命中。"},
    {"anon_id": "H30M-6a25b577", "direction": 2.0, "claims": 1.5, "timing": 1.0, "reason": "结局仅记后果如所占，首揆与中年反复之断无细节展开，claims不给满分；结局无可核时点，timing记1。"},
    {"anon_id": "H30M-714732c5", "direction": 1.5, "claims": 1.0, "timing": 0.0, "reason": "其子该次终未考上属实，但系考前出走缺考而非考场落败，留级补考亦未载；预测断语本身无应期，timing记0。"},
    {"anon_id": "H30M-77854ad6", "direction": 2.0, "claims": 1.5, "timing": 0.0, "reason": "虚冢、倍价买山后葬、后代聪颖发科举大体印证；山向龙入首等子断语未载；预测断语本身无应期，timing记0。"},
    {"anon_id": "H30M-80469b10", "direction": 2.0, "claims": 2.0, "timing": 2.0, "reason": "1999年无大劫难、地震火灾频发，断语逐项与该年结局吻合。"},
    {"anon_id": "H30M-8413b8c0", "direction": 2.0, "claims": 2.0, "timing": 0.0, "reason": "宅有淫乱不可居，结局公淫其媳家丑外扬，全验；预测断语本身无应期，timing记0。"},
    {"anon_id": "H30M-86bd7b88", "direction": 2.0, "claims": 1.5, "timing": 1.5, "reason": "1995有恋情、2001先孕后婚同年生女均验；丙子年与下月对象、相貌性情等子断语未载或未合，claims不给满分。"},
    {"anon_id": "H30M-8f2ac5c5", "direction": 2.0, "claims": 2.0, "timing": 2.0, "reason": "本月难生、至子月方生，结局子月剖腹产子，应期精确命中。"},
    {"anon_id": "H30M-90a55ad1", "direction": 1.0, "claims": 0.5, "timing": 0.0, "reason": "结局为高血压甲亢、手脚麻木发抖失眠，未明言头部有病，仅症状部分相关；预测断语本身无应期，timing记0。"},
    {"anon_id": "H30M-a1542a9f", "direction": 2.0, "claims": 2.0, "timing": 1.0, "reason": "先损复孕结局明记已准；结局无可核时点，timing记1。"},
    {"anon_id": "H30M-a224edf6", "direction": 2.0, "claims": 2.0, "timing": 2.0, "reason": "父母姐妹嫌工资低反对、本由父母做主、1996年巳月结婚逐项吻合，应期精确。"},
    {"anon_id": "H30M-a3ecbe1f", "direction": 2.0, "claims": 1.5, "timing": 2.0, "reason": "1992结婚、夫二婚同乡、1994离婚均验且年份精确；夫不在家独居等现状子断语未载，claims不给满分。"},
    {"anon_id": "H30M-a6545b32", "direction": 2.0, "claims": 2.0, "timing": 2.0, "reason": "九月大拜与九月入阁精确吻合。"},
    {"anon_id": "H30M-abe49f8d", "direction": 2.0, "claims": 2.0, "timing": 0.0, "reason": "财运不错与家中火灾两断均验：邻家打麻将大赢、家中漏电起火；预测断语本身无应期，timing记0。"},
    {"anon_id": "H30M-af728f7c", "direction": 2.0, "claims": 1.5, "timing": 1.5, "reason": "终有子成立，2000再孕、2001辰月生男与两年窗口大体相合；2000即有子表述与先孕后产细节不完全对应，不给满分。"},
    {"anon_id": "H30M-c3275a32", "direction": 2.0, "claims": 1.5, "timing": 1.5, "reason": "八月陟大司寇命中，内召入刑部在七月略早于八九月之断，claims与timing部分扣分。"},
    {"anon_id": "H30M-c51ada16", "direction": 2.0, "claims": 2.0, "timing": 2.0, "reason": "内阁首臣、乌程人、行年五十五逐项与结局记载精确吻合。"},
    {"anon_id": "H30M-f4042f33", "direction": 2.0, "claims": 1.5, "timing": 0.5, "reason": "及第、郎官、累升至礼部侍郎主线全验；令弟、阴德等子断语未载，即日食禄与多年仕途进程不合，timing低。"},
    {"anon_id": "H30M-f7fd8b2d", "direction": 2.0, "claims": 1.5, "timing": 0.0, "reason": "退避上游五百里至袁州得安、省城因武宁失守闭城均验；西方门户、辰土方位等子断语未明载；预测断语本身无应期，timing记0。"},
    {"anon_id": "H30M-fa3080ed", "direction": 2.0, "claims": 2.0, "timing": 1.0, "reason": "丈夫生殖器与精子问题致不能怀孕经医院检查逐项印证；一生之断结局无可核时点，timing记1。"},
    {"anon_id": "H30M-fd43915c", "direction": 2.0, "claims": 1.5, "timing": 1.0, "reason": "功名不成、家计败尽后靠妻家酒业渐丰、享福寿终主线全验；兄弟星散、店房居住未载；结局无可核时点，timing记1。"},
]

assert len(rows) == 28, len(rows)
out_path = "/home/hatch/workspace/divination/benchmark/phase3/runs/round87/acceptance/judging/judgeM2.jsonl"
with open(out_path, "w", encoding="utf-8") as f:
    for r in rows:
        total = r["direction"] + r["claims"] + r["timing"]
        rec = {
            "anon_id": r["anon_id"],
            "direction": r["direction"],
            "claims": r["claims"],
            "timing": r["timing"],
            "total": total,
            "pass": total >= 4,
            "reason": r["reason"],
        }
        assert rec["total"] == rec["direction"] + rec["claims"] + rec["timing"]
        assert rec["pass"] == (rec["total"] >= 4)
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

n = len(rows)
d = sum(r["direction"] for r in rows) / n
c = sum(r["claims"] for r in rows) / n
t = sum(r["timing"] for r in rows) / n
tot = sum(r["direction"] + r["claims"] + r["timing"] for r in rows) / n
p = sum(1 for r in rows if (r["direction"] + r["claims"] + r["timing"]) >= 4)
print(f"files={n} direction_mean={d:.4f} claims_mean={c:.4f} timing_mean={t:.4f} total_mean={tot:.4f} pass={p}")
