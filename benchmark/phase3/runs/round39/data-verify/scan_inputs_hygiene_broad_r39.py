#!/usr/bin/env python3
"""R39 hygiene scan, broad net (2nd pass): dump every non-question field
containing any outcome/prediction keyword, for manual adjudication.
Writes broad_candidates_r39.jsonl in same dir."""
import json, glob, os, re

BASE = "/home/hatch/workspace/divination/benchmark/phase3/inputs-dev11"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "broad_candidates_r39.jsonl")
KEYS = ["果", "驗", "验", "後來", "后来", "卒", "死", "亡", "勝", "胜", "贏", "赢", "敗", "败",
        "當選", "当选", "登基", "為帝", "为帝", "稱帝", "称帝", "狀元", "状元", "登第", "及第",
        "康復", "康复", "痊癒", "痊愈", "逝世", "去世", "身故", "自殺", "自杀", "被殺", "被杀",
        "離婚", "离婚", "成婚", "歸來", "归来", "回來", "回来", "找到", "尋回", "寻回", "失而復得",
        "predict", "won", "win", "victory", "elected", "died", "death", "recovered", "crowned",
        "assassin", "suicide", "married", "divorce", "outcome", "fulfilled", "came true", "in fact",
        "result was", "actually", "later became", "went on to", "ended up", "proved correct",
        "已知", "事後", "事后", "回溯", "回顧", "回顾", "結局", "结局", "應驗", "应验", "靈驗", "灵验",
        "斷語", "断语", "占斷", "占断", "預測", "预测", "預言", "预言", "斷曰", "断曰", "占曰"]

def collect(d, prefix=""):
    out = []
    if isinstance(d, dict):
        for k, v in d.items():
            p = f"{prefix}.{k}" if prefix else k
            if isinstance(v, (dict, list)):
                out += collect(v, p)
            else:
                out.append((p, str(v)))
    elif isinstance(d, list):
        for v in d:
            if isinstance(v, (dict, list)):
                out += collect(v, prefix)
            else:
                out.append((prefix, str(v)))
    return out

EXCLUDE = ("context.question", "subject.name_or_desc", "subject.basic_info", "subject.gender",
           "subject.birth.date", "subject.birth.time", "subject.birth.place", "subject.birth.pillars",
           "language", "id", "uid", "tradition", "system", "license_status", "redistributable", "source_id", "era")
CHART_OK = {"ascendant","asc_ruler","key_positions","yongshen","空亡","月将","三传","四课","课式","chart_complete","completeness_basis","hidden_spirit","day_master","chart_note","hexagram","pillars","casting","casting_method","ben_gua","bian_gua","configuration","moving_lines","hidden_lines","date_ganzhi","chart_lines_top_to_bottom","lines_top_to_bottom"}

rows = []
for f in sorted(glob.glob(os.path.join(BASE, "*.json"))):
    d = json.load(open(f))
    cid = d.get("id") or d.get("uid") or os.path.basename(f)
    for path, val in collect(d):
        if any(path == e or path.startswith(e + ".") for e in EXCLUDE):
            continue
        last = path.split(".")[-1]
        if last in CHART_OK:
            continue
        if path.startswith("context.hexagram"):
            continue
        hits = [k for k in KEYS if k.lower() in val.lower()]
        if hits:
            rows.append({"id": cid, "field": path, "keys": hits, "value": val[:700]})
with open(OUT, "w") as fh:
    for r in rows:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(rows))
