# 1. 简介
# Label用于在指定的窗口中显示文本和图像。最终呈现出的Label是由背景和前景叠加构成的内容。
# Label组件定义函数：Label（master=None, cnf={}, **kw） 其中，kw参数是用来自定义lable组件的键值对。

# 2.  背景自定义
# 背景的话，有三部分构成：内容区+填充区+边框
# <1>内容区参数有：width,length用于指定区域大小，如果显示前景内容是文本，则以单个字符大小为单位；如果显示的是图像，则以像素为单位。
# 默认值是根据具体显示的内容动态调整。类型是int。 background用于指定背景的颜色，默认值根据系统而定。
# <2>填充区参数:指的是内容区和边框之间的间隔大小，单位是像素。参数有：padx , pady，类型是int。
# <3>边框参数：样式relief(可选值为：flat(默认),sunken,raised,groove,ridge)，borderwidth(边框的宽度，单位是像素，默认根据系统
# 而定，一般是1或2像素)
# highlightbackground,highlightcolor,highlightthickness 三个边框参数仅在Label允许接收焦点的情况下（tackfocus=True），
# 用于设置焦点获取前后高亮边框颜色以及高亮边框宽度。
# 举个栗子（@-@）: 上图右侧为，背景图构成：内容区（黑色），填充区（绿色），边框（黄色）
# 定义的背景内容区是可容纳3X9的字符区，如上图中的右侧小窗口中的Label。增加了填充区和边框后的效果如上图中左侧的Label。

# 3.  前景自定义
# 前景定义分为文本内容和图像两小块来说明。
# 3.1 文本  
# 文本内容选项有：
# <1>指定字体和字体大小，如：font = (font_name,size)，默认有系统指定
# <2>文本对齐方式，justify = "center(默认)left/right/"
# <3>指定文本（或图像）颜色，foreground = "指定的颜色"，可以是英文名字，也可以是RGB格式的
# <4>指定文本内容：（静态的）text = "目标字符串....."；  （动态更新的）textvariable = str_obj，当str_obg的内容改变时，
# 会更新Label中对应内容。这里需要注意的是str_obj必须是TKinter所支持的字符串类型变量，如：
# str_obj = Tkinter.StringVar()      str_obj.set("目标文本内容")
# <5>单个字符添加下划线，underline = index， index是目标字符串中的字符索引值。
# <6>文本或图像在背景内容区的位置：anchor  可选值为（n,s,w,e,ne,nw,sw,se,center）eswn是东南西北英文的首字母，
# 表示：上北下南左西右东
# 图像内容选项有：
# <1>指定图片：bitmap = bitmap_image，当指定image选项的时候，这个参数会被忽略掉     
# 或者  image = normal_image(仅支持GIF, PPM/PGM格式的图片)" 。
# 需要注意的是这里的所用到的图片对象bitmap_image  normal_image都是需要经过TKinter转换后的图像格式。如： 
# bitmap_image = TKinter.BitmapImage(file = "位图片路径") ormal_image = TKinter.PhotoImage(file = "gif 、ppm/pgm图片路径")
# 图片和文本取舍：
# compound参数可以控制要显示的文本和图像。当同时指明了要显示的文本和图像时，可以通过该参数来进行不同设置。可选值：
# None 默认值，表示只显示图像，不显示文本；bottom/top/left/right，表示图片显示在文本的下/上/左/右；center,表示文本显示在图片中心上方。
# 上图左中的compound="bottom"，表示图片显示在文字下方；上图左中的compound="center"，表示文字显示在图片中间上方

# 4. Label的其他参数
# <1>activebacakground  activeforground   用于设置Label处于活动（active）状态下的背景和前景颜色,默认由系统指定。
# <2>diableforground  指定当Label不可用的状态（Disable）下的前景颜色，默认由系统指定。
# <3>cursor 指定鼠标经过Label的时候，鼠标的样式，默认由系统指定。
# <4>state  指定Label的状态，用于控制Label如何显示。可选值有：normal(默认)/active/disable。

# 程序源码


#coding=utf-8
import tkinter as tk
import sys
    
if __name__ == "__main__":
    import tkinter as tk
    master = tk.Tk()
    str_obj = tk.StringVar()
    str_obj.set("这是TKinter所支持的字符串类型")
    
    # bitmap_image = tk.BitmapImage(file =  sys.path[0] + "\\背景自定义2.bmp")
    normal_image = tk.PhotoImage(file = sys.path[0] + "\\tkinter中的颜色.png")
    print(type(normal_image)) # <class 'tkinter.PhotoImage'>
    print(normal_image) # pyimage1 
    w = tk.Label(master,
                    #背景选项
                    #height = 5,
                    #width = 20,
                    padx=10,
                    pady=20,
                    background="blue",
                    relief="ridge",
                    borderwidth=10,
                    #文本
                    text = "123456789\nabcde\nABCDEFG",
                    #textvariable = str_obj,
                    justify = "left",
                    foreground = "white",
                    underline = 4,
                    anchor = "ne",
                    #图像
                    image = normal_image,
                    compound = "bottom",
                    #接受焦点
                    #takefocus = True,
                    #highlightbackground = "yellow",
                    #highlightcolor = "white",
                    #highlightthickness = 5
                    )
    w.pack()
    master.mainloop()


