import json, pathlib
packet_path = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round60/acceptance/judging/packet-ours.json")
out_path = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round60/acceptance/judging/judgeO1.jsonl")
rows = [
 ("H21O-1a0ded83",1.5,1.0,1,"发大财、离婚、经商生财合大耗波折，子女病残与心血管等未全验；结局无可核时点"),
 ("H21O-1a2c7ce0",0.5,0.5,1,"仅结婚一事部分合，富裕事业子女得力均未见结局印证；结局无可核时点"),
 ("H21O-23dbaa40",2,2,2,"巳时停电、申时16:33复电，与断语逐项全合"),
 ("H21O-2acfeefa",2,1.5,0.5,"曾合已散、法院离婚合；窗口内但主坐标午月不合，实为子月离婚"),
 ("H21O-3fe7ad5c",2,1.5,0.5,"未婚同居终散、现独身合；断言一月内而实际同居两月后散"),
 ("H21O-4606126b",2,1.0,1,"病重难愈、无希望合，病位肝胆与实肺癌不合；结局无可核时点"),
 ("H21O-5be67e16",0,0,0,"实为塑料袋中胖大海，与钥匙串全不合；预测断语本身无应期"),
 ("H21O-5d289201",0,0,0,"其人非丈夫且贩毒外逃未归，归来断全反"),
 ("H21O-6300c590",2,1.0,2,"时段内无雨、仪式顺利合；晴热骄阳薄云与实阴凉不合，有风合"),
 ("H21O-6a158eaf",2,2,2,"当晚19:20来水在戌时内，故障原因与方向经报道一致"),
 ("H21O-789ade5e",0,0.5,0,"分数第一合过线一语，然成绩作废未录取，终局方向反；酉日坐实未发生"),
 ("H21O-8402cf9f",0,0,0,"结局明言相亲不成，与能成及对方有意全反"),
 ("H21O-8c16b39f",2,1.5,1,"男方已订婚不公开、不成婚终分手合主线；结局无可核时点"),
 ("H21O-8eadad02",1.5,1.0,1,"办退休手续离原岗合，顶替难保未验；结局无可核时点"),
 ("H21O-a1c72242",2,1.0,0,"手机找回、抽屉中合部分；实为次日晨书店，非当晚戌时家中西南"),
 ("H21O-a46725af",2,1.5,1,"伤愈拆线出院合，三日稳定与巳日无从核；结局无可核时点"),
 ("H21O-ab57d889",2,1.5,2,"7月8日仪式时约9:20降雨、雨具派用合；雨量级未明核"),
 ("H21O-c9a35d81",2,1.5,0.5,"食道癌属消化系、病逝合难保；宽窗入秋合而主坐标子月未中，实酉月逝"),
 ("H21O-d0ff70c1",1.5,1.5,1,"三角对象另有女友、未追成合；后与何人结婚未知，结局无可核时点"),
 ("H21O-da376d02",0.5,0.5,1,"生子一事合，余反馈多为未断之家庭变故，事业财运等级未验；结局无可核时点"),
 ("H21O-e23127b5",0,0,0,"女方携款逃走未归，且非妻，归至断全反"),
 ("H21O-e90d4c3b",2,1.5,0.5,"姨母旬内去世合病重性命危；主坐标丙午日不合实癸亥日，病位未验"),
 ("H21O-ef69a518",1.5,1.5,1,"28岁转房地产经商成老板、官司是非破大财合多项；婚子女健康未验，有年龄时点可核而运应仅部分合"),
 ("H21O-f278d6f4",2,1.0,1,"追而不得终没成合，另有男子相争未见结局记载；结局无可核时点"),
 ("H21O-f9ae4749",0.5,0.5,1,"官司破财仅与伤官见官之险泛合，因由不合，余断未验；结局无可核时点"),
]
packet = json.loads(packet_path.read_text(encoding="utf-8"))
packet_ids = [p["anon_id"] for p in packet]
assert [r[0] for r in rows] and set(r[0] for r in rows) == set(packet_ids), "id set mismatch"
assert len(rows) == 25 == len(packet_ids)
lines = []
for anon, d, c, t, reason in rows:
    total = d + c + t
    obj = {"anon_id": anon, "direction": d, "claims": c, "timing": t, "total": total, "pass": total >= 4, "reason": reason}
    lines.append(json.dumps(obj, ensure_ascii=False))
out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
# self-verify by re-reading
back = [json.loads(x) for x in out_path.read_text(encoding="utf-8").splitlines()]
assert len(back) == 25
assert set(x["anon_id"] for x in back) == set(packet_ids)
for x in back:
    assert set(x.keys()) == {"anon_id","direction","claims","timing","total","pass","reason"}
    for k in ("direction","claims","timing"):
        assert 0 <= x[k] <= 2 and (x[k]*2) == int(x[k]*2)
    assert x["total"] == x["direction"]+x["claims"]+x["timing"]
    assert x["pass"] == (x["total"] >= 4)
print("OK", len(back), out_path.stat().st_size)
