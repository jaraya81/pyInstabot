from PIL import Image, ImageDraw, ImageFont
import glob
import os
out_path=r"/home/soumya/Desktop/Python_Insta_botting/photos"
os.chdir(r'/home/soumya/Desktop/Python_Insta_botting/content_tst/content/pready')
myFiles=glob.glob('*.txt')
W, H = (1000,1000)
for text_file in myFiles:
    str=""
    with open(text_file,'r',encoding='utf-8-sig') as t:
        str=t.read()
    #print(str)
    in_file=r"/home/soumya/Desktop/Python_Insta_botting/content_tst/content/pready/PSU_template.jpg"
   # out_file=text_file[:-4]+".jpg"
    print(text_file)
    out_file=out_path+"/"+text_file[:-4]+".jpg"
    img = Image.open(in_file)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(r'/home/soumya/Downloads/caviar-dreams/CaviarDreams.ttf', 39)
    w, h = draw.multiline_textsize(str)
    
    print(w,h)
    if h>90:
        draw.text((((W-w)/2)-150, ((H-h)/2)-150), str, fill=(255,255,255,255),spacing=30, font=font,align ="left")
    elif h>80 and h<=90:
        draw.text((((W-w)/2)-150, ((H-h)/2)-100), str, fill=(255,255,255,255),spacing=30, font=font,align ="left")
    else:
        draw.text((((W-w)/2)-150, ((H-h)/2)-60), str, fill=(255,255,255,255),spacing=30, font=font,align ="left")
    img.save(out_file)
