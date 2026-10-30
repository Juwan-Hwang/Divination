import json, re
entries=json.load(open("/home/hatch/workspace/divination/benchmark/phase3/runs/round52/entries-r52.json",encoding="utf-8"))
for pat in [r"(抽签|求签|得签|签曰|祈签|占卜|问卜|求卜|卜之|筮之|占之|起课|布课|三传)", r"(邵雍|康节|陈抟|希夷|麻衣|柳庄|袁天纲|李淳风|鬼谷|严君平|东方朔|郭璞|管辂)", r"(能相.{0,4}人|善占|善卜|善筮|精相|精于相|占验|决疑|谈命|论命|看命|算命)"]:
    print("=== PAT", pat)
    for e in entries:
        if e["fl_title"]<137: continue
        for m in re.finditer(pat, e["body"]):
            s=max(0,m.start()-30); print(e["fl_title"], e["title"], "|", e["body"][s:m.end()+50])
