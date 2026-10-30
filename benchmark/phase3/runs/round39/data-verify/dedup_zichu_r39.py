#!/usr/bin/env python3
"""R39 Zichu J3 dedup: triple-key (character + subject + question) check of
new candidates ZC-099.. against ZC-001..098, CZ-001..033, and all ZC/CZ ids
used in holdout12-15 test_gold.jsonl. Prints character-overlap table for
manual confirmation. Output to stdout only."""
import json

NEW = [
    # (char, subject_kw, question_kw)
    ("合/黃絹", "楊修/曹操", "解字"), ("活", "楊德祖/魏武", "門字"),
    ("子系十二", "公孫述", "夢期"), ("天保", "齊文宣帝", "年號"),
    ("紫", "齊武明太后", "紫綬靴謠"), ("朕/淵", "楊帝/杳孃", "析字令"),
    ("葉子", "唐太宗/一行", "世數"), ("乘", "唐玄宗/寶符", "天寶"),
    ("柳/光", "柳光", "石壁文字"), ("八人/火", "夔州市民/翟乾祐", "今夕火"),
    ("廣明", "唐僖宗", "年號"), ("木中六字", "李思安/徐鴻", "石氏"),
    ("太平", "宋太宗", "年號壽"), ("靖康", "宋欽宗", "年號"),
    ("純/正", "宋理宗", "謚議"), ("昌", "岐王", "昌王飛語"),
    ("順", "李順", "西川"), ("曦", "吳曦", "被戎"),
    ("醋", "蔡襄", "萬安橋"), ("熊", "永嘉/高世則", "火災"),
    ("嘉", "嘉泰年號", "臨安火"), ("臀無膚", "胡易鑒", "狀元探花"),
    ("奇", "賈似道", "異志"), ("葉/相", "相哥丞相", "相位月數"),
    ("豐", "劉命熙祖父", "祖父病"), ("德", "劉/張乘榻", "行人"),
    ("陋", "柳道彥", "奴子盜金"), ("驗", "馬公/王君", "夢字"),
    ("吉帖", "姻事者", "吉帖問婚"), ("士", "董伯念", "策名名次"),
    ("可", "婚姻男女", "可字問婚"), ("問/閔", "閔君室人", "室人病"),
    ("黃", "某令君", "軍功召入都"), ("初", "楊左諸公", "刀劍之厄"),
    ("萱", "懷孕踰月者", "產期男女"),
]
zc = [json.loads(l) for l in open("/home/hatch/workspace/divination/benchmark/phase3/runs/round38/data-verify/zichu-cases-r38.jsonl")]
cz = [json.loads(l) for l in open("/home/hatch/workspace/divination/benchmark/phase3/expansion12/online-routes/cases.jsonl")]
def chars(d):
    a = (d.get("context") or {}).get("attachments") or {}
    return a.get("character_written", "")
def subj(d):
    return (d.get("subject") or {}).get("name_or_desc", "")
print("== existing ZC chars ==")
print(", ".join(f"{d['id']}:{chars(d)}" for d in zc))
print("== existing CZ chars ==")
print(", ".join(f"{d['id']}:{chars(d)}" for d in cz))
print("== overlap check (new char tokens vs existing) ==")
import re
for ch, sk, qk in NEW:
    toks = [t for t in re.split(r"[/、]", ch) if t]
    hits = []
    for d in zc + cz:
        ec = chars(d)
        if any(t and (t in ec or ec in t) for t in toks if len(t) >= 1):
            hits.append(f"{d['id']}(字:{ec};主:{subj(d)[:20]})")
    if hits:
        print(f"新[{ch}|{sk}|{qk}] 同字既有: {'; '.join(hits)}")
    else:
        print(f"新[{ch}|{sk}|{qk}] 同字既有: 無")
print("== holdout12-15 used cezi ids ==")
import glob
for h in ["holdout12", "holdout13", "holdout14", "holdout15"]:
    p = f"/home/hatch/workspace/divination/benchmark/phase3/{h}/test_gold.jsonl"
    ids = [json.loads(l)["id"] for l in open(p)]
    cezi = [i for i in ids if i.startswith(("ZC-", "CZ-"))]
    print(h, len(cezi), cezi)
