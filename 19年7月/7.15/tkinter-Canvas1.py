# Tkinter 提供了 Canvas 组件来实现绘图。程序既可在 Canvas 中绘制直线、矩形、椭圆等各种几何图形，也可绘制图片、文字、UI 组件
# （如 Button）等。Canvas 允许重新改变这些图形项（Tkinter 将程序绘制的所有东西统称为 item）的属性，比如改变其坐标、外观等。
# Canvas 组件的用法与其他 GUI 组件一样简单，程序只要创建并添加 Canvas 组件，然后调用该组件的方法来绘制图形即可。
# 如下程序示范了最简单的 Canvas 绘图： 
from tkinter import *
# 创建窗口
root = Tk()
# 创建并添加Canvas
cv = Canvas(root, background='white')
cv.pack(fill=BOTH, expand=YES)
cv.create_rectangle(30, 30, 200, 200,
    outline='red', # 边框颜色
    stipple = 'question', # 填充的位图
    fill="red", # 填充颜色
    width=5 # 边框宽度
    )
cv.create_oval(240, 30, 330, 200,
    outline='yellow', # 边框颜色
    fill='pink', # 填充颜色
    width=4 # 边框宽度
    )
root.mainloop()
# 上面程序先创建并添加了 Canvas 组件，分别绘制了矩形和椭圆

# 从上面程序可以看到，Canvas 提供了 create_rectangle() 方法绘制矩形和 create_oval() 方法绘制椭圆（包括圆，圆是椭圆的特例）。
# 实际上，Canvas 还提供了如下方法来绘制各种图形：
# create_arc：绘制弧。
# create_bitmap：绘制位图。
# create_image：绘制图片。
# create_line()：绘制直线。
# create_polygon：绘制多边形。
# create_text：绘制文字。
# create_window：绘制组件。

### Canvas 的坐标系统是绘图的基础，其中点 (0,0) 位于 Canvas 组件的左上角，X 轴水平向右延伸，Y 轴垂直向下延伸。
# 绘制上面这些图形时需要简单的几何基础：
# 在使用 create_line() 绘制直线时，需要指定两个点的坐标，分别作为直线的起点和终点。
# 在使用 create_rectangle() 绘制矩形时，需要指定两个点的坐标，分别作为矩形左上角点和右下角点的坐标。
# 在使用 create_oval() 绘制椭圆时，需要指定两个点的坐标，分别作为左上角点和右下角点的坐标来确定一个矩形，而该方法则负责绘制
# 该矩形的内切椭圆,只要矩形确定下来，该矩形的内切椭圆就能确定下来，而 create_oval() 方法所需要的两个坐标正是用于指定该矩形的
# 左上角点和右下角点的坐标。
# 在使用 create_arc 绘制弧时，和 create_oval 的用法相似，因为弧是椭圆的一部分，因此同样也是指定左上角和右下角两个点的坐标，
# 默认总是绘制从 3 点（0）开始，逆时针旋转 90° 的那一段弧。程序可通过 start 改变起始角度，也可通过 extent 改变转过的角度。
# 在使用 create_polygon 绘制多边形时，需要指定多个点的坐标来作为多边形的多个定点；在使用 create_bitmap、create_image、
# create_text、create_window 等方法时，只要指定一个坐标点，用于指定目标元素的绘制位置即可。

# 在绘制这些图形时可指定如下选项：
# fill：指定填充颜色。如果不指定该选项，默认不填充。
# outline：指定边框颜色。
# width：指定边框宽度。如果不指定该选项，边框宽度默认为 1。
# dash：指定边框使用虚线。该属性值既可为单独的整数，用于指定虚线中线段的长度；也可为形如（5,2,3）格式的元素，此时5 指定虚线中
# 线段的长度，2 指定间隔长度，3 指定虚线长度……依此类推。
# stipple：使用位图平铺进行填充。该选项可与 fill 选项结合使用，fill 选项用于指定位图的颜色。
# style：指定绘制弧的样式。该选项仅对 create_arc 方法起作用。该选项支持 PIESLICE（扇形）、CHORD（弓形）、ARC（仅绘制弧）选项值。
# start：指定绘制弧的起始角度。该选项仅对 create_arc 方法起作用。
# extent：指定绘制弧的角度。该选项仅对 create_arc 方法起作用。
# arrow：指定绘制直线时两端是否有箭头。该选项支持 NONE（两端无箭头）、FIRST（开始端有箭头）、LAST（结束端有箭头）、
# BOTH（两端都有箭头）选项值。
# arrowshape：指定箭头形状。该选项是一个形如 "20 20 10" 的字符串，字符串中的三个整数依次指定填充长度、箭头长度、箭头宽度。
# joinstyle：指定直接连接点的风格。仅对绘制直线和多向形有效。该选项支持 METTER、ROUND、BEVEL 选项值。
# anchor：指定绘制文字、GUI 组件的位置。该选项仅对 create_text()、create_window() 方法有效。
# justify：指定文字的对齐方式。该选项支持 CENTER、LEFT、RIGHT 常量值，该选项仅对 create_text 方法有效。

