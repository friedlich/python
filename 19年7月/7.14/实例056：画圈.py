# 题目 画图，学用circle画圆形。
# 程序分析 无。
import tkinter
canvas = tkinter.Canvas(width=800,height=600,bg='yellow')
canvas.pack(expand=tkinter.YES,fill=tkinter.BOTH)
k=26
j=26
for i in range(2):
    canvas.create_oval(310-k,250-k,
    310+k,250+k,
    width=1)
    k+=j
    j+=0.3
canvas.mainloop()

