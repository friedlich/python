# 掌握了上面的绘制方法之后，实际上已经可以实现一些简单的游戏了。比如前面介绍的控制台五子棋，之前程序是在控制台打印游戏状态的，
# 实际上程序完全可以在界面上绘制游戏状态，这样就能看到图形界面的五子棋了。
# 此外，该五子棋还需要根据用户的鼠标动作来确定下棋坐标，因此程序会为游戏界面的 <Button-1>（左键单击）、<Motion>（鼠标移动）、
# <Leave>（鼠标移出）事件绑定事件处理函数。下面程序示范了实现图形界面的五子棋： 
from tkinter import *
import random
BOARD_WIDTH = 535
BOARD_HEIGHT = 536
BOARD_SIZE = 15
# 定义棋盘坐标的像素值和棋盘数组之间的偏移距。
X_OFFSET = 21
Y_OFFSET = 23
# 定义棋盘坐标的像素值和棋盘数组之间的比率。
X_RATE = (BOARD_WIDTH - X_OFFSET * 2) / (BOARD_SIZE - 1)
Y_RATE = (BOARD_HEIGHT - Y_OFFSET * 2) / (BOARD_SIZE - 1)
BLACK_CHESS = "●"
WHITE_CHESS = "○"
board = []
# 把每个元素赋为"╋"，代表无棋
for i in range(BOARD_SIZE) :
    row = ["╋"] * BOARD_SIZE
    board.append(row)
# 创建窗口
root = Tk()
# 禁止改变窗口大小
root.resizable(width=False, height=False)
# 修改图标
root.iconbitmap('images/fklogo.ico')
# 设置窗口标题
root.title('五子棋')
# 创建并添加Canvas
cv = Canvas(root, background='white',
    width=BOARD_WIDTH, height=BOARD_HEIGHT)
cv.pack()
bm = PhotoImage(file="images/board.png")
cv.create_image(BOARD_HEIGHT/2 + 1, BOARD_HEIGHT/2 + 1, image=bm)
selectedbm = PhotoImage(file="images/selected.gif")
# 创建选中框图片，但该图片默认不在棋盘中
selected = cv.create_image(-100, -100, image=selectedbm)
def move_handler(event):
    # 计算用户当前的选中点，并保证该选中点在0～14之间
    selectedX = max(0, min(round((event.x - X_OFFSET) / X_RATE), 14))
    selectedY = max(0, min(round((event.y - Y_OFFSET) / Y_RATE), 14))
    # 移动红色选择框
    cv.coords(selected,(selectedX * X_RATE + X_OFFSET,
        selectedY * Y_RATE + Y_OFFSET))
black = PhotoImage(file="images/black.gif")
white = PhotoImage(file="images/white.gif")
def click_handler(event):
    # 计算用户的下棋点，并保证该下棋点在0～14之间
    userX = max(0, min(round((event.x - X_OFFSET) / X_RATE), 14))
    userY = max(0, min(round((event.y - Y_OFFSET) / Y_RATE), 14))
    # 当下棋点没有棋子时，才能下棋子，用户才能下棋子
    if board[userY][userX] == "╋":
        cv.create_image(userX * X_RATE + X_OFFSET, userY * Y_RATE + Y_OFFSET,
            image=black)
        board[userY][userX] = "●"
        while(True):
            comX = random.randint(0, BOARD_SIZE - 1)
            comY = random.randint(0, BOARD_SIZE - 1)
            # 如果电脑要下棋的点没有棋子时，才能让电脑下棋
            if board[comY][comX] == "╋": break
        cv.create_image(comX * X_RATE + X_OFFSET, comY * Y_RATE + Y_OFFSET,
            image=white)
        board[comY][comX] = "○"
def leave_handler(event):
    # 将红色选中框移出界面
    cv.coords(selected, -100, -100)
# 为鼠标移动事件绑定事件处理函数
cv.bind('<Motion>', move_handler)
# 为鼠标点击事件绑定事件处理函数
cv.bind('<Button-1>', click_handler)
# 为鼠标移出事件绑定事件处理函数
cv.bind('<Leave>', leave_handler)
root.mainloop()

# 上面程序先绘制了五子棋的棋盘，该棋盘就是一张预先准备好的图片，然后绘制选择框，当用户鼠标在棋盘上移动时，该选择框显示用户鼠标
# 当前停留在哪个下棋点上。
# 随后程序调用了 Canvas 的 coords() 方法，该方法负责重设选择框的坐标。这是 Tkinter 绘图的特别之处，绘制好的每一个图形项都不是
# 固定的，程序后面完全可以修改它们。因此，程序将会控制选择框图片随着用户鼠标的移动而改变位置。
# 程序根据用户鼠标单击来绘制黑色棋子（也就是下黑棋）和白色棋子（也就是下白棋）。在绘制黑色棋子和白色棋子的同时，也改变了底层代表
# 棋盘状态的 board 列表的数据，这样即可记录下棋状态，从而让程序在后面可以根据 board[] 列表来判断胜负（本来这个功能在 Charlie 
# 的程序中是有的，此处为了突出绘图的主题，作者删除了这部分）。另外，也可以加入人工智能，根据 board[] 列表来决定电脑的下棋点。
# 运行该程序，可以看到如图 4 所示的效果： 

# 在上面这个程序中，电脑下棋采用的方式是随机下棋，因此下得比较“凌乱”。如果要让电脑下棋更加智能，则可通过简单的人工智能来实现，
# 本教程暂不涉及。