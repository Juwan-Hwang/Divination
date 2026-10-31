from PIL import Image, ImageDraw
import os
src="pages-xuzengsheng-r92"; out="sheets-xuzengsheng-r92"; os.makedirs(out,exist_ok=True)
halves=[]  # (pdfpage, side, image)
for n in range(41,183):
    im=Image.open(f"{src}/xzs-{n:03d}.png"); w,h=im.size; mid=w//2
    halves.append((n,'R',im.crop((mid,0,w,h))))
    halves.append((n,'L',im.crop((0,0,mid,h))))
# sheets of 12 halves
per=12; tw=560
for si in range(0,len(halves),per):
    grp=halves[si:si+per]; th=int(tw*grp[0][2].size[1]/grp[0][2].size[0])
    cols=3; rows=(len(grp)+cols-1)//cols
    sheet=Image.new('RGB',(cols*tw, rows*(th+26)),'white'); d=ImageDraw.Draw(sheet)
    for i,(n,side,im) in enumerate(grp):
        t=im.resize((tw,th)); x=(i%cols)*tw; y=(i//cols)*(th+26)
        sheet.paste(t,(x,y+26)); d.text((x+6,y+6),f"PDF{n} {side}",fill='red')
    sheet.save(f"{out}/sheet-{si//per+1:02d}.png")
print("sheets:", (len(halves)+per-1)//per, "halves:", len(halves))
