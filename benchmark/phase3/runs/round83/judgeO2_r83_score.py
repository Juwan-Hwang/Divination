#!/usr/bin/env python3
"""R83 holdout27 judgeO2 scoring writer. Batches append + assertions."""
import json, os

OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round83/acceptance/judging/judgeO2.jsonl"
PACKET = "/home/hatch/workspace/divination/benchmark/phase3/runs/round83/acceptance/judging/packet-ours.json"

def row(anon_id, d, c, t, reason):
    total = d + c + t
    return {"anon_id": anon_id, "direction": d, "claims": c, "timing": t,
            "total": total, "pass": total >= 4, "reason": reason}

BATCHES = [
 [
  row("H27O-080483be", 0, 0.5, 0, "断本日晴无雨，结局上午晴后未时末转阴下雨、酉时雨大，主方向反；仅上午晴与云多得部分印证；应期虽为本日但所断晴象未成，timing 0。"),
  row("H27O-09012bbe", 0, 0.5, 0, "断升省重点办不成，结局6月10日即获省政府正式批准，主方向反；仅校长仍任职一条合；所断一年内无批文与数日即批相反，timing 0。"),
  row("H27O-0fccb311", 1.5, 1.5, 1.5, "结局自述开鞋厂为企业经营者，与经营成事主断合；2008火灾烧毁货物厂房、损失二千万与低置信火险推测及该年大动象合；妻、健康等子断语结局未载，不给满分；年档主坐标与火灾之年大体对应。"),
  row("H27O-12c27832", 2, 1.5, 1.5, "断找不到，结局半个多月后仍未找到，方向全合；被人拾走等子断语结局未载，不给满分；月档内半个多月确认无望，与约一月主坐标近，timing 1.5。"),
  row("H27O-1509f998", 0, 0, 1, "断考试可通过，结局差20分未能出成，方向与断语全反；结局无可核时点，timing 记 1。"),
  row("H27O-15e49d0e", 2, 1.5, 1.0, "断原告方胜诉并办下手续，结局三月余努力后1998年9月胜诉、买地办妥手续，方向全合；行政阻挠等过程子断语未逐项载明，不给满分；所断约五个月秋冬交，实际三月余9月，分晓偏早，timing 1.0。"),
  row("H27O-179b928c", 2, 1.0, 1, "断正规单位财务文职，结局国家政府单位科级、原会计后审计，方向全合且职业断精准；为人、夫星、健康等子断语多未载，claims 1.0；升职应期与运档对应无可核，结局无可核时点，timing 记 1。"),
  row("H27O-2cf13243", 2, 1.0, 0.5, "断包可找回，结局第六天被火车站青年拾到后领回，方向合；现金四千三百元果不见、拾交而回合，但方位断东北而实际火车站在家南边、停置低处未载，claims 1.0；主坐标第三日，实际第六日，timing 0.5。"),
  row("H27O-30ae91b9", 1.5, 1.5, 1.0, "结局为商界经营者（佛具玉器兼麻辣烫调料生意），与偏商界经营、调味类象合；官非破财一段亦与是非断语部分相合；学历妻女等子断语多未对应或未载，claims 1.5；运档与结局年份对应无据可核，timing 1.0。"),
 ],
 [
  row("H27O-47fad9cf", 2, 0.5, 1, "断车能找回，结局9月17日赃车被发现并抓贼找回，终局方向合；但断非盗远遁、暂置扣放，与实际被外地打工者偷车相反，claims 0.5；结局仅给日期无起局日可比，结局无可核时点，timing 记 1。"),
  row("H27O-51d22c8f", 0, 0, 1, "断富重于贵、官只藏不显不以仕途为归，结局命主曾任国家财政部长，主方向与断语全反；结局无可核时点，timing 记 1。"),
  row("H27O-580ca465", 2, 1.0, 1.5, "断丈夫平安渡过难关，结局其夫被公检法放回家，方向合；破财托人等子断语未载，claims 1.0；所断午月内转机，实际阴历五月（午月）放回，timing 1.5。"),
  row("H27O-585ddafb", 2, 0.5, 2, "断次日有雨，结局次日丑时起雨，方向合；但断雨量不大只作阵雨，实际雨越下越大、雷雨强风延续至戌时，claims 0.5；次日全日窗口全中，timing 2。"),
  row("H27O-5e3efc00", 1.0, 1.0, 1, "主断病位肾水第一、脾胃第二、心为兼症，结局高血压心脏病与糖尿病严重、眼底出血——心系与血糖系合但第一病位肾泌尿未载，方向与断语各部分合；运档应期无据可核，结局无可核时点，timing 记 1。"),
  row("H27O-713e640d", 2, 1.5, 1.5, "断耳环在家中床边角翻找可见，结局下午5点半在家中床上找到，方向全合；东北向、柜桌等子项未全载，claims 1.5；当日申时前后与实际17时半近，timing 1.5。"),
  row("H27O-724cc788", 1.0, 1.0, 1, "主断自营工程实业起家之富命，结局为手机器材行业高管而非自营、行当亦不合，方向部分合（管理位、合伙控股谈判与合伙分隙断语部分相应）；妻、健康子断语未载，claims 1.0；运档与2002、2003年对应无据可核，timing 1.0。"),
  row("H27O-78f344da", 0, 0, 1, "断鹦鹉会回来，结局未回，方向与断语全反；结局无可核时点，timing 记 1。"),
  row("H27O-7c689114", 1.0, 0.5, 1, "主断平常命仅关系段得验：结局男友另有同住女友且明言不想结婚，与夫缘薄、聚少离多部分相应；工作、技能、子女、健康诸断语结局均未载，claims 0.5；运档与2000年对应无据可核，timing 1.0。"),
 ],
 [
  row("H27O-a51bfff0", 2, 1.5, 2, "断丈夫会归，结局丁亥日亥时到家、在姐姐家住数日与有人接应之象部分合，方向全合；归途已动等细节未载，claims 1.5；亥日亥时与主坐标全中，timing 2。"),
  row("H27O-ad397aa9", 2, 1.0, 2, "断本日外出清理垃圾平安无大碍，结局湖畔从早到晚顶风清理、无事故记载，方向合；劳累奔波合，小摩擦磕碰未载，claims 1.0；本日窗口全中，timing 2。"),
  row("H27O-b43ae186", 2, 1.5, 1, "断赴台卡在手续、去不成，结局护照办不下来未能成行，方向全合；意愿邀请等子断语未载，claims 1.5；结局无可核时点，timing 记 1。"),
  row("H27O-bbe34e92", 2, 1.0, 1, "断摩托车可找回，结局公安追捕抓贼、车经诉讼获修理赔偿，终局合且官方介入、车有损坏合；但断未被远走藏置，与贼骑车逃窜被撞获不合，claims 1.0；结局仅给7月24日无起局日可比，结局无可核时点，timing 记 1。"),
  row("H27O-d038c737", 2, 1.5, 1, "主断私人保镖非公门正编，结局自述正是私人保镖，方向全合且职业断精准；师承、财路、妻缘等子断语多未载或未对应，claims 1.5；结局无可核时点，timing 记 1。"),
  row("H27O-d4fb39e8", 0, 0.5, 1, "断母亲病可愈、午日明显好转，结局仅载神经衰弱二十年、轻微心肌炎之病况，无痊愈或好转记载，方向不予分；病势缠绵一条合，claims 0.5；结局无可核时点，timing 记 1。"),
  row("H27O-df7c3529", 0, 0, 1, "断羊肉不可吃、食则当日病扰，结局食者平安无事，主方向与断语全反；结局无可核时点，timing 记 1。"),
  row("H27O-e3d80ed4", 1.0, 1.0, 1.5, "断次日有雨后转晴，结局次日上午阴、九点左右小雨不久即止，有雨与速止合，但下午仍阴未转晴，方向与断语各部分合；次日上午落雨时序近，timing 1.5。"),
  row("H27O-f649bf54", 0, 0, 1, "主断杏坛教育立名，结局本人实做木材生意，主方向与职业断语全反；结局无可核时点，timing 记 1。"),
 ],
]

