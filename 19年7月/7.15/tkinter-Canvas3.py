#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    from  tkinter import *
    root = Tk() #Tk()是Tkinter库中的一个函数.
    root.title('什么鬼')
    canvas = Canvas(root,
                    width = 400, # Canvas的宽度
                    height = 400,# Canvas的高度
                    bg = 'red'   # Canvas的背景颜色
                    )
    x0 = 20
    y0 = 20
    y1 = 275
    x1 = 275
    # 矩形
    canvas.create_rectangle(x0,y0,x1,y1,fill ='yellow') # 矩形 两个坐标点 (x0,y0) (x1,y1) 起始点和终点 在一个对角线上
    # 直线
    canvas.create_line(30,30,300,30,width ='1',fill = 'green') # 直线 (30,30)(300,30) 起点和终点
    # 椭圆
    a1 = 100
    b1 = 100 # 中心点坐标
    r = 60   # 半径
    w1 = 90
    h1 = 60
    # w1和h1表示 左右和上下的距离
    # canvas.create_oval(a1 - r,b1 - r,w1,h1,width = '1',fill = 'purple')
    canvas.create_oval(a1-r,b1-r,w1,h1,width = '1',fill = 'purple')

    # 圆弧
    canvas.create_arc(60,100,300,200, # 坐标含义自己尝试 extent 设置90 和 180就会明白
                      start = '60',extent = '90') # 圆弧的起止角度


    canvas.pack(expand=YES, fill=BOTH) # 将Canvas添加到主窗口
    # expand置1
    # 使能fill属性
    # expand置0
    # 关闭fill属性
    # fill = X
    # 当GUI窗体大小发生变化时，widget在X方向跟随GUI窗体变化
    # fill = Y
    # 当GUI窗体大小发生变化时，widget在Y方向跟随GUI窗体变化
    # fill = BOTH
    # 当GUI窗体大小发生变化时，widget在X、Y两方向跟随GUI窗体变化
    # canvas.pack()

    root.mainloop()

