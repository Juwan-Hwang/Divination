#!/usr/bin/env python3
"""R83 holdout27 judgeM1 (master packet) scoring writer.
Scores were determined by manual per-claim verification against outcome_record.
Writes judgeM1.jsonl in batches with assertions, then re-reads and verifies.
"""
import json

PACKET = "/home/hatch/workspace/divination/benchmark/phase3/runs/round83/acceptance/judging/packet-master.json"
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round83/acceptance/judging/judgeM1.jsonl"

# (anon_id, direction, claims, timing, reason)
SCORES = [
    ("H27M-2901fdcd", 2.0, 2.0, 2.0,
     "失而复得、壬申日9月17日找回、约28天三项全中，结局载9月17日下午发现赃车并抓到贼。"),
    ("H27M-3043f174", 1.5, 1.5, 1.5,
     "学历低、1998年结婚、头胎女孩、餐饮相关第二生意、2006年因他人惹是非官司破财十来万均验；但行业断为土杂金属与结局佛具玉器不符，故claims扣分；2006年应期命中。"),
    ("H27M-339106a8", 2.0, 2.0, 1.5,
     "晴转阴、濛濛小雨、有雷声逐条与结局上午晴、未时转阴细雨、远处雷声吻合；断语只给本日无具体时段，timing记1.5。"),
    ("H27M-3af2c2cf", 2.0, 1.5, 1.5,
     "2000年男友离婚、现男友另有同居女友且不想结婚均验；但无正式婚姻及历任皆已婚/离婚等子断语未被结局逐一记载，claims不得满分；年份窗口命中2000年。"),
    ("H27M-4013381b", 2.0, 2.0, 2.0,
     "包找回、八天内（第六天）、家南三华里、年轻男子拾包、四千三百元现金丢失而余物齐全，逐条全验。"),
    ("H27M-5704832a", 2.0, 1.5, 0.0,
     "其母有心脏问题方向命中，结局为轻微心肌炎（另有神经衰弱二十年未被断及），claims记1.5；预测断语本身无应期，timing记0。"),
    ("H27M-58840978", 2.0, 2.0, 2.0,
     "私人性质执法类职业（私人保镖）、幼年送人、2002年奉子成婚生女、今年生父肝病住院、2000年受女人牵连短暂拘留，逐条全验，年份应期全中。"),
    ("H27M-730001a0", 2.0, 1.5, 0.0,
     "官司终胜诉命中，结局载经三个多月努力胜诉与中间有阻力大体相符，但道理全在己方未被结局记载，claims记1.5；预测断语本身无应期，timing记0。"),
    ("H27M-7c964fa4", 2.0, 2.0, 2.0,
     "第二天下雨、为小雨、有风，结局载次日九点左右小雨不久即止、下午阴有风，逐条命中，应期次日命中。"),
    ("H27M-7e39095f", 2.0, 1.5, 0.0,
     "难回之结论与结局未回吻合；断语仅此一结论性判断，技术推演部分非结局可核子断语，claims记1.5；预测断语本身无应期，timing记0。"),
    ("H27M-86c5286f", 1.0, 1.0, 0.0,
     "做木材生意命中；婚姻不好、想离离不了、为情所困、得不到真情等子断语均未被结局记载（仅载其落泪），claims记1；预测断语本身无应期，timing记0。"),
    ("H27M-8a24c1c6", 0.0, 0.0, 0.0,
     "断八至十二天癸日可找回驾驶证，结局半个多月仍未找到，方向、断语、应期全反。"),
    ("H27M-8a938ce9", 2.0, 1.5, 1.5,
     "国家单位科级、1999/2000年升副科、生女孩、原做会计均验；25/26岁结婚一断结局未载年龄无法核验（仅载1997年结婚），claims与timing各记1.5。"),
    ("H27M-9989fceb", 2.0, 1.5, 2.0,
     "七中升重点获批、校长职务不动均验，且应期下周四6月10日批准正中快速档；但中层阻力、找更高领导、纪检查账无问题等子断语未被结局记载，claims记1.5。"),
    ("H27M-9a102b64", 2.0, 2.0, 2.0,
     "次日雷雨交加，结局载第二天丑时起雨大作、雷雨交加并强风，逐条命中，应期次日命中。"),
    ("H27M-9a3829b3", 2.0, 1.5, 0.0,
     "羊在高山路边干涸水池中捡到，结局为高山路边旱井中捡到整只羊，地点实质命中而池与井略有出入，claims记1.5；预测断语本身无应期，timing记0。"),
    ("H27M-9d5452fe", 2.0, 2.0, 2.0,
     "丈夫会回来、丁亥日有可能，结局载其夫于丁亥日亥时回来，应期精确命中。"),
    ("H27M-a14c9666", 2.0, 1.0, 0.0,
     "考试通不过命中（差20分未成行）；但因人做手脚之原因未被结局证实，结局仅载本人觉得分数不对，claims记1；预测断语本身无应期，timing记0。"),
    ("H27M-a4baa2d4", 2.0, 2.0, 2.0,
     "做穿的开厂（鞋厂）、2000年破大财、火灾与倒塌两可能竟俱现（火灾烧尽货物厂房倒了、损失两千多万），逐条全验。"),
    ("H27M-a5024dc2", 2.0, 2.0, 0.0,
     "在湖边清理环境垃圾、逆风受风吹之苦，结局载湖畔清理垃圾整日顶风又大又冷，逐条命中；预测断语本身无应期，timing记0。"),
    ("H27M-b2f36e8b", 2.0, 1.5, 2.0,
     "丈夫无牢狱之灾、阴历五月放出，结局载阴历五月被公检法放回家命中；但单位领导及经济问题被抓两子断语未被结局记载，claims记1.5；应期阴历五月精确命中。"),
    ("H27M-c032fdad", 1.5, 1.0, 0.0,
     "断语为解释性残句，大意为本人掌握管理财的权力机构，结局曾任财政部长大体相合但具体推断无从逐条核验，claims记1；预测断语本身无应期，timing记0。"),
    ("H27M-dc3c435f", 2.0, 1.5, 0.0,
     "车能找回破案、三名十八至二十五岁年轻人、先南后西北、约六华里、盗车人被撞伤、车损经诉讼获赔均验；身高断一米七二至一米七五，结局仅载均在一米七以上未逐一坐实，claims记1.5；预测断语本身无应期，timing记0。"),
    ("H27M-de68de57", 2.0, 1.5, 1.0,
     "耳环在自己家中找到命中（床上）；东北方向一断未被结局记载，claims记1.5；结局仅载下午5点30分找到、无起算时点可核八小时之限，timing记1。"),
    ("H27M-ea8361f9", 2.0, 1.5, 1.5,
     "学历不高、2002/2003年参加工作、做业务与手机器材、任高管、投资公司对方控股本人小股东均验；20岁前结束学业及流动型工作未被结局记载，claims记1.5；工作年份应期命中。"),
    ("H27M-ed0b9e38", 1.5, 1.0, 0.0,
     "易得糖尿病命中且已很严重、业医（中医推拿开诊所）大体命中；贪财吝啬势利等品性断语及医术还可以未被结局记载，claims记1；预测断语本身无应期，timing记0。"),
    ("H27M-fdd075aa", 2.0, 2.0, 0.0,
     "护照办不下来、难成行，结局载护照办不下来未能成行，逐条命中；预测断语本身无应期，timing记0。"),
]


