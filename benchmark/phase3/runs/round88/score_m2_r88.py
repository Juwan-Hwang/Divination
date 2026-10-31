# -*- coding: utf-8 -*-
"""R88 acceptance judging, seat M2 (master packet, second view).
Scores are hand-decided by the judge; this script only writes them out
in segments with assertions (count, fields, value domain, total/pass recompute).
"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "acceptance", "judging", "judgeM2.jsonl")
PACKET = os.path.join(BASE, "acceptance", "judging", "packet-master.json")

# (anon_id, direction, claims, timing, reason)
ROWS = [
    ("H31M-052d78b7", 2.0, 2.0, 0.0,
     "携眷移居寄寓、舟破被抢、鸣官均与原断（携眷必行、舟车逢冲破、恐有见官之事）吻合；预测未给应期，timing记0。"),
    ("H31M-36766c7d", 2.0, 2.0, 2.0,
     "孩子平安、亥月出生、乙卯日出生逐项全中，日期应期精确命中。"),
    ("H31M-3d43f4d0", 2.0, 1.5, 0.0,
     "工作没调动成与「难以调动」吻合；伏合化冲等细目结局未载，claims不给满分；预测未给应期，timing记0。"),
    ("H31M-52ae3f06", 2.0, 1.0, 0.0,
     "四月见劫耗，劫掠方向如断；为首者为家人、护救在家人、不能大逞其凶等子断语结局未具体记载，claims只给部分；预测未给应期，timing记0。"),
    ("H31M-63286ec6", 1.0, 1.0, 0.0,
     "官讼羁累与阻隔应验，但「利于奏对」未兑现——本人并未赴京引见，改调松江，方向只合一半；预测未给应期，timing记0。"),
    ("H31M-72c1b47f", 2.0, 1.5, 2.0,
     "不赴武职、改岳庙读书、己酉中举、庚戌登科皆验；「二甲二十一名」结局未载，claims扣分；年份应期命中。"),
    ("H31M-7518b051", 2.0, 2.0, 2.0,
     "来岁丁父忧、三十七岁后连任、十五年后降官闲住、再八年而卒，与结局逐段吻合，应期节点均命中。"),
    ("H31M-78a13261", 2.0, 1.5, 0.0,
     "小儿果非肺炎、只是呛奶，「不药而愈」方向命中；结局未明载痊愈经过，claims给1.5；预测未给应期，timing记0。"),
    ("H31M-7fafad48", 2.0, 1.5, 0.0,
     "因弟官非逃亡、火惊亦为弟所致，兄弟致争端与火烛之惊均验；宅昏昧、化解等子断语未载，claims扣分；预测未给应期，timing记0。"),
    ("H31M-8aa30de8", 1.5, 1.0, 0.0,
     "次年酉贼破省与西方肃杀之凶方向相合；屋多人衰、冲关免阻等子断语结局未载，claims只给部分；预测未给明确应期年份，timing记0。"),
    ("H31M-8ce84f81", 2.0, 1.5, 0.0,
     "已怀孕、生女孩均验；「第三个孩子」之序位结局未载，claims扣分；预测未给出生应期，timing记0。"),
    ("H31M-9e863514", 2.0, 1.5, 1.5,
     "丧妻再娶、四任显达、遇曹姓而显、四年后自绛帐显均验；「克四妻」结局只载三妻之亡，声名西北未载，claims扣分；四年之期命中、四旬遇曹无年龄可核，timing给1.5。"),
    ("H31M-a1bef5d3", 1.0, 1.0, 0.0,
     "道路不通、贼壅塞阻行程应验；但「宜在此处结宾主谋生理以为久远之计」被结局明确判为误断，方向与断语各只合一半；预测未给应期，timing记0。"),
    ("H31M-a63c88ce", 2.0, 1.5, 0.0,
     "贼劫果至、舍远就近避于杨家得安，就近为安与动必遇贼均验；不可求财一节结局未直接验证，claims扣分；预测未给日期应期，timing记0。"),
    ("H31M-aeb7b9c9", 1.0, 0.5, 0.0,
     "怀孕信息验；但结局为流产，「胖小子」「子月出生」均未发生，断语大半落空；出生应期因流产未兑现，timing记0。"),
    ("H31M-aee4a7ed", 2.0, 1.5, 2.0,
     "午时去取果得衣物，时点精确命中；惟因不合身起争执重改后才取走，「可到手」非全无波折，claims给1.5。"),
    ("H31M-b05d2e91", 2.0, 1.5, 1.5,
     "本月生、女孩、难产均验；侄女住院一节结局未明载，claims扣分；应期只断到月且命中，timing给1.5。"),
    ("H31M-c720bbf9", 2.0, 2.0, 1.5,
     "本月、安全顺产、女孩均验，不难产亦合；应期只断到月且命中，timing给1.5。"),
    ("H31M-d0b4bf8e", 2.0, 2.0, 2.0,
     "三授奔波、妻产亡、以弟为子、四十五岁终任外州、继子不归逐项全验，四十五六岁之期命中。"),
    ("H31M-d24fe2b1", 2.0, 1.5, 0.0,
     "鼻癌、手术、维持难愈均验；小便困难、鼻涕流不出等子断语结局未载，claims扣分；预测未给应期，timing记0。"),
    ("H31M-d73d8e81", 2.0, 2.0, 2.0,
     "六月十五丁丑日、子时、生女孩，与「丑日应子时」及两日窗口精确吻合，应期命中。"),
    ("H31M-db602352", 2.0, 2.0, 1.5,
     "难产、男孩均验，交节后寅月生合「寅月生」；应期只断到月且命中，timing给1.5。"),
    ("H31M-dcb61247", 2.0, 2.0, 0.0,
     "钱果在办公室写字台下寻回，地点断语精确命中；预测未给应期，timing记0。"),
    ("H31M-de847485", 2.0, 1.5, 1.0,
     "权署兼职、得宠行不廉、纳妾、欲去不能、外路监司恳告得解任均验；贪色寻医、俸增结局未载，claims扣分；「替时自见」仅与满替节点松散对应，timing给1。"),
    ("H31M-e0469fa2", 2.0, 2.0, 1.0,
     "因丁艰阻升、父棺白蚁泥水伤坏、服满得一任而不能终任（病归、十二月卒）逐项全验；结局无可核时点（仅载十二月卒、无年份），timing记1。"),
    ("H31M-f664f742", 1.5, 1.0, 0.0,
     "「防覆坠骑乘之患」精确应验（乘轿坠而折足死）；子息难得、妻病、神像破损等众多子断语结局全未记载，claims只给部分；预测未给坠伤应期年份，timing记0。"),
    ("H31M-fcf50885", 2.0, 2.0, 0.0,
     "子宫瘤确诊、服中药而愈，病位与治法均验；预测未给应期，timing记0。"),
    ("H31M-ff003019", 2.0, 1.5, 1.5,
     "未月胎动如断；胎儿缺水之机理结局无从核验，claims扣分；应期只断到月且命中，timing给1.5。"),
]

ALLOWED = {0.0, 0.5, 1.0, 1.5, 2.0}
FIELDS = ["anon_id", "direction", "claims", "timing", "total", "pass", "reason"]


def check_row(rec, packet_ids):
    assert list(rec.keys()) == FIELDS, rec
    assert rec["anon_id"] in packet_ids, rec["anon_id"]
    for k in ("direction", "claims", "timing"):
        assert rec[k] in ALLOWED, (k, rec[k])
    total = rec["direction"] + rec["claims"] + rec["timing"]
    assert rec["total"] == total, (rec["anon_id"], rec["total"], total)
    assert rec["pass"] == (total >= 4), rec["anon_id"]
    assert isinstance(rec["reason"], str) and rec["reason"]


def main():
    with open(PACKET, "r", encoding="utf-8") as f:
        packet = json.load(f)
    packet_ids = [p["anon_id"] for p in packet]
    assert len(packet_ids) == 28, len(packet_ids)
    assert [r[0] for r in ROWS] == packet_ids, "row order/ids must match packet"

    if os.path.exists(OUT):
        raise SystemExit("output already exists; refusing to overwrite: " + OUT)

    written = 0
    seg = 7
    with open(OUT, "w", encoding="utf-8") as out:
        for start in range(0, len(ROWS), seg):
            chunk = ROWS[start:start + seg]
            for anon_id, d, c, t, reason in chunk:
                rec = {
                    "anon_id": anon_id,
                    "direction": d,
                    "claims": c,
                    "timing": t,
                    "total": d + c + t,
                    "pass": (d + c + t) >= 4,
                    "reason": reason,
                }
                check_row(rec, set(packet_ids))
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                written += 1
            out.flush()
            # per-segment assertion: recount lines on disk
            with open(OUT, "r", encoding="utf-8") as chk:
                lines = chk.read().splitlines()
            assert len(lines) == written, (len(lines), written)
            for ln in lines:
                check_row(json.loads(ln), set(packet_ids))
            print("segment ok, lines =", written)

    with open(OUT, "r", encoding="utf-8") as f:
        final = [json.loads(ln) for ln in f.read().splitlines()]
    assert len(final) == 28
    assert [r["anon_id"] for r in final] == packet_ids
    npass = sum(1 for r in final if r["pass"])
    md = sum(r["direction"] for r in final) / 28
    mc = sum(r["claims"] for r in final) / 28
    mt = sum(r["timing"] for r in final) / 28
    size = os.path.getsize(OUT)
    print(json.dumps({
        "input_count": 28, "output_lines": len(final), "pass_count": npass,
        "mean_direction": round(md, 4), "mean_claims": round(mc, 4),
        "mean_timing": round(mt, 4), "bytes": size,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
