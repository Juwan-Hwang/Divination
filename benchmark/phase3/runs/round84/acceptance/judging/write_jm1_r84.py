#!/usr/bin/env python3
"""R84 judge M1 (master packet) writer: segmented append, per-segment asserts.
Refuses to run if judgeM1.jsonl already exists (no overwrite)."""
import json, os, sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "judgeM1.jsonl")

SEG1 = [
 {"anon_id":"H28M-02bf639c","direction":1,"claims":0.5,"timing":1,"reason":"仅言申月出空当防，未指明何事；结局为切伤中指、包扎三月余愈，方向仅泛泛凶险部分吻合，具体断语无从逐条印证；结局无可核时点"},
 {"anon_id":"H28M-04bf702c","direction":2,"claims":2,"timing":2,"reason":"断南方水灾必大且在午月发生，结局午月长江下游发生特大洪水，方向、规模与月份全中"},
 {"anon_id":"H28M-05c87204","direction":2,"claims":2,"timing":2,"reason":"断1999或2000年离婚、第二任年岁小很多且已经有了，结局确认2000年离婚且第二任情况属实，年份命中"},
 {"anon_id":"H28M-118877d4","direction":2,"claims":1.5,"timing":1,"reason":"断大麻烦、经济问题牢狱及六千万挪用，结局确认六千万挪用公款案；但前段公安局官员等职业断语有误、金额系二选其一，claims扣分；结局无可核时点"},
 {"anon_id":"H28M-183f72ec","direction":2,"claims":1.5,"timing":1.5,"reason":"当兵后入国有纺织企业任中层、计划生育下只有一女、父亡六七年、兄弟姐妹中为老大等多条印证，父亡年限经反馈确认；唯兄弟姐妹断四人实为三人，claims扣分"},
 {"anon_id":"H28M-2588b75a","direction":2,"claims":2,"timing":2,"reason":"断首次婚姻2004年结束、二婚名存实亡离不了、女儿不在身边，结局逐条确认且称一年不差，时间全中"},
 {"anon_id":"H28M-2d8db2f9","direction":1.5,"claims":1,"timing":0,"reason":"早婚、夫离过婚、亲生两女、婚姻中途出问题、夫亡等部分命中；但断夫带来两男与结局无子完全不符，claims扣分；预测断语本身无应期"},
 {"anon_id":"H28M-3491ebd1","direction":2,"claims":1.5,"timing":0,"reason":"断有可能回了老家，结局当日午时电话确认已回老家，主断命中；东南方系问答确认非断语主体，claims略扣；预测断语本身无应期"},
 {"anon_id":"H28M-55339daa","direction":2,"claims":1.5,"timing":1.5,"reason":"断去年冬天出现有别人之男人且不可能结婚，结局确认去年爱上有家室者；但2006年谈对象、明年结婚两项未被结局记载，claims不得满分；去年冬天时间坐标基本命中"},
]
SEG2 = [
 {"anon_id":"H28M-5c7ab651","direction":1.5,"claims":1,"timing":0,"reason":"父母离异、随父而有继母两项确认；职业断设计师或老师未被结局印证，所学为哲学专业，claims扣分；预测断语本身无应期"},
 {"anon_id":"H28M-62815be2","direction":2,"claims":2,"timing":0,"reason":"断妻财旺相六合、此婚可成，结局二人结婚，主断完全印证；预测断语本身无应期"},
 {"anon_id":"H28M-6c417a08","direction":2,"claims":2,"timing":2,"reason":"断可放心借50万元、朋友生意好、阴历十月连本带利归还，结局阴历十月十八前一日全数还清并付息四万余，全部命中"},
 {"anon_id":"H28M-720c4445","direction":2,"claims":2,"timing":0,"reason":"断破财之象、车子难找回，结局自行车被偷没有找回，主断印证；预测断语本身无应期"},
 {"anon_id":"H28M-72872ae8","direction":2,"claims":2,"timing":2,"reason":"断有小地震且在丑月发生，结局丑月丁巳日太原市发生有感地震，方向、量级与月份全中"},
 {"anon_id":"H28M-7dcbb56e","direction":2,"claims":2,"timing":2,"reason":"最终断次日晴天有浮云，结局次日上午下午皆晴且天空有浮云，方向、断语与次日时点全中"},
 {"anon_id":"H28M-86f3007d","direction":2,"claims":2,"timing":2,"reason":"投资打包转卖赚钱、1999年结婚、2003年生子、右脚、因财被骗、兄弟三人、2004与2005年两次入股等逐条确认，公司将解散亦合撤股走向，年份全中"},
 {"anon_id":"H28M-941cfa70","direction":1.5,"claims":0.5,"timing":2,"reason":"断难过2001年且死于肾病、会克死二女儿；结局确于2001年死亡，但死因为子宫癌非肾病，女儿一项未被结局记载，claims仅部分；死亡年份命中"},
 {"anon_id":"H28M-9608cd83","direction":1,"claims":0.5,"timing":0,"reason":"断被枪决之象，结局为犯刑入狱判死刑缓期两年执行，并非枪决，方向仅刑罚极重层面部分吻合；预测断语本身无应期"},
]
SEG3 = [
 {"anon_id":"H28M-98fbbcb9","direction":2,"claims":1.5,"timing":2,"reason":"断文件未丢、下午1点以后3点以前找到，结局13时25分于汽车座垫底下找到，未丢与时段命中；五张或五份一项未被结局记载，claims扣分"},
 {"anon_id":"H28M-9e5d924d","direction":2,"claims":1.5,"timing":0,"reason":"学历本科、搞计算机、薪水不低、母亲开过刀、妇科病肾寒等多条确认；父母关系不好与血液或脾胃病等未明确印证，claims扣分；预测断语本身无应期"},
 {"anon_id":"H28M-a7bbb0dd","direction":2,"claims":1.5,"timing":1.5,"reason":"会计、1995年恋爱、1999年拿证生男孩、夫2003年升职、母己卯年亡等多条确认；1997年同居一项未被结局记载，执法部门表述仅部分合，claims与timing略扣"},
 {"anon_id":"H28M-ac614236","direction":2,"claims":2,"timing":0,"reason":"断本金能回来、利息不好说、还款会很吃力并劝不借，结局本金全部还清而4万元利息暂给不上，逐条印证；预测断语本身无应期"},
 {"anon_id":"H28M-b17c8811","direction":2,"claims":2,"timing":0,"reason":"断书被藏在比较低的地方，结局当日于值班室柜子最底层棉花下找到，位置断语命中；预测断语本身无应期"},
 {"anon_id":"H28M-ccdf0b44","direction":2,"claims":1.5,"timing":0,"reason":"断孩子有艺术天赋、最适合搞音乐与创作，结局十岁索要吉他且唱歌水平近明星，天赋方向印证；学别的都不会喜欢一项未被结局记载，claims扣分；预测断语本身无应期"},
 {"anon_id":"H28M-d5517a18","direction":1.5,"claims":1,"timing":0,"reason":"断注意化学或生物会失分，结局只有化学没发挥好、一道大题做错，生物一项未印证，claims仅部分；预测断语本身无应期"},
 {"anon_id":"H28M-d6ccd796","direction":2,"claims":2,"timing":2,"reason":"断因下雨带来大水灾且申月发生，结局申月雨势增大发生大水、冲倒房屋冲走汽车，方向、断语与月份全中"},
 {"anon_id":"H28M-e787d999","direction":2,"claims":1.5,"timing":1,"reason":"断洪水终会退去但须待酉月、以丙寅日九月十六为退去应期；结局九月十一日酉月内结束抗洪，退去方向与酉月层面命中，但具体应期日不合且九月四日已宣布抗洪胜利，timing仅部分"},
]

def check_row(r):
    for k in ("direction","claims","timing"):
        v = r[k]
        assert 0 <= v <= 2 and (v*2) == int(v*2), (r["anon_id"], k, v)
    r["total"] = r["direction"] + r["claims"] + r["timing"]
    r["pass"] = r["total"] >= 4
    return r

def main():
    if os.path.exists(OUT):
        print("REFUSE: output already exists, no overwrite"); sys.exit(1)
    segs = [SEG1, SEG2, SEG3]
    written = 0
    with open(OUT, "a", encoding="utf-8") as f:
        for i, seg in enumerate(segs, 1):
            for r in seg:
                row = check_row(dict(r))
                out = {"anon_id": row["anon_id"], "direction": row["direction"],
                       "claims": row["claims"], "timing": row["timing"],
                       "total": row["total"], "pass": row["pass"], "reason": row["reason"]}
                f.write(json.dumps(out, ensure_ascii=False) + "\n")
            f.flush()
            written += len(seg)
            assert written == 9*i, written
            print(f"segment {i} ok, cumulative {written}")
    assert written == 27, written
    print("DONE 27 rows")

if __name__ == "__main__":
    main()
