if __name__ == '__main__':
    import tkinter as tk
    master = tk.Tk()
    w = tk.Label(master,
                height=3,
                width=9,
                padx=10,
                pady=20,
                background='blue',
                relief='ridge',
                borderwidth=10,
                text='123456789\nabcde\nABCDEFG',
                justify='right',
                foreground='red',
                anchor='center')
    w.pack()
    master.mainloop()
# 上图右侧为，背景图构成：内容区（黑色），填充区（绿色），边框（黄色）
# 定义的背景内容区是可容纳3X9的字符区，如上图中的右侧小窗口中的Label。增加了填充区和边框后的效果如上图中左侧的Label。

# 2.  背景自定义
# 背景的话，有三部分构成：内容区+填充区+边框
# <1>内容区参数有：width,length用于指定区域大小，如果显示前景内容是文本，则以单个字符大小为单位；如果显示的是图像，则以像素为单位。
# 默认值是根据具体显示的内容动态调整。类型是int。 background用于指定背景的颜色，默认值根据系统而定。
# <2>填充区参数:指的是内容区和边框之间的间隔大小，单位是像素。参数有：padx , pady，类型是int。
# <3>边框参数：样式relief(可选值为：flat(默认),sunken,raised,groove,ridge)，borderwidth(边框的宽度，单位是像素，默认根据系统
# 而定，一般是1或2像素)
# highlightbackground,highlightcolor,highlightthickness 三个边框参数仅在Label允许接收焦点的情况下（tackfocus=True），
# 用于设置焦点获取前后高亮边框颜色以及高亮边框宽度。
                    
