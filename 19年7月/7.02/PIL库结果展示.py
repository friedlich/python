# 缩略图代码：
from PIL import Image
img = Image.open(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\7.02\莲花.jpg')
img = img.resize((100, 128), Image.ANTIALIAS)
img.save(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\7.02\莲花_small.jpg')


# 图片颜色处理：
from PIL import Image
im= Image.open(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\7.02\莲花.jpg')
r,g,b=im.split()
om = Image.merge("RGB",(g,b,r))#修改颜色
om.save(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\7.02\莲花_color.jpg')


# 轮廓，浮雕，锐化等处理代码：
from PIL import Image
from PIL import ImageFilter
im= Image.open(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\7.02\莲花.jpg')
om = im.filter(ImageFilter.CONTOUR)#轮廓处理
#om = im.filter(ImageFilter.EMBOSS)#浮雕处理
#om = im.filter(ImageFilter.SHARPEN)#锐化处理
om.save(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\7.02\莲花_contour.jpg')


# 提取GIF图的每一帧代码：
from PIL import Image
im= Image.open(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\7.02\123.gif')
try:
    im.save(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\7.02\123_{:02d}.png'.format(im.tell()))
    while True:
        im.seek(im.tell()+1)
        im.save(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\7.02\123_{:02d}.png'.format(im.tell()))
except:
    print("over")