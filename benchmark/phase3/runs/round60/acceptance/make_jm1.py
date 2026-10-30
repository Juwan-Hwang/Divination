import json, pathlib
rows = [
 ("H21M-06f500eb",1.0,0.5,0.0,"离职方向部分合，但结局为高高兴兴办退休、非下岗，工作不利亦未印证；预测断语本身无应期"),
 ("H21M-0aee3b60",2.0,1.5,1.5,"18岁当陆军、转私营搞房地产任老板、经济官司破大财及投资受阻巨损均印证，年龄段大体合；大量性格等子断语未被结局记载，不给满分"),
 ("H21M-0f19e73a",2.0,1.5,2.0,"1994年遇离婚带孩女性并同居印证，性格不合致散亦合；但未领证同居非结婚，claims不给满分；年份精确命中"),
 ("H21M-29c308c9",2.0,2.0,0.0,"癌症且必凶印证：肺癌治疗无望回家疗养；预测断语本身无应期"),
 ("H21M-321ba4c6",2.0,2.0,0.0,"所问男非丈夫、乃未婚同居之象均经本人实话印证；预测断语本身无应期"),
 ("H21M-3d23f993",2.0,2.0,2.0,"明日阴天无雨有微风、典礼顺利，与结局逐项全合，应期为次日命中"),
 ("H21M-3e94e492",2.0,1.5,0.0,"胖大海为褐色、两端尖，与黑黄褐色及带尖之断大体合，色泽细节未全载；预测断语本身无应期"),
 ("H21M-454eb99a",2.0,2.0,1.5,"经法院离婚印证；结局载1998年子月离婚，与下月之断按叙事对应，应期基本命中"),
 ("H21M-5d3993f7",2.0,1.5,1.5,"第一胎男孩多病残疾、妻流产、结婚破费、发大财兼异性介入、添设备兼离婚、挣100万等多项印证；众多子断语未载，不给满分；年份序列大体对应"),
 ("H21M-70f61225",2.0,2.0,2.0,"西北方大阀门故障与晚7点20分来水全合，原因方向经报纸报道一致，时段精确命中"),
 ("H21M-713ec854",2.0,2.0,0.0,"结局称一切果如所测、相亲不成，媒人介绍与本人不愿等断语一并获认；预测断语本身无应期"),
 ("H21M-7146c2b0",2.0,1.5,0.0,"同居未领证之女携款逃走印证身份断语；不会回来未被结局明载，claims不给满分；预测断语本身无应期"),
 ("H21M-7181fac7",2.0,2.0,0.0,"单断不成，结局女方死活不愿意、最终没成，全合；预测断语本身无应期"),
 ("H21M-893aae2f",1.5,1.5,1.5,"结婚、97年生子剖腹产、丧父花费、兄官司坐牢累及家人等多项印证；事业层级等众多子断语未载；年份序列大体对应"),
 ("H21M-94f8bea5",2.0,1.5,1.5,"六个兄弟姐妹死一异腹一、86年谈对象未成年底结婚、弟犯法判刑均印证；学历断高中而实为初中略过，claims扣分；年份大体对应"),
 ("H21M-b1ad2c79",0.0,0.0,0.0,"包内prediction_text仅作用神要旨、无任何具体断语可核，无法印证；预测断语本身无应期"),
 ("H21M-b5d2bf5c",2.0,2.0,1.5,"上午10:20停电在巳时内、下午16:33复电在申时内，停复电全合；预测括注申时5-7时与实际复电钟点略有出入，timing扣分"),
 ("H21M-c4d940de",2.0,2.0,2.0,"次日上午约9时20分降雨、雨具派上用场，明日有雨且不小全合，应期命中"),
 ("H21M-cd9f935a",2.0,1.5,1.5,"结局称推断全部正确，1995年有男友及今年又现男友获认；1999年结婚对象是否该男友不得而知，claims不给满分"),
 ("H21M-d92aad5c",2.0,2.0,2.0,"食道癌晚期必死全合，卒于丁酉月丁未日，与酉月未日之断精确命中"),
 ("H21M-ea9a2418",2.0,1.5,1.5,"丧父、替友打架重伤招官司花钱平息、次年春旧事再告官司缠身躲避均印证；众多子断语未载；年份季节序列大体对应"),
 ("H21M-f92539a6",2.0,2.0,2.0,"脑溢血之断及5月26日癸亥过不去全合，其姨母于该日凌晨子时去世，应期精确"),
 ("H21M-fa0c93e8",2.0,2.0,0.0,"名单无名、未被录取印证（成绩作废致未录取）；预测断语本身无应期"),
 ("H21M-fa6edba8",2.0,2.0,0.0,"手机未丢、忘在办公桌抽屉里全合，次日寻回；预测断语本身无应期"),
 ("H21M-febb785b",2.0,2.0,2.0,"无后遗症、十三天内且最晚5月20日出院全合，结果正于5月20日上午拆线出院"),
]
out = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round60/acceptance/judging/judgeM1.jsonl")
lines=[]
for anon,d,c,t,reason in rows:
    total=d+c+t
    lines.append(json.dumps({"anon_id":anon,"direction":d,"claims":c,"timing":t,"total":total,"pass":total>=4,"reason":reason},ensure_ascii=False))
out.write_text("\n".join(lines)+"\n",encoding="utf-8")
# self-verify
packet=json.loads(pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round60/acceptance/judging/packet-master.json").read_text(encoding="utf-8"))
ids_pkt=[p["anon_id"] for p in packet]
recs=[json.loads(l) for l in out.read_text(encoding="utf-8").splitlines() if l.strip()]
assert len(recs)==25, len(recs)
assert [r["anon_id"] for r in recs]==ids_pkt or set(r["anon_id"] for r in recs)==set(ids_pkt)
for r in recs:
    assert set(r)== {"anon_id","direction","claims","timing","total","pass","reason"}, r
    for k in ("direction","claims","timing"):
        assert 0<=r[k]<=2 and (r[k]*2)==int(r[k]*2), r
    assert r["total"]==r["direction"]+r["claims"]+r["timing"]
    assert r["pass"]==(r["total"]>=4)
print("OK rows",len(recs),"bytes",out.stat().st_size,"pass_count",sum(r["pass"] for r in recs))
