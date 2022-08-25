from PIL import Image
#create new Image , have greylevel and white background
img=Image.new("L",(800,700),"white")

w,h=img.size

pixels=img.load()
#scan image size,my start value 0 and till my end value w for the starting for loop.
#if I have step 10,points appear small and many.
for i in range (0,w,10):
  for j in range (0,h,10):
    img.putpixel((i,j),0)

img.save("C:\\Users\\HP\\Desktop\\Gökçe_Yağmur_Budak_21732948\\pattern.jpg")
