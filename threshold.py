from PIL import Image
fg="C:\\Users\\HP\\Desktop\\Gökçe_Yağmur_Budak_21732948\\urban.jpg"
ft="C:\\Users\\HP\\Desktop\\Gökçe_Yağmur_Budak_21732948\\urbanThreshold.jpg"

img=Image.open(fg)
imgt=Image.new(img.mode,img.size,color=0)
pixel=img.load()

print(pixel[0,0])

threshold=125
#I scan our size of image
for y in range (img.height):
    for x in range (img.width):
#get our pixels value in image
        pixel=img.getpixel((x,y))
#think about you draw a line that perpendicular x axis -on the 125 or another value-,
#if your pixel value bigger than 125 ,that's part white or bright,
#if your pizel value smaller than 125 ,that's part black or dark..
        if pixel > threshold:
            new_value=255
            imgt.putpixel((x,y),new_value)

        else:
            new_value=0
            imgt.putpixel((x,y),new_value)


        
imgt.save(ft)
