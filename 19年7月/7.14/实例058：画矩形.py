# 题目 画图，学用rectangle画方形。
# 程序分析 无。
if __name__=='__main__':
    import tkinter
    root = tkinter.Tk()
    root.title('就这一次试验呀')
    canvas = tkinter.Canvas(root,width=400,height=400,bg='yellow') # 虽然加不加root界面不会有什么变化，但是加的话应该是直接打到root上的，肯定有影响
    x0=263
    y0=263
    x1=275
    y1=275
    for i in range(19):
        canvas.create_rectangle(x0,y0,
        x1,y1)
        x0-=5
        y0-=5
        x1+=5
        y1+=5
    canvas.pack()
    root.mainloop()


# if __name__ == '__main__':
#     from tkinter import *
#     # root = Tk()
#     # root.title('Canvas')
#     # canvas = Canvas(root,width = 400,height = 400,bg = 'yellow')
#     canvas = Canvas(width = 400,height = 400,bg = 'yellow')

#     x0 = 263
#     y0 = 263
#     y1 = 275
#     x1 = 275
#     for i in range(19):
#         canvas.create_rectangle(x0,y0,x1,y1)
#         x0 -= 5
#         y0 -= 5
#         x1 += 5
#         y1 += 5
        
#     canvas.pack()
#     # root.mainloop()
#     mainloop()

