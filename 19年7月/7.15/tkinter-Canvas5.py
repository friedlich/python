#  Canvas操作图形项的标签
# 在 Canvas 中通过 create_xxx 方法绘制图形项之后，这些图形项井不是完全静态的图形，每个图形项都是一个独立的对象，程序完全可以动态地修改、删除这些图形项。

# Canvas 以“堆叠”的形式来管理这些图形项，先绘制的图形项位于“堆叠”的下面，后绘制的图形项位于“堆叠”的上面。因此，如果两个图形项有重叠的部分，那么后绘制的图形项（位于上面）会遮挡先绘制的图形项。

# 为了修改、删除这些图形项，程序需要先获得这些图形项的引用。获得这些图形项的引用有两种方式：

#     通过图形项的 id，也就是 Canvas 执行 create_xxx() 方法的返回值。一般来说，create_xxx() 会依次返回 1、2、3 等整数作为图形项的 id。
#     通过图形项的 tag（标签）。


# 在 Canvas 中调用 create_xxx() 方法绘图时，还可传入一个 tags 选项，该选项可以为所绘制的图形项（比如矩形、椭圆、多边形等）添加一个或多个 tag（标签）。此外，Canvas 还允许调用方法为图形项添加 tag、删除 tag 等，这些 tag 也相当于该图形项的标识，程序完全可以根据 tag 来获取图形项。

# 总结来说，Canvas 提供了如下方法来为图形项添加 tag：

#     addtag_aboove(self, newtag, tagOrId)：为 tagOrId 对应图形项的上一个图形项添加新 tag。
#     addtag_all(self, newtag)：为所有图形项添加新 tag。
#     addtag_below(self, newtag, tagOrId)：为 tagOrId 对应图形项的下一个图形项添加新 tag。
#     addtag_closest(self, newtag, x, y)：为和 x、y 点最接近的图形项添加新 tag。
#     addtag_enclosed(self, newtag, x1, y1, x2, y2)：为指定矩形区域内最上面的图形项添加新tag。其中 x1、y1 确定矩形区域的左上角坐标；x2、y2 确定矩形区域的右下角坐标。
#     addtag_overlapping(self, newtag, x1, y1, x2, y2)：为与指定矩形区域重叠的最上面的图形项添加tag。
#     addtag_withtag(self, newtag, tagOrId)：为 tagOrId 对应图形项添加新 tag。


# Canvas 提供了如下方法来删除图形项的tag：

#     dtag(self, *args)：删除指定图形项的tag。


# Canvas 提供了如下方法来获取图形项的所有tag：

#     gettags(self, *args)：获取指定图形项的所有tag。


# Canvas 提供了如下方法根据 tag 来获取其对应的所有图形项：

#     find_withtag(self, tagOrId)：获取tagOrId 对应的所有图形项。

from tkinter import *
# 创建窗口
root = Tk()
root.title('操作标签')
# 创建并添加Canvas
cv = Canvas(root, background='white', width=620, height=250)
cv.pack(fill=BOTH, expand=YES)
# 绘制一个矩形框
rt = cv.create_rectangle(40, 40, 300, 220,
    outline='blue', width=2,
    tag = ('t1', 't2', 't3', 'tag4'))  # 为该图形项指定标签
# 访问图形项的id，也就是编号
print(rt) # 1
# 绘制一个椭圆
oval = cv.create_oval(350, 50, 580, 200,
    fill='yellow', width=0,
    tag = ('g1', 'g2', 'g3', 'tag4'))  # 为该图形项指定标签
# 访问图形项的id，也就是编号
print(oval) # 2
# 根据指定tag该tag对应的所有图形项
print(cv.find_withtag('tag4')) # (1, 2)
# 获取指定图形项的所有tag
print(cv.gettags(rt))  # ('t1', 't2', 't3', 'tag4')
print(cv.gettags(2))  # ('g1', 'g2', 'g3', 'tag4')
cv.dtag(1, 't1') # 删除id为1的图形项上名为t1的tag
cv.dtag(oval, 'g1') # 删除id为oval的图形项上名为g1的tag
# 获取指定图形项的所有tag
print(cv.gettags(rt))  # ('tag4', 't2', 't3')
print(cv.gettags(2))  # ('tag4', 'g2', 'g3')
# 为所有图形项添加tag
cv.addtag_all('t5')
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5')
# 为指定图形项添加tag
cv.addtag_withtag('t6', 'g2')
# 获取指定图形项的所有tag
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5', 't6')
# 为指定图形项上面的图形项添加tag, t2上面的就是oval图形项
cv.addtag_above('t7', 't2')
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5', 't6', 't7')
# 为指定图形项下面的图形项添加tag, g2下面的就是rt图形项
cv.addtag_below('t8', 'g2')
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5', 't8')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5', 't6', 't7')
# 为最接近指定点的图形项添加tag，最接近360、90的图形项是oval
cv.addtag_closest('t9', 360, 90)
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5', 't8')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5', 't6', 't7', 't9')
# 为位于指定区域内（几乎覆盖整个图形区）的最上面的图形项添加tag
cv.addtag_closest('t10', 30, 30, 600, 240)
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5', 't8')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5', 't6', 't7', 't9', 't10')
# 为与指定区域内重合的最上面的图形项添加tag
cv.addtag_closest('t11', 250, 30, 400, 240)
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5', 't8')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5', 't6', 't7', 't9', 't10', 't11')
root.mainloop()

# 上面程序示范了操作图形项的 tag 的方法，而且列出了每次操作之后的输出结果。因此，读者可以结合程序的运行结果来理解 
# Canvas 是如何管理图形项的 tag 的。
