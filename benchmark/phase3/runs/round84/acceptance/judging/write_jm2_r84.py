#!/usr/bin/env python3
"""R84 holdout28 master packet - judge M2 (independent second view).
Writes judgeM2.jsonl in 3 append segments, asserting after each segment.
No overwrite/delete: refuses to run if target already exists.
"""
import json, os, sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "judgeM2.jsonl")

SEG1 = [
 {"anon_id":"H28M-02bf639c","direction":1.0,"claims":0.5,"timing":1,"total":2.5,"pass":False,"reason":"仅泛言申月出空当防，结局确有切伤中指赴医之事，危险方向部分相符；但刀伤、手指、程度等具体断语均未见于预测，申月亦无从核对。timing：结局无可核时点"},
 {"anon_id":"H28M-04bf702c","direction":2,"claims":2,"timing":2,"total":6,"pass":True,"reason":"断今年南方有大水灾且必在午月，结局为午月长江下游特大洪水，方向、规模、地域与月份逐项印证"},
 {"anon_id":"H28M-05c87204","direction":2,"claims":2,"timing":2,"total":6,"pass":True,"reason":"断1999或2000年离婚，结局为2000年离婚；第二任妻子年岁小很多且现已有了，结局确认确实如此"},
 {"anon_id":"H28M-118877d4","direction":2,"claims":1.5,"timing":1,"total":4.5,"pass":True,"reason":"初断公安局官员被否、当过兵命中，其后银行官员获确认；大麻烦与经济问题方向命中，金额断六百万/六千万二选，结局为六千万挪用公款案命中；但牢狱与2008年未在结局中明载。timing：结局无可核时点"},
 {"anon_id":"H28M-183f72ec","direction":2,"claims":1.5,"timing":1.5,"total":5,"pass":True,"reason":"当兵后入国企、中层干部、纺织企业、计划生育下只有一女儿、长子身份均获确认；唯兄弟姐妹断四人而实为三人，故claims不给满分。父亲去世六七年获『太准了』反馈，应期大体命中"},
 {"anon_id":"H28M-2588b75a","direction":2,"claims":2,"timing":2,"total":6,"pass":True,"reason":"第一次婚姻2004年结束、第二次婚姻名存实亡维持现状、女儿不在身边均获确认，反馈称所断一年不差、正于2004年离异"},
 {"anon_id":"H28M-2d8db2f9","direction":2,"claims":1.5,"timing":0,"total":3.5,"pass":False,"reason":"早婚、丈夫离过婚、亲生两女、婚姻中途出问题、丈夫亡故均命中；但断丈夫带来两男，结局明确丈夫无孩子、本人并无儿子，该子断语落空。timing：预测断语本身无应期"},
 {"anon_id":"H28M-3491ebd1","direction":2,"claims":1.5,"timing":0,"total":3.5,"pass":False,"reason":"断有可能回了老家，结局当日午时接电话得知确已回老家，核心一断命中；惟断语带『有可能』且老家在东南方系问答所得，非预测本身。timing：预测断语本身无应期"},
 {"anon_id":"H28M-55339daa","direction":1.5,"claims":1.5,"timing":1.5,"total":4.5,"pass":True,"reason":"断去年冬天出现一个有别人的男人、不可能结婚，结局自认去年爱上一个有家室的人，与之相符且称什么都看出来了；但2006年谈对象及明年结婚未被结局记载。去年/去年冬天的时间坐标命中"},
]

SEG2 = [
 {"anon_id":"H28M-5c7ab651","direction":1.5,"claims":1,"timing":0,"total":2.5,"pass":False,"reason":"父母离异、随父且有继母均命中；但职业断设计师或老师，结局仅载现学哲学专业，未印证且方向未定。timing：预测断语本身无应期"},
 {"anon_id":"H28M-62815be2","direction":2,"claims":2,"timing":0,"total":4,"pass":True,"reason":"断此婚可成，结局载所断皆验、二人于98年酉月结婚，唯一实质断语完全印证。timing：预测断语本身无应期"},
 {"anon_id":"H28M-6c417a08","direction":2,"claims":2,"timing":2,"total":6,"pass":True,"reason":"断可放心借出50万、朋友生意好、阴历十月连本带利归还；结局为农历十月十八前一日朋友已全数还清本金并付4万多元利息，逐项命中"},
 {"anon_id":"H28M-720c4445","direction":2,"claims":2,"timing":0,"total":4,"pass":True,"reason":"断破财之象、车子难找回，结局为一辆破旧自行车被偷走没有找回，实质断语完全印证。timing：预测断语本身无应期"},
 {"anon_id":"H28M-72872ae8","direction":2,"claims":2,"timing":2,"total":6,"pass":True,"reason":"断有地震但不会大、丑月有小地震，结局为丑月太原市发生有感地震，量级与月份均命中"},
 {"anon_id":"H28M-7dcbb56e","direction":2,"claims":1.5,"timing":2,"total":5.5,"pass":True,"reason":"最终断次日为晴天有浮云，结局为次日上午晴、下午晴而非大晴、天空有一些浮云，吻合；惟断中先有晴转阴及多云之犹豫，故claims不给满分。次日时间坐标命中"},
 {"anon_id":"H28M-86f3007d","direction":2,"claims":2,"timing":2,"total":6,"pass":True,"reason":"投资打包转卖生意、1999年结婚、2002/2003生子（实2003）、右脚于生日车祸、因财被友骗光钱、三个兄弟、合伙股份制及2004/2005两次入股、有人撤股致公司将解散，均逐项获确认，年份坐标全中"},
 {"anon_id":"H28M-941cfa70","direction":1.5,"claims":0.5,"timing":2,"total":4,"pass":True,"reason":"死亡结局与2001辛巳年不过之断命中，结局确于2001年身故；但死因断为肾病，结局为子宫癌，明显不符；克死二女儿一断未被结局记载。年份应期命中"},
 {"anon_id":"H28M-9608cd83","direction":1.5,"claims":1,"timing":0,"total":2.5,"pass":False,"reason":"断被枪决之象，结局为其子犯刑入狱、被判死刑缓期两年执行；死刑判决方向相近，但缓期执行并非枪决，执行方式子断语未印证。timing：预测断语本身无应期"},
]

