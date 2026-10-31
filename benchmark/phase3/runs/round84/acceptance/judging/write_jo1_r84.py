#!/usr/bin/env python3
"""R84 judge O1 writer: segmented append + assertions. No wildcard ops."""
import json, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "judgeO1.jsonl")

SEG1 = [
 {"anon_id":"H28O-0b65b292","direction":1.5,"claims":1.0,"timing":1,"total":3.5,"pass":False,
  "reason":"方向：断本科、中上、个别科目小失手，结局化学一科失手略低于预期，方向大体合；claims：失手一条印证，本科录取与文理倾向、运程诸条结局未载，不得满分；timing：结局无可核时点，记1。"},
 {"anon_id":"H28O-0fd0746e","direction":1.0,"claims":1.0,"timing":0.5,"total":2.5,"pass":False,
  "reason":"方向：断婚姻压力大、磨折，结局2004年离异、二婚，婚变方向部分合，但未直断离婚；claims：子女量少（一女）与婚内承压部分印证，才名事业诸条未载；timing：运程段未给出离婚年份坐标，仅宽泛对应，记0.5。"},
 {"anon_id":"H28O-1afd36ed","direction":1.5,"claims":1.0,"timing":1,"total":3.5,"pass":False,
  "reason":"方向：断求学顺、以才华学业立业，结局所学哲学专业，人文学业方向合；claims：学业与文书天赋部分印证，行业、婚子女诸条结局未载；timing：结局无可核时点，记1。"},
 {"anon_id":"H28O-1c5935f3","direction":1.5,"claims":1.0,"timing":1,"total":3.5,"pass":False,
  "reason":"方向：断子偏凶有险有救、不直断绝亡，结局死刑缓期两年，凶与不立即死两端皆合；claims：险中有救印证，但所断病灾与实际刑狱入罪性质不符；timing：结局无可核时点，记1。"},
 {"anon_id":"H28O-296d124f","direction":2,"claims":1.5,"timing":0.5,"total":4.0,"pass":True,
  "reason":"方向：断中国南方水灾，结局午月长江下游特大洪水，方向全合；claims：南方、大水成灾印证，唯应期月份错位；timing：窗口数月内含午月，但主坐标申月与实际午月不符，记0.5。"},
 {"anon_id":"H28O-2a3addca","direction":1.0,"claims":1.0,"timing":1,"total":3.0,"pass":False,
  "reason":"方向：断中等偏上、专业立业，结局企业中层干部大体合；claims：一女儿、纺织企业流通业部分印证，当兵短暂、兄弟三人居长等结局要点预测未载，婚财运诸条亦未载；timing：结局无可核时点，记1。"},
 {"anon_id":"H28O-2e3fce86","direction":1.5,"claims":1.0,"timing":0,"total":2.5,"pass":False,
  "reason":"方向：断人平安，结局当日得电话知其回老家，平安合；claims：平安印证，但短期不现身不回讯被当日来电推翻；timing：主坐标寅日，实际甲辰日当日午时得讯，坐标不符，记0。"},
 {"anon_id":"H28O-32e5007f","direction":2,"claims":1.5,"timing":1.0,"total":4.5,"pass":True,
  "reason":"方向：断抗洪结束、水退，结局宣布抗洪胜利并结束抗洪工作，全合；claims：结束时点落在所断窗口内，印证度高；timing：窗口申月至戌月命中（申月宣布胜利、酉月结束），但主坐标戌月偏晚，记1。"},
 {"anon_id":"H28O-431c36eb","direction":0.5,"claims":0.5,"timing":1,"total":2.0,"pass":False,
  "reason":"方向：断中等偏上靠本事求财，结局为六千万元挪用公款案，仅财量级沾边，终局性质未断中；claims：财与是非同至勉强沾边，挪用公款一事预测全文无对应断语；timing：结局无可核时点，记1。"},
]

