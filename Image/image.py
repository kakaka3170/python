
from PIL import Image;

from dnlib import dosomething;
from dnlib import Student; 


print ('================ start01.py ===============');

print('call function something()  -- in file start01.py');
dosomething();

im=Image.open('22.png');

#print (im.format,im.size,im.mode);
im.show();
print('test object Student');
yanghaoyuan = Student(1001,'yanghaoyuan',7,'m');
yanghaoyuan.printinfo();
