# 题目 画椭圆。
# 程序分析 使用 tkinter
if __name__ == '__main__':
    import tkinter
    x = 360
    y = 160
    top = y - 30
    bottom = y - 30
    canvas = tkinter.Canvas(width=400,height=600,bg='white')
    for i in range(20):
        canvas.create_oval(250-top,250-bottom,
        250+top,250+bottom)
        top-=5
        bottom+=5
    canvas.pack()
    canvas.mainloop()

    
