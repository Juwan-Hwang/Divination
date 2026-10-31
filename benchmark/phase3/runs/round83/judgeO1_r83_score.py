#!/usr/bin/env python3
"""R83 holdout27 judgeO1 (ours, first view) scoring writer.
Writes judgeO1.jsonl in batches with assertions, then read-back verification.
"""
import json

PACKET = "/home/hatch/workspace/divination/benchmark/phase3/runs/round83/acceptance/judging/packet-ours.json"
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round83/acceptance/judging/judgeO1.jsonl"

ROWS = [
 {"anon_id":"H27O-080483be","direction":0.5,"claims":0.5,"timing":1.0,
  "reason":"断本日晴无雨，结局上午晴而未时末起转阴下雨、申时细雨、酉时雨大，主断雨象落空，仅上午晴合；云多不落雨之断语被结局直接推翻；时点同在本日故timing记1。"},
 {"anon_id":"H27O-09012bbe","direction":0.0,"claims":0.5,"timing":0.0,
  "reason":"断升省重点办不成，结局6月10日七中即获省政府正式批准，方向全反；仅校长仍在任一节合，余审批伏吟无果、真因非查账等皆不合；断一年内无批文而数日即批准，应期全错。"},
 {"anon_id":"H27O-0fccb311","direction":1.5,"claims":1.5,"timing":1.0,
  "reason":"经营实业老板主断合（鞋厂厂主），行业细目土金水行当与鞋业不尽合；火灾类象推测获结局印证（烧尽货物、厂房倒、损失2000多万），妻家、健康等子断语未被结局记载不得满分；结局未明示火灾年份、且辰运被指不好与断中高峰窗有出入，timing记1。"},
 {"anon_id":"H27O-12c27832","direction":2.0,"claims":1.5,"timing":1.5,
  "reason":"断找不到，结局半个多月后仍未找到，方向全合；被人拾走不还等辅助子断语未被结局记载，claims不给满分；约一月内确认无望与半月余未找到大体相合。"},
 {"anon_id":"H27O-1509f998","direction":0.0,"claims":0.0,"timing":1.0,
  "reason":"断考试可通过，结局差20分未能出成，方向与各断语俱反；结局无可核时点，timing记1。"},
 {"anon_id":"H27O-15e49d0e","direction":2.0,"claims":1.5,"timing":1.5,
  "reason":"断能打赢，结局三个多月努力后1998年9月胜诉、买下地皮并办妥手续，方向全合；行政阻挠等过程子断语未尽载于结局；断约五个月、秋冬之交，实际三个多月、9月，季节合而月数偏早，timing记1.5。"},
 {"anon_id":"H27O-179b928c","direction":2.0,"claims":1.5,"timing":1.0,
  "reason":"正规单位财务文职主断全合：国家政府单位、原做会计后做审计、科级且近两年升副科；婚姻经工作或长辈牵线、夫性刚、健康等子断语未被结局记载；结局无可核时点（运档升职坐标无从核对），timing记1。"},
 {"anon_id":"H27O-2cf13243","direction":2.0,"claims":1.0,"timing":0.5,
  "reason":"断能找回，结局第六天晚被拾者来电领回，方向合；方位断东北而拾包火车站在家南边、非被盗自遗之机制仅部分合，现金4300元不见与其余物品齐全两节正合；断第三日找回而实际第六日，主坐标明显偏离。"},
 {"anon_id":"H27O-30ae91b9","direction":1.5,"claims":1.5,"timing":1.0,
  "reason":"商界经营管理落点合，佛具玉器生意与餐饮调料生意并见，酒水调味之缘一节正中；官非破财之断与2006年撞人诉讼赔十余万、11月立冬后结案相合，妻性、头胎等仅部分被结局记载；结局无可核时点（运档坐标与年份对应无从核对），timing记1。"},
 {"anon_id":"H27O-47fad9cf","direction":2.0,"claims":0.5,"timing":1.0,
  "reason":"断能找到，结局9月17日下午发现赃车并抓贼找回，方向合；但断非销赃远遁、借故扣放、询问周边寻回，与结局外地青年为女友偷车、由妻兄抓贼的事实多处不合；结局无可核时点（相对起局日数无从核对），timing记1。"},
 {"anon_id":"H27O-51d22c8f","direction":0.0,"claims":0.0,"timing":1.0,
  "reason":"断富重于贵、官只藏不显、不以仕途高位为归，结局命主曾任国家财政部长，方向与断语俱反；结局无可核时点，timing记1。"},
 {"anon_id":"H27O-580ca465","direction":2.0,"claims":1.5,"timing":1.0,
  "reason":"断能平安渡过，结局其夫被公检法放回家，方向合；官非文书周折一节与被公检法处理相合，破财托人等子断语未被结局记载；结局无可核时点（仅记农历五月释放、相对起局间隔无从核对），timing记1。"},
 {"anon_id":"H27O-585ddafb","direction":1.5,"claims":1.0,"timing":2.0,
  "reason":"断次日有雨合，但雨量不大、阵雨之量级与结局不合：次日丑时起雨越下越大、雷雨强风、酉时再来戌时止；次日时点正中，timing记2。"},
 {"anon_id":"H27O-5e3efc00","direction":1.0,"claims":1.0,"timing":1.0,
  "reason":"第一病位肾水泌尿未被结局记载；第二病位脾胃代谢之糖尿病正中且严重、兼症心系之高血压心脏病眼底出血亦中，病位主次倒置故方向、claims各记1；做中医推拿开诊所与金水服务职事仅部分合；结局无可核时点，timing记1。"},
 {"anon_id":"H27O-713e640d","direction":2.0,"claims":1.5,"timing":1.5,
  "reason":"断耳环在家中，结局下午5点30分在家中床上找到，方向合；床边一节正中、自己遗忘之由亦合，东北向柜桌等细目未被结局记载；当日申时前后与17:30大体相合（已入酉时初），timing记1.5。"},
 {"anon_id":"H27O-724cc788","direction":1.5,"claims":1.0,"timing":1.0,
  "reason":"自营经营得财与合伙分财败点大体合：结局手机器材业高管、前几日刚与朋友谈判签约、控股归投资多的一方；工程地产仓储行当细目与手机器材不合，学历单位经历仅部分合，妻、健康子断语未载；结局无可核时点（运档坐标无从核对），timing记1。"},
 {"anon_id":"H27O-78f344da","direction":0.0,"claims":0.0,"timing":1.0,
  "reason":"断鹦鹉会回来，结局未回，方向与断语俱反；结局无可核时点，timing记1。"},
 {"anon_id":"H27O-7c689114","direction":1.0,"claims":1.0,"timing":1.0,
  "reason":"主断普通职事安身未被结局正面记载；夫缘一节与结局相合：首任男友为离婚者、现男友另有同居女友且明言不想结婚，聚少离多、婚缘薄之象成立；工作迁动、子女、健康诸子断语未被结局记载；结局无可核时点（运档坐标无从核对），timing记1。"},
 {"anon_id":"H27O-a51bfff0","direction":2.0,"claims":1.5,"timing":2.0,
  "reason":"断丈夫会归，结局于丁亥日亥时回来，方向合；回老家姐姐家住数日与有人接应之象仅部分合，余子断语未尽载；亥日亥时应期正中，timing记2。"},
 {"anon_id":"H27O-ad397aa9","direction":2.0,"claims":1.0,"timing":2.0,
  "reason":"断本日外出清理垃圾平安无大碍，结局在湖畔从早到晚顶风清理、无祸事记载，方向合；同伴摩擦、手足磕碰等子断语未被结局记载，劳累奔波与顶风大冷相合；本日时点正中，timing记2。"},
 {"anon_id":"H27O-b43ae186","direction":2.0,"claims":1.5,"timing":1.0,
  "reason":"断不能成行，结局护照办不下来未能成行、与预测一致，方向合；省与国务院对台办控制严与断中手续关机制相合，会期细节未被结局记载；结局无可核时点，timing记1。"},
 {"anon_id":"H27O-bbe34e92","direction":2.0,"claims":1.5,"timing":1.0,
  "reason":"断车可找回，结局公安追捕获贼、车找回并获赔修理费990元，方向合；近处一节合（石井村距家约六华里）、磕碰痕迹合（撞车受损），但未远走停置之断与贼骑车逃窜不合；结局无可核时点（相对起局日数无从核对），timing记1。"},
 {"anon_id":"H27O-d038c737","direction":2.0,"claims":1.5,"timing":1.0,
  "reason":"最具体职业断私人保镖正中、且非公门正编亦合，方向合；因打架受牵连被拘留一月与伤讼风险一节相合，怀上后结婚生女与晚婚财薄等子断语不合或未载，身世父母住院诸项非断中所及；结局无可核时点（运档坐标无从核对），timing记1。"},
 {"anon_id":"H27O-d4fb39e8","direction":0.5,"claims":0.5,"timing":1.0,
  "reason":"断母病可愈，结局仅载病症果如所测、神经衰弱二十年兼轻微心肌炎，缠绵一节合而转愈未见记载，方向、claims各记0.5；结局无可核时点（未载好转时点），timing记1。"},
 {"anon_id":"H27O-df7c3529","direction":0.0,"claims":0.5,"timing":1.0,
  "reason":"断羊肉不可吃、食则病，结局吃了羊肉的人平安无事，方向全反；仅羊肉来历异常（高山路边旱井所捡整只羊）与断中肉带病气之取材背景相合，claims记0.5；结局无可核时点，timing记1。"},
 {"anon_id":"H27O-e3d80ed4","direction":1.5,"claims":1.0,"timing":1.5,
  "reason":"断次日有雨后转晴，结局次日上午阴、九点左右小雨不久即止，雨象合；下午阴而非转晴，远段断语不合；雨在次日上午、旋止与近段时序大体合，timing记1.5。"},
 {"anon_id":"H27O-f649bf54","direction":0.0,"claims":0.0,"timing":1.0,
  "reason":"断杏坛立名、文化教育正格、非商场之命，结局其人做木材生意，方向与断语俱反；结局无可核时点，timing记1。"},
]

