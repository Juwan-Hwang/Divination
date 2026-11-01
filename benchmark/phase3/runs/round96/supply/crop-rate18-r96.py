#!/usr/bin/env python3
from PIL import Image
p = "/home/hatch/workspace/divination/benchmark/phase3/runs/round96/supply/pages-caiminghong-r96/hires/cmh-606.png"
im = Image.open(p)
W, H = im.size
print(W, H)
# upper chart approx x 0.10-0.42, y 0.22-0.44 ; lower chart y 0.52-0.74
for name, box in [("crop18-upper", (0.09, 0.21, 0.43, 0.45)), ("crop18-lower", (0.09, 0.51, 0.43, 0.75))]:
    c = im.crop((int(box[0]*W), int(box[1]*H), int(box[2]*W), int(box[3]*H)))
    c = c.resize((c.width*2, c.height*2), Image.LANCZOS)
    out = f"/home/hatch/workspace/divination/benchmark/phase3/runs/round96/supply/pages-caiminghong-r96/hires/{name}.png"
    c.save(out)
    print(out, c.size)
