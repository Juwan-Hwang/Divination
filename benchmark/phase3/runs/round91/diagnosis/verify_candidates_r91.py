import json, pathlib, re
base=pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
man=json.load(open(base/'runs/round91/judging/outcome-manifest.json',encoding='utf-8'))
cases=man['cases']
def card(cid):
    p=base/'inputs-dev12'/f'{cid}.json'
    if not p.exists(): return None
    return json.load(open(p,encoding='utf-8'))
def cardtext(cid):
    p=base/'inputs-dev12'/f'{cid}.json'
    return p.read_text(encoding='utf-8') if p.exists() else ''
groups={
 'G7_OCR互证': ['LY-027','LY-028','LY-029','LY-030','LY-031','LY-032','LY-033','LY-034','LY-035'],
 'G10_OCR校正本': ['LY-304','LY-305','LY-306','LY-307','LY-309','LY-311'],
 'G11_OCR推算复原': ['LY-312','LY-314','LY-315','LY-318','LY-319','LY-320','LY-322','LY-323','LY-324','LY-325','LY-328','LY-329','LY-330','LY-331','LY-333','LY-335','LY-336','LY-339','LY-340','LY-342','LY-344'],
 'G12_缺空亡用神': ['LY-402','LY-403','LY-404','LY-405','LY-406','LY-407','LY-408','LY-411','LY-413','LY-415','LY-418','LY-421','LY-424','LY-425'],
 'G15_OCR未能还原': ['LY-531','LY-533','LY-535','LY-536','LY-539','LY-540','LY-541','LY-542','LY-543','LY-627','LY-628','LY-629'],
 'G16_推算复原grades': ['LY-601','LY-604','LY-605','LY-606','LY-607','LY-608','LY-609','LY-610','LY-611','LY-612','LY-613'],
 'SINGLE': ['LY-007','DT-001','DT-002','AS-011','AS-207','MH-001','MH-002','MH-003','OC-010','OC-013','OC-015','OC-030','YM-035','YM-055','YM-063','YY2-005','LY-253','LY-259','LY-252','LY-218','LY-227','LY-255','YY-006','LR3-107','BZ-104','LY-614'],
}
for g, ids in groups.items():
    print("#####", g)
    for cid in ids:
        ct=cardtext(cid)
        out=cases.get(cid)
        outlen=len(out) if isinstance(out,str) else ('DICT' if out else 'MISSING')
        # evidence probes
        probes=[]
        if '行序錯亂' in ct or '行序错乱' in ct: probes.append('chart_note:行序错乱')
        if '未能可靠還原' in ct or '未能可靠还原' in ct: probes.append('未能可靠还原')
        if '逐爻表不錄' in ct or '逐爻表不录' in ct: probes.append('逐爻表不录')
        if '校正本' in ct: probes.append('校正本补录')
        if '推算復原' in ct or '推算复原' in ct: probes.append('推算复原')
        print(f"{cid}: outcome_len={outlen} probes={probes} outcome={str(out)[:60]!r}")
