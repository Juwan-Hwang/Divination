import json, pathlib
out = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round87/acceptance/judging/judgeM1.jsonl")
rows = [
{"anon_id":"H30M-10fb8b8d","direction":2.0,"claims":1.5,"timing":0.0,"reason":"城被重围、粮空兵溃、贼入城陷，与门户破败不可保方向全合；机制类子断语未被结局逐条记载，claims不给满分；预测无应期，timing记0"},
{"anon_id":"H30M-1a6cd083","direction":2.0,"claims":1.5,"timing":2.0,"reason":"夫妻关系不好终至离婚全合；妻高而漂亮、1982结婚、1992离婚均印证，第三者假象等子断语未见结局记载；婚年与离婚年均命中"},
{"anon_id":"H30M-28cf2b76","direction":1.5,"claims":1.0,"timing":0.0,"reason":"居城外一月即赴袁州、其后贼逼省垣，与难久居须迁徙大体合；盗耗、贵人受克、亥方四百里等未被结局记载；预测无应期，timing记0"},
{"anon_id":"H30M-2fab055b","direction":2.0,"claims":2.0,"timing":0.0,"reason":"对方肯定答应办事，结局厂长一点没犹豫就答应，单断全合；预测无应期，timing记0"},
{"anon_id":"H30M-3159a551","direction":1.5,"claims":0.5,"timing":1.0,"reason":"住宅拆毁、各人四散与家势退、争屋四散方向合；腹痛白带、脾泄、少妇掌家等多数子断语未见结局记载；仅以来年与己卯年作宽评，时点关系不可确核"},
{"anon_id":"H30M-3302aa36","direction":2.0,"claims":2.0,"timing":2.0,"reason":"特大火灾发生，火势大、巳月、丁卯日均与断语逐项印证；应期精确命中巳月卯日"},
{"anon_id":"H30M-52ee71b3","direction":2.0,"claims":1.5,"timing":1.5,"reason":"四月十二日西铭煤矿爆炸引起大火灾，火灾与西向大体合；西北细位与申酉日干支未被结局明载；四月十二日这一关键时点命中"},
{"anon_id":"H30M-67bf623f","direction":2.0,"claims":2.0,"timing":2.0,"reason":"六月入相、秋出师均逐项印证；应期六月与秋季均命中"},
{"anon_id":"H30M-6a25b577","direction":2.0,"claims":2.0,"timing":1.0,"reason":"结局明言后果如所占，首揆与中年反复之断由结局整体背书；结局无可核时点，timing记1"},
{"anon_id":"H30M-714732c5","direction":2.0,"claims":1.5,"timing":0.0,"reason":"其子该次考试未成、时间已过，与一次考不上合；留级或补考未见结局记载；预测无应期，timing记0"},
{"anon_id":"H30M-77854ad6","direction":2.0,"claims":1.5,"timing":0.0,"reason":"虚冢空棺、倍价买下后葬妻、后代聪颖科举均印证；卯龙向、水路文笔等子断语未见结局记载；预测无应期，timing记0"},
{"anon_id":"H30M-80469b10","direction":2.0,"claims":1.5,"timing":2.0,"reason":"1999年无大劫难而地震火灾频发全合；外星人入侵一语未被结局单独明载；该年频发的时间坐标命中"},
{"anon_id":"H30M-8413b8c0","direction":2.0,"claims":2.0,"timing":0.0,"reason":"居之后果公淫其媳、家丑外扬，宅有淫乱不明之事逐项印证；预测无应期，timing记0"},
{"anon_id":"H30M-86bd7b88","direction":2.0,"claims":1.5,"timing":1.5,"reason":"1995年有恋人、2001年先孕后婚同年生女均印证；圆脸、步快、性急及下月对象等子断语未见结局记载；婚年与生子年命中，早年应期部分合"},
{"anon_id":"H30M-8f2ac5c5","direction":2.0,"claims":1.5,"timing":2.0,"reason":"后于子月剖腹产生子，本月难生须待子月之断印证；生产方式与性别非断语内容不另计；应期子月精确命中"},
{"anon_id":"H30M-90a55ad1","direction":1.0,"claims":0.5,"timing":0.0,"reason":"结局为高血压、甲亢、手脚麻抖失眠，未明言头部有病，仅部分相关；预测无应期，timing记0"},
{"anon_id":"H30M-a1542a9f","direction":2.0,"claims":2.0,"timing":1.0,"reason":"先损复孕已准，妻孕、胎损、损后复孕逐项印证；结局无可核时点，timing记1"},
{"anon_id":"H30M-a224edf6","direction":2.0,"claims":1.5,"timing":2.0,"reason":"喜欢现男友、父母姐妹嫌其工资低而反对、1996年巳月结婚均印证；本人无主见一语未见结局记载；婚期1996年巳月精确命中"},
{"anon_id":"H30M-a3ecbe1f","direction":2.0,"claims":1.5,"timing":2.0,"reason":"1992年与同乡二婚者结婚、1994年离婚均印证；丈夫不在家独居等子断语未见结局记载；结婚与离婚年份均命中"},
{"anon_id":"H30M-a6545b32","direction":2.0,"claims":2.0,"timing":2.0,"reason":"九月果入阁，九月大拜单断全合；应期九月命中"},
{"anon_id":"H30M-abe49f8d","direction":2.0,"claims":2.0,"timing":0.0,"reason":"邻居家打麻将大赢而家中漏电起火，财运与家中火灾两断均印证；预测无应期，timing记0"},
{"anon_id":"H30M-af728f7c","direction":2.0,"claims":1.5,"timing":1.5,"reason":"2000年再孕、2001年辰月生子，有子方向全合；2000年即有孩子一读仅合于怀孕而非出生；应期落在所给2000至2001窗口内"},
{"anon_id":"H30M-c3275a32","direction":2.0,"claims":1.5,"timing":2.0,"reason":"七月入刑部右侍郎、八月陟大司寇，内召升迁方向全合；温旨一语未见结局明载；大司寇应期八月命中所断八九月"},
{"anon_id":"H30M-c51ada16","direction":2.0,"claims":2.0,"timing":0.0,"reason":"后知为乌程相、行年正五十五，首臣、籍贯、年岁逐项印证；预测无应期，timing记0"},
{"anon_id":"H30M-f4042f33","direction":2.0,"claims":1.5,"timing":0.5,"reason":"及第后历郎官至礼部侍郎，升显方向全合；其弟朝郎、阴德、即日食禄等子断语未见结局记载；仅即日一语而结局历程跨年，应期至多宽评"},
{"anon_id":"H30M-f7fd8b2d","direction":2.0,"claims":1.5,"timing":0.0,"reason":"退至上游袁州颇安、省城因武宁失守闭城、城外寓毁，宜退与闭关诸断大体印证；西方门户细位未见结局明载；预测无应期，timing记0"},
{"anon_id":"H30M-fa3080ed","direction":2.0,"claims":1.5,"timing":0.0,"reason":"查得丈夫睾丸旧伤、精子不能成活致不能怀孕，病在丈夫与精子有问题印证；一生无子等子断语未被结局记载；预测无应期，timing记0"},
{"anon_id":"H30M-fd43915c","direction":2.0,"claims":1.5,"timing":0.0,"reason":"读书不成、家计败尽后靠妻家酒业渐丰、诸子皆好享福寿终，先败后发方向全合；兄弟星散、店房居住等子断语未见结局记载；预测无应期，timing记0"},
]
assert len(rows) == 28
for r in rows:
    total = r["direction"] + r["claims"] + r["timing"]
    r2 = {"anon_id": r["anon_id"], "direction": r["direction"], "claims": r["claims"], "timing": r["timing"], "total": total, "pass": total >= 4, "reason": r["reason"]}
    assert r2["total"] == r2["direction"] + r2["claims"] + r2["timing"]
    assert r2["pass"] == (r2["total"] >= 4)
    rows[rows.index(r)] = r2
with out.open("w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(rows))
