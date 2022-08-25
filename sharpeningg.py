from PIL import Image

f = "C:\\Users\\HP\\Desktop\\Gökçe_Yağmur_Budak_21732948\\urban.jpg"
fsharp="C:\\Users\\HP\\Desktop\\Gökçe_Yağmur_Budak_21732948\\urban_sharpening.jpg"
sharp =[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,25,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

img = Image.open(f)
width, height = img.size
pixels = img.load()
imgsharp = Image.new(img.mode, img.size, color=0)

#I scan image size.
for w in range(width):
    for h in range(height):
        if w in (0, width-1) or w in (1, width-2) or h in (0, height-1) or h in (1, height-2):
#put pixel value in my new image
            imgsharp.putpixel((w, h), pixels[w, h])
            
        else:
            total = 0
            c = 24
            #c our neighboor
            for k in range(5):
                for m in range(5):
# for 5*5 , we do sharp on our new image
                    total += (pixels[w -k + 2, h- m + 2] * sharp[c])
                    c -= 1
                    newvalue = int(total/25)
                    if newvalue < 0:
                        imgsharp.putpixel((w, h), 0)
                    elif newvalue > 255:
                        imgsharp.putpixel((w, h), 255)
                    else:
                        imgsharp.putpixel((w, h), newvalue)
imgsharp.save(fsharp)