def main():
    with open(PACKET, encoding="utf-8") as f:
        packet = json.load(f)
    packet_ids = [r["anon_id"] for r in packet]
    assert len(packet_ids) == 27, len(packet_ids)
    assert [r["anon_id"] for r in ROWS] == packet_ids, "anon_id order mismatch vs packet"

    batches = [ROWS[i:i+9] for i in range(0, 27, 9)]
    assert len(batches) == 3
    written = 0
    with open(OUT, "w", encoding="utf-8") as f:
        for bi, batch in enumerate(batches):
            for r in batch:
                total = r["direction"] + r["claims"] + r["timing"]
                row = {
                    "anon_id": r["anon_id"],
                    "direction": r["direction"],
                    "claims": r["claims"],
                    "timing": r["timing"],
                    "total": total,
                    "pass": total >= 4,
                    "reason": r["reason"],
                }
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
                written += 1
            f.flush()
            assert written == (bi + 1) * 9, written
    print("written", written)

    # read-back verification
    with open(OUT, encoding="utf-8") as f:
        lines = [ln for ln in f.read().splitlines() if ln.strip()]
    assert len(lines) == 27, len(lines)
    npass = 0
    for i, ln in enumerate(lines):
        o = json.loads(ln)
        assert list(o.keys()) == ["anon_id","direction","claims","timing","total","pass","reason"], o.keys()
        assert o["anon_id"] == packet_ids[i]
        assert abs(o["total"] - (o["direction"] + o["claims"] + o["timing"])) < 1e-9
        assert o["pass"] == (o["total"] >= 4)
        for k in ("direction","claims","timing"):
            v = o[k]
            assert 0 <= v <= 2 and abs(v * 2 - round(v * 2)) < 1e-9, (k, v)
        npass += 1 if o["pass"] else 0
    print("verify ok: lines=27 pass=", npass)

if __name__ == "__main__":
    main()
