#!/usr/bin/env python3
"""R96 ZJ-unlock: inventory + text-layer search over wanted-books-6/Book ziwei corpus.
Terms: tiandi-shu, wanxiang-gui-yiyuan, yiyuan, duoyuan, sanpan (ziwei context only counts).
Read-only on sources; prints stats + hit contexts to stdout. No source copies written.
"""
import os, re, subprocess, sys, zipfile

BOOK = "/home/hatch/workspace/divination/incoming/wanted-books-6/Book"
TERMS = [
    ("天地數", r"天地數"), ("天地数", r"天地数"),
    ("萬象歸一元", r"萬象歸一元"), ("万象归一元", r"万象归一元"),
    ("萬象歸一", r"萬象歸一"), ("万象归一", r"万象归一"),
    ("歸一元", r"歸一元"), ("归一元", r"归一元"),
    ("一元", r"一元"), ("多元", r"多元"),
    ("三盤", r"三盤"), ("三盘", r"三盘"),
    ("天地人", r"天地人"), ("天地盤", r"天地盤"), ("天地盘", r"天地盘"),
]

def pdf_text(path):
    try:
        out = subprocess.run(["pdftotext", "-layout", path, "-"],
                             capture_output=True, timeout=300)
        return out.stdout.decode("utf-8", errors="replace")
    except Exception as e:
        return ""

def pdf_pages(path):
    try:
        out = subprocess.run(["pdfinfo", path], capture_output=True, timeout=60)
        s = out.stdout.decode("utf-8", errors="replace")
        m = re.search(r"Pages:\s+(\d+)", s)
        return int(m.group(1)) if m else -1
    except Exception:
        return -1

def docx_text(path):
    try:
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml").decode("utf-8", errors="replace")
        xml = re.sub(r"<[^>]+>", "", xml)
        return xml
    except Exception:
        return ""

def page_of(text, idx):
    # pdftotext separates pages with \f
    return text[:idx].count("\f") + 1

def main():
    files = sorted(os.listdir(BOOK))
    for fn in files:
        path = os.path.join(BOOK, fn)
        ext = os.path.splitext(fn)[1].lower()
        if ext == ".pdf":
            pages = pdf_pages(path)
            text = pdf_text(path)
        elif ext == ".docx":
            pages = -2
            text = docx_text(path)
        else:
            print(f"\n=== {fn} | ext={ext} SKIPPED (no text route; pdf twin searched if present) ===")
            continue
        # normalize whitespace for search but keep page breaks: remove spaces/newlines inside text for CJK matching
        flat = text.replace(" ", "").replace("\u3000", "")
        flat_nolf = flat.replace("\n", "").replace("\r", "")
        has_text = len(text.strip())
        print(f"\n=== {fn} | pages={pages} | text_chars={has_text} ===")
        if has_text < 200:
            print("  TEXTLAYER: NONE/NEGLIGIBLE -> visual-only route")
            continue
        print("  TEXTLAYER: YES")
        for label, pat in TERMS:
            hits = [m.start() for m in re.finditer(pat, flat_nolf)]
            # page numbers need original text; approximate via flat with \f kept
            flat_ff = text.replace(" ", "").replace("\u3000", "").replace("\n", "").replace("\r", "")
            print(f"  TERM {label}: {len(hits)} hit(s)")
            for h in hits[:6]:
                ctx = flat_nolf[max(0, h-45):h+55].replace("\f", "|")
                pg = flat_ff[:h].count("\f") + 1
                print(f"    ~p{pg}: ...{ctx}...")

if __name__ == "__main__":
    main()
