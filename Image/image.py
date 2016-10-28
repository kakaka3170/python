
from PIL import Image;



print ('================ image.py ===============');

im=Image.open('22.png');

print(im.size);

im45 = im.rotate(45);

im45.save('22-45.png');


##################################
box = (500,500,1200,1200);
region = im.crop(box);
#region.show();

region45 = region.rotate(45);

im.paste(region45,box)

#im.show();

##################################

def dnoo (i):
    return i*0.3;

imred = Image.new("RGB",(640,480),(255,0,0));
imred.point(dnoo);



for x in range(200,300):
    imred.putpixel((x,400),(0,233,233));
    imred.putpixel((x,401),(0,233,233));

imred.show();


##################################

r,g,b = im.split();
r.show();
g.show();
b.show();





##################################

