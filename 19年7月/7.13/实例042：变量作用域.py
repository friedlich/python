# 题目 学习使用auto定义变量的用法。
# 程序分析 python中的变量作用域。
i=0
n=0
def dummy():
    i=2 #这个东西必须存在，不然就报错，似乎是用不了外界的，而且这个赋值对外界没有作用
    i+=1 #就是要运算的话必须要有赋值表达式
    print(i) # r如果函数里没有i的运算表达式又是不会报错的，可以直接print出来i,局部可以用全局变量
    i+=1 #没有global声明，i只是局部变量，这个运算对外界不起作用，好像这个运算没有任何作用
def dummy2():
    global n
    print(n)
    n+=1 #global声明后，n作为全局变量，会影响外界
print('函数内部的同名变量')
for j in range(3):
    print(i)
    dummy()
    i+=1
print('global声明同名变量')
for k in range(3):
    print(n)
    dummy2()
    n+=10

