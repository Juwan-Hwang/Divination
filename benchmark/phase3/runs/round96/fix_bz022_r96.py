# -*- coding: utf-8 -*-
import json, os
p = "/home/hatch/workspace/divination/benchmark/phase3/runs/round96/predictions/BZ-022.json"
d = json.load(open(p, encoding="utf-8"))
add = ("\n第八节功量核 — 功量清单：财星乙卯成势生官（作用源：乙卯木，对象：官星／位位面，助成，旺相得令）强1条；"
       "丁官得用（作用源：丁火时干，对象：格局，助成）1条；亥卯半合助财（作用源：亥水，对象：财星，助成）1条；"
       "印土己辰丑生扶一线（作用源：己辰丑土，对象：日主，助成弱兼逆从势）1条弱。合计助成3强1弱、逆势压制在晚运比劫线，等级带定为一方霸主带。\n"
       "主线认定：顺财生官之势为做功主线，量级按主线定一方之主级，终局逆势运只压终局段、不改全命主线等级带。")
if "第八节" not in d["basis"]:
    d["basis"] = d["basis"] + add
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("fixed", len(d["basis"]))
