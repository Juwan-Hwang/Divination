import json, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round60/acceptance"
PACKET = os.path.join(BASE, "judging", "packet-master.json")
OUT = os.path.join(BASE, "judging", "judgeM2.jsonl")

# anon_id -> (direction, claims, timing, reason)
S = {
 "H21M-06f500eb": (1.0, 0.5, 0.0, "断下岗，结局却是高高兴兴办退休，离职方向相近但性质不符，工作不利未获印证；预测断语本身无应期，timing记0。"),
 "H21M-0aee3b60": (1.5, 1.5, 1.0, "18岁当兵陆军、28岁转房地产私营老板、经济官司破大财、投资新项目被叫停巨损均与断语多处吻合；大量性格六亲等子断语未被结局记载；应期仅年龄段部分可核。"),
 "H21M-0f19e73a": (1.5, 1.5, 2.0, "1994年末遇离婚带孩子女子并同居，与该年结婚机遇及对方有孩子断语吻合，但未成婚且两月后打孩子致分手；年份命中。"),
 "H21M-29c308c9": (2.0, 2.0, 0.0, "必凶、必为癌症两断均被结局印证，确诊肺癌且治疗无望；预测断语本身无应期，timing记0。"),
 "H21M-321ba4c6": (2.0, 2.0, 0.0, "结局证实所问男子非其夫、系离婚后未婚同居，两断逐条印证；预测断语本身无应期，timing记0。"),
 "H21M-3d23f993": (2.0, 1.5, 2.0, "明日阴天无雨有微风、仪式顺利均印证；部门领导出席一节未被结局记载；明日时间坐标命中。"),
 "H21M-3e94e492": (1.5, 1.5, 0.0, "结局掏出胖大海，褐色与带尖特征大体吻合，但断语未指明物名；预测断语本身无应期，timing记0。"),
 "H21M-454eb99a": (2.0, 2.0, 1.5, "结局经法院于1998年子月离婚，与下月离婚且须经法院两断全合；月份坐标承接下月断语，年份有载。"),
 "H21M-5d3993f7": (1.5, 1.5, 1.0, "第一胎男孩且多病残疾、妻流产、结婚花费、发财、添设备离婚、挣百万等多条印证；众多子断语未载；结局无可核时点，timing记1。"),
 "H21M-70f61225": (2.0, 2.0, 2.0, "停水原因大阀门坏、西北方向、当晚7至9时复水三断全合，实际7点20分来水且报纸证实原因方向；时间命中。"),
 "H21M-713ec854": (2.0, 1.5, 0.0, "结局明言此次相亲不成，核心断语印证；媒人介绍与本人不想去仅由总括语带过，未逐条记载；预测断语本身无应期，timing记0。"),
 "H21M-7146c2b0": (1.5, 1.5, 0.0, "结局证实所谓妻子实为未领证同居女且携款逃走；但其最终不会回来未被结局记载；预测断语本身无应期，timing记0。"),
 "H21M-7181fac7": (2.0, 2.0, 0.0, "唯一断语为不成，结局证实女方死活不愿意、最终没成，全合；预测断语本身无应期，timing记0。"),
 "H21M-893aae2f": (1.5, 1.0, 1.5, "结婚与97年生子剖腹产与96动婚、97得子剖腹断语吻合；丧父、兄坐牢等仅部分对应，众多学历官位二婚等子断语未载；97年坐标命中。"),
 "H21M-94f8bea5": (1.5, 1.5, 1.0, "学历不高、兄弟姐妹众多且有夭折异腹、谈对象未成后年底结婚、弟弟判刑入狱多条印证；其余大量子断语未载；结局无可核时点，timing记1。"),
 "H21M-b1ad2c79": (0.0, 0.0, 0.0, "包内预测全文仅有用神说明，无任何具体断语可与结局核验；预测断语本身无应期，timing记0。"),
 "H21M-b5d2bf5c": (2.0, 1.5, 1.5, "停电与复电方向全合；停电实际10点20分与所断10点30分及巳时内相符，复电16点33分在标准申时内但与书中注时段不合，故各扣半档。"),
 "H21M-c4d940de": (2.0, 1.5, 2.0, "次日上午果然降雨且雨势不小、雨具派上用场，有雨及雨不小大体印证；明日坐标命中。"),
 "H21M-cd9f935a": (1.5, 1.5, 1.0, "结局称推断全部正确且暗恋北京上大学男子细节相符，1995年有男友与今年又现男友获总括印证；1999年所婚是否此人未明，时间仅部分可核。"),
 "H21M-d92aad5c": (2.0, 2.0, 2.0, "食道癌晚期必死断语全合，实际食道癌已长八厘米；死期断酉月或戌月未日，实际1996年9月7日丁酉月丁未日去世，应期精确命中。"),
 "H21M-ea9a2418": (1.5, 1.0, 1.0, "丧父与官司缠身躲避与父病丧兆及官非口舌断语对应；其余性格事业等大量子断语未被结局记载；结局无可核时点，timing记1。"),
 "H21M-f92539a6": (2.0, 1.0, 2.0, "所断5月26日癸亥难过此日，实际其姨母5月26日凌晨癸亥日去世，应期精确；但脑溢血病因未被结局记载，claims不满。"),
 "H21M-fa0c93e8": (2.0, 1.5, 0.0, "未被录取方向全合；结局系分数第一却因代码写错成绩作废，与通知单无名表述近似而路径不同；预测断语本身无应期，timing记0。"),
 "H21M-fa6edba8": (2.0, 2.0, 0.0, "手机未丢、忘在办公室、就在抽屉里三断全合，次日果然在办公桌抽屉找到；预测断语本身无应期，timing记0。"),
 "H21M-febb785b": (2.0, 1.5, 2.0, "所断最晚5月20日痊愈出院，实际5月20日上午拆线出院，应期精确；不留后遗症一节未被结局明确记载。"),
}

with open(PACKET, encoding="utf-8") as f:
    packet = json.load(f)
ids = [e["anon_id"] for e in packet]
assert set(ids) == set(S.keys()), (set(ids) ^ set(S.keys()))
assert len(ids) == 25

rows = []
for aid in ids:
    d, c, t, reason = S[aid]
    total = d + c + t
    rows.append({"anon_id": aid, "direction": d, "claims": c, "timing": t,
                 "total": total, "pass": total >= 4, "reason": reason})

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

# 回读自验
lines = open(OUT, encoding="utf-8").read().splitlines()
assert len(lines) == 25, len(lines)
seen = set()
for ln in lines:
    o = json.loads(ln)
    assert set(o.keys()) == {"anon_id", "direction", "claims", "timing", "total", "pass", "reason"}, o.keys()
    seen.add(o["anon_id"])
    for k in ("direction", "claims", "timing"):
        v = o[k]
        assert 0 <= v <= 2 and (v * 2) == int(v * 2), (k, v)
    assert o["total"] == o["direction"] + o["claims"] + o["timing"]
    assert o["pass"] == (o["total"] >= 4)
assert seen == set(ids)
print("OK rows=25 bytes=%d npass=%d" % (os.path.getsize(OUT), sum(1 for r in rows if r["pass"])))