def check(r):
    assert set(r.keys()) == {"anon_id","direction","claims","timing","total","pass","reason"}, r
    for k in ("direction","claims","timing"):
        assert 0 <= r[k] <= 2 and (r[k]*2) == int(r[k]*2), r
    assert r["total"] == r["direction"] + r["claims"] + r["timing"], r
    assert r["pass"] == (r["total"] >= 4), r

with open(PACKET, encoding="utf-8") as f:
    packet_ids = [x["anon_id"] for x in json.load(f)]
assert len(packet_ids) == 27

if os.path.exists(OUT):
    os.remove(OUT)

written = []
for i, batch in enumerate(BATCHES, 1):
    with open(OUT, "a", encoding="utf-8") as f:
        for r in batch:
            check(r)
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
            written.append(r["anon_id"])
    with open(OUT, encoding="utf-8") as f:
        lines = f.read().splitlines()
    assert len(lines) == len(written), (i, len(lines), len(written))
    for line, aid in zip(lines, written):
        assert json.loads(line)["anon_id"] == aid
    print(f"batch {i} ok, cumulative lines={len(lines)}")

assert written == packet_ids, "anon_id order mismatch with packet"
print("all ok:", len(written), "passes:", sum(1 for b in BATCHES for r in b if r["pass"]))
