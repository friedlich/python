# font字体的参数有如下6个
#     family: 字体类别，如'Fixdsys'
#     size: 作为一个整数，以点字体的高度。为了获得字体的n个像素高，使用-n.
#     weight: "BOLD" 表示加粗, "NORMAL" 表示正常大小，默认是NORMAL
#     slant：斜体（默认正常）， “NORMAL”表示正常，"ITALIC"表示字体倾斜
#     underline：下划线，1表示添加下滑线，0表示没有，默认值为0
#     overstrike：删除线，1表示添加删除线，0表示没有，默认值为0
    # -*- coding: utf-8 -*-
from tkinter import *
# 引入字体模块
import tkinter.font as tkFont

root = Tk()
# 创建一个Label
# 指定字体名称、大小、样式
ft = tkFont.Font(family='Fixdsys', size=10, weight=tkFont.BOLD)
ft1 = tkFont.Font(size=20, slant=tkFont.ITALIC)
ft2 = tkFont.Font(size=30, weight=tkFont.BOLD, underline=1, overstrike=1)

Label(root, text='thist is a demo', font=ft).grid()
Label(root, text='hello python ', font=ft1).grid()
Label(root, text='good luck', font=ft2).grid()

root.mainloop()
# 使用tkFont.Font来创建字体。
