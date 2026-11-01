from PIL import Image
import os
H="/home/hatch/workspace/divination/benchmark/phase3/runs/round96/supply/pages-caiminghong-r96/hires"
jobs=[
 ("cmh-232.png","cmh-232-cropA-rate5.png",(0.07,0.15,0.44,0.42)),
 ("cmh-232.png","cmh-232-cropB-rate5.png",(0.07,0.52,0.44,0.74)),
 ("cmh-242.png","cmh-242-crop-rate5.png",(0.12,0.51,0.45,0.74)),
 ("cmh-243.png","cmh-243-cropA-rate5.png",(0.15,0.15,0.46,0.37)),
 ("cmh-243.png","cmh-243-cropB-rate5.png",(0.16,0.63,0.50,0.88)),
]
for src,dst,(x0,y0,x1,y1) in jobs:
    im=Image.open(os.path.join(H,src)); w,h=im.size
    c=im.crop((int(w*x0),int(h*y0),int(w*x1),int(h*y1)))
    c=c.resize((c.size[0]*2,c.size[1]*2))
    c.save(os.path.join(H,dst)); print(dst,c.size,os.path.getsize(os.path.join(H,dst)))