SEG2 = [
 {"anon_id":"H28O-4c86f5e2","direction":0,"claims":0,"timing":0,"total":0,"pass":False,
  "reason":"方向：断搞对象不成、难长久，结局二人结婚，终局正相反；claims：一时有意之外无印证，核心断语全错；timing：主坐标酉日见散，实际酉月结婚，时点与事件皆反，记0。"},
 {"anon_id":"H28O-771cf492","direction":2,"claims":1.5,"timing":2,"total":5.5,"pass":True,
  "reason":"方向：断文件未丢未盗、当日午后找回，结局13时25分找回，全合；claims：未被盗、深藏压底印证，但处所断东北方箱包柜屉与实际汽车座垫底下不符；timing：断未时（13时后）冲墓寻回，实际13:25，精确命中，记2。"},
 {"anon_id":"H28O-8c125603","direction":2,"claims":2,"timing":2,"total":6.0,"pass":True,
  "reason":"方向：断次日晴、无雨，结局次日上下午皆晴，方向全合；claims：晴、无雨两条断语逐条印证，浮云不违晴为主之断；timing：题面锁定次日，实际即次日全日晴，记2。"},
 {"anon_id":"H28O-9a415286","direction":1.5,"claims":1.0,"timing":1,"total":3.5,"pass":False,
  "reason":"方向：断才华技术立业，结局本科学历、从事计算机，方向合；claims：学历与计算机（近管账）印证，父母性情、手术等结局要点预测未载，婚子女运程诸条亦未载；timing：结局无可核时点，记1。"},
 {"anon_id":"H28O-a5e59c39","direction":0,"claims":0,"timing":0,"total":0,"pass":False,
  "reason":"方向：断借出年底不能还清、本金落空拖欠，结局50万元本金全额还清并付4万余元利息，终局正相反；claims：年底前不过收回小半、次年才有眉目、分期打折诸条全被推翻；timing：断次年寅月才有回收眉目，实际2001年12月前已全清，记0。"},
 {"anon_id":"H28O-a759a4a2","direction":1.0,"claims":0.5,"timing":0,"total":1.5,"pass":False,
  "reason":"方向：断婚姻情意在而热度淡、以责任维系，结局2000年离婚，冷淡方向部分合而维系之断被推翻；claims：婚缘与冷淡仅部分沾边，离婚未断出，才名运程诸条未载；timing：预测断语本身无离婚应期，记0。"},
 {"anon_id":"H28O-a976867d","direction":1.5,"claims":1.0,"timing":0.5,"total":3.0,"pass":False,
  "reason":"方向：断宜财会经营、食神生财，结局本人即会计，职业方向合；claims：会计、一子印证，婚缘偏晚须介绍、己当家诸条与夫为路桥公司正职等结局不尽合，余条未载；timing：结局1995恋爱、1999拿证、2001生子等时点，预测运程段无对应坐标，记0.5。"},
 {"anon_id":"H28O-b9996aff","direction":0.5,"claims":0.5,"timing":1,"total":2.0,"pass":False,
  "reason":"方向：断年运中平偏吉、事业为主，结局切伤中指入院、三月余方愈，偏吉不成立，仅多波折沾边；claims：波折一条印证，职事落身、午月转实诸条结局未载，伤灾未断出；timing：结局无可核时点，记1。"},
 {"anon_id":"H28O-bf72641b","direction":0.5,"claims":0.5,"timing":1,"total":2.0,"pass":False,
  "reason":"方向：断夫星旺、婚内压力大，结局爱上有家室者求助，感情困境沾边，但正缘婚姻之断与外遇终局不合；claims：婚内压力勉强印证，余事业财运子女诸条结局未载；timing：结局无可核时点（仅相对去年），记1。"},
]

