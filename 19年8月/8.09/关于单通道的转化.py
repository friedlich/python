from PIL import Image
import numpy as np
im = np.asarray(Image.open(r'c:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年8月\8.09\caozuo-1.jpg'))
print(im.shape)
if len(im) == 2: 
    c = [] 
    for i in range(3): 
        c.append(im) 
    im = np.asarray(c)
    im = im.transpose([1,2,0])
    print(im.shape)


# （一）：单通道图，俗称灰度图，每个像素点只能有有一个值表示颜色，它的像素值在0到255之间，0是黑色，255是白色，中间值是一些
# 不同等级的灰色。（也有3通道的灰度图，3通道灰度图只有一个通道有值，其他两个通道的值都是零）。
# （二）:三通道图，每个像素点都有3个值表示，所以就是3通道。也有4通道的图。例如RGB图片即为三通道图片，RGB色彩模式是工业界的
# 一种颜色标准，是通过对红(R)、绿(G)、蓝(B)三个颜色通道的变化以及它们相互之间的叠加来得到各式各样的颜色的，RGB即是代表红、
# 绿、蓝三个通道的颜色，这个标准几乎包括了人类视力所能感知的所有颜色，是目前运用最广的颜色系统之一。总之，每一个点由三个值表示。