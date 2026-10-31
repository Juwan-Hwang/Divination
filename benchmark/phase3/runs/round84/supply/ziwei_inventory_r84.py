#!/usr/bin/env python3
"""R84 Ziwei pack inventory: hash/size verification only. Read-only on pack."""
import hashlib, json, os, re, subprocess, sys

BASE = "/home/hatch/workspace/divination/incoming/wanted-books-6"
BOOK = os.path.join(BASE, "Book")
SUMS = os.path.join(BASE, "SHA256SUMS.txt")
SEVENZ = os.path.join(BASE, "Book.7z")

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def pdf_pages(path):
    try:
        out = subprocess.run(["pdfinfo", path], capture_output=True, text=True, timeout=30).stdout
        m = re.search(r"^Pages:\s+(\d+)", out, re.M)
        return int(m.group(1)) if m else None
    except Exception:
        return None

sums = {}
with open(SUMS, encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\n")
        if not line.strip():
            continue
        digest, name = line.split("  ", 1) if "  " in line else line.split(None, 1)
        sums[name.strip()] = digest.strip()

files = sorted(os.listdir(BOOK))
rows = []
for name in files:
    p = os.path.join(BOOK, name)
    if not os.path.isfile(p):
        rows.append({"name": name, "is_file": False})
        continue
    ext = os.path.splitext(name)[1].lower().lstrip(".")
    digest = sha256(p)
    rows.append({
        "name": name, "format": ext, "bytes": os.path.getsize(p),
        "sha256": digest, "sums_sha256": sums.get(name),
        "match": (sums.get(name) == digest),
        "in_sums": name in sums,
        "pdf_pages": pdf_pages(p) if ext == "pdf" else None,
    })

extra_in_sums = sorted(set(sums) - set(files))
result = {
    "book7z": {"bytes": os.path.getsize(SEVENZ), "sha256": sha256(SEVENZ)},
    "sums_lines": len(sums),
    "book_files": len([r for r in rows if r.get("is_file", True)]),
    "all_match": all(r.get("match") for r in rows) and not extra_in_sums,
    "extra_in_sums": extra_in_sums,
    "total_bytes_book": sum(r.get("bytes", 0) for r in rows),
    "rows": rows,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
