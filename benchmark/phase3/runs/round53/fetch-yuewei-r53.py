#!/usr/bin/env python3
"""R53 yuewei fetch: only arteducation.com.tw bookv_17130..17184"""
import urllib.request, re, json, time, pathlib, html
outdir = pathlib.Path(__file__).parent / "yuewei-raw-r53"
outdir.mkdir(exist_ok=True)
headers={"User-Agent":"Mozilla/5.0"}
results=[]
for n in range(17130,17185):
    url=f"https://www.arteducation.com.tw/guwen/bookv_{n}.html"
    fp=outdir/f"bookv_{n}.txt"
    if fp.exists() and fp.stat().st_size>200:
        results.append({"page":n,"status":"cached","size":fp.stat().st_size})
        continue
    try:
        req=urllib.request.Request(url,headers=headers)
        with urllib.request.urlopen(req,timeout=30) as r:
            raw=r.read().decode("utf-8",errors="replace")
        # extract title
        m=re.search(r"<title>(.*?)</title>",raw,re.S)
        title=html.unescape(re.sub(r"<[^>]+>","",m.group(1))) if m else ""
        # Try to isolate body content: remove scripts/styles
        body=re.sub(r"<script.*?</script>","",raw,flags=re.S)
        body=re.sub(r"<style.*?</style>","",body,flags=re.S)
        # paragraphs: split on <p or <br><br etc - keep generic: replace block tags with newline
        text=re.sub(r"</p\s*>","\n\n",body,flags=re.I)
        text=re.sub(r"<br\s*/?>","\n",text,flags=re.I)
        text=re.sub(r"<[^>]+>","",text)
        text=html.unescape(text)
        text=re.sub(r"[ \t\r\f\v]+"," ",text)
        text=re.sub(r"\n\s*\n+","\n\n",text).strip()
        fp.write_text(f"TITLE: {title}\nURL: {url}\n\n{text}\n",encoding="utf-8")
        results.append({"page":n,"status":"ok","size":fp.stat().st_size,"title":title})
    except Exception as e:
        results.append({"page":n,"status":"FAILED","error":str(e)})
    time.sleep(0.3)
print(json.dumps(results,ensure_ascii=False,indent=1))
(outdir/"fetch-log.json").write_text(json.dumps(results,ensure_ascii=False,indent=1),encoding="utf-8")
