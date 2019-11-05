# canvas其实就是画布，是各种图形的载体。
# 比如，下面的代码创建了一个绿色的画布：
from tkinter import *
root = Tk()
cv = Canvas(root,bg = 'green')
# 在画布里面画一个矩形：
# cv.create_rectangle(10,20,365,200)
# 注意此时，这个矩形左上角的坐标是(10,20)，右下角的坐标是(365,200)。
# 把这个矩形填充为蓝色：
# cv.create_rectangle(10,20,365,200,fill='blue')
# 把矩形的边界显示为红色，矩形边框的宽度是2，矩形边框设定为虚线：另外使用额外的填充方法
cv.create_rectangle(10,20,365,200,stipple = 'gray12',fill='blue',outline='red', width=2, dash=10)
cv.pack()
root.mainloop()