SEG3 = [
 {"anon_id":"H28M-98fbbcb9","direction":2,"claims":1.5,"timing":2,"total":5.5,"pass":True,"reason":"断文件不在宾馆、不会丢、再找可寻，结局为在汽车座垫底下找到；下午1时至3时窗口内13时25分获报找到，时间命中；惟文件五张/五份之数未被结局记载"},
 {"anon_id":"H28M-9e5d924d","direction":1.5,"claims":1.5,"timing":0,"total":3,"pass":False,"reason":"学历高、搞计算机、薪水不低、父母多争吵、开过刀、妇科与肾寒多项获点头或确认；但广州月薪不低于6000元的具体数及母亲血液/脾胃病的病种未被结局明确记载。timing：预测断语本身无应期"},
 {"anon_id":"H28M-a7bbb0dd","direction":2,"claims":1.5,"timing":2,"total":5.5,"pass":True,"reason":"会计职业、1995年恋爱、1999年拿证、生男孩、丈夫在政府部门有职权且2003年升正职、母亲1999年（己卯）去世均获确认；1997年同居及执法部门的细化未被结局明确记载。多个年份坐标命中"},
 {"anon_id":"H28M-ac614236","direction":2,"claims":2,"timing":1.5,"total":5.5,"pass":True,"reason":"断生意不景气缺流动资金、借出后本金可回但利息难、到期尽力还款而吃力，结局为本金20万全部归还而4万元利息暂给不上，逐项印证；到期时点的相对时间坐标命中，但无具体日期坐标故不给满分"},
 {"anon_id":"H28M-b17c8811","direction":2,"claims":2,"timing":0,"total":4,"pass":True,"reason":"断书被藏在比较低的地方，结局为在柜子最底层一团棉花下找到书，唯一实质断语完全印证。timing：预测断语本身无应期"},
 {"anon_id":"H28M-ccdf0b44","direction":2,"claims":1.5,"timing":0,"total":3.5,"pass":False,"reason":"断孩子有艺术天赋、最适合音乐，结局为十岁即欲买大吉他、唱歌水平近明星，天赋方向命中；但学别的都不会喜欢及创作一面未被结局记载。timing：预测断语本身无应期"},
 {"anon_id":"H28M-d5517a18","direction":2,"claims":1.5,"timing":0,"total":3.5,"pass":False,"reason":"断化学或生物会失分，结局为只有化学没发挥好、一道大题做错略低于预期；化学一支命中，生物一支未发生（系或然二选）。timing：预测断语本身无应期"},
 {"anon_id":"H28M-d6ccd796","direction":2,"claims":2,"timing":2,"total":6,"pass":True,"reason":"断必有大水灾、因雨而生、申月必发，结局为雨不停、申月水势骤增成大水、冲倒房屋并冲走公共汽车造成重大损失，逐项命中"},
 {"anon_id":"H28M-e787d999","direction":2,"claims":1.5,"timing":1,"total":4.5,"pass":True,"reason":"断洪水凶猛难退、终将退去皆大欢喜，方向命中，结局为抗洪胜利并结束抗洪工作；但具体应期断酉月首个寅日丙寅日（9月16日），实际9月4日申月已宣布胜利、9月11日酉月结束工作，酉月框架部分沾边而确切日落空"},
]

def check(rows, expect_ids):
    assert len(rows) == len(expect_ids), (len(rows), len(expect_ids))
    for r, eid in zip(rows, expect_ids):
        assert r["anon_id"] == eid, (r["anon_id"], eid)
        for k in ("direction","claims","timing"):
            v = r[k]
            assert 0 <= v <= 2 and (v*2) == int(v*2), (r["anon_id"], k, v)
        assert abs(r["total"] - (r["direction"]+r["claims"]+r["timing"])) < 1e-9, r["anon_id"]
        assert r["pass"] == (r["total"] >= 4), r["anon_id"]
        assert r["reason"].strip(), r["anon_id"]

def main():
    if os.path.exists(OUT):
        print("REFUSE: target already exists", OUT); sys.exit(1)
    segs = [SEG1, SEG2, SEG3]
    written = 0
    for i, seg in enumerate(segs, 1):
        check(seg, [r["anon_id"] for r in seg])
        with open(OUT, "a", encoding="utf-8") as f:
            for r in seg:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        written += len(seg)
        with open(OUT, encoding="utf-8") as f:
            lines = f.read().splitlines()
        assert len(lines) == written, (i, len(lines), written)
        ids = [json.loads(x)["anon_id"] for x in lines]
        assert len(set(ids)) == len(ids), "duplicate anon_id"
        print(f"segment {i} ok, cumulative lines={written}")
    assert written == 27
    print("DONE 27 lines ->", OUT)

if __name__ == "__main__":
    main()
