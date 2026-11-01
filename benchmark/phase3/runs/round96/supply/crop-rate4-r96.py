from PIL import Image
import os
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pages-caiminghong-r96", "hires")
# relative crops (x0,y0,x1,y1) around chart areas
jobs = {
    "cmh-215-215.png": ("crop4-215-chart.png", (0.13, 0.15, 0.47, 0.37)),
    "cmh-222-222.png": ("crop4-222-chart.png", (0.08, 0.49, 0.42, 0.71)),
    "cmh-223-223.png": ("crop4-223-charts.png", (0.11, 0.16, 0.45, 0.72)),
    "cmh-231-231.png": ("crop4-231-chart.png", (0.07, 0.53, 0.47, 0.78)),
}
for src, (dst, (x0, y0, x1, y1)) in jobs.items():
    im = Image.open(os.path.join(base, src))
    w, h = im.size
    c = im.crop((int(w*x0), int(h*y0), int(w*x1), int(h*y1)))
    c = c.resize((c.width*2, c.height*2), Image.LANCZOS)
    c.save(os.path.join(base, dst))
    print(dst, c.size)
