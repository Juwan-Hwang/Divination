import json
stems = "甲乙丙丁戊己庚辛壬癸"
branches = "子丑寅卯辰巳午未申酉戌亥"
def xk(day):
    s = stems.index(day[0]); b = branches.index(day[1])
    start_b = (b - s) % 12
    seq = [branches[(start_b + i) % 12] for i in range(10)]
    return [x for x in branches if x not in seq]
b = json.load(open('/home/hatch/workspace/divination/benchmark/phase3/runs/round65/batches.json'))
ids = b['B10'] + b['B11'] + b['B12']
for cid in ids:
    d = json.load(open(f'/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12/{cid}.json'))
    a = d['context'].get('attachments', {})
    dg = a.get('date_ganzhi') or d['context'].get('asked_at')
    calc = None
    if dg and '未明' not in dg:
        try: calc = xk(dg.rstrip('日')[-2:])
        except Exception: calc = None
    print(cid, dg, "given空:", a.get('空亡'), "calc空:", calc)
