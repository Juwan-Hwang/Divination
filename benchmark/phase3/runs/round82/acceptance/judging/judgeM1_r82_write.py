import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round82/acceptance/judging")
packet = json.loads((base/"packet-master.json").read_text(encoding="utf-8"))
packet_ids = [r["anon_id"] for r in packet]

rows = [
 ("H26M-1a9f4262",2,2,2,"次日晴转阴、有雷阵雨且雨大，结局上午晴、申时转阴电闪雷鸣大雨至次晨，方向、雷雨诸断与次日应期全合。"),
 ("H26M-1b96dd66",2,1.5,2,"事业终结与牢狱方向合，结局2005年（乙酉）被抓捕；但『最多做到2004年』结局未逐字记载何时停业，故claims不给满分；乙酉年应期命中。"),
 ("H26M-25bdd77a",2,2,2,"被骗拐、性命无忧、新余西边300公里（衡阳，断200-400公里）、第八天8月15日乙巳日归来，结局逐条全合。"),
 ("H26M-3d7e46bd",2,2,1.5,"香港永居能成、不会很快，结局已批准；应期断农历三四月，结局4月8日通知且已入辰月，大体合但结局农历标注自相矛盾，故timing扣半分。"),
 ("H26M-4e480928",2,2,2,"断次日光打雷不下雨，结局申时浓云阵阵雷声、终无一滴雨、酉时转晴，方向、断语与次日应期全合。"),
 ("H26M-5cf1031f",2,1.5,2,"断次日晴、晴间有云、很可能有雾，结局晴朗、地面有雾、未时薄云；晨间无云与『间有雲』略有出入，claims扣半分，次日应期合。"),
 ("H26M-658d1ad6",1.5,1.5,0,"病因断肿块或增生，结局为颈椎增生致痛，增生一支命中、肿块未见记载；预测断语本身无应期，timing记0。"),
 ("H26M-6aa44e8c",2,1.5,0,"断移民面试能通过，结局10月29日顺利通过；『虽有难度』结局未记载、反言顺利，故claims扣半分；预测断语本身无应期，timing记0。"),
 ("H26M-6ad2414f",2,1.5,0,"断相亲连对方脸都看不到，结局对方低头至终、未看清其脸，大体合但非全然未见人，claims扣半分；预测断语本身无应期，timing记0。"),
 ("H26M-6af342b4",2,2,2,"断在外安全、丑日必回，结局果于丑日回来且仅为出游散心，方向、断语与丑日应期全合。"),
 ("H26M-6d9a436a",2,2,0,"断二人必分手，结局果分手，单断全合；预测断语本身无应期（巳月仅见于结局），timing记0。"),
 ("H26M-6e117fd8",2,1.5,0,"断可成行、人车平安、道路阻隔、有换乘汽车之象，结局火车受阻后换乘长途汽车抵达；『两个贵人相助』结局仅载两同车人、未明言相助，claims扣半分；预测断语本身无应期，timing记0。"),
 ("H26M-7b4cc0b5",1,1,0,"断适合开店做机器机械代理，结局为钢结构公司总代理之市场部经理，代理一支近似但开店与机器机械均未合；预测断语本身无应期，timing记0。"),
 ("H26M-7bf040b4",2,1.5,1,"断与现女友必分手，结局果与原女友分手另结新欢，方向与分手断合；应期『明年』之基准年结局未载，结局无可核时点，timing记1。"),
 ("H26M-7dd62a1e",1.5,0.5,0,"断本人无大财命、靠合伙求财且得财容易，结局午运仅两年得财合计约30万元人民币与『无大财』粗合，但合伙、易得诸断结局均未记载，claims低分；预测断语本身无具体应期，timing记0。"),
 ("H26M-86ef4e61",2,2,2,"断司机被杀抛河、车被劫、约十天后找到尸，结局十天后庚午日破案并于河中找到尸、余情几乎全合，方向断语应期全合。"),
 ("H26M-878ada3a",2,1.5,1,"断人平安、私奔婚恋、西南方向、可找回，结局于市内西南小旅馆找到与南方男子同居，全程66天；两局应期20-30天与60-100天自相矛盾，66天仅合第二局，timing低分，胎产一支未见记载故claims扣半分。"),
 ("H26M-8ace669b",1,1,0,"断官职不大，结局由秘书升至某厅处长，处长属中层、与『不大』仅部分相容；预测断语本身无应期，timing记0。"),
 ("H26M-8c844402",2,1.5,0,"断当官命、掌兵权，结局为大校级军官，军官身份合，但『掌兵权』结局未明载统兵之实，claims扣半分；预测断语本身无应期，timing记0。"),
 ("H26M-9bf39c04",2,2,2,"断因车事误点约三小时、突然停车涉电，结局火车误点三小时左右、因车站突然停电，方向断语与三小时时量全合。"),
 ("H26M-c2cc97f9",1.5,1,0,"断制巳火则短寿，结局患白血病次年夏死亡，短寿方向合；但结局年份为丙子、丁丑，与断中丁巳坐标未对应，claims扣分；预测应期丁巳未见于结局记载，timing记0。"),
 ("H26M-cda76175",2,2,0,"断金融方面的官员，结局为中央银行行长，单断全合；预测断语本身无应期，timing记0。"),
 ("H26M-df660021",2,2,0,"断有惊无险、中途遇逆风，结局船中途果遇逆风、平安抵岸，断语全合；预测断语本身无应期，timing记0。"),
 ("H26M-e423130a",2,1.5,1.5,"断人在东方、平安、自己回来、二十天内归，结局在东方江阴打工后自行返家；『130里』距离结局未记载故claims扣半分，具体日断8月16日而实际8月17日晚一天，timing扣半分（二十天大框内合）。"),
 ("H26M-eea1671a",2,2,0,"断出国手续办不下来，结局层层上报后文化部门不批、护照没办成，单断全合；预测断语本身无应期，timing记0。"),
 ("H26M-f48bdc34",2,1.5,0,"断刑必伤及命主身体，结局果被炸药炸伤左手，伤身合但断语未及部位与方式、笼统，claims扣半分；预测断语本身无应期（丁卯年仅见于结局），timing记0。"),
 ("H26M-f9c8365e",2,1.5,0,"断制之不好会伤及性命，结局被高压电击死，丧命合但致死机制（申金被火克）与断语『制连体字』之对应结局未明载，claims扣半分；预测断语本身无应期，timing记0。"),
]

