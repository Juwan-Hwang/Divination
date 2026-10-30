import json, pathlib

rows = [
 ("H21O-1a0ded83",1.0,1.0,1.0,"经营生财与聚大财（15万、100万）合，婚姻断可守而实际离婚、子女仅部分合；结局无可核时点"),
 ("H21O-1a2c7ce0",0.5,0.5,1.0,"仅初中毕业，与事业中上/专业地位不合，结婚一事略合，兄弟入狱未断中；结局无可核时点"),
 ("H21O-23dbaa40",2.0,2.0,2.0,"巳时停电、申时16:33复电，与断语及应期全合"),
 ("H21O-2acfeefa",2.0,1.5,1.0,"曾合已散、法院离婚合；应期窗口内子月离婚，惟主坐标午月未中"),
 ("H21O-3fe7ad5c",2.0,1.5,0.5,"未领证同居终被女方断绝、独身合；断语称一月内而实际同居两月后散，应期偏"),
 ("H21O-4606126b",2.0,1.5,1.0,"父病难愈、治疗无望合，惟病位断肝胆而实为肺癌；结局无可核时点"),
 ("H21O-5be67e16",0.0,0.0,0.0,"断金属钥匙串，实为塑料袋中胖大海，全错；预测断语本身无应期"),
 ("H21O-5d289201",0.0,0.5,0.0,"断丈夫丑日归，实为同居男贩毒被通缉外逃不归，仅人在外一象合"),
 ("H21O-6300c590",1.5,1.0,2.0,"仪式时段无雨、顺利、有风合，惟断晴热骄阳而实阴凉无阳光；应期即所问时段命中"),
 ("H21O-6a158eaf",2.0,2.0,2.0,"当晚19:20来水在戌时内，故障原因与方向经报道证实一致，全合"),
 ("H21O-789ade5e",0.5,1.0,1.0,"分数第一合成绩有力，惟断录取而实因写错代码成绩作废未录取；结局无可核时点"),
 ("H21O-8402cf9f",0.0,0.0,1.0,"断相亲能成，实际不成，方向全反；结局无可核时点"),
 ("H21O-8c16b39f",2.0,1.5,1.0,"对象藏而不露（对方已订婚）、同居不成婚终分手合；应期坐标相对占时无从核对，结局无可核时点"),
 ("H21O-8eadad02",1.5,1.0,1.0,"离原岗办退休手续合退离方向，惟断竞争顶替未见、属自愿退休；结局无可核时点"),
 ("H21O-a1c72242",1.5,1.0,0.5,"手机在抽屉暗处找回合，惟地点在书店非居所西南；断当晚戌时得，实次日早得，应期偏"),
 ("H21O-a46725af",2.0,1.5,1.0,"侄子拆线出院、可愈合；5月20日出院有据，惟巳日主坐标无从由结局文本核对"),
 ("H21O-ab57d889",2.0,1.5,2.0,"仪式时段9时20分落雨、雨具派上用场合，雨量间歇细节未全载；应期即明日仪式时段命中"),
 ("H21O-c9a35d81",2.0,1.5,1.0,"父患消化系癌（食道癌）不治身故合；断转危主坐标子月，实秋初酉月去世，应期偏早"),
 ("H21O-d0ff70c1",1.5,1.5,1.0,"三角（对方有女友）、不敢追未成合，结局自述推断全对；惟其1999年另婚与否不明，结局无可核时点"),
 ("H21O-da376d02",1.0,1.0,1.0,"结婚、生子、家事破耗与烦累部分合，事业量级与峰值运未见结局印证；结局无可核时点"),
 ("H21O-e23127b5",0.0,0.5,0.0,"断妻辰日归，实为同居女携款逃走不归，仅人在外一象合"),
 ("H21O-e90d4c3b",2.0,1.5,1.0,"姨母病危身故合，病位未载；身故在占后旬内窗口，惟主坐标丙午日未中（实癸亥日）"),
 ("H21O-ef69a518",2.0,1.5,1.5,"离国企自营房地产为老板、官司破大财与项目巨损合；28岁入房地产落在事业起步运内，其余运程未全验"),
 ("H21O-f278d6f4",2.0,1.0,1.0,"追而不得、女方躲避终没成合，惟断女方另有男子牵连未见结局记载；结局无可核时点"),
 ("H21O-f9ae4749",0.5,0.5,1.0,"官司缠身略合伤官见官，惟断青年发迹未见、破耗断长辈文书而实因帮朋友打架；结局无可核时点"),
]

out = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round60/acceptance/judging/judgeO2.jsonl")
lines = []
for anon, d, c, t, reason in rows:
    total = d + c + t
    lines.append(json.dumps({"anon_id": anon, "direction": d, "claims": c, "timing": t,
                             "total": total, "pass": total >= 4, "reason": reason}, ensure_ascii=False))
out.write_text("\n".join(lines) + "\n", encoding="utf-8")

# self-verify
packet = json.loads(pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round60/acceptance/judging/packet-ours.json").read_text(encoding="utf-8"))
want = {p["anon_id"] for p in packet}
got_lines = out.read_text(encoding="utf-8").strip().split("\n")
assert len(got_lines) == 25, len(got_lines)
seen = set()
for ln in got_lines:
    r = json.loads(ln)
    assert set(r) == {"anon_id","direction","claims","timing","total","pass","reason"}, r
    seen.add(r["anon_id"])
    for k in ("direction","claims","timing"):
        assert 0 <= r[k] <= 2 and (r[k]*2) == int(r[k]*2), r
    assert r["total"] == r["direction"]+r["claims"]+r["timing"]
    assert r["pass"] == (r["total"] >= 4)
assert seen == want, (seen ^ want)
print("OK rows=25 bytes=", out.stat().st_size)