def main():
    with open(PACKET, encoding="utf-8") as f:
        packet = json.load(f)
    packet_ids = [row["anon_id"] for row in packet]
    assert len(packet_ids) == 27, len(packet_ids)
    assert [s[0] for s in SCORES] == packet_ids, "anon_id order mismatch with packet"

    rows = []
    for anon_id, d, c, t, reason in SCORES:
        total = d + c + t
        rows.append({
            "anon_id": anon_id,
            "direction": d,
            "claims": c,
            "timing": t,
            "total": total,
            "pass": total >= 4,
            "reason": reason,
        })

    # segmented append: 3 batches of 9
    batches = [rows[0:9], rows[9:18], rows[18:27]]
    written = 0
    with open(OUT, "w", encoding="utf-8") as f:
        for bi, batch in enumerate(batches):
            for row in batch:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
                written += 1
            f.flush()
            assert written == (bi + 1) * 9, written
    assert written == 27

    # re-read self-verification
    with open(OUT, encoding="utf-8") as f:
        lines = [ln for ln in f.read().splitlines() if ln.strip()]
    assert len(lines) == 27, len(lines)
    npass = 0
    for i, ln in enumerate(lines):
        obj = json.loads(ln)
        assert list(obj.keys()) == ["anon_id", "direction", "claims", "timing", "total", "pass", "reason"], obj.keys()
        assert obj["anon_id"] == packet_ids[i], (i, obj["anon_id"])
        assert obj["total"] == obj["direction"] + obj["claims"] + obj["timing"], obj
        assert obj["pass"] == (obj["total"] >= 4), obj
        for k in ("direction", "claims", "timing"):
            v = obj[k]
            assert 0.0 <= v <= 2.0 and (v * 2) == int(v * 2), (k, v)
        npass += 1 if obj["pass"] else 0
    print(f"OK lines=27 pass={npass}")


if __name__ == "__main__":
    main()