assert [r[0] for r in rows] == packet_ids, "order/id mismatch"
out = base/"judgeM1.jsonl"
with out.open("w", encoding="utf-8") as f:
    for anon, d, c, t, reason in rows:
        total = d + c + t
        f.write(json.dumps({"anon_id": anon, "direction": d, "claims": c, "timing": t,
                            "total": total, "pass": total >= 4, "reason": reason},
                           ensure_ascii=False) + "\n")

# self-verify
lines = out.read_text(encoding="utf-8").strip().splitlines()
assert len(lines) == 27
recs = [json.loads(x) for x in lines]
assert {r["anon_id"] for r in recs} == set(packet_ids)
for r in recs:
    assert abs(r["total"] - (r["direction"]+r["claims"]+r["timing"])) < 1e-9
    assert r["pass"] == (r["total"] >= 4)
    for k in ("direction","claims","timing"):
        assert 0 <= r[k] <= 2 and (r[k]*2) == int(r[k]*2)
n = len(recs)
print("lines", n)
print("direction_mean", sum(r["direction"] for r in recs)/n)
print("claims_mean", sum(r["claims"] for r in recs)/n)
print("timing_mean", sum(r["timing"] for r in recs)/n)
print("total_mean", sum(r["total"] for r in recs)/n)
print("pass_count", sum(1 for r in recs if r["pass"]))
