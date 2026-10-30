import json, pathlib
base = pathlib.Path.home()/'workspace/divination/benchmark/phase3/runs/round35'
extra = [
("P3-8bcd6752",1.5,1,0,"寿限偏凶方向部分合，结局果卒；断丑年为限，实际卒于卯年，应期不合"),
("P3-8bd02568",2,2,1.5,"马三日后自西归家，找回与方位全合；较自断晚一日，timing扣分"),
("P3-8bd44dc7",2,2,1,"特朗普胜选当选应验；结局无可核时点"),
("P3-8c6e8ae2",2,2,2,"林郑月娥于2017-03-26以777票当选女特首，与人选日期全合"),
("P3-8ccc3ff0",2,1.5,1,"赖萧当选应验，名次断语未被结局记载；结局无可核时点"),
("P3-8d1cbde7",1.5,1.5,1,"买马多死仅存28匹、几大亏其本合负面方向；结局无可核时点"),
("P3-8dc21ac5",2,1.5,0.5,"存货堆积四年朽坏大半大亏应验；断寅卯月见损，实际四年尺度，timing仅部分合"),
("P3-8dc25565",0.5,0.5,1.5,"断非鬼祟重祟宜医药，结局藏观音轴送寺后病愈、辰日再现达摩送寺痛愈，祟物实存与主断偏反；辰日坐标与再占辰日合"),
]
p = base/'judging/judgeY-block3.jsonl'
existing = [json.loads(l) for l in p.read_text().strip().split('\n')]
by = {r['anon_id']: r for r in existing}
for anon,d,c,t,reason in extra:
    total=d+c+t
    by[anon]={"anon_id":anon,"direction":d,"claims":c,"timing":t,"total":total,"pass":total>=4,"reason":reason}
packet = json.loads((base/'judging/packet3.json').read_text())
lines=[]
for item in packet:
    lines.append(json.dumps(by[item['anon_id']], ensure_ascii=False))
p.write_text("\n".join(lines)+"\n")
print(len(lines))
