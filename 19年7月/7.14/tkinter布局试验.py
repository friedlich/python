import tkinter
import tkinter.font as tkFont

root=tkinter.Tk() #生成主窗口
root.title('计算器') #修改框体的名字
root.resizable(0,0) #框体大小可调性，分别表示x,y方向的可变性
ft = tkFont.Font(weight=tkFont.BOLD, underline=1, overstrike=1)
# size:作为一个整数，以点字体的高度;weight:"BOLD" 表示加粗;slant：斜体（默认正常）;underline:下划线;overstrike:删除线
entry1 = tkinter.Label(root,
                       text='tkinter版本\n挺好玩',
                       font=ft,
                       justify='left',
                       padx=10,
                       pady=15,
                       relief="ridge",
                       borderwidth=10,
                       fg='#0000FF',
                       bg='#FF8C00',
                       width=20,
                       height=2,
                       anchor='nw') 
# 生成标签，标签可以显示文字或图片
# anchor:标签中文本的位置;bg:背景色;height:标签高度;width:标签宽度;text:标签中的文本，可以使用'\n'表示换行
# justify:多行文本的对齐方式;font:字体;
entry1.grid(row=0,columnspan=5) #grid组件使用行列的方法放置组件的位置;columnspan:组件的列宽;row:组件所在的行起始位置
buttonMC=tkinter.Button(root,text='MC',width=5) #text指定按钮上显示的文本;width指定按钮的宽度;command指定按钮消息的回调函数
buttonMR=tkinter.Button(root,text='MR',width=5) #生成buttonMR
buttonMS=tkinter.Button(root,text='MS',width=5)
buttonM1=tkinter.Button(root,text='M+',width=5)
buttonM2=tkinter.Button(root,text='M-',width=5)
buttonMC.grid(row=1,column=0) #grid组件使用行列的方法放置组件的位置
buttonMR.grid(row=1,column=1) #row: 组件所在的行起始位置  column: 组件所在的列起始位置
buttonMS.grid(row=1,column=2)
buttonM1.grid(row=1,column=3)
buttonM2.grid(row=1,column=4)

buttonJ=tkinter.Button(root,text='←',width=5) #text指定按钮上显示的文本 width指定按钮的宽度
buttonCE=tkinter.Button(root,text='CE',width=5)
buttonC=tkinter.Button(root,text=' C ',width=5)
button12=tkinter.Button(root,text='±',width=5)
buttonD=tkinter.Button(root,text='√',width=5)
buttonJ.grid(row=2,column=0) #grid组件使用行列的方法放置组件的位置
buttonCE.grid(row=2,column=1) #row: 组件所在的行起始位置  column: 组件所在的列起始位置
buttonC.grid(row=2,column=2)
button12.grid(row=2,column=3)
buttonD.grid(row=2,column=4)

button7=tkinter.Button(root,text=' 7 ',width=5)
button8=tkinter.Button(root,text=' 8 ',width=5)
button9=tkinter.Button(root,text=' 9 ',width=5)
buttonc=tkinter.Button(root, text=' / ',width=5)
buttonf= tkinter.Button(root, text=' % ',width=5)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
buttonc.grid(row=3,column=3)
buttonf.grid(row=3,column=4)

button4=tkinter.Button(root,text=' 4 ',width=5)
button5=tkinter.Button(root,text=' 5 ',width=5)
button6=tkinter.Button(root,text=' 6 ',width=5)
buttonx=tkinter.Button(root,text=' * ',width=5)
buttonfs=tkinter.Button(root,text='1/x',width=5)
button4.grid(row=4,column=0)
button5.grid(row=4,column=1)
button6.grid(row=4,column=2)
buttonx.grid(row=4,column=3)
buttonfs.grid(row=4,column=4)

button1 = tkinter.Button(root, text=' 1 ',width=5)
button2 = tkinter.Button(root, text=' 2 ',width=5)
button3 = tkinter.Button(root, text=' 3 ',width=5)
button_= tkinter.Button(root, text=' - ',width=5)
buttondy= tkinter.Button(root, text=' \n = \n ',width=5)
button1.grid(row=5, column=0)
button2.grid(row=5, column=1)
button3.grid(row=5, column=2)
button_.grid(row=5, column=3)
buttondy.grid(row=5, column=4,rowspan=2)

button0=tkinter.Button(root,text='   0   ',width=11)
buttonjh = tkinter.Button(root,text=' . ',width=5)
buttonjia=tkinter.Button(root,text=' + ',width=5)
button0.grid(row=6,column=0,columnspan=2)
buttonjh.grid(row=6,column=2)
buttonjia.grid(row=6,column=3)

menu=tkinter.Menu(root)
submenu1=tkinter.Menu(menu,tearoff=0)
menu.add_cascade(label='查看',menu=submenu1)
submenu2 = tkinter.Menu(menu, tearoff=0)
submenu2.add_command(label='复制')
submenu2.add_command(label='粘贴')
menu.add_cascade(label='编辑',menu=submenu2)
submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label='查看帮助')
submenu.add_separator()
submenu.add_command(label='关于计算机')
menu.add_cascade(label='帮助',menu=submenu)
root.config(menu=menu)

root.mainloop()