#!/usr/bin/env python3
import json, os
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round83/acceptance/judging/judgeM2.jsonl"
PKT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round83/acceptance/judging/packet-master.json"
rows = [
 ("H27M-2901fdcd",2,2,2,"失而复得、约28天、9月17日壬申日找到均与结局逐项吻合，应期精确命中。"),
 ("H27M-3043f174",2,1.5,1.5,"低学历、头胎女、餐饮相关第二生意及2006年因他人惹官司破财均印证；辛运结婚、酉时生、土杂金属行业等子断语未被结局记载或不合，不得满分；2006年时间坐标命中。"),
 ("H27M-339106a8",2,1.5,2,"晴转阴、濛濛小雨、雷声均印证；结局酉时雨变大超出小雨断语，故claims不给满分；本日时段进程吻合。"),
 ("H27M-3af2c2cf",2,1.5,1.5,"2000年男友离婚、现男友另有同居女友且不想结婚均印证；无正式婚姻及历任皆已婚等子断语未被结局逐条记载，不得满分；2000/2001年坐标命中。"),
 ("H27M-4013381b",2,2,2,"能找到、第六天在八天内、南边三华里、年轻男子拾包、4300元现金不见而余物齐全，全部逐项印证。"),
 ("H27M-5704832a",2,2,0,"母亲心脏病断语被轻微心肌炎印证；预测断语本身无应期，timing记0。"),
 ("H27M-58840978",2,2,2,"私人保镖式执法、送人抚养、2002年奉子成婚生女、生父肝癌、2000年受牵连因女人被拘留，均逐项印证，两处年份命中。"),
 ("H27M-730001a0",2,1.5,0,"官司终胜印证；中间阻力一节结局仅记三个多月努力、未明确记载，不得满分；预测断语本身无应期，timing记0。"),
 ("H27M-7c964fa4",2,2,2,"次日上午阴、九点左右小雨即止、下午阴有风，与小雨且有风有雨断语吻合，次日应期命中。"),
 ("H27M-7e39095f",2,2,0,"难回之象被后果未回直接印证；预测断语本身无应期，timing记0。"),
 ("H27M-86c5286f",1.5,1,0,"做木材生意印证，对象落泪仅侧面支持婚姻情感断语；想离离不了、被男人牵制、无真情等子断语未被结局记载，不得高分；预测断语本身无应期，timing记0。"),
 ("H27M-8a24c1c6",0,0,0,"断八至十二天癸日可找回，结局半个多月仍未找到，方向、断语与应期全部落空。"),
 ("H27M-8a938ce9",2,1.5,1.5,"国家单位科级、1999/2000年升副科、生女、原做会计均印证；25/26岁结婚一节结局未载年龄不得满分；调动年份命中。"),
 ("H27M-9989fceb",2,1.5,2,"七中升重点终成、校长职务不动印证；中层阻力、找高层、纪检查账无问题等子断语未被结局记载，不得满分；6月22日前且下周四批准，结局6月10日周四批准，应期精确。"),
 ("H27M-9a102b64",2,2,2,"次日雷雨交加印证，结局另有强风不与断语冲突；次日应期命中。"),
 ("H27M-9a3829b3",2,1.5,0,"高山路边干涸处捡羊大体印证，但断语作干涸水池、结局作旱井，地点形态有出入；预测断语本身无应期，timing记0。"),
 ("H27M-9d5452fe",2,2,2,"丈夫会回且丁亥日有可能，结局丁亥日亥时回来，应期精确命中。"),
 ("H27M-a14c9666",2,1,0,"考试未通过结局方向印证；因人做手脚一节结局仅记本人觉得分数不对、无可奈何，未被证实，故claims只给1；预测断语本身无应期，timing记0。"),
 ("H27M-a4baa2d4",2,2,1.5,"开鞋厂、2000年破大财、火灾且厂房倒塌损失巨大均印证；时间坐标为年份级命中。"),
 ("H27M-a5024dc2",2,2,0,"湖边清理垃圾、逆风受风吹之苦均被湖畔顶风工作印证；预测断语本身无应期，timing记0。"),
 ("H27M-b2f36e8b",2,1.5,1.5,"丈夫被公检法抓后无牢狱、阴历五月放回印证；单位领导、经济问题两节未被结局记载，不得满分；五月应期为月份级命中。"),
 ("H27M-c032fdad",1.5,1,0,"命主曾任财政部长，与掌财权机构及本人掌更大权力方向大体相合，但断语为残片式分析、具体对应含糊；预测断语本身无应期，timing记0。"),
 ("H27M-dc3c435f",2,1.5,0,"三名青年盗车、先南后西北、约六华里、被撞伤、起诉获赔修理费均印证；身高断为172至175、结局仅记均在一米七以上，精确区间未被记载，不得满分；预测断语本身无应期，timing记0。"),
 ("H27M-de68de57",2,1.5,1,"在家中找到印证；东北方向一节结局未记载、8小时内亦无起算点可核，不得满分；结局无可核时点，timing记1。"),
 ("H27M-ea8361f9",2,1.5,1.5,"低学历、2002/2003年参加工作、做业务后任高管、手机器材行业、投资为小股东由对方掌控均印证；20岁前结束学业、流动型两节未被结局记载，不得满分；入职年份命中。"),
 ("H27M-ed0b9e38",1.5,1,0,"糖尿病严重印证，从事中医推拿开诊所与医生断语大体相近；贪财势利不择手段、医术还可以等子断语未被结局记载，不得高分；预测断语本身无应期，timing记0。"),
 ("H27M-fdd075aa",2,2,0,"护照办不下来、未能成行与结局完全吻合；预测断语本身无应期，timing记0。"),
]
with open(PKT, encoding="utf-8") as f:
    pkt = json.load(f)
anon = [p["anon_id"] for p in pkt]
assert [r[0] for r in rows] == anon, "anon_id order mismatch"
assert len(rows) == 27
if os.path.exists(OUT):
    os.remove(OUT)
# segmented append, 3 batches of 9, assert after each
for start in range(0, 27, 9):
    batch = rows[start:start+9]
    with open(OUT, "a", encoding="utf-8") as f:
        for aid, d, c, t, reason in batch:
            total = d + c + t
            obj = {"anon_id": aid, "direction": d, "claims": c, "timing": t,
                   "total": total, "pass": total >= 4, "reason": reason}
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")
    with open(OUT, encoding="utf-8") as f:
        cur = f.readlines()
    assert len(cur) == start + len(batch), f"batch count fail at {start}"
# final reread verification
with open(OUT, encoding="utf-8") as f:
    lines = f.readlines()
assert len(lines) == 27
np = 0
for i, ln in enumerate(lines):
    o = json.loads(ln)
    assert set(o.keys()) == {"anon_id","direction","claims","timing","total","pass","reason"}
    assert o["anon_id"] == anon[i]
    assert abs(o["total"] - (o["direction"]+o["claims"]+o["timing"])) < 1e-9
    assert o["pass"] == (o["total"] >= 4)
    for k in ("direction","claims","timing"):
        assert 0 <= o[k] <= 2 and (o[k]*2) == int(o[k]*2)
    np += 1 if o["pass"] else 0
print(f"OK lines=27 pass={np} bytes={os.path.getsize(OUT)}")
