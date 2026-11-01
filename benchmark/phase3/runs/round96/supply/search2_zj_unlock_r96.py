#!/usr/bin/env python3
"""R96 ZJ-unlock auxiliary pass: wanxiang alone, guiyuan, yiyuanlun, dan/shuang xiang, xingshu/ganshu/weishu.
Text-layer books only (same corpus). Prints counts + first contexts."""
import os, re, subprocess, zipfile

BOOK = "/home/hatch/workspace/divination/incoming/wanted-books-6/Book"
TERMS = [("萬象", r"萬象"), ("万象", r"万象"), ("歸元", r"歸元"), ("归元", r"归元"),
         ("一元論", r"一元論"), ("一元论", r"一元论"), ("多元論", r"多元論"), ("多元论", r"多元论"),
         ("雙象", r"雙象"), ("双象", r"双象"), ("單象", r"單象"), ("单象", r"单象"),
         ("星數", r"星數"), ("星数", r"星数"), ("干數", r"干數"), ("干数", r"干数"),
         ("位數", r"位數"), ("位数", r"位数"), ("四象歸", r"四象歸"), ("四象归", r"四象归"),
         ("天地數理", r"天地數理"), ("天地数理", r"天地数理")]

def pdf_text(path):
    try:
        out = subprocess.run(["pdftotext", "-layout", path, "-"], capture_output=True, timeout=300)
        return out.stdout.decode("utf-8", errors="replace")
    except Exception:
        return ""

def docx_text(path):
    try:
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml").decode("utf-8", errors="replace")
        return re.sub(r"<[^>]+>", "", xml)
    except Exception:
        return ""

for fn in sorted(os.listdir(BOOK)):
    path = os.path.join(BOOK, fn)
    ext = os.path.splitext(fn)[1].lower()
    if ext == ".pdf":
        text = pdf_text(path)
    elif ext == ".docx":
        text = docx_text(path)
    else:
        continue
    if len(text.strip()) < 200:
        continue
    flat = text.replace(" ", "").replace("\u3000", "").replace("\n", "").replace("\r", "")
    found = []
    for label, pat in TERMS:
        hits = [m.start() for m in re.finditer(pat, flat)]
        if hits:
            found.append((label, hits))
    if not found:
        continue
    print(f"\n=== {fn} ===")
    for label, hits in found:
        print(f"  TERM {label}: {len(hits)} hit(s)")
        for h in hits[:4]:
            ctx = flat[max(0, h-40):h+50].replace("\f", "|")
            pg = flat[:h].count("\f") + 1
            print(f"    ~p{pg}: ...{ctx}...")