SEG3 = [
 {"anon_id":"H28O-c1581a26","direction":1.5,"claims":1.0,"timing":0.5,"total":3.0,"pass":False,
  "reason":"方向：断食神制杀、才艺表现天赋显，结局十岁唱歌达明星水准，才艺方向合；claims：表现天赋、受长辈规矩压制（父母反对学音乐）印证，但所列体育技术科目与音乐不尽合，健康诸条未载；timing：十岁一事预测运程段无年龄坐标，记0.5。"},
 {"anon_id":"H28O-c24f50f9","direction":0.5,"claims":0.5,"timing":0,"total":1.0,"pass":False,
  "reason":"方向：断才艺立身、际遇起伏，结局因子宫癌于2001年去世，终局死亡未断出；claims：健康条仅列妇科寒湿为弱面，与子宫癌沾边，其余婚财子女诸条未载或被早逝推翻；timing：预测无死亡应期，2001年时点无对应，记0。"},
 {"anon_id":"H28O-ebb16030","direction":0.5,"claims":0.5,"timing":0,"total":1.0,"pass":False,
  "reason":"方向：断晚婚、实业致富中上，结局21岁早婚、丈夫2005年癌逝，方向多处相反；claims：两女儿与子女缘厚沾边、婚姻有问题结局自陈，但晚婚、财峰诸条被推翻或未载；timing：断婚缘来迟与实际21岁结婚相反，夫亡无应期，记0。"},
 {"anon_id":"H28O-edb4f9bd","direction":1.5,"claims":1.5,"timing":0.5,"total":3.5,"pass":False,
  "reason":"方向：断靠决断技能流通求财、合伙防争利耗财，结局投资中介买东卖西、被友骗光15万元、公司将解散，方向合；claims：投资中介、合伙破耗、两度入股印证，车祸、行业金属机械诸条不合或未载；timing：结局1999结婚、2003等时点，预测运程段无对应坐标，记0.5。"},
 {"anon_id":"H28O-f3285551","direction":0,"claims":0,"timing":0,"total":0,"pass":False,
  "reason":"方向：断当年内太原无地震，结局丑月丁巳日太原有感地震，终局正相反；claims：无震断语被直接推翻；timing：断年末验点无震，实际年内丑月即震，记0。"},
 {"anon_id":"H28O-f61b5e1c","direction":2,"claims":2,"timing":1.0,"total":5.0,"pass":True,
  "reason":"方向：断太原有水灾成灾，结局大水冲倒房屋、冲走公交、重大经济损失，全合；claims：水势成灾与损失规模逐条印证；timing：申字命中但预测为未月窗口内申日、实际申月方大，月日层级错位，记1。"},
 {"anon_id":"H28O-f6f5f480","direction":2,"claims":1.5,"timing":0.5,"total":4.0,"pass":True,
  "reason":"方向：断外语书能找到，结局当日找到，全合；claims：能寻回、被夹放深藏（柜子最底层棉花下）印证，书皮被扯掉一节未断；timing：窗口旬内命中且当日即得，但主坐标子日与实际乙酉日酉时不符，记0.5。"},
 {"anon_id":"H28O-fea12037","direction":0,"claims":0,"timing":0,"total":0,"pass":False,
  "reason":"方向：断自行车能找回，结局被偷走没有找回，终局正相反；claims：能寻回、伏出见车诸断语全被推翻；timing：主坐标子日得车，实际始终未找回，记0。"},
 {"anon_id":"H28O-fec25462","direction":1.5,"claims":1.5,"timing":1.0,"total":4.0,"pass":True,
  "reason":"方向：断放款后收款不顺、本金大部可回而利息难足，结局本金20万全额收回、4万元利息对方给不上，方向合（本金回收还优于所断）；claims：拖延、利息难足逐条印证，唯再拖约半年至辰月收清高估，实际腊月十三已清本金；timing：戌月到期被拖住命中，收清时点早于所断辰月，记1。"},
]

def check(rows):
    for r in rows:
        assert abs(r["total"] - (r["direction"] + r["claims"] + r["timing"])) < 1e-9, r["anon_id"]
        assert r["pass"] == (r["total"] >= 4), r["anon_id"]
        for k in ("direction", "claims", "timing"):
            assert 0 <= r[k] <= 2 and (r[k] * 2) == int(r[k] * 2), (r["anon_id"], k)

def main():
    if os.path.exists(OUT):
        raise SystemExit("refuse to overwrite existing judgeO1.jsonl")
    all_rows = []
    for seg in (SEG1, SEG2, SEG3):
        check(seg)
        with open(OUT, "a", encoding="utf-8") as f:
            for r in seg:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        all_rows.extend(seg)
        with open(OUT, encoding="utf-8") as f:
            lines = [ln for ln in f.read().splitlines() if ln.strip()]
        assert len(lines) == len(all_rows), (len(lines), len(all_rows))
    ids = [r["anon_id"] for r in all_rows]
    assert len(ids) == 27 and len(set(ids)) == 27
    print("wrote", len(all_rows), "rows;", sum(1 for r in all_rows if r["pass"]), "pass")

if __name__ == "__main__":
    main()
