import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round78")
packet = [json.loads(l) for l in (base/"judging/judgeX-block3.jsonl").read_text(encoding="utf-8").splitlines()]
expected = [o["anon_id"] for o in packet[90:]]
rows = [
 ("P3-b02a68eb",1,0,0,"断终身财福不成凶向，结局仅载死于丑年，按carry口径财福面无独立记载，主断未得验；主坐标戌年与丑年不合"),
 ("P3-b0a1382e",2,1.5,1,"功名不成凶向与果削职合；结局无可核时点"),
 ("P3-b139ca12",2,1,1,"特朗普胜出与312对226合，极度胶着计票拉锯一层与优势票数不合；结局无可核时点"),
 ("P3-b1940f36",2,1.5,1,"升擢成与后擢齐地合，齐地方位与北方主断近合；结局无可核时点"),
 ("P3-b2297a88",2,2,1,"夫妻偕老与妻贤无妒同庚、妻八十一夫八十二全合；主坐标未年未见结局明载，结局无可核时点"),
 ("P3-b2466aac",0,0,1,"断在任平安虚惊无实害，结局八月丁艰，方向反；八月即酉月、忧应时点合而事件向反"),
 ("P3-b26d9058",1,0.5,1,"援例成面与『竟纳之』合按carry口径登记，吉向与名败身丧后果相左；迟速与应期面未载，结局无可核时点"),
 ("P3-b28d20c4",0,0,0,"断寿元有根成向，结局果卒于卯年，方向全反；主坐标申年与卯年不合"),
 ("P3-b2c17b63",2,1.5,2,"疫苗12月英国获批开始接种与断全合，全球接种与地方性流行近合；冬峰春转两段子断语未见结局分载"),
 ("P3-b33afa85",1,0,0,"断功名升不成凶向，结局升迁未直接记载、按carry口径对应三月行文拿问刑狱断面，凶向仅价向相符；主坐标寅月与三月不合"),
 ("P3-b393f063",0.5,0.5,1,"断母无大病安向，结局胃癌初期手术效果不错恢复中，无大病断不合而预后安一层部分合；结局无可核时点"),
 ("P3-b4c6859f",0,0,0,"断大凶难免祸有丧命之险，结局果应无事，方向全反"),
 ("P3-b53cf77d",2,1.5,1,"外交贵显国际司法荣位寿近百与数十年外交、国际法院法官、97岁卒合，婚姻结束一层与婚姻变动断近合；结局无可核时点"),
 ("P3-b58acad0",2,2,2,"求财得财与丙子日得全合，应期子日正中"),
 ("P3-b6017b92",2,1,1,"家宅地形势成吉向得结局『果一一无错』总承，按carry口径断面未分载故claims不给满；结局无可核时点"),
 ("P3-b6808b49",0,0,0,"断兄弟病可愈而迟，结局酉月丁亥日病不治，方向全反；巳日坐标未验"),
 ("P3-b7219b05",2,1.5,1,"终身功名不成与未游泮、奔驰名利皓首无成合；结局无可核时点"),
 ("P3-b7d51431",2,2,1,"脱货有利得利与往返三次俱得倍利合且超量级；主坐标未日未见结局明载，结局无可核时点"),
 ("P3-b84dc89c",0,0,0,"断终身财福成吉向，结局屡辞显贵聘、十余载贫寒淡泊，方向反"),
 ("P3-b85fa16f",2,2,2,"赖第一侯第二柯第三排序与得票份额约四成/三成三/二成六与开票结果全合，1月13日揭晓应期合"),
 ("P3-b88d8788",2,2,1.5,"韩国瑜2020败选声势回落与败选及6月罢免合，1月大选定点与全年窗口合"),
 ("P3-b92334bc",2,1.5,1,"特朗普当选与第47任总统312张选举人票合；结局无可核时点"),
 ("P3-b923fb47",2,1.5,1,"子平安无恙与平安而归合；归日按carry口径括注归属未明不可确核，亥字仅部分合"),
 ("P3-b9a3164d",2,2,1.5,"少女折花坠地伤股无大害与次晚邻女折花坠地伤股全合；主坐标明日与次晚近合"),
 ("P3-b9f286e3",2,2,1,"敬仲后代贵显终代齐与田氏终代齐有国合，桓子始大成子得政合昌大轨迹；五世代际坐标未见结局逐代明载"),
 ("P3-ba7663c1",2,1.5,0,"自病不愈与果卒于癸卯日合；主坐标未日与癸卯日不合"),
 ("P3-badd4fd9",2,1.5,2,"弟病不治与果三日死合，按carry口径终句按病弟断面读；三日应期正中"),
 ("P3-bae24e66",2,2,0.5,"妹临产顺产母子平安与次日卯时生母子平安合；主坐标巳日与次日卯时不合，应期日档近偏"),
 ("P3-bb1b7021",2,1.5,1,"得官京职言官与考入都察院系统合，后历巡抚都御史超初授量级；结局无可核时点"),
 ("P3-bbccc64c",0.5,0,0,"断病可愈，结局仅载三月贼入室被获一节，病面结局按carry口径缺位，主断未得验；申日坐标未载"),
 ("P3-bd0b17ea",1,1,2,"五日内有近祸及鱼事与五日老人赴席鱼骨鲠合，然祸在家人非老人致命一层与老人本人而终相左；第五日应期正中"),
 ("P3-bdad5437",0,0,0.5,"断父病不治，结局申酉日愈，方向全反；申酉日在断中远段关口提及而主坐标子日不合，应期仅弱合"),
]
out = base/"judging/judgeX-block3-scores.jsonl"
assert [r[0] for r in rows] == expected, "seg4 anon mismatch"
with out.open("a", encoding="utf-8") as f:
    for anon, d, c, t, reason in rows:
        total = d + c + t
        f.write(json.dumps({"anon_id": anon, "direction": d, "claims": c, "timing": t, "total": total, "pass": total >= 4, "reason": reason}, ensure_ascii=False) + "\n")
written = [json.loads(l) for l in out.read_text(encoding="utf-8").splitlines()]
all_ids = [o["anon_id"] for o in packet]
assert written == all_ids and len(written) == len(all_ids) == 122, "final assertion failed"
# validate fields
for l in out.read_text(encoding="utf-8").splitlines():
    r = json.loads(l)
    assert set(r) == {"anon_id","direction","claims","timing","total","pass","reason"}
    assert r["total"] == r["direction"] + r["claims"] + r["timing"]
    assert r["pass"] == (r["total"] >= 4)
    for k in ("direction","claims","timing"):
        assert r[k] in (0,0.5,1,1.5,2)
print("seg4 ok FINAL", len(written), "pass", sum(1 for l in out.read_text(encoding='utf-8').splitlines() if json.loads(l)["pass"]))
print("flag1 candidates", [json.loads(l)["anon_id"] for l in out.read_text(encoding='utf-8').splitlines() if json.loads(l)["direction"] <= 0.5 and json.loads(l)["total"] >= 4])
