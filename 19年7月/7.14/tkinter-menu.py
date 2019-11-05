import tkinter 
menuWin = tkinter.Tk()
menuWin.title('菜单窗口')
lab = tkinter.Label(menuWin,
            text='tkinter版本\n挺好玩',
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
lab.pack()
menus=tkinter.Menu(menuWin)
submenu=tkinter.Menu(menus,tearoff=0)
menus.add_cascade(label='文件',menu=submenu)
submenu.add_command(label='新建')
submenu.add_command(label='打开')
submenu.add_command(label='保存')
submenu.add_command(label='关闭')
submenu.add_command(label='退出')
menuWin.config(menu=menus)  # 查看代码可以知道，是由于缺少一个方法config()，需要将menu配置到window窗口
menuWin.mainloop()