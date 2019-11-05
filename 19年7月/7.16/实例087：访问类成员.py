# 题目 回答结果（结构体变量传递）。
# 程序分析 无。
if __name__ == '__main__':
    class student():
        x = 0
        c = 0
    def f(stu):
        stu.x = 20
        stu.c = 'c'
    a = student()
    print(a.x,a.c)
    a.x = 3
    a.c = 'a'
    print(a.x,a.c)
    f(a)
    print(a.x,a.c)
